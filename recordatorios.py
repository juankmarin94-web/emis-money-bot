"""
Recordatorios proactivos.

Hasta aca el bot solo respondia. El problema es que la adherencia no falla por
falta de plan, falla porque nadie te pregunta. Este modulo corre un hilo que
revisa cada 10 minutos si toca mandar algo.

Zona horaria: Adelaide. Render corre en UTC, asi que el hilo convierte antes de
comparar la hora, y por eso 'tzdata' esta en requirements: sin ese paquete
zoneinfo no encuentra la base de datos de zonas en la imagen de Render.

Anti-duplicados: cada recordatorio guarda en Firestore la fecha en que se mando
por ultima vez. Si el worker se reinicia tres veces en una manana, el
recordatorio de pesarse sale una sola vez.
"""

import threading, time, traceback
from datetime import datetime, timedelta

try:
    from zoneinfo import ZoneInfo
    TZ = ZoneInfo('Australia/Adelaide')
except Exception:                      # sin tzdata: cae a UTC en vez de morir
    TZ = None

INTERVALO_S = 600      # 10 min


def ahora():
    return datetime.now(TZ) if TZ else datetime.now()


# Cada recordatorio: (clave, dias_validos, hora, minuto_desde, funcion)
# dias_validos: set de weekday() o None para todos los dias.
def _construir(bot, db, nutricion, gym):
    st = nutricion.Store(db)

    def chats():
        """chat_id -> persona, desde el user_map que ya usa el bot de gastos."""
        snap = db.collection('emis_money').document('shared').get()
        um = (snap.to_dict() or {}).get('user_map', {}) if snap.exists else {}
        # Solo Camilo tiene perfil de nutricion; Juli usa el bot solo para gastos.
        return {cid: p for cid, p in um.items() if p == 'camilo'}

    def ya_se_mando(persona, clave, hoy):
        ref = db.collection('nutricion').document(persona)
        snap = ref.get()
        d = ((snap.to_dict() or {}).get('recordatorios') or {}) if snap.exists else {}
        return d.get(clave) == hoy

    def marcar(persona, clave, hoy):
        db.collection('nutricion').document(persona).set(
            {'recordatorios': {clave: hoy}}, merge=True)

    # ── Los recordatorios ─────────────────────────────────────────────────────
    def pesarse(persona, t):
        fecha = t.strftime('%Y-%m-%d')
        if st.dia(persona, fecha).get('peso_kg'):
            return None                      # ya se peso hoy
        dias = st.ultimos_dias(persona, 21)
        media, ritmo, _ = nutricion.media_movil_peso(dias)
        txt = ["⚖️ *Buenos dias.* Pesate antes de desayunar y manda `/peso <numero>`."]
        if media:
            txt.append(f"\nTu media de 7 dias va en *{media:.1f} kg*"
                       + (f", *{ritmo:+.2f} kg* vs la semana pasada." if ritmo is not None else "."))
        txt.append("\n_En ayunas, despues del bano, sin ropa. Misma hora siempre: "
                   "asi el dato compara con el de ayer y no con otra cosa._")
        return '\n'.join(txt)

    def registrar_cena(persona, t):
        fecha = t.strftime('%Y-%m-%d')
        d = st.dia(persona, fecha)
        tot = nutricion.sumar(d['comidas'])
        p = st.perfil(persona)
        tg = nutricion.targets_de_hoy(p, nutricion.es_dia_entreno(p, fecha))
        if not d['comidas']:
            return ("🍽 *No registraste nada hoy.*\n\n"
                    "Un dia sin registrar no es un dia libre, es un dia ciego. "
                    "Aunque te hayas pasado, metelo: `comi ...`\n\n"
                    "_Registrar es la mitad del trabajo._")
        falta_p = tg['p'] - tot['p']
        falta_k = tg['kcal'] - tot['kcal']
        if falta_p < 12 and abs(falta_k) < 180:
            return None                      # el dia cerro bien, no molestar
        txt = [f"🍽 *Cierre del dia*",
               f"Vas en *{tot['kcal']:.0f}/{tg['kcal']} kcal* y "
               f"*{tot['p']:.0f}/{tg['p']} g* de proteina.",
               nutricion.barra(tot['kcal'], tg['kcal'])]
        if falta_p >= 12:
            txt.append(f"\nTe faltan *{falta_p:.0f} g de proteina*. Lo mas rapido "
                       "que tienes: 150 g de cottage con Tajin (165 kcal, 20 P) "
                       "o un pouch de YoPRO (104 kcal, 15 P).")
        elif falta_k > 180:
            txt.append(f"\nTe sobran *{falta_k:.0f} kcal*. Comer por debajo del "
                       "target no acelera nada: te quita recuperacion y fuerza. "
                       "Manda `/receta` y cierra el dia.")
        return '\n'.join(txt)

    def entreno_del_dia(persona, t):
        clave = gym.sesion_de_hoy(t)
        if clave in ('descanso', 'cardio'):
            return None
        s = gym.W[clave]
        primeros = ', '.join(e['nombre'] for e in s['ejercicios'][:2])
        return (f"🏋️ *Hoy toca {s['nombre']}*\n\n"
                f"{len(s['ejercicios'])} ejercicios · "
                f"{sum(e['series'] for e in s['ejercicios'])} series · "
                f"{s['duracion_min']} min\n"
                f"Arranca con: {primeros}\n\n"
                "`/gym` para la sesion completa · `/set <ejercicio> <kg> <reps>` para registrar\n\n"
                "_Pines de seguridad puestos antes de la primera serie._")

    def domingo_prep(persona, t):
        m = nutricion.lista_mercado(st.perfil(persona), 7)
        n_items = sum(len(v) for v in m['secciones'].values())
        return ("🍳 *Domingo de preparacion*\n\n"
                "Las tres cosas que hacen que la semana no se caiga:\n"
                "1. *6 huevos duros* — 9 min de hervor, agua con hielo despues.\n"
                "2. *Una olla de curry de garbanzos* (`/receta d2`) — rinde 3 dias.\n"
                "3. *Dos frascos de overnight oats* (`/receta b3`) — lunes y martes resueltos.\n\n"
                f"Tu lista de mercado tiene *{n_items} items*: `/mercado`\n\n"
                "_Mañana es Upper A. La semana se gana hoy, no el lunes._")

    def semanal(persona, t):
        p = st.perfil(persona)
        t = nutricion.calcular_targets(p)
        dias = st.ultimos_dias(persona, 7)
        con = [d for d in dias if d.get('comidas')]
        media, ritmo, _ = nutricion.media_movil_peso(st.ultimos_dias(persona, 21))
        txt = ["📅 *Resumen de la semana*", ""]
        txt.append(f"Dias registrados: *{len(con)}/7*")
        if con:
            prom = nutricion.sumar([nutricion.sumar(d['comidas']) for d in con])
            n = len(con)
            txt.append(f"Promedio: *{prom['kcal']/n:.0f} kcal* (meta {t['kcal_promedio']})")
            txt.append(f"Proteina: *{prom['p']/n:.0f} g* (meta {t['proteina']})")
            txt.append(f"Fibra: *{prom['fib']/n:.0f} g* (meta {t['fibra']})")
        if media:
            txt.append(f"\nPeso, media de 7 dias: *{media:.1f} kg*")
            if ritmo is not None:
                txt.append(f"Cambio: *{ritmo:+.2f} kg*")
                if -1.2 <= ritmo <= -0.3:
                    txt.append("_Ese es exactamente el ritmo. Sigue igual._")
                elif ritmo > -0.3:
                    txt.append("_Se frenó. Revisa si estas pesando la mantequilla "
                               "de mani, el aceite y las nueces antes de tocar nada._")
                else:
                    txt.append("_Muy rapido. Sube 150 kcal de carbos: por debajo de "
                               "esto empiezas a pagar con musculo._")
            faltan = p['peso_kg'] - p['peso_meta_kg']
            if t['perdida_semanal_kg'] > 0:
                txt.append(f"\nFaltan *{faltan:.1f} kg* → "
                           f"~{faltan/t['perdida_semanal_kg']:.0f} semanas al ritmo del plan.")
        txt.append("\n_`/mercado` para la lista de la semana que entra._")
        return '\n'.join(txt)

    #  clave              dias           hh:mm   funcion
    return chats, ya_se_mando, marcar, [
        ('pesarse',       None,          (7, 0),   pesarse),
        ('entreno',       {0, 1, 3, 4},  (8, 0),   entreno_del_dia),
        ('cierre',        None,          (20, 30), registrar_cena),
        ('domingo_prep',  {6},           (10, 0),  domingo_prep),
        ('semanal',       {6},           (18, 0),  semanal),
    ]


def iniciar(bot, db, nutricion, gym):
    chats, ya_se_mando, marcar, reglas = _construir(bot, db, nutricion, gym)

    def ciclo():
        while True:
            try:
                t = ahora()
                hoy = t.strftime('%Y-%m-%d')
                for cid, persona in chats().items():
                    for clave, dias, (hh, mm), fn in reglas:
                        if dias is not None and t.weekday() not in dias:
                            continue
                        # La ventana es de 60 min: si el worker estaba dormido o
                        # reiniciando a la hora exacta, el recordatorio no se pierde.
                        objetivo = t.replace(hour=hh, minute=mm, second=0, microsecond=0)
                        if not (objetivo <= t < objetivo + timedelta(minutes=60)):
                            continue
                        if ya_se_mando(persona, clave, hoy):
                            continue
                        texto = fn(persona, t)
                        marcar(persona, clave, hoy)   # marca aunque no aplique hoy
                        if texto:
                            bot.send_message(int(cid), texto)
            except Exception:
                traceback.print_exc()
            time.sleep(INTERVALO_S)

    hilo = threading.Thread(target=ciclo, daemon=True, name='recordatorios')
    hilo.start()
    tz = 'Australia/Adelaide' if TZ else 'UTC (sin tzdata!)'
    print(f"⏰ Recordatorios activos ({tz}): "
          + ', '.join(f"{c} {h:02d}:{m:02d}" for c, _, (h, m), _ in reglas))
    return hilo

"""Entreno: muestra la sesion del dia y registra series y records."""

import os, json, re
from datetime import datetime

DATA = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data')
with open(os.path.join(DATA, 'workouts.json'), encoding='utf-8') as fh:
    W = json.load(fh)

SESIONES = ['upper_a', 'lower_a', 'upper_b', 'lower_b']
# 0=lunes … 6=domingo
POR_DIA = {0: 'upper_a', 1: 'lower_a', 2: 'cardio', 3: 'upper_b', 4: 'lower_b',
           5: 'cardio', 6: 'descanso'}


def sesion_de_hoy(fecha=None):
    dt = fecha or datetime.now()
    return POR_DIA[dt.weekday()]


def fmt_sesion(clave):
    s = W[clave]
    out = [f"🏋 *{s['nombre']}*", f"_{s['duracion_min']} min_", "",
           f"*Calentamiento*\n{s['calentamiento']}", "", "*Sesion*"]
    for i, e in enumerate(s['ejercicios'], 1):
        out.append(f"\n*{i}. {e['nombre']}*")
        out.append(f"   {e['series']} × {e['reps']} · RIR {e['rir']} · "
                   f"descanso {e['descanso_s']}s")
        if e.get('nota'):
            out.append(f"   _{e['nota']}_")
        out.append(f"   ↳ si no puedes: {', '.join(e['alternativas'])}")
    total = sum(e['series'] for e in s['ejercicios'])
    out += ["", f"*{len(s['ejercicios'])} ejercicios · {total} series*",
            "", "_Registra con_ `/set sentadilla 80 5,5,5`"]
    return '\n'.join(out)


def register(bot, db, require_person):
    def dia_ref(persona, fecha=None):
        f = fecha or datetime.now().strftime('%Y-%m-%d')
        return db.collection('nutricion').document(persona).collection('dias').document(f)

    def prs_ref(persona):
        return db.collection('nutricion').document(persona)

    @bot.message_handler(commands=['gym', 'entreno'])
    def cmd_gym(msg):
        persona = require_person(msg)
        if not persona:
            return
        args = msg.text.split()[1:]
        clave = args[0].lower() if args else sesion_de_hoy()

        if clave == 'descanso':
            bot.send_message(msg.chat.id,
                "😴 *Domingo: descanso total*\n\n"
                "No es opcional ni es pereza. En deficit calorico recuperas peor, "
                "y el musculo se construye descansando, no entrenando.\n\n"
                "_Ver otra sesion:_ `/gym upper_a`")
            return
        if clave == 'cardio':
            c = W['cardio']
            hoy = 'Miercoles' if datetime.now().weekday() == 2 else 'Sabado'
            ses = [s for s in c['sesiones'] if hoy.lower() in s['cuando'].lower()]
            out = ["🚶 *Dia de descanso activo*", "", f"_{c['principio']}_", ""]
            for s in (ses or c['sesiones'][:1]):
                out.append(f"*{s['tipo']}* — {s['duracion_min']} min")
                out.append(f"   {s['intensidad']}")
                if s.get('nota'):
                    out.append(f"   _{s['nota']}_")
            out += ["", f"🎯 Meta de pasos: *{c['pasos_objetivo']:,}*",
                    "", f"⚠️ {c['no_hacer']}",
                    "", "_Ver una sesion de pesas:_ `/gym lower_a`"]
            bot.send_message(msg.chat.id, '\n'.join(out))
            return
        if clave not in W:
            bot.send_message(msg.chat.id,
                "Sesiones: " + ', '.join(f"`{s}`" for s in SESIONES))
            return
        bot.send_message(msg.chat.id, fmt_sesion(clave))

    @bot.message_handler(commands=['set'])
    def cmd_set(msg):
        """/set sentadilla 80 5,5,5  -> registra el ejercicio y revisa el PR."""
        persona = require_person(msg)
        if not persona:
            return
        m = re.match(r'^/set\s+(.+?)\s+(\d+(?:\.\d+)?)\s+([\d,\s]+)$',
                     msg.text.strip(), re.I)
        if not m:
            bot.send_message(msg.chat.id,
                "Formato: `/set <ejercicio> <kg> <reps separadas por coma>`\n"
                "Ejemplo: `/set sentadilla 80 5,5,4`")
            return
        ejercicio = m.group(1).strip().lower()
        kg = float(m.group(2))
        reps = [int(r) for r in re.findall(r'\d+', m.group(3))]

        snap = dia_ref(persona).get()
        d = snap.to_dict() if snap.exists else {}
        entreno = d.get('entreno', {'sesion': sesion_de_hoy(), 'sets': []})
        entreno.setdefault('sets', []).append(
            {'ejercicio': ejercicio, 'kg': kg, 'reps': reps,
             'hora': datetime.now().strftime('%H:%M')})
        dia_ref(persona).set({'entreno': entreno}, merge=True)

        # Records: el mejor tonelaje (kg × reps) de una sola serie.
        psnap = prs_ref(persona).get()
        prs = ((psnap.to_dict() or {}).get('prs', {})) if psnap.exists else {}
        mejor_ahora = kg * max(reps)
        previo = prs.get(ejercicio, {})
        es_pr = mejor_ahora > previo.get('tonelaje', 0)
        if es_pr:
            prs[ejercicio] = {'kg': kg, 'reps': max(reps),
                              'tonelaje': mejor_ahora,
                              'fecha': datetime.now().strftime('%Y-%m-%d')}
            prs_ref(persona).set({'prs': prs}, merge=True)

        txt = [f"✅ *{ejercicio.title()}* — {kg:g} kg × {'/'.join(map(str, reps))}",
               f"Volumen: *{kg * sum(reps):.0f} kg* movidos",
               f"Series de hoy: {len(entreno['sets'])}"]
        if es_pr:
            if previo:
                txt.append(f"\n🏆 *RECORD* — antes {previo['kg']:g} kg × {previo['reps']}")
            else:
                txt.append("\n🏆 *Primer registro de este ejercicio.*")
        elif previo:
            txt.append(f"\nTu record: {previo['kg']:g} kg × {previo['reps']} "
                       f"({previo['fecha']})")
        bot.send_message(msg.chat.id, '\n'.join(txt))

    @bot.message_handler(commands=['prs', 'records'])
    def cmd_prs(msg):
        persona = require_person(msg)
        if not persona:
            return
        snap = prs_ref(persona).get()
        prs = ((snap.to_dict() or {}).get('prs', {})) if snap.exists else {}
        if not prs:
            bot.send_message(msg.chat.id,
                "Sin records todavia. Registra con `/set sentadilla 80 5,5,5`")
            return
        filas = sorted(prs.items(), key=lambda kv: -kv[1]['tonelaje'])
        txt = ["🏆 *Tus records*", ""]
        for nombre, r in filas:
            txt.append(f"*{nombre.title()}* — {r['kg']:g} kg × {r['reps']}  _{r['fecha']}_")
        txt += ["", "_En deficit, MANTENER estos numeros ya es ganar. "
                    "Si bajas de peso y la barra no baja, no estas perdiendo musculo._"]
        bot.send_message(msg.chat.id, '\n'.join(txt))

    @bot.message_handler(commands=['progresion'])
    def cmd_progresion(msg):
        pr = W['progresion']
        reglas = '\n'.join(f"  {i+1}. {r}" for i, r in enumerate(pr['regla']))
        bot.send_message(msg.chat.id,
            f"📈 *{pr['metodo']}*\n\n{reglas}\n\n"
            f"*Tu limitacion del garage*\n_{pr['limitacion_del_garage']}_\n\n"
            f"*Deload*\n_{pr['deload']}_")

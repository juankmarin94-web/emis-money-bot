"""
Integracion con WHOOP.

Dos detalles que definen este diseno:

1. WHOOP ROTA el refresh token. Cada vez que se canjea uno, la respuesta trae
   un refresh token nuevo y el anterior queda invalido al instante. Por eso el
   token NO puede vivir en una variable de entorno: se guarda en Firestore y se
   reescribe en cada refresh.

2. Este bot corre como worker sin servidor web, asi que no puede recibir el
   redirect de OAuth. El flujo es: autorizas una vez a mano en el navegador,
   pegas el refresh token con /whoop token <valor>, y de ahi en adelante el bot
   se renueva solo.

Las rutas del API estan todas juntas abajo a proposito: la documentacion de
developer.whoop.com no era alcanzable desde el entorno donde se escribio esto,
asi que si WHOOP mueve algo, se corrige en un solo lugar.
"""

import os, json, requests
from datetime import datetime, timedelta

BASE = 'https://api.prod.whoop.com'
OAUTH_AUTORIZAR = f'{BASE}/oauth/oauth2/auth'
OAUTH_TOKEN = f'{BASE}/oauth/oauth2/token'
API = f'{BASE}/developer'
EP_RECOVERY = f'{API}/v2/recovery'
EP_CICLO = f'{API}/v2/cycle'
EP_SUENO = f'{API}/v2/activity/sleep'
EP_ENTRENO = f'{API}/v2/activity/workout'
SCOPES = ('read:recovery read:cycles read:sleep read:workout '
          'read:body_measurement read:profile offline')

CLIENT_ID = os.environ.get('WHOOP_CLIENT_ID', '')
CLIENT_SECRET = os.environ.get('WHOOP_CLIENT_SECRET', '')


class Whoop:
    def __init__(self, db, persona):
        self.ref = db.collection('nutricion').document(persona)
        self.persona = persona

    # ── Tokens ────────────────────────────────────────────────────────────────
    def _cred(self):
        snap = self.ref.get()
        return ((snap.to_dict() or {}).get('whoop_auth') or {}) if snap.exists else {}

    def guardar_refresh(self, refresh_token):
        self.ref.set({'whoop_auth': {'refresh_token': refresh_token}}, merge=True)

    def conectado(self):
        return bool(self._cred().get('refresh_token'))

    def _access_token(self):
        """Canjea el refresh token y guarda el NUEVO que devuelve WHOOP.

        Si no se guarda el nuevo, el siguiente refresh falla: el anterior ya
        quedo invalidado del lado de WHOOP.
        """
        cred = self._cred()
        rt = cred.get('refresh_token')
        if not rt:
            raise RuntimeError('sin_token')

        vence = cred.get('expira_en')
        if cred.get('access_token') and vence and datetime.now().timestamp() < vence - 60:
            return cred['access_token']

        resp = requests.post(OAUTH_TOKEN, timeout=20, data={
            'grant_type': 'refresh_token',
            'refresh_token': rt,
            'client_id': CLIENT_ID,
            'client_secret': CLIENT_SECRET,
            'scope': 'offline',
        })
        if resp.status_code != 200:
            raise RuntimeError(f'refresh_fallo:{resp.status_code}:{resp.text[:200]}')
        tok = resp.json()
        nuevo = {
            'refresh_token': tok.get('refresh_token', rt),   # rotado
            'access_token': tok['access_token'],
            'expira_en': datetime.now().timestamp() + tok.get('expires_in', 3600),
        }
        self.ref.set({'whoop_auth': nuevo}, merge=True)
        return nuevo['access_token']

    def _get(self, url, params=None):
        r = requests.get(url, timeout=20, params=params or {'limit': 1},
                         headers={'Authorization': f'Bearer {self._access_token()}'})
        r.raise_for_status()
        return r.json()

    # ── Datos ─────────────────────────────────────────────────────────────────
    def hoy(self):
        """Recovery, sueno y strain mas recientes, aplanados."""
        out = {}
        try:
            rec = (self._get(EP_RECOVERY).get('records') or [{}])[0]
            s = rec.get('score') or {}
            out['recovery'] = s.get('recovery_score')
            out['hrv'] = s.get('hrv_rmssd_milli')
            out['rhr'] = s.get('resting_heart_rate')
        except Exception as e:
            out['error_recovery'] = str(e)[:120]
        try:
            cic = (self._get(EP_CICLO).get('records') or [{}])[0]
            out['strain'] = (cic.get('score') or {}).get('strain')
            out['kcal_quemadas'] = round(
                (cic.get('score') or {}).get('kilojoule', 0) / 4.184) or None
        except Exception as e:
            out['error_ciclo'] = str(e)[:120]
        try:
            slp = (self._get(EP_SUENO).get('records') or [{}])[0]
            st = ((slp.get('score') or {}).get('stage_summary') or {})
            ms = st.get('total_in_bed_time_milli')
            out['sueno_h'] = round(ms / 3600000, 1) if ms else None
            out['sueno_pct'] = (slp.get('score') or {}).get('sleep_performance_percentage')
        except Exception as e:
            out['error_sueno'] = str(e)[:120]
        return out


# ── Lectura de la data ────────────────────────────────────────────────────────
def interpretar(d, es_dia_entreno):
    """Convierte los numeros del WHOOP en una decision sobre hoy."""
    rec = d.get('recovery')
    sueno = d.get('sueno_h')
    consejos = []

    if rec is None:
        consejos.append("Sin recovery todavia. WHOOP solo lo calcula despues de "
                        "que termines de dormir.")
    elif rec < 34:
        consejos.append("🔴 *Recovery rojo.* Hoy no es dia de buscar records. "
                        + ("Haz la sesion pero baja 1 serie de cada compuesto y "
                           "quedate en RIR 3." if es_dia_entreno else
                           "Camina y ya, no agregues nada."))
    elif rec < 67:
        consejos.append("🟡 *Recovery amarillo.* Entrena normal pero no fuerces "
                        "el fallo. Si el primer compuesto se siente pesado de mas, "
                        "quedate en el peso de la semana pasada.")
    else:
        consejos.append("🟢 *Recovery verde.* Este es el dia para intentar "
                        "sumar la repeticion o el disco.")

    if sueno is not None and sueno < 6.5:
        consejos.append(f"😴 Solo *{sueno} h* de sueno. Dormir poco sube el hambre "
                        "(mas grelina, menos leptina): hoy el hambre no es falta "
                        "de voluntad, es bioquimica. Sostente en la proteina y "
                        "las palomitas de volumen.")
    strain = d.get('strain')
    if strain is not None and strain > 15:
        consejos.append(f"🔥 Strain de *{strain:.1f}*, dia muy cargado. Si te "
                        "sientes vacio, suma 150 kcal de carbos (50 g de arroz o "
                        "una banana). Un dia asi no rompe el deficit semanal.")
    if rec is not None and rec < 34:
        consejos.append("Si manana vuelve a salir rojo, lo primero que sobra es el "
                        "cardio extra: nunca las pesas ni la proteina.")
    return consejos


def register(bot, db, require_person):
    @bot.message_handler(commands=['whoop'])
    def cmd_whoop(msg):
        persona = require_person(msg)
        if not persona:
            return
        partes = msg.text.split()
        w = Whoop(db, persona)

        # /whoop token <refresh_token>
        if len(partes) >= 3 and partes[1].lower() == 'token':
            w.guardar_refresh(partes[2].strip())
            bot.send_message(msg.chat.id,
                "✅ Refresh token guardado. Probando la conexion…")
            try:
                d = w.hoy()
                bot.send_message(msg.chat.id, _fmt(d, persona, db))
            except Exception as e:
                bot.send_message(msg.chat.id, f"⚠️ No conecto: `{str(e)[:200]}`")
            return

        # /whoop 65 7.5 12.3  -> entrada manual (recovery, sueno, strain)
        nums = [p for p in partes[1:] if p.replace('.', '', 1).isdigit()]
        if nums:
            d = {}
            for k, v in zip(['recovery', 'sueno_h', 'strain'], nums):
                d[k] = float(v)
            db.collection('nutricion').document(persona).collection('dias') \
              .document(datetime.now().strftime('%Y-%m-%d')).set({'whoop': d}, merge=True)
            bot.send_message(msg.chat.id, _fmt(d, persona, db, manual=True))
            return

        if not w.conectado():
            bot.send_message(msg.chat.id,
                "⌚ *WHOOP sin conectar*\n\n"
                "Este bot corre como worker sin servidor web, asi que no puede "
                "recibir el redirect de OAuth. Se hace una vez a mano:\n\n"
                "1. Crea una app en `developer.whoop.com`\n"
                "2. Pon `WHOOP_CLIENT_ID` y `WHOOP_CLIENT_SECRET` en Render\n"
                f"3. Autoriza en el navegador con scope:\n`{SCOPES}`\n"
                "4. Del resultado, pega aca:\n`/whoop token <refresh_token>`\n\n"
                "De ahi en adelante el bot renueva solo. Ojo: WHOOP *rota* el "
                "refresh token en cada renovacion, y por eso se guarda en "
                "Firestore y no en una variable de entorno.\n\n"
                "*Mientras tanto, a mano:*\n"
                "`/whoop 65 7.5 12.3` → recovery 65%, 7.5 h de sueno, strain 12.3")
            return
        try:
            d = w.hoy()
            db.collection('nutricion').document(persona).collection('dias') \
              .document(datetime.now().strftime('%Y-%m-%d')).set({'whoop': d}, merge=True)
            bot.send_message(msg.chat.id, _fmt(d, persona, db))
        except Exception as e:
            bot.send_message(msg.chat.id,
                f"⚠️ Error hablando con WHOOP: `{str(e)[:200]}`\n\n"
                "Si dice `refresh_fallo`, el token se vencio o ya se uso: "
                "vuelve a autorizar y manda `/whoop token <nuevo>`.")

    def _fmt(d, persona, db, manual=False):
        import nutricion
        p = nutricion.Store(db).perfil(persona)
        entreno = nutricion.es_dia_entreno(p)
        out = ["⌚ *WHOOP" + (" (manual)" if manual else "") + "*", ""]
        if d.get('recovery') is not None:
            out.append(f"Recovery: *{d['recovery']:.0f}%*")
        if d.get('sueno_h') is not None:
            pct = f" ({d['sueno_pct']:.0f}% de rendimiento)" if d.get('sueno_pct') else ""
            out.append(f"Sueno: *{d['sueno_h']} h*{pct}")
        if d.get('strain') is not None:
            out.append(f"Strain: *{d['strain']:.1f}*")
        if d.get('hrv'):
            out.append(f"HRV: {d['hrv']:.0f} ms · RHR: {d.get('rhr', '?')} bpm")
        if d.get('kcal_quemadas'):
            out.append(f"Gasto del dia segun WHOOP: ~{d['kcal_quemadas']} kcal")
            out.append("_Ojo: no sumes esto a tu TDEE. Tu target ya lo incluye; "
                       "usarlo para comer mas es el error clasico del wearable._")
        errores = [v for k, v in d.items() if k.startswith('error_')]
        if errores and not manual:
            out.append(f"\n⚠️ Partes sin leer: {len(errores)}")
        out += ["", "*Que hacer hoy*"]
        out += [f"• {c}" for c in interpretar(d, entreno)]
        return '\n'.join(out)

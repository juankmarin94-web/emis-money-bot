"""
Modulo de nutricion para el bot.

Vive al lado del tracker de gastos y comparte el mismo bot de Telegram, el mismo
cliente de Anthropic y la misma instancia de Firestore.

Estructura en Firestore:
    nutricion/{persona}                      -> perfil + targets calculados
    nutricion/{persona}/dias/{YYYY-MM-DD}    -> comidas del dia, peso, pasos, whoop
"""

import os, json, re, difflib, base64, requests
from datetime import datetime, timedelta

DATA = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data')

with open(os.path.join(DATA, 'foods.json'), encoding='utf-8') as fh:
    _RAW_FOODS = json.load(fh)
with open(os.path.join(DATA, 'recipes.json'), encoding='utf-8') as fh:
    RECETAS = json.load(fh)

# Aplana los alimentos: los de "_por_comprar" cuentan igual para calcular macros.
FOODS = {k: v for k, v in _RAW_FOODS.items() if not k.startswith('_')}
FOODS.update({k: v for k, v in _RAW_FOODS.get('_por_comprar', {}).items()
              if not k.startswith('_')})

# Indice alias -> id, para buscar por lo que la gente realmente escribe.
SECCIONES = {k: v for k, v in _RAW_FOODS.get('_secciones', {}).items()
              if not k.startswith('_')}

ALIAS = {}
for _fid, _f in FOODS.items():
    ALIAS[_fid.replace('_', ' ')] = _fid
    ALIAS[_f['nombre'].lower()] = _fid
    for _a in _f.get('aliases', []):
        ALIAS[_a.lower()] = _fid

PERFIL_DEFAULT = {
    'peso_kg': 96.0,
    'altura_cm': 179,
    'edad': 32,
    'sexo': 'h',
    'dias_entreno': 4,
    'ritmo': 'agresivo',          # agresivo | moderado | lento
    'peso_meta_kg': 80.0,
    'vegetariano': True,
}

RITMOS = {'agresivo': 0.28, 'moderado': 0.20, 'lento': 0.12}
FACTOR_ACTIVIDAD = {0: 1.30, 1: 1.30, 2: 1.38, 3: 1.38, 4: 1.45, 5: 1.45, 6: 1.53, 7: 1.53}


# ── Calculo de targets ────────────────────────────────────────────────────────
def calcular_targets(perfil):
    """Mifflin-St Jeor -> TDEE -> deficit -> macros con carbohidratos ciclados.

    La proteina y la grasa se mantienen fijas todos los dias; solo los
    carbohidratos suben en dia de entreno. Es lo mas facil de seguir y lo mejor
    para retener musculo en deficit.
    """
    p = {**PERFIL_DEFAULT, **(perfil or {})}
    kg, cm, edad = float(p['peso_kg']), float(p['altura_cm']), int(p['edad'])

    bmr = 10 * kg + 6.25 * cm - 5 * edad + (5 if p['sexo'] == 'h' else -161)
    tdee = bmr * FACTOR_ACTIVIDAD.get(int(p['dias_entreno']), 1.45)

    objetivo = tdee * (1 - RITMOS.get(p['ritmo'], 0.28))
    objetivo = max(objetivo, bmr * 0.95, 1400)   # piso de seguridad

    prot = round(1.9 * kg)                       # 1.9 g/kg retiene musculo en deficit
    gras = round(0.6 * kg)                       # 0.6 g/kg protege hormonas
    carb_prom = max(0, round((objetivo - prot * 4 - gras * 9) / 4))

    # 4 dias de entreno y 3 de descanso mantienen el promedio semanal:
    # 4*(+140) = 3*(-187)
    dias_e = int(p['dias_entreno'])
    dias_d = max(1, 7 - dias_e)
    bump = 140
    drop = bump * dias_e / dias_d

    return {
        'bmr': round(bmr),
        'tdee': round(tdee),
        'deficit_dia': round(tdee - objetivo),
        'kcal_promedio': round(objetivo),
        'proteina': prot,
        'grasa': gras,
        'fibra': 35,
        'entreno': {'kcal': round(objetivo + bump), 'p': prot, 'f': gras,
                    'c': max(0, round(carb_prom + bump / 4))},
        'descanso': {'kcal': round(objetivo - drop), 'p': prot, 'f': gras,
                     'c': max(0, round(carb_prom - drop / 4))},
        'perdida_semanal_kg': round((tdee - objetivo) * 7 / 7700, 2),
    }


def targets_de_hoy(perfil, es_dia_entreno):
    t = calcular_targets(perfil)
    d = t['entreno'] if es_dia_entreno else t['descanso']
    return {'kcal': d['kcal'], 'p': d['p'], 'c': d['c'], 'f': d['f'],
            'fib': t['fibra'], '_full': t}


# ── Macros ────────────────────────────────────────────────────────────────────
def macros_de(food_id, gramos):
    f = FOODS.get(food_id)
    if not f:
        return None
    k = gramos / 100.0
    return {'kcal': f['kcal'] * k, 'p': f['p'] * k, 'c': f['c'] * k,
            'f': f['f'] * k, 'fib': f.get('fib', 0) * k}


def sumar(lista):
    tot = {'kcal': 0.0, 'p': 0.0, 'c': 0.0, 'f': 0.0, 'fib': 0.0}
    for it in lista:
        for k in tot:
            tot[k] += float(it.get(k, 0) or 0)
    return tot


def macros_receta(receta):
    """Calcula los macros de una receta desde sus gramos. Nunca hardcodeados."""
    items = []
    for ing in receta['ingredientes']:
        m = macros_de(ing['food'], ing['g'])
        if m:
            items.append(m)
    return sumar(items)


def buscar_receta(rid):
    for grupo, lista in RECETAS.items():
        if grupo.startswith('_'):
            continue
        for r in lista:
            if r['id'] == rid:
                return grupo, r
    return None, None


# ── Parseo de texto ───────────────────────────────────────────────────────────
_ITEM_RE = re.compile(
    r'^\s*(?P<num>\d+(?:[.,]\d+)?)\s*(?P<unit>kg|g|gr|gramos|ml|und|unidades?|u)?\s*'
    r'(?:de\s+)?(?P<nombre>.+?)\s*$', re.I)


def _match_alimento(nombre):
    n = nombre.lower().strip().rstrip('.,;')
    if n in ALIAS:
        return ALIAS[n]
    # subcadena: "cottage cheese light" -> "cottage cheese"
    for alias in sorted(ALIAS, key=len, reverse=True):
        if len(alias) >= 4 and alias in n:
            return ALIAS[alias]
    cerca = difflib.get_close_matches(n, list(ALIAS), n=1, cutoff=0.82)
    return ALIAS[cerca[0]] if cerca else None


def parse_local(texto):
    """Intenta resolver la comida sin gastar una llamada al modelo.

    Devuelve (items_resueltos, trozos_no_resueltos).
    """
    texto = re.sub(r'^\s*(com[ií]|comi|ate|f|food|comida)\b[:,]?\s*', '', texto.strip(), flags=re.I)
    trozos = [t for t in re.split(r'\s*(?:,|\+|\band\b|\by\b|\ny)\s*', texto) if t.strip()]

    items, faltan = [], []
    for tz in trozos:
        m = _ITEM_RE.match(tz)
        if not m:
            faltan.append(tz)
            continue
        num = float(m.group('num').replace(',', '.'))
        unit = (m.group('unit') or '').lower()
        fid = _match_alimento(m.group('nombre'))
        if not fid:
            faltan.append(tz)
            continue

        f = FOODS[fid]
        if unit == 'kg':
            gramos = num * 1000
        elif unit in ('g', 'gr', 'gramos', 'ml'):
            gramos = num
        elif f.get('unit_g'):          # "3 huevos" -> 3 unidades
            gramos = num * f['unit_g']
        else:
            gramos = num               # "200 cottage" -> asume gramos

        mac = macros_de(fid, gramos)
        mac.update({'nombre': f['nombre'], 'g': round(gramos, 1), 'food': fid, 'fuente': 'db'})
        items.append(mac)
    return items, faltan


def parse_con_modelo(ac, texto):
    """Respaldo para lo que no esta en la base local (restaurantes, marcas nuevas)."""
    resp = ac.messages.create(
        model="claude-haiku-4-5-20251001",
        max_tokens=700,
        system=("Eres un nutricionista que estima macros de comida en espanol. "
                "Responde SOLO con JSON valido, sin markdown ni explicacion: "
                '{"items":[{"nombre":"","g":0,"kcal":0,"p":0,"c":0,"f":0,"fib":0}]} '
                "donde p/c/f/fib son gramos de proteina, carbohidratos, grasa y fibra "
                "de la porcion completa descrita (no por 100 g). Si no se da cantidad, "
                "asume una porcion normal de adulto y ponla en g."),
        messages=[{"role": "user", "content": f"Comida: {texto}"}],
    )
    data = _json_del_modelo(resp.content[0].text)
    for it in data.get('items', []):
        it['fuente'] = 'estimado'
    return data.get('items', [])


def _json_del_modelo(txt):
    txt = txt.strip()
    txt = re.sub(r'^```(?:json)?\s*|\s*```$', '', txt).strip()
    try:
        return json.loads(txt)
    except json.JSONDecodeError:
        m = re.search(r'\{.*\}', txt, re.S)
        if not m:
            raise
        return json.loads(m.group(0))


def analizar_foto(ac, img_bytes):
    """Una sola llamada de vision que clasifica Y extrae.

    Asi el bot sabe si la foto es un recibo del banco (gastos) o un plato de
    comida (nutricion) sin gastar dos llamadas.
    """
    b64 = base64.b64encode(img_bytes).decode()
    resp = ac.messages.create(
        model="claude-haiku-4-5-20251001",
        max_tokens=900,
        system=(
            "Clasificas fotos en dos tipos y respondes SOLO JSON valido sin markdown.\n"
            'Si es un recibo, factura o captura de transaccion bancaria:\n'
            '{"tipo":"recibo","description":"nombre del comercio","amount":0.00}\n'
            'Si es comida, un plato, o una etiqueta nutricional de un producto:\n'
            '{"tipo":"comida","platillo":"nombre corto en espanol",'
            '"items":[{"nombre":"","g":0,"kcal":0,"p":0,"c":0,"f":0,"fib":0}],'
            '"confianza":"alta|media|baja"}\n'
            "Para comida: estima el peso en gramos de cada componente visible y da "
            "los macros de esa porcion completa, NO por 100 g. Se realista con las "
            "porciones: la gente subestima el aceite y las salsas. "
            'Si no es ninguna de las dos cosas: {"tipo":"otro"}'
        ),
        messages=[{"role": "user", "content": [
            {"type": "image", "source": {"type": "base64",
                                         "media_type": "image/jpeg", "data": b64}},
            {"type": "text", "text": "Clasifica y extrae."},
        ]}],
    )
    return _json_del_modelo(resp.content[0].text)


# ── Firestore ─────────────────────────────────────────────────────────────────
class Store:
    def __init__(self, db):
        self.db = db

    def perfil_ref(self, persona):
        return self.db.collection('nutricion').document(persona)

    def dia_ref(self, persona, fecha):
        return self.perfil_ref(persona).collection('dias').document(fecha)

    def perfil(self, persona):
        snap = self.perfil_ref(persona).get()
        return {**PERFIL_DEFAULT, **(snap.to_dict() if snap.exists else {})}

    def guardar_perfil(self, persona, campos):
        self.perfil_ref(persona).set(campos, merge=True)

    def dia(self, persona, fecha=None):
        fecha = fecha or hoy()
        snap = self.dia_ref(persona, fecha).get()
        base = {'comidas': [], 'fecha': fecha}
        return {**base, **(snap.to_dict() if snap.exists else {})}

    def add_comida(self, persona, items, etiqueta, fecha=None):
        fecha = fecha or hoy()
        d = self.dia(persona, fecha)
        tot = sumar(items)
        entrada = {
            'id': f'{datetime.now().timestamp():.3f}',
            'hora': datetime.now().strftime('%H:%M'),
            'etiqueta': etiqueta,
            'items': items,
            **{k: round(v, 1) for k, v in tot.items()},
        }
        d['comidas'].append(entrada)
        self.dia_ref(persona, fecha).set(d, merge=True)
        return entrada, sumar(d['comidas'])

    def borrar_ultima(self, persona, fecha=None):
        fecha = fecha or hoy()
        d = self.dia(persona, fecha)
        if not d['comidas']:
            return None, None
        fuera = d['comidas'].pop()
        self.dia_ref(persona, fecha).set(d, merge=True)
        return fuera, sumar(d['comidas'])

    def set_dia(self, persona, campos, fecha=None):
        self.dia_ref(persona, fecha or hoy()).set(campos, merge=True)

    def ultimos_dias(self, persona, n=14):
        out = []
        for i in range(n):
            f = (datetime.now() - timedelta(days=i)).strftime('%Y-%m-%d')
            snap = self.dia_ref(persona, f).get()
            if snap.exists:
                d = snap.to_dict()
                d['fecha'] = f
                out.append(d)
        return out


def hoy():
    return datetime.now().strftime('%Y-%m-%d')


def es_dia_entreno(perfil, fecha=None):
    """Lunes, martes, jueves y viernes son de pesas en el split Upper/Lower x2."""
    dt = datetime.strptime(fecha, '%Y-%m-%d') if fecha else datetime.now()
    return dt.weekday() in (0, 1, 3, 4)


# ── Formato ───────────────────────────────────────────────────────────────────
def barra(actual, meta, ancho=10):
    if meta <= 0:
        return '─' * ancho
    frac = actual / meta
    llenos = min(ancho, int(round(frac * ancho)))
    b = '█' * llenos + '░' * (ancho - llenos)
    return b + (' ⚠️' if frac > 1.10 else '')


def linea(nombre, actual, meta, unidad=''):
    falta = meta - actual
    cola = f"faltan {falta:.0f}{unidad}" if falta > 0 else f"+{-falta:.0f}{unidad} sobre meta"
    return f"{nombre} {barra(actual, meta)} {actual:.0f}/{meta:.0f}{unidad}  ({cola})"


def fmt_items(items, limite=6):
    out = []
    for it in items[:limite]:
        g = f" {it['g']:.0f} g" if it.get('g') else ''
        marca = '' if it.get('fuente') == 'db' else ' ~'
        out.append(f"  • {it.get('nombre', '?')}{g}{marca} — {it['kcal']:.0f} kcal, "
                   f"{it['p']:.0f} P / {it['c']:.0f} C / {it['f']:.0f} G")
    if len(items) > limite:
        out.append(f"  • …y {len(items) - limite} mas")
    return '\n'.join(out)


def media_movil_peso(dias, ventana=7):
    """El peso diario es ruido. La media de 7 dias es la senal."""
    pesos = [(d['fecha'], float(d['peso_kg'])) for d in dias if d.get('peso_kg')]
    pesos.sort()
    if not pesos:
        return None, None, None
    reciente = [p for _, p in pesos[-ventana:]]
    previo = [p for _, p in pesos[-2 * ventana:-ventana]]
    m1 = sum(reciente) / len(reciente)
    m0 = sum(previo) / len(previo) if previo else None
    ritmo = (m1 - m0) if m0 else None
    return m1, ritmo, pesos[-1][1]


# ── Armado de dia ─────────────────────────────────────────────────────────────
def plan_dia(perfil, entreno=None, semilla=0):
    """Arma un dia completo que cae dentro de los targets.

    Busca entre todas las combinaciones de desayuno/almuerzo/cena la que mas
    proteina da dejando espacio para snacks, y despues rellena con los snacks
    mas densos en proteina. La busqueda completa es de unos pocos cientos de
    combinaciones: mas barato que adivinar y fallar la meta de proteina, que es
    lo que pasaba llenando de forma codiciosa en dias de descanso.
    """
    if entreno is None:
        entreno = es_dia_entreno(perfil)
    t = targets_de_hoy(perfil, entreno)

    cache = {}

    def mac(r):
        if r['id'] not in cache:
            cache[r['id']] = macros_receta(r)
        return cache[r['id']]

    # Deja entre el 20% y el 30% de las calorias para snacks.
    techo_principales = t['kcal'] * 0.80
    piso_principales = t['kcal'] * 0.60

    def desviacion(tot, cupo):
        """Que tan lejos queda un trio de los targets, ya descontado el cupo
        de snacks. Quedarse CORTO de proteina se castiga fuerte; pasarse un
        poco no molesta. En los demas macros la desviacion es simetrica."""
        obj_k = t['kcal'] * cupo
        obj_p, obj_c, obj_f = t['p'] * cupo, t['c'] * cupo, t['f'] * cupo
        d = abs(tot['kcal'] - obj_k) / obj_k * 3.0
        falta_p = obj_p - tot['p']
        d += (falta_p / obj_p * 4.0) if falta_p > 0 else (-falta_p / obj_p * 0.5)
        d += abs(tot['c'] - obj_c) / max(1.0, obj_c) * 1.5
        d += abs(tot['f'] - obj_f) / max(1.0, obj_f) * 1.0
        d -= min(tot['fib'], 40) / 40 * 0.4      # la fibra siempre suma
        return d

    # Los snacks aportan alrededor del 22% del dia; los principales, el resto.
    cupo = 0.78
    ranking = []
    for b in RECETAS['desayunos']:
        for l in RECETAS['almuerzos']:
            for c in RECETAS['cenas']:
                tot = sumar([mac(b), mac(l), mac(c)])
                if tot['kcal'] > t['kcal'] * 0.88:
                    continue
                ranking.append((desviacion(tot, cupo), [b, l, c], tot))
    ranking.sort(key=lambda x: x[0])

    if not ranking:
        comidas = [min(RECETAS[g], key=lambda r: mac(r)['kcal'])
                   for g in ('desayunos', 'almuerzos', 'cenas')]
        tot = sumar([mac(r) for r in comidas])
    else:
        # La semilla rota entre los 6 mejores trios: variedad sin perder el ajuste.
        _, comidas, tot = ranking[semilla % min(6, len(ranking))]
    tot = dict(tot)

    # Snacks: los mas densos en proteina primero, y solo si aportan de verdad.
    snacks = sorted(RECETAS['snacks'], key=lambda r: -(mac(r)['p'] / max(1.0, mac(r)['kcal'])))
    elegidos = []
    for s in snacks:
        m = mac(s)
        if tot['kcal'] + m['kcal'] > t['kcal'] + 40:
            continue
        falta_p = t['p'] - tot['p']
        # Mientras falte proteina, no gastes calorias en snacks que no la traen.
        if falta_p > 15 and m['p'] < 8:
            continue
        elegidos.append(s)
        for k in tot:
            tot[k] += m[k]
        if tot['p'] >= t['p'] and tot['kcal'] >= t['kcal'] - 100:
            break

    return {'entreno': entreno, 'targets': t, 'comidas': comidas,
            'snacks': elegidos, 'totales': tot}


def fmt_plan(plan):
    t, tot = plan['targets'], plan['totales']
    tipo = 'ENTRENO' if plan['entreno'] else 'DESCANSO'
    out = [f"🍽 *Plan de hoy — dia de {tipo}*", ""]
    for r, et in zip(plan['comidas'], ['Desayuno', 'Almuerzo', 'Cena']):
        m = macros_receta(r)
        out.append(f"*{et}* · `{r['id']}` — {r['nombre']}")
        out.append(f"   {m['kcal']:.0f} kcal · {m['p']:.0f} P / {m['c']:.0f} C / {m['f']:.0f} G · {r['minutos']} min")
    if plan['snacks']:
        out.append("")
        out.append("*Snacks*")
        for r in plan['snacks']:
            m = macros_receta(r)
            out.append(f"   `{r['id']}` {r['nombre']} — {m['kcal']:.0f} kcal, {m['p']:.0f} P")
    out += ["", "*Total del dia*",
            f"   {tot['kcal']:.0f} / {t['kcal']} kcal",
            f"   {tot['p']:.0f} / {t['p']} g proteina",
            f"   {tot['c']:.0f} / {t['c']} g carbos",
            f"   {tot['f']:.0f} / {t['f']} g grasa",
            f"   {tot['fib']:.0f} / {t['fib']} g fibra",
            "", "_Manda `/receta <id>` para ver los pasos de cualquiera._"]
    return '\n'.join(out)


# ── Lista de mercado ──────────────────────────────────────────────────────────
def lista_mercado(perfil, dias=7):
    """Suma los gramos de una semana de planes y los agrupa por seccion.

    Genera la semana real (4 dias de entreno + 3 de descanso) en vez de
    multiplicar un dia por siete: los menus rotan y los gramajes cambian entre
    dia de entreno y de descanso.
    """
    gramos = {}
    entrenos = min(4, dias)
    tipos = [True] * entrenos + [False] * (dias - entrenos)
    for i, entreno in enumerate(tipos):
        plan = plan_dia(perfil, entreno=entreno, semilla=i)
        for r in plan['comidas'] + plan['snacks']:
            for ing in r['ingredientes']:
                gramos[ing['food']] = gramos.get(ing['food'], 0) + ing['g']

    fuera = []
    secciones = {}
    for fid, g in gramos.items():
        sec = next((s for s, ids in SECCIONES.items() if fid in ids), None)
        if sec is None:
            fuera.append(fid)
            continue
        secciones.setdefault(sec, []).append((fid, g))

    orden = list(SECCIONES)
    return {
        'dias': dias,
        'secciones': {s: sorted(secciones[s], key=lambda x: -x[1])
                      for s in orden if s in secciones},
        'sin_seccion': fuera,
    }


def _cantidad(fid, g):
    """Gramos en una cantidad que se pueda comprar de verdad."""
    f = FOODS[fid]
    if f.get('unit_g'):
        import math
        u = math.ceil(g / f['unit_g'])
        return f"{u} u ({g:.0f} g)"
    if g >= 1000:
        return f"{g/1000:.1f} kg"
    return f"{g:.0f} g"


def fmt_mercado(m):
    out = [f"🛒 *Lista de mercado — {m['dias']} dias*", ""]
    for sec, items in m['secciones'].items():
        out.append(f"*{sec}*")
        for fid, g in items:
            out.append(f"  ☐ {FOODS[fid]['nombre']} — {_cantidad(fid, g)}")
            if FOODS[fid].get('nota_compra'):
                out.append(f"      _{FOODS[fid]['nota_compra']}_")
        out.append("")
    if m['sin_seccion']:
        out.append("_Sin seccion asignada: " + ', '.join(m['sin_seccion']) + "_")
    out += ["_Cantidades para las recetas del plan. Lo que ya tengas en casa, tachalo._"]
    return '\n'.join(out)


# ── El registro ───────────────────────────────────────────────────────────────
FILAS_CSV = ['fecha', 'dia', 'peso_kg', 'media_7d', 'kcal', 'proteina_g', 'carbos_g',
             'grasa_g', 'fibra_g', 'meta_kcal', 'meta_proteina_g', 'adherencia_kcal_pct',
             'entreno', 'series', 'volumen_kg', 'recovery', 'sueno_h', 'strain', 'comidas']

DIAS_ES = ['lunes', 'martes', 'miercoles', 'jueves', 'viernes', 'sabado', 'domingo']


def construir_registro(perfil, dias_datos):
    """Una fila por dia con todo lo que se registro, ya cruzado con los targets.

    Los targets se recalculan por dia con el peso de ESE dia cuando existe: si el
    peso baja, el target baja con el, y comparar el consumo de marzo contra el
    target de septiembre daria una adherencia falsa.
    """
    por_fecha = {d['fecha']: d for d in dias_datos}
    pesos = sorted((f, float(d['peso_kg'])) for f, d in por_fecha.items() if d.get('peso_kg'))

    def media_hasta(fecha):
        previos = [p for f, p in pesos if f <= fecha][-7:]
        return sum(previos) / len(previos) if previos else None

    ultimo_peso = perfil['peso_kg']
    filas = []
    for fecha in sorted(por_fecha):
        d = por_fecha[fecha]
        dt = datetime.strptime(fecha, '%Y-%m-%d')
        if d.get('peso_kg'):
            ultimo_peso = float(d['peso_kg'])
        t = targets_de_hoy({**perfil, 'peso_kg': ultimo_peso},
                           es_dia_entreno(perfil, fecha))
        tot = sumar(d.get('comidas', []))
        ent = d.get('entreno') or {}
        sets = ent.get('sets', [])
        whoop = d.get('whoop') or {}
        media = media_hasta(fecha)

        filas.append({
            'fecha': fecha,
            'dia': DIAS_ES[dt.weekday()],
            'peso_kg': round(float(d['peso_kg']), 1) if d.get('peso_kg') else '',
            'media_7d': round(media, 2) if media else '',
            'kcal': round(tot['kcal']) if d.get('comidas') else '',
            'proteina_g': round(tot['p']) if d.get('comidas') else '',
            'carbos_g': round(tot['c']) if d.get('comidas') else '',
            'grasa_g': round(tot['f']) if d.get('comidas') else '',
            'fibra_g': round(tot['fib']) if d.get('comidas') else '',
            'meta_kcal': t['kcal'],
            'meta_proteina_g': t['p'],
            'adherencia_kcal_pct': round(tot['kcal'] / t['kcal'] * 100) if d.get('comidas') else '',
            'entreno': ent.get('sesion', ''),
            'series': len(sets),
            'volumen_kg': round(sum(s['kg'] * sum(s['reps']) for s in sets)) if sets else '',
            'recovery': whoop.get('recovery', ''),
            'sueno_h': whoop.get('sueno_h', ''),
            'strain': round(whoop['strain'], 1) if whoop.get('strain') else '',
            'comidas': ' | '.join(c.get('etiqueta', '') for c in d.get('comidas', [])),
        })
    return filas


def registro_csv(filas):
    import csv, io
    buf = io.StringIO()
    w = csv.DictWriter(buf, fieldnames=FILAS_CSV, extrasaction='ignore')
    w.writeheader()
    w.writerows(filas)
    return buf.getvalue()


def resumen_registro(filas, perfil):
    """Los numeros que importan de todo el periodo, no de un dia."""
    comidos = [f for f in filas if f['kcal'] != '']
    pesados = [f for f in filas if f['peso_kg'] != '']
    entrenados = [f for f in filas if f['series']]
    r = {
        'dias_total': len(filas),
        'dias_registrados': len(comidos),
        'dias_pesados': len(pesados),
        'entrenos': len(entrenados),
        'series_totales': sum(f['series'] for f in filas),
        'volumen_total': sum(f['volumen_kg'] for f in filas if f['volumen_kg']),
    }
    if comidos:
        r['kcal_prom'] = round(sum(f['kcal'] for f in comidos) / len(comidos))
        r['prot_prom'] = round(sum(f['proteina_g'] for f in comidos) / len(comidos))
        r['fibra_prom'] = round(sum(f['fibra_g'] for f in comidos) / len(comidos))
        r['adherencia'] = round(sum(f['adherencia_kcal_pct'] for f in comidos) / len(comidos))
        # Dias en los que llego a la proteina: el marcador que protege el musculo.
        r['dias_proteina_ok'] = sum(1 for f in comidos
                                    if f['proteina_g'] >= f['meta_proteina_g'] * 0.95)
    if len(pesados) >= 2:
        r['peso_inicial'] = pesados[0]['peso_kg']
        r['peso_final'] = pesados[-1]['peso_kg']
        r['cambio_kg'] = round(pesados[-1]['peso_kg'] - pesados[0]['peso_kg'], 1)
        d0 = datetime.strptime(pesados[0]['fecha'], '%Y-%m-%d')
        d1 = datetime.strptime(pesados[-1]['fecha'], '%Y-%m-%d')
        semanas = max(1, (d1 - d0).days) / 7
        r['ritmo_semanal'] = round(r['cambio_kg'] / semanas, 2)
    return r


# ── Handlers de Telegram ──────────────────────────────────────────────────────
PENDIENTES = {}   # "chat:mensaje" -> items, esperando confirmacion del usuario

PREFIJO_COMIDA = re.compile(r'^\s*(com[ií]|comida|ate|food|c)\s+', re.I)


def es_comida(texto):
    """Distingue 'comi 3 huevos' (nutricion) de '50 groceries' (gastos)."""
    return bool(PREFIJO_COMIDA.match(texto or ''))


def register(bot, ac, db, require_person):
    st = Store(db)

    def perfil_y_targets(persona):
        p = st.perfil(persona)
        return p, targets_de_hoy(p, es_dia_entreno(p))

    # ── /nutricion: el menu ───────────────────────────────────────────────────
    @bot.message_handler(commands=['nutricion', 'nutrition'])
    def cmd_menu(msg):
        bot.send_message(msg.chat.id,
            "🥗 *Nutricion y entreno*\n\n"
            "*Registrar comida*\n"
            "• `comi 3 huevos, 200g cottage, 1 thin`\n"
            "• O manda una *foto del plato* 📸\n"
            "• `/borrar` — quita la ultima comida\n\n"
            "*Ver donde vas*\n"
            "• `/hoy` — calorias y macros de hoy\n"
            "• `/semana` — promedio y tendencia de peso\n"
            "• `/historial` — el registro completo\n"
            "• `/export` — el registro en CSV para Sheets\n"
            "• `/peso 95.4` — registra tu peso\n\n"
            "*Plan*\n"
            "• `/plan` — dia completo que cuadra con tus macros\n"
            "• `/receta` — receta que cabe en lo que te falta\n"
            "• `/gym` — entreno de hoy\n"
            "• `/mercado` — lista de compras de la semana\n\n"
            "*Contexto*\n"
            "• `/perfil` — tus numeros y como se calculan\n"
            "• `/labs` — tus examenes de sangre\n"
            "• `/whoop` — recovery, sueno y strain")

    # ── /perfil ───────────────────────────────────────────────────────────────
    @bot.message_handler(commands=['perfil'])
    def cmd_perfil(msg):
        persona = require_person(msg)
        if not persona:
            return
        args = msg.text.split()[1:]
        if args:
            campos = {}
            for a in args:
                if '=' not in a:
                    continue
                k, v = a.split('=', 1)
                k = k.lower()
                if k in ('peso', 'peso_kg'):
                    campos['peso_kg'] = float(v)
                elif k in ('altura', 'altura_cm'):
                    campos['altura_cm'] = float(v)
                elif k == 'edad':
                    campos['edad'] = int(v)
                elif k in ('dias', 'dias_entreno'):
                    campos['dias_entreno'] = int(v)
                elif k == 'ritmo' and v in RITMOS:
                    campos['ritmo'] = v
                elif k in ('meta', 'peso_meta_kg'):
                    campos['peso_meta_kg'] = float(v)
            if campos:
                st.guardar_perfil(persona, campos)
                bot.send_message(msg.chat.id, "✅ Perfil actualizado. Recalculando…")

        p = st.perfil(persona)
        t = calcular_targets(p)
        imc = p['peso_kg'] / (p['altura_cm'] / 100) ** 2
        falta = p['peso_kg'] - p['peso_meta_kg']
        semanas = falta / t['perdida_semanal_kg'] if t['perdida_semanal_kg'] > 0 else 0
        bot.send_message(msg.chat.id,
            f"👤 *Perfil de {persona.title()}*\n\n"
            f"Peso: *{p['peso_kg']:.1f} kg* · Altura: {p['altura_cm']:.0f} cm · Edad: {p['edad']}\n"
            f"IMC: *{imc:.1f}* · Meta: {p['peso_meta_kg']:.0f} kg (faltan {falta:.1f} kg)\n"
            f"Entrenos: {p['dias_entreno']}/semana · Ritmo: {p['ritmo']}\n\n"
            "*Como salen tus numeros*\n"
            f"BMR (Mifflin-St Jeor): *{t['bmr']} kcal*\n"
            f"TDEE (con {p['dias_entreno']} entrenos): *{t['tdee']} kcal*\n"
            f"Deficit: *−{t['deficit_dia']} kcal/dia*\n\n"
            "*Tus targets*\n"
            f"🏋 Dia de entreno: *{t['entreno']['kcal']} kcal* — "
            f"{t['entreno']['p']} P / {t['entreno']['c']} C / {t['entreno']['f']} G\n"
            f"😴 Dia de descanso: *{t['descanso']['kcal']} kcal* — "
            f"{t['descanso']['p']} P / {t['descanso']['c']} C / {t['descanso']['f']} G\n"
            f"Promedio semanal: {t['kcal_promedio']} kcal\n"
            f"Fibra: {t['fibra']} g/dia\n\n"
            f"Ritmo esperado: *{t['perdida_semanal_kg']} kg/semana* "
            f"→ meta en ~{semanas:.0f} semanas\n\n"
            "_Cambia algo con:_ `/perfil peso=94.2 ritmo=moderado`")

    # ── /hoy ──────────────────────────────────────────────────────────────────
    @bot.message_handler(commands=['hoy', 'today'])
    def cmd_hoy(msg):
        persona = require_person(msg)
        if not persona:
            return
        p, t = perfil_y_targets(persona)
        d = st.dia(persona)
        tot = sumar(d['comidas'])
        tipo = 'entreno' if es_dia_entreno(p) else 'descanso'

        txt = [f"📊 *Hoy* — dia de {tipo}", ""]
        txt.append(linea('🔥 kcal ', tot['kcal'], t['kcal']))
        txt.append(linea('🥩 Prot ', tot['p'], t['p'], ' g'))
        txt.append(linea('🍚 Carb ', tot['c'], t['c'], ' g'))
        txt.append(linea('🥑 Gras ', tot['f'], t['f'], ' g'))
        txt.append(linea('🌾 Fibra', tot['fib'], t['fib'], ' g'))
        if d['comidas']:
            txt += ["", "*Comidas*"]
            for c in d['comidas']:
                txt.append(f"  {c['hora']} · {c['etiqueta']} — {c['kcal']:.0f} kcal, {c['p']:.0f} P")
        else:
            txt += ["", "_Nada registrado todavia. Manda `comi ...` o una foto._"]

        falta_p = t['p'] - tot['p']
        if falta_p > 25:
            txt += ["", f"⚠️ Te faltan *{falta_p:.0f} g de proteina*. "
                        "Lo mas rapido: 150 g de cottage (19 g) o un pouch de YoPRO (15 g)."]
        bot.send_message(msg.chat.id, '\n'.join(txt))

    # ── /peso ─────────────────────────────────────────────────────────────────
    @bot.message_handler(commands=['peso', 'weight'])
    def cmd_peso(msg):
        persona = require_person(msg)
        if not persona:
            return
        m = re.search(r'(\d+(?:[.,]\d+)?)', msg.text)
        if not m:
            bot.send_message(msg.chat.id, "Escribe `/peso 95.4`")
            return
        kg = float(m.group(1).replace(',', '.'))
        st.set_dia(persona, {'peso_kg': kg})
        st.guardar_perfil(persona, {'peso_kg': kg})

        dias = st.ultimos_dias(persona, 21)
        media, ritmo, _ = media_movil_peso(dias)
        p = st.perfil(persona)
        txt = [f"⚖️ Peso registrado: *{kg:.1f} kg*"]
        if media:
            txt.append(f"Media de 7 dias: *{media:.1f} kg*")
        if ritmo is not None:
            flecha = '📉' if ritmo < 0 else ('📈' if ritmo > 0 else '➡️')
            txt.append(f"{flecha} Cambio vs semana pasada: *{ritmo:+.2f} kg*")
            if ritmo > 0.2:
                txt.append("\nLa media subio. Antes de tocar las calorias revisa: "
                           "pesas la mantequilla de mani, el aceite y las nueces? "
                           "Ahi se esconde casi siempre.")
            elif ritmo < -1.2:
                txt.append("\nBajaste muy rapido. Si no fue la primera semana "
                           "(ahi es agua y glucogeno), sube 150 kcal de carbos: "
                           "perder mas de 1 kg/semana empieza a costarte musculo.")
        txt.append(f"\nFaltan *{kg - p['peso_meta_kg']:.1f} kg* para los "
                   f"{p['peso_meta_kg']:.0f} kg.")
        txt.append("\n_Pesate cada manana en ayunas, despues del bano. "
                   "El dato diario es ruido; la media de 7 dias es la senal._")
        bot.send_message(msg.chat.id, '\n'.join(txt))

    # ── /semana ───────────────────────────────────────────────────────────────
    @bot.message_handler(commands=['semana', 'week'])
    def cmd_semana(msg):
        persona = require_person(msg)
        if not persona:
            return
        p, _ = perfil_y_targets(persona)
        t = calcular_targets(p)
        dias = st.ultimos_dias(persona, 7)
        con_registro = [d for d in dias if d.get('comidas')]
        txt = ["📅 *Ultimos 7 dias*", ""]
        if con_registro:
            prom = sumar([sumar(d['comidas']) for d in con_registro])
            n = len(con_registro)
            txt += [f"Dias registrados: *{n}/7*",
                    f"Promedio: *{prom['kcal']/n:.0f} kcal* "
                    f"(meta {t['kcal_promedio']})",
                    f"Proteina: *{prom['p']/n:.0f} g* (meta {t['proteina']})",
                    f"Fibra: *{prom['fib']/n:.0f} g* (meta {t['fibra']})"]
            deficit = t['tdee'] - prom['kcal'] / n
            txt.append(f"\nDeficit real: *−{deficit:.0f} kcal/dia* "
                       f"→ ~{deficit*7/7700:.2f} kg/semana")
            if n < 5:
                txt.append("\n⚠️ Con menos de 5 dias registrados el promedio "
                           "no significa nada. Registrar es la mitad del trabajo.")
        else:
            txt.append("_Sin comidas registradas esta semana._")

        media, ritmo, ultimo = media_movil_peso(st.ultimos_dias(persona, 21))
        if media:
            txt += ["", "*Peso*", f"Media 7 dias: *{media:.1f} kg*"]
            if ritmo is not None:
                txt.append(f"Cambio semanal: *{ritmo:+.2f} kg*")
        bot.send_message(msg.chat.id, '\n'.join(txt))

    # ── /plan ─────────────────────────────────────────────────────────────────
    @bot.message_handler(commands=['plan'])
    def cmd_plan(msg):
        persona = require_person(msg)
        if not persona:
            return
        p = st.perfil(persona)
        semilla = datetime.now().timetuple().tm_yday
        bot.send_message(msg.chat.id, fmt_plan(plan_dia(p, semilla=semilla)))

    # ── /receta ───────────────────────────────────────────────────────────────
    @bot.message_handler(commands=['receta', 'recipe'])
    def cmd_receta(msg):
        persona = require_person(msg)
        if not persona:
            return
        args = msg.text.split()[1:]

        if args:
            grupo, r = buscar_receta(args[0].lower())
            if r:
                m = macros_receta(r)
                ing = '\n'.join(
                    f"  • {FOODS[i['food']]['nombre']} — {i['g']} g" for i in r['ingredientes'])
                pasos = '\n'.join(f"  {k+1}. {s}" for k, s in enumerate(r['pasos']))
                esp = ', '.join(r.get('especias', [])) or '—'
                bot.send_message(msg.chat.id,
                    f"🍳 *{r['nombre']}*\n_{r['minutos']} min · {grupo[:-1]}_\n\n"
                    f"*{m['kcal']:.0f} kcal* — {m['p']:.0f} P / {m['c']:.0f} C / "
                    f"{m['f']:.0f} G / {m['fib']:.0f} fibra\n\n"
                    f"*Ingredientes*\n{ing}\n\n*Especias*\n  {esp}\n\n*Pasos*\n{pasos}")
                return
            bot.send_message(msg.chat.id, f"No tengo la receta `{args[0]}`. Manda /receta sin nada.")
            return

        # Sin argumentos: la que mejor cabe en lo que le queda del dia.
        p, t = perfil_y_targets(persona)
        tot = sumar(st.dia(persona)['comidas'])
        resto = {'kcal': t['kcal'] - tot['kcal'], 'p': t['p'] - tot['p']}

        cand = []
        for grupo, lista in RECETAS.items():
            if grupo.startswith('_'):
                continue
            for r in lista:
                m = macros_receta(r)
                if m['kcal'] > resto['kcal'] + 50:
                    continue
                # Premia la proteina y penaliza dejar calorias sin usar.
                score = m['p'] * 3 - abs(resto['kcal'] - m['kcal']) * 0.1
                cand.append((score, grupo, r, m))
        cand.sort(key=lambda x: -x[0])

        if not resto['kcal'] > 60 or not cand:
            bot.send_message(msg.chat.id,
                f"Ya casi cierras el dia: te quedan *{resto['kcal']:.0f} kcal*.\n"
                "Si te falta proteina, 150 g de cottage con Tajin (165 kcal, 20 P) "
                "o un pouch de YoPRO (104 kcal, 15 P).")
            return

        txt = [f"🍳 *Te quedan {resto['kcal']:.0f} kcal y {resto['p']:.0f} g de proteina*",
               "", "Lo que mejor cabe:"]
        for _, grupo, r, m in cand[:4]:
            txt.append(f"  `{r['id']}` *{r['nombre']}* ({grupo[:-1]}, {r['minutos']} min)")
            txt.append(f"      {m['kcal']:.0f} kcal · {m['p']:.0f} P / {m['c']:.0f} C / {m['f']:.0f} G")
        txt.append("\n_`/receta l3` para ver los pasos._")
        bot.send_message(msg.chat.id, '\n'.join(txt))

    # ── /historial ────────────────────────────────────────────────────────────
    @bot.message_handler(commands=['historial', 'registro'])
    def cmd_historial(msg):
        persona = require_person(msg)
        if not persona:
            return
        m = re.search(r'(\d+)', msg.text)
        dias = max(3, min(60, int(m.group(1)))) if m else 14
        p = st.perfil(persona)
        filas = construir_registro(p, st.ultimos_dias(persona, dias))
        if not filas:
            bot.send_message(msg.chat.id,
                "Todavia no hay nada registrado.\n\n"
                "Empieza con `/peso 96` y `comi ...` — el registro se llena solo "
                "desde ahi.")
            return
        r = resumen_registro(filas, p)

        txt = [f"📓 *Registro — ultimos {dias} dias*", ""]
        # Tabla compacta: solo los dias con algo, los mas recientes arriba.
        txt.append("```")
        txt.append("fecha   peso   kcal  prot  gym")
        # Telegram corta en 4096 caracteres; 30 filas de ~30 chars caben de sobra.
        visibles = filas[-30:]
        for f in reversed(visibles):
            peso = f"{f['peso_kg']:>5.1f}" if f['peso_kg'] != '' else "    ·"
            kcal = f"{f['kcal']:>5}" if f['kcal'] != '' else "    ·"
            prot = f"{f['proteina_g']:>4}" if f['proteina_g'] != '' else "   ·"
            gym = f"{f['series']:>2}s" if f['series'] else " ·"
            txt.append(f"{f['fecha'][5:]}  {peso} {kcal}  {prot}  {gym}")
        txt.append("```")
        if len(visibles) < len(filas):
            txt.append(f"_Tabla: los {len(visibles)} dias mas recientes. "
                       f"Los promedios de abajo cubren los {len(filas)}._")

        txt += ["", "*Consistencia*",
                f"Dias con comida registrada: *{r['dias_registrados']}/{r['dias_total']}*",
                f"Dias pesados: *{r['dias_pesados']}/{r['dias_total']}*",
                f"Entrenos: *{r['entrenos']}* · {r['series_totales']} series"]
        if r.get('volumen_total'):
            txt.append(f"Volumen movido: *{r['volumen_total']:,} kg*")

        if r.get('kcal_prom'):
            txt += ["", "*Promedios*",
                    f"Calorias: *{r['kcal_prom']}* ({r['adherencia']}% del target)",
                    f"Proteina: *{r['prot_prom']} g* — llegaste en "
                    f"*{r['dias_proteina_ok']}/{r['dias_registrados']}* dias",
                    f"Fibra: *{r['fibra_prom']} g*"]

        if r.get('cambio_kg') is not None:
            flecha = '📉' if r['cambio_kg'] < 0 else ('📈' if r['cambio_kg'] > 0 else '➡️')
            txt += ["", "*Peso*",
                    f"{r['peso_inicial']:.1f} → {r['peso_final']:.1f} kg  "
                    f"{flecha} *{r['cambio_kg']:+.1f} kg*",
                    f"Ritmo: *{r['ritmo_semanal']:+.2f} kg/semana*"]
            faltan = r['peso_final'] - p['peso_meta_kg']
            if r['ritmo_semanal'] < -0.05 and faltan > 0:
                txt.append(f"A este ritmo real: ~{faltan / -r['ritmo_semanal']:.0f} "
                           f"semanas para los {p['peso_meta_kg']:.0f} kg.")

        txt += ["", "_`/export` te manda el archivo completo para Excel o Sheets._"]
        bot.send_message(msg.chat.id, '\n'.join(txt))

    # ── /export ───────────────────────────────────────────────────────────────
    @bot.message_handler(commands=['export', 'exportar'])
    def cmd_export(msg):
        persona = require_person(msg)
        if not persona:
            return
        m = re.search(r'(\d+)', msg.text)
        # Tope de 180 dias: cada dia es una lectura a Firestore y el plan free
        # de Render no da para barrer un ano de golpe.
        dias = max(7, min(180, int(m.group(1)))) if m else 90
        aviso = bot.send_message(msg.chat.id, f"⏳ Armando {dias} dias…")
        try:
            p = st.perfil(persona)
            filas = construir_registro(p, st.ultimos_dias(persona, dias))
            if not filas:
                bot.edit_message_text("Todavia no hay nada que exportar.",
                                      msg.chat.id, aviso.message_id)
                return
            import io
            datos = registro_csv(filas).encode('utf-8-sig')   # BOM: Excel abre bien los acentos
            archivo = io.BytesIO(datos)
            archivo.name = f"registro-{persona}-{hoy()}.csv"
            r = resumen_registro(filas, p)
            pie = [f"📓 *Registro de {persona.title()}*",
                   f"{len(filas)} dias · {r['dias_registrados']} con comida · "
                   f"{r['entrenos']} entrenos"]
            if r.get('cambio_kg') is not None:
                pie.append(f"Peso: {r['peso_inicial']:.1f} → {r['peso_final']:.1f} kg "
                           f"({r['cambio_kg']:+.1f})")
            pie.append("\nAbrelo en Sheets o Excel. Una fila por dia, "
                       "con el target de ESE dia al lado de lo que comiste.")
            bot.delete_message(msg.chat.id, aviso.message_id)
            bot.send_document(msg.chat.id, archivo, caption='\n'.join(pie))
        except Exception as e:
            bot.edit_message_text(f"⚠️ No pude armarlo: `{str(e)[:180]}`",
                                  msg.chat.id, aviso.message_id)

    # ── /mercado ──────────────────────────────────────────────────────────────
    @bot.message_handler(commands=['mercado', 'compras'])
    def cmd_mercado(msg):
        persona = require_person(msg)
        if not persona:
            return
        m = re.search(r'(\d+)', msg.text)
        dias = max(1, min(14, int(m.group(1)))) if m else 7
        bot.send_message(msg.chat.id, fmt_mercado(lista_mercado(st.perfil(persona), dias)))

    # ── /labs ─────────────────────────────────────────────────────────────────
    @bot.message_handler(commands=['labs', 'examenes'])
    def cmd_labs(msg):
        with open(os.path.join(DATA, 'labs.json'), encoding='utf-8') as fh:
            L = json.load(fh)
        meta = L['_meta']
        txt = [f"🩸 *Examenes de sangre* — {meta['fechas']['actual']}",
               f"_{meta['laboratorio']} · {meta['medico']}_", "",
               f"_{L['resumen_en_una_frase']}_", "", "*Banderas*"]
        for b in L['banderas']:
            icono = {'ALTO': '🔴', 'BAJO': '🟡'}.get(b['estado'], '🟠')
            txt.append(f"\n{icono} *{b['marcador']}* — {b['estado']}")
            txt.append(f"   {b['previo']} → *{b['actual']}* (ref {b['referencia']} {b['unidad']})")
            txt.append(f"   {b['accion']}")
        txt += ["", "*Normales y vale la pena saberlo*",
                f"  Glucosa {L['en_rango']['metabolico']['glucosa_ayunas']['actual']} · "
                f"Trigliceridos {L['en_rango']['metabolico']['trigliceridos']['actual']} · "
                f"TSH {L['en_rango']['tiroides']['tsh']['actual']}",
                "  Tu tiroides y tu glucosa estan perfectas: el deficit va a funcionar.",
                "", f"⚕️ *{meta['aviso_importante']}*",
                "", "_`/labs preguntas` para lo que hay que preguntarle al medico._"]
        if 'pregunta' in msg.text.lower():
            txt = ["🩺 *Que preguntarle a Dr Brenton Martin*", ""]
            txt += [f"{i+1}. {q}" for i, q in enumerate(L['que_preguntarle_al_medico'])]
            r = L['reexamen']
            txt += ["", f"*Reexamen:* {r['objetivo']}", f"*Cuando:* {r['cuando']}",
                    f"*Peso esperado:* {r['peso_esperado_para_entonces']}"]
        bot.send_message(msg.chat.id, '\n'.join(txt))

    # ── /borrar ───────────────────────────────────────────────────────────────
    @bot.message_handler(commands=['borrar'])
    def cmd_borrar(msg):
        persona = require_person(msg)
        if not persona:
            return
        fuera, tot = st.borrar_ultima(persona)
        if not fuera:
            bot.send_message(msg.chat.id, "No hay nada que borrar hoy.")
            return
        bot.send_message(msg.chat.id,
            f"✅ Borrado: *{fuera['etiqueta']}* (−{fuera['kcal']:.0f} kcal)\n"
            f"Hoy vas en *{tot['kcal']:.0f} kcal*, {tot['p']:.0f} g de proteina.")

    # ── Registrar comida por texto ────────────────────────────────────────────
    def log_texto(msg, persona):
        texto = PREFIJO_COMIDA.sub('', msg.text.strip(), count=1)
        items, faltan = parse_local(texto)
        if faltan:
            try:
                items += parse_con_modelo(ac, ', '.join(faltan))
            except Exception:
                bot.send_message(msg.chat.id,
                    "No pude leer: " + ', '.join(faltan) +
                    "\nPrueba con gramos: `comi 200g cottage, 3 huevos`")
                if not items:
                    return
        if not items:
            bot.send_message(msg.chat.id,
                "No entendi nada de eso. Ejemplos:\n"
                "`comi 3 huevos, 200g cottage`\n`comi receta l3`")
            return

        _, tot = st.add_comida(persona, items, texto[:60])
        p, t = perfil_y_targets(persona)
        m = sumar(items)
        bot.send_message(msg.chat.id,
            f"✅ *{m['kcal']:.0f} kcal* — {m['p']:.0f} P / {m['c']:.0f} C / {m['f']:.0f} G\n"
            f"{fmt_items(items)}\n\n"
            f"*Hoy:* {tot['kcal']:.0f}/{t['kcal']} kcal · "
            f"{tot['p']:.0f}/{t['p']} g proteina\n"
            f"{barra(tot['kcal'], t['kcal'])}\n\n"
            "_Los `~` son estimados del modelo, no de tu base de datos. /borrar si me equivoque._")

    # ── Confirmar comida de una foto ──────────────────────────────────────────
    def pedir_confirmacion(chat_id, parsed):
        items = parsed.get('items', [])
        if not items:
            bot.send_message(chat_id, "Vi comida pero no pude estimar las porciones. "
                                      "Escribela: `comi 200g arroz, 150g tofu`")
            return
        m = sumar(items)
        conf = parsed.get('confianza', 'media')
        icono = {'alta': '🟢', 'media': '🟡', 'baja': '🔴'}.get(conf, '🟡')
        sent = bot.send_message(chat_id,
            f"🍽 *{parsed.get('platillo', 'Comida')}*\n"
            f"{icono} confianza {conf}\n\n"
            f"*{m['kcal']:.0f} kcal* — {m['p']:.0f} P / {m['c']:.0f} C / {m['f']:.0f} G\n"
            f"{fmt_items(items)}\n\n"
            "Guardo esto?")
        clave = f"{chat_id}:{sent.message_id}"
        PENDIENTES[clave] = {'items': items, 'etiqueta': parsed.get('platillo', 'Comida')}
        mk = types.InlineKeyboardMarkup()
        mk.row(types.InlineKeyboardButton("✅ Guardar", callback_data=f"nut|ok|{sent.message_id}"),
               types.InlineKeyboardButton("✏️ Corregir", callback_data=f"nut|fix|{sent.message_id}"))
        mk.row(types.InlineKeyboardButton("❌ Descartar", callback_data=f"nut|no|{sent.message_id}"))
        bot.edit_message_reply_markup(chat_id, sent.message_id, reply_markup=mk)

    @bot.callback_query_handler(func=lambda c: c.data.startswith('nut|'))
    def cb_nut(call):
        _, accion, mid = call.data.split('|', 2)
        cid = call.message.chat.id
        clave = f"{cid}:{mid}"
        pend = PENDIENTES.pop(clave, None)
        persona = get_persona_cb(call)

        if accion == 'no' or not pend or not persona:
            bot.edit_message_text("❌ Descartado." if accion == 'no' else
                                  "⌛ Se vencio. Manda la foto otra vez.",
                                  cid, call.message.message_id)
            return
        if accion == 'fix':
            bot.edit_message_text(
                "✏️ Escribelo tu, que tu ojo es mejor que el mio:\n"
                "`comi 200g arroz, 150g tofu, 100g espinaca`",
                cid, call.message.message_id)
            return

        _, tot = st.add_comida(persona, pend['items'], pend['etiqueta'])
        p, t = perfil_y_targets(persona)
        bot.edit_message_text(
            f"✅ Guardado: *{pend['etiqueta']}*\n\n"
            f"*Hoy:* {tot['kcal']:.0f}/{t['kcal']} kcal · "
            f"{tot['p']:.0f}/{t['p']} g proteina\n{barra(tot['kcal'], t['kcal'])}",
            cid, call.message.message_id)

    def get_persona_cb(call):
        snap = db.collection('emis_money').document('shared').get()
        um = (snap.to_dict() or {}).get('user_map', {}) if snap.exists else {}
        return um.get(str(call.message.chat.id))

    return {'log_texto': log_texto, 'pedir_confirmacion': pedir_confirmacion,
            'store': st}


# telebot se importa aqui para que el modulo se pueda testear sin el bot vivo.
try:
    from telebot import types
except ImportError:
    types = None

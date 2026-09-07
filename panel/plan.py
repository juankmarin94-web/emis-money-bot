"""
Motor del plan: targets, macros y armado de días.

Vivía en nutricion.py, que era del bot de Telegram. Al retirar el bot esta
lógica quedó huérfana, así que se mudó aquí: es lo único de aquel módulo que el
panel necesita, y ahora el panel no depende de nada más.

Los macros nunca se escriben a mano. Las recetas guardan gramos y esto los
multiplica contra data/foods.json, que es la única fuente de verdad.
"""

import json, os

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(RAIZ, 'data')


def _cargar(nombre):
    with open(os.path.join(DATA, nombre), encoding='utf-8') as fh:
        return json.load(fh)


_RAW = _cargar('foods.json')
FOODS = {k: v for k, v in _RAW.items() if not k.startswith('_')}
FOODS.update({k: v for k, v in _RAW.get('_por_comprar', {}).items()
              if not k.startswith('_')})
SECCIONES = {k: v for k, v in _RAW.get('_secciones', {}).items()
             if not k.startswith('_')}
RECETAS = _cargar('recipes.json')
WORKOUTS = _cargar('workouts.json')
LABS = _cargar('labs.json')

PERFIL = {
    'peso_kg': 96.0, 'altura_cm': 179, 'edad': 32, 'sexo': 'h',
    'dias_entreno': 4, 'ritmo': 'agresivo', 'peso_meta_kg': 80.0,
    'vegetariano': True,
}
RITMOS = {'agresivo': 0.28, 'moderado': 0.20, 'lento': 0.12}
FACTOR = {0: 1.30, 1: 1.30, 2: 1.38, 3: 1.38, 4: 1.45, 5: 1.45, 6: 1.53, 7: 1.53}

# Lunes, martes, jueves y viernes son de pesas en el split Upper/Lower x2.
DIAS_ENTRENO = (0, 1, 3, 4)
DIA_SESION = {0: 'upper_a', 1: 'lower_a', 2: 'cardio', 3: 'upper_b',
              4: 'lower_b', 5: 'cardio', 6: 'descanso'}


def calcular_targets(perfil=None):
    """Mifflin-St Jeor -> TDEE -> déficit -> macros con carbohidratos ciclados."""
    p = {**PERFIL, **(perfil or {})}
    kg, cm, edad = float(p['peso_kg']), float(p['altura_cm']), int(p['edad'])
    bmr = 10*kg + 6.25*cm - 5*edad + (5 if p['sexo'] == 'h' else -161)
    tdee = bmr * FACTOR.get(int(p['dias_entreno']), 1.45)
    objetivo = max(tdee * (1 - RITMOS.get(p['ritmo'], 0.28)), bmr * 0.95, 1400)

    prot = round(1.9 * kg)      # retiene músculo en déficit
    gras = round(0.6 * kg)      # piso que protege las hormonas
    carb = max(0, round((objetivo - prot*4 - gras*9) / 4))

    dias_e = int(p['dias_entreno'])
    bump, drop = 140, 140 * dias_e / max(1, 7 - dias_e)
    return {
        'bmr': round(bmr), 'tdee': round(tdee),
        'deficit_dia': round(tdee - objetivo), 'kcal_promedio': round(objetivo),
        'proteina': prot, 'grasa': gras, 'fibra': 35,
        'entreno':  {'kcal': round(objetivo + bump), 'p': prot, 'f': gras,
                     'c': max(0, round(carb + bump/4))},
        'descanso': {'kcal': round(objetivo - drop), 'p': prot, 'f': gras,
                     'c': max(0, round(carb - drop/4))},
        'perdida_semanal_kg': round((tdee - objetivo) * 7 / 7700, 2),
    }


def targets_de(entreno, perfil=None):
    t = calcular_targets(perfil)
    d = t['entreno'] if entreno else t['descanso']
    return {**d, 'fib': t['fibra'], '_full': t}


def macros_de(food_id, gramos):
    f = FOODS.get(food_id)
    if not f:
        return None
    k = gramos / 100.0
    return {'kcal': f['kcal']*k, 'p': f['p']*k, 'c': f['c']*k,
            'f': f['f']*k, 'fib': f.get('fib', 0)*k}


def sumar(lista):
    tot = {'kcal': 0.0, 'p': 0.0, 'c': 0.0, 'f': 0.0, 'fib': 0.0}
    for it in lista:
        for k in tot:
            tot[k] += float(it.get(k, 0) or 0)
    return tot


def macros_receta(r):
    return sumar([m for m in (macros_de(i['food'], i['g']) for i in r['ingredientes']) if m])


def recetas_planas():
    return {r['id']: (grupo, r) for grupo, lista in RECETAS.items()
            if not grupo.startswith('_') for r in lista}


def buscar_receta(rid):
    return recetas_planas().get(rid, (None, None))


def plan_dia(entreno, semilla=0, perfil=None):
    """Elige el trío desayuno/almuerzo/cena más cercano a TODOS los targets y
    rellena con los snacks más densos en proteína.

    La fibra se penaliza cuando el trío queda corto en vez de solo premiarse:
    es la palanca del LDL 3.4, no un extra."""
    t = targets_de(entreno, perfil)
    cache = {}

    def mac(r):
        if r['id'] not in cache:
            cache[r['id']] = macros_receta(r)
        return cache[r['id']]

    cupo = 0.78          # los snacks aportan el resto del día

    def desviacion(tot):
        ok, op, oc, of = (t['kcal']*cupo, t['p']*cupo, t['c']*cupo, t['f']*cupo)
        d = abs(tot['kcal']-ok)/ok * 3.0
        falta_p = op - tot['p']
        d += (falta_p/op * 4.0) if falta_p > 0 else (-falta_p/op * 0.5)
        d += abs(tot['c']-oc)/max(1.0, oc) * 1.5
        d += abs(tot['f']-of)/max(1.0, of) * 1.0
        falta_fib = 26 - tot['fib']
        d += (falta_fib/26 * 1.4) if falta_fib > 0 else -0.35
        return d

    ranking = []
    for b in RECETAS['desayunos']:
        for l in RECETAS['almuerzos']:
            for c in RECETAS['cenas']:
                tot = sumar([mac(b), mac(l), mac(c)])
                if tot['kcal'] > t['kcal'] * 0.88:
                    continue
                ranking.append((desviacion(tot), [b, l, c], tot))
    ranking.sort(key=lambda x: x[0])

    if not ranking:
        comidas = [min(RECETAS[g], key=lambda r: mac(r)['kcal'])
                   for g in ('desayunos', 'almuerzos', 'cenas')]
        tot = sumar([mac(r) for r in comidas])
    else:
        _, comidas, tot = ranking[semilla % min(6, len(ranking))]
    tot = dict(tot)

    elegidos = []
    for s in sorted(RECETAS['snacks'], key=lambda r: -(mac(r)['p'] / max(1.0, mac(r)['kcal']))):
        m = mac(s)
        if tot['kcal'] + m['kcal'] > t['kcal'] + 40:
            continue
        if t['p'] - tot['p'] > 15 and m['p'] < 8:
            continue                     # no gastes calorías en snacks sin proteína
        elegidos.append(s)
        for k in tot:
            tot[k] += m[k]
        if tot['p'] >= t['p'] and tot['kcal'] >= t['kcal'] - 100:
            break

    return {'entreno': entreno, 'targets': t, 'comidas': comidas,
            'snacks': elegidos, 'totales': tot}


def lista_mercado(dias=7, perfil=None):
    """Suma los gramos de la semana real (4 de entreno + 3 de descanso)."""
    gramos = {}
    entrenos = min(4, dias)
    for i, entreno in enumerate([True]*entrenos + [False]*(dias-entrenos)):
        p = plan_dia(entreno, semilla=i, perfil=perfil)
        for r in p['comidas'] + p['snacks']:
            for ing in r['ingredientes']:
                gramos[ing['food']] = gramos.get(ing['food'], 0) + ing['g']
    out = {}
    for fid, g in gramos.items():
        sec = next((s for s, ids in SECCIONES.items() if fid in ids), 'Sin sección')
        out.setdefault(sec, []).append((fid, g))
    return {s: sorted(v, key=lambda x: -x[1]) for s, v in out.items()}

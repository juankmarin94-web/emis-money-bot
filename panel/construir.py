#!/usr/bin/env python3
"""
Arma el panel diario (Artifact) desde los datos reales del bot.

El panel no puede leer Firestore ni el repo en tiempo de ejecucion, asi que los
datos del plan se hornean en la pagina. Este script los genera desde los mismos
JSON que usa el bot, para que /plan en Telegram y el panel nunca muestren cosas
distintas el mismo dia.

    python3 panel/construir.py           -> panel/panel.html

Despues se publica con:
    Artifact(file_path="panel/panel.html", capabilities={"db":{}, "sample":{}})
"""
import json, os, sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, RAIZ)
import nutricion as n

AQUI = os.path.join(RAIZ, 'panel')


def payload():
    # Los 6 mejores trios por tipo de dia, en el MISMO orden que el bot: el
    # panel elige con dia-del-ano % 6 igual que plan_dia(semilla=...).
    planes = {}
    for clave, entreno in (('entreno', True), ('descanso', False)):
        planes[clave] = [
            {'comidas': [r['id'] for r in p['comidas']],
             'snacks':  [r['id'] for r in p['snacks']]}
            for p in (n.plan_dia(n.PERFIL_DEFAULT, entreno=entreno, semilla=s)
                      for s in range(6))
        ]

    recetas = {}
    for grupo, lista in n.RECETAS.items():
        if grupo.startswith('_'):
            continue
        for r in lista:
            m = n.macros_receta(r)
            recetas[r['id']] = {
                'n': r['nombre'], 'g': grupo, 'min': r['minutos'],
                'kcal': round(m['kcal']), 'p': round(m['p']), 'c': round(m['c']),
                'f': round(m['f']), 'fib': round(m['fib']),
                'ing': [[n.FOODS[i['food']]['nombre'], i['g']] for i in r['ingredientes']],
                'esp': r.get('especias', []), 'pasos': r['pasos'],
            }

    with open(os.path.join(n.DATA, 'workouts.json'), encoding='utf-8') as fh:
        W = json.load(fh)
    entrenos = {}
    for k in ('upper_a', 'lower_a', 'upper_b', 'lower_b'):
        s = W[k]
        entrenos[k] = {
            'n': s['nombre'], 'min': s['duracion_min'], 'cal': s['calentamiento'],
            'ej': [{'n': e['nombre'], 's': e['series'], 'r': e['reps'], 'rir': e['rir'],
                    'd': e['descanso_s'], 'alt': e['alternativas'], 'nota': e.get('nota', '')}
                   for e in s['ejercicios']],
        }

    with open(os.path.join(n.DATA, 'labs.json'), encoding='utf-8') as fh:
        L = json.load(fh)

    return {
        'perfil': {k: n.PERFIL_DEFAULT[k] for k in
                   ('peso_kg', 'altura_cm', 'edad', 'sexo', 'dias_entreno',
                    'ritmo', 'peso_meta_kg')},
        'planes': planes, 'recetas': recetas, 'entrenos': entrenos,
        'cardio': W['cardio'],
        'banderas': [{'m': b['marcador'], 'prev': b['previo'], 'act': b['actual'],
                      'ref': b['referencia'], 'u': b['unidad'], 'est': b['estado'],
                      'acc': b['accion']} for b in L['banderas']],
        'diaSesion': {'0': 'upper_a', '1': 'lower_a', '2': 'cardio', '3': 'upper_b',
                      '4': 'lower_b', '5': 'cardio', '6': 'descanso'},
    }


def leer(nombre):
    with open(os.path.join(AQUI, nombre), encoding='utf-8') as fh:
        return fh.read()


def main():
    datos = json.dumps(payload(), ensure_ascii=False, separators=(',', ':'))
    if '__DATOS__' not in leer('app.js.html'):
        raise SystemExit('app.js.html perdio el marcador __DATOS__')
    html = leer('head.html') + leer('body.html') + leer('app.js.html').replace('__DATOS__', datos, 1)
    salida = os.path.join(AQUI, 'panel.html')
    with open(salida, 'w', encoding='utf-8') as fh:
        fh.write(html)
    print(f"{salida}  ({len(html)/1024:.1f} KB, datos {len(datos)/1024:.1f} KB)")


if __name__ == '__main__':
    main()

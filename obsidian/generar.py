#!/usr/bin/env python3
"""
Genera el vault de Obsidian desde data/.

Por qué existe: data/*.json es la fuente de verdad de los macros, pero un JSON
no se lee en el teléfono ni se enlaza con el resto de tu segundo cerebro.
Este script proyecta esos datos a notas de Markdown con frontmatter y wikilinks,
para que el plan viva junto a todo lo demás que ya tienes en Obsidian.

    python3 obsidian/generar.py            -> obsidian/vault/

Las notas generadas se sobreescriben cada vez; NO edites nada dentro de
vault/ salvo Registro/, que es tuyo y el script nunca toca.
"""

import json, os, sys, shutil
from datetime import date

AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(os.path.dirname(AQUI), 'panel'))
import plan as P

VAULT = os.path.join(AQUI, 'vault')
HOY = date.today().isoformat()
GEN = f"generado: {HOY}"

DIAS = ['lunes', 'martes', 'miércoles', 'jueves', 'viernes', 'sábado', 'domingo']
GRUPO_ES = {'desayunos': 'Desayuno', 'almuerzos': 'Almuerzo',
            'cenas': 'Cena', 'snacks': 'Snack'}
SESION_ES = {'upper_a': 'Upper A', 'lower_a': 'Lower A',
             'upper_b': 'Upper B', 'lower_b': 'Lower B',
             'cardio': 'Caminadora', 'descanso': 'Descanso'}


def escribir(ruta, texto):
    full = os.path.join(VAULT, ruta)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, 'w', encoding='utf-8') as fh:
        fh.write(texto.rstrip() + '\n')
    return ruta


def fm(**campos):
    """Frontmatter YAML. Los campos son lo que Dataview consulta."""
    ls = ['---']
    for k, v in campos.items():
        if v is None:
            continue
        if isinstance(v, list):
            ls.append(f'{k}:')
            ls += [f'  - {x}' for x in v]
        else:
            ls.append(f'{k}: {v}')
    ls.append('---')
    return '\n'.join(ls)


# ── 00 Estado: la nota que comprime todo ─────────────────────────────────────
def nota_estado():
    t = P.calcular_targets()
    L = P.LABS
    banderas = '\n'.join(
        f"| {b['marcador']} | {b['previo']} → **{b['actual']}** | {b['referencia']} {b['unidad']} "
        f"| {b['estado']} |" for b in L['banderas'])
    imc = P.PERFIL['peso_kg'] / (P.PERFIL['altura_cm']/100)**2
    semanas = (P.PERFIL['peso_kg'] - P.PERFIL['peso_meta_kg']) / t['perdida_semanal_kg']

    return fm(tipo='estado', tags=['salud/estado'], actualizado=HOY) + f"""

# Estado — Camilo

> [!info] Esta nota es el resumen ejecutable
> Si abres una sesión nueva con Claude, **pégale esta nota sola**. Trae todo lo
> que necesita saber sin que tengas que volver a subir fotos ni reexplicar nada.

## Quién

| | |
|---|---|
| Peso inicial | {P.PERFIL['peso_kg']:.1f} kg |
| Meta | {P.PERFIL['peso_meta_kg']:.0f} kg (IMC 25,0) |
| Altura · edad | {P.PERFIL['altura_cm']} cm · {P.PERFIL['edad']} años |
| IMC inicial | {imc:.1f} |
| Dieta | Vegetariano (huevo y lácteos) |
| Gym | Garage: rack, barra, mancuernas, banco, barra Z, caminadora. **Sin máquinas.** |
| Entreno | Upper/Lower ×2, 4 días |
| Ritmo | {t['perdida_semanal_kg']} kg/semana → meta en ~{semanas:.0f} semanas |

## Energía

```
BMR  (Mifflin-St Jeor) = {t['bmr']} kcal
TDEE (4 entrenos)      = {t['tdee']} kcal
Objetivo (−28%)        = {t['kcal_promedio']} kcal
Déficit                = −{t['deficit_dia']} kcal/día
```

| | Calorías | Proteína | Carbos | Grasa | Fibra |
|---|---|---|---|---|---|
| **Entreno** (L·Ma·J·V) | {t['entreno']['kcal']} | {t['entreno']['p']} g | {t['entreno']['c']} g | {t['entreno']['f']} g | 35 g+ |
| **Descanso** (Mi·Sa·D) | {t['descanso']['kcal']} | {t['descanso']['p']} g | {t['descanso']['c']} g | {t['descanso']['f']} g | 35 g+ |

Detalle en [[Targets y macros]].

## Lo médico — prioridad real

{L['resumen_en_una_frase']}

| Marcador | Antes → Ahora | Referencia | Estado |
|---|---|---|---|
{banderas}

**Pendiente:** {L['reexamen']['objetivo']} — {L['reexamen']['cuando']}.
Detalle y preguntas para el médico en [[Analisis de sangre]].

## Reglas que no se negocian

- Desayuno = **huevos, avena o cereal**. Preferencia mía, está en [[Recetas]].
- **Alcohol en cero** hasta repetir las pruebas hepáticas.
- Creatina 5 g/día.
- En déficit **no se sube peso en la barra: se mantiene**. Ver [[Programa de entreno]].
- Peso: en ayunas, después del baño. La media de 7 días es la señal, el diario es ruido.

## Dónde vive cada cosa

| Qué | Dónde |
|---|---|
| Panel diario (marcar, peso, WHOOP, métricas) | Artifact publicado en claude.ai |
| Macros — fuente de verdad | `data/foods.json` del repo `emis-money-bot` |
| Recetas en gramos | `data/recipes.json` |
| Programa de entreno | `data/workouts.json` |
| Análisis de sangre | `data/labs.json` |
| Este vault | `obsidian/vault/`, regenerado con `obsidian/generar.py` |

> [!warning] El bot de Telegram de nutrición se retiró
> Lo reemplazó el panel. `bot.py` en el repo es **solo** el tracker de gastos
> compartido con Juli.

## Mi registro

```dataview
TABLE peso AS "kg", kcal, proteina AS "prot", recovery AS "rec", sueno AS "sueño"
FROM "Registro"
WHERE tipo = "dia"
SORT file.name DESC
LIMIT 14
```

```dataview
TABLE WITHOUT ID
  round(average(rows.peso), 2) AS "peso medio",
  round(average(rows.kcal)) AS "kcal medias",
  round(average(rows.proteina)) AS "proteína media",
  length(rows) AS "días"
FROM "Registro"
WHERE tipo = "dia" AND peso
GROUP BY dateformat(date(file.name), "kkkk-'W'WW") AS Semana
SORT Semana DESC
LIMIT 8
```

_Las dos consultas de arriba necesitan el plugin **Dataview**. Sin él se ven
como bloques de código y no pasa nada más._

## Índice

- [[Perfil]] · [[Targets y macros]] · [[Analisis de sangre]]
- [[Programa de entreno]] · [[Recetas]] · [[Alimentos]] · [[Mercado]]
- [[Plantilla dia]] — la plantilla de la nota diaria
"""


# ── Notas de referencia ──────────────────────────────────────────────────────
def nota_perfil():
    t = P.calcular_targets()
    return fm(tipo='perfil', tags=['salud/perfil'], peso_inicial=P.PERFIL['peso_kg'],
              peso_meta=P.PERFIL['peso_meta_kg'], altura_cm=P.PERFIL['altura_cm'],
              edad=P.PERFIL['edad'], actualizado=HOY) + f"""

# Perfil

Vegetariano lacto-ovo. Gym en el garage. Adelaide, Australia.

## Datos

- **Peso inicial:** {P.PERFIL['peso_kg']:.1f} kg → **meta {P.PERFIL['peso_meta_kg']:.0f} kg**
- **Altura:** {P.PERFIL['altura_cm']} cm · **Edad:** {P.PERFIL['edad']}
- **Entrenos:** {P.PERFIL['dias_entreno']}/semana · **Ritmo:** {P.PERFIL['ritmo']}

## Cómo se calculan mis números

Mifflin-St Jeor sobre el peso **actual**, no el inicial: conforme bajo de peso,
el TDEE baja y los targets bajan con él. Por eso el panel recalcula cada día
con el último peso registrado.

```
BMR  = 10·kg + 6,25·cm − 5·edad + 5
TDEE = BMR × 1,45        (4 entrenos + ~9.000 pasos)
Meta = TDEE × 0,72       (déficit del 28%)
```

Proteína 1,9 g/kg · Grasa 0,6 g/kg · Carbos al resto, ciclados por día.

Ahora mismo: BMR {t['bmr']} → TDEE {t['tdee']} → **{t['kcal_promedio']} kcal**
de promedio. Ver [[Targets y macros]].

## Restricciones y preferencias

- **Vegetariano** con huevo y lácteos. Sin carne ni pescado.
- **Desayuno:** solo huevos, avena o cereal.
- **Alcohol:** cero hasta repetir las pruebas hepáticas → [[Analisis de sangre]]
- **Suplementos:** creatina 5 g/día, proteína en polvo según falte.

Ver también: [[Estado]]
"""


def nota_targets():
    t = P.calcular_targets()
    filas = []
    for i, nombre in enumerate(DIAS):
        ent = i in P.DIAS_ENTRENO
        d = t['entreno'] if ent else t['descanso']
        filas.append(f"| {nombre.capitalize()} | {'Entreno' if ent else 'Descanso'} | "
                     f"{d['kcal']} | {d['p']} | {d['c']} | {d['f']} | "
                     f"{SESION_ES[P.DIA_SESION[i]]} |")
    return fm(tipo='referencia', tags=['salud/macros'], actualizado=HOY) + f"""

# Targets y macros

Proteína y grasa **fijas todos los días**. Solo se mueven los carbohidratos:
suben el día que entreno, bajan el día que descanso. Es lo más fácil de seguir
y lo mejor para rendir con la barra.

| Día | Tipo | kcal | Prot | Carb | Grasa | Sesión |
|---|---|---|---|---|---|---|
{chr(10).join(filas)}

**Promedio semanal:** {t['kcal_promedio']} kcal · déficit −{t['deficit_dia']}/día
→ **{t['perdida_semanal_kg']} kg/semana** esperados.

## Por qué estos números

- **Proteína {t['proteina']} g (1,9 g/kg).** En déficit decide si pierdo grasa o
  músculo. Siendo vegetariano apunto más alto que un omnívoro: la proteína
  vegetal trae menos leucina por gramo.
- **Grasa {t['grasa']} g (0,6 g/kg).** Piso que protege la producción hormonal.
  No bajar de aquí por querer más carbos.
- **Fibra 35 g+.** El doble del promedio australiano, y no es casualidad: la
  fibra soluble baja el LDL de forma medible. Con el mío en 3,4 esto es
  tratamiento. Ver [[Analisis de sangre]].
- **Carbos al resto.** Van donde generan rendimiento: los días de barra.

## Señales de que hay que ajustar

| Qué observo | Qué significa | Qué hago |
|---|---|---|
| Bajo >1,2 kg/semana sostenido | Déficit demasiado agresivo | Subir 150 kcal de carbos |
| La media de 7 días sube | Casi siempre subconteo | Pesar aceite, mantequilla de maní y nueces una semana |
| Pierdo mucho menos de lo predicho | Subconteo o TDEE sobreestimado | Pesar todo 1 semana antes de tocar calorías |
| Fuerza cae 2 semanas seguidas | Proteína o recuperación cortas | Revisar proteína y sueño antes de bajar más |

Ver también: [[Estado]] · [[Perfil]] · [[Recetas]]
"""


def nota_labs():
    L = P.LABS
    m = L['_meta']
    partes = [fm(tipo='labs', tags=['salud/analisis'], fecha=m['fechas']['actual'],
                 laboratorio=m['laboratorio'], actualizado=HOY),
              f"""
# Análisis de sangre — {m['fechas']['actual']}

**{m['laboratorio']}** · Solicitado por {m['medico']} · {m['muestra']}
Comparativa contra {m['fechas']['previo']}.

> [!danger] {m['aviso_importante']}

{L['resumen_en_una_frase']}

## Banderas, por prioridad
"""]
    for b in L['banderas']:
        partes.append(f"""
### {b['prioridad']}. {b['marcador']} — {b['estado']}

| Antes | Ahora | Referencia |
|---|---|---|
| {b['previo']} | **{b['actual']}** | {b['referencia']} {b['unidad']} |

**Qué es:** {b['que_es']}

**Contexto:** {b['contexto']}

**Acción:** {b['accion']}

**Objetivo al reexamen:** {b['objetivo_reexamen']}
""")
    partes.append("\n## En rango, y vale la pena saberlo\n")
    for cat, vals in L['en_rango'].items():
        partes.append(f"\n### {cat.replace('_', ' ').capitalize()}\n")
        partes.append("| Marcador | Valor | Referencia | Lectura |\n|---|---|---|---|")
        for k, v in vals.items():
            if k == 'lectura':
                continue
            if isinstance(v, dict):
                partes.append(f"| {k.replace('_',' ')} | **{v.get('actual','—')}** "
                              f"{v.get('unidad','')} | {v.get('referencia','—')} | "
                              f"{v.get('lectura','')} |")
        if 'lectura' in vals:
            partes.append(f"\n_{vals['lectura']}_")
    partes.append("\n## Qué preguntarle al médico\n")
    partes += [f"{i+1}. {q}" for i, q in enumerate(L['que_preguntarle_al_medico'])]
    r = L['reexamen']
    partes.append(f"""
## Reexamen

- **Qué:** {r['objetivo']}
- **Cuándo:** {r['cuando']}
- **Peso esperado:** {r['peso_esperado_para_entonces']}

Ver también: [[Estado]] · [[Targets y macros]]
""")
    return '\n'.join(partes)


def notas_entreno():
    W = P.WORKOUTS
    eq = W['_meta']['equipamiento']
    creadas = []

    filas = []
    for i, nombre in enumerate(DIAS):
        clave = P.DIA_SESION[i]
        if clave in ('descanso', 'cardio'):
            filas.append(f"| {nombre.capitalize()} | {SESION_ES[clave]} | — | — |")
        else:
            s = W[clave]
            filas.append(f"| {nombre.capitalize()} | [[{SESION_ES[clave]}]] | "
                         f"{len(s['ejercicios'])} | {sum(e['series'] for e in s['ejercicios'])} |")
    total = sum(sum(e['series'] for e in W[k]['ejercicios'])
                for k in ('upper_a', 'lower_a', 'upper_b', 'lower_b'))
    pr = W['progresion']
    c = W['cardio']

    creadas.append(escribir('Programa de entreno.md',
        fm(tipo='referencia', tags=['salud/entreno'], series_semana=total, actualizado=HOY) + f"""

# Programa de entreno

**{W['_meta']['programa']}** · {total} series semanales

## Mi gym

Tengo: {', '.join(eq['confirmado_en_fotos'][:6]).lower()}, entre otros.
**No tengo:** {', '.join(eq['no_tienes'])}.

{eq['implicacion']}

## La semana

| Día | Sesión | Ejercicios | Series |
|---|---|---|---|
{chr(10).join(filas)}

## La regla que más importa

> [!important] En déficit no se busca subir peso en la barra. Se busca MANTENERLO.
> {W['_meta']['principio']}

## Progresión — {pr['metodo']}

{chr(10).join(f"{i+1}. {r}" for i, r in enumerate(pr['regla']))}

**Límite del garage:** {pr['limitacion_del_garage']}

**Deload:** {pr['deload']}

## Seguridad entrenando solo

{chr(10).join('- ' + x for x in W['_meta']['seguridad_entrenando_solo'])}

## Cardio

{c['principio']}

Meta de pasos: **{c['pasos_objetivo']:,}**/día.

{chr(10).join(f"- **{s['tipo']}** ({s['cuando']}, {s['duracion_min']} min) — {s['intensidad']}" for s in c['sesiones'])}

> [!warning] {c['no_hacer']}

## Suplementos

{chr(10).join(f"- **{k.replace('_',' ').capitalize()}** — {v['dosis']}. {v['por_que']}" for k, v in W['suplementos'].items())}

Ver también: [[Estado]] · {' · '.join(f'[[{SESION_ES[k]}]]' for k in ('upper_a','lower_a','upper_b','lower_b'))}
"""))

    for clave in ('upper_a', 'lower_a', 'upper_b', 'lower_b'):
        s = W[clave]
        ejs = []
        for i, e in enumerate(s['ejercicios'], 1):
            ejs.append(f"""
### {i}. {e['nombre']}

**{e['series']} × {e['reps']}** · RIR {e['rir']} · descanso {e['descanso_s']} s
{f"> {e['nota']}" if e.get('nota') else ''}

_Si no puedo: {', '.join(e['alternativas'])}_
""")
        creadas.append(escribir(f"{SESION_ES[clave]}.md",
            fm(tipo='sesion', tags=['salud/entreno'], sesion=SESION_ES[clave],
               series=sum(e['series'] for e in s['ejercicios']),
               duracion_min=s['duracion_min'], actualizado=HOY) + f"""

# {s['nombre']}

{len(s['ejercicios'])} ejercicios · {sum(e['series'] for e in s['ejercicios'])} series · {s['duracion_min']} min

**Calentamiento:** {s['calentamiento']}
{''.join(ejs)}
Ver también: [[Programa de entreno]]
"""))
    return creadas


def notas_recetas():
    planas = P.recetas_planas()
    creadas = []
    por_grupo = {}

    for rid, (grupo, r) in sorted(planas.items()):
        m = P.macros_receta(r)
        ing = '\n'.join(f"- {P.FOODS[i['food']]['nombre']} — **{i['g']} g**"
                        for i in r['ingredientes'])
        pasos = '\n'.join(f"{k+1}. {s}" for k, s in enumerate(r['pasos']))
        nombre = f"{rid} {r['nombre']}".replace('/', '-').replace(':', '')
        por_grupo.setdefault(grupo, []).append((rid, r, m, nombre))
        creadas.append(escribir(f"Recetas/{nombre}.md",
            fm(tipo='receta', tags=[f"salud/receta/{grupo}"], id=rid, grupo=grupo,
               kcal=round(m['kcal']), proteina=round(m['p']), carbos=round(m['c']),
               grasa=round(m['f']), fibra=round(m['fib']), minutos=r['minutos'],
               base=r.get('base'), actualizado=HOY) + f"""

# {r['nombre']}

**{GRUPO_ES[grupo]}** · {r['minutos']} min{' · sin cocina' if r.get('sin_cocina') else ''}{' · se prepara la noche anterior' if r.get('prep_noche_anterior') else ''}

| kcal | Proteína | Carbos | Grasa | Fibra |
|---|---|---|---|---|
| **{m['kcal']:.0f}** | {m['p']:.0f} g | {m['c']:.0f} g | {m['f']:.0f} g | {m['fib']:.0f} g |

## Ingredientes

{ing}

{'## Especias' + chr(10) + chr(10) + ', '.join(r['especias']) if r.get('especias') else ''}

## Pasos

{pasos}

Ver también: [[Recetas]] · [[Alimentos]]
"""))

    secciones = []
    for grupo in ('desayunos', 'almuerzos', 'cenas', 'snacks'):
        if grupo not in por_grupo:
            continue
        filas = '\n'.join(
            f"| [[{nombre}\\|{rid}]] | {r['nombre']} | {m['kcal']:.0f} | {m['p']:.0f} | "
            f"{m['fib']:.0f} | {r['minutos']} |"
            for rid, r, m, nombre in por_grupo[grupo])
        secciones.append(f"""
## {GRUPO_ES[grupo]}s ({len(por_grupo[grupo])})

| id | Receta | kcal | Prot | Fibra | min |
|---|---|---|---|---|---|
{filas}
""")

    creadas.append(escribir('Recetas.md',
        fm(tipo='indice', tags=['salud/receta'], total=len(planas), actualizado=HOY) + f"""

# Recetas — {len(planas)}

Todas construidas con lo que hay en casa. **Los macros no están escritos a mano:**
se calculan desde los gramos contra [[Alimentos]]. Cambio un gramaje y el macro
se recalcula solo.

> [!note] Regla del desayuno
> {P.RECETAS['_meta'].get('regla_desayunos', 'Huevos, avena o cereal.')}
{''.join(secciones)}
Ver también: [[Estado]] · [[Targets y macros]] · [[Mercado]]
"""))
    return creadas


def nota_alimentos():
    filas = []
    for sec, ids in P.SECCIONES.items():
        filas.append(f"\n### {sec}\n")
        filas.append("| Alimento | kcal | Prot | Carb | Grasa | Fibra | P/100 kcal |\n|---|---|---|---|---|---|---|")
        for fid in ids:
            f = P.FOODS.get(fid)
            if not f:
                continue
            dens = f['p'] / f['kcal'] * 100 if f['kcal'] else 0
            u = f" ·  1 u = {f['unit_g']} g" if f.get('unit_g') else ''
            filas.append(f"| {f['nombre']}{u} | {f['kcal']} | {f['p']} | {f['c']} | "
                         f"{f['f']} | {f.get('fib', 0)} | {dens:.1f} g |")
    return fm(tipo='referencia', tags=['salud/alimentos'], total=len(P.FOODS),
              actualizado=HOY) + f"""

# Alimentos — {len(P.FOODS)}

**Valores por 100 g** salvo donde diga 1 u. Esta tabla es la proyección de
`data/foods.json`, que es la única fuente de verdad de todos los macros del
sistema.

> [!warning] Verifica contra tus etiquetas
> Los valores vienen de tablas AU/NZ y de las fotos de los paquetes. Si un
> número no coincide con tu envase, corrígelo en `data/foods.json` y regenera:
> las 30 recetas y el panel se actualizan solos.

La última columna, **proteína por 100 kcal**, es la que importa en déficit:
mide cuánta proteína traes por caloría gastada.
{''.join(filas)}

Ver también: [[Recetas]] · [[Mercado]]
"""


def nota_mercado():
    m = P.lista_mercado(7)
    partes = []
    for sec, items in m.items():
        partes.append(f"\n### {sec}\n")
        for fid, g in items:
            f = P.FOODS[fid]
            if f.get('unit_g'):
                import math
                cant = f"{math.ceil(g/f['unit_g'])} u ({g:.0f} g)"
            else:
                cant = f"{g/1000:.1f} kg" if g >= 1000 else f"{g:.0f} g"
            partes.append(f"- [ ] {f['nombre']} — **{cant}**")
            if f.get('nota_compra'):
                partes.append(f"    - {f['nota_compra']}")
    n = sum(len(v) for v in m.values())
    return fm(tipo='mercado', tags=['salud/mercado'], items=n, actualizado=HOY) + f"""

# Mercado — 7 días

{n} items, agrupados por sección de Coles para hacer el recorrido de una pasada.
Generado desde la semana real: 4 días de entreno y 3 de descanso, con los menús
rotando. Lo que ya tengas en casa, táchalo.
{chr(10).join(partes)}

Ver también: [[Recetas]] · [[Alimentos]]
"""


def nota_plantilla():
    hab = ['Creatina 5 g', '9.000 pasos', 'Caminata 12 min post-almuerzo',
           'Sin alcohol', '2,5 L de agua']
    return fm(tipo='dia', fecha='{{date}}', peso='', kcal='', proteina='',
              carbos='', grasa='', fibra='', recovery='', sueno='', strain='',
              entreno='', sin_alcohol='') + f"""

# {{{{date:dddd D [de] MMMM}}}}

> Plantilla de la nota diaria. En Obsidian: Configuración → Plantillas → carpeta
> `Plantillas`, y esta nota como plantilla de la nota diaria. Rellena el
> frontmatter de arriba: es lo que leen las consultas de [[Estado]].

## Mañana

- [ ] Peso en ayunas → anotar en `peso:`
- [ ] WHOOP de anoche → `recovery:`, `sueno:`, `strain:`

## Comer

{chr(10).join('- [ ] ' + x for x in ('Desayuno', 'Almuerzo', 'Cena', 'Snacks'))}

Fuera del plan:
-

## Entrenar

- [ ] Sesión del día

Cargas de hoy:
| Ejercicio | kg | Reps |
|---|---|---|
| | | |

## Hábitos

{chr(10).join('- [ ] ' + h for h in hab)}

## Notas

_Hambre, energía, ánimo, lo que sea que quiera recordar._

Ver también: [[Estado]] · [[Targets y macros]]
"""


def nota_leeme():
    return fm(tipo='meta', actualizado=HOY) + """

# Cómo funciona este vault

## Qué se genera y qué es mío

| Carpeta | Quién manda |
|---|---|
| Todo lo de la raíz, `Recetas/`, las sesiones | **Generado.** Se sobreescribe. No editar aquí. |
| `Registro/` | **Mío.** El script nunca lo toca. |
| `Plantillas/` | Generado una vez; puedes editarla y no se pisa si la mueves. |

Para cambiar un macro, una receta o un ejercicio: se edita el JSON en
`data/` del repo y se regenera. Así el vault, el panel y los cálculos nunca
se desincronizan.

```bash
python3 obsidian/generar.py
```

## El truco de la compresión

[[Estado]] existe para una sola cosa: **abrir una sesión nueva de Claude sin
gastar límite**. Pégale esa nota y ya sabe todo — perfil, targets, análisis,
reglas, dónde está cada cosa — sin que subas fotos otra vez ni reexpliques
nada.

Una conversación larga reenvía todo su historial en cada mensaje, así que el
costo crece con el largo. Sesión nueva + [[Estado]] cuesta una fracción de
seguir una conversación de 30 turnos.
"""


def main():
    if os.path.isdir(VAULT):
        # Registro/ es del usuario: se preserva entre regeneraciones.
        reg = os.path.join(VAULT, 'Registro')
        tmp = None
        if os.path.isdir(reg):
            tmp = os.path.join(AQUI, '_registro_tmp')
            shutil.rmtree(tmp, ignore_errors=True)
            shutil.copytree(reg, tmp)
        shutil.rmtree(VAULT)
        if tmp:
            shutil.copytree(tmp, reg)
            shutil.rmtree(tmp)

    creadas = [
        escribir('Estado.md', nota_estado()),
        escribir('Perfil.md', nota_perfil()),
        escribir('Targets y macros.md', nota_targets()),
        escribir('Analisis de sangre.md', nota_labs()),
        escribir('Alimentos.md', nota_alimentos()),
        escribir('Mercado.md', nota_mercado()),
        escribir('Plantillas/Plantilla dia.md', nota_plantilla()),
        escribir('LEEME.md', nota_leeme()),
    ]
    creadas += notas_entreno()
    creadas += notas_recetas()
    os.makedirs(os.path.join(VAULT, 'Registro'), exist_ok=True)
    escribir('Registro/.gitkeep', '')

    total = sum(os.path.getsize(os.path.join(VAULT, c)) for c in creadas)
    print(f"{len(creadas)} notas · {total/1024:.1f} KB en {VAULT}")
    return creadas


if __name__ == '__main__':
    main()

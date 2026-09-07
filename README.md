# Emi's Money + Nutrition Bot

Bot de Telegram que hace dos cosas en el mismo chat: **gastos compartidos** (Juli y Camilo) y
**nutrición, entreno y seguimiento de peso** (Camilo).

Corre como worker en Render. Estado en Firestore. Visión y estimación de macros con Claude.

## Estructura

```
bot.py             Tracker de gastos compartido (Juli y Camilo). Solo eso.
panel/
  plan.py          Motor del plan: targets Mifflin-St Jeor, macros, armado de dias
  construir.py     Genera panel/panel.html para publicar como Artifact
  head/body/app    Fuente del panel (estilos, markup, logica)
obsidian/
  generar.py       Proyecta data/ al vault de Obsidian
  vault/           46 notas. Registro/ es del usuario y no se sobreescribe
data/
  foods.json       53 alimentos. UNICA fuente de verdad de los macros
  recipes.json     30 recetas en GRAMOS. Los macros se calculan, nunca se escriben
  workouts.json    Upper/Lower x2 para gym de garage (sin maquinas)
  labs.json        Analisis de sangre, banderas por prioridad
PROGRAMA.md        El programa completo en prosa
```

### La regla de los datos

`data/foods.json` es la **unica fuente de verdad** de los macros. Las recetas
guardan gramos por ingrediente; todo lo demas multiplica contra ese archivo en
tiempo de ejecucion. Corrige un valor de etiqueta ahi y las 30 recetas, el panel
y el vault se actualizan solos.

```bash
python3 panel/construir.py      # -> panel/panel.html
python3 obsidian/generar.py     # -> obsidian/vault/
```

### El bot de nutricion se retiro

El panel publicado lo reemplazo. Se eliminaron `nutricion.py`, `gym.py`,
`whoop.py` y `recordatorios.py`, y `bot.py` volvio a ser solo gastos. El motor
del plan que vivia en `nutricion.py` se mudo a `panel/plan.py`, que es lo unico
que el panel necesitaba; el panel se genera identico byte a byte.

Estan en el historial de git si algun dia hacen falta:

```bash
git show HEAD~1:nutricion.py
```

## Variables de entorno

| Variable | Requerida | Para qué |
|---|---|---|
| `BOT_TOKEN` | sí | Token del bot de Telegram |
| `ANTHROPIC_KEY` | sí | Visión de fotos y estimación de comida fuera de la base |
| `FIREBASE_CREDS` | sí | JSON de service account (una línea, con `\n` escapados) |
| `WHOOP_CLIENT_ID` | no | Solo si conectas WHOOP |
| `WHOOP_CLIENT_SECRET` | no | Solo si conectas WHOOP |

## Deploy

`render.yaml` ya define el worker. Render clona el repo completo, así que `data/` viaja con el
código — no hay paso de build que lo filtre.

```
buildCommand: pip install -r requirements.txt
startCommand: python bot.py
```

`tzdata` está en requirements porque `zoneinfo` no encuentra la base de datos de zonas en la
imagen de Render sin él, y los recordatorios se calcularían en UTC (9.5 horas corridos).

## Aviso

`data/labs.json` contiene análisis de sangre reales. No es interpretación médica: es la data
transcrita y ordenada para que el plan se diseñe alrededor de ella. Las decisiones clínicas son
del médico tratante.

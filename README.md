# Emi's Money + Nutrition Bot

Bot de Telegram que hace dos cosas en el mismo chat: **gastos compartidos** (Juli y Camilo) y
**nutrición, entreno y seguimiento de peso** (Camilo).

Corre como worker en Render. Estado en Firestore. Visión y estimación de macros con Claude.

## Estructura

```
bot.py             Entrada. Handlers de gastos + ruteo de fotos + cableado de los módulos.
nutricion.py       Targets, parseo de comida, plan del día, lista de mercado, handlers.
gym.py             Sesión del día, registro de series, records.
whoop.py           Cliente de WHOOP (OAuth con refresh token rotatorio) + lectura manual.
recordatorios.py   Hilo que manda recordatorios proactivos según la hora de Adelaide.
data/
  foods.json       53 alimentos con macros por 100 g y sección de supermercado.
  recipes.json     27 recetas en GRAMOS. Los macros se calculan, nunca se escriben.
  workouts.json    Upper/Lower x2 para gym de garage (sin máquinas).
  labs.json        Análisis de sangre transcritos, banderas ordenadas por prioridad.
PROGRAMA.md        El programa completo en prosa.
```

### La regla de los datos

`data/foods.json` es la **única fuente de verdad** de los macros. Las recetas guardan gramos por
ingrediente; el bot multiplica contra `foods.json` en tiempo de ejecución. Si corriges un valor
de etiqueta, las 27 recetas, el plan del día y la lista de mercado se actualizan solos.

Los valores vienen de tablas AU/NZ y de las fotos de las etiquetas. **Verifícalos contra tus
paquetes** y corrígelos ahí.

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

## Conectar WHOOP

El worker no tiene servidor web, así que no puede recibir el redirect de OAuth. Se autoriza una
vez a mano:

1. Crea una app en `developer.whoop.com` con scopes
   `read:recovery read:cycles read:sleep read:workout read:body_measurement read:profile offline`
2. Pon `WHOOP_CLIENT_ID` y `WHOOP_CLIENT_SECRET` en Render
3. Completa el flujo de autorización en el navegador
4. En Telegram: `/whoop token <refresh_token>`

**WHOOP rota el refresh token:** cada canje devuelve uno nuevo e invalida el anterior al
instante. Por eso se guarda en Firestore (`nutricion/{persona}.whoop_auth`) y se reescribe en
cada renovación. En una variable de entorno se rompería al primer refresh.

Las rutas del API están todas en las constantes al inicio de `whoop.py`, en un solo bloque, para
que un cambio de WHOOP se arregle en un solo lugar.

Sin conectar, funciona a mano: `/whoop 65 7.5 12.3` (recovery %, horas de sueño, strain).

## Comandos

**Comida**

| | |
|---|---|
| `comi 3 huevos, 200g cottage` | Registra. Busca en la base local primero; el modelo solo para lo que no está, marcado con `~` |
| *foto* | Una llamada clasifica recibo vs comida y extrae |
| `/hoy` `/semana` | Progreso contra targets |
| `/peso 95.4` | Registra y calcula media móvil de 7 días |
| `/plan` `/receta [id]` | Día completo o receta que cabe en lo que queda |
| `/mercado [días]` | Lista de compras agrupada por sección |
| `/borrar` | Quita la última comida |

**Entreno**

| | |
|---|---|
| `/gym [sesión]` | Sesión del día o una específica |
| `/set sentadilla 80 5,5,4` | Registra serie y detecta record |
| `/prs` `/progresion` | Records y reglas de progresión |

**Contexto**

| | |
|---|---|
| `/perfil` | Números y cómo se calculan |
| `/perfil peso=94.2 ritmo=moderado` | Actualiza y recalcula |
| `/labs` `/labs preguntas` | Banderas de sangre y qué preguntarle al médico |
| `/whoop` | Recovery, sueño, strain y qué hacer hoy |

**Gastos** (sin cambios): `50 groceries` · `together 80 dinner` · `balance 1500` · `/summary` · `/undo`

## Recordatorios automáticos

Hora de Adelaide. Se deduplican por día en Firestore, así que un reinicio del worker no repite
nada. Cada uno tiene una ventana de 60 minutos para sobrevivir reinicios.

| Cuándo | Qué | Se calla si |
|---|---|---|
| 07:00 diario | Pesarse | Ya registró peso hoy |
| 08:00 L·Ma·J·V | Sesión de hoy | — |
| 20:30 diario | Cierre del día | El día cerró dentro de target |
| 10:00 domingo | Preparación en tanda | — |
| 18:00 domingo | Resumen semanal | — |

## Dos cosas que hay que saber al tocar `bot.py`

**El orden de registro importa.** telebot recorre los handlers en orden. Los de gastos usan
`func=lambda m: True` y `func=lambda c: True`, que matchean todo — si se registran antes, se
comen `/hoy`, `/gym` y los callbacks `nut|`. Por eso `nutricion.register()` va **arriba** de
`handle_photo` y `handle_text`.

**El texto de comida se desvía antes de los regex de gastos.** `comi 3 huevos` matchearía
`^(\d+\.?\d*)\s+(.+)$` y se registraría como un gasto de A$3. El desvío está al inicio de
`handle_text`.

## Pruebas

No hay suite automatizada. Hay dos scripts de humo que arrancan el bot con dobles de telebot,
Firestore y Anthropic, y disparan mensajes reales sin credenciales — útiles al tocar handlers o
recordatorios. Están en el historial de la sesión que construyó esto, no versionados.

Lo que sí conviene correr después de tocar los datos:

```bash
# Todas las recetas resuelven sus ingredientes y sus macros son plausibles
python3 -c "
import nutricion as n
for g,l in n.RECETAS.items():
    if g.startswith('_'): continue
    for r in l:
        assert all(i['food'] in n.FOODS for i in r['ingredientes']), r['id']
        m = n.macros_receta(r); print(r['id'], round(m['kcal']), round(m['p']))
"
# Los planes generados caen dentro de los targets
python3 -c "
import nutricion as n
for e in (True, False):
    for s in range(6):
        p = n.plan_dia(n.PERFIL_DEFAULT, entreno=e, semilla=s)
        t, tot = p['targets'], p['totales']
        assert abs(tot['kcal']-t['kcal']) < t['kcal']*0.07, (e, s, tot['kcal'])
        assert tot['p'] >= t['p']*0.95, (e, s, tot['p'])
print('planes OK')
"
```

## Aviso

`data/labs.json` contiene análisis de sangre reales. No es interpretación médica: es la data
transcrita y ordenada para que el plan se diseñe alrededor de ella. Las decisiones clínicas son
del médico tratante.

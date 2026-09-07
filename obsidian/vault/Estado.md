---
tipo: estado
tags:
  - salud/estado
actualizado: 2026-09-07
---

# Estado — Camilo

> [!info] Esta nota es el resumen ejecutable
> Si abres una sesión nueva con Claude, **pégale esta nota sola**. Trae todo lo
> que necesita saber sin que tengas que volver a subir fotos ni reexplicar nada.

## Quién

| | |
|---|---|
| Peso inicial | 96.0 kg |
| Meta | 80 kg (IMC 25,0) |
| Altura · edad | 179 cm · 32 años |
| IMC inicial | 30.0 |
| Dieta | Vegetariano (huevo y lácteos) |
| Gym | Garage: rack, barra, mancuernas, banco, barra Z, caminadora. **Sin máquinas.** |
| Entreno | Upper/Lower ×2, 4 días |
| Ritmo | 0.71 kg/semana → meta en ~23 semanas |

## Energía

```
BMR  (Mifflin-St Jeor) = 1924 kcal
TDEE (4 entrenos)      = 2789 kcal
Objetivo (−28%)        = 2008 kcal
Déficit                = −781 kcal/día
```

| | Calorías | Proteína | Carbos | Grasa | Fibra |
|---|---|---|---|---|---|
| **Entreno** (L·Ma·J·V) | 2148 | 182 g | 225 g | 58 g | 35 g+ |
| **Descanso** (Mi·Sa·D) | 1822 | 182 g | 143 g | 58 g | 35 g+ |

Detalle en [[Targets y macros]].

## Lo médico — prioridad real

Tu metabolismo esta sano (glucosa 4.7, trigliceridos 0.8, TSH 1.2: no hay ninguna excusa fisiologica), pero tu higado levanto la mano (ALT 68) y tu LDL sigue alto. Las dos cosas responden a lo mismo: perder grasa, comer fibra y parar el alcohol.

| Marcador | Antes → Ahora | Referencia | Estado |
|---|---|---|---|
| ALT (alanina aminotransferasa) | 28 → **68** | 5-40 U/L | ALTO |
| LDL colesterol | 3.5 → **3.4** | 0.0-2.5 mmol/L | ALTO |
| Creatinina | 79 → **56** | 60-110 umol/L | BAJO |
| Ferritina | 17 → **50** | 30-400 ug/L | NORMAL BAJO - VIGILAR |

**Pendiente:** Repetir LFT (ALT, AST, GGT), lipidos, hierro y B12 — LFT en 4-8 semanas segun indique el medico; lipidos y hierro a los 3 meses.
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

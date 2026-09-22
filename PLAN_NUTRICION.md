# De 98 a 80 — Plan de Camilo

> Actualizado 22 sep 2026 · peso confirmado **98,0 kg** · olla Philips All-in-One 6L
> Vegetariano · gym en el garage · construido alrededor de los labs de Clinpath.
>
> Artifacts originales: [plan](https://claude.ai/artifact/Gj6bStnrucSrR4L1VhqXWV) ·
> [diario](https://claude.ai/artifact/TevEF1WPJj4D8Mg3vAD4Eh)
>
> **Este documento se genera solo.** Los macros se calculan desde `data/foods.json`; la prosa
> vive en `plan_template.md`. No edites este archivo a mano — cambia los gramos o la plantilla
> y corre `python3 build_plan.py`. Así los números nunca se desincronizan.

| | |
|---|---|
| Peso | **98,0 kg** |
| Altura | 1,79 m · 32 años |
| IMC | 30,6 |
| Meta | 80 kg (IMC 25,0) |
| Entrenos | 4 días/semana |

---

## 01 · Lo primero, porque no es negociable

**ALT 68 U/L** (rango 5–40), venía de 28 hace 14 meses. El GGT lo acompañó: 32 → 47.
Clinpath escribió la instrucción, no la dejó como número suelto:

> "non-specific hepatic impairment. Possible causes … alcohol effect and viral infections.
> Repeat LFTs in one [month] to assess chronicity of abnormality."
> — Clinpath Laboratories · Lab ref 476325447 · 09-Jul-2026

1. **Repite las pruebas hepáticas.** Las pidieron para agosto. Ya vamos por el 22 de septiembre.
2. **Alcohol en cero hasta el reexamen.** Si sigues bebiendo y sigue alto, no vas a saber por qué.
3. **Perder 7–10%** es la intervención con más evidencia para hígado graso. De 98 kg son 7–10 kg.

| Marcador | May-25 | Jul-26 | Referencia | Lectura |
|---|---|---|---|---|
| ALT | 28 | **68 (H)** | 5–40 U/L | Prioridad 1 |
| LDL | 3,5 | **3,4 (H)** | <2,5 mmol/L | Estancado 14 meses. La fibra soluble es la palanca |
| Creatinina | 79 | **56 (L)** | 60–110 µmol/L | eGFR >90. Típico en vegetarianos |
| Ferritina | 17 | **50** | 30–400 µg/L | Hierro sérico bajó de 17,7 a 11,7. Vigilar |
| Glucosa | — | **4,7** | 3,6–5,4 mmol/L | Sin resistencia a la insulina |
| Triglicéridos | 0,7 | **0,8** | <1,5 mmol/L | TG/HDL 0,57 |
| TSH | 2,0 | **1,2** | 0,40–3,50 mU/L | Normal |
| Vit. D / B12 | 93 / 265 | **88 / 319** | — | Sin deficiencia |

**Tu metabolismo está sano.** Glucosa 4,7, triglicéridos 0,8 y TSH 1,2 significan que no hay
excusa fisiológica: el déficit va a funcionar. El hígado y el LDL responden a lo mismo —
perder grasa, comer fibra, parar el alcohol.

*Esto no es consejo médico. Los análisis los interpreta Dr Brenton Martin.*

---

## 02 · Tus números

```
BMR  = 10(98) + 6,25(179) − 5(32) + 5        = 1.944 kcal
TDEE = 1.944 × 1,45  (4 entrenos + 9k pasos) = 2.818 kcal
Meta = TDEE − 30%                            = 1.985 kcal
Déficit                                      = −833 kcal/día
```

| Macro | Objetivo | Por qué |
|---|---|---|
| **Proteína** | **195 g** (2,0 g/kg) | Sube de los 182 g del plan viejo. Cuanto más agresivo el déficit, más decide la proteína si lo que pierdes es grasa o músculo. Siendo vegetariano apuntas más alto: menos leucina por gramo. |
| **Grasa** | **58 g** (0,6 g/kg) — piso | Protege la producción hormonal. No bajes de aquí por querer más carbos. |
| **Carbos** | **~170 g** | Lo que queda. |
| **Fibra** | **38 g +** | El doble del promedio australiano. Con LDL en 3,4 esto es tratamiento, no adorno. |

### El ciclado de carbos se muere aquí, y es mejor así

El plan viejo ciclaba carbos: 225 g los días de entreno, 143 g los de descanso.
Con 195 g de proteína y el piso de 58 g de grasa, eso son 1.302 kcal fijas de 1.985 —
**quedan 683 kcal de carbos, y no hay suficiente presupuesto para ciclar nada.**
Lo intenté y los días de descanso no cerraban: se pasaban 120–190 kcal todos.

Así que: **un solo número todos los días, 1.985 kcal.** Los carbos se mueven *dentro* del día,
no entre días — la mayoría en la comida antes y después de entrenar. Es más fácil de seguir
y el resultado es el mismo.

### El techo de velocidad

Pediste lo más rápido posible. El techo útil es **−30%**, que es exactamente donde está este
plan. Más abajo no compras velocidad: compras músculo perdido, fuerza perdida y rebote. Y con
ALT en 68 hay una razón extra — bajar rápido es el tratamiento, pero bajar a lo bruto (dietas de
1.200 kcal, más de 1,5 kg/semana sostenido) puede empeorar las enzimas hepáticas de forma
transitoria y sube el riesgo de cálculos biliares. **Rápido sí, crash no.**

| Cuándo | Peso | Nota |
|---|---|---|
| Semanas 1–2 | 98 → 94–95 kg | Agua y glucógeno, no grasa. Se frena en la 3: es normal, no falló nada |
| Semana 6 | 94 kg | |
| **Semana 10** | **90 kg** | **8% perdido: el umbral de evidencia para hígado graso. El hito que de verdad importa** |
| Semana 14 | 88 kg | |
| Semana 20 | 85 kg | El TDEE baja con el peso: aquí el ritmo ya es ~0,65 kg/sem |
| Semana 26 | **80 kg** | Marzo 2027 |

**Recalcula cada 4 kg perdidos.** A 90 kg tu TDEE es 2.702, no 2.818, y comer 1.985 deja de ser
un déficit de 833 para ser uno de 717. El plan no se estanca: tú te vuelves más liviano.

Si bajas más de 1,2 kg/semana sostenido estás perdiendo músculo y hay que **subir** calorías.

---

## 03 · La olla es la herramienta, no un juguete

Tres cosas que antes eran fricción y ahora son gratis.

### Tiempos de presión

| Qué | Agua/caldo | Presión | Liberación |
|---|---|---|---|
| Lentejas rojas | 1 : 2,5 | 5 min | natural |
| Lentejas cafés/verdes | 1 : 3 | 9 min | natural |
| Arvejas partidas | 1 : 3 | 12 min | natural |
| Garbanzos secos (sin remojo) | 1 : 4 | 45 min | natural 15 min |
| Garbanzos remojados | 1 : 3 | 15 min | natural |
| Frijoles negros secos (sin remojo) | 1 : 4 | 30 min | natural |
| Arroz basmati | 1 : 1,25 | 5 min | natural 10 min |
| Avena steel-cut | 1 : 3 | 4 min | natural |
| Papa en cubos (en canasta) | 1 taza | 8 min | rápida |
| **Huevos duros** | 1 taza | **5 min** | natural 5 min + hielo |

Cocina todo con **caldo Campbell's en vez de agua**: cero calorías extra, el doble de sabor.
Es la mejora más barata de tu cocina.

### Huevos duros, 12 de una

1 taza de agua, canasta, 5 min de presión, 5 min de liberación natural, baño de hielo 3 min.
Pelan sin pelear. Domingo por la noche = snacks de 13 g de proteína toda la semana.

### Función Yogurt → tu proteína más barata

```
2 L de leche descremada + 150 g de leche en polvo descremada (batidos en frío)
  → 85 °C en sauté/sear low, removiendo
  → enfriar a 43 °C
  → 3 cucharadas de tu kéfir como cultivo
  → 9 h en función Yogurt
  → ~2 kg de yogurt, ~120 g de proteína, ~$5
```

Cuélalo 3 h en un colador con tela y te quedan ~1,2 kg tipo griego a ~10 g de proteína/100 g.
Comprar el equivalente cuesta el triple. **La leche en polvo es el truco real:** 35 g de proteína
por 100 g, lo más barato del supermercado por gramo de proteína, y espesa sin necesidad de colar.

*Verifica en el manual de tu modelo si la función Yogurt incluye el paso de pasteurizado.*

### Las seis reglas de la olla

1. **Los lácteos NUNCA entran a presión.** Yogurt, cottage, leche y kéfir se cortan. Van fuera del fuego, al servir.
2. **Lo espeso va arriba, sin revolver.** Dolmio, tomate concentrado, salsa. Si se pega al fondo la olla marca error de quemado y no sube presión.
3. **Legumbres y granos: liberación natural siempre.** La rápida hace que la espuma salte por la válvula.
4. **La hoja verde entra con la olla ya apagada.** Dos minutos de calor residual bastan.
5. **El tofu va en Sauté/sear high, destapado.** A presión queda esponja.
6. **Mínimo 250 ml de líquido** o nunca alcanza presión.

### Cuánto se puede llenar

| | Límite |
|---|---|
| Guisos y sopas | **2/3 = 4 L** |
| Legumbres, granos, pasta y avena | **1/2 = 3 L** — espuman y pueden tapar la válvula |

Ese límite es el que fija el tamaño máximo de cada tanda. No es una sugerencia.

### Lo que NO va en presión

Tofu · huevos revueltos · avena en hojuelas (se pega) · hoja verde · cualquier lácteo.

---

## 04 · Cocinar para varios días

Cocinas al tamaño máximo que aguanta la olla, no la porción del día.

### El domingo — cuatro tandas, en orden

La olla queda ocupada **~2 h 50 min**, casi todo desatendido.

| | Qué | Olla | Rinde |
|---|---|---|---|
| 1 | **12 huevos duros** | 5 min presión + 5 natural + hielo | toda la semana |
| 2 | **Chili de frijoles negros** `d5` | Pressure cook 30 min, natural | ×4 · nevera 5 días · congela |
| 3 | **Curry marroquí de garbanzos** `d2` | Pressure cook 8 min, natural | ×4 · nevera 4 días · congela |
| 4 | **Dahl de lentejas rojas** `l1` | Pressure cook 5 min, natural | ×4 · nevera 4 días · congela |
| 5 | **Overnight oats** `b3` | sin olla, 5 min | ×4 frascos · nevera 4 días |
| 6 | **Arroz al caldo** | Pressure cook 5 min, natural 10 | 6 porciones |
| — | **2 L de yogurt** *(de noche)* | Yogurt, 9 h | ~120 g de proteína |

**12 porciones principales** listas de los 21 platos de la semana, más desayunos, huevos,
arroz y yogurt. El resto de la semana es calentar.

**El costo:** una tanda de 4 significa comer ese plato 4 veces. Si quieres variedad, haz 2 de
cada una y vuelve a cocinar el miércoles.

### La regla de las tandas

Lo que guardas no lleva todo lo de la receta. Tres destinos:

| | Qué va ahí | Por qué |
|---|---|---|
| **A la olla** | Legumbres, verdura, especias, aceite | Es lo que se cocina y se guarda |
| **Aparte** | Arroz, pasta, wraps, arepas, avena | Tanda propia. Guardados juntos se pasan |
| **Al servir** | Yogurt, cottage, limón, fruta, mantequilla de maní | Dentro se cortan o se aguan |

El bot ya separa las tres columnas: `/receta l1 x4` te da las cantidades de cada grupo.

### Qué NO se hace por tandas

| | Por qué |
|---|---|
| `b1` `b5` `d1` — huevo revuelto y omelette | Recalentado es horrible. 10 min al momento |
| `d3` `d6` `d7` — tofu sellado | Pierde la costra. Y el edamame recalentado se arruga |

Son los platos de 10 minutos. No todo tiene que salir del congelador.

---

## 05 · Las recetas

31 recetas. Los macros salen de `data/foods.json`, no están escritos a mano.

**Desayunos**

| ID | Receta | kcal | P | C | G | Fibra |
|---|---|---|---|---|---|---|
| `b1` | Huevos rancheros en la olla | 473 | **45 g** | 41 g | 12 g | 9 g |
| `b2` | Bowl de yogurt casero con avena y berries | 542 | **54 g** | 48 g | 13 g | 9 g |
| `b3` | Overnight oats proteicos | 571 | **50 g** | 51 g | 17 g | 9 g |
| `b4` | Avena de la olla con proteína y banana | 547 | **43 g** | 65 g | 13 g | 8 g |
| `b5` | Omelette de espinaca, champiñones y cottage | 431 | **54 g** | 9 g | 19 g | 4 g |
| `b6` | Arepas caseras con huevos pericos | 537 | **45 g** | 56 g | 13 g | 3 g |
| `b7` | Bowl de yogurt y proteína (sin avena) | 458 | **58 g** | 29 g | 11 g | 5 g |

**Almuerzos**

| ID | Receta | kcal | P | C | G | Fibra |
|---|---|---|---|---|---|---|
| `l1` | Dahl de lentejas rojas (olla, 5 min) | 695 | **49 g** | 90 g | 8 g | 17 g |
| `l2` | Bowl de garbanzos al curry con arroz al caldo | 716 | **52 g** | 87 g | 15 g | 19 g |
| `l3` | Pasta con Dolmio y tofu desmenuzado | 672 | **48 g** | 69 g | 20 g | 12 g |
| `l4` | Wrap de tofu al curry | 620 | **49 g** | 50 g | 22 g | 10 g |
| `l5` | Ensalada tibia de papa y huevo (olla, 8 min) | 620 | **62 g** | 56 g | 15 g | 9 g |
| `l6` | Burrito bowl de frijoles refritos y arroz al caldo | 597 | **47 g** | 76 g | 8 g | 13 g |
| `l7` | Ensalada grande de tofu y edamame | 615 | **51 g** | 29 g | 32 g | 17 g |

**Cenas**

| ID | Receta | kcal | P | C | G | Fibra |
|---|---|---|---|---|---|---|
| `d1` | Revuelto grande de espinaca y cottage (bajo en carbos) | 541 | **70 g** | 14 g | 20 g | 7 g |
| `d2` | Curry marroquí de garbanzos y espinaca (olla, 8 min) | 603 | **52 g** | 59 g | 15 g | 21 g |
| `d3` | Tofu sellado con verduras y arroz al caldo | 631 | **49 g** | 49 g | 24 g | 13 g |
| `d4` | Sopa de lentejas y verduras (olla, 9 min) | 631 | **47 g** | 63 g | 14 g | 18 g |
| `d5` | Chili de frijoles negros (olla, 30 min) | 643 | **51 g** | 64 g | 14 g | 19 g |
| `d6` | Salteado de edamame y tofu | 641 | **50 g** | 60 g | 22 g | 18 g |
| `d7` | Tofu y verduras al wok (sin arroz) | 591 | **50 g** | 22 g | 31 g | 14 g |

**Snacks**

| ID | Receta | kcal | P | C | G | Fibra |
|---|---|---|---|---|---|---|
| `s1` | Batido de proteína con berries | 195 | **26 g** | 17 g | 2 g | 6 g |
| `s10` | Puñado de almendras (pesado) | 150 | **5 g** | 2 g | 12 g | 3 g |
| `s2` | Cottage con sriracha y tomate | 198 | **26 g** | 11 g | 5 g | 1 g |
| `s3` | Dos huevos duros de la olla | 143 | **13 g** | 1 g | 10 g | 0 g |
| `s4` | Yogurt casero con Whole Earth y canela | 165 | **24 g** | 12 g | 1 g | 0 g |
| `s5` | Edamame con sal | 182 | **18 g** | 14 g | 8 g | 8 g |
| `s6` | Tajada grande de sandia | 150 | **3 g** | 38 g | 1 g | 2 g |
| `s7` | Batido pre-gym de banana y avena | 406 | **43 g** | 49 g | 4 g | 5 g |
| `s8` | Manzana con yogurt | 193 | **15 g** | 33 g | 1 g | 4 g |
| `s9` | Manzana con mantequilla de maní | 214 | **6 g** | 28 g | 10 g | 6 g |

### La regla que resume todo

**~50 g de proteína por comida, cuatro veces al día.** Todo lo demás es detalle.

---

## 06 · La semana verificada

Cada día está armado y comprobado contra los objetivos, no estimado a ojo.

| Día | | Menú | kcal | P | C | G | Fibra |
|---|---|---|---|---|---|---|---|
| **Lunes** | entreno | Omelette de espinaca, champiñones y cottage · Ensalada tibia de papa y huevo (olla, 8 min) · Dos huevos duros de la olla · Manzana con yogurt · Curry marroquí de garbanzos y espinaca (olla, 8 min) | 1990 | **196** | 158 | 60 | 38 |
| **Martes** | entreno | Bowl de yogurt y proteína (sin avena) · Burrito bowl de frijoles refritos y arroz al caldo · Yogurt casero con Whole Earth y canela · Edamame con sal · Tofu y verduras al wok (sin arroz) | 1993 | **197** | 153 | 59 | 40 |
| **Miércoles** | descanso | Overnight oats proteicos · Ensalada grande de tofu y edamame · Batido de proteína con berries · Revuelto grande de espinaca y cottage (bajo en carbos) | 1922 | **197** | 111 | 71 | 39 |
| **Jueves** | entreno | Omelette de espinaca, champiñones y cottage · Wrap de tofu al curry · Batido de proteína con berries · Manzana con yogurt · Curry marroquí de garbanzos y espinaca (olla, 8 min) | 2042 | **196** | 168 | 59 | 45 |
| **Viernes** | entreno | Bowl de yogurt y proteína (sin avena) · Ensalada tibia de papa y huevo (olla, 8 min) · Dos huevos duros de la olla · Edamame con sal · Sopa de lentejas y verduras (olla, 9 min) | 2034 | **198** | 163 | 58 | 40 |
| **Sábado** | descanso | Bowl de yogurt casero con avena y berries · Bowl de garbanzos al curry con arroz al caldo · Edamame con sal · Revuelto grande de espinaca y cottage (bajo en carbos) | 1981 | **194** | 163 | 56 | 43 |
| **Domingo** | descanso | Overnight oats proteicos · Ensalada grande de tofu y edamame · Batido de proteína con berries · Chili de frijoles negros (olla, 30 min) | 2024 | **178** | 161 | 65 | 51 |
| | | **Promedio diario** | **1998** | **193** | 153 | 61 | 42 |

Promedio real: **1.998 kcal · 193 g de proteína · 61 g de grasa · 42 g de fibra.**
Déficit de 820 kcal/día → **0,75 kg/semana.**

### Detalle de cada receta

### Desayunos

**`b1` Huevos rancheros en la olla** — 473 kcal · 45 g P · 41 g C · 12 g G · 9 g fibra  
Huevo entero 100 g · Clara de huevo 200 g · Tomate 150 g · Espinaca 100 g · Frijoles refritos 80 g · Harina PAN 30 g

**`b2` Bowl de yogurt casero con avena y berries** — 542 kcal · 54 g P · 48 g C · 13 g G · 9 g fibra  
Yogurt griego casero 300 g · Proteína en polvo 20 g · Avena en hojuelas 30 g · Berries congelados 120 g · Mantequilla de maní 15 g

**`b3` Overnight oats proteicos** — 571 kcal · 50 g P · 51 g C · 17 g G · 9 g fibra  
Avena en hojuelas 40 g · Cottage alto en proteína 200 g · Yogurt griego casero 150 g · Berries congelados 100 g · Mantequilla de maní 15 g

**`b4` Avena de la olla con proteína y banana** — 547 kcal · 43 g P · 65 g C · 13 g G · 8 g fibra  
Avena en hojuelas 40 g · Leche descremada 250 g · Proteína en polvo 30 g · Banana 110 g · Mantequilla de maní 15 g

**`b5` Omelette de espinaca, champiñones y cottage** — 431 kcal · 54 g P · 9 g C · 19 g G · 4 g fibra  
Huevo entero 100 g · Clara de huevo 200 g · Espinaca 120 g · Champiñones 100 g · Cottage alto en proteína 100 g · Aceite de oliva 5 g

**`b6` Arepas caseras con huevos pericos** — 537 kcal · 45 g P · 56 g C · 13 g G · 3 g fibra  
Harina PAN 60 g · Huevo entero 100 g · Clara de huevo 150 g · Tomate 100 g · Cebolla larga 30 g · Cottage alto en proteína 80 g

**`b7` Bowl de yogurt y proteína (sin avena)** — 458 kcal · 58 g P · 29 g C · 11 g G · 5 g fibra  
Yogurt griego casero 300 g · Proteína en polvo 30 g · Berries congelados 100 g · Mantequilla de maní 15 g

### Almuerzos

**`l1` Dahl de lentejas rojas (olla, 5 min)** — 695 kcal · 49 g P · 90 g C · 8 g G · 17 g fibra  
Lentejas rojas secas 100 g · Tomate 150 g · Espinaca 150 g · Yogurt griego casero 150 g · Arroz basmati crudo 40 g · Aceite de oliva 5 g

**`l2` Bowl de garbanzos al curry con arroz al caldo** — 716 kcal · 52 g P · 87 g C · 15 g G · 19 g fibra  
Garbanzos de lata 240 g · Tomate 150 g · Espinaca 120 g · Yogurt griego casero 150 g · Arroz basmati crudo 40 g · Cottage alto en proteína 100 g · Aceite de oliva 5 g

**`l3` Pasta con Dolmio y tofu desmenuzado** — 672 kcal · 48 g P · 69 g C · 20 g G · 12 g fibra  
Pasta cruda 70 g · Tofu firme 200 g · Dolmio 150 g · Espinaca 150 g · Champiñones 100 g

**`l4` Wrap de tofu al curry** — 620 kcal · 49 g P · 50 g C · 22 g G · 10 g fibra  
Wrap Mission wholegrain 71 g · Tofu firme 200 g · Espinaca 80 g · Zanahoria 80 g · Yogurt griego casero 100 g · Limón 10 g

**`l5` Ensalada tibia de papa y huevo (olla, 8 min)** — 620 kcal · 62 g P · 56 g C · 15 g G · 9 g fibra  
Papa 250 g · Huevo entero 100 g · Clara de huevo 200 g · Cottage alto en proteína 150 g · Espinaca 100 g · Tomate 100 g · Limón 15 g

**`l6` Burrito bowl de frijoles refritos y arroz al caldo** — 597 kcal · 47 g P · 76 g C · 8 g G · 13 g fibra  
Arroz basmati crudo 50 g · Frijoles refritos 180 g · Salsa mild 60 g · Cottage alto en proteína 250 g · Espinaca 80 g · Limón 15 g

**`l7` Ensalada grande de tofu y edamame** — 615 kcal · 51 g P · 29 g C · 32 g G · 17 g fibra  
Tofu firme 200 g · Edamame congelado 120 g · Espinaca 150 g · Tomate 150 g · Zanahoria 80 g · Limón 15 g · Aceite de oliva 8 g

### Cenas

**`d1` Revuelto grande de espinaca y cottage (bajo en carbos)** — 541 kcal · 70 g P · 14 g C · 20 g G · 7 g fibra  
Huevo entero 100 g · Clara de huevo 250 g · Espinaca 200 g · Champiñones 150 g · Cottage alto en proteína 150 g · Cebolla larga 30 g · Aceite de oliva 5 g

**`d2` Curry marroquí de garbanzos y espinaca (olla, 8 min)** — 603 kcal · 52 g P · 59 g C · 15 g G · 21 g fibra  
Garbanzos de lata 240 g · Tomate 200 g · Espinaca 200 g · Yogurt griego casero 150 g · Cottage alto en proteína 100 g · Aceite de oliva 5 g

**`d3` Tofu sellado con verduras y arroz al caldo** — 631 kcal · 49 g P · 49 g C · 24 g G · 13 g fibra  
Tofu firme 260 g · Arroz basmati crudo 35 g · Brócoli 150 g · Calabacín 150 g · Zanahoria 80 g · Cebolla larga 30 g

**`d4` Sopa de lentejas y verduras (olla, 9 min)** — 631 kcal · 47 g P · 63 g C · 14 g G · 18 g fibra  
Lentejas cafés secas 80 g · Zanahoria 120 g · Calabacín 150 g · Tomate 150 g · Espinaca 100 g · Caldo Campbell's 500 g · Cottage alto en proteína 150 g · Aceite de oliva 8 g

**`d5` Chili de frijoles negros (olla, 30 min)** — 643 kcal · 51 g P · 64 g C · 14 g G · 19 g fibra  
Frijoles negros secos 80 g · Tomate 200 g · Pimentón 100 g · Espinaca 100 g · Salsa mild 60 g · Yogurt griego casero 150 g · Cottage alto en proteína 100 g · Aceite de oliva 8 g

**`d6` Salteado de edamame y tofu** — 641 kcal · 50 g P · 60 g C · 22 g G · 18 g fibra  
Edamame congelado 150 g · Tofu firme 150 g · Brócoli 150 g · Habichuela 100 g · Cebolla larga 40 g · Arroz basmati crudo 40 g

**`d7` Tofu y verduras al wok (sin arroz)** — 591 kcal · 50 g P · 22 g C · 31 g G · 14 g fibra  
Tofu firme 250 g · Brócoli 200 g · Champiñones 150 g · Habichuela 100 g · Cebolla larga 40 g · Aceite de oliva 8 g

### Snacks

**`s1` Batido de proteína con berries** — 195 kcal · 26 g P · 17 g C · 2 g G · 6 g fibra  
Proteína en polvo 30 g · Berries congelados 150 g

**`s10` Puñado de almendras (pesado)** — 150 kcal · 5 g P · 2 g C · 12 g G · 3 g fibra  
Almendras 25 g

**`s2` Cottage con sriracha y tomate** — 198 kcal · 26 g P · 11 g C · 5 g G · 1 g fibra  
Cottage alto en proteína 200 g · Tomate 100 g

**`s3` Dos huevos duros de la olla** — 143 kcal · 13 g P · 1 g C · 10 g G · 0 g fibra  
Huevo entero 100 g

**`s4` Yogurt casero con Whole Earth y canela** — 165 kcal · 24 g P · 12 g C · 1 g G · 0 g fibra  
Yogurt griego casero 250 g · Whole Earth 5 g

**`s5` Edamame con sal** — 182 kcal · 18 g P · 14 g C · 8 g G · 8 g fibra  
Edamame congelado 150 g

**`s6` Tajada grande de sandia** — 150 kcal · 3 g P · 38 g C · 1 g G · 2 g fibra  
Sandía 500 g

**`s7` Batido pre-gym de banana y avena** — 406 kcal · 43 g P · 49 g C · 4 g G · 5 g fibra  
Yogurt griego casero 200 g · Banana 110 g · Avena en hojuelas 20 g · Proteína en polvo 25 g

**`s8` Manzana con yogurt** — 193 kcal · 15 g P · 33 g C · 1 g G · 4 g fibra  
Manzana 180 g · Yogurt griego casero 150 g

**`s9` Manzana con mantequilla de maní** — 214 kcal · 6 g P · 28 g C · 10 g G · 6 g fibra  
Manzana 180 g · Mantequilla de maní 20 g

---

## 07 · El entreno

Cuatro días, Upper/Lower, solo con lo que hay en el garage. 84 series semanales.

| Día | Sesión | Series | Foco |
|---|---|---|---|
| Lunes | Upper A | 23 | Horizontal, fuerza. Press de banca y remo con barra |
| Martes | Lower A | 20 | Sentadilla y RDL |
| Miércoles | Caminadora | — | 45 min zona 2, inclinación 5–8% |
| Jueves | Upper B | 23 | Vertical, hipertrofia. Press militar y dominadas |
| Viernes | Lower B | 18 | Bisagra de cadera. Peso muerto y sentadilla frontal |
| Sábado | Caminata | — | 60 min afuera |
| Domingo | Descanso | — | Total |

### Upper A — Horizontal (fuerza) · 60 min
1. Press de banca con barra — 4×5-7, RIR 2. *Pines puestos. Sin observador, nunca al fallo.*
2. Remo con barra (pronado, torso 45°) — 4×6-8, RIR 2. *Tu único jalón horizontal pesado.*
3. Press inclinado con mancuernas — 3×8-10, RIR 2
4. Dominadas en la barra del rack — 3×AMRAP, RIR 1. *A 98 kg salen 0-3. Usa banda por el pie y anota cuál: pasar a una más delgada es el progreso más motivante del programa.*
5. Elevaciones laterales — 3×12-15, RIR 1. *Los hombros anchos son lo que más cambia cómo te ves cuando bajas de peso.*
6. Curl con barra Z — 3×10-12, RIR 1
7. Extensión de tríceps sobre la cabeza con barra Z — 3×12-15, RIR 1

### Lower A — Sentadilla (cuádriceps) · 55 min
1. Sentadilla trasera — 4×5-7, RIR 2. *Pines a la altura de tu punto más bajo.*
2. Peso muerto rumano — 3×8-10, RIR 2. *Sin máquina de femoral, el RDL es TU ejercicio de isquios. No lo cambies.*
3. Sentadilla búlgara con mancuernas — 3×8-10 por pierna, RIR 2
4. Hip thrust con barra apoyado en el banco — 3×8-12, RIR 1
5. Elevación de talones con barra — 4×12-15, RIR 1. *Punta del pie sobre un disco.*
6. Plancha frontal — 3×45-60 s

### Upper B — Vertical (hipertrofia) · 60 min
1. Press militar de pie — 4×6-8, RIR 2. *Glúteos y abdomen apretados, sin arquear.*
2. Dominadas (lastradas si ya salen 8+) — 4×6-10, RIR 2
3. Press de banca con mancuernas — 3×8-12, RIR 1
4. Remo con mancuerna a una mano — 3×10-12 por lado, RIR 1. *Codo hacia la cadera.*
5. Face pull con banda — 3×15-20, RIR 1. *Barato de hacer, caro de saltarse.*
6. Curl martillo — 3×10-12, RIR 1
7. Press cerrado con barra — 3×10-15, RIR 1

### Lower B — Bisagra de cadera (posterior) · 55 min
1. Peso muerto convencional — 3×4-6, RIR 2. *Solo 3 series: cobra caro en recuperación y en déficit recuperas peor.*
2. Sentadilla frontal — 3×6-8, RIR 2
3. Zancadas caminando con mancuernas — 3×10 por pierna, RIR 2
4. Buenos días con barra — 3×10-12, RIR 2. *Peso ligero. Es de isquios, no de ego.*
5. Elevación de piernas colgado — 3×10-15, RIR 1
6. Carga del granjero — 3×40 m

### La regla que más importa

**En déficit no se busca subir peso en la barra. Se busca mantenerlo.** Si sostienes los mismos
kilos mientras bajas de peso corporal, tu fuerza relativa sube y no estás perdiendo músculo.
Estancarte manteniendo el peso mientras bajas grasa no es fallar: es el objetivo del programa.

- **Doble progresión:** +1 rep por serie cada semana. Al tope del rango en todas, +2,5 kg y vuelves al tope bajo.
- **Deload cada 6 semanas:** mismo peso, mitad de series. No la negocies.
- **Entrenas solo:** pines siempre en sentadilla y banca.
- **Discos de rosca:** si el salto mínimo es demasiado, progresa sumando reps antes de subir el disco.

### Cardio

El cardio **no** pone el déficit — lo pone la comida. El cardio es para tu corazón, tu hígado y tus pasos.

- **9.000 pasos/día**
- **Miércoles:** 45 min caminadora zona 2, inclinación 5–8%. Sube el gasto sin castigar rodillas ni robarte recuperación
- **Sábado:** 60 min afuera
- **Todos los días:** 12 min después del almuerzo. Aplana el pico de glucosa. Barato, corto, funciona
- **Nada de HIIT** encima de 4 días de pesas en déficit

---

## 08 · Lo que ya tienes

**Proteína** — claras congeladas Farm Pride (**21 g de proteína por 100 kcal: lo más eficiente de
tu cocina**) · huevos · tofu Macro Perfectly Firm · 2 kg de yogurt · kéfir (también sirve de
cultivo) · leche de soya (4,1 g/100 ml — la de almendra tiene 1,4 g: esa no cuenta como proteína)

**Legumbres** — 3 latas de garbanzos · lata de lentejas · frijoles refritos Old El Paso ·
lentejas, arvejas partidas y garbanzos secos en los contenedores

**Granos** — arroz (×2) · pasta en espiral · penne · avena · cuscús · harina · **Harina P.A.N.**

**Salsas y grasas** — Dolmio · salsa mild · mostaza · aceite de oliva · canola · espray ·
balsámico · sal Saxa · pimienta · ajo crushed · sriracha

**Verdura** — espinaca · zanahoria · cebolla larga

**Grasas** — **mantequilla de maní** · aceite de coco · ghee (×2)

### Preferencias registradas
Vegetariano · **no come pescado** (la lata de salmón de la despensa no cuenta como tu proteína) ·
**no le gusta el tahini** (no aparece en ninguna de las 31 recetas) · desayuno solo de huevos,
avena o cereal.

### Cuatro herramientas que no sabías que tenías

- **Whole Earth (eritritol)** — endulza el yogurt casero y la avena a cero calorías. En un déficit agresivo, poder endulzar sin costo es adherencia pura.
- **Sandía** — 30 kcal/100 g. Para cuando el hambre es de cantidad, no de comida. Una tajada de 500 g son 150 kcal.
- **Harina P.A.N.** — arepas del tamaño que **tú** decidas. 30 g de harina = arepa de ~110 kcal, contra los 60 g por porción de las Sary con queso.
- **Aceite en espray** — 1 segundo son ~5 kcal; un chorro a ojo son ~120. Úsalo en todo lo que va a la sartén.

### Sale de la casa hoy

Papas fritas y paquetes · tartas Cadbury · los dulces · los panecillos ·
**la base de pizza Coles (venció el 13/09)** ·
**el segundo pote de ghee** — tienes el Moksha en la despensa *y* el Dokshaa en la nevera.

### Las tres grasas del estante, en orden

Con LDL en 3,4 la grasa saturada es la variable que importa, y tienes las tres:

| | Grasa saturada | Veredicto |
|---|---|---|
| **Aceite de coco** | ~87% | El más saturado de los tres, por encima del ghee. Al fondo |
| **Ghee** (×2) | ~62% | Al fondo. Un pote, no dos |
| **Aceite de oliva** | ~14% | **Este es el de todos los días** |

No es prohibición: es que el cambio más fácil de todo el plan es agarrar la botella de al lado.
Cambiar grasa saturada por insaturada baja el LDL sin tocar el total de calorías.

Lo que no compras, no te lo comes. Es la regla más barata del plan.

---

## 09 · Lista de compras (una semana)

### Proteína — lo que de verdad falta
| Qué | Cuánto | Por qué |
|---|---|---|
| **Proteína en polvo** | 1 kg | Sin esto los 195 g/día no cuadran. No es opcional |
| **Leche en polvo descremada** | 1 kg | 35 g P/100 g. Motor del yogurt de la olla |
| **Leche descremada** | 4 L | 3 para el yogurt, 1 para cocinar |
| **Cottage cheese alto en proteína** (Bulla) | 3 × 500 g | 12,5 g de proteína por 100 kcal. Aparece en 9 recetas |
| **Tofu firme** | 4 × 450 g | 22 g por serve. Sauté/sear high, nunca presión |
| **Claras congeladas** (Farm Pride) | 2 pouches | Tu proteína más eficiente |
| **Huevos** | 2 docenas | 12 duros en la olla el domingo |
| **Yogurt griego natural** | 1 kg | Hasta que el tuyo esté listo |
| **Creatina monohidrato** | 500 g | 5 g/día. Creatinina 56 + vegetariano = el perfil que más responde. Avísale al médico |

### Grasas — ya resuelto
**La mantequilla de maní ya está en tu casa**, así que esta sección no cuesta nada. Es la que
sostiene el piso de 58 g de grasa: sin ella el plan calculado caía a 44 g, por debajo del piso
hormonal. Aparece en `b2`, `b3`, `b4`, `b7` y `s9`.

**Pésala siempre.** La cucharada a ojo son 35–40 g: 130 kcal fantasma cada vez. Es el error de
conteo más común de cualquier despensa.

*Opcional:* almendras (500 g). Solo aparecen en `s10` y la mantequilla de maní ya cubre la grasa,
así que no son necesarias — pero traen el doble de fibra (12 g/100 g contra 6 g) y un puñado
pesado es más difícil de sobrepasar que un frasco abierto.

### Verdura de volumen — tu punto más débil
Solo tienes espinaca, zanahoria y cebolla larga. En un déficit agresivo la verdura es lo que
llena el plato sin costo calórico.

Brócoli (3) · calabacín (5) · champiñones (750 g) · tomates (2 kg) · pimentón (3) ·
habichuela (500 g) · coliflor (1) · **limones (6)**

*Los limones no son decoración: la vitamina C triplica la absorción del hierro vegetal, y con
ferritina en 50 siendo vegetariano eso importa. Y no tomes café ni té con las comidas de hierro.*

### Congelados — comida de emergencia que no se echa a perder
Edamame (1 kg — 12 g de proteína/100 g) · espinaca (1 kg) · berries (1 kg) · maíz (500 g)

### Fruta
Bananas (6) · manzanas (8)

**Total: 9 líneas de proteína, una bandeja de verdura, cuatro bolsas del congelador.**
El resto ya está en tu casa: las legumbres, el arroz, la pasta, la avena y la mantequilla de maní.

---

## 10 · El bot

Todo esto vive en el bot de Telegram. Los gastos siguen funcionando igual.

| Comando | Qué hace |
|---|---|
| `/hoy` | El menú de hoy con sus macros y el total contra el objetivo |
| `/plan` | La semana completa |
| `/receta l1` | Ingredientes y los pasos exactos de la olla |
| **`/receta l1 x4`** | **Las cantidades para una tanda de 4**, separadas en *a la olla*, *aparte* y *al servir* |
| `/tanda` | El domingo completo: qué cocinar, en qué orden, cuánto rinde y cuántos días dura |
| `/olla` | Llenado, las seis reglas y la tabla de tiempos |
| `/mercado` | La lista de compras de la semana, como checklist |

Si pides una tanda más grande de lo que cabe, el bot te lo dice en vez de dejarte tapar la
válvula: `/receta d4 x6` responde que el máximo seguro son 3 porciones y que lo hagas en dos.

### Cómo se mantiene

```
data/foods.json      47 alimentos · kcal, P, C, G y fibra por 100 g
data/recipes.json    31 recetas, el perfil, la semana, los métodos de olla y las tandas
data/pantry.json     lo que hay en casa y los tamaños de empaque
build_plan.py        regenera PLAN_NUTRICION.md
mercado.py           regenera LISTA_MERCADO.md sumando la semana y restando la despensa
nutricion.py         los comandos del bot (pruébalos con `python3 nutricion.py`)
```

Corriges un valor de etiqueta en `foods.json` contra tu paquete, corres los dos scripts, y el
plan, la lista y el bot quedan con el número nuevo. No hay nada escrito a mano que se pueda
desincronizar.

---

## 11 · Seguimiento

- **Peso:** cada mañana en ayunas, después del baño. El dato diario es ruido; **la media de 7 días es la señal.** Compara medias, nunca días sueltos.
- **Medidas:** cintura y pecho cada 2 semanas.
- **Fotos:** cada 4 semanas, misma luz y misma hora.

**Ajustes cada 2 semanas, sobre la media de 7 días:**
- No bajas en 2 semanas → −150 kcal (de carbos)
- Bajas más de 1,2 kg/semana → +150 kcal. Estás perdiendo músculo
- Vas a 0,7–1,0 kg/semana → no cambies nada
- Perdiste 4 kg → recalcula el TDEE completo

**Si duermes menos de 6,5 h:** el hambre de ese día es bioquímica — más grelina, menos leptina —
no falta de voluntad. Come la proteína primero y no improvises.

---

## 12 · Las primeras 72 horas

1. **Pide la cita para repetir las pruebas hepáticas.** Hoy. Es lo único de todo esto que no espera.
2. **Ve al supermercado con la lista de la sección 08.**
3. **Domingo en la olla:** 12 huevos duros (5 min), una olla de lentejas cafés (9 min), 2 L de yogurt (9 h), arroz con caldo.
4. **Tira lo de la sección 07** antes de guardar las compras nuevas.
5. **Pésate mañana en ayunas** y anótalo. Ese es tu punto cero real, no los 98 de memoria.
6. **Registra todo, aunque te pases.** Un día malo registrado sirve; uno escondido no enseña nada.

---

*Esto no es consejo médico. Tus análisis los interpreta Dr Brenton Martin. Los valores de
etiqueta en `foods.json` son aproximados: verifícalos contra tus paquetes y corrígelos ahí,
que es la única fuente de verdad.*

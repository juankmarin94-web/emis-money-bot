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
| **Proteína** | **178 g** (1,8 g/kg) | En déficit la proteína decide si pierdes grasa o músculo. Estaba en 2,0 g/kg, y bajó por una razón concreta: a 1.985 kcal, 196 g de proteína son el 39% de las calorías, y eso obliga a meterle cottage a todos los platos. 1,8 g/kg sigue de lleno en el rango que conserva masa magra (1,6–2,2) y le devuelve libertad a la comida. |
| **Grasa** | **58 g** (0,6 g/kg) — piso | Protege la producción hormonal. No bajes de aquí por querer más carbos. |
| **Carbos** | **~170 g** | Lo que queda. |
| **Fibra** | **38 g +** | El doble del promedio australiano. Con LDL en 3,4 esto es tratamiento, no adorno. |

### El ciclado de carbos se muere aquí, y es mejor así

El plan viejo ciclaba carbos: 225 g los días de entreno, 143 g los de descanso.
Con la proteína y el piso de grasa fijos quedan unas 760 kcal de carbos —
**no hay presupuesto para ciclar nada.** Lo intenté y los días de descanso no cerraban:
se pasaban 120–190 kcal todos.

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

La olla queda ocupada **~3 h**, casi todo desatendido.

| | Qué | Olla | Rinde |
|---|---|---|---|
| 1 | **12 huevos duros** | 5 min presión + 5 natural + hielo | toda la semana |
| 2 | **Dal makhani** `d1` | Pressure cook 25 min, natural | ×4 · nevera 4 días · congela |
| 3 | **Chili de tres frijoles** `d2` | Pressure cook 30 min, natural | ×4 · nevera 5 días · congela |
| 4 | **Chana masala** `l1` | Pressure cook 8 min, natural | ×4 · nevera 4 días · congela |
| 5 | **Avena cremosa** `b3` | Slow cook 20 min | ×4 frascos · nevera 4 días |
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
| `b2` — huevos pericos | Recalentados no son lo mismo. 15 min al momento |
| `d7` — tofu al ajillo | Pierde la costra si lo recalientas. 15 min |
| `l2` — risotto | Recalentado pierde la textura. Máximo 2 porciones |

Son los platos de 10 minutos. No todo tiene que salir del congelador.

---

## 05 · Las recetas

29 recetas, elegidas por sabor y construidas alrededor de la olla: chana masala, dal makhani,
risotto de champiñones, ajiaco, feijoada, frijoles paisas con chicharrón de tofu, chili con
chocolate amargo, bolognesa de carne de soya. Los macros salen de `data/foods.json`, no están
escritos a mano.

**Todo sigue siendo vegetariano, sin pescado y sin tahini.**

**Desayunos**

| ID | Receta | kcal | P | C | G | Fibra |
|---|---|---|---|---|---|---|
| `b1` | Shakshuka | 525 | **52 g** | 33 g | 20 g | 6 g |
| `b2` | Huevos pericos con arepa y aguacate | 475 | **47 g** | 32 g | 17 g | 4 g |
| `b3` | Avena cremosa de la olla con banana y canela | 455 | **35 g** | 56 g | 10 g | 7 g |
| `b4` | Bowl de yogurt con granola, mango y berries | 437 | **46 g** | 48 g | 6 g | 6 g |
| `b5` | Tortilla española de papa y cebolla | 525 | **50 g** | 39 g | 18 g | 4 g |
| `b6` | Pancakes proteicos de avena y banana | 468 | **51 g** | 51 g | 5 g | 8 g |

**Almuerzos**

| ID | Receta | kcal | P | C | G | Fibra |
|---|---|---|---|---|---|---|
| `l1` | Chana masala | 576 | **39 g** | 72 g | 13 g | 14 g |
| `l2` | Risotto de champiñones | 587 | **43 g** | 57 g | 20 g | 4 g |
| `l3` | Ajiaco vegetariano | 551 | **35 g** | 74 g | 14 g | 10 g |
| `l4` | Burrito bowl de carne de soya | 590 | **43 g** | 72 g | 15 g | 18 g |
| `l5` | Frijoles paisas con chicharrón de tofu | 597 | **36 g** | 67 g | 18 g | 13 g |
| `l6` | Curry rojo tailandés de tofu y garbanzos | 579 | **38 g** | 54 g | 22 g | 15 g |

**Cenas**

| ID | Receta | kcal | P | C | G | Fibra |
|---|---|---|---|---|---|---|
| `d1` | Dal makhani | 572 | **49 g** | 56 g | 12 g | 16 g |
| `d2` | Chili de tres frijoles con chocolate amargo | 576 | **38 g** | 59 g | 18 g | 19 g |
| `d3` | Bolognesa de carne de soya | 529 | **37 g** | 68 g | 12 g | 14 g |
| `d4` | Feijoada vegetariana | 578 | **36 g** | 70 g | 16 g | 20 g |
| `d5` | Lentejas guisadas con plátano maduro | 550 | **36 g** | 70 g | 10 g | 13 g |
| `d6` | Sopa cremosa de tomate rostizado y lenteja roja | 560 | **42 g** | 57 g | 14 g | 12 g |
| `d7` | Tofu al ajillo con brócoli | 562 | **45 g** | 36 g | 24 g | 11 g |

**Snacks**

| ID | Receta | kcal | P | C | G | Fibra |
|---|---|---|---|---|---|---|
| `s1` | Garbanzos crocantes especiados | 188 | **8 g** | 19 g | 8 g | 7 g |
| `s10` | Cottage con tomate y sriracha | 198 | **26 g** | 11 g | 5 g | 1 g |
| `s2` | Batido de mango con yogurt y proteína | 289 | **36 g** | 32 g | 2 g | 2 g |
| `s3` | Dos huevos duros | 143 | **13 g** | 1 g | 10 g | 0 g |
| `s4` | Yogurt con berries y canela | 205 | **25 g** | 20 g | 1 g | 3 g |
| `s5` | Edamame con sal y chili | 182 | **18 g** | 14 g | 8 g | 8 g |
| `s6` | Hummus con bastones de verdura | 192 | **8 g** | 21 g | 8 g | 8 g |
| `s7` | Tostada de aguacate con huevo | 242 | **17 g** | 17 g | 12 g | 5 g |
| `s8` | Manzana con mantequilla de maní | 214 | **6 g** | 28 g | 10 g | 6 g |
| `s9` | Batido pre-gym de banana y avena | 406 | **43 g** | 49 g | 4 g | 5 g |

### La regla que resume todo

**~50 g de proteína por comida, cuatro veces al día.** Todo lo demás es detalle.

---

## 06 · La semana verificada

Cada día está armado y comprobado contra los objetivos, no estimado a ojo.

| Día | | Menú | kcal | P | C | G | Fibra |
|---|---|---|---|---|---|---|---|
| **Lunes** | entreno | Bowl de yogurt con granola, mango y berries · Burrito bowl de carne de soya · Edamame con sal y chili · Cottage con tomate y sriracha · Tofu al ajillo con brócoli | 1969 | **178** | 181 | 58 | 44 |
| **Martes** | entreno | Shakshuka · Curry rojo tailandés de tofu y garbanzos · Yogurt con berries y canela · Cottage con tomate y sriracha · Bolognesa de carne de soya | 2036 | **178** | 186 | 60 | 39 |
| **Miércoles** | descanso | Tortilla española de papa y cebolla · Ajiaco vegetariano · Edamame con sal y chili · Cottage con tomate y sriracha · Dal makhani | 2028 | **178** | 194 | 57 | 39 |
| **Jueves** | entreno | Huevos pericos con arepa y aguacate · Burrito bowl de carne de soya · Yogurt con berries y canela · Edamame con sal y chili · Tofu al ajillo con brócoli | 2014 | **178** | 174 | 65 | 44 |
| **Viernes** | entreno | Shakshuka · Curry rojo tailandés de tofu y garbanzos · Yogurt con berries y canela · Cottage con tomate y sriracha · Chili de tres frijoles con chocolate amargo | 2083 | **179** | 177 | 66 | 44 |
| **Sábado** | descanso | Tortilla española de papa y cebolla · Frijoles paisas con chicharrón de tofu · Yogurt con berries y canela · Edamame con sal y chili · Dal makhani | 2081 | **178** | 196 | 57 | 44 |
| **Domingo** | descanso | Huevos pericos con arepa y aguacate · Chana masala · Batido de mango con yogurt y proteína · Dos huevos duros · Sopa cremosa de tomate rostizado y lenteja roja | 2043 | **177** | 194 | 56 | 32 |
| | | **Promedio diario** | **2036** | **178** | 186 | 59 | 40 |

Promedio real: **2.036 kcal · 178 g de proteína · 59 g de grasa · 40 g de fibra.**
Déficit de 782 kcal/día → **0,71 kg/semana.**

*Las recetas nuevas cuestan 0,04 kg por semana contra las anteriores. Es el precio de comer
dal makhani y ajiaco en vez de cottage con tomate, y vale la pena: el plan que no sigues no
adelgaza nada.*

### Detalle de cada receta

### Desayunos

**`b1` Shakshuka** — 525 kcal · 52 g P · 33 g C · 20 g G · 6 g fibra  
Huevo entero 100 g · Clara de huevo 180 g · Tomate 180 g · Pimentón 90 g · Cebolla 55 g · Cottage alto en proteína 110 g · Pan integral 25 g · Aceite de oliva 5 g

**`b2` Huevos pericos con arepa y aguacate** — 475 kcal · 47 g P · 32 g C · 17 g G · 4 g fibra  
Huevo entero 100 g · Clara de huevo 180 g · Tomate 90 g · Cebolla larga 35 g · Harina PAN 25 g · Aguacate 25 g · Cottage alto en proteína 90 g

**`b3` Avena cremosa de la olla con banana y canela** — 455 kcal · 35 g P · 56 g C · 10 g G · 7 g fibra  
Avena en hojuelas 40 g · Leche descremada 180 g · Proteína en polvo 25 g · Banana 90 g · Mantequilla de maní 10 g

**`b4` Bowl de yogurt con granola, mango y berries** — 437 kcal · 46 g P · 48 g C · 6 g G · 6 g fibra  
Yogurt griego casero 270 g · Proteína en polvo 20 g · Granola 20 g · Mango 90 g · Berries congelados 70 g

**`b5` Tortilla española de papa y cebolla** — 525 kcal · 50 g P · 39 g C · 18 g G · 4 g fibra  
Papa 160 g · Cebolla 55 g · Huevo entero 100 g · Clara de huevo 180 g · Cottage alto en proteína 110 g · Aceite de oliva 5 g

**`b6` Pancakes proteicos de avena y banana** — 468 kcal · 51 g P · 51 g C · 5 g G · 8 g fibra  
Avena en hojuelas 35 g · Clara de huevo 150 g · Banana 70 g · Proteína en polvo 25 g · Yogurt griego casero 90 g · Berries congelados 70 g

### Almuerzos

**`l1` Chana masala** — 576 kcal · 39 g P · 72 g C · 13 g G · 14 g fibra  
Garbanzos de lata 180 g · Tomate 160 g · Cebolla 70 g · Yogurt griego casero 110 g · Arroz basmati crudo 30 g · Cottage alto en proteína 90 g · Aceite de oliva 5 g

**`l2` Risotto de champiñones** — 587 kcal · 43 g P · 57 g C · 20 g G · 4 g fibra  
Arroz arborio crudo 50 g · Champiñones 220 g · Cebolla 45 g · Caldo Campbell's 360 g · Parmesano 20 g · Ricotta light 55 g · Cottage alto en proteína 140 g · Aceite de oliva 5 g

**`l3` Ajiaco vegetariano** — 551 kcal · 35 g P · 74 g C · 14 g G · 10 g fibra  
Papa criolla 140 g · Papa 90 g · Maíz tierno 80 g · Caldo Campbell's 450 g · Crema light 20 g · Alcaparras 15 g · Aguacate 35 g · Cottage alto en proteína 200 g

**`l4` Burrito bowl de carne de soya** — 590 kcal · 43 g P · 72 g C · 15 g G · 18 g fibra  
Carne de soya seca (TVP) 35 g · Arroz basmati crudo 30 g · Frijoles refritos 110 g · Tomate 110 g · Maíz tierno 55 g · Aguacate 35 g · Cottage alto en proteína 110 g · Limón 15 g · Aceite de oliva 5 g

**`l5` Frijoles paisas con chicharrón de tofu** — 597 kcal · 36 g P · 67 g C · 18 g G · 13 g fibra  
Frijol rojo seco 50 g · Plátano maduro 55 g · Tofu firme 140 g · Tomate 90 g · Cebolla 55 g · Arroz basmati crudo 20 g · Aceite de oliva 5 g

**`l6` Curry rojo tailandés de tofu y garbanzos** — 579 kcal · 38 g P · 54 g C · 22 g G · 15 g fibra  
Tofu firme 160 g · Garbanzos de lata 90 g · Leche de coco light 65 g · Pasta de curry rojo 20 g · Pimentón 90 g · Habichuela 90 g · Espinaca 70 g · Arroz jazmín crudo 25 g · Limón 15 g

### Cenas

**`d1` Dal makhani** — 572 kcal · 49 g P · 56 g C · 12 g G · 16 g fibra  
Lentejas negras secas 55 g · Frijol rojo seco 20 g · Tomate 140 g · Cebolla 65 g · Yogurt griego casero 110 g · Crema light 20 g · Cottage alto en proteína 140 g · Aceite de oliva 5 g

**`d2` Chili de tres frijoles con chocolate amargo** — 576 kcal · 38 g P · 59 g C · 18 g G · 19 g fibra  
Frijoles negros secos 30 g · Frijol rojo seco 20 g · Garbanzos de lata 70 g · Tomate 160 g · Pimentón 90 g · Cebolla 65 g · Chocolate 85% 5 g · Cottage alto en proteína 140 g · Aguacate 25 g · Aceite de oliva 5 g

**`d3` Bolognesa de carne de soya** — 529 kcal · 37 g P · 68 g C · 12 g G · 14 g fibra  
Carne de soya seca (TVP) 40 g · Pasta cruda 50 g · Pasta de tomate 25 g · Tomate 160 g · Cebolla 55 g · Zanahoria 45 g · Apio 35 g · Parmesano 20 g · Aceite de oliva 5 g

**`d4` Feijoada vegetariana** — 578 kcal · 36 g P · 70 g C · 16 g G · 20 g fibra  
Frijoles negros secos 55 g · Tempeh 80 g · Naranja 70 g · Cebolla 65 g · Tomate 90 g · Arroz basmati crudo 25 g · Espinaca 140 g · Aceite de oliva 5 g

**`d5` Lentejas guisadas con plátano maduro** — 550 kcal · 36 g P · 70 g C · 10 g G · 13 g fibra  
Lentejas cafés secas 65 g · Plátano maduro 70 g · Tomate 120 g · Cebolla 55 g · Zanahoria 65 g · Cottage alto en proteína 140 g · Aceite de oliva 5 g

**`d6` Sopa cremosa de tomate rostizado y lenteja roja** — 560 kcal · 42 g P · 57 g C · 14 g G · 12 g fibra  
Tomate 320 g · Lentejas rojas secas 50 g · Cebolla 65 g · Caldo Campbell's 360 g · Ricotta light 45 g · Cottage alto en proteína 140 g · Pan integral 20 g · Aceite de oliva 5 g

**`d7` Tofu al ajillo con brócoli** — 562 kcal · 45 g P · 36 g C · 24 g G · 11 g fibra  
Tofu firme 210 g · Brócoli 180 g · Champiñones 140 g · Cebolla larga 35 g · Salsa de soya 20 g · Arroz basmati crudo 25 g · Aceite de oliva 5 g

### Snacks

**`s1` Garbanzos crocantes especiados** — 188 kcal · 8 g P · 19 g C · 8 g G · 7 g fibra  
Garbanzos de lata 120 g · Aceite de oliva 5 g

**`s10` Cottage con tomate y sriracha** — 198 kcal · 26 g P · 11 g C · 5 g G · 1 g fibra  
Cottage alto en proteína 200 g · Tomate 100 g

**`s2` Batido de mango con yogurt y proteína** — 289 kcal · 36 g P · 32 g C · 2 g G · 2 g fibra  
Mango 150 g · Yogurt griego casero 150 g · Proteína en polvo 25 g

**`s3` Dos huevos duros** — 143 kcal · 13 g P · 1 g C · 10 g G · 0 g fibra  
Huevo entero 100 g

**`s4` Yogurt con berries y canela** — 205 kcal · 25 g P · 20 g C · 1 g G · 3 g fibra  
Yogurt griego casero 250 g · Berries congelados 80 g · Whole Earth 5 g

**`s5` Edamame con sal y chili** — 182 kcal · 18 g P · 14 g C · 8 g G · 8 g fibra  
Edamame congelado 150 g

**`s6` Hummus con bastones de verdura** — 192 kcal · 8 g P · 21 g C · 8 g G · 8 g fibra  
Hummus 80 g · Zanahoria 100 g · Pepino 100 g

**`s7` Tostada de aguacate con huevo** — 242 kcal · 17 g P · 17 g C · 12 g G · 5 g fibra  
Pan integral 30 g · Aguacate 40 g · Huevo entero 50 g · Clara de huevo 60 g

**`s8` Manzana con mantequilla de maní** — 214 kcal · 6 g P · 28 g C · 10 g G · 6 g fibra  
Manzana 180 g · Mantequilla de maní 20 g

**`s9` Batido pre-gym de banana y avena** — 406 kcal · 43 g P · 49 g C · 4 g G · 5 g fibra  
Yogurt griego casero 200 g · Banana 110 g · Avena en hojuelas 20 g · Proteína en polvo 25 g

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

## 09 · Lista de compras

**Se genera sola: `python3 mercado.py` escribe `LISTA_MERCADO.md`.**

Suma los ingredientes de los 7 días del menú, resta lo que hay en `data/pantry.json` y convierte
el resto a unidades de compra. Cambias el menú o la despensa, corres el comando, y la lista queda
al día. La de esta semana son **37 líneas**, porque las recetas nuevas traen despensa nueva:
carne de soya, arroz arborio, pasta de curry rojo, leche de coco light, lentejas negras, guascas.

Esa despensa se compra una vez y rinde meses. La compra de la semana siguiente vuelve a ser corta.

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

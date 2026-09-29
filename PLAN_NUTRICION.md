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
| **Proteína** | **172 g** (1,76 g/kg) | En déficit la proteína decide si pierdes grasa o músculo. Estaba en 2,0 g/kg y bajó por una razón concreta: a 1.985 kcal, 196 g son el 39% de las calorías, y eso obliga a meterle cottage a todos los platos. El rango que conserva masa magra es 1,6–2,2 g/kg; 1,76 está de lleno adentro y le devuelve libertad a la comida. |
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
| 2 | **Chili mexicano** `l3` | Pressure cook 10 min, natural | ×4 · nevera 5 días · congela |
| 3 | **Lentejas guisadas** `l2` | Pressure cook 9 min, natural | ×4 · nevera 4 días · congela |
| 4 | **Garbanzos guisados** `l1` | Pressure cook 8 min, natural | ×4 · nevera 4 días · congela |
| 5 | **Overnight oats** `b4` | sin olla, 3 min | ×4 frascos · nevera 4 días |
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
| `b1` `b8` `b9` `b10` — pericos, omelette y arepas | Recalentados no son lo mismo. 5 a 10 min al momento |
| `b7` — calentado paisa | Al momento, pero solo existe si el domingo dejaste arroz y frijol |
| `d6` — tofu al ajillo | Pierde la costra si lo recalientas. 15 min |
| `l6` — risotto | Recalentado pierde la textura. Máximo 2 porciones |

Son los platos de 10 minutos. No todo tiene que salir del congelador.

---

## 05 · Las recetas

31 recetas con tres reglas encima:

2. **Los desayunos son de 8 minutos o menos** — huevos con arepa o tostada, avena, yogur o cereal. Nada más.
1. **Los snacks son comprados o de dos minutos** — YoPRO con granola, batido de proteína, yogur griego con berries, cottage con granola. Dulces, sin cocinar y sin nada que lavar. Un snack que hay que preparar es un snack que no te comes.
3. **Los almuerzos van en la olla y tienen sabor** — chili mexicano, tinga de garbanzos, arroz mexicano con frijoles, lasaña, pasta bolognesa, garbanzos guisados, lentejas. Lo que se cocina solo mientras haces otra cosa.

4. **Las cenas son de una sartén** — un revuelto, un omelette, un wrap, o un bowl frío sin prender nada.
5. **Todo se consigue donde tú compras en Adelaide.** La Harina PAN, las arepas de paquete y el plátano maduro sí los encuentras, así que están dentro. Las guascas y la papa criolla no, y sin guascas no hay ajiaco — por eso el sancocho de papa, camote y mazorca ocupa ese lugar en vez de una versión triste del ajiaco.

Vegetariano, sin pescado y sin tahini. Los macros salen de `data/foods.json`, no están escritos a mano.

### La proteína del bote

Tu proteína es de arveja germinada y arroz integral: **69,7 g por 100 g, no 80**, así que una
medida de 30 g son 20,9 g de proteína. Ya está corregida en `foods.json` — las recetas la
calculan con la etiqueta real.

Y trae algo que a ti te sirve más que a la mayoría: **11,9 mg de hierro por medida, el 99% del
RDI.** Con ferritina en 50, hierro sérico cayendo de 17,7 a 11,7 y una dieta vegetariana, ese
bote es una fuente de hierro, no solo de proteína. Tómalo con fruta o limón, y **no con café ni
té**, que bloquean la absorción.

*Un detalle si quieres afinar:* la síntesis de proteína muscular responde a la leucina, y el
umbral está alrededor de 2,5 g. Tu medida de 30 g trae 1,64 g; la de 45 g trae 2,46 g. En los
días de entreno, el batido de después vale la pena hacerlo de 45 g.

**Desayunos**

| ID | Receta | Cómo se cocina | kcal | P | C | G | Fibra |
|---|---|---|---|---|---|---|---|
| `b1` | Huevos pericos con arepa | Sartén | 515 | **46 g** | 40 g | 18 g | 3 g |
| `b2` | Huevos revueltos con tostada y cottage | Tostadora + Sartén | 542 | **54 g** | 33 g | 20 g | 4 g |
| `b3` | Arepa con huevo frito y queso | Sartén | 466 | **34 g** | 25 g | 26 g | 4 g |
| `b4` | Overnight oats | Sin fuego | 521 | **49 g** | 50 g | 12 g | 11 g |
| `b5` | Yogur griego con granola y berries | Sin fuego | 497 | **48 g** | 51 g | 9 g | 9 g |
| `b6` | Weet-Bix con leche y batido | Sin fuego | 478 | **37 g** | 73 g | 4 g | 11 g |
| `b7` | Calentado paisa | Sartén | 493 | **38 g** | 36 g | 20 g | 9 g |
| `b8` | Huevos duros con tostada y aguacate | Tostadora | 552 | **39 g** | 37 g | 28 g | 8 g |

**Almuerzos**

| ID | Receta | Cómo se cocina | kcal | P | C | G | Fibra |
|---|---|---|---|---|---|---|---|
| `l1` | Garbanzos guisados con arroz | **Olla** | 553 | **31 g** | 75 g | 13 g | 16 g |
| `l2` | Lentejas guisadas | **Olla** | 523 | **34 g** | 66 g | 9 g | 10 g |
| `l3` | Chili mexicano | **Olla** | 707 | **52 g** | 74 g | 20 g | 24 g |
| `l4` | Arroz mexicano con frijoles | **Olla** | 649 | **35 g** | 91 g | 15 g | 18 g |
| `l5` | Pasta con bolognesa de carne vegetal | **Olla + Estufa** | 557 | **36 g** | 64 g | 16 g | 10 g |
| `l6` | Lasaña de olla | **Olla** | 654 | **48 g** | 60 g | 23 g | 10 g |
| `l7` | Tinga de garbanzos con tortillas | **Olla + Sartén** | 633 | **35 g** | 79 g | 19 g | 20 g |

**Cenas**

| ID | Receta | Cómo se cocina | kcal | P | C | G | Fibra |
|---|---|---|---|---|---|---|---|
| `d1` | Revuelto ligero de claras con espinaca y tomate | Sartén | 390 | **49 g** | 24 g | 9 g | 6 g |
| `d2` | Bowl frío de cottage, huevo y verduras | Tostadora | 480 | **41 g** | 32 g | 21 g | 7 g |
| `d3` | Tofu al ajillo con brócoli | **Sartén + Olla** | 525 | **41 g** | 35 g | 23 g | 10 g |
| `d4` | Shakshuka | Sartén + Tostadora | 545 | **47 g** | 41 g | 20 g | 8 g |
| `d5` | Wrap de carne vegetal con ensalada | Sartén | 578 | **43 g** | 51 g | 21 g | 12 g |
| `d6` | Omelette de tres huevos con queso | Sartén + Tostadora | 451 | **46 g** | 19 g | 20 g | 5 g |

**Snacks**

| ID | Receta | Cómo se cocina | kcal | P | C | G | Fibra |
|---|---|---|---|---|---|---|---|
| `s1` | YoPRO con granola | Sin fuego | 264 | **19 g** | 34 g | 5 g | 5 g |
| `s2` | Batido de proteína con berries | Licuadora | 192 | **22 g** | 18 g | 3 g | 8 g |
| `s3` | Yogur griego con proteína y berries | Sin fuego | 283 | **39 g** | 22 g | 3 g | 5 g |
| `s4` | YoPRO solo | Sin fuego | 99 | **15 g** | 8 g | 0 g | 0 g |
| `s5` | Cottage con granola y canela | Sin fuego | 322 | **28 g** | 30 g | 9 g | 4 g |
| `s6` | Banana con mantequilla de maní | Sin fuego | 227 | **6 g** | 30 g | 10 g | 4 g |
| `s7` | Batido pre-gym de banana y avena | Licuadora | 423 | **44 g** | 50 g | 5 g | 7 g |

### La regla que resume todo

**~50 g de proteína por comida, cuatro veces al día.** Todo lo demás es detalle.

---

## 06 · La semana verificada

Cada día está armado y comprobado contra los objetivos, no estimado a ojo.

| Día | | Menú | kcal | P | C | G | Fibra |
|---|---|---|---|---|---|---|---|
| **Lunes** | entreno | Overnight oats · Tinga de garbanzos con tortillas · YoPRO solo · Cottage con granola y canela · Omelette de tres huevos con queso | 2026 | **173** | 186 | 60 | 40 |
| **Martes** | entreno | Arepa con huevo frito y queso · Lentejas guisadas · Batido de proteína con berries · Yogur griego con proteína y berries · Wrap de carne vegetal con ensalada | 2042 | **172** | 182 | 62 | 39 |
| **Miércoles** | descanso | Yogur griego con granola y berries · Lasaña de olla · Batido de proteína con berries · YoPRO solo · Tofu al ajillo con brócoli | 1967 | **174** | 172 | 58 | 37 |
| **Jueves** | entreno | Overnight oats · Pasta con bolognesa de carne vegetal · YoPRO con granola · Batido de proteína con berries · Omelette de tres huevos con queso | 1985 | **172** | 185 | 56 | 39 |
| **Viernes** | entreno | Huevos revueltos con tostada y cottage · Lentejas guisadas · YoPRO con granola · Batido de proteína con berries · Wrap de carne vegetal con ensalada | 2099 | **172** | 202 | 58 | 39 |
| **Sábado** | descanso | Huevos pericos con arepa · Tinga de garbanzos con tortillas · Yogur griego con proteína y berries · YoPRO solo · Tofu al ajillo con brócoli | 2055 | **176** | 184 | 63 | 38 |
| **Domingo** | descanso | Huevos duros con tostada y aguacate · Chili mexicano · YoPRO con granola · YoPRO solo · Revuelto ligero de claras con espinaca y tomate | 2012 | **174** | 177 | 62 | 43 |
| | | **Promedio diario** | **2026** | **173** | 184 | 59 | 39 |

Promedio real: **2.026 kcal · 173 g de proteína · 59 g de grasa · 39 g de fibra.**
Déficit de 792 kcal/día → **0,72 kg/semana.**

*El sábado y el domingo corren unas 150–200 kcal por encima: los frijoles paisas y el calentado
son platos grandes y no tiene sentido encogerlos hasta que dejen de ser ellos. La semana
aguanta, y el costo son 10 gramos por semana.*

*Las recetas nuevas cuestan 0,04 kg por semana contra las anteriores. Es el precio de comer
dal makhani y ajiaco en vez de cottage con tomate, y vale la pena: el plan que no sigues no
adelgaza nada.*

### Detalle de cada receta

### Desayunos

**`b1` Huevos pericos con arepa** — Sartén  
515 kcal · 46 g P · 40 g C · 18 g G · 3 g fibra

Huevo entero 150 g · Clara de huevo 120 g · Tomate 95 g · Cebolla larga 30 g · Arepa casera (Harina PAN) 40 g · Cottage alto en proteína 75 g

*Condimentos:* Sal 1 g (1 pizca) · Comino molido 1 g (½ cdta) · Espray de aceite 1 g (2 segundos)

1. **Sin fuego** — Masa: 40 g de Harina PAN por 60 ml de agua tibia con sal. Amasa y deja reposar 5 min.
2. **Sartén** — Sartén seca a fuego medio: la arepa 4 min por lado. Suena hueca cuando está.
3. **Sartén** — Misma sartén, fuego bajo con espray: tomate y cebolla larga 3 min.
4. **Sartén** — Huevos y claras batidos, revuelve 3 min. Apaga cuando aún se vean húmedos.
5. **Sin fuego** — Cottage al lado.

**`b2` Huevos revueltos con tostada y cottage** — Tostadora + Sartén  
542 kcal · 54 g P · 33 g C · 20 g G · 4 g fibra

Huevo entero 150 g · Clara de huevo 150 g · Tostada integral 60 g · Cottage alto en proteína 95 g · Tomate 75 g

*Condimentos:* Sal 1 g (1 pizca) · Pimienta negra 0.5 g (al gusto) · Espray de aceite 1 g (2 segundos)

1. **Tostadora** — El pan al tostador.
2. **Sartén** — Sartén a fuego bajo con espray: huevos y claras batidos, revuelve constante 3 min.
3. **Sartén** — Apaga cuando aún se vean húmedos: se terminan de cuajar solos.
4. **Sin fuego** — Sobre la tostada, con el cottage y el tomate en rodajas al lado.

**`b3` Arepa con huevo frito y queso** — Sartén  
466 kcal · 34 g P · 25 g C · 26 g G · 4 g fibra

Arepa Sary con queso 60 g · Huevo entero 100 g · Clara de huevo 90 g · Queso cheddar light 25 g · Aguacate 40 g

*Condimentos:* Sal 1 g (1 pizca) · Espray de aceite 1 g (2 segundos)

1. **Sartén** — La arepa de paquete directo a la sartén seca, 2 min por lado.
2. **Sartén** — Espray, el huevo frito con la yema blanda y las claras vertidas alrededor.
3. **Sin fuego** — Queso rallado encima del huevo caliente para que se derrita, aguacate al lado.

**`b4` Overnight oats** — Sin fuego  
521 kcal · 49 g P · 50 g C · 12 g G · 11 g fibra

Avena en hojuelas 45 g · Yogurt griego casero 190 g · Proteína en polvo 30 g · Berries congelados 95 g · Mantequilla de maní 10 g

*Condimentos:* Canela 1 g (½ cdta)

1. **Nevera** — En un frasco la noche antes: avena, yogurt, proteína, mantequilla de maní y canela. Revuelve bien.
2. **Nevera** — Tapa y a la nevera, mínimo 6 horas.
3. **Sin fuego** — Berries encima en la mañana. Cero cocina.

**`b5` Yogur griego con granola y berries** — Sin fuego  
497 kcal · 48 g P · 51 g C · 9 g G · 9 g fibra

Yogurt griego casero 260 g · Proteína en polvo 25 g · Granola 40 g · Berries congelados 95 g

*Condimentos:* Canela 1 g (½ cdta)

1. **Sin fuego** — Yogurt y proteína, revuelve hasta que quede liso.
2. **Sin fuego** — Berries encima y la granola de última, o se ablanda. Dos minutos.

**`b6` Weet-Bix con leche y batido** — Sin fuego  
478 kcal · 37 g P · 73 g C · 4 g G · 11 g fibra

Weet-Bix 55 g · Leche descremada 240 g · Proteína en polvo 30 g · Banana 95 g

*Condimentos:* Canela 1 g (½ cdta)

1. **Sin fuego** — Weet-Bix con la leche fría y la banana en rodajas.
2. **Sin fuego** — El batido aparte: proteína en 300 ml de agua. El cereal solo te deja en 12 g de proteína; el batido es lo que lo salva.

**`b7` Calentado paisa** — Sartén  
493 kcal · 38 g P · 36 g C · 20 g G · 9 g fibra

Huevo entero 150 g · Clara de huevo 90 g · Arroz basmati crudo 20 g · Frijol rojo de lata 95 g · Cebolla larga 30 g · Aguacate 30 g

*Condimentos:* Sal 1 g (1 pizca) · Comino molido 1 g (½ cdta) · Espray de aceite 1 g (2 segundos)

1. **Sartén** — Sartén caliente con espray: arroz y frijol del domingo juntos, 4 min sin moverlos hasta que el arroz tome color.
2. **Sartén** — Cebolla larga, comino y sal, 2 min.
3. **Sartén** — Al plato. En la misma sartén el huevo frito con la yema blanda y las claras alrededor.
4. **Sin fuego** — Aguacate al lado.

**`b8` Huevos duros con tostada y aguacate** — Tostadora  
552 kcal · 39 g P · 37 g C · 28 g G · 8 g fibra

Huevo entero 150 g · Tostada integral 60 g · Aguacate 55 g · Cottage alto en proteína 95 g · Tomate 75 g

*Condimentos:* Sal 1 g (1 pizca) · Pimienta negra 0.5 g (al gusto) · Limón 5 g (unas gotas)

1. **Nevera** — Los huevos ya están: salieron de la olla el domingo. Pélalos.
2. **Tostadora** — El pan al tostador.
3. **Sin fuego** — Aguacate machacado con sal, limón y pimienta sobre la tostada. Tomate y cottage al lado.

### Almuerzos

**`l1` Garbanzos guisados con arroz** — Olla  
553 kcal · 31 g P · 75 g C · 13 g G · 16 g fibra

Garbanzos de lata 190 g · Passata de tomate 120 g · Cebolla 65 g · Pimentón 65 g · Arroz basmati crudo 30 g · Caldo Campbell's 40 g · Cottage alto en proteína 95 g · Aceite de oliva 5 g

*Condimentos:* Ajo 6 g (2 dientes) · Comino molido 2 g (1 cdta) · Paprika 2 g (1 cdta) · Laurel 0.2 g (1 hoja) · Sal 2 g (1 cdta) · Cilantro fresco 5 g (1 puñado)

1. **Olla** — OLLA en Sauté/sear high con el aceite: cebolla y pimentón picados, 6 min.
2. **Olla** — Ajo, comino y paprika, 45 segundos. Passata y laurel, 3 min.
3. **Olla** — Garbanzos escurridos y 100 ml de agua. Machaca un tercio con el tenedor: espesa sin harina.
4. **Olla** — Tapa. Pressure cook 8 min. Cuando termine NO sueltes la presión: espera a que baje sola.
5. **Olla** — El arroz aparte: 1 taza de arroz por 1¼ de caldo, Pressure cook 5 min.
6. **Sin fuego** — Cottage y cilantro al servir.

**`l2` Lentejas guisadas** — Olla  
523 kcal · 34 g P · 66 g C · 9 g G · 10 g fibra

Lentejas cafés secas 55 g · Passata de tomate 100 g · Cebolla 55 g · Zanahoria 55 g · Caldo Campbell's 280 g · Arroz basmati crudo 25 g · Cottage alto en proteína 120 g · Aceite de oliva 5 g

*Condimentos:* Ajo 6 g (2 dientes) · Comino molido 2 g (1 cdta) · Color / achiote 2 g (1 cdta) · Laurel 0.2 g (1 hoja) · Sal 2 g (1 cdta)

1. **Olla** — OLLA en Sauté/sear high con el aceite: cebolla y zanahoria en cubos, 6 min.
2. **Olla** — Ajo, comino y color, 45 segundos. Passata 3 min.
3. **Olla** — Lentejas, caldo y laurel. Pressure cook 9 min, deja que la presión baje sola.
4. **Olla** — Arroz aparte, Pressure cook 5 min.
5. **Sin fuego** — Cottage batido al servir.

**`l3` Chili mexicano** — Olla  
707 kcal · 52 g P · 74 g C · 20 g G · 24 g fibra

Carne vegetal molida 120 g · Frijol rojo de lata 120 g · Frijoles negros de lata 80 g · Passata de tomate 140 g · Pimentón 80 g · Cebolla 55 g · Maíz tierno 50 g · Cottage alto en proteína 95 g · Aguacate 30 g · Aceite de oliva 5 g

*Condimentos:* Ajo 6 g (2 dientes) · Comino molido 3 g (1½ cdta) · Paprika ahumada 2 g (1 cdta) · Chili en polvo 2 g (1 cdta) · Orégano seco 1 g (½ cdta) · Sal 2 g (1 cdta) · Cilantro fresco 5 g (1 puñado) · Limón 10 g (½ limón)

1. **Olla** — OLLA en Sauté/sear high con el aceite: la carne vegetal 5 min sin moverla mucho, hasta que tueste.
2. **Olla** — Cebolla y pimentón 5 min. Ajo, comino, paprika ahumada, chili y orégano, 45 segundos.
3. **Olla** — Passata, los frijoles escurridos y el maíz. Pressure cook 10 min, la presión baja sola.
4. **Sin fuego** — Cottage, aguacate, cilantro y limón al servir.

**`l4` Arroz mexicano con frijoles** — Olla  
649 kcal · 35 g P · 91 g C · 15 g G · 18 g fibra

Arroz basmati crudo 45 g · Frijoles negros de lata 140 g · Passata de tomate 95 g · Caldo Campbell's 140 g · Pimentón 65 g · Cebolla 50 g · Maíz tierno 50 g · Cottage alto en proteína 120 g · Aguacate 30 g · Limón 10 g · Aceite de oliva 5 g

*Condimentos:* Ajo 6 g (2 dientes) · Comino molido 2 g (1 cdta) · Paprika 2 g (1 cdta) · Sal 2 g (1 cdta) · Cilantro fresco 5 g (1 puñado)

1. **Olla** — OLLA en Sauté/sear high con el aceite: cebolla y pimentón 5 min. Ajo, comino y paprika, 45 s.
2. **Olla** — El arroz 1 min, hasta que los granos se vean vidriosos. Passata y caldo (1 taza de arroz por 1¼ de líquido).
3. **Olla** — El maíz encima SIN revolver. Pressure cook 5 min, la presión baja sola 10 min.
4. **Olla** — Suelta con tenedor. Los frijoles escurridos por encima, con el calor que queda.
5. **Sin fuego** — Cottage, aguacate, cilantro y limón. Un plato, una olla.

**`l5` Pasta con bolognesa de carne vegetal** — Olla + Estufa  
557 kcal · 36 g P · 64 g C · 16 g G · 10 g fibra

Carne vegetal molida 120 g · Pasta cruda 50 g · Passata de tomate 160 g · Pasta de tomate 25 g · Cebolla 50 g · Zanahoria 40 g · Parmesano 15 g · Aceite de oliva 5 g

*Condimentos:* Ajo 3 g (1 diente) · Laurel 0.2 g (1 hoja) · Orégano seco 1 g (½ cdta) · Sal 3 g (1½ cdta, la pasta también se sala) · Pimienta negra 0.5 g (al gusto)

1. **Olla** — OLLA en Sauté/sear high con el aceite: cebolla y zanahoria picadas finas, 6 min.
2. **Olla** — La carne vegetal 5 min hasta que tueste. La pasta de tomate 2 min: tostarla da el color oscuro.
3. **Olla** — Passata, laurel y orégano. Pressure cook 10 min, la presión baja sola.
4. **Estufa** — La pasta aparte en agua hirviendo con sal, al dente.
5. **Sin fuego** — Parmesano rallado al final.

**`l6` Lasaña de olla** — Olla  
654 kcal · 48 g P · 60 g C · 23 g G · 10 g fibra

Carne vegetal molida 120 g · Pasta cruda 45 g · Passata de tomate 180 g · Ricotta light 80 g · Mozzarella light 30 g · Cebolla 50 g · Espinaca 80 g · Aceite de oliva 5 g

*Condimentos:* Ajo 6 g (2 dientes) · Orégano seco 2 g (1 cdta) · Sal 2 g (1 cdta) · Pimienta negra 0.5 g (al gusto)

1. **Olla** — OLLA en Sauté/sear high con el aceite: cebolla 4 min, la carne vegetal 5 min hasta que tueste.
2. **Olla** — Ajo y orégano 45 s, passata 5 min. Saca la mitad de la salsa y resérvala.
3. **Olla** — Arma por capas dentro de la olla: salsa, láminas de pasta partidas para que quepan, ricotta y espinaca. Repite.
4. **Olla** — Mozzarella encima. Bake 30 min. La pasta se cuece en la salsa: no hay que hervirla antes.
5. **Sin fuego** — Deja reposar 10 min antes de servir o se desarma.

**`l7` Tinga de garbanzos con tortillas** — Olla + Sartén  
633 kcal · 35 g P · 79 g C · 19 g G · 20 g fibra

Garbanzos de lata 190 g · Passata de tomate 120 g · Cebolla 70 g · Tortilla de maíz 60 g · Cottage alto en proteína 120 g · Aguacate 30 g · Limón 10 g · Aceite de oliva 5 g

*Condimentos:* Ajo 6 g (2 dientes) · Comino molido 2 g (1 cdta) · Paprika ahumada 3 g (1½ cdta) · Orégano seco 1 g (½ cdta) · Sal 2 g (1 cdta) · Cilantro fresco 5 g (1 puñado)

1. **Olla** — OLLA en Sauté/sear high con el aceite: cebolla en pluma 6 min, hasta que dore.
2. **Olla** — Ajo, comino, paprika ahumada y orégano, 45 s. Esa paprika es la que hace la tinga.
3. **Olla** — Passata y garbanzos escurridos. Pressure cook 8 min, la presión baja sola.
4. **Olla** — Machaca un tercio para espesar.
5. **Sartén** — Las tortillas 30 segundos por lado en sartén seca.
6. **Sin fuego** — Arma los tacos: garbanzos, cottage, aguacate, cilantro y limón.

### Cenas

**`d1` Revuelto ligero de claras con espinaca y tomate** — Sartén  
390 kcal · 49 g P · 24 g C · 9 g G · 6 g fibra

Clara de huevo 210 g · Huevo entero 50 g · Espinaca 130 g · Tomate 130 g · Cottage alto en proteína 90 g · Tostada integral 30 g

*Condimentos:* Sal 1 g (1 pizca) · Pimienta negra 0.5 g (al gusto) · Ajo 3 g (1 diente picado) · Espray de aceite 1 g (2 segundos)

1. **Sartén** — Sartén a fuego medio con espray: tomate y ajo, 3 min.
2. **Sartén** — Espinaca 1 min. Escurre lo que suelte o queda aguado.
3. **Sartén** — Fuego bajo. Claras y el huevo batidos, revuelve constante 3 min.
4. **Sartén** — Apaga cuando aún se vean húmedos.
5. **Sin fuego** — Cottage encima. Una tostada seca al lado.

**`d2` Bowl frío de cottage, huevo y verduras** — Tostadora  
480 kcal · 41 g P · 32 g C · 21 g G · 7 g fibra

Cottage alto en proteína 180 g · Huevo entero 100 g · Tomate 130 g · Pepino 110 g · Aguacate 35 g · Tostada integral 30 g · Limón 15 g

*Condimentos:* Sal 1 g (1 pizca) · Pimienta negra 0.5 g (al gusto) · Orégano seco 1 g (½ cdta)

1. **Nevera** — Los huevos duros ya están del domingo. Pélalos y pártelos.
2. **Sin fuego** — Tomate y pepino en cubos, aguacate en tajadas.
3. **Sin fuego** — Todo en un bowl con el cottage, limón, sal, pimienta y orégano.
4. **Tostadora** — Una tostada al lado. Cinco minutos y no se prende nada.

**`d3` Tofu al ajillo con brócoli** — Sartén + Olla  
525 kcal · 41 g P · 35 g C · 23 g G · 10 g fibra

Tofu firme 190 g · Brócoli 180 g · Champiñones 110 g · Cebolla larga 35 g · Salsa de soya 20 g · Arroz basmati crudo 25 g · Aceite de oliva 5 g

*Condimentos:* Ajo 12 g (4 dientes laminados) · Chili en hojuelas 1 g (½ cdta) · Sal 1 g (1 pizca)

1. **Sartén** — Tofu en lonjas, apretado con papel 2 min. Sartén MUY caliente con el aceite, 4 min por lado sin tocarlo.
2. **Sartén** — Sácalo. Champiñones 4 min sin sal, brócoli 4 min.
3. **Sartén** — Ajo laminado AL FINAL, 1 min: al principio se quema y amarga.
4. **Sartén** — Devuelve el tofu, salsa de soya, chili y cebolla larga.
5. **Olla** — Arroz aparte en la olla, Pressure cook 5 min.

**`d4` Shakshuka** — Sartén + Tostadora  
545 kcal · 47 g P · 41 g C · 20 g G · 8 g fibra

Huevo entero 100 g · Clara de huevo 120 g · Passata de tomate 180 g · Pimentón 110 g · Cebolla 60 g · Cottage alto en proteína 110 g · Tostada integral 30 g · Aceite de oliva 5 g

*Condimentos:* Comino molido 2 g (1 cdta) · Paprika ahumada 2 g (1 cdta) · Chili en polvo 1 g (½ cdta) · Sal 2 g (1 cdta) · Pimienta negra 0.5 g (al gusto)

1. **Sartén** — Sartén amplia con el aceite: cebolla y pimentón en tiras, 6 min.
2. **Sartén** — Comino, paprika ahumada y chili, 30 s. Ese tostado es toda la receta.
3. **Sartén** — Passata, 8 min a fuego bajo hasta que espese de verdad.
4. **Sartén** — Huecos con la cuchara, casca los huevos dentro y las claras alrededor. TAPA 5 min.
5. **Tostadora** — Tostada para mojar. Cottage encima fuera del fuego.

**`d5` Wrap de carne vegetal con ensalada** — Sartén  
578 kcal · 43 g P · 51 g C · 21 g G · 12 g fibra

Carne vegetal molida 130 g · Wrap Mission wholegrain 71 g · Espinaca 70 g · Tomate 90 g · Cottage alto en proteína 90 g · Aguacate 25 g · Limón 15 g · Aceite de oliva 5 g

*Condimentos:* Ajo 3 g (1 diente) · Comino molido 2 g (1 cdta) · Paprika ahumada 2 g (1 cdta) · Sal 1 g (1 pizca)

1. **Sartén** — Sartén caliente con el aceite: la carne vegetal 6 min sin moverla mucho, con comino, paprika y ajo.
2. **Sartén** — El wrap 20 segundos por lado en la sartén seca: se dobla sin romperse.
3. **Sin fuego** — Rellena con la carne, espinaca, tomate, cottage y aguacate. Limón y enrolla apretado.

**`d6` Omelette de tres huevos con queso** — Sartén + Tostadora  
451 kcal · 46 g P · 19 g C · 20 g G · 5 g fibra

Huevo entero 150 g · Clara de huevo 120 g · Espinaca 90 g · Tomate 90 g · Queso cheddar light 25 g · Tostada integral 30 g

*Condimentos:* Sal 1 g (1 pizca) · Pimienta negra 0.5 g (al gusto) · Espray de aceite 1 g (2 segundos)

1. **Sartén** — Sartén a fuego medio con espray: tomate 2 min, espinaca 1 min. Escurre y saca.
2. **Sartén** — Fuego bajo. Huevos y claras batidos, 2 min SIN tocar hasta que cuaje el fondo.
3. **Sartén** — El relleno y el queso sobre una mitad, dobla, 1 min más.
4. **Tostadora** — Tostada al lado.

### Snacks

**`s1` YoPRO con granola** — Sin fuego  
264 kcal · 19 g P · 34 g C · 5 g G · 5 g fibra

YoPRO 160 g · Granola 30 g · Berries congelados 60 g

1. **Sin fuego** — Abre el YoPRO, granola y berries encima. Un minuto y nada que lavar.

**`s2` Batido de proteína con berries** — Licuadora  
192 kcal · 22 g P · 18 g C · 3 g G · 8 g fibra

Proteína en polvo 30 g · Berries congelados 150 g

1. **Licuadora** — Proteína en 300 ml de agua fría con los berries congelados. Agita o licúa.
2. **Sin fuego** — 21 g de proteína y el 99% del hierro del día. No con café ni té: bloquean el hierro.

**`s3` Yogur griego con proteína y berries** — Sin fuego  
283 kcal · 39 g P · 22 g C · 3 g G · 5 g fibra

Yogurt griego casero 250 g · Proteína en polvo 20 g · Berries congelados 80 g

*Condimentos:* Canela 1 g (½ cdta) · Whole Earth 3 g (al gusto)

1. **Sin fuego** — Yogurt y proteína, revuelve. Berries y canela encima.

**`s4` YoPRO solo** — Sin fuego  
99 kcal · 15 g P · 8 g C · 0 g G · 0 g fibra

YoPRO 160 g

1. **Sin fuego** — Un YoPRO del refrigerador, directo. 15 g de proteína, cero azúcar añadido y nada que lavar.

**`s5` Cottage con granola y canela** — Sin fuego  
322 kcal · 28 g P · 30 g C · 9 g G · 4 g fibra

Cottage alto en proteína 200 g · Granola 25 g · Berries congelados 60 g

*Condimentos:* Canela 1 g (½ cdta) · Whole Earth 3 g (al gusto)

1. **Sin fuego** — Cottage en un bowl, granola y berries encima, canela. Dulce y 26 g de proteína.

**`s6` Banana con mantequilla de maní** — Sin fuego  
227 kcal · 6 g P · 30 g C · 10 g G · 4 g fibra

Banana 120 g · Mantequilla de maní 20 g

*Condimentos:* Canela 1 g (½ cdta)

1. **Sin fuego** — Banana en rodajas con 20 g de mantequilla de maní. PÉSALOS: la cucharada a ojo son 35-40 g.

**`s7` Batido pre-gym de banana y avena** — Licuadora  
423 kcal · 44 g P · 50 g C · 5 g G · 7 g fibra

Yogurt griego casero 200 g · Banana 110 g · Avena en hojuelas 20 g · Proteína en polvo 30 g

*Condimentos:* Canela 1 g (½ cdta)

1. **Licuadora** — Yogurt griego, banana, avena y proteína en polvo a la licuadora con 150 ml de agua y hielo.
2. **Sin fuego** — Tómalo 60-90 min antes de entrenar.

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

Cada línea trae **el producto de Coles**: marca, tamaño de empaque y en qué pasillo buscarlo.
Donde no hay una marca que valga la pena, va la propia de Coles, que es la más barata y sirve
igual. Dos advertencias: los nombres y tamaños cambian cada temporada, así que guíate por la
descripción; y el tofu Macro que ya tienes es marca de **Woolworths**, no de Coles — el
equivalente allá es el Coles Firm Tofu.

Suma los ingredientes de los 7 días del menú, resta lo que hay en `data/pantry.json` y convierte
el resto a unidades de compra. Cambias el menú o la despensa, corres el comando, y la lista queda
al día. La de esta semana son **30 líneas**, porque las recetas traen despensa nueva: carne vegetal
molida, arroz arborio, pasta de curry rojo, leche de coco light, passata, tempeh.

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

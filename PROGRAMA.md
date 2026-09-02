# Programa de Camilo — Nutrición, Entreno y Seguimiento

**Punto de partida:** 96.0 kg · 1.79 m · IMC 30.0 · 32 años · vegetariano (huevo y lácteos)
**Meta:** 80 kg (IMC 25.0) · **Fecha del plan:** 2 de septiembre de 2026

---

## 1. Lo primero, porque no es negociable

Tus análisis del 9 de julio de 2026 traen una bandera que reordena todo el plan:

**ALT 68 U/L** (rango 5–40). En mayo de 2025 estaba en 28. Se te más que duplicó en 14 meses.
El GGT lo acompañó: de 32 a 47. El laboratorio escribió textual:

> *"non-specific hepatic impairment. Possible causes... alcohol effect and viral infections.
> Repeat LFTs in one [month] to assess chronicity of abnormality."*

**Tres cosas concretas:**

1. **Pide la cita para repetir las pruebas de función hepática.** El laboratorio ya lo indicó.
   No es una sugerencia mía, es una instrucción que ya está en tu papel.
2. **Alcohol en cero hasta el reexamen.** Vi botellas en la despensa. No es un juicio moral:
   el laboratorio nombró el alcohol como causa posible, y si quitas la variable antes del
   reexamen, el resultado se vuelve interpretable. Si sigues bebiendo y el ALT sigue alto,
   no vas a saber por qué.
3. **Perder 7–10% del peso es la intervención con más evidencia que existe para hígado
   graso.** De 96 kg son 7 a 10 kg. Eso es exactamente lo que este plan hace en 10–14 semanas.

Yo no soy tu médico y esto no es un diagnóstico. Lo que hice fue transcribir tus números,
ordenarlos, y diseñar el plan alrededor de ellos. Las preguntas para Dr Brenton Martin están
en `data/labs.json` y salen con `/labs preguntas`.

### El resto de tus números

| Marcador | Antes | Ahora | Referencia | Lectura |
|---|---|---|---|---|
| **ALT** | 28 | **68** | 5–40 | 🔴 Alto. Prioridad 1. |
| **LDL** | 3.5 | **3.4** | <2.5 | 🔴 Alto y estancado 14 meses. |
| **Creatinina** | 79 | **56** | 60–110 | 🟡 Baja. eGFR >90: el riñón está perfecto. Típico en vegetarianos. |
| **Ferritina** | 17 | **50** | 30–400 | 🟡 Subió bien, pero el hierro sérico bajó de 17.7 a 11.7. Vigilar. |
| Glucosa ayunas | — | 4.7 | 3.6–5.4 | ✅ Excelente. |
| Triglicéridos | 0.7 | 0.8 | <1.5 | ✅ Muy bueno. TG/HDL = 0.57. |
| TSH | 2.0 | 1.2 | 0.40–3.50 | ✅ Tiroides normal. |
| Vitamina D | 93 | 88 | 50–160 | ✅ Sin deficiencia. |
| Vitamina B12 | 265 | 319 | 130–855 | ✅ Homocisteína 6.6 → reservas repletas. |
| Hemograma | — | — | — | ✅ *"Results normal."* |

**En una frase:** tu metabolismo está sano — glucosa 4.7, triglicéridos 0.8, TSH 1.2 significan
que **no tienes ninguna excusa fisiológica**, el déficit va a funcionar. Pero tu hígado levantó
la mano y tu LDL sigue alto. Las dos cosas responden a lo mismo: perder grasa, comer fibra,
parar el alcohol.

---

## 2. Tus números de energía

Mifflin-St Jeor con tus datos reales:

```
BMR  = 10(96) + 6.25(179) − 5(32) + 5     = 1.924 kcal
TDEE = 1.924 × 1.45 (4 entrenos + 9k pasos) = 2.789 kcal
Objetivo = TDEE − 28%                      = 2.008 kcal
Déficit                                    = −781 kcal/día
```

### Carbohidratos ciclados

La proteína y la grasa se quedan fijas todos los días. Solo se mueven los carbohidratos: suben
el día que entrenas, bajan el día que descansas. Es lo más fácil de seguir y lo mejor para
rendir en el garage.

| | Calorías | Proteína | Carbos | Grasa | Fibra |
|---|---|---|---|---|---|
| **Día de entreno** (L, Ma, J, V) | **2.150** | 182 g | 225 g | 58 g | 35 g+ |
| **Día de descanso** (Mi, Sa, D) | **1.822** | 182 g | 143 g | 58 g | 35 g+ |
| *Promedio semanal* | *2.008* | | | | |

**Por qué estos números:**

- **Proteína 182 g (1.9 g/kg).** En déficit la proteína alta es lo que decide si pierdes grasa
  o pierdes músculo. Siendo vegetariano necesitas apuntar más alto que un omnívoro, porque la
  proteína vegetal tiene menos leucina por gramo.
- **Grasa 58 g (0.6 g/kg).** Es el piso que protege la producción hormonal. No bajes de aquí.
- **Fibra 35–40 g.** Es el doble del promedio australiano, y no es casualidad: la fibra soluble
  baja el LDL de forma medible. Con tu LDL en 3.4 esto es tratamiento, no adorno.
- **Carbos al resto.** Van donde generan rendimiento: los días de barra.

### Ritmo esperado y línea de tiempo

| Fecha | Peso | Hito |
|---|---|---|
| Semanas 1–2 | 96 → 92–93 kg | La bajada rápida es agua y glucógeno, no grasa. **No te emociones.** |
| ~Semana 8 (finales de oct.) | 90 kg | ~6% perdido. Aquí el ALT ya debería estar respondiendo. |
| ~Semana 12 (finales de nov.) | 88 kg | **8% perdido: el umbral de evidencia para hígado graso.** |
| ~Semana 20 (finales de ene. 2027) | 84 kg | IMC 26.2 |
| ~Semana 25 (marzo 2027) | 80 kg | **IMC 25.0. Meta.** |

Ritmo sostenido: **0.7 kg/semana.** Si bajas más de 1.2 kg/semana de forma sostenida, estás
perdiendo músculo y hay que subir calorías. El bot te avisa cuando pasa.

---

## 3. La comida

Todo está construido con lo que **ya tienes** en la nevera, el congelador y la despensa. Nada
de comprar cosas raras.

### Tus proteínas disponibles, ordenadas por eficiencia

| Alimento | Proteína/100 kcal | Por qué importa |
|---|---|---|
| Claras de huevo | 21 g | El rey absoluto. Tienes 60+ huevos. |
| Cottage cheese Bulla | 12.8 g | Tu caballo de batalla. Dos tarros. |
| YoPRO pouch | 14.5 g | Snack de emergencia, cero azúcar añadido. |
| Yogurt griego Lyttos | 10.8 g | Base de desayunos y salsas. |
| Tofu firme Nature's Kitchen | 11.1 g | 500 g en la nevera. |
| Quorn chicken pieces | 13.8 g | Dos bolsas. |
| Tiras vegetales Nature's Kitchen | 14.5 g | Dos paquetes. |
| Huevo entero | 8.8 g | |

### Las 27 recetas

Están en `data/recipes.json` y salen del bot con `/receta <id>`. **Los macros no están escritos
a mano en ningún lado:** el bot los calcula desde los gramos de cada ingrediente y la base de
`data/foods.json`. Cambias un gramaje y el macro se recalcula solo.

**Desayunos (6):** huevos rancheros con Tajín · bowl de yogurt griego · overnight oats
proteicos · overnight oats con leche de almendra y berries · batido pre-gym · scramble de tofu

**Almuerzos (6):** Quorn al curry con basmati · pasta GF con tiras vegetales · bowl mexicano de
frijol y maíz · ensalada tibia de papa y huevo · wrap de tofu al curry · burrito bowl de frijol
refrito

**Cenas (6):** pizza proteica en media base · curry marroquí de garbanzos · revuelto grande de
espinaca y cottage (58 g de proteína) · salteado asiático · tofu a la plancha con arroz al
caldo · pasta GF con Dolmio y tofu desmenuzado

**Snacks (9):** cottage con Tajín · YoPRO · pera con nueces · huevos duros · batido de whey ·
**palomitas caseras con Tajín (94 kcal por un bowl gigante)** · chocolate 85% con berries ·
pera con mantequilla de maní

### Cinco trucos que van a hacer la diferencia

1. **Pesa la mantequilla de maní.** Es el error de conteo más común de toda tu despensa. La
   "cucharada" a ojo son 35–40 g y ahí se te van 130 kcal fantasma cada vez.
2. **Cocina el arroz con el Campbell's Real Stock en vez de agua.** Cero calorías extra, el
   doble de sabor. Es la mejora más barata de tu cocina.
3. **Limón sobre la espinaca y los frijoles, siempre.** La vitamina C triplica la absorción del
   hierro vegetal. Con tu ferritina en 50 y siendo vegetariano, esto no es decoración.
4. **Aprieta el tofu antes de cocinarlo.** Dos minutos con papel de cocina. Es la diferencia
   entre dorado y aguado, y explica por qué la mayoría cree que no le gusta el tofu.
5. **Las palomitas sin aceite son tu arma secreta.** 25 g de granos = 94 kcal = un bowl enorme.
   Cuando el hambre es de masticar y no de comer, esto la apaga sin costo.

### Lo que vale la pena comprar

| Qué | Por qué |
|---|---|
| **Creatina monohidrato** | 5 g/día. Tu creatinina salió baja (56) y eres vegetariano: partes de reservas bajas, que es justo el perfil que más responde. Décadas de evidencia de seguridad. **Avísale a tu médico:** sube la creatinina medida sin que nada esté mal. |
| **Proteína en polvo** | Llegar a 182 g siendo vegetariano con comida sola es posible pero apretado. 1–2 scoops es el atajo honesto. |
| Edamame congelado | 12 g de proteína/100 g y se hace en 4 minutos. |
| Lentejas secas | Fibra soluble barata, directo al LDL. |

### Lo que hay en casa y conviene mover al fondo del estante

- **Kellogg's Nutri-Grain** — 22 g de azúcar por 100 g. Ocasional, no diario.
- **Alcohol** — cero hasta el reexamen hepático. Ver sección 1.
- **Bases de pizza** — usa media, no una entera. La receta `d1` ya está calculada así.

---

## 4. El entreno

### Tu gym

De las fotos: **power rack con barra de dominadas, barra olímpica con seguros, discos, banco
ajustable, mancuernas de rosca, barra Z, bandas elásticas, foam rollers y caminadora.**

**No tienes:** poleas, jalón al pecho, prensa, curl femoral, peck deck, dominadas asistidas.

Ni un solo ejercicio del programa depende de una máquina que no tengas. Y tener el gym en el
garage te quita la excusa más común que existe: el traslado.

### Upper / Lower × 2 — 4 días

| Día | Sesión | Series |
|---|---|---|
| Lunes | **Upper A** — horizontal, fuerza | 23 |
| Martes | **Lower A** — sentadilla | 20 |
| Miércoles | Caminadora 45 min zona 2, inclinación 5–8% | — |
| Jueves | **Upper B** — vertical, hipertrofia | 23 |
| Viernes | **Lower B** — bisagra de cadera | 18 |
| Sábado | Caminata larga afuera, 60 min | — |
| Domingo | Descanso total | — |

**84 series semanales.** Sale del bot con `/gym`. Cada ejercicio trae alternativas.

### La regla que más importa

**En déficit no se busca subir peso en la barra. Se busca MANTENERLO.**

Si sostienes los mismos kilos mientras bajas de peso corporal, tu fuerza relativa está subiendo
y no estás perdiendo músculo. Ese es el examen que importa, no el número de la barra.

Vas a estancarte. Estancarte manteniendo el peso mientras bajas grasa **no es fallar: es
exactamente el objetivo del programa.**

### Progresión y seguridad

- **Doble progresión:** suma 1 rep por serie cada semana; cuando llegues al tope del rango en
  todas las series, sube 2.5 kg y vuelve al tope bajo.
- **Deload cada 6 semanas:** mismo peso, mitad de series. No la negocies — en déficit la
  necesitas más que en volumen.
- **Entrenas solo:** pines de seguridad puestos siempre en sentadilla y press de banca. Sin
  observador, **nunca** llegues al fallo en press de banca.
- Con discos de rosca los saltos mínimos son grandes. Cuando un salto sea demasiado, progresa
  sumando reps o una serie antes de subir el disco.

### Cardio

El cardio **no pone el déficit** — eso lo hace la comida. El cardio es para tu corazón, tu
hígado y tus pasos. Meta: **9.000 pasos/día**, más 12 minutos de caminata después del almuerzo
(aplana el pico de glucosa, y es gratis).

**No metas HIIT** encima de 4 días de pesas en déficit. Te canibaliza la recuperación.

---

## 5. Cómo se usa el bot

Todo vive en el bot de Telegram que ya tienes. Los gastos siguen funcionando igual.

### Registrar comida

```
comi 3 huevos, 200g cottage cheese, 1 thin     → 511 kcal, 48 P
comi una empanada de restaurante                → estima con el modelo
[manda una foto del plato]                      → clasifica, estima, y pide confirmar
/borrar                                          → quita la última
```

Primero busca en tu base local de 53 alimentos — instantáneo y consistente. Solo si no encuentra
algo llama al modelo, y lo marca con `~` para que sepas cuál dato es estimado.

**Las fotos son una sola llamada que clasifica y extrae:** si mandas un recibo del banco va a
gastos, si mandas un plato va a nutrición. No tienes que decirle cuál es.

### Ver dónde vas

```
/hoy        → barras de progreso de kcal, proteína, carbos, grasa y fibra
/semana     → promedio real, déficit real, tendencia de peso
/peso 95.4  → registra y calcula la media móvil de 7 días
```

**Pésate cada mañana en ayunas, después del baño.** El dato diario es ruido; la media de 7 días
es la señal. El bot compara medias, no días sueltos, y te avisa si bajas demasiado rápido o si
la media sube.

### Planificar

```
/plan       → un día completo que cuadra con tus macros (12 menús rotando)
/receta     → la receta que mejor cabe en lo que te queda del día
/receta l3  → los pasos de esa receta
/gym        → el entreno de hoy
/set sentadilla 80 5,5,4   → registra series y detecta records
/prs        → tus records
```

### Contexto

```
/perfil            → tus números y cómo se calculan
/perfil peso=94.2  → actualiza y recalcula todo
/labs              → tus banderas de sangre
/labs preguntas    → qué preguntarle al médico
/whoop             → recovery, sueño, strain, y qué hacer hoy
```

### WHOOP

El bot corre como worker sin servidor web, así que no puede recibir el redirect de OAuth. Se
autoriza una vez a mano y de ahí se renueva solo:

1. Crea una app en `developer.whoop.com`
2. Pon `WHOOP_CLIENT_ID` y `WHOOP_CLIENT_SECRET` en Render
3. Autoriza en el navegador
4. `/whoop token <refresh_token>`

**Detalle importante:** WHOOP *rota* el refresh token — cada vez que se canjea uno, el anterior
queda inválido al instante. Por eso el token se guarda en Firestore y se reescribe en cada
renovación, no en una variable de entorno. Si estuviera en una env var, se rompería en el primer
refresh.

Mientras tanto funciona a mano: `/whoop 65 7.5 12.3` (recovery %, horas de sueño, strain).

**Cómo usa el WHOOP:** recovery verde → intenta sumar la rep o el disco. Amarillo → entrena
normal sin forzar el fallo. Rojo → baja una serie de cada compuesto y quédate en RIR 3. Sueño
bajo de 6.5 h → el hambre de hoy es bioquímica (más grelina, menos leptina), no falta de
voluntad.

**Lo que el bot NO hace:** sumar las calorías que WHOOP dice que quemaste a tu objetivo. Tu TDEE
ya las incluye. Comer de más por lo que marca el reloj es el error clásico del wearable.

---

## 6. Las primeras 72 horas

1. **Pide la cita** para repetir las pruebas hepáticas. Hoy, no el lunes.
2. **Pésate mañana** en ayunas y manda `/peso <número>`. Ese es tu punto cero real.
3. **Compra creatina y proteína en polvo.**
4. **Cocina en tanda el domingo:** 6 huevos duros, una olla de curry de garbanzos (`d2`, rinde
   3 días), y dos frascos de overnight oats (`b3`).
5. **Lunes: Upper A.** Con pesos conservadores — la primera semana es para calibrar dónde
   estás, no para impresionar a nadie.
6. **Registra todo, aunque te pases.** Un día malo registrado sirve; un día malo escondido no
   enseña nada. Registrar es la mitad del trabajo.

---

*Los macros de este documento se calculan desde `data/foods.json` y `data/recipes.json`. Los
valores de las etiquetas son aproximados: verifícalos contra tus paquetes y corrígelos en
`foods.json`, que es la única fuente de verdad del bot.*

*Esto no es consejo médico. Tus análisis los interpreta Dr Brenton Martin.*

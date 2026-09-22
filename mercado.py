#!/usr/bin/env python3
"""Genera LISTA_MERCADO.md sumando los ingredientes de la semana.

Suma los gramos de cada receta del menú semanal (data/recipes.json), resta lo
que ya hay en casa (data/pantry.json) y convierte el resto a unidades de
compra. La lista no se estima: se calcula.

Uso:  python3 mercado.py
"""
import json, os
from collections import defaultdict

# El yogurt casero no se compra: se hace. Estos son los insumos por kg colado.
YOGURT = {"Leche descremada": 1670, "Leche en polvo descremada": 125}

SECCIONES = [
 ("Lácteos y proteína", ["Cottage alto en proteína", "Leche descremada",
   "Leche en polvo descremada", "Proteína en polvo", "Huevo entero",
   "Clara de huevo", "Tofu firme", "Leche de soya"]),
 ("Verdura", ["Espinaca", "Champiñones", "Brócoli", "Calabacín", "Tomate",
   "Zanahoria", "Habichuela", "Coliflor", "Pimentón", "Cebolla larga", "Papa", "Limón"]),
 ("Fruta", ["Banana", "Manzana", "Sandía"]),
 ("Congelados", ["Berries congelados", "Edamame congelado", "Espinaca congelada"]),
 ("Despensa", ["Arroz basmati crudo", "Pasta cruda", "Avena en hojuelas",
   "Harina PAN", "Garbanzos de lata", "Lentejas de lata", "Lentejas rojas secas",
   "Lentejas cafés secas", "Frijoles negros secos", "Frijoles refritos",
   "Mantequilla de maní", "Almendras", "Aceite de oliva", "Dolmio", "Salsa mild",
   "Caldo Campbell's", "Wrap Mission wholegrain", "Whole Earth"]),
]

def calcular():
    """Suma la semana, resta la despensa. Devuelve datos crudos, sin formato."""
    base = os.path.dirname(os.path.abspath(__file__))
    carga = lambda n: json.load(open(os.path.join(base, "data", n), encoding="utf8"))
    alimentos = carga("foods.json")["alimentos"]
    D, P = carga("recipes.json"), carga("pantry.json")
    recetas, semana = D["recetas"], D["semana"]
    casa = {**P["despensa"], **P["nevera"]}
    unidades = P["_unidades_compra"]

    # 1. sumar la semana
    pide = defaultdict(float)
    for v in semana.values():
        for rid in v["ids"]:
            for nombre, gramos in recetas[rid]["ing"]:
                pide[nombre] += gramos

    # 2. el yogurt casero se traduce a sus insumos
    yog = pide.pop("Yogurt griego casero", 0)
    for insumo, por_kg in YOGURT.items():
        pide[insumo] += yog / 1000 * por_kg

    # 3. la espinaca de los platos cocidos se compra congelada: mitad de precio y no se marchita
    COCIDAS = {"b1","b5","d1","d2","d4","d5","d7","l1"}
    cocida = sum(g for v in semana.values() for rid in v["ids"] if rid in COCIDAS
                   for n, g in recetas[rid]["ing"] if n == "Espinaca")
    if cocida:
        pide["Espinaca"] -= cocida
        pide["Espinaca congelada"] = cocida

    # 4. restar lo que hay en casa
    comprar, tengo, sin_medir = {}, [], []
    for nombre, g in sorted(pide.items()):
        hay = casa.get(nombre, 0)
        if nombre in casa and hay is None:      # hay, pero no sé cuánto
            sin_medir.append((nombre, g)); continue
        falta = g - (hay or 0)
        if falta <= 0:
            tengo.append((nombre, g, hay)); continue
        comprar[nombre] = falta

    return {"comprar": comprar, "tengo": tengo, "sin_medir": sin_medir,
            "yogurt": yog, "pide": dict(pide), "casa": casa, "unidades": unidades,
            "dias": len(semana), "secciones": SECCIONES}

def main():
    R = calcular()
    comprar, tengo, sin_medir = R["comprar"], R["tengo"], R["sin_medir"]
    pide, casa, unidades, yog = R["pide"], R["casa"], R["unidades"], R["yogurt"]
    dias = R["dias"]

    def unidad(nombre, g):
        if nombre not in unidades:
            return f"{g/1000:.1f} kg" if g >= 1000 else f"{round(g)} g"
        tam, etiqueta = unidades[nombre]
        n = max(1, -(-round(g) // tam))         # techo
        return f"**{n} × {etiqueta}**"

    L = ["# Lista de mercado — semana siguiente", "",
         f"Calculada sumando los {dias} días del menú de `data/recipes.json` "
         "y restando lo de `data/pantry.json`.", "",
         "Corre `python3 mercado.py` para regenerarla cuando cambie la semana o la despensa.", ""]
    total = 0
    for titulo, items in SECCIONES:
        filas = [(n, comprar[n]) for n in items if n in comprar]
        if not filas: continue
        total += len(filas)
        L += [f"## {titulo}", "", "| | Compra | Usa la semana | Ya tienes |",
              "|---|---|---|---|"]
        for n, g in filas:
            hay = casa.get(n) or 0
            L.append(f"| {n} | {unidad(n, g)} | {round(pide[n])} g | "
                     f"{str(round(hay)) + ' g' if hay else '—'} |")
        L.append("")
    otros = [n for n in comprar if not any(n in it for _, it in SECCIONES)]
    if otros:
        L += ["## Sin clasificar", ""] + [f"- {n}: {round(comprar[n])} g" for n in otros] + [""]

    L += ["---", "", "## Ya está en casa — no lo compres", ""]
    for n, g in sin_medir:
        L.append(f"- **{n}** — la semana usa {round(g)} g. Revisa que alcance")
    for n, g, hay in tengo:
        L.append(f"- **{n}** — la semana usa {round(g)} g y tienes {round(hay)} g")
    L += ["", "## Al fondo del estante", "",
          "Aceite de coco (~87% grasa saturada) · ghee ×2 (~62%). "
          "Con LDL en 3,4 el de todos los días es el aceite de oliva (~14%).", ""]
    L += ["## El yogurt no se compra, se hace", "",
          f"La semana usa **{round(yog)} g de yogurt griego casero**. Eso son "
          f"**{pide['Leche descremada']/1000:.1f} L de leche descremada** y "
          f"**{round(pide['Leche en polvo descremada'])} g de leche en polvo** "
          "en la función Yogurt: 85 °C, enfriar a 43 °C, 3 cucharadas de kéfir, 9 h, colar 3 h.", ""]
    open("LISTA_MERCADO.md", "w", encoding="utf8").write("\n".join(L))
    print(f"{total} líneas de compra · {len(sin_medir)+len(tengo)} ya en casa")
    print(f"yogurt de la semana: {round(yog)} g → {pide['Leche descremada']/1000:.1f} L de leche")

if __name__ == "__main__":
    main()

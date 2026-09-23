#!/usr/bin/env python3
"""Chequea que las recetas estén completas.

Dos cosas que a ojo se escapan y en la cocina se notan:
  1. Un ingrediente que está en la lista pero ningún paso dice qué hacer con él.
  2. Un ingrediente que los pasos nombran pero no está en la lista (no lo compras).

Uso:  python3 verificar.py
"""
import json, re, sys, unicodedata

def pelar(s):
    s = unicodedata.normalize("NFD", s.lower())
    return "".join(c for c in s if unicodedata.category(c) != "Mn")

# Con qué palabra se reconoce cada ingrediente dentro de un paso.
CLAVES = {
 "Huevo entero": ["huevo"], "Clara de huevo": ["clara"],
 "Cottage alto en proteína": ["cottage"], "Yogurt griego casero": ["yogurt"],
 "Proteína en polvo": ["proteina"], "Leche descremada": ["leche"],
 "Queso cheddar light": ["cheddar"], "Parmesano": ["parmesano"],
 "Ricotta light": ["ricotta"], "Crema light": ["crema"],
 "Tofu firme": ["tofu"], "Tempeh": ["tempeh"],
 "Carne vegetal molida": ["carne vegetal"], "Hummus": ["hummus"],
 "Avena en hojuelas": ["avena"], "Granola": ["granola"], "Weet-Bix": ["weet-bix"],
 "Tostada integral": ["tostada", "pan"], "Harina PAN": ["harina pan", "masa"],
 "Arepa Sary con queso": ["arepa"],
 "Arroz basmati crudo": ["arroz"], "Arroz jazmín crudo": ["arroz"],
 "Arroz arborio crudo": ["arroz"], "Pasta cruda": ["pasta "],
 "Lentejas cafés secas": ["lenteja"], "Lentejas rojas secas": ["lenteja"],
 "Frijol rojo seco": ["frijol"], "Frijoles negros secos": ["frijol"],
 "Frijol rojo de lata": ["frijol"], "Frijoles negros de lata": ["frijol"],
 "Frijoles refritos": ["frijol"], "Garbanzos de lata": ["garbanzo"],
 "Passata de tomate": ["passata"], "Pasta de tomate": ["pasta de tomate"],
 "Tomate": ["tomate"], "Cebolla": ["cebolla"], "Cebolla larga": ["cebolla larga", "cebolla"],
 "Zanahoria": ["zanahoria"], "Apio": ["apio"], "Pimentón": ["pimenton"],
 "Champiñones": ["champinon"], "Espinaca": ["espinaca"], "Brócoli": ["brocoli"],
 "Habichuela": ["habichuela"], "Maíz tierno": ["maiz", "mazorca"],
 "Papa": ["papa"], "Camote": ["camote"], "Pepino": ["pepino"],
 "Aguacate": ["aguacate"], "Banana": ["banana"], "Manzana": ["manzana"],
 "Mango": ["mango"], "Naranja": ["naranja"], "Limón": ["limon"],
 "Berries congelados": ["berries"], "Plátano maduro": ["platano", "tajada"],
 "Edamame congelado": ["edamame"], "Mantequilla de maní": ["mantequilla de mani"],
 "Almendras": ["almendra"], "Chocolate 85%": ["chocolate"],
 "Leche de coco light": ["coco"], "Pasta de curry rojo": ["pasta de curry", "curry"],
 "Caldo Campbell's": ["caldo"], "Salsa de soya": ["soya"],
 "Aceite de oliva": ["aceite", "espray"], "Whole Earth": ["whole earth", "dulce"],
 "Alcaparras": ["alcaparra"], "Salsa mild": ["salsa"], "Dolmio": ["dolmio"],
 "Leche de soya": ["leche de soya"], "Sandía": ["sandia"],
}
# Palabras que, si aparecen en un paso, obligan a que el ingrediente esté en la lista.
REVERSO = {
 "limon": "Limón", "caldo": "Caldo", "yogurt": "Yogurt", "cottage": "Cottage",
 "aguacate": "Aguacate", "parmesano": "Parmesano", "cheddar": "Cheddar",
 "chocolate": "Chocolate", "naranja": "Naranja", "hummus": "Hummus",
 "ricotta": "Ricotta", "granola": "Granola",
}

def main():
    D = json.load(open("data/recipes.json", encoding="utf8"))
    fallos = []
    for rid, r in sorted(D["recetas"].items()):
        texto = pelar(" ".join(p["t"] if isinstance(p, dict) else p
                               for p in r.get("pasos", [])))
        for nombre, _g in r["ing"]:
            claves = CLAVES.get(nombre)
            if claves is None:
                fallos.append((rid, "sin clave", nombre)); continue
            if not any(pelar(c) in texto for c in claves):
                fallos.append((rid, "no se usa", nombre))
        if "condimentos" not in r:
            fallos.append((rid, "sin condimentos", "—"))
        # y al revés: si un paso nombra algo que no está en la lista, no lo compras
        nombres = {n for n, _ in r["ing"]}
        nombres |= {c["n"] for c in r.get("condimentos", [])}
        tengo = pelar(" ".join(nombres))
        for palabra, ingrediente in REVERSO.items():
            if palabra in texto and pelar(ingrediente) not in tengo:
                fallos.append((rid, "no está en la lista", ingrediente))
    if fallos:
        print(f"{len(fallos)} problemas:\n")
        for rid, tipo, nombre in fallos:
            print(f"  {rid:5} {tipo:16} {nombre}")
    else:
        print(f"{len(D['recetas'])} recetas · todos los ingredientes aparecen en los pasos")
    return 1 if fallos else 0

if __name__ == "__main__":
    sys.exit(main())

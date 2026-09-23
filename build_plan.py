#!/usr/bin/env python3
"""Genera PLAN_NUTRICION.md desde plan_template.md + data/recipes.json.

Los macros nunca se escriben a mano: se calculan desde data/foods.json.
Uso:  python3 build_plan.py
"""
import json

GRUPOS = {"desayuno": "Desayunos", "almuerzo": "Almuerzos",
          "cena": "Cenas", "snack": "Snacks"}

def main():
    alimentos = json.load(open("data/foods.json", encoding="utf8"))["alimentos"]
    datos = json.load(open("data/recipes.json", encoding="utf8"))
    recetas, semana, perfil = datos["recetas"], datos["semana"], datos["perfil"]

    # recalcular cada receta desde foods.json, para que no puedan desincronizarse
    for r in recetas.values():
        t = [0.0] * 5
        for nombre, gramos in r["ing"]:
            a = alimentos[nombre]
            for i, k in enumerate(("kcal", "p", "c", "f", "fib")):
                t[i] += a[k] * gramos / 100.0
        r.update(kcal=round(t[0]), p=round(t[1]), c=round(t[2]),
                 f=round(t[3]), fib=round(t[4]))

    tablas = []
    for grupo, titulo in GRUPOS.items():
        tablas += [f"**{titulo}**\n",
                   "| ID | Receta | Cómo se cocina | kcal | P | C | G | Fibra |",
                   "|---|---|---|---|---|---|---|---|"]
        for k, r in sorted(recetas.items()):
            if r["g"] != grupo:
                continue
            c = r.get("coccion", {})
            como = ("**Olla** · " if c.get("donde") == "olla" else "") + c.get("texto", "—")
            tablas.append(f"| `{k}` | {r['n']} | {como} | {r['kcal']} | **{r['p']} g** "
                          f"| {r['c']} g | {r['f']} g | {r['fib']} g |")
        tablas.append("")

    filas = ["| Día | | Menú | kcal | P | C | G | Fibra |",
             "|---|---|---|---|---|---|---|---|"]
    acum = [0] * 5
    for dia, v in semana.items():
        t = v["total"]
        acum = [a + b for a, b in zip(acum, t)]
        menu = " · ".join(recetas[i]["n"] for i in v["ids"])
        filas.append(f"| **{dia}** | {v['tipo']} | {menu} | {t[0]} | **{t[1]}** "
                     f"| {t[2]} | {t[3]} | {t[4]} |")
    prom = [a // len(semana) for a in acum]
    filas.append(f"| | | **Promedio diario** | **{prom[0]}** | **{prom[1]}** "
                 f"| {prom[2]} | {prom[3]} | {prom[4]} |")

    detalle = []
    for grupo, titulo in GRUPOS.items():
        detalle.append(f"### {titulo}\n")
        for k, r in sorted(recetas.items()):
            if r["g"] != grupo:
                continue
            ings = " · ".join(f"{n} {int(g)} g" for n, g in r["ing"])
            c = r.get("coccion", {})
            como = ("Olla · " if c.get("donde") == "olla" else "") + c.get("texto", "")
            detalle.append(f"**`{k}` {r['n']}** — {r['kcal']} kcal · {r['p']} g P · "
                           f"{r['c']} g C · {r['f']} g G · {r['fib']} g fibra  \n"
                           f"*{como}*  \n{ings}\n")

    doc = (open("plan_template.md", encoding="utf8").read()
           .replace("{{TABLAS}}", "\n".join(tablas).rstrip())
           .replace("{{SEMANA}}", "\n".join(filas))
           .replace("{{DETALLE}}", "\n".join(detalle).rstrip()))
    open("PLAN_NUTRICION.md", "w", encoding="utf8").write(doc)

    deficit = perfil["tdee"] - prom[0]
    print(f"{len(recetas)} recetas · {len(alimentos)} alimentos")
    print(f"promedio: {prom[0]} kcal · {prom[1]} g P · {prom[2]} g C · "
          f"{prom[3]} g G · {prom[4]} g fibra")
    print(f"objetivo: {perfil['kcal_dia']} kcal · {perfil['p']} g P · "
          f"{perfil['f']} g G (piso) · {perfil['fib']} g fibra")
    print(f"déficit: {deficit} kcal/día → {deficit * 7 / 7700:.2f} kg/semana")

if __name__ == "__main__":
    main()

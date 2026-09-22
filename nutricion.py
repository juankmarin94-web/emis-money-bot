"""Comandos de nutrición del bot: menú, recetas, olla y cocción por tandas.

Todo sale de data/*.json. Las funciones devuelven texto Markdown y no tocan
Telegram ni Firestore, así que se pueden probar desde la terminal:

    python3 nutricion.py            # demo de todos los comandos
    python3 nutricion.py receta l1 x4
"""
import json, os, unicodedata
from collections import defaultdict

BASE = os.path.dirname(os.path.abspath(__file__))
_cache = {}

def _cargar(nombre):
    if nombre not in _cache:
        with open(os.path.join(BASE, "data", f"{nombre}.json"), encoding="utf8") as f:
            _cache[nombre] = json.load(f)
    return _cache[nombre]

def _sin_tildes(s):
    return "".join(c for c in unicodedata.normalize("NFD", s.lower())
                   if unicodedata.category(c) != "Mn")

def _cantidad(g):
    """1200 -> '1,2 kg'   ·   85 -> '85 g'"""
    return f"{g/1000:.1f} kg".replace(".", ",") if g >= 1000 else f"{round(g)} g"

# ── /hoy y /plan ──────────────────────────────────────────────────────────────
def hoy(indice_dia):
    D = _cargar("recipes"); semana = D["semana"]
    nombre = list(semana)[indice_dia % len(semana)]
    dia = semana[nombre]; t = dia["total"]; perfil = D["perfil"]
    L = [f"🍽️ *{nombre}* — día de {dia['tipo']}", ""]
    for rid in dia["ids"]:
        r = D["recetas"][rid]
        L.append(f"`{rid}` *{r['n']}*\n    {r['kcal']} kcal · {r['p']} g P")
    L += ["", f"*Total:* {t[0]} kcal · *{t[1]} g de proteína* · {t[2]} g C · {t[3]} g G · {t[4]} g fibra",
          f"_Objetivo: {perfil['kcal_dia']} kcal · {perfil['p']} g P_", "",
          "`/receta <id>` para los pasos · `/receta <id> x4` para una tanda"]
    return "\n".join(L)

def plan():
    D = _cargar("recipes"); semana = D["semana"]; perfil = D["perfil"]
    L = [f"📅 *La semana* — objetivo {perfil['kcal_dia']} kcal y {perfil['p']} g de proteína", ""]
    acum = [0] * 5
    for nombre, dia in semana.items():
        t = dia["total"]; acum = [a + b for a, b in zip(acum, t)]
        L.append(f"*{nombre}* ({dia['tipo']}) — {t[0]} kcal · {t[1]} g P\n"
                 f"    {' · '.join(dia['ids'])}")
    n = len(semana)
    L += ["", f"*Promedio:* {acum[0]//n} kcal · *{acum[1]//n} g de proteína* · {acum[4]//n} g fibra"]
    return "\n".join(L)

# ── /receta [xN] ──────────────────────────────────────────────────────────────
def receta(rid, porciones=1):
    D = _cargar("recipes"); R = D["recetas"]
    rid = rid.lower().strip()
    if rid not in R:
        cand = [k for k, r in R.items() if _sin_tildes(rid) in _sin_tildes(r["n"])]
        if len(cand) != 1:
            return f"No conozco `{rid}`. Usa /plan para ver los ids, o /tanda."
        rid = cand[0]
    r = R[rid]; n = max(1, int(porciones))
    tanda = r.get("tanda", {})
    L = [f"*{r['n']}*  `{rid}`" + (f"  ×{n} porciones" if n > 1 else ""), ""]
    L.append(f"{r['kcal']*n} kcal · *{r['p']*n} g P* · {r['c']*n} g C · {r['f']*n} g G · {r['fib']*n} g fibra")
    if n > 1:
        L.append(f"_Por porción: {r['kcal']} kcal · {r['p']} g P_")
    fuera = D["olla"]["fuera_de_la_olla"]
    grupos = {"A la olla": [], "Aparte": [], "Al servir": []}
    for nombre, g in r["ing"]:
        destino = ("Al servir" if nombre in fuera["al_servir"]
                   else "Aparte" if nombre in fuera["aparte"] else "A la olla")
        grupos[destino].append((nombre, g))
    for titulo, items in grupos.items():
        if not items:
            continue
        nota = ""
        if n > 1 and titulo == "Al servir":
            nota = " _(no los guardes dentro: se cortan o se aguan)_"
        elif n > 1 and titulo == "Aparte":
            nota = " _(en su propia tanda)_"
        L += ["", f"*{titulo}*{nota}"]
        for nombre, g in items:
            L.append(f"• {nombre} — *{_cantidad(g*n)}*"
                     + (f"  ({_cantidad(g)} por porción)" if n > 1 else ""))
    if r.get("olla"):
        o = r["olla"]
        L += ["", f"*Olla — {o['modo']}" + (f", {o['min']} min" if o["min"] else "") +
              (f", liberación {o['liberacion']}*" if o["liberacion"] != "—" else "*"), ""]
        for i, paso in enumerate(o["pasos"], 1):
            L.append(f"{i}. {paso}")
    if tanda:
        L += ["", "*Por tandas*"]
        if tanda["max_porciones"] == 1:
            L.append(f"❌ {tanda['nota']}")
        else:
            L.append(f"✅ Hasta *{tanda['max_porciones']} porciones* por tanda · "
                     f"nevera *{tanda['nevera_dias']} días* · "
                     + ("congela bien" if tanda["congela"] else "no congela"))
            L.append(f"_{tanda['nota']}_")
            if n > tanda["max_porciones"]:
                L.append(f"\n⚠️ *{n} porciones no caben.* El máximo seguro en tu olla de 6 L "
                         f"es {tanda['max_porciones']}: las legumbres y los granos espuman y "
                         f"no se puede pasar de la mitad de la olla. Hazlo en dos tandas.")
    return "\n".join(L)

# ── /tanda ────────────────────────────────────────────────────────────────────
# Minutos que la olla queda ocupada: presión + liberación + el sofrito previo.
_OCUPA = {"d5": 60, "d2": 30, "l1": 25, "l2": 30, "d4": 30, "l5": 35, "l6": 25, "b3": 5}

def tanda():
    """Una secuencia de domingo que de verdad cabe en una tarde."""
    D = _cargar("recipes"); R = D["recetas"]; semana = D["semana"]
    principales = sum(1 for dia in semana.values()
                      for rid in dia["ids"] if not rid.startswith("s"))
    # Tres tandas a presión que congelan + los oats. Cubren ~2/3 de la semana.
    recomendadas = ["d5", "d2", "l1", "b3"]

    def bloque(rid, detalle=True):
        r = R[rid]; t = r["tanda"]; n = t["max_porciones"]
        out = [f"*{r['n']}*  `{rid}`",
               f"    🍲 *×{n}* — {r['p']*n} g de proteína en total"]
        if detalle and r.get("olla"):
            o = r["olla"]
            out.append(f"    {o['modo']}" + (f" · {o['min']} min" if o["min"] else "")
                       + (f" · liberación {o['liberacion']}" if o["liberacion"] != "—" else ""))
        out.append(f"    nevera {t['nevera_dias']} días · "
                   + ("congela el resto" if t["congela"] else "no congela"))
        out.append(f"    → `/receta {rid} x{n}`")
        return out

    porciones = sum(R[r]["tanda"]["max_porciones"] for r in recomendadas if not r.startswith("b"))
    minutos = sum(_OCUPA[r] for r in recomendadas) + 25 + 25   # + huevos + arroz

    L = ["👨‍🍳 *Domingo en la olla*", "",
         "Cuatro tandas, en este orden. La olla queda ocupada "
         f"*~{minutos // 60} h {minutos % 60} min* en total, casi todo desatendido.", ""]
    L += ["*1. Huevos duros* — 1 taza de agua, canasta, 12 huevos",
          "    5 min de presión + 5 natural + hielo 3 min. Snacks de toda la semana", ""]
    for k, rid in enumerate(recomendadas, 2):
        L += [f"*{k}. " + bloque(rid)[0][1:]] + bloque(rid)[1:] + [""]
    L += ["*6. Arroz al caldo* — 1 : 1,25, 5 min de presión, natural 10 min. Rinde 6 porciones", "",
          "*Y de noche, mientras duermes:*",
          "• *2 L de yogurt* — 85 °C → enfriar a 43 °C → 3 cucharadas de kéfir → 9 h en Yogurt.",
          "    Cuélalo 3 h el lunes. ~120 g de proteína por unos $5", "",
          f"Con esto tienes *{porciones} porciones principales* listas de los *{principales} "
          f"platos* de la semana, más desayunos, huevos, arroz y yogurt. "
          "El resto de la semana es calentar.", "",
          "⚠️ *El costo:* una tanda de 4 significa comer ese plato 4 veces. Si quieres más "
          "variedad, haz 2 de cada una y vuelve a cocinar el miércoles.", "",
          "*El resto del catálogo, si te cansas de estos*"]
    otros = [rid for rid, r in sorted(R.items())
             if r.get("tanda", {}).get("max_porciones", 1) > 1
             and rid not in recomendadas and not rid.startswith("s")]
    for rid in otros:
        t = R[rid]["tanda"]
        L.append(f"• `{rid}` {R[rid]['n']} — hasta ×{t['max_porciones']}, "
                 + ("congela" if t["congela"] else "no congela"))
    L += ["", "*Nunca por tandas — estos son de 10 minutos al momento:*"]
    for rid, r in sorted(R.items()):
        t = r.get("tanda")
        if t and t["max_porciones"] == 1:
            L.append(f"• `{rid}` {r['n']} — _{t['nota']}_")
    return "\n".join(L)

# ── /olla ─────────────────────────────────────────────────────────────────────
def olla():
    o = _cargar("recipes")["olla"]
    L = [f"🍲 *{o['modelo']}*", "", "*Cuánto se puede llenar*",
         f"• Guisos y sopas: {o['llenado']['guisos']}",
         f"• Legumbres, granos, pasta y avena: {o['llenado']['legumbres_granos_pasta_avena']}",
         "", "*Las reglas que importan*"]
    L += [f"{i}. {r}" for i, r in enumerate(o["reglas"], 1)]
    L += ["", "*Nunca a presión*", " · ".join(o["nunca_en_presion"]), "",
          "*Tiempos*", "```", f"{'':28} {'min':>4}  {'líquido':<18} liberación"]
    for k, (m, liq, lib) in o["tiempos"].items():
        L.append(f"{k:28} {m:>4}  {liq:<18} {lib}")
    L += ["```", "", "`/receta <id>` trae los pasos exactos de cada plato."]
    return "\n".join(L)

# ── /mercado ──────────────────────────────────────────────────────────────────
def mercado():
    try:
        with open(os.path.join(BASE, "LISTA_MERCADO.md"), encoding="utf8") as f:
            md = f.read()
    except FileNotFoundError:
        return "Falta `LISTA_MERCADO.md`. Corre `python3 mercado.py`."
    fuera = ("| | Compra", "|---|", "Calculada sumando", "Corre `python3")
    L = ["🛒 *Lista de mercado*", ""]
    for linea in md.splitlines():
        s = linea.strip()
        if not s or s.startswith("#") and s.count("#") == 1 or s.startswith(fuera):
            if s.startswith("## "):
                L += ["", f"*{s[3:]}*"]
            continue
        if s.startswith("## "):
            L += ["", f"*{s[3:]}*"]
        elif s.startswith("|"):
            c = [x.strip() for x in s.strip("|").split("|")]
            if len(c) >= 2 and c[1] and not c[1].startswith("---") and c[1] != "Compra":
                L.append(f"☐ {c[0]} — {c[1]}".replace("**", ""))
        elif s.startswith("- "):
            L.append(f"  {s[2:]}".replace("**", ""))
        elif s != "---":
            L.append(s.replace("**", "*"))
    return "\n".join(L)

AYUDA = ("🥗 *Nutrición*\n\n"
         "/hoy — el menú de hoy con sus macros\n"
         "/plan — la semana completa\n"
         "/receta `<id>` — ingredientes y pasos de la olla\n"
         "/receta `<id>` x4 — las cantidades para una tanda\n"
         "/tanda — qué cocinar el domingo y cuánto rinde\n"
         "/olla — tiempos, llenado y las reglas de la Philips\n"
         "/mercado — la lista de compras de la semana")

if __name__ == "__main__":
    import sys
    a = sys.argv[1:]
    if not a:
        for t in (AYUDA, hoy(0), receta("l1", 4), tanda(), olla(), mercado()):
            print("\n" + "=" * 62 + "\n"); print(t)
    elif a[0] == "receta":
        print(receta(a[1], int(a[2].lstrip("x")) if len(a) > 2 else 1))
    else:
        print({"hoy": lambda: hoy(0), "plan": plan, "tanda": tanda,
               "olla": olla, "mercado": mercado}[a[0]]())

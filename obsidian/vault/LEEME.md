---
tipo: meta
actualizado: 2026-09-07
---

# Cómo funciona este vault

## Qué se genera y qué es mío

| Carpeta | Quién manda |
|---|---|
| Todo lo de la raíz, `Recetas/`, las sesiones | **Generado.** Se sobreescribe. No editar aquí. |
| `Registro/` | **Mío.** El script nunca lo toca. |
| `Plantillas/` | Generado una vez; puedes editarla y no se pisa si la mueves. |

Para cambiar un macro, una receta o un ejercicio: se edita el JSON en
`data/` del repo y se regenera. Así el vault, el panel y los cálculos nunca
se desincronizan.

```bash
python3 obsidian/generar.py
```

## El truco de la compresión

[[Estado]] existe para una sola cosa: **abrir una sesión nueva de Claude sin
gastar límite**. Pégale esa nota y ya sabe todo — perfil, targets, análisis,
reglas, dónde está cada cosa — sin que subas fotos otra vez ni reexpliques
nada.

Una conversación larga reenvía todo su historial en cada mensaje, así que el
costo crece con el largo. Sesión nueva + [[Estado]] cuesta una fracción de
seguir una conversación de 30 turnos.

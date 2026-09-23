"""Genera un reel vertical (1080x1920) con tips para jugadores y clubes.

Uso:  pip install pillow imageio-ffmpeg && python reels/make_reel.py
Salida: reels/reel_clubes_jugadores.mp4 y reels/portada.jpg
"""
import os, subprocess
from PIL import Image, ImageDraw, ImageFont
import imageio_ffmpeg

W, H, FPS = 1080, 1920, 30
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, 'reel_clubes_jugadores.mp4')
COVER = os.path.join(HERE, 'portada.jpg')

BG1, BG2 = (6, 26, 16), (12, 58, 34)
LINE = (255, 255, 255, 22)
ACCENT = (198, 255, 61)
WHITE = (255, 255, 255)
MUTED = (190, 214, 198)

FB = '/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf'
FR = '/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf'
font = lambda p, s: ImageFont.truetype(p, s)

# (etiqueta, número, título, cuerpo, segundos)
SLIDES = [
    ('GUÁRDALO', None, 'Lo que todo jugador y club debe saber', 'Tips reales para fichar y ser fichado', 3.2),
    ('PARA JUGADORES', '01', 'Tu video: corto y directo',
     'Máximo 3–5 minutos. Tus mejores jugadas en los primeros 30 segundos. Marca quién eres en cada clip.', 4.6),
    ('PARA JUGADORES', '02', 'Tu ficha siempre lista',
     'Posición, pierna hábil, altura, año de nacimiento, club actual y contacto. Un club no debería buscar tus datos.', 4.6),
    ('PARA JUGADORES', '03', 'Ojo con los intermediarios',
     'Desde 2023 FIFA exige licencia a los agentes. Verifica que tu agente esté licenciado y nunca pagues por una "prueba".', 4.8),
    ('PARA CLUBES', '04', 'Define el perfil antes de buscar',
     'Posición, rango de edad, presupuesto y estilo de juego. Sin perfil claro, el scouting es ruido.', 4.6),
    ('PARA CLUBES', '05', 'Mira partidos completos',
     'Un highlight muestra lo mejor. Evalúa al menos 2–3 partidos: sin balón, decisiones y actitud.', 4.6),
    ('PARA CLUBES', '06', 'Tu cantera también genera ingresos',
     'Por el mecanismo de solidaridad FIFA, los clubes que formaron al jugador entre los 12 y 23 años reciben hasta el 5% de sus traspasos internacionales. Guarda tus registros.', 5.6),
    ('COMPARTE', None, '¿Te sirvió?',
     'Guárdalo y envíaselo a tu club o a ese compañero que busca equipo.', 3.6),
]

def wrap(draw, text, f, maxw):
    lines, cur = [], ''
    for w in text.split():
        t = (cur + ' ' + w).strip()
        if draw.textlength(t, font=f) <= maxw:
            cur = t
        else:
            lines.append(cur); cur = w
    if cur: lines.append(cur)
    return lines

def background():
    img = Image.new('RGB', (W, H))
    px = ImageDraw.Draw(img)
    for y in range(H):
        k = y / H
        px.line([(0, y), (W, y)], fill=tuple(int(BG1[i] + (BG2[i] - BG1[i]) * k) for i in range(3)))
    ov = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(ov)
    # líneas de cancha
    d.rectangle([60, 60, W - 60, H - 60], outline=LINE, width=4)
    d.line([60, H // 2, W - 60, H // 2], fill=LINE, width=4)
    d.ellipse([W // 2 - 200, H // 2 - 200, W // 2 + 200, H // 2 + 200], outline=LINE, width=4)
    d.rectangle([W // 2 - 300, 60, W // 2 + 300, 380], outline=LINE, width=4)
    d.rectangle([W // 2 - 300, H - 380, W // 2 + 300, H - 60], outline=LINE, width=4)
    img.paste(ov, (0, 0), ov)
    return img

def layer(h):
    return Image.new('RGBA', (W, h), (0, 0, 0, 0))

def build_elements(tag, num, title, body):
    """Devuelve lista de (capa RGBA, y) que se animan escalonadas."""
    els, tmp = [], ImageDraw.Draw(layer(10))
    cover = num is None
    # etiqueta
    ft = font(FB, 40)
    tw = tmp.textlength(tag, font=ft)
    L = layer(90); d = ImageDraw.Draw(L)
    d.rounded_rectangle([90, 10, 90 + tw + 60, 80], radius=35, fill=ACCENT)
    d.text((120, 22), tag, font=ft, fill=BG1)
    els.append(L)
    # número
    if num:
        L = layer(300); d = ImageDraw.Draw(L)
        d.text((80, 0), num, font=font(FB, 280), fill=ACCENT)
        els.append(L)
    # título
    ftt = font(FB, 110 if cover else 92)
    lines = wrap(tmp, title, ftt, W - 180)
    lh = int(ftt.size * 1.12)
    L = layer(lh * len(lines) + 30); d = ImageDraw.Draw(L)
    for i, ln in enumerate(lines):
        d.text((90, i * lh), ln, font=ftt, fill=WHITE)
    els.append(L)
    # barra
    L = layer(30); ImageDraw.Draw(L).rectangle([90, 8, 250, 20], fill=ACCENT)
    els.append(L)
    # cuerpo
    fbd = font(FR, 56 if not cover else 60)
    lines = wrap(tmp, body, fbd, W - 180)
    lh = int(fbd.size * 1.4)
    L = layer(lh * len(lines) + 20); d = ImageDraw.Draw(L)
    for i, ln in enumerate(lines):
        d.text((90, i * lh), ln, font=fbd, fill=MUTED)
    els.append(L)
    # posiciones verticales centradas
    gap = 40
    total = sum(e.height for e in els) + gap * (len(els) - 1)
    y, out = (H - total) // 2 - 40, []
    for e in els:
        out.append((e, y)); y += e.height + gap
    return out

def ease(t):
    t = max(0.0, min(1.0, t))
    return 1 - (1 - t) ** 3

def main():
    bg = background()
    total = sum(s[4] for s in SLIDES)
    ffmpeg = imageio_ffmpeg.get_ffmpeg_exe()
    proc = subprocess.Popen([
        ffmpeg, '-y', '-loglevel', 'error',
        '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-s', f'{W}x{H}', '-r', str(FPS), '-i', '-',
        '-f', 'lavfi', '-i', 'anullsrc=r=44100:cl=stereo',
        '-shortest', '-c:v', 'libx264', '-preset', 'medium', '-crf', '20',
        '-pix_fmt', 'yuv420p', '-c:a', 'aac', '-b:a', '128k', '-movflags', '+faststart', OUT,
    ], stdin=subprocess.PIPE)

    elapsed = 0.0
    for si, (tag, num, title, body, dur) in enumerate(SLIDES):
        els = build_elements(tag, num, title, body)
        n = int(dur * FPS)
        for f in range(n):
            t = f / FPS
            frame = bg.copy()
            out_a = 1 - ease((t - (dur - 0.35)) / 0.35)
            for i, (e, y) in enumerate(els):
                k = ease((t - i * 0.12) / 0.5)
                a = k * out_a
                if a <= 0: continue
                e2 = e.copy()
                if a < 1:
                    e2.putalpha(e2.getchannel('A').point(lambda v, a=a: int(v * a)))
                frame.paste(e2, (int((1 - k) * 80), y + int((1 - k) * 60)), e2)
            d = ImageDraw.Draw(frame)
            # barra de progreso global + marca de agua
            p = (elapsed + t) / total
            d.rectangle([0, 0, W, 12], fill=(255, 255, 255))
            d.rectangle([0, 0, int(W * p), 12], fill=ACCENT)
            d.text((90, H - 170), f'{si + 1}/{len(SLIDES)}', font=font(FB, 40), fill=MUTED)
            if si == 0 and f == int(1.2 * FPS):
                frame.save(COVER, quality=92)
            proc.stdin.write(frame.tobytes())
        elapsed += dur
    proc.stdin.close(); proc.wait()
    print('Listo:', OUT, f'({total:.1f}s)')

if __name__ == '__main__':
    main()

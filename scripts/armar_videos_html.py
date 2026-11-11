"""Arma anuncios/src/video-a.html y video-d.html: un cuadro por plano, en 9:16 y 4:5.
Todo el texto va dentro de una caja de 1080x1000 que en 9:16 cae entre los 290 y los 1.290 px
de altura (zona segura de Reels, regla 07-creativos) y en 4:5 queda centrada.
Uso: python3 scripts/armar_videos_html.py  ->  después  node scripts/render_anuncios.js anuncios/src/video-a.html <carpeta>
"""
import pathlib
R = pathlib.Path(__file__).resolve().parent.parent
SRC = R / 'anuncios/src'

CSS = r'''
:root{--fondo:#ECE5DA;--verde:#0B6E5F;--verde-o:#084F45;--yo:#DCF8C6;--ink:#17201D;--mut:#5E6B66;--amar:#FFF4C2;--am2:#FFD84D;--noche:#0F1A17}
*{box-sizing:border-box;margin:0;padding:0}
body{background:#666;font-family:"Plus Jakarta Sans",sans-serif;color:var(--ink);-webkit-font-smoothing:antialiased}
.f{position:relative;overflow:hidden;margin:16px;background:var(--fondo);background-image:radial-gradient(rgba(11,110,95,.09) 2px,transparent 2.2px);background-size:36px 36px}
.v{width:1080px;height:1920px}.h{width:1080px;height:1350px}
.v .box{position:absolute;left:0;top:290px;width:1080px;height:1000px}
.h .box{position:absolute;left:0;top:175px;width:1080px;height:1000px}
.deco{position:absolute;left:0;right:0;bottom:0;height:630px;overflow:hidden}
.h .deco{display:none}
.deco img{width:100%;height:100%;object-fit:cover;filter:saturate(.9)}
.deco:before{content:"";position:absolute;inset:0;background:linear-gradient(var(--fondo),rgba(236,229,218,0) 45%)}
.dark .deco:before{background:linear-gradient(var(--noche),rgba(15,26,23,0) 45%)}
.green .deco:before{background:linear-gradient(var(--verde),rgba(11,110,95,0) 45%)}
.dark{background:var(--noche);background-image:none}
.green{background:var(--verde);background-image:none;color:#fff}
h1,h2,.bg{font-family:"Bricolage Grotesque",sans-serif;letter-spacing:-.03em;line-height:1;font-weight:800}
.eti{position:absolute;top:0;left:50%;transform:translateX(-50%);background:var(--amar);color:#6b5a12;font-weight:800;font-size:30px;padding:10px 22px;border-radius:12px;white-space:nowrap;z-index:5}
/* teléfono */
.tel{position:absolute;left:110px;right:110px;top:0;bottom:0;background:#17201D;border-radius:56px 56px 0 0;padding:14px 14px 0;box-shadow:0 30px 60px rgba(23,32,29,.25)}
.tel .bar{background:var(--verde);color:#fff;border-radius:44px 44px 0 0;padding:22px 26px;font-weight:700;font-size:30px;display:flex;gap:18px;align-items:center}
.tel .bar img{width:62px;height:62px;border-radius:50%;object-fit:cover}
.tel .bar small{display:block;font-weight:500;opacity:.85;font-size:22px}
.tel .chat{background:var(--fondo);position:absolute;left:14px;right:14px;top:120px;bottom:0;padding:22px 20px;display:flex;flex-direction:column;gap:14px;justify-content:flex-end;overflow:hidden}
.dark .tel .chat{background:#0B1411}
.m{max-width:86%;padding:16px 20px 34px;border-radius:22px;position:relative;box-shadow:0 1px 2px rgba(0,0,0,.12);font-size:37px;line-height:1.3}
.m .t{position:absolute;right:16px;bottom:6px;font-size:21px;color:#7a8a84}
.ell{background:#fff;align-self:flex-start;border-top-left-radius:5px}
.yo{background:var(--yo);align-self:flex-end;border-top-right-radius:5px}
.dark .ell{background:#1F2C28;color:#E9EFEC}.dark .yo{background:#0B5C4F;color:#E9EFEC}.dark .m .t{color:#9fb3ac}
.auto{align-self:center;font-size:21px;background:var(--amar);color:#6b5a12;padding:6px 14px;border-radius:10px;font-weight:700}
.dark .auto{background:#3a3a1e;color:#f4e7a0}
.input{display:flex;gap:12px;align-items:center;background:#fff;border-radius:40px;padding:16px 24px;font-size:32px;font-weight:600;color:var(--ink);margin-top:6px}
.input:after{content:"";width:3px;height:36px;background:var(--verde);animation:none}
.pop{background:#fff;border-radius:20px;box-shadow:0 10px 30px rgba(0,0,0,.18);padding:10px 0;font-size:26px}
.pop div{padding:12px 24px;border-bottom:1px solid #eee}.pop div:last-child{border:none}
.pop b{color:var(--verde)}
.pop .sel{background:#E7F4F0}
/* texto grande encima */
.grande{position:absolute;left:60px;right:60px;z-index:4;text-align:center}
.grande span{display:inline;background:var(--ink);color:#fff;font-family:"Bricolage Grotesque";font-weight:800;letter-spacing:-.03em;font-size:84px;line-height:1.22;padding:4px 22px;border-radius:16px;-webkit-box-decoration-break:clone;box-decoration-break:clone}
.grande.am span{background:var(--am2);color:var(--ink)}
.grande.top{top:40px}.grande.mid{top:380px}.grande.bot{bottom:40px}
/* lista de chats */
.lista{position:absolute;left:90px;right:90px;top:0;bottom:0;background:#fff;border-radius:36px;overflow:hidden;box-shadow:0 20px 50px rgba(23,32,29,.18)}
.lista .c{display:grid;grid-template-columns:84px 1fr auto;gap:22px;align-items:center;padding:20px 30px;border-bottom:1px solid #EFEAE2}
.lista .av{width:84px;height:84px;border-radius:50%;background:#C9D9D3}
.lista h3{font-size:32px;font-weight:700}.lista p{font-size:28px;color:var(--mut)}
.lista .n{background:#25A35A;color:#fff;border-radius:999px;font-weight:800;font-size:24px;min-width:46px;height:46px;display:flex;align-items:center;justify-content:center;padding:0 12px}
/* pantalla de IA */
.ia{position:absolute;left:90px;right:90px;top:0;bottom:0;background:#fff;border-radius:36px;overflow:hidden;box-shadow:0 20px 50px rgba(23,32,29,.18);padding:30px 34px;display:flex;flex-direction:column;gap:20px}
.ia .cab{font-weight:800;font-size:28px;color:var(--mut);display:flex;align-items:center;gap:14px}
.ia .cab i{width:40px;height:40px;border-radius:12px;background:var(--verde);display:inline-block}
.ia .pide{align-self:flex-end;background:#F1EFEA;border-radius:24px;padding:18px 22px;font-size:32px;line-height:1.35;max-width:88%}
.ia .resp{font-size:32px;line-height:1.32}
.ia .resp div{padding:12px 0;border-bottom:1px solid #eee}
.ia .resp b{font-family:ui-monospace,monospace;background:#E7F4F0;color:var(--verde);padding:2px 10px;border-radius:8px;margin-right:8px}
/* tarjetas */
.card{position:absolute;left:70px;right:70px;top:120px;bottom:60px;border-radius:40px;padding:70px 60px;display:flex;flex-direction:column;justify-content:center}
.big h1{font-size:120px}.big p{font-size:46px;font-weight:600;margin-top:30px;line-height:1.25}
.big h1 em{font-style:normal;color:var(--am2)}
/* ficha */
.ficha{position:absolute;left:110px;right:110px;top:70px;bottom:20px;background:#fff;border-radius:30px;border-left:12px solid var(--verde);padding:40px 44px;box-shadow:0 20px 50px rgba(23,32,29,.18);font-size:37px;line-height:1.4}
.ficha small{display:block;font-size:24px;font-weight:800;color:var(--verde);letter-spacing:.06em;margin-bottom:10px}
.ficha h3{font-family:"Bricolage Grotesque";font-size:44px;margin:18px 0 6px}
.ficha .hl{background:var(--am2);border-radius:6px;padding:0 6px}
/* retrato */
.ret{position:absolute;left:150px;right:150px;top:70px;height:780px;border-radius:40px;overflow:hidden;box-shadow:0 30px 60px rgba(23,32,29,.25)}
.ret img{width:100%;height:100%;object-fit:cover}
.ret.zoom img{transform:scale(1.35);transform-origin:50% 30%}
.nombre{position:absolute;left:60px;right:60px;top:880px;text-align:center;font-size:40px;font-weight:700}
.nombre b{color:var(--verde)}
/* tapa y cierre */
.tapa{position:absolute;width:400px;left:630px;top:110px;transform:rotate(4deg);border-radius:6px 16px 16px 6px;box-shadow:0 30px 60px rgba(0,0,0,.4)}
.cierre{position:absolute;left:60px;width:540px;top:130px}
.cierre .chip{display:inline-block;background:var(--am2);color:var(--ink);font-weight:800;font-size:28px;padding:10px 20px;border-radius:12px;letter-spacing:.05em}
.cierre h2{font-size:78px;margin:22px 0}
.cierre p{font-size:38px;font-weight:600;line-height:1.3}
.boton{position:absolute;left:70px;top:800px;background:var(--am2);color:var(--ink);font-weight:800;font-size:48px;padding:28px 50px;border-radius:24px;box-shadow:0 10px 0 #C9A400}
.green .cierre p{color:#E6F4EF}

.eti ~ .tel,.eti ~ .ficha{top:80px}
.eti ~ .ret{top:80px}
'''

FONT = '<link href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,700;12..96,800&family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">'

def page(frames, deco):
    out = ['<!doctype html><html lang="es"><head><meta charset="utf-8">', FONT, '<style>', CSS, '</style></head><body>']
    for fid, cls, body, dimg in frames:
        for size, suf in (('v', '9x16'), ('h', '4x5')):
            d = dimg if dimg is not None else deco
            dh = f'<div class="deco"><img src="{d}" alt=""></div>' if d else ''
            out.append(f'<div class="f {size} {cls}" data-out="{fid}-{suf}">{dh}<div class="box">{body}</div></div>')
    out.append('</body></html>')
    return '\n'.join(out)

A = '../../landing/assets/'
CARO = A + 'IMG-02.jpg'
TAPA = 'paginas/tapa.jpg'

def tel(header, msgs, extra='', avatar=CARO, sub='en línea'):
    return (f'<div class="tel"><div class="bar"><img src="{avatar}" alt=""><div>{header}<small>{sub}</small></div></div>'
            f'<div class="chat">{msgs}{extra}</div></div>')

def ell(t, h): return f'<div class="m ell">{t}<span class="t">{h}</span></div>'
def yo(t, h): return f'<div class="m yo">{t}<span class="t">{h} ✓✓</span></div>'
def grande(t, pos='top', am=False): return f'<div class="grande {pos}{" am" if am else ""}"><span>{t}</span></div>'

# ---------------------------------------------------------------- Video A · ¿Precio?
pre = ['¿precio?', 'Hola! precio?', '¿Precio del buzo?', 'precio 🙏', '¿Precio? ¿Hay talle M?']
CAROH = 'Malva · ejemplo del libro'
pre += ['¿precio?', 'hola, precio y talles?', '¿PRECIO?']
def flood(n): return ''.join(ell(pre[i], f'10:{12+i*7:02d}') for i in range(n))
LISTA = ''.join(f'<div class="c"><div class="av"></div><div><h3>{n}</h3><p>{p}</p></div><span class="n">{k}</span></div>'
                for n, p, k in [('Vicky', '¿precio?', 3), ('Lu', 'Hola! precio del buzo?', 2), ('Romi', '¿Precio? ¿Hacés envíos?', 4),
                                ('Pato', 'precio 🙏', 1), ('Juli', '¿Me pasás precio?', 2), ('Sabri', '¿precio?', 5), ('Flor', 'Holaa, ¿precio?', 1)])
IA_PIDE = ('<div class="ia"><div class="cab"><i></i>Tu chat con la IA · ChatGPT gratis</div>'
           '<div class="pide">Usando la ficha de mi negocio, escribime las respuestas para las 15 preguntas que más me hacen…</div>')
IA_RESP = ('<div class="resp"><div><b>/precios</b> ¡Hola! El buzo gris está $18.500. Hay S, M y L. ¿Qué talle buscás? 😊</div>'
           '<div><b>/envios</b> Mando por correo a todo el país, y si estás cerca, en el día por moto…</div>'
           '<div><b>/talles</b> Te paso los talles de cada prenda…</div><div><b>/pago</b> Transferencia o Mercado Pago…</div></div>')
RESP_PRECIOS = '¡Hola! El buzo gris está $18.500. Hay en S, M y L. Envío a todo el país o retiro en Lanús. ¿Qué talle buscás? 😊'
POP = ('<div class="pop"><div class="sel"><b>/precios</b> ¡Hola! El buzo gris está…</div><div><b>/envios</b> Mando por correo…</div>'
       '<div><b>/pago</b> Transferencia o Mercado Pago…</div></div>')
CIERRE_A = (f'<img class="tapa" src="{TAPA}" alt=""><div class="cierre"><span class="chip">DÍA 1</span>'
            '<h2>WhatsApp sin perder la tarde</h2><p>Una tarea por día, con ChatGPT gratis.</p></div>')
CTA = (f'<img class="tapa" src="{TAPA}" alt=""><div class="cierre"><h2>La IA hace, vos vendés</h2>'
       '<p>Ebook · 7 días · ChatGPT gratis</p></div><div class="boton">Tocá Comprar</div>')

FA = [
    ('a01', '', tel(CAROH, flood(3)) + grande('¿Precio?', 'mid', True), A + 'IMG-08.jpg'),
    ('a02', '', tel(CAROH, flood(5)) + grande('¿Precio? ¿Precio?', 'mid', True), A + 'IMG-08.jpg'),
    ('a03', '', tel(CAROH, flood(8)) + grande('¿Precio? ¿Precio? ¿Precio?', 'mid', True), A + 'IMG-08.jpg'),
    ('a04', '', f'<div class="lista">{LISTA}</div>' + grande('Lo contestás todo el día', 'bot'), A + 'IMG-08.jpg'),
    ('a05', 'green', '<div class="card big"><h1>Esto lo resolvés <em>en una hora.</em></h1></div>', ''),
    ('a06', '', IA_PIDE + '</div>' + grande('La IA escribe tus 15 respuestas', 'bot'), A + 'IMG-07.jpg'),
    ('a07', '', IA_PIDE + IA_RESP + '</div>' + grande('Con tus precios y tu forma de hablar', 'bot'), A + 'IMG-07.jpg'),
    ('a08', '', tel(CAROH, ell('Hola!! precio del buzo gris? 🙏', '21:47')) + grande('Te escriben «¿precio?»', 'top'), A + 'IMG-08.jpg'),
    ('a09', '', tel(CAROH, ell('Hola!! precio del buzo gris? 🙏', '21:47'), POP + '<div class="input">/precios</div>') + grande('Ponés /precios…', 'top'), A + 'IMG-08.jpg'),
    ('a10', '', tel(CAROH, ell('Hola!! precio del buzo gris? 🙏', '21:47') + yo(RESP_PRECIOS, '21:47')) + grande('…y sale la respuesta lista', 'top', True), A + 'IMG-08.jpg'),
    ('a11', 'green', CIERRE_A, ''),
    ('a12', 'green', CTA, ''),
]

# Ganchos de reserva de A (mismo cuerpo desde a06)
FR = [
    ('r2a', '', tel(CAROH, ell('Hola!! precio del buzo gris? 🙏', '21:47'), POP + '<div class="input">/precios</div>') + grande('Escribís /precios…', 'top'), A + 'IMG-08.jpg'),
    ('r2b', '', tel(CAROH, ell('Hola!! precio del buzo gris? 🙏', '21:47') + yo(RESP_PRECIOS, '21:47')) + grande('…y la respuesta sale sola', 'top', True), A + 'IMG-08.jpg'),
    ('r2c', 'green', '<div class="card big"><h1>Así se arma, <em>en una hora.</em></h1></div>', ''),
    ('r3a', 'dark', tel(CAROH, ell('¿precio?', '23:31') + ell('Hola, ¿precio del buzo?', '23:34'), sub='23:40') + grande('23:40', 'mid', True), A + 'IMG-12.jpg'),
    ('r3b', 'dark', tel(CAROH, ell('¿precio?', '23:31') + ell('Hola, ¿precio del buzo?', '23:34') + ell('precio 🙏', '23:39') + ell('¿Precio? ¿Hacés envíos?', '23:40'), sub='23:40') + grande('Y te siguen preguntando el precio', 'top'), A + 'IMG-12.jpg'),
    ('r3c', 'green', '<div class="card big"><h1>Esto lo resolvés <em>en una hora.</em></h1></div>', ''),
]

# ---------------------------------------------------------------- Video D · Sol
SOL = A + 'IMG-04.jpg'
ETI = '<div class="eti">Ejemplo del libro · no es una clienta</div>'
SOLH = 'Sol Nails &amp; Lashes · ejemplo'
FICHA1 = ('<div class="ficha"><small>📌 LA FICHA DE SOL (DÍA 0)</small><h3>Lo que hago</h3>Semipermanente $14.000 · Kapping $17.000<br>Esculpidas $24.000 · Pestañas $28.000'
          '<h3>Cómo se saca turno</h3>Por WhatsApp, con <span class="{a}">seña de $5.000</span> por transferencia.<br><span class="{b}">Lunes a sábado de 10 a 19.</span>'
          '<h3>Cómo hablo</h3>De vos, cálida. Pocos emojis 💅✨</div>')
TURNOS = (ell('Hola! tenés turno esta semana?', '9:05') + ell('precio del semi?', '9:40') + ell('cuánto dura el esculpido?', '11:12')
          + ell('hacés pestañas también?', '13:30') + ell('hay que dejar seña?', '15:02'))
SOL_PRE = '¡Hola! 💅 El semi está $14.000, kapping $17.000 y esculpidas $24.000. ¿Qué te gustaría hacerte?'
AUS = ('¡Hola, bella! 💅 Ahora no estoy atendiendo, mañana desde las 10 te respondo. Si querés turno, contame '
       '{a}qué te querés hacer y qué días podés{b}, así te lo guardo apenas pueda. ✨')
NOCHE = ell('hola! tenés turno el jueves?', '22:47')
CIERRE_D = (f'<img class="tapa" src="{TAPA}" alt=""><div class="cierre"><span class="chip">DÍA 1</span>'
            '<h2>Respuestas y mensaje de ausencia</h2><p>El ejemplo de Sol está en el libro.</p></div>')

FD = [
    ('d01', '', ETI + f'<div class="ret"><img src="{SOL}" alt=""></div>' + grande('Así arma Sol sus respuestas de turnos', 'bot'), ''),
    ('d02', '', ETI + f'<div class="ret zoom"><img src="{SOL}" alt=""></div><div class="nombre"><b>Sol</b> · uñas y pestañas · Rosario<br>Un negocio armado para el libro</div>', ''),
    ('d03', '', ETI + tel(SOLH, TURNOS, avatar=SOL), A + 'IMG-12.jpg'),
    ('d04', '', ETI + FICHA1.format(a='', b='') + grande('Primero cargó su ficha', 'bot', True), A + 'IMG-07.jpg'),
    ('d05', '', ETI + FICHA1.format(a='hl', b='hl') + grande('Precios, seña y horarios', 'bot', True), A + 'IMG-07.jpg'),
    ('d06', '', ETI + tel(SOLH, ell('Hola! precio del semi?', '9:40') + '<div class="auto">Respuesta escrita con IA · la revisó Sol</div>' + yo(SOL_PRE, '9:41'), avatar=SOL) + grande('Con su tono', 'mid', True), A + 'IMG-12.jpg'),
    ('d07', 'dark', ETI + tel(SOLH, NOCHE, avatar=SOL, sub='22:47') + grande('A la noche…', 'mid', True), ''),
    ('d08', 'dark', ETI + tel(SOLH, NOCHE + '<div class="auto">Mensaje de ausencia · se manda solo</div>' + yo(AUS.format(a='', b=''), '22:47'), avatar=SOL, sub='22:47'), ''),
    ('d09', 'dark', ETI + tel(SOLH, NOCHE + '<div class="auto">Mensaje de ausencia · se manda solo</div>' + yo(AUS.format(a='<b style="background:#FFD84D;color:#17201D;border-radius:6px;padding:0 6px">', b='</b>'), '22:47'), avatar=SOL, sub='22:47') + grande('Ya le pide los datos del turno', 'mid', True), ''),
    ('d10', 'green', CIERRE_D, ''),
    ('d11', 'green', CTA, ''),
]

(SRC / 'video-a.html').write_text(page(FA + FR, ''), encoding='utf-8')
(SRC / 'video-d.html').write_text(page(FD, ''), encoding='utf-8')
print('ok')

"""Tres direcciones de diseño para la landing (prototipos: arriba + los 7 días + precio). Solo para mirar.
Uso: python3 landing/propuestas/armar.py  -> landing/propuestas/{a-cuaderno,b-revista,c-chat}.html"""
import os
D = os.path.dirname(os.path.abspath(__file__))
A = '../assets/'
DIAS = [
 ('0','La ficha de tu negocio','La página que le cuenta a la IA quién sos. La armás una vez y la usás siempre.','IMG-07'),
 ('1','WhatsApp sin perder la tarde','Tus 15 respuestas más usadas, cargadas como respuestas rápidas.','IMG-08'),
 ('2','Instagram sin quedarte en blanco','30 ideas, una semana de posteos en tu voz y tu biografía renovada.','IMG-09'),
 ('3','Vender más con lo que ya tenés','Descripciones que venden y mensajes para el que preguntó y no compró.','IMG-10'),
 ('4','Los números sin dolor de cabeza','Cuánto te cuesta de verdad, con tus horas, y un precio que te cierre.','IMG-11'),
 ('5','Clientes difíciles','El reclamo, el que regatea, el que cancela y la mala reseña.','IMG-12'),
 ('6','Promos e ideas','Tu calendario del año y promos que no te hacen perder plata.','IMG-13'),
 ('7','Tu semana en orden','Pedidos, agenda y una rutina de 20 minutos por día.','IMG-14'),
]
TRAE = ['El libro completo: Día 0, los 7 días y qué hacer la semana 2','40 instrucciones para copiar y pegar en ChatGPT',
        'La plantilla de la ficha de tu negocio','Ejemplos en 4 rubros en cada día','Una tarea para tildar al final de cada día']
SUB = 'Cómo usar la IA en tu emprendimiento en 7 días, aunque no sepas nada de tecnología.'
APOYO = 'Una tarea por día, una hora por día. Al final de la semana, la IA te contesta WhatsApp, te escribe los posteos y te ayuda con los precios, con tus datos y tu forma de hablar.'
GAR = 'Garantía de 7 días, sin preguntas. Si no te sirve, escribinos a tallertriplearg@gmail.com y te devolvemos la plata.'
P = '$ 7.990'
HEAD = lambda t, fonts, css: f'''<!doctype html><html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{t}</title><link href="https://fonts.googleapis.com/css2?{fonts}&display=swap" rel="stylesheet"><style>*{{box-sizing:border-box;margin:0;padding:0}}img{{display:block;max-width:100%}}{css}</style></head><body>'''

# ---------- A · CUADERNO ----------
A_CSS = '''
:root{--p:#F3EDE2;--ink:#1D2433;--mut:#5B5F6B;--red:#D9482B;--hl:#FFE36B;--line:#D9CFBE}
body{background:var(--p);color:var(--ink);font:17px/1.6 "Instrument Sans",system-ui,sans-serif}
.w{max-width:1080px;margin:0 auto;padding:0 22px}
h1,h2{font-family:Fraunces,Georgia,serif;font-weight:700;letter-spacing:-.015em;line-height:1.02;font-variation-settings:"SOFT" 100,"WONK" 1}
.mano{font-family:Caveat,cursive;color:var(--red);font-size:26px;line-height:1.1}
mark{background:linear-gradient(transparent 55%,var(--hl) 55%,var(--hl) 92%,transparent 92%);color:inherit;padding:0 .08em}
.btn{display:inline-block;background:var(--ink);color:var(--p);font-weight:700;font-size:18px;padding:17px 28px;text-decoration:none;border-radius:4px;box-shadow:5px 5px 0 var(--red)}
.top{padding:22px 0;border-bottom:1.5px solid var(--ink)}
.top .w{display:flex;justify-content:space-between;align-items:center;font-weight:700}
.top span{font-family:Caveat;font-size:24px;color:var(--red);font-weight:400}
.hero{padding:56px 0 70px}
.hero .w{display:grid;grid-template-columns:1.15fr .85fr;gap:56px;align-items:center}
.hero h1{font-size:clamp(50px,8.4vw,96px)}
.hero .sub{font-size:clamp(20px,2.6vw,24px);margin:22px 0 12px;font-weight:600}
.hero .apoyo{color:var(--mut);max-width:520px;margin-bottom:30px}
.nota{font-size:14px;color:var(--mut);margin-top:16px}
.foto{position:relative;transform:rotate(2deg);background:#fff;padding:12px 12px 52px;box-shadow:0 14px 30px rgba(29,36,51,.18)}
.foto img{aspect-ratio:4/5;object-fit:cover;width:100%}
.foto .mano{position:absolute;bottom:10px;left:16px;color:var(--ink)}
.cinta{position:absolute;top:-14px;left:50%;width:110px;height:30px;background:rgba(255,227,107,.8);transform:translateX(-50%) rotate(-4deg)}
.flecha{position:absolute;left:-118px;top:30%;width:130px}
.hoja{background:#FFFDF8;border:1.5px solid var(--ink);border-radius:6px;padding:46px 0 30px;margin:0 0 70px;
 background-image:repeating-linear-gradient(transparent 0 37px,var(--line) 37px 38px);position:relative}
.hoja:before{content:"";position:absolute;left:78px;top:0;bottom:0;border-left:2px solid #EFA79A}
.hoja h2{font-size:clamp(34px,5vw,52px);padding:0 30px 0 104px;margin-bottom:6px}
.hoja .intro{padding:0 30px 0 104px;color:var(--mut);margin-bottom:22px}
.item{display:grid;grid-template-columns:58px 1fr 150px;gap:22px;align-items:center;padding:14px 30px 14px 30px}
.chk{width:30px;height:30px;border:2px solid var(--ink);border-radius:4px;position:relative;justify-self:end}
.chk:after{content:"✓";position:absolute;left:3px;top:-14px;font-family:Caveat;font-size:44px;color:var(--red)}
.item .n{font-family:Caveat;font-size:24px;color:var(--red)}
.item h3{font-family:Fraunces,serif;font-size:22px;font-weight:600;line-height:1.15}
.item p{color:var(--mut);font-size:15.5px}
.item img{width:150px;aspect-ratio:3/2;object-fit:cover;border-radius:3px;transform:rotate(-1.5deg);box-shadow:0 4px 10px rgba(0,0,0,.12)}
.item:nth-child(even) img{transform:rotate(1.5deg)}
.precio{border-top:1.5px solid var(--ink);padding:64px 0 90px}
.precio .w{display:grid;grid-template-columns:1fr 1fr;gap:50px;align-items:start}
.precio h2{font-size:clamp(36px,5vw,56px)}
.ticket{background:#fff;border:1.5px solid var(--ink);padding:30px;border-radius:6px;box-shadow:8px 8px 0 var(--ink)}
.ticket ul{list-style:none;margin:6px 0 22px}.ticket li{padding:9px 0 9px 30px;border-bottom:1px dashed var(--line);position:relative}
.ticket li:before{content:"→";position:absolute;left:0;color:var(--red);font-weight:700}
.monto{font-family:Fraunces,serif;font-size:58px;font-weight:700;line-height:1}
.sello{display:flex;gap:12px;align-items:center;margin-top:20px;font-size:14px;color:var(--mut)}
.sello b{flex:none;width:64px;height:64px;border:2px solid var(--red);border-radius:50%;display:grid;place-items:center;color:var(--red);font-family:Caveat;font-size:22px;transform:rotate(-10deg);line-height:.9;text-align:center}
@media(max-width:820px){body{font-size:16px}.hero{padding:30px 0 50px}.hero .w,.precio .w{grid-template-columns:1fr;gap:34px}
.foto{width:72%;margin:0 auto}.flecha{display:none}.btn{display:block;text-align:center}
.hoja:before{left:40px}.hoja h2,.hoja .intro{padding:0 18px 0 56px}.item{grid-template-columns:34px 1fr;padding:12px 16px 12px 8px;gap:14px}.item img{display:none}.item h3{font-size:19px}}
'''
def a():
    items = ''.join(f'<div class="item"><span class="chk"></span><div><div class="n">Día {n}</div><h3>{t}</h3><p>{d}</p></div><img src="{A}{i}.jpg" alt=""></div>' for n,t,d,i in DIAS)
    return HEAD('A · Cuaderno','family=Fraunces:opsz,wght,SOFT,WONK@9..144,600..700,100,1&family=Instrument+Sans:wght@400;600;700&family=Caveat:wght@500',A_CSS)+f'''
<div class="top"><div class="w">La IA hace, vos vendés <span>ebook · 7 días</span></div></div>
<section class="hero"><div class="w"><div>
<div class="mano">para emprendedores que venden por WhatsApp e Instagram</div>
<h1>La IA hace,<br><mark>vos vendés.</mark></h1>
<p class="sub">{SUB}</p><p class="apoyo">{APOYO}</p>
<a class="btn" href="/checkout">Quiero el libro · {P}</a><p class="nota">PDF por mail apenas se acredita el pago · Garantía de 7 días</p></div>
<div class="foto"><span class="cinta"></span><img src="{A}IMG-01.jpg" alt=""><span class="mano">una hora por día, con el mate al lado</span></div>
</div></section>
<div class="w"><div class="hoja"><h2>Tu semana, día por día</h2><p class="intro">Cada día termina con algo hecho y funcionando. Lo tildás y seguís.</p>{items}</div></div>
<section class="precio"><div class="w"><div><div class="mano">lo que te llevás</div><h2>Todo listo para usar, por {P}</h2><p class="apoyo" style="margin-top:18px">Sin suscripción ni cuotas: pagás una vez con Mercado Pago y el PDF es tuyo.</p></div>
<div class="ticket"><ul>{''.join(f'<li>{x}</li>' for x in TRAE)}</ul><div class="monto">{P}</div>
<a class="btn" style="margin-top:20px" href="/checkout">Quiero el libro</a><div class="sello"><b>7 días<br>garantía</b><span>{GAR}</span></div></div></div></section></body></html>'''

# ---------- B · REVISTA ----------
B_CSS = '''
:root{--bg:#FAF8F3;--ink:#121212;--mut:#57534C;--acc:#C8361F;--rule:#121212}
body{background:var(--bg);color:var(--ink);font:17px/1.6 "Newsreader",Georgia,serif}
.sans{font-family:"Archivo",system-ui,sans-serif}
.w{max-width:1180px;margin:0 auto;padding:0 24px}
h1,h2{font-family:"DM Serif Display",Georgia,serif;font-weight:400;line-height:.95;letter-spacing:-.01em}
.btn{display:inline-block;background:var(--acc);color:#fff;font:700 15px/1 Archivo,sans-serif;letter-spacing:.06em;text-transform:uppercase;padding:20px 30px;text-decoration:none}
.mast{border-bottom:3px double var(--rule)}
.mast .w{display:flex;justify-content:space-between;padding:16px 24px;font:600 13px Archivo,sans-serif;letter-spacing:.08em;text-transform:uppercase}
.hero .w{display:grid;grid-template-columns:7fr 5fr;gap:0;border-bottom:1px solid var(--rule)}
.hero .txt{padding:60px 48px 56px 0;border-right:1px solid var(--rule)}
.hero h1{font-size:clamp(64px,10.5vw,148px)}
.hero h1 em{color:var(--acc);font-style:italic}
.hero .sub{font-size:clamp(21px,2.4vw,26px);margin:26px 0 14px;font-style:italic;max-width:560px}
.hero .apoyo{color:var(--mut);max-width:520px;margin-bottom:32px}
.hero .img{position:relative}.hero .img img{width:100%;height:100%;object-fit:cover}
.hero .cap{position:absolute;left:0;bottom:0;background:var(--bg);font:12px Archivo,sans-serif;padding:8px 12px;color:var(--mut)}
.nota{font:13px Archivo,sans-serif;color:var(--mut);margin-top:14px}
.dias{padding:70px 0}
.dias .cab{display:grid;grid-template-columns:5fr 7fr;gap:40px;align-items:end;margin-bottom:34px}
.dias h2{font-size:clamp(44px,6vw,80px)}
.dias .cab p{color:var(--mut);font-size:19px}
.grid{display:grid;grid-template-columns:repeat(4,1fr);border-top:1px solid var(--rule)}
.d{padding:22px 22px 30px 0;border-bottom:1px solid var(--rule)}
.d+.d{padding-left:22px;border-left:1px solid var(--rule)}.d:nth-child(4n+1){border-left:none;padding-left:0}
.num{font-family:"DM Serif Display",serif;font-size:96px;line-height:.8;color:var(--acc)}
.d h3{font:700 18px/1.2 Archivo,sans-serif;margin:14px 0 8px}
.d p{color:var(--mut);font-size:16px}
.d img{margin-top:16px;aspect-ratio:4/3;object-fit:cover;width:100%;filter:saturate(.85)}
.precio{background:var(--ink);color:var(--bg);padding:80px 0}
.precio .w{display:grid;grid-template-columns:1fr 1fr;gap:60px}
.precio h2{font-size:clamp(44px,6vw,84px)}.precio h2 em{color:#F08A6E;white-space:nowrap}
.precio ol{list-style:none;counter-reset:c;margin-bottom:28px}
.precio li{counter-increment:c;padding:14px 0;border-bottom:1px solid #444;display:flex;gap:18px;font-size:18px}
.precio li:before{content:counter(c,decimal-leading-zero);font:700 13px Archivo,sans-serif;color:#F08A6E;padding-top:5px}
.monto{font-family:"DM Serif Display",serif;font-size:76px;line-height:1;margin:6px 0 18px}
.gar{font:14px/1.5 Archivo,sans-serif;color:#bdb8ae;margin-top:18px;border-top:1px solid #444;padding-top:16px}
@media(max-width:820px){body{font-size:16px}.hero .w{grid-template-columns:1fr}.hero .txt{padding:36px 0 40px;border-right:none}.hero .img{order:-1;margin:0 -24px}.hero .img img{aspect-ratio:4/3}
.dias .cab,.precio .w{grid-template-columns:1fr;gap:16px}.grid{grid-template-columns:1fr 1fr}.d,.d+.d{padding:18px 14px 22px 0;border-left:none}.d:nth-child(even){padding-left:14px;border-left:1px solid var(--rule)}.num{font-size:70px}.btn{display:block;text-align:center}.precio .w{gap:36px}}
'''
def b():
    g=''.join(f'<div class="d"><div class="num">{n}</div><h3>{t}</h3><p>{d}</p><img src="{A}{i}.jpg" alt=""></div>' for n,t,d,i in DIAS)
    return HEAD('B · Revista','family=DM+Serif+Display:ital@0;1&family=Newsreader:ital,opsz,wght@0,6..72,400;1,6..72,400&family=Archivo:wght@400;600;700',B_CSS)+f'''
<div class="mast"><div class="w"><span>La IA hace, vos vendés</span><span>Ebook · 69 páginas · PDF</span></div></div>
<section class="hero"><div class="w"><div class="txt"><h1>La IA hace, <em>vos vendés.</em></h1>
<p class="sub">{SUB}</p><p class="apoyo">{APOYO}</p><a class="btn" href="/checkout">Quiero el libro — {P}</a><p class="nota">PDF por mail apenas se acredita el pago · Garantía de 7 días</p></div>
<div class="img"><img src="{A}IMG-01.jpg" alt=""><span class="cap">Una hora por día. Con ChatGPT gratis.</span></div></div></section>
<section class="dias"><div class="w"><div class="cab"><h2>Ocho días. Una tarea por día.</h2><p>Arrancás con el Día 0, que es la preparación. Cada día termina con algo hecho y funcionando.</p></div><div class="grid">{g}</div></div></section>
<section class="precio"><div class="w"><div><h2>Todo lo que trae, por <em>{P}.</em></h2></div><div><ol>{''.join(f'<li>{x}</li>' for x in TRAE)}</ol>
<div class="monto">{P}</div><a class="btn" href="/checkout">Quiero el libro</a><p class="gar">{GAR}</p></div></div></section></body></html>'''

# ---------- C · CHAT ----------
C_CSS = '''
:root{--fondo:#ECE5DA;--verde:#0B6E5F;--verde2:#1FA855;--yo:#DCF8C6;--ink:#17201D;--mut:#5E6B66}
body{background:var(--fondo);color:var(--ink);font:17px/1.55 "Plus Jakarta Sans",system-ui,sans-serif;
 background-image:radial-gradient(rgba(11,110,95,.07) 1.2px,transparent 1.3px);background-size:22px 22px}
.w{max-width:1100px;margin:0 auto;padding:0 22px}
h1,h2{font-family:"Bricolage Grotesque",sans-serif;font-weight:800;letter-spacing:-.03em;line-height:.98}
.btn{display:inline-flex;gap:10px;align-items:center;background:var(--verde);color:#fff;font-weight:700;font-size:18px;padding:17px 26px;border-radius:14px;text-decoration:none}
.hero{padding:64px 0 76px}.hero .w{display:grid;grid-template-columns:1.1fr .9fr;gap:56px;align-items:center}
.hero h1{font-size:clamp(50px,8vw,92px)}.hero h1 span{color:var(--verde)}
.hero .sub{font-size:clamp(20px,2.5vw,24px);margin:22px 0 12px;font-weight:600}
.hero .apoyo{color:var(--mut);max-width:520px;margin-bottom:28px}
.nota{font-size:14px;color:var(--mut);margin-top:14px}
.tel{background:#fff;border-radius:34px;padding:12px;box-shadow:0 30px 60px rgba(23,32,29,.22);max-width:360px;margin:0 auto;border:8px solid #17201D}
.tel .bar{background:var(--verde);color:#fff;border-radius:20px 20px 0 0;padding:12px 16px;font-weight:700;font-size:15px;display:flex;gap:10px;align-items:center}
.tel .bar i{width:30px;height:30px;border-radius:50%;background:url(%%A%%IMG-02.jpg) center/cover}
.tel .bar small{display:block;font-weight:400;opacity:.8;font-size:12px}
.chat{background:var(--fondo);padding:16px 12px 20px;display:flex;flex-direction:column;gap:8px;font-size:14.5px;border-radius:0 0 20px 20px}
.m{max-width:84%;padding:8px 11px 18px;border-radius:10px;position:relative;box-shadow:0 1px 1px rgba(0,0,0,.08)}
.m .h{position:absolute;right:8px;bottom:3px;font-size:10.5px;color:#7a8a84}
.ell{background:#fff;align-self:flex-start;border-top-left-radius:2px}
.yo{background:var(--yo);align-self:flex-end;border-top-right-radius:2px}
.ia{align-self:center;font-size:11.5px;background:#FFF4C2;color:#6b5a12;padding:4px 10px;border-radius:8px}
.sec{padding:70px 0}.sec h2{font-size:clamp(38px,5.4vw,62px);max-width:760px}
.sec .intro{color:var(--mut);font-size:19px;margin:14px 0 34px;max-width:620px}
.hilo{display:grid;grid-template-columns:1fr 1fr;gap:16px 28px}
.dm{display:grid;grid-template-columns:72px 1fr;gap:14px;background:#fff;border-radius:16px;border-top-left-radius:4px;padding:14px;box-shadow:0 1px 2px rgba(0,0,0,.07)}
.dm img{width:72px;height:72px;object-fit:cover;border-radius:12px}
.dm .n{font-size:12px;font-weight:800;color:var(--verde);letter-spacing:.04em}
.dm h3{font-family:"Bricolage Grotesque";font-size:20px;line-height:1.15;margin:2px 0 4px}
.dm p{font-size:15px;color:var(--mut)}
.precio{background:var(--verde);color:#fff;padding:76px 0}.precio .w{display:grid;grid-template-columns:1fr 1fr;gap:50px;align-items:center}
.precio h2{font-size:clamp(40px,5.5vw,66px)}
.recibo{background:#fff;color:var(--ink);border-radius:20px;padding:28px}
.recibo li{list-style:none;padding:10px 0 10px 30px;position:relative;border-bottom:1px solid #eee}
.recibo li:before{content:"✓✓";position:absolute;left:0;color:#34B7F1;font-size:13px;font-weight:700;top:13px;letter-spacing:-3px}
.monto{font-family:"Bricolage Grotesque";font-size:60px;font-weight:800;margin:18px 0 14px;line-height:1}
.gar{font-size:14px;color:var(--mut);margin-top:16px}
@media(max-width:820px){body{font-size:16px}.hero{padding:34px 0 50px}.hero .w,.precio .w{grid-template-columns:1fr;gap:36px}.hilo{grid-template-columns:1fr}.btn{display:flex;justify-content:center}.tel{max-width:320px}}
'''.replace('%%A%%',A)
def c():
    h=''.join(f'<div class="dm"><img src="{A}{i}.jpg" alt=""><div><div class="n">DÍA {n}</div><h3>{t}</h3><p>{d}</p></div></div>' for n,t,d,i in DIAS)
    return HEAD('C · Chat','family=Bricolage+Grotesque:opsz,wght@12..96,800&family=Plus+Jakarta+Sans:wght@400;600;700',C_CSS)+f'''
<section class="hero"><div class="w"><div><h1>La IA hace, <span>vos vendés.</span></h1>
<p class="sub">{SUB}</p><p class="apoyo">{APOYO}</p><a class="btn" href="/checkout">Quiero el libro · {P}</a><p class="nota">PDF por mail apenas se acredita el pago · Garantía de 7 días</p></div>
<div class="tel"><div class="bar"><i></i><div>Ejemplo · Caro, ropa<small>en línea</small></div></div><div class="chat">
<div class="m ell">Hola!! precio del buzo gris? 🙏<span class="h">21:47</span></div>
<div class="ia">Respuesta escrita con IA a partir de tu ficha · la revisás vos</div>
<div class="m yo">¡Hola! El buzo gris está $18.500. Hay en S, M y L. Envío a todo el país o retiro en Lanús, y aceptamos transferencia o Mercado Pago. ¿Qué talle buscás? 😊<span class="h">21:48 ✓✓</span></div>
<div class="m ell">M! y llega antes del sábado?<span class="h">21:48</span></div>
</div></div></div></section>
<section class="sec"><div class="w"><h2>Una tarea por día. Al final, la IA ya sabe cómo es tu negocio.</h2><p class="intro">Arrancás con el Día 0, que es la preparación. Cada día termina con algo hecho y funcionando.</p><div class="hilo">{h}</div></div></section>
<section class="precio"><div class="w"><div><h2>Todo listo para usar, por {P}.</h2></div><div class="recibo"><ul>{''.join(f'<li>{x}</li>' for x in TRAE)}</ul>
<div class="monto">{P}</div><a class="btn" href="/checkout">Quiero el libro</a><p class="gar">{GAR}</p></div></div></section></body></html>'''

for n,f in [('a-cuaderno',a),('b-revista',b),('c-chat',c)]:
    open(os.path.join(D,n+'.html'),'w').write(f())
print('ok')

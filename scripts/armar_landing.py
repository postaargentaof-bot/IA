"""Arma la landing y la página del upsell post-compra para Impultienda (HTML propio).

Uso:
  python3 scripts/armar_landing.py            -> landing/landing.html y landing/postcompra.html
  python3 scripts/armar_landing.py --preview  -> landing/preview/*.html (imágenes locales, tokens con valores de ejemplo)

Las imágenes salen de scripts/imagenes.py; se copian livianas (JPEG) a landing/assets/IMG-xx.jpg.
Para la versión de Impultienda, las direcciones de cada imagen y mockup se cargan en
imagenes/urls.json ({"IMG-01": "https://...", "tapa-ebook.png": "https://...", ...}) después de
subirlas a Diseño de tienda → Recursos. Mientras no tengan dirección salen como RECURSO:<archivo>.
Los mockups (tapas y páginas del libro) salen de los PDF reales: landing/assets/.
"""
import os, sys, json, subprocess, html
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import imagenes
from imagenes import IMAGENES

ROOT = imagenes.ROOT
PREVIEW = '--preview' in sys.argv
OUT = os.path.join(ROOT, 'landing', 'preview' if PREVIEW else '')
ASSETS = os.path.join(ROOT, 'landing', 'assets')
os.makedirs(OUT, exist_ok=True); os.makedirs(ASSETS, exist_ok=True)
URLS = {}
up = os.path.join(imagenes.CARPETA, 'urls.json')
if os.path.exists(up):
    URLS = json.load(open(up))

# ---------- mockups reales desde los PDF ----------
def pdf_png(pdf, page, name, res=110):
    dst = os.path.join(ASSETS, name)
    subprocess.run(['pdftoppm', '-r', str(res), '-png', '-singlefile', '-f', str(page), '-l', str(page),
                    os.path.join(ROOT, 'pdf', pdf), dst[:-4]], check=True, stderr=subprocess.DEVNULL)
    return name
def pagina(pdf, texto):
    """Número de página (1…) del PDF que tiene `texto` al principio (las páginas se corren al cambiar el libro)."""
    from pypdf import PdfReader
    for i, pg in enumerate(PdfReader(os.path.join(ROOT, 'pdf', pdf)).pages):
        if texto in (pg.extract_text() or '')[:80]:
            return i + 1
    raise SystemExit(f'No encontré la página que empieza con «{texto}» en {pdf}')
EB = 'la-ia-hace-vos-vendes.pdf'
MOCK = {
    'tapa': pdf_png(EB, 1, 'tapa-ebook.png'),
    'p1': pdf_png(EB, pagina(EB, 'Día 0 · La ficha'), 'pagina-ficha.png'),
    'p2': pdf_png(EB, pagina(EB, 'Bajá WhatsApp Business'), 'pagina-whatsapp.png'),
    'p3': pdf_png(EB, pagina(EB, 'La cobraba $45.000'), 'pagina-numeros.png'),
    't200': pdf_png('las-200-instrucciones.pdf', 1, 'tapa-200.png'),
}
# Copias livianas de las fotos para la web (las que se suben a Recursos de Impultienda).
USADAS = ['IMG-01', 'IMG-02', 'IMG-03', 'IMG-04', 'IMG-05', 'IMG-07', 'IMG-08', 'IMG-09', 'IMG-10',
          'IMG-11', 'IMG-12', 'IMG-13', 'IMG-14', 'IMG-15', 'IMG-31']
for _id in USADAS:
    imagenes.jpg(_id, ASSETS, 1600, 82)
def asset(name):
    if PREVIEW:
        return '../assets/' + name  # relativo: la vista previa anda en cualquier compu con el repo
    return URLS.get(name, f'RECURSO:{name}')

def img(id_, cls=''):
    """La foto. En la versión de Impultienda, sin dirección cargada en urls.json sale como
    RECURSO:IMG-xx.jpg (el archivo está en landing/assets/): se reemplaza al subirla a Recursos."""
    w, h = imagenes.PROPORCION[IMAGENES[id_][0]]
    nombre = f'{id_}.jpg'
    if not os.path.exists(os.path.join(ASSETS, nombre)):
        return imagenes.slot(id_, cls)  # no hay imagen: recuadro con el código
    src = asset(nombre) if PREVIEW else URLS.get(id_, URLS.get(nombre, f'RECURSO:{nombre}'))
    return f'<img class="img {cls}" style="aspect-ratio:{w}/{h}" src="{src}" alt="">'

PRICE = '$7.990' if PREVIEW else '{{price}}'

CSS = """
:root{--v:#5B3FD1;--vd:#2E1F73;--am:#FFD84D;--cr:#FFF8EC;--tx:#1E1A2E;--soft:#F3EFFD;--mut:#5d5873}
*{box-sizing:border-box;margin:0;padding:0}
html{scroll-behavior:smooth}
body{font-family:Inter,system-ui,-apple-system,Segoe UI,Roboto,sans-serif;color:var(--tx);background:#fff;line-height:1.55;font-size:17px;-webkit-font-smoothing:antialiased}
.w{max-width:1040px;margin:0 auto;padding:0 20px}
section{padding:64px 0}
h1,h2,h3{line-height:1.08;letter-spacing:-.02em;font-weight:900;color:var(--vd)}
h2{font-size:clamp(30px,5.4vw,46px);margin-bottom:18px}
h3{font-size:20px;font-weight:800}
.k{font-size:13px;font-weight:800;letter-spacing:.14em;text-transform:uppercase;color:var(--v);margin-bottom:12px}
.lead{font-size:clamp(18px,2.4vw,21px);color:var(--mut);max-width:680px}
.btn{display:inline-flex;align-items:center;justify-content:center;gap:10px;background:var(--am);color:var(--vd);font-weight:900;font-size:19px;padding:18px 30px;border-radius:999px;text-decoration:none;border:none;cursor:pointer;box-shadow:0 6px 0 #E0B91F;transition:transform .12s}
.btn:active{transform:translateY(3px);box-shadow:0 3px 0 #E0B91F}
.nota{font-size:14px;color:var(--mut);margin-top:12px}
.img{width:100%;display:block;border-radius:22px;object-fit:cover}
.ph-img{background:linear-gradient(135deg,#ECE6FF,#FFF3D1);display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;padding:16px;border:2px dashed #C9BDF3}
.ph-id{background:var(--v);color:#fff;font-size:12px;font-weight:800;letter-spacing:.06em;padding:4px 10px;border-radius:6px}
.ph-txt{font-size:13px;color:#6E6590;margin-top:8px;max-width:85%;line-height:1.35}
/* hero */
.hero{background:var(--vd);color:#fff;padding:0;position:relative;overflow:hidden}
.hero .bg{position:absolute;inset:0;opacity:.35}
.hero .bg .img{height:100%;border-radius:0;aspect-ratio:auto!important}
.hero .bg .ph-txt,.hero .bg .ph-id{display:none}
.hero .bg:after{content:"";position:absolute;inset:0;background:linear-gradient(90deg,var(--vd) 30%,rgba(46,31,115,.55))}
.hero .w{position:relative;display:grid;grid-template-columns:1.2fr .8fr;gap:40px;align-items:center;padding-top:72px;padding-bottom:72px}
.hero h1{color:#fff;font-size:clamp(46px,8vw,80px)}
.hero .k{color:var(--am)}
.hero .sub{font-size:clamp(20px,2.8vw,25px);margin:18px 0 14px;font-weight:600}
.hero .apoyo{opacity:.88;margin-bottom:30px;max-width:560px}
.hero .nota{color:#d8d2f5}
.libro{position:relative;justify-self:center;width:min(320px,80%)}
.libro img{width:100%;border-radius:6px 14px 14px 6px;box-shadow:-14px 22px 40px rgba(0,0,0,.45),inset 4px 0 0 rgba(255,255,255,.3);transform:perspective(900px) rotateY(-14deg) rotateZ(1deg)}
/* problema */
.prob{background:var(--cr)}
.cards{display:grid;grid-template-columns:repeat(2,1fr);gap:14px;margin:26px 0}
.card{background:#fff;border-radius:18px;padding:20px 22px;font-weight:600;box-shadow:0 2px 0 rgba(46,31,115,.07)}
.card b{display:block;font-size:28px;margin-bottom:4px}
.remate{font-size:21px;max-width:720px}
/* idea */
.dos{display:grid;grid-template-columns:1fr 1fr;gap:44px;align-items:center}
.ficha{background:var(--soft);border:2px solid var(--v);border-radius:20px;padding:22px 24px;margin-top:22px}
.ficha .tag{display:inline-block;background:var(--v);color:#fff;font-size:12px;font-weight:800;letter-spacing:.08em;padding:4px 10px;border-radius:6px;margin-bottom:10px}
/* dias */
.dias{display:grid;grid-template-columns:repeat(4,1fr);gap:16px;margin-top:30px}
.dia{background:#fff;border:1.5px solid #E7E1FA;border-radius:20px;overflow:hidden;display:flex;flex-direction:column}
.dia .img{border-radius:0}
.dia .t{padding:16px 18px 20px}
.dia .n{font-size:12px;font-weight:900;letter-spacing:.12em;color:var(--v);text-transform:uppercase}
.dia h3{margin:4px 0 8px;font-size:18px}
.dia p{font-size:15px;color:var(--mut)}
.tiempo{margin-top:22px;color:var(--mut);font-size:15px}
/* trae */
.trae{background:var(--vd);color:#fff}
.trae h2{color:#fff}.trae .k{color:var(--am)}
.lista{list-style:none;margin:24px 0}
.lista li{padding:12px 0 12px 40px;position:relative;border-bottom:1px solid rgba(255,255,255,.14)}
.lista li:before{content:"";position:absolute;left:0;top:15px;width:22px;height:22px;border-radius:7px;background:var(--am)}
.lista li:after{content:"";position:absolute;left:7px;top:19px;width:6px;height:11px;border:solid var(--vd);border-width:0 3px 3px 0;transform:rotate(45deg)}
.paginas{position:relative;height:420px}
.paginas img{position:absolute;width:58%;border-radius:8px;box-shadow:0 18px 40px rgba(0,0,0,.4)}
.paginas img:nth-child(1){left:0;top:40px;transform:rotate(-6deg)}
.paginas img:nth-child(2){left:22%;top:0;z-index:2}
.paginas img:nth-child(3){right:0;top:50px;transform:rotate(6deg)}
/* negocios */
.negocios{display:grid;grid-template-columns:repeat(4,1fr);gap:16px;margin-top:28px}
.neg{text-align:center}
.neg .img{border-radius:50%;width:78%;margin:0 auto 12px}
.neg h3{font-size:17px}.neg p{font-size:14px;color:var(--mut)}
.aclara{margin-top:22px;font-size:14px;color:var(--mut);background:var(--cr);border-radius:12px;padding:12px 16px;display:inline-block}
/* para quien */
.quien{background:var(--soft)}
.col{background:#fff;border-radius:22px;padding:26px}
.col h3{margin-bottom:14px}
.col ul{list-style:none}
.col li{padding:9px 0 9px 32px;position:relative;font-size:16px}
.si li:before{content:"✓";position:absolute;left:0;color:#1E9E5A;font-weight:900}
.no li:before{content:"✕";position:absolute;left:0;color:#C2413B;font-weight:900}
/* sin letra chica */
.chica{display:grid;grid-template-columns:repeat(2,1fr);gap:16px;margin-top:24px}
.chica div{border-left:5px solid var(--am);background:var(--cr);border-radius:0 16px 16px 0;padding:16px 20px;font-size:16px}
/* faq */
details{border-bottom:1.5px solid #E7E1FA;padding:18px 0}
summary{cursor:pointer;font-weight:800;font-size:18px;list-style:none;display:flex;justify-content:space-between;gap:16px;color:var(--vd)}
summary::-webkit-details-marker{display:none}
summary:after{content:"+";color:var(--v);font-size:24px;line-height:1}
details[open] summary:after{content:"–"}
details p{margin-top:10px;color:var(--mut)}
/* cierre */
.cierre{background:var(--cr);text-align:center}
.cierre .img{max-width:720px;margin:0 auto 34px}
.cierre p{max-width:680px;margin:0 auto 18px;font-size:19px}
.cierre .lema{font-size:clamp(32px,6vw,52px);font-weight:900;color:var(--vd);letter-spacing:-.02em;margin:10px 0 28px}
footer{padding:30px 0 110px;font-size:13px;color:var(--mut);text-align:center}
/* barra fija */
.barra{position:fixed;left:0;right:0;bottom:0;background:rgba(255,255,255,.96);backdrop-filter:blur(8px);border-top:1px solid #E7E1FA;padding:12px 20px;display:flex;align-items:center;justify-content:space-between;gap:14px;z-index:20;transform:translateY(110%);transition:transform .25s}
.barra.on{transform:none}
.barra b{color:var(--vd)}.barra span{font-size:14px;color:var(--mut);display:block}
.barra .btn{padding:13px 22px;font-size:16px;box-shadow:0 4px 0 #E0B91F}
@media (max-width:820px){
 body{font-size:16px} section{padding:48px 0}
 .hero .w{grid-template-columns:1fr;padding-top:44px;padding-bottom:52px;gap:28px}
 .libro{order:-1;width:58%}
 .dos{grid-template-columns:1fr;gap:26px}
 .dias{grid-template-columns:1fr 1fr;gap:12px}
 .dia .t{padding:12px 13px 16px}.dia h3{font-size:16px}.dia p{font-size:14px}
 .cards,.chica{grid-template-columns:1fr}
 .negocios{grid-template-columns:1fr 1fr}
 .paginas{height:300px}
 .btn{width:100%}
}
"""

DIAS = [
    ('Día 0', 'La ficha de tu negocio', 'La página que le cuenta a la IA quién sos. La armás una vez y la usás siempre.', 'IMG-07'),
    ('Día 1', 'WhatsApp sin perder la tarde', 'Tus 15 respuestas más usadas, cargadas como respuestas rápidas. Más bienvenida y ausencia.', 'IMG-08'),
    ('Día 2', 'Instagram sin quedarte en blanco', '30 ideas, una semana de posteos escritos en tu voz y tu biografía renovada.', 'IMG-09'),
    ('Día 3', 'Vender más con lo que ya tenés', 'Descripciones que venden y mensajes para el que preguntó y no compró.', 'IMG-10'),
    ('Día 4', 'Los números sin dolor de cabeza', 'Cuánto te cuesta de verdad, con tus horas, y un precio que te cierre.', 'IMG-11'),
    ('Día 5', 'Clientes difíciles', 'El reclamo, el que regatea, el que cancela y la mala reseña.', 'IMG-12'),
    ('Día 6', 'Promos e ideas', 'Tu calendario del año y promos que no te hacen perder plata.', 'IMG-13'),
    ('Día 7', 'Tu semana en orden', 'Pedidos, agenda y una rutina de 20 minutos por día.', 'IMG-14'),
]
NEG = [('IMG-02', 'Caro', 'Ropa por Instagram · Lanús'), ('IMG-03', 'Mati', 'Tortas por encargo · Morón'),
       ('IMG-04', 'Sol', 'Uñas y pestañas · Rosario'), ('IMG-05', 'Fede', 'Entrenador personal · Córdoba')]
# Mail de contacto para la garantía (decidido 11/11: el mismo de Taller Triple).
MAIL = 'tallertriplearg@gmail.com'
GARANTIA = f'Si no te sirve, escribinos a {MAIL} dentro de los 7 días y te devolvemos la plata. Sin preguntas.'

FAQ = [
    ('¿Necesito saber de computación?', 'No. Si sabés mandar un mensaje por WhatsApp, alcanza. El libro te explica desde cómo abrir la cuenta (son 5 minutos) y cómo pedirle las cosas a la IA.'),
    ('¿Lo puedo hacer desde el celular?', 'Sí. ChatGPT tiene app para el celular y hasta le podés hablar en vez de escribir. WhatsApp Business e Instagram también son del celular. Para el Día 4 (los números) es más cómodo con una compu, pero no es obligatorio.'),
    ('¿Tengo que pagar ChatGPT?', 'No. Todo el libro está hecho con la versión gratis.'),
    ('¿Sirve para mi rubro?', 'Si vendés por WhatsApp e Instagram, casi seguro que sí. Los ejemplos son de ropa, pastelería, uñas y pestañas, y entrenamiento, pero las instrucciones son para cualquier rubro: la que hace que hable de tu negocio es tu ficha, no el ejemplo.'),
    ('¿Los negocios del libro son reales?', 'No. Son ejemplos armados para enseñar, inspirados en negocios típicos de Argentina, y el libro lo aclara. Preferimos eso a inventar testimonios.'),
    ('Uso WhatsApp común, no Business. ¿Sirve?', 'Sí. El Día 1 te explica cómo pasarte a WhatsApp Business (es gratis, con el mismo número y sin perder tus chats). Las respuestas rápidas y los mensajes automáticos solo están en Business.'),
    ('¿Cuánto tiempo me lleva?', 'Una hora por día, más o menos, durante 8 días (el Día 0 y los 7 días). Después, 20 minutos por día de rutina.'),
    ('¿Tengo que hacerlo en 7 días seguidos?', 'No. Podés ir a tu ritmo. Lo único que te pedimos es que no te saltees el Día 0 y que no hagas todo en una noche.'),
    ('¿La IA les va a contestar sola a mis clientes?', 'No. La IA te escribe las respuestas y vos las mandás con dos toques. Nada sale para un cliente sin que vos lo leas. Así lo planteamos a propósito.'),
    ('¿Es seguro poner los datos de mi negocio en la IA?', 'Ponés lo mismo que ya tenés publicado en tu Instagram: qué vendés, precios, envíos y horarios. El libro te explica qué no tenés que pegar nunca: datos personales de tus clientes, contraseñas y datos bancarios.'),
    ('¿Cómo me llega?', 'Por mail, apenas se acredita el pago. Es un PDF que podés guardar en el celular o imprimir.'),
    ('¿Cómo pago?', 'Con Mercado Pago.'),
    ('¿Y si no me sirve?', 'Tenés 7 días de garantía, sin preguntas: escribinos a ' + MAIL + ' dentro de los 7 días desde la compra y te devolvemos la plata.'),
]

def boton(txt=None):
    return f'<a class="btn" href="/checkout">{txt or "Quiero el libro · " + PRICE}</a>'

dias_html = ''.join(f'<div class="dia">{img(i)}<div class="t"><div class="n">{n}</div><h3>{html.escape(t)}</h3><p>{html.escape(d)}</p></div></div>' for n, t, d, i in DIAS)
neg_html = ''.join(f'<div class="neg">{img(i)}<h3>{n}</h3><p>{d}</p></div>' for i, n, d in NEG)
faq_html = ''.join(f'<details><summary>{html.escape(q)}</summary><p>{html.escape(a)}</p></details>' for q, a in FAQ)

LANDING = f"""<!doctype html><html lang="es"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>La IA hace, vos vendés · Ebook</title>
<meta name="description" content="Cómo usar la IA en tu emprendimiento en 7 días, aunque no sepas nada de tecnología. Con ChatGPT gratis.">
<link rel="preconnect" href="https://fonts.googleapis.com"><link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800;900&display=swap" rel="stylesheet">
<style>{CSS}</style></head><body>

<section class="hero"><div class="bg">{img('IMG-01')}</div><div class="w">
 <div><div class="k">Ebook · 7 días · con ChatGPT gratis</div>
  <h1>La IA hace, vos vendés</h1>
  <p class="sub">Cómo usar la IA en tu emprendimiento en 7 días, aunque no sepas nada de tecnología.</p>
  <p class="apoyo">Una tarea por día, una hora por día. Al final de la semana, la IA te contesta WhatsApp, te escribe los posteos y te ayuda con los precios, con tus datos y tu forma de hablar.</p>
  {boton()}<p class="nota">Ebook en PDF. Te llega por mail apenas se acredita el pago.</p></div>
 <div class="libro"><img src="{asset(MOCK['tapa'])}" alt="Tapa del ebook La IA hace, vos vendés"></div>
</div></section>

<section class="prob"><div class="w">
 <div class="k">Si vendés por WhatsApp e Instagram</div><h2>Ya sabés cómo es</h2>
 <div class="cards">
  <div class="card"><b>«¿Precio?»</b>Lo contestás veinte veces por día.</div>
  <div class="card"><b>Instagram en blanco</b>No sabés qué subir, así que no subís nada.</div>
  <div class="card"><b>Precios «a ojo»</b>Cobrás sin saber si te queda plata.</div>
  <div class="card"><b>El mensaje feo</b>Un cliente te escribe mal y te arruina la tarde.</div>
 </div>
 <p class="remate">Nada de eso es difícil. Es <b>repetido</b>. Y lo repetido es justo lo que la IA hace bien. El problema es que nadie te explicó cómo usarla para <b>tu</b> negocio: le pedís algo y te devuelve un texto genérico que no suena a vos. Este libro arregla eso.</p>
</div></section>

<section><div class="w dos">
 <div>{img('IMG-08')}</div>
 <div><div class="k">La idea que hace que funcione</div><h2>La ficha de tu negocio</h2>
  <p class="lead">Antes de arrancar, armás una página con todo lo importante: qué vendés, precios, envíos, medios de pago, horarios y cómo hablás con tus clientes. Lo hacés una sola vez y la cargás en ChatGPT.</p>
  <div class="ficha"><span class="tag">DESDE AHÍ</span><p>Todo lo que te escriba la IA habla de <b>tu</b> negocio, con <b>tus</b> precios y <b>tu</b> forma de hablar. No de un negocio cualquiera.</p></div>
 </div>
</div></section>

<section style="padding-top:20px"><div class="w">
 <div class="k">Los 7 días</div><h2>Cada día termina con algo hecho y funcionando</h2>
 <p class="lead">Arrancás con el Día 0, que es la preparación. Después, una tarea por día.</p>
 <div class="dias">{dias_html}</div>
 <p class="tiempo">Entre 45 minutos y 1 hora y media por día. El Día 4, el de los números, es el más largo.</p>
</div></section>

<section class="trae"><div class="w dos">
 <div><div class="k">Qué trae</div><h2>Todo listo para usar</h2>
  <ul class="lista">
   <li><b>El libro completo:</b> Día 0, los 7 días y un cierre con los errores más comunes, los cuidados y qué hacer la semana 2.</li>
   <li><b>40 instrucciones para copiar y pegar</b> en ChatGPT, repartidas en los días.</li>
   <li><b>La plantilla de la ficha de tu negocio</b>, para completar.</li>
   <li><b>Ejemplos en 4 rubros</b> en cada día.</li>
   <li><b>Una tarea para tildar</b> al final de cada día.</li>
  </ul>
  {boton()}<p class="nota" style="color:#d8d2f5">En PDF. Te llega por mail apenas se acredita el pago.</p></div>
 <div class="paginas"><img src="{asset(MOCK['p1'])}" alt=""><img src="{asset(MOCK['p2'])}" alt=""><img src="{asset(MOCK['p3'])}" alt=""></div>
</div></section>

<section><div class="w" style="text-align:center">
 <div class="k">Los ejemplos del libro</div><h2>4 negocios te acompañan día por día</h2>
 <p class="lead" style="margin:0 auto">En cada día ves cómo resolvieron la tarea. Seguramente el tuyo se parece a alguno.</p>
 <div class="negocios">{neg_html}</div>
 <p class="aclara">Son ejemplos armados para enseñar, no testimonios. El libro lo aclara.</p>
</div></section>

<section class="quien"><div class="w">
 <div class="k">Antes de comprar</div><h2>¿Es para vos?</h2>
 <div class="dos" style="align-items:start;margin-top:24px">
  <div class="col si"><h3>Es para vos si…</h3><ul>
   <li>Tenés un emprendimiento o un negocio chico y vendés por WhatsApp e Instagram: ropa, comida, estética, artesanías, clases, servicios.</li>
   <li>Hacés casi todo vos y el celular te come el día.</li>
   <li>Nunca usaste IA, o la probaste y no le encontraste la vuelta.</li>
   <li>Querés algo concreto para hacer hoy, no una charla sobre el futuro.</li></ul></div>
  <div class="col no"><h3>No es para vos si…</h3><ul>
   <li>Tenés una empresa con un equipo de marketing.</li>
   <li>Sos programador o ya usás la IA todos los días: te va a quedar básico.</li>
   <li>Buscás «hacerte rico con IA». Esto es para que tu negocio te lleve menos tiempo.</li>
   <li>Esperás que la IA venda por vos. No lo hace: te saca el trabajo repetido.</li></ul></div>
 </div>
</div></section>

<section><div class="w">
 <div class="k">Sin letra chica</div><h2>Lo que tenés que saber</h2>
 <div class="chica">
  <div><b>Usamos ChatGPT gratis.</b> Tiene un límite de uso por día con el modelo más nuevo; cuando llegás, sigue andando con uno más simple. Para lo del libro alcanza.</div>
  <div><b>La IA se equivoca.</b> Por eso la regla del libro es: la IA escribe el borrador, vos lo revisás. Precios, cuentas y fechas, siempre los confirmás vos.</div>
  <div><b>Lo tenés que hacer.</b> Es una hora por día. Si lo leés y no hacés las tareas, no cambia nada.</div>
  <div><b>No te prometemos ventas.</b> Te prometemos las respuestas, los posteos y los números armados. Lo que vendas depende de tu producto y de vos.</div>
  <div style="grid-column:1/-1"><b>Garantía de 7 días.</b> {html.escape(GARANTIA)}</div>
 </div>
</div></section>

<section style="padding-top:10px"><div class="w" style="max-width:820px">
 <div class="k">Preguntas frecuentes</div><h2>Lo que más nos preguntan</h2>
 {faq_html}
</div></section>

<section class="cierre"><div class="w">
 {img('IMG-15')}
 <p>La IA no va a hacer crecer tu negocio sola. Lo que hace es sacarte de encima el trabajo repetido, para que el tiempo que te queda lo uses en lo que solo vos podés hacer: tu producto, tu trato con los clientes, tus ideas.</p>
 <div class="lema">La IA hace. Vos vendés.</div>
 {boton()}<p class="nota">Pagás con Mercado Pago. Te llega por mail apenas se acredita el pago. Garantía de 7 días sin preguntas.</p>
</div></section>

<footer><div class="w">{'' if PREVIEW else '{{legal_footer}}'}</div></footer>
<div class="barra" id="barra"><div><b>La IA hace, vos vendés</b><span>Ebook en PDF · {PRICE}</span></div>{boton('Comprar')}</div>
<script>
(function(){{var b=document.getElementById('barra'),h=document.querySelector('.hero');
function f(){{b.classList.toggle('on',window.scrollY>h.offsetHeight*0.8)}}window.addEventListener('scroll',f,{{passive:true}});f();}})();
</script>
</body></html>"""

UP_PRICE = '$12.990' if PREVIEW else '{price}'
POST = f"""<!doctype html><html lang="es"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1"><title>Las 200 instrucciones</title>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800;900&display=swap" rel="stylesheet">
<style>{CSS}
.ok{{background:#E7F8EE;color:#14663A;font-weight:700;text-align:center;padding:14px 20px;font-size:15px}}
.up .w{{max-width:760px}}
.up h1{{font-size:clamp(30px,6vw,46px);margin:10px 0 16px}}
.up .mock{{width:min(260px,60%);margin:24px auto 30px;display:block;border-radius:6px 12px 12px 6px;box-shadow:-10px 18px 36px rgba(46,31,115,.35)}}
table{{width:100%;border-collapse:collapse;margin:20px 0;font-size:16px}}
td{{padding:10px 4px;border-bottom:1px solid #E7E1FA}} td:last-child{{text-align:right;font-weight:800;color:var(--v)}}
.maestra{{background:var(--soft);border:2px solid var(--v);border-radius:20px;padding:20px 22px;margin:24px 0}}
.acciones{{text-align:center;margin:30px 0 10px}}
.no-gracias{{display:block;margin:18px auto 0;background:none;border:none;color:var(--mut);text-decoration:underline;font-size:15px;cursor:pointer}}
</style></head><body>
<div class="ok">¡Listo! Tu compra está hecha. En unos minutos te llega el libro por mail.</div>
<section class="up"><div class="w">
 <div class="k">Una sola cosa más</div>
 <h1>¿Querés tener una instrucción lista para cada situación de tu negocio?</h1>
 <p class="lead">El libro te enseña a usar la IA con 40 instrucciones. <b>Las 200 instrucciones</b> es la biblioteca para después: una instrucción lista para copiar y pegar para cada cosa que te va a pasar en el día a día, ordenadas por situación.</p>
 <img class="mock" src="{asset(MOCK['t200'])}" alt="Tapa de Las 200 instrucciones">
 <table>
  <tr><td>WhatsApp</td><td>30</td></tr><tr><td>Instagram</td><td>40</td></tr><tr><td>Vender</td><td>25</td></tr>
  <tr><td>Fechas y promos</td><td>30</td></tr><tr><td>Clientes</td><td>20</td></tr><tr><td>Números</td><td>20</td></tr>
  <tr><td>Organización e ideas</td><td>20</td></tr><tr><td>Proveedores y textos formales</td><td>15</td></tr>
 </table>
 <p>Sirven para cualquier rubro: donde dice [tu rubro] o [producto], ponés lo tuyo. Y debajo de cada una te decimos qué te tiene que devolver, para que sepas si salió bien.</p>
 <div class="maestra"><b>Incluye la instrucción maestra:</b> la pegás con tu ficha del Día 0 y, en una sola conversación de 20 a 30 minutos, la IA te arma el kit completo de tu negocio: 15 respuestas de WhatsApp con atajos, 30 ideas para Instagram con 3 biografías, el calendario de fechas de los próximos 12 meses para tu rubro, 5 promos y 5 respuestas para situaciones difíciles.</div>
 {img('IMG-31')}
 <div class="acciones">
  <button class="btn" data-pp-accept>Sí, sumalas a mi compra · {UP_PRICE}</button>
  <p class="nota">Te llega por mail junto con el libro.</p>
  <button class="no-gracias" data-pp-decline>No, gracias. Me quedo solo con lo que compré.</button>
 </div>
</div></section>
</body></html>"""

open(os.path.join(OUT, 'landing.html'), 'w').write(LANDING)
open(os.path.join(OUT, 'postcompra.html'), 'w').write(POST)
print('ok', OUT, f'{len(LANDING)//1024} KB landing')

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
:root{--fondo:#ECE5DA;--verde:#0B6E5F;--verde-o:#084F45;--yo:#DCF8C6;--ink:#17201D;--mut:#5E6B66;--linea:#D8CFC2;--amar:#FFF4C2}
*{box-sizing:border-box;margin:0;padding:0}
html{scroll-behavior:smooth}
body{background:var(--fondo);color:var(--ink);font:17px/1.55 "Plus Jakarta Sans",system-ui,-apple-system,Segoe UI,Roboto,sans-serif;-webkit-font-smoothing:antialiased;
 background-image:radial-gradient(rgba(11,110,95,.07) 1.2px,transparent 1.3px);background-size:22px 22px}
img{display:block;max-width:100%}
.w{max-width:1100px;margin:0 auto;padding:0 22px}
section{padding:72px 0}
h1,h2,h3{font-family:"Bricolage Grotesque",system-ui,sans-serif;letter-spacing:-.03em;line-height:1}
h1,h2{font-weight:800}
h2{font-size:clamp(36px,5.4vw,60px);max-width:780px}
h3{font-weight:700;letter-spacing:-.015em}
.intro{color:var(--mut);font-size:clamp(17px,2.2vw,19px);margin:16px 0 34px;max-width:640px}
.btn{display:inline-flex;gap:10px;align-items:center;justify-content:center;background:var(--verde);color:#fff;font-weight:700;font-size:18px;padding:17px 26px;border-radius:14px;text-decoration:none;border:none;cursor:pointer;font-family:inherit;transition:background .15s}
.btn:hover{background:var(--verde-o)}
.nota{font-size:14px;color:var(--mut);margin-top:14px}
.img{width:100%;object-fit:cover;border-radius:16px}
.ph-img{background:#fff;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;padding:16px;border:2px dashed var(--linea)}
.ph-id{background:var(--verde);color:#fff;font-size:12px;font-weight:800;padding:4px 10px;border-radius:6px}
.ph-txt{font-size:13px;color:var(--mut);margin-top:8px}
/* burbujas */
.m{max-width:86%;padding:9px 12px 19px;border-radius:12px;position:relative;box-shadow:0 1px 1.5px rgba(0,0,0,.09);font-size:15px;line-height:1.45}
.m .h{position:absolute;right:9px;bottom:3px;font-size:10.5px;color:#7a8a84}
.ell{background:#fff;align-self:flex-start;border-top-left-radius:3px}
.yo{background:var(--yo);align-self:flex-end;border-top-right-radius:3px}
.aviso{align-self:center;font-size:12px;background:var(--amar);color:#6b5a12;padding:5px 11px;border-radius:8px;text-align:center}
/* hero */
.hero{padding:64px 0 76px}
.hero .w{display:grid;grid-template-columns:1.1fr .9fr;gap:56px;align-items:center}
.hero h1{font-size:clamp(50px,8vw,92px)}.hero h1 span{color:var(--verde)}
.hero .sub{font-size:clamp(20px,2.5vw,24px);margin:22px 0 12px;font-weight:600;line-height:1.35}
.hero .apoyo{color:var(--mut);max-width:520px;margin-bottom:28px}
.tel{background:#17201D;border-radius:38px;padding:9px;box-shadow:0 30px 60px rgba(23,32,29,.25);max-width:360px;margin:0 auto;width:100%}
.tel .bar{background:var(--verde);color:#fff;border-radius:30px 30px 0 0;padding:14px 18px;font-weight:700;font-size:15px;display:flex;gap:10px;align-items:center}
.tel .bar img{width:34px;height:34px;border-radius:50%;object-fit:cover}
.tel .bar small{display:block;font-weight:400;opacity:.8;font-size:12px}
.chat{background:var(--fondo);padding:16px 12px 22px;display:flex;flex-direction:column;gap:8px;border-radius:0 0 30px 30px}
/* problema */
.prob .w{display:grid;grid-template-columns:.9fr 1.1fr;gap:56px;align-items:center}
.pila{display:flex;flex-direction:column;gap:10px;position:relative}
.pila .m{max-width:92%;font-size:16px}.pila .m b{display:block;font-family:"Bricolage Grotesque";font-size:20px;letter-spacing:-.01em;margin-bottom:2px}
.pila .m:nth-child(even){margin-left:8%}
.sinleer{position:absolute;right:0;top:-14px;background:var(--verde);color:#fff;font-size:13px;font-weight:800;border-radius:999px;padding:4px 11px}
.remate{font-size:clamp(18px,2.3vw,21px);margin-top:22px}
/* ficha */
.ficha .w{display:grid;grid-template-columns:1fr 1fr;gap:56px;align-items:center}
.fijado{background:#fff;border-radius:16px;padding:20px 22px;margin-top:22px;border-left:5px solid var(--verde);box-shadow:0 1px 2px rgba(0,0,0,.07)}
.fijado small{display:block;font-size:12px;font-weight:800;color:var(--verde);letter-spacing:.04em;margin-bottom:6px}
/* dias */
.hilo{display:grid;grid-template-columns:1fr 1fr;gap:16px 26px}
.dm{display:grid;grid-template-columns:84px 1fr;gap:15px;background:#fff;border-radius:16px;border-top-left-radius:4px;padding:14px;box-shadow:0 1px 2px rgba(0,0,0,.07)}
.dm .img{width:84px;height:84px;border-radius:12px;aspect-ratio:auto!important}
.dm .n{font-size:12px;font-weight:800;color:var(--verde);letter-spacing:.05em}
.dm h3{font-size:20px;line-height:1.15;margin:2px 0 4px}
.dm p{font-size:15px;color:var(--mut)}
.tiempo{margin-top:22px;color:var(--mut);font-size:15px}
/* trae + precio */
.trae{background:var(--verde);color:#fff}
.trae .w{display:grid;grid-template-columns:1fr 1fr;gap:56px;align-items:center}
.trae h2{color:#fff}
.libros{position:relative;height:440px;margin-top:30px}
.libros img{position:absolute;border-radius:6px;box-shadow:0 22px 44px rgba(0,0,0,.35)}
.libros .tapa{width:56%;left:0;top:0;border-radius:4px 12px 12px 4px;z-index:2}
.libros .pag{width:52%;right:0;top:60px;transform:rotate(4deg)}
.recibo{background:#fff;color:var(--ink);border-radius:22px;padding:28px}
.recibo ul{list-style:none}
.recibo li{padding:11px 0 11px 32px;position:relative;border-bottom:1px solid #eee;font-size:16px}
.recibo li:before{content:"✓✓";position:absolute;left:0;top:13px;color:#34B7F1;font-size:13px;font-weight:800;letter-spacing:-3px}
.monto{font-family:"Bricolage Grotesque";font-size:60px;font-weight:800;margin:20px 0 6px;line-height:1;letter-spacing:-.03em}
.monto small{display:block;font-family:"Plus Jakarta Sans";font-size:14px;font-weight:600;color:var(--mut);letter-spacing:0;margin-top:8px}
.recibo .btn{width:100%;margin-top:16px}
.gar{display:flex;gap:12px;align-items:flex-start;font-size:14px;color:var(--mut);margin-top:18px;background:#F4F8F6;border-radius:12px;padding:12px 14px}
.gar b{color:var(--ink)}
/* negocios */
.lista-chats{background:#fff;border-radius:20px;overflow:hidden;box-shadow:0 1px 2px rgba(0,0,0,.07);max-width:720px}
.contacto{display:grid;grid-template-columns:64px 1fr auto;gap:16px;align-items:center;padding:14px 18px;border-bottom:1px solid #EFEAE2}
.contacto:last-child{border-bottom:none}
.contacto .img{width:64px;height:64px;border-radius:50%;aspect-ratio:auto!important}
.contacto h3{font-size:19px}.contacto p{font-size:15px;color:var(--mut)}
.contacto span{font-size:12px;color:var(--verde);font-weight:700}
.aclara{margin-top:18px;font-size:14px;color:var(--mut);background:var(--amar);border-radius:10px;padding:10px 14px;display:inline-block}
/* para quien / letra chica */
.dos{display:grid;grid-template-columns:1fr 1fr;gap:20px}
.col{background:#fff;border-radius:20px;padding:26px;box-shadow:0 1px 2px rgba(0,0,0,.07)}
.col h3{font-size:22px;margin-bottom:12px}
.col ul{list-style:none}
.col li{padding:9px 0 9px 30px;position:relative;font-size:16px}
.si li:before{content:"✓";position:absolute;left:0;color:var(--verde);font-weight:800}
.no li:before{content:"✕";position:absolute;left:0;color:#B8432F;font-weight:800}
.chica{display:grid;grid-template-columns:1fr 1fr;gap:16px}
.chica div{background:#fff;border-radius:16px;padding:18px 20px;font-size:16px;box-shadow:0 1px 2px rgba(0,0,0,.07)}
.chica .full{grid-column:1/-1;border-left:5px solid var(--verde)}
/* faq como chat */
.faq .w{max-width:820px}
details{margin-bottom:12px;display:flex;flex-direction:column}
summary{list-style:none;cursor:pointer;background:#fff;border-radius:14px;border-top-left-radius:3px;padding:13px 44px 13px 16px;font-weight:700;font-size:17px;position:relative;max-width:88%;box-shadow:0 1px 1.5px rgba(0,0,0,.09);display:inline-block}
summary::-webkit-details-marker{display:none}
summary:after{content:"+";position:absolute;right:15px;top:9px;color:var(--verde);font-size:24px;font-weight:600}
details[open] summary:after{content:"–"}
details p{background:var(--yo);border-radius:14px;border-top-right-radius:3px;padding:13px 16px;margin:8px 0 6px auto;max-width:88%;font-size:16px;box-shadow:0 1px 1.5px rgba(0,0,0,.09)}
/* cierre */
.cierre{text-align:center}
.cierre .img{max-width:760px;margin:0 auto 34px;aspect-ratio:3/2}
.cierre p{max-width:660px;margin:0 auto 18px;font-size:19px}
.cierre .nota{font-size:14px;margin-top:14px}
.cierre h2{margin:10px auto 26px}.cierre h2 span{color:var(--verde)}
footer{padding:20px 0 110px;font-size:13px;color:var(--mut);text-align:center}
/* barra fija */
.barra{position:fixed;left:0;right:0;bottom:0;background:rgba(255,255,255,.97);border-top:1px solid var(--linea);padding:10px 18px;display:flex;align-items:center;justify-content:space-between;gap:14px;z-index:20;transform:translateY(110%);transition:transform .25s}
.barra.on{transform:none}
.barra b{font-size:15px}.barra span{font-size:13px;color:var(--mut);display:block}
.barra .btn{padding:12px 22px;font-size:16px}
@media (max-width:820px){
 body{font-size:16px} section{padding:52px 0}
 .hero{padding:34px 0 52px}
 .hero .w,.prob .w,.ficha .w,.trae .w,.dos,.chica{grid-template-columns:1fr;gap:30px}
 .hilo{grid-template-columns:1fr;gap:12px}
 .dm{grid-template-columns:68px 1fr}.dm .img{width:68px;height:68px}
 .hero .btn{display:flex}
 .tel{max-width:330px}
 .libros{height:300px;margin-top:10px}
 .contacto{grid-template-columns:52px 1fr;padding:12px 14px}.contacto .img{width:52px;height:52px}.contacto span{display:none}
 summary,details p{max-width:94%}
 .pags{grid-template-columns:1fr 1fr!important}.pags figure:last-child{grid-column:1/-1;max-width:60%;margin:0 auto!important}
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

def boton(txt=None, cls='btn'):
    return f'<a class="{cls}" href="/checkout">{txt or "Quiero el libro · " + PRICE}</a>'
def src(id_):
    """Dirección de una foto (para <img> con otra clase que .img)."""
    n = f'{id_}.jpg'
    return asset(n) if PREVIEW else URLS.get(id_, URLS.get(n, f'RECURSO:{n}'))

TRAE = [('El libro completo:', 'Día 0, los 7 días y un cierre con los errores más comunes, los cuidados y qué hacer la semana 2.'),
        ('40 instrucciones para copiar y pegar', 'en ChatGPT, repartidas en los días.'),
        ('La plantilla de la ficha de tu negocio,', 'para completar.'),
        ('Ejemplos en 4 rubros', 'en cada día.'),
        ('Una tarea para tildar', 'al final de cada día.')]
dias_html = ''.join(f'<div class="dm">{img(i)}<div><div class="n">{n.upper()}</div><h3>{html.escape(t)}</h3><p>{html.escape(d)}</p></div></div>' for n, t, d, i in DIAS)
neg_html = ''.join(f'<div class="contacto">{img(i)}<div><h3>{n}</h3><p>{d}</p></div><span>ejemplo</span></div>' for i, n, d in NEG)
faq_html = ''.join(f'<details><summary>{html.escape(q)}</summary><p>{html.escape(a)}</p></details>' for q, a in FAQ)
trae_html = ''.join(f'<li><b>{html.escape(a)}</b> {html.escape(b)}</li>' for a, b in TRAE)
PAGS = [('p1', 'Día 0 · La ficha de tu negocio'), ('p2', 'Día 1 · Tus respuestas de WhatsApp'), ('p3', 'Día 4 · Tus números y tu precio')]
pags_html = ''.join(f'<figure style="margin:0"><img src="{asset(MOCK[k])}" alt="{t}" style="width:100%;border-radius:10px;box-shadow:0 14px 30px rgba(23,32,29,.18);background:#fff"><figcaption style="font-size:14px;color:var(--mut);margin-top:10px;text-align:center">{t}</figcaption></figure>' for k, t in PAGS)
FONTS = '<link rel="preconnect" href="https://fonts.googleapis.com"><link href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,700;12..96,800&family=Plus+Jakarta+Sans:wght@400;600;700&display=swap" rel="stylesheet">'

LANDING = f"""<!doctype html><html lang="es"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>La IA hace, vos vendés · Ebook</title>
<meta name="description" content="Cómo usar la IA en tu emprendimiento en 7 días, aunque no sepas nada de tecnología. Con ChatGPT gratis.">
{FONTS}
<style>{CSS}</style></head><body>

<section class="hero"><div class="w">
 <div><h1>La IA hace, <span>vos vendés.</span></h1>
  <p class="auto" style="font-family:'Bricolage Grotesque',system-ui,sans-serif;font-weight:800;letter-spacing:-.02em;line-height:1.1;font-size:clamp(28px,3.8vw,42px);color:var(--verde);margin-top:18px">Automatizá tu negocio con inteligencia artificial.</p>
  <p class="sub">Cómo usar la IA en tu emprendimiento en 7 días, aunque no sepas nada de tecnología.</p>
  <p class="apoyo"><b style="color:var(--ink)">Si sabés mandar un audio, sabés usarla.</b> Una tarea por día, una hora por día, con ChatGPT gratis. Al final de la semana, la IA te contesta WhatsApp, te escribe los posteos y te ayuda con los precios, con tus datos y tu forma de hablar.</p>
  {boton()}<p class="nota">Ebook en PDF por mail apenas se acredita el pago · Garantía de 7 días</p><p class="nota" style="margin-top:6px">Sirve para ropa, comida, uñas y estética, clases, servicios y cualquier negocio que venda por WhatsApp.</p></div>
 <div class="tel"><div class="bar"><img src="{src('IMG-02')}" alt=""><div>Ejemplo · Caro, ropa<small>en línea</small></div></div><div class="chat">
  <div class="m ell">Hola!! precio del buzo gris? 🙏<span class="h">21:47</span></div>
  <div class="aviso">Respuesta escrita con IA a partir de tu ficha · la revisás vos</div>
  <div class="m yo">¡Hola! El buzo gris está $18.500. Hay en S, M y L. Envío a todo el país o retiro en Lanús, y aceptamos transferencia o Mercado Pago. ¿Qué talle buscás? 😊<span class="h">21:48 ✓✓</span></div>
  <div class="m ell">M! y llega antes del sábado?<span class="h">21:48</span></div>
 </div></div>
</div></section>

<section class="adentro" style="padding-top:8px"><div class="w">
 <h2 style="font-size:clamp(30px,4.4vw,46px)">Así es el libro por dentro.</h2>
 <p class="intro">Páginas reales: cada día te dice qué hacer, te da la instrucción para copiar y pegar y un ejemplo resuelto.</p>
 <div style="display:grid;grid-template-columns:repeat(3,1fr);gap:18px" class="pags">{pags_html}</div>
</div></section>

<section class="prob"><div class="w">
 <div><h2>Si vendés por WhatsApp e Instagram, ya sabés cómo es.</h2>
  <p class="remate">Nada de eso es difícil. Es <b>repetido</b>. Y lo repetido es justo lo que la IA hace bien. El problema es que nadie te explicó cómo usarla para <b>tu</b> negocio: le pedís algo y te devuelve un texto genérico que no suena a vos. Este libro arregla eso.</p></div>
 <div class="pila">
  <div class="m ell"><b>«¿Precio?»</b>Lo contestás veinte veces por día.<span class="h">9:12</span></div>
  <div class="m ell"><b>Instagram en blanco</b>No sabés qué subir, así que no subís nada.<span class="h">13:40</span></div>
  <div class="m ell"><b>Precios «a ojo»</b>Cobrás sin saber si te queda plata.<span class="h">18:05</span></div>
  <div class="m ell"><b>El mensaje feo</b>Un cliente te escribe mal y te arruina la tarde.<span class="h">22:31</span></div>
 </div>
</div></section>

<section class="ficha"><div class="w">
 <div>{img('IMG-08')}</div>
 <div><h2>La idea que hace que funcione: la ficha de tu negocio.</h2>
  <p class="intro" style="margin-bottom:0">Antes de arrancar, armás una página con todo lo importante: qué vendés, precios, envíos, medios de pago, horarios y cómo hablás con tus clientes. Lo hacés una sola vez y la cargás en ChatGPT.</p>
  <div class="fijado"><small>📌 DESDE AHÍ</small>Todo lo que te escriba la IA habla de <b>tu</b> negocio, con <b>tus</b> precios y <b>tu</b> forma de hablar. No de un negocio cualquiera.</div>
 </div>
</div></section>

<section><div class="w">
 <h2>Una tarea por día. Cada día termina con algo hecho y funcionando.</h2>
 <p class="intro">Arrancás con el Día 0, que es la preparación. Después, una tarea por día.</p>
 <div class="hilo">{dias_html}</div>
 <p class="tiempo">Entre 45 minutos y 1 hora y media por día. El Día 4, el de los números, es el más largo.</p>
</div></section>

<section class="trae" id="precio"><div class="w">
 <div><h2>Todo listo para usar, por {PRICE}.</h2>
  <div class="libros"><img class="tapa" src="{asset(MOCK['tapa'])}" alt="Tapa del ebook La IA hace, vos vendés"><img class="pag" src="{asset(MOCK['p2'])}" alt="Una página del libro"></div></div>
 <div class="recibo"><ul>{trae_html}</ul>
  <div class="monto">{PRICE}<small>Un solo pago con Mercado Pago. El PDF es tuyo.</small></div>
  {boton('Quiero el libro')}
  <div class="gar"><span>🛡️</span><span><b>Garantía de 7 días, sin preguntas.</b> {html.escape(GARANTIA.replace(' Sin preguntas.', ''))}</span></div>
 </div>
</div></section>

<section><div class="w">
 <h2>4 negocios te acompañan día por día.</h2>
 <p class="intro">En cada día ves cómo resolvieron la tarea. Seguramente el tuyo se parece a alguno.</p>
 <div class="lista-chats">{neg_html}</div>
 <p class="aclara">Son ejemplos armados para enseñar, no testimonios. El libro lo aclara.</p>
</div></section>

<section style="padding-top:20px"><div class="w">
 <h2>¿Es para vos?</h2>
 <div class="dos" style="margin-top:28px">
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

<section style="padding-top:20px"><div class="w">
 <h2>Sin letra chica.</h2>
 <div class="chica" style="margin-top:28px">
  <div><b>Usamos ChatGPT gratis.</b> Tiene un límite de uso por día con el modelo más nuevo; cuando llegás, sigue andando con uno más simple. Para lo del libro alcanza.</div>
  <div><b>La IA se equivoca.</b> Por eso la regla del libro es: la IA escribe el borrador, vos lo revisás. Precios, cuentas y fechas, siempre los confirmás vos.</div>
  <div><b>Lo tenés que hacer.</b> Es una hora por día. Si lo leés y no hacés las tareas, no cambia nada.</div>
  <div><b>No te prometemos ventas.</b> Te prometemos las respuestas, los posteos y los números armados. Lo que vendas depende de tu producto y de vos.</div>
  <div class="full"><b>Garantía de 7 días.</b> {html.escape(GARANTIA)}</div>
 </div>
</div></section>

<section class="faq" style="padding-top:20px"><div class="w">
 <h2>Lo que más nos preguntan.</h2>
 <p class="intro">Tocá una pregunta para ver la respuesta.</p>
 {faq_html}
</div></section>

<section class="cierre"><div class="w">
 {img('IMG-15')}
 <p>La IA no va a hacer crecer tu negocio sola. Lo que hace es sacarte de encima el trabajo repetido, para que el tiempo que te queda lo uses en lo que solo vos podés hacer: tu producto, tu trato con los clientes, tus ideas.</p>
 <h2>La IA hace. <span>Vos vendés.</span></h2>
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
{FONTS}
<style>{CSS}
.ok{{background:var(--verde);color:#fff;font-weight:700;text-align:center;padding:14px 20px;font-size:15px}}
.up{{padding-top:44px}}.up .w{{max-width:760px}}
.up h1{{font-size:clamp(34px,6vw,54px);margin:0 0 16px}}
.up .mock{{width:min(250px,58%);margin:26px auto 30px;border-radius:4px 12px 12px 4px;box-shadow:0 22px 44px rgba(23,32,29,.3)}}
.cats{{background:#fff;border-radius:20px;overflow:hidden;box-shadow:0 1px 2px rgba(0,0,0,.07);margin:20px 0}}
.cats div{{display:flex;justify-content:space-between;padding:12px 18px;border-bottom:1px solid #EFEAE2;font-size:16px}}
.cats div:last-child{{border-bottom:none}}
.cats b{{background:var(--verde);color:#fff;font-size:13px;border-radius:999px;padding:2px 10px;align-self:center}}
.maestra{{background:#fff;border-left:5px solid var(--verde);border-radius:16px;padding:18px 20px;margin:24px 0;box-shadow:0 1px 2px rgba(0,0,0,.07)}}
.acciones{{text-align:center;margin:30px 0 10px}}.acciones .btn{{width:100%;max-width:460px}}
.no-gracias{{display:block;margin:18px auto 0;background:none;border:none;color:var(--mut);text-decoration:underline;font-size:15px;cursor:pointer;font-family:inherit}}
</style></head><body>
<div class="ok">✓✓ ¡Listo! Tu compra está hecha. En unos minutos te llega el libro por mail.</div>
<section class="up"><div class="w">
 <h1>¿Querés tener una instrucción lista para cada situación de tu negocio?</h1>
 <p class="intro" style="margin-bottom:0">El libro te enseña a usar la IA con 40 instrucciones. <b>Las 200 instrucciones</b> es la biblioteca para después: una instrucción lista para copiar y pegar para cada cosa que te va a pasar en el día a día, ordenadas por situación.</p>
 <img class="mock" src="{asset(MOCK['t200'])}" alt="Tapa de Las 200 instrucciones">
 <div class="cats"><div>WhatsApp<b>30</b></div><div>Instagram<b>40</b></div><div>Vender<b>25</b></div><div>Fechas y promos<b>30</b></div><div>Clientes<b>20</b></div><div>Números<b>20</b></div><div>Organización e ideas<b>20</b></div><div>Proveedores y textos formales<b>15</b></div></div>
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

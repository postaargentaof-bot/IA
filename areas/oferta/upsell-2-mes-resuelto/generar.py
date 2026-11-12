# Genera el PDF de «El mes resuelto» en formato celular (108 x 192 mm).
# Uso: python3 generar.py <carpeta de salida>
# Necesita Playwright con Chromium (node) instalado.
import html, json, os, subprocess, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import contenido as C

out_dir = sys.argv[1] if len(sys.argv) > 1 else "."
e = html.escape

def plantilla(t):
    # resalta los [huecos]
    s = e(t)
    import re
    s = re.sub(r"\[([^\]]+)\]", r'<span class="hueco">[\1]</span>', s)
    return s.replace("\n", "<br>")

css = """
@page { size: 108mm 192mm; margin: 0; }
* { box-sizing: border-box; margin: 0; padding: 0; }
:root { --verde:#0B6E5F; --verde-c:#E3F1EC; --fondo:#ECE5DA; --yo:#DCF8C6; --ink:#17201D; --mut:#5E6B66; --amar:#FFF4C2; }
body { font-family: "Plus Jakarta Sans", system-ui, sans-serif; color: var(--ink); font-size: 9.8pt; line-height: 1.4; -webkit-print-color-adjust: exact; print-color-adjust: exact; }
h1, h2, h3 { font-family: "Bricolage Grotesque", system-ui, sans-serif; letter-spacing: -.02em; line-height: 1.05; }
.pag { width: 108mm; height: 192mm; overflow: hidden; padding: 9mm 8mm 11mm; page-break-after: always; position: relative; background: #fff; }
.pag:last-child { page-break-after: auto; }
.tapa { background: var(--verde); color: #fff; display: flex; flex-direction: column; justify-content: space-between; height: 192mm; }
.tapa h1 { font-size: 40pt; font-weight: 800; margin-top: 20mm; }
.tapa .sub { font-size: 13pt; font-weight: 600; margin-top: 6mm; line-height: 1.3; }
.tapa .de { font-size: 9.5pt; opacity: .85; }
.burbuja { background: var(--yo); border-radius: 10px; border-top-right-radius: 3px; padding: 9px 11px; margin: 4mm 0; }
.blanca { background: #fff; color: var(--ink); border-radius: 10px; border-top-left-radius: 3px; padding: 9px 11px; }
h2 { font-size: 20pt; font-weight: 800; margin-bottom: 4mm; }
h3 { font-size: 13pt; font-weight: 700; margin: 4mm 0 1.5mm; }
p { margin-bottom: 2.5mm; }
.mut { color: var(--mut); }
.chico { font-size: 8.6pt; }
.etq { display: inline-block; font-size: 7.6pt; font-weight: 800; letter-spacing: .06em; text-transform: uppercase; color: var(--verde); margin-bottom: 1mm; }
.caja { border-radius: 10px; padding: 2.4mm 3mm; margin-bottom: 2.4mm; font-size: 9pt; }
.post { background: var(--yo); border-top-right-radius: 3px; font-size: 9.3pt; }
.info { background: #F4F6F5; }
.wa { background: var(--verde-c); }
.amar { background: var(--amar); }
.hueco { background: rgba(11,110,95,.13); color: var(--verde); font-weight: 700; border-radius: 3px; padding: 0 2px; }
pre.copia { white-space: pre-wrap; font-family: inherit; font-size: 9pt; background: #F4F6F5; border-left: 3px solid var(--verde); padding: 3mm; border-radius: 6px; }
.dia-n { font-family: "Bricolage Grotesque"; font-size: 34pt; font-weight: 800; color: var(--verde); line-height: .9; }
.cab { display: flex; gap: 3mm; align-items: flex-end; margin-bottom: 1.5mm; }
.cab .fmt { font-size: 8pt; font-weight: 700; color: var(--mut); text-transform: uppercase; letter-spacing: .05em; }
.cab h2 { font-size: 16pt; margin: 0; }
.para { font-size: 9.2pt; color: var(--mut); margin-bottom: 3mm; }
table { width: 100%; border-collapse: collapse; font-size: 7.6pt; }
td, th { border-bottom: 1px solid #E3E0DA; padding: .75mm 1mm; text-align: left; vertical-align: top; }
th { font-size: 7.4pt; text-transform: uppercase; letter-spacing: .04em; color: var(--mut); }
.sem { background: var(--verde); color: #fff; }
.sem h2 { font-size: 28pt; margin-top: 30mm; }
.sem .n { font-size: 10pt; font-weight: 700; opacity: .85; letter-spacing: .06em; text-transform: uppercase; }
.sem p { font-size: 12pt; margin-top: 5mm; line-height: 1.4; }
.regla b { display: block; }
.regla { margin-bottom: 2mm; font-size: 8.6pt; line-height: 1.35; }
.vacio td { height: 10mm; }
.pie { position: absolute; bottom: 5mm; left: 8.5mm; right: 8.5mm; font-size: 7pt; color: var(--mut); display: flex; justify-content: space-between; }
"""

paginas = []
n_pag = [0]
def pag(cuerpo, clase="", pie=True):
    n_pag[0] += 1
    p = f'<div class="pie"><span>{e(C.TITULO)}</span><span>{n_pag[0]}</span></div>' if pie else ""
    paginas.append(f'<section class="pag {clase}">{cuerpo}{p}</section>')

# Tapa
pag(f"""<div><div class="de">Un complemento de «La IA hace, vos vendés»</div>
<h1>{e(C.TITULO)}</h1><div class="sub">{e(C.SUBTITULO)}</div></div>
<div><div class="blanca">«¿Qué subo hoy?» 🤔</div>
<div class="burbuja" style="color:var(--ink)">Abrí el día que toca. Ya está escrito: completás los huecos y publicás. ✓✓</div></div>""", "tapa", pie=False)

# Cómo se usa
pag(f"""<h2>Cómo se usa</h2>
<p>En el libro aprendiste a pedirle a la IA lo que necesitás. Acá está el mes hecho: <b>30 días, cada uno con qué publicar, para qué, el texto listo y qué mandar por WhatsApp.</b></p>
<h3>Cada día trae</h3>
<div class="caja post"><b>El posteo</b>, con los <span class="hueco">[huecos]</span> que completás con lo tuyo.</div>
<div class="caja info"><b>La idea de la foto o el video</b>, y <b>la historia</b> del día.</div>
<div class="caja wa"><b>WhatsApp:</b> el estado, la difusión o el mensaje del día.</div>
<h3>Dos formas de completarlo</h3>
<p><b>1. A mano</b> (5 minutos): copiás el texto y cambiás los huecos.</p>
<p><b>2. Con la IA</b> (1 minuto): usás la instrucción de la página siguiente, con tu ficha del Día 0. Te devuelve el texto con tus precios y tu forma de hablar.</p>
<p class="mut chico">Un posteo por día, entre 15 y 30 minutos. Los días 7, 14, 21 y 28 son de repaso: menos trabajo y una difusión por WhatsApp.</p>""")

pag(f"""<h2>La instrucción para la IA</h2>
<p>Copiala entera en ChatGPT (la versión gratis alcanza), pegá tu ficha y la plantilla del día:</p>
<pre class="copia">{e(C.INSTRUCCION_MAESTRA)}</pre>
<p class="chico mut">Truco: si ya tenés una conversación con tu ficha cargada (la del libro), no hace falta pegarla de nuevo. Escribí solo: «Ahora completá esta plantilla» y pegá la del día.</p>""")

pag("<h2>Antes de arrancar: 8 reglas</h2>" + "".join(
    f'<div class="regla"><b>{i+1}. {e(t)}</b>{e(d)}</div>' for i, (t, d) in enumerate(C.REGLAS)))

# Calendario
def filas(ds): return "".join(f"<tr><td><b>{d[0]}</b></td><td>{e(d[3])}</td><td>{e(d[2])}</td></tr>" for d in ds)
cab = '<tr><th>Día</th><th>Qué</th><th>Formato</th></tr>'
pag(f'<h2>El mes, de un vistazo</h2><table>{cab}{filas(C.DIAS[:15])}</table>')
pag(f'<table>{cab}{filas(C.DIAS[15:])}</table>')

# Días
sem_actual = -1
for (num, si, fmt, tit, para, post, visual, hist, wa) in C.DIAS:
    if si != sem_actual:
        sem_actual = si
        s = C.SEMANAS[si]
        pag(f'<div class="n">{e(s[0])}</div><h2>{e(s[1])}</h2><p>{e(s[2])}</p>', "sem")
    pag(f"""<div class="cab"><div class="dia-n">{num}</div><div><div class="fmt">{e(fmt)}</div><h2>{e(tit)}</h2></div></div>
<div class="para">{e(para)}</div>
<span class="etq">El posteo</span><div class="caja post">{plantilla(post)}</div>
<span class="etq">La foto o el video</span><div class="caja info">{plantilla(visual)}</div>
<span class="etq">La historia</span><div class="caja info">{plantilla(hist)}</div>
<span class="etq">WhatsApp</span><div class="caja wa">{plantilla(wa)}</div>""")
    if num == 30:
        vac = "".join('<tr class="vacio"><td></td><td></td><td></td></tr>' for _ in range(6))
        pag(f"""<h2>Tu revisión del mes</h2>
<p class="chico mut">Completala el día 30. Es la base del mes 2.</p>
<table><tr><th>Posteo (día)</th><th>Mensajes que trajo</th><th>¿Lo repito?</th></tr>{vac}</table>
<h3>Para el mes 2</h3>
<div class="caja amar">Repetí las 30 plantillas con otros productos, otras preguntas y otros detalles. Las 4 que mejor anduvieron, hacelas 2 veces. Las que no trajeron nada, cambiales el gancho (la primera frase) antes de descartarlas.</div>""")

# Ejemplos
pag('<h2>4 ejemplos resueltos</h2><p>Con los negocios que te acompañaron en el libro. <b>Son ejemplos armados para enseñar, no negocios reales.</b> Fijate cómo cada uno completó los huecos con sus datos.</p>'
    + "".join(f'<span class="etq">Día {d} · {e(q)}</span><div class="caja post">{e(t).replace(chr(10), "<br>")}</div>' for d, q, t in C.EJEMPLOS[:2]))
pag("".join(f'<span class="etq">Día {d} · {e(q)}</span><div class="caja post">{e(t).replace(chr(10), "<br>")}</div>' for d, q, t in C.EJEMPLOS[2:]))

pag("""<h2>Y ahora, el día 1</h2>
<p>No esperes al lunes ni a tener las fotos perfectas. Abrí el día 1, completá los huecos y publicá.</p>
<div class="burbuja">Recordá la regla del libro: <b>la IA hace el borrador, vos lo revisás.</b> Tus precios, tus fechas y tu forma de hablar, siempre.</div>
<p class="mut chico" style="margin-top:8mm">El mes resuelto · complemento de «La IA hace, vos vendés». Uso personal: podés usar y adaptar los textos para tu negocio todas las veces que quieras; no se puede revender ni compartir el PDF.</p>""")

doc = f"""<!doctype html><html lang="es"><head><meta charset="utf-8">
<link href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,700;12..96,800&family=Plus+Jakarta+Sans:wght@400;600;700;800&display=swap" rel="stylesheet">
<style>{css}</style></head><body>{''.join(paginas)}</body></html>"""
html_path = os.path.join(out_dir, "el-mes-resuelto.html")
open(html_path, "w").write(doc)

js = """const {chromium}=require('playwright');(async()=>{const b=await chromium.launch();const p=await b.newPage();
await p.goto('file://'+process.argv[2],{waitUntil:'networkidle'});await p.evaluate(()=>document.fonts.ready);
await p.pdf({path:process.argv[3],width:'108mm',height:'192mm',printBackground:true,preferCSSPageSize:true});await b.close();})();"""
js_path = os.path.join(out_dir, "_pdf.js")
open(js_path, "w").write(js)
pdf_path = os.path.join(out_dir, "el-mes-resuelto.pdf")
subprocess.run(["node", js_path, os.path.abspath(html_path), os.path.abspath(pdf_path)], check=True)
print(pdf_path, os.path.getsize(pdf_path))

"""Arma un PDF con diseño a partir de capítulos en markdown.
Uso: python3 scripts/armar_pdf.py config.json
"""
import json, re, subprocess, sys, tempfile, os, html
import markdown
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import imagenes
from imagenes import slot
from pypdf import PdfWriter, PdfReader

cfg = json.load(open(sys.argv[1]))
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# Carpeta temporal propia de cada corrida (antes era una ruta fija de otra sesión).
cfg['tmp'] = tempfile.mkdtemp(prefix='armar_pdf_')
# En el PDF van copias JPEG livianas (las PNG pesan ~2 MB cada una y el PDF pasaba los 15 MB).
imagenes.FUENTE = lambda id_, p: 'file://' + imagenes.jpg(id_, os.path.join(cfg['tmp'], 'img'),
                                                          cfg.get('img_lado', 1400), cfg.get('img_calidad', 80))

CSS = r"""
@page { size: 148mm 210mm; margin: 16mm 14mm 18mm 14mm; }
:root{--v:#5B3FD1;--vd:#2E1F73;--am:#FFD84D;--cr:#FFF8EC;--tx:#1E1A2E;--soft:#F3EFFD}
*{box-sizing:border-box}
body{font-family:Inter,sans-serif;font-size:10pt;line-height:1.5;color:var(--tx);margin:0}
h1{font-size:24pt;line-height:1.05;letter-spacing:-.5pt;color:var(--vd);font-weight:900;margin:0 0 4mm;break-before:page;padding-top:6mm;border-top:3mm solid var(--am)}
h1.first{break-before:auto}
h2{font-size:14pt;color:var(--v);font-weight:800;margin:7mm 0 2mm;break-after:avoid}
h3{font-size:11.5pt;color:var(--vd);font-weight:800;margin:5mm 0 1.5mm;break-after:avoid}
p{margin:0 0 2.5mm}
ul,ol{margin:0 0 3mm;padding-left:5mm} li{margin-bottom:1mm}
strong{font-weight:700}
hr{border:none;border-top:.4mm solid #E4DDF6;margin:5mm 0}
table{width:100%;border-collapse:collapse;margin:2mm 0 4mm;font-size:8.6pt;break-inside:avoid}
th{background:var(--v);color:#fff;text-align:left;padding:1.6mm 2mm;font-weight:700}
td{padding:1.6mm 2mm;border-bottom:.3mm solid #E4DDF6;vertical-align:top}
tr:nth-child(even) td{background:#FAF8FF}
blockquote{margin:3mm 0 4mm;padding:3mm 4mm;border-radius:2.5mm;break-inside:avoid}
blockquote p:last-child{margin-bottom:0}
blockquote.ej{background:var(--cr);border-left:1.2mm solid var(--am)}
blockquote.copy{background:var(--soft);border:.5mm solid var(--v);font-size:9.4pt}
blockquote.copy .lab{display:inline-block;background:var(--v);color:#fff;font-size:7pt;font-weight:800;letter-spacing:.8pt;padding:.8mm 2.2mm;border-radius:1.2mm;margin-bottom:2mm}
blockquote.copy.largo{break-inside:auto}
.cb{display:inline-block;width:3.6mm;height:3.6mm;border:.45mm solid var(--v);border-radius:.8mm;margin-right:2mm;vertical-align:-0.6mm}
li.task{list-style:none;margin-left:-5mm}
.ph{display:inline-block;width:100%;height:24mm;border:.5mm dashed #B9AEE8;border-radius:2mm;background:#FAF8FF;color:#8A7FC0;font-size:8pt;text-align:center;line-height:24mm}
em{color:#4a4560}
.img{width:100%;border-radius:3mm;object-fit:cover;display:block;margin:1mm 0 5mm}
.ph-img{background:linear-gradient(135deg,#ECE6FF 0%,#FFF3D1 100%);display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;padding:4mm;border:.4mm dashed #C9BDF3}
.ph-id{background:#5B3FD1;color:#fff;font-size:7pt;font-weight:800;letter-spacing:.6pt;padding:.8mm 2.4mm;border-radius:1.2mm}
.ph-txt{font-size:7.5pt;color:#6E6590;margin-top:2mm;max-width:85%;line-height:1.35}
.avatar{width:12mm!important;height:12mm!important;aspect-ratio:1/1!important;border-radius:50%;display:inline-flex!important;vertical-align:middle;margin:0 2.5mm 0 0!important;padding:0!important;float:left}
.avatar .ph-txt{display:none}.avatar .ph-id{font-size:4.5pt;padding:.4mm .8mm}
p.persona{min-height:13mm}
.opener{margin-top:1mm}
.toc h1{break-before:auto}
"""

COVER = """<!doctype html><html><head><meta charset="utf-8"><style>
@page{size:148mm 210mm;margin:0}
body{margin:0;font-family:Inter,sans-serif}
.c{width:148mm;height:210mm;background:%(bg)s;color:#fff;position:relative;overflow:hidden}
.bar{position:absolute;left:0;top:0;bottom:0;width:7mm;background:#FFD84D}
.k{position:absolute;left:18mm;top:124mm;font-size:8.5pt;font-weight:800;letter-spacing:2pt;text-transform:uppercase;color:#FFD84D}
h1{position:absolute;left:18mm;right:14mm;top:131mm;margin:0;font-size:%(fs)spt;line-height:.98;font-weight:900;letter-spacing:-1.5pt}
.s{position:absolute;left:18mm;right:18mm;top:%(stop)smm;font-size:12.5pt;line-height:1.35;opacity:.95}
.b{position:absolute;left:18mm;bottom:18mm;right:18mm;font-size:9pt;opacity:.85;border-top:.4mm solid rgba(255,255,255,.35);padding-top:4mm}
.ci{position:absolute;left:0;right:0;top:0;height:118mm}
.ci .img{width:100%%!important;height:118mm!important;aspect-ratio:auto!important;margin:0!important;border-radius:0!important;object-fit:cover}
.ci .ph-img{background:linear-gradient(160deg,#8C76F0 0%%,#FFE38A 100%%);border:none}
.ci .ph-id{font-size:10pt;padding:1.5mm 4mm}.ci .ph-txt{font-size:9pt;color:#3B2E80;max-width:70%%}
.fade{position:absolute;left:0;right:0;top:88mm;height:31mm;background:linear-gradient(to bottom,rgba(0,0,0,0),%(bg)s)}
.ph-img{display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;font-family:Inter,sans-serif}
.ph-id{background:#5B3FD1;color:#fff;font-weight:800;border-radius:1.5mm}.ph-txt{margin-top:2mm;line-height:1.35}
</style></head><body><div class="c"><div class="ci">%(img)s</div><div class="fade"></div><div class="bar"></div>
<div class="k">%(kicker)s</div><h1>%(title)s</h1><div class="s">%(sub)s</div><div class="b">%(bottom)s</div></div></body></html>"""

def fix_lists(text):
    out, prev = [], ''
    for line in text.split('\n'):
        core = re.sub(r'^(> ?)+', '', line)
        pcore = re.sub(r'^(> ?)+', '', prev)
        is_item = re.match(r'\s*([-*]|\d+\.)\s', core)
        prev_item = re.match(r'\s*([-*]|\d+\.)\s', pcore)
        if is_item and pcore.strip() and not prev_item and not core.startswith(' '):
            out.append(re.match(r'^(> ?)*', line).group(0).rstrip())
        out.append(line); prev = line
    return '\n'.join(out)

def md_to_html(text, first):
    text = fix_lists(text)
    text = re.sub(r'^- \[ \] ', '- @@CB@@ ', text, flags=re.M)
    text = re.sub(r'\[(FOTO-[ADE]\d)\]', r'@@\1@@', text)
    h = markdown.markdown(text, extensions=['tables', 'sane_lists'])
    h = h.replace('<li>@@CB@@ ', '<li class="task"><span class="cb"></span>')
    h = re.sub(r'@@(FOTO-[ADE]\d)@@', lambda m: slot(m.group(1), 'tabla'), h)
    def bq(m):
        inner = m.group(1)
        plain = re.sub('<[^>]+>', '', inner).strip()
        is_copy = 'COPIÁ Y PEGÁ' in inner or re.match(r'^\d+\.\s', plain) or cfg.get('quotes_are_copy')
        if 'COPIÁ Y PEGÁ' in inner:
            inner = re.sub(r'<strong>COPIÁ Y PEGÁ</strong>\s*(<br\s*/?>)?', '<span class="lab">COPIÁ Y PEGÁ</span><br>', inner, count=1)
        elif is_copy:
            inner = inner.replace('<p>', '<p><span class="lab">COPIÁ Y PEGÁ</span><br>', 1)
        cls = 'copy' if is_copy else 'ej'
        if len(plain) > 900:
            cls += ' largo'
        return f'<blockquote class="{cls}">{inner}</blockquote>'
    h = re.sub(r'<blockquote>(.*?)</blockquote>', bq, h, flags=re.S)
    for tag in ('h1', 'h2'):
        def op(m):
            txt = re.sub('<[^>]+>', '', m.group(2))
            for k, v in cfg.get('openers', {}).items():
                if txt.strip().startswith(k):
                    return m.group(0) + slot(v, 'opener')
            return m.group(0)
        h = re.sub(rf'<({tag})>(.*?)</{tag}>', op, h)
    for emo, iid in cfg.get('avatars', {}).items():
        h = re.sub(rf'<p><strong>{emo}\ufe0f?\s*', lambda m: '<p class="persona">' + slot(iid, 'avatar') + '<strong>', h)
    if first:
        h = h.replace('<h1>', '<h1 class="first">', 1)
    return h

def render(html_str, out, footer):
    with tempfile.NamedTemporaryFile('w', suffix='.html', delete=False, dir=cfg['tmp']) as f:
        f.write(html_str); path = f.name
    js = f"""
const {{ chromium }} = require('playwright');
(async () => {{
  const b = await chromium.launch(); const p = await b.newPage();
  await p.goto('file://{path}'); await p.waitForTimeout(300);
  await p.pdf({{ path: {json.dumps(out)}, preferCSSPageSize: true, printBackground: true,
    displayHeaderFooter: {str(footer).lower()}, headerTemplate: '<span></span>',
    footerTemplate: {json.dumps(cfg.get('footer_html',''))} }});
  await b.close();
}})();"""
    jsf = path + '.js'; open(jsf, 'w').write(js)
    subprocess.run(['node', jsf], check=True)

body = ''
for i, ch in enumerate(cfg['chapters']):
    t = open(os.path.join(ROOT, ch)).read()
    for pat in cfg.get('strip', []):
        pat, repl = (pat, '') if isinstance(pat, str) else pat
        t = re.sub(pat, repl, t, flags=re.M | re.S)
    body += md_to_html(t, i == 0)
# El cierre (desde el bloque anterior a la última línea divisoria) va junto, para que la última
# página no quede con una sola frase suelta.
_i = body.rfind('<hr')
if _i > 0:
    _j = max(body.rfind('</p>', 0, _i), body.rfind('</blockquote>', 0, _i), body.rfind('</ul>', 0, _i))
    if body.startswith('</blockquote>', _j):
        _k = body.rfind('<blockquote', 0, _j)
    elif body.startswith('</ul>', _j):
        _k = body.rfind('<ul', 0, _j)
    else:
        _k = body.rfind('<p', 0, _j)
    if body.startswith('<blockquote', _k) and len(re.sub('<[^>]+>', '', body[_k:_j])) > 600:
        # cuadro largo: se parte y solo su último párrafo baja con el cierre
        _cls = re.match(r'<blockquote class="([^"]*)"', body[_k:]).group(1)
        _k = body.rfind('<p', _k, _j)
        body = body[:_k] + f'</blockquote><blockquote class="{_cls}" style="margin-top:0">' + body[_k:]
        _k = body.rfind('<blockquote', 0, _k + 60)
    if _k > 0 and len(re.sub('<[^>]+>', '', body[_k:])) < 1500:
        body = body[:_k] + '<div style="break-inside:avoid">' + body[_k:] + '</div>'
doc = f'<!doctype html><html lang="es"><head><meta charset="utf-8"><style>{CSS}</style></head><body>{body}</body></html>'
cfg['footer_html'] = ('<div style="width:100%;font-family:Inter,sans-serif;font-size:7pt;color:#8A84A0;'
                      'padding:0 14mm;display:flex;justify-content:space-between">'
                      f'<span>{html.escape(cfg["footer"])}</span><span class="pageNumber"></span></div>')
cfg['cover']['img'] = slot(cfg['cover']['image'])
cover = COVER % cfg['cover']
tmpd = cfg['tmp']
render(cover, f'{tmpd}/cover.pdf', False)
render(doc, f'{tmpd}/body.pdf', True)
w = PdfWriter()
for f in (f'{tmpd}/cover.pdf', f'{tmpd}/body.pdf'):
    for pg in PdfReader(f).pages: w.add_page(pg)
w.add_metadata({'/Title': cfg['meta_title']})
w.write(os.path.join(ROOT, cfg['out']))
print(cfg['out'], len(w.pages), 'páginas')

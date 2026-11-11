// Exporta a PNG cada <div data-out="nombre"> de un HTML.
// Uso: node scripts/render_anuncios.js <archivo.html> <carpeta-de-salida>
//   piezas fijas:  node scripts/render_anuncios.js anuncios/src/creativos.html anuncios/img
//   cuadros de video: node scripts/render_anuncios.js anuncios/src/video-a.html /tmp/cuadros-a
const { chromium } = require('playwright');
const path = require('path');
const fs = require('fs');
(async () => {
  const [src, out] = process.argv.slice(2).map(p => path.resolve(p));
  fs.mkdirSync(out, { recursive: true });
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 1200, height: 2000 }, deviceScaleFactor: 1 });
  await p.goto('file://' + src, { waitUntil: 'networkidle' });
  await p.evaluate(() => document.fonts.ready);
  await p.waitForTimeout(400);
  const ids = await p.$$eval('[data-out]', els => els.map(e => e.dataset.out));
  for (const n of ids) await p.locator(`[data-out="${n}"]`).screenshot({ path: `${out}/${n}.png` });
  console.log(ids.length + ' archivos en ' + out);
  await b.close();
})();

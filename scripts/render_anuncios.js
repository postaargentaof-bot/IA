const { chromium } = require('playwright');
(async () => {
  const [src, out] = process.argv.slice(2);
  const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: 1200, height: 1500 }, deviceScaleFactor: 1 });
  await p.goto('file://' + src); await p.waitForTimeout(300);
  const names = { a1: 'anuncio1-whatsapp', c1: 'anuncio2-carrusel-1', c2: 'anuncio2-carrusel-2', c3: 'anuncio2-carrusel-3', c4: 'anuncio2-carrusel-4', c5: 'anuncio2-carrusel-5', a3: 'anuncio3-audio' };
  for (const [id, n] of Object.entries(names)) await p.locator('#' + id).screenshot({ path: `${out}/${n}.png` });
  await b.close();
})();

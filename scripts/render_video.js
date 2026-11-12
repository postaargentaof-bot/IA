// Dibuja un video de anuncios/src/video2/ cuadro por cuadro y lo pasa a ffmpeg (sin audio).
// Uso:
//   node scripts/render_video.js <v: a|d|r2|r3> <f: v|h> <salida.mp4>      -> video mudo + <salida>.sfx.json
//   node scripts/render_video.js <v> <f> --capturas <carpeta> t1,t2,...      -> PNG sueltos para revisar
const { chromium } = require('playwright');
const http = require('http'), fs = require('fs'), path = require('path'), { spawn } = require('child_process');
const ROOT = path.resolve(__dirname, '..');
const TYPES = { '.html': 'text/html', '.js': 'text/javascript', '.css': 'text/css', '.json': 'application/json', '.png': 'image/png', '.jpg': 'image/jpeg' };
(async () => {
  const [vid, fmt, out, extra] = process.argv.slice(2);
  const srv = http.createServer((q, r) => {
    const p = path.join(ROOT, decodeURIComponent(q.url.split('?')[0]));
    if (!p.startsWith(ROOT) || !fs.existsSync(p)) { r.writeHead(404); return r.end(); }
    r.writeHead(200, { 'Content-Type': TYPES[path.extname(p)] || 'application/octet-stream' }); fs.createReadStream(p).pipe(r);
  }).listen(0);
  const port = srv.address().port;
  const W = 1080, H = fmt === 'v' ? 1920 : 1350, FPS = 30;
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: W, height: H }, deviceScaleFactor: 1 });
  p.on('pageerror', e => console.error('ERROR en la página:', e.message));
  await p.goto(`http://localhost:${port}/anuncios/src/video2/video.html?v=${vid}&f=${fmt}`, { waitUntil: 'networkidle' });
  await p.waitForFunction(() => window.LISTO === true, null, { timeout: 30000 });
  const DUR = await p.evaluate(() => window.DUR);
  if (out === '--capturas') {
    fs.mkdirSync(extra, { recursive: true });
    for (const t of process.argv[6].split(',').map(Number)) {
      await p.evaluate(t => setTime(t), t);
      await p.screenshot({ path: `${extra}/${vid}-${fmt}-${t.toFixed(2).padStart(5, '0')}.png` });
    }
  } else {
    const ff = spawn('ffmpeg', ['-y', '-loglevel', 'error', '-f', 'image2pipe', '-framerate', String(FPS), '-c:v', 'mjpeg', '-i', '-',
      '-c:v', 'libx264', '-preset', 'medium', '-crf', '20', '-pix_fmt', 'yuv420p', out], { stdio: ['pipe', 'inherit', 'inherit'] });
    const n = Math.ceil(DUR * FPS);
    for (let i = 0; i < n; i++) {
      await p.evaluate(t => setTime(t), i / FPS);
      const buf = await p.screenshot({ type: 'jpeg', quality: 92 });
      if (!ff.stdin.write(buf)) await new Promise(r => ff.stdin.once('drain', r));
    }
    ff.stdin.end();
    await new Promise(r => ff.on('close', r));
    const sfx = await p.evaluate(() => SFX);
    fs.writeFileSync(out + '.sfx.json', JSON.stringify({ dur: DUR, sfx }));
    console.log(out, n, 'cuadros', DUR.toFixed(2), 's');
  }
  await b.close(); srv.close();
})();

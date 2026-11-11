// Motor de animación de los videos: cada cuadro se dibuja con setTime(t).
// La página se abre como video.html?v=a&f=v  (v = a | d | r2 | r3 ; f = v (9:16) | h (4:5))
// scripts/render_video.js la recorre cuadro por cuadro y arma el mp4 con ffmpeg.
'use strict';
const Q = new URLSearchParams(location.search);
const FMT = Q.get('f') || 'v', VID = Q.get('v') || 'a';
const W = 1080, H = FMT === 'v' ? 1920 : 1350;
// Zona segura (regla 07-creativos): todo el texto entre los 290 y los 1.290 px en 9:16.
const B = FMT === 'v' ? { cap: 300, top: 440, bot: 1290 } : { cap: 54, top: 190, bot: 1290 };
document.documentElement.style.setProperty('--W', W + 'px');
document.documentElement.style.setProperty('--H', H + 'px');
document.documentElement.style.setProperty('--cap', B.cap + 'px');
document.documentElement.style.setProperty('--top', B.top + 'px');
document.documentElement.style.setProperty('--bot', B.bot + 'px');
document.body.classList.add('f-' + FMT, 'v-' + VID);

// ---------- utilidades ----------
const clamp = (x, a = 0, b = 1) => Math.min(b, Math.max(a, x));
const lerp = (a, b, k) => a + (b - a) * k;
const prog = (t, a, b) => clamp((t - a) / (b - a));
const eOut = k => 1 - Math.pow(1 - k, 3);
const eInOut = k => k < .5 ? 4 * k * k * k : 1 - Math.pow(-2 * k + 2, 3) / 2;
const eBack = k => { const c = 1.9; return 1 + (c + 1) * Math.pow(k - 1, 3) + c * Math.pow(k - 1, 2); };
const pop = (t, t0, d = .32) => eBack(prog(t, t0, t0 + d));
function mk(tag, cls, html, parent) {
  const e = document.createElement(tag);
  if (cls) e.className = cls;
  if (html != null) e.innerHTML = html;
  (parent || document.getElementById('stage')).appendChild(e);
  return e;
}
const css = (e, o) => Object.assign(e.style, o);
const SFX = [];
const sfx = (t, s, vol = 1) => SFX.push([+t.toFixed(3), s, vol]);

// ---------- subtítulos karaoke ----------
let WORDS = [], CHUNKS = [], CAPHIDE = [];
function capSetup(words, accentCls) {
  WORDS = words;
  let cur = [];
  words.forEach((w, i) => {
    cur.push(i);
    const end = /[.,?!:]$/.test(w[0]) || cur.length >= 3;
    if (end || i === words.length - 1) { CHUNKS.push(cur); cur = []; }
  });
  window.CAPBASE = accentCls || '';
  const cap = mk('div', 'cap ' + (accentCls || ''));
  cap.id = 'cap';
}
function capUpdate(t) {
  const cap = document.getElementById('cap');
  if (!cap) return;
  const hidden = CAPHIDE.some(([a, b]) => t >= a && t < b);
  let ci = -1;
  for (let i = 0; i < CHUNKS.length; i++) if (WORDS[CHUNKS[i][0]][1] <= t + 0.04) ci = i;
  if (hidden || ci < 0) { cap.style.opacity = 0; return; }
  const ch = CHUNKS[ci];
  const t0 = WORDS[ch[0]][1];
  let wi = ch[0];
  ch.forEach(i => { if (WORDS[i][1] <= t + 0.04) wi = i; });
  if (cap.dataset.ci !== String(ci)) {
    cap.innerHTML = ch.map(i => `<span data-i="${i}">${WORDS[i][0].replace(/[.,:]$/, '')}</span>`).join(' ');
    cap.dataset.ci = ci;
  }
  cap.style.opacity = 1;
  const k = eBack(prog(t, t0 - .04, t0 + .16));
  cap.style.transform = `translateX(-50%) scale(${lerp(.86, 1, k)})`;
  cap.querySelectorAll('span').forEach(s => {
    const i = +s.dataset.i;
    s.classList.toggle('on', i === wi);
    s.classList.toggle('fut', i > wi);
    if (i === wi) {
      const kk = eBack(prog(t, WORDS[i][1] - .04, WORDS[i][1] + .12));
      s.style.transform = `scale(${lerp(.9, 1, kk)})`;
    } else s.style.transform = '';
  });
}

// ---------- escenas ----------
const SCENES = [];
let FLASHES = [];
function scene(t0, t1, cls, build, update, opt = {}) {
  const el = mk('div', 'scene ' + (cls || ''));
  const ctx = build(el) || {};
  SCENES.push({ t0, t1, el, ctx, update, opt });
  if (t0 > 0.01 && !opt.noWhoosh) sfx(t0 - 0.12, 'whoosh', .55);
  if (opt.flash) FLASHES.push(t0);
  return ctx;
}
let SHAKES = [];
function setTime(t) {
  for (const s of SCENES) {
    const on = t >= s.t0 && t < s.t1;
    s.el.style.display = on ? 'block' : 'none';
    if (!on) continue;
    const lt = t - s.t0;
    const k = eOut(prog(lt, 0, .26));
    const kind = s.opt.enter || 'zoom';
    let tr = '';
    if (kind === 'zoom') tr = `scale(${lerp(1.10, 1, k)})`;
    if (kind === 'up') tr = `translateY(${lerp(140, 0, k)}px)`;
    if (kind === 'left') tr = `translateX(${lerp(260, 0, k)}px)`;
    if (kind === 'none') tr = '';
    s.el.style.transform = tr;
    s.el.style.opacity = kind === 'none' ? 1 : clamp(k * 1.6);
    s.update(lt, t, s.ctx);
  }
  // sacudida de cámara
  let sx = 0, sy = 0;
  for (const [ts, a] of SHAKES) {
    const d = t - ts;
    if (d >= 0 && d < .28) { const f = (1 - d / .28) * a; sx += Math.sin(d * 90) * f; sy += Math.cos(d * 70) * f; }
  }
  document.getElementById('stage').style.transform = `translate(${sx}px,${sy}px)`;
  // flash de corte
  let fl = 0;
  for (const tf of FLASHES) { const d = t - tf; if (d >= 0 && d < .18) fl = Math.max(fl, .55 * (1 - d / .18)); }
  document.getElementById('flash').style.opacity = fl;
  const cap = document.getElementById('cap');
  if (cap) {
    const act = SCENES.find(s => t >= s.t0 && t < s.t1);
    const want = 'cap ' + (window.CAPBASE || '') + ' ' + ((act && act.opt.cap) || '');
    if (cap.className !== want) cap.className = want;
  }
  capUpdate(t);
  if (window.EXTRA) window.EXTRA(t);
}

// ---------- piezas reutilizables ----------
// burbuja de chat que aparece con rebote (crece de alto para empujar a las demás)
function bubble(parent, text, hora, yo, t0, extraCls = '') {
  const wrap = mk('div', 'bw ' + (yo ? 'r' : 'l'), null, parent);
  const b = mk('div', 'b ' + (yo ? 'yo ' : 'ell ') + extraCls, `${text}<span class="h">${hora}${yo ? ' <i class="ck">✓✓</i>' : ''}</span>`, wrap);
  return { wrap, b, t0 };
}
function bubbleUpdate(bb, t, full = 260) {
  const k = prog(t, bb.t0, bb.t0 + .2);
  if (t < bb.t0) { bb.wrap.style.display = 'none'; return; }
  bb.wrap.style.display = 'flex';
  bb.wrap.style.maxHeight = (k >= 1 ? 1000 : lerp(0, full, eOut(k))) + 'px';
  const p = pop(t, bb.t0, .3);
  bb.b.style.transform = `scale(${lerp(.4, 1, p)})`;
  bb.b.style.opacity = clamp(k * 3);
}
function typed(text, t, a, b) {
  const n = Math.round(text.length * prog(t, a, b));
  return text.slice(0, n);
}
function typeTicks(a, b, n) { for (let i = 0; i < n; i++) sfx(lerp(a, b, i / n), 'tick', .35); }
function phone(parent, header, sub, avatar, opt = {}) {
  const root = mk('div', 'tel' + (opt.dark ? ' dark' : ''), null, parent);
  const bar = mk('div', 'bar', `<img src="${avatar}" alt=""><div class="nm">${header}<small>${sub}</small></div><div class="badge" style="display:none">0</div>`, root);
  const chat = mk('div', 'chat', null, root);
  const input = mk('div', 'input', '<span class="tx"></span><i class="cur"></i>', root);
  const kb = mk('div', 'kb', null, root);
  const rows = [10, 9, 7];
  const keys = [];
  rows.forEach((n, r) => { const row = mk('div', 'kr', null, kb); for (let i = 0; i < n; i++) keys.push(mk('i', '', null, row)); });
  return { root, bar, chat, input, kb, keys, badge: bar.querySelector('.badge'), tx: input.querySelector('.tx') };
}
function pressKeys(ph, t, a, b, n) {
  ph.keys.forEach(k => k.classList.remove('on'));
  if (t >= a && t < b) {
    const i = Math.floor(prog(t, a, b) * n);
    ph.keys[(i * 7 + 3) % ph.keys.length].classList.add('on');
  }
}
function stamp(parent, text, cls = '') { return mk('div', 'stamp ' + cls, text, parent); }
function stampUpdate(el, t, t0, rot = -6, from = 2.4) {
  if (t < t0) { el.style.opacity = 0; return; }
  const p = pop(t, t0, .28);
  el.style.opacity = clamp((t - t0) / .06);
  el.style.transform = `translate(-50%,-50%) rotate(${rot}deg) scale(${lerp(from, 1, p)})`;
}
function chip(parent, html, cls = '') { return mk('div', 'chip ' + cls, html, parent); }
function chipUpdate(el, t, t0, dx = 0, dy = 40) {
  if (t < t0) { el.style.opacity = 0; return; }
  const p = pop(t, t0, .34);
  el.style.opacity = clamp((t - t0) / .1);
  el.style.transform = `translate(${lerp(dx, 0, p)}px,${lerp(dy, 0, p)}px) scale(${lerp(.6, 1, p)})`;
}
function ring(parent) {
  const d = mk('div', 'ring', `<svg viewBox="0 0 200 200"><circle cx="100" cy="100" r="86" class="bgc"/><circle cx="100" cy="100" r="86" class="fg"/></svg><div class="rt">1 h</div>`, parent);
  return d;
}
function ringUpdate(el, t, a, b) {
  const k = eInOut(prog(t, a, b));
  const c = 2 * Math.PI * 86;
  el.querySelector('.fg').style.strokeDasharray = `${c * k} ${c}`;
  el.style.transform = `scale(${lerp(.5, 1, pop(t, a - .15, .35))})`;
}
function tap(parent) { return mk('div', 'tap', null, parent); }
function tapUpdate(el, t, t0) {
  const d = t - t0;
  if (d < 0 || d > .6) { el.style.opacity = 0; return; }
  el.style.opacity = 1 - d / .6;
  el.style.transform = `translate(-50%,-50%) scale(${lerp(.3, 1.6, eOut(d / .6))})`;
}

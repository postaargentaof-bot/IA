// Video A «¿Precio?» y sus 2 ganchos de reserva (r2 «/precios primero», r3 «23:40»).
// Los tiempos salen de la voz (voz-*.json). El cuerpo (desde «La IA te escribe…») es el mismo en los 3.
'use strict';
const IMG = '../../../landing/assets/';
const TAPA = '../paginas/tapa.jpg';
const CARO = IMG + 'IMG-02.jpg';
const CAROH = 'Malva · ejemplo del libro';
const RESP = '¡Hola! El buzo gris está $18.500. Hay en S, M y L. Envío a todo el país o retiro en Lanús. ¿Qué talle buscás? 😊';
const POPS = [['/precios', '¡Hola! El buzo gris está…'], ['/envios', 'Mando por correo a todo…'], ['/pago', 'Transferencia o Mercado…']];

function wt(words, w, from = 0) { // tiempo de la primera palabra que empieza con w desde el segundo «from»
  const x = words.find(q => q[1] >= from && q[0].toLowerCase().startsWith(w.toLowerCase()));
  return x ? x[1] : from;
}

function armarA(words, vid) {
  capSetup(words, '');
  const tLa = words.find((q, i) => q[0] === 'La' && words[i + 1] && words[i + 1][0] === 'IA')[1];
  const off = tLa - 5.522; // corrimiento del cuerpo respecto del video A
  const fin = words[words.length - 1][2] + 0.55;
  if (vid === 'a') hookA(words, tLa);
  if (vid === 'r2') hookR2(words, tLa);
  if (vid === 'r3') hookR3(words, tLa);
  cuerpo(words, off, fin);
}

// ---------------- gancho de A: el chat se llena de «¿precio?» ----------------
const PRE = ['¿precio?', 'Hola! precio?', '¿Precio del buzo?', 'precio 🙏', '¿Precio? ¿Hay talle M?', '¿precio?', 'hola, precio y talles?', '¿PRECIO?', 'precio porfa', '¿Me pasás precio?'];
function floodScene(t0, t1, times, stamps, dark = false, horas = null) {
  scene(t0, t1, '', el => {
    const ph = phone(el, CAROH, dark ? '23:40' : 'en línea', CARO, { dark });
    const bs = times.map((tt, i) => bubble(ph.chat, PRE[i % PRE.length], horas ? horas[i] : `10:${(12 + i * 4) % 60}`.padEnd(5, '0'), false, tt));
    bs.forEach(b => sfx(b.t0, 'pop', .8));
    const st = stamps.map(([tx]) => stamp(el, tx, dark ? '' : ''));
    stamps.forEach(([, ts]) => SHAKES.push([ts, 12]));
    return { ph, bs, st };
  }, (lt, t, c) => {
    c.bs.forEach(b => bubbleUpdate(b, t));
    const n = c.bs.filter(b => t >= b.t0).length;
    c.ph.badge.style.display = n ? 'flex' : 'none';
    c.ph.badge.textContent = n;
    c.ph.badge.style.transform = `scale(${lerp(1.5, 1, eOut(prog(t, c.bs[Math.max(0, n - 1)].t0, c.bs[Math.max(0, n - 1)].t0 + .2)))})`;
    stamps.forEach(([, ts, y, rot], i) => {
      stampUpdate(c.st[i], t, ts, rot);
      c.st[i].style.top = (B.top + y * (B.bot - B.top)) + 'px';
    });
  }, { enter: t0 === 0 ? 'none' : 'zoom', flash: t0 > 0 });
}

function hookA(words, tLa) {
  const p = words.filter(w => /precio/i.test(w[0])).slice(0, 3).map(w => w[1]);
  const tSi = wt(words, 'Si'), tEsto = wt(words, 'Esto');
  floodScene(0, tSi, [0, .1, .22, p[1], p[1] + .12, p[1] + .26, p[2], p[2] + .1, p[2] + .2, p[2] + .32],
    [['¿Precio?', p[0], .22, -7], ['¿Precio?', p[1], .45, 5], ['¿Precio?', p[2], .68, -3]]);
  CAPHIDE.push([0, tSi]);
  listaScene(tSi, tEsto);
  horaScene(tEsto, tLa, 'Esto lo resolvés', 'en 1 hora.', wt(words, 'en', tEsto));
}

function listaScene(t0, t1) {
  const gente = [['Vicky', '¿precio?', 3, '#F7B7A3'], ['Lu', 'Hola! precio del buzo?', 2, '#B9D7EA'], ['Romi', '¿Precio? ¿Hacés envíos?', 4, '#F1D58A'],
    ['Pato', 'precio 🙏', 1, '#C5E0B4'], ['Juli', '¿Me pasás precio?', 2, '#D9C3E8'], ['Sabri', '¿precio?', 5, '#F5C6D6'], ['Flor', 'Holaa, ¿precio?', 1, '#BFE3DC'], ['Meli', '¿precio y talles?', 2, '#F2CFA8']];
  scene(t0, t1, '', el => {
    const l = mk('div', 'lista', '<div class="tit">Chats</div>', el);
    const rows = gente.map(([n, m, k, c], i) => {
      const r = mk('div', 'c', `<div class="av" style="background:${c}"></div><div><h3>${n}</h3><p>${m}</p></div><span class="n">${k}</span>`, l);
      sfx(t0 + .05 + i * .09, 'pop', .4);
      return r;
    });
    return { rows };
  }, (lt, t, c) => {
    c.rows.forEach((r, i) => {
      const k = eOut(prog(lt, .05 + i * .09, .35 + i * .09));
      r.style.transform = `translateX(${lerp(700, 0, k)}px)`;
      r.style.opacity = k;
      const n = r.querySelector('.n');
      n.style.transform = `scale(${1 + .18 * Math.max(0, Math.sin((lt - i * .2) * 9)) * (lt > .5 ? 1 : 0)})`;
    });
  }, { enter: 'left', flash: true });
}

function horaScene(t0, t1, l1, l2, t2) {
  scene(t0, t1, 'verdebg', el => {
    const rays = mk('div', 'rays', null, el);
    const big = mk('div', 'big', `<h1><span class="l l1">${l1}</span><span class="l l2"><em>${l2}</em></span></h1>`, el);
    const r = ring(el);
    sfx(t2, 'ding', .5);
    return { rays, big, r };
  }, (lt, t, c) => {
    c.rays.style.transform = `rotate(${lt * 14}deg)`;
    c.big.style.top = (B.top + 40) + 'px';
    const a = c.big.querySelector('.l1'), b = c.big.querySelector('.l2');
    a.style.transform = `translateY(${lerp(60, 0, eOut(prog(lt, 0, .3)))}px)`;
    a.style.opacity = prog(lt, 0, .2);
    const pb = pop(t, t2, .35);
    b.style.transform = `scale(${lerp(1.8, 1, pb)})`; b.style.transformOrigin = '0 50%';
    b.style.opacity = t >= t2 ? 1 : 0;
    c.r.style.top = (B.bot - 360) + 'px';
    ringUpdate(c.r, t, t2, t1 - .1);
  }, { enter: 'zoom', flash: true });
  CAPHIDE.push([t0, t1]);
}

// ---------------- gancho r2: /precios primero ----------------
function hookR2(words, tLa) {
  const tY = wt(words, 'y'), tAsi = wt(words, 'Así');
  respuestaScene(0, tAsi, -1, 0.12, tY, true);
  horaScene(tAsi, tLa, 'Así se arma,', 'en 1 hora.', wt(words, 'en', tAsi));
}
// ---------------- gancho r3: 23:40 ----------------
function hookR3(words, tLa) {
  const tY = wt(words, 'y', 1), tEsto = wt(words, 'Esto');
  const horas = ['23:31', '23:33', '23:34', '23:36', '23:38', '23:39', '23:40', '23:40', '23:40', '23:40'];
  floodScene(0, tEsto, [0, .25, .5, .8, 1.1, 1.4, tY, tY + .25, tY + .5, tY + .8],
    [['23:40', wt(words, 'once'), .2, -5], ['¿Precio?', wt(words, 'precio', 2), .55, 4]], true, horas);
  CAPHIDE.push([0, .3]);
  horaScene(tEsto, tLa, 'Esto lo resolvés', 'en 1 hora.', wt(words, 'en', tEsto));
}

// ---------------- chat: te escriben, ponés /precios, sale la respuesta ----------------
function respuestaScene(t0, t1, tIn, tType, tSale, primero = false) {
  scene(t0, t1, '', el => {
    const ph = phone(el, CAROH, 'en línea', CARO);
    const v1 = bubble(ph.chat, 'Me llegó el pedido, ¡me encantó! 😍', '18:02', false, -1);
    const v2 = bubble(ph.chat, '¡Qué lindo! Gracias por elegirnos 💚', '18:05', true, -1);
    v1.b.style.opacity = .55; v2.b.style.opacity = .55;
    const q = bubble(ph.chat, 'Hola!! precio del buzo gris? 🙏', '21:47', false, tIn);
    const r = bubble(ph.chat, RESP, '21:47', true, tSale);
    const pp = mk('div', 'pop', POPS.map(([a, b], i) => `<div class="${i === 0 ? 'sel' : ''}"><b>${a}</b>${b}</div>`).join(''), ph.root);
    const tp = tap(ph.root);
    sfx(tIn, 'pop', .8); typeTicks(tType, tType + .55, 8); sfx(tSale - .08, 'tap', .7); sfx(tSale, 'ding', .7);
    return { ph, q, r, pp, tp };
  }, (lt, t, c) => {
    bubbleUpdate(c.q, t); bubbleUpdate(c.r, t, 420);
    const typing = t < tSale;
    c.ph.tx.textContent = typing ? typed('/precios', t, tType, tType + .55) : '';
    pressKeys(c.ph, t, tType, tType + .55, 8);
    const show = t >= tType + .15 && t < tSale;
    const k = eOut(prog(t, tType + .15, tType + .4));
    const chatBottom = (H + 60 - B.bot) + 108;
    c.pp.style.bottom = (chatBottom + 6) + 'px';
    c.pp.style.display = show ? 'block' : 'none';
    c.pp.style.transform = `translateY(${lerp(80, 0, k)}px)`; c.pp.style.opacity = k;
    c.tp.style.left = '230px'; c.tp.style.bottom = (chatBottom + 6 + 3 * 72 - 40) + 'px'; c.tp.style.top = 'auto';
    tapUpdate(c.tp, t, tSale - .12);
    const ck = c.r.b.querySelector('.ck'); if (ck) ck.classList.toggle('leido', t > tSale + .6);
  }, { enter: primero ? 'none' : 'up', flash: !primero });
}

// ---------------- cuerpo común ----------------
function cuerpo(words, off, fin) {
  const T = x => x + off;
  // IA escribe las 15 respuestas
  const tTe = wt(words, 'Te', T(9.5));
  iaScene(T(5.522), tTe, T(5.6), T(6.55), T(7.0), tTe - .25);
  // te escriben ¿precio? → /precios → respuesta lista
  const tEs = wt(words, 'Es', T(13.3));
  respuestaScene(tTe, tEs, tTe + .1, wt(words, '/precios', tTe), wt(words, 'y', T(11.9)));
  // tapa + Día 1
  const tToca = wt(words, 'Tocá', T(17));
  tapaScene(tEs, tToca, [['DÍA 1', wt(words, 'Día', tEs), 'am'], ['15 respuestas listas', wt(words, 'de', tEs + .5), ''], ['ChatGPT gratis', wt(words, 'ChatGPT', tEs), '']]);
  ctaScene(tToca, fin + .01, wt(words, 'Comprar', tToca));
}

function iaScene(t0, t1, tp0, tp1, tr0, tr1) {
  const PIDE = 'Usando la ficha de mi negocio, escribime las respuestas para las 15 preguntas que más me hacen…';
  const RS = [['/precios', '¡Hola! El buzo gris está $18.500. Hay S, M y L. ¿Qué talle buscás? 😊'], ['/envios', 'Mando por correo a todo el país, y si estás cerca, en el día por moto.'],
    ['/talles', 'Te paso los talles de cada prenda…'], ['/pago', 'Transferencia o Mercado Pago.'], ['/cambios', 'Tenés 30 días para cambiarlo, con etiqueta.'], ['/stock', 'Sí, lo tengo. ¿Te lo separo?']];
  scene(t0, t1, '', el => {
    const ia = mk('div', 'ia', `<div class="cab"><i></i>Tu chat con la IA · ChatGPT gratis</div><div class="pide"></div><div class="dots"><i></i><i></i><i></i></div><div class="resp"></div>`, el);
    const resp = ia.querySelector('.resp');
    const lines = RS.map(([a, b]) => mk('div', '', `<b>${a}</b><span></span>`, resp));
    typeTicks(tp0, tp1, 14);
    RS.forEach((_, i) => sfx(lerp(tr0, tr1, i / RS.length), 'pop', .35));
    return { ia, lines, pide: ia.querySelector('.pide'), dots: ia.querySelector('.dots') };
  }, (lt, t, c) => {
    c.pide.textContent = typed(PIDE, t, tp0, tp1);
    c.dots.style.display = t > tp1 && t < tr0 ? 'flex' : 'none';
    [...c.dots.children].forEach((d, i) => d.style.transform = `translateY(${Math.sin(t * 12 - i) * 8}px)`);
    const n = RS.length, seg = (tr1 - tr0) / n;
    c.lines.forEach((l, i) => {
      const a = tr0 + i * seg;
      l.style.display = t >= a ? 'block' : 'none';
      l.querySelector('b').style.transform = `scale(${lerp(.5, 1, pop(t, a, .25))})`;
      l.querySelector('span').textContent = typed(RS[i][1], t, a + .05, a + seg * .9);
    });
  }, { enter: 'zoom', flash: true });
}

function tapaScene(t0, t1, chips) {
  scene(t0, t1, 'verdebg', el => {
    const rays = mk('div', 'rays', null, el);
    const tp = mk('img', 'tapa', null, el); tp.src = TAPA;
    const cs = chips.map(([tx, , cl]) => chip(el, tx, cl));
    chips.forEach(([, ts]) => sfx(ts, 'pop', .6));
    return { rays, tp, cs };
  }, (lt, t, c) => {
    c.rays.style.transform = `rotate(${lt * 12}deg)`;
    const k = eBack(prog(lt, 0, .5));
    const y = B.top + (FMT === 'v' ? 40 : 30);
    c.tp.style.left = (FMT === 'v' ? 330 : 360) + 'px';
    c.tp.style.width = (FMT === 'v' ? 460 : 400) + 'px';
    c.tp.style.top = (y + lerp(700, 0, k) + Math.sin(lt * 2.4) * 8) + 'px';
    c.tp.style.transform = `rotate(${lerp(-18, -4, k)}deg)`;
    const pos = FMT === 'v' ? [[90, .04], [430, .80], [70, .92]] : [[80, .03], [520, .72], [60, .88]];
    c.cs.forEach((e, i) => {
      e.style.left = pos[i][0] + 'px';
      e.style.top = (B.top + pos[i][1] * (B.bot - B.top)) + 'px';
      chipUpdate(e, t, chips[i][1], i % 2 ? 80 : -80, 0);
    });
  }, { enter: 'up', flash: true, cap: 'verde' });
}

function ctaScene(t0, t1, tTap) {
  scene(t0, t1, 'verdebg', el => {
    const rays = mk('div', 'rays', null, el);
    const tp = mk('img', 'tapa', null, el); tp.src = TAPA;
    const bt = mk('div', 'boton', 'Comprar', el);
    const tq = tap(el);
    const fl = mk('div', 'flecha', null, el);
    sfx(tTap, 'tap', .9);
    return { rays, tp, bt, tq, fl };
  }, (lt, t, c) => {
    c.rays.style.transform = `rotate(${lt * 12}deg)`;
    c.tp.style.width = '360px';
    c.tp.style.left = '360px';
    c.tp.style.top = (B.top + 10) + 'px';
    c.tp.style.transform = `rotate(-4deg) scale(${lerp(1.2, 1, eOut(prog(lt, 0, .3)))})`;
    const by = B.top + (FMT === 'v' ? 600 : 610);
    c.bt.style.top = by + 'px';
    const pulse = 1 + .05 * Math.sin(lt * 9);
    const press = t > tTap && t < tTap + .15 ? .92 : 1;
    c.bt.style.transform = `translateX(-50%) scale(${pulse * press * lerp(.3, 1, pop(t, t0 + .05, .3))})`;
    c.tq.style.left = '540px'; c.tq.style.top = (by + 70) + 'px';
    tapUpdate(c.tq, t, tTap);
    c.fl.style.top = (by + 210 + Math.abs(Math.sin(lt * 6)) * 30) + 'px';
    c.fl.style.display = FMT === 'v' ? 'block' : 'none';
  }, { enter: 'zoom', flash: false, cap: 'verde' });
}

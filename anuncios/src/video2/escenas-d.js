// Video D «Sol»: persona IA. Sol (IMG-04) está de fondo todo el video; paleta ciruela y rosa,
// distinta de A. Narrador en tercera persona; etiqueta fija «Ejemplo del libro · no es una clienta».
'use strict';
const SOL = '../../../imagenes/IMG-04.png';
const SOL_PRE = '¡Hola! 💅 El semi está $14.000, kapping $17.000 y esculpidas $24.000. ¿Qué te gustaría hacerte?';
const AUS_A = '¡Hola, bella! 💅 Ahora no estoy atendiendo, mañana desde las 10 te respondo. Si querés turno, contame ';
const AUS_B = 'qué te querés hacer y qué días podés';
const AUS_C = ', así te lo guardo apenas pueda. ✨';

function armarD(words) {
  const w = (x, from = 0) => wt(words, x, from);
  const fin = words[words.length - 1][2] + 0.55;
  // fondo fijo: Sol desenfocada + velo ciruela + velo de noche
  const bg = document.getElementById('bg');
  const sb = mk('div', 'sol-bg', null, bg); sb.style.backgroundImage = `url(${SOL})`;
  mk('div', 'sol-ov', null, bg);
  const noche = mk('div', 'noche-ov', null, bg);
  mk('div', 'eti', 'Ejemplo del libro · no es una clienta');
  capSetup(words, 'claro');
  const C0 = FMT === 'v' ? 520 : 250; // arriba del contenido (debajo de etiqueta + subtítulos)
  const CH = B.bot - C0;

  const tSol2 = w('Sol', 1), tHace = w('hace', 3), tPrim = w('Primero'), tLa = w('La', 9), tY = w('Y', 11), tEs = w('Es', 16), tToca = w('Tocá');
  window.EXTRA = t => {
    sb.style.transform = `scale(${1 + t * .012}) translateY(${-t * 3}px)`;
    noche.style.opacity = t < tY - .1 ? 0 : t < tEs ? eOut(prog(t, tY - .1, tY + .3)) : 1 - eOut(prog(t, tEs, tEs + .3));
  };

  // 1 · retrato
  scene(0, tSol2, '', el => {
    const r = mk('div', 'ret', `<img src="${SOL}" alt="">`, el);
    const nm = chip(el, '💅 Sol', 'rosa');
    sfx(w('Sol'), 'pop', .7);
    return { r, nm };
  }, (lt, t, c) => {
    css(c.r, { top: C0 + 'px', height: (CH - 30) + 'px' });
    c.r.querySelector('img').style.transform = `scale(${1.25 - lt * .04})`;
    c.nm.style.left = '130px'; c.nm.style.top = (B.bot - 140) + 'px'; c.nm.style.fontSize = '46px';
    chipUpdate(c.nm, t, w('Sol'), -100, 0);
  }, { enter: 'none' });

  // 2 · quién es (ejemplo armado)
  scene(tSol2, tHace, '', el => {
    const r = mk('div', 'ret', `<img src="${SOL}" alt="">`, el);
    const t1 = chip(el, 'Ejemplo armado del libro', 'am');
    const t2 = chip(el, 'Uñas y pestañas · Rosario', 'rosa');
    sfx(w('ejemplo'), 'pop', .6);
    return { r, t1, t2 };
  }, (lt, t, c) => {
    const k = eOut(prog(lt, 0, .5));
    css(c.r, { top: (C0 + lerp(0, 30, k)) + 'px', height: (CH - lerp(30, 260, k)) + 'px', left: lerp(90, 170, k) + 'px', right: lerp(90, 170, k) + 'px' });
    c.r.querySelector('img').style.transform = `scale(${1.21 - lt * .03})`;
    css(c.t1, { left: '120px', top: (B.bot - 190) + 'px' });
    css(c.t2, { left: '260px', top: (B.bot - 100) + 'px' });
    chipUpdate(c.t1, t, w('ejemplo'), -120, 0);
    chipUpdate(c.t2, t, w('ejemplo') + .45, 120, 0);
  }, { enter: 'none' });

  // 3 · le preguntan todo el día (notificaciones)
  const NOT = [['Agus', '¿Tenés turno esta semana?'], ['Mica', '¿Precio del semi?'], ['Flor', '¿Cuánto dura el esculpido?'], ['Juli', '¿Hacés pestañas también?'], ['Cami', '¿Hay que dejar seña?']];
  scene(tHace, tPrim, '', el => {
    const ns = NOT.map(([n, p], i) => mk('div', 'noti', `<div class="ic">💬</div><div><h4>${n}</h4><p>${p}</p></div><small>ahora</small>`, el));
    const st = (tPrim - tHace) / (NOT.length + .5);
    ns.forEach((_, i) => sfx(tHace + i * st, 'pop', .7));
    return { ns, st };
  }, (lt, t, c) => {
    c.ns.forEach((n, i) => {
      const a = tHace + i * c.st;
      const k = eBack(prog(t, a, a + .3));
      const slot = C0 + (NOT.length - 1 - i) * (FMT === 'v' ? 168 : 168);
      const shown = t >= a;
      n.style.display = shown ? 'grid' : 'none';
      // cada nueva entra arriba y empuja las anteriores hacia abajo
      const nShown = c.ns.filter((_, j) => t >= tHace + j * c.st).length;
      const y = C0 + (nShown - 1 - i) * (FMT === 'v' ? 168 : 168);
      n.style.top = y + 'px';
      n.style.transform = `translateY(${lerp(-160, 0, k)}px) scale(${lerp(.85, 1, k)})`;
      n.style.opacity = clamp(k * 2);
    });
  }, { enter: 'zoom', flash: true });

  // 4 · la ficha
  const tPre = w('precios', tPrim), tSen = w('seña', tPrim), tHor = w('horarios', tPrim);
  scene(tPrim, tLa, '', el => {
    const f = mk('div', 'ficha', `<div class="fk">📌 LA FICHA DE SOL · DÍA 0</div>
      <div class="row"><i class="mk"></i><b>Precios</b>Semi $14.000 · Kapping $17.000<br>Esculpidas $24.000</div>
      <div class="row"><i class="mk"></i><b>Seña</b>$5.000 por transferencia</div>
      <div class="row"><i class="mk"></i><b>Horarios</b>Lunes a sábado, de 10 a 19</div>
      <div class="row"><i class="mk"></i><b>Cómo habla</b>De vos, cálida. Pocos emojis 💅✨</div>`, el);
    [tPre, tSen, tHor].forEach(x => sfx(x, 'tick', .8));
    return { f, rows: [...f.querySelectorAll('.row')] };
  }, (lt, t, c) => {
    c.f.style.top = C0 + 'px';
    c.f.style.transform = `rotate(${lerp(4, -1, eOut(prog(lt, 0, .5)))}deg)`;
    c.rows.forEach((r, i) => {
      const a = tPrim + .1 + i * .12;
      r.style.opacity = prog(t, a, a + .2);
      r.style.transform = `translateX(${lerp(-40, 0, eOut(prog(t, a, a + .3)))}px)`;
      const hm = [tPre, tSen, tHor, tHor + 10][i];
      r.querySelector('.mk').style.width = `calc(${eOut(prog(t, hm, hm + .35)) * 100}% + 28px)`;
      r.querySelector('.mk').style.opacity = t >= hm ? 1 : 0;
    });
  }, { enter: 'up', flash: true });

  // 5 · la IA le escribe las respuestas con su tono
  scene(tLa, tY, '', el => {
    const cc = mk('div', 'chatc', `<div class="hd"><img src="${SOL}" alt=""><div>Sol Nails &amp; Lashes<small>ejemplo del libro</small></div></div><div class="bd"></div>`, el);
    const bd = cc.querySelector('.bd');
    const q = bubble(bd, 'Hola! precio del semi?', '9:40', false, tLa + .1);
    const tag = mk('div', 'auto', '✨ Escrita con IA · la revisó Sol', bd);
    const r = bubble(bd, '<span class="tt"></span>', '9:41', true, tLa + .7);
    sfx(tLa + .1, 'pop', .7); sfx(tLa + .7, 'pop', .7); typeTicks(tLa + .75, tY - .4, 12);
    return { cc, q, tag, r };
  }, (lt, t, c) => {
    c.cc.style.top = C0 + 'px';
    bubbleUpdate(c.q, t); bubbleUpdate(c.r, t, 400);
    c.tag.style.opacity = prog(t, tLa + .45, tLa + .6);
    c.tag.style.transform = `scale(${lerp(.6, 1, pop(t, tLa + .45, .3))})`;
    c.r.b.querySelector('.tt').textContent = typed(SOL_PRE, t, tLa + .75, tY - .4) || '…';
  }, { enter: 'left', flash: true });

  // 6 · a la noche: mensaje de ausencia
  const tMen = w('mensaje', tY), tQue = w('qué', tY + 1);
  scene(tY, tEs, '', el => {
    const reloj = mk('div', 'reloj', '22:47', el);
    const luna = mk('div', 'luna', null, el);
    const cc = mk('div', 'chatc night', `<div class="hd"><img src="${SOL}" alt=""><div>Sol Nails &amp; Lashes<small>fuera de horario</small></div></div><div class="bd"></div>`, el);
    const bd = cc.querySelector('.bd');
    const q = bubble(bd, 'hola! tenés turno el jueves?', '22:47', false, tY + .35);
    const tag = mk('div', 'auto', '🌙 Mensaje de ausencia · se manda solo', bd);
    const r = bubble(bd, `${AUS_A}<span class="hl">${AUS_B}</span>${AUS_C}`, '22:47', true, tMen + .15);
    sfx(tY + .35, 'pop', .7); sfx(tMen + .15, 'ding', .6);
    return { reloj, luna, cc, q, tag, r };
  }, (lt, t, c) => {
    const yTop = FMT === 'v' ? C0 : C0 - 20;
    c.reloj.style.top = yTop + 'px';
    c.reloj.style.opacity = prog(lt, .05, .3);
    c.luna.style.top = (yTop + 6) + 'px';
    c.luna.style.transform = `rotate(${-20 + Math.sin(lt * 2) * 6}deg) scale(${lerp(.3, 1, pop(t, tY + .05, .4))})`;
    c.cc.style.top = (yTop + 150) + 'px';
    bubbleUpdate(c.q, t); bubbleUpdate(c.r, t, 600);
    c.tag.style.opacity = prog(t, tMen - .1, tMen + .05);
    c.r.b.querySelector('.hl').style.backgroundSize = `${eOut(prog(t, tQue, tQue + .7)) * 100}% 100%`;
    c.r.b.querySelector('.hl').style.color = t > tQue + .2 ? '#17201D' : '';
  }, { enter: 'zoom', flash: true });

  // 7 · el libro
  scene(tEs, tToca, '', el => {
    mk('div', 'sombra', null, el).style.opacity = .55;
    const tp = mk('img', 'tapa', null, el); tp.src = TAPA;
    const cs = [['DÍA 1', w('Día', tEs), 'am'], ['Respuestas + mensaje de ausencia', w('de', tEs + .4), 'rosa'], ['ChatGPT gratis', w('vendés', tEs), '']].map(([tx, ts, cl]) => { sfx(ts, 'pop', .6); return [chip(el, tx, cl), ts]; });
    return { tp, cs };
  }, (lt, t, c) => {
    const k = eBack(prog(lt, 0, .5));
    css(c.tp, { width: (FMT === 'v' ? 470 : 400) + 'px', left: (FMT === 'v' ? 305 : 340) + 'px', top: (C0 - 20 + lerp(600, 0, k) + Math.sin(lt * 2.4) * 8) + 'px', transform: `rotate(${lerp(14, 3, k)}deg)` });
    const pos = FMT === 'v' ? [[90, .70], [60, .82], [560, .93]] : [[70, .62], [40, .76], [600, .90]];
    c.cs.forEach(([e, ts], i) => {
      css(e, { left: pos[i][0] + 'px', top: (C0 + pos[i][1] * CH - 50) + 'px' });
      chipUpdate(e, t, ts, i % 2 ? 90 : -90, 0);
    });
  }, { enter: 'up', flash: true });

  // 8 · Comprar
  scene(tToca, fin + .01, '', el => {
    mk('div', 'sombra', null, el).style.opacity = .7;
    const tp = mk('img', 'tapa', null, el); tp.src = TAPA;
    const bt = mk('div', 'boton', 'Comprar', el);
    const tq = tap(el);
    const fl = mk('div', 'flecha', null, el);
    const tTap = w('Comprar', tToca);
    sfx(tTap, 'tap', .9);
    return { tp, bt, tq, fl, tTap };
  }, (lt, t, c) => {
    css(c.tp, { width: '340px', left: '370px', top: (C0 - 20) + 'px', transform: `rotate(3deg) scale(${lerp(1.2, 1, eOut(prog(lt, 0, .3)))})` });
    const by = C0 + (FMT === 'v' ? 520 : 560);
    c.bt.style.top = by + 'px';
    const press = t > c.tTap && t < c.tTap + .15 ? .92 : 1;
    c.bt.style.transform = `translateX(-50%) scale(${(1 + .05 * Math.sin(lt * 9)) * press * lerp(.3, 1, pop(t, tToca + .05, .3))})`;
    c.tq.style.left = '540px'; c.tq.style.top = (by + 70) + 'px';
    tapUpdate(c.tq, t, c.tTap);
    c.fl.style.top = (by + 210 + Math.abs(Math.sin(lt * 6)) * 30) + 'px';
    c.fl.style.display = FMT === 'v' ? 'block' : 'none';
  }, { enter: 'zoom' });
}

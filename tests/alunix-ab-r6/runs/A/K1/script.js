/* Alunix K1 Skymning. Kameran åker in i ett fönster.
   Allt som rör sig drivs av scrollpositionen och interpoleras mjukt i båda riktningarna. */
(function () {
  'use strict';

  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)');
  var html = document.documentElement;

  // En bild som inte kom fram första gången får ett andra försök.
  Array.prototype.forEach.call(document.images, function (img) {
    img.addEventListener('error', function retry() {
      img.removeEventListener('error', retry);
      var src = img.currentSrc || img.src;
      setTimeout(function () { img.src = src.split('?')[0] + '?r=1'; }, 500);
    });
  });

  var frame = document.getElementById('frame');
  var plate = document.getElementById('plate');
  var topbar = document.getElementById('topbar');

  // Plåten (skärmbilden) täcker ramen tills sajten laddat. Vi tonar plåten, aldrig ramen.
  function plateGone() { plate.classList.add('gone'); }
  frame.addEventListener('load', function () {
    try {
      var doc = frame.contentDocument;
      if (doc && doc.title) plateGone();
      else setTimeout(plateGone, 400);
    } catch (e) { plateGone(); }
  });
  setTimeout(function () { if (frame.contentDocument && frame.contentDocument.title) plateGone(); }, 3000);

  if (reduce.matches) {
    // Ingen resa. Allt står stilla, allt syns, i rätt ordning.
    watchTopbarStatic();
    return;
  }

  html.classList.add('motion');

  var hero = document.getElementById('hero');
  var stage = document.getElementById('stage');
  var cam = document.getElementById('cam');
  var dim = document.getElementById('dim');
  var copy = document.getElementById('copy');
  var win = document.getElementById('win');
  var proof = document.getElementById('proof');
  var caption = document.getElementById('caption');
  var glow = document.getElementById('glow');
  var thesisLines = document.querySelectorAll('#thesis .reveal-line, .thesis-row');
  var night = document.getElementById('night');
  var land = document.getElementById('kontakt');
  var white = document.getElementById('klarhet');
  var reveals = Array.prototype.slice.call(document.querySelectorAll('.reveal, .price-head.reveal-line'));

  // Fönstret i fotot, som andel av bildens bredd och höjd. Ramen är 16:9 kring den punkten.
  var WIN = { fx: 0.457, fy: 0.577, fw: 0.020 };
  var IMG_AR = 2200 / 1467;
  var S_END = 22;      // skala när fönstret börjar öppna sig
  var S_DEEP = 27;     // skala när ramen fyller skärmen
  var P_OPEN = 0.78;   // andel av resan där fönstret tar över

  var vw = 0, vh = 0, trackPx = 0, holdPx = 0, cutY = 0;
  var geo = null;

  function measure() {
    vw = window.innerWidth; vh = window.innerHeight;
    var cs = getComputedStyle(html);
    trackPx = parseVh(cs.getPropertyValue('--track'));
    holdPx = parseVh(cs.getPropertyValue('--hold'));
    // Klippet: när vita grunden nått toppen av fönstret, alltså när heron tar slut.
    cutY = hero.offsetTop + hero.offsetHeight - vh;

    // object-fit: cover
    var dw, dh, ox, oy;
    if (vw / vh > IMG_AR) { dw = vw; dh = vw / IMG_AR; ox = 0; oy = (vh - dh) / 2; }
    else { dh = vh; dw = vh * IMG_AR; oy = 0; ox = (vw - dw) / 2; }
    var px = ox + WIN.fx * dw, py = oy + WIN.fy * dh;
    var ww = WIN.fw * dw, wh = ww * 9 / 16;
    geo = { px: px, py: py, ww: ww, wh: wh };
    cam.style.transformOrigin = px.toFixed(2) + 'px ' + py.toFixed(2) + 'px';
  }
  function parseVh(v) {
    v = (v || '').trim();
    if (v.slice(-2) === 'vh') return parseFloat(v) / 100 * window.innerHeight;
    return parseFloat(v) || 0;
  }

  function clamp01(x) { return x < 0 ? 0 : x > 1 ? 1 : x; }
  function smooth(x) { x = clamp01(x); return x * x * (3 - 2 * x); }
  function lerp(a, b, t) { return a + (b - a) * t; }

  var startT = performance.now();
  var lastY = -1, lastPhase = '';
  var cut = false, thesisShown = false;

  function tick(now) {
    var y = window.scrollY || window.pageYOffset || 0;
    var p = trackPx > 0 ? y / trackPx : 1;
    var drifting = p < 0.06;
    if (y !== lastY || drifting) {
      lastY = y;
      render(y, p, now);
    }
    requestAnimationFrame(tick);
  }

  function render(y, p, now) {
    // ---- Akt 1 till 3: kameran ----
    var pc = clamp01(p);
    var t = (now - startT) / 1000;
    var drift = 1 + 0.018 * (1 - Math.cos(t * 2 * Math.PI / 38)) / 2 * (1 - smooth(p / 0.25)) ;
    var zoom = pc <= P_OPEN
      ? Math.pow(S_END, smooth(pc / P_OPEN))
      : S_END * Math.pow(S_DEEP / S_END, smooth((pc - P_OPEN) / (1 - P_OPEN)));
    var s = zoom * drift;
    var centre = smooth(pc / 0.7);
    var cx = vw / 2, cy = vh / 2;
    var tx = lerp(0, cx - geo.px, centre), ty = lerp(0, cy - geo.py, centre);
    cam.style.transform = 'translate(' + tx.toFixed(2) + 'px,' + ty.toFixed(2) + 'px) scale(' + s.toFixed(4) + ')';

    // Fönstrets rektangel på skärmen, i samma transform som fotot.
    var wx = geo.px + tx, wy = geo.py + ty;
    var rw, rh;
    // Fönstret tänds när kameran börjar röra sig: i stillhet är det fotots eget fönster som syns.
    var lit = smooth(pc / 0.08);
    if (pc <= P_OPEN) {
      rw = geo.ww * s * lit; rh = geo.wh * s * lit;
    } else {
      var q = smooth((pc - P_OPEN) / (1 - P_OPEN));
      var sA = S_END * drift;
      rw = lerp(geo.ww * sA, vw, q); rh = lerp(geo.wh * sA, vh, q);
      wx = lerp(wx, cx, q); wy = lerp(wy, cy, q);
    }
    var left = Math.max(0, wx - rw / 2), top = Math.max(0, wy - rh / 2);
    var right = Math.max(0, vw - (wx + rw / 2)), bottom = Math.max(0, vh - (wy + rh / 2));
    win.style.clipPath = 'inset(' + top.toFixed(1) + 'px ' + right.toFixed(1) + 'px ' + bottom.toFixed(1) + 'px ' + left.toFixed(1) + 'px)';

    // Fönsterljuset: varmt tills fönstret är ungefär en femtedel av skärmen, sedan syns rummet.
    glow.style.opacity = (0.86 * (1 - smooth((rw / vw - 0.10) / 0.16))).toFixed(3);

    // Mörkning utanför fönstret när det öppnar sig.
    dim.style.opacity = (0.75 * smooth((pc - P_OPEN) / (1 - P_OPEN))).toFixed(3);

    // Rubriken lämnar bilden genom att tona och blurra.
    var fade = smooth(pc / 0.3);
    copy.style.opacity = (1 - fade).toFixed(3);
    copy.style.filter = fade > 0.001 ? 'blur(' + (14 * fade).toFixed(2) + 'px)' : 'none';
    copy.style.visibility = fade >= 0.999 ? 'hidden' : 'visible';

    // Sajtnamnen står kvar längst ned tills fönstret tar över.
    var pf = 1 - smooth((pc - 0.6) / 0.14);
    proof.style.opacity = pf.toFixed(3);
    proof.style.visibility = pf <= 0.001 ? 'hidden' : 'visible';

    // Akt 3: ramen är hela skärmen och får användas.
    var live = pc >= 0.999;
    if (live !== win.classList.contains('live')) {
      win.classList.toggle('live', live);
      frame.classList.toggle('live', live);
      caption.classList.toggle('on', live);
      topbar.classList.toggle('overframe', live);
    }

    // ---- Klippet till vitt ----
    var nowCut = y >= cutY - 1;
    if (nowCut !== cut) {
      cut = nowCut;
      stage.classList.toggle('cut', cut);
      if (cut && !thesisShown) {
        thesisShown = true;
        Array.prototype.forEach.call(thesisLines, function (el) { el.classList.add('in'); });
      }
    }

    // ---- Avslöjanden på vitt ----
    for (var i = 0; i < reveals.length; i++) {
      var el = reveals[i];
      if (el.classList.contains('in')) continue;
      var r = el.getBoundingClientRect();
      if (cut && r.top < vh * 0.82 && r.bottom > 0) el.classList.add('in');
    }

    // ---- Landning: nattfotot glider långsammare än texten, tills sista skärmen står stilla ----
    var lr = land.getBoundingClientRect();
    var enter = clamp01(1 - lr.top / vh);   // 0 när landningen börjar synas, 1 när den fyller skärmen
    night.style.transform = 'translateY(' + ((1 - enter) * -0.12 * vh).toFixed(1) + 'px)';

    // ---- Toppbar ----
    if (cut && topbar.classList.contains('overframe')) topbar.classList.remove('overframe');
    else if (!cut && live && !topbar.classList.contains('overframe')) topbar.classList.add('overframe');
    var wantDark = cut && lr.top > 60;
    if (wantDark !== topbar.classList.contains('dark')) topbar.classList.toggle('dark', wantDark);
  }

  // Reserv: om något avslöjande inte hunnit fyra efter en stund men står i bild, visa det.
  setTimeout(function () {
    reveals.forEach(function (el) {
      var r = el.getBoundingClientRect();
      if (r.top < window.innerHeight && r.bottom > 0) el.classList.add('in');
    });
  }, 6000);

  measure();
  window.addEventListener('resize', function () { measure(); lastY = -1; });
  window.addEventListener('load', function () { measure(); lastY = -1; });
  requestAnimationFrame(tick);

  function watchTopbarStatic() {
    var whiteEl = document.getElementById('klarhet');
    var landEl = document.getElementById('kontakt');
    var winEl = document.getElementById('win');
    function upd() {
      var w = whiteEl.getBoundingClientRect(), l = landEl.getBoundingClientRect(), f = winEl.getBoundingClientRect();
      var dark = w.top <= 60 && l.top > 60;
      topbar.classList.toggle('dark', dark);
      topbar.classList.toggle('overframe', !dark && f.top <= 60 && f.bottom > 0);
    }
    window.addEventListener('scroll', upd, { passive: true });
    upd();
  }
})();

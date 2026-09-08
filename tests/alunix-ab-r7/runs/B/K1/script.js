/* Alunix K1 Skymning — runda 4. Hela signaturen (fönsterresa, ram, utgång)
   är EN pinnad akt (#signature); allt annat om fönstermasken/utgången är
   bespoke, driven av assets/push/window-track.json och --sc-p. Motorn
   (scrollcraft.js) rörs aldrig här; #signature använder ingen
   data-sc-sequence -- bildsekvensen laddas och ritas helt själv (se
   loadFrames/applySignature), så kartläggningen ruta<->p är vår, inte
   motorns dwell/scrub-formel. */
(function () {
  'use strict';

  var NATURAL_W = 1440, NATURAL_H = 960;
  var FRAME_COUNT = 100;
  var reduce = false; // motion always plays (F-011, 2026-09-07)

  function clamp01(x) { return x < 0 ? 0 : x > 1 ? 1 : x; }
  function smooth(x) { x = clamp01(x); return x * x * (3 - 2 * x); }

  function coverBox(boxW, boxH, natW, natH) {
    var scale = Math.max(boxW / natW, boxH / natH);
    var drawnW = natW * scale, drawnH = natH * scale;
    return { scale: scale, offX: (boxW - drawnW) / 2, offY: (boxH - drawnH) / 2 };
  }

  function frameBox(kf, boxW, boxH) {
    var c = coverBox(boxW, boxH, NATURAL_W, NATURAL_H);
    var px = c.offX + kf.x * NATURAL_W * c.scale;
    var py = c.offY + kf.y * NATURAL_H * c.scale;
    var pw = kf.w * NATURAL_W * c.scale;
    var ph = kf.h * NATURAL_H * c.scale;
    return { px: px, py: py, pw: pw, ph: ph, archH: kf.arch * ph };
  }

  function pathFor(box) {
    var pw = box.pw, ph = box.ph, a = box.archH;
    return 'path("M0,' + a.toFixed(1) + ' L0,' + ph.toFixed(1) + ' L' + pw.toFixed(1) + ',' + ph.toFixed(1) +
      ' L' + pw.toFixed(1) + ',' + a.toFixed(1) + ' A' + (pw / 2).toFixed(1) + ',' + a.toFixed(1) +
      ' 0 0 0 0,' + a.toFixed(1) + ' Z")';
  }

  function interpTrack(frame, keys) {
    if (frame <= keys[0].frame) return keys[0];
    if (frame >= keys[keys.length - 1].frame) return keys[keys.length - 1];
    for (var i = 0; i < keys.length - 1; i++) {
      var a = keys[i], b = keys[i + 1];
      if (frame >= a.frame && frame <= b.frame) {
        var t = (frame - a.frame) / (b.frame - a.frame);
        return {
          x: a.x + (b.x - a.x) * t, y: a.y + (b.y - a.y) * t,
          w: a.w + (b.w - a.w) * t, h: a.h + (b.h - a.h) * t,
          arch: a.arch + (b.arch - a.arch) * t
        };
      }
    }
    return keys[keys.length - 1];
  }

  // Bugg (runda 6, större fynd 7): materialets egna artefakter (banderoll,
  // skylt, lyktstolpe) sitter i rutorna ~38-62 ("gatunivån"). Mildrar utan
  // att dölja: den sträckan passerar nu på 60% av sin tidigare andel av
  // scrollen (snabbare förbi), och den friställda andelen (0,242*0,4=0,0968
  // av t1) läggs på resten av inzoomningen mot fönstret (långsammare, mer
  // avsiktlig). Brytpunkter i frame-fraktion (idx/99): gatunivån
  // motsvarar ungefär u=0,374 (ruta 38) till u=0,616 (ruta 62).
  function warpStreet(t) {
    var bx = [0, 0.374, 0.5192, 1];
    var by = [0, 0.374, 0.616, 1];
    for (var i = 0; i < bx.length - 1; i++) {
      if (t <= bx[i + 1] || i === bx.length - 2) {
        var seg = (t - bx[i]) / (bx[i + 1] - bx[i]);
        return by[i] + seg * (by[i + 1] - by[i]);
      }
    }
    return t;
  }

  function makeHoraiFrame(cls, title) {
    var f = document.createElement('iframe');
    f.className = cls;
    f.title = title;
    f.loading = 'eager';
    f.src = '/sites/horai.html';
    return f;
  }

  // Egen preload av de 100 rutorna (runda 4: aldrig motorns
  // data-sc-sequence/data-sc-scrub -- se filhuvudet).
  function loadFrames() {
    var frames = [], loaded = 0;
    for (var i = 0; i < FRAME_COUNT; i++) {
      (function (i) {
        var img = new Image();
        img.decoding = 'async';
        img.src = 'assets/push/f' + String(i + 1).padStart(3, '0') + '.webp';
        img.onload = function () { loaded++; };
        frames[i] = img;
      })(i);
    }
    return { frames: frames, get loaded() { return loaded; }, count: FRAME_COUNT };
  }

  // ---- toppbarens zon (papper/mörk): delad mellan motion- och
  // reservläget. Bugg (runda 6, a11y-fynd 10): renderStatic() registrerade
  // tidigare ingen zonväxling alls (bara startMotion() gjorde det), så vit
  // logga/länk låg kvar över ljusa sektioner i reduced motion (2,2-2,4:1).
  function initTopbarZones() {
    var topbar = document.getElementById('topbar');
    var zoneEls = document.querySelectorAll('[data-topbar-zone]');
    if (!topbar || !('IntersectionObserver' in window) || !zoneEls.length) return;
    var zoneIO = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (e.isIntersecting) {
          topbar.classList.toggle('zone-light', e.target.getAttribute('data-topbar-zone') === 'light');
        }
      });
    }, { rootMargin: '-1px 0px -99% 0px', threshold: 0 });
    zoneEls.forEach(function (el) { zoneIO.observe(el); });
  }

  // ---- reduced motion: render the one static formed frame, mount nothing ----
  function renderStatic(track) {
    var stage = document.getElementById('rm-window-stage');
    var photo = document.getElementById('rm-window-photo');
    var mask = document.getElementById('rm-window-mask');
    if (stage && photo && mask) {
      var apply = function () {
        var box = frameBox(track.keys[track.keys.length - 1], stage.clientWidth, stage.clientHeight);
        mask.style.left = box.px + 'px'; mask.style.top = box.py + 'px';
        mask.style.width = box.pw + 'px'; mask.style.height = box.ph + 'px';
        mask.style.clipPath = pathFor(box);
      };
      if (photo.complete) apply(); else photo.addEventListener('load', apply, { once: true });
      addEventListener('resize', apply, { passive: true });
    }
    // Bugg (runda 6, blockerande fynd 3): tidigare skapades en riktig,
    // scrollbar <iframe> här också -- mushjulet över den rörde bara ramens
    // EGNA scroll, aldrig sidan (sex hjultick: sidan 0px, ramen 1800px).
    // F-001 vill ha det formade läget, inte en levande ram; markupen är nu
    // en statisk skärmbild + länk (index.html), inget att skapa här.
    initTopbarZones();
  }

  // ---- akt 6 landning: egen progress, aldrig motorns --sc-p (fynd 2) ----
  // Flow-formeln (a.p = (y+vh-top)/(height+vh)) antar att sektionen kan
  // scrollas en HEL viewport förbi sin egen topp -- sant för en sektion med
  // mer innehåll under sig, falskt för sidans SISTA sektion, där sidan tar
  // slut innan dess. Räknar i stället mot den faktiskt nåbara scrollsträckan.
  function applyLanding() {
    var landing = document.getElementById('landing');
    if (!landing) return;
    var rect = landing.getBoundingClientRect();
    var top = rect.top + scrollY;
    var startY = top - innerHeight;
    var maxScroll = document.documentElement.scrollHeight - innerHeight;
    var p = clamp01((scrollY - startY) / Math.max(maxScroll - startY, 1));
    landing.style.setProperty('--landing-p', p.toFixed(4));
  }

  // ---- motion build. Tar inte längre `track` som parameter (fynd 13):
  // motion/rm-klassbytet ska aldrig vänta på ett nätverksanrop. Spåret
  // hämtas HÄRIFRÅN, asynkront, och fönstermasken väntar bara på DET --
  // canvasritning, ramen och toppbaren startar direkt. ----
  function startMotion() {
    var api = ScrollCraft.mount(document.body);

    var sigAct = null, ledgerAct = null;
    for (var i = 0; i < api.acts.length; i++) {
      var id = api.acts[i].el.id;
      if (id === 'signature') sigAct = api.acts[i];
      if (id === 'ledger') ledgerAct = api.acts[i];
    }
    if (!sigAct) return;

    var track = null;
    fetch('assets/push/window-track.json')
      .then(function (r) { return r.json(); })
      .then(function (t) { track = t; })
      .catch(function () { /* fönstermasken uteblir; basfotot läser ändå fint */ });

    var seq = loadFrames();

    var canvas = document.querySelector('.sig-canvas');
    var cctx = canvas && canvas.getContext('2d', { alpha: false });
    var photoLayer = document.getElementById('sig-photo-layer');
    var glow = document.querySelector('.window-glow');
    var fill = document.querySelector('.window-fill');
    var glassWrap = document.querySelector('.window-glass');
    var glassCanvas = document.querySelector('.window-glass__canvas');
    var gctx = glassCanvas && glassCanvas.getContext('2d');
    var vignette = document.getElementById('sig-vignette');
    var loadingIndicator = document.getElementById('loading-indicator');
    var topbarLabel = document.getElementById('topbar-label');
    var topbar = document.getElementById('topbar');
    var lastDrawnIdx = -1;
    var originSet = false;

    // Ramen skapas i JS, aldrig med src i statisk HTML: annars laddar den
    // även när #signature aldrig blir aktiv (två-iframes-felet, runda 3).
    var revealFrame = makeHoraiFrame('', 'Hōrai, exempelsajt');
    revealFrame.style.visibility = 'hidden';
    var frameSlot = document.getElementById('reveal-frame-slot');
    if (frameSlot) frameSlot.appendChild(revealFrame);

    function resizeCanvas() {
      if (!canvas) return;
      var box = canvas.getBoundingClientRect();
      var dpr = Math.min(devicePixelRatio || 1, 2);
      canvas.width = Math.round(box.width * dpr);
      canvas.height = Math.round(box.height * dpr);
      lastDrawnIdx = -1;
      originSet = false;
    }
    resizeCanvas();
    addEventListener('resize', resizeCanvas, { passive: true });

    function drawFrame(idx) {
      var img = seq.frames[idx];
      if (!img || !img.complete || !img.naturalWidth || !cctx) return false;
      var cw = canvas.width, ch = canvas.height;
      var scale = Math.max(cw / img.naturalWidth, ch / img.naturalHeight);
      var w = img.naturalWidth * scale, h = img.naturalHeight * scale;
      cctx.drawImage(img, (cw - w) / 2, (ch - h) / 2, w, h);
      return true;
    }

    function applySignature() {
      var p = sigAct.p;
      var stage = sigAct.stage;
      if (!stage) return;

      // ---- fas 1 (p 0-0.46): kameraresan, ritad själv ----
      // warpStreet: rutorna 38-62 (gatunivån) passerar på 60% av sin
      // tidigare scrollsträcka; den friställda sträckan går till en
      // långsammare, mer avsiktlig inzoomning mot fönstret (fynd 7).
      var t1raw = clamp01(p / 0.46);
      var t1 = warpStreet(t1raw);
      var idx = Math.min(FRAME_COUNT - 1, Math.max(0, Math.round(t1 * (FRAME_COUNT - 1))));
      var frame = idx + 1;
      // Bugg (runda 5): lastDrawnIdx sattes tidigare även när ritningen tyst
      // gav upp (bilden inte klar än via nätverket) -- vid p=0, direkt efter
      // sidladdning, hann f001.webp nästan aldrig ligga klar till första
      // rAF-anropet, så canvasen fastnade svart för alltid eftersom idx
      // aldrig ändrades igen utan scroll. Försöker nu om varje ruta tills
      // ritningen faktiskt lyckas.
      if (idx !== lastDrawnIdx) { if (drawFrame(idx)) lastDrawnIdx = idx; }

      // Fynd 7, mörkningen: mjuk vinjett i högra tredjedelen, bara under
      // gatunivåns rutor (34-66, med en mjuk ramp in/ut), topp 0,25.
      if (vignette) {
        var vigT = 0;
        if (frame >= 34 && frame <= 66) {
          vigT = smooth(Math.min((frame - 34) / 4, (66 - frame) / 4, 1));
        }
        vignette.style.opacity = (vigT * 0.25).toFixed(3);
      }

      // Fynd 13: en stillsam laddningsrad tills alla 100 rutor är hämtade.
      if (loadingIndicator) {
        loadingIndicator.style.opacity = seq.loaded < seq.count ? '1' : '0';
      }

      var boxW = stage.clientWidth, boxH = stage.clientHeight;
      // Fönstermasken väntar bara på window-track.json (fynd 13) -- ingen
      // annan del av akten gör det. Ovanligt sent spår läses som "ingen
      // mask än", samma som frame<58 nedan, aldrig ett fel.
      if (frame < 58 || !track) {
        glow.style.opacity = 0; fill.style.opacity = 0; glassWrap.style.opacity = 0;
      } else {
        var kf = interpTrack(frame, track.keys);
        var box = frameBox(kf, boxW, boxH);
        var path = pathFor(box);
        [glow, fill, glassWrap].forEach(function (el) {
          el.style.left = box.px + 'px'; el.style.top = box.py + 'px';
          el.style.width = box.pw + 'px'; el.style.height = box.ph + 'px';
          el.style.clipPath = path;
        });
        var fillT = smooth((frame - track.first_frame_with_horai) / 6);
        fill.style.opacity = fillT.toFixed(3);
        // Fynd 6: spröjsmaskens topp-opacitet sänkt (var 0,15-0,55, nu
        // 0,10-0,32) och en 1px-oskärpa i CSS -- lästes som ett moiré-mönster
        // vid ?preview=window i stället för en glasreflex.
        glassWrap.style.opacity = (0.10 + fillT * 0.22).toFixed(3);
        glow.style.opacity = (1 - fillT * 0.8).toFixed(3);

        if (frame >= track.first_frame_with_horai) {
          var sx = kf.x * NATURAL_W, sy = kf.y * NATURAL_H, sw = kf.w * NATURAL_W, sh = kf.h * NATURAL_H;
          var dpr = Math.min(devicePixelRatio || 1, 2);
          glassCanvas.width = Math.max(1, Math.round(box.pw * dpr));
          glassCanvas.height = Math.max(1, Math.round(box.ph * dpr));
          gctx.setTransform(dpr, 0, 0, dpr, 0, 0);
          var img100 = seq.frames[FRAME_COUNT - 1];
          var srcImg = seq.frames[idx] && seq.frames[idx].complete ? seq.frames[idx] : img100;
          if (srcImg && srcImg.complete) gctx.drawImage(srcImg, sx, sy, sw, sh, 0, 0, box.pw, box.ph);
        }

        // Transform-ursprung för fas "fortsatt zoom" (p 0.46-0.50): satt en
        // gång, mot fönstrets mittpunkt vid sista rutan.
        if (!originSet && frame === FRAME_COUNT) {
          var lastBox = frameBox(track.keys[track.keys.length - 1], boxW, boxH);
          var ox = ((lastBox.px + lastBox.pw / 2) / boxW * 100).toFixed(2) + '%';
          var oy = ((lastBox.py + lastBox.ph / 2) / boxH * 100).toFixed(2) + '%';
          photoLayer.style.setProperty('--sig-window-x', ox);
          photoLayer.style.setProperty('--sig-window-y', oy);
          originSet = true;
        }
      }

      // ---- ram synlig/klickbar bara p 0.50-0.72 (--xfade1 * (1-xfade2)) ----
      var xfade1 = clamp01((p - 0.50) / 0.02);
      var xfade2 = clamp01((p - 0.70) / 0.02);
      var frameVisible = xfade1 > 0 && xfade2 < 1;
      revealFrame.style.visibility = (sigAct.live && frameVisible) ? 'visible' : 'hidden';

      // ---- toppbar: mörk t.o.m. ramen, papper från utgångens mitt ----
      var dim = sigAct.live && p > 0.30 && p < 0.72;
      if (topbar) {
        topbar.classList.toggle('is-dim', !!dim);
        topbar.classList.toggle('zone-light', sigAct.live && p >= 0.86);
      }
      if (topbarLabel) {
        var vis = 0;
        if (p >= 0.54 && p <= 0.68) {
          var win = 0.68 - 0.54;
          var inEnd = 0.54 + win * 0.3, outStart = 0.68 - win * 0.3;
          if (p < inEnd) vis = smooth((p - 0.54) / (inEnd - 0.54));
          else if (p <= outStart) vis = 1;
          else vis = smooth(1 - (p - outStart) / (0.68 - outStart));
        }
        topbarLabel.style.opacity = sigAct.live ? vis.toFixed(3) : 0;
      }
    }

    function loop() {
      applySignature();
      applyLanding();
      requestAnimationFrame(loop);
    }
    requestAnimationFrame(loop);

    // ---- toppbarens zon för sektionerna EFTER signaturen ----
    initTopbarZones();

    // ---- ?preview= : force a formed state for screenshotting, no scroll ----
    var params = new URLSearchParams(location.search);
    var preview = params.get('preview');
    if (preview) {
      var targets = { window: 0.499, horai: 0.6, exit: 0.85, ledger: null };
      if (preview === 'ledger' && ledgerAct) {
        var yL = ledgerAct.top + ledgerAct.height * 0.85 - innerHeight * 0.4;
        scrollTo({ top: Math.max(0, yL), left: 0, behavior: 'instant' });
        api.read();
      } else if (Object.prototype.hasOwnProperty.call(targets, preview) && targets[preview] !== null) {
        var frac = targets[preview];
        var runPreview = function () {
          var y = sigAct.top + (sigAct.height - innerHeight) * frac;
          scrollTo({ top: Math.max(0, y), left: 0, behavior: 'instant' });
          api.read();
        };
        var waited = 0;
        (function waitForFrames() {
          if ((seq.loaded >= seq.count && track) || waited > 4000) { runPreview(); return; }
          waited += 60;
          setTimeout(waitForFrames, 60);
        })();
      }
    }
  }

  // Fynd 13: motion/rm-klassen sätts SYNKRONT, direkt vid skriptkörning --
  // aldrig efter ett fetch(window-track.json). Tidigare låg den bytet inne i
  // then()-kedjan, så sidan visade reservläget en extra stund (nätverks-
  // beroende) innan den bytte till rörelseläget, ett synligt hopp. Spåret
  // hämtas nu inuti startMotion()/renderStatic() själva, oberoende av vilket
  // läge som redan valts.
  document.documentElement.classList.toggle('motion', !reduce);
  if (reduce) {
    fetch('assets/push/window-track.json')
      .then(function (r) { return r.json(); })
      .then(renderStatic)
      .catch(function () { initTopbarZones(); });
  } else {
    startMotion();
  }
})();

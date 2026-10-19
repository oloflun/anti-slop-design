import { gsap, ScrollTrigger, SplitText, CustomEase } from "/gsap.js";
import lenis from "/smooth-scroll.js";

/* Riktning B "Banden". En skalär per akt driver all geometri (en ägare per egenskap):
   st.tileIn / st.intro (introt) och st.bleed (full bleed) skriver ramens clip-path via renderFrame,
   band.p skriver de sju grunderna och innehållet via renderBands, rise.f skriver bandets stegade kant,
   slut.p skriver slutbildens bricka. Allt som döljs vid start döljs här, aldrig i CSS. */

const $ = (s, r = document) => r.querySelector(s);
const $$ = (s, r = document) => [...r.querySelectorAll(s)];
const root = document.documentElement;
const tok = (n) => getComputedStyle(root).getPropertyValue(n).trim();
const c01 = (v) => Math.max(0, Math.min(1, v));
const lerp = (a, b, t) => a + (b - a) * t;
const io2 = (t) => (t < 0.5 ? 2 * t * t : 1 - Math.pow(-2 * t + 2, 2) / 2);
const PREVIEW = new URLSearchParams(location.search).get("preview");
const FINE = matchMedia("(hover: hover) and (pointer: fine)").matches;
CustomEase.create("house", ".16,1,.3,1");

/* ---------- innehåll som bara kan ordnas i DOM (texten själv är orörd) ---------- */
function fixContent() {
  $$(".pt[data-b]").forEach((p) => {
    const b = p.dataset.b, t = p.textContent;
    if (!t.startsWith(b)) return;
    const s = document.createElement("strong");
    s.textContent = b;
    p.textContent = "";
    p.append(s, t.slice(b.length));
  });
  const k = $(".om-koncern");
  if (k) {
    const lt = k.dataset.link, t = k.textContent, i = t.lastIndexOf(lt);
    if (i >= 0) {
      const a = document.createElement("a");
      a.href = k.dataset.href; a.target = "_blank"; a.rel = "noopener"; a.textContent = lt;
      k.textContent = t.slice(0, i);
      k.append(a);
    }
  }
  const v = $(".hero-video");
  if (v && matchMedia("(max-width: 768px)").matches && v.dataset.small) {
    v.src = v.dataset.small;
    v.play?.().catch(() => {});
  }
}

/* ---------- navens grund: tar sektionens/bandets färg ---------- */
const bar = $("#bar");
const BAND = [["--t-redovisning", 1], ["--t-hr", 0], ["--t-skatt", 1], ["--t-juridik", 1], ["--t-finans", 0], ["--t-grc", 1], ["--t-opex", 0], ["--lime", 0]];
const GROUND = { paper: ["--bakgrund", 0], lime: ["--lime", 0], ink: ["--ink", 1] };
let ground = "paper";
function setGround(key) {
  if (key === ground) return;
  ground = key;
  const [v, dark] = key.startsWith("band") ? BAND[+key.slice(4)] : GROUND[key];
  gsap.to(bar, { backgroundColor: tok(v), duration: 0.4, ease: "power2.out", overwrite: true });
  bar.classList.toggle("is-dark", !!dark);
}

/* ---------- hero: ram (= brickan) ---------- */
const hero = $(".hero");
const frame = $(".hero-frame");
const slot = $(".frame-slot");
const plate = $(".hero-plate");
const mosaic = $(".hero-mosaic");
const video = $(".hero-video");
const heroRun = $(".hero-run");
const st = { tileIn: 1, intro: 1, bleed: 0 };
const G = {};

function measureHero() {
  const fr = frame.getBoundingClientRect(), sr = slot.getBoundingClientRect();
  G.fw = fr.width; G.fh = fr.height; G.H = innerHeight; G.W = innerWidth;
  G.slot = { x: sr.left - fr.left, y: sr.top - fr.top, w: sr.width, h: sr.height };
  // introts bricka: mitt i den synliga delen av ramens yta
  const vTop = Math.max(fr.top, 0), vBot = Math.min(fr.bottom, innerHeight);
  const cx = innerWidth / 2, cy = (vTop + vBot) / 2;
  G.T = 64; G.gap = 10; G.cx = cx; G.cy = cy;
  G.tile = { x: cx + G.gap / 2 - fr.left, y: cy + G.gap / 2 - fr.top, w: G.T, h: G.T };
  // plattan glider upp ur vyn: sträckan räknas i layout, inte ur en transformerad rect
  const heroTopPinned = innerHeight - hero.offsetHeight; // pinnen startar "bottom bottom"
  G.plateOut = heroTopPinned + plate.offsetTop + plate.offsetHeight + 48;
}

function renderFrame() {
  const T = G.tile, S = G.slot;
  if (!T) return;
  const ti = st.tileIn;
  let w = T.w * ti, h = T.h * ti;
  let x = T.x + (T.w - w) / 2, y = T.y + (T.h - h) / 2, r = (T.w * 10 / 51) * ti;
  const e = st.intro;
  x = lerp(x, S.x, e); y = lerp(y, S.y, e); w = lerp(w, S.w, e); h = lerp(h, S.h, e); r = lerp(r, 10, e);
  const b = io2(c01(st.bleed / 0.55));
  x = lerp(x, 0, b); y = lerp(y, 0, b); w = lerp(w, G.fw, b); h = lerp(h, G.fh, b); r = lerp(r, 0, b);
  const R = Math.max(0, G.fw - x - w), B = Math.max(0, G.fh - y - h);
  frame.style.clipPath = `inset(${y.toFixed(2)}px ${R.toFixed(2)}px ${B.toFixed(2)}px ${x.toFixed(2)}px round ${r.toFixed(2)}px)`;
}

function renderBleed() {
  renderFrame();
  const p = st.bleed;
  const mo = io2(c01(p / 0.35));
  mosaic.style.transform = `translate3d(0, ${(-mo * G.H * 0.3).toFixed(2)}px, 0)`;
  mosaic.style.opacity = String(1 - mo);
  // plattan glider upp och ut i ett stycke (ingen mask, ingen toning): rubriken klipps aldrig
  const pp = io2(c01((p - 0.5) / 0.28));
  plate.style.transform = `translate3d(0, ${(-pp * G.plateOut).toFixed(2)}px, 0)`;
  plate.style.visibility = pp >= 1 ? "hidden" : "";
  const vs = c01((p - 0.55) / 0.45);
  video.style.objectViewBox = vs > 0 ? `inset(${(4 * vs).toFixed(3)}%)` : "";
  frame.style.willChange = p > 0 && p < 1 ? "clip-path" : "";
}

/* ---------- band 1 stiger med stegad kant ---------- */
const bands = $(".bands");
const STEPS = [1, 0, 2, 1, 0, 2, 1, 2, 0, 1, 2, 1];
const rise = { f: 1 };
const uPx = () => Math.max(20, Math.min(46, innerWidth * 0.032));
function renderRise() {
  if (rise.f <= 0.001) { bands.style.clipPath = ""; return; }
  const W = bands.clientWidth, u = uPx(), n = STEPS.length, cw = W / n;
  const pts = [];
  STEPS.forEach((s, i) => { const y = (s * u * rise.f).toFixed(1); pts.push(`${(i * cw).toFixed(1)}px ${y}px`, `${((i + 1) * cw).toFixed(1)}px ${y}px`); });
  pts.push("100% 100%", "0% 100%");
  bands.style.clipPath = `polygon(${pts.join(",")})`;
}

/* ---------- sju band: varje tjänsts 2x2 växer till bandets grund ---------- */
const grounds = $$(".bg-band");
const bodies = $$(".band-body");
const bandsHead = $(".bands-head");
// index 7 = limebandet, det åttonde utan tjänst: samma mekanik, och det lämnar över till kartläggningen
const LIGHT = [false, true, false, false, true, false, true, true];
const HOLD = 0.45, TRANS = 0.55;
const PH = [];
{ let a = 0; for (let k = 0; k < 7; k++) { PH.push({ t: "hold", k, a, len: HOLD }); a += HOLD; PH.push({ t: "trans", k, a, len: TRANS }); a += TRANS; } }
const TOTAL = PH.reduce((s, x) => s + x.len, 0); // 7 (= 700 vh)
const band = { p: 0, cur: 0, navActive: false };

function geom(W, H, q, g, h, solid) {
  // accentfältet: bredd Ax (samma mått som CSS --acc, textkolumnen håller sig till vänster om det),
  // höjd Ay <= 120 px så att nedre sömmen blir ett smalt band, inte en tom ruta
  const Ax = Math.min(H * 0.2, W * (W < 768 ? 0.13 : 0.18)) * (1 + 0.6 * h);
  const Ay = Math.min(H * 0.11, 100) * (1 + 0.2 * h);
  const s0 = Math.max(12, Math.min(44, H * 0.045, W * 0.05, Ay * 0.3)), g0 = s0 * 8 / 51, m = Math.max(10, Math.min(40, W * 0.03, Ay * 0.16));
  const t = s0 * q, tg = g0 * q;
  const x1s = W - m, y1s = H - m, x0s = x1s - 2 * t - tg, y0s = y1s - 2 * t - tg;
  const e = io2(g);
  // slutläget fyller vyn exakt: ytterhörnen blir raka mot vyns kant, innerhörnen behåller brickans radie
  const x0 = lerp(x0s, 0, e), y0 = lerp(y0s, 0, e), x1 = lerp(x1s, W, e), y1 = lerp(y1s, H, e);
  const sx = lerp(x0s + t + tg / 2, W - Ax - 4, e), sy = lerp(y0s + t + tg / 2, H - Ay - 4, e);
  const rs = t * 10 / 51;
  const gap = lerp(tg, solid ? 0 : 8, e), ri = lerp(rs, solid ? 0 : 10, e), ro = lerp(rs, 0, e);
  return { x0, y0, x1, y1, sx, sy, gap, ri, ro };
}
function box(n, x0, y0, x1, y1, tl, tr, br, bl) {
  n.style.transform = `translate3d(${x0.toFixed(1)}px, ${y0.toFixed(1)}px, 0)`;
  n.style.width = `${Math.max(0, x1 - x0).toFixed(1)}px`;
  n.style.height = `${Math.max(0, y1 - y0).toFixed(1)}px`;
  n.style.borderRadius = `${tl.toFixed(1)}px ${tr.toFixed(1)}px ${br.toFixed(1)}px ${bl.toFixed(1)}px`;
}
function placeGround(el, gm) {
  const [base, t1, t2, t3, t4] = el.children, hg = gm.gap / 2, o = gm.ro, i = gm.ri;
  box(base, gm.x0, gm.y0, gm.x1, gm.y1, o, o, o, o);
  box(t1, gm.x0, gm.y0, gm.sx - hg, gm.sy - hg, o, o, i, o);
  box(t2, gm.sx + hg, gm.y0, gm.x1, gm.sy - hg, o, o, o, i);
  box(t3, gm.x0, gm.sy + hg, gm.sx - hg, gm.y1, o, i, o, o);
  box(t4, gm.sx + hg, gm.sy + hg, gm.x1, gm.y1, i, o, o, o);
}

function phaseAt(p) {
  const s = p * TOTAL;
  let ph = PH[PH.length - 1];
  for (const x of PH) { if (s < x.a + x.len) { ph = x; break; } }
  return { ph, loc: c01((s - ph.a) / ph.len) };
}

function renderBands() {
  const W = bands.clientWidth, H = bands.clientHeight;
  const { ph, loc } = phaseAt(band.p);
  const k = ph.k;
  for (let j = 0; j < grounds.length; j++) {
    let q = 0, g = 0, h = 0, vis = false;
    if (j <= k) {
      q = 1; g = 1; h = ph.t === "hold" && j === k ? loc : 1;
      vis = j === k || (ph.t === "trans" && j === k);
    } else if (j === k + 1) {
      // under hållningen kommer nästa 2x2 in liten och börjar växa (håller vyn levande utan att flytta rubriken)
      if (ph.t === "hold") { q = c01((loc - 0.15) / 0.4); g = 0.25 * c01((loc - 0.55) / 0.45); vis = q > 0; }
      else { q = 1; g = 0.25 + 0.75 * loc; vis = true; }
    }
    const el = grounds[j];
    el.style.visibility = vis ? "visible" : "hidden";
    if (vis) placeGround(el, geom(W, H, q, g, h, j === 7));
  }
  bodies.forEach((b, j) => {
    let a = 0, y = 0;
    if (ph.t === "hold") a = j === k ? 1 : 0;
    else if (j === k) { const o = c01(loc / 0.3); a = 1 - o; y = -o * H * 0.08; }
    else if (j === k + 1) { const i = c01((loc - 0.8) / 0.2); a = i; y = (1 - i) * H * 0.08; }
    b.style.opacity = a.toFixed(3);
    b.style.transform = `translate3d(0, ${y.toFixed(1)}px, 0)`;
    b.style.pointerEvents = a > 0.5 ? "auto" : "none";
  });
  // när limen tar över har rubrikkolumnen gjort sitt: den tonar ut så att kartläggningen får vyn
  bandsHead.style.opacity = ph.t === "trans" && k === 6 ? (1 - c01((loc - 0.4) / 0.22)).toFixed(3) : "";
  const cur = ph.t === "hold" ? k : loc >= 0.75 ? k + 1 : k;
  band.cur = cur;
  bands.classList.toggle("on-light", LIGHT[cur]);
  if (band.navActive) setGround("band" + cur);
}

/* ---------- slut: sista bilden krymper till en bricka ---------- */
const slut = $(".slut");
const slutMedia = $(".slut-media");
const fslot = $(".f-slot");
const slutFade = $$(".f-top .logo, .f-contact, .f-cols, .f-bottom");
const sl = { p: 0 };
const SG = {};
function measureSlut() {
  const fr = slut.getBoundingClientRect(), br = fslot.getBoundingClientRect();
  SG.W = fr.width; SG.H = fr.height;
  SG.b = { x: br.left - fr.left, y: br.top - fr.top, s: br.width };
}
function renderSlut() {
  if (!SG.b) return;
  const e = io2(c01(sl.p / 0.75));
  const x = lerp(0, SG.b.x, e), y = lerp(0, SG.b.y, e);
  const w = lerp(SG.W, SG.b.s, e), h = lerp(SG.H, SG.b.s, e), r = lerp(0, 10, e); // landar med --radie
  slutMedia.style.transform = `translate3d(${x.toFixed(1)}px, ${y.toFixed(1)}px, 0)`;
  slutMedia.style.width = `${w.toFixed(1)}px`;
  slutMedia.style.height = `${h.toFixed(1)}px`;
  slutMedia.style.borderRadius = `${r.toFixed(1)}px`;
  const c = c01((sl.p - 0.6) / 0.2); // texten kommer först när bilden har lämnat textytorna
  slutFade.forEach((n) => { n.style.opacity = c.toFixed(3); });
}

/* ---------- meny: nedfällning i bandform + mobilmeny ---------- */
function initMenus() {
  const chev = $(".chev"), panel = $("#tj-panel"), li = $(".has-panel");
  const items = $$(".tp-item", panel);
  let closeT = 0;
  const open = () => {
    clearTimeout(closeT);
    if (chev.getAttribute("aria-expanded") === "true") return;
    panel.hidden = false;
    chev.setAttribute("aria-expanded", "true");
    // opacity, inte autoAlpha: panelen måste kunna ta fokus direkt (pil ned)
    gsap.fromTo(panel, { yPercent: -8, opacity: 0 }, { yPercent: 0, opacity: 1, duration: 0.38, ease: "power3.out", overwrite: true });
    gsap.fromTo(items, { y: -10, opacity: 0 }, { y: 0, opacity: 1, duration: 0.4, ease: "power3.out", stagger: 0.03, overwrite: true });
  };
  const close = (focusBtn) => {
    clearTimeout(closeT);
    if (chev.getAttribute("aria-expanded") !== "true") return;
    chev.setAttribute("aria-expanded", "false");
    gsap.to(panel, { opacity: 0, yPercent: -8, duration: 0.22, ease: "power2.in", overwrite: true,
      onComplete: () => { if (chev.getAttribute("aria-expanded") === "false") panel.hidden = true; } });
    if (focusBtn) chev.focus();
  };
  chev.addEventListener("click", () => (chev.getAttribute("aria-expanded") === "true" ? close() : open()));
  chev.addEventListener("keydown", (e) => {
    if (e.key === "ArrowDown") { e.preventDefault(); open(); items[0]?.focus(); }
  });
  panel.addEventListener("keydown", (e) => {
    const i = items.indexOf(document.activeElement);
    if (e.key === "Escape") { e.preventDefault(); close(true); }
    else if (e.key === "ArrowRight" || e.key === "ArrowDown") { e.preventDefault(); items[(i + 1) % items.length].focus(); }
    else if (e.key === "ArrowLeft" || e.key === "ArrowUp") { e.preventDefault(); items[(i - 1 + items.length) % items.length].focus(); }
    else if (e.key === "Home") { e.preventDefault(); items[0].focus(); }
    else if (e.key === "End") { e.preventDefault(); items[items.length - 1].focus(); }
  });
  document.addEventListener("keydown", (e) => { if (e.key === "Escape" && chev.getAttribute("aria-expanded") === "true") close(true); });
  document.addEventListener("pointerdown", (e) => { if (!panel.contains(e.target) && !li.contains(e.target)) close(); });
  const outOf = () => { setTimeout(() => { const a = document.activeElement; if (!panel.contains(a) && !li.contains(a)) close(); }, 0); };
  panel.addEventListener("focusout", outOf);
  chev.addEventListener("focusout", outOf);
  if (FINE) {
    const later = () => { clearTimeout(closeT); closeT = setTimeout(() => close(), 180); };
    li.addEventListener("mouseenter", open);
    li.addEventListener("mouseleave", later);
    panel.addEventListener("mouseenter", () => clearTimeout(closeT));
    panel.addEventListener("mouseleave", later);
  }

  const mbtn = $(".menu-btn"), mm = $("#mmenu"), mclose = $(".mm-close");
  const openM = () => {
    mm.hidden = false;
    mbtn.setAttribute("aria-expanded", "true");
    lenis.stop();
    gsap.fromTo(mm, { opacity: 0, yPercent: -2 }, { opacity: 1, yPercent: 0, duration: 0.35, ease: "power3.out", overwrite: true });
    gsap.fromTo($$(".mm-list li, .mm-links li", mm), { y: 14, opacity: 0 }, { y: 0, opacity: 1, duration: 0.5, ease: "house", stagger: 0.03, overwrite: true });
    mclose.focus();
  };
  const closeM = () => {
    if (mbtn.getAttribute("aria-expanded") !== "true") return;
    mbtn.setAttribute("aria-expanded", "false");
    lenis.start();
    gsap.to(mm, { opacity: 0, duration: 0.2, overwrite: true, onComplete: () => { if (mbtn.getAttribute("aria-expanded") === "false") mm.hidden = true; } });
    mbtn.focus();
  };
  document.addEventListener("keydown", (e) => { if (e.key === "Escape") closeM(); });
  mbtn.addEventListener("click", openM);
  mclose.addEventListener("click", closeM);
  mm.addEventListener("click", (e) => { if (e.target.closest("a")) closeM(); });
  mm.addEventListener("keydown", (e) => {
    if (e.key === "Escape") { e.preventDefault(); closeM(); return; }
    if (e.key !== "Tab") return;
    const f = $$("a[href], button", mm);
    if (e.shiftKey && document.activeElement === f[0]) { e.preventDefault(); f[f.length - 1].focus(); }
    else if (!e.shiftKey && document.activeElement === f[f.length - 1]) { e.preventDefault(); f[0].focus(); }
  });
}

/* ---------- pekare: magnet på "Se tjänsterna", bandets 2x2 följer 6 px ---------- */
function initPointer() {
  if (!FINE) return;
  const mag = $(".magnet");
  if (mag) {
    const qx = gsap.quickTo(mag, "x", { duration: 0.5, ease: "power3.out" });
    const qy = gsap.quickTo(mag, "y", { duration: 0.5, ease: "power3.out" });
    const zone = mag.parentElement;
    zone.addEventListener("pointermove", (e) => {
      const r = mag.getBoundingClientRect();
      const dx = e.clientX - (r.left + r.width / 2), dy = e.clientY - (r.top + r.height / 2);
      if (Math.hypot(dx, dy) > 140) { qx(0); qy(0); return; }
      qx(dx * 0.18); qy(dy * 0.25);
    });
    zone.addEventListener("pointerleave", () => { qx(0); qy(0); });
  }
  const marks = $$(".bm-wrap");
  const fx = gsap.quickTo(marks, "x", { duration: 0.8, ease: "power3.out" });
  const fy = gsap.quickTo(marks, "y", { duration: 0.8, ease: "power3.out" });
  bands.addEventListener("pointermove", (e) => {
    fx(((e.clientX / innerWidth) - 0.5) * 12);
    fy(((e.clientY / innerHeight) - 0.5) * 12);
  });
  bands.addEventListener("pointerleave", () => { fx(0); fy(0); });
}

/* ---------- reveals: en gång, göms aldrig igen ---------- */
function lineReveal(el, start = "top 82%") {
  SplitText.create(el, {
    type: "lines", mask: "lines", linesClass: "ln", autoSplit: true,
    onSplit(self) {
      return gsap.from(self.lines, { yPercent: 150, duration: 1.1, ease: "house", stagger: 0.08,
        scrollTrigger: { trigger: el, start, once: true } });
    },
  });
}
function fadeReveal(targets, trigger, start = "top 88%") {
  // opacity, inte autoAlpha: länkar behåller namn och fokus även innan de visats
  gsap.from(targets, { y: 14, opacity: 0, duration: 0.62, ease: "power2.out", stagger: 0.06,
    scrollTrigger: { trigger, start, once: true } });
}

/* ---------- introt: en bricka blir ramen ---------- */
let introTl = null, h1Tween = null, introRunning = false;
function playIntro(h1Split) {
  const navTiles = $$(".navmk > span");
  const reds = [0, 1, 2].map((i) => {
    const d = document.createElement("div");
    d.setAttribute("aria-hidden", "true");
    const x = i % 2 === 0 ? G.cx - G.gap / 2 - G.T : G.cx + G.gap / 2;
    const y = i < 2 ? G.cy - G.gap / 2 - G.T : G.cy + G.gap / 2;
    Object.assign(d.style, { position: "fixed", left: x + "px", top: y + "px", width: G.T + "px", height: G.T + "px",
      borderRadius: (G.T * 10 / 51) + "px", background: tok("--brand-rod"), zIndex: 200, pointerEvents: "none", transformOrigin: "0 0" });
    document.body.appendChild(d);
    return d;
  });
  const order = [0, 1, 2]; // TL, TR, BL -> navmärkets tre röda
  const kicker = $(".hero-kicker"), lead = $(".hero-lead"), ingress = $(".hero-ingress"), ctas = $(".hero-ctas");
  const bricks = $$(".hb", mosaic);

  introRunning = true;
  gsap.set(navTiles, { autoAlpha: 0 });
  gsap.set(bar, { opacity: 0 });
  gsap.set([kicker, lead, ingress, ctas], { opacity: 0, y: 14 });
  gsap.set(video, { autoAlpha: 0 });
  gsap.set(bricks, { autoAlpha: 0, scale: 0.3 });
  gsap.set(h1Split.lines, { yPercent: 150 });
  st.tileIn = 0; st.intro = 0; renderFrame();
  clearTimeout(window.__introGuard);
  ["#bar", ".hero-plate", ".hero-right"].forEach((s) => { $(s).style.opacity = ""; });

  const tl = gsap.timeline({ onComplete: endIntro });
  tl.from(reds, { autoAlpha: 0, scale: 0.4, y: 40, duration: 0.7, ease: "back.out(1.4)", stagger: 0.08 }, 0.15);
  tl.to(st, { tileIn: 1, duration: 0.7, ease: "back.out(1.4)", onUpdate: renderFrame }, 0.39);
  tl.to(st, { intro: 1, duration: 1.15, ease: "power3.inOut", onUpdate: renderFrame }, 1.05);
  tl.to(reds, {
    x: (i) => { const r = navTiles[order[i]].getBoundingClientRect(); return r.left - parseFloat(reds[i].style.left); },
    y: (i) => { const r = navTiles[order[i]].getBoundingClientRect(); return r.top - parseFloat(reds[i].style.top); },
    scale: () => navTiles[0].getBoundingClientRect().width / G.T,
    transformOrigin: "0 0",
    duration: 1.0, ease: "power3.inOut", stagger: 0.05,
  }, 1.05);
  tl.to(bar, { opacity: 1, duration: 0.6, ease: "power2.out" }, 1.3);
  tl.set(navTiles, { autoAlpha: 1 }, 2.15);
  tl.set(reds, { display: "none" }, 2.15);
  tl.set(navTiles[3], { autoAlpha: 0 }, 2.15);
  tl.to(navTiles[3], { autoAlpha: 1, duration: 0.3 }, 2.2);
  tl.to(kicker, { opacity: 1, y: 0, duration: 0.62, ease: "power2.out" }, 1.45);
  h1Tween = gsap.to(h1Split.lines, { yPercent: 0, duration: 1.1, ease: "house", stagger: 0.09 });
  tl.add(h1Tween, 1.55);
  tl.to([lead, ingress, ctas], { opacity: 1, y: 0, duration: 0.62, ease: "power2.out", stagger: 0.06 }, 2.0);
  tl.to(video, { autoAlpha: 1, duration: 0.9, ease: "power1.out" }, 1.85);
  tl.to(bricks, { autoAlpha: 1, scale: 1, duration: 0.6, ease: "back.out(1.56)", stagger: { each: 0.022, from: "random" } }, 2.0);
  introTl = tl;
  function endIntro() {
    introRunning = false;
    reds.forEach((d) => d.remove());
    gsap.set([kicker, lead, ingress, ctas, bricks], { clearProps: "transform,opacity,visibility" });
  }
}

/* ---------- ?preview= ---------- */
function previewY(name, T) {
  const H = innerHeight;
  if (name === "hero") return 0;
  if (name === "fullbleed") return T.bleed.start + (T.bleed.end - T.bleed.start) * 0.62;
  const m = /^band-(\d)$/.exec(name);
  if (m) {
    const k = Math.min(6, Math.max(0, +m[1] - 1));
    const hold = PH.find((x) => x.t === "hold" && x.k === k);
    const s = (hold.a + hold.len * 0.6) / TOTAL;
    return T.bands.start + (T.bands.end - T.bands.start) * s;
  }
  if (name === "flera") return T.bands.end;
  if (name === "kartlaggning") return Math.max(T.lime.start, T.bands.end + 2);
  if (name === "om") return T.lime.end;
  if (name === "insikter") return T.insG.start;
  if (name === "slut") return ScrollTrigger.maxScroll(window);
  return 0;
}

/* ---------- start ---------- */
async function init() {
  fixContent();
  initMenus();
  await document.fonts.ready;

  hero.classList.add("is-staged");
  bands.classList.add("is-staged");
  slut.classList.add("is-staged");

  ScrollTrigger.addEventListener("refreshInit", () => { heroRun.style.height = `${Math.round(innerHeight * 2.2)}px`; });
  heroRun.style.height = `${Math.round(innerHeight * 2.2)}px`;
  measureHero();
  renderBleed();

  // h1: radmasker (autoSplit). Vid ny delning efter introt står raderna stilla.
  let h1Split = null;
  SplitText.create("#hero-h", {
    type: "lines", mask: "lines", linesClass: "ln", autoSplit: true,
    onSplit(self) { h1Split = self; if (introRunning && h1Tween) { gsap.set(self.lines, { yPercent: 0 }); } },
  });

  const T = {};
  /* 1. hero står kvar (pin utan spacing) medan full bleed och bandets stigning spelar */
  T.heroPin = ScrollTrigger.create({ trigger: hero, start: "bottom bottom", endTrigger: bands, end: "top top", pin: true, pinSpacing: false });
  /* 2. full bleed: ramen växer till hela vyn (220 vh) */
  T.bleed = gsap.to(st, { bleed: 1, ease: "none", onUpdate: renderBleed,
    scrollTrigger: { trigger: heroRun, start: "top bottom", end: "bottom bottom", scrub: true, invalidateOnRefresh: true } }).scrollTrigger;
  /* 3. band 1 stiger med stegad kant över videon (100 vh) */
  T.rise = gsap.fromTo(rise, { f: 1 }, { f: 0, ease: "none", onUpdate: renderRise,
    scrollTrigger: { trigger: bands, start: "top bottom", end: "top top", scrub: true, invalidateOnRefresh: true } }).scrollTrigger;
  /* 4. sju band (700 vh) */
  T.bands = gsap.to(band, { p: 1, ease: "none", onUpdate: renderBands,
    scrollTrigger: { trigger: bands, start: "top top", end: () => "+=" + Math.round(innerHeight * 7), pin: true, scrub: true, invalidateOnRefresh: true } }).scrollTrigger;
  T.bandsG = ScrollTrigger.create({ trigger: bands, start: "top 64px", end: () => T.bands.end + innerHeight - 64,
    onToggle: (self) => { band.navActive = self.isActive; if (self.isActive) setGround("band" + band.cur); },
    onLeaveBack: () => setGround("paper") });

  /* 5. lime: limesektionen ligger 75 vh in över bandscenen (genomskinlig där); innehållet reser sig
        när lime-2x2:an täcker ~60 % av vyn (u = 0,66 i sista bandbytet), sedan står limen kvar medan arket läggs över */
  const lime = $(".lime");
  lime.classList.add("is-staged");
  const lph = PH[PH.length - 1];
  const limeAt = () => T.bands.start + (T.bands.end - T.bands.start) * ((lph.a + lph.len * 0.66) / TOTAL);
  fadeReveal($$(".flera, .kart .kicker"), lime, limeAt);
  lineReveal($(".kart h2"), limeAt);
  fadeReveal($$(".kart-text, .kart .btn"), lime, limeAt);
  T.limeG = ScrollTrigger.create({ trigger: lime, start: () => `top+=${Math.round(innerHeight * 0.75)} 64px`, endTrigger: ".om", end: "top 64px",
    onToggle: (self) => self.isActive && setGround("lime") });
  T.lime = gsap.to(".lime-in", { y: () => -innerHeight * 0.08, ease: "none",
    scrollTrigger: { trigger: lime, start: "bottom bottom", end: () => "+=" + Math.round(innerHeight), pin: true, pinSpacing: false, scrub: true, invalidateOnRefresh: true } }).scrollTrigger;

  /* 6. om: arket, rubrik i radmasker, texten tänds ord för ord i lästempo, ledger-rader */
  T.omG = ScrollTrigger.create({ trigger: ".om", start: "top 64px", endTrigger: ".slut", end: "top 64px",
    onToggle: (self) => self.isActive && setGround("paper") });
  lineReveal($(".om h2"), "top 80%");
  // aria:"none": ingen aria-label på <p> (aria-prohibited-attr); orden läses som vanlig text
  const words = SplitText.create(".om-text", { type: "words", aria: "none" }).words;
  gsap.fromTo(words, { color: tok("--grafit") }, { color: tok("--ink"), ease: "none", stagger: 0.1,
    scrollTrigger: { trigger: ".om-text", start: "top 82%", end: "bottom 46%", scrub: true } });
  fadeReveal($$(".om-koncern"), ".om-koncern");
  fadeReveal($$(".om-list li"), ".om-list", "top 85%");

  /* 7. insikter: ledger, flow+in */
  T.insG = ScrollTrigger.create({ trigger: ".ins", start: "top 64px", endTrigger: ".slut", end: "top 64px" });
  lineReveal($(".ins-head h2"), "top 85%");
  ScrollTrigger.batch(".ins-row", { start: "top 90%", once: true,
    onEnter: (els) => gsap.from(els, { y: 14, opacity: 0, duration: 0.62, ease: "power2.out", stagger: 0.08 }) });

  /* 8. slut: sista bilden krymper till en bricka bredvid logotypen (sista triggern) */
  ScrollTrigger.create({ trigger: slut, start: "top 64px", end: "bottom top", onToggle: (self) => self.isActive && setGround("ink"),
    onLeaveBack: () => setGround("paper") });
  T.slut = gsap.to(sl, { p: 1, ease: "none", onUpdate: renderSlut,
    scrollTrigger: { trigger: slut, start: "top bottom", end: "bottom bottom", scrub: true, invalidateOnRefresh: true } }).scrollTrigger;

  ScrollTrigger.addEventListener("refresh", () => {
    measureHero(); renderBleed(); renderRise(); renderBands(); measureSlut(); renderSlut();
  });

  // tangentbord: fokus på ett dolt bands länk hoppar till det bandet
  bodies.forEach((b, j) => b.addEventListener("focusin", () => {
    if (band.cur === j) return;
    const hold = PH.find((x) => x.t === "hold" && x.k === j);
    const y = T.bands.start + (T.bands.end - T.bands.start) * ((hold.a + hold.len * 0.6) / TOTAL);
    lenis.scrollTo(y, { immediate: true, force: true });
  }));

  initPointer();
  ScrollTrigger.refresh();
  measureHero(); measureSlut();
  renderBleed(); renderRise(); renderBands(); renderSlut();

  const atTop = window.scrollY < 5 && !PREVIEW;
  if (atTop && h1Split) {
    playIntro(h1Split);
    lenis.on("scroll", () => { if (introRunning && lenis.scroll > 8 && introTl) introTl.progress(1); });
  } else {
    clearTimeout(window.__introGuard);
    ["#bar", ".hero-plate", ".hero-right"].forEach((s) => { $(s).style.opacity = ""; });
  }

  if (PREVIEW) {
    const y = previewY(PREVIEW, T);
    lenis.resize();
    lenis.scrollTo(y, { immediate: true, force: true });
    ScrollTrigger.update();
  }
  window.__cell = { T, previewY: (n) => previewY(n, T), band, st, G };
}

init().catch((e) => {
  clearTimeout(window.__introGuard);
  ["#bar", ".hero-plate", ".hero-right"].forEach((s) => { const n = $(s); if (n) n.style.opacity = ""; });
  console.error(e);
});

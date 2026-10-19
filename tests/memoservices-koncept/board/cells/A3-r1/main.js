import { gsap, ScrollTrigger, SplitText, CustomEase } from "/gsap.js";
import lenis from "/smooth-scroll.js";

// A3 "Linsen II": one fixed layer of 28 bricks (#lager) that changes formation section by
// section. Positions come from slot elements in the layout, read on every refresh.
// Each transition is one scrubbed timeline of per-brick progress proxies (ease none); a single
// ticker turns progress + live slot rects into transforms. Lenis is the only smoothing.

void CustomEase;
const $ = (s, r = document) => r.querySelector(s);
const $$ = (s, r = document) => [...r.querySelectorAll(s)];
const html = document.documentElement;
const cs = getComputedStyle(html);
const rgb = (n) => { const h = cs.getPropertyValue("--" + n).trim().slice(1); return [0, 2, 4].map((i) => parseInt(h.slice(i, i + 2), 16)); };
const KEYS = ["redovisning", "hr", "skatt", "juridik", "finans", "grc", "opex"];
const MAIN = KEYS.map((k) => rgb("t-" + k)), ACC = KEYS.map((k) => rgb("a-" + k));
const INK = rgb("ink"), ROD = rgb("brand-rod"), LIME = rgb("lime");
const PREVIEW = new URLSearchParams(location.search).get("preview");
const FINE = matchMedia("(hover: hover) and (pointer: fine)").matches;
const lerp = (a, b, t) => a + (b - a) * t;

// ---------- text that the template can only give whole ----------
$$("[data-bar]").forEach((el) => {           // the carrying word of a heading in 500
  const words = el.textContent.trim().split(/\s+/), n = +el.dataset.bar;
  el.textContent = "";
  words.forEach((w, i) => {
    if (i) el.append(" ");
    if (i === n) { const b = document.createElement("b"); b.textContent = w; el.append(b); } else el.append(w);
  });
});
$$("[data-fet]").forEach((p) => {            // original <strong> on the start of each point
  const f = p.dataset.fet, t = p.textContent;
  if (!t.startsWith(f)) return;
  const s = document.createElement("strong"); s.textContent = f;
  p.textContent = t.slice(f.length); p.prepend(s);
});
$$("a[data-del]").forEach((a) => {          // link covers only "www.memoservices.no ↗"
  const d = a.dataset.del, t = a.textContent.trim();
  if (t.endsWith(d) && t !== d) { a.before(t.slice(0, -d.length)); a.textContent = d; }
});

// ---------- slots + the layer ----------
$$("[data-slots]").forEach((c) => { for (let i = 0; i < +c.dataset.slots; i++) c.append(document.createElement("span")); });
$$(".tar-over").forEach((e) => (e.style.visibility = "hidden")); // the layer takes over the real mosaics

const lager = $("#lager"), flytt = $(".flytt", lager);
const B = [];
for (let n = 0; n < 28; n++) {
  const el = document.createElement("div"), i = document.createElement("i");
  el.className = "b"; el.append(i); flytt.append(el);
  B.push({ n, g: n >> 2, r: n & 3, el, i, ph: n * 2.39996, pe: 6 + ((n * 7) % 31) / 10, c: {} });
}
const own = (b) => (b.r < 3 ? MAIN[b.g] : ACC[b.g]);

const hero = $("#hero"), band = $(".tj-head"), platta = $(".platta"), vid = $(".hero-video");
const heroSlots = $$(".hero-raster span"), kompSlots = $$(".kompass span"), tjRad = $$(".tj-rad .m2");
const kartSlot = $(".kart-kalla"), kartQ = [...kartSlot.children], omMk = $$(".om-ledger .mk"), omKol = $$(".om-kol span");
const insMk = $$(".ins-lista .mk"), insRad = $$(".ins-rad span"), ikon = $$(".fot-ikon i");
const insMark = (b) => (b.g === 0 && b.r === 0 ? 0 : b.g === 2 && b.r === 0 ? 1 : b.g === 3 && b.r === 3 ? 2 : -1);
let rest = 0; const insRest = B.map((b) => (insMark(b) < 0 ? rest++ : -1));

let litCol = 0, kartTl;
const lit = KEYS.map(() => 0);
const HC = 9, HR = 4;          // hero window raster: 9 x 4, the 28 bricks sit in columns 2-8
// F0..F6: hero windows · compass · seven 2x2 · one lime brick · om markers + column · insikter · app icon
const F = [
  { mode: "hero", slot: (b) => heroSlots[b.r * HC + b.g + 1], col: own, fill: 0, frame: 1, fw: 2, drift: 0 },
  { mode: "fixed", slot: (b) => kompSlots[b.r * 7 + b.g], col: own, fill: 1, frame: 0, drift: 1, alpha: (b) => (b.g === litCol ? 1 : 0.45) },
  { mode: "sticky", slot: (b) => tjRad[b.g].children[b.r], grp: (b) => tjRad[b.g], dg: true, col: own, fill: 1, frame: 0, drift: 1,
    alpha: (b) => 0.55 + 0.45 * lit[b.g], boost: (b) => 1 + 0.12 * lit[b.g] },
  // the gathered brick stays: a 2x2 of lime (1.5 px ink outline) + an ink accent, 7 bricks stacked per square
  { mode: "doc", slot: (b) => kartQ[b.r], col: (b) => (b.r < 3 ? LIME : INK), fill: 1, frame: (b) => (b.r < 3 ? 1 : 0), fw: 1.5, drift: 1, shared: true },
  { mode: "doc", slot: (b) => (b.g === 0 ? omMk[b.r] : omKol[(b.g - 1) * 4 + b.r]), col: (b) => (b.g === 0 ? (b.r < 3 ? ROD : LIME) : own(b)), fill: 1, frame: 0, drift: 1 },
  { mode: "doc", slot: (b) => (insMark(b) >= 0 ? insMk[insMark(b)] : insRad[insRest[b.n]]),
    col: (b) => [MAIN[0], MAIN[2], ACC[3]][insMark(b)] || own(b), fill: 1, frame: 0, drift: 1 },
  { mode: "doc", slot: (b) => ikon[b.r], col: (b) => (b.r < 3 ? ROD : LIME), fill: 1, frame: 0, drift: 1, shared: true },
];
const M = F.map(() => B.map(() => ({ x: 0, y: 0, s: 0, cx: 0, cy: 0 })));
let items = [], heroW = 0, heroH = 0, heroRects = [];

function measure() {
  const sy = scrollY, hr = hero.getBoundingClientRect(), br = band.getBoundingClientRect();
  heroW = hr.width; heroH = hr.height;
  F.forEach((f, fi) => B.forEach((b) => {
    const r = f.slot(b).getBoundingClientRect(), m = M[fi][b.n];
    const ox = f.mode === "hero" ? hr.left : f.mode === "sticky" ? br.left : 0;
    const oy = f.mode === "hero" ? hr.top : f.mode === "sticky" ? br.top : f.mode === "doc" ? -sy : 0;
    m.x = r.left - ox; m.y = r.top - oy; m.s = r.width;
    if (f.grp) { const g = f.grp(b).getBoundingClientRect(); m.cx = g.left + g.width / 2 - ox; m.cy = g.top + g.height / 2 - oy; }
  }));
  heroRects = heroSlots.map((sp) => { const r = sp.getBoundingClientRect(); return [r.left - hr.left, r.top - hr.top, r.width]; });
  items = $$(".tj-lista > li").map((li) => { const r = li.getBoundingClientRect(); return [r.top + sy, r.bottom + sy]; });
  coverDirty = true;
}

// The scrub needs a seekable video whatever the server does with Range requests: load it as a blob.
fetch(vid.getAttribute("src")).then((r) => r.blob()).then((bl) => { vid.src = URL.createObjectURL(bl); vid.load(); }).catch(() => { vid.preload = "auto"; });

// ---------- cover: ink with 28 windows onto the video ----------
const NS = "http://www.w3.org/2000/svg";
const tacke = document.createElementNS(NS, "svg");
tacke.setAttribute("class", "tacke"); tacke.setAttribute("aria-hidden", "true");
const taPath = document.createElementNS(NS, "path");
taPath.setAttribute("fill", "currentColor"); taPath.setAttribute("fill-rule", "evenodd");
tacke.append(taPath); vid.after(tacke);
const H = { t: 0 };                       // windows grow together (one value for all: holes never overlap)
const IK = Array.from({ length: HC * HR }, () => ({ k: 0 }));   // intro: each window opens
let coverDirty = true, coverKey = "";
const rr = (x, y, w, h, r) => `M${x + r} ${y}H${x + w - r}A${r} ${r} 0 0 1 ${x + w} ${y + r}V${y + h - r}A${r} ${r} 0 0 1 ${x + w - r} ${y + h}H${x + r}A${r} ${r} 0 0 1 ${x} ${y + h - r}V${y + r}A${r} ${r} 0 0 1 ${x + r} ${y}Z`;
function drawCover() {
  const key = H.t.toFixed(4) + IK.map((o) => o.k.toFixed(3)).join("");
  if (!coverDirty && key === coverKey) return;
  coverDirty = false; coverKey = key;
  if (H.t >= 1) { tacke.style.display = "none"; return; }
  tacke.style.display = "";
  tacke.setAttribute("viewBox", `0 0 ${heroW} ${heroH}`);
  const cw = heroW / HC, ch = heroH / HR;
  let d = `M0 0H${heroW}V${heroH}H0Z`;
  heroRects.forEach(([mx, my, ms], i) => {
    const k = IK[i].k, s0 = ms * k, c = i % HC, rw = (i / HC) | 0;
    const x0 = mx + (ms - s0) / 2, y0 = my + (ms - s0) / 2;
    const x = lerp(x0, c * cw, H.t), y = lerp(y0, rw * ch, H.t), w = lerp(s0, cw, H.t), h = lerp(s0, ch, H.t);
    const r = Math.min(w, h) / 2 * lerp(0.392, 0, H.t);
    if (w > 0.5 && h > 0.5) d += rr(+x.toFixed(2), +y.toFixed(2), +w.toFixed(2), +h.toFixed(2), +r.toFixed(2));
  });
  taPath.setAttribute("d", d);
}

// ---------- the transitions ----------
const D = 0.35;
const P = [0, 1, 2, 3, 4, 5].map(() => B.map(() => ({ t: 0 })));
const order = [
  (b) => b.r / 3,                                          // windows -> compass, row by row
  (b) => b.r / 3,                                          // compass -> seven 2x2, row by row
  (b) => b.g / 6,                                          // seven 2x2 -> one brick, colour by colour
  (b) => (b.g === 0 ? 1 : ((b.g - 1) * 4 + b.r) / 24),     // split: the column top-down, the markers last (their rows are revealed by then)
  (b) => (insMark(b) >= 0 ? 1 : insRest[b.n] / 25),       // the row left to right, the markers last
  (b) => b.g / 6,                                          // into the icon, service by service
];
function addMoves(tl, k, at = 0, span = 1) {
  B.forEach((b) => tl.to(P[k][b.n], { t: 1, ease: "none", duration: (1 - D) * span }, at + order[k](b) * D * span));
}

let pinP = 0;
const pinST = { trigger: hero, pin: true, scrub: true, invalidateOnRefresh: true,
  start: () => (hero.offsetHeight > innerHeight + 1 ? "bottom bottom" : "top top"),
  end: () => "+=" + Math.round(innerHeight * 2.6) };
const pinTl = gsap.timeline({ scrollTrigger: pinST });
pinTl.to(H, { t: 1, ease: "none", duration: 0.3 }, 0);
addMoves(pinTl, 0, 0, 0.3);
// the plate pans out of the frame (never fades over the video) and leaves the facade alone
pinTl.to(platta, { y: () => -(Math.min(0, innerHeight - hero.offsetHeight) + platta.offsetTop + platta.offsetHeight + 40), ease: "none", duration: 0.3 }, 0.55);
pinTl.set({}, {}, 1);

// every layer transition is done when the next section's top stands at 45 % of the view
const section = (sel, k, end = "top 45%", extra) => {
  const tl = gsap.timeline({ scrollTrigger: { trigger: sel, start: "top bottom", end, scrub: true, invalidateOnRefresh: true } });
  if (extra) extra(tl); else addMoves(tl, k);
  tl.set({}, {}, 1);
  return tl;
};
section("#tjanster", 1);
const panel = $(".kart-panel"), kart = $("#kartlaggning");
const panelFrom = () => {
  const s = kartSlot.getBoundingClientRect(), k = kart.getBoundingClientRect();
  return `inset(${s.top - k.top}px ${k.right - s.right}px ${k.bottom - s.bottom}px ${s.left - k.left}px round ${(s.width * 10) / 51}px)`;
};
gsap.set(panel, { autoAlpha: 0 });
kartTl = section("#kartlaggning", 2, "top 45%", (tl) => {
  addMoves(tl, 2, 0, 0.6);
  tl.set(panel, { autoAlpha: 1 }, 0.55);
  tl.fromTo(panel, { clipPath: panelFrom }, { clipPath: "inset(0px 0px 0px 0px round 0px)", ease: "none", duration: 0.45 }, 0.55);
});
ScrollTrigger.create({ trigger: kart, start: "top 44px", endTrigger: "#slut", end: "top 44px", toggleClass: { targets: ".nav", className: "ljus" } });
section("#om", 3);
section("#insikter", 4);

// shared reveal: 14 px, 620 ms, once
const reveal = $$("[data-r]"), ledger = $$(".om-ledger [data-r], .ins-lista [data-r]");
gsap.set(reveal, { autoAlpha: 0, y: 14 });
const rev = (start) => ({ start, once: true,
  onEnter: (els) => gsap.to(els, { autoAlpha: 1, y: 0, duration: 0.62, ease: "power2.out", stagger: 0.06, overwrite: true }) });
ScrollTrigger.batch(reveal.filter((e) => !ledger.includes(e)), rev("top 88%"));
ScrollTrigger.batch(ledger, rev("top 92%"));   // ledger rows are there before their marker lands

section("#slut", 5, "clamp(top 45%)");   // last trigger on the page: 45 %, clamped to the page end

// ---------- intro: the windows open, the heading rises ----------
const h1 = $(".platta h1");
gsap.set(h1, { autoAlpha: 0 });
const intro = gsap.timeline();
IK.forEach((o, i) => intro.to(o, { k: 1, duration: 0.8, ease: "power3.out" }, 0.1 + ((i / HC) | 0) * 0.1 + (i % HC) * 0.03));
intro.from($$("[data-ri]"), { autoAlpha: 0, y: 14, duration: 0.62, ease: "power2.out", stagger: 0.06 }, 0.55);

const markSplit = (self) => self.masks.forEach((m) => m.parentElement.classList.add("split"));
document.fonts.ready.then(() => {
  SplitText.create(".platta .rad", { type: "lines", mask: "lines", autoSplit: true, aria: "none", linesClass: "ln",
    onSplit(self) {
      markSplit(self);
      gsap.set(h1, { autoAlpha: 1 });
      const tw = gsap.from(self.lines, { yPercent: 120, duration: 1.1, ease: "expo.out", stagger: 0.08, delay: PREVIEW ? 0 : 0.25 });
      if (PREVIEW) tw.progress(1);
      return tw;
    } });
  $$("h2.h-disp").forEach((el) => {
    const rads = $$(".rad", el);
    SplitText.create(rads.length ? rads : el, { type: "lines", mask: "lines", autoSplit: true, aria: "none", linesClass: "ln",
      onSplit: (self) => { markSplit(self); return gsap.from(self.lines, { yPercent: 120, duration: 1, ease: "expo.out", stagger: 0.08,
        scrollTrigger: { trigger: el, start: "top 86%", once: true } }); } });
  });
  ScrollTrigger.refresh();
  if (PREVIEW) jump();
});
ScrollTrigger.addEventListener("refresh", measure);
addEventListener("load", () => ScrollTrigger.refresh());

// ---------- pointer: the layer leans 0.6 % toward the pointer ----------
if (FINE) {
  const qx = gsap.quickTo(flytt, "x", { duration: 0.9, ease: "power3" }), qy = gsap.quickTo(flytt, "y", { duration: 0.9, ease: "power3" });
  addEventListener("pointermove", (e) => { qx((e.clientX / innerWidth - 0.5) * 2 * 0.006 * innerWidth); qy((e.clientY / innerHeight - 0.5) * 2 * 0.006 * innerHeight); }, { passive: true });
}

// ---------- the ticker: progress + live rects -> transforms ----------
let lastSeek = 0, moving = false, lastAct = -2, last = performance.now();
const posOf = (fi, b, hr, br, sy) => {
  const f = F[fi], m = M[fi][b.n];
  let x = m.x, y = m.y, s = m.s;
  if (f.mode === "hero") { x += hr.left; y += hr.top; const k = IK[b.r * HC + b.g + 1].k; x += (s * (1 - k)) / 2; y += (s * (1 - k)) / 2; s *= k; }
  else if (f.mode === "sticky") { x += br.left; y += br.top; }
  else if (f.mode === "doc") y -= sy;
  if (f.boost) {
    const k = f.boost(b), cx = m.cx + (f.mode === "sticky" ? br.left : 0), cy = m.cy + (f.mode === "sticky" ? br.top : 0);
    x = cx + (x - cx) * k; y = cy + (y - cy) * k; s *= k;
  }
  return [x, y, s, f.alpha ? f.alpha(b) : 1];
};
const items$ = $$(".tj-lista > li");

function tick() {
  const now = performance.now(), dt = Math.min(0.1, (now - last) / 1000); last = now;
  const sy = scrollY, vh = innerHeight, sec = now / 1000;
  const hr = hero.getBoundingClientRect(), br = band.getBoundingClientRect();
  pinP = pinTl.scrollTrigger.progress;

  // the service text passing 60 % of the view lights its 2x2; index 7 = "flera områden" lights all seven
  const line = sy + vh * 0.6;
  let act = -1;
  items.forEach(([a, z], i) => { if (line >= a && line < z) act = i; });
  if (act !== lastAct) { items$.forEach((li, i) => li.classList.toggle("on", i === act)); lastAct = act; }
  const ease = 1 - Math.exp(-dt / 0.14);
  KEYS.forEach((_, g) => { lit[g] += ((act === 7 || act === g ? 1 : 0) - lit[g]) * ease; });
  litCol = pinP < 0.65 ? 0 : 1;

  // video follows the pin
  if (vid.duration && !vid.seeking) {
    const tgt = pinP * (vid.duration - 0.05);
    // ponytail: at most one seek per 50 ms (20 video frames/s while scrolling fast); every rAF doubled the dropped frames
    if (Math.abs(vid.currentTime - tgt) > 0.03 && now - lastSeek >= 50) { vid.currentTime = tgt; lastSeek = now; }
  }

  drawCover();

  // bricks pass under the plate: a brick fades by how much of it the plate covers
  // (a clip-path on the whole layer cost a full-screen mask per frame: p95 33 ms -> 17 ms without it)
  const pl = pinP < 0.55 && hr.bottom > 0 ? platta.getBoundingClientRect() : null;

  let any = false;
  for (const b of B) {
    let k = -1;
    for (let j = P.length - 1; j >= 0; j--) if (P[j][b.n].t > 0) { k = j; break; }
    const fa = k < 0 ? 0 : k, t = k < 0 ? 0 : P[k][b.n].t;
    if (t > 0 && t < 1) any = true;
    const A = posOf(fa, b, hr, br, sy), Z = t > 0 ? posOf(fa + 1, b, hr, br, sy) : A;
    const fA = F[fa], fZ = t > 0 ? F[fa + 1] : fA;
    const x = lerp(A[0], Z[0], t), y = lerp(A[1], Z[1], t), s = Math.max(0.01, lerp(A[2], Z[2], t)), al = lerp(A[3], Z[3], t);
    const sc = s / 100;
    const tr = `translate3d(${x.toFixed(2)}px,${y.toFixed(2)}px,0) scale(${sc.toFixed(4)})`;
    if (tr !== b.c.tr) { b.el.style.transform = tr; b.c.tr = tr; }
    let cover = 0;
    if (pl) {
      const ox = Math.min(x + s, pl.right) - Math.max(x, pl.left), oy = Math.min(y + s, pl.bottom) - Math.max(y, pl.top);
      if (ox > 0 && oy > 0) cover = (ox * oy) / (s * s);
    }
    const op = (al * (1 - cover)).toFixed(3);
    if (op !== b.c.op) { b.el.style.opacity = op; b.c.op = op; }
    const fr = (f) => (typeof f.frame === "function" ? f.frame(b) : f.frame);
    const cA = fA.col(b), cZ = fZ.col(b), fill = lerp(fA.fill, fZ.fill, t), frame = lerp(fr(fA), fr(fZ), t);
    const fw = fr(fA) && fr(fZ) ? lerp(fA.fw, fZ.fw, t) : fr(fA) ? fA.fw : fZ.fw || 2;
    const bg = `rgba(${lerp(cA[0], cZ[0], t) | 0},${lerp(cA[1], cZ[1], t) | 0},${lerp(cA[2], cZ[2], t) | 0},${fill.toFixed(3)})`;
    if (bg !== b.c.bg) { b.i.style.backgroundColor = bg; b.c.bg = bg; }
    const sh = frame > 0.002 ? `inset 0 0 0 ${(fw / sc).toFixed(2)}px rgba(${INK[0]},${INK[1]},${INK[2]},${frame.toFixed(3)})` : "none";
    if (sh !== b.c.sh) { b.i.style.boxShadow = sh; b.c.sh = sh; }
    // rest drift: ±4 px, 6–9 s, its own phase (a stack drifts as one)
    const amp = (Math.min(4, s * 0.08) * lerp(fA.drift, fZ.drift, t)) / sc;
    const sharedNow = t < 0.5 ? fA.shared : fZ.shared;
    const grpNow = t < 0.5 ? fA.dg : fZ.dg;   // a 2x2 drifts as one piece
    const ph = sharedNow ? 0 : grpNow ? b.g * 2.39996 : b.ph, pe = sharedNow ? 7.5 : grpNow ? 6 + b.g * 0.45 : b.pe;
    const dx = (amp * Math.sin((sec / pe) * 6.2832 + ph)).toFixed(2) + "px", dy = (amp * Math.cos((sec / (pe * 1.13)) * 6.2832 + ph)).toFixed(2) + "px";
    if (dx !== b.c.dx) { b.i.style.setProperty("--dx", dx); b.c.dx = dx; }
    if (dy !== b.c.dy) { b.i.style.setProperty("--dy", dy); b.c.dy = dy; }
  }
  any = any || intro.isActive();
  if (any !== moving) { lager.classList.toggle("rorlig", any); moving = any; }
}
measure();
gsap.ticker.add(tick);

// ---------- ?preview=<act> ----------
function jump() {
  intro.progress(1);
  ScrollTrigger.refresh();
  const st = pinTl.scrollTrigger, top = (sel) => $(sel).getBoundingClientRect().top + scrollY;
  const first = items[0] || [0, 0];
  const y = {
    hero: 0,
    fasad: st.start + (st.end - st.start) * 0.9,
    tjanster: Math.max((first[0] + first[1]) / 2 - innerHeight * 0.6, top("#tjanster") - innerHeight * 0.45),
    kartlaggning: top("#kartlaggning"),
    om: top("#om"),
    insikter: top("#insikter"),
    slut: ScrollTrigger.maxScroll(window),
  }[PREVIEW];
  if (y === undefined) return;
  lenis.resize();   // the pin spacer was added after Lenis measured: without this, "slut" clamps to an old limit
  lenis.scrollTo(y, { immediate: true, force: true });
  ScrollTrigger.update();
}

// ---------- nav: "Tjänster" opens the centred brick downward ----------
const tgl = $(".under-knapp"), under = $("#under"), mitt = $(".nav-mitt");
const isOpen = () => tgl.getAttribute("aria-expanded") === "true";
function setUnder(open) {
  if (open === isOpen()) return;
  tgl.setAttribute("aria-expanded", String(open));
  if (open) { under.hidden = false; gsap.fromTo(under, { height: 0 }, { height: "auto", duration: 0.45, ease: "power3.out", overwrite: true }); }
  else gsap.to(under, { height: 0, duration: 0.3, ease: "power2.in", overwrite: true, onComplete: () => { if (!isOpen()) under.hidden = true; } });
}
tgl.addEventListener("click", () => setUnder(!isOpen()));
// the panel sits after the link row in the DOM: walk the keyboard into it and back out
const uLinks = $$("a", under), nextLink = $(".nav-lista > li:nth-child(2) a");
tgl.addEventListener("keydown", (e) => { if (e.key === "Tab" && !e.shiftKey && isOpen()) { e.preventDefault(); uLinks[0].focus(); } });
uLinks[0].addEventListener("keydown", (e) => { if (e.key === "Tab" && e.shiftKey) { e.preventDefault(); tgl.focus(); } });
uLinks[uLinks.length - 1].addEventListener("keydown", (e) => { if (e.key === "Tab" && !e.shiftKey) { e.preventDefault(); nextLink.focus(); } });
nextLink.addEventListener("keydown", (e) => { if (e.key === "Tab" && e.shiftKey && isOpen()) { e.preventDefault(); uLinks[uLinks.length - 1].focus(); } });
mitt.addEventListener("keydown", (e) => { if (e.key === "Escape" && isOpen()) { setUnder(false); tgl.focus(); } });
mitt.addEventListener("focusout", (e) => { if (!mitt.contains(e.relatedTarget)) setUnder(false); });
if (FINE) {
  let tid;
  $(".har-under").addEventListener("pointerenter", () => { clearTimeout(tid); setUnder(true); });
  mitt.addEventListener("pointerenter", () => clearTimeout(tid));
  mitt.addEventListener("pointerleave", () => { tid = setTimeout(() => setUnder(false), 220); });
}

// mobile menu
const mk = $(".meny-knapp"), mm = $("#mmeny");
function setMeny(o) {
  mk.setAttribute("aria-expanded", String(o));
  mk.textContent = o ? mk.dataset.stang : mk.dataset.oppna;
  mm.hidden = !o;
  if (o) lenis.stop(); else lenis.start();
}
mk.addEventListener("click", () => setMeny(mk.getAttribute("aria-expanded") !== "true"));
addEventListener("keydown", (e) => { if (e.key === "Escape" && !mm.hidden) { setMeny(false); mk.focus(); } });
mm.addEventListener("click", (e) => { if (e.target.closest("a")) setMeny(false); });

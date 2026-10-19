import { gsap, ScrollTrigger, SplitText, CustomEase } from "/gsap.js";
import lenis from "/smooth-scroll.js";

// Riktning A · "Linsen". En linjär rörelse: mosaiken blir fönster mot piren, kameraturen är
// hjulet, fasadens raster sorterar sig till sju 2×2, limeytan växer ur en bricka, brickorna
// samlas till app-ikonen i sidfoten. Allt starttillstånd sätts här (fail toward visible).

const doc = document.documentElement;
doc.classList.add("js");
if ("scrollRestoration" in history) history.scrollRestoration = "manual";

const $ = (s, c = document) => c.querySelector(s);
const $$ = (s, c = document) => [...c.querySelectorAll(s)];
const rootStyle = getComputedStyle(doc);
const tok = (n) => rootStyle.getPropertyValue("--" + n).trim().toLowerCase();
const preview = new URLSearchParams(location.search).get("preview");
const fine = matchMedia("(hover: hover) and (pointer: fine)").matches;

ScrollTrigger.config({ ignoreMobileResize: true });

// Avstånd i layout (transformer räknas inte), från el till en positionerad förfader.
function offsetIn(el, anc) {
  let x = 0, y = 0, n = el;
  while (n && n !== anc) { x += n.offsetLeft; y += n.offsetTop; n = n.offsetParent; }
  return { x, y };
}
// Seedad slump: samma spridning varje laddning (skärmdumparna går att jämföra).
function rng(seed) {
  return () => {
    seed = (seed + 0x6d2b79f5) | 0;
    let t = Math.imul(seed ^ (seed >>> 15), 1 | seed);
    t = (t + Math.imul(t ^ (t >>> 7), 61 | t)) ^ t;
    return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
  };
}

/* ---------- innehåll som bara JS kan dela utan att skriva text ---------- */
// Koncernraden: länken täcker "www.memoservices.no ↗" i slutet av meningen.
$$("[data-link-text]").forEach((p) => {
  const lt = p.dataset.linkText, tn = p.firstChild;
  if (!tn || tn.nodeType !== 3) return;
  const i = tn.data.lastIndexOf(lt);
  if (i < 0) return;
  const tail = tn.splitText(i);
  const a = document.createElement("a");
  a.href = p.dataset.href; a.target = "_blank"; a.rel = "noopener";
  tail.replaceWith(a); a.appendChild(tail);
});
// Om-punkterna: originalets <strong> på fetstilsdelen.
$$("[data-bold]").forEach((p) => {
  const b = p.dataset.bold, tn = p.firstChild;
  if (!tn || tn.nodeType !== 3 || !tn.data.startsWith(b)) return;
  tn.splitText(b.length);
  const s = document.createElement("strong");
  tn.replaceWith(s); s.appendChild(tn);
});

/* ---------- nav: Tjänster-panelen och mobilmenyn ---------- */
const navL = $(".nav-l");
const tgl = $(".tj-toggle"), panel = $("#tj-panel");
function setPanel(open) {
  tgl.setAttribute("aria-expanded", String(open));
  panel.hidden = !open;
  if (open) gsap.fromTo($$("li", panel), { autoAlpha: 0, y: 6 }, { autoAlpha: 1, y: 0, duration: 0.32, stagger: 0.025, ease: "power2.out" });
}
tgl.addEventListener("click", () => setPanel(panel.hidden));
// Panelen ligger under länkraden i DOM (brickan fälls ut nedåt); tabbordningen följer ändå
// knappen: Tab från knappen går in i panelen, Tab från sista raden vidare till "Insikter".
{
  const pLinks = () => $$("a", panel);
  const nextLink = $(".nav-links > li:nth-child(2) a");
  tgl.addEventListener("keydown", (e) => {
    if (e.key === "Tab" && !e.shiftKey && !panel.hidden) { e.preventDefault(); pLinks()[0].focus(); }
  });
  panel.addEventListener("keydown", (e) => {
    if (e.key !== "Tab") return;
    const l = pLinks(), i = l.indexOf(document.activeElement);
    if (e.shiftKey && i === 0) { e.preventDefault(); tgl.focus(); }
    else if (!e.shiftKey && i === l.length - 1) { e.preventDefault(); nextLink.focus(); }
  });
  nextLink.addEventListener("keydown", (e) => {
    if (e.key === "Tab" && e.shiftKey && !panel.hidden) { e.preventDefault(); pLinks().at(-1).focus(); }
  });
}
navL.addEventListener("focusout", (e) => { if (!panel.hidden && !navL.contains(e.relatedTarget)) setPanel(false); });
document.addEventListener("click", (e) => { if (!panel.hidden && !e.target.closest(".nav-l")) setPanel(false); });

const menu = $("#menu"), mBtn = $(".menu-btn"), mClose = $(".menu-close");
function openMenu() {
  menu.hidden = false; mBtn.setAttribute("aria-expanded", "true"); lenis.stop(); mClose.focus();
  gsap.fromTo($$(".menu-list > li, .menu > .btn", menu), { autoAlpha: 0, y: 10 }, { autoAlpha: 1, y: 0, duration: 0.4, stagger: 0.03, ease: "power2.out" });
}
function closeMenu(refocus = true) {
  menu.hidden = true; mBtn.setAttribute("aria-expanded", "false"); lenis.start(); if (refocus) mBtn.focus();
}
mBtn.addEventListener("click", openMenu);
mClose.addEventListener("click", () => closeMenu());
$$("a", menu).forEach((a) => a.addEventListener("click", () => closeMenu(false)));
document.addEventListener("keydown", (e) => {
  if (e.key !== "Escape") return;
  if (!panel.hidden) { setPanel(false); tgl.focus(); }
  if (!menu.hidden) closeMenu();
});

/* ---------- hero: lins, video, upplösning ---------- */
const hero = $(".hero");
const lens = $(".lens", hero);
const video = $("video", lens);
const plate = $(".plate", hero);
const heroH1 = $("h1", plate);
const plateBits = [$(".kicker", plate), $(".lead", plate), $(".ingress", plate), $(".actions", plate)];
const hb = $$(".hb", hero);

// Sista rutan (kameran inne i fasaden) som stillbild: bär slutet även om videon inte spelar.
const lastImg = new Image();
lastImg.src = "/tests/memoservices-koncept/assets/video/piren-last.webp";
lastImg.alt = ""; lastImg.decoding = "async";
lastImg.setAttribute("aria-hidden", "true");
lens.appendChild(lastImg);

// Pixelblock-dissolve: 8×5 ink-brickor över vyn.
const dis = document.createElement("div");
dis.className = "dissolve"; dis.setAttribute("aria-hidden", "true");
for (let i = 0; i < 40; i++) dis.appendChild(document.createElement("i"));
hero.appendChild(dis);
const tiles = [...dis.children];

// Linsen: videon syns bara genom 28 hål (clipPath = union av rects).
const NS = "http://www.w3.org/2000/svg";
const clipSvg = document.createElementNS(NS, "svg");
clipSvg.setAttribute("class", "clipdefs"); clipSvg.setAttribute("aria-hidden", "true");
const clip = document.createElementNS(NS, "clipPath");
clip.setAttribute("id", "lens-clip"); clip.setAttribute("clipPathUnits", "userSpaceOnUse");
const rects = hb.map(() => clip.appendChild(document.createElementNS(NS, "rect")));
clipSvg.appendChild(clip); document.body.appendChild(clipSvg);
const holes = hb.map(() => ({ x: 0, y: 0, w: 0, h: 0, r: 0 }));
function drawHoles() {
  for (let i = 0; i < holes.length; i++) {
    const h = holes[i], r = rects[i];
    r.setAttribute("x", h.x.toFixed(1)); r.setAttribute("y", h.y.toFixed(1));
    r.setAttribute("width", Math.max(0, h.w).toFixed(1)); r.setAttribute("height", Math.max(0, h.h).toFixed(1));
    r.setAttribute("rx", Math.max(0, h.r).toFixed(1));
  }
}
drawHoles();
lens.style.clipPath = "url(#lens-clip)";

gsap.set(plateBits, { autoAlpha: 0 });
gsap.set(heroH1, { autoAlpha: 0 });
gsap.set(hb, { autoAlpha: 0 });
gsap.set(lastImg, { autoAlpha: 0 });
gsap.set(tiles, { autoAlpha: 0 });

// Videon: scrubfilen som Blob efter första målningen; currentTime skrivs av hjulet.
const vp = { p: 0 };
function seek() {
  const d = video.duration;
  if (!d || video.readyState < 1) return;
  const t = Math.min(d - 0.04, vp.p * d);
  if (!video.seeking && Math.abs(video.currentTime - t) > 1 / 24) video.currentTime = t;
}
video.addEventListener("seeked", seek);
video.addEventListener("loadedmetadata", seek);
function loadVideo() {
  const src = video.dataset.src;
  fetch(src).then((r) => { if (!r.ok) throw new Error(r.status); return r.blob(); })
    .then((b) => { video.src = URL.createObjectURL(b); video.load(); })
    .catch(() => { video.src = src; });
}
if (document.readyState === "complete") requestAnimationFrame(() => setTimeout(loadVideo, 60));
else addEventListener("load", () => requestAnimationFrame(() => setTimeout(loadVideo, 60)), { once: true });

/* ---------- fasaden: data ---------- */
const fas = $(".fasad");
const groupsEl = $(".groups", fas);
const grps = $$(".grp", fas);
const fb = grps.flatMap((g) => $$(".b", g));
const steps = $$(".step", fas);
const SVC = [["t-redovisning", "a-redovisning"], ["t-hr", "a-hr"], ["t-skatt", "a-skatt"], ["t-juridik", "a-juridik"],
  ["t-finans", "a-finans"], ["t-grc", "a-grc"], ["t-opex", "a-opex"]];
const endHex = fb.map((_, j) => tok(SVC[j >> 2][j % 4 === 3 ? 1 : 0]));
const cells = hb.map((b) => ({ r: +b.dataset.r, c: +b.dataset.c, hex: tok(b.dataset.t) }));
// Varje bricka i en 2×2 hämtar en hero-bricka: samma färg om det finns, annars närmaste.
const assign = (() => {
  const used = new Set(), out = new Array(fb.length);
  const slot = (j) => { const g = j >> 2, k = j % 4; return { x: ((g % 4) * 2 + (k % 2)) / 7, y: ((g >> 2) * 2 + (k >> 1)) / 3 }; };
  const cpos = (c) => ({ x: (c.c - 1) / 6, y: (c.r - 1) / 4 });
  const pick = (j, sameColor) => {
    let best = -1, bd = Infinity; const s = slot(j);
    cells.forEach((c, i) => {
      if (used.has(i) || (sameColor && c.hex !== endHex[j])) return;
      const p = cpos(c), d = (p.x - s.x) ** 2 + (p.y - s.y) ** 2;
      if (d < bd) { bd = d; best = i; }
    });
    return best;
  };
  fb.forEach((_, j) => { const i = pick(j, true); if (i >= 0) { used.add(i); out[j] = i; } });
  fb.forEach((_, j) => { if (out[j] === undefined) { const i = pick(j, false); used.add(i); out[j] = i; } });
  return out;
})();

let fGeo = null, gGeo = null;
ScrollTrigger.addEventListener("refreshInit", () => { fGeo = null; gGeo = null; });
function fasGeo() {
  if (fGeo) return fGeo;
  const b = fb[0].offsetWidth, g = (b * 8) / 51, wide = innerWidth >= 900;
  const gp = offsetIn(groupsEl, fas);
  const cx = wide ? gp.x + groupsEl.offsetWidth / 2 : fas.clientWidth / 2;
  const cy = gp.y + groupsEl.offsetHeight / 2;
  const ox = cx - (7 * b + 6 * g) / 2, oy = cy - (5 * b + 4 * g) / 2;
  fGeo = fb.map((el, j) => {
    const f = offsetIn(el, fas), c = cells[assign[j]];
    return { dx: ox + (c.c - 1) * (b + g) - f.x, dy: oy + (c.r - 1) * (b + g) - f.y };
  });
  return fGeo;
}

/* ---------- sidfoten: data ---------- */
const foot = $(".foot");
const gbs = $$(".gb", foot);
const appBase = $(".app-base", foot);
const R3 = rng(23);
const scat = gbs.map(() => ({ u: R3(), v: R3(), d: R3() }));
const startCols = SVC.map((s) => tok(s[0]));
function footGeo() {
  if (gGeo) return gGeo;
  const W = foot.clientWidth, s = gbs[0].offsetWidth || 15;
  // Spridda över hela sidfoten; samlingspunkten är raden med logotypen.
  const H = foot.clientHeight;
  gGeo = gbs.map((el, i) => {
    const f = offsetIn(el, foot);
    const x = 16 + scat[i].u * (W - 32 - s), y = 24 + scat[i].v * (H - 64 - s);
    return { dx: x - f.x, dy: y - f.y };
  });
  return gGeo;
}

/* ---------- rubriker: SplitText-radmasker ---------- */
function revealLines(el, start = "top 82%", trigger = el) {
  let done = false, cur = null;
  SplitText.create(el, { // på rubriken själv: aria-label hamnar på h2, aldrig på en span
    type: "lines", mask: "lines", linesClass: "ln", autoSplit: true,
    onSplit(self) {
      cur = gsap.fromTo(self.lines, { yPercent: 120 }, { yPercent: 0, duration: 1.15, ease: "power3.out", stagger: 0.09, paused: true });
      if (done) cur.progress(1);
      return cur;
    },
  });
  ScrollTrigger.create({ trigger, start, once: true, onEnter: () => { done = true; cur && cur.play(); } });
}
function revealBatch(els, start = "top 88%") {
  if (!els.length) return;
  gsap.set(els, { autoAlpha: 0, y: 14 });
  ScrollTrigger.batch(els, {
    start, once: true,
    onEnter: (b) => gsap.to(b, { autoAlpha: 1, y: 0, duration: 0.62, ease: "power2.out", stagger: 0.06, overwrite: true }),
  });
}

/* ---------- init efter typsnitten ---------- */
const fontsReady = Promise.race([document.fonts.ready, new Promise((r) => setTimeout(r, 2200))]);
fontsReady.then(init);

function init() {
  CustomEase.create("msIn", ".34,1.56,.64,1");

  /* Akt 0 · intro: 28 brickor flyger in, blir fönster, fönstren växer ihop */
  const W = hero.clientWidth, H = hero.clientHeight;
  const R = rng(7);
  const pos = hb.map((b) => ({ ...offsetIn(b, hero), s: b.offsetWidth, r: +b.dataset.r, c: +b.dataset.c }));
  const off = pos.map((p) => {
    const a = R() * Math.PI * 2, d = Math.hypot(W, H) * 0.62;
    return { x: W / 2 + Math.cos(a) * d - p.x, y: H / 2 + Math.sin(a) * d - p.y };
  });
  pos.forEach((p, i) => Object.assign(holes[i], { x: p.x + p.s / 2, y: p.y + p.s / 2, w: 0, h: 0, r: (p.s * 10) / 51 }));
  const cw = W / 7, ch = H / 5;
  const intro = gsap.timeline({
    paused: true, onUpdate: drawHoles,
    onComplete() { lens.style.clipPath = "none"; },
  });
  intro
    .fromTo(hb, { x: (i) => off[i].x, y: (i) => off[i].y, autoAlpha: 1 },
      { x: 0, y: 0, duration: 1.1, ease: "msIn", stagger: { amount: 0.6, from: "random" } }, 0)
    .to(holes, { x: (i) => pos[i].x, y: (i) => pos[i].y, w: (i) => pos[i].s, h: (i) => pos[i].s, duration: 0.01 }, 1.72)
    .to(hb, { autoAlpha: 0.18, duration: 0.32, ease: "power1.out" }, 1.74)
    .to(holes, {
      x: (i) => (pos[i].c - 2) * cw, y: (i) => (pos[i].r - 2) * ch, w: cw * 3 + 2, h: ch * 3 + 2, r: 0,
      duration: 1.4, ease: "power3.inOut", stagger: { amount: 0.22, from: "random" },
    }, 2.05)
    .to(hb, { autoAlpha: 0, duration: 0.9, ease: "power1.in" }, 2.2)
    .addLabel("type", 2.05 + 1.62 * 0.64)
    .set(heroH1, { autoAlpha: 1 }, "type")
    .fromTo(plateBits, { autoAlpha: 0, y: 14 }, { autoAlpha: 1, y: 0, duration: 0.62, ease: "power2.out", stagger: 0.08 }, "type+=0.3");
  let firstHero = true;
  SplitText.create(heroH1, {
    type: "lines", mask: "lines", linesClass: "ln", autoSplit: true,
    onSplit(self) {
      const tw = gsap.fromTo(self.lines, { yPercent: 120 }, { yPercent: 0, duration: 0.95, ease: "power3.out", stagger: 0.09 });
      if (firstHero) { intro.add(tw, "type"); firstHero = false; } else tw.progress(1);
      return tw;
    },
  });

  /* Akt 1 · hero: pin 300 vh, kameraturen är hjulet */
  const heroTl = gsap.timeline({
    defaults: { ease: "none" },
    scrollTrigger: { trigger: hero, start: "top top", end: () => "+=" + Math.round(innerHeight * 3), pin: true, scrub: true, invalidateOnRefresh: true },
  });
  heroTl
    .to(vp, { p: 1, duration: 0.78, onUpdate: seek }, 0)
    .to(plate, { yPercent: -30, duration: 0.4 }, 0.4)
    // Under upplösningen lämnar plattan vyn uppåt, så att fogarna mellan ink-brickorna bara visar fasaden.
    .to(plate, { yPercent: -110, duration: 0.17, ease: "power2.in" }, 0.81)
    .to(lastImg, { autoAlpha: 1, duration: 0.05 }, 0.74)
    .to(tiles, { autoAlpha: 1, duration: 0.012, stagger: { amount: 0.17, from: "random" } }, 0.81)
    .set({}, {}, 1);

  /* Akt 2 · fasaden: pin 500 vh, rastret sorterar sig, en tjänst lyser i taget */
  const fLen = () => Math.round(innerHeight * (innerWidth < 900 ? 4 : 5));
  const fTl = gsap.timeline({
    defaults: { ease: "none" },
    scrollTrigger: { trigger: fas, start: "top top", end: () => "+=" + fLen(), pin: true, scrub: true, invalidateOnRefresh: true },
  });
  const R2 = rng(11);
  fb.forEach((el, j) => {
    fTl.fromTo(el,
      { x: () => fasGeo()[j].dx, y: () => fasGeo()[j].dy, backgroundColor: cells[assign[j]].hex },
      { x: 0, y: 0, backgroundColor: endHex[j], duration: 0.1, ease: "power2.inOut" }, R2() * 0.045);
  });
  const fKick = $(".f-kicker", fas), fH2 = $(".f-head h2", fas), fLink = $(".f-lank", fas);
  fTl.fromTo(fKick, { autoAlpha: 0, y: 14 }, { autoAlpha: 1, y: 0, duration: 0.03 }, 0.12);
  SplitText.create(fH2, {
    type: "lines", mask: "lines", linesClass: "ln", autoSplit: true,
    onSplit(self) {
      const tw = gsap.fromTo(self.lines, { yPercent: 120 }, { yPercent: 0, duration: 0.05, stagger: 0.012, ease: "power2.out" });
      fTl.add(tw, 0.125);
      return tw;
    },
  });
  fTl.fromTo(fLink, { autoAlpha: 0, y: 14 }, { autoAlpha: 1, y: 0, duration: 0.03 }, 0.17);
  const T0 = 0.2, S = 0.095, D = 0.025, TX = 0.945, tAt = (i) => T0 + i * S;
  gsap.set(steps, { autoAlpha: 0 });
  steps.forEach((s, i) => {
    fTl.fromTo(s, { autoAlpha: 0, y: 14 }, { autoAlpha: 1, y: 0, duration: D, immediateRender: false }, tAt(i));
    if (i < steps.length - 1) fTl.to(s, { autoAlpha: 0, y: -14, duration: D * 0.8 }, tAt(i + 1) - D * 0.5);
  });
  // Dämpade grupper: opacity .5 + saturate(.6) (bara de dämpade), aldrig lerigt mot ink.
  gsap.set(grps, { filter: "saturate(1)" });
  for (let i = 0; i < grps.length; i++) {
    fTl.to(grps, {
      opacity: (j) => (j === i ? 1 : 0.5), scale: (j) => (j === i ? 1.15 : 1),
      filter: (j) => (j === i ? "saturate(1)" : "saturate(0.6)"), duration: D,
    }, tAt(i));
  }
  fTl.to(grps, { opacity: 1, scale: 1, filter: "saturate(1)", duration: D }, tAt(grps.length));
  // Under stegets håll: korttexten tänds ord för ord (grafit → vit, floor-regel 4) och den
  // aktiva 2×2:an andas 1,00 → 1,06 (på tilt-lagret; gruppens skala ägs av stegbytena ovan).
  const tilts = grps.map((g) => $(".grp-tilt", g));
  const holdEnd = (i) => (i < steps.length - 1 ? tAt(i + 1) - D * 0.5 : TX);
  steps.forEach((s, i) => {
    const t0 = tAt(i) + D, hold = holdEnd(i) - t0;
    const words = SplitText.create($(".step-text", s), { type: "words", aria: "none" }).words;
    gsap.set(words, { color: tok("grafit") });
    fTl.to(words, { color: tok("bakgrund"), duration: 0.01, stagger: { amount: Math.max(0, hold - 0.012) } }, t0);
    if (i < grps.length) {
      fTl.fromTo(tilts[i], { scale: 1 }, { scale: 1.06, duration: hold, ease: "sine.inOut", immediateRender: false }, t0)
        .to(tilts[i], { scale: 1, duration: D * 0.8 }, holdEnd(i));
    }
  });
  // Utgång (sista ~5 %): de sju 2×2 drar sig mot radens axel och texten lämnar, så att
  // limeytan kan växa ur en bricka i mitten när sidan går vidare.
  const gc = (g) => ({ x: g.offsetLeft + g.offsetWidth / 2 - groupsEl.offsetWidth / 2, y: g.offsetTop + g.offsetHeight / 2 - groupsEl.offsetHeight / 2 });
  const toAxis = () => fas.clientWidth / 2 - (offsetIn(groupsEl, fas).x + groupsEl.offsetWidth / 2);
  fTl.to(grps, { x: (j, g) => toAxis() - gc(g).x * 0.55, y: (j, g) => -gc(g).y * 0.55, scale: 0.5, duration: 1 - TX, ease: "power2.inOut" }, TX)
    .to([$(".f-head", fas), $(".steps", fas)], { autoAlpha: 0, y: -28, duration: (1 - TX) * 0.7, ease: "power1.in" }, TX)
    .set({}, {}, 1);
  // Tangentbord: fokus på en 2×2 scrollar till dess steg så att texten syns.
  grps.forEach((g, i) => g.addEventListener("focus", () => {
    if (!g.matches(":focus-visible")) return;
    const st = fTl.scrollTrigger;
    lenis.scrollTo(st.start + (tAt(i) + S * 0.45) * (st.end - st.start), { immediate: true });
  }));

  /* Akt 3 · kartläggning: limeytan växer ur en bricka, grunden byter till papper */
  const kart = $(".kart"), kPanel = $(".kart-panel", kart);
  const kInset = () => {
    const Wk = kPanel.clientWidth, Hk = kPanel.clientHeight, b = fb[0].offsetWidth || 56, cy = innerHeight * 0.16;
    return `inset(${cy - b / 2}px ${(Wk - b) / 2}px ${Hk - cy - b / 2}px ${(Wk - b) / 2}px round ${(b * 10) / 51}px)`;
  };
  const kTl = gsap.timeline({
    defaults: { ease: "none" },
    scrollTrigger: { trigger: kart, start: "top 80%", end: () => "+=" + Math.round(innerHeight * 1.2), scrub: true, invalidateOnRefresh: true },
  });
  // Ingen tonad grund (en grå mellanton mellan ink och papper är förbjuden): limen täcker
  // ink-grunden helt, och papperet kommer under den med om-avsnittets stegade kant.
  kTl.fromTo(kPanel, { clipPath: kInset }, { clipPath: "inset(0px 0px 0px 0px round 0px)", duration: 1, ease: "power2.in" }, 0)
    .set({}, {}, 1);

  const header = $(".nav");
  ScrollTrigger.create({
    trigger: kart, start: "top 40px", endTrigger: ".insikter", end: "bottom 40px",
    onToggle: (s) => { header.dataset.theme = s.isActive ? "light" : "dark"; },
  });
  revealBatch($$("[data-rv]", kart), "top 92%");
  revealLines($("h2", kart), "top 72%");

  /* Akt 4 · om: stegad kant i brickans enhet, ledger med 2×2-markörer */
  const om = $("#om");
  const edge = { k: 1 };
  function drawEdge() {
    const Wo = om.clientWidth, b = fb[0].offsetWidth || 51, u = b + (b * 8) / 51;
    const n = Math.ceil(Wo / u), pts = [];
    for (let i = 0; i < n; i++) {
      const h = (((i * 5 + 2) % 4) * 8 * edge.k).toFixed(1);
      pts.push(`${(i * u).toFixed(1)}px ${h}px`, `${Math.min(Wo, (i + 1) * u).toFixed(1)}px ${h}px`);
    }
    pts.push("100% 100%", "0% 100%");
    om.style.clipPath = `polygon(${pts.join(",")})`;
  }
  drawEdge();
  ScrollTrigger.addEventListener("refresh", drawEdge);
  gsap.to(edge, { k: 0, ease: "power3.in", onUpdate: drawEdge, scrollTrigger: { trigger: om, start: "top bottom", end: "top 12%", scrub: true } });
  revealBatch($$("[data-rv]", om));
  revealLines($("h2", om), "top 80%");
  const marks = $$(".ledger .m2", om);
  gsap.set(marks, { opacity: 0.25 });
  ScrollTrigger.batch($$(".ledger li", om), {
    start: "top 86%", once: true,
    onEnter: (rows) => gsap.to(rows.map((r) => $(".m2", r)), { opacity: 1, duration: 0.5, stagger: 0.09, ease: "power2.out" }),
  });

  /* Akt 5 · insikter: ledger-rader glider in */
  const ins = $(".insikter");
  revealLines($("h2", ins), "top 84%");
  revealBatch($$("[data-rv]", ins));

  /* Akt 6 · slut: brickorna samlas till app-ikonens 2×2 (sista triggern) */
  const gTl = gsap.timeline({
    defaults: { ease: "none" },
    scrollTrigger: { trigger: foot, start: "top bottom", end: "bottom bottom", scrub: true, invalidateOnRefresh: true },
  });
  gbs.forEach((el, i) => {
    gTl.fromTo(el,
      { x: () => footGeo()[i].dx, y: () => footGeo()[i].dy, scale: 1.7, backgroundColor: startCols[i % 7] },
      { x: 0, y: 0, scale: 1, backgroundColor: i >= 21 ? tok("lime") : tok("bakgrund"), duration: 0.62, ease: "power2.inOut" },
      scat[i].d * 0.22);
  });
  gTl.fromTo(appBase, { autoAlpha: 0, scale: 0.4 }, { autoAlpha: 1, scale: 1, duration: 0.12, ease: "back.out(1.6)" }, 0.86).set({}, {}, 1);

  /* Pekare: magnet på primär-CTA, tilt 6° på de sju 2×2 */
  if (fine) {
    const cta = $(".btn-magnet");
    const qx = gsap.quickTo(cta, "x", { duration: 0.5, ease: "power3" }), qy = gsap.quickTo(cta, "y", { duration: 0.5, ease: "power3" });
    cta.addEventListener("pointermove", (e) => {
      const r = cta.getBoundingClientRect();
      qx((e.clientX - r.left - r.width / 2) * 0.28); qy((e.clientY - r.top - r.height / 2) * 0.36);
    });
    cta.addEventListener("pointerleave", () => { qx(0); qy(0); });
    grps.forEach((g) => {
      const t = $(".grp-tilt", g);
      gsap.set(t, { transformPerspective: 600 });
      const rx = gsap.quickTo(t, "rotationX", { duration: 0.6, ease: "power3" }), ry = gsap.quickTo(t, "rotationY", { duration: 0.6, ease: "power3" });
      g.addEventListener("pointermove", (e) => {
        const r = g.getBoundingClientRect();
        ry(((e.clientX - r.left) / r.width - 0.5) * 12); rx(-((e.clientY - r.top) / r.height - 0.5) * 12);
      });
      g.addEventListener("pointerleave", () => { rx(0); ry(0); });
    });
  }

  ScrollTrigger.refresh();
  lenis.resize(); // pin-spacers just grew the page; Lenis's limit must follow before any scrollTo
  addEventListener("load", () => { ScrollTrigger.refresh(); lenis.resize(); }, { once: true });

  /* ?preview=<akt> */
  const top = (el) => el.getBoundingClientRect().top + scrollY;
  const at = (st, p) => st.start + p * (st.end - st.start);
  const targets = () => ({
    hero: 0,
    fasad: at(fTl.scrollTrigger, 0.195),
    tjanster: at(fTl.scrollTrigger, tAt(0) + 0.05),
    kartlaggning: kTl.scrollTrigger.end,
    om: top(om),
    insikter: top(ins),
    slut: ScrollTrigger.maxScroll(window),
  });
  window.__previewTargets = targets;
  if (preview && preview in targets()) {
    intro.progress(1);
    const y = Math.round(targets()[preview]);
    lenis.scrollTo(y, { immediate: true, force: true });
    ScrollTrigger.update();
  } else {
    lenis.scrollTo(0, { immediate: true, force: true });
    intro.play();
    // Den som börjar scrolla under introt väntar inte: introt spelas klart i fyrdubbel takt.
    const hurry = () => { if (intro.progress() < 1) intro.timeScale(4); };
    requestAnimationFrame(() => {
      addEventListener("wheel", hurry, { once: true, passive: true });
      addEventListener("touchmove", hurry, { once: true, passive: true });
      addEventListener("keydown", hurry, { once: true });
      addEventListener("scroll", hurry, { once: true, passive: true });
    });
  }
}

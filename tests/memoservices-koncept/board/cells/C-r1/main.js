import { gsap, ScrollTrigger, SplitText, CustomEase } from "/gsap.js"; import lenis from "/smooth-scroll.js";

/* C · Passagen
   Akter: intro → hero (parallax i tre plan) → passagen (pin + pan, brickmolnet blir första objektet)
   → kartläggning (limebrickan växer ur railen) → om (arket läggs över, orden tänds)
   → insikter (reveal per objekt) → slut (brickorna lägger sig som sidfotens index).
   Ingenting döljs i CSS; varje starttillstånd sätts här. Ingen läsning av prefers-reduced-motion (F-011). */

const $ = (s, r = document) => r.querySelector(s);
const $$ = (s, r = document) => Array.from(r.querySelectorAll(s));
const root = document.documentElement;
const tok = (n) => getComputedStyle(root).getPropertyValue(n).trim();
const PREVIEW = new URLSearchParams(location.search).get("preview");
const FINE = matchMedia("(hover: hover) and (pointer: fine)").matches;
const DESK = matchMedia("(min-width: 1360px)");
const clamp01 = gsap.utils.clamp(0, 1);
CustomEase.create("settle", "0.16, 1, 0.3, 1");

const hdr = $("#hdr");
const H = () => hdr.offsetHeight;
const tail = () => Math.round(innerHeight * 0.35); // pinnens svans: limen täcker, bandet under tar över
const U = () => (innerWidth < 768 ? 40 : 59); // brickans enhet: 51 + 8 px (mindre på mobil)
const setHdr = () => {
  root.style.setProperty("--hdr", hdr.offsetHeight + "px");
  root.style.setProperty("--tail", tail() + "px");
  root.style.setProperty("--u", U() + "px");
};

/* ── 0. DOM-justeringar (ingen text ändras) ─────────────────────────────── */
const video = $(".hero-video");
if (video && matchMedia("(max-width: 768px)").matches && video.dataset.small) {
  video.src = video.dataset.small;
  video.load();
  video.play().catch(() => {});
}
// pilen i "→"-länkarna i brandröd
$$("[data-arrow]").forEach((a) => {
  const w = document.createTreeWalker(a, NodeFilter.SHOW_TEXT);
  let n, last = null;
  while ((n = w.nextNode())) if (n.nodeValue.includes("→")) last = n;
  if (!last) return;
  const arrow = last.splitText(last.nodeValue.lastIndexOf("→"));
  arrow.splitText(1);
  const s = document.createElement("span");
  s.className = "arr";
  arrow.replaceWith(s);
  s.append(arrow);
});
// koncernraden: länken täcker bara "www.memoservices.no ↗" (utan JS länkar hela raden)
{
  const p = $(".koncern"), a = p && p.querySelector("a");
  if (a) {
    const t = a.textContent, i = t.indexOf("www.");
    if (i > 0) { a.textContent = t.slice(i); p.prepend(document.createTextNode(t.slice(0, i))); }
  }
}
// om-punkterna: originalets <strong> på fetstilsdelen
$$("[data-bold]").forEach((p) => {
  const b = p.dataset.bold, t = p.textContent;
  if (!b || !t.startsWith(b)) return;
  const s = document.createElement("strong");
  s.textContent = b;
  p.textContent = "";
  p.append(s, t.slice(b.length));
});

/* ── Meny (mobil) ───────────────────────────────────────────────────────── */
const menuBtn = $(".menu-btn"), nav = $("#meny");
function setMenu(open) {
  if (!nav || !menuBtn) return;
  const was = nav.classList.contains("open");
  nav.classList.toggle("open", open);
  menuBtn.setAttribute("aria-expanded", String(open));
  $(".mb-open", menuBtn).hidden = open;
  $(".mb-close", menuBtn).hidden = !open;
  if (open) { lenis.stop(); const f = nav.querySelector("a"); f && f.focus(); }
  else if (was) lenis.start();
}
menuBtn && menuBtn.addEventListener("click", () => setMenu(!nav.classList.contains("open")));
document.addEventListener("keydown", (e) => {
  if (e.key === "Escape" && nav.classList.contains("open")) { setMenu(false); menuBtn.focus(); }
});
DESK.addEventListener("change", () => setMenu(false));
// "Om oss" (/#om) på startsidan: rulla dit i stället för att lämna sidan
$$('a[href="/#om"]').forEach((a) => a.addEventListener("click", (e) => {
  if (e.metaKey || e.ctrlKey || e.shiftKey || e.altKey || e.button) return;
  e.preventDefault();
  setMenu(false);
  lenis.scrollTo($("#om"), { offset: -H() });
}));

/* ── Init efter typsnitten ──────────────────────────────────────────────── */
let pinST, flightST, objs = [], hold, overflow;
Promise.race([document.fonts.ready, new Promise((r) => setTimeout(r, 2500))]).then(init);

function init() {
  setHdr();
  ScrollTrigger.addEventListener("refreshInit", setHdr);
  const intro = buildIntro(!!PREVIEW);
  heroParallax();
  passage();
  kart();
  om();
  insikter();
  footer();
  pointer();
  ScrollTrigger.refresh();
  lenis.resize();
  if (PREVIEW) jump(PREVIEW);
  else if (intro) {
    intro.play();
    // den som scrollar under introt vill vidare: spela klart det fort
    const hurry = () => { if (window.scrollY > 40) { intro.timeScale(5); removeEventListener("scroll", hurry); } };
    addEventListener("scroll", hurry, { passive: true });
  }
}

/* ── Intro → hero (regel 1): kickern sätts på papper, papperet lyfter, kickern blir navbarens etikett ── */
function buildIntro(skip) {
  const kicker = $("#kicker");
  const others = [$(".logo"), $(".links"), $(".nav-cta"), $(".index"), $(".menu-btn")].filter(Boolean);
  const bricks = $$(".cloud .b");
  const rest = [$(".lead"), $(".ingress"), $(".actions")];
  const splits = $$(".h1 > span").map((s) =>
    SplitText.create(s, { type: "lines", mask: "lines", linesClass: "ln", autoSplit: true, aria: "none" }));
  if (skip) { root.classList.remove("pre"); return null; }

  const curtain = document.createElement("div");
  curtain.className = "curtain";
  curtain.setAttribute("aria-hidden", "true");
  document.body.append(curtain);
  root.classList.add("intro");

  const kr = kicker.getBoundingClientRect();
  const sc = Math.min(2.2, (innerWidth * 0.84) / kr.width);
  const words = SplitText.create(kicker, { type: "words", aria: "none" });
  // heroens kicker är röd på papperet; i navbaren blir den ink
  gsap.set(kicker, {
    x: innerWidth / 2 - (kr.left + kr.width / 2),
    y: innerHeight * 0.44 - (kr.top + kr.height / 2),
    scale: sc,
    color: tok("--ink"), // ink även i introt: 11 px röd mäter 4,17:1 (axe), under 4,5
  });
  gsap.set(others, { autoAlpha: 0 });
  gsap.set(words.words, { autoAlpha: 0, yPercent: 60 });
  const lines = splits.flatMap((s) => s.lines);
  gsap.set(lines, { yPercent: 145 });
  gsap.set(rest, { autoAlpha: 0, y: 14 });
  gsap.set(bricks, { autoAlpha: 0, y: (i) => -(180 + ((i * 37) % 9) * 32) });
  root.classList.remove("pre");

  const tl = gsap.timeline({
    paused: true,
    onComplete() {
      curtain.remove();
      root.classList.remove("intro");
      words.revert();
      gsap.set(kicker, { clearProps: "transform,color" });
    },
  });
  tl.to(words.words, { autoAlpha: 1, yPercent: 0, duration: 0.5, ease: "power2.out", stagger: 0.065 })
    .addLabel("lift", "+=0.3")
    .to(curtain, { yPercent: -100, duration: 1.2, ease: "power3.inOut" }, "lift")
    .to(kicker, { x: 0, y: 0, scale: 1, color: tok("--ink"), duration: 1.2, ease: "power3.inOut" }, "lift")
    .to(bricks, { autoAlpha: 1, y: 0, duration: 0.9, ease: "back.out(1.3)", stagger: 0.028 }, "lift+=0.35")
    .to(lines, { yPercent: 0, duration: 1.05, ease: "settle", stagger: 0.08 }, "lift+=0.55")
    .to(rest, { autoAlpha: 1, y: 0, duration: 0.62, ease: "power2.out", stagger: 0.06 }, "lift+=0.85")
    .to(others, { autoAlpha: 1, duration: 0.5, ease: "power1.out", stagger: 0.04 }, "lift+=0.95");
  return tl;
}

/* ── Akt 1 · hero: tre brickplan parallaxar (fjärr −31 %, mellan −17 %, nära 1×) ── */
function heroParallax() {
  const hero = $(".hero");
  [[".far", 0.31], [".mid", 0.17]].forEach(([sel, lag]) => {
    gsap.to($(".plane" + sel), {
      y: () => (hero.offsetHeight + H()) * lag,
      ease: "none",
      scrollTrigger: { trigger: hero, start: () => `top ${H()}`, end: "bottom top", scrub: true, invalidateOnRefresh: true },
    });
  });
}

/* ── Akt 2 · passagen ───────────────────────────────────────────────────── */
function passage() {
  const sec = $("#passage"), rail = $(".rail");
  objs = $$(".obj-svc", rail);
  const first = objs[0];
  const firstMos = $(".mos-lg", first);
  const targets = $$("i", firstMos);
  const limeB = $(".lime-brick");
  const idxList = $(".index");
  const idx = $$(".index a");
  overflow = () => Math.max(0, rail.scrollWidth - innerWidth);
  hold = () => Math.round(innerHeight * 0.5);
  const limeSpan = () => Math.round(innerHeight * 1.2);

  /* Orsak in: brickfältet bildar nästa objekt. Heroens 25 brickor flyger (live-FLIP mot
     sina egna lägen varje bildruta) ihop till den första 2×2:an medan grunden blir ink. */
  const cloudBricks = $$(".cloud .b");
  const flight = document.createElement("div");
  flight.className = "flight";
  flight.setAttribute("aria-hidden", "true");
  const fb = cloudBricks.map(() => flight.appendChild(document.createElement("i")));
  document.body.append(flight);
  const clouds = $$(".cloud");
  const colI = cloudBricks.map((b, k) =>
    gsap.utils.interpolate(getComputedStyle(b).backgroundColor, getComputedStyle(targets[k % 4]).backgroundColor));
  const delays = cloudBricks.map((b, k) => ((k * 11) % 25) / 25 * 0.3);
  const ease = gsap.parseEase("power2.inOut");
  let flying = null;

  /* Ink kommer underifrån som en stegad mosaikkant: kolumner en brickenhet breda, toppen
     sjunker i hela enheter. Passagen ligger 4 enheter upp över heroens fot (CSS) och är
     helt öppen när pinnen börjar. */
  function edge(e) {
    if (e >= 1) { if (sec.style.clipPath) sec.style.clipPath = ""; return; }
    const u = U(), n = Math.ceil(sec.offsetWidth / u), max = 4 * u, pts = ["0 100%"]; // max = överlappet, aldrig djupare
    for (let k = 0; k < n; k++) {
      const d = 0.27 * (1 - k / n) + (((k * 7) % 5) / 5) * 0.18; // trappa + brus, ≤ 0,45
      const inset = Math.ceil(((1 - clamp01((e - d) / 0.55)) * max) / u) * u;
      pts.push(`${k * u}px ${inset}px`, `${(k + 1) * u}px ${inset}px`);
    }
    pts.push("100% 100%");
    sec.style.clipPath = `polygon(${pts.join(",")})`;
  }

  function renderFlight(p) {
    edge(pinST ? clamp01(window.scrollY / Math.max(1, pinST.start)) : 0);
    const on = p > 0 && p < 1;
    if (on !== flying) {
      flying = on;
      flight.style.visibility = on ? "visible" : "hidden";
      fb.forEach((el) => (el.style.willChange = on ? "transform" : "auto"));
    }
    clouds.forEach((c) => (c.style.visibility = p > 0 ? "hidden" : ""));
    firstMos.style.visibility = p > 0 && p < 1 ? "hidden" : "";
    if (!on) return;
    for (let k = 0; k < fb.length; k++) {
      const s = cloudBricks[k].getBoundingClientRect();
      const d = targets[k % 4].getBoundingClientRect();
      const q = ease(clamp01((p - delays[k]) / 0.7));
      const w = s.width + (d.width - s.width) * q;
      gsap.set(fb[k], {
        x: s.left + (d.left - s.left) * q,
        y: s.top + (d.top - s.top) * q,
        scale: w / 100,
        backgroundColor: colI[k](q),
      });
    }
  }
  flightST = ScrollTrigger.create({
    trigger: sec,
    start: 0,
    end: () => `top+=${hold()} ${H()}`,
    invalidateOnRefresh: true,
    onUpdate: (st) => renderFlight(st.progress),
    onRefresh: (st) => renderFlight(st.progress),
  });

  // Pin: hold (flygningen landar) + railens överflöde + limebrickans tillväxt
  pinST = ScrollTrigger.create({
    trigger: sec,
    start: () => `top ${H()}`,
    end: () => `+=${hold() + overflow() + limeSpan() + tail()}`,
    pin: true,
    anticipatePin: 1,
    invalidateOnRefresh: true,
    onToggle: markActive,
  });

  // Pan: x = -(scrollWidth - innerWidth), ease none
  const pan = gsap.to(rail, {
    x: () => -overflow(),
    ease: "none",
    scrollTrigger: {
      trigger: sec,
      start: () => pinST.start + hold(),
      end: () => pinST.start + hold() + overflow(),
      scrub: true,
      invalidateOnRefresh: true,
      onUpdate: markActive,
    },
  });

  // Andra lagret: fasadens raster bakom railen, parallax 0,3 mot railen
  const bg = $(".passage-bg");
  const sizeBg = () => (bg.style.width = innerWidth + Math.round(overflow() * 0.3) + "px");
  sizeBg();
  ScrollTrigger.addEventListener("refreshInit", sizeBg);
  gsap.to(bg, {
    x: () => -Math.round(overflow() * 0.3),
    ease: "none",
    scrollTrigger: {
      trigger: sec,
      start: () => pinST.start + hold(),
      end: () => pinST.start + hold() + overflow(),
      scrub: true,
      invalidateOnRefresh: true,
    },
  });

  // Rail settle: varje objekt utom det första kommer in .55 → 1, 24 → 0
  $$(".rail > .obj").forEach((it, i) => {
    if (i === 0 || it.classList.contains("obj-lime")) return;
    gsap.fromTo(it, { opacity: 0.55, y: 24 }, {
      opacity: 1, y: 0, ease: "none",
      scrollTrigger: { trigger: it, containerAnimation: pan, start: "left 100%", end: "left 70%", scrub: true },
    });
  });

  // Orsak ut: panel ur axeln. Limebrickan sist i railen växer tills den täcker vyn.
  function coverScale() {
    const size = limeB.offsetWidth;
    let x = 0, y = 0, el = limeB;
    while (el && el !== sec) { x += el.offsetLeft; y += el.offsetTop; el = el.offsetParent; }
    const cx = x - overflow() + size / 2, cy = y + size / 2;
    const w = sec.offsetWidth, h = sec.offsetHeight;
    return (Math.max(cx, w - cx, cy, h - cy) / (size / 2)) * 1.32;
  }
  gsap.fromTo(limeB, { scale: 1 }, {
    scale: () => coverScale(),
    ease: "power2.in",
    scrollTrigger: {
      trigger: sec,
      start: () => pinST.start + hold() + overflow(),
      end: () => pinST.start + hold() + overflow() + limeSpan(),
      scrub: true,
      invalidateOnRefresh: true,
      // när limen täcker vyn tar bandet under över (samma lime, sömlöst)
      onUpdate: (st) => (sec.style.visibility = st.progress >= 0.999 ? "hidden" : ""),
      onRefresh: (st) => (sec.style.visibility = st.progress >= 0.999 ? "hidden" : ""),
    },
  });

  // Indexraden markerar den aktiva tjänsten i passagen
  function markActive() {
    if (!pinST) return;
    const live = pinST.isActive;
    idxList.classList.toggle("live", live);
    let best = -1, bd = Infinity;
    if (live) objs.forEach((o, i) => {
      const r = o.getBoundingClientRect();
      const d = Math.abs(r.left + r.width / 2 - innerWidth / 2);
      if (d < bd && r.right > 0 && r.left < innerWidth) { bd = d; best = i; }
    });
    idx.forEach((a, i) => a.classList.toggle("on", i === best));
  }

  // Klick på ett indexnamn: rulla till objektets läge i passagen (desktop)
  idx.forEach((a, i) => a.addEventListener("click", (e) => {
    if (!DESK.matches || e.metaKey || e.ctrlKey || e.shiftKey || e.altKey || e.button) return;
    e.preventDefault();
    lenis.scrollTo(objY(objs[i]));
  }));

  // Tangentbord: fokus på en länk i railen rullar objektet till mitten, som indexet gör
  rail.addEventListener("focusin", (e) => {
    const o = e.target.closest(".rail > .obj");
    if (o) { lenis.scrollTo(objY(o), { immediate: true }); ScrollTrigger.update(); } // fokus ska synas direkt
  });
}
function objY(o) {
  return pinST.start + hold() + gsap.utils.clamp(0, overflow(), o.offsetLeft - (innerWidth - o.offsetWidth) / 2);
}

/* ── Rubriker: radmask, en gång ─────────────────────────────────────────── */
function lineReveal(el, trigger, start) {
  SplitText.create(el, {
    type: "lines", mask: "lines", linesClass: "ln", autoSplit: true, aria: "none",
    onSplit(self) {
      return gsap.from(self.lines, {
        yPercent: 145, duration: 1.05, ease: "settle", stagger: 0.08,
        scrollTrigger: { trigger, start, once: true },
      });
    },
  });
}
function flowIn(els, trigger, start, delay = 0.15) {
  gsap.from(els, { // opacity, inte autoAlpha: länkarna ska gå att tabba till innan de visats
    opacity: 0, y: 14, duration: 0.62, ease: "power2.out", stagger: 0.06, delay,
    scrollTrigger: { trigger, start, once: true },
  });
}

/* ── Akt 3 · kartläggning ───────────────────────────────────────────────── */
function kart() {
  // Bandet ligger redan under passagen; raderna reser sig medan limepanelen lyfter av det.
  const wrap = $(".sheets");
  const at = () => pinST.end - tail() + 4;
  lineReveal($(".kart .h2"), wrap, at);
  flowIn([$(".kart .kick"), $(".kart-t"), $(".kart .btn")], wrap, at);
  // den växta limebrickan landar som bandets 2×2
  gsap.from($(".kart-mos"), { scale: 1.6, opacity: 0, duration: 1.05, ease: "settle",
    scrollTrigger: { trigger: wrap, start: at, once: true } });
  // bandet driver långsamt uppåt medan det står framme (eget lager, 0,05×)
  gsap.fromTo($(".kart-in"), { y: 48 }, {
    y: -48, ease: "none",
    scrollTrigger: { trigger: wrap, start: () => pinST.end - tail(), end: () => pinST.end + 1.4 * $("#passage").offsetHeight, scrub: true, invalidateOnRefresh: true },
  });
}

/* ── Akt 4 · om: arket läggs över (CSS sticky), orden tänds grå → ink ───── */
function om() {
  const sec = $("#om");
  $$(".om .h2 > span").forEach((s) => lineReveal(s, sec, "top 72%"));
  flowIn([$(".om .kick"), $(".om-t"), $(".koncern")], sec, "top 72%");
  const words = SplitText.create($$(".ledger p"), { type: "words", aria: "none" }).words;
  gsap.fromTo(words, { color: tok("--grafit") }, {
    color: tok("--ink"), ease: "none", stagger: 0.12,
    scrollTrigger: { trigger: ".ledger", start: "top 82%", end: "bottom 48%", scrub: true },
  });
}

/* ── Akt 5 · insikter: clip-path nedifrån per objekt ────────────────────── */
function insikter() {
  const sec = $(".ins");
  lineReveal($(".ins .h2"), sec, "top 78%");
  flowIn([$(".ins-head .more")], sec, "top 78%");
  gsap.fromTo($$(".art"), { clipPath: "inset(100% 0% 0% 0%)" }, {
    clipPath: "inset(0% 0% 0% 0%)", duration: 1.05, ease: "settle", stagger: 0.08,
    scrollTrigger: { trigger: ".ins-list", start: "top 82%", once: true },
  });
}

/* ── Akt 6 · slut: brickorna lägger sig som sju små 2×2 i TJÄNSTER ──────── */
function footer() {
  const tiles = $$(".ftr-svc .mos i");
  const rnd = (i, a, b) => a + (((i * 53) % 29) / 29) * (b - a);
  gsap.fromTo(tiles, {
    x: (i) => rnd(i, 40, 420),
    y: (i) => -rnd(i * 7 + 3, 140, 420),
    rotation: (i) => rnd(i * 3 + 1, -40, 40),
    autoAlpha: 0,
  }, {
    x: 0, y: 0, rotation: 0, autoAlpha: 1, ease: "power2.out", stagger: 0.02,
    scrollTrigger: { trigger: ".ftr", start: "top bottom", end: "bottom bottom", scrub: true },
  });
}

/* ── Pekare: tilt på brickorna, magnet på primär-CTA ────────────────────── */
function pointer() {
  if (!FINE) return;
  objs.forEach((o) => {
    const m = $(".mos-lg", o);
    gsap.set(m, { transformPerspective: 700 });
    const rx = gsap.quickTo(m, "rotationX", { duration: 0.6, ease: "power3" });
    const ry = gsap.quickTo(m, "rotationY", { duration: 0.6, ease: "power3" });
    o.addEventListener("pointermove", (e) => {
      const r = m.getBoundingClientRect();
      ry(gsap.utils.clamp(-6, 6, ((e.clientX - r.left) / r.width - 0.5) * 12));
      rx(gsap.utils.clamp(-6, 6, -((e.clientY - r.top) / r.height - 0.5) * 12));
    });
    o.addEventListener("pointerleave", () => { rx(0); ry(0); });
  });
  const b = $(".magnet");
  if (!b) return;
  const qx = gsap.quickTo(b, "x", { duration: 0.6, ease: "power3" });
  const qy = gsap.quickTo(b, "y", { duration: 0.6, ease: "power3" });
  const box = b.parentElement;
  box.addEventListener("pointermove", (e) => {
    const r = b.getBoundingClientRect();
    const cx = r.left - gsap.getProperty(b, "x") + r.width / 2;
    const cy = r.top - gsap.getProperty(b, "y") + r.height / 2;
    const dx = e.clientX - cx, dy = e.clientY - cy;
    if (Math.hypot(dx, dy) > 140) { qx(0); qy(0); return; }
    qx(dx * 0.3); qy(dy * 0.35);
  });
  box.addEventListener("pointerleave", () => { qx(0); qy(0); });
}

/* ── ?preview=<akt> ─────────────────────────────────────────────────────── */
function jump(name) {
  ScrollTrigger.refresh();
  lenis.resize(); // Lenis mäter sidhöjden asynkront; pinnens spacer måste vara med innan hoppet
  const abs = (el) => el.getBoundingClientRect().top + window.scrollY;
  let y = 0;
  switch (name) {
    case "hero": y = 0; break;
    case "passage": y = pinST.start + hold(); break;
    case "passage-4": y = objY(objs[3]); break;
    case "kartlaggning": y = pinST.end; break;
    case "om": y = abs($("#om")) - H(); break;
    case "insikter": y = abs($(".ins")) - H(); break;
    case "slut": y = ScrollTrigger.maxScroll(window); break;
    default: return;
  }
  lenis.scrollTo(Math.round(y), { immediate: true, force: true });
  ScrollTrigger.update();
}
window.__jump = jump;

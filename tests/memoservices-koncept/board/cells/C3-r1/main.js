import { gsap, ScrollTrigger, SplitText, CustomEase } from "/gsap.js";
import lenis from "/smooth-scroll.js";

// C3 "Väggen": ett bricklager (28 brickor) byter formation genom hela sidan.
// moln (hero) -> vägg -> sju dyk (en 2x2 växer till rummet) -> golv -> kolumn -> rad -> index.
// En ägare per egenskap: .b = läge/storlek (master-tidslinjen), .b>i = färg/radie (master),
// .b>i transform = intro, .b>i CSS translate (--dx/--dy) = vila, #lager xPercent/yPercent = pekare,
// .lager-scroll transform = scroll-offset.

const $ = (s, r = document) => r.querySelector(s);
const $$ = (s, r = document) => [...r.querySelectorAll(s)];
const root = document.documentElement;
const tok = (n) => getComputedStyle(root).getPropertyValue(n).trim();
const KEYS = ["redovisning", "hr", "skatt", "juridik", "finans", "grc", "opex"];
const MAIN = KEYS.map((k) => tok("--t-" + k));
const ACC = KEYS.map((k) => tok("--a-" + k));
const [lr, lg, lb] = gsap.utils.splitColor(tok("--lime"));
const [ir, ig, ib] = gsap.utils.splitColor(tok("--ink"));
const EXTRA = { rod: tok("--brand-rod"), lime: tok("--lime"), kontur: `rgba(${lr},${lg},${lb},0)` };
const RING = (on) => `inset 0px 0px 0px ${on ? 1.5 : 0}px rgba(${ir},${ig},${ib},${on ? 1 : 0})`;
const N = 28;
const own = (i) => (i % 4 === 3 ? ACC : MAIN)[i >> 2];

CustomEase.create("ut", ".16,1,.3,1");

const setBanner = () => root.style.setProperty("--banner-h", $(".banner").offsetHeight + "px");
setBanner();

// mobil: lättare videofil
const video = $(".hero-video");
if (matchMedia("(max-width: 768px)").matches) {
  video.src = video.src.replace("piren-hero.mp4", "piren-hero-540.mp4");
  video.play().catch(() => {});
}

// ---------- slots som bara behövs när lagret finns ----------
const mini = (s, tom) => {
  const m = document.createElement("span");
  m.className = tom ? "mini tom" : "mini";
  m.dataset.s = s;
  for (let q = 0; q < 4; q++) {
    const i = document.createElement("i");
    if (!tom) i.dataset.q = q;
    m.append(i);
  }
  return m;
};
$$(".dyk").forEach((sec) => {
  const k = +sec.dataset.dyk, rad = $(".dyk-rad", sec);
  for (let j = 0; j < 7; j++) rad.append(mini(j, j === k));
});
const golv = $(".golv");
for (let r = 0; r < 4; r++) {
  const row = document.createElement("div");
  row.className = "golv-rad";
  for (let c = 0; c < 7; c++) {
    const i = document.createElement("i");
    i.dataset.s = c;
    i.dataset.q = r;
    if (r === 3 && ACC[c] === tok("--lime")) i.dataset.c = "kontur"; // lime på limegrund syns inte: accenten blir en ink-kontur i golvet
    row.append(i);
  }
  golv.append(row);
}
const kol = $(".om-kolumn");
[0, 1, 2, 4, 5, 6].forEach((s) => kol.append(mini(s)));
const MARK = [0, 8, 15]; // Redovisning, Skatt, Nyhet (juridikens accent = brandröd)
const insRad = $(".ins-rad");
for (let i = 0; i < N; i++) {
  if (MARK.includes(i)) continue;
  const el = document.createElement("i");
  el.dataset.s = i >> 2;
  el.dataset.q = i % 4;
  insRad.append(el);
}
$$(".markor").forEach((el, n) => {
  el.dataset.s = MARK[n] >> 2;
  el.dataset.q = MARK[n] % 4;
});

// ---------- formationerna (sidordning) ----------
const FORMS = [
  { el: $(".hero") },
  { el: $(".vagg"), order: "farg" },
  ...$$(".dyk").map((el) => ({ el, order: "dyk", k: +el.dataset.dyk, slut: 0.45 })),
  { el: $(".kart"), order: "radMal" },
  { el: $(".om"), order: "radKalla" },
  { el: $(".ins"), order: "kolKalla" },
  { el: $(".fot"), order: "kolKalla", slut: 0 },
];
FORMS.forEach((f) => {
  f.slots = new Array(N);
  f.color = new Array(N);
  f.ring = new Array(N).fill(false);
  $$("[data-q]", f.el).forEach((el) => {
    const sEl = el.dataset.s != null ? el : el.closest("[data-s]");
    const i = +sEl.dataset.s * 4 + +el.dataset.q;
    f.slots[i] = el;
    f.color[i] = el.dataset.c ? EXTRA[el.dataset.c] : own(i);
    f.ring[i] = el.dataset.c === "kontur";
  });
});

// ---------- lagret ----------
const lager = $("#lager");
const scr = document.createElement("div");
scr.className = "lager-scroll";
lager.append(scr);
const B = [], I = [];
for (let i = 0; i < N; i++) {
  const b = document.createElement("div");
  const c = document.createElement("i");
  b.className = "b";
  b.append(c);
  scr.append(b);
  B.push(b);
  I.push(c);
}
root.classList.add("lager-on");

const rect = (el) => {
  const r = el.getBoundingClientRect();
  return { x: r.left, y: r.top + scrollY, w: r.width, h: r.height };
};
const rad = (r) => Math.min((Math.min(r.w, r.h) * 10) / 51, r.w > 300 ? 28 : Infinity); // fält: tak 28 px

// Dyk: utgående grupp krymper 0-60 % av fönstret, inkommande växer 30-100 % (överlappar, inget tomt papper).
const UT = [0, 0.6], IN = [0.3, 1];
const L = (a, b, t) => a + (b - a) * t;
// gruppens rutnät ur fyra rutor [TL, TR, BL, BR]: rektangel, sömmar och delningar
function grid(q) {
  const [a, b, c] = q;
  const sx = b.x - (a.x + a.w), sy = c.y - (a.y + a.h);
  const w = b.x + b.w - a.x, h = c.y + c.h - a.y;
  return { x: a.x, y: a.y, w, h, sx, sy, cx: a.w / (w - sx), cy: a.h / (h - sy) };
}
// q i [0,1] så att gruppens yta har gått andelen `andel` från startyta till slutyta
function qForArea(g0, g1, andel) {
  const A = L(g0.w * g0.h, g1.w * g1.h, andel);
  const dw = g1.w - g0.w, dh = g1.h - g0.h, a = dw * dh, b = g0.w * dh + g0.h * dw, c = g0.w * g0.h - A;
  if (Math.abs(a) < 1e-9) return b ? gsap.utils.clamp(0, 1, -c / b) : andel;
  const r = Math.sqrt(Math.max(0, b * b - 4 * a * c));
  const r1 = (-b + r) / (2 * a), r2 = (-b - r) / (2 * a);
  return gsap.utils.clamp(0, 1, r1 >= -1e-6 && r1 <= 1 + 1e-6 ? r1 : r2);
}
// de fyra brickorna läggs i gruppens rektangel: kan aldrig överlappa, rummet växer som en helhet
function groupRects(g0, g1, q) {
  const x = L(g0.x, g1.x, q), y = L(g0.y, g1.y, q), w = L(g0.w, g1.w, q), h = L(g0.h, g1.h, q);
  const sx = L(g0.sx, g1.sx, q), sy = L(g0.sy, g1.sy, q);
  const lw = (w - sx) * L(g0.cx, g1.cx, q), th = (h - sy) * L(g0.cy, g1.cy, q);
  return [
    { x, y, w: lw, h: th }, { x: x + lw + sx, y, w: w - sx - lw, h: th },
    { x, y: y + th + sy, w: lw, h: h - sy - th }, { x: x + lw + sx, y: y + th + sy, w: w - sx - lw, h: h - sy - th },
  ];
}
const KURVA = { ut: (v) => v, in: (v) => 1 - (1 - v) ** 3 }; // ytandel över gruppens del av fönstret
function gruppLage(G, v) {
  const q = qForArea(G.g0, G.g1, KURVA[G.typ](v));
  return { q, rs: groupRects(G.g0, G.g1, q) };
}
function placeGroup(G, v) {
  const { q, rs } = gruppLage(G, v);
  rs.forEach((r, j) => {
    // stora fält ligger under de små brickorna (indexraden syns alltid ovanpå rummet)
    gsap.set(B[G.ids[j]], { x: r.x, y: r.y, width: r.w, height: r.h, zIndex: r.w * r.h > 40000 ? 0 : 1 });
    gsap.set(I[G.ids[j]], { borderRadius: rad(r) });
  });
  if (G.text) G.text.style.opacity = gsap.utils.clamp(0, 1, (L(G.g0.w, G.g1.w, q) * L(G.g0.h, G.g1.h, q)) / (G.g0.w * G.g0.h));
}

// i vilken ordning brickorna lämnar en formation: färg för färg, eller rad för rad. Aldrig slump.
function times(f, R) {
  const F = FORMS[f], P = FORMS[f - 1], out = new Array(N);
  if (F.order === "farg") {
    for (let i = 0; i < N; i++) {
      const t0 = (i >> 2) * 0.07 + (i % 4) * 0.02;
      out[i] = [t0, t0 + 0.5];
    }
  } else if (F.order === "dyk") {
    const k = F.k, p = P.order === "dyk" ? P.k : -1;
    let j = 0;
    for (let s = 0; s < 7; s++) {
      for (let q = 0; q < 4; q++) {
        const i = s * 4 + q;
        // utgående och inkommande 2x2 flyttas som grupper (GRUPP nedan); raden glider hela fönstret
        if (s === p) out[i] = UT;
        else if (s === k) out[i] = IN;
        else out[i] = [j * 0.03, 0.85 + j * 0.03];
      }
      if (s !== k && s !== p) j++;
    }
  } else {
    const src = F.order === "radMal" ? R[f] : R[f - 1];
    const key = F.order === "kolKalla" ? (i) => [src[i].x, src[i].y] : (i) => [src[i].y, src[i].x];
    const idx = [...Array(N).keys()].sort((a, b) => {
      const A = key(a), Bk = key(b);
      return A[0] - Bk[0] || A[1] - Bk[1];
    });
    idx.forEach((i, r) => {
      const t0 = (r / (N - 1)) * 0.45;
      out[i] = [t0, t0 + 0.55];
    });
  }
  return out;
}

const dykText = $$(".dyk-text");
const tl = gsap.timeline({ paused: true });
let WIN = [], AMP = [], VIS = [], REV = [];
function build() {
  tl.clear();
  const vh = innerHeight, max = ScrollTrigger.maxScroll(window);
  const clamp = gsap.utils.clamp(0, max);
  const R = FORMS.map((f) => f.slots.map(rect));
  AMP = R.map((rs) => rs.map((r) => (Math.max(r.w, r.h) > 120 ? 0.8 : 4)));
  VIS = R.map((rs) => rs.map((r) => [r.y - 10, r.y + r.h + 10]));
  for (let i = 0; i < N; i++) {
    const a = R[0][i];
    gsap.set(B[i], { x: a.x, y: a.y, width: a.w, height: a.h, zIndex: 1 });
    gsap.set(I[i], { borderRadius: rad(a), backgroundColor: FORMS[0].color[i], boxShadow: RING(false) });
  }
  WIN = [];
  let prev = 0;
  for (let f = 1; f < FORMS.length; f++) {
    const top = FORMS[f].el.getBoundingClientRect().top + scrollY;
    let s0 = Math.max(clamp(top - vh), prev);
    let s1 = Math.max(clamp(top - vh * (FORMS[f].slut ?? 0.25)), s0 + 1);
    if (f === FORMS.length - 1) s1 = Math.max(Math.min(s1, max - vh * 0.1), s0 + 1); // Lenis stannar några px före max: sista brickan ska hinna landa
    prev = s1;
    WIN.push([s0, s1]);
    const d = s1 - s0, T = times(f, R), F = FORMS[f], P = FORMS[f - 1];
    const ids = (s) => [0, 1, 2, 3].map((q) => s * 4 + q);
    const grupper = [];
    if (F.order === "dyk") {
      if (P.order === "dyk") grupper.push({ typ: "ut", s: P.k, text: dykText[P.k], span: UT });
      grupper.push({ typ: "in", s: F.k, span: IN });
    }
    const iGrupp = new Set();
    for (const G of grupper) {
      G.ids = ids(G.s);
      G.ids.forEach((i) => iGrupp.add(i));
      G.g0 = grid(G.ids.map((i) => R[f - 1][i]));
      G.g1 = grid(G.ids.map((i) => R[f][i]));
      const proxy = { v: 0 };
      tl.fromTo(proxy, { v: 0 }, { v: 1, ease: "none", duration: (G.span[1] - G.span[0]) * d, immediateRender: false,
        onUpdate: () => placeGroup(G, proxy.v) }, s0 + G.span[0] * d);
      if (G.typ === "in") {
        // dyktexten visas när inkommande fält täcker 90 % av sin slutyta
        const full = G.g1.w * G.g1.h;
        let v = 0;
        while (v < 1) {
          const { q } = gruppLage(G, v);
          if (L(G.g0.w, G.g1.w, q) * L(G.g0.h, G.g1.h, q) >= 0.9 * full) break;
          v += 0.005;
        }
        REV[F.k] = s0 + (G.span[0] + v * (G.span[1] - G.span[0])) * d;
      }
    }
    // sista dyket mot golvet: texten tonar ut med fältets yta (brickorna glider var för sig dit)
    if (F.order !== "dyk" && P.order === "dyk") {
      const ut = ids(P.k), full = ut.reduce((t, i) => t + R[f - 1][i].w * R[f - 1][i].h, 0), proxy = { v: 0 }, text = dykText[P.k];
      tl.fromTo(proxy, { v: 0 }, { v: 1, ease: "none", duration: d, immediateRender: false, onUpdate: () => {
        let area = 0;
        for (const i of ut) {
          const a = R[f - 1][i], b = R[f][i], [t0, t1] = T[i], u = gsap.utils.clamp(0, 1, (proxy.v - t0) / (t1 - t0));
          area += L(a.w, b.w, u) * L(a.h, b.h, u);
        }
        text.style.opacity = Math.min(1, area / full);
      } }, s0);
    }
    for (let i = 0; i < N; i++) {
      const a = R[f - 1][i], b = R[f][i], [t0, t1] = T[i];
      const at = s0 + t0 * d, dur = (t1 - t0) * d;
      const ringA = FORMS[f - 1].ring[i], ringB = FORMS[f].ring[i];
      if (ringA || ringB) tl.fromTo(I[i], { boxShadow: RING(ringA) }, { boxShadow: RING(ringB), ease: "none", duration: dur, immediateRender: false }, at);
      if (iGrupp.has(i)) continue; // läge, storlek och radie ägs av gruppens proxy i detta fönster
      tl.fromTo(B[i], { x: a.x, y: a.y, width: a.w, height: a.h },
        { x: b.x, y: b.y, width: b.w, height: b.h, ease: "none", duration: dur, immediateRender: false }, at);
      tl.fromTo(I[i], { borderRadius: rad(a), backgroundColor: FORMS[f - 1].color[i] },
        { borderRadius: rad(b), backgroundColor: FORMS[f].color[i], ease: "none", duration: dur, immediateRender: false }, at);
    }
  }
  tl.set({}, {}, Math.max(max, prev));
}
build();

// ---------- vila (±4 px sinus) och scroll-offset ----------
const PH = Array.from({ length: N }, (_, i) => ({ p: 6 + (((i * 7) % 13) / 12) * 3, a: i * 2.399, b: i * 1.618 + 1 }));
const amp = new Array(N).fill(4);
const dykIn = $$(".dyk").map((sec) => ({ els: $$("[data-in]", sec), head: $(".dyk-namn", sec), done: false }));
function visaDyk(k, direkt) {
  const d = dykIn[k];
  d.done = true;
  if (direkt) gsap.set(d.els, { opacity: 1, y: 0 });
  else gsap.to(d.els, { opacity: 1, y: 0, duration: 0.62, ease: "power2.out", stagger: 0.06 });
  d.head.__visa ? d.head.__visa(direkt) : (d.head.__vantar = direkt ? "direkt" : "spela");
}
gsap.ticker.add((t) => {
  const y = scrollY;
  // dyktexten visas först när inkommande fält täcker 90 % av sin yta
  for (let k = 0; k < dykIn.length; k++) {
    if (!dykIn[k].done && REV[k] != null && y >= REV[k]) visaDyk(k, y > REV[k] + innerHeight);
  }
  scr.style.transform = `translate3d(0,${-y}px,0)`;
  let f = 0, moving = false;
  for (let k = 0; k < WIN.length; k++) {
    if (y >= WIN[k][1]) f = k + 1;
    else {
      moving = y > WIN[k][0];
      break;
    }
  }
  const target = AMP[f] || [], vis = VIS[f] || [];
  for (let i = 0; i < N; i++) {
    amp[i] += ((target[i] ?? 4) - amp[i]) * 0.04;
    if (!moving && vis[i] && (vis[i][0] > y + innerHeight || vis[i][1] < y)) continue; // utanför vyn i vila
    const w = (2 * Math.PI * t) / PH[i].p;
    I[i].style.setProperty("--dx", (amp[i] * Math.sin(w + PH[i].a)).toFixed(2) + "px");
    I[i].style.setProperty("--dy", (amp[i] * Math.cos(w * 0.83 + PH[i].b)).toFixed(2) + "px");
  }
});

// ---------- pekaren: hela lagret 0,6 % mot pekaren ----------
if (matchMedia("(hover: hover) and (pointer: fine)").matches) {
  const xTo = gsap.quickTo(lager, "xPercent", { duration: 1.2, ease: "power3" });
  const yTo = gsap.quickTo(lager, "yPercent", { duration: 1.2, ease: "power3" });
  addEventListener("pointermove", (e) => {
    xTo((e.clientX / innerWidth - 0.5) * 1.2);
    yTo((e.clientY / innerHeight - 0.5) * 1.2);
  }, { passive: true });
}

// ---------- intro (1,2 s): molnet fälls ut plan för plan, rubriken stiger ur sina masker ----------
const plane = FORMS[0].slots.map((el) => (el.classList.contains("p1") ? 0 : el.classList.contains("p2") ? 1 : 2));
const introIn = $$('[data-in="intro"]');
const h1 = $('[data-split="intro"]');
gsap.set(introIn, { opacity: 0, y: 14 });
gsap.set(h1, { opacity: 0 });
const intro = gsap.timeline({ delay: 0.1 });
intro.from(I, { scale: 0, y: 26, duration: 0.8, ease: "back.out(1.5)", stagger: (k) => plane[k] * 0.14 + (k % 4) * 0.03 + (k >> 2) * 0.012 }, 0);
intro.to(introIn, { opacity: 1, y: 0, duration: 0.62, ease: "power2.out", stagger: 0.07 }, 0.45);

// ---------- hero: videon zoomar 1 -> 1,12 medan heron lämnar (ingen pin) ----------
const hero = $(".hero"), media = $(".hero-media");
gsap.fromTo(media, { scale: 1 }, {
  scale: 1.12, ease: "none",
  scrollTrigger: {
    trigger: hero, start: 0, end: () => hero.offsetTop + hero.offsetHeight, scrub: true, invalidateOnRefresh: true,
    onToggle: (s) => {
      media.style.willChange = s.isActive ? "transform" : "";
      s.isActive ? video.play().catch(() => {}) : video.pause(); // ingen avkodning när heron är ur bild
    },
  },
});

// ---------- delad reveal: 14 px / 620 ms, en gång ----------
const inEls = $$("[data-in]").filter((el) => el.dataset.in !== "intro" && !el.closest(".dyk"));
gsap.set($$(".dyk [data-in]"), { opacity: 0, y: 14 });
gsap.set(inEls, { opacity: 0, y: 14 });
ScrollTrigger.batch(inEls, {
  start: "top 88%", end: "max", once: true,
  onEnter: (els) => {
    // ett hopp förbi (preview, ankare) visar det som redan passerat direkt; bara det i vyn tonar in
    const passed = els.filter((el) => el.getBoundingClientRect().bottom < 0);
    const rest = els.filter((el) => !passed.includes(el));
    if (passed.length) gsap.set(passed, { opacity: 1, y: 0, overwrite: true });
    if (rest.length) gsap.to(rest, { opacity: 1, y: 0, duration: 0.62, ease: "power2.out", stagger: 0.06, overwrite: true });
  },
});

// ---------- indexraden: aktiv tjänst lyser under dyken ----------
$$(".dyk").forEach((sec) => {
  const a = $(`.index a[data-ix="${sec.dataset.dyk}"]`);
  ScrollTrigger.create({ trigger: sec, start: "top 50%", end: "bottom 50%", toggleClass: { targets: a, className: "aktiv" } });
});

// ---------- master: en scrubbad tidslinje, tid = scroll i px ----------
const master = ScrollTrigger.create({
  trigger: document.body, start: "top top", end: "bottom bottom",
  scrub: true, animation: tl, invalidateOnRefresh: true,
});
ScrollTrigger.addEventListener("refreshInit", setBanner);
ScrollTrigger.addEventListener("refresh", () => {
  build();
  tl.progress(master.progress);
});

// ---------- rubriker: radmasker efter typsnitten ----------
function splitHeads() {
  $$("[data-split]").forEach((el) => {
    const isIntro = el.dataset.split === "intro";
    let done = false;
    SplitText.create(el, {
      type: "lines", mask: "lines", autoSplit: true,
      onSplit(self) {
        gsap.set(self.masks, { paddingTop: ".16em", marginTop: "-.16em", paddingBottom: ".14em", marginBottom: "-.14em" });
        if (done) return;
        gsap.set(self.lines, { yPercent: 130 });
        gsap.set(el, { opacity: 1 });
        const play = () => {
          done = true;
          if (el.getBoundingClientRect().bottom < 0) return gsap.set(self.lines, { yPercent: 0 });
          gsap.to(self.lines, { yPercent: 0, duration: 1, ease: "ut", stagger: 0.09, delay: isIntro ? 0.2 : 0 });
        };
        if (isIntro) play();
        else if (el.dataset.split === "dyk") {
          el.__visa = (direkt) => (direkt ? (done = true, gsap.set(self.lines, { yPercent: 0 })) : play());
          if (el.__vantar) el.__visa(el.__vantar === "direkt");
        } else ScrollTrigger.create({ trigger: el, start: "top 88%", end: "max", once: true, onEnter: play });
      },
    });
  });
}

// ---------- meny och undermeny ----------
const uk = $(".under-knapp"), under = $("#undermeny");
const setUnder = (open) => {
  uk.setAttribute("aria-expanded", String(open));
  under.hidden = !open;
};
uk.addEventListener("click", () => setUnder(under.hidden));
$(".har-under").addEventListener("focusout", (e) => {
  if (!e.relatedTarget || !e.currentTarget.contains(e.relatedTarget)) setUnder(false);
});
document.addEventListener("click", (e) => {
  if (!under.hidden && !e.target.closest(".har-under")) setUnder(false);
});
const mk = $(".meny-knapp"), mm = $("#mobilmeny");
const setMeny = (open) => {
  mk.setAttribute("aria-expanded", String(open));
  mm.hidden = !open;
  mk.textContent = open ? mk.dataset.close : mk.dataset.open;
  open ? lenis.stop() : lenis.start();
};
mk.addEventListener("click", () => setMeny(mm.hidden));
mm.addEventListener("click", (e) => {
  if (e.target.closest("a")) setMeny(false);
});
document.addEventListener("keydown", (e) => {
  if (e.key !== "Escape") return;
  if (!under.hidden) {
    setUnder(false);
    uk.focus();
  }
  if (!mm.hidden) {
    setMeny(false);
    mk.focus();
  }
});

// ---------- ?preview=<akt> ----------
const PREVIEW = {
  hero: null, vagg: ".vagg", "dyk-1": '.dyk[data-dyk="0"]', "dyk-4": '.dyk[data-dyk="3"]',
  kartlaggning: ".kart", om: ".om", insikter: ".ins", slut: "max",
};
const pv = new URLSearchParams(location.search).get("preview");

Promise.race([document.fonts.ready, new Promise((r) => setTimeout(r, 1500))]).then(() => {
  splitHeads();
  ScrollTrigger.refresh();
  if (!pv || !(pv in PREVIEW)) return;
  const sel = PREVIEW[pv];
  if (!sel) lenis.scrollTo(0, { immediate: true });
  else if (sel === "max") lenis.scrollTo(ScrollTrigger.maxScroll(window), { immediate: true });
  else {
    const el = $(sel);
    // dyk: vilan precis innan nästa fönster börjar (sektionens botten i vyns botten)
    const off = el.classList.contains("dyk") ? -(innerHeight - el.offsetHeight) : -$(".hdr").offsetHeight;
    lenis.scrollTo(el, { immediate: true, offset: off });
  }
  ScrollTrigger.update();
});

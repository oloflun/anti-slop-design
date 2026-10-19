import { gsap, ScrollTrigger, SplitText, CustomEase } from "/gsap.js";
import lenis from "/smooth-scroll.js";

// B3 "Banden II". Ett bricklager (#lager, 28 brickor) som byter formation genom hela sidan.
// En scrubbad huvudtidslinje: tid = scroll-px. Varje övergång är ett segment i den (ease none,
// Lenis är utjämningen). Slot-element i layouten ger alla mål; inga handskrivna koordinater.
// Runda 3b: varje övergång är klar när nästa sektions topp står vid 45 % av vyn; bandbytet är
// en stegad mosaikkant (clip-path i brickans enhet) som sveper nedifrån, ingen färgtween.

const $ = (s, r = document) => r.querySelector(s);
const $$ = (s, r = document) => [...r.querySelectorAll(s)];
const root = document.documentElement;
if ("scrollRestoration" in history) history.scrollRestoration = "manual";

const css = getComputedStyle(root);
const tok = (n) => css.getPropertyValue(n).trim();
const rgba = (hex, a) => { const n = parseInt(hex.slice(1), 16); return `rgba(${(n >> 16) & 255},${(n >> 8) & 255},${n & 255},${a})`; };
const SV = [
  ["--t-redovisning", "--a-redovisning", "dark"], ["--t-hr", "--a-hr", "light"], ["--t-skatt", "--a-skatt", "dark"],
  ["--t-juridik", "--a-juridik", "dark"], ["--t-finans", "--a-finans", "light"], ["--t-grc", "--a-grc", "dark"],
  ["--t-opex", "--a-opex", "light"],
].map(([m, a, tone]) => ({ m: tok(m), a: tok(a), tone }));
const C = { paper: tok("--bakgrund"), ink: tok("--ink"), red: tok("--brand-rod"), lime: tok("--lime") };
C.paper3 = rgba(C.paper, 0.3);
const sv4 = (s, j) => (j === 3 ? SV[s].a : SV[s].m);

const chrome = $("#chrome"), bar = $(".bar"), fb = $("#fullbleed");
const setChrome = () => root.style.setProperty("--chrome", chrome.offsetHeight + "px");
setChrome();

// --- video: mobilkälla, flyttas in i lagret ---
const video = $(".fb-band video");
if (matchMedia("(max-width: 768px)").matches) {
  video.querySelector("source").src = "/tests/memoservices-koncept/assets/video/piren-hero-540.mp4";
  video.load();
}

// --- meny: Tjänster-panelen och mobilmenyn (oberoende av rörelsen) ---
const hp = $(".has-panel"), hpA = hp.querySelector(":scope > a");
let closeT = 0, quiet = false;
const setP = (o) => { clearTimeout(closeT); hp.classList.toggle("open", o); hpA.setAttribute("aria-expanded", String(o)); };
hp.addEventListener("mouseenter", () => setP(true));
hp.addEventListener("mouseleave", () => { closeT = setTimeout(() => setP(false), 180); });
hp.addEventListener("focusin", () => { if (!quiet) setP(true); quiet = false; });
hp.addEventListener("focusout", (e) => { if (!hp.contains(e.relatedTarget)) setP(false); });
const mb = $(".menu-btn"), mob = $("#mobilmeny");
mob.setAttribute("data-lenis-prevent", "");
const setM = (o) => { mb.setAttribute("aria-expanded", String(o)); mob.hidden = !o; o ? lenis.stop() : lenis.start(); };
mb.addEventListener("click", () => { const o = mb.getAttribute("aria-expanded") !== "true"; setM(o); if (o) mob.querySelector("a").focus(); });
addEventListener("keydown", (e) => {
  if (e.key !== "Escape") return;
  if (!mob.hidden) { setM(false); mb.focus(); }
  if (hp.classList.contains("open")) { setP(false); quiet = true; hpA.focus(); }
});

await document.fonts.ready;
setChrome();
root.classList.add("lager");

// --- lagret: 28 brickor (0–3 blir fälten, 4–27 de små) + videons ram ---
const lager = $("#lager");
const mk = (cls, parent) => { const d = document.createElement("div"); d.className = cls; parent && parent.append(d); return d; };
const G = { F: mk("g g-f", lager), S: mk("g g-s", lager) };
const bricks = Array.from({ length: 28 }, (_, i) => {
  const el = mk("b", i < 4 ? G.F : G.S), bi = mk("bi", el);
  // fälten har ett svep-lager: nästa bandfärg kommer in bakom en stegad kant
  const bw = i < 4 ? mk("bw", bi) : null;
  return { el, bi, bw, p1: 6 + ((i * 7) % 31) / 10, p2: 6.5 + ((i * 5) % 25) / 10, ph: i * 2.39996 };
});
const vidF = mk("vid", G.F);
vidF.append(video);
video.play().catch(() => {});
const mosaicCells = $$(".hero-mosaic i");
const startColor = mosaicCells.map((c) => getComputedStyle(c).backgroundColor);
const tj = $("#tjanster"), stage = $(".tj-stage"), blocks = $$(".tj-blocks .band");
const HIDE = "inset(100% 0% 0% 0%)";

// HTML-mosaiken finns kvar utan JS; lagret tar över här
gsap.set([...mosaicCells, ...$$(".om-ledger .mk"), ...$$(".ins-ledger .mk"), ...$$(".fm2").slice(0, 6), $(".icon2")], { visibility: "hidden" });

// --- heron -> full bleed: den enda pinnen ---
const chromeH = () => chrome.offsetHeight;
const pinST = ScrollTrigger.create({
  trigger: fb, pin: true, start: () => "top " + chromeH() + "px",
  end: (self) => self.start + 2 * innerHeight, invalidateOnRefresh: true,
});

// --- mätning ---
function docTop(el, r = el.getBoundingClientRect()) {
  const sp = fb.parentElement;
  if (fb.contains(el) && sp.classList.contains("pin-spacer"))
    return r.top - fb.getBoundingClientRect().top + sp.getBoundingClientRect().top + scrollY;
  return r.top + scrollY;
}
const D = (el) => { const r = el.getBoundingClientRect(); return { x: r.left, y: docTop(el, r), w: r.width, h: r.height }; };
const V = (el) => { const r = el.getBoundingClientRect(); return { x: r.left, y: r.top, w: r.width, h: r.height }; };
function measure() {
  const top = (sel) => docTop($(sel));
  const sr = stage.getBoundingClientRect(), br = blocks[0].getBoundingClientRect();
  return {
    vw: innerWidth, vh: innerHeight, max: ScrollTrigger.maxScroll(window),
    pinA: pinST.start, pinB: pinST.end,
    svc: top("#tjanster"), sp: $$(".tj-sp i").map((e) => docTop(e)), kl: top("#kartlaggning"),
    om: top("#om"), ins: top("#insikter"), foot: top("#sidfot"),
    mosaic: mosaicCells.map(D), video: D($(".fb-band")),
    fields: $$(".fx-fields > i").map(V), raster: $$(".fx-raster i").map(V),
    rasterCols: getComputedStyle($(".fx-raster")).gridTemplateColumns.split(" ").length, edges: $$(".fx-edges i").map(V),
    boff: { x: br.left - sr.left, y: br.top - sr.top },
    klF: $$(".kl-f").map(D), klRows: $$(".kl-rows i").map(D),
    omMk: $$(".om-ledger .mk").map(D), omRow: $$(".row20 i").map(D),
    insMk: $$(".ins-ledger .mk").map(D), insRow: $$(".row21 i").map(D),
    icon: $$(".icon2 i").map(D), foot2: $$(".fm2").slice(0, 6).flatMap((m) => [...m.children].map(D)),
  };
}

// den stegade kanten: kolumner i brickans enhet över hela rummet, fyra trappnivåer i mönster
function wipeOf(g) {
  const fs = g.fields;
  const X0 = Math.min(...fs.map((f) => f.x)), X1 = Math.max(...fs.map((f) => f.x + f.w));
  const Y0 = Math.min(...fs.map((f) => f.y)), Y1 = Math.max(...fs.map((f) => f.y + f.h));
  const n = Math.max(4, Math.round((X1 - X0) / 56)), u = (X1 - X0) / n, pat = [0, 2, 1, 3];
  // p = 0: hela kanten under rummet; p = 1: hela kanten ovanför. Linjärt i p, så scrub ger jämn rörelse.
  const edge = (p) => Array.from({ length: n }, (_, i) => Y1 + u * pat[i % 4] - p * (Y1 - Y0 + 3 * u));
  const poly = (p, ox, oy, below) => {
    const e = edge(p), far = below ? 1e4 : -1e4, pts = [[X0 - 60, far]];
    e.forEach((y, i) => pts.push([i === 0 ? X0 - 60 : X0 + i * u, y], [i === n - 1 ? X1 + 60 : X0 + (i + 1) * u, y]));
    pts.push([X1 + 60, far]);
    return "polygon(" + pts.map(([x, y]) => `${(x - ox).toFixed(1)}px ${(y - oy).toFixed(1)}px`).join(", ") + ")";
  };
  const bx = fs[0].x + g.boff.x, by = fs[0].y + g.boff.y;
  const block = (p, below) => poly(p, bx, by, below);
  // fälten: samma kant som kolumner (en div per brickenhet) som bara flyttas med transform
  const cols = (j) => ({ n, left: (i) => X0 + i * u - fs[j].x, w: u + 1, h: Y1 - Y0 + 4 * u + 10 });
  const colY = (j, p) => edge(p).map((y) => y - fs[j].y);
  return { block, cols, colY, n };
}
// bygger kolumnerna i varje fälts svep-lager när geometrin ändrats
function buildCols() {
  for (let j = 0; j < 4; j++) {
    const bw = bricks[j].bw, c = P.wipe.cols(j);
    bw.replaceChildren(...Array.from({ length: c.n }, (_, i) => {
      const d = document.createElement("i"); d.className = "wc";
      d.style.cssText = `left:${c.left(i).toFixed(1)}px;width:${c.w.toFixed(1)}px;height:${c.h.toFixed(0)}px`;
      return d;
    }));
  }
}

// --- plan: fönster, viloperioder, formationer ---
const rad = (r) => Math.min(24, (Math.min(r.w, r.h) * 10) / 51);
const DONE = 0.45; // en övergång är klar när nästa sektions topp står vid 45 % av vyn
let P = null;
function plan(g) {
  const { vh } = g;
  let prev = 0;
  const win = (a, b) => { a = Math.max(a, prev); b = Math.max(b, a + 1); prev = b; return [a, b]; };
  const into = (t) => win(t - vh, t - DONE * vh);
  const T1 = win(g.pinA, g.pinB);
  const T2 = into(g.svc);
  const T3 = g.sp.slice(1).map(into);          // band 2–7 + "flera områden"
  const T4 = into(g.kl);
  const T5 = into(g.om);
  const T6 = into(g.ins);
  const T7 = win(g.foot - vh, Math.max(g.max, prev + 1));
  const trans = [T1, T2, ...T3, T4, T5, T6, T7];
  const kinds = ["T1", "T2", "W", "W", "W", "W", "W", "W", "WF", "T4", "T5", "T6", "T7"];
  const sw = kinds.map((k) => (k[0] === "W" ? 0.7 : 0.5)); // där ton och nav byter
  // om/insikter: de små är framme innan sektionens rubrik når vyn (raden ligger under rubriken),
  // och följer sedan dokumentet, så att ingen bricka korsar en rubrik som läses
  const part = (T, f) => [T[0], T[0] + f * (T[1] - T[0])];
  const T5S = part(T5, 0.45), T6S = part(T6, 0.3);
  // viloperioder där en grupp följer dokumentet (brickorna står still mot texten)
  const rests = [
    { a: 0, b: T1[0], g: ["F", "S"] }, { a: T4[1], b: T5[0], g: ["F", "S"] },
    { a: T5S[1], b: T6[0], g: ["S"] }, { a: T6S[1], b: T7[0], g: ["S"] },
  ];
  const W = (grp, s) => rests.reduce((w, r) => (r.g.includes(grp) ? w - Math.min(Math.max(s - r.a, 0), r.b - r.a) : w), 0);

  const fx = (r) => ({ r, doc: false }), dc = (r) => ({ r, doc: true });
  const full = { x: 0, y: 0, w: g.vw, h: g.vh };
  const rIdx = (col, row) => (g.rasterCols === 7 ? row * 7 + col : col * 4 + row);
  const st = [];
  // S0 hero-mosaiken
  st.push({ s: 0, hdr: C.paper, tone: "light",
    F: [0, 1, 2, 3].map((j) => ({ ...dc(g.mosaic[j]), c: startColor[j] })),
    S: g.edges.map((_, k) => ({ ...dc(g.mosaic[4 + k]), c: startColor[4 + k] })),
    V: { ...dc(g.video), o: 1 } });
  // S1 full bleed: fyra fält bakom videon, 24 små ute vid kanterna
  st.push({ s: T1[1], hdr: SV[0].m, tone: "dark",
    F: [0, 1, 2, 3].map((j) => ({ ...fx(g.fields[j]), c: sv4(0, j) })),
    S: g.edges.map((r, k) => ({ ...fx(r), c: startColor[4 + k] })),
    V: { ...fx(full), o: 1, rr: 0 } });
  // S2..S8 banden: fälten bär tjänsten, rastret står i accentfältet med den aktiva kolumnen tom
  const band = (b, s) => {
    const cols = [0, 1, 2, 3, 4, 5, 6].filter((c) => c !== b);
    return { s, hdr: SV[b].m, tone: SV[b].tone,
      F: [0, 1, 2, 3].map((j) => ({ ...fx(g.fields[j]), c: sv4(b, j) })),
      S: g.edges.map((_, k) => ({ ...fx(g.raster[rIdx(cols[k >> 2], k % 4)]), c: C.paper3 })),
      V: { ...fx(g.fields[0]), o: 0 } };
  };
  for (let b = 0; b < 7; b++) st.push(band(b, (b === 0 ? T2 : T3[b - 1])[1]));
  // S9 "flera områden": samma rum som sista bandet, men rastrets 24 tänds i sina egna tjänstefärger
  const flera = band(6, T3[6][1]);
  flera.S = flera.S.map((e, k) => ({ ...e, c: sv4(k >> 2, k % 4) }));
  st.push(flera);
  // S10 kartläggning: rummet blir lime, accentfältet ink med sex 2x2 i två rader
  st.push({ s: T4[1], hdr: C.lime, tone: "light",
    F: [0, 1, 2, 3].map((j) => ({ ...dc(g.klF[j]), c: j === 3 ? C.ink : C.lime })),
    S: g.edges.map((_, k) => { const s = k >> 2, j = k % 4; return { ...dc(g.klRows[(j >> 1) * 12 + s * 2 + (j & 1)]), c: sv4(s, j) }; }),
    V: { ...fx(g.fields[0]), o: 0 } });
  // S11 om: fälten tonar till papper; fyra markörer + en rad
  const omC = [C.red, C.red, C.red, C.lime];
  st.push({ s: T5[1], sS: T5S[1], hdr: C.paper, tone: "light",
    F: [0, 1, 2, 3].map((j) => ({ ...fx(g.fields[j]), c: C.paper })),
    S: g.edges.map((_, k) => (k < 4 ? { ...dc(g.omMk[k]), c: omC[k] } : { ...dc(g.omRow[k - 4]), c: SV[(k - 4) % 7].m })),
    V: { ...fx(g.fields[0]), o: 0 } });
  // S12 insikter: tre markörer i kategorins färg + en rad
  const insC = [SV[0].m, SV[2].m, C.red];
  st.push({ s: T6[1], sS: T6S[1], hdr: C.paper, tone: "light",
    F: [0, 1, 2, 3].map((j) => ({ ...fx(g.fields[j]), c: C.paper })),
    S: g.edges.map((_, k) => { if (k < 3) return { ...dc(g.insMk[k]), c: insC[k] }; const q = k - 3; return { ...dc(g.insRow[q]), c: q % 3 === 2 ? SV[(q / 3) | 0].a : SV[(q / 3) | 0].m }; }),
    V: { ...fx(g.fields[0]), o: 0 } });
  // S13 sidfot: fälten krymper till app-ikonen, de små blir sex 2x2 i TJÄNSTER
  st.push({ s: T7[1], hdr: C.paper, tone: "light",
    F: [0, 1, 2, 3].map((j) => ({ ...dc(g.icon[j]), c: j === 3 ? C.lime : C.paper })),
    S: g.edges.map((_, k) => ({ ...dc(g.foot2[k]), c: sv4(k >> 2, k % 4) })),
    V: { ...fx(g.fields[0]), o: 0 } });

  // till lagrets koordinater (gruppens wrapper bär förankringen)
  const ws = (e, grp, s) => ({ x: e.r.x, y: (e.doc ? e.r.y - s : e.r.y) - W(grp, s), w: e.r.w, h: e.r.h, c: e.c, rad: e.rr ?? rad(e.r) });
  for (const S of st) {
    S.Fw = S.F.map((e) => ws(e, "F", S.s));
    S.Sw = S.S.map((e) => ws(e, "S", S.sS ?? S.s));
    S.Vw = { ...ws(S.V, "F", S.s), o: S.V.o };
    S.amp = [...S.Fw, ...S.Sw].map((e) => Math.min(4, 0.1 * Math.min(e.w, e.h)));
  }
  return { g, trans, kinds, sw, rests, W, st, wipe: wipeOf(g), T1, T2, T7 };
}

// --- huvudtidslinjen ---
const tl = gsap.timeline({ paused: true, defaults: { ease: "none" } });
let masterST = null;
const geo = (e) => ({ x: e.x, y: e.y, width: e.w, height: e.h });
const paint = (e) => ({ backgroundColor: e.c, borderRadius: e.rad });
const same = (a, b) => a.x === b.x && a.y === b.y && a.w === b.w && a.h === b.h && a.c === b.c;
// [start, längd] som andel av fönstret; allt slutar senast vid 1 (= nästa topp vid 45 %)
const ORDER = {
  T1: { F: (j) => [0.15 + 0.05 * j, 0.4], S: (k) => [0.25 * (k / 23), 0.3], V: [0, 0.55], o: null, H: [0.3, 0.25] },
  T2: { F: (j) => [0, 0.6], S: (k) => [0.3 * (k / 23), 0.6], V: [0, 0.7], o: [0.15, 0.27], H: [0, 0.6] },
  W: { S: (k) => [0.1 * (k % 4), 0.5] },
  T4: { F: (j) => [0.06 * j, 0.7], S: (k) => [0.3 * (k / 23), 0.6], V: [0, 1], o: null, H: [0.1, 0.6] },
  // om: fältens färg till papper är klar vid 55 % av vyn (0,82 av fönstret)
  T5: { F: (j) => (j === 3 ? [0, 0.4] : [0.04 * j, 0.66]), S: (k) => [0.15 * (k / 23), 0.3], V: [0, 1], o: null, H: [0, 0.6] },
  T6: { F: (j) => [0, 1], S: (k) => [0.1 * (k / 23), 0.2], V: [0, 1], o: null, H: [0, 0.6] },
  T7: { F: (j) => [0.1 + 0.06 * j, 0.7], S: (k) => [0.25 * (k / 23), 0.6], V: [0, 1], o: null, H: [0, 0.6] },
};
function segment(i, A, B, [a, b], kind) {
  const O = ORDER[kind[0] === "W" ? "W" : kind], L = b - a, at = (d) => a + L * d;
  const move = (pa, pb, brick, d, du) => {
    tl.fromTo(brick.el, geo(pa), { ...geo(pb), duration: L * du, immediateRender: false }, at(d));
    tl.fromTo(brick.bi, paint(pa), { ...paint(pb), duration: L * du, immediateRender: false }, at(d));
  };
  A.Sw.forEach((pa, k) => { const pb = B.Sw[k]; if (!same(pa, pb)) move(pa, pb, bricks[4 + k], ...O.S(k)); });
  if (kind[0] === "W") {
    // bandbyte: nästa färg stiger nedifrån bakom en stegad kant, i fälten och i bandtexten samtidigt
    // (polygonen skrivs direkt från ett scrubbat p; GSAP:s strängtolkning av clip-path tappar polygonpunkter)
    const k = i - 1, inB = blocks[k], outB = blocks[k - 1], wf = kind === "W", o = { p: 0 };
    if (wf) A.Fw.forEach((pa, j) => { tl.set(bricks[j].bw, { color: B.Fw[j].c }, a); tl.set(bricks[j].bi, { backgroundColor: B.Fw[j].c }, b); });
    const draw = () => {
      const p = o.p, mid = p > 0 && p < 1;
      if (wf) for (let j = 0; j < 4; j++) {
        const bw = bricks[j].bw;
        bw.style.visibility = mid ? "visible" : "hidden";
        if (mid) { const ys = P.wipe.colY(j, p); [...bw.children].forEach((c, i) => { c.style.transform = `translate3d(0,${ys[i].toFixed(1)}px,0)`; }); }
      }
      inB.style.clipPath = p >= 1 ? "none" : p <= 0 ? HIDE : P.wipe.block(p, true);
      outB.style.clipPath = p <= 0 ? "none" : p >= 1 ? HIDE : P.wipe.block(p, false);
    };
    tl.fromTo(o, { p: 0 }, { p: 1, duration: L, immediateRender: false, onUpdate: draw }, a);
    if (A.hdr !== B.hdr) tl.set(bar, { backgroundColor: B.hdr }, at(0.7));
    return;
  }
  A.Fw.forEach((pa, j) => { const pb = B.Fw[j]; if (!same(pa, pb)) move(pa, pb, bricks[j], ...O.F(j)); });
  // scenen (rail + bandtext) finns bara medan rummet bär tjänsterna: in när videon har tonat, ut när fälten lämnar
  // (opacitet, inte visibility: länkarna i scenen ska gå att nå med tangentbordet hela tiden)
  if (kind === "T2") tl.fromTo(stage, { opacity: 0 }, { opacity: 1, duration: L * 0.2, immediateRender: false }, at(0.42));
  if (kind === "T4") tl.fromTo(stage, { opacity: 1 }, { opacity: 0, duration: L * 0.2, immediateRender: false }, a);
  if (!same(A.Vw, B.Vw)) tl.fromTo(vidF, { ...geo(A.Vw), borderRadius: A.Vw.rad }, { ...geo(B.Vw), borderRadius: B.Vw.rad, duration: L * O.V[1], immediateRender: false }, at(O.V[0]));
  if (A.Vw.o !== B.Vw.o) tl.fromTo(video, { opacity: A.Vw.o }, { opacity: B.Vw.o, duration: L * O.o[1], immediateRender: false }, at(O.o[0]));
  if (A.hdr !== B.hdr) tl.fromTo(bar, { backgroundColor: A.hdr }, { backgroundColor: B.hdr, duration: L * O.H[1], immediateRender: false }, at(O.H[0]));
}
function applyState(S) {
  bricks.forEach((b, i) => {
    const e = i < 4 ? S.Fw[i] : S.Sw[i - 4];
    gsap.set(b.el, geo(e)); gsap.set(b.bi, paint(e));
    if (b.bw) b.bw.style.visibility = "hidden";
  });
  blocks.forEach((bl, k) => { bl.style.clipPath = k === 0 ? "none" : HIDE; });
  gsap.set(stage, { opacity: 0 });
  gsap.set(vidF, { ...geo(S.Vw), borderRadius: S.Vw.rad });
  gsap.set(video, { opacity: S.Vw.o });
  gsap.set(bar, { backgroundColor: S.hdr });
  gsap.set([G.F, G.S], { y: 0 });
}
function build(g) {
  P = plan(g);
  buildCols();
  tl.clear();
  applyState(P.st[0]);
  for (const r of P.rests) {
    if (r.b - r.a < 1) continue;
    for (const grp of r.g) tl.fromTo(G[grp], { y: P.W(grp, r.a) }, { y: P.W(grp, r.b), duration: r.b - r.a, immediateRender: false }, r.a);
  }
  P.trans.forEach((w, i) => segment(i, P.st[i], P.st[i + 1], w, P.kinds[i]));
  tl.set({}, {}, g.max);
  tl.progress(0).progress(masterST ? masterST.progress : 0);
}
let lastKey = JSON.stringify(measure());
build(JSON.parse(lastKey));
masterST = ScrollTrigger.create({ animation: tl, start: 0, end: "max", scrub: true, invalidateOnRefresh: true });
ScrollTrigger.addEventListener("refreshInit", setChrome);
ScrollTrigger.addEventListener("refresh", () => {
  const key = JSON.stringify(measure());
  if (key === lastKey) return;
  lastKey = key;
  build(JSON.parse(key));
});
ScrollTrigger.config({ ignoreMobileResize: true });

// --- intro (1,2 s): brickorna lägger sig rad för rad, och de stannar sidan ut ---
const introOrder = bricks.map((b, i) => [b.bi, P.st[0][i < 4 ? "Fw" : "Sw"][i < 4 ? i : i - 4]])
  .sort((a, b) => a[1].y - b[1].y || a[1].x - b[1].x).map((p) => p[0]);
gsap.from(introOrder, { scale: 0.3, autoAlpha: 0, duration: 0.7, ease: "power3.out", stagger: 0.018, delay: 0.1 });
gsap.from(vidF, { autoAlpha: 0, duration: 0.9, ease: "power2.out", delay: 0.15 });

// --- rubriker: radmasker, en gång ---
$$("[data-split]").forEach((el) => {
  let entered = false, done = false, cur = null;
  SplitText.create(el, {
    type: "lines", mask: "lines", linesClass: "sl", aria: "none", autoSplit: true,
    onSplit(self) {
      if (done) return;
      cur = gsap.from(self.lines, { yPercent: 130, duration: 1.05, ease: "power3.out", stagger: 0.09, paused: !entered, onComplete: () => { done = true; } });
      return cur;
    },
  });
  ScrollTrigger.create({ trigger: el, start: "top 88%", once: true, onEnter: () => { entered = true; cur && cur.play(); } });
});

// --- delad reveal: 14 px / 620 ms, en gång. Ledgerns radtext tidigare (92 %) så att den finns när markören landar ---
const revealBatch = (els, start) => {
  gsap.set(els, { autoAlpha: 0, y: 14 });
  ScrollTrigger.batch(els, {
    start, once: true,
    onEnter: (hit) => {
      // ett hopp tänder många på en gång: de som redan passerat sätts direkt, resten staggas kort
      const vis = hit.filter((e) => e.getBoundingClientRect().bottom > 0);
      gsap.set(hit.filter((e) => !vis.includes(e)), { autoAlpha: 1, y: 0 });
      gsap.to(vis, { autoAlpha: 1, y: 0, duration: 0.62, ease: "power2.out", stagger: Math.min(0.06, 0.36 / vis.length), overwrite: true });
    },
  });
};
const ledgerR = $$(".ledger [data-r]");
revealBatch($$("[data-r]").filter((e) => !ledgerR.includes(e)), "top 88%");
revealBatch(ledgerR, "top 92%");

// SplitText och revealer kan ha flyttat layouten: mät om (refresh-lyssnaren bygger om vid ändring)
ScrollTrigger.refresh();
addEventListener("load", () => ScrollTrigger.refresh());

// --- vila: varje bricka driver ±4 px; ton, rail, scenens fönster, video och will-change följer läget ---
const railA = $$(".rail a");
let curBand = -2, curMove = null, curClip = "", curLive = null;
const stateAt = (y) => { let idx = 0; P.trans.forEach((t, i) => { if (y >= t[0] + (t[1] - t[0]) * P.sw[i]) idx = i + 1; }); return idx; };
gsap.ticker.add((time) => {
  const y = scrollY;
  const idx = stateAt(y), S = P.st[idx];
  if (root.dataset.tone !== S.tone) root.dataset.tone = S.tone;
  const band = idx === 1 ? 0 : idx >= 2 && idx <= 9 ? Math.min(idx - 2, 6) : -1;
  if (band !== curBand) {
    curBand = band;
    railA.forEach((a, i) => (i === band ? a.setAttribute("aria-current", "true") : a.removeAttribute("aria-current")));
  }
  // bandtexten får sin egen ton först när den står på sin färg (före dess syns den inte)
  const live = y >= P.T2[0];
  if (live !== curLive) { curLive = live; tj.classList.toggle("live", live); }
  // scenen syns bara inom övre vänstra fältet: aldrig över en söm eller under navet
  // (snittet av fältets plats och var fältbrickan faktiskt är: när fälten lämnar för kartläggningen följer texten med ut)
  const r = stage.getBoundingClientRect(), f = P.g.fields[0], fb0 = bricks[0].el.getBoundingClientRect();
  const T = Math.max(f.y, fb0.top), Bt = Math.min(f.y + f.h, fb0.bottom), Lf = Math.max(f.x, fb0.left), Rt = Math.min(f.x + f.w, fb0.right);
  const ins = (v) => Math.max(0, Math.round(v)) + "px";
  const cp = Bt <= T || Rt <= Lf ? "inset(100% 0px 0px 0px)" : `inset(${ins(T - r.top)} ${ins(r.right - Rt)} ${ins(r.bottom - Bt)} ${ins(Lf - r.left)})`;
  if (cp !== curClip) { curClip = cp; stage.style.clipPath = cp; }
  const moving = P.trans.some((t) => y > t[0] - 2 && y < t[1] + 2);
  if (moving !== curMove) { curMove = moving; lager.classList.toggle("moving", moving); }
  const off = y > P.T2[1] + 4;
  if (off && !video.paused) video.pause();
  else if (!off && video.paused) video.play().catch(() => {});
  const TAU = Math.PI * 2;
  bricks.forEach((b, i) => {
    const a = S.amp[i];
    b.bi.style.setProperty("--dx", (a * Math.sin((time * TAU) / b.p1 + b.ph)).toFixed(2) + "px");
    b.bi.style.setProperty("--dy", (a * Math.cos((time * TAU) / b.p2 + b.ph * 1.3)).toFixed(2) + "px");
  });
});

// --- pekare: hela lagret 0,6 % mot pekaren, inget annat ---
if (matchMedia("(hover: hover) and (pointer: fine)").matches) {
  const qx = gsap.quickTo(lager, "x", { duration: 0.9, ease: "power3" });
  const qy = gsap.quickTo(lager, "y", { duration: 0.9, ease: "power3" });
  addEventListener("pointermove", (e) => {
    qx((e.clientX / innerWidth - 0.5) * 2 * 0.006 * innerWidth);
    qy((e.clientY / innerHeight - 0.5) * 2 * 0.006 * innerHeight);
  }, { passive: true });
}

// --- rail: klick = lenis.scrollTo till bandets vila; tangentbordsfokus i ett dolt band tar dit det ---
const restStart = (idx) => P.trans[idx - 1][1] + 2;
railA.forEach((a, i) => a.addEventListener("click", (e) => {
  e.preventDefault();
  lenis.scrollTo(restStart(2 + i), { onComplete: () => { blocks[i].setAttribute("tabindex", "-1"); blocks[i].focus({ preventScroll: true }); } });
}));
blocks.forEach((bl, k) => bl.addEventListener("focusin", () => {
  if (stateAt(scrollY) !== 2 + k) lenis.scrollTo(restStart(2 + k), { immediate: true });
}));
$(".tj-rail-col").addEventListener("focusin", () => {
  const s = stateAt(scrollY);
  if (s < 2 || s > 9) lenis.scrollTo(restStart(2), { immediate: true });
});

window.__st = ScrollTrigger; // dev-krokar för mätningar
window.__b3 = () => ({ trans: P.trans, max: P.g.max, t: tl.time(), dur: tl.duration(), y: scrollY });

// --- ?preview=<akt> ---
const pv = new URLSearchParams(location.search).get("preview");
if (pv) {
  lenis.resize();
  const restMid = (idx) => (P.trans[idx - 1][1] + P.trans[idx][0]) / 2;
  const T = { hero: 0, fullbleed: P.T1[0] + 0.85 * (P.T1[1] - P.T1[0]), kartlaggning: restMid(10), om: restMid(11), insikter: restMid(12), slut: P.g.max };
  // band-n: slutet av bandets vila (scenen står fast, nästa svep har inte börjat)
  const m = /^band-(\d)$/.exec(pv);
  const y = m ? P.trans[1 + +m[1]][0] - 4 : T[pv];
  if (y != null) lenis.scrollTo(y, { immediate: true, force: true });
}

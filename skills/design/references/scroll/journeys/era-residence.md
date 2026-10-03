# The Era journey — era-residence.com broken down and rebuilt as a grammar

Catalogue entry: `design-catalogue/entries/era-residence/` (rank #1 in `ranking.txt`,
`motion_floor: 2`; `motion/sheet.webp` is the 20-step contact sheet, `motion/probe.json` the
stack). Read 2026-10-03 by the lead from the sheet, and from a static inventory of the site's
own motion file (Slater `60900.js`, 59 KB, agency THEFIRSTTHELAST).

Anton, 2026-10-03: *"själva resan på sidan, inte den exakta layouten eller utseendet, men det är
en sån typ av visuell resa jag vill skapa åt användarna på de sidor vi producerar, med olika
stil- och formspråk i övrigt, ingen sida får vara den andra lik."*

So this file describes the **trip** — what the visitor is carried through and how one act hands
over to the next — as something to rebuild with a different shape, material, palette and type
every time. It is not a layout to copy. The variation slots in § 5 are the point.

## 1. The stack (measured, not guessed)

Webflow page, no Webflow Interactions. **GSAP 3.15.0 with only ScrollTrigger, SplitText and
CustomEase registered** — no ScrollSmoother, no Flip, no SVG plugins, no WebGL, no three.js, no
shaders. **Lenis 1.3.21** (`duration 1.2`, `smoothWheel`, `touchMultiplier 2`, expo-style easing,
`lenis.on("scroll", ScrollTrigger.update)`, `gsap.ticker` drives `raf`, `lagSmoothing(0)`).
Barba 2.10.3 for page transitions. Lottie once (the agency credit). Eight bougainvillea video
loops (webm/mov, avif posters) played by ScrollTrigger on enter, paused on leave.

Everything rich on the page is **CSS mask / clip-path driven by GSAP, SplitText masks, `position:
sticky` + scrub, and timing**. The lesson for the chain: the showcase level is reached with two
plugins and discipline, not with a plugin inventory.

Motion tokens (mirrored as CSS variables):
```
durS 0.4   durM 0.8   durL 1.2   stagger 0.1   delayReveal 0.3
InOut  .75,0,.25,1   Out .25,1,.5,1   In .5,0,.75,0   Ease .25,.1,.25,1
Write  .333,0,.667,1   diveIn .6,0,0,1   horScroll .25,0,.75,1   loader: custom SVG path ease
html { font-size: 1vw }   breakpoint 992
```
Type: ambroise-francois-std (condensed display serif), sloop-script-three (script accent),
Maison Neue Extended (body). Ground: burgundy `#340C25`, sky/pool blues, cream, pale blue.

## 2. The journey, act by act

| # | Act (what the visitor sees) | Mechanism (what the code does) | House equivalent |
|---|---|---|---|
| 0 | **Burgundy overture.** Logo mark, the words of the place (Costa · del Sol) ghosted huge in script behind, the name in condensed serif with the town in script, a thin vertical rule, a one-line promise. A progress bar runs ~4 s on the first visit. | Preloader `position: fixed`, SplitText reveals, 1.2 s hold, bar with the custom `loaderEase`; `sessionStorage.hasVisited` → repeat visits skip to the dive. | Intro pattern "copy first" + rule 1 of `showcase-floor.md`: the overture's last frame is the hero's first. |
| 0→1 | **The arch dive.** An arch-shaped opening rises from the bottom of the burgundy screen, frames the sky, widens, and the camera flies *through* it onto the estate. | Three CSS rectangles + an arch SVG as `mask-image`; GSAP tweens `--arch-w` 24→36 vw and `--arch-y` 104→15 vh (1.5 s InOut), then 125 vw / −100 vh (2.4 s diveIn) while the hero photo scales 0.75→1 (1.15→1 on mobile). Barba starts 25 % into the dive. | The handoff is the brand's own architecture. On our pages: the signature shape (a window, a page corner, a lens, a letter counter) is the door. |
| 1 | **Hero: descent to the pool.** The title holds over the sky; the estate rises behind it; the text column and the tall background drift at different rates; then the photo zooms until we are over the water. | `.hero-w` sticky 100 vh inside a scroll area `calc(100vh*4 + 50rem + 100vh)`; scrubbed: two translate rates, then `scale 1→2` from `transform-origin 50% 75%` ("In" ease). | A pinned act of ~5 screens with **one** continuous camera move; heading still for ≥ 40 vh before the zoom (F-025). |
| 2 | **"A place to live, to return year after year."** A pale half-moon rises from the bottom with a sentence set along its curve; it grows until it is the next ground. | Section pulled up by `−(50rem + 100vh)` so it overlaps the zoom; SVG circle text with `wordSpacing` 0→10 rem scrubbed. | Transition cause "panel grows from the axis" + "text on the curve of the shape that frames the image" — the arch again, now as a bowl. |
| 3 | **Benefits as slides.** Real-life location · community, not complex · built to stay · boutique: a small photo card grows to full bleed, the next slides in. | `[data-snap]` section; Lenis custom snap (40 ms after stop, >50 % visible → `lenis.scrollTo`); the `slide` reveal = `clipPath polygon(100% 0,100% 0,101% 100%,125% 100%)` → full rectangle while the inner image goes from `scale 1.5, xPercent 25` to rest, 1.2 s InOut (a diagonal wipe with a counter-zoom). | "card-to-full-bleed grow". Our build: Flip or a clip-path scrub; snap through Lenis, never ScrollTrigger snap on the page. |
| 4 | **Quote.** A pull quote over a pool photo that parallaxes away. | `img-out` parallax (yPercent 0→20). | A rest beat. One per three acts. |
| 5 | **Location: the horizontal passage.** The page turns sideways: the concept, then "Spain / New / Golden / Mile" in huge serif whose lines drift at different offsets, "Between Marbella and Estepona", a hand-drawn route with stops that draws itself, flowers drifting past. | Section height = track width; sticky screen; `x: −(scrollWidth − width)` with `horScroll` ease, `scrub 0.25`, from "2.5% top" to "97.5% bottom"; title lines `wrap([-5,25,-15])→wrap([5,-25,25])`; path revealed by clip-path over 2.4 s; info block fades 0→1 and scales 0.75→1. Desktop only. | "horizontal pin pan" (Khanh). Reveals inside use `containerAnimation`. DrawSVG for the route. Mobile gets the same acts stacked. |
| 6 | **Master plan.** An aerial render settles; a cloud marquee crosses; three pulsing pins open floating tips. | Image `scale 1.15→1` scrubbed; `@keyframes` marquee 32 s with every even cloud flipped; pins with an infinite pulse ring; tips follow the cursor (2.4 s, power3). | The "object with hotspots" device; CSS does the marquee. |
| 7 | **Apartment types.** Three typologies in an auto slider with a progress bar. | 6 s per slide, paused by IntersectionObserver < 0.2; change = hide text (SplitText −110 %), wipe in the image (`slide`), reveal text. | A ledger-with-image act; the slide wipe is the recurring transition. |
| 8 | **Residences range from 104 to 244 m².** Rules and paragraphs reveal. | `line` reveal `clipPath inset(0 0 100% 0)→inset(0)`, `p` reveal masked lines `yPercent 110→0`. | Shared reveal, house-physics. |
| 9 | **Amenities.** Vertical tabs with a sliding highlight; on exit the whole content zooms past the camera while fading. | Sticky screen in a 2.5-screen area; scrubbed exit `scale 1→2`, wrapper `opacity 1→0`. | "exit through the lens" — the act leaves by the same camera that brought us in. |
| 10 | **Interior.** Accordion of upgrades, a gallery that opens a lightbox (zoom + pan). | Reuses the reveals; lightbox `scale 0.5→1`, slides ±125 %, smoothed mouse pan on desktop, pinch on mobile. | Read-mode pocket inside a persuade page. |
| 11 | **Architecture: the second arch.** "The space to live in" rises as a second half-moon; two window openings grow in a photo and open fully; the side flowers push outward; the frame scales from 0.75 to 1. | Sticky `.arch-w`, scrubbed "top bottom"→"200% top": two polygon clip-path masks; intro `scale 1→1.84`; flowers `scale` up and `xPercent ±50`; text reveals at "30% top"; image parallax 25 % from "55% top". Desktop only. | Rule 3: the signature object (arch + flowers) **recurs and changes** — overture door, mid-page bowl, now a pair of windows. |
| 12–13 | **Facts, CTA.** Developer, architects, licence, "a short conversation is enough". | Reveals. | Ledger + one action. |
| 14 | **Footer: the window closes.** The last photo shrinks from full bleed into a framed window — the arch's rectangle cousin — while the footer rises and the scroll cue fades. | Scrubbed from "top 30%": `clipPath inset(0)→inset(8% 22% 8% 22%)` (`4% 32%` mobile); footer content `opacity 0→1`, `scale 0.75→1`. | The ending answers the opening: we came in through an opening, we leave looking out through one. |

Always present: a fixed header whose logo spins on the ticker at 30 °/s ± 10·|Lenis velocity| (so
the mark breathes with the scroll), a desktop scrollbar with a 00–99 label, a scroll cue, and a
header that swaps light/dark/colour theme per section (`[data-bg]` triggers at the header's
centre line). Hover grammar: magnetic buttons (strength 25, power4 1.6 s, elastic release), nav
words rolling as two masked copies, link characters flipping ±90° with an underline that exits
right and re-enters left, circle buttons whose arc stroke grows 4 %→50 %, siblings dimming to 0.2
via `:has()`.

Reveal system (`[data-scroll-reveal]`, once at "top bottom"; inside the track via
`containerAnimation` at "left bottom"): `a` script accent (chars from opacity 0, rotateX 90,
x 10 rem, origin bottom; 1.2 s Out, stagger 0.1) · `h` headings (chars yPercent 50, rotateY 90;
stagger 0.05) · `p` paragraphs (masked lines yPercent 110→0; hide −110 in 0.4 s In) · `ctn`
blocks (y 3.333 rem, opacity 0) · `line` rules (clip inset) · `slide` images (diagonal wipe +
counter-zoom). Parallax: `img` ±15 % scrub 0.5, `img-in` −20→0, `img-out` 0→20, `ctn-up/down`
±10 from "top 125%" to "bottom −25%"; any of them switched off per breakpoint with
`data-mob="off"` / `data-desk="off"`.


### 2b. Seen at 60 frames (`MOTION_FRAMES=60`, 2026-10-03)

The 20-frame sheet hid how the acts hand over. At 60 frames each transition shows its material:

- **The bowl hands its colour on.** The half-moon of act 2 carries "Three reasons to choose Era"
  along its curve; it rises in pale sky blue and, fully grown, *is* the benefits section's ground.
  The transition and the next act are the same colour field. Nothing fades; the shape becomes the
  ground.
- **Flowers bridge the ground change.** Where pale blue turns to cream (benefits → concept), a
  bougainvillea cut-out enters from the lower edge first and the cream follows it, so the change
  has a cause on screen before it happens.
- **Clouds carry the route into the master plan.** The hand-drawn route of the horizontal passage
  runs into a bank of clouds; the clouds part onto the aerial render. Act 5 → 6 is a camera
  descending through weather, not a cut.
- **The reverse grow.** After the master plan the full-bleed aerial shrinks back into a framed
  card on pale blue (the typology slider). The same card ↔ full-bleed move is used in both
  directions, which is what makes it read as one system.
- **The overture's burgundy returns as blocks.** In "The space to live in" the burgundy of the
  first screen comes back as rectangular colour panels holding bougainvillea photos, and the
  closing "ARCHITECTURE" sets condensed type across the photograph (rule 5: type and media in one
  frame).

House reading: rule 2 of `showcase-floor.md` is met here by *one* material per transition (a
shape, a plant, weather, a card), each taken from the subject itself. That is the bar for the
Alunix next round (AUDIT-ALUNIX-R9.md § 4).

## 3. What makes it a journey (the part to keep)

1. **One shape is the thread.** The arch is the loader's exit, the mid-page bowl with text on
   its rim, the pair of windows in the architecture act, and the closing frame. The visitor
   never names it, but the page feels like one building.
2. **Camera, not sections.** The hero is a descent; the amenities leave by zooming past the
   lens; the location turns the page sideways; the end pulls back into a window. Acts are
   *moves of one camera*, and each transition has a material cause (rule 2 of the floor).
3. **Alternation.** Full-bleed photo → cream text chapter → photo → pale-blue chapter. Never two
   dark photo acts in a row, never two text chapters in a row. Rest beats (the quote) every
   third act.
4. **One passage of a different axis.** A single horizontal stretch in a vertical page, placed
   after the first third, carrying the biggest type on the site.
5. **A living material that crosses the chapters.** Bougainvillea video loops bleed in from
   the frame edges in five different acts, each time larger or from another side.
6. **Text behaves the same way everywhere.** Every heading arrives the same way (chars standing
   up), every paragraph the same way (masked lines), every script word the same way — and then
   it stands still. Consistency of reveal is what lets the big moves read as big.
7. **The ending answers the opening.** Door in, window out.
8. **Tempo is set, not left to the wheel.** Lenis 1.2 s duration, chapters that snap, a hero of
   five screens, scrub values of 0.25–0.5 — slow enough that nothing is missed (F-020).

## 4. Rebuild recipe (house toolchain)

Static HTML with the importmap from `toolchain.md`; `./gsap.js` exports `gsap, ScrollTrigger,
SplitText, CustomEase, Flip, DrawSVGPlugin`; `./smooth-scroll.js` exports the Lenis instance
with the house tempo (`lerp .075`, `wheelMultiplier .6`) — do not copy Era's Lenis numbers.

```js
import { gsap, ScrollTrigger, SplitText, CustomEase, DrawSVGPlugin } from "./gsap.js";
import lenis from "./smooth-scroll.js";

// tokens — rename per project, never reuse the values as a set
CustomEase.create("inOut", "0.75,0,0.25,1"); CustomEase.create("out", "0.25,1,0.5,1");
CustomEase.create("in", "0.5,0,0.75,0");     CustomEase.create("dive", "0.6,0,0,1");
const D = { s: 0.4, m: 0.8, l: 1.2, stagger: 0.1 };

// 0→1  the door: a masked opening that rises, widens, and we pass through
const door = gsap.timeline({ paused: true });
door.to(":root", { "--door-w": "36vw", "--door-y": "15vh", duration: 1.5, ease: "inOut" })
    .to(":root", { "--door-w": "125vw", "--door-y": "-100vh", duration: 2.4, ease: "dive" })
    .fromTo(".hero-plate", { scale: 0.75 }, { scale: 1, duration: 3.9, ease: "dive" }, 0);
// overture copy reveals first (SplitText masks), a hold, then door.play()

// 1  hero descent: ~5 screens, one camera move, heading still ≥ 40 vh
gsap.timeline({ scrollTrigger: { trigger: ".hero-area", start: "top top", end: "bottom bottom", scrub: 0.5 } })
  .to(".hero-copy", { yPercent: -40, ease: "none" }, 0)
  .to(".hero-plate", { yPercent: -15, ease: "none" }, 0)
  .to({}, { duration: 0.35 })                                            // the still beat
  .to(".hero-plate", { scale: 2, transformOrigin: "50% 75%", ease: "in" });
// .hero-area is 500vh tall; .hero-w is position: sticky; top: 0; height: 100vh

// 2  the bowl: a shape rises and grows into the next ground, its rim carrying a sentence
gsap.timeline({ scrollTrigger: { trigger: ".bowl", start: "top bottom", end: "top top", scrub: 0.4 } })
  .fromTo(".bowl-shape", { yPercent: 60, scale: 0.8 }, { yPercent: 0, scale: 1.6, ease: "none" })
  .to(".bowl-rim-text", { attr: { "word-spacing": "10rem" } }, 0);     // <textPath> on the arc

// 3  slide wipe (the recurring image transition)
const wipeIn = (img) => gsap.timeline()
  .fromTo(img.parentElement, { clipPath: "polygon(100% 0,100% 0,101% 100%,125% 100%)" },
          { clipPath: "polygon(0 0,100% 0,100% 100%,0 100%)", duration: D.l, ease: "inOut" })
  .fromTo(img, { scale: 1.5, xPercent: 25 }, { scale: 1, xPercent: 0, duration: D.l, ease: "inOut" }, 0);

// 5  the sideways passage
const track = document.querySelector(".track");
const pan = gsap.to(track, { x: () => -(track.scrollWidth - innerWidth), ease: "none",
  scrollTrigger: { trigger: ".passage", pin: true, start: "top top", scrub: 0.25,
                   end: () => "+=" + (track.scrollWidth - innerWidth), invalidateOnRefresh: true } });
gsap.fromTo("#route", { drawSVG: "0%" }, { drawSVG: "100%", ease: "none",
  scrollTrigger: { containerAnimation: pan, trigger: "#route", start: "left 70%", end: "right 40%", scrub: 0.4 } });

// 14  the window closes
gsap.timeline({ scrollTrigger: { trigger: ".outro", start: "top 30%", end: "bottom bottom", scrub: 0.5 } })
  .to(".outro-plate", { clipPath: "inset(8% 22% 8% 22%)", ease: "none" })
  .fromTo(".footer", { autoAlpha: 0, scale: 0.75 }, { autoAlpha: 1, scale: 1, ease: "none" }, 0);

// text, the same way everywhere
document.fonts.ready.then(() => {
  SplitText.create("[data-reveal=p]", { type: "lines", mask: "lines", autoSplit: true,
    onSplit: s => gsap.from(s.lines, { yPercent: 110, duration: D.l, ease: "out", stagger: D.stagger,
      scrollTrigger: { trigger: s.elements[0], start: "top 85%", once: true } }) });
  SplitText.create("[data-reveal=h]", { type: "chars,words", autoSplit: true,
    onSplit: s => gsap.from(s.chars, { yPercent: 50, rotateY: 90, autoAlpha: 0, duration: D.m, ease: "out", stagger: 0.05,
      scrollTrigger: { trigger: s.elements[0], start: "top 85%", once: true } }) });
});

// chapter snap through Lenis (never ScrollTrigger snap at page level)
let t; lenis.on("scroll", () => { clearTimeout(t); t = setTimeout(() => {
  const hit = [...document.querySelectorAll("[data-snap]")].find(s => { const r = s.getBoundingClientRect();
    return Math.min(r.bottom, innerHeight) - Math.max(r.top, 0) > innerHeight * 0.5 && r.top !== 0; });
  hit && lenis.scrollTo(hit, { duration: 1.2 }); }, 60); });
```

Verification stays the house's: `section_probe.py` on the whole page against the baseline
(F-021), `motion_probe.py` for staircase/frame time (F-013), the contact sheet read by the lead,
and the two floor-2 references open beside it (`showcase-floor.md` § 1).

## 5. Variation slots — how the next page is *not* Era

Fill every slot differently from Era and from the last house page; the fingerprint gate
(`feel-and-fingerprint.md`) checks it, but decide it here first.

| Slot | Era | Other answers seen in the catalogue |
|---|---|---|
| The thread shape | an arch (architecture) | a lens (elegantseagulls), a letter counter (khanhnguyen's parting word), a window in a photo (Hōrai), a vinyl (lesburgersdecolette), a cube unfolding (d2c-lifescience), a pen standing in the sentence (nota), a bolt that wipes (agencefoudre) |
| The door (overture → hero) | fly through the shape | counter → mark (ddark, nickho), copy first then light (seewhateyesee), curtain/push (filmbot), letters out of blur (millemann), object in the loader (ikea), pixel-block dissolve (davidecattaneo, meesverberne) |
| The camera | descent, then zoom past | dolly into a drawing (illoca), corridor of photos (thisisonward), orbit a product (neiru), a walk through rooms (maximeguillon), a room of text (stabondar) |
| The living material | flower video loops at the edges | smoke, grain, paper fibre, a drifting cloud marquee, cut-out people (vazzi), stickers, a ribbon (digidop) |
| The passage of a different axis | one horizontal location chapter | a vertical column wall (markclennon), a checkerboard swap (thomasmonavon), a tilted plane (wodniack), a 3D ring (annnimate) |
| The reveal grammar | chars standing up / masked lines | words lighting grey→ink (forge, filmbot), lines through blur (12 studio), scramble (modus), letters bobbing (flashform) |
| The rest beat | a quote over a parallax pool | a single full-bleed still, a line drawing, silence on a flat ground |
| The ending | the photo becomes a framed window | the shape returns as the sign-off (heart mask → staircase, maelruffini), the wordmark melts back (thisisbond), Hello/Bye bookends (huge), the loader object sprints across the lab (runrobrun) |
| Tempo | Lenis 1.2 s, snap, scrub .25–.5 | house tempo fixed; vary act length and the position of the peak instead |

Rule of thumb: change the **shape, the material and the door** and the page is already its own;
keep the eight journey properties in § 3 and it will still feel like a trip.

## 6. Below the floor on Era itself (not to copy)

- `prefers-reduced-motion` is not read anywhere — consistent with the house (F-011), noted
  only because the a11y audit will ask.
- No `<img>` has `width`/`height`; srcset tops at 1920 w; `html { font-size: 1vw }` makes
  every rem scale with the viewport (type gets very small on narrow desktops).
- A Swiper init that never runs (dead code), and the location and architecture acts are
  desktop-only — mobile gets a flatter page. The house version keeps the acts on mobile as
  stacked scenes.
- First-visit-only overture via `sessionStorage`: fine, but the repeat-visit door must still
  satisfy rule 1 (something persists across the handoff) — on Era it does, the dive stays.

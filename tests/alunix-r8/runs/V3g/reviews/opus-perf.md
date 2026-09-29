fix

## persistence

**Status: pass, with one gap in the inputs.** Everything was measured on this build (index.html, mtime 2026-09-27 19:11) on 2026-09-28. Every browser was headless and started through `browser_lock.py`, one at a time. Frame timing used new-headless `channel="chromium"` with `--enable-gpu` (ANGLE D3D11, Iris Xe).

- **Read this run:** `performance.md` (§1 budget, §6 Never), `motion-smoothness.md`, `optimize.md` § NEVER, `scroll/devices.md` § The engine, `BYGGSPEC.md` §1, `concepts.md` l.819–825 (budget line), and the full source (CSS, markup, and inline JS l.908–2070).
- **Gap:** V3g has no `BRIEF.md`, so there is no § performance plan and no § reference lock to read. I used `BYGGSPEC.md` §1 as the performance plan. It says the Calyx and Hōrai iframes are mounted lazily.
- **Server:** my first pass used my own `serve.py` on port 3317. After the session restart I used the coordinator's server on 3305, which is also HTTP/1.1 with Content-Length.
- **Output:** all results are in `shots/perf-review/`. Raw traces and scratch scripts are in `shots/perf-review/traces/`.

**Probes that ran:**

| Probe | Runs | Exit | Key numbers (run A / run B) |
|---|---|---|---|
| `perf_probe` 1440, 4x CPU | 2 | 1 / 1 | LCP 8140 / 4596 ms · CLS 2.851 / 2.851 · long tasks under scroll 3 / 1 · own transfer 1.37 MB, plus 1.52 MB from the Calyx iframe · DOM 1136 · 2 font files, 44.6 kB |
| `perf_probe` 390, 4x CPU | 1 | 1 | LCP 680 ms · CLS 0.0009 · long tasks under scroll 5 · DOM 499 |
| `section_probe` (1x, GPU) | 2 | 0 / 0 | p95 16.8 ms in 7 of 7 sections, except one run each at 33.2 ms (process) and 33.3 ms (exempelcase). Frames over 33 ms: tes 3/5, process 7/6, exempelcase 6/6, showcase 8/9, hero, pris and kontakt 0. 1 load per iframe, 0 refreshes during the pass, 60 px per notch |
| `click_scroll_probe` | 2 | 0 | max step 59 / 71 px (lead: 44-60) |
| `motion_probe` fast 100:60 | 2 | 1 / 1 | `#cardFlip` p95 66.6 / 66.7 ms, over 33 ms 107 / 139, max_step 1.91 / 2.70 %, staircase 0 / 0 |
| `motion_probe` slow 20:120 x120 | 1 | 1 | p95 33.4 ms, max_step 0.47 %, staircase 0 |
| Control `tests/motion/smooth.html` | 1 | 1 | p95 16.8 ms, 1 frame over 33 ms. The host is not perfectly quiet, so single-frame counts are at noise level; counts over 100 are not. |
| CDP trace, GPU, hero 0-2400 px | 4x twice, 1x once | - | at 4x: p95 100.1 / 83.4 ms, median 66.6 / 50.0, main frame 52.3 / 41.4 ms, Commit + Layerize 25.3 / 20.5 ms, 211 layers. At 1x: p95 16.8, main frame 5.5 ms |
| CDP trace, GPU, showcase 7097-10697 px | 4x twice, 1x once | - | at 4x: p95 133.3 / 116.7 ms, median 66.6 / 66.8, main frame 56.0 / 57.9 ms, Commit + Layerize 35.9 / 38.0 ms, 254 layers. At 1x: p95 16.8 |
| Load check (GPU) | 4x and 1x | - | 1 Calyx load, 3 ScrollTrigger refreshes, all at load. `.showcase-stage` never rendered in view at scrollY 0. One 404 (URL not captured). Tailwind CDN warning. |

**What is noise and what is signal:**
- The size of the 4x numbers varies between runs (LCP 8140 vs 4596; showcase p95 133 vs 117). The pass/fail verdict does not.
- The single 33 ms p95 values at 1x are noise. The counts of frames over 33 ms repeat in both of my runs and in the lead's, so they are signal.
- Tracing adds overhead, so absolute trace milliseconds run high. Read the traces as A/B comparisons.
- `motion_probe` and `perf_probe` launch headless-shell without GPU flags. I used them for value continuity, LCP/CLS and weight, not as the GPU frame clock.

## fidelity

- **Signature act (hero card flip, `#cardFlip` rotateY 0-180 over the 220 % pin): it moves. It is not DEAD.**
  - The sparklines `motion-fast-a/track-0.png` and `motion-slow-a/track-0.png` show a clean power1.inOut S-curve with no flat shoulder, staircase 0 and max_step 0.47-2.70 %.
  - The ÖH/NV dither parallax moves too (max_step 1.36-1.87 %). The fast run B shows one reversal, which is at noise level.
- **The value is not the fault. The frame clock is.** This is fault 2 in `motion-smoothness.md`, not fault 1.
  - The frame-times sparklines show a jagged baseline of 33-66 ms at 4x CPU.
  - At 1x the hero holds 16.8 ms.
- **Showcase:** it glides (click max step 59-71 px, 1 load per iframe, 0 refreshes during the pass).
- **Engine house rules: all met.**
  - `scrub:true` is the only smoothing layer.
  - Each pin is created once.
  - `pinSpacer` is set for the iframe pin.
  - `lagSmoothing(500,33)` is in place.
  - Lenis runs at 0.075 / 0.6.
  - The timeline is padded to 1.
  - The `--sc-ps` contract does not apply: this is GSAP, with no scrollcraft variables.
- **Drift from the plan (defect): the Calyx iframe is mounted at load** (`src` is in the HTML, l.720). `BYGGSPEC.md` §1 and `concepts.md` l.823 ask for a lazy mount. The Hōrai iframe follows the plan; Calyx does not.

## ceiling

- **aspensearch-com** (the composition reference in BYGGSPEC): not measured. There is no locked build or performance data for it, so I cannot rank the two on performance.
- **cyphr-studio** (the source of the tile-dissolve motion): not measured, for the same reason. This build's version of the loan, 728 permanently promoted tiles, is the largest single cost I measured.
- **No `BRIEF.md` § reference lock exists for V3g.** No other reference can be ranked.

## material_fixes

1. **HIGH, resting `will-change`.**
   - **Cause:** `.tile-grid>span{will-change:opacity}` (l.508) promotes 728 tiles for the life of the page: 3 cells x 96 plus 11 figures x 40. `.case-choice-frame img{will-change:transform}` (l.239) adds two more.
   - **Measured, same host, removing only these two rules:**
     - Hero at 4x: layers 211 -> 19, Commit + Layerize 20.5-25.3 -> 7.2 ms/frame, median frame 50-67 -> 16.9 ms, frames over 33 ms 112-113 -> 39.
     - Showcase: layers 254 -> 31, Commit + Layerize 36-38 -> 20.6 ms/frame (one run).
   - **Fix:** remove both class rules. Opacity tweens need no permanent promotion.
   - **Target:** resting will-change 0, layers <= 30, hero p95 at 4x -> <= 20 ms.
2. **HIGH, frame budget at the 4x CPU the gate runs at.**
   - **Measured:** hero p95 83-100 ms and showcase p95 117-133 ms. At 1x, 3-9 frames over 33 ms in tes, process, exempelcase and showcase in every run (budget: 0).
   - **What remains after fix 1 (one run each):**
     - Hero: p95 66.6 ms, main frame 25.7 ms (paint 8.5 ms, rAF 6.7 ms).
     - Showcase with the Calyx grain overlay also off: median 33.3 ms, main frame 33.7 ms (paint 12.9 ms). Turning the grain off alone changed nothing (main frame 53.5 ms).
   - **Fix:** apply fix 1, then re-run `trace.py`.
   - **Target:** p95 <= 20 ms and 0 frames over 33 ms at 4x in hero and showcase. At 1x, over-33 frames go from 3-9 -> 0 per section.
3. **HIGH, Calyx iframe mounted at load.**
   - **Measured:**
     - The iframe adds 1.52 MB at load, including a hotlinked Unsplash AVIF of 1.12 MB and the Tailwind Play CDN (126 kB, measured by curl). Load transfer is 2.89 MB against a 2.5 MB budget.
     - Long tasks attributed to `iframe:/sites/calyx.html` at 4x: 1197 ms and 1391 ms.
     - DOMContentLoaded: 5.9 s (GPU, 4x) or 9.2 s (no GPU, 4x).
   - **Fix:** use `data-lazy-src` the way Hōrai does (`maybeLoadHorai`, AHEAD=2). The poster covers until the iframe loads.
   - **Target:** 1.37 MB at load, 0 iframe long tasks before the first scroll.
4. **HIGH, CLS 2.851 at 1440 (both runs; 0.0009 at 390).**
   - **At load:** three entries of 0.9467 each from `.showcase-stage` (rect 852 -> 0). They coincide with the three load-time `ScrollTrigger.refresh()` calls. The stage never renders in view, but the metric counts the shifts.
   - **During scroll:** 0.571 + 0.569 from the `.tes-top` pin.
   - **LCP side effect:** the hero dither image is first painted at 1300 ms (4x), but a new LCP entry is logged after each refresh, so LCP reports 4.6-11.8 s.
   - **Fix:** one refresh, gated on `Promise.all([fonts.ready, calyx load])` instead of the fonts.ready call plus `setTimeout(400)` plus the initial call. Drop `anticipatePin:1` on the hero and tes pins, then re-measure.
   - **Target:** CLS <= 0.05, LCP <= 1800 ms at 1440.
5. **MEDIUM, oversized case screenshots.**
   - **Measured:** both are 2880x1800. `calyx-1440.webp` is 515 kB (the largest image; the `hero-image` rule fails at both viewports). `horai-1440.webp` is 278 kB and is fetched at load even though its poster is `display:none`.
   - **Fix:** re-encode at 1680 px, q80. Test encodes came to 201 kB and 114 kB. Defer the Hōrai poster until the case is activated.
   - **Target:** largest image <= 250 kB, images at load 1.06 MB -> <= 0.6 MB.
6. **MEDIUM, LCP hint on the wrong image.**
   - **Measured:** the LCP element is `k1-stage-pool-dither-grey.webp` (900x600, 2.4 kB), which has no `fetchpriority`. `fetchpriority="high"` sits instead on the card photo, `k1-stage-pool.webp`: 1600 px wide and 65 kB for a card about 460 px wide. The card photo, demo-hyperborea and k4-cabin-desk are served from `/tests/alunix-concepts-r3/`, outside the build.
   - **Fix:** move `fetchpriority` to the dither image. Re-encode the card photo at 1040 px (test encode: 33 kB). Vendor all of these into `assets/`.
   - **Target:** LCP <= 1800 ms, card photo 65 -> <= 35 kB.
7. **MEDIUM, main-thread work during scroll.**
   - **Cause:**
     - `maybeLoadHorai` calls `getBoundingClientRect()` on every Lenis scroll event, after `ScrollTrigger.update` has written styles, until Hōrai mounts.
     - `prewarmInactiveCase` calls `getComputedStyle` x3 on every element of the Hōrai document, mid-scroll.
   - **Measured:** forced style/layout (`UpdateStyleAndLayout`) costs 2.3-3.4 ms/frame at 4x. Long tasks under scroll: 3 / 1 at 1440, 5 at 390.
   - **Fix:** mount through an IntersectionObserver with `rootMargin` of 200 %. Prewarm from a static list of the 6 background URLs.
   - **Target:** 0 long tasks under scroll at both viewports.
8. **LOW, dead weight.**
   - **What:**
     - The `mountDue`/`iframe[data-src]` block matches no element, but its Lenis listener stays registered.
     - `var(--flip)` is unused (l.160).
     - 12 CSS classes are unused.
     - Comments make up 42 kB of the 120 kB HTML.
     - A stale "lagSmoothing(0)" comment remains (l.919).
     - The geist-500 font in the fold has no preload.
     - Unused files ship in `assets/`: demo-calyx-1440*.webp (139 kB), geist-700, public-sans-300, and 8 dither files.
   - **Target:** HTML 120 -> <= 80 kB, 1 font preload, 0 unused assets.

## keep

Keep value continuity exactly as it is: `scrub:true` as the only smoothing layer, pins created once, the custom `pinSpacer` for the iframe pin, and `lagSmoothing(500,33)`. Together they give staircase 0, card max_step <= 2.7 %, 1 load per iframe, 0 refreshes during the pass, and a 59-71 px click step. The fixes above cut work per frame; none of them should touch how the values are driven.

# Performance — the budget, and what spends it

Until 2026-09-08 the chain had one line about performance and no script, no budget and no
gate. The cost showed up as taste: a page that drops frames during scroll gets called
"hackigt och billigt" (F-012), which is the same sentence a stepping value gets, and the
two need opposite fixes. Measure with `scripts/perf_probe.py`; read
[`motion-smoothness.md`](motion-smoothness.md) for the other half.

## 1 · Budget (gate 93)

Measured locally through `scripts/serve.py`, real Chrome, `Emulation.setCPUThrottlingRate
4`, no network throttling, at 1440×900 and 390×844.

| Measure | Limit | Why that number |
|---|---|---|
| LCP | ≤ 1.8 s | ≈ 2.5 s in the field, the Core Web Vitals floor |
| CLS | ≤ 0.05 | Metric-matched font fallbacks plus `aspect-ratio` on every image make 0 reachable; 0.05 is margin |
| Long tasks (> 50 ms) during scroll | **0** | A long task under the thumb *is* the jank |
| Frame time during scroll | p95 ≤ 20 ms, none > 33 ms | 60 fps with headroom |
| Transfer at 1440 | ≤ 2.5 MB total | V3b shipped 4.9 MB |
| Hero image | ≤ 250 kB WebP | It is the LCP |
| Fonts | ≤ 3 files, ≤ 300 kB | V3b shipped 19 files / 732 kB |
| DOM | ≤ 1500 nodes | Single-file HTML |
| Resting `will-change` | 0 elements | Promotion is for motion in flight, not for standing still |
| `filter` / `backdrop-filter` on > 50 % of the viewport | 0 | GPU repaint per frame during scroll |

**A scrubbed clip has its own line and does not count against the page budget:**
≤ 32 MiB for all desktop clips, ≤ 16 MiB for all mobile clips, fetched as a Blob *after*
first paint so it never sits on the LCP path. A clip loaded in the fold breaks both
budgets at once.

## 2 · Loading

- **Every `<img>`**: `width` and `height` attributes (both — the single largest cause of
  layout shift), `decoding="async"`, `fetchpriority="high"` on the LCP image,
  `loading="lazy"` below the fold, `srcset`/`sizes` when it renders under 60 % of the
  viewport width.
- **The hero must be vendored.** Downscale to ~2200 px on the long edge, re-encode WebP,
  commit it. It must not depend on another company's CDN — measured 2026-09-08, V3b's
  heaviest resource was a 1.1 MB hero hotlinked from `images.unsplash.com`, which is both
  a budget failure and a Step 5b rule violation nobody had caught by eye.
- **Fonts**: `.woff2` only; `<link rel="preload" as="font" crossorigin>` for the display
  weight that appears in the fold, and only that one; `font-display: swap`; a
  metric-matched fallback `@font-face` (`size-adjust`, `ascent-override`,
  `descent-override`) so the swap costs no shift; one variable file once you need three
  weights or more; `font-weight` as a property, never `font-variation-settings`;
  `-webkit-font-smoothing` set once on the root, never per element.
- **Iframes**: `loading="lazy"` *and* mounted by an `IntersectionObserver` about one
  viewport ahead. Three live iframes mounted at load is the heaviest thing a marketing
  page can do to itself.
- **`content-visibility: auto`** with `contain-intrinsic-size` on long sections below the
  fold. It is the cheapest single win on a twelve-act page.
- **preconnect** to any origin the fold actually needs.

## 3 · Rendering

- **Animate `transform`, `opacity` and `filter`.** Everything else costs layout or paint
  per frame. `clip-path` composites only in newer Chromium — treat it as a paint cost
  elsewhere and keep the animated area small.
- **`will-change` only while the element is moving**, removed at rest. Setting it
  class-wide promotes every match to its own layer for the life of the page, which is
  itself a jank source on a mid-range GPU. `sc-smooth.js` corrects the engine's own
  class-level promotions at runtime.
- **Blur is expensive in proportion to area.** `backdrop-filter` only on fixed or sticky
  chrome, never on a full-bleed surface during scroll. Grain film goes on a fixed,
  `pointer-events: none` pseudo-element at 4–5 % so it is painted once.
- **`transition: all` is a defect**, not a shortcut: it animates properties you never
  meant to animate, including layout-triggering ones, and retargets on every change.
- **No layout reads in a scroll handler.** One passive listener that only schedules, one
  rAF loop that reads and writes, a deadband so the loop stops when nothing moves. The
  engine's own shape is the model; `window.addEventListener('scroll')` doing
  `getBoundingClientRect()` per event is the anti-pattern.
- **`min-height: 100dvh`, never `height: 100vh`.** The iOS address bar changes `vh`
  mid-scroll and the act jumps.
- **Isolate a continuous animation in a leaf element** so it cannot force its parent to
  re-render.

## 4 · Motion

Timings, easings and the ban list live in [`motion.md`](motion.md); the smoothness rules
and the `--sc-ps` contract live in [`motion-smoothness.md`](motion-smoothness.md). The
performance-relevant half:

- Transitions retarget from their current value; keyframes restart. For anything a user
  can interrupt, use a transition.
- A scrubbed clip needs a **dense GOP** or it seeks like mud — see
  [`assets.md`](assets.md) § Encoding. A normal web encode places a keyframe every two to
  five seconds and plays back perfectly while scrubbing terribly.
- Stagger at 30–80 ms and cap the number of staggered items; a cascade of forty is forty
  animations.

## 5 · Measuring

```bash
python ~/.claude/skills/design/scripts/serve.py --port 3000 --root .
python ~/.claude/skills/design/scripts/perf_probe.py --url http://127.0.0.1:3000/page.html --cpu 4 --out shots/perf
python ~/.claude/skills/design/scripts/motion_probe.py --url http://127.0.0.1:3000/page.html \
    --track "#hero:--sc-p,#hero:--sc-ps,.plate-card:transform" --out shots/perf
```

Never `python -m http.server`: it is HTTP/1.0 and drops large WebP responses under
Chromium on Windows, so you end up measuring a page that failed to load.

Both probes are proven in both directions before they are trusted —
`tests/perf/{heavy,clean}.html` and `tests/motion/{staircase,smooth}.html`. A check that
only ever fires is as useless as one that never does: if a probe flags a known-good
reference build, it is over-greedy and gets narrowed, not waived.

## 6 · Never

- A hero image on someone else's CDN.
- `transition: all`.
- `will-change` on a class.
- A blurred surface larger than half the viewport, animated during scroll.
- More than three font files, or a preload for a weight that is not in the fold.
- An iframe mounted at load.
- A scroll handler that reads layout.
- `height: 100vh` on a full-height act.
- Shipping a number from this file that you did not measure on the actual page.

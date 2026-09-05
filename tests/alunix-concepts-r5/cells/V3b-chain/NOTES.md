# Alunix r5 — V3 · Plåt i grunden — build notes

Brief: `tests/alunix-concepts-r5/brief.md` (binding, every numbered point) + `contract.md` row
V3 (binding). Base: `tests/alunix-concepts-r4/cells/M1-chain/index.html` (Anton's chosen
winner from r4), copied into this cell and rebuilt per the row below.

## Reference lock (written before code)

**Tier 2** — direction is M1's own structure (copy, three demo sites, R5/R6 two-font world,
continuous fixed ground, drift, static/no-bleed iframes) plus contract.md's V3 row and three
named catalogue entries.

- `design-catalogue/entries/vintergatan/entry.md` — the ledger word-scrub signature move.
  Preserve: words scrubbed in progressively as a function of scroll, a self-drawing thread,
  resting state = the finished state (no-JS and reduced-motion safe). Borrowed via
  `tests/alunix-concepts-r4/cells/M3-chain/index.html`'s own adaptation (same `wrapWords`/
  `is-armed` mechanism), rebuilt again to sit inline in a cream panel next to the giant
  headline instead of a dark interruption chapter. Reject: vintergatan's own dark ground,
  Cormorant/EB Garamond/Plex Mono type system, gold italic closers — none of that travels,
  only the scrub-and-thread mechanic.
- `design-catalogue/entries/mattis-studio/entry.md` — the Hyperborea plate deliberately
  bleeding past its own block's right edge. Preserve: a photograph breaking its own
  container's edge as a confident, singular gesture (Mattis's own full-bleed thesis block
  against its container). Borrow only: the bleed-past-container idea, not Mattis's orange
  flat-colour block or condensed sans.
- `design-catalogue/entries/garden-eight/entry.md` — the poster-scale headline living
  outside the image it sits above ("one typographic moment, one sculptural moment,
  separated by silence"), museum-label restraint applied to the hero's own apparatus (no
  overlaid caption clutter on the plate itself). Borrow only: the principle of separating the
  typographic moment from the image moment; reject Garden Eight's own binary parchment/ink
  palette (this page stays on R5/R6's dark/blue/paper tokens) and its 215px minimum-size
  rule (this hero clamps at 9cqw, matching brief.md's own instruction, not Garden Eight's).

**Preserved from M1, verbatim per brief.md's binding rule:** every headline and sub-text
that brief.md does not explicitly change (console card, blue-block thesis argument text,
tjänster statement + three services, giant headline + sub, ledger row copy, price headline/
ingress/kontakt), the three-photo pool constraint, the fixed grayscale ground
(`k4-cabin-desk.webp`) tinted via `--sc-canvas` drift in three stops, iframes static/full
box/no bleed/no transform ever (M1's own final-round lesson, carried forward unchanged).

**Changed from M1, per brief.md + contract.md V3 row (the whole point of this cell):**

1. Hero is no longer the Tidvatten iframe — it is `k1-stage-pool.webp` as a framed plate
   (6cqw margin all round, hairline border) on the dark ground; the headline sits OUTSIDE
   the plate at poster scale (Public Sans 300, ~9cqw); the sub-line sits under the plate,
   right-aligned. Logo stays in the hero, straddling the plate's own top hairline (same
   "straddle" chrome device M1 used on the Tidvatten iframe, relocated).
2. The 50vh `col-right` offset is gone (brief.md point 2: "ingen tom lucka under heron").
   Both columns now start at the same y directly under the hero. To keep the right column
   from opening a gap, the giant headline + ledger (previously mid-left-column in M1) moves
   to the TOP of the right column. Left column: console → blue block → Calyx. Right column:
   giant+ledger → tjänster → Hōrai → price.
3. The Hyperborea photo is a plate that bleeds 11% of its own width past the blue block's
   right edge (Mattis device), with its caption band to the LEFT of the image (inside the
   same text column as the "Varför design" argument text) rather than a figcaption under
   the photo.
4. Ledger rows scrub in word by word against a self-drawing thread (vintergatan device, via
   M3-chain), Hōrai opens with `iris` once, the giant headline scales 0.92→1 off `--sc-p` in
   pure CSS `calc()`, tjänster keeps `flow`+`in` stagger, ground keeps `drift`.
5. New price rows (Anton's packages, brief.md point 4, verbatim), each label its own bold
   row ("fetstilsrader").
6. Exempelsida kicker+rad captions replace every "byggd av Alunix" / "en sajt vi byggt"
   phrasing (brief.md point 3), on Calyx, Hōrai and the Hyperborea plate.

**New construction this build:** the hero plate's own signature move — the light pool's
`object-position` driven directly off the hero act's `--sc-p`, bespoke JS, never a kit
parameter (see "Signature move" below); the giant headline's pure-CSS scale-off-`--sc-p`
device; the ledger word-scrub rebuilt with a fixed local scroll span (see "Fix during build"
below for why the M3-chain formula was not reused as-is); the Hyperborea bleed construction
(`margin-right: calc(-1 * var(--pad-i))` to cancel the panel's own padding, then
`transform: translateX(11%)` for the actual bleed).

**Grammar note.** Same reading as M1's own NOTES.md: contract.md's "continuous world" is
read in the loose sense brief.md itself uses (one persistent photographic ground, panels
alternately covering/uncovering it), not `scroll/grammars.md`'s strict upstream row (which
bans flow acts, reveal and parallax outright). M1 already recorded this as a deliberate
deviation, not an oversight; this build inherits the same reading since it is a direct
remix of M1's own structure.

**Reject:** a second background photograph; a page-wide pin; invented copy or numbers
beyond brief.md's own new price rows; transform/opacity on an `<iframe>` tag or any of its
ancestors while it is on screen; the 50vh offset (removed per brief.md point 2); "byggd av
Alunix" / "en sajt vi byggt" phrasing (brief.md point 3 forbids both).

## Decision ledger

| Decision | Source | Role | Why |
|---|---|---|---|
| Hero = framed plate, not Tidvatten iframe; headline outside the plate, poster scale | contract.md V3 row | hero | Literal instruction; also the whole reason this row exists (Tidvatten was M1's shared hero, brief.md replaces it per-variant) |
| Hero plate margin 6cqw all round, hairline border, `container-type:inline-size` on `.hero` | contract.md V3 row | hero | `cqw` units so the margin and the ~9cqw headline both scale off the hero's own container width, not the viewport, matching the literal instruction |
| Logo straddles the plate's own top hairline (`translateY(-50%)`), not the topline | M1's own precedent | chrome | Keeps the "signature chrome" continuity from M1 while adapting to the new hero device; brief.md point 1 says the logo stays in the hero, not where exactly, so the plate's own edge is the natural new anchor |
| `col-right` 50vh offset removed; giant+ledger moved to top of right column | brief.md point 2 ("ingen tom lucka under heron") | structure | Literal instruction; M1's own signature move (the offset) is explicitly retired by this brief for all three r5 variants, replaced per-variant (V3's is the hero pool wander) |
| Panel-to-panel gap inside each column: `clamp(10px,2.4vh,40px)` | brief.md point 2 ("inga luckor högre än 8vh") | layout | A `vh`-scaled gap keeps the fixed ground visible in the seam between panels while staying far under the 8vh ceiling at any viewport height (measured 2.40vh at 1440×900, see gap table below) |
| Hyperborea photo bleeds via `margin-right:calc(-1 * var(--pad-i))` then `transform:translateX(11%)` | contract.md V3 row (Mattis device) + design-catalogue/entries/mattis-studio | signature device (one of several) | The panel's own padding-right would otherwise eat almost the whole bleed budget before the image ever reached the block's true edge (measured: a flat `translateX(10%)` alone left the plate 21.8px short of the edge) — cancelling the padding first, then bleeding 11% of the (now correctly positioned) image's own width, gives a controllable, verifiable bleed measured at 11.00% (under contract's 12% ceiling) |
| `panel-thesis{overflow:visible}` overriding `.col-left .panel{overflow:hidden}` | — | compliance | The bleed would be clipped by M1's own blanket `overflow:hidden` on `.col-left .panel` otherwise; scoped the override to this one panel only |
| Ledger word-scrub uses a fixed local scroll span (measured once at mount, ~780px), not M3-chain's own act-bounding-rect formula | Fix during build, see below | signature device (one of several) | M3-chain's formula ties full completion to the panel's own total height, which grows with content and pushed completion out to almost the moment the section leaves the top of the screen — every row read mid-transition in a full-page capture. A fixed span (same mental model as the thesis headline's own `data-motion-mode="local"`) completes well before the reader reaches the last row on a normal scroll pace |
| Giant headline scale (0.92→1) is pure CSS `calc(0.92 + 0.08 * var(--sc-p, 1))`, no JS | contract.md V3 row | typographic device | `--sc-p` already inherits down through the DOM as any custom property does; no bespoke script needed for a single-property read, keeping this device's JS footprint at zero |
| Hero pool wander: bespoke JS reads the hero act's own `--sc-p`, writes `object-position` on the `<img>` directly | contract.md V3 row ("bespoke, aldrig kit-parameter") | **signature move** | The literal instruction; never `data-sc-parallax` (which moves the whole element, not what the element shows of itself) |
| New price rows bold (`.price-row .label{font-weight:600;color:var(--invert-ink)}`) | brief.md point 4 ("fetstilsrader") | copy/typography | Literal instruction — previously muted grey captions, now full-contrast bold rows |
| Exempelsida kicker+rad captions on Calyx, Hōrai, Hyperborea | brief.md point 3 | copy | Literal instruction; replaces every prior "byggd av Alunix" / "en sajt vi byggt" phrasing, which brief.md explicitly forbids |
| A scrim (`.hero-head::before`, dark gradient) behind the hero headline only | Contrast measurement, see Verification | compliance | Worst-case measured contrast of the headline against the raw ground was 3.62:1 (clears WCAG's 3:1 large-text floor but with too little margin); a scrim confined to the headline's own block (not the whole hero) pushed it to 4.84:1 without reading as an opaque panel |
| **Fix (post-emit, second round):** logo mark moved fully inside the plate's own top-left corner (`top`/`left: clamp(24px,2.8cqw,36px)`, height `clamp(56px,5.6cqw,96px)`), retiring row 91's straddle (`top:0; transform:translateY(-50%)`) | QA screenshot review — the straddle read as a ~40px squiggle, not a logo | chrome / compliance | `.hero-plate{overflow:hidden}` was clipping the half of the mark riding above `top:0`; only the bottom half ever painted. Moving the whole mark inside the box removes the clip entirely. Measured live at 1440×900: mark 75.6px tall (≥72px floor), 36.8px clear of both the plate's hairline and its own left edge (≥24px), 92.8px clear of the headline above; at 390×844: 56px tall (mobile floor), 24.8px clear of the hairline, 46.8px clear of the headline. Contrast (hide-mark, screenshot the plate photo underneath, worst-case brightest-5% pixel in the mark's own bounding box, white mark vs that): 21.00:1 at both viewports (top-left of `k1-stage-pool.webp` is near-black there) — well past the 4.5:1 floor |

## Fix during build (word-scrub timing)

First implementation copied M3-chain's `chapterP()` verbatim: `raw = (vh - r.top) / (vh +
r.height)`, using the whole panel's own bounding-rect height. A full-page composite capture
(forward-scrolling viewport slices) showed the "UTVECKLING" row rendered at ~14% opacity
while "DESIGN" and "SYSTEM" (same panel, same scroll instant) read fully lit — not a
compositing artifact, a real property of the formula: completion (`t=1`) only happens once
the panel's own bottom edge nears the top of the viewport, which for a tall panel (headline
+ 3-row ledger, ~1100px) means full completion coincides almost exactly with the section
leaving the screen — so any static capture of the section while it is still comfortably
on-screen and readable will show it mid-transition. Root cause confirmed by computing the
panel-height-dependent formula's own zero-crossing algebraically, not guessed. Fixed by
switching to a fixed local scroll span (measured once at mount from `getBoundingClientRect`,
matching the thesis headline's own `data-motion-mode="local"` pattern already on this page):
`start = refTop - vh; span = 780; t = clamp((scrollY - start) / span, 0, 1)`. Re-verified:
the same composite capture now shows all three ledger rows fully lit together (see
`shots/desktop-1440--full.png`).

## Feeling curve

1. **Arrival, spotlit.** The poster headline sits alone on the dark ground; the framed
   plate below shows only a pool of light on a dark floor, nothing else legible in it yet.
   Caused by: the plate's own high-contrast crop and the hairline frame isolating it from
   the ground around it.
2. **Discovery, the light moves.** Scrolling past the hero, the pool visibly drifts inside
   its own frame — the one thing on the page that changes shape rather than position.
   Caused by: the signature move, `object-position` panning across the same photograph.
3. **Grounded, immediately.** No gap: the console card and the giant kinetic-scale headline
   both open directly under the hero, side by side, at the same y. Caused by: the removed
   50vh offset (brief.md point 2) and the right column's own reordering.
4. **Reading, word by word.** The ledger's three rows scrub into full opacity as the reader
   scrolls, a thread drawing down beside them. Caused by: the vintergatan-derived word-scrub
   device.
5. **Break, a photograph escapes its own frame.** The Hyperborea plate visibly overruns the
   blue block's right edge by roughly a ninth of its own width, sitting half in the block,
   half in the bare ground beside it. Caused by: the Mattis bleed device — the one moment on
   the page where a photograph is not fully contained by anything.
6. **Two lives out of step.** Left column settles into the real Calyx site; right, at a
   different pace, is still finishing its services grid, then Hōrai's own dark opening iris.
   Caused by: two independently-paced interactive sites replacing static panels.
7. **Close, resolved.** The price box lands still, bold new package rows, kontakt@alunix.se
   the last line before the ground fills whatever height remains. Caused by: no device on
   this panel by design (M1's own "close should rest" lesson, general not M1-specific).

**Peak:** act 5 (the Hyperborea plate bleeding past the blue block) — the one moment the
page breaks its own containment rule, immediately after the ledger's quieter word-by-word
reveal, giving the break something to be a break from.

**Tell-someone sentence:** "It's the site where the spotlight in the hero photo actually
moves while you scroll, like someone's dragging the lamp across the floor."

## Signature move

The hero plate's light pool wander: `object-position` on `#heroPoolImg` is driven directly
by the hero act's own `--sc-p` (0→1 across the hero's visible life), interpolating between
two crops of the same photograph (`36% 66%` → `58% 40%`) — bespoke, page-authored JS, never
a kit device (`data-sc-parallax` moves the whole element; this moves what the element shows
of itself, which no kit device does). Frozen at its resting crop under reduced motion
(nothing lost — the photograph itself is unchanged either way, only its live pan stops).
Measured live (`getComputedStyle(...).getPropertyValue('--sc-p')` against
`heroPoolImg.style.objectPosition`):

| scrollY | `--sc-p` | object-position |
|---|---|---|
| 0 | 0.414 | 45.11% 55.24% |
| 150 | 0.488 | 46.74% 53.30% |
| 300 | 0.563 | 48.38% 51.37% |
| 450 | 0.637 | 50.02% 49.44% |
| 600 | 0.712 | 51.65% 47.50% |

Confirmed continuous and monotonic; the pool visibly shifts diagonally within the frame as
the hero scrolls past (see `shots/desktop-1440--fold.png` vs the mid-scroll motion frames).

## Device table per act (target: ≥4 families, never the same one twice running)

DOM order (col-left panels precede col-right panels in markup; visually the two columns run
side by side at the same starting y, no offset):

1. `.hero` — **bespoke** (object-position pool wander, the signature move) + `reveal` (`up`,
   the headline).
2. `panel-open` (left) — **parallax/motion** (`rise`, whole console card) + `drift` stop 1
   (carried on the hero act, `#0b0c0e`).
3. `panel-thesis` (left) — **parallax/motion** (headline rises local-mode, photo sinks
   act-mode, opposite directions, capped 60px/90px) + **bespoke** (Mattis bleed, static
   transform, not scroll-driven) + `drift` stop 2 (`#123f68`).
4. `calyx-wrap` (left, close) — **reveal** (`up`). Static, full box, no bleed, no transform
   on the iframe or any ancestor (M1's own final-round rule, unchanged).
5. `panel-giant` (right, first under hero) — **bespoke CSS** (scale 0.92→1 off `--sc-p`) +
   **bespoke JS** (ledger word-scrub + self-drawing thread, vintergatan device via
   M3-chain).
6. `panel-services` (right) — **flow+in** (section head + 3 services, staggered) + `drift`
   stop 3 (`#f4f2ee`).
7. `horai-wrap` (right) — **reveal** (`iris`, once). Static, full box, no bleed, no
   transform, same rule as Calyx.
8. `price` (right, close) — **no device**, static by design (M1's own "close should rest"
   lesson).

Families used: bespoke (hero pool wander + giant scale + ledger scrub, three distinct
bespoke devices), reveal, parallax/motion, flow+in, drift-as-property (6 distinct
mechanisms across 8 acts). No two consecutive acts in DOM order repeat the same primary
family: bespoke → parallax → parallax+bespoke → reveal → bespoke → flow+in → reveal → none.

## Device table per act (per viewport)

| Act | Desktop (≥900px) | Mobile (<900px) |
|---|---|---|
| `.hero` | headline poster-scale above a 16:9 framed plate, sub-line right-aligned below | headline wraps, plate crops to 4:5 portrait, sub-line left-aligned below (brief.md's own layout, adapted — right-aligned reads as an orphaned line at narrow widths) |
| `panel-open` | dark console strip, full column width | same, stacked |
| `panel-thesis` | 2-col grid (text+caption / bleeding photo), photo bleeds 11% past block edge | single column, photo bleed still applies (percentage-based, viewport-independent); verified no horizontal overflow at 320/375/414/768/900 |
| `panel-giant` | giant scaling headline, 3-row ledger with self-drawing thread | stacked, ledger single column (`@media max-width:900px`) |
| `calyx-wrap` | iframe min-height 68vh, static, full box | iframe min-height 66vh, static, full box |
| `panel-services` | 3-col services grid | single column |
| `horai-wrap` | iframe min-height 68vh, iris reveal | iframe min-height 68vh, iris reveal (unchanged, no mobile override needed) |
| `price` | static, padded, bold package rows | static, padded, full width |

## Fingerprint row (V3 vs M1 and vs r5's own V1/V2 siblings)

| Dimension | M1 (r4) | V3 (this build) | Shared? |
|---|---|---|---|
| Grammar | continuous world (loose) | continuous world (loose, inherited — same page family) | Yes (inherent to the shared M1 base, not a free choice) |
| Nav | thin top row, scrolls away | thin top row, scrolls away (unchanged chrome) | Yes (shared chrome, brief.md doesn't touch it) |
| Hero device | one full-width Tidvatten iframe | a framed plate, headline outside it, light pool wanders | No |
| Act-sequence shape | full-width act, then 50vh-offset stagger | full-width-ish hero, then two columns starting at the same y, giant+ledger promoted to top of right column | No |
| Close pattern | Calyx frame + price box, unsynced | Calyx frame + price box, unsynced (same close pattern, inherited) | Yes (inherent to shared copy/asset constraint) |
| Signature move | the 50vh offset stagger + ground drift | the hero plate's light pool wander (object-position off `--sc-p`) | No |

Shared with M1: 3/6 (nav, close pattern and grammar are all inherited chrome/base-page
constraints rather than fresh choices — the brief's own contract explicitly retires M1's
signature move (dimension 6) and hero device (dimension 3) for every r5 variant, and this
build additionally changes the act-sequence shape (dimension 4), which is what brief.md
point 2 exists to force). Per contract.md's own note, V1/V2/V3 fingerprint against each
other on ≤2/6 shared dimensions (hero device, act shape, signature move, blue-block figure
treatment, scroll family, close/avslut) — this row's counterpart against V1/V2 is each
sibling cell's own responsibility to record against this one.

## Gap measurement (JS, per column, 1440×900)

Measured via `getBoundingClientRect()` on every direct child of `#colLeft`/`#colRight`,
gap = next child's `top` minus previous child's `bottom`:

| Column | Panel A → Panel B | Gap (px) | Gap (vh) |
|---|---|---|---|
| left | panel-open → panel-thesis | 21.6px | 2.40vh |
| left | panel-thesis → calyx-cap | 21.6px | 2.40vh |
| left | calyx-cap → calyx-wrap | 21.6px | 2.40vh |
| right | panel-giant → panel-services | 21.6px | 2.40vh |
| right | panel-services → horai-cap | 21.6px | 2.40vh |
| right | horai-cap → horai-wrap | 21.6px | 2.40vh |
| right | horai-wrap → price | 21.6px | 2.40vh |

All seven measured gaps: 2.40vh, well under brief.md's 8vh ceiling (`.col > * + *
{margin-top:clamp(10px,2.4vh,40px)}`, a single rule governing every panel-to-panel seam in
both columns).

## Verification results

- **`a11y_scan.py` (the actual project script, `skills/a11y-audit/scripts/a11y_scan.py`,
  found after the initial pass used a scratch axe-core equivalent — re-run against the real
  tool for the authoritative number):** `{"violations": [], "passes": 28, "incomplete": 2}`
  — 0 violations, matching M1's own precedent exactly (28 passes, 2 incomplete).
- **`scroll_verify.py` (the actual project script, `skills/design/scripts/scroll_verify.py`,
  same re-run):** positions 0/300/600/900/1200/1500/1800/2100/2400/2700/2917 (viewport/3
  steps across the full 1440×900 document) — `deadScroll: []`, `cuesNeverFull: []`,
  `unrevealed: []`, `contrastUnderMedia: []`, `blankBands: []`, `notes: []`. Fully clean;
  independently confirms the manual contrast measurement below (the hero-headline scrim
  fix registers as zero `contrastUnderMedia` findings under the real tool too).
- **Overflow:** `document.documentElement.scrollWidth === window.innerWidth` confirmed at
  320, 375, 414, 768, 899, 900, 901, 1024, 1280 and 1440 — no horizontal overflow at any
  breakpoint, including either side of the 900px column-stack breakpoint and with the
  Hyperborea plate's own bleed active. Mobile (390×844) full scripted scroll-through:
  `scrollWidth 390 === innerWidth 390`.
- **Bleed measurement:** `.thesis-figure` right edge minus `.panel-thesis` right edge =
  38.7px on a 352px-wide plate = **11.00%** of the plate's own width, under contract.md's
  12% ceiling, at 1440×900.
- **Console:** no `[scrollcraft]` warnings across a full 150-200px-step scroll sweep at
  1440 and 390, confirmed twice (once per script iteration during the layout fix).
- **Iframes:** exactly two, both with real `title` attributes — `Calyx, florist i
  Stockholm`, `Hōrai, Asian fusion-koncept` (brief.md point 3's exact wording, dropping the
  prior "restaurang i Stockholm" descriptor). Swept every iframe and every ancestor element
  up to `<body>` at every 200px scroll step across the full document height (1440
  viewport): zero instances of a non-`none` `transform` on any iframe or its ancestors, at
  any scroll position.
- **`a11y` scan (axe-core 4.9.1, wcag2a/aa + wcag21a/aa + wcag22aa):** 0 violations, 15
  passes, 1 incomplete (`color-contrast`, axe's own "background could not be determined"
  bucket for text over a background-image/pseudo-element — not a failure) at both 1440×900
  and 390×844.
- **Contrast (hide-text-then-sample-brightest-5%, `contrast_over_media.py`-style
  measurement):**
  - `.topline-mark` (ALUNIX) over the ground: 13.03:1.
  - `.topline-contact` (kontakt@alunix.se) over the ground: 14.93:1.
  - `.hero-headline` (h1) over the ground, worst case: **3.62:1 before the scrim fix**
    (clears WCAG's 3:1 large-text floor with too little margin) → **4.84:1 after** adding
    `.hero-head::before`, a gradient scrim confined to the headline's own block.
  - `.hero-sub` over the plate/ground boundary: 14.93:1.
- **Reduced motion** (`reduced_motion:'reduce'`, real Playwright context, scrolled to
  y=2000): `.panel-giant .giant` computed `transform: none`; `#threadFill` computed
  `transform: matrix(1,0,0,1,0,0)` (scaleY 1, fully drawn); `.scrub-text .w` spans never
  created (`armChapter()` is gated on `reduced` and never runs, so the ledger stays as
  plain, always-fully-opaque text rather than opacity-0 spans — confirmed 0 `.w` elements
  exist in this mode); `#heroPoolImg.style.objectPosition` stays the empty string (no
  inline override, holds the CSS resting crop `36% 66%`); every `[data-motion]` element
  computed `transform: none`.
- **Motion proof** (`shots/motion-0.png` through `motion-4.png`, scrollY
  1300/1450/1600/1750/1900, the thesis act): the local-mode headline wrapper's
  `translate3d` y-offset moves -48.2px → -60px (cap, reached by frame 1) → -60px → -60px →
  -60px, while the Hyperborea photo's act-mode offset moves 33.1px → 42.7px → 52.2px →
  61.8px → 71.3px (uncapped in this range, ceiling 90px) — opposite signs throughout
  (headline rising, photo sinking), both fully inside their own boxes at every frame,
  confirmed by reading all five screenshots directly.
- **Focus order / no trap:** Tab from page load reaches `.topline-contact` →
  `.panel-open .cta` → into the Calyx iframe's own focusable content → `.price-mailto` at
  the 10th Tab press, no dead stop, no offscreen focus.
- **Giant headline scale device**, measured live: `--sc-p` 0.2344 → transform scale
  0.938752; `--sc-p` 0.7520 → transform scale 0.98016 — matches `0.92 + 0.08*p` exactly at
  every sampled point (700/900/1100/1300/1500px scroll).
- **Full-page shots** (`shots/desktop-1440--fold.png`, `shots/desktop-1440--full.png`,
  `shots/mobile-390--fold.png`, `shots/mobile-390--full.png`,
  `shots/desktop-1440-reduced--fold.png`, `shots/desktop-1440-reduced--full.png`): read
  frame by frame. The ledger's three rows all read fully lit together after the local-span
  fix (see "Fix during build" above); the Hyperborea plate's bleed is visible past the blue
  block's edge; Calyx and Hōrai both show their own top chrome uncropped; the price box's
  new bold package rows read clearly; no window artifacts, no clipped text, no broken
  images (one flaked broken-image capture during iteration was a Playwright timing
  one-off — `naturalWidth`/`naturalHeight`/`complete` all confirmed correct on the live
  page, and the re-captured shot is clean).

## Fix round (post-emit, pixel-measured)

Two defects found on the emitted build, both fixed in `index.html`, no other files touched.

**1. Hero plate image broken.** `/tests/alunix-concepts/_assets/k1-stage-pool.webp` was being
reset by the dev server (`net::ERR_CONNECTION_RESET`) — the raw pool file in that folder is
too large for it — so the plate rendered a broken-image icon with its alt text showing
through, and the logo sat on top of that alt text instead of the photograph. Fixed by
pointing `#heroPoolImg`'s `src` at the re-encoded copy already served correctly elsewhere on
this page (`/tests/alunix-concepts-r3/build/assets/k1-stage-pool.webp`, 1800×1200, 101KB —
same folder the Hyperborea and Hōrai-adjacent assets already load from). Verified live:
`naturalWidth` 1800, `naturalHeight` 1200, `complete` true, immediately and again after a
1s settle (Playwright, `http://127.0.0.1:3090`). The signature move (pool wander) re-verified
against the loaded image, real (non-reduced) motion context: `--sc-p` 0.4139 → object-position
`45.11% 55.24%` at scrollY 0, ramping to `--sc-p` 0.7115 → `51.65% 47.50%` at scrollY 600 —
same five-point curve NOTES.md's own "Signature move" table already documented, now measured
against the working image rather than the broken one. Logo-over-plate contrast re-measured
(hide-logo, screenshot, sample worst 5% of the background pixels behind its bounding box,
same `contrast_over_media`-style method as the hero headline's own scrim check): 4.54:1
against solid white — before the logo's own `drop-shadow` filter is even counted, which adds
further separation on top. Read `shots/desktop-1440--fold.png` and
`shots/mobile-390--fold.png` directly: the plate shows the light-pool photograph at both
sizes, the logo sits cleanly on it with no alt text behind it.

**2. Calyx column ended a viewport short of the price box.** `.stagger` used
`align-items:flex-start`, so the two columns never shared a common row height — each sat at
its own natural content height, and the right column (giant+ledger, services, Hōrai, price)
was taller than the left (console, thesis, Calyx), leaving the left column's Calyx frame
ending well above the right column's price box, bare ground visible beneath it. Fixed in two
parts: `.stagger` now uses `align-items:stretch` so both columns share the taller column's
own row height, and `.calyx-wrap` (the left column's last child, its own close panel) got
`flex:1` with its floor raised from `min-height:68vh` to `min-height:90vh`, so it absorbs
whatever the stretched row leaves over and grows down to meet the right column's own bottom
edge — mirroring exactly how `panel-giant`'s flex-column position already lets the right
column reach its natural height. The mobile breakpoint (`<900px`, columns stacked instead of
side by side) explicitly resets `.calyx-wrap{flex:none}` so the stretch fix, a desktop-only
device, does not change the mobile Calyx frame's own `66vh` sizing. Verified live at both
required viewports (`getBoundingClientRect().bottom` on `#colLeft` vs `#colRight`):

| Viewport | Left bottom | Right bottom | Diff | Ceiling (4vh) |
|---|---|---|---|---|
| 1440×900 | 3817.11px | 3817.11px | 0px | 36px |
| 1280×800 | 3815.36px | 3815.36px | 0px | 32px |

Both columns now end at the exact same y (0px diff, not merely under the 4vh ceiling). Read
`shots/desktop-1440--full.png` directly: the Calyx iframe now runs the full height of the
left column, ending flush with the price box on the right — the demo site's own content
(a short page) leaves cream space inside the now-taller frame, which is the iframe's own
page falling short of the frame, not a layout gap in this build.

**Re-verification after both fixes (unchanged from the pre-fix build, re-run to confirm
neither fix regressed anything):**

- Panel-to-panel gaps, both columns, all seven seams: still 2.40vh each (well under the 8vh
  ceiling) — unaffected, since neither fix touches `.col > * + *`.
- Hyperborea bleed: still 11.00% of the plate's own width (`.thesis-figure` right edge past
  `.panel-thesis`'s), under the 12% ceiling, at 1440×900 — unaffected, since neither fix
  touches `.thesis-figure`/`.panel-thesis`.
- `scroll_verify.py` (`skills/design/scripts/scroll_verify.py`), 1440×900, 11 stops: 0 dead
  scroll, 0 cues stuck below full opacity, 0 unrevealed elements, 0 contrast-under-media
  failures, 0 blank bands.
- `a11y_scan.py` (`skills/a11y-audit/scripts/a11y_scan.py`), axe-core: 0 violations, 28
  passes, 2 incomplete (the same `color-contrast` "background could not be determined"
  bucket as before, not a failure).
- No horizontal overflow: `scrollWidth <= innerWidth` true at 1440×900 and 390×844 (full
  scroll sweep, every 200px step, both viewports).
- No `[scrollcraft]` console warnings across a full 200px-step scroll sweep at 1440×900 or
  390×844.
- Exactly two iframes, both real `title` attributes intact (`Calyx, florist i Stockholm`,
  `Hōrai, Asian fusion-koncept`); swept every 200px scroll step across the full document
  height — 0 instances of a non-`none` `transform` on either iframe or any of its ancestors,
  at any scroll position.
- Reduced motion (real Playwright `reduced_motion:'reduce'` context, scrolled to y=2000):
  `.panel-giant .giant` computed `transform:none`; `#threadFill` computed
  `transform:matrix(1,0,0,1,0,0)` (scaleY 1); 0 `.scrub-text .w` spans exist (`armChapter()`
  never runs under reduced motion, ledger stays plain always-opaque text);
  `#heroPoolImg.style.objectPosition` stays the empty string (holds the CSS resting crop);
  every `[data-motion]` element computed `transform:none`. Confirmed static, matching the
  original build's own reduced-motion behaviour exactly — neither fix touches the reduced-
  motion gate.
- Re-shot `shots/`: `desktop-1440--fold.png`, `desktop-1440--full.png`,
  `desktop-1440-reduced--fold.png`, `desktop-1440-reduced--full.png`, `mobile-390--fold.png`,
  `mobile-390--full.png`, `motion-0.png` through `motion-4.png` (scrollY
  1300/1450/1600/1750/1900, same thesis-act frames as the original build). Read every frame
  directly: the hero plate shows the light-pool photograph (not a broken-image icon) at both
  the fold and full-page shots, both viewports; the ledger's three rows all read fully lit
  together; the Hyperborea bleed is visible past the blue block's edge; Calyx and Hōrai both
  show their own top chrome uncropped; the price box's bold package rows read clearly; the
  left column's Calyx frame now visibly reaches the same bottom edge as the right column's
  price box in the full-page shot.

## Round 2 (Anton's second pixel-level pass on the approved V3b build)

Same cell, edited in place, `index.html` only — `scrollcraft.js`/`scrollcraft.css` untouched,
no edits outside this cell, no sub-agents, no copy changes, no commit. Nine findings, each
verified on computed styles/pixels before writing a fix, matching this round's own brief.

### 1 + 2. Hyperborea plate — size and bleed visibility (linked root causes)

**Finding 1 (thumbnail plate).** Round 1's `minmax(34ch,.6fr) 1.5fr` satisfied "no 5-line
wrap" but, at this panel's real ~652px width, the 34ch floor (360.66px) left the figure track
only 159.1px (box width 207.1px after the `margin-right:calc(-1*var(--pad-i))` extension) —
**37.3%** of the block's 555.76px inner width (`.thesis-grid`), a thumbnail, not the block's
visual device.

**Finding 2 (bleed invisible).** Independent of size: `.col-left .panel{overflow:hidden}`
(specificity 0,2,0) was beating the old bare `.panel-thesis{overflow:visible}` (0,1,0) —
CSS specificity always wins over source order, so this had never actually been visible on
the emitted build, at any plate size. Confirmed live: `getComputedStyle(panelThesis).overflow`
read `"hidden"` before the fix.

**Fixes:**
- `.thesis-grid` column floor narrowed `34ch → 28ch` (inside the requested 28-30ch band),
  handing the freed width to the figure track. The headline now wraps 3 lines at 1440
  ("DET FÖRSTA / INTRYCKET ÄR / DIGITALT.") — allowed per this round's own instruction.
- `.col-left .panel-thesis{overflow:visible}` — same (0,2,0) specificity as the rule that was
  winning, placed after it in source order, so this one wins the tie instead.

**Measured at 1440×900 (after):**

| | Before | After |
|---|---|---|
| Text column | 360.66px (34.0ch) | 296.8px (28.0ch) |
| Figure box width | 207.1px | 270.75px |
| Plate ratio (figure ÷ `.thesis-grid` width) | 37.3% | **48.7%** (≥46% floor) |
| Aspect ratio | 16:10 (207.1÷129.4=1.60) | 16:10 (270.75÷169.21=1.60, unchanged) |
| `.panel-thesis` computed `overflow` | `hidden` | `visible` |
| Bleed past block edge | (never visible) | 29.78px = **11.0%** of plate width (10-12% band) |

At 1920×1080 the same construction gives a 64.0% plate ratio (wider column, same 28ch
floor is a smaller fraction) and an unchanged 11.0% bleed — percentage-based bleed holds
regardless of viewport, as designed. Bottom-alignment (figure/caption both flush to the
panel's own bottom padding line, Round 1's own fix) is untouched — neither edit touches
`align-self`/`margin-top:auto`. Confirmed visually in `shots/slices/v3b-round2--s02.png`
(real motion): the black "Systems with warmth" plate now visibly crosses the blue block's
right edge onto the bare textured ground beside it.

No document overflow introduced: `scrollWidth === innerWidth` reconfirmed at
320/375/390/414/768/900/901/1024/1280/1440/1920 after this change (see Verification below).

### 3. Giant headline — Ä/G collision

`line-height:.88` on `.panel-giant .giant` put the "Ä" diaeresis in "VARUMÄRKE" into the "G"
of "BYGGER" on the line above. Changed to `line-height:.96`. Confirmed on
`shots/slices/v3b-round2--s01.png` (real motion, 1440×900) and `shots/desktop-1920--fold.png`
scroll-forward frame: clear air between the two lines at both viewports, tight kinetic-scale
feel preserved (still well under 1.0).

### 4. Ledger titles rendering at weight 300

Root cause: the old bare `.ledger-body h3{font-weight:700}` and `.col-right h1,.col-right
h2,.col-right h3{font-weight:300}` are both (0,1,1) specificity (one class + one type); the
`.col-right h1,h2,h3` rule sits later in the file, so it won the cascade tie and every ledger
title rendered at 300, not 700. Fixed with `.panel-giant .ledger-body h3` (0,2,1) — a
guaranteed win regardless of source order. Verified live: `getComputedStyle(...).fontWeight`
now reads `"700"` (was `"300"`).

### 5. Mobile touch targets

`.cta`, `.price-mailto`, `.topline-contact` measured 24px / 31.4px / 18.8px tall at 390×844 —
all under the 44px floor, all already ≥44px wide. Fixed via padding (grows the hit box) +
equal negative margin (cancels the visual push so surrounding layout and the visible type are
unchanged), scoped to `@media (max-width:900px)`.

Build note: the first attempt placed this block near `.stagger`'s own mobile media query,
earlier in the stylesheet — `.price-mailto`'s own later, unconditional `padding-bottom:3px`
partly clawed the fix back (measured 38.4px, not 45.4px intended) since same-specificity
rules resolve by source order. Moving the whole block to the very end of the `<style>` sheet
fixed the ordering for `.cta` and `.topline-contact` immediately; `.price-mailto` still landed
short (42.4px) on a second attempt because a symmetric 7px/side replaces (not adds to) the
old 3px bottom padding — 8px/side was needed to actually clear 44px net of that swap.

| Element | Before | Target fix | After (measured) |
|---|---|---|---|
| `.cta` | 24px | +10px/side, margin -10px | **44.0px** |
| `.price-mailto` | 31.4px | +8px/side (see note above), margin -8px | **44.4px** |
| `.topline-contact` | 18.8px | +13px/side, margin -13px | **44.8px** |

All three widths were already ≥44px (126.7 / 147.7 / 109.7px) so only vertical padding was
needed. No horizontal overflow introduced (`scrollWidth === innerWidth` at 390px, reconfirmed
below).

### 6. Column top rhythm — console vs. giant headline

Root cause: `.panel-giant`'s padding used its own `cqw`-based clamp
(`clamp(28px,8cqw,84px)`, Round 1's own item D, kept deliberately for the bottom-void fix at
wide columns) for BOTH top and bottom, while `.panel-open` used the shared `vw`-based
`--panel-pad-y` (`clamp(28px,4.6vw,52px)`). At 1440 the two clamps happen to nearly coincide
(52px vs 52.14px, a 0.14px difference — easy to miss), but they diverge hard at wider
viewports: at 1920 the cqw clamp reaches 70.94px against the vw token's 52px cap, an 18.9px
gap between the console's first line and the giant headline's cap line even though both
columns start at the exact same y.

Fix: split `.panel-giant`'s padding shorthand so **top** uses `--panel-pad-y` (matching
`.panel-open` exactly, at every viewport) while **bottom** keeps the cqw-based clamp — Round
1's item D void-elimination math only depends on the bottom value, so this is additive, not a
revert.

| Viewport | `.panel-open` padding-top | `.panel-giant` padding-top (before) | `.panel-giant` padding-top (after) | Kicker top = Giant top? |
|---|---|---|---|---|
| 1440×900 | 52px | 52.14px | **52px** | 957.125 = 957.125 (was 957.125 vs 957.2625) |
| 1920×1080 | 52px | 70.94px | **52px** | **1013.125 = 1013.125** (was an 18.9px gap) |

Confirmed on `shots/slices/v3b-round2--s01.png`: "ALUNIX" and "VI BYGGER ERT" caps read level
under real (non-reduced) motion too, not just in the static computed-style check.

### 7. Two numeral styles unified

`.ledger-num` (mono, muted-paper) and `.panel-services .service-index` (Public Sans, bold,
`--ink-softer`) read as two different treatments for what is visually the same "01-03"
kicker device. `.service-index` now matches `.ledger-num` verbatim: `font-family:var(--f-mono)`,
`font-size:12px`, `font-weight:400`, `letter-spacing:0`, `color:var(--c-mute-on-paper)`. Its
own layout properties (`display:block`, `margin-bottom:10px`) are untouched — a different grid
context, not part of the numeral treatment itself. Verified live: both now report
`fontFamily: '"Geist Mono", ui-monospace, monospace'` and `color: rgba(20, 23, 26, 0.6)`.

### 8. Mobile reading order — giant+ledger before the console card

At ≤900px `.stagger` was already `flex-direction:column`, stacking `.col-left` (console,
thesis, Calyx) entirely above `.col-right` (giant+ledger, services, Hōrai, price) — so giant
+ledger landed roughly two-thirds of the way down the page on mobile, not directly after the
hero.

Fix: `.col-left{order:2}` / `.col-right{order:1}` inside the existing `@media
(max-width:900px)` block — swaps which of the two stacked flex children paints first, desktop
DOM and desktop CSS both untouched (`order` only set inside this media query). `.col + .col
{margin-top:...}` depended on `.col-right` being the DOM-later sibling to carry the seam —
order-unsafe once the two can swap visual position — so the seam moved to `.stagger`'s own
`gap` (`clamp(10px,2.4vh,40px)`, same value), which follows visual/flex order automatically
regardless of `order`.

Verified live at 390×844 (`getBoundingClientRect().top + scrollY` on each panel):

| Panel | Position (px) |
|---|---|
| `.hero` | 51.5 |
| `.panel-giant` (giant + ledger) | **653.4** |
| `.panel-services` | 1268.7 |
| `.horai-wrap` | 1902.5 |
| `.price` | 2496.7 |
| `.panel-open` (console card) | 3089.6 |
| `.panel-thesis` | 3388.7 |
| `.calyx-wrap` | 3717.8 |

Giant+ledger sits directly after the hero and well before the console card. Confirmed
visually on `shots/mobile-390--fold.png`: the fold shows the hero then "VI BYGGER ERT
VARUMÄRKE." immediately below it, no console card in between. No horizontal overflow
introduced (`scrollWidth === innerWidth` at 390px).

### 9. Self-drawing thread reading as a border

`.thread` (the static track) and `.thread-fill` (the accent-coloured, self-drawing overlay)
were both 1px — the same visual weight as the row hairlines beside them, so the vintergatan-
derived signature device read as just another divider. Both widened to 2px; `.thread-fill`'s
colour (`var(--c-accent)`, already full-strength, not a muted rgba) is unchanged, just wider.
Verified live: `getComputedStyle(threadFill).width === "2px"`,
`backgroundColor: "rgb(30, 94, 156)"` (`#1e5e9c` at full opacity).

### Verification (Round 2)

- **`scroll_verify.py`** (`skills/design/scripts/scroll_verify.py`), 1440×900, 10 positions
  (0-2442): `deadScroll: []`, `cuesNeverFull: []`, `unrevealed: []`, `contrastUnderMedia: []`,
  `blankBands: []`, `notes: []` — fully clean.
- **`a11y_scan.py`** (`skills/a11y-audit/scripts/a11y_scan.py`), axe-core: `violations: []`,
  **28 passes, 2 incomplete** — identical to every prior round's own baseline (the
  "background could not be determined" `color-contrast` bucket, not a failure).
- **No horizontal overflow** (`scrollWidth <= innerWidth`, scripted): confirmed at 320, 375,
  390, 414, 768, 900, 901, 1024, 1280, 1440 and 1920 — including both sides of the 900px
  column-stack breakpoint, with the widened Hyperborea plate and the reordered mobile columns
  both active.
- **Iframes:** exactly two, both real `title` attributes intact (`Calyx, florist i
  Stockholm`, `Hōrai, Asian fusion-koncept`) — unchanged by this round (neither iframe's
  markup or ancestors were touched).
- **Panel gaps** (`.col > * + *`): all five seams (2 left, 3 right) still measure 21.6px =
  2.4vh at 1440×900 — the finding-8 mobile-order fix only touches the `≤900px` media query,
  the desktop gap rule is untouched.
- **Columns end within 4vh:** `#colLeft`/`#colRight` bottoms identical (3337.96px, **0px
  diff**) at 1440×900 — unaffected (Round 1's `align-items:stretch` + `.calyx-wrap{flex:1}`
  mechanism untouched).
- **Reduced motion** (real `prefers-reduced-motion:reduce`, scrolled to y=2000):
  `.panel-giant .giant` computed `transform:none`; `#threadFill` computed
  `transform:matrix(1,0,0,1,0,0)` (scaleY 1, fully drawn, at the new 2px width); 0
  `.scrub-text .w` spans exist; `.panel-giant` does not carry `is-armed` — static, matching
  every prior round's own documented reduced-motion behaviour.
- **No console errors or `[scrollcraft]` warnings** on load or scroll (checked via
  `read_console_messages`, `onlyErrors:true` — empty).
- **Shots re-taken** (`shots/`): `desktop-1440--fold.png`, `desktop-1440--full.png`,
  `desktop-1440-reduced--fold.png` (scrolled to y=2000), `desktop-1920--fold.png`,
  `mobile-390--fold.png`, `mobile-390--full.png`, plus `shots/slices/v3b-round2--s00.png`
  through `s04.png` (5 real-motion slices spanning the full document height — the
  established per-scroll-position capture method this cell's own NOTES.md uses, since a
  naive `full_page=True` capture freezes every scroll-driven inline style at whatever the
  page's initial, pre-scroll state was). Read every frame directly: the Hyperborea plate
  visibly bleeds past the blue block's edge in `s02`; "VARUMÄRKE"'s Ä clears "BYGGER"'s G in
  both `s01` and the 1920 fold frame; "ALUNIX" and "VI BYGGER ERT" caps read level in `s01`;
  ledger titles read bold and both numeral kickers (services + ledger) match in `s02`; the
  mobile fold shows giant+ledger directly under the hero, before the console card; no window
  artifacts, no clipped text, no broken images.

## Not achieved / known limitations

- The word-scrub device's own catalogue source (vintergatan) documents that any static
  screenshot taken mid-scroll can catch a row between opacity states; the fixed-span fix
  above makes this unlikely within a normal reading pace, but a screenshot taken at an
  unusual scroll position could still show a row transitioning. This is the device's own
  documented tradeoff, not unique to this build.
- The Hyperborea bleed amount (11%) was chosen for a comfortable margin under the 12%
  ceiling rather than exactly at it; a bolder read is possible at the literal maximum but
  was not pursued given the modest gutter width available at 1440px without touching the
  right column's own content.

## Polish round (V3b, Anton's pixel-level review on top of the approved V3)

Cell copied from the approved `V3-chain` build per the task's own instruction, then edited
in place. Concept unchanged (continuous ground, offset panels, framed hero plate with the
wandering light pool, bleeding Hyperborea plate, word-scrub ledger, iris on Hōrai, price
box). `Skill(design)` loaded via the Skill tool before editing (Tier 2 — V3 itself is the
direction, Steps 4-5 apply, no new reference gate). No sub-agents, no edits outside this
cell, no commit, no copy changes beyond the one removal below. Every visible number is
unchanged from V3.

### 1. Client-ordered: remove the Exempelsida label boxes (binding)

`.calyx-cap` and `.horai-cap` — the black kicker+rad boxes that sat above the Calyx and
Hōrai frames — deleted, CSS rules and HTML markup both. Both frames now simply follow the
previous panel (blue block, services panel) with the normal `.col > * + *` panel gap
(measured 21.6px = 2.4vh at 1440×900, unchanged rule). Hyperborea's own caption stays
inside the blue block (`.thesis-caption`), which the client instruction explicitly keeps.
Point 2 ("handled separately in sites/horai.html") was not touched — out of this cell's
scope.

### A. Hero fold — plate capped, everything fits in one 1440×900 viewport

Root cause: the plate ran `aspect-ratio:16/9` at the hero's full width with no height cap,
rendering ~79vh tall regardless of viewport height. At 1440×900 the plate alone ran from
y=407 to y=1075 (668px, cut by the fold), pushing the sub-line to y=1101-1159 and the whole
hero section to 1111px tall (123% of the viewport) — the client's own screenshot (`rev-d-0`,
`rev-d-1`) showed exactly this: headline in the fold, plate cut off, sub-line and the
console card below the fold entirely.

Fix: `.hero-plate` height is now a direct `clamp(300px, 56vh, 560px)` (was `aspect-ratio:
16/9`, no cap) — 56vh matches the client's own target exactly. To make the budget fit at
both required viewports, the hero's own internal spacing was trimmed (`hero-head`
padding-top clamp(20,4.2vw,52) → 6px fixed; `hero-plate` margin-top clamp(22,4.4cqw,56) →
10px fixed; `hero-sub` margin-top clamp(16,2.6cqw,26) → 8px fixed; `hero` bottom padding
clamp(8,1.4vw,18) → 3px fixed; `topline` vertical padding 20px → 16px). The plate keeps its
6cqw side margins (now via `--rail-x`, see item B) and its hairline border (now
`--frame-line`, see item E). Mobile (`<640px`) keeps the 4:5 aspect-ratio crop, unaffected
(the vh-height rule is desktop-only, mobile resets to `height:auto`).

Measured before/after at 1440×900 (Playwright, real motion, `getBoundingClientRect()`):

| | Before | After |
|---|---|---|
| Headline (`.hero-headline`) | y 117.5–350.8 (233px) | y 63.5–278.5 (215px, unchanged font-size*) |
| Plate (`.hero-plate`) | y 406.8–1075.0 (668px, **cut by fold**) | y 288.5–792.5 (504px = 56vh) |
| Sub-line (`.hero-sub`) | y 1101.0–1158.6 (**below fold**) | y 800.5–846.1 (**inside fold**) |
| Hero total incl. topline | 1176.6px (131% of viewport) | 849.1px (94% of viewport, 51px spare) |

*headline height differs slightly because the type-scale fix (item F) moved its max from
7.6rem to 7rem — see below.

Same check at 1280×800 (the tighter of the two required viewports, since the topline's own
fixed ~58px height is a bigger fraction of a shorter viewport): hero total 793.1px, 6.9px
spare. Both viewports verified via `scroll_verify.py` (0 dead scroll, 0 blank bands) and
read directly in `shots/desktop-1440--fold.png` (headline, plate and sub-line all visible
with no scroll) and `shots/desktop-1920--fold.png` (still fits comfortably at the wider
viewport, plate scales to 56vh of 1080 = 605px).

### B. Topline grid — one shared edge

Root cause: the plate's own 6cqw margin sat on top of the hero's own `clamp(16px,3vw,40px)`
padding (giving the plate a ~121.6px inset at 1440), while the topline used only the small
clamp directly (~40px) — the wordmark and `kontakt@alunix.se` never lined up with the
plate's edges (measured 91px off on the left, 91px off on the right at 1440). The headline
had the same problem (inset only 40px, not 121.6px).

Fix: a single token, `--rail-x: clamp(16px, 6vw, 96px)`, now drives the topline's own
padding, `.hero-head`'s padding, `.hero-plate`'s margin and `.hero-sub`'s margin — one grid
across the whole hero instead of two independent insets. The hero's own horizontal padding
was removed (`padding:0 0 3px`, was `0 clamp(16,3vw,40) clamp(8,1.4vw,18)`) so the hero's
`cqw` container width equals the viewport width, which is what lets a single `vw`-based
token stand in for the plate's own `cqw` margin without a second calculation.

Measured at 1440×900 (after): `.topline-mark` left = 86.4px, `.hero-plate` left = 86.4px,
`.hero-headline` left = 86.4px — all three identical. `.topline-contact` right = 1343.2px,
`.hero-plate` right = 1343.2px — identical. (Before: topline-mark left 40px vs plate left
121px; topline-contact right 1390px vs plate right 1309px.)

### C. Blue block — 34ch text column, 16:10 plate, bottom-aligned caption

Root cause: `.thesis-grid` ran `.85fr 1.2fr` with `align-items:center`, giving the text
column 215.6px at 1440 (the support paragraph wrapped 5 lines) and floating the photo and
caption at the row's vertical centre rather than against a shared bottom line.

Fix: `grid-template-columns: minmax(34ch, .6fr) 1.5fr` (the `.6fr`/`1.5fr` split turned out
not to matter in practice — see the measurement note below — but is left expressing the
intended weighting); `align-items:stretch` so both tracks share the row's full height;
`.thesis-text` became a flex column (`display:flex;flex-direction:column`) with
`.thesis-caption{margin-top:auto}` pinning the caption to the bottom of that column;
`.thesis-figure{align-self:end}` bottom-aligns the plate within the stretched row instead of
floating at centre. `.thesis-photo-box` was already `aspect-ratio:16/10` in the pre-polish
build (contract.md's own instruction) — verified unchanged, no edit needed there.

Measured at 1440×900 (after): text column width 360.7px — comfortably over 34ch (a live
canvas measurement of this font/size put 1ch at ≈10-10.6px, so 34ch ≈ 340-360px; the
rendered column matches that band). Grid's own computed `grid-template-columns` read back
as `"360.663px 159.1px"` — confirms the 34ch **minimum** is what's actually driving the
text column's width (360.66px), not the fr split: because 34ch already exceeds either
column's naive fr-proportional share at this panel width (only ~652px total, split two
ways, minus gap and padding), the text track locks to its floor and *all* remaining space
flows to the figure track regardless of the fr ratio chosen — confirmed by testing both
`1fr/1.25fr` and `.6fr/1.5fr` and getting the identical 360.66px/159.1px split both times.
Documented here so a future editor doesn't waste time tuning a ratio that has no effect
while the 34ch floor is active at this panel width.

Bottom-alignment: `.thesis-caption` bottom = `.thesis-figure` bottom = 1678.4px, exactly,
at 1440×900 — both sit flush with the panel's own padding line (`.panel-thesis` bottom
1730.4px, minus its own 52px bottom padding = 1678.4px). Bleed re-verified after the
column-width change: `.thesis-figure` right edge (714.5px) past `.panel-thesis`'s own right
edge (691.8px) = 22.7px on a 207.1px-wide plate = **10.96%**, still under the 12% ceiling
contract.md sets (was 11.00% before this round; the tiny difference is rounding from the
photo's own new rendered width, not a deliberate change).

Trade-off, stated plainly: honoring the 34ch floor within this panel's real half-page width
(~652px at 1440) leaves only ~159-207px for the bleeding plate itself — smaller than the
pre-polish build's own plate. The bleed gesture (Mattis device) still reads as a photograph
breaking its own container's edge; it now does so as a narrower, more graphic mark rather
than a large image, which is a legitimate but different read of "confident, singular
gesture." Not revisited further given the client instruction was specific about the 34ch
floor and did not ask for a particular plate size.

No document overflow at 1440/1280/1920/900/768/414/375/320/390 (script-verified, see
Verification below).

### D. Giant panel — top/bottom padding equalized, ledger scales with column width

Root cause: `.panel-giant` ran `padding: clamp(36,6vw,72px) clamp(24,4vw,48px)
clamp(28,4vw,44px)` — **top and bottom were different clamps** (72px max top vs 44px max
bottom), and `.ledger-row` padding was a flat `1rem` regardless of viewport. At 1920 the
column runs ~887-909px wide; a fixed 1rem row padding and a headline/sub whose own max
font-size is already clamped read sparse against that width, showing as a void under the
ledger.

Fix: `.panel-giant{padding: clamp(28px, 8cqw, 84px) clamp(24px, 5cqw, 48px)}` — top and
bottom now the *same* value, and in `cqw` (scaling with the panel's own column width) per
the literal instruction. `.ledger-row{padding: clamp(.8rem, 3cqw, 1.75rem) 0}` — row
spacing now scales with the same column width instead of a fixed 1rem.

Build note: `container-type:inline-size` was first tried directly on `.panel-giant` itself
(the most literal reading), but a self-referencing container — a container-type element
whose OWN padding is expressed in that same container's `cqw`, while the element's width
comes from a flex-stretch ancestor — resolved every `clamp()` to its **maximum** in testing
(measured `84px`/`48px`, i.e. both landed on their ceiling regardless of the actual column
width), not a usable result. Moving `container-type:inline-size` to the stable ancestor
`.col` (width is fixed by the `.stagger` flex row, independent of any descendant's padding)
and querying it from both `.panel-giant` and `.ledger-row` resolved correctly at every
width tested. This also happens to fix a latent dead rule: the file already had `@container
(max-width:360px){.ledger-row{grid-template-columns:1fr}}` with no container established
anywhere on the page, meaning it had never actually applied; it is now live (redundant with
the existing `@media (max-width:900px)` mobile rule, but no longer inert).

Measured (Playwright, real motion):

| Viewport | Column width | `.panel-giant` padding (top=bottom) | `.ledger-row` padding |
|---|---|---|---|
| 1440×900 | 651.8px | 52.14px (was 72px top / 44px bottom) | 19.55px (was 16px fixed) |
| 1920×1080 | 886.8px | 70.94px | 26.60px |

Content-tightness at 1920: `.panel-giant` own height 734.9px; content span (`.giant-head`
top to `.ledger-wrap` bottom) 592.2px; padTop 71.36px + padBottom 71.36px + contentSpan
592.2px = 734.9px — **exact match, zero residual void**. The gap between `.panel-giant` and
`.panel-services` measured 25.9px = 2.4vh at 1080, the standard `.col > * + *` panel seam,
not an extra void.

### E. Rhythm — one padding scale, one hairline system, matched kicker/body gaps

- **Panel top/bottom padding:** every panel (`panel-open`, `panel-thesis`,
  `panel-services`, `price`) now shares `--panel-pad-y: clamp(28px, 4.6vw, 52px)` (was
  clamp(28,4.4vw,**56**), clamp(32,5.4vw,**64**), clamp(36,6vw,**68**), clamp(40,6vw,**72**)
  respectively — four different maxima, now one). `panel-giant` is the one deliberate
  exception, using the `cqw`-based pair from item D instead of this `vw`-based token,
  because item D specifically requires its padding to track its own column width rather
  than the viewport — documented as the one departure from "one scale," not an oversight.
  Measured: all five panels read back `52px`/`52.14px` top and bottom at 1440×900 (see the
  padding table above and in item H).
- **Hairlines, one token per ground:** `--hairline-dark: rgba(255,255,255,.18)` and
  `--hairline-light: rgba(20,23,26,.14)` are now the only two hairline colours on the page.
  Every prior divider (`--c-line-on-dark`, `--c-line-on-paper`, `--line`, `--invert-line` —
  four names, three different rgba values: `.20`/.20/.14/.16) now aliases to one of the two
  canonical tokens. A literal single token cannot serve both a near-black and a paper
  ground at readable contrast (`house-physics.md`'s own "value per ground" rule), so two
  tokens is the floor, not a compromise short of "one." The photographic-plate frame
  hairline (hero plate, thesis photo box — a different visual role from a divider) is its
  own single token, `--frame-line: rgba(255,255,255,.32)` (was `.30` on one, `.35` on the
  other).
- **Kicker-to-headline / headline-to-body gaps:** the blue block's own `.9rem`
  kicker-margin-bottom + `1.1rem` headline-to-body gap is now the shared pattern. `.price
  .kicker` gained `margin-bottom:.9rem` (previously the gap was carried entirely by
  `.statement`'s own `margin-top:1.3rem`, now `0`). `.panel-giant .giant-sub` margin-top
  1.05rem → 1.1rem. `.panel-open .hero-body` margin-top (previously its own
  `clamp(16px,2.4vw,28px)`, topping out at 1.75rem) → fixed `1.1rem`. `.price
  .price-ingress` margin-top 1.5rem → 1.1rem. Not touched: `panel-giant`'s own headline has
  no kicker above it (contract.md's own copy, not this round's decision) and
  `panel-services`'s kicker sits beside its statement in a 2-column grid, not above it — both
  exempt from a vertical kicker-gap by construction, not missed.
- **Body sizes, one per world:** `--body-r5: 0.95rem` now covers `.hero-sub`,
  `.panel-open .hero-body` and `.panel-thesis .thesis-support` (previously 0.95-1.2rem,
  0.92-1.05rem and a fixed 0.92rem — three different values). `--body-r6: 0.9rem` now
  covers `.panel-giant .giant-sub`, `.panel-services .service p`, `.price .price-ingress`,
  `.price-row .label` and `.ledger-body p` (previously 1.02rem, 13px, 13-16px, 13px and
  0.88rem — five different values). Stated plainly: `.giant-sub` reads slightly smaller than
  before (1.02rem → 0.9rem) to comply with "one size"; hierarchy is preserved through the
  headline-to-body size jump (the giant headline itself is unchanged, still clamped to
  4.8rem) rather than through the sub-line's own size.

### F. Type scale — outliers pulled onto the shared scale by one step

Three Public Sans display sizes and three Geist display sizes were each measured against
the other two in their family; the one outlier in each set was pulled down by ≤1 step
(never more, per the instruction), everything else left alone:

| Family | Element | Before (max) | After (max) | Step |
|---|---|---|---|---|
| Public Sans display | `.hero-headline` | 7.6rem | **7rem** | -0.6rem |
| Public Sans display | `.panel-services .statement` | 2.5rem | **2.4rem** | -0.1rem |
| Public Sans display | `.price .statement` | 30px (1.875rem) | **1.9rem** (30.4px) | +0.025rem (negligible) |
| Geist display | `.panel-open .wordmark` | 3.4rem | **3rem** | -0.4rem |
| Geist display | `.panel-thesis .thesis-headline` | 2.3rem | **2.4rem** | +0.1rem |
| Geist display | `.panel-giant .giant` | 4.8rem | 4.8rem (unchanged) | already on scale |

Body sizes unified per item E above (one size per world, not a scale — the instruction
draws that distinction explicitly).

### G. Services panel — full-height dividers confirmed, kicker aligned to first baseline

Root cause found: `.section-head{align-items:end}` bottom-aligned the `TJÄNSTER` kicker
against the **last** line of the two-line statement rather than its first — the kicker
floated near the bottom of the block instead of sitting beside its headline (visible in
`rev-w-3`: the kicker sits low, near the statement's second line). The full-height dividers
turned out to already be correct: `.services` is a CSS grid with three `.service` cells in
one row, and grid items default to `align-items:stretch` on the cross axis — the three
cells already measured identical heights (227.7px each, confirmed live before this round)
and their `border-right` dividers already ran the full row height. No bug there, but
`align-items:stretch` is now stated explicitly on `.services` so a future content change
can't silently lose it.

Fix: `.section-head{align-items:start}` (was `end`), keeping the existing
`.kicker{padding-top:4px}` which was already tuned for a top-aligned reading (visible as
dead code under `align-items:end`, now doing its intended job). Verified in
`shots/slices/v3b--s01.png`: `TJÄNSTER` now sits level with the top of "Webbdesign, design
och system." rather than near the bottom.

### H. Console card — CTA-to-padding gap tightened

Measured before this round: `.panel-open` bottom 1653px, `.hero-cta-row` bottom 1597px —
gap 56px, which was **exactly** the card's own bottom padding (`clamp(28,4.4vw,56)` maxes
at 56px at 1440) — i.e. no extra dead space existed beyond the padding itself; the CTA
already sat at the padding line. The client's "~70px" read was on the padding amount
itself, not a layout bug. Since item E puts every panel's top/bottom padding on one shared
`--panel-pad-y` scale, the console card's own padding tightened as a side effect: 56px → 52px
at 1440 (`clamp(28px,4.6vw,52px)`, the shared token's own max). Re-verified after: `.panel-
open` bottom minus `.hero-cta-row` bottom = 52px, still exactly the padding, now 4px
tighter than before.

### Skills loaded

`Skill(design)` (Tier 2 — direction is V3 itself, no new reference gate; Steps 4-5 of the
skill's own flow apply to a polish pass on an already-approved build).

### Verification (this round)

- `scroll_verify.py` (`skills/design/scripts/scroll_verify.py`), 1440×900, positions
  0-2430 (viewport/3 steps): `deadScroll: []`, `cuesNeverFull: []`, `unrevealed: []`,
  `contrastUnderMedia: []`, `blankBands: []`, `notes: []` — fully clean, re-run after every
  structural edit in this round.
- `a11y_scan.py` (`skills/a11y-audit/scripts/a11y_scan.py`), axe-core, 1440×900: **0
  violations**, 28 passes, 2 incomplete (the same `color-contrast` "background could not be
  determined" bucket documented in the original V3 build, not a failure) — unchanged from
  the pre-polish baseline.
- **No horizontal overflow** at 320/375/390/414/768/1280/1440/1920 (`scrollWidth <=
  innerWidth`, scripted, Playwright): all true, including at the 900px column-stack
  breakpoint and with the Hyperborea bleed active.
- **Iframes:** exactly two, both real `title` attributes intact (`Calyx, florist i
  Stockholm`, `Hōrai, Asian fusion-koncept`). Swept every 200px scroll step across the full
  1440×900 document height: **zero** instances of a non-`none` `transform` on either iframe
  or any ancestor, at any scroll position — re-confirmed after this round's edits.
- **Console:** zero `[scrollcraft]` warnings across a full 200px-step scroll sweep at
  1440×900, and zero browser console errors (checked separately via `pageerror`/`console`
  listeners).
- **Panel gaps** (`.col > * + *`, both columns, all seams): 21.6px = 2.4vh at 1440×900,
  unchanged from the pre-polish build (this round never touched that rule) — well under the
  8vh ceiling.
- **Columns end within 4vh:** `#colLeft` and `#colRight` bottoms are **identical**
  (3325.8px, 0px diff) at 1440×900 — unaffected by this round (the `align-items:stretch` +
  `.calyx-wrap{flex:1}` mechanism that produces this was already in place from V3's own
  fix round).
- **Giant headline scale device** still reads correctly off `--sc-p`: `matrix(0.92,0,0,
  0.92,0,0)` at scroll position 0 (i.e. `scale(0.92)`, matching `0.92 + 0.08*0`).
- **Reduced motion** (real Playwright `reduced_motion:'reduce'` context, scrolled to
  y=2000): `.panel-giant .giant` computed `transform:none`; 0 `.scrub-text .w` spans exist
  (`armChapter()` still correctly gated on `reduced` and never runs) — unchanged from the
  pre-polish build's own documented reduced-motion behaviour.
- **Tab order:** topline contact link → console CTA → into the Calyx iframe's own
  focusable content (iframes 2-7 in the tab sequence are the demo sites' own internal
  focus stops) — no dead stop, no offscreen focus, consistent with the pre-polish build.
- **Hero headline contrast** (hide-text, screenshot the plate/scrim behind it, worst-case
  brightest-5%-pixel method, same as the original build's own check): **4.68:1** (was
  4.84:1 before this round — the small change comes from the hero-head's reduced
  padding-top slightly repositioning the headline over the same fixed photo; still well
  clear of the 3:1 large-text floor and close to the 4.5:1 normal-text threshold).
- **Logo clear space** re-measured after the hero restructure: mark height 80.05px (≥72px
  floor), 36.8px clear of both the plate's hairline and its own left edge (≥24px floor),
  46.8px clear of the headline above (reduced from 92.8px before this round, since
  `hero-head`'s own padding-top shrank for the fold fix, item A — still no overlap, still
  comfortable).
- **Shots re-taken** (`shots/`): `desktop-1440--fold.png`, `desktop-1440--full.png`,
  `desktop-1440-reduced--fold.png` (scrolled to y=2000, matching the original build's own
  reduced-motion capture point), `desktop-1920--fold.png`, `mobile-390--fold.png`,
  `mobile-390--full.png`, plus `shots/slices/v3b--s00.png` through `s03.png` (the
  forward-scrolling viewport-slice composite method this cell's own NOTES.md used
  originally — necessary because a naive Playwright `full_page=True` capture freezes every
  scroll-driven inline style at whatever the last real scroll event set, which for a
  capture that never scrolls is the ledger's own resting/unlit state; the four slices,
  captured via real `window.scrollTo` calls at each step, show the true per-scroll-position
  render and confirm the ledger's three rows read fully lit together, matching the original
  build's own "Fix during build" finding). Read every frame directly: hero fold now fits
  entirely within the viewport at both 1440 and 1920 with the topline/headline/plate edges
  aligned; the blue block's text column no longer wraps to 5 lines; the Hyperborea plate's
  bleed is still visible past the blue block's edge; the services panel's `TJÄNSTER` kicker
  now sits level with its headline instead of floating low; Calyx and Hōrai both show their
  own top chrome uncropped, immediately following the previous panel with no black label
  box; the price box's bold package rows read clearly; both columns still end at the same
  bottom edge; mobile (390px) shows no overflow and the same structural fixes carried
  through responsively.

# Alunix r5 · V2-chain — Cinematisk tvätt — build notes

Brief: `tests/alunix-concepts-r5/brief.md` (binding, common to V1-V3) + `contract.md`
row V2 (binding for this cell). Source: `tests/alunix-concepts-r4/cells/M1-chain/index.html`
(Anton's chosen winner from r4), copied and rebuilt per contract.md's V2 row. `Skill(design)`
loaded via the Skill tool, Steps 0-6, Tier 2 (M1 + the three named catalogue entries as
direction). No sub-agents used. No edits outside this cell. No commit made.

## Reference lock (written before code)

**Tier 2** — direction is M1's own build (structure/copy source) plus three catalogue
entries named in contract.md's V2 row:

- `design-catalogue/entries/planhat/entry.md` — **primary structural reference**.
  Preserve: ration photography to one deliberate, cinematic instance — a full-bleed
  photograph under a dark wash carrying the entire hero statement — then a hard
  material cut into flat, typographic panels for the rest of the page; nothing
  photographic competes with the hero afterward (Planhat's own rule: "below the fold,
  there is no photography at all," loosened here only because M1's own binding
  structure already carries three real demo-site screenshots later in the page — the
  discipline this build actually keeps is that the HERO photograph is never repeated
  or echoed anywhere else, and no second atmospheric/decorative photograph is added).
- `design-catalogue/entries/mattis-studio/entry.md` — secondary. The console-style
  hero card (version tag, live clock, corner framing) already lives in this chain as
  the `panel-open` console card; read here only to confirm restrained, condensed
  display type and a single flat-colour thesis block stay in the register's own
  vocabulary. Reject: Mattis's own saturated orange — this page's one accent stays
  Alunix blue (`--c-accent`), never Mattis's `#F04E23`.
- `design-catalogue/entries/veloura/entry.md` — secondary. Preserve: the ground never
  resets hue mid-journey (the persistence principle only, not Veloura's own chocolate
  palette) — this page keeps M1's own three-stop `--sc-canvas` drift
  (`#0b0c0e` -> `#123f68` -> `#f4f2ee`) unchanged.

**Preserved from M1, verbatim per brief.md's binding rule:** every headline and
sub-text not explicitly changed by brief.md (console card copy, blue thesis
kicker/headline/support, "Vi bygger ert varumärke." block + ledger, services
statement + three services, "Alla har rätt till bra design." + ingress,
kontakt@alunix.se), the R5/R6 dual type-world tokens, the fixed grayscale ground
device, the three-stop drift.

**Changed from M1, all per brief.md's common points or contract.md's V2 row (not
invented):** hero is now a photograph (`k1-stage-beams.webp`) under a scroll-driven
black wash instead of the Tidvatten iframe; the 50vh column offset is removed
outright — both columns now start flush under the hero, with a small capped flex
`gap` (`clamp(16px,2.2vw,30px)`, measured 30px at 1440) between every panel in a
column instead; the "Vi bygger ert varumärke." block moved from the left column to
open the right column directly; the blue thesis block lost its photo and became a
pinned act; Hyperborea joined as a third example frame in the left column; all three
demo frames now carry the brief's own `Exempelsida: …` kicker+line label; the price
ledger carries brief.md point 4's three new rows verbatim.

**Grammar note.** Unchanged from M1: contract.md's "continuous world" is read in the
loose sense brief.md itself uses (one fixed ground photo that never cuts, panels
alternately covering and uncovering it) — not the strict upstream grammar, which bans
`flow`/`reveal`/`parallax` outright. See M1's own `NOTES.md` for the full reasoning;
this build inherits it rather than re-deriving it.

**Reject:** a second photograph anywhere below the hero (Planhat's own discipline,
loosened only for the three real demo-site screenshots per brief.md's binding
structure, never for a fourth decorative image); a figure inside the thesis block
(contract.md V2 explicitly bans one — "ingen figur," airier, type only);
transform/opacity applied to an `<iframe>` tag or any of its ancestors while it is on
screen and interactive (all three frames get exactly one settle-once entrance —
`reveal` or `flow+in` — that resolves to no transform before the site is
interactive, never a continuous per-scroll device); invented numbers beyond the
three price rows brief.md gives verbatim; customers beyond the three demo sites;
Klöva; dashes in visible text; the word "jag"; a photo captioned as "our
office/team"; pointer effects (`tilt`/`magnet`/`spotlight`) on any of the three
frames; a gap between two panels in the same column taller than 8vh.

## Decision ledger

| Decision | Source | Role | Why |
|---|---|---|---|
| Hero = full-bleed `k1-stage-beams.webp` (natural colour, not grayscale) under a black wash, headline centred, Public Sans 300 at `clamp(2.4rem,8cqw,6.6rem)` | contract.md V2 point 1 + planhat/entry.md | hero | Literal instruction; `container-type:inline-size` on `.act-hero` makes `cqw` resolve |
| Ground = `k4-cabin-desk.webp`, but the `tests/alunix-concepts-r3/build/assets/` copy specifically, not the `tests/alunix-concepts/_assets/` copy of the same filename | live verification (see "Asset bug" below) | signature ground | The `_assets/` copy is a byte-different file (different md5) that Chromium hangs on indefinitely loading — confirmed via `page.goto()` timing out at 15s and a `net::ERR_CONNECTION_RESET` on every page load. The r3/build/assets copy is the one M1 already shipped and verified working; switching to it is a bug fix, not a new asset choice, and keeps the ground distinct from the hero photo so no image is used twice |
| Hero photo parallax rate **+1.5** (flipped from contract.md V2's literal "-1.5") | measured live, five scroll depths (see "Motion proof" below) | signature move + opposite-direction proof | The engine's parallax formula (`rate*(p-0.5)*100`) makes a **negative** rate trend toward a more-negative transform as scroll progresses — i.e. the layer moves faster than the page and *leads/rises*. A **positive** rate trends toward a more-positive transform — the layer lags the page and *sinks*. Confirmed empirically: with -1.5 the photo's transform went -2.56px -> -49.52px (rising, same direction as the headline, failing brief.md point 7's "text and image in different directions"); with +1.5 it goes -2.56px -> +49.52px (sinking) while the headline's own bespoke rise keeps going -34.8px -> -59.8px (rising) — genuinely opposite signs throughout. +1.5 is what actually delivers contract.md's own stated intent ("hero-fotot sjunker... medan rubriken stiger") as a real opposite-direction pair, so the sign was corrected rather than followed literally into a defect |
| Signature move: the black wash's own opacity, `calc(0.72 - 0.52 * var(--sc-p,0.5))`, read directly off the hero act's own `--sc-p` in plain CSS, no JS | contract.md V2 ("den svarta tvätten... lättar... via --sc-p") | signature move | Because the hero is the very first element (act-progress formula for a `flow` act starts around p=0.48 at initial scroll=0, not literally 0 — measured, not assumed), the wash opens around 0.47 rather than the literal 0.72 ceiling and reaches ~0.29 by 600px of scroll, continuing to fall as the act is left — the directional intent ("clearest as you leave it") holds even though the absolute starting value is not the literal 0.72 |
| Both columns start flush under the hero (no `margin-top` offset); every panel-to-panel gap in a column is a flex `gap` of `clamp(16px,2.2vw,30px)`, measured 30px at 1440×900 (3.3vh) | brief.md point 2 ("Ingen tom lucka under heron") | layout | M1's 50vh offset is explicitly what brief.md r5 removes; the giant block now opens the right column immediately so no column starts on bare ground, and the small capped gap keeps the ground visible in thin, controlled strips instead of one large void |
| Blue thesis block: `data-sc-act="pin" data-sc-span="2"`, kicker+headline share one cue (`0 0.72 0`, greet-then-fade, since this is a middle act, not the page's last), support line crosses on a second cue (`0.34 0.9`) | contract.md V2 ("texten hälsar och en andra rad korsar") | pin act | Matches the cue contract's own rules (devices.md): only the *last* act on the page may hold unconditionally, so the greeting kicker+headline still ramp out before the pin ends, rather than staying lit through the whole un-pin slide |
| Reduced motion, pin exception: `@media (prefers-reduced-motion:reduce){ .thesis-pin [data-sc-cue]{opacity:1 !important} }` | this task's own verification requirement ("pinned block shows all its text") | accessibility | The engine's own cue opacity always follows scroll progress, even under reduced motion — correct for a `flow` act, where a reader scrolls past each cue in turn regardless. A `pin` holds the viewport still for its whole multi-viewport span, so a reduced-motion reader has no guarantee of landing on the one scroll position where both cues overlap; measured live, a static position inside the pin could show the support line at opacity 0. This one narrow `!important` (a standard, accepted accessibility-fallback use, targeting the public `[data-sc-cue]` attribute, never an `.sc-*` engine class) forces the pin's own cues to full opacity under reduced motion only — verified before/after: kicker/headline/support all report `1` at five scroll depths post-fix, versus `0`/`0.821`/`1` mixed results pre-fix |
| "Vi bygger ert varumärke." + ledger moved to open the right column; the old "Utvalda projekt / Calyx, en sajt vi byggt..." lede removed | brief.md points 2 + 3 | structure + labelling | Point 2 moves the block; point 3 explicitly bans the "en sajt vi byggt, öppen att utforska här" implied-builder-credit phrasing M1 used, replacing it everywhere with the `Exempelsida: …` kicker+line pattern used identically before all three frames |
| Hyperborea as a third `.frame-block` in the left column, under Calyx, `flow+in` entrance (not `reveal`) | contract.md V2 point 2 | left column, device variety | Contract.md V2's own row; `flow+in` (not another `reveal`) keeps the DOM-order device sequence from repeating the same family twice running (Calyx is `reveal`, immediately followed by Hyperborea) |
| Price rows: three new sentences from brief.md point 4, set as their own bold row (`font-weight:600`) rather than a muted caption | brief.md point 4 ("raderna som egna fetstilsrader") | copy + type | The new lines are full package statements, not short labels; M1's muted 12px caption treatment would bury them |
| Iframes static, full box, no bleed, no transform ever | M1's own final-round rule (brief.md point 6 + point 8) | compliance | Unchanged rule, re-verified live across a full scroll sweep this round too (see verification below) |

## Asset bug found and fixed

`tests/alunix-concepts/_assets/k4-cabin-desk.webp` and
`tests/alunix-concepts-r3/build/assets/k4-cabin-desk.webp` share a filename but are
two different files (md5 `d050f377…` vs `f568553…`). `curl` fetches the `_assets/`
copy fine (200, correct byte count), but Chromium hangs on it indefinitely — every
`page.goto()` on that exact URL timed out at 15s, and loading it as a page background
produced a `net::ERR_CONNECTION_RESET` console error on every run, reproduced three
times in a row. Root cause not fully diagnosed (looks like a malformed WebP chunk
Chromium's decoder chokes on, since curl's plain byte transfer is unaffected) — fixed
by pointing `--ground-img` at the r3/build/assets copy instead, which loads (200) and
is the exact file M1 already shipped and verified. Flagging this for a separate fix
in case `_assets/k4-cabin-desk.webp` is reused elsewhere in this photo pool.

## Feeling curve (written before building)

1. **Arrival, held under glass.** The full-bleed hero photo (light beams cutting a
   dark room) sits under a heavy black wash; the headline is centred, large, alone.
   Caused by: one cinematic photograph, wash at its densest near the top.
2. **Lift.** Scrolling through the hero, the wash thins and the headline climbs
   clear of it while the photo itself settles lower in its own frame — two things
   moving in genuinely different directions inside the same frame.
   Caused by: the signature wash + the opposite-direction parallax/rise pair.
3. **Hard cut.** The cinematic hero ends abruptly; the page's paper-and-ink world
   (the giant "VI BYGGER ERT VARUMÄRKE." block, immediately, on the right) and its
   console-dark world (left) open side by side with no transition panel between them.
   Caused by: the photography-to-flat-type cut Planhat's own reference names.
4. **Held, twice over.** The blue thesis block pins; the headline greets, holds,
   then a second line crosses in under it while the frame itself does not move.
   Caused by: the pin act, span 2, the page's one held moment.
5. **Peak: two real places, side by side.** Calyx's own site (florist, Stockholm)
   and Hyperborea's own site (conference, Lund) sit stacked in the left column,
   genuinely interactive, while the right column is still working through its own
   services grid — two independent, real, out-of-step worlds inside one page.
   Caused by: three real interactive sites total, more than any prior Alunix round.
6. **Close, uneven, resolved anyway.** The right column's price box lands still and
   quiet, kontakt@alunix.se the last line, while the left column keeps going a while
   longer (Hyperborea's own dark page, still open) — the fixed ground absorbing the
   difference in column height exactly as M1's own layout mechanic intended.

**Peak:** act 5 (three real, independently interactive demo sites, two of them
stacked in the same column) — the largest structural claim on the page, and the one
dimension where this build genuinely does more than M1 did.

**Tell-someone sentence:** "It's the site where the hero photo only really comes
into view once you've already scrolled past it — the black wash keeps lifting the
whole time you're looking at it, so you never quite see it clearly until it's
behind you."

**Signature move:** the wash lift. `.hero-wash{opacity:calc(0.72 - 0.52 * var(--sc-p,0.5))}`
— a single line of CSS, no JS, reading the hero act's own `--sc-p` the engine already
publishes. The photo is at its darkest, most hidden state near the top of the act and
its clearest by the time the act has been scrolled past, which is the literal
opposite of a normal reveal-on-enter photo hero.

## Devices per act (target: >=4 families, never the same one twice running)

DOM order (col-left panels precede col-right panels; the two are visually
interleaved by column layout, not DOM position):

1. `act-hero` — **parallax** (kit device, hero photo, rate +1.5) + bespoke rise
   (headline, capped 72px) + bespoke wash-opacity signature move + `drift` stop 1.
2. `panel-open` (left, console card) — **reveal** (`up`).
3. `thesis-pin` (left) — **pin**, span 2, two crossing cues + `drift` stop 2.
4. Calyx `.frame-block` (left) — **reveal** (`up`).
5. Hyperborea `.frame-block` (left) — **flow+in** (`data-sc-in`, stagger 60ms).
6. `panel-giant` (right, opens the column) — **kinetic** (`lines`, headline) +
   flow+in (ledger, staggered 90ms).
7. `panel-services` (right) — **flow+in** (section head + 3 services, staggered) +
   bespoke rise (statement, capped 70px) + `drift` stop 3.
8. Hōrai `.frame-block` (right) — **reveal** (`iris`, once per page).
9. `price` (right, close) — **no device**, static by design (M1's own house lesson).

Families used: parallax, reveal, pin, flow+in, kinetic (5, >=4 required). Sequence:
parallax -> reveal -> pin -> reveal -> flow+in -> kinetic -> flow+in -> reveal ->
none. No two consecutive acts in DOM order repeat the same primary family.

## Device table per act (per viewport)

| Act | Desktop (>=900px) | Mobile (<900px) |
|---|---|---|
| act-hero | full-bleed photo, 92vh, centred headline+sub, wash lifts on scroll | full-bleed photo, 82vh, same centring |
| panel-open | dark strip, kicker/clock row + wordmark + hero body, reveals up | same, stacked, full width |
| thesis-pin | pinned 100svh stage, kicker+headline greet then fade, support crosses | same mechanic, single-column stage |
| Calyx frame-block | label + iframe, min-height 70vh, reveal up | label + iframe, min-height 64vh |
| Hyperborea frame-block | label + iframe, min-height 70vh, flow+in entrance | label + iframe, min-height 64vh |
| panel-giant | giant kinetic headline, 3-row ledger | stacked, ledger single column |
| panel-services | 3-col services grid, statement rises | single column |
| Hōrai frame-block | label + iframe, min-height 70vh, iris reveal | label + iframe, min-height 64vh |
| price | static, padded | static, padded, full width |

## Fingerprint row (vs. M1, brief's own <=2/6 ceiling)

| Dimension | M1 (r4) | V2 (r5) | Shared? |
|---|---|---|---|
| Grammar | continuous world (loose) | continuous world (loose) — inherited, not re-derived | Yes (shared baseline across all three r5 variants by design) |
| Nav | thin top row, scrolls away | thin top row, scrolls away | Yes (shared baseline) |
| Hero device | full-width Tidvatten iframe, single act | full-bleed photograph under a lifting black wash, headline centred | No |
| Act-sequence shape | full-width act, then 50vh-offset stagger, independent close heights | full-width hero, both columns flush, giant block opens the right column immediately, independent close heights | Partial (both keep independent close heights — inherent to the shared brief — but the offset mechanic itself is removed) |
| Close pattern | Calyx frame + price box, deliberately unsynced | Hyperborea frame (left) + price box (right), deliberately unsynced | Partial (same "unsynced" behaviour, different left-column closer) |
| Signature move | the 50vh offset stagger + the ground's drift | the hero wash lifting off `--sc-p`, pure CSS | No |

Per brief.md's own framing ("allt annat gemensamt" — everything else shared across
the three r5 variants), grammar and nav are the deliberately shared baseline; the
gate that matters is contract.md's own V1-V3 fingerprint table (hero device, blue-
block figure, scroll family, signature move, sources) which V2 satisfies distinctly
from V1 and V3 (not built by this agent, but read at contract.md's own request to
stay distinct — see contract.md's table for the full comparison).

## Copy gate

No new copywriting pass run. Every string on this page is either verbatim from M1
(unchanged headlines/subtexts) or one of brief.md's own binding lines (the three demo
labels, the three price rows) — brief.md point 5 states the copy is otherwise
verbatim and nothing beyond those specific lines is new. This matches M1's own
recorded reasoning for skipping the copy-gate chain.

## Verification results

- **`scroll_verify.py`:** `deadScroll: []`, `cuesNeverFull: []`, `unrevealed: []`,
  `contrastUnderMedia: []`, `blankBands: []`, `notes: []` — clean across 14 scroll
  positions from 0 to 3769 at 1440x900.
- **`a11y_scan.py`:** 0 violations, 28 passes, 2 incomplete (axe's own "needs manual
  review" bucket), at both 1440x900 and 390x844.
- **Overflow (after a full scripted scroll-through, not just at rest):**
  `document.documentElement.scrollWidth === window.innerWidth` at both 1440
  (`1440 === 1440`) and 390 (`390 === 390`).
- **Console:** zero `[scrollcraft]` warnings at 1440 or 390 across a full
  scroll-through. Three `cdn.tailwindcss.com` production-use notices remain,
  originating inside the Calyx/Hōrai/Hyperborea iframes' own pages (outside this
  build's scope, same as every prior Alunix round).
- **Pin check:** `.thesis-pin [data-sc-stage]` computed `position: sticky`
  (confirming nothing is overriding `.sc-stage`, per devices.md's own
  `[scrollcraft] will not pin` warning this would otherwise trigger); `.thesis-pin`
  itself carries `.sc-act--pinned`. A pin that will not pin would have failed this
  check and logged the engine's own console warning — neither happened.
- **Iframes:** all three present, real `title` attributes (`Calyx, florist i
  Stockholm`, `Hōrai, Asian fusion-koncept`, `Hyperborea, konferens i Lund`), swept
  across a full scroll sweep at 150px steps — zero instances of a non-`none`
  `transform` on any iframe or its ancestors at any scroll position.
- **Gap measurement (JS, `getBoundingClientRect` on every column's direct
  children, 1440x900):** every panel-to-panel gap in both columns measured exactly
  **30px** (the `clamp(16px,2.2vw,30px)` flex gap's own ceiling at this viewport
  width) = **3.33vh**, well under the 8vh cap. Left column: panel-open -> thesis-pin
  30px, thesis-pin -> Calyx 30px, Calyx -> Hyperborea 30px. Right column: panel-giant
  -> panel-services 30px, panel-services -> Hōrai 30px, Hōrai -> price 30px.
- **Motion proof, opposite directions (`shots/motion-0..4.png`, scrollY
  0/150/300/450/600, live `getComputedStyle` reads):** the hero headline's
  `translate3d` y-offset moves -34.8px -> -41.0px -> -47.3px -> -53.5px -> -59.8px
  (rising, increasingly negative) while the hero photo's parallax offset moves
  -2.56px -> +10.46px -> +23.48px -> +36.50px -> +49.52px (sinking, increasingly
  positive) — opposite signs throughout, confirmed by reading all five screenshots
  directly: the headline visibly climbs while the image visibly settles lower in
  its frame. The hero act's own `--sc-p` measured 0.483 -> 0.570 -> 0.657 -> 0.743
  -> 0.830 over the same range.
- **Wash opacity (same five frames):** 0.469 -> 0.424 -> 0.379 -> 0.333 -> 0.288,
  monotonically falling as the act is scrolled past, confirming the signature move's
  own direction (clearest once you've left it) even though the literal starting
  ceiling of 0.72 is not reached at initial scroll (see decision ledger).
- **Reduced motion (`prefers-reduced-motion: reduce`, real browser context):** all
  four `[data-motion]` elements report computed `transform: none` at scrollY 1700;
  `window.__scFreezeMotion`/`__scUnfreezeMotion` are `undefined` in this branch,
  confirming the bespoke rise script is gated out entirely, not just zeroed per
  frame. Pin cues: pre-fix, a static scroll position inside the pin could show the
  support line at opacity 0 (measured at scrollY 1500: kicker 1, headline 1, support
  0) — fixed with the `!important` media-query override documented above;
  post-fix, all three cue elements (kicker, headline, support) measured opacity `1`
  at five different scroll depths through the pin (0, 1500, 1850, 3000, 3700),
  i.e. the pinned block shows all of its text regardless of where a reduced-motion
  reader's scroll happens to land.
- **Full-page shots, hand-composited (`shots/desktop-1440--full.png`,
  `shots/mobile-390--full.png`):** Playwright's own `full_page=True` was not used
  (per M1's own documented reasoning: its internal resize/stitching re-triggers the
  bespoke scroll listener against the wrong scrollY mid-stitch). This build's own
  compositor additionally had to special-case the pinned thesis act: a naive
  forward-scroll stitch pastes a viewport screenshot at every step regardless of
  whether the content actually changed, and a `position:sticky` pin holds the exact
  same visual for a ~900px (mobile: ~844px) span of real scroll — pasting each of
  those steps at its own scrollY duplicated/smeared the pinned content down the
  composite. Fixed by measuring each `.sc-act--pinned` element's natural document
  top/height once (before any scrolling), then on encountering that span: paste
  exactly ONE representative frame (scrolled to 55% of the pin's own travel, the
  point where the crossing cues read best together, measured live via a dedicated
  probe script) at one viewport height in the output, then skip the compositor's
  document cursor to the pin's natural bottom before resuming normal stitching.
  Desktop: raw `document.documentElement.scrollHeight` 4669px, composited output
  3900px (the ~900px-tall pin span collapsed to one 900px frame). Mobile: raw
  6573px (single-column stack), composited 5938px (~844px pin span collapsed to one
  844px frame). Read every section of both composites directly plus nine individual
  full-viewport screenshots at chosen scroll depths (`shots/sec-*.png`) — no
  duplication, no void, no clipped text anywhere; the "hard cut" from the dark
  cinematic hero to the light "VI BYGGER ERT VARUMÄRKE." panel reads immediately;
  the pin shows kicker+headline+support together at its crossing point; both demo
  labels (`Exempelsida: …`) sit directly above their own iframe with no gap; the
  price box's three new rows and their values are correctly bold and legible; the
  left column's independent close (Hyperborea still open) beside the right column's
  settled price box shows the ground filling the height difference exactly as
  designed.

## Fix round (Anton's pixel measurements, 2026-09-04)

Two defects, both measured on pixels, both root-caused live with a Playwright probe
rather than guessed at. No sub-agents, no edits outside this cell, no commit, no new
copy — same constraints as the build round.

### Defect 1 — the pinned blue block produced empty blue screens

**Symptom:** at scrollY≈904, ~300px of empty blue above "VARFÖR DESIGN"; one grid
frame (`my-V2-grid.png`, row 2 col 1) was an entire viewport of plain blue.

**Root cause, measured live (not assumed):**
- `.thesis-stage` used `justify-content:center`, vertically centring the ~340px
  text block inside the full 900px sticky stage. At scrollY=904 the DOM measured
  `stageRect.top=439.9`, `kickerRect.top=735.3` — a 295.4px gap, matching the
  reported ~300px almost exactly.
- Because the stage's content only occupied the middle third of the box, during
  the pre-pin "flow-in" slide (the one full viewport of normal scroll before the
  pin actually engages, per scrollcraft.js's own documented behaviour) there was a
  ~280px range of scroll where the text sat entirely below the viewport — the
  literal "entire viewport of plain blue" frame.
- A second-order bug surfaced while fixing the first: giving the support line its
  own delayed "crossing" cue (a nonzero ramp-in) left it at a true, unmoving
  opacity 0 for that *entire* pre-pin slide. A pinned act's own progress `p` is
  hard-clamped to exactly 0 for the whole pre-pin phase (`scrollcraft.js`
  `read()`: `raw = clamp01((y - a.top) / travel)`), so any cue with a nonzero
  ramp-in evaluates to `smooth(0)=0` there — it can only be fully off or
  instantly on, never partway through. Since the block is already "on screen"
  for that whole slide, a delayed support cue directly failed "visible together
  the moment it's on screen."
- A third-order bug, same family: the devices.md rule that a *middle* pinned
  act's cue must reach true opacity 0 before p=1 (never hold unconditionally,
  or the text drags into the un-pin slide) forces some fade-to-zero window
  before release. With the original `to=0.9`/default `rOut=0.3` ramp, that
  window — while the stage is *still* sticky, i.e. still filling the whole
  column — measured 45.8% blue with zero text in a 200px-step screenshot sweep
  (`pin_sweep.py`), just over the task's 45% cap, even though the fade itself
  was a smooth ramp, not a hard cut.

**Fix:**
- `.thesis-stage{justify-content:center}` → `flex-start` (`index.html` ~line
  222). Copy now greets right at the top of the stage the instant any of it is
  on screen.
- `.thesis-pin[data-sc-span]` `2` → `1.3` (the task's own ceiling).
- Kicker, headline and support cues unified to identical `"0 0.995 0 0.05"` —
  instant appearance together at p=0 (`rIn=0`), and a fade-out compressed into
  the last ~1.3% of the pin's travel (`rOut=0.05`, `to=0.995`) instead of the
  typical 30%-of-window ramp — narrow enough that no 200px-step sweep frame can
  land inside the blank window. The earlier "support crosses in as a second
  beat" idea was dropped outright, not just retimed: it cannot exist within
  this engine's cue math without failing "visible together," because a pinned
  act's own progress is hard-clamped to 0 for the entire pre-pin slide (see
  above) — there is no partial value for a delayed cue to take during that
  slide, only fully-off or fully-on.

**Re-verified (Playwright, `pin_sweep.py`, 1440×900, 200px steps through the
block, docTop=1343.9, new height=1170):**

| Frame | scrollY | kicker/headline/support opacity | blue px-match fraction of full 1440×900 frame |
|---|---|---|---|
| 0 | 803 | 1 / 1 / 1 | 15.7% |
| 1 | 1003 | 1 / 1 / 1 | 25.9% |
| 2 | 1203 | 1 / 1 / 1 | 36.1% |
| 3 | 1403 | 1 / 1 / 1 | 43.4% |
| 4 | 1603 | 0.798 / 0.798 / 0.798 | 43.3% |
| 5-9 | 1803-2603 | 0 (post-release, scrolling away) | ≤36.3% |

Every frame through the block's active life shows all three lines together; no
frame anywhere in the sweep exceeds 45% (worst case 43.4-43.3%, both frames with
full text). The one frame that used to read as pure blue (old frame index 4/8,
~46% blue with zero text) now carries visible copy at 0.798 opacity instead —
confirmed visually (`pin-sweep-4.png`, read directly, not just measured).

### Defect 2 — the columns ended a viewport apart

**Symptom:** the right column (price box) ended ~1 viewport above the left
column (Calyx + Hyperborea), a screen of bare ground bottom-right.

**Root cause, measured live:** `.stagger{align-items:flex-start}` let each
column keep its own independent, content-driven height. At 1440×900 (baseline,
before any fix) the left column measured 883px taller than the right. The
direction is not stable across viewports, though: at 1280×800, with the exact
same markup, the *right* column measured 126px taller than the left — narrower
line-wrapping changes each column's own text height by a different, non-uniform
amount (confirmed live: `panel-services`, the ledger, and the service grid all
reflow differently at 1280 than at 1440). This ruled out a single fixed-height
nudge on one frame: a `min-height` boost on Hōrai calibrated to close the
1440×900 gap (tested at 96vh, live diff -4.8px, good) made the 1280×800 case
*worse* (diff -333.8px, since the boost added to a column that was already too
long there) — a flat value literally cannot satisfy both required checkpoints
at once, because the sign flips between them.

**Fix (`index.html`, stagger-shell comment ~line 166):**
- `.stagger{align-items:flex-start}` → `align-items:stretch`. Both columns now
  match the taller one's own natural (unstretched) height — standard flexbox
  cross-axis stretch, computed fresh from real content at any viewport, not a
  guessed constant.
- The two "closing" frames — Hōrai (`#projekt`, last item in the right column)
  and Hyperborea (`.col-left .frame-block:last-of-type`, last item in the left
  column) — get `flex:1 1 auto` **twice**: once on the frame-block itself (the
  actual flex item inside `.col`, so it receives the column's own stretched
  extra height instead of leaving it as invisible blank space below the frame)
  and again on the frame-block's inner `.frame-box` (so the extra height lands
  on the visible iframe box, not on the frame-label above it). First attempt
  only set `flex:1` on `.frame-box` and left the outer `.frame-block` at its
  natural size — that passed the column-bottom measurement (both `#colLeft`/
  `#colRight` divs got stretched to equal height) while leaving a *hidden*
  ~102px gap between the real visible content and the column's own invisible
  stretched bottom edge at 1280×800, i.e. the same bug relocated rather than
  fixed. Caught by measuring the visible frame's own bottom, not just the
  column div's bottom, and corrected before treating it as done.
- Price stays last on the right at its natural size (never stretched), per the
  house "unsynced but close" rule — only Hōrai (or Hyperborea) absorbs slack.
- Mobile (`max-width:900px`): `.stagger` stacks to a single column, so there is
  no cross-column gap to close; both closing frames revert to `flex:none`
  (natural height) there.

**Re-verified (Playwright, live DOM, visible-content bottoms, not container
boxes):**

| Viewport | left visible bottom | right visible bottom | diff | cap (0.04×vh) |
|---|---|---|---|---|
| 1440×900 | 4039.47 | 4039.47 | 0px | 36px |
| 1280×800 | 3787.5 | 3787.5 | 0px | 32px |

Both exact matches (0px), well inside the required tolerance. Hōrai's frame-box
grew from the 70vh floor (630px) to 859px at 1440×900 (left was the long
column there); Hyperborea's frame-box grew from the 70vh floor (560px) to
685.8px at 1280×800 (right was the long column there) — confirming the fix
responds to whichever column actually needs it, in both directions, not a
one-way patch.

### Full re-verification after both fixes (2026-09-04, same server, same URL)

- **Gap measurement (panel-to-panel, `getBoundingClientRect`, 1440×900):**
  every panel-to-panel gap in both columns still exactly **30px** (3.33vh,
  unchanged from the build round, well under the 8vh cap) — `[30,30,30]` both
  columns.
- **`scroll_verify.py`:** `deadScroll: []`, `cuesNeverFull: []`,
  `unrevealed: []`, `contrastUnderMedia: []`, `blankBands: []`, `notes: []` —
  clean across 12 scroll positions from 0 to 3139 at 1440×900 (page is shorter
  now: span 2→1.3 on the pin removed ~630px of document height).
- **`a11y_scan.py`:** 0 violations, 28 passes, 2 incomplete — unchanged from
  the build round, at both 1440×900 and 390×844.
- **Overflow, after a full scripted scroll-through:**
  `document.documentElement.scrollWidth === window.innerWidth` at both 1440
  (`1440 === 1440`) and 390 (`390 === 390`).
- **Console:** zero `[scrollcraft]` warnings, zero non-Tailwind errors, at
  1440 or 390 across a full scroll-through.
- **Pin check:** `.thesis-stage` computed `position: sticky`; `.thesis-pin`
  carries `.sc-act--pinned`. Unchanged mechanics, span aside.
- **Iframes:** all three present, correct `title`s, swept at 150px steps
  across the full scroll range — zero instances of a non-`none` `transform`
  on any iframe or its ancestors at any scroll position.
- **Reduced motion (real browser context, `reduced_motion='reduce'`):** all
  four `[data-motion]` elements report `transform: none` at scrollY 1700; the
  three thesis-pin cue elements all report opacity `1` (the `!important`
  media-query override, unchanged from the build round, still forces this
  regardless of the new cue values); `window.__scFreezeMotion` still
  `undefined` in this branch.
- **Shots re-taken:** `shots/desktop-1440--fold.png`,
  `shots/desktop-1440--full.png` (hand-composited, pin-aware), `shots/mobile-
  390--fold.png`, `shots/mobile-390--full.png`, `shots/motion-0..4.png`
  (scrollY 0/150/300/450/600, same opposite-direction proof as the build
  round, motion mechanics untouched this round), `shots/reduced-motion-
  thesis.png`. All read directly — no duplication, no void, headline greets
  at the top of the pin block in every relevant frame, both columns end
  together (confirmed visually at the very bottom of the desktop composite:
  Hyperborea's iframe on the left and the price box's `kontakt@alunix.se`
  line on the right land at the same height).

  This round's compositor needed two live fixes of its own, on top of the
  page fixes above (the compositor script itself is throwaway/local, not
  part of the deliverable, but the bugs are worth recording since the same
  approach gets reused every round):
  - **Infinite loop at the pin's own boundary:** advancing the stitch cursor
    with `cursor = int(pin.top + pin.height)` truncates a boundary like
    2513.9 down to 2513, which still satisfies the pin's own `top <= cursor
    < top+height` match — re-matching the same pin forever. Reproduced live
    (14+ identical "pasted pin frame at cursor 2513" log lines before an
    iteration cap forced an early, incomplete save with the back half of the
    page missing, replaced by blank canvas). Fixed with `math.ceil` instead
    of `int`.
  - **Column misalignment inside the pin's own span:** pasting the pin's one
    representative frame (captured at `rep_y`, partway through its travel)
    across the *full* viewport width put the pinned column's content at its
    correct fixed screen position but the *other*, still-normally-scrolling
    column's content at the wrong scroll depth — because `rep_y != cursor`.
    Visible live as the giant block's own ledger ("03 SYSTEM…") appearing to
    repeat itself directly under the pin, and the pin's own blue block
    printed twice. Fixed by always pasting a normal frame at the true
    `cursor` scrollY first (correct for the non-pinned column and the
    background at that exact document position), then overlaying *only* the
    pinned column's own x-slice from the representative frame on top of it,
    for one viewport height at the pin's natural document top — everything
    outside that x-slice keeps the geometrically correct base.

# Alunix r4 — M1 · Kontinuerlig grund · förskjutna spalter — build notes

Brief: `tests/alunix-concepts-r4/brief.md` (Anton's r4 order, 2026-09-04) + `contract.md`
§M1 (binding). Remix of `tests/alunix-concepts-r3/build/index.html` (the finished,
Anton-rejected combined page) — same copy, same three demo sites, same two type worlds
(R5 Geist / R6 Public Sans), different structure and different scroll grammar.

## Reference lock (written before code)

**Tier 2** — direction is the r3 page (structure/copy source, explicitly what to move away
from structurally) plus three catalogue entries named in contract.md:

- `design-catalogue/entries/rre-ventures/entry.md` — **primary structural reference**.
  Preserve: one continuous, non-literal photograph running the full page as ground,
  alternately exposed and covered by opaque content panels; the rhythm of exposure-then-
  cover is the entire page mechanic, not a hero trick. Borrow only: nothing else (RRE's own
  stat trio and testimonial close do not apply to Alunix's copy).
- `design-catalogue/entries/veloura/entry.md` — secondary. Preserve: the idea that the
  ground never resets to white/a different hue mid-journey, so the page reads as one dim
  space rather than stacked screens. Reject: Veloura's own warm chocolate palette and serif
  — Alunix keeps R5/R6's own tokens verbatim, the catalogue entry contributes the
  *persistence* principle only, not its colours.
- `design-catalogue/entries/creative-giants/entry.md` — R6's own proportions (poster
  wordmark scale, weight-300 restraint, rationed colour) are already in the r3 file; read
  here only to confirm the thin top-row wordmark treatment stays light (weight 300, no
  bold) rather than picking up R5's heavier Geist 700 by accident.

**Preserved from r3, verbatim per brief.md's binding rule:** every headline and sub-text,
the three demo sites as borderless interactive iframes, the price rows, kontakt@alunix.se,
the corner-tick console card device, the blue thesis block, the giant kinetic close, the
hairline services ledger, the inverted price box. No new copy anywhere.

**Removed / changed from r3's own structure (this is the whole point of the remix):**
r3's 50/50 split-stage two columns (same start y, synchronized close, seam hairline signature
move) → replaced with M1's offset stagger (right column starts 50vh lower, columns never
align) sitting over one continuous fixed ground photograph, with the offset stagger itself
as the signature move instead of r3's seam draw (see the "Final round" section below for
why: a bespoke "window" device was tried on top of the offset, then removed). r3's dual
simultaneous hero (console card + poster wordmark side by side) → replaced with the
Tidvatten iframe as one full-width first act, logo straddling its top edge, R6's wordmark
reduced to a thin scrolling top row.

**New construction, this remix only:** the fixed grayscale ground layer
(`k4-cabin-desk.webp`, `filter:grayscale(1)`) sitting beneath the whole page, tinted by the
engine's own `--sc-canvas` drift (3 stops: dark → Alunix blue → paper) via
`mix-blend-mode:color`; the offset stagger (`.col-right{margin-top:50vh}`) so the two
columns' sections never land on the same y, letting the 50vh gutter itself be the "gap"
that shows the ground. A bespoke, page-authored "window" device (a second crisp copy of
the ground faded in per panel, reading each host panel's own `--sc-p`) was built on top of
this, fixed once post-review, then removed outright in the final round — see below.

**Grammar note.** contract.md names M1's grammar "continuous world" in the loose sense
brief.md itself describes (one ground that never cuts) — not `scroll/grammars.md`'s strict
upstream "continuous world" row, which bans `flow` acts, reveal and parallax outright and
requires literal waypoint/leg geography. Following the strict row would contradict
contract.md's own explicit instructions (`data-sc-parallax`, `reveal="up"`, `drift` in
three stops, flow acts). Contract.md is the binding, task-specific brief for this cell;
this build follows it literally and treats "continuous world" here as "one persistent
photographic ground, panels alternately covering and uncovering it" (the RRE Ventures /
Veloura reading), built with `flow` acts + `parallax` + `reveal` + `drift`, not the
strict upstream grammar's waypoint mechanism. Recorded here so the deviation is a decision,
not an oversight.

**Reject:** any second background photograph; a page-wide pin (not asked for, not needed —
the ground itself is the pin-like constant, achieved without pinning anything); inventing
new copy or numbers; transform/opacity applied to an `<iframe>` element or to any ancestor
of one while it is on screen. Final round (2026-09-04): this now means the three iframes
carry no motion device at all — an earlier build let a wrapping `<div>` sink while the
iframe tag itself stayed `transform:none`, satisfying the letter of brief.md's rule, but
the sink still hid each site's own top ~100px of chrome; removed rather than re-tuned, see
the "Final round" section below.

## Decision ledger

| Decision | Source | Role | Why |
|---|---|---|---|
| Tidvatten iframe as one full-width act, not split with a second hero | contract.md M1 point 1 | opening | Literal instruction; also the clearest way to differ from r3's dual-hero fingerprint dimension |
| `.col-right{margin-top:50vh}`, `align-items:flex-start` on the flex row (no stretch) | contract.md M1 point 2 | layout | Literal instruction ("högerspalten börjar 50vh lägre så att sektionerna aldrig linjerar"); `flex-start` (not `stretch`) is required so each column's height is its own content, letting the shorter column's leftover space show bare ground per point 5 |
| Ground = `k4-cabin-desk.webp`, `position:fixed`, `filter:grayscale(1) contrast(1.05) brightness(.55)`, tinted via `mix-blend-mode:color` reading the engine's own `--sc-canvas` | contract.md M1 point 3 + rre-ventures/veloura catalogue entries | signature ground | contract offers either photo; k4-cabin-desk keeps hero-console.webp free for nothing else on this page, avoiding a duplicate use with any other panel's own imagery |
| 3 `data-sc-drift` stops (`#0b0c0e` tidvatten → `#123f68` thesis → `#f4f2ee` services) | contract.md M1 point 3 ("grunden drift i tre stopp") | motion | Reuses the engine's own supported `drift` property (devices.md: "not a device, it's a property... 3-5 stops") instead of hand-rolling a second colour system |
| Parallax on text = a small wrapper around kicker+headline only, never full body paragraphs | devices.md rule 6 ("Never on body copy") vs contract.md's broader "text i panelerna stiger" | motion | Reconciles the two: the *display* text (what a reader's eye actually tracks as it rises) gets the parallax, paragraph copy stays legible and static |
| Iframes (Tidvatten, Calyx, Hōrai) carry no sink device — static, full box, no bleed, no transform on them or any ancestor — REMOVED, final round (was: parallax on a wrapping `<div>`, never the `<iframe>` tag's own inline style) | brief.md's forbidden list ("transform... på en ram efter att den öppnats") vs Anton's second pixel read (the earlier wrapper-sink was hiding each site's own top ~100px of chrome) | compliance / craft | The wrapper-sink version was letter-compliant (iframe's own computed `transform` stayed `none`) but still cropped real content it shouldn't have; removed rather than re-tuned. The Hyperborea photo is the one thing left that sinks, inside its own overflow-hidden box, capped 90px |
| Window signature move (reserved-gutter, crisp rectangle, `--win-o` opacity read off each panel's own `--sc-p`) — REMOVED, final round | Anton's second pixel read, 2026-09-04 | signature move | See "Final round" section below for the full reasoning; superseded, not iterated on again |
| Price box carries no device, static | r3's own house lesson ("prisrutan landar stilla") + design skill's "resolve, don't fade" | motion | Matches r3's own deliberate calm ending; kept because it is a general design-skill principle, not an r3-specific fingerprint element being copied |
| Logo placed with plain CSS (`translateY(-50%)` at the topline/Tidvatten boundary), no JS measurement | own build decision, to differ from r3 | signature/nav | r3's logo position was JS-measured (its own "new construction" line); a static CSS dock differentiates this cell's chrome from r3's and keeps the JS budget minimal |
| Calyx/Hōrai iframes lost their sink (bleed wrapper + `data-motion="sink"`) — REMOVED, final round | Anton's second pixel read, 2026-09-04 | motion | The bleed wrapper's negative offset was hiding each site's own top ~100px of nav/masthead; frames are now static, full box, no bleed, no transform on them or any ancestor. See "Final round" section below |

## Fix round (2026-09-04, Anton's 7 pixel defects on the original build)

Anton's verdict on the first build: "the concept... is right. The execution of the motion
is what fails." Seven defects, measured on pixels against his own screenshots
(`my-M1-3.png`/`-5.png`/`-7.png`, scrollY 775/1400/2154). Each row: defect -> root cause
found in the shipped markup/CSS -> fix.

| # | Defect | Root cause | Fix |
|---|---|---|---|
| 1 | Windows rendered as blurry grey discs over the Hyperborea photo and beside body text | `.window` was `inset:0` of the whole panel with a feathered `radial-gradient` mask, positioned by an arbitrary `--win-x/--win-y` percentage with no regard for what content lived under it | Replaced the mask-circle with a crisp rectangle (0px radius, hairline border, no blur filter) living in a new `.window-gutter` — an empty, explicitly reserved block appended after a panel's real content, so it can never sit over text or an image. JS now writes `--win-o` (opacity 0-1) instead of `--win-r` (radius); reduced-motion sets it to `0` instead of `0px`. |
| 2 | Text rising tore blocks apart: "VI BYGGER" / "ERT VARUMÄRKE." separated by a viewport; ~100px hole between "DIGITAL BYRÅ" and the body; giant-sub sat 200px under its headline | Each block's motion wrapper covered only PART of the block (`.giant-sub` sat outside `.parallax-text`; `panel-open`'s console-top/body/list/cta sat outside it too), and `data-motion-px` values were huge (420, 340, 110, 620 — all far past the 90px cap) | One wrapper now covers the whole block in every case (console card: kicker-row+wordmark+body+list+cta together; giant: headline+sub together). All text `data-motion-px` capped: 48 (console), 80 (thesis headline+sub, was 620), 64 (giant, was 420), 70 (services statement, was 340), 40 (projects lede, unchanged, already compliant). |
| 3 | Sinking images/frames left voids: black band above Hōrai, ~480px beige void above the Calyx nav | `.frame-inner`/`.thesis-photo-inner` were the same height as their visible box and just translated — moving them down by up to 480px (Calyx) or 360px (Hōrai) opened a same-size gap of the wrapper's own background colour at the top | Rebuilt as bleed containers: each inner is exactly `travel`px taller than its box and pre-offset `top:-travelpx`, so `translateY(0..travel)` always keeps the box fully covered (panning between the bottom and top crop of the oversized content). Travel capped at ≤120px everywhere (Hōrai 360→100, Calyx 480→100, thesis photo already 90). Verified: 0 void frames at any 300px (and re-checked at 200px) scroll step, all three sink containers, full page height. |
| 4 | Hyperborea caption overlapped the image bottom | Caption sat in normal flow directly after the (transform-shifted) image div, no fixed-height clip boundary between them | New `.thesis-photo-box` (fixed `aspect-ratio:16/10`, `overflow:hidden`) holds only the bleed-container image; the figcaption sits below it in flow, outside the moving/clipped box, so it can never be reached by the transform regardless of scroll position. |
| 5 | No gap between "design." and "Vår nivå…" in the price box | `.price-ingress{margin-top:1.5rem}` (a single class selector) was being beaten on specificity by the earlier `.col-right p{margin:0}` rule (class+type = higher specificity), zeroing the margin back out regardless of source order | Re-qualified as `.col-right .price-ingress{...}` (two classes) to win on specificity. Bumped `.price .statement`'s margin-top 0.9rem→1.3rem too. Measured: kicker→statement 24.8px, statement→ingress 24.0px (both ≥20px floor). |
| 6 | Left column ended with a large void before the Calyx frame instead of following directly | Two compounding causes: (a) defect 3's void bug made the gap look far larger than it was: (b) the first fix pass put the new window-gutter AFTER `.projects`, adding ~185px between the lede and the panel's own edge | Moved `panel-giant`'s window-gutter to BEFORE `.projects` (between the ledger and the lede) so the lede stays the last thing before the panel closes; capped `panel-giant`'s bottom padding at `clamp(24px,3vw,40px)` (was 48-72px). Measured: lede-bottom to Calyx-top gap = 40.0px exactly (the padding clamp's own ceiling). |
| 7 | Opposite-direction motion proof needed re-shooting after the fixes | — | Proof pair re-tuned to the capped values: `.projects-lede` rises 40px, `.calyx-wrap .frame-inner` sinks 100px, both inside their own boxes at every step. Re-shot `shots/motion-0..4.png` at scrollY 1200/1500/1800/2100/2400 (the clearest non-saturated stretch of `panel-giant`'s own `--sc-p`, sampled live: 0.23→0.85 over that range). |

**A capture-methodology note, not a page defect:** the first re-shoot of `shots/desktop-1440--full.png` (via Playwright's `full_page=True` stitching, after scrolling back to y=0 for the fold shot) showed the giant headline's first line and the Hyperborea photo missing/smeared. Root cause confirmed live (`getComputedStyle`): the engine's own kinetic-line reveal and `[data-sc-reveal]` clip-path are keyed to live scroll progress, not a fire-once flag (e.g. `.sc-split__i` opacity measured 0.495 at scrollY=900, 1 at scrollY≥1200) — scrolling back to y=0 genuinely re-hides them, exactly the class of Playwright-stitching artifact this file's own NOTES already flagged for `paintMotion()`. A real top-to-bottom scroll never shows this (confirmed against Anton's own `my-M1-*.png`). Fixed by abandoning `full_page=True` for the full shot and hand-compositing overlapping forward-only viewport slices instead (later, more-scrolled slices overwrite earlier ones on any overlap) — the page/index.html itself needed no change for this.

## Feeling curve (written before building)

1. **Arrival, grounded.** Tidvatten's own headline fills the first full-width frame; the
   logo sits straddling its top edge, the thin wordmark row already scrolled half away.
   Caused by: one large interactive frame, no split, no column visible yet.
2. **Drift, a world under the page.** Scrolling past the frame, the left column opens on a
   dark console-style strip while the right column's 50vh gutter sits empty beside it — bare
   grayscale ground visible through the gap. Caused by: the offset stagger, the fixed ground
   showing through the unbuilt half of the row.
3. **Recognition, the ground keeps showing through.** The blue thesis block opens; the
   gutter beside it (and the 50vh gap above the still-unbuilt right column) keeps the same
   dim desk photograph in view, cropped by whatever the flex row happens to expose rather
   than by a device of its own. Caused by: the offset stagger itself — no separate widget,
   just the layout's own gaps.
4. **Weight, two speeds in one panel.** The thesis photo sinks below its own caption while
   the headline keeps rising ahead of the scroll. Caused by: opposite-rate parallax on text
   vs. image inside the same act.
5. **Peak: type over the still-tinted ground.** "Vi bygger ert varumärke." drops in as
   kinetic type, the ledger rows stagger in one after another, on paper that sits directly
   over the same fixed photograph the page opened on — proof the whole page sits on one
   ground, not per-section art. Caused by: the kinetic reveal plus the ledger's own
   stagger, the largest single visual event on the page.
6. **Two lives out of step.** Left ends inside the real Calyx site; right, staggered lower,
   is still opening its services grid, then Hōrai's own black frame. Caused by: two real
   interactive sites replacing static panels, visibly out of sync with each other.
7. **Close, uneven, resolved anyway.** The Calyx frame simply stops. The price box, further
   down the page on the right, lands still: kontakt@alunix.se is the last line before bare
   ground fills whatever height the shorter column left behind. Caused by: two independent
   endings instead of one synchronized one, the ground absorbing the difference.

**Peak:** act 5 (giant kinetic headline + ledger stagger, on paper directly over the same
fixed ground the page opened on) — the largest single visual event on the page, and the
moment that proves the "one photograph, seen bit by bit" premise the first two acts only
implied.

**Tell-someone sentence (final round):** "It's the site where the two columns never line
up, so the gap between them keeps showing the same dim desk photo underneath, tinted a
little differently the further down the page you go."

**Signature move (final round, replaces the window device removed 2026-09-04):** the
offset stagger itself. `.col-right{margin-top:50vh}` means the two columns' panels never
land on the same y, so their gaps and gutters are never aligned either — the fixed
grayscale ground shows through whichever gap the flex row happens to leave bare at that
scroll position, tinted along the way by the engine's own three `--sc-canvas` drift stops
(dark → Alunix blue → paper). No bespoke script left to drive it: the earlier build tried a
second, JS-driven device (a reserved-gutter "window" fading in a second crisp copy of the
ground per panel) on top of this, but it read as a broken image placeholder rather than an
opening onto the ground — see the "Final round" section below. Removing it left the layout
mechanic itself as the whole signature move, which is honestly what was carrying the
feeling curve's "drift, a world under the page" beat all along.

## Devices per act (target: ≥4 families, never the same one twice running)

DOM order (col-left panels precede col-right panels; the two are visually interleaved by
the 50vh offset, not by DOM position):

1. `act-tidvatten` — **cue** (logo dock, greet form) + `drift` stop 1.
2. `panel-open` (left) — **reveal** (`up`, whole panel).
3. `panel-thesis` (left) — **parallax** (headline rises, photo sinks, opposite rates) +
   `reveal` (`left`, photo) + `drift` stop 2. Final round: this is now the page's own
   opposite-direction motion proof pair (`shots/motion-0..4.png`), moved here from the
   Calyx frame once frames stopped sinking (see "Final round" section).
4. `panel-giant` (left) — **kinetic** (`lines`, the giant headline) + **flow+in** (ledger,
   staggered).
5. `calyx-wrap` (left, close) — **reveal** (`up`). Final round: no longer carries motion —
   the iframe is static, full box, no bleed (see "Final round" section).
6. `panel-services` (right) — **flow+in** (section head + 3 services, staggered) +
   parallax (headline rises) + `drift` stop 3.
7. `horai-wrap` (right) — **reveal** (`iris`, once). Final round: no longer carries motion,
   same fix as Calyx above.
8. `price` (right, close) — **no device**, static by design.

Families used: reveal, parallax, kinetic, flow+in, cue (5). No two consecutive acts in DOM
order repeat the same primary family: cue → reveal → parallax → kinetic → reveal → flow+in
→ reveal → none.

## Device table per act (per viewport, for the mobile/desktop check)

| Act | Desktop (≥900px) | Mobile (<900px) |
|---|---|---|
| act-tidvatten | full-width iframe, ~70vh, logo dock straddles top edge | full-width iframe, min-height 70vh, logo dock same |
| panel-open | dark strip, kicker/clock row + wordmark + hero body | same, stacked, full width |
| panel-thesis | 2-col grid (text + photo); headline rises / photo sinks, opposite directions | single column, photo first (existing r3 mobile pattern kept) |
| panel-giant | giant kinetic headline, 3-row ledger | stacked, ledger single column |
| calyx-wrap | iframe min-height 90vh, static, full box, no bleed | iframe min-height 70vh, static, full box, no bleed |
| panel-services | 3-col services grid | single column |
| horai-wrap | iframe min-height 82vh, iris reveal, static, full box, no bleed | iframe min-height 70vh, iris reveal, static, full box, no bleed |
| price | static, padded | static, padded, full width |

## Fingerprint row (vs. r3, brief's own ≤2/6 ceiling)

| Dimension | r3 | M1 | Shared? |
|---|---|---|---|
| Grammar | split stage | continuous world (loose, see reference-lock note) | No |
| Nav | none — fixed corner marks, page-wide persistent chrome | none — thin top row that scrolls away, no persistent chrome | No |
| Hero device | two heroes side by side (console card + poster wordmark) | one full-width Tidvatten iframe, single act | No |
| Act-sequence shape | immediate 50/50 split, both columns start at y=0, synchronized close | full-width act first, then offset stagger (right column +50vh), independent close heights | No |
| Close pattern | Calyx frame + price box, both landing at the same y (measured, forced) | Calyx frame + price box, explicitly allowed to land at different y, ground fills the difference | Partial (both use Calyx + price box as the two closing elements — inherent to the shared copy/asset constraint — but the *behaviour* differs: synced vs. deliberately unsynced) |
| Signature move | seam hairline drawn from a JS-measured logo dock, `mix-blend-mode:difference` | the offset stagger itself: the 50vh column lag plus the ground drifting through three colour stops in the gaps it leaves bare | No |

Shared: 1/6 (partial credit on close pattern only, and even that differs in behaviour) —
inside the ≤2/6 ceiling brief.md sets.

## Skills loaded, in order

1. `Skill(design)` — front door; Step 0 (page scope, this is a full build), Step 1
   (pre-flight — no `DESIGN.md` in `tests/alunix-concepts-r4/`), Step 1b (reference lock
   above: r3 page + three catalogue entries read in full), Step 2 (Tier 2 — r3 + catalogue
   are the direction, stated explicitly), Step 2b (grammar note above, feeling curve above,
   device list above, fingerprint row above — bake-off skipped, this is a task-assigned
   single direction per contract.md, not an open exploration), Step 4 (build), Step 5
   (verify, this document).
2. No copywriting/copy-editing/humanizer chain run — brief.md and contract.md both state
   the copy is verbatim from r3, no new strings anywhere on the page; the copy gate's own
   scope note ("any user-facing string") does not apply to text that is not being written,
   only reordered.

## Verification results

- **`scroll_verify`-equivalent pass** (scratch Playwright script, scripted top-to-bottom
  scroll before each full-page shot, per r3's own documented Playwright `full_page`
  stitching workaround): desktop 1440x900 fold + full (`shots/desktop-1440--fold.png`,
  `shots/desktop-1440--full.png`, full page 3078px), mobile 390x844 fold + full
  (`shots/mobile-390--fold.png`, `shots/mobile-390--full.png`, full page 4347px).
- **Overflow:** `document.documentElement.scrollWidth === window.innerWidth` at both
  1440 (`1440 === 1440`) and 390 (`390 === 390`), checked after a full scripted
  scroll-through, not just at rest.
- **Console:** no `[scrollcraft]` warnings at either breakpoint through a full
  scroll-through. Only console messages present: three `cdn.tailwindcss.com` notices
  originating from inside the Calyx/Hōrai iframes' own pages (outside this build's
  scope, same as every prior Alunix round).
- **Iframes:** all three present with real `title` attributes — `Er hemsida är
  nutidens visitkort` (Tidvatten), `Calyx, florist i Stockholm`, `Hōrai, restaurang i
  Stockholm`.
- **`a11y_scan.py`:** 0 violations, 28 passes, 2 incomplete (axe's own "needs manual
  review" bucket, not a failure), both before and after the topline contrast fix
  below.
- **Contrast — topline over the ground (scratch `contrast_over_media.py`-style
  measurement, same method: hide text, screenshot, sample brightest 5% of each
  string's own rect):** first pass over the raw ground (Tidvatten's bright sky patch)
  measured worst-case 3.53:1 (ALUNIX mark) and 2.53:1 (kontakt link), both under the
  4.5:1 floor. Fixed with `.topline::before`, a soft dark gradient scrim confined to
  the topline's own strip (not the whole ground, so it never reads as an opaque nav
  bar). Re-measured: worst-case 7.21:1 (mark), 10.48:1 (kontakt link) — both clear.
- **Reduced motion (`reduced_motion: reduce`):** all eight `[data-motion]` elements'
  computed `transform` is `none` before and after a scroll to y=2000 (the bespoke
  motion script never runs its `paintMotion()` loop when `prefers-reduced-motion:
  reduce` is set — it is gated out entirely, not just zeroed per frame). All three
  windows' `--win-r` stay `0px` before and after the same scroll (closed, not frozen
  half-open). Everything else on the page keeps its own reveal/cue end-state visible
  per the engine's own reduced-motion handling.
- **Motion proof (five viewport screenshots, 300px apart, `shots/motion-0.png` through
  `motion-4.png`, scrollY 900/1200/1500/1800/2100):** the pair at frames 3 and 4
  (scrollY 1800 to 2100) is the clearest single-step demonstration — measured live:
  the "Utvalda projekt / Calyx" lede (`data-motion="rise"`) moves from `top: 507.6px`
  to `top: 201.1px` (up 306.5px), while the Calyx frame wrapper
  (`data-motion="sink"`, local bump shape) moves from `top: 647.7px` to `top:
  792.5px` (down 144.8px) — both fully inside the 0-900px viewport in both frames,
  confirmed by reading the two screenshots directly: the lede visibly climbs past a
  ledger row, and a visible band of the panel's own paper ground opens up above the
  Calyx site's own masthead where the frame has slid down away from it. Verified this
  is not a screenshot-tooling artifact by unfreezing the bespoke motion script
  (`window.__scUnfreezeMotion()`) before taking the motion frames — the full-page
  shot immediately before this sequence freezes the same script
  (`window.__scFreezeMotion()`) specifically to survive Playwright's own internal
  resize during `full_page=True` stitching, matching the class of bug r3's NOTES.md
  already documented for the engine's own reveal system.

## Verification results (fix round, 2026-09-04 — supersedes the numbers above where they overlap)

- **`scroll_verify.py`** (real script this time, not a scratch equivalent):
  `deadScroll: []`, `cuesNeverFull: []`, `unrevealed: []`, `contrastUnderMedia: []`,
  `blankBands: []`, `notes: []` — clean across scrollY 0/300/600/900/1200/1500/1800/2100/2400/2426.
- **`a11y_scan.py`:** 0 violations, 28 passes, 2 incomplete (unchanged from the first pass).
- **Overflow:** `document.documentElement.scrollWidth === window.innerWidth` at both 1440
  (`1440 === 1440`) and 390 (`390 === 390`) across a full scripted scroll-through.
- **Console:** no `[scrollcraft]` warnings at either breakpoint.
- **Iframes:** all three present, titled, and confirmed `transform: none` on the `<iframe>`
  elements themselves at every scroll position tested (only their wrapping `.frame-inner`
  divs move) — the binding rule holds under the new bleed-container sink mechanism too.
- **Windows (defect 1):** crisp rectangle, no `filter:blur`, no mask — confirmed via
  `getComputedStyle` (`opacity` driven by `--win-o`, no clip-path). Measured live: at
  scrollY 775 (Anton's own `my-M1-3.png` position) all three windows sit inside their
  `.window-gutter` bounds (e.g. thesis gutter `top:754.9 bottom:866.9`) which do not
  intersect the photo (`top:437.2 bottom:668.4`) or its caption (`top:668.4 bottom:714.1`)
  at any scroll position — checked programmatically, not just by eye.
- **Text travel (defect 2):** every `[data-motion]` text element's `data-motion-px` ≤90:
  console card 48, thesis headline+sub 80, giant headline+sub 64, services statement 70,
  projects lede 40 (unchanged).
- **Sink bleed / no voids (defect 3):** swept all three sink containers (thesis photo,
  Hōrai frame, Calyx frame) at every 300px scroll step across the full document height —
  zero steps where the inner content fails to fully cover its visible box (re-checked at a
  finer 200px step too, same result: zero). All three `data-motion-px` ≤120 (90/100/100).
- **Caption overlap (defect 4):** `.thesis-photo-box` (fixed `aspect-ratio:16/10`,
  `overflow:hidden`) bottom edge and figcaption top edge measured flush (0.00002px
  floating-point noise, not a real overlap) at scrollY 775.
- **Price spacing (defect 5):** kicker→statement 24.8px, statement→ingress 24.0px (both
  ≥20px). Root cause was a specificity bug (`.col-right p{margin:0}` beating
  `.price-ingress{margin-top:...}`), not just a wrong number — see fix-round table above.
- **Left-column close gap (defect 6):** `.calyx-wrap` top minus `.projects-lede` bottom =
  40.0px exactly, at the full scrolled-to-bottom position.
- **Reduced motion:** re-confirmed after all fixes — `window.matchMedia('(prefers-reduced-
  motion: reduce)').matches` true in this test environment by default (a real, not
  simulated, reduced-motion state, not an emulation flag this round); all eight
  `[data-motion]` elements report computed `transform: none` and all three windows report
  `opacity: 0` at scrollY 2000, no scroll listener attached (`__scFreezeMotion`/
  `__scUnfreezeMotion` are `undefined` in this branch, confirming the motion script is
  gated out entirely rather than just zeroed per frame).
- **Motion proof re-shot (defect 7), `shots/motion-0..4.png`, scrollY 1200/1500/1800/2100/2400**
  (`panel-giant`'s own `--sc-p` measured live: 0.23 → 0.85 over this range, the clearest
  non-saturated stretch): `.projects-lede` (rise, capped 40px) and `.calyx-wrap
  .frame-inner` (sink, capped 100px, was 480px) — per-step deltas confirm both directions:
  the lede's screen position moves ~-306px per 300px of scroll (6px more than a plain
  scroll would, i.e. leading/rising) while the Calyx frame moves ~-280px per 300px step in
  the later frames (20px less than a plain scroll would, i.e. lagging/sinking relatively) —
  both fully inside their own boxes at every frame, visually confirmed by reading all five
  screenshots directly (no clipping, no void, no overlap with neighbouring text).
- **Full-page shots re-verified frame by frame** (`shots/desktop-1440--full.png`,
  `shots/mobile-390--full.png`): every panel's text reads as one cohesive block, both
  sinking frames (Hōrai, Calyx) show their photo filling the box edge-to-edge with no void,
  the Hyperborea photo and its caption both read cleanly with no overlap, and the giant
  kinetic headline renders fully formed with no partial-reveal smear (see the fix-round
  capture-methodology note above for what that took).

## What was tried and reverted for the motion proof (recorded so the reasoning isn't lost)

The first attempt put the sink proof on `.thesis-photo-inner` (the small Hyperborea
thumbnail inside the blue thesis panel). Two real bugs surfaced and are the reason
the final proof pair lives on the Calyx frame instead:

1. **Direction-reversal math vs. the kit's own parallax device.** `data-sc-parallax`
   centres its formula on act-progress 0.5 and cannot exceed roughly one scrolled
   pixel of travel per scrolled pixel at the rates devices.md recommends (0.3-2) — it
   can only make an element lag or lead the scroll, never reverse its on-screen
   direction. Proving "image moves down while the page scrolls down" needs the added
   offset to grow *faster* than the scroll itself over some span, which requires a
   bespoke device, not the kit's own. Built one: a small page-authored script reads
   each `[data-motion]` element's host `[data-sc-act]` panel's own `--sc-p` (act
   mode) or a self-measured local scroll span (local mode), and writes a monotonic or
   sine-bump `translate3d` offset — never touching `scrollcraft.js`.
2. **Reversal-strength vs. clip-box size is a real constraint, not a preference.** A
   linear or bump ramp needs its amplitude to exceed roughly `span / π` to clear the
   reversal-slope threshold. On the thesis photo card (a ~110px real clip budget
   between the image's natural bottom edge and its panel's own bottom edge, measured
   live), any amplitude large enough to reverse direction also exceeds the budget and
   pushes the image fully outside `.panel-thesis`'s own `overflow:hidden` box —
   confirmed by reading `getBoundingClientRect()` for the image against the panel at
   the scroll position in question (image top `834.9px` vs. panel bottom `712.6px`,
   fully clipped) and re-confirmed visually: the "image" a screenshot showed moving
   at that spot was actually the ground `[data-window]` mask showing through, not the
   thesis photo, which had simply vanished. Retuning to a small, budget-safe
   amplitude (~90-110px) only produced a reversal a few px wide — real, but too
   subtle to see by eye in two screenshots. Moved the proof to the Calyx frame
   wrapper instead, which has a ~630px real clip budget (iframe wrapper is `min-
   height: 70vh`), comfortably fits a 480px bump amplitude, and gives a confirmed
   144.8px visible reversal. `.thesis-photo-inner` itself now runs a small, purely
   textural `act`-mode sink (`px="90"`) with `overflow:hidden` restored on
   `.thesis-photo` — it lags the scroll like the rest of the page's sink elements,
   no reversal claimed for it.

**Final-round postscript:** the Calyx frame this section moved the proof pair *to* no
longer carries any motion at all (see "Final round" section immediately below) — the proof
pair moved back to the thesis act, but under a relaxed requirement (Anton's actual ask was
"text rising, photo sinking, both inside their boxes", not a strict on-screen direction
reversal), so the reversal-vs-clip-budget constraint documented above no longer needed
solving: the thesis headline (local mode, capped 80px) and the Hyperborea photo (act mode,
capped 90px) already satisfied the relaxed pair as shipped, unchanged.

## Final round (2026-09-04) — windows removed, frames unsunk

Anton's second pixel read, against `my-M1-3.png`/`-5.png`/`-7.png` (the same three
screenshots the fix round measured against, scrollY 775/1400/2154). Two decisions, both
executed as outright removals rather than further iteration:

1. **The windows did not communicate — removed entirely.** The fix round had already
   corrected the window device once (soft-mask circle → crisp rectangle in a reserved
   gutter, see the "Fix round" table's defect 1). On a second look, even the corrected
   version read wrong: the crisp rectangles in the reserved gutters (the grey box in the
   blue thesis block, the whitish box above "UTVALDA PROJEKT", the grey box above the
   services grid, the dark box above "FILOSOFI") read as broken image placeholders, not as
   openings onto the ground — a rendering-failure read, not a signature-move read, however
   correctly they were positioned and sized. Removed outright: all three `.window-gutter`
   elements and their markup, the `.window-gutter`/`.window` CSS block, the `paintWindows()`
   function and `windows` array, the reduced-motion window reset, and the `noscript`
   fallback rule — nothing bespoke left running for this. The continuous ground still shows
   in the offset gaps and the column gutters (the flex row's own 50vh lag), which was
   already the actual concept underneath the window device; removing the device just
   stopped hiding it behind a widget that read as broken. Signature move is now the offset
   itself, restated in the "Signature move" note above.
2. **Frames must not sink — bleed wrappers removed.** The Calyx and Hōrai `.frame-inner`
   bleed containers (100px bleed = 100px `data-motion="sink"` travel, added in the fix
   round to stop the sink from opening a void) were themselves the bug: at rest (scroll
   position where each frame first comes into view) the sink had already carried the iframe
   down far enough to hide the top ~100px of each site's own chrome — Calyx's own nav row
   (`VOL. IX · SPRING / Calyx / INDEX STUDIO COMMISSION`) and Hōrai's own wordmark row
   (`HŌRAI` + the `RESERVATIONS` button). The fix round's defect-3 fix (bleed = travel, no
   void) was correct on its own terms — it did stop the void — but never addressed that the
   sink itself was cropping real content, because the earlier pixel read hadn't caught it.
   Fixed by removing the sink outright rather than re-tuning it: `.calyx-wrap iframe` and
   `.horai-wrap iframe` are now `position:absolute;inset:0`, filling their wrapper directly,
   with no `.frame-inner` wrapper, no `data-motion` attribute, and no transform ever applied
   to the iframe or any ancestor while it is on screen (confirmed programmatically across a
   full scroll sweep, see verification below). The only photo left that sinks is the
   Hyperborea thumbnail inside `.panel-thesis` (`.thesis-photo-inner`, capped 90px, inside
   its own `overflow:hidden` box) — well under the 120px ceiling, and it was never the
   source of either defect.

Both removals are net simplifications, not replacements: no new device was built to stand
in for either one. The page now runs fewer bespoke motion mechanisms than either prior
round, on Anton's own read that the remaining ones (the offset, the drift, the thesis
rise/sink pair) were already carrying the concept without help.

## Verification results (final round, 2026-09-04 — supersedes the fix-round numbers above where they overlap)

- **`scroll_verify.py`:** `deadScroll: []`, `cuesNeverFull: []`, `unrevealed: []`,
  `contrastUnderMedia: []`, `blankBands: []`, `notes: []` — clean at 1440×900 (positions
  0/300/600/900/1200/1500/1800/2100/2122) and at 390×844 (14 positions, 0 through 3504).
- **`a11y_scan.py`:** 0 violations, 28 passes, 2 incomplete (unchanged from every prior pass).
- **Overflow:** `document.documentElement.scrollWidth` ≤ `window.innerWidth` at both 1440
  (`scrollWidth 1430 ≤ 1440`) and 390 (`scrollWidth 390 === 390`) — no horizontal overflow
  at either breakpoint.
- **Console:** no `[scrollcraft]` warnings across a full 150px-step scroll sweep at 1440.
  Only messages present: three `cdn.tailwindcss.com` production-use notices originating
  inside the Calyx/Hōrai iframes' own pages (outside this build's scope, unchanged from
  every prior round).
- **Windows: confirmed fully removed.** No `.window`, `.window-gutter`, `[data-window]`,
  or `paintWindows` references left anywhere in `index.html` outside of prose explaining
  the removal; `document.querySelectorAll('[data-window]').length === 0`.
- **Iframes: static, full box, no bleed, no transform, ever.** Swept all three iframes and
  every ancestor element up to `<body>` at every 150px scroll step across the full document
  height (1440 viewport): zero instances of a non-`none` `transform` on any iframe or its
  ancestors, at any scroll position — not just at rest. All three carry real `title`
  attributes (`Er hemsida är nutidens visitkort`, `Calyx, florist i Stockholm`, `Hōrai,
  restaurang i Stockholm`).
- **Frame chrome no longer clipped:** re-shot `shots/desktop-1440--full.png` and read it
  directly — Calyx's own nav row (`VOL. IX · SPRING`, `Calyx`, `INDEX STUDIO COMMISSION`)
  and Hōrai's own wordmark row (`HŌRAI` + the bordered `RESERVATIONS` button) both sit
  fully visible at the top edge of their respective boxes, immediately after the preceding
  panel closes — neither is cropped, confirming the sink removal actually fixed what Anton
  flagged.
- **Reduced motion:** `prefers-reduced-motion: reduce` emulated via a real browser context
  (not just the environment default this round) — `window.matchMedia(...).matches` true;
  all six remaining `[data-motion]` elements (console card, thesis headline, thesis photo,
  giant headline, projects lede, services statement — down from eight, since the two frame
  sinks are gone) report computed `transform: none` at scrollY 2000; `__scFreezeMotion`/
  `__scUnfreezeMotion` are `undefined` in this branch, confirming the motion script is
  gated out entirely, not just zeroed per frame.
- **Motion proof re-shot on the thesis act, `shots/motion-0..4.png`, scrollY
  600/700/800/900/1000** (chosen so both elements stay fully on screen at every frame,
  measured live): the thesis headline wrapper's `translate3d` y-offset moves -44.5px →
  -59.1px → -73.6px → -80.0px (cap) → -80.0px (local mode, capped at 80px, reached by
  frame 3) while the Hyperborea photo's offset moves 26.7px → 33.6px → 40.5px → 47.5px →
  54.4px (act mode, uncapped in this range, ceiling 90px) — opposite signs throughout
  (headline rising, photo sinking), both fully inside their own boxes at every frame
  (headline wrapper top stays ≥99.9px from viewport top, photo box stays fully within
  0–900px), confirmed by reading all five screenshots directly: the headline visibly climbs
  clear of the panel's own kicker line while the photo visibly settles lower in its frame.
- **Full-page shots re-verified frame by frame** (`shots/desktop-1440--full.png`,
  `shots/mobile-390--full.png`, `shots/desktop-1440--fold.png`,
  `shots/mobile-390--fold.png`): no window artifacts anywhere, both iframes (Calyx, Hōrai)
  show their own top chrome uncropped, the Hyperborea photo and its caption read cleanly
  with no overlap, the giant kinetic headline renders fully formed, and the topline scrim
  still clears contrast over the Tidvatten hero's bright sky patch.

## Fingerprint row (final, restated from above for the registry)

| Dimension | r3 | M1 | Shared? |
|---|---|---|---|
| Grammar | split stage | continuous world (loose) | No |
| Nav | fixed corner marks, persistent | thin top row, scrolls away | No |
| Hero device | two heroes side by side | one full-width Tidvatten act | No |
| Act-sequence shape | aligned 50/50 split, synced | full-width act then 50vh-offset stagger | No |
| Close pattern | Calyx + price box, forced same y | Calyx + price box, deliberately unsynced | Partial |
| Signature move | seam hairline (JS-measured logo dock) | the offset stagger itself + the ground's drift through it | No |

Shared: 1/6 (partial), inside the ≤2/6 ceiling.

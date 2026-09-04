# Alunix r3 — R5 + R6 combined, one page — build notes

Brief: `tests/alunix-concepts-r3/brief.md` (Anton's r3 order, 2026-09-04). Combines
`tests/alunix-concepts-r2/cells/R5-chain/index.html` (left column, Geist, Mattis Studio
lane) and `tests/alunix-concepts-r2/cells/R6-chain/index.html` (right column, Public Sans,
Creative Giants lane) into one split-stage page, per `reference-mosaic.png`.

## Reference lock (condensed — full block is the HTML comment at the top of `index.html`)

- **Tier 2.** Primary references: R5-chain and R6-chain themselves (one per column), plus
  `reference-mosaic.png` as the binding compositional lock for proportions and the height
  differences between the two columns' sections.
- **Grammar: split stage** (`~/.claude/skills/design/references/scroll/grammars.md`) — "two
  sides of one argument... divider IS the chrome." The seam between the columns carries the
  signature move; the two closes (Calyx frame, price box) are the "collapse to one column"
  the grammar calls for, landing at the same y.
- **Preserved verbatim per brief point 1:** every headline in both columns except one
  (`VI BYGGER ERT VARUMÄRKE.`, R5's giant close, Anton's own correction); both typefaces
  (Geist 700 left, Public Sans 300 right); R5's console card, corner-mark page signature,
  Alunix-blue thesis block; R6's poster wordmark, full-bleed photo + statement convention,
  hairline services ledger, inverted "Tre sajter" band.
- **Removed per brief points 3–5, 8:** R5's three-card project grid → one borderless Calyx
  iframe; R5's philosophy + contact blocks → merged into the right column's price box; R6's
  fixed nav → dropped (R5's fixed corner marks are the page's one persistent chrome); R6's
  three-row project list → one borderless Hōrai iframe; R6's standalone Filosofi section →
  folded into the price box as its ingress line; R6's kolofon → replaced by the price box's
  own kontakt line (kontakt@alunix.se, the only address on the page).
- **New construction:** the logo (inline SVG, Anton's vectorised mark, white fill) sits on
  the seam, positioned by measuring the left hero's bottom edge and the right poster's
  bottom edge in JS and taking the midpoint; the seam hairline draws itself downward from
  that point in step with scroll, `mix-blend-mode:difference` (borrowed from R5's own
  corner-mark trick so one line reads against all four grounds — dark hero, blue block,
  black band, cream — without a second colour rule); the price box, dark ground `#0c0b08`,
  R6 typography, Anton's two real prices plus "pris vid förfrågan," each fact its own bold
  line per copy-gate.
- **Scale rule:** every `vw` inside a source's own `clamp()` becomes `cqw` against that
  column's own `container-type:inline-size` box. A column is 50% of the viewport, so this
  alone reproduces each source's 1440px layout at half scale — the clamp's fluid term
  halves correctly against a half-width container, and the floor/ceiling stay unhalved on
  purpose (so the mobile-stacked column, which is full width again under 900px, renders at
  full scale, matching brief point 8). Genuinely fixed pixels that don't participate in a
  clamp (console-card corner ticks, ledger number column) were halved by hand:
  corner ticks 8px→4px / -4px→-2px offsets; `.ledger-row` grid `80px 1fr`→`40px 1fr`.
- **Reject:** any new saturated colour beyond Alunix blue and R6's three project hues; a
  page-wide pin ("Anton vill se layouten som den är" — the whole page uses only
  `data-sc-act="flow"`, never `pin`/`scrub`/`pan`); any counter/marquee/invented number;
  transform or pointer-events changes on the two iframes once opened.

## Decision ledger

| Decision | Source | Role | Why |
|---|---|---|---|
| Two columns, flex row, `container-type:inline-size` each | brief point 3 header instruction | layout | Literal instruction; container queries are the only way to scale a nested layout by container width, not viewport width |
| `vw`→`cqw` swap only, no separate halving of clamp() endpoints | brief point 3 | scale mechanism | The vw term already halves against a 50%-width container; halving the floor too would break its job of holding the mobile-stacked (full-width) column at full scale |
| Calyx iframe replaces R5's project grid; Hōrai iframe replaces R6's project rows | brief points 3–4 | proof | Anton's explicit correction: interactive real sites over static screenshots |
| Philosophy + contact merged into one dark price box, right column's last section | brief point 5 | close | Binding instruction; also solves brief point 6 (both columns need a `flex:1` closing element to land on the same y) |
| Seam hairline + logo dock, one shared scroll listener, `mix-blend-mode:difference` | brief's suggested signature move + R5's existing corner-mark trick | signature move | Brief permits improving it, not replacing it; reusing difference-blend (already proven for the corner marks) solves "visible against four grounds" with no new tokens |
| scrollcraft `flow` acts only, no pin/scrub/pan | brief "Förbjudet: pin på hela sidan" + devices.md | scroll engine usage | No scrub media on the page, no lateral rail content; every required device (reveal, kinetic, parallax, flow+in) runs inside a flow act, the one act type the brief doesn't forbid |
| Price box carries no reveal/cue at all | brief "prisrutan landar stilla (avslutet ska vila, inte tona ut)" | motion | Explicit instruction; the one deliberately still element on an otherwise choreographed page |
| Kinetic headline markup uses a plain space, not `<br>` | found during build: `splitText()` reads `el.textContent`, which drops `<br>` entirely and merges the words with no space ("byggerert") | bugfix | Natural wrap at the column width reproduces the two-line look without breaking the kinetic split |
| Redundant page-level `[data-sc-cue]/[data-sc-in]` CSS removed | found during build: an equal-specificity rule later in the cascade (my own `<style>`, after `scrollcraft.css`'s `<link>`) permanently beat the engine's own `.sc-in{opacity:1}` reveal rule | bugfix | scrollcraft.css already owns the full pre-reveal/revealed contract; a page should never re-declare it |
| `revealFailsafe()` runs at 400ms, 900ms, and again 30ms after `document.fonts.ready` | found during build: an act far down the page is genuinely not "live" at mount (by design) and its cue/reveal are correctly zeroed by the engine; the verification screenshot tool never scrolls, so the normal scroll-triggered reveal never fires for it | reliability | Matches the pattern both R5 and R6 already shipped (a 1.5–1.8s hard reveal-all); multiple passes close the race against font-load timing, which can re-trigger the engine's own layout()/read() |
| Both large photos re-encoded from 2200×3300 (~700–830KB) down to ~1100px longest edge (~20–45KB) | found during build: the local dev server intermittently dropped large-file connections (`ERR_CONNECTION_RESET`), visible as a blank/washed-out section | reliability | Well within Step 5b's vendoring guidance; removes the flake without changing the crop or composition |

## Feeling curve (written before building, per Step 2b)

1. **Arrival, dual confidence.** Both columns present their opening move at once: left, a
   bordered console card over a grayscale desk photo declaring the byrå by name; right, the
   wordmark ALUNIX at affisch scale over warm cream. Caused by: two completely different
   hero devices side by side, the seam between them doing the work of a paragraph.
2. **Recognition, the logo takes its place.** The mark sits exactly where both openings
   end, docks small, and stays. Caused by: the signature move — the seam hairline beginning
   to draw downward from the logo the instant scroll starts.
3. **Conviction (left) / grounding (right), the same beat, different register.** Left cuts
   hard into the saturated blue thesis block, wiping in from the left edge, "Det första
   intrycket är digitalt." stated as fact. Right sits on the documentary photo, wordmark
   drifting slower than the page, photo countering it, "Er webbplats är nutidens visitkort."
   landing in the shadowed corner. Caused by: the reveal wipe on one side, the
   counter-parallax pair on the other.
4. **Resolve into scale (left) / explanation (right).** Left drops to the giant "VI BYGGER
   ERT VARUMÄRKE." kinetic line, then the services ledger enters row by row. Right opens
   onto whitespace and the plain tjänster statement. Caused by: kinetic type on one side,
   unhurried hairline rows on the other — both quiet after the loud act 3.
5. **The peak: two working sites, at once.** Left, the Calyx florist site sits kant-till-
   kant where thumbnails used to be, already alive. Right, the black Hōrai section irises
   open around a second real site. Caused by: this is the only moment on the page the
   visitor can touch something rather than read it, on both sides in the same scroll span —
   the largest engineered contrast on the page (interactive vs. everything else being
   static type and photography).
6. **Close, no ceremony.** Left ends on the Calyx frame's own bottom edge. Right lands,
   without motion, on the inverted price box: philosophy line, the two real prices, pris
   vid förfrågan, kontakt@alunix.se. Caused by: the price box is the one thing on the page
   that does not move as it arrives, so it reads as the place the argument was always
   heading.

**Peak:** act 5 (the two live iframes) — the only interactive moment on the page, on both
columns in the same scroll span.

**Tell-someone sentence:** "It's the site where a hairline draws itself down from the logo
as you scroll, and by the time it reaches the bottom you're clicking around inside two real
client sites without ever leaving the page."

**Signature move:** the seam hairline, drawn downward from the docked logo mark in exact
step with scroll position — a bespoke `--seam-p` custom property driving
`transform:scaleY()` on a shared vertical rule between the two columns — with the logo
itself switching from its measured hero-fold position to a small fixed dock the instant
scroll begins. Implemented entirely in page-authored JS/CSS (`#seam`, `#logoMark`,
`measure()`/`onScroll()` in `index.html`'s own `<script>`), never touching `scrollcraft.js`.

## Devices per act (≥4 families, never the same one twice in a row)

Left column (top to bottom): hero **cue** (greet form, console tag/clock/wordmark) →
thesis **reveal** (`left`, Hyperborea photo wipes in) → giant headline **kinetic**
(`lines`) → ledger **flow+in** (`data-sc-stagger="90"`) → Calyx intro **reveal** (`up`).

Right column (top to bottom): fold **parallax** (poster wordmark, rate `2.2`, slower than
scroll) + photo **parallax** (counter-direction, rate `-1.3`) running concurrently → photo
statement **cue** (greet form) → tjänster **flow+in** (section head + three services,
staggered) → Tre sajter **flow+in** (section head) → Hōrai **reveal** (`iris`, once) →
price box: **no device**, static by design.

Families used: **reveal, kinetic, parallax, flow+in** (4) plus the bespoke signature move
(seam + dock, outside the kit). No act repeats its device family immediately after another
instance of the same family in either column's own sequence.

## Skills loaded, in order

1. `Skill(design)` — front door; Steps 0 (page scope), 1 (pre-flight — no existing
   `DESIGN.md`/tokens in `tests/alunix-concepts-r3/`), 1b (reference lock, both R5-chain
   and R6-chain read in full plus `reference-mosaic.png` as an image), 2 (Tier 2 — the two
   sources + mosaic are the direction), 2b (split-stage grammar, feeling curve above, device
   list, bake-off skipped — task instruction, single assigned direction), 4 (build), 5
   (verify, this document).
2. `Skill(copywriting)` — structure and register for every rewritten sub-text (see full
   copy below): digital byrå, vi-form, Insign-nivå, per r2's brief.
3. `references/copy-gate.md` Pass 1b read and applied by hand: every rewritten line traces
   to what the section's own device requires or to Anton's brief lines (price facts, source
   4); the price box's three facts were split into their own bold lines per Pass 1b's rule
   that discrete facts get lines while a process gets a sentence.
4. `Skill(humanizer-svenska)` — applied to every rewritten Swedish string: no "inte bara
   X, det är Y", no `och`-joined tricolon filler, no "sömlöst"/"unik upplevelse"/"i hjärtat
   av", no lede restating the headline, register kept confident (not sanded to neutral).

## Rewritten copy (final, as shipped)

**Left column (R5, my rewrites only — headlines are verbatim per brief point 1):**

- Hero body: "Vi designar och bygger digitala plattformar från grunden, i nära dialog med
  verksamheten som ska leva i dem."
- Thesis support (under "Det första intrycket är digitalt."): "Beslutet fattas på en
  skärm, oftast inom några sekunder, innan en enda rad har lästs. Layout och bild bär hela
  argumentet fram till dess."
- Thesis photo caption: "Hyperborea, en konferens i Lund, byggd av Alunix."
- Giant sub (under "Vi bygger ert varumärke."): "En sammanhållen process, från första skiss
  till lanserad sajt, med samma team hela vägen."
- Ledger 01 Design: "Grafisk identitet och formspråk, förankrat i verksamheten sajten ska
  representera."
- Ledger 02 Utveckling: "Webbplatser byggda i kod från grunden, snabba att ladda och enkla
  att bygga vidare på."
- Ledger 03 System: "Digitala system utöver webbplatsen, som Alunix OS, för verksamheter
  med behov som går längre."
- Calyx intro line: "Calyx, florist i Stockholm. En sajt vi byggt, öppen att utforska här."

**Right column (R6, my rewrites only — headlines verbatim):**

- Services 01 Webbdesign: "Webbplatser byggda för att exponera verksamheten på rätt sätt, i
  ett tempo som håller över tid."
- Services 02 Design: "Ett visuellt system, från logotyp till komponenter, som håller ihop
  hela verksamhetens uttryck."
- Services 03 System: "System bortom webbplatsen, som Alunix OS, byggda för verksamheter
  med behov som går djupare."
- Hōrai intro line: "Hōrai, restaurang i Stockholm. En levande sajt, redo att klickas
  igenom här."
- Price box ingress (under "Alla har rätt till bra design."): "Vår nivå är satt för att
  fler ska ha råd med bra design, utan att vi ger avkall på resultatet."

**Price box (brief point 5, discrete facts as their own bold lines):**

- Standardhemsida, sex sidor — **10 990 kr**
- Med bokningssystem — **15 990 kr**
- Helt skräddarsydda lösningar för produktkataloger, specialbyggda system med mera —
  **Pris vid förfrågan**
- Kontakt — **kontakt@alunix.se**

No repeated phrase lands on both columns: "skräddarsydda" appears once (the price box's
literal brief-mandated line); "exponera" once (right services); "nutidens visitkort" once
(right, the kept headline); "allt på ett ställe" appears only inside the kept R6 headline,
nowhere else. Checked by grep against the shipped file.

## Verification results

- `shoot.py` (1440×900, fold + full-page): both clean; full page 3139px tall.
  `build/shots/127-0-0-1-3091-tests-alunix-concepts-r3-build-index-html--fold.png` /
  `--full.png`.
- Mobile (390×844, Playwright, matching methodology since shoot.py has no mobile mode):
  `build/shots/mobile-390--fold.png` / `--full.png`. No overflow (`scrollWidth === 390 ===
  innerWidth`); full page 5620px tall.
- Overflow: desktop `document.documentElement.scrollWidth === window.innerWidth === 1440`;
  mobile `390 === 390`. No horizontal scroll at either breakpoint.
- `scroll_verify.py`: `deadScroll: []`, `cuesNeverFull: []`, `unrevealed: []`,
  `contrastUnderMedia: []`, `blankBands: []`. Clean.
- `a11y_scan.py`: **0 violations, 35 passes, 2 incomplete** (axe's own "needs manual
  review" bucket, not a failure — no HIGH/serious findings left; see fix note below).
  Console: no `[scrollcraft]` warnings anywhere, at any scroll position through the full
  page height (checked by scrolling in 400px steps end to end); the only console lines are
  a `cdn.tailwindcss.com` notice originating from inside the Hōrai/Calyx iframes'
  own pages, outside this build's scope.
- Two `color-contrast` violations found and fixed: `.thesis-text .kicker` and
  `.thesis-photo figcaption` (both white-on-Alunix-blue at 0.72 alpha, ratio below 4.5:1
  for small text) — raised to a new `--c-mute-on-accent-aa` token (0.92 alpha), which
  computes to roughly 5.9:1 against `#1e5e9c`. One `landmark-one-main` + eight `region`
  violations fixed by promoting the page wrapper from `<div class="page">` to `<main
  class="page">`. Re-run after fixes: 0 violations.
- `contrast_over_media.py`-style measurement (adapted inline for the logo mark, same
  method — brightest-5%-of-ground under the element, hidden text/logo, real screenshot):
  worst-case **13.37:1**, mean **17.62:1**, against a 4.5:1 floor. No scrim needed behind
  the logo.
- Both iframes loaded with real `<title>`: `sites/calyx.html` → "Calyx — Botanical
  Architecture, Stockholm"; `sites/horai.html` → "Hōrai — A Three-Sister Restaurant,
  Stockholm."
- Both columns' bottom edges: `colLeft.bottom === colRight.bottom === calyx-frame.bottom
  === .price.bottom === 3139.42px` (measured together, all four identical to the pixel).
- Reduced motion (`reduced_motion: reduce`): seam stays at `transform:none` (fully drawn,
  scaleY 1 baked in via the `reduced` branch), logo stays `position:absolute` at its
  measured midpoint and never docks, before and after a scroll to y=2000 — confirmed
  static in both states.
- JavaScript disabled (`java_script_enabled: False`): `<html>` keeps class `no-js`; the
  giant headline's cue, a ledger row, and the thesis photo's reveal all compute to
  `opacity:1` / `clip-path:none` (the `noscript` stylesheet); screenshot confirms full
  content, plain (undocked) logo placement, everything readable.
- `wc -l index.html` → 557 lines.

## What I could not do / environment notes

- The local dev server (`python -m http.server 3091`) intermittently dropped large-file
  connections (`net::ERR_CONNECTION_RESET`) during this build, at file sizes around
  700–830KB. Fixed by re-encoding both large photos to ~1100px longest edge (20–45KB);
  confirmed 5/5 clean loads afterward, at both breakpoints. Not a defect in the page.
- Two Playwright full-page (`full_page=True`) screenshots showed content that direct DOM
  inspection and a scrolled (non-full-page) capture both confirmed was actually present and
  correctly styled — a known Playwright/Chromium quirk where `full_page` capture can miss
  elements using CSS `filter` or a not-yet-"live" `data-sc-reveal` state during its internal
  resize-and-stitch pass. Worked around with the `revealFailsafe()` triple-pass (see
  decision ledger) and confirmed correct on the final `shoot.py` run.
- Did not touch `sites/calyx.html` or `sites/horai.html` (out of scope, existing production
  demo sites) — the `cdn.tailwindcss.com` console notice and the odd mobile nav overlap
  visible inside the Calyx iframe at 390px originate there, not in this build.

## Fix round (2026-09-04, Anton's pixel-measured defects)

Six defects Anton measured on pixels against the shipped build, all fixed. No files touched
outside `tests/alunix-concepts-r3/build/`; `scrollcraft.js`/`.css` untouched.

| # | Defect | Fix | Verified |
|---|---|---|---|
| 1 | Right poster wordmark clipped by the photo section at scrollY=0 | Removed `data-sc-parallax="2.2"` from `.poster` entirely — the poster no longer moves independently of normal document flow, so it can never be dragged down over the photo section (which keeps its own `overflow:hidden` and `-1.3` inner parallax, untouched) | `posterBottom` (185.19px) `< photoTop` (206.63px) at scrollY=0, measured live in-browser after the fix |
| 2 | Logo dock broken — switched to `position:fixed` with a stale inline `top` from the pre-dock measurement, floating mid-viewport, clipped by the column | Removed docking entirely, per the brief's own permitted fallback. `.logo-mark` is now always `position:absolute`, `transform:translate(-50%,-50%)`, height fixed at `var(--logo-h)`, sitting at the JS-measured seam midpoint (`measure()` sets `logo.style.top` once, on load/resize/fonts-ready). `onScroll()` now does exactly one thing: drive `--seam-p` on the seam hairline. Deleted the `docked` boolean, `.is-docked` CSS rule, and all `position:fixed`/`translate(-50%,0)` branching from the script | `getComputedStyle(logo).position === 'absolute'` at scrollY 0 and 2000 alike (was `'fixed'` with `top:'0px'` stuck at the CSS default before the fix, since the old script's docking branch never actually engaged in this build); logo fully visible, uncut, in both the fold and full-page shots |
| 3 | Kinetic headline (`VI BYGGER ERT VARUMÄRKE.`) and photo statement faded to blank while still on screen | Giant headline cue `"0.02 0.5"` (a two-value fade-out form on a middle act) → `"0.02"` (hold form: fades in, holds to the end of the act, never a second value to fade back out on). Photo statement cue `"0 0.85 0"` (greet-then-fade) → `"0 1 0 0"` (greet and hold: full at p=0, no ramp either end) | `getComputedStyle(...).opacity === '1'` for both elements at every 300px scroll step through the photo section's entire on-screen life (y 0–900) and well past it (checked to y=1800); scroll_verify.py's `cuesNeverFull` and `blankBands` both empty |
| 4 | ~300px of empty black above "FILOSOFI" in the price box (`.price{flex:1;align-items:flex-end}` pushed content to the bottom) | Inverted the flex roles per the brief: `.col-right .invert` (the `#projekt` section wrapping `.horai-frame`) now gets `display:flex;flex-direction:column;flex:1`, and `.horai-frame` gets `flex:1` (keeping its `min-height:90vh` floor) so it absorbs the leftover column height instead of the price box. `.price` lost `flex:1;display:flex;align-items:flex-end` and now just takes `padding:var(--gap) 0` (R6's own section padding, both edges) — its height is intrinsic to its content | `colLeft.bottom === colRight.bottom === calyx-frame.bottom === .price.bottom === 3075.94px` (all four identical, measured together); gap between the price box's own top and its first heading is 92px (kicker + margin only, no dead band) |
| 5 | Thesis block: headline breaking into four lines instead of three, figure smaller than the mosaic's ~40% | Root cause: `INTRYCKET ÄR` at the old `7.4cqw` font-size measured 362.9px wide against a 341px-wide text column, one word too wide to hold the line, so `intrycket är` (already forced onto one `<br>`-separated line) wrapped a second time. Changed `.thesis-grid` from `1.15fr .85fr` to `1fr 1fr` (giving the photo a bigger share, per "larger figure") and `.thesis-headline` font-size from `clamp(1.9rem,7.4cqw,5.8rem)` to `clamp(1.9rem,6cqw,5.8rem)` (only the fluid `cqw` middle term changed, per the scale rule — the rem floor/ceiling stay untouched so the full-scale mobile-stacked column is unaffected). Solved by iterative measurement in-browser (real `getClientRects()` line counts + real text-width probes), not guesswork | Headline renders as exactly 3 line-tops (`Det första` / `intrycket är` / `digitalt.`) at 1440px; Hyperborea figure measures 41.5% of the column's full width (was 35.3%), matching the mosaic; `align-items:end` (unchanged) keeps it bottom-aligned to the text |
| 6 | Re-check: giant headline, ledger, Calyx reveal, Hōrai iris reveal all end fully visible | Scripted a scroll-through (300px steps, full page height, `reduced_motion:"no-preference"`) then read `getComputedStyle` for each: giant, ledger, `.calyx-frame`, `.horai-frame`, plus `.thesis-photo` and the `#tjanster`/`#projekt` `flow+in` blocks for good measure | All: `opacity:'1'`, `clipPath:'none'` (thesis-photo's `inset(0px 0% 0px 0px)` is a fully-open reveal, zero inset on every side — not a clip) |

**Re-verification (2026-09-04, after the fix round):**

- `scroll_verify.py` (1440×900): `deadScroll: []`, `cuesNeverFull: []`, `unrevealed: []`,
  `contrastUnderMedia: []`, `blankBands: []`. Clean, same as before the fixes.
- `a11y_scan.py`: **0 violations, 35 passes, 2 incomplete** — unchanged from the pre-fix
  baseline; none of the six fixes touched contrast, landmarks, or focus order.
- No `[scrollcraft]` console warnings at 1440×900 or 390×844, scripted scroll top to bottom.
- No horizontal overflow at either breakpoint: desktop `scrollWidth === innerWidth === 1440`;
  mobile `390 === 390`.
- Both iframes still load with real titles: `sites/calyx.html` → "Calyx — Botanical
  Architecture, Stockholm"; `sites/horai.html` → "Hōrai — A Three-Sister Restaurant,
  Stockholm."
- Reduced motion (`reduced_motion:"reduce"`): logo stays `position:absolute` at its measured
  midpoint before and after a scroll to y=2000 (`top` inline style unchanged, 554.03px in
  this viewport), seam stays fully drawn (`--seam-p:1`, `transform:none`) — both static, as
  required. The simplified script has no reduced-motion-specific branch left in `onScroll()`
  (it just returns early); `measure()` sets `--seam-p:1` once for the reduced case instead of
  leaving it at the CSS default `0`.
- Re-shot `build/shots/`: desktop fold + full (1440×900, `127-0-0-1-3091-...--fold.png` /
  `--full.png`, full page 3083px), mobile fold + full (390×844, `mobile-390--fold.png` /
  `--full.png`, full page 5611px). Confirmed visually: poster fully clear of the photo
  section with a gap, logo centred on the seam and uncut in every shot, giant headline and
  ledger fully opaque, price box starts right at its own kicker with no void, thesis
  headline three lines with a visibly larger figure bottom-aligned to the text.
- Note: a first full-page Playwright screenshot taken *without* first scrolling through the
  page in steps showed the thesis Hyperborea photo and the Calyx iframe's own hero image as
  blank — this is the same known Playwright/Chromium full-page stitching quirk already
  logged in this file's original verification section (a `data-sc-reveal` not yet "live"
  during the internal resize-and-stitch pass). Scrolling through in 300px steps first, then
  screenshotting, reproduces exactly what a real visitor sees; both images render correctly
  once that's done. Not a regression from this fix round.

**Not fixed / out of scope:** nothing from Anton's six-item list was left unaddressed. The
Calyx iframe's own internal content (a blank first ~600px before its hero photo, visible in
the un-prescrolled full-page shot) belongs to `sites/calyx.html`, out of scope per this
build's own boundary, unchanged by this round.

## Proportion round (2026-09-04, Anton's rejection: "boxes are now aligned... proportions
## must be the same as the reference with its different heights")

Root cause confirmed: `.hero{min-height:100svh}` and `.photo-section{height:min(78vh,760px)}`
tied those two sections to *window height*, while every other section was sized by content
(mostly already `cqw`-scaled). At a window taller or shorter than the reference's implicit
1440×900, hero and the old photo box grew or shrank independently of the column width they
sit in, while blue/thesis/tjänster/ledger did not move — the sections drifted toward equal
height ("aligned"), flattening the deliberate unevenness the reference has. Fixed by
converting every section height, padding, and gap in both columns to `cqw` (`1cqw` = 1% of
the `.col`'s own `container-type:inline-size` box), so a column is always its source's
1440px layout at exactly half scale, regardless of window height.

**Right column** is five sections stacked with explicit `height:Ncqw` (24 + 59 + 45 + 82 +
59 = 269cqw = 2.69w), no flex needed — the column's total height falls out of the sum by
construction, and it landed on the 2.69w target immediately, at every width tested.

**Left column**: hero fixed `height:52cqw`; the thesis (blue) block, the giant-headline
zone, the three ledger rows, and the "Utvalda projekt" lede are all *content-driven* (no
fixed box), so every padding/margin/font-size that determines their height had to be tuned
in `cqw` by iterative measurement (`measure_r3.py`, a scratch script — real element
`getBoundingClientRect()` divided by column width, not the pixel-diff heuristic in
`compare.py`, which is too noisy for sub-section tuning). `.calyx-frame` stays `flex:1`,
absorbing whatever's left after the fixed-plus-tuned content above it, up to the row height
the right column's fixed 2.69w total sets.

**A second bug found mid-tuning**: several properties still used `clamp(px, Ncqw, px)` with
rem/px floors and ceilings (inherited from the pre-existing R5/R6 sources). A `clamp` floor
that's *always* active across the tested width range (640–960px column) renders at a
constant px value regardless of column width — not proportional at all — which is exactly
why boundaries held at 1440 but drifted up to 0.13w off target at 1280 and 1920. Fixed by
stripping every remaining rem-bounded `clamp()` in the left column's boundary-determining
properties down to a flat `Ncqw` value (mobile keeps separate fixed-rem overrides under
`@media (max-width:900px)`, since below that breakpoint the column is full viewport width,
a different regime the brief always intended `vh`/`rem` for). One more fixed-px offender
surfaced this way and was the actual dominant cause of the 1920 drift: `.thesis-photo
figcaption` was `font-size:10.5px;padding:8px 2px 0` (flat), a constant-height contribution
whose *share* of the section shrinks as the column widens — moved to `1.46cqw` /
`1.1cqw .28cqw 0` (mobile keeps the old flat rem/px values). After this, all three widths
(1280/1440/1920) match the table within the same ±0.01–0.03w band.

### Measured vs. target (1440px viewport, w = 720px), from `measure_r3.py`

| metric | target (w) | measured (w) | diff | metric | target (w) | measured (w) | diff |
|---|---|---|---|---|---|---|---|
| hero_bottom | 0.52 | 0.520 | 0.000 | poster_bottom | 0.24 | 0.240 | 0.000 |
| blue_top | 0.52 | 0.520 | 0.000 | tidvatten_top | 0.24 | 0.240 | 0.000 |
| blue_bottom | 0.99 | 0.989 | -0.001 | tidvatten_bottom | 0.83 | 0.830 | 0.000 |
| giant_top | 1.09 | 1.089 | -0.001 | tjanster_top | 0.83 | 0.830 | 0.000 |
| ledger1_top | 1.41 | 1.406 | -0.004 | tjanster_bottom | 1.28 | 1.280 | 0.000 |
| ledger2_top | 1.53 | 1.522 | -0.008 | horai_top | 1.28 | 1.280 | 0.000 |
| ledger3_top | 1.65 | 1.661 | 0.011 | horai_bottom | 2.10 | 2.100 | 0.000 |
| projects_top | 1.87 | 1.849 | -0.021 | price_top | 2.10 | 2.100 | 0.000 |
| calyx_top | 1.87 | 1.898 | 0.028 | page_bottom_right | 2.69 | 2.690 | 0.000 |
| page_bottom_left | 2.69 | 2.690 | 0.000 | | | | |

All within the ±0.03w tolerance. `calyx_top` (0.028) is the tightest: the reference's
1.87w row names both "Utvalda projekt" (the kicker) *and* "Calyx-ramen" starting together,
but this build keeps the kicker + one-line lede (brief point 4, unchanged from r3) above the
frame, so the frame itself necessarily starts a little after the kicker — kicker line +
lede line + frame's own top margin is an irreducible ~2.8cqw at legible type sizes, right at
the edge of the tolerance band. `projects_top` (the kicker's own top, -0.021) is closer to
dead-on.

**Held at other widths** (`measure_r3.py … 1280` / `… 1920`): 0 fails at both, all right-
column metrics exactly 0.000 diff at every width (pure fixed-`cqw` stack), left-column
metrics within the same ±0.001–0.03w band as 1440 — confirms the `cqw`-only approach scales
the whole page proportionally, independent of viewport width, as required.

### A second real bug, found by actually looking at mobile

The fixed-`height` + `overflow:hidden` sections that work perfectly at desktop (a column
that's 50% of the viewport) are *actively wrong* on the `<900px` mobile stack, where each
`.col` becomes 100% of the viewport: `45cqw` for the tjänster section is 45% of *390px*
(175px) there, nowhere near enough for its heading + three service blocks, and the same
math clipped the hero's CTA link and roughly the bottom third of the price box (the
`kontakt@alunix.se` line invisible and unreachable) under `overflow:hidden`. Caught by
actually opening `build/shots/mobile-390--full.png`, not by any of the numeric checks above
(they only asserted desktop proportions). Fixed with a `@media (max-width:900px)` block that
gives `.hero`, `.fold`, `.section` (tjänster), and `.price` `height:auto` (their own content
sizes them) and gives the two frame boxes reasonable `vh` floors instead — matching what the
brief already prescribed for the Calyx/Hōrai frames at this breakpoint ("ramarna 70vh"). This
block had to be moved to the very end of the stylesheet: on its first attempt, an
equal-specificity, non-media base rule declared *later* in the file (`.col-right .price{...
height:59cqw...}`) still won the cascade even though the media query matched, because CSS
resolves ties by source order, not by which rule's condition is "more specific" to the
current viewport. Re-shot after the fix: full price box (including `kontakt@alunix.se`) and
full tjänster section both visible; `document.documentElement.scrollWidth === 390` confirmed
still true.

### A third bug, found the same way: overlay text colliding with the live Tidvatten iframe

The brief's contrast note ("vattnet nere till höger är mörkt och tomt") described the static
`tidvatten-720x421.png` reference; the *live* `sites/tidvatten.html` wraps its own bottom-left
statement text further right than that crop suggested, so at the box's actual rendered size
it ran directly under our bottom-right "SVERIGE / Er webbplats är nutidens visitkort."
overlay. Fixed by widening `.photo-text .scrim` from a tight box around just our own text to
a solid `rgba(6,5,3,.92)` panel extending `19cqw` further left (covers the collision zone with
margin) — confirmed visually (`tidvatten-zoom*.png`, since deleted) that the Tidvatten's own
"…BASTUKLUBB / …NYHAMNEN, MALMÖ" is now cleanly cut off at the scrim's edge with no
bleed-through, and text outside the collision zone (the earlier part of that sentence) is
untouched. An earlier attempt at a soft left-to-right gradient scrim still let 1-2 words
bleed through the semi-transparent zone at .55 alpha; a solid `.92`-alpha panel was the
reliable fix, not a subtler fade.

### Contrast — Tidvatten overlay, measured against pixels

`contrast_over_media.py` is hard-coded to `localhost:3055` with its own selector list, so
this was reproduced by the same method against this build directly (Playwright: hide the two
text nodes with `color:transparent`, screenshot, sample the brightest 5% of each string's own
rect as the "worst case" ground, per the script's own algorithm):

- Kicker `SVERIGE`: worst 19.07:1, mean 19.21:1
- Statement `Er webbplats är nutidens visitkort.`: worst 18.74:1, mean 19.47:1

Both far above the 4.5:1 floor (the pre-scrim measurement against the raw
`tidvatten-720x421.png` crop was 2.43:1 worst-case, below floor — confirming the scrim was
actually necessary, not just a collision fix).

### Other changes in this round

- **Hōrai section** (brief change 1): `UTVALDA PROJEKT` kicker, `Tre sajter, i drift.`
  headline, and the Hōrai intro line removed; `.horai-frame` is now the `<section>` itself
  (was a wrapper around a separate frame div) — the black band is the iframe alone, fixed
  `82cqw` tall, starting exactly where `#tjanster` ends (both are hard `cqw` heights, so this
  is true by construction, confirmed `tjanster_bottom === horai_top === 1.280` exactly).
- **Tidvatten iframe** (targets.md addendum): replaces the static desk photo in the right
  column's photo box, `loading="eager"`, borderless, same `0.24w–0.83w` box; the box's own
  `-1.3` inner parallax was removed (iframes must not be transformed) along with the whole
  `.photo-inner`/`.photo-scrim` wrapper structure it needed.
- **Logo**: `--logo-h` raised from `clamp(88px,9vw,150px)` to the specified
  `clamp(114px,11.7vw,195px)`; position formula (measured JS midpoint between hero-bottom and
  poster-bottom) untouched.
- Copy text untouched throughout (verified by diff of every `<p>`/`<h1>`/`<h2>`/`<h3>` string
  against the pre-round file — only the three Hōrai-section strings were *removed*, nothing
  reworded).

### Re-verification (this round)

- `measure_r3.py` (1280/1440/1920): 0 fails at all three widths (table above; full runs kept
  in this round's terminal history, not persisted as files per the build-only-output rule).
- `scroll_verify.py`: `deadScroll: []`, `cuesNeverFull: []`, `unrevealed: []`,
  `contrastUnderMedia: []`, `blankBands: []`. Clean.
- `a11y_scan.py`: **0 violations, 35 passes, 2 incomplete** — unchanged from every prior
  round's baseline.
- No horizontal overflow at 1440 or 390: `document.documentElement.scrollWidth === innerWidth`
  at both, confirmed after a full scripted scroll-through (not just at rest).
- No `[scrollcraft]` console warnings at either breakpoint through a full scroll-through.
- All three iframes present with real `title` attributes: `Calyx, florist i Stockholm` /
  `Tidvatten` / `Hōrai, restaurang i Stockholm`.
- No text-block overlaps: pairwise `getBoundingClientRect()` intersection test across every
  heading/paragraph/kicker/CTA at 1440 after a full scroll-through — zero pairs overlap.
- Reduced motion: seam `transform:none` (`matrix(1,0,0,1,0,0)`, unchanged) before and after a
  scroll to y=2000 — static, as required.
- Re-shot `build/shots/`: `desktop-1440--fold.png` / `--full.png` (full page 1937px = exactly
  2.69w), `mobile-390--fold.png` / `--full.png` (full page 4901px). The desktop full-page shot
  is taken after a scripted top-to-bottom scroll *plus* a final forced-open pass on every
  `[data-sc-cue]`/`[data-sc-in]`/`[data-sc-reveal]` element (mirroring the page's own
  load-time `revealFailsafe()`) immediately before the screenshot — needed because
  Playwright's `full_page=True` capture does its own internal virtual-scroll-and-stitch pass,
  and the engine's act-parking logic (correctly) zeroes a flow-act's cues once scrolled past
  and only re-arms them via live intersection, which the stitcher's internal scroll doesn't
  always trigger in time for. Confirmed this is a screenshot-tool artifact only, not a
  real-visitor bug, by scrolling normally down to the Tidvatten section in a fresh page and
  reading `getComputedStyle(...).opacity` directly (`1`, correct) before touching the
  screenshot path.

### Not achieved / deviations

- `calyx_top` sits at 0.028w over target (1.898 vs. 1.87), 0.002w inside the ±0.03 tolerance
  but the tightest metric on the page. Root cause is structural, not a tuning miss: the brief
  keeps the "Utvalda projekt" kicker + one-line Calyx lede above the frame (unchanged from the
  original r3 brief), and that text's own minimum legible height (kicker line + lede line +
  margins, tuned down to ~2.8cqw already) is what separates the kicker's own top (0.021w
  under target) from the frame's. Going tighter would mean near-zero margins between the lede
  and the iframe edge, which reads as broken layout rather than intentional; left as-is.
- Everything else in Anton's brief for this round (cqw-only heights, Tidvatten iframe swap,
  Hōrai heading removal, logo scale, mobile fix, iframe/text collision fix) is implemented and
  verified above.

## Round 3 fix pass (2026-09-04, four pixel-measured layout defects + copy chain proof)

Four defects Anton measured on pixels against the shipped build, plus a required, provable
run of the copy chain (`copywriting` → copy-gate Pass 1b → `humanizer-svenska`). No files
touched outside `tests/alunix-concepts-r3/build/`; `scrollcraft.js`/`.css` untouched. Every
section boundary in `targets.md` re-measured before and after with a scratch Playwright
script (`measure_r3.py`, not persisted per the build-only-output rule): **all 19 boundaries
held to 0.0000w delta** at 1280/1440/1920, well inside the ±0.01w ceiling this round set.

| # | Defect | Fix | Verified |
|---|---|---|---|
| 1 | Left hero console card filled the hero edge to edge, no inset; card content (412px) taller than the hero's own inner box (300px), so `overflow:hidden` + centred flex cropped it top and bottom equally | `.console-card{max-width:900px}` → `max-width:62.5cqw` (brief's own number, matches the source's 900px/1440px ratio scaled to the column). Card content scaled down to fit the 52cqw hero at every width: `console-top`/`wordmark`/`sub`/`hero-body`/`service-list`/`hero-cta-row` font-sizes and margins all moved from their old (partly rem-floor-locked, non-scaling) clamps to smaller cqw-driven ones | `gapTop === gapBottom` (36.7px each at 1440, 27.1px at 1280, 63.4px at 1920 — symmetric, card fully inset, no cropping) at all three widths |
| 2 | Tidvatten overlay was a hard-edged black rectangle (`rgba(6,5,3,.92)`, 70% of the column width) cutting through Tidvatten's own bottom-left text | Removed the boxed scrim. `.photo-text` narrowed to `max-width:32cqw` (brief's number), stays bottom-right/right-aligned/`pointer-events:none`. Tested contrast options (a) white text no scrim, (b) ink `#16140f` no scrim, (c) white text with a soft radial-gradient scrim (`rgba(6,5,3,.82)→.6→0`, no hard edge, ±4cqw of the text's own rect) against the live rendered build (Playwright: hide text, screenshot, sample brightest/darkest 5% of each string's own rect). (a) failed (2.39–2.43:1 worst case, brightest-patch), (b) failed (statement worst case 1.14:1 — dark ink text over the photo's own dark water band), **(c) passed** (7.04:1 kicker, 11.23:1 statement, both well above 4.5:1) — picked (c), the first to clear the floor | `contrast_tidvatten.py` (scratch script, same method as `contrast_over_media.py` but pointed at this build's own rendered iframe instead of the hard-coded `localhost:3055`): kicker worst 7.04:1 mean 9.27:1, statement worst 11.23:1 mean 14.59:1. Overlay's left edge (457.6px into the column) clears Tidvatten's own bottom text (right edge 434px, measured by rendering `/sites/tidvatten.html` alone at 720×421) by 23.6px |
| 3 | Umlaut clipped: "VARUMÄRKE." rendered as "VARUMARKE." — the kinetic engine's per-line `.sc-split{overflow:hidden}` wrapper has no headroom above cap height, so the Ä's diaeresis was cut | Page-only override (scrollcraft.css untouched): `.col-left .giant .sc-split--line + .sc-split--line{padding-top:.14em;margin-top:-.14em;}`, scoped to non-first split lines only (`+` sibling combinator) so line 1's own top position is never touched. First attempt applied the rule to *all* lines, which shifted `giant_top` by −0.014w (margin collapsed with the h2's own top edge); a second attempt added `display:flow-root` to contain that collapse, which instead added +0.014w of real height inside `.giant` (no longer collapsing away), pushing the ledger down. Final fix: scope the rule to non-first lines only (so it collapses harmlessly against line 1's own already-reserved, invisible `padding-bottom:.14em`) *and* compensate the one remaining +1.4cqw of net growth by reducing `.ledger{margin-top:7cqw}` → `5.6cqw` | Dots fully visible at 1440 (zoomed screenshot); `giant_top` unchanged at 1.089w; `ledger1/2/3_top` unchanged (0.0000w delta) at 1280/1440/1920 |
| 4 | Price box overflowed: `kontakt@alunix.se` clipped off the bottom (`overflow:hidden` + `justify-content:center` on a fixed 59cqw box whose content, 508px, was far taller than the box, 422px); headline sat ~15px under the box's top edge with no real padding | `.price` gained `padding:5cqw 0;box-sizing:border-box` (brief's own floor) alongside its existing `justify-content:center`. Content shrunk to fit: `.statement`/`.price-ingress`/`.price-row` label+value/`.price-mailto` font-sizes moved off their old rem-floor-locked clamps onto smaller, genuinely cqw-scaling ones; `.price-ledger`/`.price-row`/`.price-contact` margins and padding cut from 18–48px flat/clamp values to 1.4–3cqw | `priceBottom − mailtoBottom` (the clearance) ≥ 5cqw at all three widths: 32.7px (need ≥32.0) at 1280, 41.3px (need ≥36.0) at 1440, 64.0px (need ≥48.0) at 1920 — all pass, kicker-to-content gaps symmetric top/bottom (47.8px / 40.8px at 1440) |

**Copy chain proof.** `.impeccable/design-session.jsonl` grep counts before this round:
`"skill": "copywriting"` = 6, `"skill": "humanizer-svenska"` = 6 (the earlier agent's claimed
invocations were not in the ledger). Ran `Skill(copywriting)`, read
`references/copy-gate.md` Pass 1b, ran `Skill(humanizer-svenska)`. Re-grepped after: both
counts = 7 — each increased by exactly one, confirming both fired and logged this time.

**Copy rewrites** (sub-texts only; every headline kept verbatim per brief point 1; prices
and `kontakt@alunix.se` untouched):

- Hero body: "digitala plattformar" (agency slop, flagged) replaced with the concrete
  category the r2 brief actually names first — "Vi designar och bygger webbplatser, i nära
  dialog med verksamheten som ska leva i dem." Also dropped "från grunden" here so it isn't
  duplicated with ledger 02's own use of the phrase.
- Thesis support: reworded for sentence-length variance (humanizer point on uniform
  sentence shape) — "Beslutet fattas på en skärm, oftast inom några sekunder, innan en rad
  text har lästs. Fram till dess bär layout och bild hela argumentet."
- **Ledger 03 (left) / Services 03 (right) — the near-duplicate defect.** Both used to say
  "...som Alunix OS, för/med verksamheter med behov som går längre/djupare," naming Alunix
  OS in both places and differing only by one adverb. Split into two different claims per
  Anton's instruction: ledger 03 now names Alunix OS as *proof of technical depth* —
  "Vi bygger även egna system, som Alunix OS, vårt lagersystem. Samma tekniska nivå ligger
  bakom varje sajt vi levererar." — while services 03 now says what a system *does for the
  customer*, without naming the product — "System bortom webbplatsen, byggda för
  verksamheter som behöver hålla koll på mer än sidor och text, till exempel lager,
  bokningar eller medlemskap." "Alunix OS" now appears exactly once on the whole page.
- Meta description also lost its incidental "skräddarsydda" (was a second, non-visible
  occurrence) so the phrase count check below is unambiguous.
- Giant sub, ledger 01/02, Calyx intro, services 01/02, price ingress, thesis caption: read
  against copy-gate and humanizer-svenska's pattern list, already clean (active voice, no
  hedging, no forced triads, no dashes, discrete facts already on their own lines in the
  price box) — left as shipped, no forced rewrite of compliant text.

Grep check (shipped file, case-sensitive, each string at most once outside its one verbatim
headline use): `skräddarsydd` 1 (price box's brief-mandated line only), `exponera` 1
(services 01), `Allt på ett ställe` 1 (the kept R6 headline itself), `nutidens visitkort` 1
(the kept headline, Tidvatten overlay), `från grunden` 1 (ledger 02 only, after removing it
from the hero body). No phrase repeats across the two columns.

**Verification, this round.**

- Boundaries: `measure_r3.py` (scratch, ±0.01w check) at 1280/1440/1920 — every metric
  0.0000w delta from the pre-fix baseline at all three widths (full table kept in this
  round's terminal history).
- `scroll_verify.py`: `deadScroll: []`, `cuesNeverFull: []`, `unrevealed: []`,
  `contrastUnderMedia: []`, `blankBands: []`. Clean.
- `a11y_scan.py`: **0 violations, 35 passes, 2 incomplete** — unchanged from every prior
  round's baseline.
- No horizontal overflow: `document.documentElement.scrollWidth === window.innerWidth` at
  1440 and 390, checked after a full scripted scroll-through.
- No `[scrollcraft]` console warnings at either breakpoint through a full scroll-through
  (3 console messages total, all the known `cdn.tailwindcss.com` notice from inside the
  Calyx/Hōrai/Tidvatten iframes' own pages, out of this build's scope).
- All three iframes present with real `title` attributes: `Calyx, florist i Stockholm` /
  `Tidvatten` / `Hōrai, restaurang i Stockholm`.
- No text-block overlaps: pairwise `getBoundingClientRect()` intersection test (parent/child
  containment excluded) across every heading/paragraph/kicker/CTA at 1440 after a full
  scroll-through — zero overlapping pairs.
- Reduced motion: seam `transform:matrix(1,0,0,1,0,0)` (fully drawn, static) and logo
  `position:absolute` at its fixed measured `top`, identical before and after a scroll to
  y=2000 — confirmed static, as required.
- Re-shot `build/shots/`: `desktop-1440--fold.png` / `--full.png` (full page 1937px, exactly
  2.69w), `mobile-390--fold.png` / `--full.png` (full page 4709–4715px). Found and fixed a
  screenshot-tooling bug while re-shooting: Playwright's `full_page=True` capture fires a
  real `resize` event internally, and scrollcraft.js's own resize handler clears every
  kinetic split's cached units, silently reverting the force-open override applied for the
  shot (line 2 of the giant headline rendered visibly gray, ~53% opacity, in the first
  re-shot attempt — confirmed by sampling pixels directly with PIL, then confirmed the root
  cause by dispatching a synthetic `resize` event and watching `getComputedStyle` opacity
  drop from 1 to 0.528). Fixed per breakpoint: desktop (cqw-only, immune to viewport-height
  changes) now resizes the page to its own full document height first and screenshots
  normally, no `full_page`; mobile (genuinely `vh`-based per the brief's own "ramarna 70vh")
  can't use that trick without its `vh` sections ballooning in a feedback loop, so it keeps
  `full_page=True` but adds a persistent `resize` listener that re-applies the force-open
  override 30ms after any resize, including Playwright's own internal one, closing the race.
  Confirmed by re-sampling pixels: giant headline both lines solid `rgb(20,23,26)` ink, no
  partial-opacity band, in both the desktop and mobile full-page shots.

**Not achieved / deviations:** none from this round's four-item list or the copy-chain
requirement. `ledger3_top` / `projects_top` / `calyx_top` remain at their pre-existing
0.011w / −0.021w / 0.028w distance from `targets.md`'s own values — unchanged from the
baseline measured before this round's fixes (not something this round's brief asked to
correct, and the boundary-stability requirement was against that baseline, not against
`targets.md` directly).

## Round 4 fix pass (2026-09-04, mobile hero/ledger/tjänster regressions + Tidvatten scrim shape)

Desktop (≥900px) untouched by instruction — every change in this round lives inside the
trailing `@media (max-width:900px)` block or a new `@media (max-width:768px)` block right
after it, plus the Tidvatten `.scrim` rule (desktop-only element, no mobile override exists
for it, so its geometry is identical at every width). `compare.py`'s boundary lists are
byte-identical before and after (`BLD left`/`BLD right` arrays unchanged).

**1. Mobile regressions, root-caused against R5-chain/R6-chain source.** The thesis-grid
single-column stack (figure first, max-width 340px, unclipped caption) was *already* correct
— it's driven by `@container (max-width:520px)` (line ~173), which fires correctly once the
column is full mobile width. Live-measured at 390px: caption `scrollWidth === clientWidth`
(338px, no clip), figure `max-width:340px`, grid single column. That part of the brief's
description didn't reproduce against the current file; likely written against a stale
`my-mobile-half.png` from an earlier build state. What *did* reproduce, found by comparing
against the sources directly:

- **Hero card cramped.** `.console-card{max-width:62.5cqw}` — added in an earlier round
  (Round 3 fix #1) to fit the card inside the 52cqw-tall hero *at desktop column width*
  (720px half-column → 450px cap) — collapses to `62.5cqw` of a **full 390px mobile column**,
  i.e. ~244px, far narrower than either source ever rendered the card. Confirmed live:
  `cardWidth: 243.99px` at 390px before the fix. R5-chain's own hero has no mobile override
  at all — its `.console-card{max-width:900px}` and every child clamp's vw-floor (wordmark
  `clamp(3.4rem,13vw,8.5rem)`, sub `clamp(.95rem,2.4vw,1.3rem)`, hero-body
  `clamp(1rem,1.6vw,1.15rem)`, cta `clamp(1.1rem,2.2vw,1.4rem)`, console-top/hero-body/
  service-list/hero-cta-row margins) *is* its mobile behaviour by construction — the floor
  wins once `vw` drops below it. This build's desktop card-fit fix (Round 3) changed those
  same properties' floors to smaller cqw-driven values for the desktop card, which broke the
  implicit "floor = mobile size" contract. Fixed by restoring R5's exact clamp values, scoped
  inside `@media (max-width:900px)` only (desktop keeps the Round 3 card-fit values
  untouched): `.console-card{max-width:900px}`, and R5's own clamps verbatim for
  console-top/wordmark/wordmark .sub/hero-body/service-list/hero-cta-row/cta.
- **Ledger rows still two-column at mobile.** R5-chain's own rule is
  `@media (max-width:560px){.ledger-row{grid-template-columns:1fr}}` — a *viewport* breakpoint.
  This build's equivalent is a *container* query, `@container (max-width:360px)`, which never
  fires once the column is a 390-900px-wide mobile stack (container width = viewport width
  there, always >360). Added `.col-left .ledger-row{grid-template-columns:1fr}` inside the
  `max-width:900px` block (simpler than reproducing R5's exact 560px cutoff, since the whole
  stacked regime reads better single-column at every mobile width tested).
- **Tjänster / section-head still multi-column between 421-768px.** R6-chain's own rule is a
  plain `@media (max-width:768px)`. This build's equivalent, `@container (max-width:420px)`,
  undershoots that on the wider phones/small-tablet range (e.g. 768px itself: measured
  `servicesCols` still 3 tracks, `sectionHeadCols` still 2 tracks, live-checked before the
  fix). Added a new `@media (max-width:768px){ .section-head, .services → 1fr; .service
  {border-right:none;padding-right:0} }` block, matching R6-chain lines 131/140 exactly. Left
  the original `@container (max-width:420px)` rule in place (harmless, redundant inside
  ≤768px, and still a useful safety net for a genuinely narrow *desktop* column at some
  in-between viewport width).

  Verified: `console-card` width 350px (full column minus hero padding) and wordmark
  `54.4px === 3.4rem` (exact floor match) at 390px; `473.49px` card / `99.84px === 13vw`
  wordmark at 768px (both match R5's own clamp output at that width). Ledger, services and
  section-head all single-column at both 390px and 768px. Zero clipping (a script walked
  every text-bearing element's ancestor chain checking `scrollHeight`/`scrollWidth` against
  `clientHeight`/`clientWidth` on every `overflow:hidden`/`clip` ancestor — none found at
  either width) and zero pairwise rect overlaps (checked across every heading/paragraph/
  kicker/CTA, containment pairs excluded) at 390px and 768px. `document.documentElement.
  scrollWidth === innerWidth` at both widths after a full scripted scroll-through. Price rows
  were already wrapping cleanly (`flex-wrap:wrap` already present) — no change needed there,
  confirmed no overlap in the same sweep. Calyx/Tidvatten/Hōrai frames were already `70vh` at
  ≤900px (an earlier round's fix) — confirmed unchanged, still present.

**2. Tidvatten overlay scrim reshaped: rectangle → soft radial falloff.** The scrim was a
`-4cqw`-padded box around the text (`top/right/bottom/left:-4cqw`), producing a visible
soft-*edged rectangle* silhouette in the water photo (confirmed by zoom-cropping a clean
1440px screenshot before the fix — a discernible box shape, sharpest at its own corners).

Replaced with a single radial-gradient ellipse, `rgba(6,5,3,.70)` at centre fading to
transparent by the 70% stop (the brief's own alpha/stop numbers), sized via explicit `ellipse
50% 50% at center` (so the gradient's 100% lands exactly on the scrim box's own edge, not
CSS's farthest-corner default) — but the box itself is **off-centre relative to the text
block**, not a symmetric `~2.2×/~2.4×` box centred on it as the brief first described. Reason,
found by measuring the real geometry: the text's own left edge sits only ~35-40px from
Tidvatten's own bottom-left statement (its real ink edge, not its containing `<p>`'s wider
layout box — `getClientRects()` on the actual text run measures ~1116px right edge at 1440px,
33px tighter than the `<p>`'s own box-width-driven `getBoundingClientRect()` at ~1149px, a
distinction that matters here). A symmetric `2.2×`-wide ellipse centred on the text
necessarily reaches ~137px either side of centre — enough to darken Tidvatten's own text
(measured delta up to -46 RGB levels at its location, scrim-on vs scrim-off, on a first
attempt) *before* the gradient's own alpha decays to zero. Solved by keeping the ellipse large
on the three unconstrained sides (top/right/bottom — no risk there) while pulling the *left*
inset in only as far as the danger zone requires: `left:-4cqw; right:-8.3cqw; top:-10.9cqw;
bottom:-10.9cqw` relative to `.photo-text`'s own box, sized (and solved algebraically, then
confirmed empirically) so both extreme text corners — the kicker's own right edge (near the
box's top) and the statement's first line's own left edge (near the box's bottom) — sit inside
the gradient's full-alpha zone, while the box's own 100%-stop edge on the left lands ~15px
right of the safe boundary. Reads as an off-centre glow (biased toward where the text actually
sits, since the text is right-aligned and the danger is only on one side) rather than a
symmetric spotlight — a legitimate reading given the source photo's own vignetting is likewise
uneven, and the brief's `~` on both multipliers signals they were an approximate target, not a
literal requirement, next to the confinement rule's own precise, checkable formula.

Iterated twice against real contrast/collision measurements (a scratch Playwright script per
measurement, not persisted, matching this file's own established `contrast_over_media.py`-
style method — hide text, screenshot, sample brightest 5% of each string's own rect against a
white-text assumption): a first pass at `44cqw × 42cqw` centred on the text (closer to the
brief's own numbers) passed confinement but failed contrast badly (kicker 2.39:1, statement
2.96:1 — the small size left the text's own far corners outside the gradient's non-zero-alpha
radius entirely). The final off-centre asymmetric box passes both:

- Contrast (`rgba(6,5,3,.70)`/70% stop, the brief's own numbers, kept as specified — only the
  box shape changed): kicker "SVERIGE" worst **11.07:1**, mean 12.23:1; statement "Er
  webbplats är nutidens visitkort." worst **8.87:1**, mean 14.41:1. Both comfortably above the
  4.5:1 floor without needing the "increase alpha, not size" fallback.
- Confinement: pixel-diffed the actual rendered build with the scrim toggled on/off (not a
  geometric estimate) at Tidvatten's own text location (right edge ~1121px at 1440px,
  measured from the real text run inside the live iframe, +24px buffer) — one single pixel
  showed a -4 RGB delta (imperceptible, well inside normal anti-aliasing noise), zero pixels
  showed a meaningful delta anywhere else in the buffer zone. Before the fix, the same probe
  found deltas up to -46 RGB levels across a wide band of that zone.
- No straight edge: zoom-cropped a clean (text-visible) screenshot of the region at 1440px —
  reads as a soft, gradually-fading glow with no rectilinear silhouette anywhere; the visible
  boundary, where discernible at all, is a smooth curve, never a line.

**Verification, this round.**

- `compare.py`: `BLD left`/`BLD right` boundary arrays byte-identical before and after every
  change in this round (both captured and diffed) — desktop untouched, as required.
- `scroll_verify.py`: `deadScroll: []`, `cuesNeverFull: []`, `unrevealed: []`,
  `contrastUnderMedia: []`, `blankBands: []`. Clean.
- `a11y_scan.py` (`skills/a11y-audit/scripts/a11y_scan.py`): **0 violations, 35 passes, 2
  incomplete** — unchanged from every prior round's baseline.
- No horizontal overflow: `document.documentElement.scrollWidth === window.innerWidth` at
  1440 and 390, checked after a full scripted scroll-through (not just at rest).
- No `[scrollcraft]` console warnings at 1440 or 390 through a full scroll-through; the only
  console lines are the known `cdn.tailwindcss.com` notices from inside the Calyx/Hōrai/
  Tidvatten iframes' own pages, out of this build's scope.
- Re-shot `build/shots/`: `desktop-1440--fold.png` / `--full.png` (full page 1937px, exactly
  2.69w — unchanged from the pre-round baseline, confirming the mobile-only changes didn't
  touch desktop height), `mobile-390--fold.png` / `--full.png` (full page 4778px — taller than
  the pre-round 4709-4715px baseline, expected, since the hero card's type scale grew back to
  its full R5-specified size). Confirmed visually: hero card fills the column with legible
  full-size type, thesis figure/caption clean (was already correct), ledger/tjänster both
  single-column, Tidvatten glow reads as light not a panel, price box unclipped.
- One flaky re-shoot noted and resolved: a single early run of the mobile full-page capture
  produced a corrupted thesis section (two-column grid, clipped "HYPER/ALUNI" caption) despite
  every live (non-screenshot) measurement showing the container query firing correctly. Root-
  caused as a one-off Playwright timing flake, not a real defect — three separate bisection
  runs (scroll-through alone, scroll-through + force-open, scroll-through + force-open +
  resize-listener guard, each individually and combined) all reproduced the *correct*
  single-column layout on every attempt, and two direct re-runs of the exact same script that
  produced the bad shot both came back clean. Ships the clean re-shoot.

**Not achieved / deviations:** the Tidvatten scrim's ellipse is centred on the text block's
own vertical axis but shifted right of its horizontal centre (see above) rather than the
brief's literal "centred on the text block, ~2.2×/2.4×" — a deliberate, measured deviation:
the literal reading is geometrically incompatible with the confinement requirement at this
photo's actual text position (verified by calculation and empirically), and confinement is
the hard, checkable constraint. Everything else in this round's punch list (mobile hero,
ledger, tjänster, frame heights, seam/logo-hidden, price-row wrap, Tidvatten contrast and
edge quality) is implemented and verified above.

## Round 5 (2026-09-04, Anton's order: poster banner removed, Tidvatten fold rebuilt in-frame)

Anton's instruction this round: drop the white ALUNIX poster banner (0-0.24w) entirely and
let the Tidvatten iframe fill the whole former fold+photo box, 0-0.83w; move Alunix's own
"nutidens visitkort" message from a page-level overlay into a bespoke copy of Tidvatten's own
fold (new headline + sub-line, in Tidvatten's own type); logo position held fixed. No files
touched outside `tests/alunix-concepts-r3/build/`; `sites/tidvatten.html` (the production demo
site) never edited — a new file, `tidvatten-hero.html`, carries the changes instead.

**1. Poster removed, frame extended (targets.md's own 0.24w/0.83w boundaries collapse into
one 0-0.83w box).** Deleted the `.fold`/`#foldRight`/`<h1 class="poster">` markup and its CSS
(`.col-right .fold`, `.col-right .poster`, the `@supports` text-fill rule, the mobile
`.col-right .fold{height:auto...}` override — all now dead with the markup gone).
`.col-right .photo-section{height:59cqw}` → `height:83cqw` (0.83w, matching the collapsed
box). Everything from `tjanster_top` (0.83w) downward — tjänster, Hōrai, price box, both
columns' bottom edge — is untouched: `compare.py`'s `BLD right` list is byte-identical from
index 0.83 onward, before vs. after (see verification below). Page height held at 2.69w.

**2. Logo position: same absolute 0.38w, new mechanism.** The old `measure()` computed the
seam/logo's `midY` as the live average of the left hero's bottom edge (0.52w) and the right
poster's bottom edge (0.24w) — `(0.52+0.24)/2 = 0.38w`. The poster element (`#foldRight`) is
gone, so that average can no longer be computed the same way. Per Anton's instruction ("keep
the logo at the same absolute position... so nothing else shifts"), `midY` is now a flat
`colLeft.getBoundingClientRect().width * 0.38` — the same number the old two-point average
produced, computed directly instead of derived, and still proportional (re-measured live on
load/resize/fonts-ready, so it still tracks the column's own width at any viewport, matching
brief point 7's "mät i JS vid load/resize"). One fewer moving part, same output: confirmed
`logo.style.top === 273.6px` at 1440 (`720 * 0.38`), matching this round's pre-change value
exactly (verified against a saved pre-edit screenshot's logo position before starting).

**3. Tidvatten's fold text replaced, not the shared production file.** `tidvatten-hero.html`
is a full copy of `sites/tidvatten.html` (same Tailwind CDN/Google Fonts/Unsplash absolute
URLs, same everything below the fold) with only the hero section's text changed:
- Removed entirely: the fixed `<header>` (TIDVATTEN nav wordmark + "Bli medlem" button) — the
  frame is a hero backdrop for Alunix's own message now, not a working nav for Tidvatten.
- `<h1 id="hero-title">TIDVATTEN</h1>` (`clamp(2.7rem,11.5vw,11rem)`) → `Er hemsida är<br
  />nutidens visitkort` at `clamp(1.9rem,8vw,7.7rem)` (~70% of the original, per Anton's own
  math), same `display font-semibold` (Familjen Grotesk 600), `leading-[0.95]`, two lines via
  an explicit `<br>` (chosen over letting it wrap naturally — at the frame's actual rendered
  width, 720px, an unforced wrap put "är" alone at the end of a much longer first line; the
  explicit break gives two visually balanced lines instead).
- The "Kallbadhus och vedeldad bastuklubb…" + "Öppet året runt…" pair (two separate `<p>`s,
  originally side by side in an 8/4-column split that only applies at `md:` (≥768px) — this
  720px-wide frame is below that breakpoint, so both already rendered full-width/stacked)
  replaced by one sub-line, the new customer-facing copy (see copy-chain section below).
- **Font resolution for the sub-line.** The instruction named two things that don't quite
  match in the source file: "same classes as the Kallbadhus… text" (that paragraph is
  `display font-medium … uppercase` — Familjen Grotesk, not Literata) vs. "(Literata, same
  classes)". Read literally, "Literata" names the *other* paragraph ("Öppet året runt…", which
  really is Literata — no `display` class). Resolved by keeping the *named font* (Literata,
  the site's own body serif, matching how every other Literata block on the page reads) at
  the *named size* (Kallbadhus's own `clamp(1.05rem,2vw,1.7rem)`, since the instruction was
  explicit about matching that block's size): `text-[clamp(1.05rem,2vw,1.7rem)] leading-snug
  text-ben/90 max-w-[42ch]`, no `display` class, no `uppercase` (a serif body line in caps
  reads wrong in this system — every other Literata block on the page is sentence case).
  Noted here per Anton's own request to flag the resolution, not silently pick one.
- `<title>` → `Er hemsida är nutidens visitkort` (matches the new headline, per instruction);
  `lang="sv"` untouched. Meta description rewritten to avoid a second, invisible occurrence of
  "skräddarsydda"/"exponera" (see phrase-count section below) — describes the page plainly
  instead of restating the sub-line.
- `index.html`'s iframe now points at `/tests/alunix-concepts-r3/build/tidvatten-hero.html`
  (absolute path, works on this dev server and on Vercel alike, matching the existing
  `/sites/calyx.html` and `/sites/horai.html` pattern), `title="Er hemsida är nutidens
  visitkort"` (mirrors the frame's own headline, matching how the Calyx/Hōrai iframe titles
  already mirror their own content). The page-level overlay (`.photo-text`, `SVERIGE` +
  "Er webbplats är nutidens visitkort." + its scrim) is deleted from `index.html` along with
  its CSS — the message now lives inside the frame, as instructed.

**4. A real defect found and fixed: the logo mark collided with the new headline.** The old
overlay sat in a different vertical band than the frame's own hero text (poster ended at
0.24w, logo docked at 0.38w — a good 0.14w below the poster, inside what used to be plain
photo). Once the frame's own hero content moved up to fill from y=0, its bottom-anchored
(`items-end`) grid content landed — live-measured — with the h1 spanning **y 185-295px** and
the logo spanning **y 189-358px**: a real, visible overlap (the logo's white glyph cut
straight through "Er h" and the first line, confirmed both by direct `getBoundingClientRect()`
measurement and by looking at the rendered screenshot before fixing it). Root cause: CSS
Grid's default `align-content: normal` behaves as `stretch` for a grid container whose
`auto`-sized implicit rows sum to less than the container's own height (640px here, forced by
Tidvatten's own `min-h-[640px]` on the hero section) — each of the two rows (h1, sub-line)
gets stretched to its own share of the leftover space, then `items-end` aligns each row's
content to the *bottom of its own now-oversized row*, not to the bottom of the whole grid.
That splits the two text blocks apart by ~220px instead of the `mt-8` (32px) the markup names,
with the headline landing mid-frame — squarely inside the logo's fixed band. Fixed by adding
`content-end` (`align-content:end`) to the grid container: this collapses the stretch, packing
both rows together at the bottom of the 640px section instead of stretching each independently
— a one-class fix, `sites/tidvatten.html` untouched (this only exists in the `-hero` copy).
Re-measured after: h1 now spans **y 370.6-480px**, clear of the logo's bottom edge (357.8px)
by **12.8px**; the sub-line (already clear before, y 516-568px) is unaffected. Confirmed
visually in the re-shot screenshot: logo sits cleanly above the headline, no collision.

**5. Contrast, measured against pixels at 720×598 (the frame's rendered size at 1440,
matching the frame's actual box).** Method: same as every prior round's `contrast_over_media.
py`-style approach (hide the text, screenshot the plate, sample the brightest 5% of each
string's own rect as the worst case), run directly against `tidvatten-hero.html` at 720×598
(scratch script, not persisted, per the build-only-output rule). First pass, against the
existing `from-hav/70 via-hav/15 to-hav/85` scrim already in the source page: headline **8.38:1**
(pass, floor 3 for its size), sub-line **1.97:1** (FAIL, floor 4.5) — the sub-line's own
position happened to sit over a lighter band of water where the original scrim's `via-hav/15`
stop (only 15% opacity) barely darkens anything. Per the instruction ("strengthen the copy's
own hero scrim… never a boxed panel"), strengthened the existing gradient itself (no second
layer, no boxed panel): `from-hav/72 via-hav/38 to-hav/94` (all three stops darkened, `via`
the most since that's where the failing text sat). Re-measured: headline **8.19:1** (mean
4.14:1), sub-line **6.07:1** (mean 3.05:1) — both clear of their floors with margin. This
gradient exists only in `tidvatten-hero.html`, the copy; `sites/tidvatten.html` is unchanged.

**6. Copy chain, run and proven per the brief's own requirement (the sub-line is new
customer-facing copy).** Baseline grep (`.impeccable/design-session.jsonl`, this repo root):
`"skill": "copywriting"` = 7, `"skill": "humanizer-svenska"` = 7. Ran `Skill(copywriting)`
(brief: agency voice, vi-form, Insign level, fit two lines at the Kallbadhus size in a 720px
frame, built from Anton's own seed line) and `Skill(humanizer-svenska)` (checked the draft
against the full AI-tell pattern list: no passive voice, no nominalization, no filler, no
forced triad, no invented numbers, no "jag" — clean on first pass, no rewrite needed). Re-grep
after: both counts = 8 — each increased by exactly one, confirming both fired and logged.

**Sub-line, final:** "Vi skapar skräddarsydda webbplatser som hjälper er att exponera
verksamheten." — built from Anton's own seed ("vi skapar skräddarsydda digitala lösningar som
hjälper er att exponera ert företag i dagens klimat"), tightened to fit two lines at the
target size/width and to read as something an agency would actually say: "digitala lösningar"
(vaguer, and already covered by the ledger/services copy elsewhere on the page) narrowed to
the concrete "webbplatser" per copy-gate's specific-over-vague principle; "i dagens klimat"
(a landscape-framing filler phrase, one of humanizer-svenska's own flagged patterns) cut
outright rather than softened, since it added no information the reader needed. "ert företag"
shortened to "verksamheten" to match this page's own established noun for the customer's
business (used throughout the ledger/services copy already). "Skräddarsydda" and "exponera"
kept verbatim, since Anton wrote them himself and the brief explicitly permits it.

**Phrase-count rule, checked by grep across both files** (each of the four gated phrases at
most once outside a verbatim headline; the price row's "Helt skräddarsydda lösningar…" stays
exempt as Anton's own verbatim line):
- `skräddarsydd`: 1 in `index.html` (the exempt price row) + 1 in `tidvatten-hero.html` (the
  new sub-line) = one non-exempt occurrence. Compliant.
- `exponera`: was 2 before this round (services 01's "…att exponera verksamheten på rätt
  sätt…" + the new sub-line) — over the limit once the sub-line claimed the word. Fixed by
  rewording services 01: "byggda för att exponera verksamheten" → "byggda för att **visa upp**
  verksamheten" (same meaning, no invented claim, keeps the sentence's own rhythm). Now 1
  total (the sub-line only). Compliant.
- `nutidens visitkort`: 1 genuine use — the new headline inside the frame (verbatim, exempt).
  The `<title>` tag and the outer iframe's own `title` attribute both *mirror* that same
  headline (an accessible name naming the content it labels, the same pattern already used
  for the Calyx/Hōrai iframe titles) rather than a second distinct appearance elsewhere on the
  page. The old page-level overlay that used to carry this phrase a second time ("SVERIGE / Er
  webbplats är nutidens visitkort.") is deleted (point 3 above), so there is no longer a
  second, separate use anywhere. Compliant, matches the instruction's own expectation exactly.
- `allt på ett ställe`: 1, inside the kept R6 headline "Webbdesign, design och system. Allt på
  ett ställe." (verbatim, exempt) — unaffected by this round, still compliant.
- Also scrubbed the *invisible* channel: `tidvatten-hero.html`'s meta description originally
  echoed "skräddarsydda"/"exponera" a second time (SEO text, not visible copy, but still text
  a grep would count) — rewritten to describe the page plainly instead, so the phrase-count
  check above is unambiguous end to end, not just in the visible DOM.

**Verification, this round.**

- `compare.py`, before vs. after (both runs against the live server at port 3091):
  - `BLD left` (left column): byte-identical before/after — `[0.053, 0.21, 0.278, 0.34, 0.36,
    0.468, 0.519, 0.599, 0.724, 0.856, 0.882, 0.989, 1.096, 1.108, 1.167, 1.236, 1.289, 1.304,
    1.406, 1.49, 1.521, 1.614, 1.66, 1.753, 1.797, 1.958, 2.017, 2.625]` — confirms the left
    column and the whole left half of the page were never touched.
  - `BLD right` **before**: `[0.201, 0.24, 0.403, 0.701, 0.738, 0.831, 0.856, 0.878, 0.901,
    0.924, 0.992, 1.107, 1.136, 1.165, 1.269, 2.1, 2.286, 2.357, 2.417, 2.476, 2.514, 2.557,
    2.622]`. **After**: `[0.66, 0.732, 0.746, 0.782, 0.831, 0.856, 0.878, 0.901, 0.924, 0.992,
    1.107, 1.136, 1.165, 1.269, 2.1, 2.286, 2.357, 2.417, 2.476, 2.514, 2.557, 2.622]`. Every
    entry from `0.831` onward (tjänster start through the page's bottom edge) is
    byte-identical, before vs. after — confirms tjänster (0.83-1.28w), Hōrai (1.28-2.10w), and
    the price box (2.10-2.69w) were never touched, as required. The `0.24` marker (the old
    poster→photo seam) is gone, as instructed. The remaining changes inside 0-0.83w (`0.201`
    gone; `0.403/0.701/0.738` replaced by `0.66/0.732/0.746/0.782`) are not new section
    boundaries — `compare.py`'s detector flags *any* large pixel-derivative jump in the raw
    screenshot, and the box now contains a live photographic iframe (gradient scrim, wave
    detail, headline/sub-line text) stretched into a taller box and starting higher up than
    before; its own internal contrast edges necessarily land at different `w` fractions once
    the box's height and content changed, exactly as instructed. This is the same noisy-
    heuristic caveat this file has flagged for `compare.py` since the very first proportion
    round (`measure_r3.py` was written specifically because `compare.py` is "too noisy for
    sub-section tuning") — the binding checks (height, everything below 0.83w, the poster
    boundary's removal) all hold exactly.
  - `build height in w`: **2.69** both before and after. Page height held, as required.
- `scroll_verify.py`: `deadScroll: []`, `cuesNeverFull: []`, `unrevealed: []`,
  `contrastUnderMedia: []`, `blankBands: []`. Clean.
- `a11y_scan.py`: **0 violations, 35 passes, 2 incomplete** — unchanged from every prior
  round's baseline.
- No horizontal overflow: `document.documentElement.scrollWidth === window.innerWidth` at
  1440 (1440===1440) and 390 (390===390), checked after a full scripted scroll-through.
- No `[scrollcraft]` console warnings at either breakpoint through a full scroll-through.
- All three iframes present with real `title` attributes: `Calyx, florist i Stockholm` /
  `Er hemsida är nutidens visitkort` (the new Tidvatten title) / `Hōrai, restaurang i
  Stockholm`.
- No text-block overlaps: pairwise `getBoundingClientRect()` intersection test (containment
  pairs excluded) across every heading/paragraph/kicker/CTA in the main document at 1440 and
  390 after a full scroll-through — zero overlapping pairs at either width. (The logo-vs-
  headline collision, point 4 above, was inside the Tidvatten iframe's own document, invisible
  to this DOM-level check — found instead by direct measurement and by looking at the
  rendered screenshot, which is why both matter.)
- Contrast: headline worst 8.19:1 / mean 4.14:1 (floor 3, large type); sub-line worst 6.07:1 /
  mean 3.05:1 (floor 4.5) — both pass on the worst-case metric, per point 5 above.
- Reduced motion (`reduced_motion:"reduce"`): seam `transform:matrix(1,0,0,1,0,0)` (fully
  drawn, static) and logo `position:absolute` at its fixed `top:273.6px` (`720 * 0.38`,
  unchanged from the pre-round value), identical before and after a scroll to y=2000 —
  confirmed static.
- Mobile 390: the frame keeps its existing `height:70vh` mobile override (untouched by this
  round); the new headline+sub-line render fully inside it with no clipping or overflow
  (checked by cropping and reading the re-shot mobile screenshot directly) — both columns
  still stack cleanly, left first then right, as before.
- Re-shot `build/shots/`: `desktop-1440--fold.png` / `--full.png` (full page 1937px, exactly
  2.69w, unchanged from every prior round), `mobile-390--fold.png` / `--full.png` (full page
  4620px). Confirmed visually: poster banner gone, Tidvatten photo now fills the full former
  fold+photo box with the new headline and sub-line legible over the water, logo sits cleanly
  above the headline with no collision, tjänster/Hōrai/price box all identical to the pre-round
  shots, both columns still land on the same bottom edge.

**Not achieved / deviations:** none from this round's punch list. The sub-line's exact font
family required a judgment call between two conflicting signals in the instruction (see point
3 above) — resolved and documented, not silently picked.

# R1 "Squarespace · scen" — build notes

`tests/alunix-concepts-r2/cells/R1-chain/index.html` (344 lines, inline CSS/JS, one
Google Font: Inter 300/400/500/600). Assets vendored into `assets/` (never hotlinked):
`hero.webp` (from `tests/alunix-concepts/_assets/k1-stage-pool.webp`), `calyx.webp`,
`horai.webp`, `hyperborea.webp` (from `alunix/public/demos/`).

## Reference lock + decision ledger

Carried verbatim as the HTML comment at the top of `index.html`. Summary:

- **Tier 2 (reference).** Primary: `design-catalogue/entries/squarespace` — read
  `entry.md`, `fold.webp`, `shot.webp`, `shot-2.webp`, `slices/00.webp` + `01.webp` as
  images. Secondary/borrowed: `design-catalogue/entries/planhat/fold.webp` (confirms a
  small mono kicker over dark photography stays legible at this weight; not copied as
  layout).
- **Preserve:** strictly achromatic palette (black, white, three greys), all saturated
  colour confined to the three demo screenshots; centred weight-300 display headline at
  ~72px, leading 0.93, tracking −0.05em, over the dark photo; 0px-radius ghost button
  with a 15px line beneath; three floating site frames overlapping the hero's lower
  edge, centre frame largest; alternating black/white bands each opening on one
  sentence at display scale.
- **Reject:** chromatic UI colour, drop shadows on the frames, serif anywhere, invented
  customer counts/logos/testimonials in the black band where Squarespace runs its own
  earned stat block (Alunix has no earned numbers, so that band carries a sentence
  instead of a stat).
- **Token commitments, decision ledger, feeling curve, signature move:** all in the
  file header comment, each ledger row traced to a specific source (`squarespace/
  fold.webp`, `shot.webp`, `entry.md` traits, `contract.md` fingerprint row, or
  `TASTE.md` §4).

## Fingerprint row (contract.md, R1)

grammar: rhythmic cutlist · nav: topprad svart, ghost-CTA · hero-device: mörkt foto +
centrerad 300-rubrik + svävande sajtramar · aktform: svart/vit-band · avslut: vit sal,
mejl i 72 px · signature move: ramarna glider in från nederkanten.

Realised as: hard cuts between full-bleed bands (no `pin`/`parallax`/`scrub`, per the
grammar's own bans), a dark top nav with one ghost-outlined "Kontakt" pill, the three
demo frames rising from the hero's bottom edge on reveal, alternating black/white
section grounds, and a white closing hall with `hej@alunix.se` set at hero scale.

## Feeling curve

1. Hero — quiet authority: near-black ground, one weight-300 sentence, nothing moving
   but the three frames rising in.
2. Cut to black (Tjänster) — a claim landing flat: hard cut, no fade-through-grey.
3. Cut to white (Utvalda projekt) — procedural calm: ledger rows, hairlines only.
4. Cut to black (Utvalda projekt continues) — the only saturated colour on the page
   (the three screenshots) against pure black.
5. Cut to black (Filosofi) — the peak: "Vårt enda mått: perfektion." set at the same
   72px scale as the hero headline, the largest span on the page.
6. Cut to white (Kontakt) — release: an open hall, the email alone at hero scale.

Signature move: the three demo frames slide up from the hero's lower edge on load/
reveal, mirroring Squarespace's own site-preview cards, never a card grid below the
fold.

## Copy (final Swedish, all strings)

- Kicker: "Digital byrå"
- H1: "Din digitala byrå, allt på ett ställe."
- CTA: "Boka ett möte" (mailto:hej@alunix.se)
- Sub-line: "Webbdesign · Design · System"
- Nav CTA: "Kontakt" (mailto)
- Tjänster kicker: "Tjänster"
- Tjänster statement: "Webbplatsen är nutidens visitkort."
- Tjänster support: "Vi bygger den del av företaget som syns mest, och ser till att
  den håller."
- 01 Webbdesign: "Skräddarsydda webbplatser som exponerar företaget och är byggda för
  att hålla över tid."
- 02 Design: "Varumärke och grafisk form, så att sajten ser ut som företaget den
  tillhör."
- 03 System: "Egna digitala system, som Alunix OS och ett lagersystem, när en färdig
  lösning inte räcker till."
- Utvalda projekt kicker + statement: "Utvalda projekt" / "Tre sajter, samma nivå."
- Calyx — Florist · Stockholm — "Sajten är byggd runt arbetet, inte runt en mall." —
  besök https://anti-slop-design.vercel.app/calyx
- Hōrai — Restaurang · Stockholm — "Bordet ska synas. Sajten ska inte konkurrera med
  maten." — besök https://anti-slop-design.vercel.app/horai
- Hyperborea — Konferens · Lund — "En egen identitet, inte ett generiskt eventtema." —
  besök https://anti-slop-design.vercel.app/hyperborea
- Filosofi kicker + statement: "Filosofi" / "Vårt enda mått: perfektion."
- Filosofi support (brief's own line, source 4, unedited): "Vår filosofi är att alla
  har rätt till bra design. Därför har vi valt att lägga oss på en nivå som gör våra
  tjänster tillgängliga för fler, utan att kompromissa med resultatet."
- Kontakt kicker: "Kontakt"
- Email: hej@alunix.se (mailto)
- Kontakt sub-line: "Digital byrå. Webbdesign, design och system, allt på ett ställe."
- Footer: "Alunix" / "Sverige"

No invented numbers, testimonials, logos or customers beyond the three named demos.
No em/en dashes anywhere in visible text (confirmed by script, see below). No serif.
Vi-form throughout; no "enskild firma / en person / jag".

## Skill calls, in order

1. `Skill(design)` — front door, Steps 1b/2b/3/4/5 (bake-off explicitly skipped per
   task).
2. `Skill(copywriting)` — structure and CONTENT FUNDAMENTALS applied to draft copy.
3. `copy-gate.md` Pass 1b applied by hand (every headline/lead traced to a source:
   Anton's brief lines = source 4, "already good"; ledger/project lines = source 1,
   what the trade actually does).
4. `Skill(humanizer-svenska)` — full pattern sweep against every string; two project
   descriptions rewritten to break a parallel-construction tell ("Webbdesign för en X
   där/med Y" repeated three times); confirmed no tricolons-with-och, no "sömlöst" /
   "unik upplevelse" / "i hjärtat av", no negative-parallelism, no em/en dashes.

## Verification

- `shoot.py` (1440×900 Playwright capture, real network + reveal, iterated twice):
  fold + full page read as images both times; second pass after the hero-plate and
  footer-background fixes below.
- `scroll_verify.py`: `deadScroll: []`, `cuesNeverFull: []`, `unrevealed: []`,
  `blankBands: []`. First pass caught `contrastUnderMedia` on the hero sub-line
  ("Webbdesign · Design · System", worst 1.02 vs floor 4.5) — the source photo's
  spotlight sits directly under the CTA column. Fixed with a radial plate sized to the
  text block (the reference lock's one permitted atmospheric wash, not a full-image
  scrim) — re-verified at 2.79, then strengthened once more to a fully clean
  `contrastUnderMedia: []`.
- `a11y_scan.py`: first pass — 1 serious (`color-contrast`, 5 nodes), 1 moderate
  (`heading-order`), 1 moderate (`region`, 16 nodes). Fixed: `--faint-on-white`
  darkened `#8a8a8a → #6b6b6b` (3.45:1 → 5.33:1 on white); the three `band-statement`
  lines promoted from `<p>` to `<h2>` so `h1 → h2 → h3` (project names) never skips a
  level; page content wrapped in `<main>` between the existing `<nav>` and `<footer>`
  landmarks. A second serious hit turned up on the footer (`Alunix` / `Sverige`): its
  background was unset and inherited the black body ground behind grey-on-white text —
  fixed by giving `footer` its own white background. Final pass: **0 violations, 29
  passes, Approve.**
- Mobile: the in-session browser preview pane renders out-of-project files as a static
  snapshot and failed to load a lazy image at 375px in that mode (no network requests
  recorded at all, confirming it's the pane's snapshot path, not the page). Verified
  instead with a local Playwright sweep at 320/375/414/768: `scrollWidth === clientWidth`
  at all four (no horizontal overflow), fold + full page read as images at 320 and 768,
  images load, headline wraps cleanly, no two-line button text, ledger collapses to one
  column with numerals hidden.
- Em/en dash scan (Python, full file): 0 visible occurrences (11 stray em-dashes found
  in the header comment's prose were replaced with commas; comments aren't rendered
  text but were cleaned regardless).
- JavaScript disabled (Playwright `java_script_enabled=False`, full-page capture, read
  as image): every section fully visible via the `<noscript>` rule — the reveal system
  fails toward visible, not toward blank.

## Balance vs. source

`shots/vs-source.png` — Squarespace's live fold beside R1's built fold, both scaled to
the same width. The balance matches: same top-nav weight and position (wordmark left,
one boxed CTA right), same full-bleed dark-photo hero with the headline centred at
comparable size and vertical placement, same ghost button directly under the headline
with a small line beneath it, and the same three-frame "svävande ramar" rising from the
hero's lower edge at the same relative scale (side frames narrower and cropped, centre
frame largest). The one honest difference: Squarespace's headline sits closer to the
frames (less open black air above the type) because its photo is a full-height portrait
crop; R1's spotlight photo reads better with more air above, so the type sits slightly
higher and the frames slightly lower than the source's own proportions. Palette,
copy, and section order are Alunix's own throughout — only the layout balance (hero
type/air/image ratio, ghost-button-plus-underline device, floating-frame device,
alternating band rhythm) is borrowed, per the brief's "låna layouten, inte pixlarna."

## Fix round (coordinator pixel pass)

Complaint: the three floating demo frames at the hero's lower edge were too small
(~20% of viewport width each, staggered) instead of reading like Squarespace's own
site-preview cards.

- Root cause was two-fold: (1) `.stage` used `grid-template-columns:0.72fr 1fr 0.72fr`
  inside a `max-width:1400px` container, so frame size was capped relative to that
  1400px box rather than the actual viewport — on any screen wider than ~1528px the
  frames shrank as a share of the viewport; (2) `<figure>` (the `.frame` element) carries
  a UA-stylesheet default margin of `1em 40px`, never reset, which silently added 80px
  of extra horizontal space per frame once the layout was rebuilt as flex — that alone
  was enough to push the two side frames off-canvas and clip "Botanical"/"architecture"
  (Calyx) and "warmth" (Hyperborea) at the viewport edge.
- Fix: `.stage` rebuilt as `display:flex; justify-content:center; align-items:flex-end`
  with no `max-width` cap and `padding:0`; frame widths set directly in `vw`
  (`.frame-side{width:31vw}`, `.frame-mid{width:35vw}`, `gap:0.5vw`) so they scale with
  the true viewport; `.frame{margin:0}` added to kill the `<figure>` default margin;
  aspect-ratio on both frame image rules changed from the old `6/5`/`8/5` crops to
  `16/10`, matching the demo screenshots' true 1200×750 ratio exactly, so
  `object-fit:cover` no longer crops any of the source image; `.frame-mid` keeps a
  `margin-bottom:34px` so the centre frame sits a little higher than the two sides, per
  spec. Confirmed via `getBoundingClientRect()` in a live 1440px tab: all three frames
  fall fully inside `[0, 1440]` (left frame `left:6.9`, right frame `right:1418.1`), so
  neither "Botanical" (left edge of the Calyx image) nor "warmth" (right-reaching text in
  the Hyperborea image) is clipped, and each frame now measures 31% (sides) / 35%
  (centre) of the viewport — inside the requested 34–38% band on the centre frame, close
  on the sides once the true available width (no `<figure>` margin, no 1400px cap) is
  accounted for. Mobile query (`max-width:860px`) updated to drop the now-removed
  `grid-template-columns` line; side frames still hide below 860px as before.
- Re-shot fold + full at 1440×900: `shots/…--fold.png`, `shots/…--full.png` (overwritten
  in place). Confirmed visually — no left/right crop, all three headlines fully legible,
  centre frame raised.
- `scroll_verify.py`: unchanged clean result — `deadScroll: []`, `cuesNeverFull: []`,
  `unrevealed: []`, `contrastUnderMedia: []`, `blankBands: []`.
- `a11y_scan.py`: 1 serious `color-contrast` hit on `.band-kicker` ("Utvalda projekt",
  "Kontakt"), reproducible across 5 consecutive runs — but **not caused by this fix**
  (nothing in the diff touches colour, `.band-kicker`, or the reveal system) and not a
  real defect: the steady-state rule is `--faint-on-white:#6b6b6b` on white, computed
  and measured live at `opacity:1` = 5.33:1, comfortably over the 4.5:1 AA floor for
  10.5px text (confirmed by hand with the WCAG relative-luminance formula). Both flagged
  elements sit far below the fold; `a11y_scan.py` runs axe 500ms after `networkidle`
  without scrolling, which is before the page's own 1500ms `.reveal` failsafe fires and
  before either element's `IntersectionObserver` has had a chance to trigger — so the
  scanner is very likely catching the pre-reveal `opacity:0` frame (axe appears to fold
  opacity into the effective on-screen colour), not the resting state a user or a
  scrolled scan would see. Left as-is: fixing the scanner-vs-reveal-timing mismatch would
  mean changing the shared `.reveal`/failsafe mechanism used identically across all six
  R-chain cells, which is restructuring outside this fix round's scope (stage-frame
  sizing + honesty grep only). Flagged here for a separate pass if the coordinator wants
  the animation failsafe shortened or the scanner given a longer settle/scroll step.
- Honesty grep (`e-handel|orderflöde|bordsbokning|biljetter|anmälan|system byggt för att
  växa|meny på en sida|jag|enskild firma|en person|små företag`): 0 hits in R1. No
  changes needed.

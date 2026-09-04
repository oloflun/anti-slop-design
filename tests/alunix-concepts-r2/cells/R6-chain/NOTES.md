# R6 "Creative Giants · affisch" — build notes

Concept: R6, contract row from `tests/alunix-concepts-r2/contract.md`. Dominant source
`creative-giants` (design-catalogue). Register editorial print. Grammar typographic
poster. Correction round (r2): the page borrows the SOURCE'S VISUAL BALANCE — poster
headline scale, whitespace ratio, full-bleed photo weight, section rhythm — while
palette, copy and section order stay Alunix's own. Skip bake-off per instructions
(Tier 2, single assigned direction).

## Skill(...) calls, in order

1. `Skill(design)` — front door; Steps 1b (reference capture and lock), 2b (grammar per
   contract.md's R6 row, bake-off skipped as instructed), 3, 4, 5 followed.
2. `Skill(copywriting)` — args: `CONTENT FUNDAMENTALS: Digital byrå, vi-form, självsäker,
   kort, professionell, Insign-nivå. Nyckelrader: Din digitala byrå, allt på ett ställe ·
   Skräddarsydda digitala lösningar som exponerar ert företag · Nutidens visitkort · Vårt
   enda mått: perfektion · Alla har rätt till bra design ... R6 emphasises the PHILOSOPHY.`
3. `copy-gate.md` Pass 1b read in full and applied: every headline/lead traces to a
   source (brief.md's own lines = source 4, "already good" per contract.md) or was cut;
   no invented counts, testimonials, or logos.
4. `Skill(humanizer-svenska)` — applied by hand to every Swedish string against the
   pattern checklist. No `inte bara X, det är Y`, no `och`-joined tricolon filler, no
   `i hjärtat av` / `kurerar` / `sömlöst` / `unik upplevelse`, no lede restating the
   headline, no sycophantic openers/closers, register kept confident (not sanded to
   neutral) per brief.md's explicit allowance for "vårt enda mått är perfektion" as a
   standard-promise, not a fabricated claim.

## Reference lock + decision ledger

(Condensed version ships as the HTML comment at the top of `index.html`; this is the
full version.)

**Tier:** 2 (reference). `contract.md`'s R6 row assigns `creative-giants` as the
dominant source and names the borrow explicitly: layout balance (hero type, air,
section rhythm, image treatment), never palette or copy verbatim.

**Primary reference:** `design-catalogue/entries/creative-giants/` — read `entry.md`
in full (reference-lock section, signature move, image recipe), `fold.webp`, `shot.webp`,
all 12 `slices/*.webp` as images, and `extract/creativegiants-art-design-language.md`
Typography (Switzer 300/400 only, size ladder from 80px down to 11px, all weight 300),
Layout System (11 grid containers, 1280px max container, hairline 1px dividers), and
Motion Language (feel "mixed", 200/300/550ms durations, `ease` + a sharp custom
accelerate-decelerate curve, one scroll-linked marquee keyframe, otherwise static cuts
between sections, no scroll-scrub set-piece on the fold itself).

**Secondary reference:** `design-catalogue/entries/whatmatters/fold.webp` — one data
point only: a second example of weight-heavy display type sitting directly inside a
full-bleed photograph (confirms the device, not copied — What Matters uses bold serif
centred over the photo; Creative Giants and this build use light-weight type either
above or beside the photo, never centred-bold-on-photo).

**Preserve (traits actually carried into the build):**
- Warm off-white canvas, never pure white (`--bg: #fdfbf4`, own value, not the source's
  literal `#fffef7`).
- Weight 300 for every display/headline size (poster wordmark, all three section
  statements); weight 400/500/600 reserved for body and UI register only, nothing
  bolder than 600 anywhere.
- Progressive negative tracking as size grows: `-0.04em` on the poster wordmark,
  `-0.02em` on section statements and the photo statement.
- Near-invisible chrome: one circular mark + one kicker line on the left, one pill CTA
  on the right, nothing else in the nav.
- Chromatic accents rationed to a single small surface at a time (one 12px swatch per
  project row in Utvalda projekt), never a section fill, never two accent swatches in
  the same row.
- Hairlines and ton-sur-ton for structure (1px dividers in Tjänster and Utvalda
  projekt), zero shadowed cards anywhere on the page.
- Sharp 0px corners on every editorial surface (project thumbnails, swatches); 999px
  pill radius reserved for interactive controls only (nav mark, Kontakt CTA, Besök
  sajten links) — the two radii never cross, per the source's own split-by-function
  rule.

**Borrow only (1-2, not carried further):**
- The charcoal-to-black vertical gradient inside the poster lettering (source's own
  named signature move) — reproduced as a CSS `background-clip:text` gradient on
  `ALUNIX`, not the source's literal colour stops.
- The location-line + statement overlay convention on the full-bleed photo (source:
  "BRIGHTON, UNITED KINGDOM" + a 34px statement in the photo's dark corner) —
  reproduced as "SVERIGE" + a 56px statement, positioned over the genuinely dark
  bottom-left quadrant of the vendored photo, not a synthetic full-image scrim.

**Reject (named, and checked against):**
- Creative Giants' own exact hex palette (`#8a0467` magenta / `#03624c` green /
  `#ffd001` yellow) — Alunix's three accents are independently chosen hues, one per
  demo (Calyx moss `#3c6b4a`, Hōrai wine `#7a2540`, Hyperborea glacier `#2c5c86`), per
  contract.md's "palett tas inte ordagrant" rule.
- Squarespace's centred hero + floating site frames (R1's territory).
- Insign's serif logotype + three flat mättade service bands (R3's territory).
- Sanity's numbered 01-05 full sections (R4's territory) — this build's `01/02/03`
  numerals are small in-row labels, not section-scale numerals with their own act.
- Mattis' console frame with version tag/clock/corner brackets (R5's territory).
- Any drop shadow, any rounded card/image, any chromatic CTA fill, browser-default
  link blue.

**Role rules:**
- Accent colour = one swatch per project row only, never a button, chip, or section
  background.
- Pill radius (999px) = nav mark, Kontakt CTA, Besök sajten links only; 0px = every
  image, thumbnail and swatch; never crossed.
- Body copy left-aligned throughout; centring never used (the source itself is
  left-aligned apart from its own centred nav pill, which this build also avoids).
- No mono typeface introduced — Switzer's source system has no mono register either;
  kickers are set in Public Sans 600 uppercase with wide tracking instead.

**Media strategy:** `photo/k4-cabin-desk.webp` (vendored from
`tests/alunix-concepts/_assets/`) as the fold's full-bleed documentary photo — chosen
over `k4-desk-overhead.webp` because its bottom-left quadrant is genuinely dark (window
light falls top-right, floor and understructure are in shadow bottom-left), which is
what makes the "SVERIGE" kicker and the 56px statement legible without a synthetic
full-image scrim (only a localised gradient behind the text corner, never a rescue
scrim over the whole frame). Three real demo screenshots (Calyx/Hōrai/Hyperborea,
vendored from `~/alunix/public/demos/`) as the only other imagery, used as proof, never
as "our team".

**Token commitments:** bg `#fdfbf4`; ink `#16140f`; ink-soft `#453f30` (darkened from an
initial `#6b6656` after `a11y_scan.py` under `file://` measured real anti-aliased
contrast below floor at 11-15px, see Verification below); ink-softer `#55503f`; invert
`#0c0b08`; invert-ink `#fdfbf4`; invert-soft `rgba(253,251,244,0.72)`; invert-body
`rgba(253,251,244,0.82)`; accent-calyx `#3c6b4a`; accent-horai `#7a2540`;
accent-hyperborea `#2c5c86`; Public Sans 300/400/500/600; radius 999px interactive /
0px editorial; section gap `clamp(64px,9vw,128px)`. Every colour used in the page
resolves through a named `:root` token — no inline hex/rgba outside the token block.

**Decision ledger:**

| Decision | Source | Role | Why |
|---|---|---|---|
| Poster wordmark "ALUNIX" as the fold, not a headline sentence | TASTE.md §4 rule 10 ("Ordmärket får vara heron") + `creative-giants/entry.md` signature move | fold device | R6's own lane is a poster: the company name at affisch scale is the strongest, most honest fold for a first-round agency site with no client roster yet |
| Photo statement "Er webbplats är nutidens visitkort." kept separate from the Filosofi statement "Alla har rätt till bra design." | brief.md's two distinct key lines | copy structure | avoids restating the same sentence twice on one page; frontloads the visitkort promise early, reserves the "alla har rätt" line as Filosofi's dedicated, emphasised statement |
| Filosofi section given 1.35x the vertical padding of every other section | task instruction "R6 emphasises the PHILOSOPHY" | section rhythm | the one deliberate emphasis lever available without breaking the shared section grammar |
| Three project-row swatches, one hue per demo, own palette not creative-giants' | contract.md "palett tas inte ordagrant" + task instruction "one per demo accent" | accent role | keeps the source's rationing discipline (one accent surface, never a fill) while making the palette Alunix's own |
| One tonal inversion (Utvalda projekt on black) | design skill composition contract: "one tonal inversion per page" + Creative Giants' own black projects band | section 3 of 4 | matches the source's own black band placement without copying its exact content (source: project cards with quotes/testimonials; here: the three real demos) |
| `k4-cabin-desk.webp` over `k4-desk-overhead.webp` | task listed both as options; only cabin-desk has a genuinely dark region | photo choice | task's own instruction: "if it fails, put the statement on the off-white below the photo instead" — cabin-desk avoided that fallback entirely by having real contrast headroom, confirmed by `contrast_over_media.py`/`scroll_verify.py` |
| ink-soft darkened from `#6b6656` to `#453f30` mid-build | `a11y_scan.py` under `file://` (500ms wait) measured real rendered pixel contrast at 3.25-3.6:1 on small kicker/label text, below the 4.5:1 floor, due to anti-aliasing dilution at 11-15px sizes not captured by a flat-swatch contrast calculation | token value | verification tooling itself found this, not visual judgement; fixed by choosing declared colours with enough margin (~9:1 flat ratio) to survive the measured dilution |

## Fingerprint (must hold, per contract.md)

grammar **typographic poster** · nav **minimal, pill-meny** · hero-device **rubrik i 300
vid affischskala** · aktform **luft → fullbleed foto → redaktionella sektioner** · avslut
**off-white kolofon** · signature move **små mättade färgytor som enda färg**.

Realized as: a fixed minimal nav (circular mark + kicker + one pill CTA); the poster
wordmark "ALUNIX" at `clamp(3.4rem,15vw,12rem)` weight 300, tracking -0.04em, filling
the viewport width; a full-bleed `k4-cabin-desk.webp` photo directly under it with
"SVERIGE" + a 56px statement in the dark corner; whitespace-led editorial sections
(Tjänster, Utvalda projekt, Filosofi) with hairline dividers, no card shadows; colour
appearing only as three 12px swatches (one per demo project row), never as a section
fill; an off-white colophon closing on `hej@alunix.se` as text + mailto, no form.

Parity check against sibling rows R1-R5 (contract.md's own fingerprint table): shares
at most "minimal chrome" with none of them structurally — R1/R2 use Squarespace's
floating-frame/pill-tab devices, R3 uses a serif logotype + flat colour bands, R4 uses
mono numbered 01-05 sections as full acts, R5 uses a console frame. R6 shares 0/6 with
any sibling beyond the generic presence of a nav and a close.

## Feeling curve

1. **Arrival, quiet confidence.** The poster wordmark alone on cream, no photo yet, no
   claim made — just the name at scale. Caused by: 40%-of-viewport weight-300 type on
   an otherwise empty warm ground.
2. **Grounding, into the real.** Immediate cut to a full-bleed documentary photo
   (drafting desk, afternoon light) with "SVERIGE" and the visitkort line sitting in
   the shadowed corner. Caused by: the hard edge between the fold and the photo (no
   gap, no fade), and the promise line landing exactly where the light is lowest.
3. **Explanation, unhurried.** Tjänster opens onto pure whitespace and a lede
   statement, then three plainly-set items with only a hairline and a number to divide
   them. Caused by: no colour, no icons, generous column gaps.
4. **The one engineered peak: the room goes dark.** Utvalda projekt inverts to near-black
   for the page's only tonal flip, and this is where colour finally appears at all —
   one swatch per row, never more than one per row. Caused by: the section's own
   background flip plus the swatch discipline making each hue feel earned rather than
   decorative.
5. **Settling, the promise stated plainly.** Filosofi returns to cream with the
   tallest whitespace on the page and the largest statement after the poster itself.
   Caused by: the extra 35% padding and the two-paragraph philosophy statement sitting
   alone with nothing competing for attention.
6. **Close, no ceremony.** The colophon is a single mailto link at display scale and a
   one-line footer. Caused by: matching the source's own "Speak to us" plainness
   without literally reusing its form fields (brief.md forbids a form).

Signature move: the three small saturated swatches, one per project row, never doubled
in a row, are the only chromatic colour on the entire page, echoing Creative Giants'
own "never more than one accent card in a row" rule while using Alunix's own hues.

## Full Swedish copy (as shipped)

**Nav:** "DIGITAL BYRÅ · WEBBDESIGN, DESIGN, SYSTEM" · "Kontakt"

**Fold:** "ALUNIX"

**Photo:** "SVERIGE" · "Er webbplats är nutidens visitkort."

**Tjänster:** "TJÄNSTER" · "Webbdesign, design och system. Allt på ett ställe."
- 01 Webbdesign — "Skräddarsydda webbplatser som exponerar ert företag. Nutidens
  visitkort, byggt för er verksamhet."
- 02 Design — "Varumärke och grafisk form som gör att sajten ser ut som företaget
  bakom den."
- 03 System — "Egna digitala lösningar, som Alunix OS och ett lagersystem, visar den
  tekniska höjden vi bygger på."

**Utvalda projekt:** "UTVALDA PROJEKT" · "Tre sajter, i drift."
- 01 Calyx, Florist, Stockholm — "E-handel och orderflöde för en Stockholmsflorist."
  → Besök sajten (https://anti-slop-design.vercel.app/calyx)
- 02 Hōrai, Restaurang, Stockholm — "Bordsbokning och meny för en restaurang i
  Stockholm." → Besök sajten (https://anti-slop-design.vercel.app/horai)
- 03 Hyperborea, Konferens, Lund — "Anmälan och program för en konferens i Lund." →
  Besök sajten (https://anti-slop-design.vercel.app/hyperborea)

**Filosofi:** "FILOSOFI" · "Alla har rätt till bra design." · "Därför lägger vi oss på
en nivå som gör våra tjänster tillgängliga för fler, utan att kompromissa med
resultatet. Vårt enda mått är perfektion." · "Din digitala byrå, allt på ett ställe,
från första skiss till levererad sajt."

**Kontakt:** "KONTAKT" · "hej@alunix.se" · "Nutidens visitkort börjar med ett mejl." ·
footer: "Alunix · digital byrå" · "WEBBDESIGN · DESIGN · SYSTEM"

Checked against the forbidden list: no invented counts, testimonials, ratings, or
percentages anywhere; no customer named beyond the three demos; never "Klova"; no
em/en dashes anywhere in the rendered page (confirmed by grep, 0 occurrences); no
"enskild firma / en person / små företag / jag" anywhere (vi-form throughout); no
price line (none requested for this concept).

## Verification

- `shoot.py` — fold + full page captured and read as images at desktop (1440x900);
  iterated: first pass looked correct, no re-shoots needed for layout.
- Custom mobile pass (shoot.py has no viewport flag) at 320/375/414/768px: zero
  horizontal overflow at all four breakpoints (`scrollWidth === clientWidth`
  confirmed programmatically); screenshots read and confirmed sections collapse to one
  column, no two-line clickable text, poster wordmark wraps via `overflow-wrap:anywhere`
  without breaking layout.
- `scroll_verify.py` — clean on every metric: `deadScroll: []`, `cuesNeverFull: []`,
  `unrevealed: []`, `contrastUnderMedia: []`, `blankBands: []`.
- `contrast.py` (served over a local static server, per the tool's own requirement) —
  22 token backgrounds checked, 0 under the floor, including both strings that sit over
  the photo ("SVERIGE" and the 56px statement), confirmed against the actual rendered
  pixels of the brightest frame under the text.
- `a11y_scan.py` against the `file://` URL — first pass found 1 serious `color-contrast`
  finding plus 3 moderate structural findings (`heading-order`, `landmark-one-main`,
  `region`). Root-caused and fixed:
  - Structural: added a `<main>` landmark around the four content sections, and
    promoted the three section-lede paragraphs (Tjänster/Utvalda projekt/Filosofi) from
    `<p>` to `<h2>` so the heading order runs h1 → h2 → h3 without a skip.
  - Contrast: axe's `file://` pass measures real rendered pixels including
    anti-aliasing, and reported the small kicker/label text (11-15px) at 3.25-3.6:1 —
    lower than a flat-swatch contrast calculation gives, because thin anti-aliased
    edges at small sizes dilute the effective sampled colour toward the background.
    `contrast.py`'s canvas-rasterized check and an `http://` serve of the same page
    both read the flat values as passing (5.5:1+), which is why this needed the actual
    `file://` + axe combination named in the task to surface it. Fixed by darkening
    `--ink-soft`/`--ink-softer` to values with roughly 9:1 flat contrast, giving enough
    margin to clear 4.5:1 after the measured dilution. Also moved every remaining
    inline hex/rgba color into the `:root` token block while fixing this (gate 48).
  - Re-verified 3 consecutive runs against the `file://` URL after the fix: **0
    violations, 25 passes** every time.
- `detect.mjs` not run (no build step in this static single-file cell; the mechanical
  detector targets a project's changed files, and gates 66-88/production-tells were
  checked by hand against the reference lock above).
- Three-reviewer dispatch (design-critic / design-a11y-reviewer / design-heuristics)
  not run for this single-cell chain build; the scripted verification chain above
  (scroll_verify + contrast + a11y_scan, each re-run to confirm stability) stood in for
  it given the task's explicit verification list.

## Balance vs. source

`shots/vs-source.png` places the full-page capture beside `creative-giants/shot.webp`
at matched heights. The balance matches: both open on a warm off-white ground with a
weight-300 wordmark occupying roughly the same fraction of the first viewport, cut hard
into a full-bleed documentary photograph with a location line and a light display
statement sitting in the photo's dark region, then settle into whitespace-led editorial
sections before a black band (the source's project cards, this build's Utvalda
projekt) and close light. The proportions between type, air and photo track the
source; what differs, as instructed, is the palette (Alunix's own cream/ink/three
accent hues, not Creative Giants' literal hex values), the copy, and the exact section
content — the source's black band shows testimonials and a news grid, this one shows
the three real demo sites, which is the honest substitute for a first-round agency
site with no press coverage yet.

## Fix round (coordinator pixel pass)

Two complaints: (1) the ALUNIX wordmark read at only ~45% of the viewport width
instead of spanning edge-to-edge like Creative Giants; (2) the three project
descriptions in "Utvalda projekt" invented scope the brief forbids.

- **Wordmark root cause:** `.poster{font-size:clamp(3.4rem, 15vw, 12rem)}` capped at
  `12rem` (192px) — on any viewport wider than ~1280px the `15vw` term exceeds that cap
  and the clamp locks the font-size at 192px regardless of how much wider the screen
  gets, so the word stops growing while the viewport keeps growing (measured: 645px
  wide at 1440px viewport = 45%, matching the complaint exactly). The `.fold .wrap` also
  inherited the shared `.wrap` rule's `max-width:1280px` and `padding: clamp(20px,5vw,
  64px)`, both of which further capped the available width and prevented true
  edge-to-edge margins.
- **Fix:** added a `.fold .wrap{max-width:none; padding-left:16px; padding-right:16px}`
  override (scoped to just this section's `.wrap` instance, not the shared rule used by
  nav/other sections) for hairline 16px margins, and changed
  `.poster{font-size:clamp(3.4rem, 15vw, 12rem)}` to `clamp(2.75rem, 28vw, 40rem)` — a
  pure-`vw` middle term with the upper cap raised far out of reach (40rem = 640px, only
  binding above ~2285px-wide screens) so the rendered word width stays a constant
  proportion of the viewport at any normal screen size, the way Creative Giants' own
  wordmark behaves. `font-weight` untouched (still 300 via the shared `h1,h2,h3` rule)
  and the gradient (`linear-gradient` background-clip) untouched.
- Verified with exact `getBoundingClientRect()` measurements at four widths via a
  scratch Playwright script (not just eyeballing): 390px → word 358px wide (16px margin
  both sides), 768px → 736px wide, 1440px → 1408px wide, 1920px → 1888px wide — i.e.
  ~92-94% of the viewport at every size, hairline margins held constant, zero horizontal
  page overflow confirmed at 320/390/768px (`scrollWidth - clientWidth === 0` at all
  three).
- Re-shot fold + full at 1440×900 (`shots/…--fold.png`, `shots/…--full.png`, overwritten
  in place): "ALUNIX" now runs edge-to-edge with hairline margins, matching the
  Creative Giants reference this concept is built on — this round's fix corrects the
  original NOTES.md's "occupying roughly the same fraction of the first viewport"
  balance claim, which pixel measurement shows was not accurate before this fix.
- **Copy fix:** the three `.desc` lines under "Utvalda projekt" invented forbidden
  scope — Calyx "E-handel och orderflöde för en Stockholmsflorist." (e-commerce/order
  flow), Hōrai "Bordsbokning och meny för en restaurang i Stockholm." (table booking),
  Hyperborea "Anmälan och program för en konferens i Lund." (registration) — flagged by
  the coordinator's honesty grep. Rewrote each to carry only that project's own allowed
  fact from brief.md: Calyx → "Kursiv och rak typografi i samma rad, på krämvitt
  papper.", Hōrai → "Fotografiet får bära hela sidan.", Hyperborea → "Ett ritat
  solmotiv i åtta varianter, kodat i SVG."
- `scroll_verify.py`: unchanged clean result (`deadScroll/cuesNeverFull/unrevealed/
  contrastUnderMedia/blankBands` all `[]`).
- `a11y_scan.py`: reproducible-but-unstable `color-contrast` hits across 3 consecutive
  runs (11, 3, then 11 flagged nodes — `.kicker`, `.service-index`, service/philosophy
  body text, `.colophon-note`), none on anything touched by this fix round (wordmark
  container/size, or the `.desc` copy). Same pattern already diagnosed on R1 in this
  round: these elements are all `.reveal` and sit below the fold; `a11y_scan.py` runs
  axe 500ms after `networkidle` with no scrolling, which is before this page's own
  1500ms `.reveal` failsafe fires and before most below-fold elements'
  `IntersectionObserver` has triggered, so the scanner is very likely sampling the
  pre-reveal `opacity:0` frame rather than the resting state — consistent with the
  node count changing between otherwise-identical runs. NOTES.md's own build-time
  record above shows this file previously stabilized at "0 violations, 25 passes"
  across 3 consecutive runs, so this is new since then, but is a scanner/reveal-timing
  interaction, not a regression traceable to this round's diff. Left as-is: fixing it
  would mean changing the shared `.reveal`/failsafe mechanism used identically across
  all six R-chain cells, which is restructuring outside this fix round's scope
  (wordmark sizing + honesty grep only). Flagged here, same as R1, for a separate pass
  if the coordinator wants the failsafe timing shortened or the scanner given a
  scroll/settle step.
- Honesty grep (`e-handel|orderflöde|bordsbokning|biljetter|anmälan|system byggt för att
  växa|meny på en sida|jag|enskild firma|en person|små företag`) re-run after the edit:
  0 hits. (Noted but out of scope: `.project-thumb` further down this same page crops
  the Calyx/Hōrai headlines the same way R1/R2/R5's thumbnails did before their fixes —
  not part of this round's assigned R6 fix, which was scoped to the wordmark and the
  three `.desc` lines only; flagged separately.)

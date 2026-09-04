# K6 "Kortlek" — build notes

Concept: K6, contract row from `tests/alunix-concepts/contract.md`. Authority = rörelsen
(motion). Category playful. Register modern clean, light and airy. Grammar live surface.
World: *Skrivbord med kort* — a light desk surface, the three demo sites as a deck of
cards that fans out as you scroll, drawing instead of photography.

## Skill(...) calls, in order

1. `Skill(design)` — front door, Steps 1b/2b/3/4/5 followed as instructed.
2. `Skill(animate)` — motion gate for the card-deck signature move (frequency, purpose,
   tool, properties, easing, interruption, reduced motion).
3. `Skill(copywriting)` — args: `CONTENT FUNDAMENTALS: Verb först, lekfull, en rad per
   sektion som får le, resten rak. Swedish B2B micro-site for Alunix web design service,
   K6 Kortlek concept.`
4. `Skill(humanizer-svenska)` — applied by hand to every Swedish string against its
   33-pattern checklist (no `inte bara X, det är Y`, no tricolons-with-`och` filler, no
   `i hjärtat av` / `kurerar` / `sömlöst` / `unik upplevelse`, no lede restating the
   headline, no sycophantic openers/closers).

`copy-gate.md` (Pass 1b line-sources + the structure rule) was read in full and applied
between steps 3 and 4, per the design skill's Step 6 copy gate.

## Reference lock + decision ledger

(Condensed version ships as an HTML comment at the top of `index.html`; this is the full
version.)

**Tier:** 2 (reference), inside an already-assigned diversity-contract cell —
`contract.md`'s K6 row is the binding tier-2 brief. Alunix's own brand evidence (Tier 1)
is thin — one existing near-black "instrument" register, explicitly free for reuse by at
most one of the six concepts, not this one — so the catalog references carry direction.

**Primary reference/direction:** Dovetail (`design-catalogue/entries/dovetail/entry.md`)
— butter-cream editorial calm, zero stacked shadow, three radius values each with one
job, monochrome line illustration — as the dominant structural voice. Bumble
(`entries/bumble/entry.md`) contributes the card-as-object device. André Cândido
(`entries/andre-candido/entry.md`) contributes the single-reserved-accent discipline.

**Preserve (3-5 traits):** cards read as physical objects (soft confident radii, exactly
one whisper shadow value, drawn linework detailing), never a shadow stack; one warm mood
colour deployed at display scale only, never as a button/chip/badge fill; every icon is
drawn linework, never an icon set; a light, quiet canvas with hairline separations, never
a saturated colour block; type stays weight 300-500 at modest sizes so the deck's motion,
not the type, carries the page (TASTE.md §1 "Rörelsen" row + §4 rule 8).

**Borrow only (1-2):** the tilted, overlapping card-collage feeling from Bumble, rebuilt
as the three real demo screenshots (never member photos, never on a honey ground); André
Cândido's single-reserved-accent discipline (the mood colour lives only in linework and
the CTA underline, never a UI fill).

**Role rules:** accent never fills a button, chip or card background, display scale only
(linework, CTA underline, the drifting doodle); the one shadow value belongs to the cards
alone, nothing else on the page casts one; 28px radius is cards-only, 999px is pills-only
(nav, CTA, chips), the two are never crossed; mono type is register only (kicker, nav
label), never a heading; body copy stays left-aligned, centring is display-line only.

**Media strategy:** product surface (the three vendored demo screenshots, copied from
`~/alunix/public/demos/`, never hotlinked) for proof, the only imagery on the page; drawn
inline SVG for every icon and desk motif; no photography, no stock imagery, no icon font.

**Reject:** honey-yellow ground (Bumble's own palette, explicitly forbidden by
`contract.md`); Bumble's literal member-photo tilt collage reused verbatim; a second
chromatic hue; colour-block sections (K2/K5's register, forbidden by `contract.md`);
display type above 96px (K3/K5's territory, forbidden by `contract.md`); any icon font or
line-icon set; scroll-scrub video (forbidden by `contract.md`); Klova as a named customer
(forbidden by `brief.md`, binding).

**Token commitments:** canvas `oklch(96% .014 75)` warm oat linen; card face
`oklch(98% .008 80)`; canvas-deep `oklch(90% .02 70)` for chip/hairline backgrounds; ink
`oklch(24% .02 50)`; ink-soft `oklch(44% .02 50)` (body/secondary, measured against
canvas, see contrast numbers below); accent `oklch(70% .12 20)` warm coral-rose,
CTA-underline/linework/drift only; type Manrope 300-600 for voice, IBM Plex Mono 500 for
register at 11px/0.16em tracking; radius 28px cards / 999px pills; shadow one value only
(`0 14px 28px -16px`, cards only); page max-width 1180px, section gap
`clamp(64px,10vw,120px)`.

**Decision ledger:**

| Decision | Source | Role | Why |
|---|---|---|---|
| World "Skrivbord med kort" | `contract.md` K6 row | binding world preamble | assigned cell, not invented |
| Card-as-object + exactly one shadow | `bumble/entry.md` "one approved shadow value" | shadow role: cards only | a physical card needs to lift off the desk; the house rule against shadow stacks caps it at one value system-wide |
| Drawn line illustration, zero icon set | `dovetail/entry.md` media strategy + TASTE.md §3 "playful" row ("Illustration bara som teckning... aldrig ikon-set") | icon role: all iconography | matches contract's "teckning i stället för foto" |
| One reserved warm accent, never a UI fill | `andre-candido/entry.md` role rules + TASTE.md §4 rule 4 | accent role: linework/CTA-underline/drift only | one warm mood colour without landing on honey-yellow, which is forbidden |
| Radius split 28px cards / 999px pills, never crossed | `dovetail/entry.md` "three distinct radius values, each one job" | radius role | confident radii per house-physics.md §5, without literally reusing Dovetail's own 91px value |
| Canvas is oat/linen, not butter-cream, not honey | TASTE.md §2 "ett papper, en accent" + `contract.md` forbidden list | canvas role | stays distinct from Dovetail's exact butter cream and Bumble's honey |
| Type weight 300-500, modest scale, never above 96px | TASTE.md §1 "Rörelsen" row + §4 rule 8 + `contract.md` forbidden list | type role: quiet | motion is this page's authority, so type stays quiet and under the K3/K5 display ceiling |
| Grammar "live surface" realized via contract.md's own concrete fingerprint | `contract.md` K6 fingerprint row | nav/hero/act/close/signature | `contract.md`'s per-K fingerprint table is the binding spec for this bake-off cell; `scroll/grammars.md`'s generic "app-chrome" reading of live-surface is a different literal interpretation and is deliberately not used here |

## Fingerprint (must hold, per contract.md)

grammar **live surface** · nav **a floating pill** · hero device **a fanning card deck**
· act shape **drift/parallax** · close **a reveal** · signature move **the deck
reshuffles on scroll**.

Realized as: a fixed floating pill nav (wordmark + mailto pill); a hero deck of the
three demo screenshots as the fold's dominant object — a two-column fold grid (41fr
text / 59fr deck at desktop) with cards cascading diagonally to a bounding box of
`2.05 × cw` by `2.6 × ch` (≈57% of viewport width, near full section height at 1440px),
legibly fanned (not stacked flat) with a slow idle float, deliberately larger than the
headline so motion, not type, reads as this page's authority; the same three
screenshots as the full-size proof cards, continuously reordering their rotation/
offset/z-index as the proof section scrolls past (the signature reshuffle — driven by a
single rAF loop, `transform`/`z-index` only, capped to a small amplitude so the motion
never bleeds into the next section); a drifting ink doodle in the fold as the page's
other drift/parallax touch; a close section that is nothing more than the shared reveal
transition, no dark inversion, no bigger type than the rest of the page.

## Feeling curve

- **Fold** — calm confidence. A light desk, a deck that sits closed and waiting; the
  headline invites a shuffle ("Blanda korten...").
- **Bevis** — curiosity into proof. The cards drift as the section scrolls, each one a
  real site you can leave the page for. Peak: full fan, three cards spread, the deck
  quietly reordering itself the whole time you are reading.
- **Hur det går till** — steadying. The cards settle into a plain three-step row, one
  drawn line icon per step, two honest placeholders instead of a made-up price.
- **Avslut** — quiet exhale. The shared reveal, nothing louder than the rest of the
  page, one mailto and one line about the same hands building the other two products.

## Full Swedish copy (plain text)

**Nav**
Alunix
Skriv ett mejl (→ mailto:hej@alunix.se)

**Fold**
Kicker: Webbdesign · en utvecklare
H1: Blanda korten, se tre helt olika sajter dyka upp.
Body: Jag bygger sajter åt små företag i Sverige. En person, inget team, ingen mall som
redan är vald åt dig. Designen hämtas ur ditt eget material varje gång, inte ur ett tema
någon annan sålt först.
CTA: Mejla hej@alunix.se

Mini-deck tags: Calyx / Hōrai / Hyperborea

**Bevis**
Kicker: De tre korten
H2: Dra ett kort, öppna en sajt på riktigt.
Body: Tre sajter, samma byggare, tre olika röster. Klicka och syna själv, ingenting här
är en mockup.

Card 1 — Calyx
Voice line: Kursiv och rak i samma rad
Fact: Florist i Stockholm. Cream papper, Cardo och PT Mono, ett prissatt index i stället
för en meny med bilder.
Link label: Öppna sajten → https://anti-slop-design.vercel.app/calyx

Card 2 — Hōrai
Voice line: Fotografiet bär hela sidan
Fact: En restaurang med tre systrar bakom. Lackröd accent, Cinzel i kapitäler, nästan
ingen text i vägen för bilden.
Link label: Öppna sajten → https://anti-slop-design.vercel.app/horai

Card 3 — Hyperborea
Voice line: Ett ritat solmotiv i åtta varianter
Fact: Konferens i Lund. Midnattsblått, bärnsten och en sol som är kodritad SVG, ingen
bild är en photo.
Link label: Öppna sajten → https://anti-slop-design.vercel.app/hyperborea

**Hur det går till**
Kicker: Så går det till
H2: Peka på vad du behöver, så ritar jag resten.

Step 01 — Skicka det du har
Logotyp, produkt, bransch, en länk till sajten ni har i dag om det finns en.

Step 02 — Jag härleder en riktning
Typsnitt, palett och rytm väljs ur ert material, aldrig ur ett färdigt tema.

Step 03 — Du testar en levande sajt
Innan något lanseras, inte efteråt. Ni klickar runt precis som i korten ovan.

Chips: Pris → [behövs pris] · Leveranstid → [behövs leveranstid]

**Kontakt (avslut)**
Kicker: Kontakt
H2: Skriv ett mejl, få svar av mig.
Body: Jag ritar sajten och jag svarar i mejlen. Inget formulär, ingen mellanhand. Ibland
är svaret nej, och då säger jag det.
Mailto: hej@alunix.se
Small line: Samma händer bygger Alunix OS, ett skrivbordsprogram som ritar upp ett
företags kunskap som en graf, och ett lagersystem för gods och följesedlar. Webbdesign
är den tredje delen, den du ser här.

**Footer**
Alunix · webbdesign

## Coordinator pixel-pass, round 2 (post-delivery fixes)

Three fixes requested after a pixel pass of the delivered page:

1. **Honesty.** "Tre kunder, samma byggare" called the demo sites customers, against
   `brief.md`'s rule that the three demos are never customers. Changed to "Tre sajter,
   samma byggare" in the Bevis body copy (`index.html` and this file, above). Searched
   the whole file for `kund` — this was the only occurrence.
2. **Deck as dominant hero device.** The fold was rebuilt from a single centred column
   into a two-track grid (`.fold-grid`, 41fr text / 59fr deck at ≥900px) so the deck is
   no longer a small accessory under the headline. The deck itself was resized so its
   own bounding box, not just its column, is the dominant object: `--cw` (card width)
   now clamps up to 420px at desktop, cards cascade diagonally
   (`left: 0 / 0.55cw / 1.05cw`, `top: 0 / 0.85ch / 1.6ch`), giving a bounding box of
   `2.05 × cw` wide by `2.6 × ch` tall — roughly 800×640px at 1440px viewport width,
   about **57% of viewport width** and close to full fold-section height. Confirmed by
   re-reading the fold screenshot: the deck now visibly outsizes the headline block.
3. **Dead vertical bands.** Two contributing causes, both fixed: (a) `--gap` (the
   shared section padding token) cut from `clamp(64px,10vw,120px)` to
   `clamp(48px,6vw,88px)`; (b) the fold's own vertical slack shrank as a side effect of
   fix 2 — a much taller deck leaves far less empty centring space in its column.
   Measured directly on the re-shot `--full.png` (pixel crops, not guessed): fold→Bevis
   gap ≈200px, Bevis→"Så går det till" ≈196px, chips→Kontakt ≈182px — all well under
   one viewport height, none read as a void in the static capture.

## Verification (Step 5)

All commands run from the repo root, every PNG read as an image, not inferred from code.

1. **`shoot.py`** (`tests/alunix-concepts/cells/K6-chain/shots/*--fold.png`,
   `*--full.png`) — iterated three times:
   - Round 1 found the deck's scroll-linked `translateY` bleeding into the next
     section, hiding the "SÅ GÅR DET TILL" kicker under the card shadows. Fixed by
     capping the reshuffle amplitude (±8px translate, ±4px translateX, no accumulating
     drift) instead of a progress-scaled offset, plus a small buffer margin on `.deck`.
   - Round 2 found every section's vertical padding collapsed to zero: `.wrap{padding:0
     24px}` (a class selector) was silently beating `section{padding:var(--gap) 0}` (a
     tag selector) on specificity regardless of source order, on every `section.wrap`
     in the document. Fixed by changing `.wrap` to `padding-left`/`padding-right`
     longhands only, so it never touches the vertical padding the base `section` rule
     sets.
   - Round 3: clean. Fold and full-page screenshots read; hierarchy, spacing and the
     deck all correct. (One known Chromium/Playwright full-page-screenshot quirk: the
     fixed nav pill appears a second time near the very bottom of the stitched
     `--full.png` — confirmed by grep that only one `<nav>` exists in the DOM; this is a
     capture artifact of `full_page=True` screenshots with `position:fixed` elements,
     not a real duplication on the live page.)
   - Round 4 (coordinator's pixel pass): re-shot after the fold rebuild (two-column
     grid, dominant deck, tighter `--gap`). Both PNGs read again: the deck reads as the
     fold's largest object at every breakpoint checked, and the section-to-section gaps
     measured by pixel crop (see above) dropped from the earlier ~400-500px impression
     to ~180-200px.

2. **`scroll_verify.py`** — clean, both before and after round 4:
   `deadScroll: []`, `cuesNeverFull: []`, `unrevealed: []`, `contrastUnderMedia: []`,
   `blankBands: []`. Post-fix run: 9 scroll positions sampled 0→2206px (page got
   shorter once the fold's dead centring space shrank).

3. **`a11y_scan.py`** — first run found one moderate `heading-order` violation (the
   "Bevis" and "Hur det går till" section ledes were `<p class="lede">`, skipping from
   `<h1>` straight to `<h3>` on the steps). Fixed by promoting both ledes to `<h2
   class="lede">` (semantically correct — they are each section's heading). Second run:
   **0 violations, 25 passes, 1 incomplete** (axe's own "needs manual review" flag, not
   a failure).

4. **Contrast** — `contrast.py` in the design skill ignores its CLI argument and always
   hits `localhost:3055`, so it silently scored an unrelated already-running page. Wrote
   a corrected copy of the same rasterising-canvas JS pointed at this file directly
   (used once, then deleted, not part of the deliverable): **24 token background pairs
   checked, 0 under the WCAG floor**, ratios from 5.31:1 up to 17.17:1. 0 strings sit
   over photo/video (the mini-deck tags have their own opaque overlay background, so
   they are token-measurable, not photo-measurable).

5. **Mobile** — 320 / 375 / 414 / 768px re-checked after the fold rebuild with a one-off
   Playwright script (used, screenshots kept in `shots/mobile-*.png`, script deleted):
   `scrollWidth === clientWidth` at all four widths, no horizontal overflow. The deck
   stacks below the text below 900px and stays legible and cascading; cards collapse to
   one column under 820px; chips wrap; nav pill stays on one line.

6. **Reduced motion** — re-checked after the fold rebuild with `reduced_motion: "reduce"`
   (screenshots kept in `shots/reduced-fold.png` and `shots/reduced-scrolled.png`,
   script deleted): the mini-deck's idle float animation is gated behind
   `@media (prefers-reduced-motion: no-preference)` so it never runs; the JS reshuffle
   loop returns immediately after the failsafe reveal when
   `matchMedia('(prefers-reduced-motion: reduce)')` matches, so the deck, now the
   dominant fold object, stays in its static cascaded CSS position at every scroll
   position, fully legible, no jitter.

7. **Contrast, a11y and scroll_verify were all re-run after round 4** and stayed clean
   (0 a11y violations, 0 blankBands/unrevealed/deadScroll) — the fold rebuild only
   touched layout geometry, not colour tokens, headings or the reveal system.

8. **Line budget** — `index.html` is 394 lines, inline CSS/JS, Google Fonts only,
   no other CDN, no framework.

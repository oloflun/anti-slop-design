# R4 — Sanity · numrerat (Alunix)

## Reference lock
**Primary:** Sanity.io (`design-catalogue/entries/sanity`) — full-bleed dark hero with a
compressed, tightly-tracked display headline and one pill CTA, dropping to a white canvas
of Swiss-editorial numbered sections (01–05) with a sticky mono number rail beside real
product screenshots.
**Preserve:** onyx (not pure black) dark surfaces · huge compressed left-aligned headline,
tracking −0.04em · exactly one accent confined to the CTA pill, never decorative · sticky
01–05 mono number rail beside scrolling content · real unstyled screenshots standing in
for illustration · dark closing band as the accent's second and last use.
**Borrow only:** pill radius on every interactive control; low (4px) radius on images,
never card-shadowed.
**Role rules:** accent (#1E5E9C, Alunix blue, never orange) appears on exactly two pills
(hero CTA, closing CTA) and nowhere else — no accent text, no accent backgrounds, no
accent numerals. Mono is register only (nav, numbers, captions), never body voice.
**Media strategy:** photo:vendored (`hero.webp` = `k1-stage-beams.webp`, dark stage-light
texture, treated as atmosphere, not a literal claim) for the hero; three genuine product
screenshots (Calyx, Hōrai, Hyperborea, vendored from `~/alunix/public/demos`) as the
numbered-section imagery, standing in for illustration per Sanity's own signature move.
**Reject:** orange or a second saturated accent · drop shadows · centred display
headlines · card grids · invented stats, customer counts or logos · a full scrim over the
hero photo as a contrast shortcut.
**Token commitments:** bg `#ffffff`; dark `#0c0c0e` (onyx, not pure black); accent
`#1E5E9C` (~6.7:1 white-on-blue, AA); display/body Archivo 700/400,
clamp(2.6rem,7vw,6.4rem)/leading .96/tracking −0.04em for display; register IBM Plex Mono
400/500 for nav, kickers, numbers, captions; radius 999px interactive, 4px images;
max-width 1240px.

The full reference-lock block and decision ledger are also written as an HTML comment at
the top of `index.html`, per Step 1b.

## Fingerprint row (contract.md)
grammar: chaptered editorial · nav: mörk topprad, mono-nav · hero-device: fullbleed
texturfoto + komprimerad rubrik · aktform: 01–05 numrerade vita sektioner · avslut: mörkt
band + pill · signature move: numren 01–05 i mono som spår. Matches contract.md's R4 row;
shares only ≤2/6 dimensions with R1–R3 and R5–R6 (grammar is the one deliberate overlap
with R2/R3, everything else — nav, hero device, act shape, close, signature move — is R4's
own).

## Feeling curve
1. **Hero** — arrival, confidence. A dark, textured stage-light photo and a huge
   compressed headline say "this is a serious partner" before a word is read.
2. **Process intro** — relief. "Fem steg till en sajt som gör jobbet" promises order
   after the hero's weight.
3. **01–02 (Behovsanalys, Design)** — trust building. Short, concrete process copy, then
   the first real proof (Calyx) lands as the peak of the numbered run — a genuine
   shipped site, not a mockup.
4. **03–04 (Utveckling, Lansering)** — competence. Alunix OS/lagersystem as evidence of
   technical depth, then "Vårt enda mått: perfektion" paired with Hyperborea as the
   second, larger proof point — the engineered peak of the page.
5. **05 + close** — reassurance and action. The philosophy line closes the process, then
   the dark band (the accent's second and last appearance) asks for one thing: an email.

Signature move: the sticky 01–05 mono rail running beside the scrolling process content,
directly borrowed from Sanity's own numbered-section device and reframed as Alunix's
project process instead of a feature list.

## Copy (Swedish, final)
**Fold** — kicker: Digital byrå · H1: "Er digitala byrå. Allt på ett ställe." · sub: "Vi
skapar skräddarsydda digitala lösningar som exponerar ert företag: webbdesign, grafisk
form och egna system, samlat hos en partner." · CTA: "Boka ett möte" (mailto) / "Se
processen" (ghost).

**Process intro** — kicker: Processen · H2: "Fem steg till en sajt som gör jobbet" ·
lead: "Vi håller ordning på arbetet så att ni slipper göra det. Från första samtalet till
lanserad sajt vet ni alltid var vi är i processen."

**01 Behovsanalys** — "Vi lär känna företaget" / "Vi går igenom vad företaget gör och vad
sajten faktiskt ska lösa. Ingen färdig mall. Resultatet är en tydlig plan för resten av
arbetet."

**02 Design** — "Design som ser ut som er" / "Grafisk form och varumärke sätts innan en
enda rad kod skrivs. Färg, typografi och ton väljs utifrån företaget som ska bära dem."
Proof: Calyx, florist → anti-slop-design.vercel.app/calyx.

**03 Utveckling** — "Byggt för att hålla" / "Sajten byggs skräddarsydd för verksamheten,
inte hoprafsad i ett färdigt tema. Vi bygger även egna system, bland annat Alunix OS och
ett lagersystem, så vi vet hur teknik ska hålla över tid." Proof: Hōrai, restaurang →
anti-slop-design.vercel.app/horai.

**04 Lansering** — "Vårt enda mått: perfektion" / "Innan lansering går vi igenom varje
sida, länk och bild. Så här ser resultatet ut när det är klart." Proof: Hyperborea,
konferens → anti-slop-design.vercel.app/hyperborea.

**05 Förvaltning** — "Alla har rätt till bra design" / "Vår filosofi är att alla har rätt
till bra design. Därför lägger vi oss på en nivå som gör våra tjänster tillgängliga för
fler, utan att kompromissa med resultatet. Det gäller efter lansering också."

**Close** — kicker: Kontakt · H2: "Nutidens visitkort är er sajt." · body: "Hör av er så
pratar vi om hur den ska se ut." · CTA: hej@alunix.se (mailto).

No invented numbers, customers, reviews or logos. No em dashes anywhere visible (checked
by grep). Vi-form throughout; no "enskild firma / en person / jag".

## Skill(...) calls, in order
1. `Skill(design)` — SKILL.md, Steps 1b (reference lock + ledger), 2b (grammar/feeling
   curve/fingerprint, bake-off skipped per instruction), 3, 4, 5.
2. `Skill(copywriting)` — CONTENT FUNDAMENTALS: digital byrå, vi-form, självsäker, kort,
   professionell, Insign-nivå; R4 emphasis = process (01–05).
3. Read `copy-gate.md` Pass 1b directly (Anton's brief lines = source 4, already
   pre-approved; used "Din digitala byrå, allt på ett ställe", "Nutidens visitkort",
   "Vårt enda mått: perfektion" and the "alla har rätt till bra design" philosophy
   paragraph close to source).
4. `Skill(humanizer-svenska)` — every Swedish string checked against the 16 pattern
   families; no tricolon padding, no "sömlöst"/"unik upplevelse"/"inte bara X utan Y", no
   nominalisation or copula avoidance, no hedging or sycophancy. Fixed one violation this
   pass introduced: an em dash in the `<title>` and footer wordmark line, both replaced
   with "·".

## Verification numbers
- `shoot.py` fold + full (1440×900 viewport, full page 5319px): clean on first render
  except two real bugs, both fixed and re-shot:
  1. `.step__num` label column (72px) too narrow for "Förvaltning"/"Behovsanalys" at 15px
     mono bold — text bled into the headline column. Fixed: column widened to
     `minmax(0,132px)`, label font reduced to 12.5px with `overflow-wrap:break-word`, and
     a `max-width:639px` query stacks the step to a single column on phones.
  2. Mobile nav (`.nav-links`) had no breakpoint hiding it below 640px, so at 320–414px
     "KONTAKT" was clipped at the viewport edge by `overflow-x:clip`. Fixed: nav-links
     hidden below 640px, `.nav-cta` (Boka möte pill) shown at all widths instead.
- Mobile sweep via a throwaway Playwright script at 320/375/414/768px: `scrollWidth ==
  clientWidth` at every width (no horizontal overflow); full-page captures read clean at
  all four after the two fixes above — one blank-page bug was caught here too (see below).
- `scroll_verify.py`: `deadScroll: []`, `cuesNeverFull: []`, `unrevealed: []`,
  `contrastUnderMedia: []`, `blankBands: []` — **0 / 0 / 0**, clean on the run this NOTES
  reports.
  - Root cause of the blank-page bug it exposed: the reveal failsafe timer was 2500ms,
    longer than the ~900–1200ms wait both `shoot.py` and my mobile script use before
    capturing, so full-page screenshots (which resize the viewport rather than scroll it)
    were taken before the IntersectionObserver had fired or the failsafe had run —
    content sat at `opacity:0` for the whole page below the fold. Fixed: failsafe cut to
    700ms and `rootMargin` widened to `400px` so reveals fire earlier under real scroll
    too. Reduced-motion and no-IntersectionObserver paths were already fail-open.
- `a11y_scan.py`: 0 violations, 33 passes, 1 incomplete (an axe-core "incomplete" check,
  not a finding). One moderate "region" violation on the first pass (sections not
  contained by a landmark) fixed by wrapping the hero-through-close sections in `<main>`;
  re-run came back clean.
- Line count: 312 lines (cap was 440).

## Balance vs. source
`shots/vs-source.png` places the full R4-chain capture beside Sanity's `shot.webp`. The
hero half matches Sanity's balance closely: full-bleed dark texture, a headline at
roughly the same relative scale and left position, one pill CTA, mono nav on a dark
topband. The white body diverges deliberately from Sanity's own page (which keeps several
dark feature blocks before dropping to white) and goes straight from the dark hero into
the white 01–05 rhythm, because that split is what contract.md's R4 row specifies
("fullbleed texturfoto + komprimerad rubrik" for the hero, then "01–05 numrerade vita
sektioner" as the whole rest of the page) rather than a literal page-for-page clone of
Sanity's own section order. Within the white section the balance holds: same sticky
mono-numeral rail, same asymmetric two-column rhythm, same use of a real screenshot in
place of an illustration per number. Verdict: the hero's balance matches the source
directly; the body's balance matches the source's *device* (numbered rail + screenshot)
while intentionally shortening the dark-to-white transition per the brief's own
instruction — a deliberate, documented departure, not a miss.

## Fix round (coordinator pixel pass)

No pixel complaint assigned to R4 this round — instruction was "no change unless the
honesty grep hits." Ran the coordinator's grep
(`e-handel|orderflöde|bordsbokning|biljetter|anmälan|system byggt för att växa|meny på
en sida|jag|enskild firma|en person|små företag`) against `index.html`: **0 hits**, so
no copy changes made. Re-verified the existing build stays clean regardless: re-shot
fold + full at 1440×900 (`shots/…--fold.png`, `shots/…--full.png`, overwritten in place,
unchanged content), `scroll_verify.py` still `deadScroll/cuesNeverFull/unrevealed/
contrastUnderMedia/blankBands` all `[]`, `a11y_scan.py` still **0 violations, 33 passes,
1 incomplete**. No edits to `index.html` in this fix round.

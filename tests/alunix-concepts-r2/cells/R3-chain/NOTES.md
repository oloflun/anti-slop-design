# R3 — Insign · tjänsteband — build notes

## Reference lock

Primary reference: `design-catalogue/entries/insign` (fold.webp, shot.webp, all 8 slices,
`extract/insign-se-design-language.md`) — plain white title-page hero with a serif
logotype and a grotesque sentence-case headline, no photo; mosaic collage of client work;
three full-width fully saturated colour-per-service bands, each with one device
photograph; white project archive; dark closing band. Secondary reference:
`design-catalogue/entries/kinhive/fold.webp`, one detail only — a display serif carrying
a headline on its own, without a photo behind it.

Preserve: title-page hero with no media; mosaic strip of real work directly under it;
one non-repeating fully saturated flat colour per service band, acting as navigation;
every other section (hero, archive, footer) plain white or near-black so the bands stay
loudest; each band paired with exactly one small photograph; black ink `#17181B` held
constant across all three bands, matching insign's own AA-verified table rather than
splitting into a second ink system.

Borrow only: the serif-logotype-only role (from kinhive); insign's pill-button shape
(radius 999px, ink border, fills solid on hover).

Reject: insign's own hues taken literally (chartreuse `#ECF58F`, lavender `#D1C8D6`,
coral `#F2895C`); a drawn/fake device bezel; any invented stat, review, rating or logo
row — Anton's correction replaces insign's "5/5 · 130+ omdömen" stats band with the
philosophy line instead.

Media strategy: `photo:vendored` — the three live Alunix demo screenshots, copied from
`C:\Users\Anton L\alunix\public\demos\{calyx,horai,hyperborea}.webp` into `img/`, used in
the mosaic, in each service band's device figure, and in the project archive. No stock
photography, no photos of people as "our team."

## Decision ledger

| Decision | Source | Role | Why |
|---|---|---|---|
| No photo in hero, sentence-case H1 at 76px/400 (Hanken Grotesk) | insign fold.webp + contract.md row R3 | hero device | Anton's correction: match insign's own balance exactly |
| Mosaic strip, 6 tiles, mixed sizes, three demos re-cropped via `transform:scale`+`transform-origin` | insign slices/00.webp collage | proof device | insign's move, rebuilt on Alunix's only real assets (no client logos exist) |
| Three full-width saturated bands = the services | contract.md R3 signature move "färgbanden är tjänsterna" | act shape | binding; colour becomes the service index |
| Band hues: blue from Alunix's own `#1E5E9C`, plum from Calyx's rose, amber from Hyperborea/Hōrai's warm glow | brief.md correction 2026-09-04 | token roles | explicit instruction to reject insign's exact hues |
| Black ink `#17181B` on all three bands | insign extract's accessibility table (18/18 AA pairs, black-ink-dominant) | text-ink role | keeps R3's balance close to source instead of inventing a second ink system |
| Device image = hairline-border `<figure>`, no drawn bezel | design/SKILL.md gate 47 | imagery | "plain device frame" language satisfied without re-drawn chrome |
| Dark close = philosophy line only, no stats/logos/reviews | brief.md "put the three demos or the philosophy instead" | proof format | insign's stats band would require invented numbers; forbidden |
| Reveal easing `cubic-bezier(0.68,-0.55,0.265,1.55)` | insign extract, Motion Language spring/overshoot curve | motion | "insign's springy feel, on reveals only" |
| `<main>` landmark added around hero→archive | a11y_scan.py first pass (landmark-one-main, region) | structure | fixes two moderate violations, zero content change |
| Plum band retuned `#C05C90` → `#C86A9A` | a11y_scan.py first pass (color-contrast, serious) | token value | 4.37:1 on black ink failed the 4.5 floor; retuned to 5.06:1 |

## Fingerprint

chaptered editorial · vit topprad, serif-logotyp · vit yta, grotesk-rubrik, ingen bild ·
mosaik → tre färgband → arkiv · mörkt band med kontakt · färgbanden är tjänsterna.
Shares only "chaptered editorial" (grammar) with R2 — 1 of 6 dimensions, inside the ≤2/6
budget against every other row in `contract.md`.

## Feeling curve

1. **Fold** — calm confidence: white, one claim, one quiet CTA, nothing else competing.
2. **Mosaic** — a quick pulse of proof: real work glimpsed before any pitch is made.
3. **Three bands** — the peak: three hard saturated cuts, one per service, colour
   carrying the argument instead of copy.
4. **Archive** — cooldown: back to white, a plain list, three real links.
5. **Dark close** — resolve: near-black, the promise restated once, one contact line.

Signature move (per contract): the colour bands *are* the services — a visitor can
identify Webbdesign / Design / System by hue alone before reading a word, same device as
insign, rebuilt in Alunix's own three hues.

## Full Swedish copy (as shipped)

**Nav:** Alunix · Tjänster · Projekt · Filosofi · Kontakt

**Fold**
- H1: "Din digitala byrå. Allt på ett ställe."
- Sub: "Vi designar och bygger webbplatser, varumärken och digitala system under ett tak."
- CTA: "Boka ett möte" (mailto:hej@alunix.se) · "hej@alunix.se"

**Webbdesign (blue band)**
- H2: "Webbdesign"
- Body: "Skräddarsydda webbplatser som exponerar ert företag. Webbplatsen är nutidens
  visitkort, byggd för att faktiskt användas."
- Länkar: Skräddarsydd design · Struktur och innehåll · Prestanda och SEO

**Design (plum band)**
- H2: "Design"
- Body: "Varumärke och grafisk form som håller ihop er digitala närvaro, från logotyp
  till knapp."
- Länkar: Varumärke och identitet · Grafisk form · Foto och innehåll

**System (amber band)**
- H2: "System"
- Body: "Utöver webb och design bygger vi egna digitala system, som Alunix OS och ett
  lagersystem för gods och följesedlar. De visar den tekniska höjd vi arbetar på."
- Länkar: Skräddarsydda system · Integrationer · Drift och support

**Utvalda projekt (white archive)**
- H2: "Utvalda projekt"
- Lede: "Tre levande sajter, designade och byggda av oss."
- Calyx — Florist, Stockholm — Besök sajten → https://anti-slop-design.vercel.app/calyx
- Hōrai — Restaurang, Stockholm — Besök sajten → https://anti-slop-design.vercel.app/horai
- Hyperborea — Konferens, Lund — Besök sajten → https://anti-slop-design.vercel.app/hyperborea

**Dark close**
- H2: "Vårt enda mått: perfektion"
- Body: "Vår filosofi är att alla har rätt till bra design. Därför lägger vi oss på en
  nivå som gör våra tjänster tillgängliga för fler, utan att kompromissa med resultatet."
- Contact: "Boka ett möte" (mailto) · "hej@alunix.se"

No invented numbers, reviews, ratings, logos or customer counts anywhere. No em/en
dashes in visible text. No "enskild firma / en person / små företag / jag" — vi-form
throughout.

## Skills invoked, in order

1. `Skill(design)` — SKILL.md Steps 1b, 2b (grammar/feeling curve/signature move/
   fingerprint; bake-off skipped per task instruction), 3, 4, 5.
2. `Skill(copywriting)` — structure and CTA formula for the copy above.
3. `references/design/copy-gate.md` Pass 1b applied by hand (Anton's brief lines counted
   as source 4, already good; the rest sourced from what the trade does and the real
   product names Alunix OS / lagersystem).
4. `Skill(humanizer-svenska)` — full 16-pattern checklist applied to every string;
   negative-parallelism drafts ("X, inte Y") caught and rewritten before shipping
   ("Webbplatsen är nutidens visitkort, byggd för att faktiskt användas" instead of a
   "not the brochure" construction).
5. `Skill(design-verify)` procedure followed manually via the scripts below (a11y-audit
   skill's own scripts + design skill's scroll_verify.py).

## Verification numbers

- **shoot.py** (1440×900, full page 3888px): two passes. First pass found the mosaic
  tiles repeating near-identical crops of the same three source images (aspect-ratio
  mismatch made `object-position` alone ineffective) and the logotype rendering with a
  default anchor underline; both fixed (mosaic tiles rebuilt with `transform:scale` +
  `transform-origin` inside `overflow:hidden` wrappers; `text-decoration:none` added to
  `.logotype`). Third pass clean.
- **Mobile sweep** (320 / 375 / 414 / 768, ad hoc Playwright script since `shoot.py` is
  desktop-only): `overflowX = 0` at all four widths. Nav initially disappeared below
  700px with no substitute; fixed by letting the nav row wrap instead of hiding the
  links, so all four links stay reachable at every width.
- **a11y_scan.py**: first pass — 2 moderate (`landmark-one-main`, `region`, from having
  no `<main>`) + 1 serious (`color-contrast` on the plum band, 4.37:1 against the 4.5
  floor). Both fixed (added `<main>` around hero→archive; retuned plum `#C05C90` →
  `#C86A9A`, now 5.06:1). Second pass: **0 violations, 38 passes, 0 incomplete.**
- **scroll_verify.py**: `deadScroll: []`, `cuesNeverFull: []`, `unrevealed: []`,
  `contrastUnderMedia: []`, `blankBands: []` — **0 / 0 / 0**, clean.
- **Manual contrast check** (black ink `#17181B` on each band, WCAG formula): blue
  `#6E8CF2` → 5.66:1, plum `#C86A9A` → 5.06:1, amber `#E7A53A` → 8.32:1. All clear the
  4.5:1 body-text floor.
- Line count: 344 lines (budget ≤440).
- The bounce-easing detector correctly flagged `cubic-bezier(0.68,-0.55,0.265,1.55)` on
  the reveal — this is intentional and sourced: it is insign's own measured
  spring/overshoot easing token from `extract/insign-se-design-language.md`, applied
  only to reveals per the task's explicit instruction, not an unsourced AI default.

## Balance vs. source

`shots/vs-source.png` places insign's own `shot.webp` beside this build's full-page
capture at matched width. The proportions match: same nav height and serif-logotype
placement, same hero air-to-type ratio with no photo, the same mosaic-strip-directly-
under-hero move, the same three-hard-cut saturated band rhythm with a device photo and
link list in each, the same return to white for the project list, the same dark closing
band. The build is shorter than insign's page because the brief explicitly forbids the
sections that would require invented content (star rating, omdömen count, team
headshots, dated news strip) — that is a deliberate compression the brief licensed, not
a balance miss. Judged on the sections both pages share, R3 reads as insign's own
weight class: same confidence, same restraint outside the colour bands, same colour-does-
the-talking move, in Alunix's own hues.

## Fix round (coordinator pixel pass)

Complaint: the mosaic strip repeated the same Hōrai crop twice and showed chopped
letters (e.g. only "AI" visible instead of "HORAI").

- Root cause: each `.mtile img` used `transform:scale(N);transform-origin:X% Y%` with
  origin points chosen without checking where each demo's headline actually sits in the
  1200×750 source. `transform-origin` percentages are relative to the *already
  object-fit:cover-cropped* rendered box, not the raw source image, so hand-picked
  origins landed inside text on multiple tiles regardless of which of the three demos
  was used — the six crops read as near-duplicates because most origin points fell
  close to each image's dominant headline, which dominates the frame at any reasonable
  zoom.
- Fix approach: mapped each source image's text bounding boxes precisely first (a
  scratch script overlaid a 100px pixel grid on all three `img/*.webp` files and the
  boxes were read off directly — headline/subhead/caption/nav regions for each of
  Calyx, Hōrai, Hyperborea), then picked six crop windows in true source-pixel space:
  one "hero" tile per demo that shows its full headline uncropped (`m1`/`m2`/`m3`, kept
  as simple `object-position` on an `<img>`, no zoom — at these tiles' aspect ratios
  `object-fit:cover` already shows the whole headline with no cut), and one "detail"
  tile per demo picked from a verified text-free region only (`m4` Hōrai's wine-glass/
  table blur, `m5` Calyx's leaf-and-berry texture, `m6` Hyperborea's amber glow) —
  converted those three from `<img>+transform:scale` to a `background-image` on the
  `.mtile` div with computed `background-size`/`background-position`, because the
  background-position percentage formula (`offset = (containerSize − bgSize) ×
  percent/100`) is exactly solvable for "make source window [x0,x1]×[y0,y1] fill this
  box", unlike the compounded object-fit-then-transform math that produced the original
  bug. Numbers were computed by hand from each window's pixel bounds and the tile's
  measured CSS box (`~402×264` for the tall tiles, `~402×176` for the wide-short ones),
  then verified empirically: two earlier attempts (plain `object-position`, then
  `transform:scale` with hand-guessed origins) still clipped text and were caught by
  re-shooting and cropping the mosaic region out of the full-page PNG before landing on
  the background-image numbers below.
- Final values: `m4{background-size:240% auto;background-position:100% 16.5%}`,
  `m5{background-size:366% auto;background-position:15.6% 14%}`,
  `m6{background-size:400% auto;background-position:100% 84%}`.
- Re-shot fold + full at 1440×900 (`shots/…--fold.png`, `shots/…--full.png`, overwritten
  in place) and cropped the mosaic band out of the full PNG for close inspection: all
  six tiles distinct, zero repeated crops, zero chopped headline fragments — three show
  each demo's full wordmark/headline, three show pure texture/detail with no text at
  all, matching insign's own collage (a mix of hero moments and plain material close-
  ups, not six near-identical text zooms).
- `scroll_verify.py`: unchanged clean result (`deadScroll/cuesNeverFull/unrevealed/
  contrastUnderMedia/blankBands` all `[]`).
- `a11y_scan.py`: **0 violations, 38 passes, 0 incomplete** (same as before the fix —
  the mosaic images are decorative `alt=""`/backgroundless-`alt`, and the parent
  `.mosaic` already carries `role="img"` with a descriptive `aria-label` covering all
  six tiles, unchanged by this edit).
- Honesty grep (`e-handel|orderflöde|bordsbokning|biljetter|anmälan|system byggt för att
  växa|meny på en sida|jag|enskild firma|en person|små företag`): 0 hits, before and
  after — R3's copy was already clean.

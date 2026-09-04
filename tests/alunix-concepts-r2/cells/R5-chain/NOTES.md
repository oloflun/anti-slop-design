# R5 · Mattis · konsol — build notes

Concept for Alunix, contract row R5 (`../../contract.md`). Dominant source: `design-catalogue/entries/mattis-studio` (fold.webp, shot.webp, all 12 slices, extract design-language.md). Secondary: `design-catalogue/entries/studioagriculture/fold.webp` (wordmark-at-viewport-width scale only).

File: `index.html`, 315 lines (limit 440).

## Reference lock + decision ledger

Full block lives as an HTML comment at the top of `index.html` (Step 1b, binding). Condensed here:

- **Primary reference:** Mattis Studio — versioned software-console hero card, breaking into one flat-colour thesis block with black-and-white photography, closing on plain oversized display type ("WE BUILD WEBSITES").
- **Preserve (balance, per contract row R5):** hero framed as a bordered, corner-marked console card carrying a tag line and a live clock; wordmark large inside that card with a small caps sub-line; one full-bleed saturated-colour section for a short caps thesis; black-and-white photography wherever it meets that saturated block; a white closing block with a giant "WE BUILD WEBSITES"-scale headline.
- **Borrow only:** the corner-mark motif, generalised into a page-wide fixed device (follows scroll) instead of repeating on the card alone — this is the literal fingerprint requirement ("hörnmarkeringarna följer med i skroll").
- **Secondary reference:** studioagriculture/fold.webp, for the edge-to-edge oversized-wordmark scale of "VI BYGGER WEBBPLATSER." only, not its palette.
- **Rejected:** Mattis's founder photo + signature overlay (a personal image the brief forbids); the "slots left this month" scarcity counter (fabricated availability Alunix cannot verify); a fake version number ("VERSION 1.0.4") — replaced with the one true console fact, the current year, plus a live clock and "SVERIGE"; orange as the saturated block (contract requires Alunix blue or a deep green).
- **Token commitments:** `--c-black #0b0c0e` (console ground), `--c-white #fff`, `--c-paper #f4f2ee` (close-block ground, warm off-white), `--c-ink #14171a`, `--c-accent #1e5e9c` (Alunix blue — the one saturated block, CTA underline, focus ring), `--c-accent-deep #123f68`. Geist 700 for all display type, Geist 400 body, Geist Mono for every tag/kicker/number only (register, never voice, per TASTE §4 rule 2).
- Decision ledger (source → role → why) for every major visual choice is the table in the HTML comment; it covers the console card, the fixed corner marks, the wordmark/service-row content, the blue accent choice, the thesis layout, the giant close headline, the ledger-not-cards services, the honest-proof project plates, and the truthful console tags.

## Fingerprint row (contract.md table)

| grammar | nav | hero-device | aktform | avslut | signature move |
|---|---|---|---|---|---|
| split stage | console frame with tag/clock (no separate nav bar — the console *is* the nav) | wordmark in console frame over grayscale photo | black → saturated block → white | white block with giant headline | corner marks follow the scroll (fixed to viewport) |

Matches contract.md's R5 row exactly; shares ≤2/6 dimensions with every other row (R1–R4, R6 all use a top nav bar or pill-flikar, none use a console-frame hero-device or fixed corner marks).

## Feeling curve (Step 2b)

1. **Console hero (black).** Curiosity, then precision. The agency's own homepage framed like a piece of versioned software — a bordered card, a live clock ticking, a tag stating the year and country — before a single word of sales copy. The photo (a real desk, grayscale, darkened) sits behind as atmosphere, never staged as "our office."
2. **Thesis block (Alunix blue).** Conviction. One flat, saturated colour, one short caps claim ("Det första intrycket är digitalt.") stated as fact, one black-and-white project photo as the only supporting evidence. No stat, no count — TASTE §4 rule 4 ("ett papper, en accent, och accenten gör en sak") kept literally: the accent is Alunix blue and its only job here is to carry the thesis.
3. **White close.** Resolution. A giant plain headline ("Vi bygger webbplatser.") at the scale of the source's own close, then the concrete: a services ledger, three real projects with real links, the philosophy quote from Anton's own line, and a plain mailto. The register drops from declaration to conversation on purpose — the loudest moment already happened in act 2.

**Peak:** act 2, the blue block — largest colour-to-content contrast on the page, per house-physics "exactly one saturated accent deployed at display scale."

**Signature move:** four small corner marks (`position:fixed`, `mix-blend-mode:difference`) sit at the viewport's four corners through the entire scroll — they never move relative to the window, which is the literal read of "hörnmarkeringarna följer med i skroll." `mix-blend-mode:difference` keeps them legible against the black hero, the blue block and the white close without three separate colour rules.

## Copy (final, Swedish)

Console tag: `2026 · SVERIGE` (live year) · `HH:MM:SS · LOKAL TID` (live clock, JS-driven, ticks every second, freezes under `prefers-reduced-motion: reduce`).

**Hero**
- Wordmark: ALUNIX / Digital byrå
- Body: "Din digitala byrå, allt på ett ställe. Vi designar och bygger skräddarsydda webbplatser som exponerar ert företag."
- Service row: Design · Utveckling · System
- CTA: "Boka ett möte →" (mailto:hej@alunix.se)

**Thesis (blue)**
- Kicker: Varför design
- Headline: "Det första intrycket är digitalt."
- Support: "Ett företag väljs bort eller väljs in på några sekunder, långt innan någon hunnit läsa en rad text. Det är rubriken och bilden som avgör, inte innehållet."
- Photo caption: "Ett av tre projekt vi har byggt"

**Close (white)**
- Giant headline: "Vi bygger webbplatser."
- Sub: "Skräddarsydda lösningar för ert företag, från första skiss till lansering."
- Ledger:
  - 01 Design — "Varumärke och grafisk form, så att sajten ser ut som företaget bakom den."
  - 02 Utveckling — "Skräddarsydda webbplatser, byggda för att exponera verksamheten rätt."
  - 03 System — "Egna digitala system, som Alunix OS, för företag som behöver mer än en webbplats."
- Kicker: Utvalda projekt — Calyx (Florist · Stockholm, anti-slop-design.vercel.app/calyx), Hōrai (Restaurang · Stockholm, .../horai), Hyperborea (Konferens · Lund, .../hyperborea)
- Kicker: Filosofi — "Vår filosofi är att alla har rätt till bra design. Därför har vi valt att lägga oss på en nivå som gör våra tjänster tillgängliga för fler, utan att kompromissa med resultatet." Byline: "Vårt enda mått: perfektion."
- Kicker: Kontakt — hej@alunix.se (mailto) · "Sverige" · "© 2026 Alunix"

No invented counts, testimonials, logos, or prices anywhere. Only true numbers on the page: the current year and the live clock, both computed client-side, never hardcoded.

## Skill calls, in order

1. `Skill(design)` — read SKILL.md, followed Steps 1b / 2b (grammar + feeling curve only, bake-off skipped per task instruction, R5 row is fixed) / 3 / 4 / 5.
2. `Skill(copywriting)` — structure and voice for the Swedish copy above, CONTENT FUNDAMENTALS = digital byrå / vi-form / Insign-nivå per task instruction.
3. Read `references/copy-gate.md` Pass 1b by hand (radkälla check: Anton's brief lines count as source 4 and were used near-verbatim for the philosophy quote; every other line traced to what the trade does or what the source's device required).
4. `Skill(humanizer-svenska)` — applied by hand against the pattern list (no "inte bara X — det är Y", no tricolons joined by "och", no "sömlöst"/"unik upplevelse"/"i hjärtat av", no lede restating the headline, no em-dashes; kept the register confident and short per brief, did not sand it toward neutral).

## Verification

- `shoot.py` → `shots/…--fold.png`, `shots/…--full.png` (4226px), both read as images.
- `scroll_verify.py` → `deadScroll: []`, `cuesNeverFull: []`, `unrevealed: []`, `contrastUnderMedia: []`, `blankBands: []`. Clean on first run.
- `a11y_scan.py` → `violations: []`, `passes: 32`, `incomplete: 1` (no serious/critical; nothing waived).
- `contrast_over_media.py` on the hero → **worst 20.28:1, mean 17.82:1** at the brightest frame among the sampled scroll positions, measured against the console-card's own scrim plate under "ALUNIX" — well clear of AA.
- Mobile overflow swept at 320 / 375 / 414 / 768 px via Playwright (`scrollWidth - clientWidth`): **0px overflow at all four**. Screenshots read at 320 (fold + full) and 768 (full): project grid collapses to one column under 820px, thesis grid stacks with the photo promoted above the text, wordmark and giant headline wrap via `overflow-wrap:anywhere` without breaking layout.
- Reduced motion (Playwright `reduced_motion="reduce"`): clock text identical before/after a 2.2s wait (frozen, not blank), all `.reveal` elements at `opacity:1` immediately (content kept, only the travel removed).
- JavaScript disabled (Playwright `java_script_enabled=False`): `<html>` keeps class `no-js`, every `.reveal` element still renders at `opacity:1` (CSS default state), console clock shows its static placeholder text rather than blank.
- `wc -l index.html` → 315 (limit 440).

## Balance vs. source

`shots/vs-source.png` is a side-by-side of Mattis's `shot.webp` (left) against this page's full-page capture (right), both scaled to the same width. The first three acts read as the same instrument: a centred, bordered console card on a dark photographic ground with a tag/clock row above a large wordmark and a small caps line below it, cutting hard into one full-bleed saturated block carrying a short caps thesis beside a single photograph, cutting again into a light ground with a giant edge-to-edge headline at the same relative scale. The proportions between hero-card-to-viewport, thesis-block height, and the giant headline's type size versus body copy all land within the source's own ratios. Where the two diverge on purpose: Mattis continues for another eight sections (testimonials, pricing, news) that this concept's brief does not call for, and its palette is black/orange/grey where this page is black/Alunix-blue/off-white per the contract's binding "not orange" rule — the balance is borrowed, the palette and copy are the agency's own. **The visual balance matches the source.**

## Fix round (coordinator pixel pass)

Complaint: the photo in the blue thesis block cropped Hyperborea's headline down to
"ystems" / "ith warmth" — the left edge of every line was cut off.

- Root cause: `.thesis-photo img` was set to `aspect-ratio:4/5` (a tall portrait box)
  while the vendored screenshot (`assets/demo-hyperborea.webp`) is 1200×750, i.e. 16:10
  landscape. `object-fit:cover` on a portrait box built from a landscape source has to
  crop most of the width to fill the height, and with no `object-position` set (default
  centre), that crop cut symmetrically into both the left edge of "Systems"/"with" and
  the right edge of "warmth."
- Fix: changed `.thesis-photo img{aspect-ratio:4/5}` to `aspect-ratio:16/10}`, matching
  the screenshot's true ratio exactly, so `object-fit:cover` shows the complete image
  with zero crop — same fix pattern as R1/R2's demo frames. `filter:grayscale(1)
  contrast(1.05)` untouched, so the photo stays black-and-white as the reference lock
  requires. The box is now shorter relative to its width than before (16:10 vs 4:5), but
  the grid (`align-items:end`, two columns) absorbs that fine — re-shot and confirmed
  the thesis block still balances against the text column at 1440px.
- Re-shot fold + full at 1440×900 (`shots/…--fold.png`, `shots/…--full.png`, overwritten
  in place); cropped the thesis block out of the full PNG for a close look — "Systems
  with warmth 温度のある機械" reads completely, no clipped glyphs on either edge, still
  fully desaturated.
- `scroll_verify.py`: unchanged clean result (`deadScroll/cuesNeverFull/unrevealed/
  contrastUnderMedia/blankBands` all `[]`). `a11y_scan.py`: **0 violations, 32 passes,
  1 incomplete** (same incomplete check as before the fix, not new).
- Honesty grep (`e-handel|orderflöde|bordsbokning|biljetter|anmälan|system byggt för att
  växa|meny på en sida|jag|enskild firma|en person|små företag`): 0 hits, before and
  after — R5's copy was already clean. (Noted but out of scope: the "Utvalda projekt"
  cards further down this same page crop the Calyx/Hōrai headlines the same way R1/R2
  did before their fixes — not part of this round's assigned R5 fix, which was scoped
  to the thesis-block photo only.)

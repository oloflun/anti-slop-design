# R2 — Squarespace · band (2026-09-04)

## Reference lock

```
Primary reference/direction: Squarespace "Grow your business" band (pill filter
tabs over a dark feature-card row) plus its black stat band and Clarkson
weight-300 display type — design-catalogue/entries/squarespace (fold.webp,
shot.webp, shot-2.webp, slices/00-08).
Preserve: white hero band with a left-aligned weight-300 display headline; a row
of 100px-radius pill tabs directly under the headline that address the content
below; a row of dark, image-bearing cards each closing on a small arrow link;
one pure-black band carrying a single display sentence as the page's one tonal
inversion; radius split by role (0px rectangles, 100px pills only); zero
chromatic colour in the UI shell.
Borrow only: Aarke's thin 1px ghost-button border and left-aligned proportions
(design-catalogue/entries/aarke/fold.webp).
Role rules: pill radius (100px) never applies to a button or card; the
achromatic shell never gets a chromatic fill; colour is licensed only inside
the three vendored demo screenshots, exactly as Squarespace licenses colour
only inside customer-site previews.
Media strategy: product surface — three vendored screenshots of Alunix's own
delivered demos (Calyx, Hōrai, Hyperborea), never stock, never hotlinked.
Reject: Squarespace's literal palette (#000/#fff/#2f2f2f/#898989/#dddddd/
#999999) copied verbatim; a fullbleed photographic hero (R1's move, not R2's);
card drop shadows; gradient pills; any chromatic accent added to the UI chrome.
Token commitments: bg #ffffff / #0e0e0e; ink #121212; muted-on-light #595959;
muted-on-dark #b3b3b3; border-on-light #d8d8d8; border-on-dark #2c2c2c;
display Figtree 300 at 40-72px / leading 0.95 / -0.05em tracking; body Figtree
400 15-16px; radius 0px buttons and cards, 100px pills exclusively; section
gap 56-96px (own rhythm, not Squarespace's raw pixel gaps).
```

## Decision ledger

| Decision | Source | Role | Why |
|---|---|---|---|
| White hero, left-aligned 72px/300 headline, no image | squarespace slices/01,02.webp ("Grow your business") | layout: type-carries hero | R1 already owns the fullbleed-photo hero; R2 is the calmer second reading Anton asked for |
| Pill row under headline, anchor-linked to the three cards | squarespace slices/01.webp (Services/Online Store/Invoicing tabs) | nav role: content filter, not decoration | Contract signature move: "pill-flikarna byter vilken sajt som visas" |
| Dark cards, screenshot top / text+arrow bottom | squarespace slices/02,03.webp (Website Editing / Design Intelligence cards) | proof role: utvalda projekt | Brief's only sanctioned proof is the three demos; dark-card grammar is the source's own device for showing product |
| One pure-black band, one centred sentence | squarespace slices/05.webp (14M+/$36B+ stat band), compressed to a single sentence | tonal inversion, philosophy line | House-physics: one inversion per page; brief's "vårt enda mått: perfektion" fits a single display sentence |
| Three text columns, hairline-separated, no icons | contract R2 row + TASTE.md §1/§3 | tjänster: Webbdesign/Design/System | Explicit brief requirement; TASTE rejects icon-grids and filler cards |
| Ghost buttons, 0px radius; pills 100px only | aarke/fold.webp "Shop now" outline button + squarespace radius-by-role rule | button role: CTA only | Contract: "ghost-knappar överallt"; TASTE §5 "rundning är ett beslut" |
| Own gray family, not Squarespace's literal hex | contract.md | token role: achromatic shell | "palett tas inte ordagrant" — balance borrowed, palette is Alunix's own |

Tier: **2 — reference.** Every token traces to the squarespace/aarke catalogue entries or to contract.md's explicit R2 row; nothing invented outside those.

## Fingerprint row

grammar **chaptered editorial** · nav **white top bar, pill filter row under the hero** ·
hero device **white type-only band, left-aligned 300-weight headline, no photograph** ·
act shape **white hero → dark cards → black inversion → white columns → quiet contact** ·
close **quiet white contact block, no colophon** · signature move **pill tabs anchor-scroll
to and CSS `:target`-highlight the matching demo card, working with zero JavaScript**.

Checked against R1 (same source, contract.md row): different hero device (R1 fullbleed
photo + centred rubrik + floating site frames vs. R2 white type-only band, left-aligned),
different nav (R1 dark top bar vs. R2 white top bar + pills), different act shape
(R1 rhythmic black/white band alternation vs. R2 white/dark-cards/black/white), different
signature move. Shares only: source (squarespace) and register (modern clean). 2/6 — inside
the ≤2/6 budget the contract sets for R1/R2.

## Feeling curve

1. **Fold** — calm confidence. A left-aligned, unhurried 72px headline on plain white; no
   photo competing for attention. The pill row invites a click before any commitment is asked.
2. **Utvalda projekt** — proof, at last colour. The page has been strictly achromatic; the
   three screenshots (botanical pinks, restaurant warmth, Hyperborea's amber sun) land as
   the one legitimate burst of colour, because they are the actual product.
3. **Vårt enda mått är perfektion** — the peak. One sentence, full black, centred, the
   page's only tonal inversion. Largest contrast swing on the page by design.
4. **Tjänster** — back to white, unhurried, three equal columns that each carry real
   weight (a full paragraph, not a whispered caption).
5. **Kontakt** — quiet close on a soft gray wash, one visible mailto, no form, no colophon.

Signature move: the pill tabs are real anchor links (`href="#calyx"` etc.), so clicking one
works with JavaScript fully disabled — native browser scroll plus a CSS `:target` outline
ring on the matching card. JS only adds the shared reveal-on-scroll; verified by disabling
JavaScript in Playwright (see Verification).

## Copy (final, Swedish)

**Nav:** Alunix · Tjänster · Projekt · Kontakt · Boka ett möte (mailto)

**Fold:**
- H1: "Din digitala byrå, allt på ett ställe."
- Sub: "Vi bygger skräddarsydda webbplatser, varumärken och digitala system som exponerar ert företag."
- Pills: Calyx · Hōrai · Hyperborea
- CTA: "Boka ett möte" → mailto:hej@alunix.se

**Utvalda projekt:**
- Calyx — Florist · Stockholm — "En sajt där bilderna får bära hela sidan." — Se sajten → (anti-slop-design.vercel.app/calyx)
- Hōrai — Restaurang · Stockholm — "Bordsbokning och meny på en sida där maten får synas." — Se sajten → (/horai)
- Hyperborea — Konferens · Lund — "Program, talare och biljetter i ett system byggt för att växa varje år." — Se sajten → (/hyperborea)

**Filosofi (svart band):** "Vårt enda mått är perfektion."

**Tjänster:**
- Intro: "Vi tror att alla har rätt till bra design. Därför lägger vi oss på en nivå som gör våra tjänster tillgängliga för fler, utan att kompromissa med resultatet."
- Webbdesign: "Skräddarsydda webbplatser som exponerar ert företag och gör det enkelt för besökare att hitta rätt. Vi utgår från hur ni faktiskt arbetar, inte från en mall."
- Design: "Varumärke och grafisk form som gör att sajten ser ut som företaget bakom den. Typsnitt, färg och bildspråk hänger ihop, från logotyp till knapp."
- System: "Vi bygger också egna digitala system, som Alunix OS och ett lagersystem. Det visar att vi klarar mer än sajter, om ert företag behöver det."

**Kontakt:**
- "Er webbplats är nutidens visitkort."
- "Hör av er, så pratar vi om er sajt."
- hej@alunix.se (mailto) · "Skriv till oss" (mailto)
- Foot line: "Alunix, digital byrå."

No invented numbers, testimonials, logos, or customer names beyond the three sanctioned
demos. No em/en dashes anywhere visible (checked by eye across every string above). No
"enskild firma / en person / jag" language; every line is vi-form.

## Skill(...) calls, in order

1. `Skill(design)` — front door, Steps 1b/2b/3/4/5 per the assignment (bake-off explicitly skipped, per contract row already fixing R2's direction).
2. `Skill(copywriting)` — structure and CONTENT FUNDAMENTALS applied (digital byrå, vi-form, self-assured, short, Insign-level; Anton's four sanctioned lines used as source 4 per copy-gate Pass 1b).
3. Read `references/copy-gate.md` Pass 1b — every headline/lead traced to a source: brief's sanctioned lines (H1, filosofi, black band), the demo's own facts (project descriptions), or the brief's service list (tjänster columns). No invented proof.
4. `Skill(humanizer-svenska)` — full pattern sweep against every string above: no signifikansuppblåsning, no landskapsuppramning, no particip-flex, no vaga attributioner, no nominalisering, no anglicism, no "inte X, det är Y" negativ parallellism, no sycophancy, no bullet/emoji formatting. Register kept confident and Insign-level, not sanded neutral (kept "Vårt enda mått är perfektion" and the filosofi line at near-full strength, as the brief explicitly sanctions).

## Verification

- **Lines:** 350 (budget ≤420).
- **shoot.py:** fold + full captured and read as images (`shots/…--fold.png`, `…--full.png`). Balance confirmed by eye: white hero → dark card row → black inversion → white columns → gray-wash contact, echoing the source's band alternation.
- **scroll_verify.py:** `deadScroll: []`, `cuesNeverFull: []`, `unrevealed: []`, `contrastUnderMedia: []`, `blankBands: []` — clean 0/0/0 (plus 0 blank bands) after tightening the hero-to-projects gap (was doubling to ~280px from two adjacent `padding-block` values; fixed to asymmetric hero padding + a smaller `--gap-section`).
- **a11y_scan.py:** `violations: []`, `passes: 32`, `incomplete: 1`.
- **tab_walk.py:** 15 stops, every one with a visible focus indicator, correct order, nothing offscreen, `issues: []`.
- **reflow.py:** `overflow320: []`, `overflowZoom200: []`, `hiddenUnderReducedMotion: 0`.
- **detect.mjs:** `[]` — zero mechanical findings.
- **Mobile sweep (custom Playwright, 320/375/414/768):** zero horizontal overflow at every width; zero interactive elements under the 44px touch-target floor (fixed two misses — the wordmark link and the nav text links were under 44px tall before an explicit `min-height:44px` was added).
- **JS-disabled check:** with `javascript_enabled=False`, all three `.proj-card` elements report `display:block, opacity:1` at full size (the reveal system's CSS fails toward visible with no JS running), and clicking a pill navigates the URL to `#hyperborea` via native anchor behaviour alone — the pill filter works with JavaScript off, as required.
- **contrast.py:** not usable as-is — the script hardcodes `http://localhost:3055/` rather than taking the CLI URL argument, and that port was serving a different, unrelated concurrent build in this session (cream palette, "ALUNIX" wordmark at 192px, "Tre sajter, i drift.") — not this file. Relied instead on `a11y_scan.py`'s axe color-contrast rule (0 violations) and manual computation: muted-on-light `#595959` on `#ffffff` ≈ 7.3:1, muted-on-dark `#b3b3b3` on `#171717`/`#0e0e0e` ≈ 8:1, both well above the 4.5:1 floor.
- **vs-source.png:** `shots/vs-source.png`, full source page (design-catalogue/entries/squarespace/shot.png) beside the full built page, same scaled height.

## Balance vs. source

**Yes, the band rhythm matches at the macro level Anton asked for.** Both pages open on a
band, drop into a component row (Squarespace's dark feature cards / Alunix's dark project
cards), hit one full-width tonal inversion, and close quiet. The proportions the contract
named were followed directly: pill filter row sized and radiused like the source's
Services/Online Store tabs, dark cards with a bottom-right arrow link matching the source's
card grammar almost exactly, and the black band compressed to Squarespace's "one sentence at
scale" move rather than its literal three-stat layout (there is nothing honest to put in
three stats, so one sentence was the correct read of "en enda sats i skala"). The one
deliberate divergence from the source's own fold — a photographic hero — is intentional and
stated in the brief: R1 already owns that move, and R2 is named as "the second reading,"
the white-band-plus-pills part of Squarespace's page rather than its top-of-page hero.

## Fix round (coordinator pixel pass)

Two complaints on the dark project-card row (`#projekt`):

1. **Cropped headlines.** `.proj-media` was `aspect-ratio:4/3` (1.33) against the demo
   screenshots' true 1200×750 ratio (1.6, i.e. 16:10). `object-fit:cover` was forced to
   crop ~17% off one edge of every screenshot, which sliced the headline in the Calyx and
   Hyperborea captures ("otanical"/"hitecture" was visible instead of the full
   "Botanical architecture" and "Systems with warmth"). Fixed by changing
   `.proj-media{aspect-ratio:4/3}` to `aspect-ratio:16/10}`, matching the screenshots'
   native ratio exactly — `object-fit:cover` now displays the full image with zero crop
   (kept `cover` rather than switching to `contain`, since a matching ratio makes them
   equivalent and `cover` avoids letterboxing bars on the dark card).
2. **Shared/invented copy.** The Calyx card's description ("En sajt där bilderna får bära
   hela sidan.") was actually Hōrai's fact ("fotografiet bär hela sidan," per brief.md),
   duplicated onto the wrong project. Hōrai's own line ("Bordsbokning och meny på en sida
   där maten får synas.") and Hyperborea's ("Program, talare och biljetter i ett system
   byggt för att växa varje år.") both invented scope the brief explicitly forbids
   (table booking, tickets, "a system built to grow") — flagged by the coordinator's
   honesty grep. Rewrote all three to each carry only that project's own allowed fact:
   - Calyx → "Kursiv och rak typografi i samma rad, på krämvitt papper." (the brief's
     "kursiv och rak i samma rad" / cream paper facts)
   - Hōrai → "Fotografiet får bära hela sidan." (the brief's own line for Hōrai)
   - Hyperborea → "Ett ritat solmotiv i åtta varianter, byggt i kod." (the brief's "ett
     ritat solmotiv i åtta varianter" / code-drawn SVG fact)

Re-shot fold + full at 1440×900 (`shots/…--fold.png`, `shots/…--full.png`, overwritten in
place): all three headlines ("Botanical architecture, from Stockholm", "HŌRAI", "Systems
with warmth") fully visible inside their cards, each card now carries its own fact.
`scroll_verify.py`: unchanged clean result (`deadScroll/cuesNeverFull/unrevealed/
contrastUnderMedia/blankBands` all `[]`). `a11y_scan.py`: **0 violations, 32 passes**
(up from 29 passes pre-fix — the taller card body pushed nothing out of contrast range).
Honesty grep (`e-handel|orderflöde|bordsbokning|biljetter|anmälan|system byggt för att
växa|meny på en sida|jag|enskild firma|en person|små företag`) re-run after the edit: 0
hits.

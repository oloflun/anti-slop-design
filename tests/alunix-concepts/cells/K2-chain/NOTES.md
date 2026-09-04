# K2 "Tjänsteledger" — build notes

Concept row: K2, `tests/alunix-concepts/contract.md`. Brief: `tests/alunix-concepts/brief.md`.
Build: `tests/alunix-concepts/cells/K2-chain/index.html` (389 lines, single file, inline CSS/JS,
Google Fonts only).

## Reference lock + decision ledger (also inlined as an HTML comment at the top of index.html)

**Tier: 2 — reference.** No `DESIGN.md`, no Alunix brand-hex evidence usable (the current site's
"instrument" register is explicitly reserved for K3, not K2), so direction comes from the
contract's assigned catalog entries.

**Primary reference/direction:** insign — one fully saturated, non-repeating flat colour
assigned to each category, functioning as navigation by colour; plain white/black framing
around every saturated section.

**Preserve (3–5 traits):**
- One saturated flat colour sheet per chapter, non-repeating.
- Hero and close stay plain (white / near-black) so the three chapters stay the loudest part
  of the page.
- Each coloured sheet carries exactly one small, specific screenshot, never an abstract icon.
- The palette itself differentiates the chapters (colour as navigation/memory).

**Borrow only (1–2, secondary references):**
- From **mattis-studio**: the bordered, corner-marked "inspected component" framing — reduced
  to a hairline keyline offset around each screenshot. Explicitly *not* borrowed: the version
  tag, live clock, or "slots left" counter (fabricated-scarcity devices, forbidden by the
  brief's ban on invented numbers).
- From **kinhive**: the idea of a colour value continuously tied to scroll — reduced to each
  chapter's own panel deepening with local scroll progress. Explicitly *not* borrowed: the
  marquee band, the photo-layered signup card, or the italic-serif emphasis word (K2's register
  is grotesque sans, not serif, and the brief has no people photography to layer under a card).

**Role rules:** no two adjacent chapters share a colour family; saturated colour never appears
in the hero, "hur det går till", or the close band; each chapter panel carries exactly one
screenshot.

**Media strategy:** product surface — the three real demo screenshots, vendored from
`~/alunix/public/demos/` into `cells/K2-chain/demos/`, never hotlinked. No stock photography,
no other imagery anywhere on the page.

**Reject:**
- insign's own three full-width stacked bands — K2's contract explicitly forbids this
  structure; the build uses a two-column split stage per chapter instead.
- Any full-bleed atmospheric photograph (forbidden by contract).
- K1's achromatic black/white register (forbidden by contract; K2 is the saturated-block row).
- Mattis's scarcity counter and live clock (fabricated data, forbidden by brief).
- Kinhive's photo-layered card and italic-serif emphasis (no photography of people exists in
  this brief; register mismatch).

**Token commitments:** paper `#fbfaf7` / ink `#1a1815`; chapter colours drawn honestly from
each demo's own real accent — Calyx rust `#a34827`→`#7a3319`, Hōrai lacquer red `#7a1414`→
`#530c0c`, Hyperborea amber `#e8b04a`→`#c98f2c` — at full saturation, deployed at display
scale (the entire chapter panel), never as fill on a small control. Fonts: Bricolage Grotesque
(display, 600/800) + Geist (body, 400/500) + JetBrains Mono (one role only: the "meta/data"
register — screenshot captions, the price/delivery placeholders, and the close-band system
stats — never a third body font).

| Decision | Source | Role | Why |
|---|---|---|---|
| Split stage, not stacked band | contract.md K2 row | act shape | insign's own structure is explicitly forbidden for K2 |
| Chapter colour = each demo's real accent | brief.md demo descriptions | identity colour, display-scale only | Honest (no invented palette) and doubles as "samma händer" proof |
| Corner-tick screenshot frame | mattis-studio (borrow-only) | decorative only | One licensed detail, not the whole metadata hero-card |
| Panel deepens with local scroll progress | kinhive (borrow-only, reduced) | signature move | Fulfils "kapitelfärgen skroll-länkad" without the marquee/photo-card apparatus |
| No button filled with a chapter colour | color.md + house-physics | accent role: display only | Accent never on small controls |
| CTA = solid ink button | insign's own black "Visa alla tjänster" pill, observed in fold.webp | CTA-only | Matches the primary reference's own restrained CTA logic |
| Reused client line as hero question | brief.md §Röst, explicitly licensed for one concept | headline | Sourced, not invented; fits the "en fråga per kapitel" voice rule |

## Fingerprint row built

| Build | Grammar | Nav | Hero device | Act-sequence shape | Close pattern | Signature move | Register | World |
|---|---|---|---|---|---|---|---|---|
| K2-chain | split stage | vänsterrail, sticky (top bar on mobile) | vit yta, grotesk-rubrik, inget foto | fast vänstertext, högerkolumn byter färg per kapitel (3 chapters) | mörkt band (hej@alunix.se, systemtextur, tre färgprickar) | kapitelfärgen fördjupas med lokalt skrollframsteg (`color-mix`, `--p` custom property) | modern clean, mättade block | Tryckt tjänsteledger i dagsljus |

Checked against every forbidden item in the K2 contract row: no three stacked bands, no
full-bleed photo, no K1 black/white. Checked against the other five rows' fingerprints: K2's
own act shape (fixed-text/colour-changing-column split stage) and signature move (scroll-tied
colour depth) do not appear in any other row's cells.

## Feeling curve

1. **Recognition** — the reused question lands cold on plain white, nothing to hide behind.
2. **Curiosity** — Calyx's rust sheet arrives; a real screenshot inside it, not a claim.
3. **Confidence** — Hōrai's lacquer sheet deepens as you read; same builder, different hand.
4. **Trust** — Hyperborea's amber sheet; still legible with zero photographs anywhere on it.
5. **Resolve** — the page goes dark; the three colours reduce to three small ticks, one address.

**Peak:** the Hyperborea chapter. It is the one demo with zero photographs of its own, proven
on a page that itself has none — the largest conceptual payoff of the "bevis" argument.

**Signature move:** each chapter's colour sheet is not static. As the visitor scrolls through a
chapter, that panel's background continuously deepens via `color-mix(in oklch, var(--c),
var(--c-deep) calc(var(--p) * 55%))`, where `--p` is a page-authored local scroll-progress
value (0–1, computed from `getBoundingClientRect()` on a `requestAnimationFrame`-throttled
scroll listener) — like ink settling into a page as you read further down it. Under
`prefers-reduced-motion: reduce` the scroll listener never attaches, so `--p` stays at its
CSS default and every chapter simply shows its own flat, static colour — motion is removed,
content and colour are not.

## Full Swedish copy (plain text, final)

**Rail (persistent):** ALUNIX · Bevis · Hur det går till · Kontakt · hej@alunix.se

**Fold:**
- En person bygger sajten och svarar sedan i mejlen, inte ett formulär.
- Vad gör du för hand som inte borde göras för hand?
- Tre riktiga sajter visar svaret. Öppna dem och syna.
- [CTA] Mejla hej@alunix.se — Svar från personen som ritade sidan.

**Bevis (section intro):**
- Bevis
- Tre sajter, samma byggare. Ingen delad palett. Inget delat typsnitt. Ingen delad rytm mellan
  dem. Det är hela poängen.

**Chapter I — Calyx:**
- Ska sajten kännas lika taktil som blommorna?
- Calyx är en florist i cream och kursiv Cardo, med ett prissatt index i stället för en meny.
- "Kursiv och rak i samma rad."
- Öppna calyx ↗ (https://anti-slop-design.vercel.app/calyx)
- Caption: Florist · Stockholm / anti-slop-design.vercel.app/calyx

**Chapter II — Hōrai:**
- Ska en enda bild bära hela sidan?
- Hōrai är en tresystrarsrestaurang där fotografiet bär hela sidan, i lackröd accent och
  Cinzel-kapitäler.
- "Fotografiet bär hela sidan."
- Öppna hōrai ↗ (https://anti-slop-design.vercel.app/horai)
- Caption: Restaurang · Stockholm / anti-slop-design.vercel.app/horai

**Chapter III — Hyperborea:**
- Finns det inget foto, bara en idé?
- Hyperborea är en konferens utan ett enda foto, bara ett solmotiv ritat i kod, i åtta
  varianter.
- "Ett ritat solmotiv i åtta varianter."
- Öppna hyperborea ↗ (https://anti-slop-design.vercel.app/hyperborea)
- Caption: Konferens · Lund / anti-slop-design.vercel.app/hyperborea

**Hur det går till:**
- Varifrån kommer designen? — Ur ditt material: logotyp, produkt, bransch. Aldrig ur ett
  färdigt tema.
- Vem svarar när du mejlar? — Jag. Inget formulär, inget team, ingen mellanhand.
- Vad händer om svaret är nej? — Då säger jag det, direkt.
- Omfattning och pris — [behövs pris]
- Leveranstid — [behövs leveranstid]

**Kontakt (close, dark band):**
- Skriv, så svarar jag.
- hej@alunix.se
- Alunix är en enskild firma, en person. Samma händer bygger Alunix OS och ett lagersystem åt
  en annan kund, men den här sidan handlar om sajten din verksamhet behöver.
- Tre sajter. Tre färger. Samma hand. (+ tre färgprickar)

## Post-review fixes (coordinator pixel pass, 2026-09-04)

1. **Dropped the "Läser du engelska också?" Q&A.** Its answer ("En engelsk version kommer
   senare") promised a timeline not in brief.md — the brief only says a switcher will exist
   eventually, built in Swedish for now. The coordinator offered two fixes: answer with the
   switcher fact, or drop the question. Answering with "Sidan finns på svenska och engelska,
   med en växlare i huvudet" would itself be false for *this* concept page (no switcher is
   actually built here), so the question was dropped rather than replaced. "Hur det går till"
   now runs three Q&A pairs instead of four.
2. **Removed the close-band system-number ledger** (757 entiteter / 2 847 kopplingar / 346
   skills i 21 buntar / 84 agenter, plus its caption). That data-as-texture device is K3's
   contract signature, not K2's, and K2's fingerprint row never asked for it. The close now
   reads: heading, mailto, the one-paragraph "enskild firma" line, and the three colour chips
   with their caption — nothing else. Removed the now-dead `.kontakt__grid` / `.kontakt__stats`
   CSS along with the markup; file is 369 lines (down from 389).

No em or en dashes anywhere in visible text. No fabricated numbers, testimonials, logos, or
customer names — Klova is never mentioned. Every number traces to brief.md. Price and delivery
time are the literal bracket placeholders, styled as a dashed-border label, never a number.

## Skills invoked, in order

1. `Skill(design)` — front door, Steps 1b/2b/3/4/5 per the assignment (bake-off skipped, this
   build IS a bake-off cell).
2. `Skill(copywriting)` — structure/offer pass against the CONTENT FUNDAMENTALS voice rule
   ("varm andra person, en fråga per kapitel, svaret i en mening").
3. Copy gate Pass 1b (`references/copy-gate.md`) applied by hand — every headline/lead traced
   to a source line in brief.md (see decision ledger and the sourced-line list above); no
   invented proof.
4. `Skill(humanizer-svenska)` — full pattern scan against the copy; removed a duplicate
   sentence, split one comma-chained triad into short sentences, and cut a mild "inte bara"
   negative-parallelism construction from the Calyx question.
5. `a11y-audit` scripts (`a11y_scan.py`, `tab_walk.py`, `reflow.py`) — see verification numbers
   below.
6. `design-verify` procedure (`shoot.py`, `scroll_verify.py`) — see verification numbers below.

## Verification numbers (final, clean pass, re-run after the post-review fixes)

**`shoot.py`** — fold + full-page (3619px after the two removals) captured and read at
1440×900; read again at
320/375/414/768 via a local Playwright helper (`shots/_mobile_shoot.py`) plus a
`prefers-reduced-motion: reduce` capture. No horizontal overflow at any width
(`scrollWidth === clientWidth` at 320/375/414/768).

**`scroll_verify.py`** — final run, zero findings on every axis:
```
deadScroll: []
cuesNeverFull: []
unrevealed: []
contrastUnderMedia: []
blankBands: []
```
(One interim finding — `.chapter__cap` never reaching full opacity, because it was styled at a
static `opacity:.86` — was fixed by removing the opacity rule; the mono captions are now full
opacity, differentiated by size/colour/family instead.)

**`a11y_scan.py`** — final run: `"violations": [], "passes": 30, "incomplete": 0`. (One interim
serious `color-contrast` finding — the Calyx panel's caption text at ~4.36:1 — was fixed by
darkening the Calyx chapter colour from `#b8552f`/`#8f3f20` to `#a34827`/`#7a3319`, restoring
~5.4:1 against the on-panel text.)

**`tab_walk.py`** — 13 stops, every stop has a visible focus indicator, all in viewport, no
keyboard trap. One heuristic `order_mismatch` flag: the sticky rail's bottom-anchored mail link
(flex `space-between`, tall sticky column) sits visually lower on screen than the hero CTA that
follows it in DOM order. This is the expected two-region pattern (persistent sidebar nav, top
to bottom, then main content, top to bottom) rather than a broken tab order — not fixed, noted
here per the a11y-audit reporting convention rather than silently waived.

**`reflow.py`** — `overflow320: []`, `overflow200Zoom: []`, `hiddenUnderReducedMotion: 0`.

**Mobile hit targets** — nav links, CTA button, and chapter links are all ≥44px min-height;
verified visually at 320/375/414/768 with no two-line button/link wraps.

## Files

- `tests/alunix-concepts/cells/K2-chain/index.html` — the build (369 lines).
- `tests/alunix-concepts/cells/K2-chain/demos/{calyx,horai,hyperborea}.webp` — vendored demo
  screenshots (copied from `~/alunix/public/demos/`, never hotlinked).
- `tests/alunix-concepts/cells/K2-chain/shots/` — `shoot.py` fold/full captures, mobile
  captures at 320/375/414/768, a reduced-motion capture, and the helper script that produced
  the mobile set (`_mobile_shoot.py`).
- `tests/alunix-concepts/cells/K2-chain/NOTES.md` — this file.

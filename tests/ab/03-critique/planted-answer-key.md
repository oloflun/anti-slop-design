# Answer key — planted.html

Fixture: `planted.html`, a single-file landing page for **Florhuset Majorna**
(florist/ateljé, Mariaplan 4, Göteborg), built to the editorial-print house
physics (cream ground, hairlines, ledger for prices, one accent — poppy red
`#C1432B` on cream `#F6F1E8`/ink `#1E2A1F`). It is otherwise clean; exactly
seven defects are planted on purpose, each marked in the source with an HTML
comment `<!-- PLANTED n: ... -->` (three sit in `<style>` as CSS comments
adjacent to the rule that causes them, since that's where the defect actually
lives).

| # | Defect | Dimension | Where in the page |
|---|---|---|---|
| 1 | Two competing primary CTAs in the hero — "Beställ bukett" and "Boka bröllopsmöte" — both rendered with the identical filled `.btn-primary` treatment (same accent fill, same weight, same size), so neither reads as the default action. | Affordance | Hero, `.hero .ctas` (~line 180 in source; both links share class `btn-primary`). |
| 2 | Buried CTA in the subscription section: a decorative badge ("★ Mest bokade" — accent-filled pill, bold, all-caps) sits visually louder than the actual conversion action, a small plain underlined text link ("Starta prenumeration →") dropped at the bottom of the section in body-text weight and stone-grey styling. | Affordance | `#prenumeration` section — `.badge-decorative` vs `.cta-quiet` (~lines 251–255). |
| 3 | Spacing drift with no shared scale: section `padding-block` alternates 96px (hero) / 116px (buketter ledger, and again on "om ateljén") / 84px (bröllop) / 120px (prenumeration) / 96px (ateljékvällar) — no 8pt-ish rhythm underneath. Compounded by card-gap drift: the "om ateljén" info grid uses `gap:22px` while the footer column grid uses `gap:18px` for a structurally similar three-up layout. | Density / Composition | CSS rules `.hero`, `.ledger-section`, `.flat-text-bröllop`, `.flat-text-prenumeration`, `.flat-text-ateljekvallar`, `.about-section` (padding); `.info-grid` vs `footer .cols` (gap). |
| 4 | Two adjacent hierarchy levels within 1.15× of each other: inside "om ateljén", `h2` is set to 28px and the immediately following `h3` ("Öppettider") to 25px — a 1.12× ratio — so the section heading and its subheading read as roughly the same weight of importance instead of a clear step down. | Hierarchy / Typography | `.about-section h2`, `.about-section h3` rules; rendered in `#om`, "Om ateljén" / "Öppettider". |
| 5 | Caption grey `#9A9A9A` set on the cream ground `#F6F1E8` measures roughly 2.5:1 contrast — under the 3:1 floor even for large/meta text (WCAG AA needs 3:1 for large text, and this is genuinely small, 11px). Used on every figcaption. | Colour | `--caption-grey` token; `.hero figcaption`, `.about-section figcaption` (the hero photo caption and the "om ateljén" photo caption). |
| 6 | "Slutsåld" (sold out) state on the Dahliabukett ledger row is carried by colour alone: an accent-red dot (`.dot-slut`) with no adjoining text, no `aria-label`, nothing a screen reader or a colour-blind visitor can read as "sold out" versus any other status a red dot might mean. | Affordance / Colour | `#buketter` ledger, row 03 "Dahliabukett" — `.ledger-status` / `.dot-slut` (~line 221). |
| 7 | Three consecutive sections in the middle of the page — Bröllop, Prenumeration, Ateljékvällar — share identical anatomy: kicker + h2 + one paragraph, no imagery, same cream ground, same 720px text column. Breaks the "at least three distinct section anatomies" floor and reads as one long undifferentiated scroll between the ledger and the "om ateljén" photo section. | Composition / Brand | `#brollop`, `#prenumeration`, `#ateljekvallar` — all three use the shared `.flat-text` class with only padding varying (itself defect 3). |

## Notes for whoever grades against this key

- Defects 3 and 7 overlap spatially (the three flat-text sections are also
  where three of the four drifting padding values live) but are distinct
  findings: 3 is about the padding *scale*, 7 is about section *anatomy*.
  A critique that catches only one of the two should not get full credit for
  both.
- Defect 2's badge is intentionally not itself a defect in isolation — a
  decorative badge is fine. The defect is the *relative* weighting against
  the real CTA sitting right below it.
- Everything else on the page (kicker microformat, ledger construction for
  the bouquet list, one accent used only at display scale, hairline
  separators, the tonal-inversion footer, `prefers-reduced-motion` handling,
  focus-visible ring, single `h1`, real address/hours, no lorem, no invented
  customer counts) is deliberately correct and should not be flagged as a
  defect by a working critique procedure.

# AB02 — a11y-audit i loopen (signup i tre steg + dashboard, Operate, Tier 1)

A = produktreferenserna (product-surfaces, interaction-and-states, responsive). B = samma + a11y-audit-skillen: bygg → mekaniskt pass → åtta pass → EN fix-runda → mekaniskt pass igen.

| Mått | A | B (efter fix) | Not |
|---|---|---|---|
| axe-violations (desktop + 390) | 0 | 0 | båda rena mekaniskt |
| tab_walk-issues (slutläge, rättat skript) | 0 | 0 | B:s egen före/efter-körning: 1 → 0 (skip-link utanför viewport vid fokus) |
| reflow 320 / 200 % / dold vid reduced motion | 0 / 0 / 0 | 0 / 0 / 0 | |
| fynd i B:s egen granskning | — | 2 HIGH, 1 MAJOR, 5 minor | modalens tysta validering, tabellsemantik vid mobil-kollaps, 44 px-träffytor, dvh, reduced-transparency |
| synliga a11y-affordanser | numrerade steg | "Steg 1 av 3", formathint före fält, tabellcaption | principer ur skillen |

Visuellt (compare/signup.png, dashboard.png lästa): båda är korrekta Operate-ytor på Klova-tokens; A är kompaktare, B har fler orienteringssignaler och större KPI-siffror. Ingen visuell defekt i någon. Skillnaden är det som inte syns i en stillbild: B:s modal säger vad som blev fel, B:s tabell förblir en tabell för skärmläsare på mobil (5 role-attribut mot 0), B:s träffytor är 44 px.

**Beslut: IN.** Kostnad: en fix-runda och tre skriptkörningar. Modifiering (gjord): fixturens sökväg i SKILL.md är absolut (`~/anti-slop-design/tests/a11y/broken.html`) så agenten inte letar i fel projekt; skripten körs även i `#dashboard`-läget (hash-routen) — noterat i skillen.

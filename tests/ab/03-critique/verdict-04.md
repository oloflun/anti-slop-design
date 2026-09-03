# AB04 — designpowers-granskarna som Sonnet-subagenter (design-critic, design-a11y-reviewer, design-heuristics)

Samma planterade sida. Tre agenter parallellt, mina egna ögon som facit (7 planterade fel + skärmbilder).

| Granskare | Planterade fel | Extra fynd (verkliga) | Falska/svaga fynd | Verdict |
|---|---|---|---|---|
| design-critic | 7/7 | lane-avvikelse (inget "salt-bleached harbour" i paletten), accent aldrig i display-skala, en-dash i öppettider, ★-badge som ounderbyggd superlativ | — | revise |
| design-heuristics | 6/7 (missade h2/h3-kvoten) | ingen beställningsväg per bukett, mailto utan telefon, döda footer-länkar (#), ingen skip/back-to-top | "ingen sticky header" är smak, inte fel | revise |
| design-a11y-reviewer | 4 relevanta (dot, caption 2.5:1, CTA-par, h2/h3) | footer-rubriker 2.92:1 (axe + contrast.py eniga), fokusring under 3:1 på samma par, saknat `<main>`, nav-träffytor 17 px | letade fixturen i fel projekt (sa "finns inte"); sökvägen i skillen ska vara absolut | **Block** |

Reconciliation (accessibility > usability > brief): fyra HIGH från a11y först, sedan heuristikens "ingen beställningsväg", sedan critic:s lane-avvikelse. Tillsammans: 7/7 planterade + 9 verkliga extrafynd som mina egna ögon inte hade listat (footer-kontrasten, träffytorna, mailto-fallet).

**Beslut: IN.** Tre läsande Sonnet-granskare med fasta roller hittar mer än en ensam granskare och kostar inga skrivrättigheter. Modifieringar: (1) a11y-skillen pekar på fixturen med absolut sökväg (`~/anti-slop-design/tests/a11y/broken.html`); (2) Step 5 dispatchar de tre parallellt efter första rena bygget, jag verifierar mot pixlar innan fix-rundan; (3) heuristics-agenten får mobilskivor i inputen (den flaggade själv att 390-bilden saknades).

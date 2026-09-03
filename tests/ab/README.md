# A/B-tester — design rework v3

Varje tillägg testas isolerat mot baslinjen (kedjan som den var 2026-09-03 före v3),
sedan kumulativt. Byggare: färska Sonnet-subagenter, ingen dialog, ingen iteration.
Bedömning: mina egna ögon på PNG (shoot.py + shoot_slices.py, desktop 1440 + mobil 390 +
reduced-motion) plus siffror (measure.py, contrast.py, a11y_scan.py, scroll_verify.py,
detect.mjs). Varje mapp: `A-baseline/`, `B-with/`, `verdict.md` (bilder namngivna,
siffror i tabell, tre meningars visuellt omdöme, beslut: in / in-modifierad / ut).

| # | Tillägg | Brief | Mäts |
|---|---|---|---|
| 01 | hook-klassificerare | intent_corpus + 3 riktiga icke-designprompter i ett kodrepo | falska positiva = 0, sanna = 100 %, ledger tyst |
| 02 | a11y-audit | "Signup i tre steg + en enkel dashboard för en bokningstjänst (Tier 1: derive från Klova-tokens)" | axe, tab-walk, reflow 320/200 %, persona-walkthrough; bygge med auditen i loopen mot utan |
| 03 | visual-critique | landningssida med tre planterade fel (två primära CTA, buried CTA, 20 px-drift i spacing) | dimensionerna hittar de planterade felen |
| 04 | designpowers-granskare | samma trasiga sida granskad av 3 subagenter mot enbart mig | fynd/precision, falska fynd |
| 05 | reference-lock | Tier 2: "landningssida för ett API-verktyg, referenser: Linear (mörk), en syra-gul docs-sajt, en serif-editorial" | averaging-testet: hamnar B på cream + orange + artig serif? |
| 06 | scroll-craft | "Persuade-sida för en fysisk produkt (specialkaffe på burk), register warm photographic, egna Unsplash-foton" | ≥4 device-familjer, dead scroll 0, cue-opacity, kontrast under ljusaste frame, fingerprint mot sites/ |
| 07 | shotgun/bake-off | "Startsida för en florist i Göteborg" | 3 riktningar klarar fingerprint 3/6 mot varandra; vald → bygge; mot direktbygge |
| 08 | emil-uppdatering | "Settings-yta med drawer, toast, tabs och hold-to-delete" | review-animations Block/Approve, easing/duration, reduced-motion |
| 09 | frontend-design på/av | brief 07 med frontend-design-skillen injicerad resp. ej | konvergens mot look 1/2, lane-namn, generic-default-test |
| 10 | katalog | Tier 2-bygge med 3 katalogposter som referenser mot utan | reference-lock-kvalitet, referens-läst-event |
| K | kumulativt | brief 07 efter varje adoption i ordningen 01→10 | inget mått får försämras; verify grönt; unloaded strong routes = 0 |

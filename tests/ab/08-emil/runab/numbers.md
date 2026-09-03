# A/B numbers: 08run

- A (baseline): `tests/ab/08-emil/A-baseline`
- B (with): `tests/ab/08-emil/B-with`

No visual judgement here -- raw numbers only. Screenshots are in A-baseline/ and B-with/.

## measure.py

| metric | A | B |
|---|---|---|
| height | 5020 | 9281 |
| textElements | 68 | 93 |
| distinctFontSizes | 11 | 17 |
| distinctTextColors | 4 | 11 |
| distinctWeights | 1 | 3 |
| hairlineRules | 10 | 23 |
| distinctBackgrounds | 2 | 5 |
| contentWidthUsed | 1376 | 1392 |
| images | 0 | 2 |

## contrast.py

| | A | B |
|---|---|---|
| token backgrounds checked | 16 | 12 |
| below floor (fails) | 0 | 0 |

## a11y_scan.py (axe-core violations by impact)

| impact | A | B |
|---|---|---|
| minor | 1 | 0 |
| **total** | **1** | **0** |

## tab_walk.py

| | A | B |
|---|---|---|
| tab stops | 8 | 8 |
| issues | 4 | 4 |

## reflow.py

| | A | B |
|---|---|---|
| overflow @320px | 0 | 18 |
| overflow @200% zoom | 0 | 18 |
| hidden under reduced motion | 4 | 5 |

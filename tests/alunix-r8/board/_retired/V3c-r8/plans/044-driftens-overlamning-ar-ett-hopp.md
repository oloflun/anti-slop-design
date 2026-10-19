# 044 · Driftens överlämning tes → jätte är ett hopp: blå till papper i en bildruta vid scrollY 3 600

- **Status**: TODO (R10, loop 4)
- **Commit**: R9-läget av `runs/V3c/index.html`, md5 `909916d1`
- **Severity**: MEDIUM (visuellt/rörelse: grundens kalla ljus släcks i ett steg mitt i bandet, i båda riktningarna; gate 94 punkt 1 i andan, H-19:s "kallt ljus, inte en tvätt" har ett klipp i sig)
- **Category**: Visuellt / rörelse, H-19; Astra loop 4 fix 3, verifierad av arkitekten (`shots/loop-4/astra-verify/verify_astra4.json`)
- **Estimated scope**: 1 fil, ~4 rader JS (en variabel i `measureAct`, en rad i `driftColor`)
- **Källor**: `index.html` rad 1587 till 1600 (`driftColor()`: `if (t < 1) … else { a = STOPS[1]; b = STOPS[2]; k = driftSmooth(g / 0.35); }`), rad 1768 till 1775 (`measureAct`: `thesisTop/H`, `giantTop/H`); geometri `shots/loop-4/geom4.json` (tes 3 222 + 378, jätte 3 330 + 820, vh 900); mätning `astra-verify/verify_astra4.json`

## Problem

Leg 1 (svart → blå) körs medan tesens råa progress `t < 1`; leg 2 (blå → papper) tar över
när `t` når 1, med `k = smooth(g / 0.35)` där `g` är jättens råa progress. Jätten börjar 108
px efter tesen, så när tesen är klar (scrollY = 3 222 + 378 = 3 600 vid 1440) är
`g = (3 600 + 900 − 3 330) / (820 + 900) = 0,68`, och `smooth(0,68 / 0,35)` = 1: leg 2 står
redan på sitt slut. Mätt (`verify_astra4.json`, 1440, ramarna vakna):

| scrollY | `--sc-canvas` på `.ground` | träpanel (720,40) | marginal (1420,400) |
|---|---|---|---|
| 3 580 | rgb(18,63,104) | (119,130,140), chroma 21 | (50,61,71), chroma 21 |
| 3 600 | rgb(18,63,104) | (119,130,140), chroma 21 | (50,61,71), chroma 21 |
| 3 620 | rgb(244,242,238) | (129,128,127), chroma 2 | (60,59,58), chroma 2 |

Ett hopp på 20 px scroll, från kallt ljus till neutralt, och tillbaka uppåt. Motorns egen
loop (`scrollcraft.js` rad 972 till 984, "första akten mitt i, byt när föregående är klar")
gjorde samma sak i R7/R8, så 041 reproducerade felet troget ("pixel för pixel identiskt");
det är ett fel i kurvan, inte i 041:s flytt.

```js
/* index.html:1596-1598 - current */
    if (t < 1){ a = DRIFT_STOPS[0]; b = DRIFT_STOPS[1]; k = driftSmooth(t / 0.35); }
    else { a = DRIFT_STOPS[1]; b = DRIFT_STOPS[2]; k = driftSmooth(g / 0.35); }
```

## Target

Leg 2 räknas från överlämningspunkten, inte från jättens egen start: `gH` är jättens råa
progress i det ögonblick tesen når 1 (en ren funktion av de fyra topp/höjd-talen och vh,
mätt i `measureAct` tillsammans med dem), och `k = smooth((g − gH) / 0.35)`. Vid
överlämningen är `g = gH`, `k = 0`, färgen exakt blå på båda sidor; papper nås 0,35 av
jättens liv senare (≈ 600 px vid 1440), kontinuerligt i båda riktningarna.

```js
/* target: i measureAct, efter giantTop/giantH */
    driftHand = giantH ? Math.min(1, Math.max(0, (thesisTop + thesisH + window.innerHeight - giantTop) / (giantH + window.innerHeight))) : 0;
/* target, index.html:1596-1598 */
    /* PLAN 044 (loop 4): leg 2 räknas från överlämningen (g = driftHand när
       t når 1), inte från jättens start; annars står smooth(g/0,35) redan
       på 1 när tesen är klar och färgen hoppar blå -> papper i ett steg
       (astra-verify/verify_astra4.json, scrollY 3600 -> 3620). */
    if (t < 1){ a = DRIFT_STOPS[0]; b = DRIFT_STOPS[1]; k = driftSmooth(t / 0.35); }
    else { a = DRIFT_STOPS[1]; b = DRIFT_STOPS[2]; k = driftSmooth((g - driftHand) / 0.35); }
```

`driftHand` deklareras bredvid `thesisTop` (rad 1760) och skrivs i `measureAct` (som
körs vid mount, load, resize). Om jätten skulle ligga så att `gH ≥ 1` (aldrig i dagens
layout) blir leg 2 konstant blå; det är rätt fallback (inget hopp).

## Repo conventions to follow

- De tre stoppen, 24 %, `mix-blend-mode:color`, skrivning på `.ground` (038, 041): orörda.
- H-19:s mätpunkt (tesen centrerad, scrollY 2 961, `t` = 0,5, leg 1) påverkas inte: chroma 21 står.
- Ledgerrad i `BRIEF.md` § Byggarens rader, R10: "Driftens leg 2 räknas från överlämningen".

## Steps

1. Lägg `driftHand` och ändra raden enligt Target.
2. Pixelkontroll (scratch, som `shots/loop-4/scripts/verify_astra4.py` § drift): scrollY 3 400, 3 580, 3 600, 3 620, 3 700, 3 900, 4 200 vid 1440: `--sc-canvas` monotont från rgb(18,63,104) mot rgb(244,242,238) utan steg > 40 per kanal mellan två grannpositioner (20 px scroll); träpanelens chroma vid 3 600 och 3 620 lika ± 2; vid 4 200 ≤ 4. Samma sekvens uppåt (4 200 → 3 400): samma värden per position.
3. `drift2.py`-punkterna vid tesen centrerad och i folden (038:s tal): (720,180) chroma 21 ± 2 vid tesen, 0 i folden.
4. Kontrollera 390x844 (tes 2 870 + 488, jätte 4 157 + 677): samma monotona övergång från scrollY 3 358.

## Boundaries

- Inga nya stopp, ingen ny färg, ingen ändring av leg 1.
- Matchar inte rad 1587 till 1600 eller 1768 till 1775: STOPPA.

## Verification

- **Mekaniskt:** steg 2, 3, 4.
- **Skärmbild:** `astra-verify/drift-3580.png` mot `drift-3620.png` motsvarigheter: ingen synlig skillnad i grundens ton mellan de två; `slices-1440/…s03` (tesen) oförändrad i ton.
- **Feel check:** hjul långsamt över 3 500 till 4 200: ljuset släcks gradvis, inget klipp; uppåt tänds det gradvis.
- **Done when:** H-19 bockad utan not om överlämningen.

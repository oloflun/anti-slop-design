# 041 · Driften skrivs på `.ground` av sidan, inte på `:root` av motorn (mätgrindad)

- **Status**: TODO (R9, loop 3)
- **Commit**: R8-läget av `runs/V3c/index.html`, md5 `70214a22`
- **Severity**: LOW (kod/bildtid; behålls bara med mätt vinst)
- **Category**: Kod (bildtid), H-21, H-22; plan 028 D:s motorfynd; Astra loop 3 fix 4
- **Estimated scope**: 1 fil, 2 attribut bort, ~14 rader JS
- **Källor**: loop 2 `shots/loop-2/profile/`, `synth3`: `:root --sc-canvas` 9,13 ms per ändring vid cpu 1, 0,24 ms skriven på `.ground`; `scrollcraft.js` rad 972 till 984 (drift-legs, `smooth(raw / 0.35)`, `docEl.style.setProperty`), `scrollcraft.css` rad 102 (`body{background:var(--sc-canvas)}`, dold under `.ground`); loop 3 A/B `shots/loop-3/probe/ab/mount-noclip-*` mot `mount-noclip-nodrift-*` (35,1 / 35,0 mot 40,8 / 35,4 ms i prisfönstret: ingen skillnad där driften inte skrivs)

## Problem

Motorn samlar `data-sc-drift` på `.panel-thesis` (rad 1154) och `#giant-section` (rad 1215)
och skriver `--sc-canvas` på `<html>` varje bildruta som värdet ändras (de första 35 % av
respektive akts råa liv). En custom property på roten invaliderar hela dokumentet: 9,13 ms
per ändring vid cpu 1 (loop 2), ~36 ms vid cpu 4, i exakt de fönster där tesen bleeder och
jätten scrubbar. Enda konsumenten som syns är `.ground::after` (rad 255 till 257,
`contain:strict`). Loop 3:s A/B visade ingen vinst i **prisfönstret**, för där ändras
värdet inte; vinsten, om den finns, ligger i tes- och jättefönstren.

## Target

Attributen tas bort (motorn har då inga drift-legs och skriver aldrig `--sc-canvas`).
Sidan räknar samma tre stopp med motorns egen kurva och skriver på `.ground`:

```js
/* target, i plan 035:s latchTick (körs medan någon akt lerpar) eller i readState */
  var STOPS = [[11,12,14],[18,63,104],[244,242,238]];   /* --c-black, --c-accent-deep (#123f68), --bg (#f4f2ee): samma värden som attributen bar */
  function smooth(x){ x = x < 0 ? 0 : x > 1 ? 1 : x; return x * x * (3 - 2 * x); }
  function driftColor(){
    var t = thesisRaw(), g = giantRaw();          /* aktens råa progress som motorn: (y + vh - top) / (h + vh) */
    var a = STOPS[0], b = STOPS[1], k = smooth(t / 0.35);
    if (g > 0){ a = STOPS[1]; b = STOPS[2]; k = smooth(g / 0.35); }
    var c = [0,1,2].map(function(i){ return Math.round(a[i] + (b[i] - a[i]) * k); });
    return 'rgb(' + c.join(',') + ')';
  }
  /* skriv bara vid ändring, och bara på .ground */
  var col = driftColor(); if (col !== lastCol){ lastCol = col; ground.style.setProperty('--sc-canvas', col); }
```

Stoppen skrivs som tokens, inte hex, i koden: läs dem en gång vid mount ur
`getComputedStyle(document.documentElement)` för `--c-black`, `--c-accent-deep`, `--bg`
(gate 48: värdena bor i `:root`-blocket), parsade till RGB. Motorns `mixColor` blandar i
sRGB per kanal; samma här.

## Repo conventions to follow

- Motorn och `scrollcraft.css` rörs inte; `:root --sc-canvas:#0b0c0e` (rad 181) står som initialvärde.
- `.ground`:s `contain:strict` och pseudolagren står.
- Ledgerrad i `BRIEF.md` § Byggarens rader, R9: "Driften skrivs på `.ground` av sidan" **eller** "041 mätt utan vinst, återställd".

## Steps

1. **Mät före:** `motion_probe.py` `.panel-thesis:--sc-ps` cpu 1, 100:60, 18 ticks från `.panel-thesis.top − 900` (≈ 2 322), och `#giant-section:--sc-ps` 18 ticks från `#giant-section.top − 900` (≈ 2 430), ramarna förmonterade (scratch `motion_probe_ab.py --pre` med `MOUNT`-strängen ur `shots/loop-3/scripts/ab_band.sh`), tre körningar var, median p95.
2. Ta bort `data-sc-drift` på rad 1154 och 1215; lägg JS enligt Target.
3. Pixelkontroll: `drift2.py`-punkterna ((720,180), (1000,180), (1300,100) vid tesen centrerad; samma vid `#giant-section.top − 200`; (1420,850) vid scrollY 0) inom ± 2 RGB-steg av före-värdena (samma kurva, samma stopp).
4. **Mät efter:** samma som steg 1. Behåll bara om medianen p95 är ≥ 3 ms lägre i båda fönstren; annars återställ attributen och skriv talen (som 028 E).

## Boundaries

- Ingen ny färg; stoppen är de tre som redan står i attributen.
- Matchar inte rad 1154, 1215 eller 255 till 257: STOPPA.

## Verification

- **Mekaniskt:** steg 3 (pixlar), steg 4 (tal, tre körningar var, median).
- **Skärmbild:** `s03`, `s04` vid 1440 identiska i ton med före (efter plan 038:s 24 %).
- **Feel check:** samma ljus som förut när tesen kommer in och när jätten går mot papper.
- **Done when:** talen före/efter i NOTES § R9 och ledgerraden säger vilket utfall som gäller.

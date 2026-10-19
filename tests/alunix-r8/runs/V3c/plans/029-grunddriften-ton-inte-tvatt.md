# 029 · Grunddriften: en mätbar ton, inte en tvätt av fotografiet

- **Status**: TODO (R8, loop 2)
- **Commit**: R7-läget av `runs/V3c/index.html`, md5 `d30355da`
- **Severity**: MEDIUM
- **Category**: Visuellt (grund och material), H-19, T-6; leadens R7-fynd 2
- **Estimated scope**: 1 fil, 1 rad CSS
- **Källor**: leadens pixelläsning R7 (grundpixlar (20,48,73) till (105,133,158)); loop 2 `shots/loop-2/diag/diag3.json` `B_ground`/`B_summary` (åtta varianter × fem stopp × tre punkter), bilderna `diag/B-current-62-giant.png`, `B-baseline-gray-giant.png`, `B2-mix-40-giant.png`, `B2-mix-34-giant.png`, `B-mix-28-giant.png`, samma vid tesen; skivorna `slices-1440/v3c-1440--s03.png`, `s04.png`

## Problem

Plan 017 A flyttade gråskalan till fotolagret och lade tonen ovanpå (`.ground::after`,
`mix-blend-mode:color`, 62 %). Driften blev mätbar (H-19: delta 15 mellan fold och
tesband) men hela fotografiet färgas blått: grundpixeln i spaltrännan bakom jätten
(720,450) mäter (58,86,111) mot gråskalans (80,80,80); högermarginalen (8,23,37), chroma
29. I skivorna `s03`/`s04` läser rummet som doppat i blått, inte som ett gråskalefoto med
en kall ton: det är ett kulörbyte av grunden, och accenten får därmed en fjärde roll (hela
grunden) i stället för sina två (tesplåten, måtten).

```css
/* index.html:250-252 - current */
  .ground::after{content:"";position:absolute;inset:0;
    background:color-mix(in srgb,var(--sc-canvas) 62%,transparent);
    mix-blend-mode:color;}
```

Uppmätt (högermarginalen (1420,850), fold → tesband; spaltrännan bakom jätten):

| tonstyrka | fold | tesband | delta max | chroma tes | rännan bakom jätten |
|---|---|---|---|---|---|
| 0 (bara gråskala) | (20,20,20) | (20,20,20) | 0 | 0 | (80,80,80) |
| 62 % (i dag) | (20,20,22) | (8,23,37) | 15 | 29 | (58,86,111) |
| 40 % | (21,20,18) | (12,22,31) | **13** | 19 | (66,84,101) |
| 34 % | (20,20,19) | (13,22,30) | 11 | 17 | (68,83,97) |
| 28 % | (20,20,19) | (14,21,27) | 8 | 13 | (70,83,94) |
| multiply 62 % | (19,19,19) | (8,11,13) | 11 | 5 | (34,43,51) |
| soft-light 62 % | (44,44,43) | (10,14,18) | 34 | 8 | ljusar upp folden: fel |

40 % är den lägsta styrka som klarar H-19:s 12 steg (delta 13) och den högsta där rummet
i `B2-mix-40-giant.png` fortfarande läser som ett gråskalefoto i kallt ljus: träpanelen
är trä, lampan är lampa, bara ljuset är kallt. Vid 62 % (`B-current-62-giant.png`) är
träet blått.

## Target

```css
/* target, index.html:250-252 */
  /* PLAN 029: 62 % färgade hela fotografiet (rännan (58,86,111) mot gråskalans
     (80,80,80), leadens R7-fynd). 40 % är lägsta styrka som håller H-19:s 12 steg
     (delta 13 fold → tesband, mätt loop 2) och högsta där rummet förblir ett
     gråskalefoto i kallt ljus i stället för ett blått. */
  .ground::after{content:"";position:absolute;inset:0;
    background:color-mix(in srgb,var(--sc-canvas) 40%,transparent);
    mix-blend-mode:color;}
```

## Repo conventions to follow

- Tonen läser motorns `--sc-canvas` (drift-stoppen på rad 1114 och 1169 rörs inte).
- `.ground`:s `contain:strict` och de två pseudolagren (plan 017 A) står.
- Ledgerrad i `BRIEF.md` § Byggarens rader, R8: "Grunddriften 40 %".

## Steps

1. Byt `62%` → `40%` på rad 251.
2. Mät (Playwright, 1440x900, `reduced_motion="reduce"`, 500 ms settle): grundpixel
   (1420,850) vid scrollY 0 och vid `.panel-thesis` centrerad; skriv RGB. Villkor: största
   kanalskillnad ≥ 12. Faller det (talet var 13 med 1 steg marginal): höj till 44 % och
   mät om; ligger 44 % också under 12 (annan färgprofil eller Chrome-version): STOPPA och
   skriv talen.
3. Mät samma punkt vid `.panel-giant.top − 200` (driften mot `#f4f2ee`): kanalerna ska
   ligga inom 12 steg av varandra (chroma ≤ 12 vid papperstoppet: grunden bakom papperet
   är ljusgrå, inte blå).
4. `contrast_over_media.py --url` på `.hero-headline` och `.hero-sub` (grunden bakom
   folden är oförändrad: tonen vid ps 0 är `#0b0c0e`, mätt fold (21,20,18)).

## Boundaries

- Rör inte `filter` på `::before`, inte `mix-blend-mode`-typen (multiply och soft-light
  mättes och förkastades: multiply tappar H-19 (delta 11) och mörknar rummet; soft-light
  ljusar upp folden till (44,44,43)).
- Matchar inte rad 250-252: STOPPA.

## Verification

- **Mekaniskt:** steg 2 ≥ 12; steg 3 chroma ≤ 12; `motion_probe` heron inte sämre (samma
  lager, bara annan alfa).
- **Skärmbild:** skivorna `s03` och `s04` vid 1440: rummet bakom tesen och jätten är ett
  gråskalefoto i kallt ljus; spaltrännans trä läser som trä. Jämför mot
  `shots/loop-2/diag/B2-mix-40-giant.png` (målbilden) och `B-current-62-giant.png` (felet).
- **Feel check:** scrolla från folden till priset: ljuset kallnar när tesen kommer in
  och går mot papper vid jätten, utan att fotot byter kulör.
- **Done when:** H-19 bockad med talet; leadens "blå tvätt" borta i pixlarna.

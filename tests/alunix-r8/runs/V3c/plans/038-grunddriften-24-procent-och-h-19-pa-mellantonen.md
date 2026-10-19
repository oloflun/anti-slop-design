# 038 · Grunddriften 44 → 24 %: kallt ljus mätt på mellantonen, inte tvätt mätt på svärtan

- **Status**: TODO (R9, loop 3)
- **Severity**: MEDIUM
- **Commit**: R8-läget av `runs/V3c/index.html`, md5 `70214a22`
- **Category**: Visuellt (grund och material), H-19, T-6; leadens R8-fynd 2; TASTE § 2.2 och § 4.4 (en accent som gör en sak)
- **Estimated scope**: 1 fil, 1 rad CSS (+ kommentaren)
- **Källor**: leadens pixelläsning R8 (`s1440-03`, `s1440-04`, `s390-03`: "blåtonad"); loop 3 `shots/loop-3/drift2/drift2.json` (fem styrkor × tre lägen × fem punkter), bilderna `drift2/d44-thesis.png` (felet), `d24-thesis.png` (målbilden), `d18-thesis.png`, `d0-thesis.png` (gråskalan); loop 3 `slices-1440/v3c-1440--s03.png`, `s04.png`

## Problem

Plan 029 stannade vid 44 % för att H-19:s golv ("minst 12 RGB-steg mellan heron och
tesbandet") mättes på högermarginalens grundpixel (1420,850), som är nästan svart
(L ≈ 20). `mix-blend-mode:color` för över kulör i proportion till luminansen: en pixel
vid L 20 kan bara flytta sig några steg, medan träpanelen vid L 128 flyttar sig fyra gånger
så mycket. Golvet 12 på svärtan **tvingar** därför en tvätt på mellantonerna. Mätt i loop 3
(1440x900, tesen centrerad, R8-läget):

| tonstyrka | trä (720,180), gråskala (128,128,128) | chroma trä | marginal (1420,850) | delta marginal fold → tes |
|---|---|---|---|---|
| 44 % (i dag) | (112,132,150) | **38** | (11,22,32) | 11 |
| 30 % | (117,131,143) | 26 | (14,22,28) | 8 |
| **24 %** | (119,130,140) | **21** | (15,21,27) | 7 |
| 18 % | (122,130,138) | 16 | (16,21,25) | 5 |
| 0 % | (128,128,128) | 0 | (20,20,20) | 0 |

Folden är neutral vid alla styrkor (chroma 0 till 1 på (1300,700), (1420,850), (1200,450)).
I `d44-thesis.png` är rummet blått: trä, lampa och skrivbord har samma kulör som tesplåten.
I `d24-thesis.png` är rummet ett gråskalefoto i kallt ljus: träet är grått, ljuset är
kallt. `d18-thesis.png` är nästan neutralt (driften syns inte). Dom mot TASTE § 4.4:
accenten gör en sak (tesplåten och måtten); grunden får ett kallt ljus, inte en kulör.

```css
/* index.html:255-257 - current */
  .ground::after{content:"";position:absolute;inset:0;
    background:color-mix(in srgb,var(--sc-canvas) 44%,transparent);
    mix-blend-mode:color;}
```

**H-19 skrivs om av arkitekten** (loop 3): driften mäts på en mellantonspixel i grunden
(träpanelen, gråskala L 110 till 140), inte på svärtan: vid tesen chroma 12 till 24, vid
folden chroma ≤ 2. Det gamla talet (12 steg på svärtan) var fel mätpunkt, inte fel princip.

## Target

```css
/* target, index.html:255-257 */
  /* PLAN 038 (loop 3): H-19 mätt på mellantonen. 44 % gav chroma 38 på träpanelen
     (blå tvätt); 24 % ger chroma 21: kallt ljus, träet förblir trä. Golvet 12 steg
     på den nästan svarta marginalen var fel mätpunkt (color-blending skalar med
     luminansen) och är omskrivet i HELHET H-19. */
  .ground::after{content:"";position:absolute;inset:0;
    background:color-mix(in srgb,var(--sc-canvas) 24%,transparent);
    mix-blend-mode:color;}
```

## Repo conventions to follow

- Tonen läser `--sc-canvas` (drift-stoppen `#123f68` och `#f4f2ee` rörs inte; efter plan 037 skrivs variabeln på `.ground` av sidan, samma värde).
- `.ground`:s `contain:strict` och de två pseudolagren (017 A) står; `filter` på `::before` rörs inte; blandningstypen rörs inte (multiply och soft-light mätta och förkastade i loop 2).
- Ledgerrad i `BRIEF.md` § Byggarens rader, R9: "Grunddriften 24 %, H-19 på mellantonen".

## Steps

1. Byt `44%` → `24%` på rad 256; skriv om kommentaren enligt Target.
2. Mät (Playwright 1440x900, `reduced_motion="reduce"`, 700 ms settle) pixlarna (720,180), (1000,180), (1300,100) vid `.panel-thesis` centrerad och (1300,700), (1420,850) vid scrollY 0. Villkor: chroma (max − min) på (720,180) mellan 12 och 24; på (1300,700) och (1420,850) ≤ 2. Skriv RGB för alla fem.
3. Samma punkt (720,180) vid `.panel-giant.top − 200`: chroma ≤ 24 (driften mot papper är ljusgrå, inte blå).
4. `contrast_over_media.py --url` på `.hero-headline` och `.hero-sub` (folden oförändrad).

## Boundaries

- Bara raden 256 och dess kommentar. Matchar inte rad 255 till 257: STOPPA.
- Faller steg 2 (chroma på träet utanför 12 till 24): skriv talen, prova 22 % och 26 %, ta det som håller, STOPPA om ingen.

## Verification

- **Mekaniskt:** steg 2 till 4; `motion_probe` heron inte sämre (samma lager, annan alfa).
- **Skärmbild:** skivorna `s03` och `s04` vid 1440 (`scrollTo`-skivor räcker för grunden): rummet bakom tesen och jätten är ett gråskalefoto i kallt ljus. Målbild `shots/loop-3/drift2/d24-thesis.png`; felet `d44-thesis.png`.
- **Feel check:** scrolla från folden till priset: ljuset kallnar när tesen kommer in och går mot papper vid jätten, fotot byter aldrig kulör.
- **Done when:** H-19 (omskriven) bockad med talen; leadens "blåtonad" borta i pixlarna.

# 050 · V3d R3: tesbandets regression (Astra-oberoende, lead-fynd ur runda 2)

- **Status**: TODO (V3d R3, en runda)
- **Beställning**: lead läste `shots/lead-r2/d-004.png` + `sheet-d0/m0/m1.png`. Två fel, resten
  av R2 håller. Rör ingenting annat.

## Fel 1 (HIGH) · Tesrubriken bryts mitt i ord vid 1440 (och 1024/1280/1920)

**Problem, uppmätt (samma skript, alla fem breddar).** `.thesis-grid{grid-template-columns:
minmax(14ch,.5fr) 1.5fr}` (plan 049 fix 6 P03) låser textspalten till sitt 14ch-golv (135px)
vid VARJE skrivbordsbredd, eftersom `.5fr` aldrig ger mer än så här (bilden tar resten via sitt
eget bleed). Uppmätt före fix:

| Bredd | Textspalt | Rubrikrader | Bild %vw |
|---|---|---|---|
| 768 | 707px (mobilblock, enkolumn — håller redan) | 1 | 92 |
| 1024 | 135px | 5 | 39.5 |
| 1280 | 135px | 6 | 39.6 |
| 1440 | 135px | 7 | 40.4 |
| 1920 | 190px | 5 | 40.0 |

Låst rubrik "DET FÖRSTA INTRYCKET ÄR DIGITALT." delas `DET/FÖRST/A/INTRYC/KET ÄR/DIGITA/LT.`
— `overflow-wrap:anywhere` (satt som skydd mot overflow, plan-historik okänd) klipper ordet när
spalten är smalare än ett ord. Stycket får samma spaltbredd, alltså också för smalt (36ch-målet
kräver ~320-350px vid `--body-r5`, uppmätt långt under det).

**Target.** Inget ord bryts mitt i ordet vid 768/1024/1280/1440/1920. Textspalt ≥36ch för
stycket. Rubrik ≤4 rader. Bild ≥40%vw vid 1440 (kravet håller redan där, får inte tappas).

**Beslut.** Sida vid sida hålls (996px av 1344px tillgänglig bredd vid 1440 räcker gott och väl
för en 380px textspalt + 36px mellanrum + oförändrad bildbredd — ingen anledning att stapla).
1. `.thesis-grid{grid-template-columns:minmax(340px,1fr) minmax(0,1.6fr)}` — pixelgolv i
   stället för `ch` (samma skäl som plan 049 dokumenterade: `ch` på grid-containern löste inte
   ut mot styckets egen fontstorlek förra gången heller, och gav 135px oavsett). 340px mätt
   ge ≥36ch av `--body-r5`-stycket vid alla fem breddar (se § Verifiering).
2. `.thesis-figure`s bleed-konstanter (`margin-right`, `translateX`-koefficienterna) räknas om
   efter att spaltbredden ändrats, eftersom bildens bas-bredd nu kommer ur en mindre `1.6fr`-
   andel av samma innehållsbredd. Justeras empiriskt mot uppmätt %vw (mål ≥40 vid 1440), inte
   gissat.
3. `overflow-wrap:anywhere` på `.thesis-headline` behålls (sista skyddsnätet vid extremt smala
   fönster), men bär inte längre den dagliga bredden — 340px-golvet gör att den aldrig behöver
   klippa ett ord vid de fem mätta breddarna.

## Fel 2 (MEDIUM) · Calyx/Hōrai-ramarna tomma en hel skärm vid hjulscroll

**Problem, uppmätt (`lead-r2/sheet-d0.png` rad 3, bild 1).** Vid 800px hjulsteg visar en bild
en tom beige platta (Calyx) och en helt svart platta (Hōrai) — inget laddat innehåll — och
först nästa bild (800px senare) visar båda färdiga. Ramarnas montering (bild-src, `loading`,
ev. reveal-gate) sker för sent relativt scrollhastigheten.

**Target.** Besökaren ser aldrig en tom ram, mätt vid hjulscroll 800/400/100px vid 1440 och 390.

**Fix.** Undersöks och löses i steg 1 (se nedan) — troligen `loading="lazy"` på Calyx/Hōrai-
bilderna kombinerat med sen `IntersectionObserver`-tröskel; antingen tidigarelägg triggerns
`rootMargin` (montera bilden innan den är i viewport) eller ta bort `loading="lazy"` för dessa
två (de ligger redan djupt in i sidan, ingen LCP-risk). Ingen ny platshållarbild krävs om
tidigareläggning räcker — mäts, inte antas.

## Boundaries

- Rör bara `.thesis-grid`/`.thesis-figure`/bleed-konstanterna och Calyx/Hōrai-bildernas
  laddningsattribut. Ingenting annat i R2 rörs.
- Låst copy 15/15 oförändrad, ordagrant. Noll tankstreck.
- Kirurgiska `Edit`, aldrig en full omskrivning av filen.

## Verifiering

- Skript mäter VARJE rubrik på sidan (inte bara tesrubriken) vid 768/1024/1280/1440/1920:
  rendera med `overflow-wrap:normal` (ordbrytning avstängd) och räkna rader, jämför mot faktisk
  rendering, och kontrollera att inget ord delas (ingen synlig radbrytning mitt i ett ord).
- Hjulscrollsekvenser (`mouse.wheel`) genom tesbandet vid 768/1024/1280/1440/390, lästa.
- Par-bilder P02 och P03 i `shots/r3/` (samma metod som R2: en skärm per sida, ingen ihopsydd
  helsida, lokal HTTP-server inte `file://`).
- Kort grind: 0 horisontell scroll, `a11y_scan` vid 1440/390, låst copy 15/15, 0 tankstreck.

**Done when:** tabellen ovan visar 0 ord delade vid alla fem breddar, textspalt ≥36ch,
rubrik ≤4 rader, bild ≥40%vw vid 1440, och hjulscroll 800/400/100px aldrig visar en tom ram.

# Alunix, V3d runda 3: regressionen i tesbandet. Cell {{KONCEPT}}, ut-mapp `{{UT_MAPP}}`, port {{PORT}}.

Lead har läst runda 2 i hjulscrollsbilder, alltså `{{UT_MAPP}}/shots/lead-r2/d-004.png` och
kontaktarken `sheet-d0.png`, `sheet-m0.png` och `sheet-m1.png`. Resten av runda 2 håller.
Två fel ska lagas.

## Fel 1 (HIGH): tesrubriken bryts mitt i orden vid 1440
Fix 6 (P03) gjorde Hyperborea-bilden bredare, och då klämdes textspalten i den blå panelen
till cirka 140 px. Den låsta rubriken "DET FÖRSTA INTRYCKET ÄR DIGITALT." sätts därför som
`DET / FÖRST / A / INTRYC / KET ÄR / DIGITA / LT.`, och stycket får fem ord per rad. Panelen
är samtidigt cirka 650 px bred och till största delen tom blå yta. Det här är sämre än V3c,
och det är låst copy som går sönder.

**Mål:**
- Inget ord i någon rubrik bryts mitt i ordet vid 768, 1024, 1280, 1440 och 1920.
- Textspalten i tespanelen är minst 36 ch för stycket, och rubriken har högst fyra rader.
- Hyperborea är fortfarande minst 40 % vw i tesintervallet vid 1440, och bilden får gärna
  bleeda ut över panelens kant.
- Löses det genom att bilden läggs bredvid eller under texten i stället för ovanpå: gör så.

Mät för varje rubrik på sidan med skript. Jämför antalet rader med ordbrytning avstängd mot
antalet rader i den faktiska renderingen, och kontrollera att inget ord har delats. Skriv
tabellen i NOTES.

## Fel 2 (MEDIUM): ramarna står tomma en hel skärm vid hjulscroll i 1440
Vid hjulscroll i 800 px-steg (`lead-r2/sheet-d0.png`, rad 3, bild 1) syns bandet med en tom
beige platta där Calyx ska stå och en helt svart platta där Hōrai ska stå. Först i nästa bild
är båda laddade. Tidigareläggningen av ramarnas montering, eller en platshållare som är en
riktig stillbild av sajten i stället för tom yta, ska göra att en besökare aldrig ser en tom
ram. Mät med hjulscroll i 800, 400 och 100 px-steg vid 1440 och 390.

## Gör
- `Skill(design)` först.
- Skriv planen `{{UT_MAPP}}/plans/050-tesbandet.md`.
- Använd kirurgiska `Edit`.
- Ta hjulscrollssekvenser genom tesbandet vid 768, 1024, 1280, 1440 och 390, läs dem, och
  lägg par-bilderna P02 och P03 i `{{UT_MAPP}}/shots/r3/`.
- Kör en kort grind: noll horisontell scroll, `a11y_scan` vid 1440 och 390, låst copy 15/15,
  och noll tankstreck.

Rör ingenting annat från runda 2. Sista raden i NOTES § V3d R3 ska vara `V3d R3 klar` eller
`[PAUSED — steg X]`.

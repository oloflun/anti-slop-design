# Alunix, V3d runda 5: två fel ur leadens pixelläsning av R4. Cell {{KONCEPT}}, ut-mapp `{{UT_MAPP}}`, port {{PORT}}.

Lead har läst R4 i hjulscroll, 900 px per steg vid 1440 och 800 px vid 390. Resultatet
ligger i `{{UT_MAPP}}/shots/lead-r4/sheet-d0.png`, `sheet-d1.png` och `sheet-m0.png`. Allt
annat från R4 håller. Två fel ska lagas, och ingenting annat rörs.

## Fel 1 (HIGH): kapitelskärmen är ljus
"Från samtal till lanserad sida." står på en ljusgrå grund vid både 1440 och 390, se
`sheet-d0.png` rad 3 bild 2 och `sheet-m0.png` rad 2 bild 2. Antons beställning är att
processakten är inverterad, och kapitelskärmen hör till akten. Leads prompt för R4 strök
uttryckligen punkten om högst fyra mörka skärmar i följd. Den gränsen gäller inte.

**Mål:** kapitelskärmen står på aktens mörka grund, `--c-drafting`, med ljust bläck. Behåll
det R4 vann: skärmen står ensam vid 1440 och fyller sin skärm vid 390. Kontrasten mäts med
`contrast_over_media --url`.

## Fel 2 (HIGH): Calyx beskärs vid 390
I steg 06 och 07 zoomar kameran in så långt att Calyx-sajtens rubrik klipps i vänsterkanten
till "mical / tecture / kholm", se `sheet-m0.png` rad 2 bild 6 och rad 3 bild 1–2. Fyllnaden
på 80 % nåddes alltså genom beskärning. En beskuren produktbild läser som ett fel.

**Mål:** vid 390 visas **hela** Calyx-bilden, med alla fyra kanterna synliga och rubriken
"Botanical architecture, from Stockholm." hel. Bilden ska ändå fylla minst 80 % av arkets
yta i steg 06 och 07. Det nås genom att arkets egen proportion, eller öppningen, anpassas
till bildens 16:9 vid mobil, inte genom mer zoom. Kontrollera också 768 och 1024.

## Gör
- Kör `Skill(design)` först.
- Skriv planen `{{UT_MAPP}}/plans/052-kapitel-och-mobilbeskarning.md`.
- Använd kirurgiska `Edit`.
- Ta hjulscrollssekvenser, `mouse.wheel`, genom processakten vid 390, 768 och 1440. Lägg dem
  i `{{UT_MAPP}}/shots/r5/` och läs dem.
- Kör en kort grind: noll horisontell scroll 320–1920, `a11y_scan` vid 390 och 1440,
  `contrast_over_media`, rubrikskriptet (noll delade ord), låst copy 15/15, samt grep för
  tankstreck och `prefers-reduced-motion`.

Leverans: `NOTES.md` § V3d R5. Sista raden ska vara `V3d R5 klar` eller `[PAUSED — steg X]`.

# Alunix, V3d runda 21: ta bort omlandningen av konturarket. Cell {{KONCEPT}}, ut-mapp `{{UT_MAPP}}`, port {{PORT}}.

R20 löste inte felet. Lead har läst bilderna enskilt:
- `{{UT_MAPP}}/shots/lead-r20/1920-05.png` och `1920-06.png`: konturarket ramar fortfarande in
  band 01:s text.
- `{{UT_MAPP}}/shots/lead-r20/390-05.png`–`390-08.png`: **två ark syns staplade**, det frysta
  arket ovanför steg 01:s riktiga ark.

Lead väljer reservvägen ur R20-prompten: **ta bort `data-frozen`/`data-gone`-omlandningen
helt**, med tillhörande JS, CSS och eventuella `position:fixed`-lägen. Det landade konturarket
ska rulla ut med kapitlet, som i R19a. Behåll allt annat från R19: det blå planets
krympning, konstruktionslinjerna i 2 px och landningslinjen.

`Skill(design)` först. Använd kirurgiska `Edit`, och ta bort mer än du lägger till.

Verifiera med en hjulsekvens i 20 px-steg, åt båda hållen, genom kapitlet och steg 01 vid
1920x930, 1440, 768 och 390. Läs enskilda bilder. Det får aldrig finnas två ark samtidigt, och
aldrig ett streck över eller genom text. Pixeldiffa resten av sidan mot R19. Kör rubrikskriptet
och `a11y_scan` vid 390. Leverans: `NOTES.md` § V3d R21. Sista raden ska vara
`V3d R21 klar`.

# 056 — Astras granskning av R8 (reviews/r8-astra.md), tre mobilfynd (390)

V3d runda 9. Astras femte pass: alla R7-fixar stängda utom två, båda öppna bara vid 390.
Vid 1440 håller varje PARITET-rad — inget där rörs. `sites/*` rörs aldrig, copyn rörs inte.

## Fix 1 (HIGH) — Hōrais citat döljs bakom navet vid 390

`case-horai-03` centrerar `#quote-section` i ramen (Astra r7 fix 4, uppföljning), men vid
390 är ramens innerhöjd bara 450px. En sant centrerad `min-h-[1000px]`-sektion i en så kort
ram lägger citatet delvis bakom sajtens egen nav (`sites/horai.html`, orörd). Astras egna
måltal: ih ≥ 625px om ankaret förblir centrerat, ELLER ih ≥ 525px om ankaret läggs 100px
ovanför centrum.

**Fix:** höj Hōrais egen mobila case-fig-rad från delad `58svh` till en Hōrai-specifik
`72svh` (568px ih vid 844, klart över 525-tröskeln), och lägg ett offset-läge i
`measureCase()`: `a[2]` = extra px läggs till `'center'`-beräkningen, `a[3]` = ih-tröskel
under vilken offset:et aktiveras. Hōrais citat-ankare blir
`['#quote-section', 'center', -100, 700]` — vid 390 (ih≈568<700) skiftar ankaret 100px
ovanför sant centrum; vid 768/1440 (ih redan uppmätt godtyckligt högre än 700 i tidigare
rundor) förblir tröskeln ouppfylld och ankaret exakt sant centrerat, som i dag. Ingen
ändring vid 1440 by construction (villkoret är på ramens EGEN uppmätta höjd, inte
brytpunkt i CSS).

## Fix 2 (HIGH) — tomt blått band i tesbandet vid 390

`.thesis-figure` ärver `align-self:end` (bas-regeln, rad 628, aldrig återställd i
`@media (max-width:767px)`). Grid-raden (`grid-row:3`, `1fr`) är hög, men align-self:end
gör att figuren bara tar sin EGEN innehållshöjd och läggs i radens underkant — figurens
flex-container (`display:flex;flex-direction:column`) får då ingen definit höjd, så
`.thesis-photo-box{flex:1;min-height:0}` har inget fritt utrymme att växa in i och faller
tillbaka på sin `aspect-ratio:16/10` (bas-regeln, rad 629, också aldrig återställd) = 215px
hög bild. Resultat: ett tomt band ovanför den korta bilden, mätt 285px.

**Fix:** i `@media (max-width:767px)`, lägg `align-self:stretch` på `.thesis-figure` och
`aspect-ratio:auto` på `.thesis-photo-box`. Figuren fyller nu hela grid-raden, flex:1 får
fritt utrymme att växa in i, bilden fyller raden (object-fit:cover, redan satt, beskär utan
distorsion). Ingen av de nya reglerna läser `--sc-ps` — bilden flyttar sig inte mellan
meningarna.

## Fix 3 (HIGH) — Calyx steg 03: bildtexten hamnar under ramen vid 390

Ankaret `['#studio + section', 0]` siktar på sektionens EGEN topp, men första figurens
(`photo-1` + figcaption) topp ligger ~76px längre ner (sektionens egen padding/gap), och
figur+bildtext tillsammans är 484px höga (uppmätt direkt i `sites/calyx.html` vid 390×844:
`figTopAbs≈1631`, `capBottomAbs≈2115`). Vid nuvarande ih=450 räcker varken befintlig höjd
eller ankarplacering för att få hela figur+bildtext innanför ramen.

**Fix:** två delar. (a) Höj Calyx-radens (delade `.case-stage`-basregel) `58svh` till
`66svh` (517px ih vid 844, ≥484px behövda + marginal). (b) Byt Calyx steg 3-ankaret från
`['#studio + section', 0]` till `['#studio + section figure', 0]` — `querySelector` träffar
FÖRSTA figuren (photo-1 + dess bildtext), vars topp ligger precis vid sektionens
bildinnehåll i stället för sektionens yttre padding. Med ih=517 och ankare vid figurens
egen topp ryms figur+bildtext (484px) helt inom ramen (≈33px marginal).

Calyx-basregelns höjning till 66svh är delad med Hōrai INNAN Hōrai-overridet (72svh)
läggs till direkt efter — samma mönster som den redan befintliga
`.case--horai .case-stage{grid-template-columns:...}`-overriden vid desktop (rad 844).

## Gör

1. Kirurgiska `Edit` i `index.html`: (1) `.case-stage`-basregelns mobila `grid-template-rows`
   58svh→66svh + ny `.case--horai .case-stage{grid-template-rows:72svh minmax(0,1fr);}`-rad
   direkt efter. (2) `measureCase()` + `CASES`-arrayens Hōrai-ankare (offset-läge). (3)
   `.thesis-figure`/`.thesis-photo-box` i tesbandets mobila media query (align-self/
   aspect-ratio). Calyx steg 3-ankaret i `CASES`-arrayen. Copyn rörs inte.
2. Enskilda skärmbilder (inga kontaktark) vid 390 och 375 för `?preview=thesis-01..05`,
   `case-horai-03`, `case-calyx-03`, plus hjulsekvens genom samma lägen. Läs varje bild.
3. Samma lägen vid 1440, pixel-för-pixel mot `shots/astra-r8/ours/`-baslinjen. Oförändrat.
4. Kort grind: noll horisontell scroll 320–1920, `a11y_scan` vid 390, låst copy 15/15,
   grep noll tankstreck.
5. `NOTES.md` § V3d R9, tabell fix/mål/före/efter/bild.

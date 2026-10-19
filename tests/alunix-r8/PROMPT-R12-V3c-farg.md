# Alunix r9, runda 12. Cell {{KONCEPT}}. Calyx får sin färg i sista steget.

En plan. Antons beställning 2026-09-17: Calyx ska inte vara svartvit, den får vara gråskala
under ritningsprocessen men ska få sin färg i den färdiga versionen i sista steget.
Ut-mapp `{{UT_MAPP}}`, port {{PORT}}.

## 0. Läs först

1. `{{UT_MAPP}}/plans/046-calyx-far-sin-farg.md` i sin helhet. Varje värde står där: fönstret
   (`--k6`, steg 06, med skälet mätt i pixlar), Target A (färgfilen ensam med
   `filter: grayscale(calc(1 - var(--k6)))`), fallbacken Target B (två `<image>`, grå som
   basskikt, färg på `opacity: var(--k6)`), A/B-protokollet med **två** fönster, gränsen
   5 ms p95 vid cpu 1, invert-lägets dämpning och preview-golven.
2. `{{UT_MAPP}}/plans/README.md` § R12 och `{{UT_MAPP}}/assets/ASSETS.md` (assetet
   `demo-calyx-1440-color.webp`, 1076x606, 79 178 B, vendorat av lead, F-009: du hämtar
   ingenting själv och genererar ingenting).
3. `{{UT_MAPP}}/NOTES.md` § Copy-gaten: en copy-agent har just skrivit om fjorton synliga
   rader i filen. **Radnumren i planen är ungefärliga.** Hitta varje ankare med `Grep` på
   dess kod och STOPPA med en rad i NOTES om koden inte matchar planen i sak.
4. `Skill(design)` som första handling, `Skill(animate)` och `Skill(emil-design-eng)` före
   filterändringen. Via `Skill`-verktyget, namngivna i transkriptet.

## 1. Bygg

Planens Steps i ordning. Kirurgiska `Edit`-anrop på `{{UT_MAPP}}/index.html`, aldrig `Write`
av hela filen, aldrig shell-skrivningar mot UI-filer. Motorn `scroll/scrollcraft.js`,
`scrollcraft.css` och `sites/*` rörs aldrig.

Två gränser planen namnger och som du inte får gå över:
- `filter: grayscale(1) contrast(1.05)` finns på **två** ställen. Det andra är
  `.thesis-photo-box img`, Hyperborea-plåten i tesbandet, och den rörs aldrig.
- `--kN` registreras **inte** med `@property`. Det som måste vara registrerat är `--sc-ps`,
  och det är det redan.

## 2. Mät, innan du kallar något klart

1. **Grå-ekvivalens:** stegen 01 till 05 ska se ut exakt som före ändringen. Färgfilen och
   gråskalefilen har praktiskt taget identisk luminans (mean 0,545 mot 0,544, p95 0,941 mot
   0,941), så en skillnad där är implementationen, inte assetet. Mät bildrektangelns mean
   luminans i steg 05 före och efter.
2. **A/B i två fönster**, som planen föreskriver: steg 06 (vinsten) och kontrollfönstret i
   steg 05 (påståendet att filtret kostar i vila). Sammanflätade par, ren kontroll emellan,
   tre par, median. Gräns 5 ms p95 vid cpu 1, `max_step ≤ 3 %`, staircase 0. Är Target A
   mätbart dyrare i kontrollfönstret: bygg Target B i stället och skriv båda serierna.
3. **Invert-läget:** dämpningen ska vara det **minsta** som får texten att behålla skärmen.
   Planens 0,34 är en gräns, inte ett mål: räcker en `brightness()` nära 1, är det rätt svar.
   Skriv vilket värde som blev fallet och varför, med mean och p95 redovisade. Pappersläget
   dämpas aldrig.
4. **Monotoni:** tolvstegs ramsekvens genom övergången med bildrektangelns mean chroma mätt i
   varje ram. Kurvan ska vara monoton och inget steg större än 20 % av totalspannet.
5. Preview-golv: mean chroma ≥ 12 i steg 06 och 07, gråskala i 01 till 05, båda bredderna,
   båda lägena.
6. Hela grinden ur `PROMPT-R11-V3c-loop.md` § 2: `motion_probe` med kontrollprotokollet,
   `scroll_verify`, `perf_probe` (sidvikten växer med assetets storlek, inte mer),
   `preflight_taste`, `contrast_over_media`, a11y-triaden, grep-kontrollerna.

## 3. Invarianter

F-011, F-014, gate 47/79 (bilden är en riktig produktyta, aldrig en ritad sida), gate 75,
låst copy 15/15 ordagrant (copy-gaten är körd, rör ingen sträng), `PRODUCT.md` § absences,
ingen tredje iframe, ingen generering. Fullständig output; `[PAUSED — steg X]` som sista rad
om du måste pausa.

## 4. Leverans

- `{{UT_MAPP}}/index.html`, `{{UT_MAPP}}/shots/r12/papper/` och `{{UT_MAPP}}/shots/r12/invert/`
  med parvisa filnamn: steg 05, 06 och 07 vid 1440 och 390, plus ramsekvensen.
- `{{UT_MAPP}}/NOTES.md` § R12: vilken target du byggde och varför, alla tal ur § 2, F-007
  mot planens målbild, avvikelser med skäl.
- `{{UT_MAPP}}/BRIEF.md` § decision ledger: raden planen anger.

Sista raden: `R12 klar` eller `[PAUSED — steg X]`.

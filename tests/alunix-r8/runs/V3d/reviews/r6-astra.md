fix

## persistence
Egna färska par-bilder i `shots/astra-r6/`: 16 rader vid 1440 och 390, en skärmbild per sida (`ours/`, par-bilderna `P01-1440.png` till `P15a-390.png`, kontaktark `sheet-ours-1440.png` / `sheet-ours-390.png`). Varje läge nåddes med `mouse.wheel` från toppen i en ren sida, 2,5 s vila och väntan på synliga bilder (`capture.py`, landade lägen i `positions.json`). Kontrollen av r5-fixarna: `verify.py` → `verify.json`:
- Hjulsekvens var 40:e px, 13760 till 14440, vid 1440: `strip-exit-1440.png` plus `exit-<y>.png`.
- Steg 05/06/07 vid 390 och 768, både i preview och med hjul: `steg-<w>-process-0x.png`.
- `.giant` vid 768/1024/1280/1440/1920, i preview-ledger, med hjul och i scrub 0.
- Mätning av bandgridden 768 till 1024: `band768.py`.
- Zoomer: `zoom-390-07-rev.png`, `zoom-390-06-sheet.png`, `zoom-P13-1440-rev.png`.

Codex körde en gång (`gpt-6-astra`, reasoning medium, read-only, 24 bilder). Bilderna var P01 till P15a och kontaktarket vid 1440, P03/P04/P12/P13/P15a och kontaktarket vid 390, `zoom-390-07-rev` och `steg-768-process-07`. Prompten finns i `prompt.txt` och svaret i `codex-out.txt`. De 390-rader som Codex inte fick som par (P01, P02, P05 till P11 och P14) läste jag själv i `sheet-ours-390.png` och i par-bilderna.
- **Paritetsrader:** 16 kom tillbaka, och 15 håller enligt både Codex och min läsning. P13 håller inte, och det är verifierat i mått och zoom.
- **Kodfynd:** 2 kom tillbaka och båda är verifierade: bandgridden vid 768 till 1023 och mobilens revisionsfält. Båda hade jag hittat själv innan Codex svarade, och Codex bekräftade dem oberoende.
- **r5-fixarna:** Codex bedömde dem som 3 stängda och 1 delvis öppen. Min läsning är densamma.
- **Släppt:** 0.

## fidelity
**PARITET, en rad per skärm:**
- **P01 fold: håller nivån.** Heron och kortet äger folden vid båda bredderna. Oförändrad sedan r5.
- **P02 kortets baksida: håller nivån.** ALUNIX i displaystorlek på kortet och tom grund runt om.
- **P03 tesbandet: håller nivån.** Rubriken och Hyperborea-bilden väger lika vid 1440. Vid 390 står rubrik, text och bild i ett blått band.
- **P04 jätten inverterad: håller nivån.** Detta är nytt i R6.
  - `?preview=ledger` och hjul till 4050 ger samma läge. h2 är 116 px på två rader, och rubrikblocket är 263 px, alltså 29,2 % av viewportens höjd. Det är större än kapitelrubriken (103,68 px).
  - Hela h2 syns i viewporten, plåten är 1285 px vid top 100 och liggaren 01 till 03 är läsbar (`P04-1440.png`).
  - Vid 390 är rubriken en tvåradig display överst på en svart plåt.
- **P05 Hōrai-bandet: håller nivån vid 1440.** Vid 390 kapas Hōrais undertitel inuti iframen. Det ligger i `sites/horai.html`, som enligt lead aldrig rörs, så det är noterat och inte räknat.
- **P06 kapitelskärmen: håller nivån.** Mörk, ensam skärm, 104 px respektive 56 px.
- **P07 steg 01: håller nivån.** Arket 81 % vw vid 1440. Vid 390 ligger arket överst och siffran och texten under.
- **P08 steg 02: håller nivån.** Måttkedjan 320/768/1440 läses på avstånd vid båda bredderna.
- **P09 steg 03: håller nivån.** Ett kapitel per skärm.
- **P10 steg 04: håller nivån.** "96 PX" och hatchen står inom arket vid 390.
- **P11 steg 05: håller nivån.** Calyx står i gråskala i arket, utan föräldralösa linjer. `#p-glyph` har redan opacitet 0 vid 390.
- **P12 steg 06: håller nivån.**
  - Vid 1440 är Calyx i färg ≥ 960×540.
  - Vid 390 har `#p-glyph` opacitet 0, `.p-live` är 16..374 i ett ark på 16..374 (ingen beskärning) och inga streck syns ovanpå fotot (`zoom-390-06-sheet.png`).
- **P13 steg 07: håller inte.**
  - Vid 1440 håller den: "A" står i revisionsfältet utanför fotot (`zoom-P13-1440-rev.png`).
  - Gapet vid 390: `#p-rev` har y 14..32 i viewporten medan `.p-live` börjar på y 30. Fältets underkant ligger alltså 2 px in på Calyx gräddvita navigeringslist (`zoom-390-07-rev.png`, underkanten på den hatchade rutan).
  - Därför läses revisionsfältet som en stämpel på bilden och inte som en detalj på arket, och r5:s Expected ("#p-rev utanför .p-live") uppfylls inte.
- **P14 Hur vi tänker: håller nivån.** Papper i full bredd, och båda halvorna bär.
- **P15 pris + kontakt: håller nivån.** Samma som r3 och r5: rubriken står halvt kapad i sista viewporten, men avslutet ryms helt i läget före.
- **P16 hela sidan: håller nivån.** Materialbytena är foto, blått, svart plåt, ritbordet, papper och foto. Fyra-skivor-gränsen är struken.

**r5-fixarna:**
1. **Mobilarket 06/07: delvis stängd, fortfarande öppen.**
   - Ritmärket har tonat ut (opacitet 0 i 05/06/07 vid 390), och `.p-live` är lika bred som arket (358 px), alltså ingen beskärning.
   - Revisionsfältet flyttades till y 2..18. Men `#p-cam`-zoomen 1,05 kring y 100 lyfter öppningens överkant från 20 till 16 enheter, så fältet överlappar fotot med 2 enheter (2 px).
   - Vid 768 är mobilarket rent. Det använder skrivbordets koordinater, och `#p-rev` 437..449 ligger ovanför `.p-live` 451.
2. **Revisionsbokstaven vid 1440: stängd.** `index.html:2689` är `[861,13,296,13]`, och "A" står i fältet (`zoom-P13-1440-rev.png`). Inget "A" syns över Calyx i hjulbilderna 13760 till 14440.
3. **Aktens utgång vid 1440: stängd.**
   - Band 07 släpper vid 14160, `.process-stick` vid ~14195.
   - I varje ruta i `strip-exit-1440.png` rullar "07", FÖRVALTNING och brödtexten ut i överkant och skärs aldrig av arket. Mätningen gav noll textelement som korsar arkets överkant.
4. **Jättens rubrik i displayskala: stängd.**
   - Vid 1440 är h2 116 px, 29,2 % av höjden, helt i viewporten.
   - 0 delade ord vid 768 (38,8 px), 1024 (85,8 px), 1280 (104,7 px), 1440 och 1920 (116 px), både i scrub 1 och scrub 0.
   - Liggaren är läsbar i båda scrubbändarna.

## ceiling
- **Motor och shim:** n/a. Allt som rör sig läser `--sc-ps`, och motorn är orörd. F-011 respected.
- **Referenserna:** hoy ger varje kapitel en viewport och ett dominerande element. Det når V3d nu i 15 av 16 rader, jätten inräknad.
- **Kvar under referensen:** revisionsfältets 2 px vid 390, och stegbandet vid 768 till 1023. Bandet är ingen PARITET-kolumn, men där ligger text ovanpå text.

## material_fixes
1. **Stegbandet vid 768 till 1023 px: brödtexten ligger ovanpå siffran och noten i alla sju steg.** Orsak: `index.html:1135` (`.step-band .process-p{grid-column:1 / -1;}`) ändrar kolumnen men ärver `grid-row:1 / span 2` från `:1122`. Stycket delar alltså celler med `.ledger-num` och `.process-note`, och rubriken trycks ner under dem. Mätt vid 768: siffran har y 31..103 och stycket 31..112 till 167. Samma överlapp finns vid 900 och 1023, men inte vid 1024. Syns i `steg-768-process-07.png` (övre 0..235 px: "07" ovanpå "Vi finns kvar…", noten ovanpå stycket) och `steg-768-process-05.png`. Det syns också i leadens eget `shots/r6/sheet-steps0607-768.png`, som NOTES R6 kallar "bekräftat rent". Åtgärd: i `@media (max-width:1023px) and (min-width:768px)` sätts `.step-band .process-p{grid-row:3;}`, eventuellt med titeln explicit på `grid-row:1`. Expected, `?preview=process-01..07` vid 768, 900 och 1023: noll skärningar mellan rektanglarna för `.ledger-num`, `.process-step-title`, `.process-note` och `.process-p` i alla sju band. Om bandet blir högre måste `--band-h` räknas om (measureAct gör det redan).
2. **Mobilens revisionsfält korsar fotot med 2 px (P13-390).** `index.html:1502-1503` sätter fältet till y 2..18. `:1519` skalar `#p-cam` med 1,05 kring y 100, så öppningens överkant hamnar på 100 + (20 − 100) × 1,05 = 16. Åtgärd: flytta fältet till y 0..15 (till exempel `M280 0 H312 V14 H280 Z` och `y:0; height:14px`). Ett alternativ är att låta fältet dela `#p-cam`s transform, eller att sätta skalans transform-origin så att öppningens överkant står still (`160px 20px`). Mobilvärdet för bokstaven i `:2689` justeras så att "A" står i fältets mitt. Expected, `?preview=process-07` och hjulscroll genom steg 07 vid 390: underkanten på `#p-rev`s rect ligger minst 1 px ovanför överkanten på `.p-live`s rect, `#p-c-rev` ligger helt inuti `#p-rev`, och `.p-live` är fortfarande ≤ 358 px bred.

## keep
- **Jätten:** `font-size`-höjningen bunden till `--scrub` (`:942`) ger 116 px vid 1440 i ledger-läget och 88 px i den smala startspalten, med 0 delade ord vid alla fem bredder. Plåten är 1285 px vid top 100.
- **Aktens utgång:** `.process-steps{padding-bottom:80svh}` (`:1107`) gör att band 07 släpper före arket.
- **Mobilarket:**
  - `#p-glyph{opacity:var(--cam-fade)}` (`:1513`).
  - Zoomen 1,05 (`:1519`), som ger Calyx hel i arket utan kantbeskärning.
- **Revisionsbokstaven på skrivbordet:** `[861,13]` (`:2689`).
- **Kapitelskärmen och tesen:** som i r5, orörda och fortfarande på nivån.
- **Motion:** allt som rör sig läser `--sc-ps`, och motorn och shimen är orörda. F-011 respected.

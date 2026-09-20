fix

## persistence
Egna färska par-bilder i `shots/astra-r5/`: 16 rader vid 1440 och 390, en skärmbild per sida (`ours/`). Varje läge nåddes med `mouse.wheel` (120 px per 45 ms) från toppen i en ren sida, därefter 2,5 s och väntan på synliga bilder. Målpositionen för preview-raderna lästes ur preview-lägets egen scrollY i en separat sida. Positioner: `capture.py`. Parbilderna är `P01-1440.png` till `P15a-390.png`, kontaktark `sheet-ours-1440.png` och `sheet-ours-390.png`. Kompletterande underlag:
- DOM-mått i sju lägen per bredd: `measure.py`, utdata i `measure.json`.
- Hjulsekvenser genom aktens utgång: `strip-d-exit.png` (13500 till 14220 i steg om 80) och `strip-m-0607.png` (9300 till 10740 i steg om 160). Klippsonden i `exitprobe.py` går i steg om 20 px.
- Zoomer: `zoom-P12-390-sheet.png`, `zoom-P13-390-sheet.png`, `zoom-exit-14140-14220.png`, `zoom-P13-1440-revfield.png`, `zoom-P14-1440-top.png`.

Codex körde en gång (`gpt-6-astra`, reasoning medium, read-only, 24 bilder: P01 till P15a och kontaktarket vid 1440, P02/P03/P05/P06/P10/P12/P13 vid 390 och `zoom-P13-390-sheet`). Prompt och svar finns i `prompt.txt` och `codex-out.txt`. Svaret gav 16 paritetsrader och 5 kod-/pixelfynd.
- **Paritetsrader: 13 överens med min läsning, 3 underkända (P04, P12, P13). Alla tre verifierade.**
  - P04 mätt: `.giant` 88 px, en rad 81 px hög, alltså 9 % av viewportens höjd, mot kapitelrubriken 103,68 px.
  - P12 och P13 sedda i zoom och mätta, se material_fixes 1.
- **Kodfynd: 4 av 5 överlevde som egna fynd, 1 slogs ihop.**
  - Revisionsbokstaven på skrivbordet: `:2625` mot `:1931`. Mätt: `#p-c-rev` har x/y 54/451 och rect 191,807 vid `process-07`. Synlig i `zoom-P14-1440-top.png`. Fältet är tomt i `zoom-P13-1440-revfield.png`.
  - Mobilens revisionsblock: `:1461-1462` mot öppningen på `:1454`. Syns i zoomen.
  - Mobilens ritmärke: `:1858`, `translate(24,24)`. Syns i båda zoomerna.
  - Mobilzoomen bredare än arket (`:1463`, 304 × 1,08 = 328 > 320). Mätt: `.p-live` 367 px mot arket 358 px vid `process-06/07`. Kanterna kapas ~5 px per sida. Det är för litet för en egen punkt, så jag slog ihop det med fynd 1.
  - Hōrai vid 390: bara noterat, enligt lead.
- **Codex påstod "inga kapade processglyfer", och jag behåller mitt fynd mot det.** Codex fick inte utgångssekvensen. I min hjulsekvens står "07" och tredje brödtextraden halvt täckta vid scrollY 14040 till 14160 (se material_fixes 3).
- **Släppt: 0.**

## fidelity
**PARITET, en rad per skärm:**
- **P01 fold: håller nivån.** Heron och kortet äger folden vid båda bredderna.
- **P02 kortets baksida: håller nivån.** ALUNIX tar ~41 % av kortets bredd (367 av 896 px, 103 px enligt NOTES). Kortet står som objekt med tom grund runt.
- **P03 tesbandet: håller nivån.** Rubriken är 64,8 px, panelen 720 av 900 px (80 %) och bilden 587 px (40,8 % vw). Rubrik och bild väger lika. Panelen är 45 % vw och inte full bredd, men det motsvarar r3:s Expected (höjdägande) och är inget nytt gap.
- **P04 jätten inverterad: håller inte.**
  - Bredden är löst: plåten är 1285 px vid top 100, och hela rubriken syns.
  - Gapet: rubriken är 88 px (`:916`), en rad 81 px hög, alltså 9 % av viewportens höjd. Det är mindre än kapitelrubriken (103,68 px).
  - Liggarens tre rader tar resten av plåten och konkurrerar med rubriken.
  - PARITET kräver sidans starkaste typografiska ögonblick efter heron. Referensens rubrik tar ~44 % av höjden.
- **P05 Hōrai-bandet: håller nivån vid 1440.** Vid 390 kapas undertiteln ("RESTAURANT, STOCKHO"). Det är r3-fix 7 i `sites/horai.html`, som enligt lead aldrig rörs. Noterat, inte räknat.
- **P06 kapitelskärmen: håller nivån.**
  - Mörk grund `oklch(0.21 0.022 250)`, rubriken 103,68 px vid 1440 och 56 px vid 390.
  - Kapitlet står ensamt (`.process-chapter` 900 respektive 844 px hög) och är vertikalt centrerat vid 390.
- **P07 steg 01: håller nivån.** Arket 1168 px (81 % vw). Vid 390 ligger arket överst och texten under, utan överlapp.
- **P08 steg 02: håller nivån.** Måttkedjan läses på avstånd vid båda bredderna.
- **P09 steg 03: håller nivån.** Ett kapitel per skärm.
- **P10 steg 04: håller nivån.** Hatchen och "96 PX" syns vid 390 (`#p-c-row` 61,131 inom arket 16..374 × 12..236).
- **P11 steg 05: håller nivån.** Calyx 839×473 i ett ark på 1168×657. Inga föräldralösa linjer: `#p-ledgers`/`#p-hatch` har opacitet 0.
- **P12 steg 06: håller inte.**
  - 1440 håller: Calyx 1071×603 i färg.
  - Vid 390 ligger ritmärket `#p-glyph` (~26×36 enheter) kvar i full ton över Calyx övre vänstra hörn och korsar dess header "VOL. IX" (`zoom-P12-390-sheet.png`). PARITET: "ritningen har dragit sig tillbaka".
- **P13 steg 07: håller inte.**
  - 1440 håller i komposition: revisionsfältet 41×22 px ligger utanför `.p-live`.
  - Bokstaven "A" hamnar inte i fältet på 1440. Den står på 191,807, över Calyx nedre vänstra hörn (`zoom-P14-1440-top.png`), och fältet är en tom hatch (`zoom-P13-1440-revfield.png`).
  - Vid 390 korsar revisionsblocket (`#p-title` 208..304 × 16..52, `#p-rev`) Calyx navigation och foto (`zoom-P13-390-sheet.png`, övre högra delen), och ritmärket ligger kvar.
- **P14 Hur vi tänker: håller nivån.** Papper i full bredd, och båda halvorna bär.
- **P15 pris + kontakt: håller nivån.** Samma som r3: rubriken kapas i sista viewporten, men allt ryms i ett tidigare läge.
- **P16 hela sidan: håller nivån.** Foto, blått, svart plåt, ritbordet, papper, foto. Den långa mörka akten är beställd, och fyra-skivor-gränsen är struken av lead.

**r3-fixarna:**
1. **Steg 07 stående scen: stängd vid 1440, öppen vid 390.** Vid 1440 står 07 färdigritat i hjulsekvensen från 13500 till 13980, och revisionsfältet ligger utanför `.p-live` och innanför arket. Vid 390 ligger revisionsfältet inuti `.p-live` (rect 249,30,107,13 mot live 11,27,367,207). Det är en R5-regression: öppningen flyttades till y 20, men `#p-title`/`#p-rev` stod kvar.
2. **Jättens bredd medan rubriken syns: stängd.** Plåten är 1285 px vid top 100, h2 syns helt, och `?preview=ledger` visar samma scrollY som organisk hjulscroll (4050).
3. **Kapitelskärmen ensam: stängd.** Inget från band 01 syns, kapitlet är mörkt enligt lead, och rubriken är 56 px vid 390, centrerad.
4. **Steg 04/06 vid 390: stängd i mått, öppen i renhet.** "96 px" står inom arket. Calyx är hel i 16:9 och tar 95 % av arkets yta. Ritmärket och den kapade kanten (1,08-zoom) gör ändå att P12-390 inte håller.
5. **Tesrubriken i displayskala: stängd.** 64,8 px, 80 % av höjden, bilden 40,8 % vw.
6. **ALUNIX på baksidan: stängd.** ~103 px, 41 % av kortets bredd.
8. **Glyffragment och föräldralösa linjer: linjerna stängda, glyffragmentet öppet med ny mekanism.** Vid 1440 släpper `.process-stick` vid ~14000 och glider upp över band 07, som står sticky på top 0 till ~14160. Därför är "07" och tredje brödtextraden avskurna vid 14040 till 14160 (`zoom-exit-14140-14220.png`, rad 1). Detta är inget `--slit-p`-klipp, eftersom `clip-path` är `inset(0%)` hela vägen (`exitprobe.py`). Vid 390 rullar texten normalt in under det sticky arket.
- **Fix 7 (Hōrai-overflow):** inte tagen enligt lead, noterad under P05.

## ceiling
- **Motor och shim:** n/a. Allt som rör sig läser `--sc-ps`, och motorn är orörd. F-011 respected.
- **Referenserna:** hoy ger varje kapitel en viewport och ett dominerande element. Det når vi nu i P01 till P03, P05 (1440), P06 till P11, P14 och P15, och P12/P13 vid 1440.
- **Kvar under referensen:**
  - Jättens typografiska ögonblick (P04).
  - Renheten i mobilarket i steg 06/07.
  - Aktens utgång vid 1440.

## material_fixes
1. **Mobilarket i steg 06/07: ritningen ska dra sig tillbaka från produkten (P12-390, P13-390).** `#p-glyph` (`index.html:1858`, `translate(24,24)`) får vid ≤767 samma `--cam-fade`-tillbakadragning som `#p-guides`, eller flyttas ut ur öppningen (y 20..191). `#p-title`/`#p-rev` (`:1461-1462`, y 16..52) flyttas till den fria remsan ovanför öppningen (y 0..20) eller under den (191..200), inom 320 enheter. Mobilzoomen (`:1463`, `1 + 0.08*--cam`) sänks till ≤ 1,05 så att 304 × skala ≤ 320. Expected, `?preview=process-06` och `process-07` vid 390: inga streck ovanpå `.p-live`s rect, `#p-rev`s rect utanför `.p-live` och innanför arket, och `.p-live`s bredd ≤ arkets (358 px).
2. **Revisionsbokstaven hamnar fel på skrivbordet (P13-1440, P14-1440).** `MOBILE_TEXT['p-c-rev']` (`:2625`) har kvar skrivbordsvärdet [54,451] sedan före R4, och `plansch()` (`:2641`) skriver över markupens 861/13 (`:1931`). Sätt skrivbordsvärdet till [861,13]. Mobilvärdet ska ligga i centrum av det flyttade mobilfältet enligt fix 1. Expected, `?preview=process-07` vid 1440: `#p-c-rev`s rect ligger inuti `#p-rev`s rect (1270,215,41,22), och inget "A" syns över Calyx i hjulbilderna 13500 till 14800.
3. **Aktens utgång vid 1440: arket glider över ett stillastående band 07.** `.process-stick` (`:1059`) släpper vid scrollY ~14000, men band 07 (`.step-band`, `:1081`, sticky top 0) står kvar till ~14160. Låt bandet och arket släppa samtidigt. Ett sätt är att låta li 07 sluta där `.process-steps` padding-bottom (`:1074`) slutar, så att bandets sticky-behållare tar slut samtidigt med arkets. Ett annat är att följa `.process-stick`s släpp med samma offset. Expected: i en hjulsekvens var 20:e px från 13980 till 14240 vid 1440 är "07", "FÖRVALTNING" och brödtexten antingen hela eller rullar ut i överkant, och skärs aldrig av arkets överkant.
4. **Jättens rubrik i displayskala (P04).** `.giant` (`:916`, `clamp(2.1rem,7.4vw - 18px,5.5rem)`) ska vara ≥ 110 px vid 1440 i ledger-läget, alltså större än kapitelrubrikens 103,68. Två rader inom plåten på 1285 px är tillåtet. Skalan kan bindas till `--scrub`, så att det smala startläget (555 px spalt, PLAN 030:s ordbrytning) inte bryter ord. Expected, `?preview=ledger` vid 1440: h2 ≥ 110 px, rubrikblocket ≥ 25 % av viewportens höjd, hela h2 inom viewporten och 0 delade ord vid 1024/1280/1440/1920. Liggaren 01 till 03 ska vara läsbar i scrubbens slutläge.

## keep
- Kapitelskärmen som egen mörk skärm i full höjd, 104/56 px, ensam.
- Jättens plåt på 1285 px vid top 100, där `?preview=ledger` och organisk scroll ger samma läge.
- Tesen: 64,8 px, panel 80 % av höjden, bild 40,8 % vw, noll delade ord.
- Mobilarket på 320×200 med öppningen exakt 16:9 (304×171): Calyx hel, "Botanical architecture, from Stockholm." obeskuren. Bara det som ritas ovanpå och zoomfaktorn ska ändras.
- Steg 07 vid 1440: stående scen från 13500 till 13980, med revisionsfältet utanför `.p-live`.
- `#p-ledgers`/`#p-hatch` × `--cam-fade`: inga föräldralösa linjer i 05.
- Allt som rör sig läser `--sc-ps`. Motorn och shimen är orörda. F-011 respected.

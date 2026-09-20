fix

## persistence
Egna bilder i `shots/astra-r7/`. Varje läge nåddes med `mouse.wheel` från toppen i en ren sida, en skärmbild per sida, och ramarna var laddade (`capture.py`, `settle_media` väntar på iframe-load och synliga bilder). Par-bilder `Pxx-1440.png` / `Pxx-390.png` finns för alla PARITET-rader utom P05, som är utgången. Tesbandet, casen och bryggan har egna bilder vid 768 i `ours/*-768.png`.

Mätsvep (`sweep.py`, resultat i `sweep-*.json` och `sweeps.log`):
- **Tesbandet:** hjul i steg om 40 px ner och upp vid 1440, 768 och 390 (`thesis-<w>/`). Varje .ts fick sitt synliga clip-fönster räknat ur aktens `--sc-ps` med sidans egen formel.
- **Casen:** hjul i steg om 60 px genom `#case-calyx` och `#case-horai`, ner och upp, vid 1440 och 390 (`cases-<w>/`). Jag mätte ramens `contentWindow.scrollY` och jämförde fram och bak i vila vid 10/30/50/70/90 %.
- **Hela sidan:** hjul i steg om 150 px vid 1440 och 390 (`whole-<w>/`, `sheet-whole-*.png`). Rubrikkollisioner kontrollerades med `elementFromPoint`, och horisontell scroll mättes.
- **Geometri:** `measure.py` → `measure.json`.

Codex (`gpt-6-astra`, medium, read-only) körde en gång med 24 bilder. Prompten ligger i `prompt.txt` och svaret i `codex-out.txt`.
- **Kodfynd:** 8 kom tillbaka och 7 överlevde verifieringen.
- **Omformulerat:** fynd 8 ("steg 01 syns i kapitelskärmen") är ett felsikte i `?preview=chapter`, inte ett sidfel. Hjulbilderna vid 1440 visar kapitlet ensamt före band 01. Det står som fix 8.
- **Släppt:** Codex läste P08–P10 som "evidence gap". Jag läste dem själv (`sheet-ours-1440-process.png`, `sheet-ours-390-rows.png`) och de håller. Codex kopplade också Hōrais fram/bak-avvikelse på 68–98 px till citatet. Den ligger vid 70 % (steget "Rummet") och inte vid citatet. Avvikelsen är liten, är borta efter en omätning, och hålls utanför material_fixes.

Leadens två fynd:
- **(a) bekräftat och bredare än leaden såg.** Det gäller alla fyra övergångar vid alla tre bredderna, inte bara 4→5. Max överlapp mellan de synliga fönstren är 130 px vid 1440, 62 vid 768 och 41 vid 390. Bilder: `thesis-1440/down-041.png` (SKÄRMEN MÖTER / INNAN ETT ORD ovanpå varandra), `down-021.png` och `thesis-390/down-039.png`.
- **(b) avfärdat.** `whole-390` gav 170 bildrutor med 0 rubrikkollisioner. I `strip-390-curtain-cases.png` står "Från samtal till lanserad sida." en gång per bild och blir avtäckt rent under ridåns kant, och "Så blev ritningen en sida." står ensam. Dubbleringen i `sheet-m0.png` kommer av att kontaktarkets celler (146×316) ligger kant i kant utan mellanrum, så underkanten på en bild läses ihop med överkanten på nästa (m09→m10, m16→m24).

Casens synk:
- Monoton i båda riktningarna, 0 bakåtsteg (Calyx 0 till 3920 / 5118 px, Hōrai 0 till 7161 / 8410 px).
- Fram och bak ger samma värde i vila vid alla punkter utom Hōrai 70 %, där skillnaden är 68 px vid 1440 och 98 px vid 390.
- Ingen tom ram. Horisontell scroll är 0 vid 390, 768 och 1440 i samtliga bilder.

## fidelity
- **P01 fold: håller nivån.** Oförändrad sedan r6. Heron och kortet äger folden vid båda bredderna.
- **P02 kortets baksida: håller nivån.**
- **P03 tesbandet: håller inte.**
  - Gapet, 1: i varje meningsbyte står två meningar med överlagrade glyfer i samma rubrikplats (`thesis-1440/down-041.png`, `thesis-390/down-039.png`). Beställningen var "mening för mening", och övergången är inte ren.
  - Gapet, 2: vid 1440 är Hyperborea 496×310 (34,4 % vw, målet ≥ 36 %) och står nere till höger, medan referensens bild står i höjd med rubriken (`P03-3-1440.png`).
  - Gapet, 3: vid 390 finns ett tomt blått band på ~220 px mellan meningen och strecken (`P03-4-390.png`).
  - I vila håller meningen: 88 px (390: 35,5 px), ensam och hel i sitt intervall.
- **P04 ridån: håller nivån.**
  - `P04-curtain-1440/390`: det blå lyfter av på en ren hårlinje, och kapitlet står stilla under.
  - `P04-chapter-390`: kapitlet står ensamt.
  - `P04-chapter-1440` visar band 01 i underkanten. Det är ett felsikte i preview (fix 8). Med hjul (`sheet-whole-1440-0.png`, rad 3) står kapitlet ensamt före 01.
- **P05:** utgången.
- **P06 kapitelskärmen: håller nivån.** Samma bilder som P04. Rubriken är 103,68 px vid 1440.
- **P07 steg 01: håller nivån.**
- **P08 steg 02: håller nivån.** Måttkedjan 320/768/1440 läses på avstånd vid båda bredderna.
- **P09 steg 03: håller nivån.**
- **P10 steg 04: håller nivån.**
- **P11 steg 05: håller nivån.**
- **P12 steg 06: håller nivån.**
- **P13 steg 07: håller nivån.** Revisionsfältet ligger utanför fotot vid 390 (r6-fixen håller).
- **P14 case-kapitlet: håller nivån.** `.cases-title` är 103,68 px på papper i full bredd och läses som ett nytt kapitel (`P14-1440.png`).
- **P15 pris + kontakt: håller nivån.** Samma avslut som r6. Rubriken står kapad i sista viewporten vid 390, men avslutet ryms helt i läget före.
- **P16 hela sidan: håller inte.**
  - Gapet: Calyx-caset ska vara det ljusa fältet, men det står på heroens gråa fotografi (`sheet-whole-1440-1.png`, rad 1–2, och `strip-390-curtain-cases.png`, nedre raden).
  - Därför går rytmen papper → foto → svart plåt och inte papper → papper → svart plåt.
- **P17 case Calyx: håller inte.**
  - Gapet, 1: stagens grund är genomskinlig, så text och skena står på fotot i stället för papper (`P17-1/3-1440.png`, `P17-3-390.png`).
  - Gapet, 2: ramen är 806×789, det vill säga 56 % vw × 87,7 % vh (målet ≥ 58 % × 88 %). Vid 390 är ramen 400 px, 47 % vh (målet ≥ 50 %).
  - Gapet, 3: stegbytena överlagrar två stycken med 9 px.
  - Synken håller (fram och bak lika).
- **P18 bryggan: håller nivån.** Rubriken är 80 px (390: 40 px) på svart, ensam (`P18-1440.png`).
- **P19 case Hōrai: håller inte.**
  - Gapet, 1: vid `-03` står citatet halvformat. "料理は対話である" är dämpat och "COOKING IS A CONVERSATION" suddigt, vid båda bredderna (`P19-3-1440.png` och `P19-3-390.png`, ramens nedre del).
  - Gapet, 2: stegbytena överlagrar stycken (`cases-1440/case-horai-down-042.png`, "står i klassiska versaler" ovanpå "besökaren en paus").
  - Spegelkompositionen håller.
- **P20 Hōrai → priset: håller nivån.** Kanten mellan svart plåt och fotot är ren, och "Alla har rätt till bra design." kommer utan tomt band (`P20-1440.png`).

## ceiling
- **Motor och shim:** n/a. Allt som rör sig läser `--sc-ps`, motorn är orörd, `sites/*` är orörda. F-011 respected.
- **Referenserna:** hoy låter ett kapitel äga en viewport med en rubrik i taget. V3d når det i vila i 15 av 20 rader. Gapet är övergångarna (tes och casesteg) och Calyx-grunden. Kompositionen är inte gapet.
- **Hōrais eget citat:** `sites/horai.html:430–434` formar citatet när sektionen står centrerad i ramens viewport. Sidan (`index.html`) siktar på fel punkt, se fix 4.

## material_fixes
1. **Tesens meningsbyte ska vara exklusivt, `index.html:602–607`.** Mätt: `--in` och `--out` öppnar och stänger samtidigt kring `b` (fönster `f/2` åt båda håll), och translateY ±0,55em lägger ut- och inkommande mening i samma rad. Två meningar syns samtidigt i alla fyra övergångarna, med överlapp 130 px vid 1440, 62 vid 768 och 41 vid 390 (`thesis-1440/down-041.png`). Expected: utgående mening är helt stängd innan inkommande öppnar, till exempel `--out` över [b − f/2, b] och `--in` över [b, b + f/2]. I ett hjulsvep med 40 px-steg ska högst en .ts ha synlig yta per bildruta, och överlappet ska vara 0 vid 1440, 768 och 390 i båda riktningarna.
2. **Calyx-stagens grund, `index.html:797`.** Mätt: `.case--calyx{--bg:var(--bg);--ink:var(--ink);}` är en cyklisk deklaration, så `--bg` blir tom och `#case-calyx .case-stage` får `background-color: rgba(0,0,0,0)`. Den fasta `.ground` (fotot, rad 263) syns genom stagen (`P17-1-1440.png`, `P17-3-390.png`). Expected: raden tas bort eller pekar på papperstoken, så att `getComputedStyle(.case-stage).backgroundColor` blir `rgb(253, 251, 244)` och texten `--ink` (#16140f) vid alla bredder. Det ger också P16 sin ljusa sträcka.
3. **Casestegens byte, `index.html:823–828`.** Mätt: samma samtidiga fönster som i fix 1. Två `.cs` syns samtidigt med 9 px y-överlapp i varje övergång, för Calyx och Hōrai vid 1440 och 390 (`cases-1440/case-horai-down-042.png`). Expected: samma exklusiva sekvens som fix 1. Högst en `.cs` ska synas per bildruta, med 0 px överlapp, medan ramens scroll löper vidare.
4. **Hōrais citatankare, `index.html:2129`.** Mätt: `['#quote-section', -0.40]` lägger sektionens överkant 0,40 × ramhöjd under ramens topp. Där blir horai.html:s proximity ≈ 0,52 och citatet halvformat (`P19-3-1440.png`, `P19-3-390.png`). Expected: ankaret är sektionen centrerad i ramen, `offsetTop + (sektionshöjd − ih)/2`, vilket blir ≈ +0,15 vid `h-[130vh]`. Vid `?preview=case-horai-03` och med hjul till samma läge ska `#quote-jp` ha opacitet 1 och `#quote-text` ha `filter: blur(0px)` i ramen, vid 1440 och 390.
5. **Casens ramstorlek, `index.html:799–801` och mobilt `index.html:838`.** Mätt: `.case-wrap` är 806×789 vid 1440 (56 % vw, 87,7 % vh). Vid 390 är den 400 px (47,4 % vh), eftersom `52svh` delas med bildtexten. Expected: ramen själv ska vara ≥ 836 × ≥ 792 px vid 1440 och ≥ 422 px hög vid 390, med bildtexten budgeterad utanför de måtten, och flush mot sin kant i båda casen.
6. **Hyperboreas andel av tesbandet, `index.html:590`.** Mätt: `.thesis-photo-box` är 496×310 vid 1440 (34,4 % vw), och vid 768 är den 265×165 (34,5 % vw, 16 % vh). Expected: ≥ 519 px bred vid 1440, det vill säga ≥ 36 % vw, flush mot högerkanten och vid 768 samma ≥ 36 % vw. Rubrikplatsen ska behålla 88 px utan delade ord.
7. **Mobilens tomma band i tesbandet, `index.html:629`.** Mätt: `.thesis-lines` har min-height 7 × 0,98 × 35,5 px, alltså 243 px. Med meningar på 2–3 rader blir det ~220 px tomt blått mellan meningen och strecken (`P03-4-390.png`). Expected: platsen dimensioneras efter den längsta faktiska meningen vid 390 (4 rader, ≈ 139 px), strecken följer direkt under, och det frigjorda utrymmet går till bilden. Bilden ska inte flytta sig mellan meningarna.
8. **`?preview=chapter` siktar förbi kapitlets ensamma fönster, `index.html:2355`.** Mätt: `ridaY(150)` ligger 10 vh bortom hållarens 140 vh (100 lyft + 40 ensam, rad 870). Därför visar par-bilden band 01 i underkanten vid 1440 (`P04-chapter-1440.png`). Expected: målet ligger inom fönstret, till exempel `ridaY(120)`, och par-bilden ska visa 0 px av band 01 vid 1440 och 390.

## keep
- **Tesbandet:** 100 % vw × 100 % vh, alla fem meningar 88 px (390: 35,5 px), och gråskala som går till färg vid mening 3.
- **Ridån:** `#process{margin-top:-100svh}` plus sticky `.process-chapter` ger en stillastående kapitelrubrik och en ren hårlinjekant vid 1440 och 390.
- **Casens synk:** ramarna skrollas inifrån ur aktens lerpade `cur` (rad 1963–1971), monotont i båda riktningarna och lika fram och bak. Exakt 2 iframes, som monteras vid steg 05.
- **Kapitlen:** case-kapitlet (103,68 px på papper), bryggan (80 px på svart) och övergången från Hōrai till priset utan lucka.
- **Processakten:** P07–P13 är oförändrade och håller. Revisionsfältet ligger utanför fotot vid 390.
- **Grundnivå:** 0 horisontell scroll vid alla bredder. F-011 respected.

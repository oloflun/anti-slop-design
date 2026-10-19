fix

## persistence
Egna bilder i `shots/astra-r18/`: `capture.py` (r15:s verktyg med R17/R18-raderna) gav 32 lägen × 1920x930, 1440x900 och 390x844. Det blev 96 par-bilder `Pxx-<bredd>.png`, med hjulbilderna i `ours/`. Chromium kördes med `ignore_default_args=['--hide-scrollbars']`. Varje läge nåddes med `mouse.wheel` i en ren sida, en skärmbild per sida, och ramarna var laddade. Alla 96 landade exakt på målet (`positions-*.json`). Ramarnas `innerWidth-clientWidth` och `innerHeight-clientHeight` var 0 i båda iframes i varje fångst. Överlapp och övergångar är dömda i enskilda bilder, aldrig i kontaktark.

Mätningar (`measure18.py` → `measure18.json`, `edges18.py` → `edges18.json`, `bandshots.py`, `longtask18.py` → `longtask-*.json`):
- **Kantlinje runt ramarna:** en profil −3…+3 px över varje ramkant, med 40 punkter per kant, i P17-1, P17-5, P19-1 och P19-6 vid alla tre bredderna. Övergången går rakt från grunden (papper `253,251,244` / svart `11,12,14`) till sajtens egen yta. Det finns ingen mellanliggande linje på någon kant. Utanför högerkanten vid 1920/390 ligger rullningslisten.
- **Prissektionen på en skärm**, vid dokumentets slut: 1920x930 ger titel 136 / mailto-underkant 874 (≤ 906). 1440x900 ger 171 / 846 (≤ 876). 390x844 ger 52 / 794, alltså allt i en bild.
- **`microtext_scan.py --price-ledger`:** vid 390 finns bara kortbaksidans 4 (`Digital byrå`, `Design`, `Utveckling`, `System`). Vid 1440 finns samma 4 plus 3 × `span.label` i liggaren. De tre är klassnamnsträffar på låst säljcopy i 17 px, samma som i R17. Ingen ny småtext.
- **Halvklippta rubriker**, 20 px-hjul med r12:s clip-medvetna `SWEEP_JS`: 0 träffar i tes → ritning (154/149/140 bildrutor), 0 i Calyx → Hōrai (113/108/101) och 0 i Hōrai → pris (900 per bredd). Detta gäller vid 1920, 1440 och 390.
- **Glyfspringor mellan stegband:** 20 px-hjul genom alla sju band vid 1920 och 1440. I de bildrutor där två band syns samtidigt är det inkommande bandet i sin springa, under arkets yta. Bytesbilderna `ours/band-1440-{8960,9000,9100,9120,9960}.png` och `band-1920-{9260,9400,9420,10300}.png` är lästa en och en. Det avgående bandet klipps bara av viewportens överkant, och de sista 6–26 px är utfyllnad plus hårlinje, utan glyfer. 0 springor.
- **Horisontell scroll:** 0 vid 320, 375, 390, 414, 768, 1024, 1280, 1440 och 1920.
- **Delade ord:** 1 träff vid alla tre bredderna. Liggarens första etikett bryts "SEO-" / "optimering." (`P15-1920`, `P15-390`, fix 4). I övrigt 0.
- **Långa uppgifter under scroll**, 120 px-hjul över hela sidan: 5 vid 1440, 8 vid 1920 och 6 vid 390. **Alla** är iframe-monteringar, och ingen sitter i sidans egen kod.
  - Calyx monteras vid ingången till case-kapitlet (`#case`): 1440 ger 102 + 288 + 167 ms vid scrollY 15 840, 1920 ger 102 + 315 + 160 + 54 + 63 ms och 390 ger 120 + 244 + 149 + 64 ms.
  - Hōrai monteras **mitt i Calyx → Hōrai-övergången**: 383 ms vid 1440 (scrollY 21 720, mellan `case-seam-ground` 21 519 och `case-seam` 22 293), **646 ms** vid 1920 (scrollY 22 440) och 485 ms vid 390. Sedan följer 56–81 ms efterslängar (fix 3).

Codex (`gpt-6-astra`, medium, read-only) kördes en gång med 24 par (`prompt.txt`, `imgs.txt`, `codex-out.txt`). Det var 13 par vid 1920, 5 vid 1440 och 6 vid 390. Codex gav en rad per par (14 håller, 10 håller inte) och 8 fynd. Utfall:
- **2 fynd överlevde:** nr 1 (`.seam-h` 1 px, som jag hade hittat själv innan körningen) och nr 3 (för lätt linjevikt, omskriven till fix 2 med uppmätt kontrast).
- **6 fynd släpptes:**
  - **Nr 2** (de blå ursprungen nollas): plan 061 föreskriver det, med blått bara där linjen inte krockar med tickstrecken och linjerna i kanten vid 768/390.
  - **Nr 4** (arket 64 % vw vid 1920): verifierat, men det är r15:s fix 4, som ligger hos Anton (NOTES R16). Det står under fidelity och inte som fix.
  - **Nr 5** (Calyx-texten "torkas" bort): verifierat i `P22-text-1440`. Det är ändå den form plan 060 anger (klipp + 32 px), och svepet ger 0 halvklippta rubriker.
  - **Nr 6** (siffran 86 px vid 390 mot 150): PARITET:s 150 px gäller inte 390-kolumnen.
  - **Nr 7** (`.process-locked` som småtext): låst rad ur PRODUCT.md i 20–24 px, alltså brödtextstorlek. Den klarar F-016:s test.
  - **Nr 8** (kontakten 17 px vid 390): plan 060:s 390-kolumn anger 17 px, och 1920/1440 är uppmätta 21,1/19,4 px enligt målet.

## fidelity
Beställningarna, punkt för punkt:
- **Exempelcase i serif:** klar. Young Serif, ett ord på en rad (`P14-1920`, `P14-390`).
- **Sidramarnas kantlinje bort:** klar. Pixelprofilen ger 0 linjer vid alla tre bredderna.
- **Bryggan bort, Calyx → Hōrai med scrolleffekt:** klar i form. Textspalten lämnar, papperet blir svart medan ramen står still och det svarta andrummet är ~225 px (`P22-*`). Effekten fryser dock 0,4–0,65 s mitt i lager 2 när Hōrai monteras (fix 3).
- **Scrolleffekt in i priset:** klar. Slöjan framkallar fotot och rubriken är i oskärpa (`P20-in-1920`). Skarven är ren.
- **Prissektionen med roligare typsnitt, allt på en skärm:** klar vid alla tre bredderna (mått ovan).
- **"Pris vid förfrågan" och kontakten rätt storlek:** klar. 32 px mot 64 px vid 1920, och kontakten är 21,1 / 19,4 / 17 px.
- **All liten beskrivande text bort:** klar. Bara kortbaksidan finns kvar vid 390.
- **Hōrais bokning mindre text:** klar. Bokningen ligger helt inne i ramen (`P19-6-1920`).
- **Processtegen kortare i större text:** klar. 28 px vid 1440 och 32 px vid 1920, fullt bläck och rubriken i samma storlek (`P09-*`).
- **Övergången blått → ritning:** inte klar.
  - Den vågräta landningslinjen ritas inte. Den är 1 × 1 px vid alla bredder (fix 1). Det gäller även leadens egen `r18/seam-4-1920.png`, trots att NOTES R18 skriver "4 lodräta + vågrät synlig".
  - Linjerna är för svaga för referensens nivå (fix 2).

**Min dom om övergången blått → ritning: för återhållsam.**
- Rörelsen finns och är scrubbad. Men det enda som händer är fyra 1 px-linjer, och på det blå har de kontrasten **2,86:1** (`P04-t2-1920`, x 348: `141,173,204` mot `30,94,156`), alltså under 3:1 för grafik.
- Kanten mellan blått och mörkt är fortfarande en rak horisontell skarv, och den landning som skulle knyta ihop linjerna saknas.
- I `P04-t4-1920` och i leadens `1920-t04.png`/`t05.png` läses därför fyra lösa streck som hänger i luften ovanför rubriken, inte "tesen blir ritning i ett drag".
- Highway-referensen bär samma drag med en ~4 px accentlinje med ett markerhuvud. Vår motsvarighet är ungefär en fjärdedel så tung och har inget huvud.
- Den är synlig, men inte fin nog och inte i nivå med Antons "fin övergång med en scrolleffekt".

**PARITET, rad för rad (1920 / 1440 / 390):**
- **P01, P02, P03-1…4:** håller vid alla tre bredderna. Detta är orört sedan R15, och bilderna är tagna.
- **P04 tes → ritning:** håller **inte** vid någon bredd (fix 1 och 2). 0 halvklippta rubriker, och linjernas x stämmer mot arket.
- **P06 kapitelskärmen:** håller vid alla tre bredderna (`P06-chapter-1920`).
- **P07–P13 stegen:** håller vid 1440 och 390. Texten är nu bandets största läsbara massa, och arket är 81 % vw vid 1440. Vid 1920 håller de **inte**, eftersom arket är 63 % vw (`ours/P09-1920.png`, x 348–1561). Det är r15:s fix 4, som enligt NOTES R16 ligger hos Anton och inte återöppnas här.
- **P14 case-kapitlet:** håller vid alla tre bredderna.
- **P15 och P21 pris + kontakt:** håller vid alla tre bredderna, med ett undantag: det delade ordet "SEO-optimering" (fix 4).
- **P16 hela sidan:** materialrytmen håller i enskilda bilder. Hård kant finns bara i P04, där den inte är tänkt (fix 1 och 2).
- **P17 Calyx och P19 Hōrai:** håller vid alla tre bredderna. Ramarna är flush, har ingen rullningslist och ingen kantlinje.
- **P20 Hōrai → pris:** håller.
- **P22 Calyx → Hōrai:** håller i bild vid alla tre bredderna. Under hjul fryser den (fix 3).
- **P23 Hōrais bokning:** håller.

## ceiling
- **Motor och shim:** n/a. `scrollcraft.js` är orörd, `sites/*` är orörda utom Hōrais bokningssektion, och det finns exakt två iframes. F-011 respected.
- **highway s03 (P04):** referensen låter en scrollritad tråd med vikt och huvud leda in i kapitlet. Vår tråd är 1 px utan huvud och saknar sin landning.
- **hoy (P07–P13 vid 1920):** referensens kapitel bär hela viewporten vid varje bredd. Vårt ark är höjdbundet vid 1920 (hos Anton).
- **Kända rester, noterade och inte fynd:** 813 `elementFromPoint`-träffar vid 390, där det sticky arket ligger över stegtexten, samma beteende sedan R1. Hōrais 390-överflöd i `sites/horai.html`.

## material_fixes
1. **Landningslinjen ritas som en punkt på 1 × 1 px.** `index.html:1161` `.seam i{…width:1px;}` har specificiteten 0,1,1 och vinner över `index.html:1174` `.seam-h{…width:calc(var(--x4) - var(--x1) + 1px)}` med 0,1,0. Uppmätt `getBoundingClientRect()` på `.seam-h` är 1 × 1 vid 1920, 1440 och 390 (`measure18.json`, `seam_h`). Pixelrader i `P04-t4-1920` / `r18/seam-4-1920.png` visar ingen linje mellan x1 och x4. Expected: en selektor med högre specificitet, t.ex. `.seam .seam-h{…}`. Kontroll: vid `tes-till-ritning-4` ska `.seam-h`-bredden vara 1214 / 1168 / 348 px vid 1920 / 1440 / 390, 40 ± 2 px ovanför `#process-title`. Pixelraden ska vara obruten från x1 till x4, och den geometriska kontrollen ska fortfarande ge 0 rubrikkorsningar.
2. **Övergången är för lätt för referensens nivå (P04), Antons "extremt platt" är inte stängt.** Det gäller `index.html:1161–1176`. Linjerna är 1 px, och `--seam-on-blue` ger 2,86:1 mot det blå. Expected, inom plan 061:s form och på samma `--tx`-klocka: arkets kantlinjer (`data-l="1"` och `"4"`) och landningslinjen 2 px, stationerna 1 px, och `--seam-on-blue` ≥ 3:1 mot `--c-accent`, mätt på renderade pixlar. Kontroll: i `tes-till-ritning-2` vid 1920 och 390 läses linjerna utan zoom som ritningens kanter, och i `-4` sluter de sig i landningslinjen (fix 1).
3. **Hōrai-ramen monteras mitt i Calyx → Hōrai-övergången, så den beställda scrolleffekten fryser 383 / 646 / 485 ms** vid 1440 / 1920 / 390 (`longtask-*.json`, scrollY 21 720 / 22 440 / 17 640, mellan `case-seam-ground` och `case-seam`). Orsaken är `index.html:2704–2714`: `rootMargin:'40% 0px'` på Hōrais wrapper träffar exakt när lager 2 spelar. Expected: Hōrais `mountFrame` körs i ett läge där ingen akt är mitt i en övergång, t.ex. köad med `requestIdleCallback` när Calyx står i steg 1–3. Ramarna ska inte transformeras och `sites/*` ska inte röras. Kontroll: `longtask18.py` ger 0 uppgifter > 50 ms mellan Calyx `--sc-ps` 0,80 och Hōrai steg 1 vid alla tre bredderna, och den totala antalet uppgifter blir inte fler.
4. **Delat ord i liggaren:** "SEO-" / "optimering." på två rader vid 1920, 1440 och 390 (`P15-1920`, `P15-390`, `measure18.json` `split`). Det gäller `index.html:2106`. Expected: ett icke-brytande bindestreck (`SEO&#8209;optimering`). Ordvalet är oförändrat. Kontroll: 0 delade ord i `.price-row` vid 320–1920.

## keep
- **R18:s stegband:** `--step-fs` 32 / 28,2 / 21,9 px, fullt bläck och rubriken i samma storlek i samma spalt. `--band-h` är 219 / 216 px och arket 81 % vw vid 1440. Tickern har 0 glyfspringor.
- **Blåkopians mekanik:** den nästlade flow-akten på `.process-chapter` med `--tx` ur `--sc-ps`, linjernas x ur arkets egna stationer (±1 px mot arket) och rubrikens bläckning 62 → 100 %. 0 halvklippta rubriker i hjulsvepet. Bara vikt och landning behöver åtgärdas.
- **Ramarna utan kantlinje:** `inset:-1px` och `snapCaseWrap` ger 0 linjer i pixelprofilen och 0 px rullningslist.
- **Prisenheten:** allt ryms i en bild vid alla tre bredderna, siffrorna i Young Serif bildar en rytm i högerkanten, "Pris vid förfrågan" har halva storleken och kontakten har handlingsform.
- **Calyx → Hōrai i bild:** ramen står still, grunden blir svart utan kant och andrummet är ~225 px. Bara monteringstiden behöver flyttas.

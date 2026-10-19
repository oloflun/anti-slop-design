fix

## persistence
Egna bilder och mått i `shots/astra-r8/`. Samma verktyg som r7 (`capture.py`, `sweep.py`), men `sweep.py` läser nu varje `.ts`/`.cs`:s **beräknade** `clip-path` (box-shorthand-parser, 1 till 4 token) i stället för att räkna om sidans formel, så mätningen följer koden som den faktiskt står. Varje läge nåddes med `mouse.wheel` från toppen i en ren sida, en skärmbild per sida, ramarna laddade (`settle_media`). Par-bilder `Pxx-1440.png` / `Pxx-390.png` för alla PARITET-rader (P05 utgången), 768-bilder i `ours/`. Alla kollisioner är dömda i enskilda skärmbilder, inga ark.

Mätsvep (`sw-thesis.log`, `sw-cases.log`, `sw-whole.log`, `sweep-*.json`):
- **Tesbandet, 20 px-steg ner och upp:** 1440 208/208 bildrutor, 768 236/237, 390 195/196. 0 bildrutor med två synliga meningar, 0 px överlapp.
- **Casen, 20 px-steg ner och upp:** Calyx och Hōrai vid 1440, 768 och 390. Totalt 2 874 bildrutor, 0 med två synliga steg och 0 px överlapp. Ramens scroll är monoton (0 bakåtsteg) i alla sex svepen. Fram och bak i vila är lika vid alla punkter utom Hōrai 70 % (68 / 86 / 91 px vid 1440 / 768 / 390). Det är samma lilla avvikelse som i r7, vid steget "Rummet", och den hålls utanför material_fixes.
- **Hela sidan, 150 px-steg:** 1440 201 bildrutor och 390 170, 0 rubrikkollisioner (`elementFromPoint`) och 0 horisontell scroll.
- **Mått (`measure8.py`, `measure8.json`, `q390.py`, `q390b.py`):** se fidelity.

Codex (`gpt-6-astra`, medium, read-only) körde en gång med 24 par-bilder: 20 vid 1440 och 4 vid 390 (`prompt.txt`, `imgs.txt`, `codex-out.txt`). De 390-par som inte bifogades läste jag själv, en bild i taget.
- **Fyra fynd kom tillbaka och tre överlevde** (Hōrai 390, tesbandet 390, Calyx 390 -03).
- **Släppt, fynd 4 ("prisrubriken kommer för sent i P20").** Rubrikens topp ligger vid ~68 % vh i `P20-1440.png`. Men det läget är konstruerat av mig: `capture.py` placerar `#pris` överkant exakt vid 50 % vh. Mellan kanten och rubriken finns inget tomt band, bara fotot med scrim som grund, och rubriken når övre halvan vid nästa hjulsteg. Koden är oförändrad sedan r7, där raden höll. Det här är inget sidfel.
- **Codex rad 22 (Calyx 390).** Omformulerat efter egen mätning: den andra bilden i paret kan inte stå bredvid den första, eftersom Calyx staplar bilderna på mobil. Det som går att stänga är att märkningen saknas, se fix 3.

Leadens egen kontroll (`lead-r8/sheet.png`, tesen vid 1440) stämmer med mina svep. Den täcker dock inte 390, och det är där de återstående fynden finns.

## fidelity
**r7-fixarna:**
- **Fix 1, tesbytet: stängd.** Överlappet är 0 px vid 1440, 768 och 390, i båda riktningarna och i alla 1 280 bildrutor. `index.html:615–617` har de asymmetriska fönstren.
- **Fix 2, Calyx-grunden: stängd.** `backgroundColor` är `rgb(253, 251, 244)` och ink `rgb(22, 20, 15)` vid 1440, 768 och 390 (`P17-1-1440.png`, `P17-3-390.png`: papper, inte foto).
- **Fix 3, casestegen: stängd.** 0 px överlapp, båda casen, tre bredder, båda riktningarna.
- **Fix 4, Hōrais citat: öppen vid 390.** Vid 1440 är citatet format och skarpt i ramen (`P19-3-1440.png`), och vid 768 syns det (jp y=233). Vid 390 har `#quote-jp` opacitet 1 och `#quote-text` blur 0, men båda ligger **ovanför** ramens synliga yta: jp y=-139..-114, citatet y=-58..53, och sajtens nav täcker 0..117. I `P19-3-390.png` syns bara bylinen "LINNEA BERGSTRÖM" på en nästan tom mörk ram. Se fix 1.
- **Fix 5, Calyx-ramen: stängd.** 922×807 vid 1440 (64,0 % vw, 89,7 % vh), 492×924 vid 768 och 451 px vid 390 (53,4 % vh).
- **Fix 6, Hyperboreas andel: stängd.** 534×334 vid 1440 (37,1 % vw) och 285 px vid 768 (37,1 %), flush mot höger.
- **Fix 7, tomt band vid 390: öppen, bandet har flyttat.** Mellan meningen och strecken är det nu 41 px, men mellan strecken (slutar y=258) och bilden (börjar y=543) står **285 px tomt blått**, 34 % vh, i alla fem meningarna (`P03-3-390.png`, `ours/P03-*-390.png`). Bilden är oförändrat 343×215. Se fix 2.
- **Fix 8, `?preview=chapter`: stängd.** Band 01 börjar y=1080 vid 1440 (vh 900) och y=1261 vid 390 (vh 844). `P04-chapter-1440.png` visar kapitlet ensamt.

**PARITET, rad för rad:**
- **P01 fold: håller nivån.** Oförändrad. Heron och kortet äger folden vid båda bredderna.
- **P02 kortets baksida: håller nivån.**
- **P03 tesbandet: håller inte.**
  - 1440 håller: meningen ensam i 88 px, Hyperborea 37,1 % vw flush höger, rena byten.
  - 390 håller inte: 285 px tomt blått band mellan strecken och bilden, och bilden är bara 25 % vh (`P03-3-390.png`). Referensen fyller skärmen med rubrik, text och bild utan dött fält.
- **P04 ridån: håller nivån.** Hårlinjekanten är ren vid båda bredderna, och kapitlet står ensamt i `P04-chapter-1440/390`.
- **P05:** utgången.
- **P06 kapitelskärmen: håller nivån.** Samma bilder som P04.
- **P07 steg 01: håller nivån.**
- **P08 steg 02: håller nivån.** Måttkedjan läses på avstånd vid båda bredderna.
- **P09 steg 03: håller nivån.**
- **P10 steg 04: håller nivån.**
- **P11 steg 05: håller nivån.**
- **P12 steg 06: håller nivån.**
- **P13 steg 07: håller nivån.**
- **P14 case-kapitlet: håller nivån.** Pappersgrund och rubriken i 103,68 px.
- **P15 pris + kontakt: håller nivån.** Som i r7. Rubriken är kapad i sista viewporten vid 390, men priser och adress bär avslutet.
- **P16 hela sidan: håller nivån.** Calyx-caset står nu på papper. Rytmen går foto → blått → ritbord → papper (kapitel och Calyx) → svart plåt (brygga och Hōrai) → foto (`sheet-whole-1440-1.png`, bara för rytmen). 0 kollisioner.
- **P17 case Calyx: håller inte, vid 390.**
  - 1440 håller: ram 64 % × 89,7 % på papper, och `-03` visar bildparet med två märkningar (y=449 och 579).
  - 390, `-03`: ramen är 451 px och visar ett enda beskuret foto. Märkningen som steget beskriver ("med en liten märkning under varje") ligger vid y=500, utanför ramens 450 (`P17-3-390.png`). Se fix 3.
- **P18 bryggan: håller nivån.**
- **P19 case Hōrai: håller inte, vid 390.**
  - 1440 håller: citatet formas skarpt i ramen, och spegelkompositionen håller.
  - 390, `-03`: citatet syns inte i ramen (fix 1).
- **P20 Hōrai → priset: håller nivån.** Kanten är ren och det finns inget tomt band (`P20-1440.png`). Codex fynd om rubrikläget är släppt, se persistence.

## ceiling
- **Motor och shim:** n/a. Allt som rör sig läser `--sc-ps`, motorn är orörd, `sites/*` är orörda. F-011 respected.
- **Referenserna:** hoy fyller varje mobilskärm med sitt innehåll. V3d gör det vid 1440 i alla rader. Vid 390 återstår tre skärmar där den inramade sajtens egen mobillayout eller en rad utan fyllnad lämnar skärmen utan det steget lovar.
- **Hōrais egen citatlayout** (`sites/horai.html:157–173`) är en `overflow-hidden`-sektion på 1000 px med en `sticky`-kolumn på 487 px, och `sticky` fastnar aldrig inom `overflow-hidden`. Vid en ram på 450 px kan citatet därför inte stå både format (sektionen centrerad) och synligt. Det är en egenskap hos sajten. Fixen måste göras på sidans sida, via ramhöjd eller ankare.

## material_fixes
1. **Hōrais citat vid 390, `index.html:2178` (ankaret `['#quote-section','center']`) och mobilraden `index.html:881`.** Mätt vid `?preview=case-horai-03`, 390×844: ramens `innerHeight` är 450, sektionen är centrerad, och `#quote-text` ligger på y=-58..53 och `#quote-jp` på -139..-114, bakom och ovanför navigationen (0..117). Formeln i ramen (`q390b.py`, sajten i ramens mått 390×450): `#quote-text`-topp = ih − 507,5 när sektionen är centrerad. När ankaret flyttas s px ovanför centrum blir det opacitet/blur 0,97/0,4 px vid s=100, 0,81/2,3 px vid s=200 och 0,64/4,3 px vid s=272. Expected: vid 390, i preview och med hjul till samma läge, ligger `#quote-text` helt inom [117, ih] med opacitet ≥ 0,95 och `blur` ≤ 0,5 px. Mätt krav: ih ≥ 625 om ankaret förblir centrerat, eller ih ≥ 525 om ankaret sätts 100 px ovanför centrum. 1440 och 768 ska vara oförändrade (i dag skarpt och synligt där).
2. **Tesbandets tomma band vid 390, `index.html:628` och `index.html:629`, samt mobilreglerna `index.html:649` och `index.html:654`.** Mätt: `.thesis-figure` ärver `align-self:end` från rad 628, så figuren sträcks aldrig över `1fr`-raden. `.thesis-photo-box` behåller `aspect-ratio:16/10` från rad 629, så `flex:1` växer aldrig. Bilden står kvar på 343×215 på y=543, med 285 px tomt blått ovanför. Expected, vid ≤767: figuren fyller rad 3 (`align-self:stretch`) och boxen tappar aspect-ratio (`aspect-ratio:auto`). Mätbart: avståndet från strecken till bildens överkant är 16–32 px, bilden är ≥ 400 px hög vid 390×844 med bildtexten kvar inom stagen, bildens y är lika i alla fem meningarna, och 0 horisontell scroll.
3. **Calyx `-03` vid 390, ankaret `['#studio + section', 0]` på `index.html:2176`.** Mätt: i ramen (ih 450, `contentWindow.scrollY` 1425) står första märkningen ("Cmsn. 0211 …") på y=500, alltså under ramen. Bara ett foto syns, utan märkning (`P17-3-390.png`). Expected: vid ≤767 får steget ett ankare, till exempel ett förskjutet värde eller ett `figcaption`-ankare, så att minst ett foto och dess märkning ligger helt inne i ramen, i preview och med hjul. 1440 ska vara oförändrad (två märkningar synliga i dag).

## keep
- **Bytena:** de asymmetriska `--in`/`--out`-fönstren i `.js .ts` och `.js .cs` (`index.html:615–617`, `863–866`). De ger exakt en synlig mening eller ett synligt steg i varje bildruta vid tre bredder, och mätningen läser den beräknade `clip-path`.
- **Calyx på papper:** grunden ärvs från `:root`, och den cykliska raden är borta. Det ger P16 sin ljusa sträcka.
- **Casramarna:** 64 % vw × 89,7 % vh vid 1440, 53 % vh vid 390, flush mot kanten, spegelvända för Hōrai.
- **Hyperborea:** 37,1 % vw vid 1440 och 768.
- **Ridån och kapitlet:** `ridaY(120)` i preview, den stillastående kapitelrubriken och hårlinjekanten.
- **Casens synk:** monoton, lika fram och bak (utom Hōrai 70 %, några tiotal px), exakt 2 iframes.
- **Grundnivå:** processakten P07–P13, bryggan och avslutet oförändrade. 0 horisontell scroll och 0 rubrikkollisioner vid alla bredder. F-011 respected.

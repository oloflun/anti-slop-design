fix

## persistence
Egna bilder och mått i `shots/astra-r10/`. Verktygen är r8:s, kopierade: `capture.py` och `sweep.py`. Nytt är `measure10.py` (fixarna vid 390 och 375, i preview och med hjul, samt horisontell scroll 320–1920) och `jump.py` (fotots överkant per hjulsteg genom tesbandet). Varje läge nåddes med `mouse.wheel` från toppen i en ren sida, med en skärmbild per sida och ramarna laddade (`settle_media`). Par-bilder `Pxx-1440.png` / `Pxx-390.png` finns för alla PARITET-rader (P05 är utgången). 375-bilder för P03, P17-3 och P19-3 ligger i `ours/`. Alla överlapp är dömda i enskilda skärmbilder, inga kontaktark.

Mätsvep (`sw-thesis.log`, `sw-cases.log`, `sw-whole.log`, `measure10.json`):
- **1440 mot `astra-r8/ours/`:** 27 av 27 bilder har 0 pixlar med differens över 40. P17-1 och P19-3 har var sin kantlinje på 12 px med differens under 40, alltså kantutjämning. 1440 är oförändrat.
- **390 mot `astra-r8/ours/`:** P01, P02, P04-chapter, P07–P14, P15a och P18 är pixelidentiska och behåller r8:s dom. Ändrade är P03 (alla fem meningarna), P04-curtain, P17, P19, P15b och P20 (bara ramens övre del). De är lästa en och en.
- **Tesbandet, 20 px-steg ner och upp:** vid 390 195/196 bildrutor och vid 375 188/189. 0 bildrutor med två synliga meningar, 0 px överlapp.
- **Casen vid 390, 20 px-steg:** Calyx 200/201 och Hōrai 238/239 bildrutor. 0 synliga dubbelsteg, 0 px överlapp. Ramens scroll är monoton med 0 bakåtsteg. I vila är fram och bak lika utom Hōrai 70 % (4826 / 4919, alltså 93 px), samma avvikelse som i r8 och fortfarande utanför material_fixes.
- **Hela sidan, 150 px-steg:** 1440 med 201 bildrutor och 390 med 170. 0 rubrikkollisioner (`elementFromPoint`).
- **Horisontell scroll:** 0 vid 320, 375, 390, 414, 768, 1024, 1280, 1440 och 1920.
- **Fotots position per hjulsteg (`jump.py`):** se fidelity och fix 1.

Codex (`gpt-6-astra`, medium, read-only) körde en gång med 24 bilder (`prompt.txt`, `imgs.txt`, `codex-out.txt`). 23 var par: 14 vid 390 och 9 vid 1440. Den 24:e var en ensam bildruta av hoppet. Codex gav en rad per par, 23 av 23 "håller" som stillbild, och två fynd. **Båda överlevde verifieringen, inget släpptes:**
- Fynd 1: radnumren `index.html:598`, `620` och `648` är lästa och stämmer.
- Fynd 2: `index.html:2212` och `2249` stämmer, och måttet −28 finns i `measure10.json`.

En egen incident: min första körning skrev av misstag en del sweep-bildrutor i `astra-r8/`: 5 i `thesis-390/`, 16 i `whole-1440/` och 8 i `whole-390/`. Jag stoppade den inom ungefär en minut. r8:s JSON-filer, loggar, `ours/` och par-bilder är orörda. Den mapp som tillkom av misstag (`thesis-375/`) är flyttad till `astra-r10/_stray/`. De skrivna bildrutorna visar dagens sida, inte r8:s, och r8:s slutsatser vilar inte på dem ensamma.

## fidelity
**r8-fixarna:**
- **Fix 1, Hōrais citat vid 390: stängd.** Vid 390 är ih 568. `#quote-text` ligger på y=162..273 inom [117, 568], med opacitet 0,974 och blur 0,31 px. Värdena är desamma i preview (tre omladdningar) och med hjul (`fix-case-horai-03-390-wheel.png`). Vid 375 är ih 545 och citatet ligger på 151..262 med 0,973 / 0,32 px. 1440 är pixelidentiskt. Två saker ingick inte i Expected och är inga fynd. `#quote-jp` ligger på y=80, bakom sajtens nav. Klippningen i högerkanten är det kända fallet med horai.html (675 px), och det avgör Anton.
- **Fix 2, tesbandets tomma band: delvis stängd.**
  - Det som håller: strecken till bildens överkant är 16 px vid 390 och 375, och bilden är 449/483 px hög vid 390 och 425/459 vid 375. Bildtexten slutar på 818 av 844, och den horisontella scrollen är 0.
  - Det som inte håller: kravet "bildens y är lika i alla fem meningarna". Överkanten ligger på 309 i mening 1–2 och 274 i mening 3–5 (375: 302 / 268). Fotot hoppar 35 px i **ett** hjulsteg (scrollY 4430→4450) när mening 3 går in, och tillbaka på vägen upp (`jump-390-down-4450.png`, `jump-390-up-4410.png`, `jump-375-*`).
  - Hoppet uppstod i R9: `align-self:stretch` låter fotot följa strecken, som i r8 stod bottenankrade. NOTES R9 påstår "identisk vertikal position", och det stämmer inte. Se fix 1.
- **Fix 3, Calyx -03 vid 390: märkningen är räddad, fotot är beskuret upptill.** Vid 390 är ih 517 och vid 375 496. Märkningen "Cmsn. 0211 …, 02/14" ligger helt inne på y=424..455. Första figuren ligger på y=−28..455, så 28 px av fotot står ovanför ramen. Expected löd "minst ett foto och dess märkning ligger helt inne i ramen", och det uppfylls inte. Se fix 2. 1440 är pixelidentiskt.
- **R10, vänsterankrat Hyperborea-foto:** "Systems / with" läses från vänsterkanten vid 390 och 375 (`ours/P03-*-390.png`, `P03-1-375.png`). `object-position` är `0% 0%`, bara under 768. 1440 är pixelidentiskt.

**PARITET, rad för rad:**
- **P01 fold:** håller nivån vid 1440 och 390, oförändrad.
- **P02 kortets baksida:** håller nivån, oförändrad.
- **P03 tesbandet:** håller inte helt.
  - Som stillbild håller den vid båda bredderna. Vid 390 äger meningen rubrikplatsen och bilden resten av skärmen (`P03-1-390`, `P03-3-390`, `P03-5-390`), och det döda blå fältet från r8 är borta.
  - Som sekvens håller den inte vid 390 och 375: fotot hoppar 35 px mitt i bandet (fix 1).
  - 1440 är oförändrat och håller.
- **P04 ridån:** håller nivån. Kanten mot ritbordet är ren i `P04-curtain-390`, och kapitelrubriken som delvis täcks är en del av lyftet.
- **P05:** utgången.
- **P06 kapitelskärmen:** håller nivån, oförändrad.
- **P07–P13 processens steg:** håller nivån vid båda bredderna. Pixlarna är identiska med r8, utom en hårlinje i P10-390 med differens under 40.
- **P14 case-kapitlet:** håller nivån, oförändrad.
- **P15 pris + kontakt:** håller nivån. P15a är oförändrad. I P15b-390 har bara Hōrai-ramens del ändrats.
- **P16 hela sidan:** håller nivån. Rytmen är densamma som i r8, med 0 kollisioner och 0 horisontell scroll.
- **P17 case Calyx:** 1440 håller. Vid 390 håller -01 och -05 nivån. -03 håller som skärm (foto och märkning läses som ett katalogexempel), men fotots topp är beskuren med 28 px mot Expected (fix 2).
- **P18 bryggan:** håller nivån, oförändrad.
- **P19 case Hōrai:** håller nivån vid 1440. Vid 390 håller den inom leadens avgränsning: citatet syns format under naven i -03, och fotot äger skärmen i -01. Klippningen i högerkanten i -01, -03 och -06 är fallet med horai.html, och det avgör Anton.
- **P20 Hōrai → priset:** håller nivån. Kanten är ren och rubriken når rätt läge vid nästa hjulsteg, precis som i r8.

## ceiling
- **Motor och shim:** n/a. Allt som rör sig läser `--sc-ps`, motorn är orörd och `sites/*` är orörda. F-011 respected.
- **Referenserna:** hoy låter ett element stå still medan rubriken byts. V3d gör samma sak vid 1440, där fotot är bottenankrat i kolumn 2. Vid 390 följer fotot numera strecken, som i sin tur följer höjden på rubrikcellen. Den höjden varierar när en mening animerar sin `letter-spacing` och radbryts om. Referensens stillhet är alltså inte uppnådd på mobil.
- **Calyx egen layout:** sajtens header krockar med sitt eget index vid 390 ("Calyx" över "INDEX · STUDIO", `P17-1-390`). Det är sajtens egen mobillayout. Den var oförändrad sedan r8 och hör till samma kategori som Hōrai, så den är inget fynd.

## material_fixes
1. **Tesfotot hoppar 35 px vid 390 och 375 när mening 3 går in. Det gäller `index.html:620` (`letter-spacing:calc(-.02em + (1 - var(--in)) * .06em)`) och gridet på `index.html:598`, som mobilens `min-height` på `index.html:648` inte skyddar.** Alla `.ts` staplas i samma cell. Mening 3 med `--in=0` får +0,06em och radbryts då till 5 rader (174 px) i stället för 4 (139 px). När den blir aktiv krymper cellen, och strecken och fotot flyttar sig upp 35 px i ett hjulsteg (390: scrollY 4430→4450, 309→274; 375: 302→268). Mätt med `letter-spacing:-.02em` injicerad för `.js .ts` under 768: fotot står på y=274 i alla fem meningarna och hoppet försvinner (`jump.py`, variant "inject"). Expected, vid ≤767: fotots överkant är lika (±1 px) i alla fem meningarna och i varje 20 px-hjulsteg genom den pinnade delen, ner och upp, vid 390 och 375. Samtidigt ska R9:s 16 px-avstånd och en bildhöjd på ≥ 400 px hålla, och 1440 och 768 ska vara pixelidentiska med `astra-r8/ours/`.
2. **Calyx -03-fotot beskärs 28 px upptill vid 390 och 375, ankaret `['#studio + section', 0, 76, 700]` på `index.html:2212`.** Offsetvärdet 76 är uppmätt mot en annan layout än den ramen faktiskt renderar: figuren står på y=−28..455 i en ram på 517 px (375: 496). Expected, vid ih < 700: första figuren står på y ≥ 0 och märkningens underkant på ≤ ih, i preview och med hjul, vid 390 och 375. Det går att nå på två sätt. Det ena är offsetvärdet 48 i stället för 76, vilket ger 0..484 i ramen. Det andra är att ankra på figuren själv (`'#studio + section figure'`, 0), som plan 056 först föreslog och som följer figuren oberoende av ramens bredd. 1440 ska vara oförändrat (villkoret ih < 700 slår aldrig till där).

## keep
- **R9 fix 1:** Hōrais höjd på 72svh och offsetläget i `measureCase()` (`a[2]`/`a[3]`, `index.html:2249`). Citatet står skarpt under naven vid 390 och 375, och villkoret på ramens egen ih lämnar 1440 orört.
- **R9 fix 2:s fyllnad:** `align-self:stretch` och `aspect-ratio:auto` under 768. Det döda blå fältet är borta, med 16 px mellan strecken och bilden och en bild på 449–483 px. Behåll dem när fix 1 görs, och lös hoppet i rubrikcellen, inte genom att bottenankra fotot igen.
- **R10:** `object-position:left top` under 768, så att Hyperboreas rubrik läses hel.
- **Calyx på 66svh:** märkningen är räddad. Bara ankaret behöver justeras.
- **Bytena:** de asymmetriska `--in`/`--out`-fönstren. 0 dubbelmeningar och 0 dubbelsteg vid 390 och 375.
- **Grundnivån:** 1440 är pixelidentiskt med r8 i alla rader. 0 horisontell scroll från 320 till 1920, 0 rubrikkollisioner, monoton synk i casen och exakt ett synligt steg per bildruta. F-011 respected.

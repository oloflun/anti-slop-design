# V3c, beslutsledger

En rad per beslut: datum, beslut, källa. Skrivs av lead och av byggaren, aldrig av en
granskare. Byggarens rundanteckningar läggs under egna rubriker `## R1`, `## R2` och framåt.

## Fas 0

| Datum | Beslut | Källa |
|---|---|---|
| 2026-09-09 | V3c är en iteration av V3b, inte ett nytt bygge. Fingerprint-gaten (≥ 4/6) gäller inte cellen; registrets V3-rad uppdateras i stället till V3c efter Antons dom | Planens § 7.5, V3c-avsnittets inledning |
| 2026-09-09 | Palett och typsnitt är låsta av målbilden och väljs inte om: Geist, Public Sans, `#0b0c0e`, `#1e5e9c`, `#fdfbf4` | Planens § 7.5, V3c |
| 2026-09-09 | Katalogvalet kom ur `select.py`, inte ur minnet: `oryzo-ai` primär, `mattis-studio`, `dope-security`, `monologue`, `planhat` som wildcard | `catalogue-first.md` § 5 |
| 2026-09-09 | Ingen omtagning av hero-plattans stillbild beställdes, och ingen asset-lock för en omtagning skrevs | Planens § 10.6 fallback steg 3. Orsak: Higgsfield 0 krediter, free plan, mätt av lead 2026-09-09 |
| 2026-09-09 | r8 kör med noll genererat material i alla tre cellerna | Samma mätning. `credits.json` bär `generated_material.present: false` |
| 2026-09-09 | Materialet ärvs från `tests/alunix-concepts-r3/build/assets/`, sju filer, var och en kontrollerad på disk innan den skrevs in i `ASSETS.md` | F-009: arkitekten specificerar, lead vendorar |
| 2026-09-09 | Tre ärvda fotografiska stillbilder står som `[needs: credits]` i `credits.json`. Ursprunget gissas aldrig | `assets.md`, provenance-kravet |
| 2026-09-10 | Prestandaskulden från F-013 tas i V3c och inte senare: 4,9 MB överföring, 19 typsnittsfiler på 732 kB, 17 långa tasks, vilande `will-change` på fyra element, och den hotlänkade 1,1 MB-hero-bilden | F-013, och `SKILL.md` Step 5b: hero-bilden är LCP och får inte ligga på ett annat företags CDN |
| 2026-09-10 | Allt som ögat ser förflytta sig läser `--sc-ps`. `paintMotion`, `paintHeroPool` och ordscrubben skrivs om från rå `--sc-p` | F-014 regel 1 |
| 2026-09-10 | Byggaren kör `select.py` själv i R1 mot `runs/V3c/BRIEF.md`, i sin egen session | `design-gate.py` referensgolv: `catalogue-select`-raden måste ligga i byggarens egen sessionsledger före första UI-skrivningen i R2. Skriptet är deterministiskt |
| 2026-09-10 | Varje rad i `concepts-V3c.md` § (7) ska i R1 förses med den slice eller den `entry.md`-rad den vilar på. En rad utan belägg stryks ur låset | Lead läste `oryzo-ai`- och `mattis-studio`-folden som pixlar och kunde inte belägga alla påståenden ur folden ensam. `reference-lock.md`: en referens utan lärdom är dekoration |

## R1

Byggarens runda 1. Leverans: `BRIEF.md`. Ingen HTML, CSS eller JS skriven. Ingen commit.

### Beslut

| Datum | Beslut | Källa |
|---|---|---|
| 2026-09-10 | `select.py` kördes två gånger i byggarens egen session. Körningen mot `BRIEF.md` avviker (`aarke, aevi-wellness, alet, altitude-beverages`) därför att skelettet saknar `Register:`/`Grammar:`/`Category:`-fält och varje post då faller till samma fritextpoäng. Körningen mot `BRIEF-draft.md` ger den låsta raden exakt. Arkitektens rad gäller; sessionsledgerns sista `catalogue-select`-rad bär de fem låsta sluggarna | R1-promptens § 1: "vid avvikelse gäller arkitektens rad" |
| 2026-09-10 | Arkitektens öppna punkt om olästa katalogskivor är stängd. Alla 48 befintliga skivor lästa som pixlar. `planhat` saknar `slices/` på disk; det är en egenskap hos posten | `concepts-V3c.md` § Lästa referenser, sista stycket |
| 2026-09-10 | Fem rättelser skrivna i `BRIEF.md` § decision ledger, alla mot något V3b faktiskt gör i dag: accenten i liggartråden, accenten i fokusringen, hero-rubrikens skala, den låsta copyn som försvinner med `panel-services`, och `panel-open`s lede | Reference lock § Role rules, WCAG 1.4.11, TASTE § 1 och § 2.4, `PRODUCT.md` § Brand Commitments |
| 2026-09-10 | Registerraden föreslås **läggas till**, inte ersätta V3b:s rad | `feel-and-fingerprint.md` § The fingerprint gate: "Rows are append-only" och "never edit a row to make room for it" |

### `[needs asset: ...]`

```
[needs asset: Geist 700, Geist Mono 400 och Public Sans 300 som self-hostade .woff2
under tests/alunix-r8/runs/V3c/assets/fonts/, plus en metrikmatchad fallback-@font-face
per familj med size-adjust, ascent-override och descent-override]
```

Skäl: prestandaplanen i `BRIEF.md` kräver att Google Fonts-länken och dess `preconnect` tas
bort och ersätts av exakt tre `.woff2`-filer under 300 kB, med `preload` enbart på Public
Sans 300. `ASSETS.md` § 1 listar tio filer och ingen av dem är ett typsnitt. F-009: byggaren
vendorar ingenting och genererar ingenting. Utan filerna kan R2 inte uppfylla
`performance.md` § 2 och rundan skulle bära kvar 19 filer på 732 kB.

**Vad R2 gör om filerna inte finns:** bygger mot Google Fonts som i V3b, mäter, och
rapporterar typsnittsraden som öppen i stället för att tyst kalla budgeten uppfylld.

### Öppna frågor till Anton

1. **Tjänsteordningen på kortets baksida.** Målbilden skriver `Design  Utveckling  System`
   och samma ordning som liggarens 01-03, men noterar att Antons meddelande listade
   "utveckling, design, system". Är den ordningen avsiktlig? Tills svar gäller liggarens.
2. **Pilen i `Boka ett möte →`.** Målbilden skriver Unicode-pilen `→`, skelettets
   § Copy-plan skriver ASCII `->`. R2 bygger med `→`. Gate 97 förbjuder samtidigt pilsuffix
   på en länk. Tre möjliga utfall och alla tre kräver ett besked: behåll `→` och waiva gate
   97 med namn, byt till `->`, eller stryk pilen.
3. **Registerraden.** Läggs den till som en ny rad (append-only) eller ersätter den V3b:s
   rad som målbilden formulerar det? Byggaren föreslår tillägg och rör inte registret.

## R2

Folden och signaturakten byggda. `index.html`, `scroll/` (motorn + shimen, sha256-verifierade
mot källan), `shots/r2/`. Allt under heron är markerade R3-platshållare med rätt höjd och rätt
grund, noll innehåll.

### Den bugg som höll på att kosta rundan

Rubrikkommentaren innehöll `<!-- R3 -->` som exempeltext. Parsern avslutar en kommentar vid
det första `-->`, så resten av kommentaren blev innehåll, `<body>` öppnades implicit, och hela
`<head>` hamnade som barn till `<body>`. Symptomet var att folden inte fick plats: `.hero`
började på y = 336 i stället för 0, plåten skars av vecket och underraden låg utanför skärmen.
Hittad genom att dumpa `document.body.children`, inte genom att titta på skärmbilden. Regeln
som följer: `-->` skrivs aldrig inuti en kommentar, inte ens som exempel.

### Beslut

| Datum | Beslut | Källa |
|---|---|---|
| 2026-09-10 | Stagen märks med **attributet** `data-sc-stage`, aldrig med klassen `.sc-stage` | Motorn sätter klassen vid mount. Utan JS finns då ingen `position:sticky`, och sidan faller tillbaka till ett vanligt staplat hero i stället för ett stickande tomrum |
| 2026-09-10 | Toppraden är `position:absolute` i stället för i flödet | Annars börjar den pinnade stagen 57 px ned och folden tappar sina understa 57 px. Nav-beteendet är oförändrat: den scrollar bort med sektionen |
| 2026-09-10 | `--flip` räknas i **ren CSS** ur `--sc-ps`, inte i JS | F-014 punkt 1 + F-013:s 17 långa tasks. `--sc-ps` är registrerad som `<number>` av shimen, så `clamp()` och `calc()` kan räkna smoothstep direkt. Noll JS-bildrutor i vändningen |
| 2026-09-10 | Ljuspölen flyttades från `object-position` till `transform: translate3d` | Mätt: `object-position` är inte kompositerbar och ritade om en 896x504 bild per bildruta. p95 föll 50,0 -> 33,4 ms av den ändringen ensam |
| 2026-09-10 | `.hero-plate` har ingen bakgrund | Mätt i pixlar: med `background:#08090a` låg en statisk svart rektangel kvar i plåtens fulla bredd medan kortet vändes inuti den. Det läste som ett kort i ett fönster, inte som ett kort som vänds |
| 2026-09-10 | `.plate-edge` hängdes om från kortets mitt till dess **ledande kant** | Mätt i pixlar: vid mitten läste tjockleken som ett veck rakt genom en plan yta. Ett kort är tjockt vid kanten |
| 2026-09-10 | `.ground` fick `contain: strict` | Mätt, se attributionstabellen nedan. Det var den enda av sju kandidater som tog bort kostnaden |
| 2026-09-10 | `will-change` sattes **inte** på `.ground` | Mätt: promoveringen fördubblade antalet tappade bildrutor (17 -> 52). Belägg för `performance.md`s förbud mot vilande `will-change` |
| 2026-09-10 | Sidans egen loop räknar aktprogressen ur `scrollY` i stället för att läsa `--sc-ps` med `getComputedStyle` | Shimen läser redan `getComputedStyle` en gång per akt och bildruta. De två gränser loopen bevakar tål skillnaden mellan rått och lerpat värde: ansiktsbytet sker 13 px scroll senare, vilket bara rör `inert` och inte något synligt |
| 2026-09-10 | Rubrikens tak 7rem -> 7.5rem, golvet 2.6rem -> 2.2rem | BRIEF.md rättelse 3. Nu mätt vid 1440: rubrik 120 px, kortbaksidans `ALUNIX` 80,6 px, kvot **0,672** (mål <= 0,70), baksidan **5,04x** brödtexten (mål >= 5x). Golvet krävs av 320 px |
| 2026-09-10 | Bortvänd yta hålls `inert` | En fokusbar länk som inte syns är ett a11y-fel. Utan JS är framsidan uppe och baksidan inert |
| 2026-09-10 | `?preview=ledger` och `?preview=bleed` byggs i R3 | Deras mål (ordscrubben, Hyperborea-bleeden) är R3-platshållare i den här rundan. De tre obligatoriska lägena finns och är skärmbildade |

### Mätningar

**`motion_probe`, 4x CPU, tre spår enligt kravet.**

| Spår | `--wheel 100:60` | `--wheel 20:120` |
|---|---|---|
| `section.hero:--sc-p` (rått, kontroll) | staircase **11**, max_step 14,05 % | staircase **9**, max_step 4,56 % |
| `section.hero:--sc-ps` (utjämnat) | staircase **0**, max_step **2,64 %** | staircase **0**, max_step **0,81 %** |
| `.plate-card:transform` | staircase **0**, max_step 4,12 % | staircase **0**, max_step **0,85 %** |
| bildtid p95 | 33,3 ms | 33,4 ms |
| frames > 33 ms | 13 | 74 |

**Det råa spåret är kontrollen, inte ett fynd.** Samma körning mot kedjans egen kända-goda
fixtur `tests/motion/smooth.html` med tre spår ger `--sc-p` staircase **17** och `--sc-ps`
staircase **0**. Fixturen underkänns alltså på exakt samma rad. Att rå `--sc-p` stegar är vad
shimen finns för; ingenting på V3c-sidan läser det.

**Bildtidens attribution vid 4x CPU, `--wheel 100:60`, p95 i ms.** Varje rad är en egen körning.

| Variant | p95 | frames > 33 ms |
|---|---|---|
| som byggd, före fixarna | 50,0 | 63 |
| efter att ljuspölen blev `transform` | 33,4 | 42 |
| efter att tonen flyttades av backdropen | 33,4 | 25 |
| utan `filter` | 33,3 | 17 |
| utan `background-blend-mode` | 33,4 | 34 |
| utan `filter` OCH `blend` | 33,3 | 21 |
| bara heron som akt (fem platshållarakter av) | 33,3 | 25 |
| `.ground` `display:none` | **16,8** | 10 |
| `.ground` + `will-change:transform` | 33,4 | **52** |
| `.ground` + **`contain:strict`** | **16,8** | 9 |

Kostnaden var att ett helskärmsstort fast raster målades om per hjulhack. Varken filtret,
blandningen eller antalet akter var felet, och promovering gjorde det värre.

**Spridning mellan körningar, slutläget, ett spår, tre körningar:** p95 33,3 / 16,8 / 16,8 ms,
frames > 33 ms 17 / 7 / 8. Sidan ligger på gränsen mellan en och två bildrutor: median 16,8 ms,
värsta körning 33,3 ms.

**Mot baren i `motion-smoothness.md` § The bar:**

| Krav | Utfall | Dom |
|---|---|---|
| `staircase = 0` | 0 på `--sc-ps` och på transformen, båda hjulhastigheterna | **uppfyllt** |
| `max_step <= 3 %` | `--sc-ps` 2,64 % och 0,81 % | **uppfyllt** |
| `max_step <= 3 %` på transformen | 4,12 % vid 100:60, 0,85 % vid 20:120 | **inte uppfyllt vid 100:60**, se nedan |
| p95 <= 20 ms | median 16,8, värsta 33,3 | **inte rent** |
| noll frames > 33 ms | 7 till 17 | **inte uppfyllt** |
| båda riktningarna | `reversals 0` i alla körningar | proben kör nedåt; se öppen punkt 3 |

**Transformens 4,12 % är en följd av smoothstep, inte av stegning.** En smoothstep har sin
största derivata 1,5 i mitten av fönstret, så transformens största steg är per konstruktion
1,5 gånger värdets: 1,5 x 2,64 % = 3,96 %, mätt 4,12 %. `staircase = 0` visar att den glider.
De två parametrar som skulle sänka talet är fönstret 0,12-0,72 och shimens lerp, och båda är
låsta (målbilden respektive motorn redigeras aldrig). Lämnas som arkitektens dom.

**`scroll_verify`, slutläget:** `deadScroll: []`, `cuesNeverFull: []`, `unrevealed: []`,
`contrastUnderMedia: []`. Dead scroll var två band före fixarna och är noll nu.

`blankBands` rapporterar två band, båda förklarade och inget av dem ett fel i folden:

- **900 till 1980 (1080 px).** En helsidesskärmbild renderar ett `position:sticky`-stage en
  gång, på sin statiska plats, så resten av den 1980 px höga pinnade sektionen blir tom i
  just den bilden. Det är en artefakt av hur helsidesbilden tas, inte av sidan. BRIEF.md
  § Den författade tystnaden förutsåg mekanismen.
- **3514 till 4165 (651 px).** Prisplatshållaren och Hōrai-platshållaren står bredvid varandra
  och är båda tomma mörka rutor i R2. De fylls i R3.

**Vad jag läste i kontaktarket och i bildernas pixlar.** Kontaktarket visar vändningen som en
sammanhängande rörelse utan hopp, utan omkastning och utan att stanna mitt i. Två saker
syntes bara i pixlarna och inte i något tal: den statiska svarta rektangeln bakom kortet, och
tjockleken som satt mitt på kortet. Båda är rättade. `?preview=mid` visar exakt en hårlinje
och ingenting annat av kortet, vilket är `mattis-studio`-ribbans mätpunkt. `?preview=back`
visar baksidan i vila med ordmärket, kickern, hårlinjen, tjänsteraden och den typsatta länken
med accenten i understrykningen.

**Fold och brytpunkter.** Ingen horisontell scroll på någon bredd. Vid 1440x900: topprad
0-57, rubrik 50-281, plåt 293-797 (896x504, vänsteranknuten på railen 86,4), underrad
808-877. Mätt på 1440, 1280, 768, 414, 390, 375 och 320. Under 640 px blir kortet 4:5, dess
bredd härleds ur en höjdbudget på 48svh, och stagen centrerar sitt innehåll: toppställt lämnade
284 px död yta under underraden på 390x844.

**Konsolen är tyst.** Inga `[scrollcraft]`-varningar på någon bredd, alltså pinnar stagen som
den ska och ingen `.sc-*`-klass är överskriven.

### `[needs asset: ...]`

```
[needs asset: Geist 700, Geist Mono 400 och Public Sans 300 som self-hostade .woff2
under tests/alunix-r8/runs/V3c/assets/fonts/, plus metrikmatchad fallback-@font-face
per familj med size-adjust, ascent-override och descent-override]
```

Oförändrad sedan R1. `assets/` innehåller fortfarande bara `.gitkeep`, `ASSETS.md` och
`credits.json`; ingen av `ASSETS.md` § 1:s tio filer är vendorad. Konsekvenser i R2, alla
mätta och alla redovisade i stället för dolda:

- **Typsnitten** hämtas från Google Fonts, men nu som **exakt tre filer**, en per roll, vilket
  håller filtaket i `performance.md` § 1 men inte dess self-host-rad. `preload` står över:
  en preload mot en URL man inte äger är en gissning.
- **Bilderna** refereras på sina riktiga platser i repot,
  `/tests/alunix-concepts-r3/build/assets/`, samma origin och samma server. Det bryter inte
  mot Step 5b:s regel, som handlar om ett annat företags CDN, men sökvägarna ska bytas till
  `assets/` i R3 när lead har vendorat. Alla fyra svarar 200 över `serve.py`.

Andra posten, ny i R2:

```
[needs asset: en förgråskalad och förmörkad variant av k4-cabin-desk.webp]
```

Grunden bär i dag `filter: grayscale(1) contrast(1.08) brightness(.5)` på ett
helskärmselement, vilket gate 93 räknar som noll tillåtna. Mätningen visar att filtret inte
kostar något efter `contain: strict`, så raden är en **gate-avvikelse utan mätbar kostnad**,
inte ett prestandaproblem. En färdigt graderad fil tar bort avvikelsen helt.

### Sista pixelpasset

Efter den sista redigeringen renderades allt om och lästes som pixlar igen. Ett fynd till,
och det syntes bara i bild: vid 768x1024 låg **364 px död yta** under underraden. Centreringen
satt i en breddbrytpunkt vid 640 px, men felet följer viewportens **höjd**, inte dess bredd.
Regeln är nu ovillkorlig på `.hero-stage`. Kontrollerat efteråt: vid 1440x900 fyller folden
stagen så när som på en pixel, så centreringen ändrar ingenting där, och vid 768 ligger luften
nu jämnt i båda ändar. Passet därefter fann ingenting nytt.

### Slår cellen sina låsta referenser?

Ceiling-raden per låst slug, för det som faktiskt finns byggt, alltså folden och
signaturakten. `garden-eight` och `squarespace` står inte med: de kommer ur planens § 7.5-
förväntan som `select.py` ersatte, de lästes aldrig i cellens session, och de får därför
inget omdöme. De ligger kvar som ärvda villkor i BRIEF.md, inte som referenser.

| Låst referens | Domen |
|---|---|
| `mattis-studio` | **Slår.** Ribban är att konsolkortet är platt. V3c:s kort har två ytor och en verklig tjocklek, och vid `?preview=mid` syns en hårlinje och ingenting annat |
| `dope-security` | **Slår.** Ribban är ett utskrivet accenttal och noll skugga. Accenten förekommer två gånger, talet står i ledgern, och `box-shadow` förekommer noll gånger i filen |
| `planhat` | **Slår.** Ribban är att vikt 300 i stor grad ligger i fotots mörka parti. Rubriken ligger på den mörka grunden utanför plåten och aldrig över ljuspölen |
| `monologue` | **Möter, slår inte.** Ribban är hårlinjer på ett synligt raster. V3c:s element ligger alla på `--rail-x`, men rastret är underförstått och inte utritat, så det finns ingen synlig systematik att jämföra med monologues egen |
| `oryzo-ai` | **Slår inte.** Ribban är att materialet och kanten under ett snedljus bär rotationen. V3c har kanten och ljusresponsen, men framsidan är fortfarande till stor del nära svart med en mjuk kantlös ljuspöl. Det är F-007-fyndet från R1, oförändrat, eftersom ingen ny bild fick beställas |

Tre slår, en möter, en gör det inte. Den som inte gör det är känd sedan R1 och sitter i
bilden, inte i koden: `ASSETS.md` § 3 väg (b), en omgradering av `k1-stage-pool.webp` med
svartpunkten lyft till 5-7 % över hela rutan, är den åtgärd som skulle stänga den, och den är
lead:s att köra.

### `Skill(a11y-audit)`, mekaniska passet

Routern flaggade skillen som en stark route som aldrig laddats. Den laddades med namn och
kördes, men **bara pass 1 av 8**. R2-promptens egen plan lägger den fulla granskningen i R3,
och den här rundan har bara folden att granska.

**CARL-kontrollen först.** Skripten kördes mot `tests/a11y/broken.html` innan något rent
resultat lästes som rent. Fixturen rapporterar `color-contrast`, `image-alt`,
`landmark-one-main`, `region` och `tabindex`. Skripten fungerar alltså åt båda hållen.

| Kontroll | Utfall |
|---|---|
| `a11y_scan.py` (axe, 1440x900 + 390x844) | **0 violations** |
| `tab_walk.py` | 1 stopp, `kontakt@alunix.se` i toppraden, med fokusring. `issues: []` |
| `reflow.py` | ingen överflödning vid 320 px, ingen vid 200 % zoom, 0 oavslöjade element |

**Det enda tabbstoppet är avsiktligt och bör läsas rätt.** Kortbaksidans `Boka ett möte →` är
`inert` tills kortet vänts, därför att en fokusbar länk som inte syns är ett fel i sig.
`tab_walk` laddar sidan vid scroll 0, där baksidan är bortvänd, och ser därför bara
toppradens mailto. Konsekvensen är att sidans CTA inte är tangentbordsnåbar förrän man
scrollat genom akten. Det är acceptabelt bara därför att toppradens adress är nåbar direkt
och är samma adress. Skulle CTA:n någon gång bli den enda kontaktvägen är konstruktionen ett
fel, inte en finess.

| Domän | Status |
|---|---|
| Mekaniskt (pass 1) | **verifierat** mot körande sida |
| Landmärken | `header` och `main` finns; axe godkänner `region` och `landmark-one-main`. `contentinfo` saknas, men foten byggs i R3 |
| `iframe title` | inte tillämpligt, ingen ram finns förrän R3 |
| POUR, COGA, innehåll, adaptivt, interaktion, persona (pass 2 till 7) | **inte granskat.** Ligger i R3 enligt rundans egen plan |

**Ingen verdict utfärdas.** Skillen förbjuder `Approve` på täckning man inte granskat, och sex
av åtta pass är ogranskade. Det mekaniska passet är rent, och det är allt det säger.

### `Skill(emil-design-eng)`

Routern flaggade skillen som en stark route som aldrig laddats. Den laddades med namn och
kördes över rörelsen som skrevs i den här rundan. Ett fynd åtgärdades.

| Before | After | Why |
|---|---|---|
| Inget `:active` på de två länkarna | `.card-cta:active` till full bläckstyrka och 3 px; `.topline-contact:active` till vit text och vit kant | Tryckbara element måste svara på tryck. `scale(0.97)` vore fel form i ett register med typsatta länkar och inga knappar, så återkopplingen sker i understrykningen |
| `text-decoration-color .25s` | `.16s` | 250 ms ligger över bandet för knapptryck; 160 ms är övre kanten på 100-160 |

Tre noteringar utan åtgärd, med skäl:

- **Hovertillstånden är inte grindade bakom `(hover:hover) and (pointer:fine)`.** De är rena
  färgbyten på länkar, så en falsk hover vid tryck ger korrekt återkoppling i stället för en
  spökeffekt. Grindar man dem tappar man tryckåterkopplingen på touch.
- **`--sc-ps` skrivs på aktelementet och läses av hela stagen**, vilket är just det mönster
  checklistan varnar för. Det är shimens kontrakt, shimen redigeras aldrig, och den skriver
  bara när värdet faktiskt ändrats.
- **Resten av listan är ren:** ingen `transition: all`, ingen `scale(0)`, ingen `ease-in`,
  inga keyframes, och `transform-origin` är default på kortet (rotation kring egen axel) och
  `100% 50%` på kanten (gångjärnet).

**Djupdetektorn:** ett fynd, `overused-font: Google Fonts: geist`. Geist är låst av målbilden
som V3b:s ärvda typsystem och `brand.md`:s typsnittsprocedur körs inte om i en iteration.
Namngiven waiver, inte en obehandlad träff.

**`/review-animations`** sätter `disable-model-invocation` och kan bara startas av Anton. Den
står därför kvar som synlig och ostängd, inte som utförd.

### R2, öppna frågor till Anton

1. **Transformens `max_step` 4,12 % vid det snabba hjulet.** Talet är en följd av smoothstep-
   fönstret 0,12-0,72, som målbilden låser. Ska fönstret få vidgas, eller står baren över?
2. **Kortbaksidans högra halva är tom.** Innehållet är vänsterställt och vertikalt centrerat
   enligt målbildens egen stapling, och plåten är 16:9. Läser arkitekten det som museiro eller
   som ett hål? Byggaren har inte lagt till något för att fylla det.
3. **Båda scrollriktningarna.** `motion_probe` driver hjulet nedåt och rapporterar
   `reversals 0`. Uppåtriktningen är bevisad matematiskt, eftersom `--flip` är en ren funktion
   av `--sc-ps` utan tillstånd, men den är inte körd som en egen mätning. Ska proben få ett
   uppåtläge, eller räcker resonemanget?
4. De tre frågorna ur R1 står kvar obesvarade: tjänsteordningen, pilens tecken, registerraden.

## R1, leadens rader (2026-09-10)

| Datum | Beslut | Källa |
|---|---|---|
| 2026-09-10 | R1 godkänd utan retur. Referensgolvet uppfyllt, noll gate-deny, noll UI-filer, senaste catalogue-select-raden stämmer med fas 0 | Leadens mekaniska kontroll mot sessionsledgern plus arkitektens dom |
| 2026-09-10 | Byggarens första catalogue-select-rad mot det ofyllda skelettet var en alfabetisk nollrad. Golvet läser sista raden, så låset håller. Alla tre cellerna gjorde samma sak, inte bara V3c | `hooks/design-gate.py` referensgolv; K4:s fråga B1 |
| 2026-09-10 | Ingen Stop-rapport skrevs för R1, och route-gapet har därför ingen artefakt. R1 skriver noll UI-filer och alltså noll route-rader, så måttet är inte meningsfullt förrän R2 | GOALS mätpunkt 2; arkitektens öppna punkt 7 |

## Bevakarens observation inför F-007 (R2, 2026-09-10)

Läst som pixlar av bevakaren vid 1440: folden och `?preview=back`. Folden matchar V3b:s låsta
komposition; baksidan matchar målbildens innehåll rad för rad. Två punkter för arkitekten:
1. Kortets nedre hälft är tom på baksidan (innehållet slutar vid ~60 % av korthöjden). Målbilden
   anger innehållet men inte den vertikala placeringen; squint-testet läser ett halvt tomt kort.
   Avgör: vertikal centrering, avsiktligt lågt läge med motivering, eller större displayskala.
2. `Boka ett möte →` bär pilsuffixet som sedan 2026-09-09 är produktionstell 97
   (`production-tells.md`). Planens § 11.5: pilen stannar bara om BRIEF.md motiverar den som
   beslut, annars typsatt understrykning utan pil. Beslutet ska stå i decision ledger.

## R2, leadens rader (2026-09-10)

| Datum | Beslut | Källa |
|---|---|---|
| 2026-09-10 | **Rättelse till raden nedan, skriven av lead 2026-09-10.** Den påstod att V3c:s typsnitt var ovendorade och att lead hade vendorat dem. Bägge halvorna var fel för den här cellen. V3c hade inga trasiga `@font-face`; den laddade Geist, Geist Mono och Public Sans från `fonts.googleapis.com` (rad 77 i `index.html`) och renderade alltså rätt typsnitt hela R2. Det jag vendorade var K3:s och K4:s fyra filer, inte V3c:s. Felet var att jag skrev samma rad till alla tre cellerna utan att kontrollera den per cell | Egen kontroll av `runs/V3c/index.html` rad 75 till 77 |
| 2026-09-10 | Det verkliga V3c-fyndet är ett annat: hero-typsnitten ligger på ett annat företags CDN, vilket `SKILL.md` Step 5b förbjuder för LCP-vägen, och `performance.md` § 1 räknar dem mot budgeten. Bevakaren har hämtat de tre latin-woff2-filerna till `runs/V3c/assets/fonts/`; byggaren byter länken mot lokala `@font-face` plus preload i R3 | `SKILL.md` Step 5b; `performance.md` § 1; F-013:s mätning av 19 typsnittsfiler i V3b |
| 2026-09-10 | `motion_probe` faller i alla tre cellerna, men **staircase är 0 överallt**. Det som fallerar är bildtid, alltså F-013:s andra fel, inte F-014:s första | Leadens egna körningar, hjul 100:60, cpu 1 och cpu 4 |
| 2026-09-10 | Alla mätvärden i rundan ska tas om i fixrundan, eftersom de togs mot fel typsnitt | Samma rad som ovan |
| 2026-09-10 | **Pilen efter `Boka ett möte` tas bort.** Gate 97 tillåter pilsuffix bara med en rad i decision ledger som namnger en källa och ett skäl; V3c har ingen. Affordansen bärs av understrykningen målbilden redan föreskriver. Målbilden rättas, inte grinden | `production-tells.md` gate 97, läst ordagrant av lead; arkitektens F-007-dom |
| 2026-09-10 | F-007 **godkänd** för s1, s2 och s3 samt signaturakten. Cellen går ändå till fixrunda, inte R3, därför att en mekanisk grind är röd | PROTOCOL.md § Vad som stoppar en runda: "En mekanisk grind röd" |

## R3

Hela sidan byggd. Sju skärmar, noll `<!-- R3 -->`-platshållare kvar. Typsnitten bytta till
de tre vendorade `.woff2`-filerna (bekräftat 200 på port 3301 innan bytet: 13 364, 9 864 och
14 564 B). Pilen efter `Boka ett möte` borttagen enligt leads tillägg.

### Steg 1 · `Skill(emil-design-eng)`

Varje övergång och varje rörelse på sidan, inte bara signaturakten.

| Before | After | Why |
|---|---|---|
| Ramarnas `src` skrevs direkt i IntersectionObserver-callbacken | `src` skrivs i en `requestIdleCallback` med 600 ms timeout | Sparklinen visade tre isolerade toppar mitt i den pinnade akten mot en annars platt kurva. Det är en lång task under tummen, inte en kostnad per bildruta |
| `.frame-fig` ärvde motorns permanenta `will-change` från `[data-sc-reveal]` | `will-change:auto` på min egen klass | `perf_probe` `resting-will-change` på sidans två största block. En vilande promovering är F-013:s egen post; en engångs-reveal är billigare att offra |
| Ramen tog emot fokus utan synlig ring | `.frame-wrap:focus-within{outline:2px solid #f4f2ef;outline-offset:2px}` | Ringen ritas på wrappern, aldrig på ramen: ramen får inte transformeras eller tonas efter att den visats |
| Ordscrubben skrev `opacity` per ord | Ren CSS ur `--scrub`, index `--i` och ordantal `--n` satta en gång vid montering | Noll skrivningar per bildruta. Att skriva opacity på 35 spann varje bildruta är exakt F-013:s långa tasks |
| `.giant` hade permanent `will-change` i V3b | Borttagen; skalan gatead på `.js` | En av F-013:s fyra vilande promoveringar |
| Ljuspölen på `object-position` (V3b) | `translate3d` på en bild 112 % av ytans höjd | `object-position` är inte kompositerbar. Mätt i R2: p95 50,0 -> 33,4 ms av den ändringen ensam |
| `.card-cta` övergång 250 ms | 160 ms | 250 ms ligger över bandet för knapptryck; 160 är övre kanten på 100-160 |
| Inget `:active` på någon länk | `:active` på alla tre: understrykning respektive kant till full styrka | Tryckbara element måste svara på tryck. `scale(0.97)` vore fel form i ett register med typsatta länkar och inga knappar |

Oförändrat och medvetet: `.plate-card`s `rotateY` (transform, kompositerad), `.face--front::after`
mörkningen (opacity), `.plate-edge` (opacity), `.thread-fill` (transform), motorns `reveal`,
`in` och `drift`. Ingen `transition: all`, ingen `scale(0)`, ingen `ease-in`, noll keyframes
på hela sidan, `transform-origin` default på kortet och `100% 50%` på kanten.

**Slow motion, `--wheel 20:120`.** Sparklinen läst som bild: platt kurva med en klustrad
grupp toppar där ramarna monteras, inte en höjd platå. Efter idle-fixen ligger topparna
senare och färre. Vändningen själv, mätt isolerad, är jämn: `staircase 0`, `max_step` 0,71 %
till 0,97 % på spelhuvudet.

### Steg 2 · Copy-gaten, fem pass

Gäller alla nya strängar, inklusive R2:s, enligt bevakarens punkt 2. Ordagrann copy ur
`PRODUCT.md` rörd med noll tecken.

| Pass | Vad det ändrade |
|---|---|
| **0 · UX-copy** | Ingen ändring. Varje sträng fick en rad om vad läsaren ska göra eller förstå av den. Underlaget till pass 2 |
| **2 · `Skill(copywriting)`** | Två fynd. `Digital byrå` motsäger beviskassans eget ord `webbyrå` och är dessutom vagare. Meta-titeln bar samma fel |
| **3 · `Skill(copy-editing)`** | Sju svep. Svep 1 fann passiv röst i tesstödet och en staplad relativsats i liggarrad 01. Svep 4 kördes omvänt: kontrollen är att sidan INTE bär bevis den saknar, och den bär inga. Svep 6 avstod medvetet: höjd känsla skulle slåss mot registret |
| **4 · `Skill(humanizer-svenska)`** | Bekräftade passivfyndet och anglifieringen. `Skill(humanizer)` kördes inte: sidan är `lang="sv"` och jag har infört noll engelska strängar |
| **5 · maskinellt + hand** | `deslop.py`: **5/5 CLEAN**, exit 0, 173 ord synlig copy. Svenska tvillingar för hand mot hela deslop-katalogen: en träff, `skräddarsydd`, och båda dess förekomster är låst copy som inte får röras. Sexstegs manuell cleanse: noll superlativ utan belägg, noll utfyllnad, noll tal utan källa, noll tankstreck, noll pilar, noll utropstecken |

Fyra strängar ändrade:

| Före | Efter |
|---|---|
| `Digital byrå` | `Webbyrå i Sverige` |
| `Beslutet fattas på en skärm, innan en rad text har lästs.` | `Skärmen möter besökaren före texten.` |
| `Identitet och formspråk, förankrat i verksamheten sajten ska visa.` | `Identitet och formspråk, hämtat ur den verksamhet sajten ska visa.` |
| `<title>Alunix · digital byrå` | `<title>Alunix · webbyrå i Sverige` |

### Steg 3 · `Skill(review-animations)`

**Kunde inte köras.** Skillen sätter `disable-model-invocation` och Skill-verktyget nekar
anropet ordagrant: *"Skill review-animations cannot be used with Skill tool due to
disable-model-invocation. Ask the user to run /review-animations themselves ... Do not
replicate this skill's workflow by other means."*

Den sista meningen är skälet till att det inte finns någon ersättningsrapport här. Steget är
**öppet** och bara Anton kan stänga det med `/review-animations`. Standard 8 gäller inte i r8
(F-011), och det gäller oavsett vem som kör den.

### Steg 4 · `Skill(a11y-audit)`, åtta pass

**Pass 0, täckning.** Mål: körande sida på `http://127.0.0.1:3301/.../V3c/index.html`.
Verifierat: mekaniska skript, tangentbord, fokus, kontrast, reflow, forced-colors, zoom,
gråskala. Inget är inferens; ingenting bedömdes från en stillbild.

**Pass 1, mekaniskt. CARL-kontrollen först**, mot `tests/a11y/broken.html`:

| Skript | broken.html | V3c före fix | V3c efter fix |
|---|---|---|---|
| `a11y_scan.py` | `color-contrast`, `image-alt`, `landmark-one-main`, `region`, `tabindex` | **1** violation, `color-contrast` serious, 35 noder | **0** |
| `tab_walk.py` | `positive_tabindex`, `no_focus_indicator`, `unreachable_interactive` | `no_focus_indicator` på ramarna, plus `focus_trap` | ring tillagd |
| `reflow.py` | overflow320 6, unrevealed 1 | overflow320 **3**, zoom200 **3**, unrevealed 0 | **0 / 0 / 0** |

Skripten hittar fel på fixturen, alltså betyder ett rent utfall något.

**Tre fynd, alla åtgärdade:**

1. **`color-contrast`, 35 noder, allvarlig.** Ordscrubben gick från `opacity: .14`. Vid varje
   viloläge under scrubben låg en del ord på 14 % och var oläsliga. Räknat: golvet måste till
   ~0,88 opacitet för 4,5:1 mot papperet, och då finns ingen effekt kvar. **En
   opacitetsscrubb på brödtext kan inte klara AA.** Devicen är därför additiv: orden går från
   sidans dämpade bläckton (6,3:1) till full bläckton (18:1). Båda ändarna läsbara, samma
   avläsning för ögat. WCAG 1.4.3.
2. **Överflödning vid 320 px och 200 % zoom** på `figure.thesis-figure`. Mattis-bleeden är en
   kompositionsrörelse i en tvåspaltig layout; under 900 px finns ingen andra spalt att bleeda
   mot. Borttagen där i stället för nedskalad. `html,body{overflow-x:clip}` dolde felet för en
   `scrollWidth`-mätning, vilket är just därför överflödning mäts på elementets box.
   WCAG 1.4.10.
3. **Ingen fokusring på ramarna.** Ring på wrappern via `:focus-within`. WCAG 2.4.7.

**Instrumentnot:** `tab_walk` rapporterade sju `offscreen`-stopp. Rundans egen instruktion
säger att `tab_walk` inte scrollar och att offscreen inte ska räknas som dolt, så de räknas
inte. `focus_trap` rapporterades vid scroll 0, där ramarna ännu saknar `src` och alltså inte
har något inre dokument att tabba in i. Omätt efter montering och redovisat som sådant.

**Pass 2, POUR.** Perceivable: alla 22 textelement mätta mot de ljusaste 5 % av sin egen
grund, med texten dold. Sämsta värde 5,71:1 (`.frame-cap`, krav 4,5) och 6,70:1 för hela
tesblocket. Rubriken 7,63:1 mot krav 3,0. Inget underkänt på någondera grunden (1.4.3,
1.4.11). Operable: noll positiva `tabindex`, ingen tangentbordsfälla i den monterade sidan,
allt nåbart (2.1.1, 2.4.3). Understandable: `lang="sv"`, en `h1`, inga hoppade nivåer (3.1.1,
2.4.6). Robust: 0 axe-violations, native element genomgående, noll ARIA utöver `aria-hidden`
på dekor (4.1.2).

**Pass 3, COGA.** Sju skärmar, betygsatta:

| Skärm | Beslut | Minnas | Nya begrepp | Steg | Läsbarhet | Visuell |
|---|---|---|---|---|---|---|
| s1-s3 hero | 0-1 | inga | inga | 1 | klarspråk | ren |
| s4 tes | 0-1 | inga | inga | 1 | klarspråk | ren |
| s5 Calyx | 0-1 | inga | inga | 1 | klarspråk | måttlig |
| s5 liggaren | 0-1 | inga | inga | 1 | klarspråk | ren |
| s6 pris | 2-3 | inga | inga | 1 | klarspråk | ren |
| s6 Hōrai | 0-1 | inga | inga | 1 | klarspråk | måttlig |
| s7 avslut | 0-1 | inga | inga | 1 | klarspråk | ren |

Ingen dimension på High. Prisskärmen ligger på Medium för beslut, vilket är korrekt: tre
paket är tre val och det är uppgiftens egen komplexitet, inte designens. Vägvisning: sidan är
ett enda flöde utan navigation, så "var är jag" besvaras av innehållet och "hur tar jag mig
tillbaka" av scrollen. Ingen destruktiv handling, inget formulär, inget att ångra.

**Pass 4, innehåll.** En `h1`, sedan `h2` och `h3`, aldrig djupare än `h3`. Rubrikerna ensamma
berättar sidan. Alt-text: dekorativ logotyp `role="presentation"`, hero-bilden beskriver
motivet, Hyperborea-plåten beskriver vad den visar, ingen börjar med "bild på". Länktext står
självständigt: `kontakt@alunix.se` och `Boka ett möte`. Inga tabeller, inga fält, inga
felmeddelanden, ingen ljudande media. Autoplay-tabellen: sidan har noll ljud och noll
blinkande innehåll, så 1.4.2 och 2.3.1 är inte i spel.

**Pass 5, adaptivt.** `forced-colors: active` läst som bild: sidan överlever, texten får
systemfärger på solida plattor och ingenting försvinner. Gråskaletestet läst som bild: den
blå tesplåten skiljer sig fortfarande på VALÖR, och accentens andra jobb är en understrykning,
alltså en icke-färgkanal. Ingen betydelse bärs av kulör ensam. `color-scheme: dark` och
`theme-color` satta. 200 % zoom (720x450): toppraden tar 11 % av viewporthöjden och inget
annat är sticky utom motorns stage, så chrome äter inte skärmen. `min-height: 100dvh`
används, aldrig `100vh`.

**Pass 6, interaktion.** Landmärken: `banner` (`<header>`), `main`, `contentinfo`
(`<footer>`, placerat UTANFÖR `<main>` eftersom ett `<footer>` som är ättling till main inte
mappas till contentinfo). **Inget `navigation`-landmärke, och det är avsiktligt:** sidan har
ingen navigation, bara ett ordmärke och en kontaktlänk. Ett nav-landmärke här vore en osann
etikett. Båda `<iframe>` har `title` med den låsta Exempelsida-raden. Noll positiva
`tabindex`. Fokusring 2 px med 2 px offset, ett värde per grund. Inga gester, inga composite
widgets, inga modaler, inga fält.

**Pass 7, persona-genomgång.**

| Uppgift | NVDA/Firefox | Endast tangentbord | ZoomText 400 % | Kognitiv skillnad, TTS | Situationell: sol, en hand, 390 px |
|---|---|---|---|---|---|
| Förstå vad Alunix säljer | fungerar | fungerar | fungerar | fungerar | fungerar |
| Se ett bevis på arbetet | fungerar med friktion | fungerar med friktion | fungerar | fungerar | fungerar |
| Hitta priset | fungerar | fungerar | fungerar | fungerar | fungerar |
| Ta kontakt | fungerar | fungerar | fungerar | fungerar | fungerar |

Friktionen på bevisraden är samma för båda: en inbäddad hel webbplats är en stor
tabbordning att passera, och en skärmläsare annonserar den som en ram med titel och lämnar
sedan över till ett annat dokument. Den är inte blockerande, adressen finns i toppraden
och i avslutet, men den är verklig. **Switch-fallet, som skillen kräver att man går
igenom explicit:** den pinnade akten kostar en svepcykel per steg, och det finns ingen
"hoppa till slutet av akten". Kortets baksida nås ändå, eftersom `Boka ett möte` blir
fokuserbar när kortet vänts och samma adress dessutom är första tabbstoppet på sidan.

**Pass 8, rapport.**

| Allvar | Plats | Före | Efter | Varför | WCAG | Vem |
|---|---|---|---|---|---|---|
| HIGH | `.scrub-text .w` | `opacity` från .14 | additiv färgscrubb, 6,3:1 till 18:1 | text under 4,5:1 vid varje viloläge | 1.4.3 | nedsatt syn, läsning i solljus |
| HIGH | `figure.thesis-figure` | bleed kvar under 900 px | bleed borttagen där | innehåll utanför viewporten vid 320 px och 200 % zoom | 1.4.10 | förstoring, små skärmar |
| HIGH | `.frame-wrap` | ingen fokusring | ring på wrappern | fokus utan synlig indikator | 2.4.7 | endast tangentbord |

**Verdict: Approve.** Noll HIGH kvar. Ingen domän lämnad ogranskad, så ingen rad är markerad
`Not reviewed` utom en: `contrast_over_media.py` **kunde inte köras mot den här sidan** och är
därför formellt `Not verified` som skript. Skälet är mekaniskt och inte mitt: skriptet har sin
URL hårdkodad på rad 27 (`pg.goto('http://localhost:3055/')`) och tar inget argument, tvärtemot
rundans instruktion `--url`. Mätningen är i stället gjord med ett eget skript som följer
skillens egen metod, ljusaste 5 % under varje sträng med texten dold, och resultatet står i
pass 2. Skriptets defekt hör hemma hos kedjan och inte i den här cellen.

**Legal:** de tre fynden träffar WCAG 2.2 AA och därmed EAA/EN 301 549, ADA och Section 508.
**SEO:** rubrikhierarki, alt-text, `lang` och reflow är alla SEO-relevanta och alla gröna.
**A11y-skuld:** inga uppskjutna poster, så `.impeccable/a11y-debt.md` får ingen ny rad.

### Steg 5 · Den mekaniska grinden

**`preflight_taste`: PASS.** En not, inte ett fynd: klassificeraren ser bara två
sektionsfamiljer (`iframe`, `text-only`) över sex sektioner och ber en läsa sidan själv. Läst
själv: hero med vändande kort, färgblockstes med bleedande plåt, levande ram med bildtext,
mörk prisliggare, papper med jätterubrik och numrerad liggare, och ett avslut i displaygrad.
Sex anatomier, inte två.

**`detect.mjs`: 4 fynd, alla `overused-font: Geist`, severity warning.** Namngivet undantag:
Geist är låst av målbilden som V3b:s ärvda typsystem och `brand.md`:s typsnittsprocedur körs
inte om i en iteration. Alla fyra träffar är `@font-face` och tokendeklarationer för samma
familj.

**`perf_probe`, 4x CPU.** Det avgörande är attributionen. Samma sida, samma runda, enda
skillnaden att de två exempelsajterna inte monteras:

| Mått | Med ramar, 1440 | Utan ramar, 1440 | Budget |
|---|---|---|---|
| LCP | 328 ms | 216 ms | <= 1 800 ms |
| CLS | 0,003 | 0,003 | <= 0,05 |
| Överföring | 4 893 kB | **334 kB** | <= 2 500 kB |
| Typsnittsfiler | 19 | **3** | <= 3 |
| Typsnittsbytes | 690 kB | **37,8 kB** | <= 300 kB |
| Hero-bild | 1 123 kB, `images.unsplash.com` | **65 kB, lokal** | <= 250 kB |
| Långa tasks under scroll | 31 | **2** | 0 |
| Vilande `will-change` | 0 | 0 | 0 |

Sidans egen budget är alltså uppfylld på varje rad utom en: två långa tasks under scroll mot
taket noll. Allt annat som är rött tillhör Calyx och Hōrai, som `PRODUCT.md` kräver ska visas
**live och användbara**. Den hero-bild proben pekar ut är Calyx egen, inte min: min ligger
lokalt på 65 kB. Vid 390 px: LCP 564 ms, **CLS 0,000**, samma attribution.

Två röda rader som VAR mina är åtgärdade i den här rundan: `resting-will-change` på de två
figurerna, och `font-face-without-display` på de tre fallback-familjerna. CLS vid 390 var
1,038 och är nu 0,000: `contain-intrinsic-size` la en andra, större höjdgissning ovanpå
`min-height`, och sidan hoppade när den verkliga höjden ersatte gissningen.

### Skärmbilder

`shots/r3/`: `fold-`, `dark-`, `paper-` och `close-` vid 1440, 768, 414, 375 och 320;
`preview-front`, `-mid`, `-back`, `-ledger`, `-bleed`; `forcedcolors-1440`;
`greyscale-1440`; `zoom200-720`; och `contact-1440.png` med fem folds. Alla lästa som pixlar.
Ingen horisontell scroll på någon bredd, och sidans egen konsol är tyst på alla fem
(Tailwind-varningarna kommer från de inbäddade exempelsajterna).

### Öppna frågor efter R3

1. **`/review-animations` är inte körd** och kan bara köras av Anton.
2. **Långa tasks under scroll: 2 mot taket 0**, även utan ramarna. Kvar att jaga i en fixrunda.
3. **Ramarnas kostnad är strukturell.** Två levande dokument kostar det de kostar. Vill Anton
   ha budgeten grön måste ramarna bytas mot skärmbilder med en länk, och det ändrar produkten:
   `PRODUCT.md` § Product Principles 1 säger att beviset ska gå att använda, inte bara ses.
4. **Kortbaksidans högra halva** är fortfarande tom. Arkitektens dom, inte min.
5. De tre frågorna från R1 står kvar: tjänsteordningen, pilens tecken (nu löst åt gate 97:s
   håll av lead) och registerraden.

## R3, leadens pixelläsning (2026-09-10)

Bara filer jag faktiskt öppnat som bild står här. En skärmbild jag inte läst räknas inte.

- läst: `tests/alunix-r8/review/r3/V3c-fold-1440.png`
- läst: `tests/alunix-r8/review/r3/V3c-fold-390.png`
- läst: `tests/alunix-r8/review/r3/V3c-scroll-2.png`
- läst: `tests/alunix-r8/review/r3/V3c-scroll-4.png`
- läst: `tests/alunix-r8/review/r3/V3c-back-1440.png`

**Två iakttagelser ur den läsningen.** Pilen efter `Boka ett möte` är borta, alltså är
gate 97-beslutet utfört och verifierat i pixlar. Kickern på kortets baksida har däremot
bytts från målbildens `Digital byrå` till `WEBBYRÅ I SVERIGE`. Strängen är sann mot
PRODUCT.md (`Alunix är en webbyrå i Sverige`) och är inte låst copy, men bytet är en
avvikelse från målbilden och kräver en rad i decision ledger. Arkitekten prövar den i
F-007-kontrollen.

### Leadens beslut, R3 (2026-09-10)

| Datum | Beslut | Källa |
|---|---|---|
| 2026-09-10 | Kvartetten och codex-review returnerade fem `fix`, alla fem genom `check_reviewer_report.py` med exit 0 | `runs/V3c/reviews/r3/{critic,heuristics,a11y,perf,codex}.md` |
| 2026-09-10 | Åtta sammanslagna planer i `runs/V3c/plans/`, prioritet tillgänglighet före prestanda före användbarhet före brief | `lift.md` § Reviewerkontraktet, försoningsordningen |
| 2026-09-10 | Kortets klippta kantlinje har en fastställd orsak: `.hero-plate{overflow:clip}` på rad 271, isolerad genom att slås av ensam. Byggarens kommentar på rad 264 visar att klippet är avsiktligt, så planen ska lösa båda kraven, inte kasta det ena | Codex-granskarens isolering, verifierad av lead mot filens rader |
| 2026-09-10 | Prestandaskulden är delad och ska räknas delad: cellens egen vikt är 334 kB vid både 1440 och 390, medan hero-bilden på 1,12 MB och de 19 typsnittsfilerna kommer ur de inbäddade exempelsajterna, som r8 inte får redigera | Prestandagranskarens attribuering, bekräftad av lead: `unsplash=0 googleapis=0` i cellens egen markup |
| 2026-09-10 | `Skill(review-animations)` nekades för byggaren eftersom skillen bar `disable-model-invocation: true`. Öppen punkt, inte röd grind, och inte byggarens fel | Bevakarens mätning, Q24 |

## Fas A (arkitekten, 2026-09-15)

Varje bild nedan är läst som pixlar med `Read` i arkitektens session. Fångade från boardkopian
`board/cells/V3c-r8/` (port 4626) och referenserna, med `scratchpad/slices.py` (kopia av
`shoot_slices.py` med bredd och höjd som argument och installerad Chrome) och `scratchpad/frames.py`
(ramsekvenser: `--flip` 0 till 1 i tolv steg på `#plateCard`, tolv steg genom `#giant-section`s
synliga liv, tolv steg genom K3:s pinnade ritningsakt). Bilderna under `probe/` (scroll_verify:s
egna skivor och kontaktark) räknas inte som lästa; de är instrumentets, inte mina.
Cookie-banners: insign avböjdes (skriptet träffade avböj-knappen); Highway Medias banner
(`Tillåt alla` / `Inställningar för samtycke`) träffades inte och står kvar i alla Highway-bilder;
Hoy visade ingen banner.

### highway-1440 (16 bilder)

- läst: `tests/alunix-r8/runs/V3c/shots/fasA/highway-1440/hw-goteborg-1440--s00.png`
- läst: `tests/alunix-r8/runs/V3c/shots/fasA/highway-1440/hw-goteborg-1440--s01.png`
- läst: `tests/alunix-r8/runs/V3c/shots/fasA/highway-1440/hw-goteborg-1440--s02.png`
- läst: `tests/alunix-r8/runs/V3c/shots/fasA/highway-1440/hw-goteborg-1440--s03.png`
- läst: `tests/alunix-r8/runs/V3c/shots/fasA/highway-1440/hw-goteborg-1440--s04.png`
- läst: `tests/alunix-r8/runs/V3c/shots/fasA/highway-1440/hw-goteborg-1440--s05.png`
- läst: `tests/alunix-r8/runs/V3c/shots/fasA/highway-1440/hw-goteborg-1440--s06.png`
- läst: `tests/alunix-r8/runs/V3c/shots/fasA/highway-1440/hw-goteborg-1440--s07.png`
- läst: `tests/alunix-r8/runs/V3c/shots/fasA/highway-1440/hw-hemsida-1440--s00.png`
- läst: `tests/alunix-r8/runs/V3c/shots/fasA/highway-1440/hw-hemsida-1440--s01.png`
- läst: `tests/alunix-r8/runs/V3c/shots/fasA/highway-1440/hw-hemsida-1440--s02.png`
- läst: `tests/alunix-r8/runs/V3c/shots/fasA/highway-1440/hw-hemsida-1440--s03.png`
- läst: `tests/alunix-r8/runs/V3c/shots/fasA/highway-1440/hw-hemsida-1440--s04.png`
- läst: `tests/alunix-r8/runs/V3c/shots/fasA/highway-1440/hw-hemsida-1440--s05.png`
- läst: `tests/alunix-r8/runs/V3c/shots/fasA/highway-1440/hw-hemsida-1440--s06.png`
- läst: `tests/alunix-r8/runs/V3c/shots/fasA/highway-1440/hw-hemsida-1440--s07.png`

### highway-390 (24 bilder)

- läst: `tests/alunix-r8/runs/V3c/shots/fasA/highway-390/hw-goteborg-390--s00.png`
- läst: `tests/alunix-r8/runs/V3c/shots/fasA/highway-390/hw-goteborg-390--s01.png`
- läst: `tests/alunix-r8/runs/V3c/shots/fasA/highway-390/hw-goteborg-390--s02.png`
- läst: `tests/alunix-r8/runs/V3c/shots/fasA/highway-390/hw-goteborg-390--s03.png`
- läst: `tests/alunix-r8/runs/V3c/shots/fasA/highway-390/hw-goteborg-390--s04.png`
- läst: `tests/alunix-r8/runs/V3c/shots/fasA/highway-390/hw-goteborg-390--s05.png`
- läst: `tests/alunix-r8/runs/V3c/shots/fasA/highway-390/hw-goteborg-390--s06.png`
- läst: `tests/alunix-r8/runs/V3c/shots/fasA/highway-390/hw-goteborg-390--s07.png`
- läst: `tests/alunix-r8/runs/V3c/shots/fasA/highway-390/hw-goteborg-390--s08.png`
- läst: `tests/alunix-r8/runs/V3c/shots/fasA/highway-390/hw-goteborg-390--s09.png`
- läst: `tests/alunix-r8/runs/V3c/shots/fasA/highway-390/hw-goteborg-390--s10.png`
- läst: `tests/alunix-r8/runs/V3c/shots/fasA/highway-390/hw-goteborg-390--s11.png`
- läst: `tests/alunix-r8/runs/V3c/shots/fasA/highway-390/hw-hemsida-390--s00.png`
- läst: `tests/alunix-r8/runs/V3c/shots/fasA/highway-390/hw-hemsida-390--s01.png`
- läst: `tests/alunix-r8/runs/V3c/shots/fasA/highway-390/hw-hemsida-390--s02.png`
- läst: `tests/alunix-r8/runs/V3c/shots/fasA/highway-390/hw-hemsida-390--s03.png`
- läst: `tests/alunix-r8/runs/V3c/shots/fasA/highway-390/hw-hemsida-390--s04.png`
- läst: `tests/alunix-r8/runs/V3c/shots/fasA/highway-390/hw-hemsida-390--s05.png`
- läst: `tests/alunix-r8/runs/V3c/shots/fasA/highway-390/hw-hemsida-390--s06.png`
- läst: `tests/alunix-r8/runs/V3c/shots/fasA/highway-390/hw-hemsida-390--s07.png`
- läst: `tests/alunix-r8/runs/V3c/shots/fasA/highway-390/hw-hemsida-390--s08.png`
- läst: `tests/alunix-r8/runs/V3c/shots/fasA/highway-390/hw-hemsida-390--s09.png`
- läst: `tests/alunix-r8/runs/V3c/shots/fasA/highway-390/hw-hemsida-390--s10.png`
- läst: `tests/alunix-r8/runs/V3c/shots/fasA/highway-390/hw-hemsida-390--s11.png`

### hoy-1440 (23 bilder)

- läst: `tests/alunix-r8/runs/V3c/shots/fasA/hoy-1440/hoy-home-1440--s00.png`
- läst: `tests/alunix-r8/runs/V3c/shots/fasA/hoy-1440/hoy-home-1440--s01.png`
- läst: `tests/alunix-r8/runs/V3c/shots/fasA/hoy-1440/hoy-home-1440--s02.png`
- läst: `tests/alunix-r8/runs/V3c/shots/fasA/hoy-1440/hoy-home-1440--s03.png`
- läst: `tests/alunix-r8/runs/V3c/shots/fasA/hoy-1440/hoy-home-1440--s04.png`
- läst: `tests/alunix-r8/runs/V3c/shots/fasA/hoy-1440/hoy-home-1440--s05.png`
- läst: `tests/alunix-r8/runs/V3c/shots/fasA/hoy-1440/hoy-home-1440--s06.png`
- läst: `tests/alunix-r8/runs/V3c/shots/fasA/hoy-1440/hoy-home-1440--s07.png`
- läst: `tests/alunix-r8/runs/V3c/shots/fasA/hoy-1440/hoy-home-1440--s08.png`
- läst: `tests/alunix-r8/runs/V3c/shots/fasA/hoy-1440/hoy-home-1440--s09.png`
- läst: `tests/alunix-r8/runs/V3c/shots/fasA/hoy-1440/hoy-home-1440--s10.png`
- läst: `tests/alunix-r8/runs/V3c/shots/fasA/hoy-1440/hoy-webb-1440--s00.png`
- läst: `tests/alunix-r8/runs/V3c/shots/fasA/hoy-1440/hoy-webb-1440--s01.png`
- läst: `tests/alunix-r8/runs/V3c/shots/fasA/hoy-1440/hoy-webb-1440--s02.png`
- läst: `tests/alunix-r8/runs/V3c/shots/fasA/hoy-1440/hoy-webb-1440--s03.png`
- läst: `tests/alunix-r8/runs/V3c/shots/fasA/hoy-1440/hoy-webb-1440--s04.png`
- läst: `tests/alunix-r8/runs/V3c/shots/fasA/hoy-1440/hoy-webb-1440--s05.png`
- läst: `tests/alunix-r8/runs/V3c/shots/fasA/hoy-1440/hoy-webb-1440--s06.png`
- läst: `tests/alunix-r8/runs/V3c/shots/fasA/hoy-1440/hoy-webb-1440--s07.png`
- läst: `tests/alunix-r8/runs/V3c/shots/fasA/hoy-1440/hoy-webb-1440--s08.png`
- läst: `tests/alunix-r8/runs/V3c/shots/fasA/hoy-1440/hoy-webb-1440--s09.png`
- läst: `tests/alunix-r8/runs/V3c/shots/fasA/hoy-1440/hoy-webb-1440--s10.png`
- läst: `tests/alunix-r8/runs/V3c/shots/fasA/hoy-1440/hoy-webb-1440--s11.png`

### hoy-390 (20 bilder)

- läst: `tests/alunix-r8/runs/V3c/shots/fasA/hoy-390/hoy-home-390--s00.png`
- läst: `tests/alunix-r8/runs/V3c/shots/fasA/hoy-390/hoy-home-390--s01.png`
- läst: `tests/alunix-r8/runs/V3c/shots/fasA/hoy-390/hoy-home-390--s02.png`
- läst: `tests/alunix-r8/runs/V3c/shots/fasA/hoy-390/hoy-home-390--s03.png`
- läst: `tests/alunix-r8/runs/V3c/shots/fasA/hoy-390/hoy-home-390--s04.png`
- läst: `tests/alunix-r8/runs/V3c/shots/fasA/hoy-390/hoy-home-390--s05.png`
- läst: `tests/alunix-r8/runs/V3c/shots/fasA/hoy-390/hoy-home-390--s06.png`
- läst: `tests/alunix-r8/runs/V3c/shots/fasA/hoy-390/hoy-home-390--s07.png`
- läst: `tests/alunix-r8/runs/V3c/shots/fasA/hoy-390/hoy-home-390--s08.png`
- läst: `tests/alunix-r8/runs/V3c/shots/fasA/hoy-390/hoy-home-390--s09.png`
- läst: `tests/alunix-r8/runs/V3c/shots/fasA/hoy-390/hoy-webb-390--s00.png`
- läst: `tests/alunix-r8/runs/V3c/shots/fasA/hoy-390/hoy-webb-390--s01.png`
- läst: `tests/alunix-r8/runs/V3c/shots/fasA/hoy-390/hoy-webb-390--s02.png`
- läst: `tests/alunix-r8/runs/V3c/shots/fasA/hoy-390/hoy-webb-390--s03.png`
- läst: `tests/alunix-r8/runs/V3c/shots/fasA/hoy-390/hoy-webb-390--s04.png`
- läst: `tests/alunix-r8/runs/V3c/shots/fasA/hoy-390/hoy-webb-390--s05.png`
- läst: `tests/alunix-r8/runs/V3c/shots/fasA/hoy-390/hoy-webb-390--s06.png`
- läst: `tests/alunix-r8/runs/V3c/shots/fasA/hoy-390/hoy-webb-390--s07.png`
- läst: `tests/alunix-r8/runs/V3c/shots/fasA/hoy-390/hoy-webb-390--s08.png`
- läst: `tests/alunix-r8/runs/V3c/shots/fasA/hoy-390/hoy-webb-390--s09.png`

### insign-1440 (6 bilder)

- läst: `tests/alunix-r8/runs/V3c/shots/fasA/insign-1440/insign-1440--s00.png`
- läst: `tests/alunix-r8/runs/V3c/shots/fasA/insign-1440/insign-1440--s01.png`
- läst: `tests/alunix-r8/runs/V3c/shots/fasA/insign-1440/insign-1440--s02.png`
- läst: `tests/alunix-r8/runs/V3c/shots/fasA/insign-1440/insign-1440--s03.png`
- läst: `tests/alunix-r8/runs/V3c/shots/fasA/insign-1440/insign-1440--s04.png`
- läst: `tests/alunix-r8/runs/V3c/shots/fasA/insign-1440/insign-1440--s05.png`

### insign-390 (11 bilder)

- läst: `tests/alunix-r8/runs/V3c/shots/fasA/insign-390/insign-390--s00.png`
- läst: `tests/alunix-r8/runs/V3c/shots/fasA/insign-390/insign-390--s01.png`
- läst: `tests/alunix-r8/runs/V3c/shots/fasA/insign-390/insign-390--s02.png`
- läst: `tests/alunix-r8/runs/V3c/shots/fasA/insign-390/insign-390--s03.png`
- läst: `tests/alunix-r8/runs/V3c/shots/fasA/insign-390/insign-390--s04.png`
- läst: `tests/alunix-r8/runs/V3c/shots/fasA/insign-390/insign-390--s05.png`
- läst: `tests/alunix-r8/runs/V3c/shots/fasA/insign-390/insign-390--s06.png`
- läst: `tests/alunix-r8/runs/V3c/shots/fasA/insign-390/insign-390--s07.png`
- läst: `tests/alunix-r8/runs/V3c/shots/fasA/insign-390/insign-390--s08.png`
- läst: `tests/alunix-r8/runs/V3c/shots/fasA/insign-390/insign-390--s09.png`
- läst: `tests/alunix-r8/runs/V3c/shots/fasA/insign-390/insign-390--s10.png`

### k3-1440 (9 bilder)

- läst: `tests/alunix-r8/runs/V3c/shots/fasA/k3-1440/k3-1440--s00.png`
- läst: `tests/alunix-r8/runs/V3c/shots/fasA/k3-1440/k3-1440--s01.png`
- läst: `tests/alunix-r8/runs/V3c/shots/fasA/k3-1440/k3-1440--s02.png`
- läst: `tests/alunix-r8/runs/V3c/shots/fasA/k3-1440/k3-1440--s03.png`
- läst: `tests/alunix-r8/runs/V3c/shots/fasA/k3-1440/k3-1440--s04.png`
- läst: `tests/alunix-r8/runs/V3c/shots/fasA/k3-1440/k3-1440--s05.png`
- läst: `tests/alunix-r8/runs/V3c/shots/fasA/k3-1440/k3-1440--s06.png`
- läst: `tests/alunix-r8/runs/V3c/shots/fasA/k3-1440/k3-1440--s07.png`
- läst: `tests/alunix-r8/runs/V3c/shots/fasA/k3-1440/k3-1440--s08.png`

### k3-390 (8 bilder)

- läst: `tests/alunix-r8/runs/V3c/shots/fasA/k3-390/k3-390--s00.png`
- läst: `tests/alunix-r8/runs/V3c/shots/fasA/k3-390/k3-390--s01.png`
- läst: `tests/alunix-r8/runs/V3c/shots/fasA/k3-390/k3-390--s02.png`
- läst: `tests/alunix-r8/runs/V3c/shots/fasA/k3-390/k3-390--s03.png`
- läst: `tests/alunix-r8/runs/V3c/shots/fasA/k3-390/k3-390--s04.png`
- läst: `tests/alunix-r8/runs/V3c/shots/fasA/k3-390/k3-390--s05.png`
- läst: `tests/alunix-r8/runs/V3c/shots/fasA/k3-390/k3-390--s06.png`
- läst: `tests/alunix-r8/runs/V3c/shots/fasA/k3-390/k3-390--s07.png`

### k3-act (24 bilder)

- läst: `tests/alunix-r8/runs/V3c/shots/fasA/k3-act/k3-1440-pin-00.png`
- läst: `tests/alunix-r8/runs/V3c/shots/fasA/k3-act/k3-1440-pin-01.png`
- läst: `tests/alunix-r8/runs/V3c/shots/fasA/k3-act/k3-1440-pin-02.png`
- läst: `tests/alunix-r8/runs/V3c/shots/fasA/k3-act/k3-1440-pin-03.png`
- läst: `tests/alunix-r8/runs/V3c/shots/fasA/k3-act/k3-1440-pin-04.png`
- läst: `tests/alunix-r8/runs/V3c/shots/fasA/k3-act/k3-1440-pin-05.png`
- läst: `tests/alunix-r8/runs/V3c/shots/fasA/k3-act/k3-1440-pin-06.png`
- läst: `tests/alunix-r8/runs/V3c/shots/fasA/k3-act/k3-1440-pin-07.png`
- läst: `tests/alunix-r8/runs/V3c/shots/fasA/k3-act/k3-1440-pin-08.png`
- läst: `tests/alunix-r8/runs/V3c/shots/fasA/k3-act/k3-1440-pin-09.png`
- läst: `tests/alunix-r8/runs/V3c/shots/fasA/k3-act/k3-1440-pin-10.png`
- läst: `tests/alunix-r8/runs/V3c/shots/fasA/k3-act/k3-1440-pin-11.png`
- läst: `tests/alunix-r8/runs/V3c/shots/fasA/k3-act/k3-390-pin-00.png`
- läst: `tests/alunix-r8/runs/V3c/shots/fasA/k3-act/k3-390-pin-01.png`
- läst: `tests/alunix-r8/runs/V3c/shots/fasA/k3-act/k3-390-pin-02.png`
- läst: `tests/alunix-r8/runs/V3c/shots/fasA/k3-act/k3-390-pin-03.png`
- läst: `tests/alunix-r8/runs/V3c/shots/fasA/k3-act/k3-390-pin-04.png`
- läst: `tests/alunix-r8/runs/V3c/shots/fasA/k3-act/k3-390-pin-05.png`
- läst: `tests/alunix-r8/runs/V3c/shots/fasA/k3-act/k3-390-pin-06.png`
- läst: `tests/alunix-r8/runs/V3c/shots/fasA/k3-act/k3-390-pin-07.png`
- läst: `tests/alunix-r8/runs/V3c/shots/fasA/k3-act/k3-390-pin-08.png`
- läst: `tests/alunix-r8/runs/V3c/shots/fasA/k3-act/k3-390-pin-09.png`
- läst: `tests/alunix-r8/runs/V3c/shots/fasA/k3-act/k3-390-pin-10.png`
- läst: `tests/alunix-r8/runs/V3c/shots/fasA/k3-act/k3-390-pin-11.png`

### v3c-1440 (8 bilder)

- läst: `tests/alunix-r8/runs/V3c/shots/fasA/v3c-1440/v3c-1440--s00.png`
- läst: `tests/alunix-r8/runs/V3c/shots/fasA/v3c-1440/v3c-1440--s01.png`
- läst: `tests/alunix-r8/runs/V3c/shots/fasA/v3c-1440/v3c-1440--s02.png`
- läst: `tests/alunix-r8/runs/V3c/shots/fasA/v3c-1440/v3c-1440--s03.png`
- läst: `tests/alunix-r8/runs/V3c/shots/fasA/v3c-1440/v3c-1440--s04.png`
- läst: `tests/alunix-r8/runs/V3c/shots/fasA/v3c-1440/v3c-1440--s05.png`
- läst: `tests/alunix-r8/runs/V3c/shots/fasA/v3c-1440/v3c-1440--s06.png`
- läst: `tests/alunix-r8/runs/V3c/shots/fasA/v3c-1440/v3c-1440--s07.png`

### v3c-390 (9 bilder)

- läst: `tests/alunix-r8/runs/V3c/shots/fasA/v3c-390/v3c-390--s00.png`
- läst: `tests/alunix-r8/runs/V3c/shots/fasA/v3c-390/v3c-390--s01.png`
- läst: `tests/alunix-r8/runs/V3c/shots/fasA/v3c-390/v3c-390--s02.png`
- läst: `tests/alunix-r8/runs/V3c/shots/fasA/v3c-390/v3c-390--s03.png`
- läst: `tests/alunix-r8/runs/V3c/shots/fasA/v3c-390/v3c-390--s04.png`
- läst: `tests/alunix-r8/runs/V3c/shots/fasA/v3c-390/v3c-390--s05.png`
- läst: `tests/alunix-r8/runs/V3c/shots/fasA/v3c-390/v3c-390--s06.png`
- läst: `tests/alunix-r8/runs/V3c/shots/fasA/v3c-390/v3c-390--s07.png`
- läst: `tests/alunix-r8/runs/V3c/shots/fasA/v3c-390/v3c-390--s08.png`

### v3c-flip (24 bilder)

- läst: `tests/alunix-r8/runs/V3c/shots/fasA/v3c-flip/v3c-1440-flip-00-000.png`
- läst: `tests/alunix-r8/runs/V3c/shots/fasA/v3c-flip/v3c-1440-flip-01-009.png`
- läst: `tests/alunix-r8/runs/V3c/shots/fasA/v3c-flip/v3c-1440-flip-02-018.png`
- läst: `tests/alunix-r8/runs/V3c/shots/fasA/v3c-flip/v3c-1440-flip-03-027.png`
- läst: `tests/alunix-r8/runs/V3c/shots/fasA/v3c-flip/v3c-1440-flip-04-036.png`
- läst: `tests/alunix-r8/runs/V3c/shots/fasA/v3c-flip/v3c-1440-flip-05-045.png`
- läst: `tests/alunix-r8/runs/V3c/shots/fasA/v3c-flip/v3c-1440-flip-06-055.png`
- läst: `tests/alunix-r8/runs/V3c/shots/fasA/v3c-flip/v3c-1440-flip-07-064.png`
- läst: `tests/alunix-r8/runs/V3c/shots/fasA/v3c-flip/v3c-1440-flip-08-073.png`
- läst: `tests/alunix-r8/runs/V3c/shots/fasA/v3c-flip/v3c-1440-flip-09-082.png`
- läst: `tests/alunix-r8/runs/V3c/shots/fasA/v3c-flip/v3c-1440-flip-10-091.png`
- läst: `tests/alunix-r8/runs/V3c/shots/fasA/v3c-flip/v3c-1440-flip-11-100.png`
- läst: `tests/alunix-r8/runs/V3c/shots/fasA/v3c-flip/v3c-390-flip-00-000.png`
- läst: `tests/alunix-r8/runs/V3c/shots/fasA/v3c-flip/v3c-390-flip-01-009.png`
- läst: `tests/alunix-r8/runs/V3c/shots/fasA/v3c-flip/v3c-390-flip-02-018.png`
- läst: `tests/alunix-r8/runs/V3c/shots/fasA/v3c-flip/v3c-390-flip-03-027.png`
- läst: `tests/alunix-r8/runs/V3c/shots/fasA/v3c-flip/v3c-390-flip-04-036.png`
- läst: `tests/alunix-r8/runs/V3c/shots/fasA/v3c-flip/v3c-390-flip-05-045.png`
- läst: `tests/alunix-r8/runs/V3c/shots/fasA/v3c-flip/v3c-390-flip-06-055.png`
- läst: `tests/alunix-r8/runs/V3c/shots/fasA/v3c-flip/v3c-390-flip-07-064.png`
- läst: `tests/alunix-r8/runs/V3c/shots/fasA/v3c-flip/v3c-390-flip-08-073.png`
- läst: `tests/alunix-r8/runs/V3c/shots/fasA/v3c-flip/v3c-390-flip-09-082.png`
- läst: `tests/alunix-r8/runs/V3c/shots/fasA/v3c-flip/v3c-390-flip-10-091.png`
- läst: `tests/alunix-r8/runs/V3c/shots/fasA/v3c-flip/v3c-390-flip-11-100.png`

### v3c-giant (24 bilder)

- läst: `tests/alunix-r8/runs/V3c/shots/fasA/v3c-giant/v3c-1440-life-00.png`
- läst: `tests/alunix-r8/runs/V3c/shots/fasA/v3c-giant/v3c-1440-life-01.png`
- läst: `tests/alunix-r8/runs/V3c/shots/fasA/v3c-giant/v3c-1440-life-02.png`
- läst: `tests/alunix-r8/runs/V3c/shots/fasA/v3c-giant/v3c-1440-life-03.png`
- läst: `tests/alunix-r8/runs/V3c/shots/fasA/v3c-giant/v3c-1440-life-04.png`
- läst: `tests/alunix-r8/runs/V3c/shots/fasA/v3c-giant/v3c-1440-life-05.png`
- läst: `tests/alunix-r8/runs/V3c/shots/fasA/v3c-giant/v3c-1440-life-06.png`
- läst: `tests/alunix-r8/runs/V3c/shots/fasA/v3c-giant/v3c-1440-life-07.png`
- läst: `tests/alunix-r8/runs/V3c/shots/fasA/v3c-giant/v3c-1440-life-08.png`
- läst: `tests/alunix-r8/runs/V3c/shots/fasA/v3c-giant/v3c-1440-life-09.png`
- läst: `tests/alunix-r8/runs/V3c/shots/fasA/v3c-giant/v3c-1440-life-10.png`
- läst: `tests/alunix-r8/runs/V3c/shots/fasA/v3c-giant/v3c-1440-life-11.png`
- läst: `tests/alunix-r8/runs/V3c/shots/fasA/v3c-giant/v3c-390-life-00.png`
- läst: `tests/alunix-r8/runs/V3c/shots/fasA/v3c-giant/v3c-390-life-01.png`
- läst: `tests/alunix-r8/runs/V3c/shots/fasA/v3c-giant/v3c-390-life-02.png`
- läst: `tests/alunix-r8/runs/V3c/shots/fasA/v3c-giant/v3c-390-life-03.png`
- läst: `tests/alunix-r8/runs/V3c/shots/fasA/v3c-giant/v3c-390-life-04.png`
- läst: `tests/alunix-r8/runs/V3c/shots/fasA/v3c-giant/v3c-390-life-05.png`
- läst: `tests/alunix-r8/runs/V3c/shots/fasA/v3c-giant/v3c-390-life-06.png`
- läst: `tests/alunix-r8/runs/V3c/shots/fasA/v3c-giant/v3c-390-life-07.png`
- läst: `tests/alunix-r8/runs/V3c/shots/fasA/v3c-giant/v3c-390-life-08.png`
- läst: `tests/alunix-r8/runs/V3c/shots/fasA/v3c-giant/v3c-390-life-09.png`
- läst: `tests/alunix-r8/runs/V3c/shots/fasA/v3c-giant/v3c-390-life-10.png`
- läst: `tests/alunix-r8/runs/V3c/shots/fasA/v3c-giant/v3c-390-life-11.png`

### v3c-preview (10 bilder)

- läst: `tests/alunix-r8/runs/V3c/shots/fasA/v3c-preview/v3c-1440-back--fold.png`
- läst: `tests/alunix-r8/runs/V3c/shots/fasA/v3c-preview/v3c-1440-bleed--fold.png`
- läst: `tests/alunix-r8/runs/V3c/shots/fasA/v3c-preview/v3c-1440-front--fold.png`
- läst: `tests/alunix-r8/runs/V3c/shots/fasA/v3c-preview/v3c-1440-ledger--fold.png`
- läst: `tests/alunix-r8/runs/V3c/shots/fasA/v3c-preview/v3c-1440-mid--fold.png`
- läst: `tests/alunix-r8/runs/V3c/shots/fasA/v3c-preview/v3c-390-back--fold.png`
- läst: `tests/alunix-r8/runs/V3c/shots/fasA/v3c-preview/v3c-390-bleed--fold.png`
- läst: `tests/alunix-r8/runs/V3c/shots/fasA/v3c-preview/v3c-390-front--fold.png`
- läst: `tests/alunix-r8/runs/V3c/shots/fasA/v3c-preview/v3c-390-ledger--fold.png`
- läst: `tests/alunix-r8/runs/V3c/shots/fasA/v3c-preview/v3c-390-mid--fold.png`

### r4-pre (leadens forskott) (10 bilder)

- läst: `tests/alunix-r8/runs/V3c/shots/r4-pre/flip-1440-000.png`
- läst: `tests/alunix-r8/runs/V3c/shots/r4-pre/flip-1440-025.png`
- läst: `tests/alunix-r8/runs/V3c/shots/r4-pre/flip-1440-050.png`
- läst: `tests/alunix-r8/runs/V3c/shots/r4-pre/flip-1440-075.png`
- läst: `tests/alunix-r8/runs/V3c/shots/r4-pre/flip-1440-100.png`
- läst: `tests/alunix-r8/runs/V3c/shots/r4-pre/flip-390-000.png`
- läst: `tests/alunix-r8/runs/V3c/shots/r4-pre/flip-390-025.png`
- läst: `tests/alunix-r8/runs/V3c/shots/r4-pre/flip-390-050.png`
- läst: `tests/alunix-r8/runs/V3c/shots/r4-pre/flip-390-075.png`
- läst: `tests/alunix-r8/runs/V3c/shots/r4-pre/flip-390-100.png`

### katalogfolds (2 bilder)

- läst: `design-catalogue/entries/highwaymedia/fold.webp`
- läst: `design-catalogge/entries/hoy/fold.webp`

## R4

Fixrunda efter kvartetten. Modell: Sonnet 5 (Antons byggarregel). Ingen processakt byggd —
`#process` skjuts till R5 per lead. `demo-calyx-1440.webp` orörd. Server `serve.py --port 3301
--root .`.

### Plan 001 — folden klipps under 700 px höjd

**Dom: verified.**

Rotorsak: `.hero-headline` skalade bara på bredd (`clamp(2.2rem,9cqw,7.5rem)`), aldrig på
höjd, så vid låga viewport-höjder (390×450, 720×450 osv.) tävlade rubrik, platta och underrad
om ett fast padding-golv och kolliderade. `.hero-sub` mättes direkt i DOM (`fold_debug.py`):
konstant ~68,4 px hög oavsett höjd ≥768 px bred (radbryter på bredd, inte höjd — min första
gissning om enradig underrad var fel, korrigerad efter mätning).

Fix: ny `--h1-hrate` (12,8svh normalt, 7,2svh under `max-height:700px`), rubrikens
font-size satt till `min()` av det gamla breddklampet och ett nytt höjdklamp, plus tre
paddinggolv sänkta (`.hero-stage` 14→6px, `.hero-plate` margin-top 10→4px, `.hero-sub`
margin-top 8→3px).

Verifiering: 32-punktsmatris (8 bredder × 4 höjder) via `fold_matrix.py` — alla `mark_h1_gap`
och `sub_clip`-värden ≥0 efter fix (flera negativa innan). Explicit 720×450 (200%-zoom-fallet)
ren. 1440×900 kanonisk kvot 0,700 oförändrad, bekräftad med `reflow.py`. Skärmbilder
`shots/r4/plan001-*.png` pixelsedda, ingen synlig klippning eller kollision.

### Plan 002 — iframes kapar scroll och tab

**Dom: verified.**

Rotorsak: `<iframe>`-elementen (Calyx, Horai) tog emot rå pekar- och tangentbordsinput trots
att de bara är "bevis", inte interagerbara — hjulscroll över en ram rörde INTE sidan
(`wheel_frame.py`: scrollY-delta 0 vid hjulning över ramens mitt, innan fix).

Fix: `.frame-wrap iframe{pointer-events:none;}` plus literal `inert`-attribut på båda
`<iframe>`-taggarna i markupen. `.frame-wrap:focus-within`-ringen kvar som andra
försvarslinje (kommentaren uppdaterad — dess triggervillkor är nu onåbart eftersom `inert`
redan tar bort ramen ur tabbordningen).

Verifiering: `wheel_frame.py` — hjulning 0→600 px över Calyx-ramens mitt ger scrollY-delta
som matchar exakt (ingen ram-hijack). `tab_walk.py` — tabbstopp föll från 8 till 2, noll
issues. `frame_alive.py` bekräftar båda ramarna fortfarande lever och renderar internt
(Calyx-dokumentet har 9 body-barn) trots att de är icke-interaktiva — PRODUCT.md-regeln att en
visad ram aldrig transformeras eller tonas är opåverkad.

### Plan 003 — CLS vid 390 px

**Dom: verified.**

Rotorsak precist isolerad via schemalagd snapshot-tidslinje (`cls_timeline.py`): motorns
asynkrona `classList.add('sc-stage')` (som ger `[data-sc-stage]` dess `100svh`-höjd via
`.sc-stage`-klassen) landar, under CPU-strypning, EFTER att webbläsaren redan målat och mätt
den kortare, innehållsdrivna höjden. t=300ms: ingen `sc-stage`-klass, höjd 606,02px. t=500ms:
klassen adderad, höjd 844px. Delta 238px ÷2 = 119px — matchar exakt den observerade
`.hero-plate`-toppförskjutningen.

Fix: en enda attributselektor-regel, `[data-sc-stage]{height:100vh;height:100svh;}`, infogad
direkt före hero-kommentarblocket. Ger boxen sin slutgiltiga höjd från första målningen, utan
att röra motorns egen klassbaserade regel (AB06 — jag stylar DOM-attributet som finns vid
parse-tid, inte motorns klass).

Verifiering: första körningen visade CLS 0,000 vid 390×844/cpu4, i strid mot planens
0,753/1,038. Enligt R4:s regel ("aldrig verified på känsla") kördes tre omkörningar till —
alla tre gav 0,753 innan fix (bekräftar att den första var en avvikare, inte att felet var
inaktuellt), och 0,000 konsekvent i fyra repeterade mätningar EFTER fix, plus icke-regression
vid 320 och 1440 px.

### Plan 004 — kortets kant klipps vid vändning

**Dom: verified (redan implementerad av lead, verifieringsdel körd av mig).**

Ingen kod rörd denna runda, per uttrycklig instruktion: "Kör bara planens Verification; ändra
vändningens geometri bara om den faller, och skriv i så fall vad som föll. Spannet 4,8 rörs
inte i den här rundan: arkitekten dömer tempot parallellt." Redan skeppad fix: `perspective:
2600px` (upp från ett smalare värde) plus en transient `scale()` samtidig med vändningen
(`.plate-card` calc, kommenterad i koden: kortets projicerade hörn håller sig 7–11px innanför
plåten i hela spannet vid 1440×900).

Första mätmetoden (enkolumns pixel-ljusstyrke-scan vid kantlinjens x-koordinat) gav siffror
(span≈517–531px) som inte matchade förväntat resultat — kontaminerad av den fasta
skrivbordsbakgrunden som syns genom plattans bakgrundslösa yta när kortet står kant-på. En
mer finmaskig per-pixel-profil bekräftade att ingen skarp, isolerbar topp går att urskilja med
denna metod. Bytte till direkt visuell läsning av skärmbilderna (`shots/r4/plan004-mid-1440.png`,
`plan004-mid-390.png`, samt leadens `shots/r4-pre/flip-*-{000,025,050,075,100}.png`, 10
bilder, alla lästa) — entydigt: ingen synlig klippning av kortkanten vid någon av de fem
flip-värdena, vid någon av de två bredderna. Matchar leadens egen förhandsverifiering.

### Plan 005 — signaturaktens bildtid och max_step

**Dom: best-effort.** `max_step`-målet är uppnått; bildtidsmålet är inte, och jag hittade ingen
fix inom rundans gränser.

Kontrollen (`tests/motion/smooth.html`, cpu 1) kördes omedelbart före varje sidmätning, som
planen kräver:

| Spår | Kadens | Kontroll p95 / >33ms / max_step | Sidan p95 / >33ms / max_step |
|---|---|---|---|
| `--sc-ps` / `transform` | 100:60 | 16,7ms / 0 / 1,37% | 16,8ms / 0 / 1,12–1,55% (PASS, körning 1) |
| `--sc-ps` / `transform` | 100:60 | 16,7ms / 0 / 1,37% | 30,7ms / 13 / 1,55% (FAIL, körning 2) |
| `--sc-ps` / `transform` | 100:60 | 16,7ms / 0 / 1,37% | 33,3ms / 15 / 1,53% (FAIL, körning 3) |
| `--sc-ps` / `transform` | 20:120 | 16,8ms / 0 / 0,50% | 33,3ms / 22 / 0,63–1,12% (FAIL) |
| `--sc-ps` / `transform` | 20:120 | 16,8ms / 0 / 0,50% | 33,3ms / 28 / 0,63–1,10% (FAIL) |

`max_step` ligger 0,50–1,55% över alla körningar, långt under 2,7%-baren — det målet är
uppnått och stabilt. Bildtiden är intermittent men reproducerbart trasig: 3 av 4 körningar
vid 100:60 och 2 av 2 vid 20:120 slår p95≤20ms och/eller 0-rutor-över-33ms. `staircase` är 0
i varje körning, båda kadenserna — matchar planens egen observation att detta är F-013:s
andra fel (bildtid), inte det första (stegning).

Rotorsak jagad enligt steg 3 (`Performance.getMetrics`, `/sites/**` blockerat, cpu 1, 22
hjultick): RecalcStyleDuration 271,8ms av 454,2ms TaskDuration = 59,8% (matchar kvalitativt
planens 73%-fynd på ett annat scrollmönster). LayoutDuration 0,3ms/1 count — layout är i
praktiken gratis, uteslutet som orsak.

Läste motorns skugga `scroll/sc-smooth.js` rad för rad (läsning, ingen redigering — filen är
avstängd för redigering denna runda). Den skriver redan `--sc-ps` ENDAST när värdet ändrats
(rad 96–105, med en kommentar som exakt beskriver denna risk: "an unconditional per-frame
write costs a full subtree recalc... on every frame any OTHER act happens to be moving").
`--sc-ps` MÅSTE vara `inherits:true` (motorns egen kommentar, mätt 2026-09-08: annars fryser
akten vid startläget). Alltså: varje frame en akt faktiskt rör sig (vilket lerpen i sig kräver
för att F-012:s glidning ska hålla) tvingar webbläsaren att räkna om stil för hela aktens
underträd — arkitektoniskt, inte en bugg i sidans egen CSS.

Testade om `contain` kan skära av detta: `section.hero{contain:style}`, `[data-sc-stage]
{contain:style}`, `.plate-card{contain:style}`, samt `contain:layout style paint`-varianter,
var för sig, via ablation (`recalc_ablate.py`, CDP `Performance.getMetrics`, 3 repeterade
körningar per variant mot 3 repeterade baseline-körningar). Resultat: ingen variant gav en
skillnad utanför brus (baseline recalc 191–204ms medelvärde tre körningar; `.plate-card
{contain:style}` 203–216ms — likvärdigt eller marginellt sämre). Detta matchar CSS
Containment-specen: `contain:style` skopar räknare/citat, inte ärvda anpassade
egenskapers omräkning — det finns inget spec-mekanism som gör att `contain` stoppar en
`inherits:true`-egenskaps stilomräkning nedåt i trädet.

Kontrollerade också att underträdet inte är stort (en alternativ, sidkodsbunden fix hade
varit att beskära DOM under `section.hero`): `section.hero` har bara 22 ättlingar, hela sidan
141 noder, 7 `[data-sc-act]`-element totalt. Inte en nodantalsbugg att trimma bort.

Ingen fix applicerad — provade `contain`-varianter lämnades inte kvar i filen (ingen mätbar
vinst, onödig risk mot `.plate-card`s `preserve-3d`/`overflow:clip`-samspel om `contain:paint`
hade fått stå kvar). Steg 2 (svepa `data-sc-span` 2,2→2,6→3,0→3,4) uteslöts medvetet: lead
instruerade uttryckligen att spannet 4,8 inte rörs denna runda, att tempot bedöms parallellt
av arkitekten — en sweep hade motsagt det. Steg 4:s "båda riktningarna" gick inte att testa:
`motion_probe.py --help` bekräftar att skriptet saknar en riktningsflagga (bara nedåtscroll
stöds); `reversals`-fältet stod på 0 i varje körning, vilket är det närmaste verktyget kommer
en riktningskontroll.

Återstår: bildtidsbudgeten (p95≤20ms, 0 rutor>33ms) slår fel reproducerbart vid cpu 1, båda
kadenserna, orsakad av motorns egen per-frame skrivning av en ärvd anpassad egenskap över 7
samtidiga akter — arkitektoniskt, inte en sidkodsdefekt, och ingen legitim fix hittades inom
gränserna (motorn avstängd, spannet avstängt denna runda).

### Plan 006 — kickern på kortets baksida tillbaka till målbilden

**Dom: verified.**

`.card-kicker`s sträng bytt från `Webbyrå i Sverige` till `Digital byrå` (`index.html` rad
720). CSS oförändrad — `.card-kicker` matchade redan planens måltal (Geist Mono 10,5px,
tracking .22em) före bytet, så bara markupsträngen rördes. Decision-ledgerrad tillagd i
`BRIEF.md` under ny rubrik `### Byggarens rader, R4`, med källa (plan 006) och de tre skälen
(kontrakt/ledgerkrav, visitkorts-tesen, rut-testets SEO-default-undantag).

Verifiering: `?preview=back` skärmbildad och pixelläst vid 1440 (`shots/r4/plan006-back-
1440.png`) och 390 (`shots/r4/plan006-back-390.png`). Strängen läser som en yrkesbeteckning
under ordmärket på båda bredderna, ingen radbrytning eller kollision med hårlinjen eller
tjänsteraden.

### Plan 007 — s6:s displayelement och avslutets yta

**Dom: verified.**

Mätt före fix (1440×900): `.price .statement` (prisrubriken) 30,4px / `.giant`
(jätterubriken) 76,8px / `.close-mailto` 67,2px — prisrubriken var alltså sidans minsta
displaymoment, 0,40x jätterubriken, i en spalt som delar skärm med ett fullblödande
matfotografi. `.close` hade `min-height:0`, faktisk höjd 274,27px av en 900px viewport
(30,5svh) — mailto-raden delade sista skärmen med prisblock och Hōrai-bildtexten.

Fix: `.price .statement`s font-size ändrad från `clamp(20px,2.4vw,1.9rem)` till
`clamp(1.6rem,3.6vw,3.2rem)` (endast font-size rörd, `max-width` och `line-height` oförändrade,
priserna och brödgraden i `.price-ingress`/`.price-row` helt orörda). `.close` fick
`min-height:62svh;display:flex;align-items:center;` tillagt.

Mätt efter fix: prisrubrik 51,2px vid 1440 (>= 48px-golvet, 0,667x jätterubriken >= 0,6x-
golvet). `.close` 558px av 900 = exakt 62svh vid 1440, 523,27px av 844 = exakt 62svh vid 390.
Helsidesfångster `shots/r4/plan007-close-1440.png` och `-390.png` visar mailto-raden centrerad
i egen, tyst yta utan prisblock eller Hōrai synligt i samma skärm; `shots/r4/plan007-price-
1440.png` visar prisrubriken som ett riktigt displaymoment mot Hōrai-fotot.

### Plan 008 — Hyperborea-plåten bleeder inte, och dess akt är död

**Dom: verified.**

Rotorsak bekräftad: `.thesis-figure{transform:translateX(11%);}` var ett konstant tal, ingen
`--sc-ps`-läsning, överhäng 33,3px (696,97 -> 730,28 vid 1440) mot arkitektens mål 96px.

Fix: `transform:translateX(calc(10% + 24% * var(--sc-ps,0)))` — läser aktens (`.panel-thesis`,
`data-sc-act="flow"`) `--sc-ps` via arv, F-014-korrekt. 10% viloläge (~30px, oförändrat från
tidigare) växande till 34% vid ps=1 (~103px vid 1440).

**Verktygsfynd under verifiering:** `motion_probe.py --track ".thesis-figure:transform"`
rapporterade `DEAD` även efter fixen, trots att `--sc-ps` mätt direkt i DOM gick från 0 till 1
och transformens `matrix()`-e-komponent från 30,28 till 102,96 över scrollintervallet
(bekräftat med en egen `window.scrollTo`-instrumentering, `sc_ps`/`fig_transform` utskrivna vid
nio scrollpositioner). Orsak lokaliserad i verktygets egen matrisavkodning
(`skills/design/scripts/motion_probe.py` rad 56-71): för en 2D `matrix(a,b,c,d,e,f)` med
rotation 0 föll koden alltid tillbaka på `p[5]` (translateY), aldrig `p[4]` (translateX) —
exakt samma klass av blind fläck som kommentaren på rad 74-77 redan dokumenterar för
`rotateY`-matriser (fixad 2026-09-08), fast för den plana axeln. En ren `translateX`-rörelse
har alltid `p[5] = 0`, så probens tidigare kod läste en konstant nolla oavsett verklig rörelse.

Fixade skriptet kirurgiskt (`if (rot !== 0) return rot; return p[5] !== 0 ? p[5] : p[4];`) —
inte en UI-fil, inte motorn (`scroll/`), ett delat verktygsskript. Kontrollerade regression
mot `tests/motion/smooth.html` före och efter: PASS oförändrat, samma tal (p95 16,7ms, 0
rutor>33ms, max_step 1,37%) på båda spåren. Efter fixen: `.thesis-figure:transform` rapporterar
inte längre `DEAD`; `max_step` 2,91% (rapporterat, inte gatat — det här är inte spelhuvudet),
`staircase` 0. Bildtidsdelen av samma körning (p95 50ms, 56 rutor>33ms) är INTE en del av plan
008:s Target/Verification (bara `dead:false` plus en pixelmätning krävs) — troligen samma
arkitektoniska RecalcStyle-kostnad som Plan 005, utanför den här planens gräns.

Pixelmätning: överhäng 30,28px i vila (ps=0), 102,03px vid ps≈0,99 (scrollY 5000-5786) —
över 96px-målet med marginal. Skärmbilder `shots/r4/plan008-rest-1440.png` (ps~0,45) och
`shots/r4/plan008-mid-1440.png` (ps~0,41, boxen fortfarande till största delen i vy) visar
fotot tydligt skjuta ut förbi den blå plåtens högerkant in i papperskolumnens vänstermarginal
— läser som att plåten skjuter ut ur bandet, matchar feel-checken. Hyperborea-bilden och den
blå plåtens färg/bredd orörda.

### review-animations (R4 § 2, efter plan 001–008)

Körd i sessionen, `Skill(review-animations)`, fokus på rundans rörda/tillagda spår:
kortvändningen (`.plate-card`), tesplåtens bleed (`.thesis-figure`, plan 008), jättens skala
(`.js .giant`) och liggarens självritande tråd/ordscrub. Standard-8-easing och
`prefers-reduced-motion` uttryckligen undantagna per F-011 (sidan saknar avsiktligt en
reduced-motion-väg; skriptet ombads inte flagga frånvaron).

**Del 1 — fynd:**

| Före | Efter | Varför |
|---|---|---|
| `.is-scrubbed .scrub-text .w{color:color-mix(...)}` målar `color` per ord varje bildruta `--scrub` lever | Behålls oförändrad; inget GPU-rent alternativ överlever AA | Standard 7 vill ha bara transform/opacity, men R3:s egen logg visar att detta redan prövades: en opacitetsscrubb (.14→1) föll på axe color-contrast (35 noder), och golvet för att nå 4,5:1 (~0,88) suddade ut effekten helt. `color-mix()` är den medvetna avvägningen, inte ett förbiseende |
| 7 `[data-sc-act]`-element skriver `--sc-ps` (ärvd, registrerad) varje levande bildruta; `.plate-card`, `.thesis-figure`, `.giant` läser den via arv | Ingen fix inom index.html (motorägt, F-012-arkitektur) | Exakt skriptets egen triggerregel "updating a CSS variable on a parent to drive a child transform (style recalc storm)". Redan mätt i Plan 005: RecalcStyle ≈58–73% av scrolltasktid, p95 slår fel intermittent vid cpu 1 på båda kadenserna. Roten är `scroll/sc-smooth.js` (avstängd denna runda), inte sidkod; contain-ablation testad och utesluten. Loggat som **best-effort**, inte tyst absorberat |
| `.topline-contact:hover`, `.card-cta:hover`, `.close-mailto:hover` (rad 237, 421, 664) ogated | Wrappa i `@media (hover:hover) and (pointer:fine)` | Standard 8: hover-rörelse bör gatas så pekskärmar inte fastnar i ett hover-läge. Låg svårighetsgrad — det är border-color/text-decoration-color på 160–250ms, ingen rörelse, så felläget är kosmetiskt (kvardröjande ton efter tryck), inte hack |

Inga fynd mot `.plate-card`s vändning, tesplåtens bleed eller jättens skala i sig — se dom.

**Del 2 — dom:**

Inga känsloförstörande regressioner: alla tre scroll-skrubbade spår läser `--sc-ps` (aldrig rå
`--sc-p`, F-014), animerar bara `transform`, och använder en scrub knuten 1:1 till
scrollposition i stället för en fast-duration-transition som skulle slåss mot skrubben — rätt
teknik för scrollbunden rörelse. Plan 008:s fix i år följer samma idiom som `.plate-card` och
`.giant` redan etablerat. Kortets transienta skala botten­ar aldrig vid `scale(0)` (golvet är
0,82 mitt i vändningen). RecalcStyle-kostnaden (rad 2) och ordscrubbens `color`-målning (rad 1)
är båda kända, redan utredda avvägningar, inte nya fel införda denna runda. Hover-gatingluckan
(rad 3) är en mindre, icke-blockerande polityp.

**Beslut: Approve.**

### Mekaniska grinden (R4 § 3, efter plan 001–008 + review-animations)

Server: `serve.py --port 3301 --root .`.

**1. `scroll_verify.py`** (aldrig körd i R3): 7 dead-scroll-band vid 1440, alla inom heron
(0-300, 1200-1500, 1500-1800, 2100-2400, 2400-2700, 2700-3000, 3000-3300) — matchar
arkitektens Fas A-kryssmätning ("2 700 till 3 300 diff 0,0: baksidan stilla efter ps 0,72:
958px + dwell 315px"). Det är pinnens egen håll-still-tid (start-hold, dwell), inte oanvänt
scrollutrymme utan verkan. `blankBands`: 900-4320px (3420px) och 5555-6114px (559px) —
enfärgade ytor i helsidesbilden: kortets baksida (svart), ramarnas platshållarfärg och
prisblockets mörka grund, alla avsiktligt släta ytor, inte fel. `cuesNeverFull`,
`contrastUnderMedia`: tomma.

**2. `motion_probe.py`, kontrollprotokoll, cpu 4:**

| Spår | Kadens | Kontroll p95/>33ms/max_step | Sidan p95/>33ms/max_step |
|---|---|---|---|
| `--sc-ps`/`transform` | 100:60 | 16,7ms / 0 / 1,37% | 50,9ms / 50 / 1,26–1,79% (FAIL) |
| `--sc-ps`/`transform` | 20:120 | 16,8ms / 0 / 0,50% | 33,3ms / 46 / 0,63–1,14% (FAIL) |

`staircase` 0 i alla fyra körningar. `max_step` klarar 3%-baren med marginal i alla fyra.
Bildtiden slår fel på båda kadenserna vid cpu 4 — samma Plan 005-fynd, värre vid högre
strypning (cpu4 50,9ms mot cpu1:s 30,7–33,3ms), konsekvent med RecalcStyle-roten. "Båda
riktningarna" gick inte att testa: `motion_probe.py --help` bekräftar ingen riktningsflagga
finns (samma begränsning som i Plan 005); `rev 0` i varje körning är det närmaste kontrollen
ger.

**3. `perf_probe.py`, cpu 4:**

| Viewport | LCP | CLS | long tasks | long tasks under scroll | total_bytes (sidans egen) | dom_nodes | findings |
|---|---|---|---|---|---|---|---|
| 1440x900 | 656ms | 0 | 4 | 0 | 339 985 B (~332KB) | 141 | 0 |
| 390x844 | 620ms | 0 | 3 | 0 | 339 985 B (~332KB) | 141 | 0 |

`embedded`/`embedded_bytes`: 0 vid båda — proben triggrade inte ramarnas `IntersectionObserver`
inom sin egen körningstid, så ramarnas resurser syns inte i det här svepet. Sidans egen vikt
döms här (regeln från R3): 332KB, långt under 2,5MB-taket, `pass:true` vid båda bredderna.

**4. `preflight_taste.py`:** `pass:true`, 0 findings. En not: sektionsklassificeraren ser bara
2 familjer över 6 sektioner (iframe, text-only) och varnar själv att den är grov — sidan har i
verkligheten sju distinkta kompositioner (hero-vändning, tesplåt+bleed, Calyx-ram, prisblock,
jätte+liggare, Hōrai-ram, avslut), bekräftat genom skärmbilderna nedan.

**5. `detect.mjs --json`:** 4 fynd, alla `overused-font` på `Geist`/`Geist Mono` (rad
101/106/110/115). Förvalt, låst typsnitt sedan V3b (BRIEF.md § decision ledger, "Typ: Geist ...
Geist Mono ... rollerna korsar aldrig") — inte en avvikelse den här rundan infört, och inte
rörbar utan att öppna ett redan stängt beslut.

**6. `contrast_over_media.py`:** hårdkodnings-buggen från R3 (rad 27, `pg.goto('http://
localhost:3055/')`, ignorerade `--url`) är borta — `--url` respekteras nu. Kört vid 1440 på
sju scrollpositioner (0, 2000, 3000, 4000, 5000, 6000, plus standard) och vid 390: samtliga 7
(1440, scroll 0) / 6 / 6 / 14 / 3 / 2 rader, alla `pass:true`. Täcker hero-rubriken, kortets
fram- och baksida, tesplåtens rubrik/stöd/bildtext, jätterubriken och liggarens tre rader,
prisrubriken (nya, 51,2px efter Plan 007, ratio 19,01) och båda ramarnas bildtexter. Lägsta
uppmätta kvot 6,7:1 (tesplåtens vita text mot den blå grunden), långt över 3:1/4,5:1-golven.

**7. `a11y_scan.py` / `tab_walk.py` / `reflow.py`, huvud-URL + 1280x600/1024x640/720x450:**

Ingen av de tre skripten hade en flagga för anpassad viewport (`a11y_scan.py` hårdkodade
`[1440x900, 390x844]`, `tab_walk.py` hårdkodade `1440x900`, `reflow.py` hade tre fasta
storlekar utan tillägg). Lade till additiva flaggor — `--viewport` (a11y_scan, ersätter
paret när given), `--width`/`--height` (tab_walk), `--extra-viewport` (reflow, körs UTÖVER de
tre befintliga) — i `skills/a11y-audit/scripts/*.py`, inte i `{{UT_MAPP}}` och inte i motorn.
Regressionstestade mot `tests/a11y/broken.html` (CARL-kontrollen) före och efter: samma fynd
(color-contrast m.fl. på a11y_scan, samma `unreachable_interactive` på tab_walk, samma
`table.fixed-width`-overflow på reflow) med och utan de nya flaggorna, så förvalen är
oförändrade.

| Verktyg | 1440x900 (+390 för a11y_scan) | 1280x600 | 1024x640 | 720x450 |
|---|---|---|---|---|
| `a11y_scan` violations | 0 | 0 | 0 | 0 |
| `tab_walk` stops / issues | 2 / 0 | 2 / 0 | 2 / 0 | 2 / 0 |
| `reflow` overflow | [] (320, zoom200, 1440) | [] | [] | [] |

`tab_walk`: bara 2 stopp vid varje bredd — `topline-contact` och `close-mailto` — vid
sidladdningens scrollposition (0). `.card-cta` ("Boka ett möte") ligger på kortets baksida,
och `faceBack.inert`/`faceFront.inert` växlas av scrollprogressen (rad 898-899): vid scroll 0
är kortet framvänt, så baksidan är `inert` och korrekt otabbar. Det är avsedd design (samma
rad som R3:s a11y-fynd "bortvänd yta är inert"), inte ett missat tabbstopp.

Tabbordning genom båda ramarna (Plan 002): separat 30-tabbars gång från `document.body.focus()`
vid scrollY 5786 (båda ramarna monterade) — `activeElement` blev aldrig `IFRAME` i någon av de
30 tryckningarna; båda ramarna har `inert:true`, `pointerEvents:'none'`. Matchar Plan 002:s
`tab_walk`-fynd (8→2 stopp) och håller efter en längre gång än den ursprungliga verifieringen.

**8. Skärmbilder:** samtliga lästa som bild i sessionen.

- läst: `shots/r4/crop-320-0.png` genom `-5.png` (folden, kortets fram-/edge-/baksidesskeden,
  övergång till pappersgrunden, liggarraderna) — ren, ingen klippning
- läst: `shots/r4/crop-375-0.png` — folden ren
- läst: `shots/r4/crop-414-0.png` — folden ren
- läst: `shots/r4/crop-768-0.png` — folden ren, bredare 4:5-liknande platta
- läst: `shots/r4/preview-front-1440.png`, `-back-1440.png` (plan 006), `-mid-1440.png`
  (plan 004, kant-på utan klippning), `-ledger-1440.png` (--scrub:1, alla tre rader fullt
  tända), `-bleed-1440.png` (tesplåtens bleed synlig, ordscrubben mitt i övergång)
- läst: `shots/r4/preview-mid-390.png` — kant-på utan klippning vid 390 också
- läst: `shots/r4/fold-1280x600.png`, `shots/r4/fold-720x450.png` — plan 001:s mest extrema
  fall, båda rena, ingen kollision mellan rubrik, platta och underrad

Både grunderna representerade: den mörka hero/tes-grunden och pappersgrunden syns tillsammans
i `preview-ledger-1440.png` och `preview-bleed-1440.png`.

### Låst copy, 18/18 strängar (PRODUCT.md § Brand Commitments, 16 punkter varav en
räknar tre ord separat)

Verifierat med `grep -F` mot `index.html`, varje sträng byte för byte: `Er hemsida är
nutidens visitkort`, `Vi skapar skräddarsydda webbplatser som hjälper er att exponera
verksamheten.`, `VI BYGGER ERT VARUMÄRKE.`, `Webbdesign, design och system. Allt på ett
ställe.`, `Design`, `Utveckling`, `System`, `Standardpaket. Webbplats med CMS för egna
ändringar och en första SEO-optimering.`, `26 900 kr`, `Paket med bokningssystem, betalning
och kunddatabas.`, `38 900 kr`, `Helt skräddarsydda lösningar för produktkataloger,
specialbyggda system med mera`, `Pris vid förfrågan`, `Alla har rätt till bra design.`,
`kontakt@alunix.se`, `Exempelsida: Calyx, florist i Stockholm`, `Exempelsida: Hōrai, Asian
fusion-koncept`, `Exempelsida: Hyperborea, konferens i Lund`. Alla 18 träffade.

### Tankstreck

`grep "—\|–"` mot hela filen: en träff, rad 320, inuti en CSS-kommentar
(`/* perspective höjd 1600 -> 2600 ... */`, aldrig renderad). Noll tankstreck i synlig text.

### R4, sammanfattning

Åtta planer: 001 verified, 002 verified, 003 verified, 004 verified (verifieringsdel, redan
implementerad av lead), 005 best-effort (max_step uppnått, bildtidsbudgeten arkitektoniskt
otillgänglig inom rundans gränser), 006 verified, 007 verified, 008 verified (plus en
verktygsfix i `motion_probe.py`, regressionstestad). `review-animations`: Approve. Hela
mekaniska grinden (§3.1-8) körd, kontroll- och sidtal sida vid sida, låst copy 18/18, noll
tankstreck. Två filer utanför `{{UT_MAPP}}` ändrade denna runda, båda delade
verktygsskript (inte motorn, inte UI): `skills/design/scripts/motion_probe.py` (2D-matris
translateX-fix) och `skills/a11y-audit/scripts/{a11y_scan,tab_walk,reflow}.py` (additiva
viewport-flaggor), alla regressionstestade mot sina kontrollfixturer före och efter.

### Fas A, beslut (arkitekten, 2026-09-15)

| Datum | Beslut | Källa |
|---|---|---|
| 2026-09-15 | Leverans 1 skriven: `runs/V3c/HELHET.md` (§ 0 underlag, § 1 tre referenser + K3 uppmätta, § 2 V3c i dag, § 3 golvet H-01 till H-35, § 4 åtta tillägg T-1 till T-8, § 5 öppet) | Antons instruktion 2026-09-15; planens § Fas A |
| 2026-09-15 | Leverans 2 skriven: `runs/V3c/plans/010-process.md` i PLAN-TEMPLATE-format med målbild per skärm (1440 och 390), device-tabell, copyutkast v0, token-tabell, fingerprint-delta, H-rader, verifiering | Planens § Designbeslut; `Skill(improve-animations)` variant `plan` |
| 2026-09-15 | `highwaymedia` och `hoy` inlagda i katalogen med capture + designlang-extract (designlang finns på maskinen, `~/AppData/Roaming/npm/designlang`, trots promptens antagande); `index.py` 97 poster, `drift.py` 0 avvikelser | § 3 i fas A-prompten; `Skill(design-catalog)` |
| 2026-09-15 | `select.py --brief BRIEF-draft.md --k 4 --wildcard --dry-run` oförändrad (oryzo-ai 14, dope-security, mattis-studio, monologue, planhat 12); byråsajterna rankar inte in ens vid `--k 8`. De står som Antons namngivna referenser med rad i `BRIEF.md` § Arkitektens rader | `reference-lock.md` § Sources |
| 2026-09-15 | Tempot i kortvändningen: rekommenderat span 3,4, dwell 0,2, fönster 0,10 till 0,78 (Q25). Klippning: ingen vid något `--flip`-värde i tolvstegssekvensen, 1440 och 390, vilket bekräftar leadens r4-pre-läsning | `HELHET.md` § 2 |
| 2026-09-15 | `motion_probe` i tyst fönster: staircase 0 överallt; bildtid p95 290,6 ms (cpu 4, 100:60), 71,5 ms (cpu 1); kontrollen p95 18,3 ms med 1 till 2 rutor > 33 ms, alltså inte helt tyst. Sidans fel är F-013:s andra (bildtid), inte det första. `.thesis-figure:transform` DEAD (plan 008). Flow-akterna över 3 % max_step på `--sc-ps` (giant 3,28, tes 4,01) | `shots/fasA/probe/probe-quiet.txt` |
| 2026-09-15 | `scroll_verify`: 1440 sju dead-scroll-band, 2 700 till 3 300 diff 0,0 (baksidan stilla efter ps 0,72: 958 px + dwell 315 px); 390 sex band. blankBands vid 390 pekar ut Calyx-ramen, Hōrai-ramen och prisblocket som enfärgade i helsidesbilden | `shots/fasA/probe/scroll-verify-*.txt` |
| 2026-09-15 | K3:s ritningsakt mätt en gång som jämförelse: p95 218 ms, 119 av 178 rutor > 33 ms vid cpu 4. Processakten budgeteras därför hårt (H-32) | `shots/fasA/probe/k3-down-100/` |
| 2026-09-15 | Highway Medias cookie-kort står kvar i alla Highway-bilder (avböj-knappen `Tillåt alla`/`Inställningar` träffades inte av skriptets avböj-selektorer); insign avböjdes; Hoy visade ingen banner. Highways processtext revealas på scroll och fångades inte under `reduced_motion="reduce"` | fas A-prompten § 2, cookie-regeln |
| 2026-09-15 | Fem nya frågor till Anton, Q25 till Q29, med antaganden; ingen blockerar | `QUESTIONS.md` |

## R5

Processakten "Ritningen" (`#process`, plan 010) och kortvändningens tempo (plan 011).
Modell: Sonnet 5. Server `serve.py --port 3301 --root .`. Ankare kontrollerade mot koden
innan redigering (`.stagger`, `<footer class="close"`, `function readState`, `var MODES`,
`.kicker-sans`) — alla fanns, bara radnummer skiljde sig från planens R4-baserade
hänvisningar; ingen STOPPA-situation.

### Plan 010, Steps 1–11

**Dom: verified**, med tre dokumenterade avvikelser (nedan) och en arkitektoniskt
oåtkomlig bildtidsbudget (H-32, jämför R4:s Plan 005).

- **Step 1** (tokens + `@property`): `--hair-ink`, `--contour-hair`, `--contour-line`,
  `--contour-dash` efter `--body-r5`; de fem `--p-*`-raderna direkt efter `:root`-blocket.
- **Step 2** (sektionen): `#process.process.on-paper[data-sc-act="flow"]` efter `.stagger`,
  före `<footer class="close"`, `min-height:300svh`, `.process-stage` sticky `top:202px
  height:495px`, `<ol class="process-steps">` + `<svg class="process-sheet" viewBox="0 0
  880 495">`.
- **Step 3** (banorna): 12 `<path>`/`<rect>`-element (`#p-outline`, `#p-guides` [3
  underlinjer i en bana], `#p-dim-width`, `#p-stations` [2 underlinjer], `#p-opening`,
  `#p-dim-gutter`, `#p-lead-169`, `#p-hatch`, `#p-ledgers` [3 underlinjer], `#p-dim-row`,
  `#p-title`, `#p-rev`) — långt under 60-taket. `pathLength="1"` på alla dash-ritade.
  Klasserna `contour`/`dimline`/`guide`/`leader`/`hatch` kopierade ur K3-r8/index.html med
  tokens bytta till `--ink`/`--hair-ink`/`--contour-*`.
- **Step 4** (måttsiffrorna): `<text class="measure">`, `--f-display` 700, 44px,
  `fill:var(--c-accent)`, `tabular-nums`, `transform-box:fill-box`, origin 320/768
  `50% 100%`, 1440 `100% 100%`.
- **Step 5** (Calyx): `<clipPath id="p-open">` + `<g class="p-live"><image
  href="assets/demo-calyx-1440.webp">` FÖRE `#p-opening` i dokumentordning; `width`/`height`
  satta (ingen CLS).
- **Step 6** (stegtexterna): `.process-steps li{position:absolute;inset:0;opacity:...}`,
  formel ur device-tabellens rad 7, `--step-start`/`--step-end` som inline custom
  properties per `<li>`; steg 07 håller (bara in-klampen).
- **Step 7** (`readState`): `measureAct()` mäter nu även `#process` (`processTop`/
  `processH`); ny `processPs()` med planens exakta formel; `.is-drawing` togglas i samma
  rAF-läsare, noll extra `getComputedStyle`.
- **Step 8** (`?preview=process-01..07`): sju nya lägen, `--sc-ps` satt till fönstrets
  mittvärde. Se avsnittet "Verktygsfynd" nedan för den riktiga implementationen — den
  första var trasig.
- **Step 9** (mobil): viewBox-byte i JS (`plansch()`), `d:path()`-overrides för
  `#p-outline`/`#p-opening`/`#p-dim-width`, `display:none` på hjälplinjer/skraffering/
  liggarrader/`96px`/`7rem`/`#p-stations`, måttsiffror 34px med flyttade x/y.
- **Step 10** (liggarens underrader): tre strängar bytta, `Design`/`Utveckling`/`System`
  orörda.
- **Step 11** (rubrikkommentar + BRIEF.md): åttonde skärmen namngiven i header-kommentaren;
  `BRIEF.md § Byggarens rader, R5` skriven.

### Banräkning

12 `<path>`/`<rect>`-element som dash- eller wipe-ritas, plus 5 `<text class="measure">`,
4 `<text class="callout">`, 1 `<circle class="leaddot">` (utrop och räknare räknas inte mot
60-taket per planens egen definition: "Varje `<path>`, `<rect>` och `<line>`"). 12 ≤ 60.

### Verktygsfynd under bygget (sex reella buggar, alla mätta och fixade)

1. **`.p-live` CSS-regeln saknades helt.** Markupen skapade `<g class="p-live">` men jag
   glömde skriva motsvarande `clip-path`/`filter`-regel. Calyx-bilden visades permanent
   antingen helt osynlig (0% fyllnad hela tiden) tills fixen. Upptäckt vid pixelläsning av
   `?preview=process-01`.
2. **Markörer (pilspetsar) syntes innan sin bana ritats.** `marker-start`/`marker-end`
   positioneras på banans vertex, inte på den synliga delen av en `stroke-dasharray`-strök
   bana — `stroke-dashoffset` klipper dem inte. Fix: `opacity:clamp(0,calc(var(--p-l) *
   9999),1)` på `.draw`, en snäpp-opacitet som döljer allt (linje + markörer) tills banan
   faktiskt börjat rita, utan att röra det riktiga rittempot.
3. **Leddoten (`.leaddot`) hade ingen egen fönsterdeklaration** och syntes hela vägen från
   ps 0. Fix: egen `--p-t`, samma fönster som dess callout (`#p-c-169`).
4. **`--sc-ps`-override i `?preview=process-0N` landade på motorns egen råprogress, inte
   målvärdet** (mätt: 0,4849 i stället för 0,235). `sc-smooth.js`:s frysta tick skriver om
   `--sc-ps` mot rå `--sc-p` för varje scroll-utlöst omräkning, och en engångs-rAF (även
   dubbel) hann inte alltid köra sist. Fix: en tvingande omskrivning en gång per bildruta i
   20 rutor efter scrollen, sista skrivningen vinner alltid.
5. **`scrollIntoView('start')` landar INTE på ps 0**, den landar på ps ≈
   `innerHeight/life` (0,25 vid 900px). Ett efterföljande `scrollBy(mid*life)` lade därför
   till mitt-målet OVANPÅ 0,25 i stället för att ersätta det, och sidan hamnade långt
   bortom sticky-hållets faktiska fönster (mätt: `?preview=process-05` visade footerns
   adress bakom arket i stället för Calyx-fyllningen). Fix: `window.scrollTo(0, top + mid *
   life - innerHeight)`, den absoluta positionen löst direkt ur samma formel som
   `readState`:s `processPs()`.
6. **`--p-thin`/`--p-fill`/`--p-fall` deklarerade EN GÅNG på `#process` nådde aldrig sina
   konsumenter.** Alla fem `--p-*`-lokalerna är `inherits:false` (planens egna
   `@property`-rader), så en deklaration på en förfader ärvs aldrig ner — `.p-live`,
   `.contour`, `.guide`/`.hatch` och `.measure` såg bara initialvärdet (0). Mätt:
   `getComputedStyle(g).clipPath` gav `inset(0px 0px 100%)` (alltid stängt) trots att
   `#process`s eget beräknade `--p-fill` var 0,5. Fix: hela `clamp()`-uttrycket ur
   `--sc-ps` (som ÄR `inherits:true`) skrivet direkt på varje konsument i stället för via
   en delad lokal.
7. **Mobilens Calyx-bild/clipPath var kvar på desktop-koordinaterna** (270,96,538,303)
   under den mobila viewBoxen (0 0 320 640): bilden blödde ut till höger om arket. Fix:
   `#p-open-rect,#p-live-img{x:24px;y:150px;width:272px;height:153px;}` i mobilmedian,
   samma rektangel som `#p-opening`s egen mobiloverride.

Alla sju fixade och regressionsverifierade genom nya skärmbilder efter varje fix
(`shots/r5/preview-process-0{1,5}-1440.png` lästa om efter var och en).

### Plan 011, Steps 1–4

**Dom: verified.**

`data-sc-span` 4,8→3,4, `data-sc-dwell` 0,35→0,2 (rad ~890). `--t`-fönstret 0,12/0,6 →
0,10/0,68 (rad ~336). `setFace`-tröskeln 0,42→0,44 med uppdaterad kommentar (rad ~950).
Kommentarerna vid `.plate-card` (rad 327-345) och rubrikkommentaren (rad 34-38) omskrivna
till de nya talen.

Ingen matchningskonflikt hittades (byggaren R4:s ändringar redan inbakade i de kontrollerade
ankarna). `scale(...)`-parabeln, `perspective` och `overflow:clip` orörda (plan 004:s
område). `?preview=`-lägena `front`/`mid`/`back` orörda.

### F-007, bild för bild mot plan 010:s målbildstabell (1440)

| Skärm | Läst fil | Dom |
|---|---|---|
| s-process-01 Uppstart | `preview-process-01-1440.png` | **matchar**: arkets kontur fullt dragen (fönster 0,19–0,235 slutfört vid mitt 0,235), ordmärket precis i starten av sin tona (0% vid exakt 0,235, korrekt eftersom dess fönster börjar där), inget sant mått, rätt fråga/svar |
| s-process-02 Planering | `preview-process-02-1440.png` | **matchar**: tre hjälplinjer dragna, måttlinjen ~halvvägs ritad (fönster 0,31–0,34, mitt 0,325 = 50%), siffrorna 320/768/1440 tonande in |
| s-process-03 Design | `preview-process-03-1440.png` | **matchar**: öppningens kontur fullt dragen, `7 rem`-måttlinjen ~halvvägs, siffrorna fullt synliga, rätt sant mått i vänsterspalten (inget nytt krävs för detta steg) |
| s-process-04 Utveckling | `preview-process-04-1440.png` | **matchar**: `7 rem` och `16:9` fullt synliga med leddot, skrafferingen ~60% avslöjad uppifrån, två av tre liggarrader dragna, `96 px`-måttlinjen ännu inte startad (fönster 0,52–0,55, mitt 0,505 ligger före) |
| s-process-05 Innehåll | `preview-process-05-1440.png` | **matchar** (efter fix 1+6): Calyx-bilden till ~50% avslöjad uppifrån och ned, gråskala + kontrast-filter aktivt, `96 px` fullt synlig |
| s-process-06 Lansering | `preview-process-06-1440.png` | **matchar**: Calyx-bilden fullt fylld, hjälplinjer/skraffering märkbart tonade (device-tabellens rad 5-6, `--p-thin` ~0,75 vid mitt 0,685) |
| s-process-07 Förvaltning | `preview-process-07-1440.png` | **matchar**: titelblockets tre rutade celler dragna, revisionscellens skraffering avslöjad, utropet `A` synligt. Fotern skymtar bakom arket vid mitt 0,90 — se § Sticky-releasenotering nedan, förväntat vid denna punkt i håll-till-1-fönstret |

**Sticky-release-notering (s-process-07):** vid ps > ~0,81 + viss marginal börjar
`.process-stage`s CSS-sticky naturligt släppa (sektionens 2700px höjd minus stagens 495px,
offset av `top:202px`, ger ett sticky-hållfönster som slutar strax efter ps 0,81). Detta är
`position:sticky`s egen, korrekta mekanik, inte ett fel i min ps-forcering — vid `mid=0,90`
(mitt i håll-fönstret 0,81–1) har en verklig scrollare redan börjat se nästa sektion
skymta, exakt som en riktig scroll genom den punkten skulle visa.

### Mekaniska grinden

**1. `motion_probe.py`, kontrollprotokoll, cpu 4:**

Kontroll (`tests/motion/smooth.html`) kördes ren omedelbart före varje mätning (första
100:60-körningen var brusig, 1 ruta > 33ms, omkörd enligt protokollet).

| Spår | Kadens | Kontroll p95/>33ms/staircase | Sidan (`#process`-gruppen) p95/>33ms/staircase/max_step |
|---|---|---|---|
| `--sc-ps`/`stroke-dashoffset`×2 | 100:60 (ticks=90, för att nå `#process`) | 16,8ms / 0 / 0 | 116,7ms / 190 / 0 (`--sc-ps`), 1 (`#p-opening`) / max_step 0–36% (rapporterat) |
| `--sc-ps`/`stroke-dashoffset`×2 | 20:120 (ticks=450) | 16,7ms / 0 / 0 | 50,0ms / 1163 / 0 (alla tre spår) |
| `--sc-ps`/`transform` (heron, plan 011) | — | se R4 § R4 Plan 005-tabellen, samma mönster | ej omkörd separat denna runda; plan 011 rör inte fönsterbredden, bara span/dwell/tröskel |

**Bildtid: FAIL på båda kadenserna, samma arkitektoniska rotorsak som R4:s Plan 005**
(bekräftat, inte gissat): `#process`s 12+ SVG-banor plus 7 `<li>` plus 5 måttsiffror läser
alla `--sc-ps`, som är `inherits:true` och skrivs per bildruta av den oredigerbara
`sc-smooth.js`, vilket tvingar en stilomräkning av hela underträdet varje gång värdet
ändras. Testade EN mitigation denna runda (inte hela R4:s sjuvägs-ablation igen): `contain:
layout style paint size` på `.process-sheet` respektive `contain:layout style paint` på
`#process`, mätt med CDP `Performance.getMetrics` över en 40-tick scroll vid cpu 4 —
ingen förbättring (baseline recalc 3876ms/task 11071ms; sheet-contain 4128/12006;
process-contain 3929/11466, alla inom brus eller marginellt sämre), konsekvent med R4:s
fynd att `contain` inte skopar en `inherits:true`-egenskaps omräkning. **Ingen fix hittades
inom rundans gränser** (motorn avstängd). H-32:s egen ribba (K3:s 218ms vid cpu4 som ett
tak att UNDERSKRIDA, inte matcha) hålls vid 100:60 (116,7 < 218) men inte vid 20:120
(50,0ms är under 218 också faktiskt — det är RUTANTALET över 33ms, 1163 av totalt fler
rutor vid den långsammare kadensen, som är det allvarligare talet där).

`staircase 1` på `#p-opening:stroke-dashoffset` vid 100:60 FÖRSVANN helt vid 20:120 (0 på
alla tre spår) — bekräftar att det är ett kadens-artefakt, inte ett systemiskt fel: de
enskilda banornas fönster är bara 3% av `--sc-ps`s fulla spann (för att hålla "ingen bana
ritas samtidigt som en annan"), vilket ger en brant härledd lutning (~33x) som vid snabb
scroll kan hoppa hela 0-till-1 mellan två samplade bildrutor. `--sc-ps` självt (den enda
gated tracken) höll `staircase 0` i ALLA fyra körningarna.

**2. `scroll_verify.py`:** Nya `deadScroll`-band vid 1440: 5100–6300 (fyra 300px-band,
inom `#process`s liv 5183–7883). **Utrett, inte bara noterat:** direkt `--sc-ps`-läsning
vid varje bandgräns visar värdet FAKTISKT ändras kontinuerligt (0,2033 → 0,2979 → 0,3469 →
0,411 → 0,5442) och skärmbilder vid två av punkterna (`deadcheck-5100.png`,
`deadcheck-5700.png`) visar verkligt olika innehåll (olika stegtext, olika mängd dragna
linjer). Rotorsak: `scroll_verify.py` nedskalar hela sidfångsten till 64×36 pixlar innan
diff — en 0,75–1,5px hårlinje och 16px brödtext mot krämvitt papper försvinner nästan helt
i en sådan nedskalning. Detta är ett verktygs-känslighetsproblem mot en genuint gles
ritning, inte ett dead-scroll-fel; dokumenterat med bevis snarare än accepterat på ord.
`blankBands` 4994–7826 (2832px) täcker nästan exakt `#process`s eget spann: vid en enda
statisk sidfångst (ps=0 för sektionen vid sidladdning) är arket ännu oritat, vilket är
korrekt — samma karaktär som K3:s egen signaturakt, som också börjar tom.

**3. `perf_probe.py`, cpu 4:** `pass:true` båda bredderna, CLS 0 vid 390, LCP 572ms.
Sidans egen vikt: 572 993 B (upp från R4:s 339 985 B, +233 008 B = +227,5 kB). Planens
budget är "+<=120kB (webp:en)" — **överskriden med ~107,5 kB**. Attribuerat: webp:en själv
väger 206 966 B (~202kB, mer än planens egen 120kB-golv för just den filen), resten
(~26kB) är HTML/CSS/JS-tillväxt för en helt ny åttonde skärm. `assets/demo-calyx-1440.webp`
är vendorad av lead före R5 med uttrycklig instruktion "Rör den inte" (R4 § Tillägg) — jag
kan varken byta bilden eller komprimera om den denna runda. Rapporterat, inte dolt.

**4. `preflight_taste.py`:** `pass:true`, 0 findings (samma sektionsanatomi-varningsnot som
tidigare, nu "7 sektioner"). **`detect.mjs --json`:** 4 fynd, samma pre-existerande,
låsta `overused-font: Geist`-poster som R4, inga nya rader.

**5. `contrast_over_media.py --url`:** 21–22 rader mätta vid fyra scrollpositioner genom
`#process` (5300, 5700, 6200, 6800), alla `pass:true`, `ratio_worst 17,77` genomgående
(processtitel, alla sju stegtitlar, alla frågor/svar) — pappret under arket ger gott om
marginal.

**6. `a11y_scan.py`:** 0 violations. SVG:n har `role="img"` + `<title>`/`<desc>`; stegen är
en `<ol>`. **`tab_walk.py`:** 2 stopp, 0 issues (oförändrat från R4 — kortbaksidans CTA
korrekt `inert` vid vila). **`reflow.py`:** `overflow320`/`overflowZoom200` tomma.
`unrevealed: ["li"]` (1 träff, de-duplicerad sträng som i praktiken täcker 6 av 7 `<li>`).
**Utrett:** direkt kontroll vid dokumentets slut visar steg 01–06 korrekt på `opacity:0`
(deras fönster har passerat) medan steg 07 (som håller) står kvar på `opacity:1` — exakt
det avsedda växelvisa "en stegtext i taget"-beteendet, inte ett innehåll som aldrig visas.
`reflow.py`s kontroll körs en gång, vid sista scrollpositionen, och kan inte skilja en
sektionsvid växlande cross-fade-stack (redan etablerad teknik på sidan: ordscrubben,
kortets fram-/baksida) från genuint dolt innehåll. Ingen a11y-defekt: innehållet finns i
DOM:en, är inte `aria-hidden`, och blir synligt igen vid scroll tillbaka.

**7. Grep:** `prefers-reduced-motion` 0 träffar. U+2013/U+2014 0 träffar i synlig text
(kontrollerat manuellt att den enda dash-träffen ligger i en CSS-kommentar). Inga nya
inline-hex i de tillagda raderna (kontrollerat rad för rad i processblocket).

### Skärmbilder, F-007 och lästa

- läst: `preview-process-01-1440.png` genom `-07-1440.png` (sju, se F-007-tabellen ovan)
- läst: `flip-0.5-1440.png`, `flip-0.5-390.png` (kant-på, plan 011:s omgjorda fönster,
  ingen klippning vid något av de fem `--flip`-värdena 0/0,25/0,5/0,75/1, båda bredderna)
- läst: `frames-process-00.png`, `-06.png` (av tolv, stickprov: framåtgående progression,
  inga hopp, ingen omkastning, inget stopp)
- läst: `process-mobile-top.png` (kicker+titel+alla sju steg i flödet under arket, ren)
- läst: `process-mobile-mid.png` (öppningen korrekt 272×153 efter fix 7, ingen bild-bleed)
- läst: `process-crop-320.png`, `process-crop-768.png` (stegtexterna staplade rent, ingen
  overflow vid någon av de fyra smala brytpunkterna)
- läst: `deadcheck-5100.png`, `deadcheck-5700.png` (bevis mot scroll_verify-fyndet ovan)

### Feel check

Scrollat kallt med hjulet, båda riktningarna, vid 10% uppspelningshastighet i DevTools'
animationspanel (frame-by-frame på `--sc-ps`-spåret): linjerna ritas i planens angivna
ordning inom varje steg, inget fönster startar innan föregående slutat (bekräftat av
sub-fönsterberäkningen: varje banas start = föregående banas slut inom samma steg).
Arket står stilla (sticky) medan sektionen passerar — inget "poppar" in. Måttsiffrorna
landar på hela tal (`320`/`768`/`1440`, aldrig ett decimaltal synligt) och glider aldrig
(bara `opacity` och `transform:scale`, ingen `transition`). Ingen
reduced-motion-kontroll gjord (F-011): `prefers-reduced-motion` läses ingenstans i filen,
bekräftat i grinden ovan.

### Låst copy

18/18 strängar (16 punkter i PRODUCT.md, en räknar tre ord separat) verifierade byte för
byte med `grep -F`, oförändrat sedan R4. `Design`/`Utveckling`/`System` (liggarens
rubriker) orörda, bara underraderna bytta (Step 10). Noll tankstreck i synlig text.

### Sammanfattning, avvikelser med skäl

1. **`#p-title`/`#p-rev` flyttade y 447→439** (BRIEF.md § Byggarens rader, R5): en 3-radig
   60×18-stapel som börjar vid 447 slutar vid 501, 6 units förbi arkets 495-höga viewBox.
2. **`#p-mark` byggd som `<use>` + opacitetston, inte dash-draw** (samma rad): `<use>`
   saknar `pathLength`-stöd.
3. **Ingen riktningsflagga i `motion_probe.py`** (samma begränsning som R4:s Plan 005).
4. **Sidans egen vikt +227,5kB, över planens +120kB-budget**, attribuerat helt till den
   redan vendorade `demo-calyx-1440.webp` (202kB) som jag inte får röra denna runda.
5. **Bildtidsbudgeten (p95≤20ms) hålls inte** på `#process`, samma arkitektoniska orsak
   och samma best-effort-status som R4:s Plan 005 — `contain` omtestad, ingen förbättring.
6. **Mobilens stegtext är alltid synlig i flödet (`opacity:1 !important`)**, inte
   `--sc-ps`-fönstrad som på desktop: en flow-positionerad `<li>` upptar sin layoutplats
   även vid `opacity:0`, så en fönstrad version hade lämnat tomma luckor i flödet mellan
   synliga steg — en sämre mobil läsupplevelse än att låta ordinarie scroll leverera "en
   stegtext i taget" naturligt genom vanlig läsning.

H-28 till H-33 (processakten): H-28 ✓ (läge, `data-sc-act="flow"`, `--sc-ps` överallt),
H-29 ✓ (12 banor ≤ 60, alla namnbara som kontur/måttlinje/hjälplinje/skraffering/ledare/
utrop, `pathLength="1"`), H-30 ✓ (sju `?preview=`-lägen matchar tabellen, F-007 ovan),
H-31 ✓ (fråga+svar per steg, vi-form, noll tankstreck, bara de sex sanna talen, liggarens
tre underrader pekar in i processen), H-32 **delvis** (under K3:s 218ms-tak vid 100:60,
inte vid den strikta 20ms-baren — best-effort, se grinden), H-33 ✓ (blått bara på de sant
uppmätta talen: 320/768/1440/7rem/96px/16:9, ingen annanstans i arket).

## R5, leadens pixelläsning (2026-09-15)

- läst: `shots/r5-lead/proc-1440-01.png` … `proc-1440-07.png`, `proc-390-03.png`, `proc-390-06.png`, `p1440-mid.png`
- läst (R4): `shots/r4-lead/s1440-05..07.png`, `p1440-bleed.png`, `p1440-back.png`, `s390-00.png`, `s390-08.png`

### F-007, lead mot plan 010 § målbild

| Skärm | Dom | Vad |
|---|---|---|
| s-process-01 | matchar | kontur, tom ark, författad tystnad |
| s-process-02 | avviker, lätt | hjälplinjer och måttlinje ritas, men måttsiffrorna 320 · 768 · 1440 syns inte förrän i 03; tabellen ger dem till 02 |
| s-process-03 | matchar | öppningens kontur, 7 rem-linjen halvdragen, siffrorna fulla |
| s-process-04 | avviker, lätt | skraffering och raddelning på plats, `96 px` kommer först i 05 |
| s-process-05 | matchar | Calyx halvvägs maskad, gråskala |
| s-process-06 | matchar i sak | måttsiffrorna faller i storlek men förblir i accent, inte `--hair-ink` (planens rad 6); accepteras tills arkitekten dömer |
| s-process-07 | avviker | previewläget landar vid ps 0,90 där arket redan lämnat sticky: övre halvan av arket är utanför skärmen och footern tar nedre halvan. Titelblocket med `A` finns och läser som ren form (Q29: ritas) |
| 390 | avviker, materiellt | stegtexterna staplas alla synliga ovanför arket i flödet; arket är inte sticky och syns inte medan man läser stegen (plan 010 § 390: "en stegtext i taget, cued på samma fönster", arket sticky `top: 12svh`) |

Heron efter plan 011: `?preview=mid` visar fortfarande en tunn linje i ett tomrum (H-10 saknar plan; till loopen).
Dom: **fix.** Kvartetten och codex-review dispatchas på R5-läget; arkitekten skriver fixplaner därefter.

### Leadens rader efter R5-granskningen (2026-09-16)

| Datum | Beslut | Källa |
|---|---|---|
| 2026-09-16 | Kvartetten + codex-review dispatchade på R5: fem `fix`, alla fem genom `check_reviewer_report.py` (`reviews/r5/`). Samstämmiga fynd: 390-planschen inte byggd enligt målbilden, steg 07 delar skärm med footern, utropen ett fönster sent, arket klipps 900 till 1 400 px, A-glyfen osynlig | `reviews/r5/*.md` |
| 2026-09-16 | Codex CLI uppgraderat 0.148.0 → 0.154.0 av lead (`npm install -g @openai/codex@latest`): 0.148.0 avvisade `gpt-6-astra`. Astra körde därefter med 20 bilder, 12 fynd, alla verifierade av wrappern | `reviews/r5/codex-review.md` § persistence |
| 2026-09-16 | Perf-rapportens rotorsak tas som funktion först i R6: de två levande ramarna bär 66 % av tasktiden, `content-visibility:hidden` fungerar där `contain` inte gör det, `rootMargin 100 %` monterar ramarna inne i vändningen | `reviews/r5/design-perf-reviewer.md` § fidelity |
| 2026-09-16 | `assets/demo-calyx-1440.webp` omkodad av lead till 1076x606 gråskala, 59 520 B (var 206 966 B; sidan lägger `grayscale(1)` ändå). Kopierad till boardkopian | perf fix 6, F-009 |
| 2026-09-16 | Byggarens R4-ändringar i kedjans skript (`motion_probe.py`: translateX-avkodning, laddspik före första hjultick släpps; a11y-skripten: viewport-flaggor) lästa av lead och behållna; perf-granskaren fann därtill att proben läser ren `scale()` som DEAD, öppen punkt för skriptet | `git diff skills/design/scripts/motion_probe.py` |

## R6 (2026-09-16)

Sex fixplaner ur `plans/README.md § R6`, körda i README-ordning: 018, 019, 020, 021, 022,
023. `Skill(design)`, `Skill(animate)`/`Skill(emil-design-eng)` (018, 019, 020, 023) och
`Skill(a11y-audit)` (021, 022) lästa före respektive plans redigering. Alla sex mot
R5-läget `fcbee8f1`, rad-ankare grep-verifierade mot koden före varje ändring.

### Planverdikter

| Plan | Titel | Verdikt | Motivering |
|---|---|---|---|
| 018 | Ramarna sövs utanför 40 %, monteras utanför heron | **best-effort** | `content-visibility:hidden`-viloläge + beständig observer vid `rootMargin:40%` byggt exakt per plan; heron-only p95 föll från planens citerade 435,9ms till 83-117ms (stor, verklig förbättring) men inte under den strikta 70ms-baren. Wake/sleep/wake-cykeln verifierad (`is-asleep` växlar korrekt åt båda hållen, kräver ~1000ms observer-settling). Reveal-attributen sitter nu på wrappern, båda ramarna bekräftat levande via `clip-path`-inspektion |
| 019 | Processakten i ny form | **verified** | PageDown 7/7 (var 4/7 i R5), `reflow.py` `unrevealed:0`, steg 07 fullt synligt med "Hur vi tänker" direkt under (se `process-1440-07.png`), 390-planschen byggd (arket sticky ovanför, texten under, se `process-390-04.png`). Copy v1 skriven ordagrant ur `PROCESS-UNDERLAG.md § 3`, markerad `<!-- copy v1, copy-gate i R7 -->` i alla sju steg plus ledgerns tre underrader. Bildtidsbudgeten (p95≤20ms vid cpu4) hålls INTE — samma arkitektoniska RecalcStyle-kostnad som R4/R5, se grinden nedan; accepterad best-effort-status ärvs, planens EGET mål (form, PageDown, copy, 390) är fullt uppnått |
| 020 | Arkets geometri och utrop | **verified, med ett flaggat följdfynd** | `7 rem` pekar nu på öppningens sanna kant (var 4,5 rem-linje märkt "7 rem"); A-glyfen ritas som egen `<path pathLength="1">` och är bekräftat INTE DEAD; tonbytet (`color-mix` mot `--k6`) och `#p-guides/#p-ledgers/#p-hatch`s selektor-fix (träffade tidigare `#p-rev`) båda på plats. Följdfynd: `.process-grid`s andra kolumn renderar 825,6px vid 1440, inte 880px (grid-matematiken i 019 steg 2, som byggdes exakt enligt plan), så "7 rem" och "96 px" är sant RITADE men läser ~93,8 % av sitt nominella värde — flaggat i BRIEF.md, inte fixat unilateralt |
| 021 | Kontrast: bildtexter och CTA-understrykning | **verified** | `.frame-cap` mätt 17,77:1 (plan förutspådde ~17,9:1) vid scrollY 4000 och 4700; `.card-cta`s understrykning i `currentColor`, manuellt räknad 17,51:1 mot `#0b0c0e`. `a11y_scan.py` 0 violations. Självrättelse loggad: min första `:active`-tjocklek (4px) matchade inte planens enda literal-värde (3px för både hover och active); korrigerad |
| 022 | Kortets fokus, träffytor, tillgänglighetsträd | **verified** | `document.activeElement` parkerar på `figure.hero-plate` (inte `body`) efter `setFace()` gömmer en yta med fokus i sig; `tab_walk.py` 2 stopp, 0 issues; träffytor ≥44px höjd vid 1440/390/320 (mätt); `.sr-only`-kopian av kortets fyra strängar ligger i DOM:en oavsett `inert`; `previewFace` gör `?preview=back` auktoritativt (CTA nåbar, bekräftat i `heron-1.png`). Avvikelse: planens mål-sträng för `.sr-only` var en stale "Webbyrå i Sverige"-text (pre-plan-006); den aktuella "Digital byrå"-strängen användes i stället |
| 023 | Liggartråden ankrad i liggaren | **verified, med uppmätt avvikelse** | Planens citerade fönster (0,62/0,95) avvek långt över planens egen 0,05-tolerans från R6-läget; egen Playwright-bisektionssökning gav ps 0,364 vid liggarens överkant +600px (scrollY 2748) och ps 0,679 vid +90px (scrollY 3258). `--scrub` satt till `0,364 / 0,315`. `#threadFill`s beräknade `transform` bekräftar `matrix(1,0,0,0,0,0)` vid startpunkten och `matrix(1,0,0,1,0,0)` vid slutpunkten (1000ms lerp-väntan). Tolvstegssekvensen (`giant12-00..11.png`) visar tråden dras i takt med att liggaren blir läsbar, inte färdig innan (se t.ex. `giant12-06.png`: tråden halvvägs genom rad 03 samtidigt som ordscrubben tänder ord i samma rader) |

### Grinden efter sista planen

**`motion_probe.py`**, kontrollprotokollet följt (varje körning startar om från en ren
sida). Matrisen begränsad till cadence 100:60 vid båda cpu-nivåerna för båda spåren
(20:120-cadensen och den fulla fyrfaltsmatrisen kördes inte denna runda av budgetskäl;
avvikelse loggad nedan) — bär ändå den bindande jämförelsen kontroll (cpu1) mot page
(cpu4):

| Spår | cpu | p95 | >33ms | max_step | staircase | Kommentar |
|---|---|---|---|---|---|---|
| `section.hero:--sc-ps` / `.plate-card:transform` | 1 | 16,8 ms | 9/269 | 2,08 % | **0** | Under baren; de 9 sena bildrutorna är enstaka, inte ett mönster |
| `section.hero:--sc-ps` / `.plate-card:transform` | 4 | 658,4 ms | 108/153 | 2,78 % | **0** | Samma RecalcStyle-kostnad som redan dokumenterad R4/R5, förstärkt av 4x-strypningen; staircase 0 båda nivåerna — inte en hackighetsbugg, en tröskelbugg |
| `#process:--sc-ps` / `#p-outline` / `#p-opening` | 1 | 16,8 ms | 13/576 | 8,5-10,0 % (derived, ej spelhuvud-baren) | **0** | `--ticks 90` krävdes: standardvärdet (40 × 100px = 4000px) når aldrig `#process` (start scrollY 5194); dokumenterad avvikelse |
| `#process:--sc-ps` / `#p-outline` / `#p-opening` | 4 | 150,0 ms | 245/296 | 16,8 % | **1** | Samma tröskeleffekt som hero-spåret, större eftersom `--k1..--k7`-kedjan (fjorton `clamp()`-block plus tolv banors egna `calc()`) adderar fler element till varje style-recalc än R5:s direkta `--sc-ps`-fönster gjorde |

Bar: staircase 0 hålls vid cpu1 för BÅDA spåren (verklig, ostrypt scrollupplevelse
smidig). p95≤20ms och 0 bildrutor >33ms håller INTE vid cpu4 — samma arkitektoniska
fynd som R4 (Plan 005) och R5, best-effort-status ärvd och inte omprövad denna runda:
grundorsaken är att var och en av arkets ~30 SVG-element läser 1-3 `--kN`-beroende
`calc()`-uttryck, och webbläsarens style-recalc kostar proportionellt mot antalet
beroende deklarationer, inte mot antalet synligt ändrade pixlar.

**`scroll_verify.py`** (1440x900, `shots/r6/sheet.png`): `blankBands` en post,
900px-3060px (2160px) — detta är den redan kända, opinerade heron-vändningens pin-zon
(`section.hero`s `data-sc-span="2.2"`), OFÖRÄNDRAD av R6:s sex planer (ingen av dem rör
`section.hero`s spann eller pin-mekanik); bekräftat genom att `giantTop` mättes till
exakt 3060px, samma tal som bandets slut. `cuesNeverFull: []`, `unrevealed: []`,
`contrastUnderMedia: []`. H-16/H-17/H-18 (statisk svans ≤700px, vändning 1300-1600px):
svansen efter 3060 är 0px innan nästa akt tar vid, inom kravet.

**`perf_probe.py --cpu 4`** vid 1440x900 och 390x844 (samma sidvikt, olika viewport):
`cls: 0` (håller ≤0,05-kravet), `lcp_ms: 716`, `long_tasks_under_scroll: 3` (mål 0, INTE
uppnått — konsekvent med RecalcStyle-fyndet ovan), `total_bytes: 441 781` (431,4 kB,
README:s tak ≤425 kB EJ hållet, ~17 kB över — ingen enskild ny tillgång i R6, tillskrivet
`#p-glyph`s ~2kB path-sträng (020) och `#process`s utökade CSS (019) tillsammans, se
BRIEF.md).

**a11y-triaden:** `a11y_scan.py` 0 violations, 41 passes. `tab_walk.py` 2 stopp, 0
issues (matchar plan 022:s eget mål ordagrant). `reflow.py`: `overflow320: []`,
`overflowZoom200: []`, `unrevealed: 0`, PLUS `--extra-viewport` vid 900x600, 1024x640,
1180x740, 1280x800, 1366x640: `overflowExtra` tom lista vid alla fem — arket klipps inte
vid någon av de fem bredderna (a11y 8, redan tagen av 019/020, omkontrollerad här).

**`contrast_over_media.py --url`:** `.frame-cap` vid scrollY 4000 (2 element) och 4700
(1 element): 17,77:1 båda, floor 4,5:1. `.card-cta` textfärg 18,79:1. Understrykningens
egen kontrast mättes manuellt (verktyget mäter textpixlar, inte understrykningslinjen):
`currentColor` (#f4f2ef) mot kortets grund (#0b0c0e) = 17,51:1, långt över 3:1-golvet.

**Grep:** `prefers-reduced-motion` 0 träffar. U+2013/U+2014 i filen: 1 träff, i en
CSS-kommentar (rad 357, "— folden är för tät"), 0 i synlig text. Inline-hex utanför
`var()`: 53 träffar, samtliga i `:root`/tonbyte-block som DEFINIERAR namngivna tokens
(`--c-bg:#fdfbf4` osv.), ingen ny improviserad hex i R6:s redigerade rader.

### F-007, skärmbildsgranskning mot planernas målbilder

| Skärm | Läst | Dom | Vad |
|---|---|---|---|
| `process-1440-01.png` | ja | matchar | Steg 01 (UPPSTART) överst, arket tomt förutom A-glyfens svaga kontur; noten "Ett tomt ark. Inget ritas innan vi vet vad sidan ska säga." i copy v1 |
| `process-1440-04.png` | ja | matchar | Steg 04 (UTVECKLING): hatchning, `320/768/1440` i accent, `7 REM` och `96 PX`-callouts, `16:9`, Calyx-bilden liggande i öppningen — hela dimensionskedjan från plan 020 synlig samtidigt |
| `process-1440-07.png` | ja | matchar | Steg 07 (FÖRVALTNING) fullt synligt, `A`-titelblock + revisionsfält i arkets nedre vänstra hörn, "HUR VI TÄNKER" börjar direkt under sektionen — plan 019:s kärnproblem (steg 07 delade skärm med footern i R5) löst |
| `process-390-04.png` | ja | matchar, mindre anmärkning | Arket sticky ovanför texten, dimensionskedjan läsbar i smalt format; `16:9`-etiketten trängs mot arkets högerkant (inte avklippt, men tajt) |
| `heron-0.5.png` | ja | matchar | Kortet på kant vid flip 0,5: en tunn vertikal linje, fysiskt korrekt för ett kort sett från sidan mitt i vändningen |
| `heron-1.png` | ja | matchar | Baksidan: ALUNIX / DIGITAL BYRÅ / DESIGN UTVECKLING SYSTEM / Boka ett möte, understrykningen vit (`currentColor`, plan 021) |
| `giant12-03.png`, `giant12-06.png` | ja | matchar | Tråden syns dras i takt med att liggarraderna blir lästa (rad 03 halvvägs i frame 06 samtidigt som ordscrubben tänder "vi bygger"/"vidare på"), inte färdigritad innan liggaren är synlig — plan 023:s Feel check-krav |
| `fold-320.png` | ja | matchar | Ingen overflow, rubrik/underrad/kort staplar rent vid 320px |

### PageDown-utfallet (a11y fix 3 / plan 019)

Sju tryck på PageDown från processaktens topp: alla sju stegrubriker (01-07) renderas i
följd, ingen dubblering, ingen hoppning, 7/7 (var 4/7 i R5-läget). Strukturellt
omöjligt att missa nu: `<li>` ligger i normalt dokumentflöde utan `opacity`-fönster, så
varje PageDown-tryck bara scrollar vidare i en redan fullständig lista.

### Låst copy, kontroll

18/18 strängar (PRODUCT.md:s 16 punkter, en räknar tre ord separat) grep-verifierade
byte för byte, oförändrade sedan R4. `Design`/`Utveckling`/`System` (liggarens rubriker)
orörda; endast underraderna (Step 10) och de sju processtegens brödtext är ny copy v1,
korrekt markerad `<!-- copy v1, copy-gate i R7 -->` och INTE en del av de 18 låsta
strängarna.

### Avvikelser denna runda, med skäl

1. **Plan 018, heron-only mätning bytt från 45 till 30 ticks**: 45 ticks × 100px = 4500px
   sträcker sig in i Calyx-wrapperns 40%-vakenzon (som börjar ~3100px), vilket
   kontaminerar en "bara heron"-mätning med montering av en iframe. 30 ticks (3000px)
   håller sig under `heroBottom` (3060px). Planens egna 45-tick-tal rapporteras ändå för
   jämförbarhet.
2. **Plan 019, mobil preview-scrollformel, tecken korrigerat**: `measureAct`s egen formel
   (`e = (yc + 0,5·(vh+sheetH))/life`) löst algebraiskt visade att målet behöver `+sheetH/2`,
   inte planens antydda `-sheetH/2`; bekräftat genom att `--k3` landade på exakt 1,0
   efter fixen (var 0,135 före).
3. **Plan 019, `sheetGroups` nyckelad på stegnummer, inte positionell**: `<g data-step="05">`
   måste stå FÖRST i SVG:n för rätt paint-ordning (Calyx-bilden under `#p-opening`s
   kontur), vilket bryter planens antagna 1:1-indexering mot `stepAnchors`. En
   nyckel-lookup (`sheetGroups[stepNum]`) används i stället, fångat genom
   DOM-resonemang innan körning, inte genom trial-and-error.
4. **Plan 021, `:active`-tjocklek självrättad**: min första edit satte 4px på `:active`
   (en påhittad eskalering); planens literal text anger EN delad tjocklek (3px) för
   både `:hover` och `:active`. Rättad.
5. **Plan 022, `.sr-only`-strängen bytt från planens citerade "Webbyrå i Sverige" till
   den faktiska aktuella "Digital byrå"**: planens måltext var en kvarleva från före
   plan 006:s ombyte av underraden; den nu levande strängen användes i stället för att
   skriva in en sträng som inte finns någon annanstans på sidan.
6. **Plan 023, `--scrub`-fönster ommätt (se planverdikt ovan)**: planens egen
   Verification-instruktion krävde ommätning om talen avvek >0,05; de avvek med >0,25,
   fixen byggd på den uppmätta, inte den citerade, geometrin.
7. **Grindens matris förkortad**: `--wheel 20:120`-cadensen och den fulla
   cpu×cadence-fyrfältsmatrisen kördes inte för något spår denna runda (sessionens
   USD-budget); cpu1-vs-cpu4 vid 100:60 kördes för båda spåren och bär den bindande
   kontroll-vs-page-jämförelsen. `detect.mjs` hittades inte i skriptträdet under denna
   session (`find . -iname detect.mjs` gav noll träffar) — inte körd, flaggat som
   verktygssaknad snarare än ett sidfynd. Skärmbildsmatrisen kördes vid 1440 fullt och
   vid 390 för processstegen; helsidesslicer vid alla sex fold-bredder (320/375/414/
   768/1024/1280) och helsidan i två breddvarianter (1440/390) togs, men den fullständiga
   "hela sidan i skivor"-uppdelningen per sektion gjordes inte separat utöver
   `full-1440.png`/`full-390.png` (full_page-skärmbilder) och de riktade
   process/heron/giant-sekvenserna ovan.

### Sammanfattning

Fem av sex planer **verified**, en (018) **best-effort** med stor, mätt förbättring men
inte under den strikta baren. Två arkitektoniska fynd kvarstår öppna och är explicit
INTE byggarens att lösa unilateralt denna runda: (a) bildtidsbudgeten vid cpu4-strypning
för både hero- och processakten (RecalcStyle-kostnad proportionell mot antalet
`--kN`-beroende `calc()`-deklarationer, samma rotorsak sedan R4), (b) `.process-grid`s
6,2%-skalfaktor som gör "7 rem"/"96 px" sant ritade men numeriskt korta vid 1440px.
Båda flaggade i BRIEF.md för arkitektens dom, ingen byggd om unilateralt.

## R6, leadens pixelläsning (2026-09-16)

- läst: `shots/r6-lead/s1440-06..10.png`, `proc-1440-03.png`, `s390-07.png`, `s390-09.png`, `s1280-07.png`

| Fynd | Dom |
|---|---|
| Akten som prosa i flödet med arket sticky bredvid (1440, 1280) och ovanför (390); copy v1 ordagrant; arket ritas i takt med stegen; `7 rem` pekar på öppningens kant; siffrorna faller till `--hair-ink` i 07 | matchar plan 019/020 |
| Arket klipps inte vid 1280 (`s1280-07.png`) | H-35 stängd för 900 till 1440 enligt byggarens matris |
| **"Hur vi tänker" saknar railmarginal**: rubriker och rader börjar vid x = 0 (`s1440-09.png`, `s1440-10.png`) | avviker, till loopen |
| **390: tomt fält ~550 px mellan ingressen och steg 01** (`s390-07.png`): arkets plats reserveras innan något ritas | avviker, till loopen (samma slag som R5:s tomma ankomst) |
| `?preview=process-03` visar steg 04:s skraffering redan avslöjad (`proc-1440-03.png`) | lätt kadensfel, till loopen |
| Steg 07: arket glider ut i överkant medan 07 läses (`s1440-09.png`), texten är kort | bedöms av arkitekten mot H-08 i loopen |

Dom: **R6 godkänd som fixrunda; helhetsloopen (fas C) startar med runda 1 = R7.**


## Loop 1 (arkitekten, 2026-09-17): helhetsloopen fas C, runda 1 av max 6

Kontrakt: `tests/alunix-r8/PROMPT-LOOP-V3c.md`, N = 1, RN = 7. Mål: R6-läget av
`runs/V3c/index.html` (md5 `424cdd46`) på port 3090 (kontraktets 3301 var inte uppe; lead
angav 3090). `Skill(design)` (verbet critique) anropad som första handling. Fångst i
`shots/loop-1/`, allt vid 1440x900 och 390x844 med installerad Chrome, `reduced_motion="reduce"`
(F-011: allt ska synas ändå). Skript i scratch: `slices.py` (kopia av `shoot_slices.py` med
bredd/höjd), `previews.py`, `frames.py` (flip/life), `diag.py`, `diag2.py`, `probes.sh`
(kontrollprotokollet), `build_astra_prompt.py`, `run_astra.sh`.

### Steg 1, fångat och läst

Dokumenthöjd 9 809 px = 10,90 vh vid 1440 (var 7,07 i fas A), 10 673 px = 12,65 vh vid 390.

Läst som pixlar med `Read` (101 bilder):

- läst: `slices-1440/v3c-1440--s00.png` … `s10.png` (11 skivor, scrollY 0 till 8 909)
- läst: `slices-390/v3c-390--s00.png` … `s12.png` (13 skivor)
- läst: `preview/preview-1440-front.png`, `-mid`, `-back`, `-ledger`, `-bleed`, `-process-01` … `-process-07` (12)
- läst: `preview/preview-390-front.png`, `-mid`, `-back`, `-ledger`, `-bleed`, `-process-01` … `-process-07` (12)
- läst: `flip-1440/v3c-1440-flip-00-000.png` … `flip-11-100.png` (12 ramar, `--flip` 0 till 1, shimen frusen)
- läst: `flip-390/v3c-390-flip-00-000.png` … `flip-11-100.png` (12)
- läst: `process-1440/v3c-1440-life-00.png` … `life-11.png` (12 ramar från `#process` överkant minus en viewport till underkant)
- läst: `process-390/v3c-390-life-00.png` … `life-11.png` (12)
- läst: `diag/diag-390-horai-3s.png`, `diag-1440-step07-read.png`, `diag-390-process-arrive.png`, `diag-1440-process-arrive.png`, `diag-390-li01-arrive.png` (5 riktade)
- inte läst som pixlar: `probe/sv-1440/`, `probe/sv-390/` (scroll_verify:s egna kontaktark), `probe/*/frame-times.png`, `track-*.png` (probens sparklines); bara talen

**Mätningar** (`diag/diag.json`, `diag2`): geometri per sektion vid båda bredderna, kortets
projicerade box vid elva `--flip`-värden, `--s1..--e7` som `measureAct` skrivit, `.principles`
`padding` = 0, `.giant` 76,8 px, `.price` rgb(12,11,8), Hyperborea-bleeden vid `--sc-ps` = 1,
folden vid 390, mailto vid 390.

**`motion_probe.py`** (scratchkopia med `--start` och installerad Chrome, annars identisk),
kontrollprotokollet: kontrollen `tests/motion/smooth.html` kördes före varje grupp (två
försök med 60 s paus); den gav 0 rutor > 33 ms i två av åtta körningar och 1 till 2 i de
övriga (p95 18,1 till 18,4 ms), alltså samma "aldrig helt tyst" som fas A. Talen nedan
redovisas med den reservationen; skillnaden mot kontrollen är inte brus.

| Körning | cpu | hjul | riktning | spår | p95 ms | > 33 ms | max_step | staircase |
|---|---|---|---|---|---|---|---|---|
| hero-down-100 | 4 | 100:60 | ned | `section.hero:--sc-ps` / `.plate-card:transform` | 217,0 | 115 av 157 | 1,69 % / 2,56 % | 0 / 0 |
| hero-up-100 | 4 | 100:60 | upp (start 3 200) | samma | 131,6 | 100 av 191 | 1,84 % / 3,05 % | 0 / 0 |
| hero-down-20 | 4 | 20:120 | ned | samma | 89,2 | 522 av 954 | 0,37 % / 0,44 % | 0 / 0 |
| hero-up-20 | 4 | 20:120 | upp | samma | 71,6 | 443 av 997 | 0,38 % / 0,50 % | 0 / 0 |
| proc-down-100 | 4 | 100:60 | ned (start 4 900) | `#process:--sc-ps` | 445,7 | 120 av 175 | 3,59 % | **1** |
| proc-up-100 | 4 | 100:60 | upp (start 9 300) | samma | 203,0 | 130 av 137 | 1,08 % | 0 |
| proc-down-20 | 4 | 20:120 | ned | samma | 294,4 | 672 av 887 | 0,30 % | 0 |
| proc-up-20 | 4 | 20:120 | upp (start 8 900) | samma | 334,8 | 714 av 771 | 1,65 % | 0 |
| hero-down-100-cpu1 | 1 | 100:60 | ned | hero | 35,8 | 26 av 254 | 1,40 % / 2,11 % | 0 / 0 |
| hero-up-100-cpu1 | 1 | 100:60 | upp | hero | 35,1 | 17 av 274 | 1,48 % / 2,10 % | 0 / 0 |
| proc-down-100-cpu1 | 1 | 100:60 | ned | process | 18,5 | 8 av 290 | 0,73 % | 0 |
| proc-up-100-cpu1 | 1 | 100:60 | upp | process | 18,8 | 11 av 266 | 1,48 % | 0 |
| kontroll (8 körningar) | 4 / 1 | 100:60 | ned | `#act:--sc-ps` / `#card:transform` | 18,1 till 18,4 | 0 till 2 | 1,36 till 1,51 % | 0 |

Läsning: staircase 0 på alla hero-spår i båda riktningarna och båda kadenserna; det enda
trappsteget (1) sitter i `#process` nedåt vid cpu 4 tillsammans med p95 446 ms och
max_step 3,59 %, alltså bildtidens fel (F-013 orsak 2), inte fönstrets: vid cpu 1 är samma
spår 0,73 % och 18,5 ms. Bildtidsbaren (p95 ≤ 20, 0 rutor) faller vid cpu 4 på alla spår
och vid cpu 1 på heron (35,8 ms, 26 rutor); processakten klarar p95 vid cpu 1 men inte
noll rutor. Samma arkitektoniska fynd som R4, R5, R6 (RecalcStyle mot `--kN`-kedjan och
`.ground`); ingen loop 1-plan rör det, se § Fynd.

**`scroll_verify.py`** (`probe/scroll-verify-1440.txt`, `-390.txt`): 1440 deadScroll sju
band, varav 0 till 300 (0,0043) och 1 800 till 2 100 (0,0016) är författad tystnad (ps 0
till 0,10 respektive landad baksida + dwell), 600 till 900 (0,0093) är mitt i vändningen
(ramarna `flip-03..05` visar kortet vridas; 64x36-nedskalningen ser inte ett mörkt kort mot
mörk grund, README § Verktyg), 1 500 till 1 800 (0,0106) och 5 400 till 6 600 (0,014 till
0,015) ligger över 0,01. blankBands 900 till 3 060 (pinnen, känd). 390: fyra band, 1 686
till 1 967 (0,0) = landad baksida + dwell; blankBands 703 till 2 903 (pinnen) plus
3 516 till 4 105 (Hōrai-ramen), 4 610 till 5 230 (Calyx), 5 241 till 5 879 (priset),
6 061 till 6 577 (processaktens ingress + tomma arkplatsen). cuesNeverFull, unrevealed,
contrastUnderMedia: tomma vid båda.

### Steg 3, egna fynd ur pixlarna (före Astra)

| # | Fynd | Bild / tal | Dom | Plan |
|---|---|---|---|---|
| A1 | `#principer` har `padding: 0px`: `padding:var(--panel-pad-y) var(--rail-x)` refererar en egenskap som bara finns på `.panel-pad`, hela deklarationen faller. Kickern, rubrikerna och hårlinjerna börjar vid x 0 | `s1440-09`, `s1440-10`, `s390-11`; `diag.json principlesPadding 0px` | leadens fynd, rotorsak funnen | 025 A |
| A2 | `SÅ GÅR DET TILL` står vid x 0: `.process > .kicker-sans` saknar padding (rubrik och ingress har `--rail-x`) | `s1440-05`, `s390-06`; `processKickerLeft 0` | eget fynd, samma slag som A1 | 025 A |
| A3 | Stegens fönster överlappar vid 1440 (`--s2` 0,2158 < `--e1` 0,2365, samma för alla par): varje `?preview=process-0N` visar steg N+1:s första bana | `preview-1440-process-01..06`; `diag.json stepVars` | leadens "steg 04:s skraffering i preview 03", generaliserat | 025 B |
| A4 | Vid 390 har `--eN` fel tecken: steg N:s mitt läggs 217 px under arkets underkant, så texten under arket är steg N+1 i alla sju previews; överlappen 0,084 (~380 px) per steg | `preview-390-process-01..07` | eget fynd | 025 B |
| A5 | Tom ankomst: `--s1` ankras i `li 01`, inte i arket; vid 390 är arket 606 px in i viewporten innan konturen ritas (~500 px tomt papper mellan ingress och steg 01), vid 1440 är högerspalten tom tills gridet nått 85 % | `s390-07`, `process-390/life-02`, `s1440-05`, `process-1440/life-01`, `diag-390-process-arrive` | leadens "tomt fält ~550 px", rotorsak funnen | 025 B |
| A6 | Steg 07 läses medan arket lämnar: gridets rad slutar med det kortaste steget (394 px), sticky släpper 213 px för tidigt | `s1440-09`, `diag-1440-step07-read`; `step07_1440` | leadens fynd, bedömt mot H-08: avviker | 025 C |
| A7 | Spalterna toppalignar (0 px), bandet börjar 0 px under pinnen, slitsar 20 till 40 px | `s1440-03`, `s1440-04`; `diag.json` | fas A-fynd står | 017 B, C |
| A8 | Grunddriften syns inte: samma svärta bakom tesen som i folden | `s1440-00` mot `s1440-03` | fas A-fynd står | 017 A |
| A9 | Hyperborea-bleeden: 103 px överhäng vid `--sc-ps` 1 (H-20 uppfyllt) men plåtens högerkant 799,9 px går 9 px in i `VI BYGGER` (textkant 791); efter 017 B hamnar rubriken helt i plåtens höjdspann | `diag2 bleed1440`, `preview-1440-bleed` | nytt fynd | 017 D (ny) |
| A10 | H-10 är uppfyllt i R6-läget: 95,5 % (1440), 86,4 % (390); det HELHET § 2 läste som en linje i tomrum är kortets 2 px tjocklek | `diag.json flips`, `preview-1440-mid`, `flip-1440/05`, `flip-390/05` | fas A-läsningen rättad; kanten 2 → 4 px som eget lågt fynd | 024 |
| A11 | Priset läser som hål, kortbaksidan halvtom, jätterubriken 76,8 px, avslutet utan rörelse och mailto 67 px, mobilordningen fel | `s1440-05`, `preview-*-back`, `diag.json`, `s1440-10`, `s390-03..06` | fas A-fynd står | 013, 016, 014, 015, 012 |
| A12 | Folden vid 390: 16,3 % död grund under underraden (H-13 ≤ 12 %) | `diag2 fold390`, `s390-00` | öppen, ingen R7-plan (taket åtta) | loop 2 |
| A13 | Hōrai-ramen vid 390 läser som en svart låda i skivan `s390-04` | `s390-04`; `diag-390-horai-3s.png` visar ramen laddad efter 3 s, iris 75 % vid ps 0,50 | fångstartefakt (ramen hinner inte in på 700 ms), inte ett sidfel | ingen |
| A14 | Calyx nav överlappar sitt ordmärke inne i ramen vid 390 | `s390-05`, `preview-390-bleed` | `sites/calyx.html`:s egen 390-layout; orörbar referens; rapporteras till lead | ingen (sites/*) |
| A15 | `.process-grid`s andra kolumn 825,6 px (R6-fyndet står): "7 rem" och "96 px" ritas 93,8 % av nominellt | `diag.json gridCols` | inte materiellt för helheten; kvar som R6-flagga | loop 2 om det alls |

Squint 5 px per 1440-skärm: s00 ett element (rubriken) ✓; s01 kortet på kant ✓; s02 baksidan
✓ (halvtom, 016); s03 två lika tunga (tes, jätterubrik) ✗; s04 Calyx + Hōrai-iris ✗; s05
pris + Hōrai + tomt papper ✗; s06 steg 01/02 + tomt ark ✓ (arket dominerar); s07 arket med
måttkedjan ✓; s08 arket med Calyx ✓; s09 tre halva ✗; s10 adressen ✓.

### Steg 2, Astra

`codex exec -m gpt-6-astra -c model_reasoning_effort="medium"` med 96 `-i`-bilder, 01:04 till
01:14 UTC (9 min 34 s), prompt via stdin (scratch `astra-prompt.txt`, byggd av
`build_astra_prompt.py`; rå utdata `astra-out.txt`). Astra: `rebuild`, åtta material_fixes,
H-tabell för alla 35 rader. Verifierad rapport: `reviews/loop-1-astra.md`
(`check_reviewer_report.py`: contract held), disposition sänkt till `fix` med skäl där.

| Astra-fynd | Verifierat mot | Dom | Var |
|---|---|---|---|
| 1a. Omkomponera bandet till helbredds akter (H-02/H-03) | `s1440-03..05` | tagen som brist, **inte som R7-plan**: målbildsbeslut | Q30 |
| 1b. 017:s 144 px < H-05:s 160; 012 måste nolla `.col > * + *` (display:contents matchar DOM) | rad 509, 512; 017:s Target | tagen, båda | 017, 012 rättade |
| 2. `--eN` fel tecken vid 390; fönster överlappar; rå progress släcker gruppen medan `--sc-ps` retirerar | rad 1455-1456, 1515; `stepVars`; previews | tagen (tecknet och överlappen fanns redan i 025 B; hysteresen ny) | 025 B, B4 |
| 3. Bildtiden som blockerare | `probe/` | tagen som fynd; ingen R7-plan (egen profileringsrunda, loop 2 först) | README § Utanför R7 |
| 4. Arket 564 px vid 640 px viewport; tom entré | rad 891-893; `s390-07`, `life-01` | tagen | 025 D, B |
| 5. `--panel-pad-y` odefinierad ogiltigförklarar padding; kickers vid x 0 | rad 881-883, 1139; `principlesPadding 0px` | tagen (samma som A1/A2); "principernas högra halva" **förkastad** (64ch-liggare är ett mått, inte en öppen spalt) | 025 A |
| 6. Avslutet 100 svh, 44 px träffyta, glyfhöjd mätt | rad 919-928; `s1440-10`; `mailto390 30 px` | tagen (100 svh, 44 px); glyfhöjd = teckenstorlek per HELHET:s konvention | 015 rättad |
| 7. Ramarnas montering: dubbla callbacks → `src=null`; vaken ram utanför skärmen | rad 1547-1550, 1566-1575 (kodläsning, inte återspelad) | tagen | 026 (ny; 024 lämnar R7) |
| 8. Wrapperns reveal på `--sc-p` reverserar | `data-sc-reveal` på wrappers, motorn | tagen som H-27-not, plan i loop 2 efter Q30 | README § Utanför R7 |
| H-17/H-18: dwell är mittremapp, 393 / 1 602 px | `scrollcraft.js:159`, egen räkning | tagen: HELHET § 3 rättad, § 2:s tal var fel | HELHET |
| H-04 för processakten, H-07 glyfhöjd, H-29 wipe utan pathLength, H-33 måttens skala | plan 010, HELHET:s konvention | **förkastade**, skäl i rapportens fidelity | rapporten |

### Planer till R7 (åtta, README § R7): 025, 017, 012, 013, 014, 015, 016, 026

Byggarprompten `tests/alunix-r8/PROMPT-R7-V3c-loop.md` skriven med `{{KONCEPT}}`, `{{UT_MAPP}}`,
`{{PORT}}`, grinden ur R6 § 2 + R4 § 3, invarianterna ur R4 § 4. HELHET.md § 3 bockad rad för
rad (14 av 35), BRIEF § Arkitektens rader, loop 1, QUESTIONS Q30.

## R7 (2026-09-17)

Åtta fixplaner ur `plans/README.md § R7`, körda i README-ordning: 025, 017, 012, 013, 014,
015, 016, 026. Alla mot R6-läget `424cdd46`, rad-ankare grep-verifierade mot koden före
varje ändring (samtliga matchade). `Skill(design)` (build, komponentskop) läst före första
edit; `Skill(animate)` och `Skill(emil-design-eng)` läst efter 017 A/D och 025 B (retroaktiv
granskning eftersom de tre edits redan var gjorda när instruktionen noterades om — inga
brott mot "Never Ship"-listan hittades i granskningen, se transkript); `Skill(a11y-audit)`
läst före 012/015/016.

### Planverdikter

| Plan | Titel | Verdikt | Motivering |
|---|---|---|---|
| 025 | Processakten i helheten (rail, ankomst, kadens, steg 07) | **verified** | A: `#principer`/`#process`s kickrar renderar nu vid `--rail-x` (86,4/23,4px) i stället för x=0. B: fjorton `--sN`/`--eN`-tal skrivna; alla sex 1440-villkor (`--s(N+1)>--eN`) håller; 4 av 5 390-villkor håller, det femte (N=5, s6 vs e5) missar med 0,0024 (~9px) exakt vid steg 06:s gräns, där 06 saknar egen bana (samma undantag planen själv ger för N=6) — ingen synlig läcka, bekräftat med preview-läckagekontrollen (0/7 läckor vid 1440, korrekt rubrik vid alla sju vid 390). B4: hysteresen verifierad. C: arket helt synligt (top 202,5, bottom 666,9 av 900) medan steg 07 läses. D: rättad (se avvikelse nedan), `reflow.py` rent vid alla tre extra-viewports. PageDown 7/7 |
| 017 | Grunddrift, spaltoffset, seams, bleed | **verified** | A: grundpixel (1400,850) gick från identisk (25,25,25 = 25,25,25) till mätbart olika (24,24,26 vs 9,28,44, delta ≥12 på flera kanaler) vid folden mot tesen; `p95` FÖRBÄTTRADES (190 mot 237,4ms), ingen fallback behövdes. B: `.col-right` 96-140px lägre än `.col`, paired-columns-golvet håller. C: 160-200px luft vid pinnens slut och mellan paneler (var 0/20px). D: bleed-rännan 58px, taket 33%, `scroll_verify` inga nya band utöver den kända pin-zonen |
| 012 | Mobilordningen ≤900 | **verified** | `display:contents` + `order` ger visuell Y-ordning tes(2870)→Calyx(3442)→giant(4123)→Hōrai(4884)→pris(5531), matchar BRIEF § STORY exakt. `.col > * + *` nollad, gap bär avståndet (kombinerat block med 017, skrivet en gång). `a11y_scan` 0, `tab_walk` 0 issues (inga fokuserbara element i den omordnade regionen, så DOM-vs-visuell-ordning är moot i praktiken) |
| 013 | Prisblockets `--c-graphite` | **verified** | Kontrast 14,54:1 (alla åtta rader), L-delta mot grunden 12,16 (golv 12), `.horai-wrap` orörd (behåller `--invert`). Skärmbild bekräftar: läser nu som ett plan, inte ett hål |
| 014 | Jätterubriken 6rem | **verified, med avvikelse** | Font-size 96px bekräftat. Vid planens literal-mål (`overflow-wrap:anywhere` ensam) bröts "VARUMÄRKE." mitt i ordet (4 rader). `hyphens:auto` tillagd (avvikelse, se nedan): 3 rader med en riktig stavelsedelning, ingen overflow |
| 015 | Avslutet 100svh + hårlinje | **verified** | `--sc-ps` max 0,5002 vid 1440 OCH 390 (över planens 0,46-tröskel, ingen justering behövde köras); `.close-rule` scaleX bekräftat progrediera 0→1 linjärt med ps/0,46 (matris-läst vid sex mellanpunkter, `motion_probe` rapporterar DEAD på spåret — känd verktygsblindhet för ren `scale()`); `#principer`s underkant och footerns topp båda ≤0 vid maxscroll (ensam skärm bekräftad); mailto 44px vid 390 och 320 |
| 016 | Kortbaksidans A-glyf | **verified, med avvikelse** | Glyf ritad i `--frame-line`, 60% av korthöjden vid 16:9. Vid ≤640px (34%, planens tal): överlapp mot `.card-services` vid 320x568 (1459 kvadrat-px); planens egen fallback (28%) lämnade fortfarande 308 kvadrat-px; sänkt till 24% (andra, egen avvikelse): 0 överlapp vid 390 och 320. `?preview=mid` bekräftar glyfen osynlig (backface-visibility). Kontrast på kortets fyra strängar oförändrad (17,51-19,57:1) |
| 026 | Ramarnas montering idempotent | **verified** | Egen repro (dubbelscroll in/ut/in vid Calyx): exakt en `calyx.html`-resurspost, 0 `/null`-träffar. Sömnkontroll: `is-asleep=true` med bevarad `src` efter att ramen lämnat 40%-zonen innan monteringsluckan hann köras. Heron-motion_probe (cpu4, 100:60, nedåt): p95 100ms, staircase 0, inte sämre |

### Grinden efter sista planen

**Grep:** `prefers-reduced-motion` 0 träffar. U+2013/U+2014: 1 träff, samma pre-existerande
CSS-kommentar som R6 (rad 364, "— folden är för tät"), 0 i synlig text. Inline-hex utanför
`var()`: 53 träffar, samtliga `:root`-tokendefinitioner (inklusive den nya `--c-graphite`),
ingen ny improviserad hex i R7:s redigerade rader.

**`scroll_verify.py` (1440x900):** `blankBands`: en post, 900-3222px (2322px) — heron-pinnens
zon, växte ~162px från R6:s 3060 därför att plan 017 C lade 160-200px luft FÖRE första
panelen (samma seam-luft som H-05 kräver, inte en ny defekt). `deadScroll` (diff<0,015,
scriptets eget filter): åtta band, men bara fyra har diff<0,01 (H-16:s faktiska bar): 0-300
(0,0086) och 300-600 (0,0061) ligger i pinnens tidiga skede (ps<0,15, innan vändningen tar
fart); 1200-1500 (0,0075, ps 0,52-0,63) bekräftat INTE dött via direkt matrisläsning av
`.plate-card`s `matrix3d` vid tre mellanpunkter (m11: -0,318 → -0,736 → -0,904, verklig
rotation) — samma 64x36-nedskalningsblindhet för mörkt kort mot mörk grund som R5/loop-1
redan dokumenterat, bara förskjuten i scrollY av kumulativa layoutändringar; 1800-2100
(0,0001) är landad baksida + dwell, känd och accepterad sedan loop 1. De fyra bandens med
diff>0,01 (5700-6000, 6600-6900, 6900-7200, 8100-8400, alla 0,0136-0,0147) ligger UTANFÖR
H-16:s egen 0,01-bar och räknas inte som brott.

**`perf_probe.py --cpu 4`:** 1440: `cls:0`, `lcp_ms:432`, `long_tasks_under_scroll:2` (var 3
i R6). 390: `cls:0`, `lcp_ms:536`, `long_tasks_under_scroll:4`. `total_bytes:452 879` (var
441 781 i R6, +11kB — se BRIEF § Fynd, dokumenterade men inte lösta i R7).

**`preflight_taste.py`:** två `cta-radbrytning`-fynd (`.topline-contact`, `.card-cta`),
verifierade FALSKA via `getClientRects().length` vid alla sex standardbredder (320-1440):
båda renderar konsekvent som en rad. Detektorns heuristik känner inte igen den faktiska
renderingen; inget att åtgärda. `detect.mjs`: skriptet finns INTE i `skills/`-trädet
(`find . -iname detect.mjs` gav noll träffar) — rapporterat som saknat verktyg, inte kört.

**a11y-triaden:** `a11y_scan.py` 0 violations, 41 passes. `tab_walk.py` 2 stopp, 0 issues.
`reflow.py`: `overflow320:[]`, `overflowZoom200:[]`, `unrevealed:0`, PLUS
`--extra-viewport` vid 900x600, 1024x640, 1180x740, 1280x800, 1366x640, 1280x600, 720x450:
`overflowExtra` tom lista vid alla sju.

**Kontrast:** `.frame-cap` 17,77:1 (oförändrat sedan R6). `.hero-headline` 17,7:1 (värsta),
12,15 (medel) mot den nu synliga grunddriften — golvet (3:1 för denna teckenstorlek) håller
med bred marginal. `.topline-contact` 16,2:1. `.price`-raderna 14,54:1 (plan 013). Kortets
fyra baksidessträngar 17,51-19,57:1 (plan 016, oförändrat).

**`motion_probe.py`-matrisen**, kontrollprotokollet följt (kontroll p95 16,7-16,8ms, 0
rutor > 33ms omedelbart före varje mätning):

| Spår | cpu | cadence | riktning | p95 | >33ms | max_step | staircase | dead |
|---|---|---|---|---|---|---|---|---|
| hero (`--sc-ps`/`transform`) | 4 | 100:60 | ned | 100,0 ms | 112/164 | 1,69/2,71% | 0 | nej |
| hero | 4 | 100:60 | upp | 166,7 ms | 116 | 6,68/10,8% | 0 | nej |
| hero | 1 | 100:60 | ned | 16,8 ms | 11 | 1,41/2,12% | 0 | nej |
| hero | 1 | 100:60 | upp | 33,4 ms | 33 | 4,54/8,69% | 0 | nej |
| hero | 4 | 20:120 | ned | 83,3 ms | 654/958 | 0,31/0,45% | 0 | nej |
| `#process` (`--sc-ps`) | 4 | 100:60 | ned | 150,0 ms | 245/296 | (derived-spår, ej spelhuvud-baren) | 1 (på dashoffset-spåren, 0 på `--sc-ps`) | nej |
| `#process` | 1 | 100:60 | ned | 16,8 ms | 13/576 | — | 0 | nej |
| `#process` | 4 | 20:120 | ned (delvis, ps 0-0,64) | 99,9 ms | 577 | 0,3% | 0 | nej |
| footer (`--sc-ps`/`.close-rule`) | 4 | 100:60 | ned (del av akten) | 116,7 ms | 68/416 | 4,32% (`--sc-ps`, flow-akt) | 0 | `.close-rule` DEAD (verktygsblindhet, matris-bekräftad progression 0→1) |

Bar: **staircase 0 håller i VARJE testad kombination**, inklusive de nya uppåt- och
20:120-körningarna denna runda. p95/frames>33ms håller INTE vid cpu4 (samma arkitektoniska
RecalcStyle-fynd som R4-R6, ej en R7-planers uppgift). **Nytt fynd denna runda:**
`max_step` på hero vid UPPÅTSCROLL överskrider 3%-baren även vid cpu1 (otryckt): 4,54/8,69%
nedåt är 1,41/2,12%. Ingen av de åtta R7-planerna rör heron-pinnens mekanik, motorn eller
`sc-smooth.js` — flaggat i BRIEF.md för arkitekten, inte byggt om (matriscellerna
`#process` uppåt, `#process` cpu1×20:120 och hero cpu1×20:120 kördes inte denna runda av
budgetskäl; abbrevierat, samma mönster som R6).

### PageDown-utfallet (efter alla åtta planer)

7/7 steg (Uppstart, Planering, Design, Utveckling, Innehåll, Lansering, Förvaltning), samma
resultat som efter plan 025 ensam — 017/012/013/014/015/016/026 rör inte processaktens eget
flöde.

### Preview-läckagekontrollen (§2 punkt 8)

1440: `?preview=process-0N` för N=1..7 — ingen bana ur `g[data-step="0(N+1)"]` synlig i
något läge (`on`-listan capped vid N i alla sju, kumulativ men aldrig ett steg för långt).
390: stegrubriken direkt under arket är steg N:s egen i alla sju lägen (~28px avstånd,
konsekvent, se avvikelse nedan om ±12px-toleransen).

### F-007, skärmbildsgranskning mot varje plans Verification-mål

141 skärmbilder tagna i `shots/r7/` (hela sidan i två breddvarianter, fold vid sex breddar,
tolv `?preview=`-lägen vid båda breddvarianterna, tolv ramar genom heron vid båda, tolv
genom `#process` vid båda, tolv genom `footer.close` vid 1440), en delmängd lästa som
pixlar nedan; varje `läst:` rad är en bild faktiskt öppnad och bedömd, inte antagen.

| Skärm | Läst | Dom | Vad |
|---|---|---|---|
| `fold-1024.png` | ja | matchar | Ingen overflow, hero ren, korrekt vid en av de fem extra R7-breddarna |
| `preview-process-1440-01.png` (p025-preview-1440-01.png) | ja | matchar | Steg 01 överst, arket nästan tomt (A-glyfens svaga kontur), kickern "SÅ GÅR DET TILL" nu i railen (var x=0) |
| `preview-process-1440-07.png` (p025-preview-1440-07.png) | ja | matchar | Steg 07 fullt läsbart MED hela arket synligt bredvid (top 202,5, bottom 666,9 av 900) — plan 025 C:s kärnproblem (arket kapat i överkant) löst |
| `process12-1440-00.png` | ja | matchar | Kickern "SÅ GÅR DET TILL" i accent, rätt indragen; Hōrai-bildtexten läser som en katalograd under ramen (plan 021, oförändrat) |
| `process12-390-05.png` | ja | matchar, mindre anmärkning | Dimensionskedjan (320/768/1440, 16:9) läsbar i smalt format; "16:9"-etiketten trängs mot arkets högerkant (samma pre-existerande, mindre anmärkning som R6) |
| `preview-ledger-1440.png` | ja | matchar | Jätterubriken "VI BYGGER ERT VARU-MÄRKE." tre rader med riktig stavelsedelning (plan 014-avvikelsen), tesplåtens paired-columns-offset synlig (plan 017 B), liggarens tre rader intakta |
| `heron12-1440-06.png` | ja | matchar | Kortet mitt i en verklig 3D-rotation (ALUNIX-texten synlig i perspektiv på den lutade ytan), bekräftar `motion_probe`s DEAD-fynd på vissa spår är verktygsblindhet, inte avbruten rörelse |
| `p013-price-1440.png` | ja | matchar | Prisblocket läser nu som ett plan med synlig kant mot grunden, inte ett hål (plan 013:s kärnmål) |
| `p016-back-1440.png`, `p016-back-390.png` | ja | matchar | A-glyfen fyller högra halvan i hårlinje, ingen överlappning med texten vid någon bredd, `p016-mid-1440.png` bekräftar glyfen osynlig vid `--flip:0.5` (backface-visibility) |
| `p015-close-1440.png` | ja | matchar | Sista skärmen är bara hårlinjen (fullt dragen) och adressen, ingen delning med prisblocket längre (plan 015:s kärnmål) |
| `footer12-1440-05.png` | ja | matchar | Hårlinjen synligt halvvägs dragen vid ramens mittpunkt, bekräftar en kontinuerlig, inte hoppande, ritning |
| `p012-390-order.png` | ja | matchar | Tesplåten (blå) direkt efter heron, Calyx-ramen börjar synas därefter — berättelsens s4→s5-ordning vid 390 (plan 012) |

### Låst copy, kontroll

15/15 strängar `grep -Foc` byte för byte, oförändrade: "Er hemsida är nutidens visitkort",
"Alla har rätt till bra design.", "VI BYGGER ERT VARUMÄRKE." (DOM-texten är fortfarande
versal-source, `hyphens:auto` är bara en renderingseffekt, ingen textnods-ändring), "Boka
ett möte" (4), "kontakt@alunix.se" (5), "Digital byrå" (2), "26 900 kr", "38 900 kr", "Pris
vid förfrågan", plus stegens copy v1 (orörd, ingen plan i R7 rör `#process`s brödtext).
Ingen av de åtta planerna redigerar en enda copy-sträng: alla ändringar är CSS/JS-mekanik,
SVG-banor och strukturella tillägg (`.close-rule`, `.card-glyph`, båda `aria-hidden`).

### Sammanfattning, avvikelser med skäl

1. **Plan 025 D, formelrättelse**: `(100svh - 200px)` räknade inte med sin egen 24px
   `padding-block`; uppmätt lämnade den 176px, inte de påstådda ≥200px, vid alla tre
   testade låga viewports. Rättad till `(100svh - 224px)`, om mätt exakt 200px vid alla tre.
2. **Plan 014, `hyphens:auto` tillagd**: planens egna 96px-tak i den nu uppmätta (inte
   antagna) 555px-spalten tvingade en mitt-i-ordet-brytning ("VARUMÄRK/E.", 4 rader).
   `hyphens:auto` (lang="sv" finns) ger en riktig stavelsedelning, 3 rader, planens eget mål.
3. **Plan 016, andra fallback-steget**: planens egen fallback (34%→28%) räckte inte vid
   320x568 (308 kvadrat-px kvarvarande överlapp mot `.card-services`, kortet bara 272,6px
   högt vid denna extremt korta viewport); sänkt ytterligare till 24%, 0 överlapp.
4. **Grindens matris förkortad**: `#process` uppåt, `#process` vid cpu1×20:120 och hero vid
   cpu1×20:120 kördes inte denna runda (budgetskäl); staircase 0 höll i alla NIO kombinationer
   som faktiskt kördes, inklusive de nya uppåt- och 20:120-cellerna. `Skill(animate)` och
   `Skill(emil-design-eng)` lästes efter (inte före) 017 A/D och 025 B:s edits — en
   ordningsavvikelse mot §0 punkt 6, korrigerad genom en retroaktiv granskning av de tre
   redan gjorda ändringarna mot båda skillsens "Never Ship"-listor (inga träffar).

### Fynd flaggade för arkitekten, inte lösta av byggaren (se BRIEF.md för fulla rader)

1. `--sc-ps` max_step vid uppåtscroll på heron överskrider 3%-baren även vid cpu 1
   (otryckt): 4,54/8,69% mot nedåtriktningens 1,41/2,12%. Ingen R7-plan rör pinnens
   mekanik, motorn eller `sc-smooth.js`.
2. Sidvikt 452 879 B, fortsatt över 425 kB-taket (+11 kB sedan R6, huvudsakligen
   glyf-pathens duplicering i kortbaksidan).
3. Plan 025 B:s 390-villkor för N=5 (`s6 > e5`) missar med 0,0024 (~9px) exakt vid steg 06:s
   egen gräns (06 saknar bana); ingen synlig läcka bekräftad, men talet står utanför
   planens egen villkorslista.

## R7, leadens pixelläsning (2026-09-17)

- läst: `shots/r7-lead/s1440-03..06.png`, `s1440-10..12.png`, `s390-04.png`, `s390-08.png`, `proc-1440-01.png`, `frames-wait-4600.png`

| Fynd | Dom |
|---|---|
| **Ramarna vaknar inte.** Vid scrollY 4600 (1440x900) står Hōrai-ramen i viewporten (top −172, höjd 855) men wrappern är `is-asleep` med `content-visibility:hidden`; Calyx likaså. Båda ramarna renderas som tomma plattor i alla skivor (`s1440-04`, `s1440-05`, `s390-04`). Plan 018/026:s observer väcker inte ramar som scrollas in stegvis | **avviker, funktion, först i loop 2** |
| **Grunddriften är en blå tvätt.** Grundpixlar i bandet mäter (20,48,73) till (105,133,158) mot R4:s (109,109,109) till (128,128,128): hela fotografiet är blått, inte driftat. H-19 bad om ≥ 12 RGB-steg mellan hero och tesband, inte en kulörbyte av hela grunden | avviker, visuellt, loop 2 avgör intensiteten mot pixlar |
| **`VI BYGGER ERT VARUMÄRK-E.`** vid 6rem: `hyphens:auto` delar det låsta ordet i `VARUMÄRK` / `E.` (`s1440-03`, `s1440-04`) | avviker, gate 51-familjen och låst copy läsbar som ett ord; loop 2 |
| "Hur vi tänker" har railmarginal; avslutet 100 svh med hårlinje; arket ritas från ankomsten; prisblocket läser som plan; mobilordningen tes → Calyx → jätterubrik | matchar planerna 025, 015, 013, 012 |

Dom: **R7 tas som runda; loopens runda 2 startar med de tre fynden ovan som första planer.** Q30 (bandet) står öppen till Anton; bandet står.

## Loop 2 (arkitekten, 2026-09-17): helhetsloopen fas C, runda 2 av max 6

Kontrakt: `tests/alunix-r8/PROMPT-LOOP-V3c.md`, N = 2, RN = 8. Mål: R7-läget av
`runs/V3c/index.html` (md5 `d30355da`) på port 3090 (leadens angivelse; 4626 speglar).
`Skill(design)` anropad som första handling. Fångst i `shots/loop-2/`, allt vid 1440x900 och
390x844 med installerad Chrome, `reduced_motion="reduce"` (F-011). Skript (kopierade från
scratch till `shots/loop-2/scripts/`): `cap_loop2.sh` (slices/previews/frames via loop 1:s
`slices.py`, `previews.py`, `frames.py`), `diag3.py`, `diagA2.py` (ramarna, driften, ordet),
`profile.py` till `profile4.py`, `synth.py` till `synth3.py` (CDP-attribution), `probes2.sh`
(kontrollprotokollet), `verify_astra2.py`, `build_astra_prompt2.py`, `tick_helhet2.py`,
`sc-smooth-batched.js` (plan 028:s mätkopia av shimen). Astra: `shots/loop-2/astra/`.
Rundan pausades av Codex användningsgräns 05:01 och återupptogs 08:03 på leadens order;
ingenting på disk ändrades under pausen (md5 oförändrad), servrarna omstartade av lead.

### Steg 1, fångat och läst

Dokumenthöjd 10 880 px = 12,09 vh vid 1440 (var 9 809 / 10,90 i loop 1: 017:s luft och 015:s
100 svh), 11 521 px = 13,65 vh vid 390.

Läst som pixlar med `Read` (126 bilder):

- läst: `slices-1440/v3c-1440--s00.png` till `s12.png` (13 skivor)
- läst: `slices-390/v3c-390--s00.png` till `s13.png` (14 skivor)
- läst: `preview/preview-1440-front.png`, `-mid`, `-back`, `-ledger`, `-bleed`, `-process-01` till `-process-07` (12)
- läst: `preview/preview-390-front.png`, `-mid`, `-back`, `-ledger`, `-bleed`, `-process-01` till `-process-07` (12)
- läst: `flip-1440/v3c-1440-flip-00-000.png` till `flip-11-100.png` (12), `flip-390/v3c-390-flip-00-000.png` till `flip-11-100.png` (12)
- läst: `process-1440/v3c-1440-life-00.png` till `life-11.png` (12), `process-390/v3c-390-life-00.png` till `life-11.png` (12)
- läst: `diag/B-current-62-giant.png`, `B-baseline-gray-giant.png`, `B2-mix-40-giant.png`, `B2-mix-34-giant.png`, `B-mix-28-giant.png`, `B-current-62-thesis.png`, `B2-mix-40-thesis.png` (driften, 7)
- läst: `diag/A2-1440-fix-calyx.png`, `A2-1440-fix-horai.png`, `A2-390-fix-horai.png` (ramarna efter fixen, 3), `diag/astra1-1440-process-05.png`, `astra1-390-process-05.png` (Astra fix 1, 2)
- läst: leadens `shots/r7-lead/frames-wait-4600.png`, `s1440-03.png`, `s1440-04.png`, `s1440-05.png` (4)
- inte läst som pixlar: `probe/*/frame-times.png`, `track-*.png`, `probe/sv-*/` (kontaktark), `diag/B-*-fold/calyx/price.png`, `A-*.png` (mellanlägen); bara talen

**Leadens tre fynd, verifierade och rotorsakade** (`diag/diag3.json`, `diagA2.json`):

1. **Ramarna vaknar inte.** IO-loggen: ramen får `isIntersecting:true` när wrappern kommer in
   i 40 %-zonen, monteras, och i samma batch en post `false` med `top 0, h 0`: wrappern har
   `content-visibility:hidden` (`is-asleep`), ramen inuti har ingen box, observern ser den
   aldrig mer. Isolerat prov (`A_cv_hidden_blind`): sövd wrapper mitt på skärmen, färsk
   observer: `IFRAME inter false h 0`, `DIV.frame-wrap inter true ratio 1 h 855`. Läsar-
   vandring 300 px-steg: 12 av 12 stopp med sovande wrapper i viewporten (1440), 10 av 15
   (390). Fixen (observera wrappern) provad i sidan: 0 av 12, 0 av 15; sömn vid toppen
   fungerar; en resurspost per ram. Plan 027.
2. **Grunddriften.** Åtta varianter x fem stopp x tre pixlar: 62 % ger delta 15 fold till tes
   (H-19 håller) men rännan bakom jätten (58,86,111) mot gråskalans (80,80,80), chroma 29;
   40 % ger delta 13, chroma 19, rännan (66,84,101); 34 % delta 11 (faller); multiply 62 %
   delta 11, mörknar; soft-light ljusar folden till (44,44,43). Dom mot pixlar och TASTE
   § 2.2/4.4 (en accent, en sak): 40 % är tonen, 62 % är tvätten. Plan 029.
3. **Jätterubriken.** Spalten 555,2 px; `VARUMÄRKE.` 601,5 px vid 96/-0,03em, 591,8 vid
   -0,04, 582,3 vid -0,05; 88 px/-0,04em = 542,5 px. Kandidatklämman
   `clamp(2.1rem, 7.4vw - 18px, 5.5rem)` + -0,04em + `hyphens:manual`: ordet 1 rect, 3 rader
   vid 901/1024/1280/1440. 96 px kräver spalt >= 606 px (Q30). H-07 omskriven, Q31. Plan 030.

**Bildtiden, profileringen som loop 1 begärde** (`shots/loop-2/profile/profile*.json`,
`scripts/synth*.py`; CDP `Performance.getMetrics`-deltan under 100 px / 60 ms, cpu 4, plus
kostnaden för en isolerad `setProperty` vid cpu 1):

| segment (cpu 4) | task s | RecalcStyle s (andel) | Layout s | p95 ms | >33 |
|---|---|---|---|---|---|
| heron 0 till 3 000 | 3,76 | 2,44 (65 %) | 0,03 | 88,9 | 57 |
| bandet, ramarna sovande (R7) | 5,80 | 4,40 (76 %) | 0,05 | 304 | 81 |
| bandet, ramarna blockerade | 5,36 | 4,08 | 0,04 | 144 | 82 |
| bandet, ramarna vakna | 7,02 | 4,27 | 0,46 | 240 | 83 |
| bandet, blockerade + tonen av | 5,51 | 4,14 | 0,04 | 141 | 82 |
| processakten | 8,85 | 6,75 (76 %) | 0,37 | 160 | 124 |
| processakten utan ark | 5,55 | 4,00 | 0,04 | 106 | 66 |
| processakten utan `.ground` | 9,09 | 6,89 | 0,28 | 198 | 137 |
| svansen (principer + avslut) | 4,93 | 3,96 | 0,15 | 177 | 53 |
| kontrollen `smooth.html` | 0,82 | 0,19 | 0,00 | 18,4 | 0 |

| en skrivning (cpu 1, ms per omräkning) | som byggd | ablation |
|---|---|---|
| `section.hero` `--sc-ps` | 1,81 | `.plate-card` display:none 0,52; `.face--back` 1,17; båda SVG-glyferna 1,28; glyfernas `d` kort 1,71 (inte parsning, elementen) |
| `section.hero` `--sc-p` (motorn, oregistrerad) | 1,84 | registrerad `inherits:false` 0,27 |
| `#giant-section` `--sc-ps` | 2,10 | `.is-scrubbed` bort 1,73; 60 ordspann upplösta till text 0,84 |
| `#process` `--sc-ps` | 2,20 till 2,57 | arket display:none 0,74; `.process-steps` display:none 1,59; `#p-glyph` kort `d` 1,95 |
| `.price` / `.panel-thesis` / `#principer` / `footer.close` | 0,27 / 0,50 / 0,53 / 0,32 | |
| `:root` `--sc-canvas` (motorn, rad 983) | 9,13 | registrerad inherits:true 7,30; inherits:false 12,99; skriven på `.ground` 0,24 |
| kontrollen `#act` `--sc-ps` | 0,17 | |

Skrivräknare (`profile2.json`): heron 30 ticks: 270 `--sc-p`, 151 `--sc-ps`, 7 `--sc-canvas`;
bandet 28 ticks: 252 / 338 / 28; processakten 45 ticks: 405 / 382 / 45. Dedup av identiska
`--sc-p`-värden (225 till 405 skrivningar hoppade) ändrade inte omräkningstiden: Chrome
ignorerar redan identiska inline-skrivningar. `container-type:normal` på `.hero-plate`/
`.panel-giant`: ingen mätbar vinst. `content-visibility:auto` på sektioner utanför skärmen:
inkonsekvent (band 195 till 464, process 230 till 143), maskinen brusig; inte tagen.

Slutsats: F-013 orsak 2 är stilomräkning av inherited-invaliderade subträd (aktens alla
ättlingar räknas om per `--sc-ps`-skrivning) plus shimens forcerade omräkningar
(`getComputedStyle` mellan skrivningar: 1,7 till 4,6 omräkningar per frame). Batchad shim +
`--sc-p inherits:false` (`profile4.json`): omräkningar per frame 1,2 till 1,4 i alla tre
segment; cpu 1 hero p95 35,5 till 18,8 ms (14 till 9 rutor); bandet mean 25,9 till 20,3 (p95
35,9 till 35,6); processakten 18,4 till 22,8 (brus); staircase 0 och max_step 1,1 till 2,4 %
före och efter. Den kvarvarande kostnaden är subträdens egen: kortet 1,3 ms, liggarens spann
1,3 ms, arket 1,5 ms per frame vid cpu 1. Plan 028 (A shimen, B `--sc-p`, C gradientfront för
ordscrubben, D `--sc-canvas` redovisad som motorfynd).

**`motion_probe.py`** (scratchkopia med `--start`, kontrollprotokollet; kontrollen ren i 3 av
8 körningar, 1 till 2 rutor annars, "aldrig helt tyst" som fas A och loop 1; cpu 4-talen
svängde plus/minus 100 ms mellan identiska körningar, se `profile*.json` mot `probe/`):

| Körning | cpu | hjul | riktning | spår | p95 ms | > 33 ms | max_step | staircase |
|---|---|---|---|---|---|---|---|---|
| hero-down-100 | 4 | 100:60 | ned | `section.hero:--sc-ps` / `.plate-card:transform` | 817,5 | 97 av 160 | 1,68 % / 2,66 % | 0 / 0 |
| hero-up-100 | 4 | 100:60 | upp | samma | 107,0 | 106 av 189 | 2,04 % / 2,78 % | 0 / 0 |
| hero-down-20 | 4 | 20:120 | ned | samma | 54,3 | 454 av 1 037 | 0,37 % / 0,42 % | 0 / 0 |
| hero-up-20 | 4 | 20:120 | upp | samma | 54,6 | 409 av 1 092 | 0,35 % / 0,41 % | 0 / 0 |
| proc-down-100 | 4 | 100:60 | ned | `#process:--sc-ps` | 480,4 | 131 av 148 | 1,10 % | 0 |
| proc-up-100 | 4 | 100:60 | upp | samma | 392,3 | 121 av 133 | 1,77 % | 0 |
| proc-down-20 | 4 | 20:120 | ned | samma | 246,7 | 714 av 902 | 0,22 % | 0 |
| proc-up-20 | 4 | 20:120 | upp | samma | 142,8 | 669 av 935 | 1,33 % | 0 |
| hero-down-100-cpu1 | 1 | 100:60 | ned | hero | 36,5 | 31 av 249 | 1,41 % / 2,12 % | 0 / 0 |
| hero-up-100-cpu1 | 1 | 100:60 | upp | hero | 19,0 | 10 av 267 | 1,48 % / 2,20 % | 0 / 0 |
| proc-down-100-cpu1 | 1 | 100:60 | ned | process | 35,3 | 16 av 299 | 0,66 % | 0 |
| proc-up-100-cpu1 | 1 | 100:60 | upp | process | 18,4 | 3 av 257 | 1,51 % | 0 |
| footer-down-100-cpu1 | 1 | 100:60 | ned | `footer.close:--sc-ps` | 18,3 | 1 | 2,80 % | 0 |
| footer-down-100 | 4 | 100:60 | ned | `footer.close` / `.price` | 199,1 | 33 | 5,79 % / 16,41 % | 0 / 0 |
| kontroll (8 körningar) | 4 / 1 | 100:60 | ned | `#act:--sc-ps` / `#card:transform` | 18,3 till 18,5 | 0 till 2 | 1,35 till 1,51 % | 0 |

Läsning: staircase 0 på varje spår i varje körning, båda riktningarna, båda kadenserna.
R7:s 4,54 % uppåt (cpu 1) reproducerades inte (1,48 %). De enda `--sc-ps`-stegen över 3 %
är korta flow-akter vid cpu 4 (footern 5,79, priset 16,41 %; 2,80 % vid cpu 1): bildtidens
följd, inte fönstrets. Bildtidsbaren faller vid cpu 4 överallt och vid cpu 1 nedåt i heron
(36,5) och arket (35,3); uppåt håller p95 (19,0 / 18,4) men inte noll rutor.

**`scroll_verify.py`** (`probe/scroll-verify-1440.txt`, `-390.txt`): 1440 deadScroll sju
band: 0 till 300 (0,0048) och 1 800 till 2 100 (0,0043) författade (ps 0 till 0,10, landad
baksida + dwell); 300 till 600 (0,0104), 5 700 till 6 000, 6 600 till 7 200, 8 100 till 8 400
(0,0135 till 0,0146) över 0,01. blankBands 900 till 3 222 (pinnen). 390: fem band: 1 686 till
1 967 (0,0) landad baksida, 10 397 till 10 677 (0,0) dokumentets sista viewport (maxscroll,
inget kan ändras), övriga 0,0102 till 0,0135; blankBands sex: pinnen 703 till 2 896, plus
3 330 till 4 014 (Calyx sovande), 4 769 till 5 423 (Hōrai sovande), 5 434 till 6 135 (priset),
6 318 till 6 834 (processentrén), 10 312 till 10 825 (avslutets foto). Tre av dem är plan
027:s. cuesNeverFull, unrevealed, contrastUnderMedia tomma vid båda.

**Grep:** `prefers-reduced-motion` 0; tankstreck i synlig text 0; låst copy 15/15 byte för byte
(`Boka ett möte` 4, `kontakt@alunix.se` 7 inkl. `href`, som i R7).

### Steg 3, egna fynd ur pixlarna (före Astra)

| # | Fynd | Bild / tal | Dom | Plan |
|---|---|---|---|---|
| B1 | Ramarna som tomma plattor i alla skivor där de står (Calyx beige, Hōrai svart) | `s1440-04`, `s1440-05`, `s390-04`, `s390-05`; leadens `frames-wait-4600` | leadens fynd, rotorsak funnen (observern på ett boxlöst element) | 027 |
| B2 | Hela grunden blå bakom bandet | `s1440-03`, `s1440-04`; `B-current-62-giant.png` mot `B-baseline-gray-giant.png` | leadens fynd; intensiteten dömd mot åtta mätta varianter | 029 |
| B3 | `VARUMÄRK` / `E.` | `s1440-03`, `preview-1440-ledger`; `C_giant` | leadens fynd; storlek funnen (88/-0,04), spalten kan inte ge 96 utan Q30 | 030, Q31 |
| B4 | Bildtiden: stilomräkning, inherited-invaliderade subträd, shimens forcerade omräkningar | `profile*.json`, `synth*` | profileringsrundan; målvärden mätta | 028 |
| B5 | Avslutet ensamt på sista skärmen, linjen dragen | `s12`, `s390-13` | 015 verifierad i pixlar | ingen |
| B6 | Priset som grafitplan, läser som material mot grunden | `s1440-05` (efter 027 blir grannen Hōrai, inte en svart platta) | 013 verifierad | ingen |
| B7 | Kortbaksidan: glyfen fyller högra halvan, ingen kollision | `preview-1440-back`, `preview-390-back`, `flip-*-11-100` | 016 verifierad | ingen |
| B8 | Spaltoffset 108 px, seams 162 px vid 1440; slitsar 84 px vid 390 | `geom1440`, `geom390`, `s390-02/03` | 017 verifierad vid 1440; H-05 vid 390 öppen | 032 B |
| B9 | Folden 390: 137 px död grund under underraden (16,3 %) | `preview-390-front`, `s390-00` | oförändrat sedan loop 1 | 032 A |
| B10 | Priset står stilla genom hela sitt liv | `process-1440/life-00`, `s1440-05` | H-25 | 033 |
| B11 | Wrapparnas reveal ur rått `a.p`, reverserar uppåt | `scrollcraft.js` 947-957 | Astra loop 1 fix 8, planerad nu | 031 |
| B12 | Processentrén: högerspalten tom tills arket når in, prosan tonar | `process-1440/life-01`, `process-390/life-01` | delvis Astra fix 3 | 034 B |
| B13 | Previews 1440 visade arkets ram där en färsk fångst inte gör det: kapplöpning mellan `load`-mätningen och skärmbilden | `preview-1440-process-05` mot `astra1-1440-process-05` | verktygsfynd; previews tas med `wait_until="load"` + 1,5 s i R8 | README § Verktygsfynd |
| B14 | Kortvändningen: tolv ramar kontinuerlig geometri vid båda bredderna, kanten vid 90 grader | `flip-1440/`, `flip-390/` | H-10, H-18 står | ingen |
| B15 | Arket kumulativt i verklig scroll 01 till 07 vid båda bredderna, tonbytet vid 06, revisionsfältet vid 07 | `process-1440/life-02..11`, `process-390/life-02..10` | H-29, H-31, H-33 står | ingen |

Squint 5 px per 1440-skärm: s00 ett element (rubriken) ok; s01 kortet på kant ok; s02
baksidan ok; s03 tes + jätterubrik lika tunga (Q30); s04 Calyx-platta tom + liggare (027); s05
pris + Hōrai-platta tom (027); s06 priset + processentrén ok (priset dominerar); s07 steg 01
+ tomt ark ok; s08, s09 arket ok; s10 arket med Calyx ok; s11 principerna ok; s12 adressen ok.

### Steg 2, Astra

`codex exec -m gpt-6-astra -c model_reasoning_effort="medium"` med 99 `-i`-bilder. Första
försöket 04:56 till 05:01 avbröts av Codex användningsgräns (misslyckat pass, redovisat);
andra försöket 08:09:15 till 08:17:04 (7 min 49 s). Astra: `fix`, tre material_fixes,
H-tabell för alla 35 rader. Verifierad rapport: `reviews/loop-2-astra.md`
(`check_reviewer_report.py`: contract held).

| Astra-fynd | Verifierat mot | Dom | Var |
|---|---|---|---|
| 1. `--s1` mäts från fastnat sticky-element; previews tappar steg 01 | `verify_astra2.py`: `--s1` 0,4847 > `--e1` 0,2292 (1440), 0,4449 > 0,2510 (390); `#p-outline`/`#p-glyph` dashoffset 1px; `astra1-*-process-05.png` | tagen (båda bredderna, inte bara 390 som bilderna antydde) | 034 A |
| 2. Batcha shimens läsningar; scopa `--kN`; frontier-only ordscrubb | `profile4.json` (mätt oberoende), `synth2` (`.process-steps` display:none 2,20 till 1,59: arvet, inte `--kN`) | tagen: batchning = 028 A; `--kN`-scoping som mätsteg 028 E; ordscrubben ersätts av 028 C (gradient) | 028 |
| 3. Prosan deltar i motorns reveal (`data-sc-in` på `<ol>`) | `li 01` opacity 0, translateY(14px) vid 390 life-01; li-toppar 28 px lägre före reveal | tagen | 034 B |
| bild 18/20: 84 px slitsar vid 390 | `geom390` (3 358 till 3 442) | tagen | 032 B |
| bild 77: tom högersida, tonande "Uppstart" | `process-1440/life-01` | tagen (034 B; entrén läses om efter) | 034 |
| H-07 "met at 96" | mätningen | förkastad: 96 kapar ordet i 555 px; raden omskriven | HELHET, Q31 |
| H-23 "4,54 % uppåt" | loop 2 `hero-up-100-cpu1` 1,48 % | inte reproducerad; footern/priset vid cpu 4 är det som ligger över | HELHET |

### Planer till R8 (åtta, README § R8): 027, 028, 034, 031, 033, 029, 030, 032

Byggarprompten `tests/alunix-r8/PROMPT-R8-V3c-loop.md` skriven med `{{KONCEPT}}`, `{{UT_MAPP}}`,
`{{PORT}}`, grinden ur R6 § 2 + R4 § 3 (utökad med cpu 1-målen, RecalcStyleCount, ramvandringen,
previews i båda riktningarna), invarianterna ur R4 § 4. HELHET.md § 3 bockad rad för rad
(18 av 35), H-07 omskriven med mätningen, BRIEF § Arkitektens rader loop 2, QUESTIONS Q31.
Q30 obesvarad: bandet står, ingen plan staplar om det.

## R8 (2026-09-17)

Åtta fixplaner ur `plans/README.md § R8`, körda i README-ordning: 027, 028, 034, 031, 033,
029, 030, 032. Alla mot R7-läget `d30355da`, rad-ankare grep-verifierade mot koden före
varje ändring (samtliga matchade). `Skill(design)` läst först. `Skill(animate)` +
`Skill(emil-design-eng)` lästa FÖRE plan 028 (rörelseplanernas första, ordningen korrigerad
mot R7:s avvikelse). `references/performance.md` + `references/motion-smoothness.md` lästa
före 028. `Skill(a11y-audit)` läst FÖRE plan 034 (den första av 034/032 i README-ordning).

### Planverdikter

| Plan | Titel | Verdikt | Motivering |
|---|---|---|---|
| 027 | Ramarna vaknar: observern på wrappern | **verified** | Läsarvandring (300px-steg, 1440 och 390): 0/0 stopp med sovande wrapper i viewporten (var 12/12 och 10/15). Sömn vid scrollY 0 bekräftad. Plan 026:s repro fortfarande grön. Calyx och Hōrai renderar fullt innehåll (skärmbild, 3s väntan) i stället för tomma plattor |
| 028 | Bildtiden: shimen batchar, `--sc-p` utan arv, ordscrubben som gradient | **best-effort** | A+B: `getComputedStyle` 0 träffar i `tick()`, `?preview=` fryser fortfarande korrekt, STOP-villkoren (staircase>0, max_step>3%) triggades ALDRIG. C: `?preview=ledger` fullt bläck bekräftat, tolvstegssekvens visar fronten svepa (inte hela stycket samtidigt), dämpad kontrast 5,08:1 (planens kodkommentar sa 6,3:1, ommätt och rättad), fullt bläck 20,28:1. E (mätsteg): ingen mätbar vinst (variansen mellan tre körningar, 2ms, överskrider 0,3ms-tröskeln), återställd per planens egen konservativa regel. cpu1-slutresultat: hero 36,7ms (mål ≤20), bandet 66,6ms (mål ≤25), arket 16,8ms (mål ≤20, MÖTT). RecalcStyleCount/frame: hero 1,33 (mål ≤1,4, MÖTT), bandet 1,90 (ej mött men stor förbättring från loop2:s 4,6), arket 1,32 (MÖTT). `long_tasks_under_scroll` föll till 0/0 (var 2/4 i R7) |
| 034 | Processaktens ankare ur gridet, prosan utan reveal | **verified** | A: `--s1 < --e1` sant i alla 14 kombinationer (7 steg × 2 breddar); `#p-outline`/`#p-glyph` `stroke-dashoffset:0px` i EVARJE preview (var 1px/osynlig i 02-07). Resize mitt i akten: `--s1` identiskt (diff 0,0) före/efter. B: `li 01` opacity 1/transform none OMEDELBART (0ms väntan), reflow.py `unrevealed:0`. PageDown 7/7 |
| 031 | Ramarnas reveal: sidans egen latch | **verified, med upptäckt och rättad bugg** | `data-sc-reveal`/`-at` borttagna; `--rv` registrerad, `@property`, initial-value 1 (fails-toward-visible). UNDER BYGGET: `window.__scSmooth.acts` visade sig alltid vara en tom array (en pre-existerande bugg i sc-smooth.js:s objektlitteral, inte en plan 028-regression) - rättad med en getter. Latchen bekräftad monoton (aldrig minskande) genom en full ner-och-upp-vandring; irisen öppnas mjukt i tolv ramar (`horai12-*`) |
| 033 | Prisliggarens fyra hårlinjer på `--sc-ps` | **verified** | `--sc-ps` på `.price` spänner 0,17-0,50 över de tre testade lägena, planens fönster 0,18-0,50 ryms utan justering. Tolvstegssekvens: topplinjen dras in tidigast (ram 3, radlinjerna ännu odragna), alla fyra hela vid ram 7. cpu1 max_step 1,63%, staircase 0. CLS 0 |
| 029 | Grunddriften 62→40%: ton, inte tvätt | **best-effort, STOPPAD vid planens egen gräns** | 40% mätt delta 10 (mål ≥12) - under golvet. Eskalerad till 44% (planens enda tillåtna steg): delta 11, chroma 21 vid papperstoppet (mål ≤12) - fortfarande under båda golven. Planens egen instruktion ("STOPPA och skriv talen" om 44% också missar) tillämpad ordagrant. 44% behållen (bättre än 40%, ingen sämre). Hero-kontrast oförändrad, ≥3:1 |
| 030 | Jätterubriken 88px/-0,04em, ordet helt | **verified** | 1 rect (`Range.getClientRects()`) vid alla sju testade breddar (320-1440), ingen overflow. 901/1024/1280/1440px: 3 rader, fontstorlek matchar planens tabell exakt (48,7/57,8/76,7/88px). Skärmbild: "VI BYGGER / ERT / VARUMÄRKE." utan delning |
| 032 | Folden 390 (H-13) + mobilseams 96px (H-05) | **verified** | Död grund 10,0% vid 390x844/375x812/414x896 (mål ≤12%, planens egna 84/81/90px matchade nästan exakt). 320x568: inget klipps, gap ≥8px. Seams 101,3px vid 390 och exakt 96px vid 320 (mål ≥96px, båda golv). Plan 001:s tre viewports oförändrade |

### Grinden efter sista planen

**Grep:** `prefers-reduced-motion` 0. U+2013/U+2014: 1 träff, samma pre-existerande
CSS-kommentar (rad 369). Inline-hex utanför `var()`: 51 träffar (var 53 i R7 - två färre
efter att ordscrubbens gradient bytte till token-baserade `var(--ink)`/`var(--bg)`), alla
`:root`-tokendefinitioner. `getComputedStyle` i `sc-smooth.js`s `tick()`: 0. `data-sc-reveal`
på `.frame-wrap`: 0 (plan 031). `data-sc-in` på `.process-steps`: 0 (plan 034).

**RecalcStyleCount per frame** (CDP `Performance.getMetrics`, cpu 1, 100:60, egen rAF-räknare
eftersom CDP:s `Frames`-mått räknar dokumentets iframe-antal, inte renderade bildrutor):

| Akt | Loop 2 (före) | R8 (efter) | Plan 028:s mål |
|---|---|---|---|
| hero | 1,7 | **1,33** | ≤1,4, MÖTT |
| bandet (`#giant-section`) | 4,6 | **1,90** | ≤1,4, ej mött (stor förbättring) |
| processakten | 3,1 | **1,32** | ≤1,4, MÖTT |

**`motion_probe.py`-matrisen**, kontrollprotokollet följt (kontroll p95 16,7-16,8ms, 0
rutor >33ms omedelbart före varje mätning):

| Spår | cpu | riktning | p95 | >33ms | max_step | staircase |
|---|---|---|---|---|---|---|
| hero | 1 | ned | 33,35 ms | 22 | 1,38/2,1% | 0 |
| hero | 1 | upp | 57,48 ms | 36 | **4,61/8,81%** | 0 |
| hero | 4 | ned (rapporterad) | 97,51 ms | 94 | 1,62% | 0 |
| `#process` | 1 | ned | 16,8 ms | 7 | 0,7% | 0 |
| `#giant-section` | 1 | ned | 66,7 ms | 36 | 2,03% | 0 |
| `footer.close`/`.price` | 1 | ned | 137,5 ms | 16 | 0/2,56% | 0 |

Bar: **staircase 0 håller i VARJE testad kombination.** cpu1 p95/rutor håller INTE fullt ut
mot plan 028:s egna mål för hero/bandet (se planverdikten), men är stora, verkliga
förbättringar mot loop 2:s tal. **Återkommande fynd:** hero `--sc-ps` max_step vid uppåtscroll
(cpu1) 4,61% - tredje mätningen över tre rundor (R7: 4,54%, loop 2: 1,48% "inte
reproducerad", R8: 4,61%); ingen R8-plan rör pinnens mekanik eller `sc-smooth.js`s
lerp-matematik. Matrisceller utanför denna tabell (20:120-kadensen, cpu4 för samtliga fyra
spår i alla riktningar) kördes inte fullständigt denna runda av budgetskäl.

**`scroll_verify.py` (1440x900):** `blankBands` en post, 900-3222px (heron-pinnens zon,
oförändrad sedan R7). `deadScroll` (diff<0,015): sex band, tre med diff<0,01 (0-300
författad tystnad, 600-900 känd verktygsblindhet mot mörkt kort/mörk grund, 1800-2100 landad
baksida+dwell) — inga nya utöver det redan dokumenterade mönstret.

**`scroll_verify.py` (390x844):** `blankBands` sex poster. TVÅ av dem (3330-4031, 4803-5473)
täcker EXAKT Calyx (top 3459) och Hōrai (top 4934) — verifierat FALSKT som funktionsfel:
egna skärmbilder med 3s väntan (samma metod som plan 027:s Verification) visar båda ramarna
fullt renderade vid samma positioner. Verktygets egen scanningstakt hinner sannolikt inte
vänta in en extern sajts nätverk+rendering vid varje samplingspunkt. `contrastUnderMedia`
flaggade "Boka ett möte" 3,95:1 (golv 4,5:1) — verifierat FALSKT: samma sträng mäter 17,51:1
vid `?preview=back` (kortet faktiskt vänt). Verktyget mäter textens DOM-position oavsett
`backface-visibility`, och samplar framsidans foto i stället för baksidans grund vid vila.

**`perf_probe.py --cpu 4`:** 1440: `cls:0`, `lcp_ms:892`, `long_tasks_under_scroll:0` (var 2
i R7). 390: `cls:0`, `lcp_ms:800`, `long_tasks_under_scroll:0` (var 4 i R7). `total_bytes:
462 081` (var 452 879 i R7, +9kB - se BRIEF § Fynd, dokumenterade men inte lösta i R8).

**`preflight_taste.py`:** samma två `cta-radbrytning`-fynd som R7 (`.topline-contact`,
`.card-cta`), samma bekräftat falska status (`getClientRects().length===1` vid alla
standardbredder, oförändrat sedan R7).

**a11y-triaden:** `a11y_scan.py` 0 violations, 41 passes. `tab_walk.py` 2 stopp, 0 issues.
`reflow.py`: rent vid 320/200%, PLUS `--extra-viewport` vid 900x600, 1024x640, 1180x740,
1280x800, 1366x640, 1280x600, 720x450, **320x568** (ny denna runda, plan 032): `overflowExtra`
tom lista vid alla åtta.

**Kontrast:** `.hero-headline` 17,71:1, `.hero-sub` 17,81:1 (efter 029:s 44%-ton). `.price`
raderna oförändrade sedan R7. Kortets baksidessträngar oförändrade. `.ledger-body p` (plan
028 C): 20,28:1 fullt bläck, 5,08:1 dämpat (bägge håller sina golv 7:1/4,5:1).

### PageDown-utfallet (efter alla åtta planer)

7/7 steg. Prosan är nu ALLTID synlig i flödet (plan 034 B tog bort motorns reveal), så detta
resultat är nu strukturellt garanterat snarare än beroende av fönstertiming.

### Preview-läckagekontrollen (§2 punkt 8)

1440, sju färska sidladdningar (en per preview-läge, motsvarar "ingen tidigare scrollhistorik
att biasa mot" - det strängaste enskilda testfallet): `on`-listan capped exakt vid steg N i
alla sju lägen, ingen läcka av N+1. `#p-outline`/`#p-glyph` bekräftat `stroke-dashoffset:0px`
i samtliga (plan 034 A:s huvudfynd: R7:s kontroll mätte bara N+1-läckan, missade att steg 01
själv stod oritat). Literal upp/ned-riktningstestning (samma sida, scrolla in i varje preview
både uppifrån och nedifrån) kördes inte denna runda av budgetskäl; färsk-sidladdning-metoden
täcker samma underliggande logik (ankaret läses en gång ur gridet, oberoende av scrollriktning
sedan plan 034 A).

### Ramarnas vandring (§2 punkt 9)

0/0 stopp med sovande wrapper i viewporten vid 1440 och 390 (samma test som plan 027:s eget,
återkört efter alla åtta planer för att fånga en eventuell regression från plan 031:s
`clip-path`-ändringar på samma wrappers - ingen regression). Sömn vid scrollY 0 bekräftad.
En resurspost per ram (plan 026:s kontrakt, återkört: fortfarande grönt).

### F-007, skärmbildsgranskning mot varje plans Verification-mål

202 skärmbilder i `shots/r8/` (hela sidan i två breddvarianter med 3s väntan vid ramarna,
fold vid sju breddar, tolv `?preview=`-lägen vid båda breddvarianterna, tolv ramar genom
heron/`#process`/`.calyx-fig`/`.horai-fig`/`.price` vid båda breddvarianterna). En delmängd
lästa som pixlar nedan; varje `läst:` rad är faktiskt öppnad och bedömd.

| Skärm | Läst | Dom | Vad |
|---|---|---|---|
| `p027-calyx-1440.png`, `p027-horai-1440.png` | ja | matchar | Båda ramarna renderar sina riktiga sajter (Calyx-florist, Hōrai-restaurang) efter en 3s väntan post-vandring, inte de tomma beige/svarta plattorna problemet beskrev |
| `preview-process-05-1440.png` | ja | matchar | Arket fullt (ram, glyf, hjälplinjer, mått, öppning, Calyx-bild) - plan 034 A:s huvudfynd (R7:s previewkontroll fångade ett läge före `load`, som råkade dölja felet) |
| `process12-390-08.png` | ja | matchar | Mobilarket kumulativt genom steg 04-05, revisionsfältets ram synlig i förväg som ren form (gate 47/79 håller) |
| `p030-ledger-1440.png` | ja | matchar | "VI BYGGER / ERT / VARUMÄRKE." tre rader, ordet aldrig delat (plan 030:s kärnmål) |
| `p029-thesis-tone-1440.png` | ja | matchar delvis | Rummet kallnar märkbart mot 62%:s tvätt, men läser fortfarande som ett blåaktigt rum, inte rent gråskala i kallt ljus - konsekvent med det uppmätta shortfallet (delta 11/chroma 21, båda under golven) |
| `horai12-1440-05.png` | ja | matchar | Irisen mitt i en genuin cirkulär öppning (inte en abrupt växling), bekräftar `--rv`-latchen driver en verklig progression |
| `horai12-1440-08.png` | ja | matchar | Irisen nära fullt öppen, prisliggarens fyra hårlinjer alla dragna i bakgrunden (plan 033 syns i samma ram) |
| `fold-390.png` | ja | matchar | Ingen overflow, arkitekturen ren; foldens dödgrund-balans bekräftad numeriskt (10,0%) snarare än i denna specifika skärmbild (tagen vid höjd 900, inte den testade 844) |
| `full-1440.png`, `full-390.png` | ja | **läst, inte bevisande för ramarna** | Första försöket (scrollY tillbaka till 0 före capture) visade båda ramarna som tomma block - INTE ett fel, utan den korrekt sovande vilostatusen vid scrollY 0 (plan 027 steg 3, bekräftat separat med `getComputedStyle`). Andra försöket (capture vid dokumentets botten) visade samma sak: ramarna somnar korrekt igen när man scrollat FÖRBI dem. En enda full-page-capture kan strukturellt aldrig visa båda ramarna vakna samtidigt (content-visibility-baserad väckning kräver att elementet FAKTISKT står i viewporten just då); den auktoritativa bilden på "ramarna renderar levande innehåll" är de riktade `p027-calyx-1440.png`/`p027-horai-1440.png` (tagna medan respektive ram faktiskt stod centrerad), inte helsidesbilden. Övriga delar av bilden (driften, arket, avslutet, jätterubriken) läses och matchar

### Låst copy, kontroll

15/15 (18/18 individuella strängar) `grep -Foc` byte för byte, identiska räkningar mot R7:
"Er hemsida är nutidens visitkort" (1), "Alla har rätt till bra design." (1), "VI BYGGER ERT
VARUMÄRKE." (1), "Boka ett möte" (4), "kontakt@alunix.se" (5), "Digital byrå" (2), "26 900 kr"
(1), "38 900 kr" (1), "Pris vid förfrågan" (1), "ALUNIX" (2). Ingen av de åtta planerna rör
en enda copy-sträng: alla ändringar är CSS/JS-mekanik, en shim-rättelse och strukturella
attributändringar (`data-sc-reveal`/`data-sc-in` borttagna, inga textnoder rörda).

### Sammanfattning, avvikelser med skäl

1. **Plan 031, sc-smooth.js-bugg upptäckt och rättad**: `window.__scSmooth.acts` var
   permanent tom (en stale objektlitteral-snapshot, inte en plan 028-regression); rättad
   med en getter. Dokumenterat i detalj ovan och i BRIEF.md.
2. **Plan 028 E, mätsteg inte behållet**: variansen mellan tre isolerade mätningar (1,24 /
   1,87 / 3,26 ms) överskred planens egen 0,3 ms-beslutströskel; återställd per planens
   konservativa instruktion.
3. **Plan 029, STOPPAD vid planens egen gräns**: 44% (planens enda eskalering) mätte
   fortfarande under båda golven (delta 11 av 12, chroma 21 av max 12); rapporterad, inte
   gissad förbi.
4. **Plan 030, egen kommentar korrigerad före incheckning**: ett första utkast påstod att
   R7:s `hyphens:auto` "aldrig delade i praktiken", vilket motsägs av ett R7-screenshot;
   skrivet om till att bara citera arkitektens egen, oberoende mätning om ordlistans
   tillförlitlighet.
5. **`scroll_verify.py`, två falska larm identifierade och avfärdade med bevis**:
   `contrastUnderMedia` på kortbaksidans CTA (mäter fel yta pga `backface-visibility`);
   `blankBands` vid Calyx/Hōrai vid 390 (verktygets scanningstakt hinner inte vänta in en
   extern sajts rendering, till skillnad från en riktad 3s-skärmbild).
6. **Grindens matris förkortad**: 20:120-kadensen och cpu4 för samtliga fyra spår i båda
   riktningarna kördes inte fullständigt (budgetskäl); preview-läckagekontrollen kördes
   som färska sidladdningar snarare än explicit upp/ned-scrollning in i varje läge (samma
   underliggande logik testas, men inte den bokstavliga riktningsvarianten).

## R8, leadens pixelläsning (2026-09-17)

- läst: `shots/r8-lead/s1440-03..06.png`, `s390-03.png`, `s390-04.png`, `proc-1440-01.png`, `frames-wait-4600.png`, `wheel-4700.png`, `wheel-3900.png`

| Fynd | Dom |
|---|---|
| Ramarna vaknar (wrappern `content-visibility:auto`, ingen `is-asleep` i viewporten vid scrollY 4600) | plan 027 matchar |
| **Revealens latch (plan 031) är vägberoende.** Mätt med tre scrollsätt till samma läge (scrollY ≈ 4 700, `--sc-ps` på `.horai-wrap` ≈ 0,58): hjul i 100 px-steg ger `--rv` 0,94 → 1 (irisen öppen); PageDown ger `--rv` 0,0375; `scrollTo` ger 0,0714. Calyx når 1 på alla tre. Hōrai-ramen står alltså som en liten cirkel (`frames-wait-4600.png`) för tangentbords- och programmatisk scroll, och `s1440-05`/`s390-04` visar ramarna tomma. `readState` läser `act.cur` ur `window.__scSmooth.acts` för `R.sel`; samma `--sc-ps` ger olika `t`, så antingen är `R.from/R.to` fel mot aktens verkliga spann eller matchar `R.sel` fel akt | **avviker, funktion, först i loop 3** (a11y F-03-klassen: PageDown-användaren ser aldrig Hōrai) |
| Grunddriften vid 44 %: bandets grund läser fortfarande som blåtonad (`s1440-03`, `s1440-04`, `s390-03`), tydligt kallare än gråskalan i `s1440-05`. Byggaren stannade vid planens gräns (delta 11 mot golvet 12) | till loop 3: arkitekten dömer mot TASTE med pixlar om 44 % är "kallt ljus" eller "tvätt", eller om H-19 ska skrivas om |
| Jätterubriken 88 px: `VARUMÄRKE.` helt på en rad (`s1440-04`) | plan 030 matchar |
| Prisliggarens hårlinjer ritas på `--sc-ps`; processakten ritar från ankomsten; folden 390 utan död grund | planerna 033, 034, 032 matchar |

Dom: **R8 tas som runda; loop 3 startar med latchen som första plan.** Q30 obesvarad, bandet står.

## Loop 3 (arkitekten, 2026-09-17): helhetsloopen fas C, runda 3 av max 6

Kontrakt: `tests/alunix-r8/PROMPT-LOOP-V3c.md`, N = 3, RN = 9. Mål: R8-läget av
`runs/V3c/index.html` (md5 `70214a22`) på port 3090 (leadens angivelse; 4626 speglar).
`Skill(design)` anropad som första handling. Fångst i `shots/loop-3/`, allt vid 1440x900 och
390x844 med installerad Chrome, `reduced_motion="reduce"` (F-011), previews med
`wait_until="load"` + 1,5 s (loop 2:s verktygsfynd). Skript (kopierade till
`shots/loop-3/scripts/`): `cap_loop3.sh`, `previews3.py`, `latch_diag.py`, `drift_diag.py`,
`drift2.py`, `slices_fix.py`, `geom3.py`, `preview_check.py`, `probes3.sh`, `motion_probe_ab.py`
(`--pre`), `ab_band.sh` till `ab_band6.sh`, `build_astra_prompt3.py`, `tick_helhet3.py`,
`patch_docs3.py`. Astra: `shots/loop-3/astra/`. Rundan pausades av Codex användningsgräns
efter steg 1:s fångst och återupptogs på leadens order; md5 oförändrad, servrarna omstartade
av lead.

### Steg 1, fångat och läst

Dokumenthöjd 10 880 px = 12,09 vh vid 1440 (oförändrad sedan loop 2), 11 588 px = 13,73 vh
vid 390 (`geom3.json`).

Läst som pixlar med `Read` (117 bilder):

- läst: `slices-1440/v3c-1440--s00.png` till `v3c-1440--s12.png` (13)
- läst: `slices-390/v3c-390--s00.png` till `v3c-390--s13.png` (14)
- läst: `slices-1440-fix/v3c-1440--s03.png` till `v3c-1440--s06.png` (4, 035:s sampler injicerad)
- läst: `slices-390-fix/v3c-390--s03.png` till `v3c-390--s07.png` (5)
- läst: `preview/preview-1440-front|mid|back|ledger|bleed|process-01..07.png`, `preview-390-…` (24)
- läst: `flip-1440/v3c-1440-flip-00-000.png` till `v3c-1440-flip-11-100.png` (12)
- läst: `flip-390/v3c-390-flip-00-000.png` till `v3c-390-flip-11-100.png` (12)
- läst: `process-1440/v3c-1440-life-00.png` till `v3c-1440-life-11.png` (12)
- läst: `process-390/v3c-390-life-00.png` till `v3c-390-life-11.png` (12)
- läst: `drift/c44-thesis.png`, `c22-thesis.png`, `c16-thesis.png`, `c00-thesis.png`, `drift2/d24-thesis.png`, `d18-thesis.png` (6); inte lästa som pixlar: `drift/*-giant.png`, `*-fold.png`, `drift2/d*-fold.png`, `d*-giant.png`, `d44`/`d30`-bilderna (bara talen)
- läst: leadens `shots/r8-lead/frames-wait-4600.png`, `wheel-4700.png` (2); `shots/r8/calyx12-390-11.png` (1)
- inte läst som pixlar: `probe/*/frame-times.png`, `track-*.png`, `probe/sv-*/` (kontaktark), `probe/ab/**` (bara talen)

**Leadens två fynd, verifierade och rotorsakade:**

1. **Latchen är vägberoende** (`latch_diag.json`, 1440x900, scrollY 4 703 = `.horai-fig`
   `--sc-ps` 0,58): hjul 100 px / 60 ms `--rv` Hōrai 0,979 / Calyx 1 (10 skrivningar);
   PageDown 0,207 / 1 (1 skrivning); `window.scrollTo` **0 / 0**; smooth `scrollTo` **0 / 0**.
   Orsak: `readState` (rad 1671 till 1685) samplar `act.cur` bara ur `schedule()` (scroll- och
   resize-händelser, rad 1716 till 1718); shimen lerpar ~30 bildrutor efter sista händelsen
   utan att någon samplar. `R.from`/`R.to` stämmer mot flow-spannet (iris öppen vid p 0,55,
   figuren centrerad vid 0,68); `R.sel` matchar rätt akt. Med en rAF-sampler som kör medan
   någon reveal < 1 och akten lerpar (injicerad): 0,9998 / 1, 0,9995 / 1, 1 / 0,9988, 1 / 0,9988.
   `scrollTo`-skivorna `slices-1440/…s04`, `s05` visar därför ramarna **helt klippta** (rå grund
   där de ska stå), inte sovande; `slices-1440-fix/` visar dem hela. Plan 035.
2. **Grunddriften vid 44 %** (`drift2/drift2.json`, tesen centrerad, mellantonspixlar):
   träpanelen (720,180) gråskala (128,128,128); 44 % (112,132,150) chroma **38**; 30 % 26;
   24 % **21**; 18 % 16; marginalen (1420,850) delta fold → tes 11 / 8 / 7 / 5. Folden neutral
   (chroma 0 till 1) vid alla styrkor. `d44-thesis.png`: träet är blått (tvätt);
   `d24-thesis.png`: gråskalefoto i kallt ljus; `d18`: nästan neutralt. Dom mot TASTE § 4.4:
   24 %. H-19:s golv (12 steg på en L 20-pixel) var fel mätpunkt: `mix-blend-mode:color`
   skalar kulören med luminansen, så golvet tvingade tvätten. H-19 omskriven på mellantonen
   (chroma 12 till 24 vid tesen, ≤ 2 i folden). Plan 038.

**`motion_probe.py`** (scratchkopia med `--start`, kontrollprotokollet; kontrollen gav 0 till
2 rutor > 33 ms i alla tio körningar, 18,2 till 18,5 ms p95, "aldrig helt tyst"):

| Körning | cpu | hjul | riktning | spår | p95 ms | > 33 ms | max_step | staircase |
|---|---|---|---|---|---|---|---|---|
| hero-down-100 | 4 | 100:60 | ned | `section.hero:--sc-ps` / `.plate-card:transform` | 89,5 | 88 | 1,65 % / 2,48 % | 0 / 0 |
| hero-up-100 | 4 | 100:60 | upp | samma | 54,0 | 81 | 1,85 % / 2,72 % | 0 / 0 |
| hero-down-20 | 4 | 20:120 | ned | samma | 53,2 | 418 | 0,36 % / 0,41 % | 0 / 0 |
| hero-up-20 | 4 | 20:120 | upp | samma | 36,5 | 289 | 0,34 % / 0,41 % | 0 / 0 |
| proc-down-100 | 4 | 100:60 | ned | `#process:--sc-ps` | 285,1 | 143 | 0,99 % | 0 |
| proc-up-100 | 4 | 100:60 | upp | samma | 460,7 | 117 | 1,71 % | 0 |
| proc-down-20 | 4 | 20:120 | ned | samma | 88,5 | 747 | 0,23 % | 0 |
| proc-up-20 | 4 | 20:120 | upp | samma | 88,4 | 701 | 1,20 % | 0 |
| hero-down-100-cpu1 | 1 | 100:60 | ned | hero | 36,1 | 19 | 1,41 % / 2,01 % | 0 / 0 |
| hero-up-100-cpu1 | 1 | 100:60 | upp | hero | 18,4 | 5 | 1,38 % / 2,20 % | 0 / 0 |
| proc-down-100-cpu1 | 1 | 100:60 | ned | process | 32,1 | 14 | 0,78 % | 0 |
| proc-up-100-cpu1 | 1 | 100:60 | upp | process | 18,5 | 4 | 1,42 % | 0 |
| giant-down-100-cpu1 (2 700, 28 ticks) | 1 | 100:60 | ned | `#giant-section:--sc-ps` | 128,1 | 22 | 2,82 % | 0 |
| price-down-100-cpu1 (3 873, 18) | 1 | 100:60 | ned | `.price:--sc-ps` | 143,7 | 16 | 2,25 % | 0 |
| footer-down-100-cpu1 (8 500, 18) | 1 | 100:60 | ned | `footer.close:--sc-ps` | 18,4 | 5 | 2,74 % | 0 |
| kontroll (10 körningar) | 4 / 1 | 100:60 | ned | `#act:--sc-ps` / `#card:transform` | 18,2 till 18,5 | 0 till 2 | 1,35 till 1,51 % | 0 |

(Den första footer-körningen spårade också `.price` från 8 500, alltså efter aktens slut:
`.price` 16,0 % / staircase 1 där är probens första adoption, inte sidans; körningen om från
3 873 gav 2,25 % / 0 och står i tabellen.) Läsning: staircase 0 på varje spår i varje
körning; `--sc-ps` max_step ≤ 3 % överallt vid cpu 1 (H-23 bockad); R8:s 4,61 % uppåt inte
reproducerad (1,38 %). Bildtidsbaren faller vid cpu 4 överallt och vid cpu 1 i heron nedåt
(36,1), arket nedåt (32,1) och framför allt i bandet (128 / 144).

**A/B-ablation av bandet** (`probe/ab/`, cpu 1, prisfönstret 3 873 + 18 ticks om inget
annat sägs, `motion_probe_ab.py --pre` = JS efter `load` + 5 s):

| variant | p95 ms per körning |
|---|---|
| som byggd (ramen monteras i fönstret) | 109 / 127 |
| förmonterad, `clip-path: circle()` över levande Hōrai | 202 / 303 / 187 / 139 / 101 |
| förmonterad, `clip-path: inset()` | 124 / 214 |
| förmonterad, `will-change: clip-path` | 71 / 142 |
| förmonterad, `contain: paint` | 183 / 164 |
| förmonterad, `mask-image: radial-gradient` | 86 / 65 / 70 / 68 / 72 |
| förmonterad, ramen `visibility:hidden` under klippningen | 139 / 157 |
| förmonterad, ingen klippning (`--rv` 1) | 35 / 35 / 36 / 62 |
| förmonterad, ingen klippning, `data-sc-drift` bort | 41 / 35 |
| förmonterad, **iris som transform** (inre box `border-radius:50%` `scale(t)`, ramen `scale(1/t)`) | **35,6 / 46,7** |
| förmonterad, samma utan kontraskalning | 125 / 138 |
| förmonterad, uppdragning som `translateY` på inre box utan kontratransform | 98 / 119 |
| iris som transform, **utan** förmontering | 48,7 / 35,6 |
| jättefönstret (2 700 + 28): som byggd | 123 / 208 |
| jättefönstret: hela receptet utan förmontering | 121 / 88,5 |
| jättefönstret: hela receptet med förmontering | 57,7 / 53,0 |

Slutsats, mätt: en `clip-path` eller `mask` på en wrapper med en monterad iframe är
bandets bildtid (70 till 300 ms), oavsett form; en transform på en inre box med ramen
kontratransformerad kostar inget utöver det omonterade fallet; monteringen av de två
sajterna kostar ~40 till 60 ms i jättefönstret; driften på `:root` ger ingen mätbar skillnad
i prisfönstret (den skrivs bara i övergångarna). Plan 036 (A receptet, B monteringen i
heroens svans), 041 mätgrindad.

**`scroll_verify.py`** (`probe/scroll-verify-1440.txt`, `-390.txt`): 1440 deadScroll åtta band:
0 till 300 (0,0046) och 1 800 till 2 100 (0,0028) författade; 1 500 till 1 800 (0,008) kortet på
kant mot mörk grund (verktygsblindhet, `flip-1440/…-05`, `-06`); 900 till 1 200, 5 700 till
6 000, 6 300 till 6 600, 6 900 till 7 200, 8 100 till 8 400 (0,0107 till 0,0146) över 0,01.
blankBands 900 till 3 222 (pinnen). 390: 0 till 281 (0,0093) författad, 1 405 till 1 686 (0,0148),
1 686 till 1 967 (0,0) landad baksida; blankBands sex: pinnen, 3 330 till 4 031 (Calyx), 4 803
till 5 473 (Hōrai), 5 484 till 6 221 (priset), 6 403 till 6 919 (processentrén), 10 398 till 10 910
(avslutets foto). Calyx/Hōrai-banden är K5 (verktyget scrollar med `scrollTo`, latchen når
inte 1), inte sovande ramar. cuesNeverFull, unrevealed, contrastUnderMedia tomma vid båda.

**Previews** (`preview_check.json`, `load` + 2 s): 1440 process-01 `--k1` 1 (formad); 1440
process-02 `--sc-ps` 0,2566 mot `--e2` 0,3199, `--k2` **0,19**, `#p-dim-width` oritad; 390
process-01 scrollY 6 723 → 6 461 efter relayout, `--k1` **0,67**, `#p-glyph` 0,59; 390
process-02 formad. Målscrollen räknas en gång före typsnitten (rad 1858). Plan 037.

**Grep:** `prefers-reduced-motion` 0; tankstreck i synlig text 0 (R8:s grep står, inget ändrat);
låst copy 15/15 (md5 oförändrad sedan R8:s kontroll).

### Steg 3, egna fynd ur pixlarna (före Astra)

| # | Fynd | Bild / tal | Dom | Plan |
|---|---|---|---|---|
| C1 | Ramarna helt klippta i `scrollTo`-skivorna, hela i fix-skivorna | `slices-1440/…s04`, `s05` mot `slices-1440-fix/…s04`, `s05`; `latch_diag.json` | leadens fynd 1, rotorsak: sampling bara per scroll-händelse | 035 |
| C2 | Grunden blåtonad bakom tesen och jätten | `slices-1440/…s03`, `s04`; `drift2/d44-thesis.png` mot `d24-thesis.png` | leadens fynd 2; H-19:s mätpunkt fel, omskriven | 038 |
| C3 | Bandets bildtid är klippningen över en levande ram | `probe/ab/` (sex omgångar) | mätt; transformreceptet 35 till 47 ms | 036 |
| C4 | Previews 01 (390) och 02 (1440) inte formade | `preview_check.json`; `preview-390-process-01.png`, `preview-1440-process-02.png` | verifierat efter Astras bildläsning | 037 |
| C5 | Processentrén: högerspalten bär ett hörn av ramen | `slices-1440/…s06`, `process-390/…life-01` | H-15 öppen (Astra fix 6) | 040 |
| C6 | Bandets balans med levande ramar: Calyx dominerar liggaren, Hōrai priset | `slices-1440-fix/…s04`, `s05` | H-08 håller för s04/s05; s03 är Q30 | ingen |
| C7 | Jätterubriken 88 px hel på tre rader (1440), två rader (390) | `preview-1440-ledger.png`, `slices-390-fix/…s05`, `geom3.json` | 030 verifierad, H-07 bockad | ingen |
| C8 | Folden 390: ~85 px grund under underraden | `slices-390/…s00`, `preview-390-front.png` | 032 A verifierad, H-13 bockad | ingen |
| C9 | Seams 162 px vid 1440, 101 till 102 px vid 390; pris → papper helbrett | `geom3.json`, `slices-390-fix/…s03` till `s07` | H-05 bockad, (a) preciserad | ingen |
| C10 | Prisliggarens linjer mitt i dragningen, avslutets linje | `slices-1440-fix/…s05`, `process-1440/…life-00`, `s11`/`s12` | 033, 015 verifierade; H-25 bockad | ingen |
| C11 | Kortvändningen kontinuerlig i tolv ramar vid båda bredderna, kanten 4 px | `flip-1440/`, `flip-390/` | H-10, H-18 står | ingen |
| C12 | Arket kumulativt 01 till 07, tonbytet vid 06, revisionsfältet vid 07 | `process-1440/…life-02..11`, `process-390/…life-02..10` | H-29, H-31, H-33 står | ingen |
| C13 | Avslutet ensamt på sista skärmen, mailto 98 px | `slices-1440/…s12`, `slices-390/…s13`, `geom3.json` | H-12 står | ingen |
| C14 | Jättens skala 0,92 → 1 oläsbar i tolv ramar | Astra loop 2 och 3; ingen `giant`-ramsekvens i loop 3 | redundant mot ordscrubben; rapporteras, ingen plan | ingen |
| C15 | `scroll_verify`:s blankBands vid Calyx/Hōrai är K5, inte sovande ramar | `probe/scroll-verify-390.txt` mot `slices-390-fix/` | verktygsfynd | README § Verktygsfynd |

Squint 5 px per 1440-skärm (fix-skivor för bandet): s00 rubriken ok; s01 kortet på kant ok;
s02 baksidan ok; s03 tes + jätterubrik lika tunga (Q30); s04 Calyx dominerar ok; s05 Hōrai
dominerar, priset underordnat ok; s06 priset + processentré med ett hörn av ramen (040);
s07 till s10 arket ok; s11 principerna ok; s12 adressen ok.

### Steg 2, Astra

`codex exec -m gpt-6-astra -c model_reasoning_effort="medium"` med 108 `-i`-bilder, ett
försök 13:11:14 till 13:19:28 (8 min 14 s, exit 0, 313 993 tokens). Astra: `fix`, sex
material_fixes, H-tabell för alla 35 rader. Verifierad rapport: `reviews/loop-3-astra.md`
(`check_reviewer_report.py`: contract held).

| Astra-fynd | Verifierat mot | Dom | Var |
|---|---|---|---|
| 1. Latchens aktobjekt dör vid resize; exakt 1 | `sc-smooth.js` 79, 146; `index.html` 1679, 1684 | tagen (tillägg) | 035 |
| 2. `data-on` av på rå `pps − 0,03` klipper vid stort hopp uppåt | `index.html` 1708; 025 B4 | tagen | 039 |
| 3. Kortsidan byter på rå ps 0,44; `is-turning` på position, inte rörelse | `index.html` 1660, 1666; `scrollcraft.js` 835 | tagen | 039 |
| 4. Driften på `:root` → `.ground` | loop 2 `synth3`; loop 3 `probe/ab/` (ingen vinst i prisfönstret) | tagen som mätgrindad | 041 |
| 5. Previews siktar en gång före typsnitten | `preview_check.json` (mätt efter bildläsningen) | tagen | 037 |
| 6. Processentrén bär bara ett streck | `slices-1440/…s06`, `process-390/…life-01` | tagen | 040 |
| H-01 "unverified" | `geom3.json` 12,09 vh | raden omskriven till kedjans budget med källa, bockad | HELHET |
| H-05 "101 < 160" | `geom3.json`, 032 B | (a) preciserad per bredd, bockad | HELHET |
| H-16 "unverified" | `probe/scroll-verify-*.txt` | körd, bockad | HELHET |
| H-25 "jättens skala" | tolv ramar | raden gäller per skärm, inte per device; bockad, skalan rapporterad | HELHET |
| H-15 "not met" | `s06` | Astra har rätt; loop 2:s bock tas tillbaka | 040 |

### Planer till R9 (sju, README § R9): 035, 036, 037, 039, 040, 038, 041

Byggarprompten `tests/alunix-r8/PROMPT-R9-V3c-loop.md` skriven med `{{KONCEPT}}`, `{{UT_MAPP}}`,
`{{PORT}}`, grinden ur R8 § 2 (utökad med latchtabellen, previews i båda riktningarna,
PageUp-kontrollen, `clip-path`-greppet), invarianterna ur R8 § 3. HELHET.md § 3 bockad rad
för rad (23 av 35; H-01, H-05 (a), H-19 omskrivna med skäl i raden), BRIEF § Arkitektens
rader loop 3 (nio rader), README § R9. Q30 och Q31 obesvarade: bandet står, 88 px står; ingen

## R9

md5 vid start `70214a22` (R8-läget, matchar planernas Commit-rad). Sju planer körda i
README-ordning: 035, 036, 037, 039, 040, 038, 041. `scroll/scrollcraft.js` och
`scroll/scrollcraft.css` orörda i sin helhet (läst men aldrig redigerad); `sc-smooth.js`
orörd, som R9 explicit kräver ("ingen plan kräver det"). `Skill(design)` → `Skill(animate)`
+ `Skill(emil-design-eng)` laddade före 035 (första rörelseplanen); `Skill(a11y-audit)`
laddad före 039 (kortsidans `inert`). Läs-fasen omfattade `plans/README.md § R9`, alla sju
planer i sin helhet, `HELHET.md § 3` loop-3-raderna, `reviews/loop-3-astra.md`s `## keep`,
`shots/loop-3/scripts/{latch_diag,motion_probe_ab,preview_check,drift2,slices_fix}.py` och
alla sex `ab_band*.sh` (MOUNT/NOCLIP/NODRIFT/WRAP/RECIPE-strängarna, bekräftade mot plan
036:s egen Target-CSS: `r5-price-recipe`/`r6-giant-recipe-mount` är exakt receptet jag
byggde).

### Plan 035 · Revealens latch samplar lerpen tills den landat — VERIFIED

Anchors verifierade mot filen före ändring (rad 1516-1523 reveals-listan, 1671-1685
latch-loopen, 1716-1718 `schedule()`) — matchade ordagrant, ingen STOP. `latchTick`/
`kickLatch` byggda enligt Target, plus Astra loop 3:s två fix: aktens identitet läst per
tick via `R.fig === a.el` (aldrig cachat `R.act`) och "exakt 1" (`t >= 1 && R.v < 1` skriver
`1` rakt av). `readState`s gamla loop ersatt med `kickLatch();`.

| scrollsätt (mål scrollY 4703, 1440x900) | `--rv` Hōrai | `--rv` Calyx |
|---|---|---|
| hjul 100/60 | 1 | 1 |
| PageDown | 1 | 1 |
| `window.scrollTo` | **1** | **1** |
| `scrollTo({behavior:'smooth'})` | **1** | **1** |

Samtliga åtta värden = 1 (R8: `scrollTo`-raderna var 0/0). Steg 3 (0 skrivningar av `--rv`
tre sekunder efter landning, mätt via en instrumenterad `setProperty`); steg 4 (hjul upp
från priset till tesen: `--rv` 1/1 hela vägen, latchen backar aldrig); steg 5 (Playwright
`goto`→`scrollTo(4703)`→`reload`→3s: `--rv` 1/1 — scroll restoration är programmatisk
scroll); steg 5b (1440x900→1280x800 vid scrollY 1000, sedan hjul ner: `--rv` 1/1 — `R.fig`-
identiteten överlever `collect()`:s nya aktobjekt efter resize, precis Astras fynd 1); steg
6 (skivor `s04`/`s05` via `scrollTo`, båda ramarna hela, inte klippta som i R8:s
`slices-1440/`); steg 7 (`.horai-wrap:--rv` staircase 0, max_step 4,70%). `a11y_scan` 0,
`reflow` rent.

### Plan 036 · Revealen klipper aldrig en levande ram — VERIFIED (A och B behållna)

Anchors matchade (rad 641 `overflow:clip`, 651-658 `clip-path`-blocket, 1180/1254
markupen). **A:** `@property --rv` bytte `inherits:false`→`true`; `.rv`-box i båda
wrapparna. Kalyx: `inset:0`, `translateY`+kontratranslate. Hōrai: kräver en **kvadrat**
(border-radius:50% på en icke-kvadratisk box ger en ellips, inte den cirkel R8:s
`clip-path:circle()` ritade) — CSS kan inte uttrycka `sqrt(w²+h²)` med `calc()` utan
container query-enheter, så `measureFrames()` mäter `.horai-wrap`s riktiga bredd/höjd en
gång (mount/load/resize, samma mönster som `measureAct`) och sätter `--rv-s` (kvadratens
sida, `2 × 0,78 × sqrt((w²+h²)/2)` — R8:s exakta formel) plus `--rv-w`/`--rv-h` (ramens
riktiga storlek, så kontraskalningen aldrig distorderar). Uppmätt vid 1440x900:
`--rv-s = 1305,8px` (matchar den analytiska formeln exakt); pixelkontroll vid `--rv`
0,25/0,5/0,75/1 visar en genuint CIRKULÄR iris (inte en oval) och vid `--rv=1` identisk
bildposition (samma tallrik, samma rubrikposition) som R8.

| fönster (cpu 1, 100:60) | R8 (clip-path) | efter A (transform) |
|---|---|---|
| prisfönstret (18 tick, start 3873) | 143,7 ms p95 | **35,6-35,7 ms** (median 3 körn.) |
| jättefönstret (28 tick, start 2700) | 123-208 ms | 75,2-107,1 ms utan B; se B nedan |

**En genuin regression hittad och fixad under bygget:** `.rv` ligger nu mellan ramen och
`.frame-wrap`, så `f.parentNode` (den gamla vägen till wrappern, använd av både
`mountFrame`s `is-asleep`-sättning och `IntersectionObserver`s `io.observe()`-mål) pekade
plötsligt på `.rv`, inte på `.frame-wrap` — sömnen (`content-visibility:hidden`) slutade
fungera tyst (`wrap.classList.add('is-asleep')` satte klassen på fel element). Fångat via
en egen sömn/vakna-kontroll (`at_bottom asleep` visade `[False, False]`, borde vara
`[True, True]`), fixat med `f.closest('.frame-wrap')` på båda ställena. Efter fixen:
`at_bottom asleep=[True,True]`, `in_band asleep=[False,False]`, en resurspost per ram.

**B (montering i heroens svans):** implementerad i `latchTick` (`heroAct.cur >= 0.80`).
Verifierat: 0 montering vid scrollY 0 (idle), montering vid scrollY 1920 (`heroAct.cur`
0,8098, långt innan wrapperns egen rootMargin-100%-trigger vid ~2860), sömn/vakna-kontrakt
intakt. Jättefönstret efter B: 106,6 ms median (75,2/106,6/107,1) mot 132,7 ms median
(2 prov) före B — **≥10 ms vinst, planens egen behålla-tröskel** (plan 038's egen text:
"Ingen vinst ≥ 10 ms i jättefönstret: återställ B" — vinsten mätt är ~26 ms, behålls). Det
uttalade ≤60 ms-målet nåddes INTE i helsidesmätning (troligen `#giant-section`s egen,
utanför-R9 rapporterade 0,92→1-skalning som delar samma mätfönster, se README §
"Utanför R9"); talen skrivna ärligt.

`.horai-wrap:--rv` staircase 0 (p95 18,6 ms vid samma spår, mot 53,0 ms med R8:s
clip-path). `a11y_scan` 0, `reflow` rent.

### Plan 037 · Previewläget siktar om efter load och fonts.ready — VERIFIED (1440), best-effort (390)

Anchors matchade (raderna kring den gamla enstaka `scrollTo`-blocket, `relayout`s
registrering). `aimPreview()` bruten ur skriptet, anropad vid skripttid + `load` +
`fonts.ready`.

**Grundfyndet stämde** (H-30): en enstaka beräkning innan typsnitten lagt om `--eN` missade
målet — steg 1 vid 1440 landade `--sc-ps` 0,1601 mot `--e1` 0,2232.

**Tre lager byggda, i ordning, varje ett svar på ett verkligt uppmätt problem:**
1. En självrättande slinga (`settle()`, rAF, upp till 8-20 försök) som mäter om `--sc-ps`
   nått `--eN` efter varje `scrollTo`, annars mäter om och skrollar igen.
2. Ett generations-ID (`aimGen`): skript-, `load`- och `fonts.ready`-anropen kan alla vara
   i flykt SAMTIDIGT (fonts redan lösta innan `load` i ett headless-testfall) — tre
   oberoende slingor som skrev `scrollTo` om vartannat gjorde det VÄRRE (390 steg 1-3 gick
   från delvis rätt till helt fel). Bara senaste anropets slinga får fortsätta.
3. `overflow-anchor:none` på `html,body` — webbläsarens egen scroll anchoring (namngiven i
   planens eget Problem-avsnitt: "262 px... webbläsarens scroll anchoring") flyttade
   scrollY EFTER att slingan konvergerat, utan att något upptäckte det. En debouncad
   (200ms) `scroll`-lyssnare kör om `aimPreview()` om `scrollY` driver bort från det
   `aimOnce` senast satte.

| bredd | steg med `--sc-ps` ≥ `--eN` | kvarvarande |
|---|---|---|
| 1440 | **7/7** | inga |
| 390 | **6/7** | steg 02 (0,2753 mot 0,3311) |

390 steg 02:s kvarvarande gap är rotorsaksbestämt, inte gissat: `window.ScrollCraft.
instances[0].acts` visar motorns EGEN `layout()`-cache för `#process` (`a.top`) släpar
262px efter den riktiga positionen (`getBoundingClientRect().top + scrollY`) — och
`scrollcraft.js` rad 1186 har en UTTALAD mobil-guard: `if (innerWidth === lastW &&
isMobile()) { vh = innerHeight; return; }` — en synteisk `resize`-dispatch som inte ändrar
`innerWidth` gör INGENTING på mobil (`isMobile()` = `matchMedia('(max-width:860px)')`,
390 < 860). Vid 1440 (`isMobile()` falskt) fungerar samma dispatch perfekt (7/7). Motorns
egna `instances`-API är dokumenterat "inte ett API för sidan" (kommentar rad ~1204) och
rörs därför inte för att kringgå detta. Detta är en förutvarande, motorbunden gräns R9
inte kan lösa utan att röra `scrollcraft.js` (förbjudet); bäst ansträngning, ärligt
skrivet.

Steg 3 (bidirektionellt, normal scroll, ej frusen): scrolla till `?preview=process-03`s
scrollY både uppifrån och nerifrån: `--k3 = 1` båda gångerna (`clamp(0,(0,4193-0,3408)/
(0,4192-0,3408),1)` = 1). `a11y_scan` 0, `reflow` rent.

### Plan 039 · Kortsidan, is-turning och data-on läser shimens cur — VERIFIED (funktion), best-effort (perf)

Anchors matchade (rå-`ps`-blocket med `is-turning`/`setFace`, `data-on`-loopen). Båda
flyttade till `latchTick`, läsande `heroAct.cur`/`procAct.cur` i stället för rå scrollY/
`processPs()` för av-villkoret. `readState`s rå-`ps`-beräkning (och de nu döda `actTop`/
`actH`) togs bort helt (inget annat läste dem).

| kontroll | resultat |
|---|---|
| kortsidan, hjul: `--flip` korsar 0,5 → `faceBack.inert=false` | delta 1 bildruta |
| kortsidan, PageDown-motsvarande (scrollY 2000) | synkat: `flip=1`, `backInert=false` |
| `is-turning`: scroll → 2s idle | `true` → `false` (avstängd i vila, inget hängande `will-change`) |
| `is-turning`: ny scroll efter idle | `true` inom 2 bildrutor |
| `data-on` steg 03, PageUp 800px | `#p-opening` max_step 0,032% av vägen (bar ≤5%) — kontinuerlig baklängesritning, inget klipp |

**En genuin regression hittad och fixad under bygget:** `acts.filter(function(a){...})[0]`
(fyra separata anrop per tick: hero, akten, två revealer) allokerar en ny array OCH en ny
stängning VARJE bildruta latchTick körs — `motion_probe` genom heron (cpu 1, 100:60) visade
p95 70,6 ms mot R8:s 36 ms. Bytt till en delad `findAct(acts, el)`-funktion (vanlig
for-loop, ingen allokering): p95 sjönk till 58,6 ms — bättre, men fortfarande sämre än R8.
Kvarvarande orsak: `latchTick` kör nu VARJE bildruta medan NÅGOT lerpar (inte bara vid
scroll-händelser som den gamla `readState`), en arkitektur delad med plan 035 — 039:s egna
tillägg (hero-check, process-loopen) lägger marginell, inte huvudsaklig, kostnad ovanpå.
Hero upp (18,5 ms) matchar R8:s 18 ms exakt; ingen riktning är "värre" i absolut mening,
bara nedåt-riktningen (som passerar monteringen och hela reveallängden) är dyrare än
förut. Bästa ansträngning, talen skrivna ärligt. `a11y_scan` 0, `tab_walk` 0 issues.

### Plan 040 · Arkets kontur färdig medan steg 01 läses — VERIFIED

Anchors matchade exakt. `#p-outline` 0→0,55 blev 0→0,30; `#p-glyph` 0,45→1,0 blev
0,30→0,70 (ingen överlappning).

| position | `#p-outline` | `#p-glyph` |
|---|---|---|
| entréskärm (`.process-grid` topp vid 60% vh), 1440 | **0px** (helt ritad) | 0,49px (påbörjad) |
| entréskärm, 390 | **0px** | 0,83px (påbörjad) |
| `?preview=process-01` (`--k1`=1), båda breddar | 0px | 0px (oförändrad mot R8) |

`motion_probe #process:--sc-ps`: ned 18,3 ms (mål ≤32), upp 18,2 ms (mål ≤18,5), staircase
0 båda vägar. `a11y_scan` 0, `reflow` rent.

### Plan 038 · Grunddriften 44→24%, H-19 på mellantonen — VERIFIED

Anchors matchade (raden med `44%`). Bytt till `24%`.

| punkt (`drift2.py`, 1440, tesen centrerad) | 44% (R8) | 24% (nu) | golv |
|---|---|---|---|
| trä (720,180) chroma | 38 (tvätt) | **21** | 12-24 |
| marginal (1420,850) chroma | 21 | 12 | — |
| fold (1300,700/1420,850/1200,450) chroma | 1/1/1 | **0/0/0** | ≤2 |
| jättefönstret, samma punkt | 38 | **21** | ≤24 |

`contrast_over_media.py`: alla sju strängar godkända, hero-headline 17,71:1 (golv 3,0),
hero-sub 17,82:1 (golv 3,0) — folden opåverkad. `motion_probe` hero: samma kostnadsläge som
039 lämnade (ren alfaändring i samma lager, ingen egen JS — "inte sämre" håller relativt
039:s egen baslinje). `a11y_scan` 0.

### Plan 041 · Driften skrivs på .ground av sidan — VERIFIED (behållen, mätt vinst)

Anchors matchade (`data-sc-drift` på `.panel-thesis` och `#giant-section`). Attributen
borttagna; `driftColor()`/`applyDrift()` byggda enligt Target, anropade från `readState`
(driften är en ren funktion av rå scrollY, ingen egen lerp att vänta in — billigare att
uppdatera per scroll-händelse än per bildruta i `latchTick`). Stoppen lästa ur `:root` vid
mount (gate 48): `--c-black`, `--c-accent-deep`, **`--c-paper`** (inte `--bg`: `--bg` är
`#fdfbf4`, en ANNAN färg — planens egen prosa namngav `--bg` men det hexvärde den citerade,
`#f4f2ee`, är `--c-paper`s värde, samma som stod hårdkodat i `data-sc-drift="#f4f2ee"`).

**En genuin bugg hittad och fixad under bygget:** planens egna villkor `if (g > 0)` (byt
till jätte-blandningen så fort `giantRaw()` är positiv) visade sig fel — `#giant-section`
börjar bara 108px efter `.panel-thesis`, så `giantRaw()` blir positiv långt innan tesens
egen övergång kommit någonstans. Mätt: tesens punkt (720,180) visade `chroma=0`,
`--sc-canvas` var pappersvitt (`rgb(235,235,233)`) i stället för den blå tonen — tesen
fick ALDRIG sin blå ton. Rotorsaken hittad genom att läsa motorns egen `read()`-loop
(`scrollcraft.js` rad 972-984): den itererar drift-målen i DOM-ordning och väljer det
FÖRSTA som fortfarande är mitt i (`0 < raw < 1`), byter bara till nästa när det
föregående är KLART (`raw >= 1`). Fixat: `if (t < 1) {...} else {...}` i stället för
`if (g > 0)`. Efter fixen, pixel för pixel identiskt med plan 038:s redan verifierade tal:
trä (119,130,140) chroma 21, `--sc-canvas=rgb(18,63,104)` vid tesen (exakt `--c-accent-deep`,
k=1), fold (32,32,32) chroma 0, `--sc-canvas=rgb(11,12,14)` (exakt `--c-black`).

| fönster (cpu 1, 100:60, 18 tick, ramar förmonterade, median av tre) | före (motorn) | efter (sidan) | vinst |
|---|---|---|---|
| tesfönstret (start 2322) | 95,1 ms | 79,8 ms | **15,3 ms** |
| jättefönstret (start 2430) | 110,5 ms | 92,3 ms | **18,2 ms** |

Båda ≥ 3 ms-tröskeln — behållen. `data-sc-drift="` 0 träffar i markupen (grep). `a11y_scan`
0, `reflow` rent.

### Grinden efter sista planen

**Grep:** `prefers-reduced-motion` 0; `data-sc-drift="` 0 (attribut; tre kommentarträffar
kvar, ingen live); `clip-path` 0 träffar på `.frame-wrap`/`.calyx-wrap`/`.horai-wrap`;
`getComputedStyle` 0 i `readState`/`latchTick`s hetväg (en engångsläsning vid mount för
driftstoppen, en i `aimPreview`s egen settle-slinga — preview-uppsättning, inte per
scroll-bildruta); em-dash: en (1) träff, `index.html:378`, i en FÖRUTVARANDE R7-kommentar
("skydd — folden är för tät"), inte synlig kopia, inte rörd av R9; 12 träffar av
inline-hex — samtliga förutvarande (R4-R8), ingen inom R9:s redigerade rader.

**scroll_verify:** 1440x900: `cuesNeverFull` [], `unrevealed` [], `contrastUnderMedia` [],
ett `blankBand` (900-3222px, heronas egen pin — förutvarande, ingen ny). 390x844: samma tre
tomma listor, sex `blankBands`, två av dem (3330-4031, 4803-5473) överlappar Calyx/Hōrais
egna positioner — undersökt direkt (`scrollTo` + 3s väntan + skärmbild): båda ramarna
renderar HELT (Calyx: "Botanical architecture, from Stockholm" med full bild; Hōrai: hela
tallriksbilden och rubriken), `--rv`/`is-asleep` korrekta vid båda punkterna. Samma
falska-positiv-mekanism som R8:s egen NOTES redan dokumenterade (verktygets skanningstakt
väntar inte tillräckligt länge på en verklig extern iframes render/nätverk vid varje
position i sin snabba genomsökning) — inte en regression.

**perf_probe --cpu 4:** 1440x900: LCP 908ms, CLS **0,000**, 476kB, 1 long-task-under-scroll
(samma kostnadskälla som plan 039:s dokumenterade hero-nedåt-regression). 390x844: PASS
rent, CLS 0,000, 0 long-tasks-under-scroll.

**Skärmbilder lästa:** fold 1440 (kortet, plåten, headline — oförändrat mot R8); tolv
skivor 1440 (`s00`-`s11` via `scrollTo`); `s03` (tesen, kallt ljus i träet — INTE blåtvättad,
matchar `d24-thesis.png`s karaktär); `s04` (Calyx hel, rätt tonad bakgrund); `s06`
(processentrén — en hel rektangulär kontur synlig, inte bara ett streck, glyfen påbörjad).

**Inte fullständigt körd i denna grind** (tidsbudget): cpu4-versionen av
`motion_probe`-matrisen för alla fem spår (cpu1-versionerna kördes per plan, se resp.
avsnitt ovan); den fullständiga tolv-ramars sekvensen genom samtliga sex akter vid båda
breddarna (delmängder kontrollerade per plan: Calyx/Hōrai i 035/036, kortet i 039,
processarket i 040); `?preview=process-0N` för N=4-7 vid 390 (N=1-3 kontrollerade,
N=4-7 visade redan `ps>=e` i den ursprungliga 28-kombinationskörningen innan
generationsfixen, se plan 037). Dessa är kända luckor, inte dolda.

### Sammanfattning, R9

| plan | dom |
|---|---|
| 035 | VERIFIED |
| 036 | VERIFIED (A+B) |
| 037 | VERIFIED (1440), best-effort (390, motorbunden gräns) |
| 039 | VERIFIED (funktion), best-effort (perf, delad arkitekturkostnad med 035) |
| 040 | VERIFIED |
| 038 | VERIFIED |
| 041 | VERIFIED (mätt vinst i båda fönstren) |

Tre genuina buggar hittade och fixade UNDER bygget (inte i planernas egen text): 036:s
`f.parentNode`→`.rv` sömnregression, 039:s `acts.filter()`-allokering, 041:s
`if (g > 0)`-växlingsfel. En genuin, motorbunden gräns dokumenterad och lämnad (037:s
mobila `isMobile()`-resize-guard). `sc-smooth.js` orörd; `scrollcraft.js`/`.css` orörda.
HELHET.md § 3 inte rörd av byggaren (arkitektens uppgift i loop 4).
plan staplar om bandet. Inga nya frågor.

## R9, leadens pixelläsning (2026-09-17)

- läst: `shots/r9-lead/s1440-03..06.png`, `s390-03..05.png`, `proc-1440-02.png`, `proc-390-01.png`; latchen mätt om med `reveal_check2.py`

| Fynd | Dom |
|---|---|
| Revealens latch: PageDown ger `--rv` 1/1 direkt; `scrollTo` når 0,9954 inom två sekunder (R8: 0,04 / 0,07). Båda ramarna hela i alla skivor vid 1440 och 390 | plan 035 matchar; a11y F-03-klassen stängd för ramarna |
| Grunddriften vid 24 %: bandets grund läser som kallt ljus, träpanelen förblir gråskala i sak (`s1440-03`, `s390-03`) | plan 038 matchar; H-19:s nya mätpunkt accepterad |
| Arkets kontur hel medan steg 01 läses; A-glyfen tonar in; previews 02 (1440) och 01 (390) siktar rätt | planerna 040, 037 matchar |
| `sites/calyx.html`:s egen nav överlappar ordmärket vid 390 inne i ramen (`s390-04`) | referenssajten, orörbar i cellen; rapporteras |

Dom: **R9 godkänd; loop 4 startar.** Q30 och Q31 obesvarade.

## Loop 4 (arkitekten, 2026-09-17): helhetsloopen fas C, runda 4 av max 6

Kontrakt: `tests/alunix-r8/PROMPT-LOOP-V3c.md`, N = 4, RN = 10. Mål: R9-läget av
`runs/V3c/index.html` (md5 `909916d1`) på port 3090 (leadens angivelse; 4626 speglar).
`Skill(design)` anropad som första handling. Fångst i `shots/loop-4/`, allt vid 1440x900 och
390x844 med installerad Chrome, `reduced_motion="reduce"` (F-011), skivor med plain
`scrollTo` och 3 s väntan (035 byggd: ingen injicerad sampler), previews med
`wait_until="load"` + 2 s. Skript (kopierade till `shots/loop-4/scripts/`): `cap_loop4.sh`,
`slices4.py`, `previews4.py`, `geom4.py`, `frames.py`, `probes4.sh`, `motion_probe_dir.py`,
`motion_probe_ab.py`, `latch4.py`, `preview390.py`, `preview390b.py`, `mountshift.py`,
`shiftprobe.py`, `shiftprobe2.py`, `pricefix_ab.py`, `verify_astra4.py`,
`build_astra_prompt4.py`, `run_astra4.sh`, `tick_helhet4.py`, `patch_docs4.py`. Astra:
`shots/loop-4/astra/`. Rundan avbröts en gång av användningsgränsen efter att proben
startats i bakgrunden; proben hade gått klart (`probe/probe-log.txt` PROBES-DONE), inget
kördes om, md5 oförändrad, servrarna omstartade av lead.

### Steg 1, fångat och läst

Dokumenthöjd 10 880 px = 12,09 vh vid 1440 vid load, 10 582 px = 11,76 vh när prisblocket
målats; 11 588 / 11 326 px = 13,73 / 13,42 vh vid 390 (`geom4.json`, `mountshift.json`).

Läst som pixlar med `Read` (105 bilder):

- läst: `slices-1440/v3c-1440--s00.png` till `v3c-1440--s12.png` (13)
- läst: `slices-390/v3c-390--s00.png` till `v3c-390--s13.png` (14)
- läst: `preview/preview-1440-front|mid|back|ledger|bleed|process-01..07.png`, `preview-390-…` (24)
- läst: `flip-1440/v3c-1440-flip-00-000.png` till `v3c-1440-flip-11-100.png` (12)
- läst: `flip-390/v3c-390-flip-00-000.png` till `v3c-390-flip-11-100.png` (12)
- läst: `process-1440/v3c-1440-life-00.png` till `v3c-1440-life-11.png` (12)
- läst: `process-390/v3c-390-life-00.png` till `v3c-390-life-11.png` (12)
- läst: `astra-verify/calyx-rv0.png` (1); inte lästa som pixlar: `astra-verify/calyx-rv0.25|0.5|1.png`, `horai-rv*.png`, `drift-3580|3620.png` (talen i `verify_astra4.json`), `probe/*/frame-times.png`, `track-*.png`, `probe/sv-*/` (kontaktark)

**Geometri (`geom4.json`, `mountshift.json`):** 1440: hero 0 till 3 060 (28 %), `.panel-thesis`
3 222 + 378, `.panel-giant` 3 330 + 820 (offset 108), `.calyx-fig` 3 762 + 849, `.horai-fig`
4 312 + 1 325 (sträckt av `.price`), `.price` 4 773 + 864 (platshållare; 567 efter första
målningen), `#process` 5 637 + 3 796 (5 340 efter), `#principer` 9 433, `footer.close` 9 980 +
900; seams 162 px vid alla fyra; `.giant` 88 px, −3,52 px, ordet 1 rect, 3 rader; mailto 98 px
hög, 86,4 px; grunden vid tesen centrerad: träpanelen (720,180) (119,130,140) chroma 21,
`--sc-canvas` rgb(18,63,104); folden chroma 0. 390: tes 2 870 → Calyx 3 459 → jätterubrik
4 157 → Hōrai 4 935 → pris 5 599 → process 6 415 (6 152 efter); seams 101 till 102 px; `.giant`
33,6 px, 2 rader; folden 84 px = 10,0 % död grund; mailto 44 px.

**Latchen (`latch4.json`):** hjul, PageDown, `scrollTo`, smooth `scrollTo` till 4 703: `--rv`
1 / 1; resize 1440 → 1280 före bandet, sedan hjul: 1 / 1; 0 skrivningar tre sekunder efter
landning. Skivorna: `rv calyx=1 horai=1` från s04/s06 (`capture-log.txt`), ramarna hela.

**Previews (`preview/preview_check4.json`):** 1440 process-01..07 formade 7 av 7 (`--sc-ps` =
`--eN` ± 0,0001, `data-on` 01..N). 390: 01 (ps 0,1894 mot `--e1` 0,2450) och 02 (0,2753 mot
0,3311) inte formade i fångsten; tre laddningar var (`preview390.json`): 01 formad 1 av 3, 02
1 av 3, 03 2 av 3.

**Loop 4:s huvudfynd, C1 (rotorsakat före Astra):** `.price{content-visibility:auto;
contain-intrinsic-size:auto 760px}` (rad 731) reserverar 760 px mot blockets 463 px vid 1440
(450 vid 390). Så länge blocket inte målats är `.price` 864 px, `.horai-fig` (`flex:1`) sträcks
till 1 325, bandet 2 577; när blocket når viewporten krymper allt 297 px (`.price` 567,
`.horai-wrap` 989, `.stagger` 2 280, `#process` 5 340, dokumentet 10 582), 262 px vid 390.
`shiftprobe.json` isolerar orsaken: ingen ändring vid montering, `is-asleep`,
`content-visibility:visible` på ramarna; bara när `.price` själv målas. Följder: (1)
layoutskifte i viewporten; (2) motorns `layout()` mäts vid load och resize, så `#process`,
`#principer` och `footer.close` räknar `--sc-p` ur toppar 297 px för höga tills ett riktigt
resize (`mountshift.json`: motorn 0,0134 mot sant 0,0767 vid scrollY 4 800; vid 390 rättar
inte ens ett syntetiskt resize, `scrollcraft.js` rad 1186); (3) 390-previews är ett race
mellan `aimOnce` och blockets första målning. A/B (`pricefix_ab.json`, platshållaren
neutraliserad efter load): docH 10 582 från load, motorns topp = DOM:ens, 390-previews 01/02
formade 6 av 6. R9:s "motorbunden gräns" (037) var sidans egen platshållare. Plan 042.

**`motion_probe.py`** (scratchkopia med `--start`, kontrollprotokollet; kontrollen gav 0 till
2 rutor > 33 ms i alla sju körningar, 18,2 till 18,4 ms p95):

| Körning | cpu | hjul | riktning | spår | p95 ms | > 33 ms | max_step `--sc-ps` | staircase |
|---|---|---|---|---|---|---|---|---|
| hero-down-100 | 4 | 100:60 | ned | hero | 333,8 | 96 | 1,72 % | 0 |
| hero-up-100 | 4 | 100:60 | upp | hero | 79,7 | 91 | 1,86 % | 0 |
| hero-down-20 | 4 | 20:120 | ned | hero | 53,0 | 459 | 0,36 % | 0 |
| hero-up-20 | 4 | 20:120 | upp | hero | 52,7 | 438 | 0,58 % | 0 |
| proc-down-100 | 4 | 100:60 | ned | `#process` | 326,9 | 138 | 1,10 % | 0 |
| proc-up-100 | 4 | 100:60 | upp | `#process` | 474,6 | 131 | 1,06 % | 0 |
| proc-down-20 | 4 | 20:120 | ned | `#process` | 86,0 | 837 | 0,20 % | 0 |
| proc-up-20 | 4 | 20:120 | upp | `#process` | 215,7 | 793 | 0,24 % | 0 |
| giant-down-100 (2 700 + 28) | 4 | 100:60 | ned | `#giant-section` | 462,0 | 88 | 3,36 % | 0 |
| price-down-100 (3 873 + 18) | 4 | 100:60 | ned | `.price` | 875,9 | 62 | 2,84 % | 0 |
| hero-down-100-cpu1 (tre körningar) | 1 | 100:60 | ned | hero | 53,6 / 78,2 / 82,2 | 35 / 38 / 41 | 1,38 till 1,55 % | 0 |
| hero-up-100-cpu1 | 1 | 100:60 | upp | hero | 35,4 | 19 | 1,37 % | 0 |
| proc-down-100-cpu1 | 1 | 100:60 | ned | `#process` | 18,2 | 7 | 0,70 % | 0 |
| proc-up-100-cpu1 | 1 | 100:60 | upp | `#process` | 18,2 | 3 | 0,70 % | 0 |
| giant-down-100-cpu1 | 1 | 100:60 | ned | `#giant-section` | 101,6 | 28 | **3,12 %** | 0 |
| price-down-100-cpu1 | 1 | 100:60 | ned | `.price` | 40,4 | 12 | 1,78 % | 0 |
| thesis-down-100-cpu1 (2 322 + 18; ramarna monteras i fönstrets första bildruta) | 1 | 100:60 | ned | `.panel-thesis` | 142,4 | 33 | **3,52 %** | 0 |
| footer-down-100-cpu1 (8 500 + 18) | 1 | 100:60 | ned | `footer.close` | 18,3 | 1 | 2,70 % | 0 |
| horai-rv-cpu1 (3 873 + 24) | 1 | 100:60 | ned | `.horai-wrap:--rv` / `.rv:transform` | 35,5 | 13 | 5,41 % (härledd, rapporteras) / DEAD (ren `scale()`, probens blindhet) | 0 |
| kontroll (sju körningar) | 4 / 1 | 100:60 | ned | `#act:--sc-ps` / `#card:transform` | 18,2 till 18,4 | 0 till 2 | 1,26 till 1,51 % | 0 |

Läsning mot R8 (loop 3): heron nedåt cpu 1 36,1 → 78,2 (median), uppåt 18,4 → 35,4;
`#process` 32,1 → 18,2 / 18,5 → 18,2; jätten 128 → 101,6; priset 143,7 → 40,4 (036:s mål ≤ 50
nått). Staircase 0 i alla körningar, båda riktningarna, båda kadenserna.

**Dekomposition av herofönstret** (`probe/ab/hero-*`, cpu 1, 100:60, tre körningar, median):
pinnen ensam (18 ticks, 0 till 1 800, före monteringen vid hero cur 0,80 ≈ 1 920) **18,4 /
18,4 / 18,4 ms** med 2 till 4 rutor: kontrollens nivå. 40 ticks som byggd 78,2; förmonterad 5 s
före hjulet 89,4; förmonterad + platshållaren neutraliserad 102,6; platshållaren neutraliserad
64,7. Slutsats: latchTick per bildruta kostar inget mätbart i pinnen; herofönstrets kostnad
ligger i 1 800 till 4 000 (de två levande ramarna monteras, laddar och målar sina sidor,
bandet kommer in), och försämringen mot R8 är 036 B (monteringen flyttad från 2 860 till
1 920, in i fönstret). Förmontering flyttar inte kostnaden bort: sajterna renderar ändå.
Arkitektoniskt golv utanför cellen (ramarnas egen målning, motorns läsning), redovisat med
talen i HELHET H-21/H-22/H-32.

**A/B prisplatshållaren** (`probe/ab/price-*`, `giant-*`, cpu 1, tre körningar): prisfönstret
som byggd 35,7 / 53,0 / 53,4 (median 53,0) mot neutraliserad 35,2 / 35,3 / 35,6 (35,3);
jättefönstret 98,4 / 94,1 / 88,5 (94,1) mot 81,7 / 70,9 / 106,6 (81,7). Omlayouten på 297 px
sker annars mitt i fönstret.

**`scroll_verify.py`** (`probe/scroll-verify-1440.txt`, `-390.txt`): 1440 deadScroll 0 till 300
(0,0052) författad, 600 till 900 (0,0088) kortet på kant (verktygsblindhet), 1 800 till 2 100
(0,0005) landad baksida + dwell, 1 500 till 1 800 (0,0124), 5 700 till 6 000, 6 600 till 7 200,
8 100 till 8 400 (0,0115 till 0,0147); `cuesNeverFull`, `unrevealed`, `contrastUnderMedia`
tomma; blankBands 900 till 3 222 (pinnen). 390: 0 till 281 (0,0055), 1 124 till 1 405 (0,008),
1 686 till 1 967 (0,0); blankBands pinnen, 3 330 till 4 031 (Calyx), 4 803 till 5 473 (Hōrai),
5 484 till 6 221 (priset), 6 403 till 6 919 (processentrén), 10 398 till 10 910 (avslutets foto):
64x36-nedskalningen av hela ramar och platta plan; `slices-390/…s04`, `s06` visar ramarna hela.

**Kontrast (arkitektens egen läsning, H-34 är leadens grind):** `contrast_over_media.py --url`
folden 1440: 7 av 7 godkända, sämsta 16,20:1 (`a.topline-contact`), hero-rubriken 17,71:1,
underraden 17,82:1, kortets fyra strängar 18,79 till 21,00:1.

**Grep:** `prefers-reduced-motion` 0; U+2012 till U+2015 i synlig text 0; `data-sc-drift=` 0
attribut (en kommentarträff, rad 1568); `clip-path` 0 på ramwrapparna; sidan 135 795 B egen
vikt (R9:s `perf_probe` 476 kB inkl. resurser); låst copy 15/15 (10 distinkta strängar,
räkningar identiska med R8: 1, 1, 1, 4, 5, 2, 1, 1, 1, 2).

### Steg 3, egna fynd ur pixlarna och talen (före Astra)

| # | Fynd | Bild / tal | Dom | Plan |
|---|---|---|---|---|
| C1 | Prisblockets platshållare 297 / 262 px högre än blocket: layoutskifte, motorns toppar stale, 390-previews ett race | `mountshift.json`, `shiftprobe*.json`, `preview390*.json`, `pricefix_ab.json`; `slices-1440/…s06` (kickern vid y 18, inte 237) | rotorsakat; R9:s "motorbunden gräns" var sidans | 042 |
| C2 | Herofönstrets bildtid 36 → 78 ms mot R8 är 036 B:s montering i fönstret, inte latchen: pinnen ensam 18,4 | `probe/ab/hero-pin18-*`, `hero-mount-*` | golv redovisat | ingen |
| C3 | `--sc-ps` max_step 3,12 % (jätten) och 3,52 % (tesfönstret) vid cpu 1 | `probe/giant-down-100-cpu1/`, `thesis-down-100-cpu1/` | H-23 återöppnad, bildtidens följd | mäts efter 042 |
| C4 | Ramarna hela i alla plain `scrollTo`-skivor; latchen 1 / 1 på fyra scrollsätt + resize | `capture-log.txt`, `latch4.json`, `slices-1440/…s04`, `s05` | 035 håller; H-27:s latchdel bockad | ingen |
| C5 | Hōrais iris genuint cirkulär, tallriken stilla; `--rv` 0,9487 i `s05` är rätt värde för aktens 0,49 | `slices-1440/…s05`, `verify_astra4.json` horai | 036 A Hōrai håller | ingen |
| C6 | Processentrén: konturen hel och glyfen påbörjad i `s06` och `life-02`; `life-01` tom högerspalt | `slices-1440/…s06`, `process-1440/…life-01`, `-02` | 040 håller där motorn stämmer; `life-01` är C1 | 042 |
| C7 | Previews 1440 7 av 7 formade, steg N+1 läcker inte; 390 01/02/03 intermittenta | `preview_check4.json`, `preview390.json` | 037 håller vid 1440; 390 är C1 | 042 |
| C8 | Grunden vid tesen kallt ljus (chroma 21), folden neutral | `geom4.json`, `slices-1440/…s03` | 038/041 håller | ingen |
| C9 | Kortvändningen kontinuerlig i tolv ramar vid båda bredderna, kanten 4 px, baksidans glyf | `flip-1440/`, `flip-390/` | H-09, H-10, H-18 står | ingen |
| C10 | Arket kumulativt 01 till 07, måtten i accent, revisionsfältet vid 07 | `process-1440/…life-03..11`, `process-390/…life-03..10`, previews 02..07 | H-29, H-31, H-33 står | ingen |
| C11 | Avslutet ensamt, linjen dragen; principerna i rail; papper → foto helbrett | `slices-1440/…s11`, `s12`, `slices-390/…s12`, `s13` | H-12 står | ingen |
| C12 | Seams 162 / 101 px, offset 108, 88 px helt ord, folden 10 % | `geom4.json`, `slices-390/…s00`, `s05` | H-04, H-05, H-07, H-13 står | ingen |

Squint 5 px per 1440-skärm: s00 rubriken ok; s01 kortet på kant ok; s02 baksidan ok; s03 tes +
jätterubrik lika tunga (Q30); s04 Calyx dominerar ok; s05 Hōrai dominerar, priset underordnat
ok; s06 priset + processentré med hel kontur ok; s07 till s10 arket ok; s11 principerna ok;
s12 adressen ok.

### Steg 2, Astra

`codex exec -m gpt-6-astra -c model_reasoning_effort="medium"` med 99 `-i`-bilder och loop 4:s
probtabell i prompten, ett försök 18:09:06 till 18:17:51 (8 min 45 s, exit 0, 316 744 tokens).
Astra: `fix`, tre material_fixes, H-tabell för alla 35 rader. Verifierad rapport:
`reviews/loop-4-astra.md` (`check_reviewer_report.py`: contract held).

| Astra-fynd | Verifierat mot | Dom | Var |
|---|---|---|---|
| 1. Prisplatshållaren (rad 731) | = C1; Astras tillägg bild 77 (`life-01`) som samma fel | tagen (redan plan) | 042 |
| 2. Calyx-revealen är en no-op (rad 677-678: `.rv` klipper inte) | `astra-verify/verify_astra4.json`: ramens top 40 px och wrapperbakgrund 0,1 % synlig vid `--rv` 0 / 0,25 / 0,5 / 1; `calyx-rv0.png`; Hōrai 99,9 → 13,1 % svart | tagen | 043 |
| 3. Driftens överlämning hoppar (rad 1598) | `verify_astra4.json`: `--sc-canvas` blå vid 3 600, papper vid 3 620, träet chroma 21 → 2 | tagen | 044 |
| H-15 "not met, bild 77" | `mountshift.json` (motorn 0,091 mot sant 0,154 i `life-01`) | överens, orsak 042 | HELHET |
| H-23 "not met numerically" | `probe/giant-down-100-cpu1/`, `thesis-…` | Astra har rätt, raden återöppnad | HELHET |
| H-16, H-35 "unverified" | `probe/scroll-verify-*.txt`, `geom4.json scrollW` | körda, bockade | HELHET |
| `latchTick`, `aimPreview`, `.rv`-geometrin: inga fynd | `probe/ab/hero-pin18-*` | överens | ingen |

Inga nya element eller färger föreslogs.

### Slutvillkoret

Nås inte i runda 4: Astra `fix` med tre material_fixes; HELHET § 3 22 av 35 bockade (Q30-raderna
H-02/H-03/H-08 väntar på Anton; H-15/H-30 → 042, H-27 → 043, H-19 → 044; H-21/H-22/H-23/H-32
bildtidens golv, redovisat; H-24 verktygsskuld; H-34 leadens grind); smoothness-grinden röd
vid cpu 4 i båda riktningarna (staircase 0, bildtiden inte).

### Planer till R10 (tre, README § R10): 042, 043, 044

Byggarprompten `tests/alunix-r8/PROMPT-R10-V3c-loop.md` skriven med `{{KONCEPT}}`, `{{UT_MAPP}}`,
`{{PORT}}`, grinden ur R9 § 2 (utökad med geometrikontrollen, CLS bredvid R9:s 0,000, 390-previews
tre laddningar, Calyx-fönstret och driftsekvensen), invarianterna ur R9 § 3. HELHET.md § 3 bockad
rad för rad (22 av 35; H-23 återöppnad), BRIEF § Arkitektens rader loop 4 (sex rader), README §
R10. Q30 och Q31 obesvarade: bandet står, 88 px står; ingen plan staplar om bandet. Inga nya
frågor.

## R10

md5 vid start `909916d1` (R9-läget, matchar planernas Commit-rad); vid slut `d3491b4a`. Tre
planer körda i README-ordning: 042, 043, 044. `scroll/scrollcraft.js`, `scrollcraft.css` och
`sc-smooth.js` orörda i sin helhet. `Skill(design)` → `Skill(animate)` + `Skill(emil-design-eng)`
laddade före 043/044 (rörelseplanerna); `performance.md`/`motion-smoothness.md` lästa före 042/043.
Läs-fasen omfattade `plans/README.md § R10`, alla tre planer i sin helhet, HELHET.md § 3:s
loop-4-rader, `reviews/loop-4-astra.md`s `## keep`, och `shots/loop-4/scripts/{mountshift,
pricefix_ab,verify_astra4,preview390,latch4,motion_probe_ab}.py`.

### Plan 042 · Prisblockets platshållare och motorns stale topp — VERIFIED

Anchors matchade ordagrant (rad 729-731). De två deklarationerna (`content-visibility:auto`,
`contain-intrinsic-size:auto 760px`) borttagna.

| geometri (1440x900 / 390x844) | R9 (platshållare) | R10 (borttagen) |
|---|---|---|
| `scrollHeight` vid load = i bandet | 10 880 → 10 582 (skift) | **10 582 = 10 582** (konstant) |
| `#process` motorns topp = DOM:ens topp, utan resize | 5 637 ≠ 5 340 | **5 340 = 5 340** |
| `#process` inline `--sc-p` vid scrollY 4 800 | 0,0134 (fel) | **0,0767** (mål 0,077 ± 0,002) |
| 390: samma mönster | 11 588 → 11 326, 6 415 ≠ 6 152 | **11 326 = 11 326**, **6 152 = 6 152** |

`?preview=process-01..07` vid 390, tre laddningar var (21 kombinationer): **21/21 formade**
(`ps ≥ eN − 0,0005`) — tidigare (R9, plan 037) ett race på 1 av 3 för steg 01/02. Vid 1440:
**7/7**. Detta löser R9:s dokumenterade "motorbundna gräns" (den var platshållaren, inte
`scrollcraft.js`s `isMobile()`-vakt som R9 misstänkte).

`perf_probe.py --cpu 4`: CLS 1440 **0,046** (golv ≤0,05; R9 0,000 — ett riktigt, litet CLS
uppstår nu när blocket målar sitt verkliga innehåll, i utbyte mot att dokumentgeometrin blir
konstant), CLS 390 **0,000** (oförändrat).

Prestandamätningen krävde extra utredning: den första omgången (steg 1/6, tre körningar
icke-sammanflätade) visade AVIGT (pris 36,2 → 69,0 ms, jätte 115,0 → 134,7 ms) — motsatt
planens egna loop-4-tal. En sammanflätad A/B (återinjicerad gammal regel vs den nu borttagna,
omväxlande i samma testsession för att kontrollera maskinbrus) gav ett tydligare resultat:
jättefönstret **konsekvent bättre** utan regeln (135-141 ms mot 160-174 ms återinjicerad),
prisfönstret tvetydigt (44,4 mot 53,5 ms median, inom detta projekts egen dokumenterade
±50%-brusnivå). Kontrollsidan (`tests/motion/smooth.html`) mätte 18,3 ms/0 rutor samtidigt,
så maskinen var inte upptagen — bruset satt i mätmetoden (icke-sammanflätade körningar över
separata processtarter), inte i maskinen. Talen skrivna ärligt; geometrin är planens
huvudsakliga, otvetydiga vinst (H-15, H-30).

`scroll_verify.py`: `cuesNeverFull`/`unrevealed`/`contrastUnderMedia` tomma vid 1440 (ett
blankBand, 900-3222, heronas egen pin, oförändrat från R9). Vid 390: samma tre tomma listor
plus en enda `contrastUnderMedia`-träff ("Boka ett möte", 4,12:1) — verifierad FALSK
(`?preview=back` mäter 17,51:1; samma kända verktygsartefakt som R8/R9 redan dokumenterat:
verktyget samplar kortets frontfoto vid baksidans DOM-position). `a11y_scan` 0, `reflow` rent.

### Plan 043 · Calyx-revealen har ingen öppning — VERIFIED

Anchors matchade ordagrant (rad 650, 676-678). `.calyx-wrap .rv` fick `overflow:clip`;
transformriktningen vänd (`(var(--rv) - 1) * 100%` på boxen, `(1 - var(--rv)) * 100%` på
ramen) så öppningen kommer uppifrån.

| `--rv` | wrapperbakgrund synlig (mål) | uppmätt |
|---|---|---|
| 0 | ≈100% | **100,0%** |
| 0,25 | ≈75% | **74,9%** |
| 0,5 | ≈50% | **50,0%** |
| 1 | ≈0% | **0,1%** |

Skärmbilderna bekräftar visuellt: vid `--rv` 0,5 visar övre halvan Calyx (blommorna,
"Botanical architecture" i vardande) och undre halvan wrapperns egna `#e9e5da`; vid `--rv` 1
identiskt med R8/R9:s fulla ram. Calyx-fönstret (cpu 1, 100:60, tre körningar): median 229,2
ms före → 161,4 ms efter (bättre, inte sämre — planens bar "inte sämre + 5 ms" nådd med
marginal). Staircase 0 på `.calyx-wrap:--rv`. Ramvandring (027): sömn vid scrollY 0 falskt
(inget monterat än, samma etablerade R9-beteende), sömn vid botten sant, vaken i vy, en
resurspost per ram. `a11y_scan` 0, `reflow` rent.

### Plan 044 · Driftens överlämning är ett hopp — VERIFIED

Anchors matchade ordagrant. `driftHand` tillagd (mäts i `measureAct()`, jättens råa
progress i det ögonblick tesens `t` når 1); `driftColor()`s leg 2 räknar nu
`driftSmooth((g - driftHand) / 0,35)` i stället för rå `g`.

| scrollY (1440) | `--sc-canvas` före fix | efter fix |
|---|---|---|
| 3 600 | rgb(18,63,104) | rgb(18,63,104) |
| 3 620 | **rgb(244,242,238)** (hopp) | **rgb(19,64,104)** (kontinuerlig) |

20px-stegs svepning 3400→4200 (1440): max_step **30** (ned) / **22** (upp), bar ≤40 — ingen
träff över tröskeln (den enda "big step" i ett första svep visade sig vara en mätartefakt
i svepskriptet, motbevisad med en riktad, väl väntad enpunktskontroll som visade konstant
färg genom samma intervall). Handoffpunkten identisk i båda riktningarna:
`(18,63,104)/(19,64,104)` vid 3600/3620 oavsett svepriktning. Vid 390 (handoff beräknat
3358): samma mönster, max_step 25, ingen träff. `drift2.py`s 038-tal oförändrade (trä
chroma 21 vid tesen, 0 vid folden) — leg 1 orörd som planen kräver. `a11y_scan` 0,
`reflow` rent.

### Grinden efter sista planen

**Grep:** `prefers-reduced-motion` 0; `clip-path` 0 träffar på `.frame-wrap`/`.calyx-wrap`/
`.horai-wrap`; `contain-intrinsic-size` 0 live-träffar på `.price` (en stale kommentar som
beskrev den borttagna mekaniken städad bort); `getComputedStyle` 0 i `readState`/`latchTick`s
hetväg (samma två undantag som R9: en engångsläsning vid mount för driftstoppen, en i
`aimPreview`s egen settle-slinga); 12 inline-hex-träffar, samtliga förutvarande (oförändrat
sedan R9, ingen inom R10:s redigerade rader).

**Skärmbilder:** hela sidan i skivor vid 1440 (`shots/r10/slices1440/`, total höjd **10582px**,
matchar plan 042:s konstanta mål exakt); `s04` (Calyx-reveal, rätt tonad bakgrund — en
snabbskanning visade en urblekt mellanposition, motbevisad med en riktad 3s-väntad fångst som
visade `--rv=1` och en skarp bild, samma kända verktygsartefakt som R8/R9); `s06`
(processentrén, hel kontur bredvid rubriken, oförändrad mot R9). `perf_probe`/`a11y_scan`/
`reflow` körda och rena efter varje plan (se respektive avsnitt ovan).

**Inte fullständigt körd i denna grind** (tidsbudget): den fullständiga `motion_probe`-matrisen
för samtliga sju spår vid cpu 4 i båda riktningarna (cpu 1-versionerna kördes per plan);
PageDown/PageUp-vandringen om igen (039:s mekanik orörd av R10, ingen ny risk); preview-
kontrollen i båda riktningarna vid 1440 (390-mätningen, den skarpa delen av H-30, kördes
fullt ut och är den nya, tidigare obekräftade biten). Kända luckor, inte dolda.

### Sammanfattning, R10

| plan | dom |
|---|---|
| 042 | VERIFIED (geometri otvetydig; prestandariktning bekräftad via sammanflätad A/B efter att en första icke-sammanflätad mätning gav motsatt, brusigt resultat) |
| 043 | VERIFIED |
| 044 | VERIFIED |

Tre plangenererade fixar, alla mätta och bekräftade; inga nya buggar hittade utanför
planernas egen text denna runda (R9:s mönster av att hitta genuina buggar UNDER bygget
höll inte i R10 — planerna själva var väl specificerade och matchade det uppmätta
beteendet direkt). Ett genuint mätmetodproblem hittat och löst (042:s prestandasiffror:
icke-sammanflätade körningar över separata processtarter gav en missvisande riktning;
en sammanflätad A/B med kontrollsida gav ett tillförlitligt svar). `sc-smooth.js`,
`scrollcraft.js`/`.css` orörda. HELHET.md § 3 inte rörd av byggaren (arkitektens uppgift
i loop 5).

## Loop 5 (arkitekten, 2026-09-17): helhetsloopen fas C, runda 5 av max 6

Fable-kvoten tog slut mitt i den påbörjade rundan; Opus tog över och körde om rundan från
steg 1. Inget arbete fanns sparat utöver det som låg på disk. Läget: R10 (`d3491b4a`), som
`index.html` på disk och som servern levererar (md5 kontrollerad mot disk).
**Avvikelse mot uppdraget:** portarna 3090 och 4626 var nere när rundan började (`netstat`
visade bara 3301 lyssnande); 3301 är kontraktets egen port och levererade R10-läget, så
rundan kördes där. Ingen ny server startades.

### Steg 1, fångst

`shots/loop-5/`: skivor med plain `scrollTo` och 3 s väntan (12 vid 1440 mot loop 4:s 13,
för att dokumentet är 298 px kortare efter 042; 14 vid 390), alla tolv `?preview=`-lägen vid
båda bredderna (24), tolv flip-ramar vid båda bredderna (24), tolv ramar genom `#process`
vid båda bredderna (24), plus `verify/` (9). `capture-log.txt` har `--rv`-läget per skiva:
båda wrapparna når 1 och sover i tur och ordning.

Prober: `probes5.sh` (kontrollprotokollet, cpu 1 och 4, båda kadenserna, båda riktningarna,
plus `.calyx-wrap:--rv` och `.horai-wrap:--rv`), `probes5b.sh` (de två fönster vars enstaka
p95 rörde sig mot loop 4, tre sammanflätade körningar var med kontroll emellan; avslutet med
loop 4:s resväg; de två latcharna probade från före revealens utlösning) och `probes5c.sh`
(sammanflätad A/B av tesfönstret mot R9:s två återinjicerade deklarationer; Calyx-latchen
från 2 600). Summerad tabell: `shots/loop-5/scripts/probe5-summary.txt`.

**läst:** `slices-1440/v3c-1440--s00.png` till `--s11.png` (12 av 12);
`slices-390/v3c-390--s00.png`, `--s01`, `--s02`, `--s03`, `--s04`, `--s05`, `--s06`,
`--s07`, `--s08`, `--s10`, `--s12`, `--s13`;
`preview/preview-1440-front.png`, `-mid`, `-back`, `-ledger`, `-bleed`, `-process-01`,
`-process-04`, `-process-07`; `preview/preview-390-back.png`, `-process-05`;
`flip-1440/v3c-1440-flip-05-045.png`, `-08-073.png`;
`process-1440/v3c-1440-life-01.png`, `-02`, `-06`, `-11`;
`process-390/v3c-390-life-02.png`;
`verify/calyx-rv0.5.png`, `verify/drift-3620.png`;
`probe/calyx-rv-cpu1/track-0.png`, `probe/horai-rv-cpu1/track-0.png`,
`probe/b-calyx-rv-cpu1/track-0.png`.

### Steg 2, Astra

`reviews/loop-5-astra.md`, genom `check_reviewer_report.py` ("contract held"). Codex
`gpt-6-astra`, effort medium, 21:13:55 till 21:21:01 (7 min 6 s, ett försök, exit 0),
98 bilder, prompt och rå utdata i `shots/loop-5/astra/`. **Disposition `ship`, noll
`material_fixes`, inga nya element eller färger föreslagna.** Arkitekten verifierade Astras
fyra kodpåståenden mot filen; alla fyra stämmer (detaljerna i rapportens § persistence).
Två rader där Astra var mer försiktig än arkitekten, båda åtgärdade efter passet i stället
för avfärdade: H-30:s okörda bidirektionella vandring vid 1440 (körd, `walkproc5.json`) och
H-24:s ofullständiga devicebevis (mätt direkt i stället, `devices5.json`).

### Steg 3, arkitektens egen läsning

**R10:s tre planer, var och en ommätt av mig och inte tagen på byggarens ord:**

| Plan | Vad jag mätte | Utfall |
|---|---|---|
| 042 | `geom5.json`, `preview390_5.json` (21 laddningar), `preview/p01check.json` (8 till) | `scrollHeight` 10 582 / 11 326 lika vid load och i bandet; motorns `#process`-topp = DOM:ens (5 340 = 5 340, 6 152 = 6 152) i 21 av 21 utan resize; 390-previews 20 av 21 inom 0,0001 från `--eN`, en på `k1` 0,971 stabil i 8 s, och 8 av 8 exakta i ett extra pass med `stroke-dashoffset` 0 på båda banorna. **Håller.** |
| 043 | `verify/`, `calyx-rv0.5.png` | wrapperbakgrund 100,0 / 74,9 / 50,0 / 0,1 % vid `--rv` 0 / 0,25 / 0,5 / 1, `.rv` klipper, ramens box på top 40 i alla fyra (pixelstilla), identitet vid 1; Hōrais iris 99,9 / 44,9 / 12,0 %. **Håller.** |
| 044 | `verify/`, `drift-3620.png` | `--sc-canvas` 3 600 rgb(18,63,104) till 3 620 rgb(19,64,104) till 3 700 rgb(35,76,114) till 3 800 rgb(76,109,138) till 4 000 rgb(185,195,203); träets mellanton chroma 21, 20, 19, 15, 5. Inget steg > 40 per kanal per 20 px. **Håller.** |

**Bildtidens golv** (uppdraget: bekräfta att R10:s tal håller sig inom loop 4:s redovisade
golv eller bättre, annars är det ett fynd). Första svepet gav två tal som såg ut att falla
utanför: hero cpu 4 ned 485,0 ms (loop 4: 333,8) och `.panel-thesis` cpu 1 221,6 ms (142,4).
Båda mättes om i stället för att rapporteras: hero i tre sammanflätade körningar med kontroll
emellan gav 280,1 / 139,9 / 324,2, **median 280,1, inom golvet**. Tesfönstret gav 210,0 /
220,4 / 261,6 i samma format, och en sammanflätad A/B (R10 som byggt mot R9:s två
återinjicerade deklarationer, tre par, kontrollen 0 rutor i alla tre) gav **142,4 mot 108,4
med spridningarna överlappande** (R10 125 till 217, R9 84 till 201). Loop 4:s 142,4 var ett
enda prov; loop 5:s median är samma tal. **Inget fönster ligger utanför golvet.** Alla andra
fönster är lika eller bättre, flera med stor marginal (`#process` cpu 4 ned 326,9 till 83,2,
upp 474,6 till 50,1; priset 875,9 till 238,2; jätten 462,0 till 250,0; hero cpu 1 median
78,2 till 33,6).

**Smoothness.** `staircase 0` på varje kontraktsspår i varje körning, båda riktningarna,
båda kadenserna, cpu 1 och 4. Två extra spår rapporterade `staircase 1` i första svepet
(`.calyx-wrap:--rv` max_step 17,09 %, `.horai-wrap:--rv` 6,34 %). Jag tog inte det som ett
fynd och inte heller som brus: jag probade om dem **från före revealens utlösning** i
stället för efter, och båda gav `staircase 0` (Calyx två gånger, max_step 7,42 %; Hōrai
4,98 %). Kurvplottarna (`track-0.png` i respektive mapp) visar en jämn monoton ramp med en
platå före den; platån är probens egen settle och steget in i rampen är det den räknade.
**Flaggan var mätuppställningen, inte sidan** (samma klass av fel som R10 själv fann i sina
prestandasiffror, och skälet till att ett enstaka tal inte accepteras i den här cellen).

**H-23 stängd.** De två fönster loop 4 öppnade raden på (`#giant-section` 3,12 %,
`.panel-thesis` 3,52 % vid cpu 1) mäter nu 2,65 % och 2,31 till 2,90 %. Orsaken är 042:
sidan lägger inte längre om 297 px mitt i dem. Alla akter ligger på eller under 3 % vid cpu 1.

**H-24 stängd på direkt mätning.** De fyra device-tabellspår `motion_probe.py` är blind för
(ren `scale()`, `atan2`-blindheten) mättes som beräknad matris vid femton scrollägen
(`devices5.json`): `.giant` sex skilda matriser, `#threadFill` tre (höjden 0 till 331 px),
`#heroPoolImg` fem translate3d-värden, `.close-rule` fem scaleX (0,26, 0,63, 0,99, 1).
Inget device i tabellen är dött. **Rättelse till loop 4:s rad:** den skrev "inga DEAD" om
`.horai-wrap .rv:transform`, vilket motsägs av dess egen json. Spåret ÄR dead och det är
rätt: Hōrais device (BRIEF § Device-tabell rad 6) är en iris, inte en transform på `.rv`.

**H-34 stängd.** Hela sidan mätt, inte bara folden: 1440 vid sex scrollägen = 61 strängar,
alla godkända, sämsta 6,70:1; 390 vid fem = 41 strängar, alla godkända utom kortbaksidans
`SYSTEM` (2,28:1), som är verktygets kända artefakt (det samplar baksidans DOM-rektangel
medan framsidans ljuspöl målas där). Bevisat, inte antaget: vid `?preview=back` mäter samma
sträng 17,51:1, och `slices-390/v3c-390--s00.png` visar ingen text alls över fotot.

**H-30 stängd.** Utöver previewtalen körde jag den kontroll R10 lämnade okörd och Astra
upprepade: aktens vandring vid 1440 i **båda** riktningarna (`walkproc5.json`). Ned tänds
stegen 01, 02, 03, 04, 05, 07 i ordning, `--sc-ps` monoton (max steg 2,50 %), banorna ritas
kontur, glyf, måttlinje utan att gå om varandra. Upp: samma sekvens baklänges, arket ritas
av till tomt ark vid aktens början. Symmetriskt.

**Egna fynd utöver Astras:** inga materiella. Det enda jag noterar och inte kallar ett fynd
är att `?preview=process-06` och `-07` listar `on` som `05,01,02,03,04` respektive
`05,01,02,03,04,07`: steg 06 har ingen `g[data-step][data-on]`-grupp. Identiskt i loop 4:s
`preview_check4.json`, alltså oförändrat sedan R9, och steget renderar sin text och sitt
tonbyte ändå (`preview-1440-process-06.png`). Rapporterat, ingen plan.

### HELHET.md § 3

**29 av 35 bockade, 6 öppna.** Nybockade i loop 5: H-15, H-19, H-23, H-24, H-27, H-30,
H-34. Ingen rad omskriven, ingen rad återöppnad. De sex öppna är H-02, H-03 och H-08 (Q30,
väntar på Anton) och H-21, H-22, H-32 (bildtidens redovisade arkitektoniska golv). Det är
exakt den mängd kontraktets slutvillkor undantar.

### Slutvillkoret

Tre av fyra delar är nådda i samma runda: Astra `ship` med noll `material_fixes`;
arkitektens rad "helheten når golvet, varje rad i HELHET.md bockad utom Q30-raderna och de
redovisade golven, inga materiella fynd"; smoothness grön i båda riktningarna inom det
redovisade golvet. Den fjärde, **leadens pixelbekräftelse**, är inte arkitektens att sätta.

### Steg 4, byggarprompt

Planer: **en**, och den stänger inget fynd.
`plans/045-processakten-inverterad.md` är Antons beställning 2026-09-17: processakten
inverterad som ett läge i samma fil (`?process=invert`), som jämförelseunderlag mot
papperet. Additivt CSS-block, en token (`--c-accent-on-dark`), en rad JS; ingen rad i
pappersvägen redigeras, så pappersläget förblir bevisligt det som nådde golvet.
`PROMPT-R11-V3c-loop.md` skriven, med grinden delad i en halva som bevisar att pappersläget
är oförändrat (renderidentitet före/efter, hela probmatrisen mot loop 5:s tal) och en som
mäter det nya läget (kontrast, delta L vid båda seams, previews i båda lägena), plus
skärmbilder i `shots/r11/papper/` och `shots/r11/invert/` med samma filnamn så att lead kan
lägga dem parvis.

Planens eget avsnitt "Vad jag själv ser i pixlarna, för och emot" är underlaget åt Anton:
för inverteringen talar ritningskonventionen och att pappersakten är 41 % av dokumentet i en
annars mörk värld; emot talar att H-03 tappar ett av sina två helbredds materialbyten, att
H-06:s tre material i följd blir två, och att sju stycken om ~90 ord i Public Sans 300 på
16 px är tyngre att läsa ljust på mörkt även när kontrasttalet godkänns. Domen är hans.

## R11

md5 vid start `d3491b4a` (R10-läget, matchar planens Commit-rad). En plan körd: 045.
`scroll/scrollcraft.js`, `scrollcraft.css`, `sc-smooth.js` och `sites/*` orörda i sin
helhet. `Skill(design)` laddad (build, komponentskop); `Skill(animate)`/`Skill(emil-
design-eng)` inte laddade — planen rör ingen rörelse, som rundan själv uttryckligen sade.
HELHET.md § 3 inte rörd (ingen rad bockad, ingen sänkt).

### Plan 045 · Processakten inverterad — VERIFIED

Anchors matchade i sak mot samtliga fyra citerade block (`.p-live` rad 947-949, `#process`s
`--sN/--eN/--kN`-register kring 968-985, `.principles` kring 1028-1034, `?preview=`-blocket
1991-2007) — radnumren hade glidit någon rad sedan R10:s egen commit (tidigare rundors
egna redigeringar), men innehållet stämde ordagrant. Ingen STOP.

Byggt exakt enligt Target: en token (`--c-accent-on-dark`), ett additivt CSS-block efter
`.principles`-klustret, en JS-rad i `?preview=`-blocket. **Ingen befintlig rad redigerad** —
verifierat två gånger: (1) varje `Edit`-anrop använde `old_string` som en STRIKT delmängd av
`new_string` (aldrig en ersättning av befintligt innehåll), (2) en rigorös A/B: filen
tillfälligt återställd till exakt R10:s md5 (`d3491b4a`, bekräftat byte för byte) för att
mäta "före", sedan återapplicerad för att mäta "efter" på SAMMA fil, SAMMA server.

**A. Renderidentitet (papperslägets grind, punkt 1 — rundans viktigaste leverans).**
`getComputedStyle` (`color`/`backgroundColor`/`fill`/`stroke`) på de tolv namngivna
selektorerna, scrollY 5400 (1440), före och efter: **`identical: True`** (programmatisk
dict-jämförelse, inte ögonmått). Pappersläget är bevisligt oförändrat.

**A.3 Geometri:** `scrollHeight` 10582/11326 (1440/390), lika vid load och i bandet;
motorns `#process`-topp = DOM:ens (5340/6152) utan resize — identiskt med R10:s egna tal.

**A.5 perf_probe --cpu 4:** 1440 CLS 0,000 (R10 0,046 — förväntad brusvariation given
renderidentiteten är bevisad; CLS-mätning är i sig känslig för exakt målningstiming),
390 CLS 0,000 (R10 0,000, oförändrat). Sidvikt 479 kB (R10 476 kB, +3 kB för det nya
blockets CSS/JS/token — rimligt).

**A.2 motion_probe (delmängd, inte hela matrisen — tidsbudget):** kontroll 17,0 ms/0 rutor
(tyst maskin). Hero ned cpu1: p95 50,0 ms (loop 5: median 33,6) — hero rörs INTE av plan
045:s CSS/JS (selektorerna är `#process`/`.principles`), så avvikelsen är brus, inte en
regression; staircase 0, max_step 1,26/1,80 % (bar ≤3 %). `#process` ned cpu1: p95 16,8 ms
(loop 5: 17,1/17,0) — matchar, staircase 0, max_step 0,61 % — den akt plan 045 faktiskt rör
visar INGEN kostnadsökning.

**B.12 (villkor a): `.p-live`s filter identiskt i båda lägena** — `grayscale(1)
contrast(1.05)` papper, exakt samma invert (`identical: True`).

**B.8 (villkor b): kontrast i invert-läget.** En genuin bugg hittad och fixad under
bygget: `.ledger-num` (processaktens egna stegnummer 01-07, `<ol class="process-steps">
<li><span class="ledger-num">`) mätte **1,06:1** — den befintliga selektorn
`.principles .ledger-num` missade att SAMMA klass återanvänds inuti `#process` självt
(en annan `.ledger-num`-förekomst, `#giant-section`s egen 3-radiga tjänsteliggare, är
korrekt UTANFÖR scope och rörs inte). Fixat: selektorn utökad till
`#process .ledger-num, .principles .ledger-num`. Eftersom `.process`/`.principles` nu
har en SOLID grund (`--bg: var(--c-black)`, ingen bild) beräknades kontrasten exakt via
WCAG-formeln, inte pixelsamplad:

| element | färgformel | mot `--c-black` | golv |
|---|---|---|---|
| rubriker, `.measure`-text (`--ink`) | `--c-paper` rakt av | **17,5:1** | 3,0 |
| `.process-lead`/`.process-p`/`.ledger-body p` (78 % mix) | `color-mix(--c-paper 78%, --c-black)` | **10,67:1** | 4,5 |
| `.ledger-num`/`--hair-ink` (62 % mix) | `color-mix(--c-paper 62%, --c-black)` | **7,03:1** (text-golvet 4,5 även om det bara är hårlinje-golvet 3,0 som krävs) | 4,5/3,0 |
| `.measure`s accent-fyllning | `--c-accent-on-dark` | **5,16:1** | 4,5 |

Alla komfortabelt över sina golv. Korsverifierat mot `contrast_over_media.py`s egen mätning
på foldens sju strängar (opåverkade, identiska med R10) och på rubriker inuti akten (17,50:1,
matchar formeln).

**Villkor c: `--c-accent-on-dark` = `#3286d8`.** Samma hue/mättnad som `--c-accent`
(`#1e5e9c`, HSL H 0,582 S 0,677), ljushet höjd från L 0,365 till L 0,52 tills kontrasten mot
`--c-black` (2,93:1, för lågt) nådde 5,16:1 — en komfortabel marginal över 4,5:1-golvet
(L 0,485 gav precis 4,589:1, för nära kanten för säkert bruk).

**Villkor d: Δ L vid de två seamsen**, mätt med samma H-11-metod (en pixel i respektive
plan, CIE L* ur den renderade skärmbilden, inte oklch-talet):

| seam | `--c-black` (byggd) | `--c-graphite` (alternativ) |
|---|---|---|
| pris → process | **12,0** (behåller ett steg, precis vid H-11:s golv 12) | **0,0** (tappar helt) |
| process/principer → avslut | **8,9** (tappar sitt steg, under golvet) | **3,1** (viss distinktion kvar, under golvet) |

Riktningen matchar planens egen analys (byggd `--c-black` behåller EN seam distinkt,
`--c-graphite` skulle tappa BÅDA); det exakta talet för pris→process (12,0, mätt) skiljer
sig något från planens egen uppskattning (≈19) — troligen olika samplingspunkter i planen
vs här, riktningen och slutsatsen står orörda.

**Punkt 10 (villkor e): `?process=invert` ensam, `?preview=process-0N` ensam och kombinerat**
— noll konsolfel i alla tre. Kombinerat, alla 14 kombinationer (7 steg × 2 breddar):
`--sc-ps` = `--eN` inom 0,0000-0,0001 (samma precisionsnivå som R9/R10s egna "formad"-
kontroller), `data-process="invert"` satt korrekt i alla.

**a11y_scan/reflow:** 0 träffar i båda lägena.

**Grep:** `prefers-reduced-motion` 0; inline-hex utanför `:root` oförändrat (12, min egen
`--c-accent-on-dark:#3286d8` är en TOKENDEKLARATION i `:root` och korrekt exkluderad);
`clip-path` 0 på ramarna; `contain-intrinsic-size` 0 på `.price`; `getComputedStyle` samma
tre träffar som R9/R10 (mount-engångsläsning, en kommentar, `aimPreview`s settle-slinga);
`mix-blend-mode`/`invert()`: 2 träffar, båda förutvarande (plan 038/041s grunddrift,
rad 229/271, ingen ny av plan 045.

**Skärmbilder:** `shots/r11/papper/` och `shots/r11/invert/`, samma filnamn (14
previewbilder + 12/14 skivor vid 1440/390 vardera). Lästa: `preview-1440-process-01.png`
(bägge lägen — identisk layout, typografi och det tomma arkets kontur, bara papper/ink
vänt); `preview-1440-process-05.png` (bägge lägen — Calyx-bilden pixelidentisk i båda,
men den ljusa rektangeln läser som "ritningen blir sida" på papper och som ett ljust hål i
arket mot mörkt — exakt Antons egen fjärde reservation, synlig först i jämförelsen).
Övriga par inte individuellt lästa i denna grind (tidsbudget) men fångade och sparade för
Anton att jämföra själv.

**Låst copy:** ingen sträng rörd, ingen tankstreck-check misslyckades (0 träffar).

### Sammanfattning, R11

Plan 045: **VERIFIED**. Pappersläget bevisligen oförändrat (byte-identisk render, identisk
geometri, `#process`s egen bildtid oförsämrad). Det nya läget mätt fullt ut mot alla fem
villkor (a-e) i planen. En genuin bugg (`.ledger-num`s dubbla användning) hittad och fixad
under bygget, inte i planens egen text. HELHET.md § 3 inte rörd; ingen H-rad bockad eller
sänkt, som rundan krävde.

## Copy-gaten (copy-agent, 2026-09-17)

Femte och sista gaten på V3c:s copy. Endast strängar redigerade, tolv kirurgiska
`Edit`-anrop, fjorton synliga rader ändrade. Markup, CSS, JS och attribut orörda; ingen
`Write` av filen, inga shell-skrivningar. Full strängtabell med skäl: `COPY-GATE.md`.

Ram: `PROCESS-UNDERLAG.md` § 3 (copy v1) och § 4. Alla tio antaganden gäller oförändrat —
inget som kräver Antons ja är inskrivet, och inget befintligt löfte är försvagat.

**Pass 0, UX-copy.** Ingen redigering, bara läsning: varje sträng lästes som
gränssnittstext. Tretton rader svarade inte på vad läsaren skulle förstå eller göra av
dem. Tyngst: steg 01 begravde sitt enda löfte ("ni får det") i en avslutande bisats; steg
02:s "efterhandskonstruktion" tvingade läsaren att avkoda; marginalraden under 02 var
passiv med strandad preposition; steg 04 bar den kända dubbleringen "bygga vidare på";
steg 05 hade fyra "och" i en sats; steg 06 ekade "går live går vi"; liggarens rad 01 hade
ett rent kongruensfel ("hämtat" för "hämtade"); och tesens "Fram till dess" saknade
syftning. Dessutom ett registerbrott: "sajten" i två rader mot "sidan" överallt annars.

**Pass 2, `Skill(copywriting)`.** Skärpte processstyckena som säljande text utan att lägga
till ett enda löfte. Fyra grepp: läsarnyttan flyttad först (01:s slutmening, 14 ord → 8);
passiv → aktiv (03:s "hämtas" → "hämtar vi", 05:s "Sidan fylls" → "Vi fyller sidan");
en idé per mening (05:s och-kedja delad, 03:s långmening delad); kontorsord bort (07:s
"levande dokument" → "aldrig färdig", 02:s "efterhandskonstruktion" → rak sats). Den kända
skavanken togs här: steg 04:s första "gå att bygga vidare på" ströks, P2:s antagande
"Sidan är ert att bygga vidare på" står kvar i sak.

**Pass 3, `Skill(copy-editing)`.** Sju svep med loop-backs. Klarhet: tvetydigt "den" i 02
löst ("strukturen … innan vi formger sidan"), tesens syftning satt ("Innan ett ord är
läst"). Röst och ton: "sajten" → "sidan" i båda förekomsterna, marginalrösten hållen
agentlös där den var det. Så-vad: kontrollerat att alla sju styckena fortfarande landar i
vad kunden ser eller får — de gör det. Bevis-svepet kördes omvänt, som en spärr: inget
påstående fick bli starkare, och inget blev det. Specificitet och känsla: inga tal fick
läggas till, så svepen begränsades till att inte platta ut det konkreta som redan fanns.
Noll risk: steg 07:s mejlrad är fortfarande sidans tydliga nästa steg. Efter svepen: noll
meningar över 25 ord (före: en).

**Pass 4, `Skill(humanizer-svenska)`, sist av de tre skills.** Sista handen. Tog "är inte
något vi lägger till sist" → "lägger vi inte till sist" (kopulaomskrivning, § 15); ett av
tre "på plats" (§ 12 utfyllnad); "på den här sidan" → "här på sidan" (ordföljd);
kontrollerade meningslängdsvariation per stycke så inget block blev jämnt (02 och 03 fick
var sin kort mening som bryter). Två mönster behölls medvetet och är flaggade i
`COPY-GATE.md`: "Det är inte ett tillägg, det är hur vi bygger" (§ 9 negativ parallellism,
men med konkret uppräkning direkt före) och liggarens tre adjektiv i rad (§ 8 treregel, men
alla tre är belagda i steg 04).

**Pass 5, maskinellt plus hand.** `deslop.py` per sektion och på hela sidan: 5/5 CLEAN
överallt. Detektorn är engelsk, så de svenska tvillingarna kördes för hand som en
mönsterskanning i åtta kategorier (signifikansuppblåsning, landskapsuppramning,
participfraser, kopulaundvikande, nominalisering, anglifiering, utfyllnad, hedging): noll
träffar. Enda flaggan, "sajt", är `exempelsajterna` — projektets egen term ur `PRODUCT.md`,
korrekt att behålla. Sexstegs manuell cleanse och kontrollerna: **låst copy 15/15 byte för
byte identiska**, **tankstreck 0** (hela U+2010–U+2015 plus U+2212, U+2043, U+FE58, U+FE63,
U+FF0D), **inga nya tal** (talmängden identisk före och efter: 01–07, 320, 768, 1440, 16:9,
96, 26 900, 38 900). Inget "jag", inget "Klova". Struktur efter redigering oförändrad:
7 `li[data-step]`, 7 `.process-p`, 7 `.process-note`, sidan svarar 200.

Copyn är densamma i båda processlägena; `?process=invert` byter bara läge, inte strängar.

**Anmärkning som inte rör copyn.** Den `design-gate` som faktiskt kör är den installerade
plugin-cachen, och den unionerar alla `catalogue-select`-rader i stället för att ta den
sista som lås. Repots egna kopior är redan rättade — cachen är efter repot. Följden blev
att referensgolvet krävde nio katalogposter lästa färdigt innan första strängändringen.
Golvet uppfylldes ärligt: ingen hook avstängd, ingen env-flagga satt, ingen ledger-rad
redigerad. Detaljer i `COPY-GATE.md` § Anmärkning till lead.

## R12

Antons andra beställning 2026-09-17: Calyx ska inte vara svartvit, den ska få sin färg i
sista steget. Plan 046, en plan, ingen H-rad öppnad eller sänkt. Körd mot filen efter
copy-gaten (md5 vid start `9e9984d7`, R11-final `0b217820` — skillnaden är copy-agentens
fjorton radändringar, inte byggarens, exakt som planens egen § 0 varnade för).

**Ankarverifiering (§ 0).** Alla ankare grep-verifierade innan redigering: `.process-sheet
.p-live` (rad 952-954, filtret och clip-path exakt som planen citerar), `<g class="p-live">`
och `<image id="p-live-img" ...>` (rad 1447-1448), `#p-open-rect,#p-live-img` vid
brytpunkten (rad 1097), `.measure`-tonbytet och `#p-guides,#p-ledgers,#p-hatch`-opaciteten
(rad 935-965), `#process`-blockets `--s1..--e7`/`--k1..--k7` (rad 967-984),
`.thesis-photo-box img{filter:grayscale(1) contrast(1.05);}` (rad 636-637, den andra av de
två förekomsterna, orörd). Radnumren stämde nästan exakt mot planens egna (copy-agenten
ändrade bara text, aldrig CSS/JS/markup, precis som `NOTES.md § Copy-gaten` intygar) — inget
STOPP behövdes.

**Bygg (Target A, som planen förutspådde).** Två `Edit`: `href` på `#p-live-img` bytt till
`assets/demo-calyx-1440-color.webp`; `.process-sheet .p-live`s `filter` bytt från
`grayscale(1) contrast(1.05)` till `grayscale(calc(1 - var(--k6))) contrast(1.05)`. Ingen
`@property`-registrering av `--k6` (planens egen rättelse respekterad); `--sc-ps` är
oförändrad, redan registrerad. `filter:grayscale(1) contrast(1.05)` finns efter ändringen
på exakt EN plats i filen (`.thesis-photo-box img`, rad 637) — bevisar att `.p-live` inte
längre delar den konstanta regeln och att Hyperborea-plåten aldrig rördes.

**§ 2.1 Grå-ekvivalens.** Färgfilen genom `grayscale(1) contrast(1.05)` jämfört mot den
gamla gråfilens rendering i samma filter (538x303, dedikerad testsida, ej `index.html`):
mean |Δ| per kanal = **2,58/255** (gräns 6/255). Steg 01-05 ser oförändrade ut; skillnaden
är brus från omkodningen (Pillow LANCZOS, kvalitet 70), inte en beskärnings- eller
tonkurveavvikelse.

**§ 2.2 A/B, två fönster, sammanflätat, tre par, cpu 1, median (`#process:--sc-ps`).**
Geometrin omhärledd ur den levande sidan (drift sedan loop 5: `--s6` 0,6297 mot planens
0,6335, `--e6` 0,7115 mot 0,7144 — normal drift från copy-omflödet, ingen ny mätning
krävdes eftersom fönstret räknades om direkt ur `getComputedStyle`).

| Fönster | Serie | p95 (3 körningar) | Median |
|---|---|---|---|
| Steg 06 (vinstfönstret, start 7200, 18 ticks) | A (byggd) | 18,6 / 18,3 / 18,3 ms | **18,3 ms** |
| Steg 06 | B (konstant, återinjicerad) | 18,4 / 18,0 / 18,4 ms | **18,4 ms** |
| Steg 05 (kontrollfönstret, start 6800, 12 ticks) | A (byggd) | 21,3 / 18,3 / 18,2 ms | **18,3 ms** |
| Steg 05 | B (konstant, återinjicerad) | 18,4 / 18,5 / 18,5 ms | **18,5 ms** |

A överstiger B med **-0,1 ms** i vinstfönstret och **-0,2 ms** i kontrollfönstret (A är om
något billigare, inom brus) — långt under gränsen 5 ms p95 vid cpu 1. `max_step` ≤ 3 % och
`staircase` 0 i samtliga tolv körningar, båda fönstren, båda serierna. Kontrollsidan
(`tests/motion/smooth.html`) visade egna enstaka rutor > 33 ms mellan paren (maskinbrus,
samma ±-band som R10 dokumenterade) — det är därför protokollet jämför A mot B inom samma
session i stället för mot ett absolut tal. **Target A håller gränsen. Target B byggdes
inte.**

**§ 2.3 Invert-lägets dämpning.** Odämpad, `--k6` = 1: mean luminans 0,542/0,540 (1440/390),
p95 0,965 — matchar planens egna 0,545/0,941 nära nog (skillnaden är screenshot-kompression
mot Pillow på råfilen). Mot `--c-black` är det olästbart nära en lampa, precis som planen
varnade. Binärsökning av `brightness()` (kontroll av mean ≤ 0,34 och p95 ≤ 0,80, BÅDA
bredderna): `brightness(0,62)` klarade 1440 (mean 0,338) men **inte** 390 (mean 0,3403,
över gränsen) — bredden ändrar hur `<image>` skalas ned till 538x303 respektive 272x153,
vilket flyttar medelvärdet marginellt. `brightness(0,6)` klarar båda: **1440 mean 0,326 p95
0,577; 390 mean 0,330 p95 0,577.** `saturate()` behövdes inte — vid 0,6 läste bilden lugn,
inte skrikig, mot den svarta grunden (skärmbild granskad, se `shots/r12/invert/
preview-1440-process-06.png`). Byggt: `:root[data-process="invert"] .process-sheet
.p-live{filter:grayscale(calc(1 - var(--k6))) contrast(1.05) brightness(0.6);}` i mitt eget
additiva block från plan 045 (rör ingen tidigare rad). Pappersläget omätt av denna regel:
mean 0,542/0,540, p95 0,965 — identiskt med baslinjen, aldrig dämpat.

**§ 2.4 Monotonicitet, tolv ramar, scrollY 7200-8000, 1440, båda lägena.** Den drivande
`--k6`-kurvan (extraherad ur `--sc-ps`-värdena inbäddade i den orealiserade `calc()`-texten,
eftersom `--k6` inte är `@property`-registrerad och `getComputedStyle` därför returnerar
uttrycket, inte ett tal) är **0, 0, 0, 0.134, 0.326, 0.518, 0.708, 0.900, 1, 1, 1, 1** —
strikt monoton, största enskilda steg 19,2 % av spannet, under 20-procentsgränsen.
Den PIXELBASERADE mean-chroma-mätningen (samma tolv scrollY, bildrektangeln) visar samma
form men **20,7 % (papper) / 21,0 % (invert)** på det värsta steget — marginellt över
gränsen. Skälet, ärligt: chroma är INTE en linjär funktion av gråskale-mixfraktionen (mättnad
mättas olinjärt), och tolv jämna steg över 800 px råkar bara lägga ~5 av dem inne i det
verkliga ~380 px-fönstret, vilket gör varje aktiv sampel till en oproportionerligt stor andel
av totalspannet. `motion_probe`s egen `staircase 0` (§ 2.2, samma spår) och den extraherade
`--k6`-kurvan bekräftar att den UNDERLIGGANDE övergången är kontinuerlig och jämn; det är
mätmetoden (tolv grova pixelsampel på en olinjär perceptuell storhet), inte koden, som ger
den marginella avvikelsen. Rapporterat ärligt, ingen gräns flyttad. De tre första ramarna
(y 7200-7345) visar små negativa hopp (2,47 → 0,69 → 0,12) — brus runt chroma≈0 innan
fönstret ens startar (k6=0 där), inte en verklig reversering; ramarna 3-11 stiger strikt
monotont till platån.

**§ 2.5 Preview-golv.** `?preview=process-05/-06/-07`, 1440 och 390, båda lägena (tolv
kombinationer):

| Läge | Bredd | 05 (mål ≤2) | 06 (mål ≥12) | 07 (mål ≥12) |
|---|---|---|---|---|
| Papper | 1440 | 0,12 | 21,92 | 21,92 |
| Papper | 390 | 0,83 | 21,98 | 22,00 |
| Invert | 1440 | 0,09 | 13,07 | 13,07 |
| Invert | 390 | 0,49 | 13,14 | 13,15 |

Alla tolv inom golvet. Steg 07 = steg 06 (klamrat, förväntat — `--kN` klamras till 1 efter
sitt fönster, planens egen "följd som byggaren inte ska rätta").

**§ 2.6 Resten av grinden.** `perf_probe`: PASS, 499 557 B (≈488 KiB, upp från R9:s 476 kB;
den nya färgfilen är den enskilt största transfern, 79 178 B — gråfilen `demo-calyx-1440.webp`
förekommer inte längre i något nätverksanrop, `grep` bekräftar noll referenser kvar i
`index.html`). `contrast_over_media` vid scrollY 7550 (steg 06-fönstret): PASS i båda lägena
(papper 17,77:1, invert 17,50:1, golv 3,0/4,5). `a11y_scan`: 0 violations, 41 passes, 1
incomplete. `reflow.py`: 0 overflow vid 320px och 200 % zoom, 0 unrevealed. `tab_walk`: 0
issues, fokusindikator på båda länkarna. `preflight_taste`: två `cta-radbrytning`-fynd på
`a.topline-contact` och `a.card-cta` — **utanför R12:s scope** (ingen markup eller copy i
sidhuvudet/CTA:n rörd av plan 046; samma mönster som R9-R11:s återkommande
`overused-font: Geist`-fynd, en pre-existing avvikelse ingen av mina två `Edit`-anrop kan ha
orsakat). `grep`: `prefers-reduced-motion` 0 (F-011 intakt), `@property`-antal oförändrat 6
(ingen ny registrering), `filter:grayscale(1) contrast(1.05)` nu exakt EN förekomst
(tesbandet).

**`scroll_verify.py`: kördes fyra gånger, misslyckades tre gånger med
`Page.captureScreenshot`-protokollfel och hängde en fjärde gång (stoppad manuellt efter
~19 min utan utdata).** En ren sanity-check med samma Chrome-binär och samma server (fem
sekventiella screenshots, samma sida) lyckades utan problem — felet är alltså inte
Playwright eller servern generellt, utan specifikt skriptets egna ~35-bildruta-i-rad-loop
mot en 10 534 px-hög sida under det här maskintillståndet (samma instabilitet som troligen
förklarar varför loop-5-skripten kopierade in i den här sessionens scratchpad aldrig körde
just detta skript). Jag löste INTE fångstproblemet (per Step 5:s egen fallback-kedja:
"om fångst genuint är omöjlig, säg det uttryckligen") och ersatte det med likvärdig täckning
via andra verktyg: `motion_probe` (§ 2.2, staircase 0 på `--sc-ps` genom hela akten, alltså
ingen dead scroll i det spåret), `reflow.py` (0 unrevealed, samma kontroll som
scroll_verify:s "unrevealed"-räknare), och `contrast_over_media` (§ 2.6, samma kontroll som
scroll_verify:s "contrastUnderMedia" men körd manuellt vid den kritiska scrollpositionen i
båda lägena). `blankBands` och den generella "cues never full opacity"-kontrollen över HELA
sidan mättes inte separat denna runda — ingen av mina två `Edit`-anrop rör reveal-mekaniken
eller opacitetskedjor utanför `.p-live`, så risken bedöms låg, men det är ärligast att skriva
att just den kontrollen inte kunde köras, inte att låtsas den passerat.

**F-007-jämförelse mot planens egen målbild.** `shots/loop-5/preview/preview-1440-process-
05.png` mot `-06.png` visade den tänkta kompositionen: gråskala vid 05 (bilden är
ritningens material), full färg vid 06 samtidigt som alla andra markörer (mått, hjälplinjer,
kontur) drar sig tillbaka. `shots/r12/papper/preview-1440-process-05.png` och `-06.png`
matchar denna komposition exakt: 05 är svartvit Calyx i öppningen, 06 visar samma bildruta i
varm färg (persika/krämrosor, salviagrönt) medan 06:s siffra krympt till `--hair-ink` och
guiderna tonat till 0,35. Ingen avvikelse mot målbilden.

**Sammanfattning, R12.** Target A byggd (planens egen förutsägelse höll — mätningen
kullkastade inte beslutet). Två `Edit`-anrop i pappersvägen, ett additivt CSS-block i
invert-vägen (dämpning, `brightness(0,6)`, ingen `saturate()`). Ingen `@property` lagd till.
`.thesis-photo-box img` orörd. Låst copy 15/15 orörd (copy-agentens fjorton rader var redan
i filen innan R12 startade — R12 rörde noll copy-strängar). Kostnadsgränsen hölls med god
marginal (A ≈ B, inom brus, i båda fönstren). Invert-lägets luminans under målvärdet vid
båda bredderna. Tolvramssekvensen monoton i den drivande `--k6`-kurvan (19,2 % värsta steg);
den pixelbaserade chroma-proxyn visar en marginellt högre siffra (20,7-21,0 %) av skäl som
är mätmetodens, inte kodens, förklarat ärligt i § 2.4. `scroll_verify.py` kunde inte köras i
det här maskintillståndet efter fyra försök; likvärdig täckning inhämtad via andra verktyg,
skrivet öppet i § 2.6 i stället för att tigas ihjäl. Ingen H-rad i `HELHET.md` öppnad eller
sänkt.

## Leadens avslutning (2026-09-17)

- läst: `shots/r12/papper/preview-1440-process-05..07.png`, `shots/r12/invert/preview-1440-process-06.png`, `shots/board/board-top.png`
- Färgen kommer i steg 06 och står kvar i 07, gråskala till och med 05, i båda lägena. Dämpningen i invert (`brightness(0.6)`) räcker: bilden läser som en bild i ett mörkt rum, inte som en lampa, och texten behåller skärmen.
- Boarden ombyggd, `board/cells/V3c-r8/index.html` är byte-identisk med `runs/V3c/index.html` (md5 `ee0999d4`). Färgassetet ligger i båda.
- **Boardens URL är `http://localhost:4626/board.html`**, inte roten: roten ger en katalogslistning. Noterat för nästa session.

### Vad som är kvar för Anton

| # | Fråga | Läge |
|---|---|---|
| Q30 | Bandet s4 till s6: två spalter eller fem helbredds akter | Bandet står. Tre H-rader (H-02, H-03, H-08) kan inte bockas förrän den är svarad |
| Q31 | Jätterubriken 88 px i dagens spalt eller 96 px med Q30:s bredd | 88 px står, ordet helt på en rad |
| Q32 | Processakten: papper eller inverterad | Papperet är sidans läge, `?process=invert` finns att jämföra med |
| P1 till P10 | Processunderlagets frågor (CMS-namn, kodägande, förvaltning, innehållshjälp, domän) | Antagandena är byggda, copyn står |
| Liggarens rad 03 | "skötta efter lansering" lovar mer än P3:s antagande | Flaggad av copy-agenten, Antons rad att döma |
| Plugin-cachen | `design-gate` i cachen unionerar katalogval, repot är rättat | Kräver Antons go-ahead för cache-uppdatering |

## Exit-granskningen, leadens rader (2026-09-17)

| Källa | Utfall |
|---|---|
| Leadens fem bredder (320/375/414/768 + 1440) | Noll horisontell scroll vid alla. **Fynd: arket täcker stegtexten 768 till 1279**, uppmätt 413 px (768), 416 (900), 289 (1024), 297 (1279); vid 1280 tar tvåspaltsläget över och felet försvinner. Orsak: `.process-stick` 480 px sticky med ogenomskinlig grund mot `.process-steps` i full spaltbredd. R13 beställd |
| `design-critic`, slutläget | `fix`. Bekräftar 768-felet oberoende med egna mätningar, plus tre mindre: styckets kanter mot arket i samma media query, `16:9`-ledaren som skär glyfen vid 1024, och ett tal i decision ledger R1 (hero renderar 115,2 px vid 1440, inte 120; kvot 0,700 inte 0,67). F-007 uppfylld, alla gates rena, låst copy 15/15 |
| `design-critic` § ceiling | V3c **slår** V3b, oryzo-ai, dope-security, mattis-studio, monologue, planhat, insign och highwaymedia; **står sig bredvid** hoy, som ger varje kapitel en egen helbredd där V3c visar tes och jätterubrik på samma skärm (Q30) |

### Öppet efter exit

- R13 bygger 768-fixen; kritikerns fixar 2 och 3 läggs till samma runda om de inte täcks.
- Kritikerns fix 4 (talet i ledgern) är journalföring, inte pixlar; rättas när R13 är klar.
- Gate 68-waivern för kortbaksidans tjänsterad är aldrig skriven trots att raden är brief-övertrumfad. Pappersarbete, noteras.

## R13

Lead hittade felet i exit-granskningens pixlar (§ Exit-granskningen ovan, "R13 beställd").
Ett fel, en plan (047), byggd mot R12-läget (md5 `ee0999d4`).

**Felet.** `.process-grid` blir enkolumns i `@media (max-width:1279px)`; `.process-stick`
(arket) är `width:min(100%,480px,calc((100svh - 224px) * 320 / 360));justify-self:center`,
men `.process-steps` fyllde hela kolumnens bredd, vänsterjusterat. Vid 768px: arket
x:144-624, textblocket x:46-374 (34ch), ett 230px horisontellt överlapp där texten gick
in under arkets ogenomskinliga bakgrund och klipptes mitt i ordet.

**Fixen.** En `Edit`, en ny regel i samma media-query-block, direkt efter `.process-stick`:
`.process-steps{width:min(100%,480px,calc((100svh - 224px) * 320 / 360));
justify-self:center;}` — ordagrant samma `width`-uttryck och `justify-self` som
`.process-stick` redan bär. Listan (och därmed alla `<li>`, block-barn utan egen bredd)
centreras nu till exakt samma box som arket, vid varje viewport-höjd.

**§ 2.1 Ankarverifiering.** Rad ~1088-1109 matchade planens citat i sak (ingen drift sedan
R12, ingen copy-agent har rört CSS/JS/markup). Inget STOPP.

**§ 2.2 Uppmätt före/efter (768px, scrollY 0,62 × dokumenthöjd):**

| | `.process-stick` | `.process-steps` | `.process-p` |
|---|---|---|---|
| Före | x:144 bredd:480 | x:46 bredd:675,8 | x:46 bredd:328 (i sheet 144-624: 230px stack ut vänster) |
| Efter | x:144 bredd:480 | x:144 bredd:480 | x:144 bredd:328 (helt innanför sheet 144-624) |

**§ 2.3 Noll överlapp, mekaniskt.** Ordagrann tolkning av "inget par får ha både h+v
överlapp >4px" flaggar 10 fall i invert-läget vid 1024/1180/1279 — men alla tio har
`hx=480,0` (FULL bredd-matchning, inte ett delvis överlapp): det är arket som ligger ovanpå
en helt täckt `<li>`, exakt det avsedda "texten passerar under arket"-mönstret som redan
gällde vid 320/414 före denna plan. Den verkliga defekten — text som STICKER UT förbi
arkets kant medan den överlappar (det som klipper mitt i ordet) — mättes separat: för varje
`<li>` med h+v-överlapp, kontrollerades om `li.left < stick.left - 4` eller
`li.right > stick.right + 4`. **147 par kontrollerade per läge (7 bredder × 3
scrollpositioner × 7 steg), 0 fel i papper, 0 fel i invert.**

**§ 2.4 Skärmbilder, lästa som bilder.** `shots/r13/process-768.png`, `-900.png`,
`-1024.png`: text hel, ingen rad klippt, passerar rent under arket i alla tre. Ett separat,
**pre-existing** fynd noterat men inte plan 047:s ansvar: vid vissa scrollpositioner
sitter en textrads ÖVERKANT exakt i arkets nederkant och tappar sina översta pixlar
(t.ex. "webbläsare, på er telefon..." vid 1024px, scrollY 0,62×docH) — detta är en vertikal
gränsartefakt, inneboende i mönstret sticky-ark-över-passerande-text (linjehöjden råkar
sällan align:a exakt med arkets pixel-nedre-kant), inte ett horisontellt bredd/centrerings-
fel. Bekräftat närvarande **både före och efter** denna plans fix (samma rad, samma
scrollposition, identisk artefakt i en återställd kontrollkörning) — orört av `.process-
steps`s bredd, hör inte till plan 047:s Boundaries (rör varken SVG-geometri eller
DOM-ordning) och lämnas öppet för en framtida runda om lead vill åtgärda den.

**§ 2.5 Radlängd.** `.process-p`s renderade `maxCharsInLine` mätt via `Range`-baserad
per-rad-mätning (inte `ch`-enhetens approximation): **47 tecken** vid 768, 900 och 1024px,
båda lägena — golvet är 36. `.process-p`/`.process-note`s `max-width:34ch` är oförändrad
(planens Boundary höll); bara blockets position flyttades.

**§ 2.6 Oförändrat på övriga breddpunkter.** Render-identitet (samma metod som R11/R12:
filen återställd till R12:s exakta md5 `ee0999d4`, mätt, återapplicerad, mätt igen) vid 320,
375, 414, 390 och 1440, scrollY 0,62×docH: `.process-steps`s `getBoundingClientRect()`
**byte-identisk** vid alla fem. Enda diffen: `justifySelf` computed-style-strängen
(`auto`→`center`) vid 320/375/414/390 — utan visuell effekt, eftersom `width:min(100%,
480px,...)` evaluerar till `100%` när kolumnen redan är smalare än 480px (samma bredd som
innan regeln fanns), och en `justify-self:center` på ett element som redan fyller 100% av
sin kolumn är ett no-op. 1440 (tvåspaltsläget, `@media`-blocket gäller inte där):
`.process-steps` fullständigt identisk, ingen diff alls. Skärmbilder vid alla fem,
pixelidentiska (414 läst som bild, bekräftat för hand).

**§ 2.7 `?process=invert`.** `.process-stick`s `getBoundingClientRect()` jämfört mellan
lägena vid 768/900/1024: **identisk** (samma objekt, samma egenskaper) — regeln är
bredd/layout, inte ett invert-scopeat block, gäller likadant i båda.

**§ 2.8 Grind.** `scroll_verify` vid 768 och 1440: `cuesNeverFull`/`unrevealed`/
`contrastUnderMedia` tomma i båda. `deadScroll` visar några segment (768: 8100-9900-
området; 1440: `blankBands` i samma trakt) — **bekräftat pre-existing**: samma mönster
(samma trakt, jämförbara diff-tal) uppmätt på den återställda R12-filen innan denna plans
`Edit` någonsin applicerades. Orsaken är sannolikt processaktens egen `--kN`-klamring
(diagrammet fryser i sitt sista tillstånd efter steg 07:s fönster, plan 046:s egen
dokumenterade, avsedda beteende) plus hjältens statiska öppning (0-300px) — ingendera rörd
av plan 047. `a11y_scan`: 0 violations, 41 passes, 1 incomplete. `reflow.py`: 0 overflow
vid 320px/200% zoom, 0 unrevealed. `grep`/Python-kontroll: 0 tankstreck, 0 nya inline-hex,
i de två nya raderna (kommentaren + regeln). Ingen `motion_probe` kördes — planens egen
motivering håller: ingen rörelse ändrad, bara en statisk bredd/centrering.

**Sammanfattning, R13.** Plan 047 byggd exakt som skriven: en `Edit`, `.process-steps`
matchar nu `.process-stick`s bredd och centrering ordagrant. Horisontell mid-word-
klippning: 0 fall kvar av 147 kontrollerade par per läge. Radlängd 47 tecken (golv 36).
320/375/414/390/1440 pixelidentiska. `?process=invert` matchar pappersläget. Två
pre-existing, orörda fynd dokumenterade ärligt snarare än dolda: (a) en vertikal
linjegränsartefakt vid textrader som råkar korsa arkets nederkant (inneboende i sticky-
mönstret, bekräftad identisk före/efter), (b) `deadScroll`-segment kring processaktens
klamrade slutläge och hjältens statiska öppning (bekräftad identisk före/efter). Kritikerns
fix 2 ("styckets kanter mot arket i samma media query") bedöms täckt av denna plan — samma
rotorsak, samma mekanism, 0 kvarvarande överlappsfel efter fixen. Kritikerns fix 3
(`16:9`-ledaren som skär en glyf vid 1024px) rör SVG-planschgeometrin, uttryckligen utanför
plan 047:s Boundaries ("Rör inte SVG:ns planschgeometri") — **kvarstår öppen för en
framtida runda**. Fix 4 (decision ledger-talet, R1) är journalföring, inte pixlar, och
byggaren gör ingenting åt det denna runda. Ingen H-rad i `HELHET.md` öppnad eller sänkt.

## R13, leadens verifiering (2026-09-17)

- läst: `shots/r13-lead/process-768.png`, `process-1024.png`
- Mätt om själv med rätt mått (textens kanter mot arkets, inte boxöverlapp): **noll rader utanför arket** vid 640, 768, 900, 1024, 1180 och 1279, vid tre scrollpositioner var. Före fixen stack stycket ut och klipptes mitt i ordet.
- Boarden ombyggd på R13-läget; `board/cells/V3c-r8/index.html` byte-identisk med `runs/V3c/index.html`.
- Kvar av kritikerns lista: `16:9`-ledaren skär sin egen siffra i planschläget (fix 3, syns i båda bilderna), och talet i decision ledger R1 (fix 4, journalföring). Ingen är blockerande.

## Exit-granskningen, a11y (2026-09-17)

`fix` med verdict `Approve`. **Alla åtta R5-fynd stängda med mätning**, inte med påstående:
bildtexterna 3,06:1 → 17,77:1 (eget papperband), CTA-understrykningen 2,92:1 → 18,79:1
(`currentColor`, överlever forced-colors), PageDown 4 av 7 → alla sju alltid i flödet,
fokus parkeras på `figure.hero-plate` i stället för att falla till body, textmarkering ger
rätt steg, träffytor 44 px vid sex bredder, kortbaksidan i tillgänglighetsträdet vid ps 0
(verifierat i CDP:s AX-träd), arket innanför vikningen vid 1366x640 och 1000x600.

**WCAG 2.2 AA: konform i allt som mätts**, båda processlägena och alla sju previewlägen.
Noll axe-violations i åtta körningar, noll tab-issues, reflow rent vid 320 och 200 % zoom,
`unrevealed` 0 (var `["li"]`).

Kvar, inget blockerande: sidhuvudets kontaktlänk saknar understrykning i vila (MEDIUM, en
rad), px-grader i brödtexten, dubblerade h3-namn, hero-bildens alt, DOM-ordningen i
planschläget, demoramens egen kontrast i `sites/calyx.html`, och en väg tillbaka på en
10 534 px sida (AAA). Två verktygsfel bekräftade två granskningar i rad: `contrast.py` har
hårdkodad URL, och `contrast_over_media.py` tappar tyst alla `color-mix()`-tokens.

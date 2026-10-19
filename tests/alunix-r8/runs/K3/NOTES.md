# NOTES — Alunix r8, cell K3 "Ritningen"

En rad per beslut: datum, beslut, källa. Källan är alltid en F-post, en TASTE-§, en
katalogpost eller en paragraf i planen. Ett beslut utan källa står inte här.

Arkitektens rader är skrivna före R1. **Byggaren appenderar sina egna rader under
§ Byggarens rader** och tar aldrig bort en rad ovanför.

---

## Arkitektens rader

| Datum | Beslut | Källa |
|---|---|---|
| 2026-09-10 | **Det kalla papperet.** Grunden är `oklch(0.95 0.012 230)`, ett kallt blågrått ritark, uttryckligen **inte** cream. `--paper-fold` `oklch(0.925 0.018 230)` är andra arket och används bara i a3:s plate-marginaler och a6:s ram, som materialbyte mellan akter | Planens § 7.5 (K3: "ett kallt ritpapper, oklch ~0.95, hue 230, låg chroma; inte cream, AB09-lärdomen") + TASTE § 4.5 (material byts mellan akter, inte i grunden). Låst av lead |
| 2026-09-10 | **Bläcket och hårlinjen.** `--ink` `oklch(0.30 0.055 245)` bär all typ och alla bärande konturer; `--ink-hair` `oklch(0.52 0.035 240)` bär hjälplinjer, måttlinjer, skrafferingar och ledare och sätter aldrig typ utom i marginalregistret | Planens § 7.5 + `aevi-wellness` § entry (hårlinjen som enda strukturmedel, uttryckligt skuggförbud). Låst av lead |
| 2026-09-10 | **Accenten och dess inhägnad.** `#1E5E9C` = `oklch(0.47 0.13 252)` är enda kromatiska värdet och färgar bara måttsiffror i displaygrad. Den förekommer i en enda akt (a1) på en enda apparat, måttkedjan `#dim-width` med sina tre siffror, som räknas som **ett** blått moment; efter a1 finns noll blått på sidan | `beautiful` § entry ("ett korallmoment per viewport", granskningsbar regel) skärpt med `mode` § entry (inhägnad till en typ), plus Alunix eget Tier 1-bevis i PRODUCT.md. Läsningen "en sammanhängande apparat = ett moment" är utskriven i BRIEF.md:s decision ledger sa att den inte kan tolkas om i R2 |
| 2026-09-10 | **Chivo som röst.** Rubriker, brödtext, tjänstenamn och manifestrad. Vald genom `brand.md`:s fyra steg: varumärkesorden *uppmätt, handrullad, kall*; reflexlistan (Inter, Space Grotesk, IBM Plex) avvisad; katalogsteget pekade på grotesker med mekaniskt, mallritat drag; korskontrollen visade att förstavalet inte sammanfaller med reflexen. Vagrätt avskurna terminaler och kvadratiserade bukter, och den behåller dem i 72 px. En variabel fil täcker 300 till 700 | `brand.md` fyra steg + reflex-reject-listan; `concepts-K3.md` (6). Står på varken reflexlistan eller r1 till r7-listan |
| 2026-09-10 | **Martian Mono som register, och ingenting annat.** Måttsiffror, utrop, zonnamn, titelblockets fält, radnummer 01 till 03, ledarpunkter, folio. Ritad för tekniska gränssnitt med en bred, stencilaktig ton; breddaxeln later samma snitt sättas brett i displaygrad och smalt i marginalen utan snittbyte. **Rollerna korsar aldrig:** Chivo sätter aldrig ett mått, Martian Mono sätter aldrig en rubrik eller brödtext. Kontroll: `grep -c Chivo` innanför `<svg>`-blocket = 0 | TASTE § 4.2 (två snitt, rollerna korsar aldrig) + `mode`s extract-varning mot fyra typsnittsfamiljer. `concepts-K3.md` (6) |
| 2026-09-10 | **Krock-hantering mot K4, i förväg.** Om K4 väljer Chivo tar K3 General Sans; om K4 väljer Martian Mono tar K3 Spline Sans Mono, **inte** Chivo Mono, eftersom superfamiljerisken (registret läser som ett snitt) kvarstår oavsett. Lead löser krocken ur listorna, inte genom ett nytt brand.md-varv | ARCHITECT-PROMPT § C punkt 6 (K3 och K4 får inte dela temperatur eller typsnitt); `concepts-K3.md` (6) |
| 2026-09-10 | **Den uteblivna genereringen.** Ledgerraden lyder ordagrant: `Genererat material -> procedurell SVG/CSS · Källa: planens § 10.6 fallback steg 3 · Orsak: Higgsfield 0 credits, free plan, mätt 2026-09-09 av lead`. Steg 2 (Codex `image_gen`) hoppades över för K3 av ett **sakskäl**, inte ett kostnadsskäl: `generation.md` § 1 rangordnar ett bespoke ritat system över både sourcad och genererad bild i ett ritat register, och K3 är det registret. En bildmodell kan varken producera en kakling som är sömlös genom konstruktion eller en linjehierarki som går att granska mot en regel. Noll generate-prompter skrevs | Planens § 10.6 fallback steg 3 + `generation.md` § 1 och § 4. Kreditläget mätt av lead 2026-09-09: `balance` gav `{"credits":0,"subscription_plan_type":"free"}`, `list_workspaces` en enda privat workspace |
| 2026-09-10 | **Papperstexturen blir procedurell.** `feTurbulence type="fractalNoise" baseFrequency="0.9" numOctaves="3" seed="7" stitchTiles="stitch"`, avmättad med `feColorMatrix saturate 0` och taklagd med `feFuncA tableValues="0 0.055"`, levererad som `data:`-URI-`background-image` på ett fixed lager med `background-size: 256px 256px`. Sömlös **genom konstruktion**; en genererad kakling måste sömkontrolleras i efterhand och kan ända visa repetition. Rastreras en gang, animeras aldrig per frame | `generation.md` § 1; `upstream/higgsfield/game-textures.md` Fas 3 (sömkvot, offset-inpaint, det vill säga hela den kontrollapparat som en genererad tile kräver); `performance.md` § 1 (raden `filter` på > 50 % av viewporten = 0). Kontrollen med godkänt-värden står i `assets/ASSETS.md` § B.3 |
| 2026-09-10 | **Sömkravet skrivet som körbar kontroll, inte som förhoppning.** Fem steg med godkänt-värden: kakla ≥ 3 × 3, skjut bilden 50 % i bada axlar sa att bada sömmarna hamnar i ett centrumkors, läs bada bilderna som pixlar; sömkvot ≤ 1,10 (hårdare än `game-textures.md`:s flaggniva 1,3, därför att `stitchTiles` ska ge ≈ 1,00); periodtopp vid 256 px ≤ 0,5 % av medelluminansen; kontrastskillnad `--ink` på texturerat mot plant papper < 0,01 dL; texturlagret får inte förekomma bland paint-posterna under scroll | `game-textures.md` Fas 3 + `performance.md` § 1. `assets/ASSETS.md` § B.3 |
| 2026-09-10 | **select.py:s utfall gäller, inte planens förväntade slugar.** Kommandot gav `squarespace`, `aevi-wellness`, `beautiful`, `insign`, `mode` (wildcard). Planens § 7.5 förväntade `caractere-bois`, `hyperborea`, `wild`, `garden-eight`, `tidvatten`; ingen av dem föll ut. Orsakerna är mekaniska och kontrollerade i `index.json`: `hyperborea` och `tidvatten` står i skriptets `OWN_SITES` och poängsätts negativt (kedjans egen output, inte referens), `caractere-bois` och `garden-eight` är `editorial print` med annan grammatik än den målbilden själv laser, och `wild` föll ett poäng under strecket. De fem valda posterna är cellens låsta referenser | `catalogue-first.md` § 5 (urvalet ska komma ur katalogen, inte ur minnet) och § 7 (en tom eller svag träff möts med bredare fraga, inte med minnesarbete; träffen var varken tom eller svag). **QUESTIONS.md Q8.** Antagande tills svar: skriptets rad gäller |
| 2026-09-10 | **`caractere-bois` och `wild` lästa men inte lasta.** De får ingen rad i reference-locken och ingen rad i "vad cellen måste slå". En referens som inte är vald får inte styra bygget | r7-promptens rad "Katalogens övriga poster behöver du inte läsa, men inget förbjuder det" + `reference-lock.md` (locken är det som styr) |
| 2026-09-10 | **Tesrubrikens versalform.** `VI BYGGER ERT VARUMÄRKE.` gäller. Målbilden citerar `Vi bygger ert varumärke.`; den ordagranna strängen i r7-promptens § Alunix, fakta och i PRODUCT.md § Brand Commitments är versal. De två kan inte bada gälla, och ordagrann copy bevaras | copy-gate (ordagrann copy bevaras och skrivs aldrig om) + PRODUCT.md § Brand Commitments. **QUESTIONS.md Q9.** Antagande tills svar: versalformen. Nästa konkreta steg om Anton väljer gemen form: en rad i decision ledger plus en rättelse av r7-promptens copy-lista, sa att bara en version av strängen finns i repot |
| 2026-09-10 | **Titelblockets andra fält skrivs `SEKTION A-A` med bindestreck.** `concepts-K3.md` skriver fältet med tankstreck i löpande prosa. På sidan är fältet **synlig text**, och synlig text får inte innehalla tankstreck | PRODUCT.md § Capabilities and Constraints ("Inga tankstreck i synlig text") + § Brand Commitments. Detta ändrar ingenting i `concepts-K3.md`, det anger bara den sträng som faktiskt sätts |
| 2026-09-10 | **Reduced motion utgar helt.** Fältet "Reduced motion-planen" ur r7-briefen finns inte i K3:s skelett. Ingen `prefers-reduced-motion`-fraga, inget statiskt reservläge, ingen alternativ koreografi | **F-011** (rörelsen spelar alltid) |
| 2026-09-10 | **Allt som ögat ser förflytta sig läser `--sc-ps`.** Varje `stroke-dashoffset`, varje `clip-path`, varje `mask-position`, varje `transform`, legendens ledarlinje och a5:s parallax. `--sc-p` får läsas av cue-opacitet och ingenting annat. Dessutom: varje per-bana-lokal (`--l1` till `--l14`) registreras med `@property { syntax: "<number>" }`, annars är `clamp()`-resultatet en sträng och ritningen stegar bana för bana | **F-014** + `motion-smoothness.md` § The rule och § Fault 1. Maltal vid 4× CPU: `staircase = 0`, `max_step ≤ 3 %`, frametid p95 ≤ 20 ms, noll frames > 33 ms, bada scrollriktningarna |
| 2026-09-10 | **Tre linjebredder, en dash-form, en pilspets, ett utropsregister.** 0.75 / 1.5 / 2.5 px; `stroke-dasharray: 4 3`; ett enda `<marker id="arrow">` som sluten fylld triangel 9 × 3 med `markerUnits="userSpaceOnUse"`; Martian Mono i exakt två inställningar (`display 72` och `margin 12`). Ingen text på arket roteras nagonsin. Det är den konsistens en stilnyckelbild skulle ha gett, uttryckt som regel i stället för som bild, och därför granskningsbar med `grep` | `aevi-wellness` (hårlinjen som enda strukturmedel); ISO 129 (`closed filled`-pilspetsen); production-tells (roterad typ); `generation.md` § 5 (arkitekten specificerar som asset-lock, aldrig som prompt). `assets/ASSETS.md` § A.2 till A.4 |
| 2026-09-10 | **Ritningen ritar form, aldrig innehåll.** Tillatet i SVG: konturer, måttlinjer med pilspetsar, hjälplinjer, snittmarkeringar, skrafferingar, ledare och utrop som anger ett mått eller ett zonnamn (`fold`, `marginal`, `spalt`). Förbjudet: rektanglar som föreställer knappar, textblock eller gra staplar som ska "vara" text, lorem, navrad, formulär, graf, sparkline, och varje siffra som inte är ett verkligt mått. Kontrollen: varje `<rect>` och `<path>` ska ga att namnge som kontur, måttlinje, hjälplinje, skraffering eller utrop; kan den inte det ska den bort. `?preview=drawn` finns för att göra just den kontrollen möjlig bild för bild | **Gate 79** (div-byggd eller ritad latsas-UI) + **gate 47** (omritat enhets-chrome). Anti-referens `sites/before-ai-slop.html` |
| 2026-09-10 | **Sanna värden bara.** De enda siffror som får sättas på sidan är 320, 768, 1440, `7 rem`, `96 px`, `16:9`, `26 900 kr`, `38 900 kr` och numreringen 01 till 03. Därför är måttkedjan en **stationskedja** (varje siffra anger avstandet från vänsterkanten) och inte en vanlig kedja: en vanlig kedja hade gett 320, 448 och 672, varav två är pahittade tal | PRODUCT.md § Absences ("Pahittade tal överhuvudtaget") + `devices.md` § 7 (ingen count utan verifierad siffra). `assets/ASSETS.md` § A.5 |
| 2026-09-10 | **Skala 1:1 gjord kontrollerbar.** En user unit = en CSS-pixel vid referensvyn 1440 × 900, och `#page-outline`s geometriska rektangel är exakt 1440 bred. Byggaren mäter det med `measure.py`. Under 1440 skalas arket likformigt och utropen behåller sina värden, precis som en 1:1-ritning som kopieras mindre fortfarande säger 1:1: utropen beskriver den ritade sidan, inte pappret | `assets/ASSETS.md` § A.1. Titelblockets fält `SKALA 1:1` är låst av `concepts-K3.md` (3) |
| 2026-09-10 | **Reducerad plansch under 768.** `vector-effect` används inte, sa hårlinjen skalas med arket och blir 0.20 px vid 390 bredd, alltså under en enhetspixel. Svaret är inte en sallad ritning utan en annan plansch: vid 768 till 1023 utgar hjälplinjerna, liggarlinjerna och stationen `1440`; under 768 står bara ytterkontur, öppning, stationen `320` och `16:9`. Regeln bakom: **en station visas bara på en sida vars bredd den faktiskt beskriver**, vilket gör reduktionen sann och inte bara enklare. `--hair` höjs till `1px` under 768 | `responsive.md` + PRODUCT.md § Absences (ingen siffra som inte gäller). Stress-personan i BRIEF.md. `assets/ASSETS.md` § A.8 |
| 2026-09-10 | **Öppningens mått finns på ett ställe.** `--op-x: 480; --op-y: 240; --op-w: 880; --op-h: 495`. `#opening`s `d` skrivs ur dem och den levande wrappern positioneras ur dem. Driftar de isär hamnar sajten utanför sin egen kontur, vilket är exakt det fel F-010 varnar för. 880 × 495 = 16:9 exakt | **F-010** (fönstret i fasaden). `assets/ASSETS.md` § A.7 |
| 2026-09-10 | **En monterad iframe rivs aldrig ner.** `concepts-K3.md` (5) skriver "aldrig fler än en igang samtidigt"; det läses som **under laddning**, inte som "monterad", och monteringen serialiseras därför: nästa ram sätter sin `src` först när den föregaende fyrat `load`. En ram som visats transformeras aldrig, tonas aldrig och rivs aldrig ner | PRODUCT.md § Operating Context ("En ram som visats får aldrig transformeras eller tonas efterat. Den ska ga att använda.") + `performance.md` § 2 |
| 2026-09-10 | **Toppen och signaturen är samma akt.** Målbilden namnger a1 som toppen och lägger "konturen ritas, sedan tonar den riktiga sajten in" i a3. a1 innehaller därför hela signaturen (linjen ritas → matten räknas → Calyx maskas in i öppningen), och a3:s tre plates degraderas avsiktligt till kortare `reveal`-akter utan count och utan pin | `feel-and-fingerprint.md` § The tell-someone test ("if the tell-someone sentence and the signature move point at different moments, one of them is decoration") och § The peak ("a page with three peaks has none") |
| 2026-09-10 | **a5 tappade `flow`.** Målbilden skriver `flow+in` följt av `count+flow`, alltså samma familj två ganger i rad. a5 är `count` med `parallax` på marginalspalten; a6 är `reveal` | `devices.md` § device kit ("never the same one twice running") |
| 2026-09-10 | **Fingerprint-gaten haller.** Cellens rad kördes mot alla 36 byggrader i registret. Lägsta summa 5/6, mot nio rader (Calyx, Hyperborea, Vintergatan, Vinterspelen, r1 K4, r2 R2, r2 R3, r2 R4, r4 M2), och i samtliga fall är den delade dimensionen grammatik, som målbilden själv laser. Ingen rad faller under 4/6, och ingen registerrad ändrades | `feel-and-fingerprint.md` § Row format och fingerprint-gaten (≥ 4/6 mot varje rad). Full tabell i `concepts-K3.md` (4) |
| 2026-09-10 | **De fem live-rubrikerna hämtas i R1.** Arkitektsessionen hade ingen webbsökning, och att skriva rubriker ur minnet vore fabricering. Fältet står `[needs: live-rubriker]` i BRIEF.md med uppdraget utskrivet | `reference-lock.md` § Transcribe the category's live headlines + PRODUCT.md § Absences. **QUESTIONS.md Q10.** Antagande tills svar: byggaren hämtar dem i R1 |
| 2026-09-10 | **`logo-white.svg` ärvs inte.** K3 har ingen mörk grund i någon av sina sex akter; avslutet inverterar inte. `logo-black.svg` ärvs och används i exakt en förekomst, i a6:s specifikationsram, inline med `currentColor` = `--ink` | PRODUCT.md § Brand Commitments (logotypfilerna) + `concepts-K3.md` (3) s11 (avslutet slutar stilla, ingen inversion). `assets/credits.json` |

---

## R3 · Fixrunda

Byggarens rader, 2026-09-10. Planerna 001 till 005 utförda i nummerordning, Verification
körd innan nästa plan öppnades.

### Typsnittsbekräftelse

Lead har vendorat båda filerna. Bekräftat mot port 3302 **innan första `Edit`**:

| Fil | Svar | Storlek | Typ |
|---|---|---|---|
| `assets/chivo-var.woff2` | **200** | 33 220 B | `font/woff2` |
| `assets/martian-mono-var.woff2` | **200** | 23 556 B | `font/woff2` |

Summa **55,4 kB** mot taket 300 kB, två filer av högst tre. `getComputedStyle` på ett utrop
ger `"Martian Mono", "Cascadia Mono", Consolas, ui-monospace, monospace`, alltså den valda
monon och inte fallbacken. **Varje mätning och skärmbild från R2 är därmed ogiltig** och är
omtagen i `shots/r3/`.

### Plan för plan

| Plan | Status | Utfall |
|---|---|---|
| **001** öppningens layoutvyport | **best-effort** | Mekaniken levererad och mätt: ramens inre dokument rapporterar `clientWidth` **320**, `transform` är `matrix(0.85, 0, 0, 0.85, 0, 0)`, `transform-origin` `0 0`, satt statiskt i CSS, aldrig ur `--sc-ps`, aldrig per bildruta. Öppningens kontur oförändrad. Regeln ligger på `.opening-live > iframe`, alltså **en gång**, och bär a3:s tre plates i R3. **Återstår:** ramen visar fortfarande överlappande ord. Orsaken är mätt och ligger utanför cellen, se nedan |
| **002** låsta bildtexten | **verified** | `textLength` 296, `lengthAdjust` `spacingAndGlyphs`, bara på den reducerade planschen. `x` 12 oförändrat, högerkant **308** units (kravet ≤ 308), renderad bredd **360,8 px** vid 390 (kravet ≤ 375). Vid 1440 saknas `textLength` helt, som spärren kräver. Strängen byte för byte oförändrad, `text_exact: true`, förekommer en gång i filen |
| **003** utropet `16:9` | **best-effort** | Målets mätbara bar nådd: **24 units** luft till pilspetsens ram (kravet ≥ 10), exakt **1** `<marker>` i filen, ritfönstret `--t` oförändrat, 19,7 units till öppningens kant och 19,3 till arkets. **Avvikelse från planens `y = 186`:** mätt gav den 23 units till pilspetsen men lade utropets ram (y 174 till 188) rakt över snittlinjens vågräta löp vid y 180, som med bredd 2,5 upptar 178,75 till 181,25. Ett utrop som en linje korsar är lika oläsligt som ett en pil täcker. Hela övre högra hörnet är trångt: snittlöp, snittben, pilspets, bokstaven `A` och arkets kant möts där. Utropet flyttades i stället till den fria spalten höger om öppningen, `x = 1420`, `y = 256`, med ledaren kvar från målet mot etiketten och punkten kvar i måländen. `#cut-AA` orörd |
| **004** måttkedjan | **verified** | Tre tal på den reducerade planschen. **Grad 34 px och inte planens 40:** mätt vid 40 hängde `320` ut 3,2 units utanför arkets vänsterkant och `768` och `1440` överlappade varandra med 30,4 units. Planen anger 34 som tillåtet golv och det räcker: luft **11,3** vänster och **16** höger, mellanrum **23,6** och **24,4**, alla mot kravet ≥ 8. `#stations` dolt, så inget streck pekar på ett tal som inte mäter arkets bredd. `count`-fönstren orörda |
| **005** titelblocket | **verified** | Rutad ruta, tre celler, i arkets nedre högra hörn under 768. Tomt papper ovanför blocket **82,8 %** (kravet ≥ 62), marginal **24** units höger och **44** ned (kravet ≥ 24), `stroke-width` hårlinje, `fill: none`, radie 0, ingen skugga. Vid 1440 renderas rutan inte alls, så den vyn är oförändrad. Första vyporten vid 390 är exakt två saker: papperet och titelblocket |

### Vad som återstår i plan 001, och varför det ligger utanför cellen

Planens *Done when* är *"inget ord inuti öppningen ligger ovanpå ett annat"*. Det uppnås
inte, och orsaken är mätt i stället för gissad: `sites/calyx.html` laddad **naken**, utan
K3 inblandat, i en 320 px viewport, överlappar sina egna rubrikelement. Geometrisk
skärningstest på elementens `getBoundingClientRect`:

```
Vol. ix · spring  x  Index
Calyx             x  Studio
Calyx             x  Commission
```

Calyx kolumntitel kollapsar alltså vid 320, som är dess eget golv och det golv planen satte
målvärdet till. Att gå högre än 320 hjälper inte heller: då blir skalan mindre än 0,85 och
texten mindre, inte mer utspridd. Fixen ligger i exempelsajtens egen responsivitet, och
`sites/*.html` redigeras aldrig (planens § Boundaries och Q23). Skärmbild:
`shots/r3/p001-calyx-bare-320.png`. **Lyft till arkitekten**, inte löst här.

### Fixar utöver planerna

| Datum | Beslut | Källa |
|---|---|---|
| 2026-09-10 | **Måttlinjen `#dim-width` flyttad från y 560 till y 505 på den reducerade planschen.** Den löper hela arkets bredd och gick därför rakt genom plan 005:s titelblocksruta (530 till 596) och genom dess mittfält. Att korta linjen vore att göra måttet osant, så det är linjens höjd som flyttar. 505 ger 24 units till kedjans underkant och 25 till rutans överkant | Följdfel av plan 005, mätt med skärningstest i R3 |
| 2026-09-10 | **Måttkedjan flyttad från y 600 till y 480 på den reducerade planschen.** Samma orsak: kedjans ram (560 till 601) låg över titelblocksrutan. Mellanbandet är tomt och gör kedjan till vyns tydliga displayelement | Följdfel av plan 005 mot plan 004 |
| 2026-09-10 | **Legendens träffyta under 768 höjd från 17 px till 44 px** med `padding-block` plus negativ marginal, så att märket står kvar men ytan går att träffa | `preflight_taste` flaggade raderna; mätt till 18 × 17 px. `impeccable/reference/layout.md`: *"Keep touch targets usable even when their visible marks are small"* |
| 2026-09-10 | **`<link rel="preload" as="font" crossorigin>` på Martian Mono**, inte på Chivo | `performance.md` § 2: preload bara för den vikt som står i folden. Titelblocket är det enda i folden vid `--sc-ps` = 0 och det är satt i mono. Skrevs in nu därför att filerna finns; i R2 fanns de inte. **Mätt effekt: LCP 680 ms → 284 ms** |

### Mekaniska grinden

**`detect.mjs`:** **0 fynd.**

**`preflight_taste`:** 7 fynd, alla granskade mot pixlar och mätning, inget tystat.

| Fynd | Bedömning |
|---|---|
| `nav-hojd 900 px (tak 80)` | **Namngivet undantag.** Kontrollen antar att ett nav är en topprad. K3:s nav är en fullhöjd marginallegend och målbilden förbjuder uttryckligen en topprad. Höjden är avsedd |
| `cta-radbrytning` × 6 | **Falskt positivt, mätt.** Kontrollen räknar ankarets tvådelade låda (blocksatt symbolprov över en textrad) som bruten text. Radlådor för enbart textnoderna: **1 rad** för var och en av de sex, vid 1440, 390 och 320. Gate 49 gäller klickbar text som bryts; ingen text bryts |
| `sektionsanatomi: 2 familjer över 7 sektioner` | **Väntat i R3.** Fem av sju sektioner är tomma `<!-- R3 -->`-platshållare. Posten är märkt `not:` och ber själv om en egen läsning |

**`motion_probe`, 4× CPU.** Kontrollen kördes omedelbart före sidan, i samma session:

| Körning | Spår | p95 | > 33 ms | max_step | **staircase** |
|---|---|---|---|---|---|
| **Kontroll** `smooth.html` 100:60 | `#act:--sc-ps` | 16,7 ms | **0** | 1,37 % | **0** |
| **Kontroll** `smooth.html` 100:60 | `#card:transform` | 16,7 ms | **0** | 1,37 % | **0** |
| Sidan 100:60 | `--sc-ps` | 66,7 ms | 123 | **2,02 %** | **0** |
| Sidan 100:60 | `#page-outline` dashoffset | 66,7 ms | 123 | 15,50 % | 1 |
| Sidan 100:60 | `#opening` dashoffset | 66,7 ms | 123 | 12,00 % | 1 |
| Sidan 20:120 | `--sc-ps` | 50,1 ms | 174 | **0,98 %** | **0** |
| Sidan 20:120 | `#page-outline` dashoffset | 50,1 ms | 174 | 2,60 % | **0** |
| Sidan 20:120 | `#opening` dashoffset | 50,1 ms | 174 | — | **0** `DEAD` |

`--sc-ps` klarar baren i båda kadenserna: `staircase = 0` och `max_step ≤ 3 %`. På härledda
spår rapporteras `max_step` men grindar inte (Q22). `#opening` läses `DEAD` vid 20:120
därför att 20 px-hjulet inte hinner in i den banans fönster (`ps` 0,36 till 0,44) under
körningen, inte därför att banan står still.

**Bildtiden klarar inte baren, och nu är kontrollen bevisad ren i samma session.** p95
66,7 respektive 50,1 ms mot taket 20, och 123 respektive 174 rutor över 33 ms mot taket 0,
medan `smooth.html` samtidigt ger 16,7 ms och **noll** rutor över 33 ms. Felet är alltså
sidans, inte maskinens eller strypningens. Orsaken förblir **inte isolerad**: R2:s ablation
över fem lager, körd både en gång per variant och interleavat i tre varv, gav en spridning
inom varianterna som översteg skillnaden mellan dem. Jag namnger fortfarande ingen orsak.

**`perf_probe`, 4× CPU:**

| Post | 1440 | 390 | Budget | Utfall |
|---|---|---|---|---|
| LCP | **284 ms** | 580 ms | ≤ 1800 | klarar |
| CLS | **0,000** | **0,000** | ≤ 0,05 | klarar |
| Överföring | 1710 kB | 1677 kB | ≤ 2500 | klarar |
| DOM | 93 | 92 | ≤ 1500 | klarar |
| Typsnittsfiler | 5 | 4 | ≤ 3 | **klarar inte**, se nedan |
| Hero-bild | 1 122 865 B | samma | ≤ 250 kB | **klarar inte**, se nedan |
| Långa tasks under scroll | 16 | 4 | 0 | **klarar inte** |
| Preload | finns | finns | krävs | klarar, ny i R3 |

`font-files 5` är **två egna plus tre som Calyx laddar från Google Fonts inuti ramen**.
K3:s eget skal laddar exakt två, self-hostade, utan `preconnect`. `hero-image` är Calyx egen
hotlänkade Unsplash-bild inuti ramen; K3 har noll egna bilder. Båda posterna mäter
exempelsajtens skuld genom K3:s ram och kan inte åtgärdas utan att redigera `sites/*.html`.

**`scroll_verify`:** `cuesNeverFull` **tom**, `unrevealed` **tom**, `contrastUnderMedia`
**tom**. `deadScroll` 12 band och `blankBands` 128 → 5850: det första bandet (0 → 300) är
**den författade tystnaden**, deklarerad i `BRIEF.md`; resten ligger i R3-platshållarna, som
är tomma med avsikt. Ingetdera tystas.

**`contrast_over_media`:** kunde inte köras. Skriptet ignorerar `--url` och går mot
`http://localhost:3055/`, som ger `ERR_CONNECTION_REFUSED`. Sakläget: **sidan har ingen yta
med text över bild.** Enda mediet är exempelsajten i sin ram, och ingen K3-text ligger över
den; bildtexten sitter på papperet under öppningen. `scroll_verify`s egen
`contrastUnderMedia` är tom, vilket är samma kontroll från andra hållet. Verktygets
port-default rapporteras som ett fynd till lead.

### Lästa skärmbilder

Alla i `shots/r3/`, lästa som bilder.

- läst: `p001-filled-390.png` — ramen fylld, men Calyx egen rubrikrad överlappar (orsak ovan)
- läst: `p001-calyx-bare-320.png` — attribueringen, Calyx naken vid 320
- läst: `p002-filled-390.png` — hela den låsta raden syns, slutar på `Stockholm`, luft till kanten
- läst: `p003-drawn-1440.png` — `16:9` helt läsbart i fria spalten, båda snittpilarna kvar
- läst: `p004-drawn-390.png` — `320 768 1440` i displayblått på en rad, inget streck pekar på dem
- läst: `p005-sheet-390.png` — exakt två saker: papperet och en rutad titelblocksruta i hörnet
- läst: `drawn-375.png` — hela den reducerade planschen samlad och läsbar
- läst: `drawn-768.png` — 1440-planschen letterboxad, hårlinjerna överlever, mellanplanschen saknas fortfarande

### Öppet efter R3

- **Calyx överlapp vid 320** blockerar plan 001:s sista led. Ligger i `sites/calyx.html`.
- **Mellanplanschen 768 till 1023** (`ASSETS.md` § A.8 rad 2) är fortfarande inte byggd.
- **Bildtidsbudgeten** klaras inte och orsaken är inte isolerad.
- **`contrast_over_media.py` ignorerar `--url`** och går mot port 3055.
- `[needs asset: assets/logo-black.svg]` för a6, som byggs i R3:s innehållsrunda.

---

## R2 · Folden och signaturakten

Byggarens rader, 2026-09-10. En rad per beslut: datum, beslut, källa.

### Avvikelser från målbilden, med källa

| Datum | Beslut | Källa |
|---|---|---|
| 2026-09-10 | **`data-sc-span` 4.0, inte målbildens 2.4.** Motorn sätter akthöjden till `span * vh` och den **pinnade** resan blir `(span - 1) * vh`. 2.4 ger alltså 1,4 vh = 1260 px för fjorton ritsteg, 90 px per steg, mindre än ett hjulhack. **Mätt vid 2.4:** `--sc-ps` max_step 3,44 % mot barens 3 %. 4.0 ger 2700 px resa, 162 px per linjesteg, och **mätt max_step 2,02 %** vid hjul 100:60 och **0,84 %** vid 20:120 | `motion-smoothness.md` § The bar (max_step ≤ 3 % är en hård grind) mot planens § 7.5 (spannet är ett riktvärde). Grinden vinner. `scroll/pace.md`: för snabbt läser som billigt. Akten har fortfarande sidans största spann med bred marginal (`feel-and-fingerprint.md` § The peak) |
| 2026-09-10 | **`#cut-AA` ritas som en enda obruten bana** `M48 220 V180 H1392 V220`, alltså upp för vänsterbenet, tvärs över, ner för högerbenet. ASSETS.md § A.6 steg 2 skriver "från vänster till höger, sedan benen nedåt" | ASSETS.md § A.3 kräver att varje pil är `marker-start`/`marker-end` på **ett** `<marker>`, och att det finns exakt ett `<marker>`-element i filen. Med tre separata banor får bara den första och sista änden en markör; med en obruten bana pekar båda spetsarna nedåt av sig själva via `orient="auto-start-reverse"`. Ritordningen blir dessutom mer bokstavligt "en enda obruten hand" (BRIEF.md § Motion-tes, Continuity) |
| 2026-09-10 | **`#m-1440` sätts vid x 1416, inte ASSETS.md:s 1430.** `letter-spacing: 0.02em` lägger ett spatium **efter** sista glyfen, så ett `text-anchor="end"` vid 1430 sköt sista nollan förbi arkets kant | Mätt i R2, pixelläst i `shots/r2/drawn-1440.png`. ASSETS.md § A.5 anger 1430; avvikelsen är 14 user units och bevarar utropets roll |
| 2026-09-10 | **`#c-169` och `#lead-16-9` flyttade in från 1424 till 1412.** Samma orsak: utropet klipptes av ytterkonturen | Samma mätning |
| 2026-09-10 | **`#lead-marginal` och `marginal` flyttade från y 396 till y 268.** Legenden är fixerad och vertikalt centrerad; vid 1440 × 900 låg den gamla punkten rakt under legendraden DETALJER. Ett utrop som ett annat element täcker är ett utrop utan roll | Mätt i R2, pixelläst i den första `drawn`-bilden. ASSETS.md § A.5 anger y 396 |
| 2026-09-10 | **Fem registrerade lokaler (`--l`, `--t`, `--thin`, `--fill`, `--fall`) i stället för en per bana (`--l1` till `--l14`).** Varje bana sätter sitt **eget fönster** i samma namn; `inherits: false` gör dem oberoende av varandra. Mekaniken blir en rad CSS och `?preview=drawn` blir en regel i stället för fjorton | ASSETS.md § A.6 kräver `@property { syntax: "<number>" }` per lokal, vilket är uppfyllt. Kravet gäller registreringen, inte antalet namn. `motion-smoothness.md` § Fault 1 |
| 2026-09-10 | **Allt läser `--sc-ps`, även utropens opacitet.** BRIEF.md § Motion-tes säger att cue-opacitet får läsa rå `--sc-p`. En opacitet som stegar vid varje hjulhack läser som flimrande text, och `--sc-ps` är strikt jämnare utan att någon regel förbjuder det | **F-014** regel 1 kräver `--sc-ps` för allt som förflyttar sig och **tillåter** `--sc-p` för cue-opacitet; den kräver det inte. Strängare är aldrig fel |
| 2026-09-10 | **`color-mix` sker i `srgb`, inte i `oklch`.** Tokens är fortfarande oklch; bara interpolationsrummet är bytt, på de två blandningar som körs per frame (pilspetsarnas intoning, måttsiffrornas färgfall) | `performance.md` § 3 (skär arbetet per frame). Skillnaden i resultat är omätbar på en 12 px-siffra; skillnaden i arbete per frame är det inte. **Notera:** ändringen gav ingen mätbar vinst i bildtid, se § Mätningar |
| 2026-09-10 | **Legenden tonar in först när första kapitlet närmar sig**, i stället för att finnas från start | BRIEF.md § Direction contract, FIRST VIEWPORT är **låst** till exakt två saker, papperet och titelblocket, och räknar uttryckligen upp "ingen legend". Första bygget bröt låset; mätt i `shots/r2/sheet-1440.png` |
| 2026-09-10 | **Legendens rader har papperskulör bakom sig.** Raderna ligger i marginalzonen, som är skrafferad, och 12 px mono på en 45-gradig skraffering är inte läsbart | Ritpraxis: ett utrop som ligger på en skraffering bryter skrafferingen. Det är **inte ett kort** (TASTE § 2.3, F-006): ingen radie, ingen kant, ingen skugga, ingen elevation, ingen egen yta utöver papperets egen färg |
| 2026-09-10 | **Ledarlinjen dras med `transform: scaleX()`, aldrig med `width`.** Första bygget animerade `width` | `detect.mjs` flaggade `layout-transition: transition: width` direkt vid skrivning. `performance.md` § 3: animera `transform` och `opacity`, allt annat kostar layout eller paint per frame |
| 2026-09-10 | **`stroke-dashoffset` skrivs med explicit enhet:** `calc((1 - var(--l)) * 1px)` och `stroke-dasharray: 1px` | Utan enheten serialiserar Chromium det beräknade värdet som `calc(1px)` respektive `0%`, alltså två olika typer, och `motion_probe.py` kunde inte parsa någondera: **proben rapporterade `DEAD` på en bana som ritade sig korrekt på skärmen.** En rörelse som inte går att mäta är inte verifierad, hur rätt stillbilden än ser ut (F-014, lärdomen om en prob som kan godkänna en död sida) |
| 2026-09-10 | **Skrafferingens linje färgas via en CSS-regel** `#hatch line { stroke: var(--ink-hair) }` | `currentColor` inuti ett `<pattern>` resolveras mot mönstrets **egen** ärvda `color`, alltså mot `<svg>`-roten, inte mot den refererande rektangeln. Mätt i R2: skrafferingen ritades i `--ink` och läste dubbelt så tung som hjälplinjerna bredvid |
| 2026-09-10 | **`transform-box: fill-box` på måttsiffrorna, med `transform-origin` per siffra.** ASSETS.md § A.6 steg 14 kräver origo vid varje siffras egen baslinje men anger ingen mekanik | Utan `fill-box` ligger origo i SVG:ns user-space-nollpunkt, så siffran skalar mot arkets övre vänstra hörn. **Mätt:** alla tre siffrorna landade under titelblocket i första `filled`-bilden |
| 2026-09-10 | **Previewlägena skriver måttsiffrornas måltal direkt.** Motorns `count` skriver bara `textContent` medan akten är live och progressen ligger i countfönstret; ett fruset previewläge sätter CSS-lokalerna men aldrig talet | Mätt: siffrorna stod på `0` i den bild F-007-kontrollen läser. Målet läses ur elementets eget `data-sc-count`, så inget tal kan uppstå som inte redan står i markupen (PRODUCT.md § Absences) |
| 2026-09-10 | **Två planscher i R2, inte tre.** Hela inventariet vid 768 och uppåt, den reducerade vid 320 till 767. Mellanplanschen 768 till 1023 som ASSETS.md § A.8 specificerar är **inte byggd** och står som öppen nedan | ASSETS.md § A.8. Den reducerade planschens geometri ligger i en mediafråga; `viewBox` sätts av JS eftersom det är ett attribut och inte en CSS-egenskap |
| 2026-09-10 | **Utropens position per plansch sätts med attribut i JS, inte i CSS.** `x` och `y` är CSS-geometriegenskaper på `<rect>`, `<image>`, `<foreignObject>` och `<use>`, men **inte på `<text>`**: en CSS-regel mot dem ignoreras tyst | Mätt i R2: alla utrop försvann ur den reducerade planschen därför att de satt kvar på sina 1440-koordinater, utanför den nya viewBoxen |

### Varje ritad bana och dess roll (gate 79-kontrollen)

Nitton ritade element i `#drawing`. Var och en kan namnges som kontur, snittmarkering,
måttlinje, hjälplinje, ledare, skraffering eller utrop. Ingen kan namnges som knapp, text,
navrad, formulär, graf, sparkline eller enhetsram.

| # | id | Element | Klass, alltså roll | Vad den är |
|---|---|---|---|---|
| 1 | `#page-outline` | `path` | **kontur** 1.5 | Den ritade sidans ytterkontur, 1440 bred |
| 2 | `#opening` | `path` | **kontur** 1.5 | Den måttsatta öppningen, 880 × 495 = 16:9 |
| 3 | `#cut-AA` | `path` | **snittmarkering** 2.5 | Snittet A-A, pil i båda benens ändar |
| 4 | `#guides` > `path` | `path` | **hjälplinje** 0.75 dash | Spalt A vänster och höger, spaltavståndets högerkant |
| 5 | `#ledgers` > `path` | `path` | **hjälplinje** 0.75 dash | Liggarens tre rader, delning 96 |
| 6 | `#exts` > `path` | `path` | **hjälplinje** 0.75 dash | Två förlängningslinjer vid x 320 och 768 |
| 7 | `#hatch-marginal` | `rect` | **skraffering** | Marginalzonen, 45 grader, delning 8 |
| 8 | `#dim-width` | `path` | **måttlinje** 0.75 | Totalbredden, stationskedja |
| 9 | `#stations` > `path` | `path` | **måttlinje** 0.75 | Stationsstrecken vid 320 och 768 |
| 10 | `#dim-gutter` | `path` | **måttlinje** 0.75 | Spaltavståndet, 7 rem |
| 11 | `#dim-row` | `path` | **måttlinje** 0.75 | Liggarens raddelning, 96 px |
| 12 | `#lead-16-9` | `path` | **ledare** 0.75 | Från öppningens hörn till utropet 16:9 |
| 13 | `#lead-marginal` | `path` | **ledare** 0.75 | Från marginalzonen till zonnamnet |
| 14 | `#dot-16-9` | `circle` r=1 | **ledare**, punkt | Ledarens målände. Aldrig en pilspets |
| 15 | `#dot-marginal` | `circle` r=1 | **ledare**, punkt | Samma |
| 16 | `#title-block` (3 `text`) | `text` | **utrop** | `ALUNIX` · `SEKTION A-A` · `SKALA 1:1` |
| 17 | `#cut-a-l`, `#cut-a-r` | `text` | **utrop** | Snittbokstäverna `A` och `A` |
| 18 | `#c-gutter`, `#c-row`, `#c-169`, `#c-marginal`, `#c-spalt`, `#c-fold`, `#c-calyx` | `text` | **utrop** | `7 rem` · `96 px` · `16:9` · `marginal` · `spalt` · `fold` · den ordagranna Calyx-raden |
| 19 | `#m-320`, `#m-768`, `#m-1440` | `text` | **utrop**, displaygrad | De tre sanna måtten, enda kromatiska på arket |

Plus **ett** `<marker id="arrow">` (ISO 129 closed filled, 9 × 3) och **ett**
`<pattern id="hatch">`. Ingen andra pilspetsform, ingen fjärde linjebredd, ingen andra
dash-form, ingen roterad text, noll `box-shadow`, noll gradient, noll radie.
`<foreignObject>` innehåller **ett riktigt gränssnitt**, inte ett ritat: exempelsidan Calyx
live i en `<iframe>` från samma origin.

### Mätningar

**`motion_probe.py`, 4× CPU, nedåt.** Spårat: aktens `--sc-p`, aktens `--sc-ps` och
`#page-outline:stroke-dashoffset`.

| Hjul | värde | p95 | frames > 33 ms | max_step | **staircase** |
|---|---|---|---|---|---|
| 100:60 | `--sc-p` (rå) | 91,7 ms | 106 | 6,41 % | **17** |
| 100:60 | `--sc-ps` | 91,7 ms | 106 | **2,02 %** | **0** |
| 100:60 | `#page-outline` dashoffset | 91,7 ms | 106 | 14,70 % | **0** |
| 20:120 | `--sc-p` (rå) | 50,0 ms | 157 | 3,51 % | **9** |
| 20:120 | `--sc-ps` | 50,0 ms | 157 | **0,84 %** | **0** |
| 20:120 | `#page-outline` dashoffset | 50,0 ms | 157 | **2,50 %** | **0** |

**Uppåt**, egen mätning (`motion_probe.py` driver bara nedåt), 4× CPU, samma kadenser:

| Hjul | `--sc-ps` staircase | `--sc-ps` max_step | Verkan |
|---|---|---|---|
| −100:60 | **0** | 6,61 %* | Ritningen suddas helt: `ps` 0,964 → 0, dashoffset 0 → 1 |
| −20:120 | **0** | 3,30 %* | Delvis resa, `ps` 0,999 → 0,591 |

\* Min uppåtprob samplar var 60:e respektive 120:e ms, alltså inte per frame som
`motion_probe.py`. Den aliasar därför flera frames till ett steg och `max_step` är **inte
jämförbart** med tabellen ovan. `staircase` är det, och det är noll i båda riktningarna.

**Domen på rörelsen.** `staircase = 0` på **varje** utjämnat värde, i **båda**
riktningarna, vid **båda** kadenserna. Det är talet som namnger F-012-felet och det är
uppfyllt. `--sc-ps` klarar 3 %-baren med marginal i båda kadenserna. `--sc-p` stegar 9 till
20 gånger, vilket är precis vad shimen finns för och bevisar att den arbetar.

**`max_step` på en enskild banas dashoffset är kadensbunden och inte ett fel.** En bana
ritas över sitt eget fönster, som är en bråkdel av akten: `#page-outline` äger `ps`
0,12 → 0,22, alltså 0,10 × 2700 px = 270 px. Ett hjulhack på 100 px är då 37 % av den banans
egen resa, och proben mäter `max_step` som procent av **värdets eget** spann. Vid 20 px hack
faller samma tal till 2,50 % och banan klarar baren. Aritmetiken är skalinvariant: att bredda
akten flyttar båda talen lika mycket. `staircase = 0` är därför diskriminatorn här, inte
`max_step`, och den är noll vid båda kadenserna.

**`perf_probe.py`, 4× CPU, 1440 × 900:**

| Post | Mätt | Budget | Utfall |
|---|---|---|---|
| LCP | **672 ms** | ≤ 1800 ms | klarar |
| CLS | **0,000** | ≤ 0,05 | klarar |
| Överföring | **1641 kB** (inkl. Calyx-ramen) | ≤ 2500 kB | klarar |
| DOM | **91 noder** | ≤ 1500 | klarar |
| Långa tasks under scroll | **9** | 0 | **klarar inte** |
| Hero-bild | **1 122 865 B** från `images.unsplash.com` | ≤ 250 kB | **klarar inte** |
| Typsnittspreload | saknas | krävs | **klarar inte**, se `[needs asset:]` |
| Bildtid p95 under scroll | **50 till 92 ms** | ≤ 20 ms | **klarar inte** |
| Frames > 33 ms | **86 till 157** | 0 | **klarar inte** |

Hero-bilden är **Calyx egen hotlänkade Unsplash-bild inuti ramen**, inte K3:s material.
K3 har noll egna bilder. Detta är F-013:s sidofynd, mätt igen, i kedjans egen exempelsajt.

**Bildtiden: vad jag mätte och vad jag inte kunde fastställa.**

1. **Ramen är inte orsaken.** Samma skriptade hjul, samma körning, enda skillnaden att
   iframens sub-resurser blockerades på nätverksnivå: p95 **50,1 ms** med ram mot
   **50,0 ms** utan, frames > 33 ms **94** mot **95**. Nollresultat.
2. **Baren är nåbar och instrumentet fungerar åt båda hållen.** Under identiska villkor
   (4× CPU, hjul 100:60) ger `tests/motion/smooth.html` **pass**, noll frames > 33 ms,
   staircase 0, max_step 1,36 %; `tests/motion/staircase.html` ger **fail**, staircase 18.
   Bildtidsfelet i K3 är alltså verkligt och inte en artefakt av strypningen.
3. **Orsaken inom K3 är INTE isolerad.** Jag ablerade fem lager (papperstextur, hela SVG:n,
   `color-mix`-strokarna, `clip-path`-wiparna, `stroke-width`-animeringen), först en gång
   per variant och sedan interleavat i tre varv för att kontrollera för drift. **Spridningen
   inom en variant översteg skillnaden mellan varianter i båda uppläggen** (baslinjen
   `over33` 86 till 97, variant C 84 till 100). Den enda signal som återkom var att
   `color-mix`-varianten hade lägst median-p50 i två av tre varv, och det är för svagt för
   att kallas en mätning. Jag gjorde srgb-ändringen ändå, eftersom den är mindre arbete per
   frame oavsett vad mätningen säger, och **den gav ingen mätbar vinst**. Jag namnger därför
   ingen orsak. Att peka ut den variant som råkade se bäst ut vore att hitta på ett resultat
   som datat inte bär, vilket är exakt felet F-013 rättade åt andra hållet.

**`scroll_verify.py`:** `cuesNeverFull` tom, `unrevealed` tom, `contrastUnderMedia` tom,
`notes` tom. `deadScroll` rapporterar 0 → 300 px (diff 0,0012), vilket är **den författade
tystnaden**, deklarerad i BRIEF.md § Feeling curve och i akten själv. Övriga
`deadScroll`-band och hela `blankBands` (128 → 5850) ligger i R3-platshållarna, som är tomma
med avsikt i den här rundan. **Ingetdera tystas.**

**Vad jag läste i kontaktarket** (`shots/r2/sheet.png`, arton positioner): tomt ark med bara
titelblocket i ruta 1 och 2; ytterkontur och snittmarkering i ruta 3; hjälplinjer i ruta 4;
öppningens kontur i ruta 5; liggarrader och mått byggs i ruta 6 och 7; **ruta 8 fångar
räknaren i flykten på `129` · `738` · `88`**, alltså verkliga mellanvärden och inte ett hopp
till målet; ruta 9 och 10 visar `320` · `768` · `1440` landade; ruta 11 visar Calyx
kolumntitel tona in innanför konturen; ruta 12 visar sajten hel med bläcket kvar som ram;
ruta 13 visar siffrorna fallna till marginalgrad; ruta 14 och framåt är R3-platshållarna med
legenden tänd i vänstermarginalen. Det svarta fältet nederst till höger är kontaktarkets
egna ofyllda rutor (18 positioner i ett rutnät om 20), inte sidan.

**Vad jag läste i skärmbilderna.** `sheet-1440`: exakt två saker, papperet och titelblocket,
ingen legend, ingen kontur, ingen cue. `drawn-1440`: hela inventariet, måttkedjan i blått,
och varje märke på arket går att namna i tabellen ovan; noll låtsas-UI. `filled-1440`: Calyx
live innanför konturen, bläcket kvar som ram, och sajten är det enda mättade i vyn.
`drawn-390` och `filled-390`: den reducerade planschen är läsbar där den fulla var en
utsmetad remsa.

### Routningsluckan, och vad varje route gav

Stop-hooken flaggade tre starka routes som matchade riktig kod utan att laddas:
`a11y-audit`, `animated-navigation`, `emil-design-eng`. F-014:s efterspel är precis den
här situationen: när `emil-design-eng` hoppades över i r7 föll tre buggar ut, varav en
frös akten på varje sida som använde shimen.

| Route | Status | Utfall |
|---|---|---|
| `emil-design-eng` | **R3** | R2-promptens § 7 i r8-kedjan schemalägger den till R3 tillsammans med `review-animations`. Inte hoppad, schemalagd |
| `a11y-audit` | **R3** | Samma. Sidan har i R2 en skip-länk, `:focus-visible` på legendens rader, `aria-current` som statusmarkör (inte färg), `role="img"` med `<title>` och `<desc>` på ritningen, och `aria-label` per sektion. Ingen av dem ersätter granskningen |
| `animated-navigation` | **Laddad i R2** | Legenden är ny kod ur den här rundan, så routen hörde till R2 och inte till R3. Utfall nedan |

**`animated-navigation`, utfall.** Skillen beskriver ett specifikt projekts header:
`bg-black/95`, `backdrop-blur-md`, sticky topprad, utrullande pill-tab i accentfärg,
glas-dropdown med `rounded-b-2xl` och `shadow-[0_40px_80px_-15px]`, plus en flygande
pil-bild som utgår från en logotyp. **Nästan allt är en avvisning för K3:** cellen har
ingen topprad alls (målbilden förbjuder den), inga dropdowns, inga pillformer, noll glas,
noll `backdrop-filter`, noll skugga, noll radie (TASTE § 5, F-006) och ingen logotyp att
flyga från. Skillen får bidra med hantverksvokabulär, aldrig med riktning
(`design/SKILL.md` § Demoted skills).

Två regler bekräftade det som redan var byggt: ledarlinjen har `pointer-events: none` så
den aldrig fångar ett klick, och kurvan är fast-start med mjuk inbromsning
(`cubic-bezier(0.23, 1, 0.32, 1)`), inte linjär och inte studsande.

**En regel fann en riktig bugg.** § The Standard Underline: *"Active state: scale-x-100
transition-none — always visible, no animation needed."* K3:s ledarlinje animerades alltid
fram, även när tillståndet redan gällde vid ankomst: djuplänkas sidan till `#liggaren`
gled ledaren ut vid landning, alltså en animation av något som aldrig ändrades. Fixat med
`.legend__lead.is-instant { transition: none }`, satt före första `markActive()` och
borttagen efter två frames. **Ändringen är skärmbildsneutral** (den styr om en övergång
körs, inte sluttillståndet), så inga bilder i `shots/r2/` behövde tas om.

### Öppet efter R2

- `[needs asset: assets/chivo-var.woff2]` och `[needs asset: assets/martian-mono-var.woff2]`.
  Båda står som `[needs: vendor]` i `assets/ASSETS.md` § C och vendoras av lead (F-009).
  `@font-face` pekar redan på de slutliga filnamnen, så sidan blir rätt i samma ögonblick
  filerna landar. **Alla skärmbilder i `shots/r2/` visar fallback-stacken, inte den valda
  typografin.** `<link rel="preload">` skrivs in när filen finns; `perf_probe` flaggar
  `no-font-preload` tills dess, och det är väntat.
- `[needs asset: assets/logo-black.svg]`. Används i exakt en förekomst i a6, som är R3.
- **Mellanplanschen 768 till 1023** (ASSETS.md § A.8 rad 2) är inte byggd. R2 har två
  planscher; den tredje är R3.
- **Öppningens ram ger Calyx en 272 units bred layoutviewport på den reducerade planschen**,
  alltså under 320 px-golvet, och Calyx egen kolumntitel överlappar där. Mätt i
  `shots/r2/filled-390.png`. Nästa konkreta steg i R3: låt ramen layouta vid 320 px och
  skala ner den statiskt vid montering med `272/320`. En **statisk** skala satt vid
  montering är inte samma sak som att transformera en ram efter att den visats
  (PRODUCT.md § Operating Context); skillnaden skrivs ut i ledgern när den byggs. Samma
  lösning gäller a3:s tre plates och bör göras en gång.
- **Calyx-bildtexten klipps i högerkant på den reducerade planschen.** Den ordagranna raden
  `Exempelsida: Calyx, florist i Stockholm` behöver ~290 user units i fallback-monon och
  planschen är 320 bred; med Martian Mono, som är bredare, klipps den mer. Raden är låst
  copy och får inte kortas. Nästa konkreta steg i R3: `textLength` med
  `lengthAdjust="spacingAndGlyphs"` på just den raden i den reducerade planschen, alltså ett
  utrop som passas in i sitt utrymme, vilket är ritpraxis och inte en ny typinställning.
  Mätt i `shots/r2/filled-390.png`.
- **Bildtidsbudgeten är inte nådd** och orsaken är inte fastställd. Se § Mätningar punkt 3.
  R3 äger att mäta med ett stabilare upplägg, förslagsvis Chromes egen tracing i stället för
  rAF-sampling, innan någon ändring görs.
- Alla åtta `sites/*.html` laddar `cdn.tailwindcss.com`, som loggar en produktionsvarning i
  konsolen så fort en av dem monteras i en ram. Kedjans egna exempelsajters skuld, inte
  K3:s, men den syns i K3:s konsol.
- `C:\Users\ANTONL~1\AppData\Local\Temp\inspect.py` skuggar stdlib-modulen `inspect` och får
  varje Python-körning med den katalogen som cwd att krascha i importen. Inte designarbete,
  men det stoppade en mätning i den här rundan.

---

## Byggarens rader

`[fylls i R1]` — en rad per materiellt beslut byggaren fattar, i samma format: datum,
beslut, källa. Obligatoriskt att skriva in här, utover det byggaren själv väljer:

- De fem live-rubrikerna med källdomän, och en mening om vad ribban faktiskt är.
- Legendens fem kapitelnamn, ordagrant.
- Tjänsternas tre underrader, ordagrant (QUESTIONS.md Q6).
- Utfallet av den omkörda `select.py`, och en avvikelserad om raden skiljer sig.
- De fyra sömkontrollernas mätta värden ur `assets/ASSETS.md` § B.3.
- `contrast_over_media.py`-siffran för `--ink` på texturerad grund, per grund i R3.
- `motion_probe`-siffrorna: `staircase`, `max_step`, frametid p95 och antal frames > 33 ms,
  bada scrollriktningarna, med `--wheel 20:120` och `--wheel 100:60`.
- Den mätta överföringen vid 1440 och de tre exempelsajternas egna tal.
- `--hair`-undantaget under 768, som en egen rad.

## R1, leadens rader (2026-09-10)

| Datum | Beslut | Källa |
|---|---|---|
| 2026-09-10 | R1 godkänd utan retur. Referensgolvet uppfyllt, noll gate-deny, noll UI-filer, senaste catalogue-select-raden stämmer med fas 0 | Leadens mekaniska kontroll mot sessionsledgern plus arkitektens dom |
| 2026-09-10 | Byggarens första catalogue-select-rad mot det ofyllda skelettet var en alfabetisk nollrad. Golvet läser sista raden, så låset håller. Alla tre cellerna gjorde samma sak, inte bara V3c | `hooks/design-gate.py` referensgolv; K4:s fråga B1 |
| 2026-09-10 | Ingen Stop-rapport skrevs för R1, och route-gapet har därför ingen artefakt. R1 skriver noll UI-filer och alltså noll route-rader, så måttet är inte meningsfullt förrän R2 | GOALS mätpunkt 2; arkitektens öppna punkt 7 |

## Bevakarens observation inför F-007 (R2, 2026-09-10)

Läst som pixlar av bevakaren vid 1440: vila (ps = 0) och `?preview=drawn`. Det formade läget
matchar målbilden: sektionsritning på kallt papper, sanna mått, stationstalen 320/768/1440 som
enda blå moment (Q15-antagandet tillämpat), inga fotografier, Chivo + Martian Mono. Två punkter:
1. Folden i vila är nästan tomt papper: bara titelblocket (ALUNIX / SEKTION A-A / SKALA 1:1) syns
   innan p lämnar 0. `devices.md` § "Ground or greet" och `scroll_verify`s `blankBands`-kontroll
   (en enfärgad yta över 60 % av en vyport i helsidesbilden) träffar precis det här. Avgör om
   snittlinjen och platens kontur ska ligga förinkade vid p = 0 och bara måttkedjorna ritas på
   scroll, eller om en greet-cue bär folden. Ett svar ska stå i decision ledger innan R3.
2. Etiketten `16:9` uppe till höger kolliderar med snittpilen A (läses som `1_:9`). Fix i R3
   med målvärde: etiketten flyttas 24 px vänster om pilens fot eller pilen kortas.

## R2, leadens rader (2026-09-10)

| Datum | Beslut | Källa |
|---|---|---|
| 2026-09-10 | Typsnitten var **ovendorade under hela R2**. Cellens `@font-face` pekade på filer som inte fanns, så varje skärmbild och varje mätning i rundan, byggarens egna inräknade, togs mot fallback-stacken. Lead har nu vendorat dem och bekräftat att de laddar | F-009: lead vendorar material. R1-briefens `[needs: vendor]`-rad var min att stänga och blev liggande |
| 2026-09-10 | `motion_probe` faller i alla tre cellerna, men **staircase är 0 överallt**. Det som fallerar är bildtid, alltså F-013:s andra fel, inte F-014:s första | Leadens egna körningar, hjul 100:60, cpu 1 och cpu 4 |
| 2026-09-10 | Alla mätvärden i rundan ska tas om i fixrundan, eftersom de togs mot fel typsnitt | Samma rad som ovan |
| 2026-09-10 | F-007 **avvikelse**. Akt-koordinater: a1 p 0,55 till 0,78 (måttkedjan saknas vid 390), a1 p 0,72 till 0,80 (`16:9` täcks av snittpilen, båda bredderna), a1 p 0,78 till 1,0 (öppningen och den låsta bildtexten vid 390) | Arkitektens F-007-kontroll mot leadens pixlar |
| 2026-09-10 | Den författade tystnaden bär vid 1440 men inte vid 390: tre monorader i överkanten på ett tomt fält läser som en sida som inte laddat. Titelblocket flyttas under 768 till nedre högra hörnet som på en riktig ritning, så FIRST VIEWPORT-låset hålls intakt | Arkitektens dom, plan 005 |

## Bevakarens observationer inför F-007 (R3 fixrunda, 2026-09-10)

Läst som pixlar: `review/r3/K3-filled-390.png`. Arkitekten dömer; det här är vad bilden visar.

1. Planerna 002, 004 och 005 syns utförda: bildtexten hel, måttkedjan `320 · 768 · 1440` på plats under öppningen, titelblocket i nedre högra hörnet på papper.
2. Plan 001 (`best-effort`): ramen i öppningen visar Calyx egen mobilnav mosad över ordmärket (`VOLUME`/`INDEX`/`STUDIO`/`COMMISSION` ovanpå varandra kring `Calyx`). Det är exempelsajtens kalibreringsbrist vid smal layoutvyport (Q23), inte K3:s, men vid 320 px layoutvyport blir den mycket synlig. Arkitekten avgör om layoutvyporten ska vara 1440 skalad (som K4 valde) i stället för 320, vilket skulle dölja bristen utan att röra exempelsajten.
3. Plan 003: utropet `16:9` står nu fritt uppe till höger med ledare till ramens hörn; ingen kollision syns.

## R3, leadens pixelläsning (2026-09-10)

- läst: `tests/alunix-r8/review/r3/K3-fold-390.png`
- läst: `tests/alunix-r8/review/r3/K3-filled-390.png`
- läst: `tests/alunix-r8/review/r3/K3-filled-1440.png`

### Leadens beslut, R3 (2026-09-10)

| Datum | Beslut | Källa |
|---|---|---|
| 2026-09-10 | Planerna 002, 004 och 005 `verified`. Plan 003 accepterad avvikelse: byggaren mätte att arkitektens `y = 186` lade utropets ram över snittlinjens vågräta löp, och flyttade till y 256; planens egen princip kräver då att etiketten flyttar längre, inte att den stannar | Arkitektens F-007-dom mot pixlarna |
| 2026-09-10 | Plan 001 **kvarstår**. Attribueringen till Calyx egen layout är riktig, men den bevisar orsaken, inte att målet är onåbart: `sites/calyx.html` har en `grid-cols-12`-header utan responsiv brytning och alltså inget 320-golv. K4 löste samma problem i samma runda med fast layoutvyport plus statisk skala. Ny plan 006 ersätter 001 | Arkitektens läsning av `sites/calyx.html` rad 61 till 68 |
| 2026-09-10 | `preflight_taste` sju fynd dömda: `nav-hojd` 900 px är ett namngivet undantag, eftersom kontrollen antar en topprad och cellens nav är en fullhöjds marginallegend som målbilden kräver; de sex `cta-radbrytning` är falska positiv, kontrollerade i pixlar, ingen etikett bryter rad | Arkitektens dom mot gate 49:s ordalydelse |
| 2026-09-10 | Den tysta folden vid 390 bär nu. R2-avvikelsen är stängd av plan 005 | Arkitektens dom mot `K3-fold-390.png` |

# BRIEF — Alunix r8, cell K3 · Ritningen · ritningen blir sidan

Skelettet är skrivet av arkitekten. Fält märkta `[fylls i R1]` fyller **byggaren** i runda
1. Fält utan den märkningen är låsta och ändras bara med en ny rad i decision ledger som
namnger källan (F-post, TASTE-§, katalogpost, planparagraf).

Målbilden är `tests/alunix-r8/malbilder/K3.md` (planens § 7.5, ordagrant) och den är
bindande. Målbildsgrinden i sin helhet: `tests/alunix-r8/concepts-K3.md`. Ritningens
fullständiga geometri, linjehierarki och ritordning: `runs/K3/assets/ASSETS.md`.

**F-011 gäller:** rörelsen spelar alltid. Det finns inget reduced-motion-fält i det här
skelettet, ingen `prefers-reduced-motion`-plan och inget statiskt reservläge. Fältet är
borttaget med avsikt, inte glömt.

---

## catalogue-select

```
catalogue-select: squarespace, aevi-wellness, beautiful, insign, mode
```

Skriven av `python scripts/catalogue/select.py --brief tests/alunix-r8/runs/K3/BRIEF-draft.md --k 4 --wildcard --explain`
till `.impeccable/design-session.jsonl`. Primär = `squarespace`. Wildcard = `mode`
(`split stage`, utanför kategorin). Full utdata och poäng står i `concepts-K3.md`
§ catalogue-select, tillsammans med det mekaniska skälet till att planens § 7.5-lista
(`caractere-bois`, `hyperborea`, `wild`, `garden-eight`, `tidvatten`) inte föll ut.
**Byggaren kör om samma kommando i sin egen session** och rapporterar avvikelse; vid
avvikelse gäller raden ovan. Anti-referens: `sites/before-ai-slop.html`.

### Byggarens omkörning, R1

Jag körde först kommandot som R1-prompten skrev det, alltså mot `BRIEF.md` i stället för mot
`BRIEF-draft.md`. **Det gav en annan rad.** Hela utdatan, ordagrant:

```
Brief: tests\alunix-r8\runs\K3\BRIEF.md  ->  4 poster

    6  aarke                    warm photographic      gallery/catalog
       +6 fritext (bar, cta, editorial, headlines)
    6  aevi-wellness            modern clean           chaptered editorial
       +6 fritext (accent, editorial, headlines, hero)
    6  alet                     editorial print        gallery/catalog
       +6 fritext (accent, category, editorial, image)
    6  altitude-beverages       editorial print        chaptered editorial
       +6 fritext (can, display, gradient, itself)

Mediastrategi ur posternas egna falt (Photo search) - locken ska inte gissa:
  - aarke: Unsplash first, Pexels second. - "kitchen counter natural light product styled" - "coffee maker steel kitchen morning light" - "marble count
  - aevi-wellness: Unsplash first, Pexels second. - "skincare bottles overlapping flat lay natural light" - "dropper bottle apothecary product close up" - "min
  - alet: Unsplash first, Pexels second. - "editorial product photography warm natural light" - "interior photography natural light desaturated" - "på
  - altitude-beverages: Unsplash first, Pexels second. - "beverage can product shot gradient background studio" - "condensation can drink close up" - "rosemary garn

catalogue-select skriven: aarke, aevi-wellness, alet, altitude-beverages  ->  C:\Users\Anton L\anti-slop-design\.impeccable\design-session.jsonl
```

**Orsaken är mekanisk och kontrollerad, inte en oenighet om urvalet.** `select.py` poängsätter
en brief på fyra axlar som läses ur rubrikfält (`register`, `grammar`, `category`, `mode`,
`authority`) plus fritext. `BRIEF.md` är ett skelett vars fält står som `[fylls i R1]`, så alla
fyra tunga axlar gav noll och bara fritexten poängsatte: högsta poäng blev 6, mot 13 i
arkitektens körning. Skriptet är alltså fortfarande deterministiskt; det fick bara ett annat
dokument. Två av arkitektens fem föll ändå ut även ur skelettet (`aevi-wellness` direkt,
och `beautiful` ligger i samma familj som `aarke` och `alet`), vilket är ett svagt men
positivt tecken på att fritexten pekar åt samma håll.

Jag körde därför om **arkitektens exakta kommando**, mot `BRIEF-draft.md`, i den här
sessionen. Det reproducerade den låsta raden tecken för tecken, inklusive alla poäng och
delpoäng, och skrev den som senaste `catalogue-select`-rad i min egen
`.impeccable/design-session.jsonl`:

```
catalogue-select skriven: squarespace, aevi-wellness, beautiful, insign, mode  ->  C:\Users\Anton L\anti-slop-design\.impeccable\design-session.jsonl
```

**Arkitektens rad gäller**, och jag har inte bytt en enda referens på egen hand. Följdfynd som
lead äger: R1-promptens `--brief`-argument pekar på `BRIEF.md`, medan raden som ska
reproduceras kom ur `BRIEF-draft.md`. Så länge skelettet bär `[fylls i R1]` kan de två aldrig
ge samma svar. Nästa konkreta steg om lead vill stänga det: låt prompten namnge
`BRIEF-draft.md`, eftersom utkastet finns just för att ge skriptet något att poängsätta mot.

## Design Read (en rad)

**Kall ritpappersteknik i petrolbläck**: en `modern clean`-yta läst som ett arkitektritat
snitt, berättad som `chaptered editorial` där varje kapitel är ett fält på samma ark och
ritningen själv är både titelsida, nav och avslut.

Låst underlag: register `modern clean`, grammatik `chaptered editorial`, kategori
`portfolio` / `editorial`, auktoritet `surface`, mode `persuade`.

## Dial-deklaration

**variance 8 · motion 6 · density 6.** Arkitektens riktvärden hålls oförändrade, alla tre, och
skälen är mina egna:

- **Variance 8.** Konceptet finns inte i registret: ingen av de 36 raderna ritar sitt eget nav,
  och lägsta fingerprintsumma är 5/6. Åttan och inte tian, därför att grammatiken
  (`chaptered editorial`) är delad med nio rader och målbilden låser den, så en dimension av
  sex är på förhand upptagen.
- **Motion 6.** En enda pinnad akt bär hela signaturen; de fem andra akterna är `kinetic`,
  `reveal`, `flow`, `count` och `reveal`, alltså kittets lugnaste familjer. Noll `scrub`, noll
  `drift`, noll `pan`, noll pekar-devices, och exakt en embodiment på hela sidan. Sexan mäter
  att rörelsen är koncentrerad, inte att den är sparsam: inuti a1 är rörelsen auktoriteten.
- **Density 6.** Arket bär 25 stroke-banor och 14 textnoder, vilket är tätt för en yta, men
  typskalan har exakt tre grader (72 / 15 / 12 px) och varje skärm har ett displayelement.
  Tätheten sitter i linjearbetet och aldrig i typografin, och det är skillnaden mot en sjua.

Arkitektens riktvärden att motivera avvikelse från: **variance 8** (nytt koncept, ingen
ärvd estetik, lägsta fingerprint-summa 5/6 mot registret), **motion 6** (en pinnad
signaturakt bär allt; resten är reveal, flow och count, noll scrub, noll drift, noll
pekar-devices), **density 6** (elva skärmar och ett tätt linjearbete, men ett
displayelement per skärm och en typskala som är sparsam i allt utom måttsiffrorna).

## Reference lock (7 fält)

```text
Primary reference/direction: squarespace (design-catalogue, modern clean / chaptered
  editorial). Vad som lånas är reservationen som princip: all mättnad hålls undan
  marknadsföringsytan och reserveras för kundernas egna sajter. K3 flyttar den ett hack
  och gör den strukturell: det enda mättade i vyn är en verklig kundsajt inne i den
  ritade öppningen, och det enda kromatiska på arket är en sann uppmätt siffra.
Preserve: kallt ritpapper oklch(0.95 0.012 230); bläck oklch(0.30 0.055 245); hårlinje
  oklch(0.52 0.035 240); accent #1E5E9C enbart på måttsiffror i displayskala; Chivo som
  röst och Martian Mono som register, rollerna korsar aldrig; ingen topprad; ritad
  teckenförklaring i vänstermarginalen som sidans enda nav; tre exempelsajter live i
  <iframe> från samma origin; de ordagranna copy-raderna ur PRODUCT.md § Brand
  Commitments; sanna värden bara (320, 768, 1440, 7 rem, 96 px, 16:9, 26 900, 38 900,
  Pris vid förfrågan).
Borrow only: (1) squarespace — steps(1, start)-tickningen ur dess uppmätta motion
  language, lånad enbart som räknarbeteende: en måttsiffra landar på ett heltal, den
  glider aldrig. (2) beautiful — den granskningsbara accentregeln "ett korallmoment per
  viewport", ordagrant överförd som "ett blått moment per viewport". (3) mode — den
  färgkodade teckenförklaringen bredvid lagerillustrationen, lånad som legend-mönster och
  ritad i stället för färgad. (4) insign — lånad som AVVISNING: dess bevisapparat
  (betygschip, 180+ omdömen, teamgrid, logotypvägg) är exakt det Alunix inte har och
  aldrig får hitta på. (5) aevi-wellness — hårlinjen som enda strukturmedel plus det
  uttryckliga skuggförbudet. Ingen av de fem lånas som komposition.
Role rules: #1E5E9C gör exakt en sak på hela sidan: den färgar måttsiffror i displaygrad,
  och ingenting annat. Aldrig en yta, aldrig en länk, aldrig en ram, aldrig en fyllning.
  Blått förekommer i exakt en akt (a1) och på exakt en apparat (måttkedjan #dim-width med
  sina tre siffror), som räknas som ETT blått moment; efter a1 finns noll blått på sidan.
  Chivo är röst: rubriker, brödtext, tjänstenamn, manifestrad. Martian Mono är register:
  måttsiffror, utrop, zonnamn, titelblockets fält, radnummer 01 till 03, ledarpunkter,
  folio. Chivo sätter aldrig ett mått; Martian Mono sätter aldrig en rubrik eller
  brödtext; grep på "Chivo" inuti <svg>-blocket ska ge 0. Hårlinjen är EN bredd, 0.75 px,
  och den gäller både inuti ritningen och för varje HTML-regel på sidan. Radie 0 överallt.
Media strategy: product surface (Calyx, Hōrai och Hyperborea, byråns egna sajter, live i
  <iframe> från samma origin) + drawn system (hela ritningen och papperstexturen,
  handförfattad inline-SVG respektive procedurell SVG/CSS). Enum, ett värde per plats.
  INTE photo:unsplash, INTE photo:pexels, INTE generated, INTE placeholder. Noll
  fotografier på sidan.
Reject: glaskort, dashboard-over-foto, "live"-punkter och telemetri-chrome (F-006);
  omritat enhets-chrome, webbläsarfält, flikrad, URL-fält, telefonbezel, trafikljusprickar
  (gate 47); div-byggd eller SVG-ritad låtsas-UI, låtsasknappar, låtsastext, lorem, gra
  staplar som ska "vara" text, navrad i ritningen, formulär, graf, sparkline (gate 79);
  scroll-cue-text (gate 88); ikongrid; gradient och mesh; centrerad hero med badge-rad;
  lila eller indigo accent; skuggade kort; stockfoto av leende team; dekorativa blobbar;
  tre lika feature-kort; tre priskort med "populärast"; logotypvägg, omdömen, betyg,
  kundantal, år i branschen; tankstreck i synlig text; en andra accent; box-shadow;
  backdrop-filter; roterad typ.
Token commitments: --paper oklch(0.95 0.012 230) (arket, hela sidan); --paper-fold
  oklch(0.925 0.018 230) (andra arket: a3:s plate-marginaler och a6:s ram, som
  materialbyte mellan akter); --ink oklch(0.30 0.055 245) (all typ, alla bärande
  konturer); --ink-hair oklch(0.52 0.035 240) (hjälplinjer, måttlinjer, skrafferingar,
  ledare, aldrig typ utom margin-register i utropen); --blue oklch(0.47 0.13 252) =
  #1E5E9C (enda accenten, bara måttsiffror i displayskala); --hair 0.75px (enda
  hårlinjebredden); --contour 1.5px; --cut 2.5px; radie 0; box-shadow none;
  display Martian Mono 500 / 72 px (bara måttsiffror); röst Chivo 300 och 700, max ~72 px;
  brödtext Chivo 300 / 15 px; register Martian Mono 400 / 12 px, tracking 0.14em, versal.
```

## Decision ledger

En rad per materiellt val. Ett val utan rad skeppas inte.

| Area | Decision | Source | Source rule | Why |
|---|---|---|---|---|
| **Palett** | Kallt ritpapper `oklch(0.95 0.012 230)`, bläck `oklch(0.30 0.055 245)`, hårlinje `oklch(0.52 0.035 240)`, accent `#1E5E9C`. Restrained. Inget cream | Målbilden (planens § 7.5) + AB09-lärdomen, låst av lead | TASTE § 4.4, ett papper och en accent som gör en sak | Ett ritark är kallt; cream gör det till ett bokuppslag och AB09 mätte det som fel värld |
| **Accentens inhägnad** | `#1E5E9C` färgar bara måttsiffror i displaygrad. Den förekommer i en enda akt (a1) och på en enda apparat: måttkedjan `#dim-width` med sina tre siffror, vilken räknas som **ett** blått moment | `beautiful` (ett korallmoment per viewport) skärpt med `mode` (inhägnad till en typ) | "State an accent's frequency as a number, not a feeling" | En innehållsregel kan inte drifta när en ny komponent uppstår; en komponentregel kan. Läsningen "en sammanhängande apparat = ett moment" är utskriven här sa att den inte kan tolkas om i R2 |
| **Typ** | Chivo (röst, 300 och 700) och Martian Mono (register, 400 och 500). Två variabla filer. Rollerna korsar aldrig | `brand.md`:s fyra steg, utförda i `concepts-K3.md` (6) | TASTE § 4.2, två snitt och rollerna korsar aldrig | Objektet är ett titelblock, inte en tidskriftsrubrik: vagrätt avskurna terminaler och en mono ritad för teknik. Ingen av de två står på reflexlistan eller i r1 till r7 |
| **Nav** | Ingen topprad. Navigationen är en ritad teckenförklaring i vänstermarginalen, sticky: fem rader med symbolprov (hårlinje, måttpil, skraffering) plus kapitelnamn, och en ledarlinje som ritas från den aktiva raden ut till kapitlets egen kontur | Målbilden + `mode` (legend-mönstret) | `feel-and-fingerprint.md` dimension 2 | Kategorins reflex är en sticky pill-rad med en CTA. En legend är samma funktion uttryckt i ritningens eget språk, och den är dessutom sidans enda hover-oberoende statuskvittens |
| **Hero-device** | `section.act-1` blir `data-sc-act="pin" data-sc-span="2.4" data-sc-dwell="0.35"`. Ritningen är en inline-`<svg>` vars banor har `pathLength="1"` och ritas av `stroke-dashoffset` ur `--sc-ps`. Motorns stage-markup ur `template.html`, aldrig restylade `.sc-*`-klasser | Målbilden | AB06, motorn redigeras aldrig | En hel anatomi måste ritas medan ramen står stilla; en `flow`-akt har inte det scrollrummet |
| **Aktform** | Sex akter, ~13 vh: `pin` 2,4 (+ staplad `count`) → `kinetic` lines → `reveal` ×3 → `flow`+`in` → `count` (+ `parallax` på marginalspalten) → `reveal`. Noll `scrub`, noll `drift`, noll `pan`, noll pekar-devices, aldrig samma familj två ganger i rad | Målbilden, med två rättelser | `devices.md` § device kit, "never the same one twice running"; `feel-and-fingerprint.md` § The peak | Målbilden satte `flow+in` följt av `count+flow`, alltså samma familj två ganger i rad; a5 är därför `count` och a6 `reveal`. Toppen och signaturen slogs ihop till a1 sa att sidan har en topp, inte tre |
| **Avslut** | Ett specifikationsblad på samma kalla papper: paketen som stycklista med ledarpunkter och de sanna priserna, manifestraden `Alla har rätt till bra design.` och `kontakt@alunix.se` som mailto, allt inuti en ritad ram vars fyra linjer dras in sist i ordningen överkant, höger, underkant, vänster. Ingen inversion, sidan slutar stilla | Målbilden + r7 § Alunix, fakta | "inget formulär som skickar nagonstans"; `feel-and-fingerprint.md` § The peak, avslutet ska lösa upp | Rut-testet: kategorins default är ett mörkt CTA-band med ett formulär. En ritning slutar med sitt titelblock |
| **Memorable detail** | *Ritningen blir sidan.* Samma rektangel som bläcket nyss ritade fylls med Calyx fold i en levande `<iframe>` medan konturen står kvar ovanpa som ram | F-010 (fönstret i fasaden), omtolkat från "innehållet maskas in i objektets verkliga öppning" | `reference-lock.md`: Memorable detail-raden är obligatorisk | Besökaren ser ritningen och det byggda vara samma sak, vilket är exakt vad byran säljer: de ritar innan de bygger |
| **Genererat material** | `Genererat material -> procedurell SVG/CSS · Källa: planens § 10.6 fallback steg 3 · Orsak: Higgsfield 0 credits, free plan, mätt 2026-09-09 av lead` | Planens § 10.6 fallback steg 3 | `generation.md` § 1: i ett ritat register slar ett ritat system både sourcad och genererad bild | Papperstexturen blir ett `feTurbulence`-filter med `stitchTiles="stitch"`, alltså sömlös genom konstruktion i stället för sömkontrollerad efterat. Codex-fallbacken (steg 2) hoppas over för K3 därför att steg 3 är strikt bättre här, inte bara billigare. Full motivering i `assets/ASSETS.md` § B |
| **Rörelsens datakälla** | Allt som ögat ser förflytta sig läser `--sc-ps`: varje `stroke-dashoffset`, varje `clip-path`, varje `mask-position`, varje `transform`, ledarlinjen i legenden och parallaxen i a5. `--sc-p` får läsas av cue-opacitet och ingenting annat | F-014 punkt 1 | `motion-smoothness.md` § The rule | En ritad linje som läser rått `--sc-p` stegar synligt: bana efter bana får en notch per hjulklick i stället för en hand som drar |
| **Registrerade lokalvariabler** | Varje per-bana-lokal (`--l1` till `--l14`) registreras med `@property { syntax: "<number>"; inherits: false; initial-value: 0 }` | `motion-smoothness.md` § Fault 1 | "`--sc-p` is an unregistered custom property. To CSS it is a string, so it never interpolates" | Utan registrering är fönsterberäkningen en sträng och `clamp()` returnerar inget interpolerbart. Det är samma fel som F-013 mätte, en niva ner |
| **Iframe-montering** | Alla tre exempelsajterna monteras via IntersectionObserver ungefär en viewport i förväg, med `loading="lazy"` som bälte och hängslen. Monteringen är **serialiserad**: nästa ram börjar inte laddas förrän den föregaende har fyrat `load`. En ram som en gang monterats rivs aldrig ner, transformeras aldrig och tonas aldrig | `concepts-K3.md` (5) Budget ("aldrig fler än en igang samtidigt") läst mot PRODUCT.md § Operating Context | `performance.md` § 2: "Three live iframes mounted at load is the heaviest thing a marketing page can do to itself" | "En igang" läses som **under laddning**, inte som "monterad": PRODUCT.md kräver att en visad ram förblir användbar, sa nedrivning är förbjuden. Serialiseringen haller natverket och huvudtraden bundna utan att bryta den regeln |
| **Prestanda** | Se § Prestandaplan nedan; varje post har ett målvärde | F-013 + `performance.md` § 1 | Gate 93 | Tre live-iframes plus en procedurell textur är budgetens två svaraste poster och de måste bada ha en skriven plan innan första raden kod |
| **Tesrubrikens form** | `VI BYGGER ERT VARUMÄRKE.` i versal form | r7 § Alunix, fakta + PRODUCT.md § Brand Commitments | copy-gate: ordagrann copy bevaras och skrivs aldrig om | Målbilden citerar `Vi bygger ert varumärke.`; de två kan inte bada gälla och den ordagranna strängen vinner. Se QUESTIONS.md Q9 |
| **Titelblockets andra fält** | `SEKTION A-A` skrivs med bindestreck, aldrig med tankstreck | PRODUCT.md § Capabilities and Constraints | "Inga tankstreck i synlig text" | `concepts-K3.md` skriver fältet med tankstreck i löpande prosa. På sidan är det synlig text och får därför inte innehalla ett |

**Byggarens rader, R1.** En per materiellt val jag fattar utöver arkitektens.

| Area | Decision | Source | Source rule | Why |
|---|---|---|---|---|
| **Legendens fem rader** | Fem kapitel, ett ord vardera: `TESEN` · `DETALJER` · `LIGGAREN` · `STYCKLISTA` · `TITELBLOCK`, i den ordningen uppifrån och ner, en per akt a2 till a6. a1 får ingen rad: a1 är arket självt, inte ett kapitel i det | ASSETS.md § A.9 (legenden är fem rader och sidans enda nav) + copy-planens krav "ett ord vardera, inte marknadsföringsord" | `feel-and-fingerprint.md` dimension 2: navet är chrome med ett syfte | Alla fem är ritnings- eller liggarord, inga är verb och inget lovar något. `TITELBLOCK` binder ihop sidan: s1 öppnar på titelblocket i arkets hörn och a6 stänger på samma objekt, ritat större |
| **Symbolprovens mappning** | Varje legendrad bär den linjeroll kapitlets eget ritarbete är gjort av, inte en godtycklig symbol: `TESEN` → hårlinje · `DETALJER` → kontur · `LIGGAREN` → måttpil · `STYCKLISTA` → ledare · `TITELBLOCK` → skraffering | ASSETS.md § A.9 låser de fem symbolerna (hårlinje, måttpil, skraffering, kontur, ledare); mappningen är min | ASSETS.md § A.2 (varje linje har en namngiven roll) | En legend vars symboler inte pekar på något är dekor. Belägget per rad: linjalen under kapitelrubriken är en hårlinje; de tre plate-ramarna är konturer; `#dim-row` utropar radhöjden `96 px`; ledarpunkterna löper fram till priskolumnen; a6:s ram får ett skrafferat innerband, se nästa rad |
| **a6:s skrafferade innerband** | a6:s ritade ram får ett 8 user units brett skrafferat band längs sin underkant, samma `<pattern id="hatch">` som `#hatch-marginal`, `--ink-hair`, ingen egen kontur | Följer av symbolmappningen ovan: skrafferingen måste ha ett belägg i a6 för att få stå i legenden | ASSETS.md § A.5 ("skraffering är en yta, inte en form") | Standard ritpraxis: titelblockets fält markeras som arkets eget material, inte som en del av det ritade objektet. Det ger a6 ett materialbyte utan en andra accent och utan `--paper-fold` i grunden. **Kostnad: en `<rect>` och noll nya banor**, budgeten står kvar på 25 stroke-banor |
| **Tjänsternas tre underrader** | `Design` → `Vi ritar sidan innan vi bygger den.` · `Utveckling` → `Koden skriver vi själva.` · `System` → `Vi kopplar in CMS, bokning och betalning.` | PROMPT.md § Alunix, fakta ("en kort underrad var, i byråröst, utan påståenden om kunder eller resultat"); QUESTIONS.md Q6 lämnar texten öppen | copy-gate: nya strängar går genom fem pass i R3 | Tre olika satsformer, inte tre likadana, så liggaren inte läser som tre kort med olika ord. Ingen av dem påstår ett resultat, nämner en kund eller innehåller ett tal. Den första binder underraden till konceptet utan att förklara det |
| **Exempelsajternas mätta överföring** | Calyx 1,48 MB · Hōrai 2,90 MB · Hyperborea 0,40 MB, summa **4,78 MB**, mätt i R1 med `perf_probe.py` vid 4× CPU. Summan överstiger ensam budgetens 2,5 MB. **Rapporterat till lead som ett fynd**; ingen ram byts mot en skärmbild utan leads beslut | Egen mätning, R1. Kommandot och de tre utfallen står i § Prestandaplan | `performance.md` § 1 (tak 2,5 MB) + gate 93; PRODUCT.md § Operating Context (en visad ram förblir användbar) | Fyndet ändrar inte cellens media strategy: ramarna är beviset och beviset ska gå att använda. Det ändrar var lösningen ligger, från K3:s skal till exempelsajternas egen skuld (två av tre hotlänkar Unsplash och laddar Google Fonts). Serialiseringen och `content-visibility` är fortfarande rätt, men de flyttar kostnaden i tid, inte i byte |
| **`--hair` under 768** | `--hair` höjs från `0.75px` till `1px` under 768 px viewportbredd, som cellens enda breddundantag. Höjningen gäller **både** inuti `<svg>` och varje HTML-regel, så det finns fortfarande exakt en hårlinjebredd per viewport | ASSETS.md § A.8 anger undantaget och kräver uttryckligen att byggaren skriver det som en egen ledgerrad | ASSETS.md § A.2 ("den enda hårlinjebredden") | `vector-effect` används inte, så 0.75 skalas till 0.20 px vid 390 bredd, alltså under en enhetspixel. Kontrollen i R2 är att `grep` fortfarande bara ger tre bredder inom varje mediafråga, inte fyra i filen som helhet |
| **Legendens spaltmått** | Legenden sätter sin text i `margin 12` inom x 0 till 120, med symbolprovet i x 12 till 32 och kapitelnamnet vänsterställt vid x 40. Längsta namnet (`STYCKLISTA` och `TITELBLOCK`, 10 tecken) mäts i R2 med `measure.py`; håller det inte inom x 40 till 116 kortas namnet, aldrig graden | ASSETS.md § A.9 (slot x 0 till 120) + § A.4 (ingen tredje typinställning) | ASSETS.md § A.4 ("det finns ingen tredje inställning") | Marginalen är samma 120 units som `#hatch-marginal` upptar, så legenden och skrafferingen delar spalt. Regeln skriver ut vad som viker om måttet inte går ihop, så att R2 inte frestas att införa en 10 px-grad |
| **Två `?preview=`-lägen till** | `?preview=legend` och `?preview=plates`, se § `?preview=`-plan | Egen slutsats: två formade lägen saknar skärmbildsväg i arkitektens fem | F-007 (signaturakten jämförs bild för bild) + gate 47/79-kontrollen | Legendens ledarlinje är sidans nav och syns i inget av de fem lägena; a3:s tre plate-ramar är ritade konturer och måste kunna prickas av mot gate 79 på samma sätt som a1:s ritning |

**Byggarens rader, R2.** Alla mätvärden och den fullständiga listan står i `NOTES.md` § R2.

| Area | Decision | Source | Source rule | Why |
|---|---|---|---|---|
| **Aktens spann** | `data-sc-span` **4.0**, inte målbildens 2.4 | Egen mätning i R2 | `motion-smoothness.md` § The bar: `max_step ≤ 3 %` är en hård grind | Motorn ger pinnad resa `(span - 1) * vh`, så 2.4 ger bara 1,4 vh = 1260 px för fjorton ritsteg, alltså 90 px per steg, mindre än ett hjulhack. **Mätt vid 2.4: `--sc-ps` max_step 3,44 %**, över baren. Vid 4.0: **2,02 %** vid hjul 100:60 och **0,84 %** vid 20:120. Spannet är ett riktvärde, baren är en grind, och grinden vinner. Akten har fortfarande sidans största spann med bred marginal |
| **Snittmarkeringens ritordning** | `#cut-AA` är **en** obruten bana `M48 220 V180 H1392 V220` | ASSETS.md § A.3 (exakt ett `<marker>`, varje pil är `marker-start`/`marker-end`) | ASSETS.md § A.3, "En pil ritad som två `<line>` är ett fel" | Med tre separata banor får bara första och sista änden en markör. En obruten bana ger båda spetsarna nedåt via `orient="auto-start-reverse"` och är dessutom mer bokstavligt "en enda obruten hand" |
| **Allt läser `--sc-ps`** | Även utropens opacitet, inte bara det som förflyttar sig | F-014 regel 1 | Regeln **kräver** `--sc-ps` för rörelse och **tillåter** `--sc-p` för cue-opacitet | En opacitet som stegar vid varje hjulhack läser som flimrande text. Strängare än regeln är aldrig fel, och det tar bort en hel felklass |
| **Fem lokaler, inte fjorton** | `--l`, `--t`, `--thin`, `--fill`, `--fall`, var och en registrerad med `@property { syntax: "<number>"; inherits: false }`. Varje bana sätter sitt eget fönster i samma namn | ASSETS.md § A.6 | Kravet gäller **registreringen**, inte antalet namn | `inherits: false` gör banorna oberoende av varandra, vilket är hela poängen med en bana i taget. Mekaniken blir en rad CSS och `?preview=drawn` blir en regel i stället för fjorton |
| **Legendens närvaro** | Tonar in först när första kapitlet närmar sig; osynlig i `?preview=sheet` och `?preview=drawn` | BRIEF.md § Direction contract, FIRST VIEWPORT | Fältet är **låst** och räknar uttryckligen upp "ingen legend" | Första bygget bröt låset. Indexet finns när det finns kapitel att indexera |
| **Legendens papperskulör** | Varje legendrad har `background: var(--paper)` och 4 px sidopadding | Ritpraxis: ett utrop på en skraffering bryter skrafferingen | TASTE § 2.3 och F-006 förbjuder **kort** | Raderna ligger i den skrafferade marginalzonen och 12 px mono på en 45-gradig skraffering är oläsbart. Detta är **inte ett kort**: ingen radie, ingen kant, ingen skugga, ingen elevation, ingen yta utöver papperets egen färg |
| **Ledarlinjens mekanik** | `transform: scaleX()`, aldrig `width` | `detect.mjs`, som flaggade `layout-transition: transition: width` vid skrivning | `performance.md` § 3 | En width-transition kostar layout per frame. `transform` komponeras |
| **Explicit enhet på dashoffset** | `stroke-dashoffset: calc((1 - var(--l)) * 1px)`, `stroke-dasharray: 1px` | Egen mätning i R2 | F-014: en prob som inte kan mäta värdet är värdelös | Utan enheten serialiserar Chromium det beräknade värdet som `calc(1px)` respektive `0%`, två olika typer, och `motion_probe.py` rapporterade **`DEAD` på en bana som ritade sig korrekt på skärmen**. En rörelse som inte går att mäta är inte verifierad |
| **`transform-box: fill-box`** | På måttsiffrorna, med `transform-origin` per siffras ankare | ASSETS.md § A.6 steg 14 kräver origo vid baslinjen men anger ingen mekanik | Samma | Utan raden ligger origo i SVG:ns nollpunkt och siffran skalar mot arkets hörn. **Mätt:** alla tre landade under titelblocket |
| **`color-mix` i `srgb`** | På de två blandningar som körs per frame. Tokens är fortfarande oklch | `performance.md` § 3 | Skär arbetet per frame | Omätbar skillnad i resultat på en 12 px-siffra. **Gav ingen mätbar vinst i bildtid**, vilket står utskrivet i `NOTES.md` hellre än att döljas |
| **Den reducerade planschen** | Byggd för 320 till 767. Mellanplanschen 768 till 1023 är **inte** byggd och står som öppen | ASSETS.md § A.8 | Stress-personan i § Persona-skisser | Mätt vid 390: hela den fulla planschen lästes som en utsmetad remsa, exakt som personan förutsade. `x` och `y` är inte CSS-egenskaper på `<text>`, så utropens position sätts med attribut i JS |
| **Måttsiffrornas x-läge** | `#m-1440` vid x 1416 och `#c-169` vid 1412, inte ASSETS.md:s 1430 respektive 1424 | Egen pixelläsning i R2 | ASSETS.md § A.5 | `letter-spacing: 0.02em` lägger ett spatium efter sista glyfen, så ett `text-anchor="end"` vid 1430 sköt sista nollan förbi arkets kant |
| **`marginal`-utropets läge** | Flyttat från y 396 till y 268 | Egen pixelläsning i R2 | ASSETS.md § A.5 | Legenden är fixerad och vertikalt centrerad; vid 1440 × 900 låg den gamla punkten rakt under legendraden DETALJER. Ett utrop som ett annat element täcker är ett utrop utan roll |
| **Bildtidsbudgeten** | **Inte nådd**, och orsaken **inte fastställd**. Ingen orsak namnges | Egen mätning: fem lager ablerade, först en gång per variant och sedan interleavat i tre varv | `performance.md` § 1 gate 93; F-013 (mät i stället för att gissa) | Spridningen inom en variant översteg skillnaden mellan varianter i båda uppläggen. Ramen är **inte** orsaken (nollresultat: p95 50,1 med ram mot 50,0 utan). Baren är nåbar: `tests/motion/smooth.html` klarar den under identiska villkor. Att peka ut den variant som råkade se bäst ut vore att hitta på ett resultat som datat inte bär |

## Direction contract

- **THESIS:** Alunix ritar innan de bygger, och sidan bevisar det på det enda sätt en byrå
  kan bevisa det: den ritar sig själv färdig och blir sedan det den ritade.
- **OWN-WORLD:** Ett kallt ritark där varje linje har en namngiven roll och varje siffra är
  ett mått besökaren kan kontrollera mot sin egen skärm. Ingen annan byrå kan låna världen
  utan att också behöva stå för att varje tal på sidan är sant, vilket är precis det
  kategorin inte gör.
- **STORY:** elva skärmar, i ordning.
  1. **s1** Ett kallt tomt ark håller stilla, med ett titelblock i övre vänstra hörnet som
     enda innehåll.
  2. **s2** En enda linje börjar färdas, och en sidas anatomi växer fram kontur för kontur
     medan titelblocket faller till marginalgrad.
  3. **s3** Måttkedjan `320 · 768 · 1440` räknar upp i blått medan konturen går ner till
     hårlinjevikt.
  4. **s4** Öppningen bläcket nyss ritade fylls uppifrån och ner av Calyx, live, och
     måttsiffrorna krymper ner i marginalen.
  5. **s5** Kapitelrubriken `VI BYGGER ERT VARUMÄRKE.` anländer rad för rad under en linjal
     som dras samtidigt.
  6. **s6** Calyx igen, nu i sin egen ritade ram i läsbar grad, med den ordagranna
     bildtexten som marginaletikett.
  7. **s7** Samma anatomi, Hōrai.
  8. **s8** Samma anatomi, Hyperborea, varefter kapitlet är slut.
  9. **s9** Tre tjänstenamn på tre rader i en liggare, med radhöjden `96 px` utropad i
     marginalen.
  10. **s10** Priskolumnen räknar upp till `26 900` och `38 900` med ledarpunkter fram till
      kolumnen, i bläck och inte i blått.
  11. **s11** En ritad ram dras in runt `Alla har rätt till bra design.` och mailadressen,
      linje för linje, och sidan slutar röra sig.
- **FIRST VIEWPORT:** vid 1440×900 och `--sc-ps` = 0 syns **exakt två saker**: arket, alltså
  `--paper` med sin procedurella textur ut i alla fyra kanter, och `#title-block` i övre
  vänstra hörnet, tre rader `margin 12` i `--ink` vänsterställda vid x = 48 med baslinjer
  y = 68, 98 och 128: `ALUNIX` · `SEKTION A-A` · `SKALA 1:1`. Ingenting annat. Ingen kontur,
  ingen måttlinje, inget utrop, ingen legend, ingen scroll-cue, ingen topprad, ingen
  logotyp. **Låst:** oförändrat.
- **FORM:** Sidan är ett enda plant ark: tre linjebredder (0.75 / 1.5 / 2.5 px), en dash-form
  (`4 3`), en pilspetsform, två monoinställningar, radie 0, noll skugga och noll gradient,
  så att allt djup som finns kommer ur överlapp och ton på ton.

## Persona-skisser

`reference-lock.md` § Three persona sketches. Villkoren är situationella, inte bara
permanenta.

```text
Primary: Verksamhetsägare i Sverige, 35 till 55, som ska bestalla sin första riktiga
  webbplats · barbar dator, 1440 bredd, kontorsuppkoppling, mitt på dagen · kom för att
  se om byran kan något och vad det kostar, och har aldrig sett en teknisk ritning av en
  webbsida förut. Villkoret: hen måste första att arket är en ritning och inte ett
  trasigt gränssnitt inom de första 0,12 av a1, utan att en enda förklarande mening
  skrivs ut.
Edge:   Samma person med markörprecision nedsatt av en handskada, som scrollar med
  tangentbord i stället för hjul · Page Down flyttar `--sc-p` i hopp, inte i hack · det
  som bryter först är a1: en linje som ritas i hopp läser som en trasig animation, inte
  som en hand. Villkoret: `staircase = 0` måste hålla också när varje scrollhändelse är
  ett helt viewport-hopp.
Stress: Samma bestallare på en telefon, 390 bredd, utomhus i höstsol med en hand upptagen,
  som ska bestamma på fem minuter om hen ska mejla · har inte rad att tappa priserna eller
  mejladressen. Villkoret: en 1440 bred ritning som skalas till 390 gör hårlinjen 0.20 px
  bred, alltså under en enhetspixel, och da försvinner halva ritningen eller aliasar till
  gratt. Under 768 gäller den reducerade plansch som står i ASSETS.md § A.8.
```

Intersektionen som betalar två ganger: den minsta linjebredd som överlever nedskalningen
till 390 är samma varde som gör hårlinjen läsbar i solreflex och för nedsatt syn, och
tangentbordsscrollens hopp är samma problem som ett trögt hjul.

Den persona som är obekvämast: **Stress**, därför att den angriper cellens premiss och
inte bara dess utförande. En ritning som skalas ner slutar vara en ritning; svaret får
inte vara att lata den bli sallad, utan att rita en annan plansch. Konkret krav:
`shoot.py` vid 390 och 320, och en pixelläsning av foldens hårlinjer innan R2 lämnas.
Konkret krav för Edge: `motion_probe` körs med `--wheel 20:120` **och** `--wheel 100:60`,
och `staircase` ska vara 0 i bada.

## Motion-tes

Låst, ur `concepts-K3.md` (5). Byggaren skriver om den med sina egna ord och lägger till
matta värden.

- **Focal:** Ögat följer **linjespetsen**, den enda punkt på arket som rör sig, och det håller
  i tio av fjorton ritsteg. Fokus flyttas exakt tre gånger i hela akten: från linjespetsen
  till måttkedjan när siffrorna börjar räkna (`ps` 0,58), och från måttkedjan till öppningen
  när den börjar fyllas (`ps` 0,78). Att det är tre och inte fler är själva mätpunkten: om
  två saker rör sig samtidigt någon annanstans än i de skiftena är akten fel byggd.
- **Continuity:** Ritordningen är en enda obruten hand. Ingen bana överlappar en annan i tid,
  ingenting hoppar in i vy, och ingenting tonar in ur intet: varje element börjar i en
  linjeände som redan var synlig. Öppningen som fylls är samma rektangel som konturen
  ritade, positionerad ur samma fyra `--op-*`-tal, inte en ny ruta ovanpå (F-010). **Hela
  ordningen står utskriven nedan**, och den är kontraktet R2 ritar efter.
- **Feedback:** Scrollen **är** pennan: 1 % scroll ger 1 % ritad linje, åt båda hållen, utan
  låsning och utan hijack utöver motorns egen pin. Att scrolla uppåt suddar linjen i exakt
  omvänd ordning, därför att varje bana är ett rent `calc()`-uttryck mot `--sc-ps` och ingen
  bana har en enkelriktad `transition` eller en `animation`. Legendens ledarlinje är sidans
  enda andra kvittens och den är hover-oberoende.
- **Budget:** **En** `<svg>` med 25 stroke-banor och 14 textnoder, mot kittets tak 60. Ett
  enda `stroke-dashoffset`-uttryck per bana, alla drivna av `--sc-ps` via `calc()` i CSS;
  ingen per-frame JS-skrivning per bana och ingen layoutläsning i någon scroll-handler.
  Varje lokal `--l1` till `--l14` registreras med `@property { syntax: "<number>" }`.
  `will-change: stroke-dashoffset` sätts bara medan `0 < ps < 1` och städas av shimen i
  vila. Mätt vid 4× CPU i **båda** riktningarna: `staircase = 0`, `max_step ≤ 3 %`,
  bildtid p95 ≤ 20 ms, noll frames > 33 ms.

### Ritningens ordning, utskriven före R2

Fjorton steg i den pinnade akten a1, ur `assets/ASSETS.md` § A.6, med `--sc-ps`-fönstret och
den lokal varje steg driver. Detta är den ordning R2 ritar i, och avvikelse kräver en rad i
decision ledger. **En linje åt gången: inget fönster överlappar ett annat.**

| Steg | Lokal | Fönster `--sc-ps` | Vad som dras | Roll |
|---|---|---|---|---|
| 0 | ingen | statiskt | `#title-block`, tre rader `margin 12` i arkets övre vänstra hörn | Utrop. Ritas aldrig. Enda innehållet i 0 → 0,12: **den författade tystnaden** |
| 1 | `--l1` | 0,12 → 0,22 | `#page-outline`, medurs från övre vänstra hörnet | Kontur, 1.5 |
| 2 | `--l2` | 0,22 → 0,28 | `#cut-AA` vänster till höger, sedan de två benen nedåt; bokstäverna `A` tonar in vid 0,27 på `--sc-p` | Snittmarkering, 2.5, `#arrow` i båda benens ändar |
| 3 | `--l3` | 0,28 → 0,36 | `#guide-col-a-l`, `#guide-col-a-r`, `#guide-gutter-r`, i ordning från vänster, en åt gången | Hjälplinjer, 0.75, dash `4 3` |
| 4 | `--l4` | 0,36 → 0,44 | `#opening`, medurs från sitt övre vänstra hörn | Kontur, 1.5 |
| 5 | `--l5` | 0,44 → 0,48 | `#hatch-marginal`, avslöjad vänster till höger med `clip-path: inset()` | Skraffering. **Enda banan som avslöjas med clip och inte med dash**, därför att ett `<pattern>` inte kan dash-ritas |
| 6 | `--l6` | 0,48 → 0,55 | `#ledger-1`, `#ledger-2`, `#ledger-3`, uppifrån och ner, en åt gången | Hjälplinjer, 0.75, dash `4 3` |
| 7 | `--l7` | 0,55 → 0,64 | `#dim-width`s baslinje vänster till höger, sedan `#ext-320` och `#ext-768`, sedan stationsstrecken. Samtidigt går `#page-outline` ner till hårlinjevikt via `calc(1.5px - 0.75px * var(--l7))` | Måttlinje, 0.75, `#arrow` i båda ändar |
| 8 | `--l8` | 0,64 → 0,68 | `#dim-gutter`; utropet `7 rem` tonar in vid 0,67 | Måttlinje |
| 9 | `--l9` | 0,68 → 0,72 | `#dim-row`; utropet `96 px` tonar in vid 0,71, vågrätt och aldrig roterat | Måttlinje |
| 10 | `--l10` | 0,72 → 0,75 | `#lead-16-9`: punkten `r=1` sätts först, sedan dras ledaren **från målet mot etiketten** | Ledare, 0.75, ingen pilspets |
| 11 | `--l11` | 0,75 → 0,78 | `#lead-marginal`, sedan zonnamnen `spalt` och `fold` | Ledare och utrop, sist av allt ritat |
| 12 | motorns egen | 0,58 → 0,76 | Räknaren: `320` startar 0,58, `768` vid 0,64, `1440` vid 0,70, alla landade före 0,78. `steps(1, start)`-tickning, lånad ur `squarespace`s uppmätta motion language. Startar tom, aldrig på 0, och visar aldrig ett tal större än sitt mål | `count` |
| 13 | `--l13` | 0,78 → 0,88 | Öppningen fylls: `clip-path: inset(0 0 calc((1 - var(--l13)) * 100%) 0)` på `.opening-live`, ett svep uppifrån och ner. Vid `--l13` = 1 tas klippet bort **en gång** och `pointer-events` går till `auto` | Signaturmomentet |
| 14 | `--l14` | 0,88 → 1,0 | Siffrorna faller: `transform: scale()` 72 px → 12 px med `transform-origin` i varje siffras egen baslinje, färgen `--blue` → `--ink-hair` via `color-mix`. `font-size` ändras aldrig | Nedskalning, inte en tredje typinställning |

**Bakåt.** Samma uttryck körs baklänges när `--sc-ps` sjunker; linjerna suddas i omvänd
ordning. `motion_probe` mäter båda riktningarna, med `--wheel 20:120` och `--wheel 100:60`.

**Efter a1** står `#page-outline` och `#opening` kvar som kontur och är den grund a2 till a6
ligger på. Ingenting suddas för att ge plats.

## Feeling curve

| Akt | Känsla | Vad på skärmen orsakar den |
|---|---|---|
| a1 · TOPPEN | Fascination | Ett tomt kallt ark haller stilla, sedan börjar en enda linje färdas, en sidas anatomi växer fram ur ingenting, matten landar på sina riktiga tal, och öppningen linjen just ritat fylls av en verklig webbplats |
| a2 | Beslutsamhet | Kapitelrubriken anländer rad för rad under en linjal som dras samtidigt |
| a3 | Tillit | Tre riktiga sajter, en i taget, var och en innanför sin egen ritade ram, i en grad där man kan läsa dem |
| a4 | Klarhet | Tre rader, tre ord, en utropad radhöjd `96 px`, ingenting annat i vyn |
| a5 | Trygghet | Priserna kommer in som en stycklista och räknas upp till 26 900 och 38 900, med ledarpunkter fram till kolumnen |
| a6 | Ro | Ramens fyra linjer dras in runt manifestraden och sidan slutar röra sig |

Aldrig två lika i rad. Toppen är a1.

**Byggarens bekräftelse, R1: alla sex rader står oförändrade.** Kontrollerad rad för rad mot
`feel-and-fingerprint.md` § The feeling curve. Inga två grannar delar känsla, och kurvan har
formen en topp följd av ett fall och en långsam stigning mot ro: Fascination (topp) →
Beslutsamhet → Tillit → Klarhet → Trygghet → Ro. Det enda jag skärper är mätpunkten, inte
raden: a1 har span 2,4 mot övriga akters ~13 vh delat på fem, alltså den största spannen på
sidan med synlig marginal, vilket är vad § The peak kräver av en topp.

**Författad tystnad.** De första 0,12 av a1 är ett medvetet nästan tomt ark med bara
titelblocket. Det är tystnaden före toppen, inte död scroll. Står här sa att
`scroll_verify.py`s `blankBands` inte larmar falskt; byggaren tar aldrig bort den för att
tysta en varning.

## Tell-someone

> Det är sajten där man ser hemsidan ritas som en ritning, och sen blir ritningen sidan
> på riktigt.

## Device-tabell

Kolumnen **läser** anger `--sc-p`, `--sc-ps` eller "motorns egen" per device. F-014: allt
som ögat ser förflytta sig läser `--sc-ps`.

| # | Akt | Sektion | Device | Familj | Span / cue | Läser | Varför just denna |
|---|---|---|---|---|---|---|---|
| 1 | a1 | Ritningen | `pin` med staplad `count` | pin | span 2,4 · dwell 0,35 · cue `0 1 0 0` | `--sc-ps` för ritningen och masken; `--sc-p` för utropens opacitet; motorns egen för `count` | Ramen måste hålla stilla medan en enda idé korsar den (`grammars.md`, pin) |
| 2 | a2 | Tesen | `kinetic` lines | kinetic | cue `0.1 0.9 0.15 0.4` | motorns egen för raderna; `--sc-ps` för linjalens `scaleX` | En kinetisk rubrik per akt, rader nästan alltid rätt (`devices.md` § 5) |
| 3 | a3 | Tre plates | `reveal` ×3, riktning `up` | reveal | `data-sc-reveal-at="0.15 0.55"` per plate | `--sc-ps` för konturen och wipe-masken | En `clip-path`-wipe är ett tillstandsbyte; `iris` sparas och används inte alls på sidan |
| 4 | a4 | Liggaren 01 till 03 | `flow` + `in` | flow | stagger 70 ms, reducerad blockpadding | `--sc-p` för opacitet; motorns egen för 14 px-lyftet | Administrativt innehåll komprimeras, aldrig pinnas (`feel-and-fingerprint.md` § Pacing) |
| 5 | a5 | Specifikationen | `count` med `parallax` på marginalspalten, rate 0,4 | count | `data-sc-count-at="0.1 0.5"`, 1,4 s, cubic ease-out | motorns egen för `count`; `--sc-ps` för parallaxen | Endast sanna tal får en count (`devices.md` § 7); parallax i en spalt är chaptered editorials egen |
| 6 | a6 | Avslutet | `reveal` | reveal | cue `0.25`, ett värde: sista akten måste hålla | `--sc-ps` | Avslutet ska lösa upp, inte tona ut (`feel-and-fingerprint.md` § The peak) |

Fem familjer, aldrig samma två i rad. `will-change` sätts bara på `#drawing`s banor och
bara medan `0 < ps < 1`; noll vilande promoveringar på hela sidan.

**Embodiment, en enda** (`feel-and-fingerprint.md` § Being in it, "one or two per page"):
dwell-triggad detalj i a1. Står `--sc-ps` stilla över nagra frames medan akten är pinnad,
ritas ett extra utrop in i marginalen, spaltavstandet `7 rem`, som aldrig behövdes för att
första ritningen. Belöning för att stanna. Inget annat på sidan reagerar på besökaren.

## Rejected-lista

Ur `find-animation-opportunities`-gaten, fyra frågor per kandidat. Full tabell i
`concepts-K3.md` (5). **Avvisade:** tilt på de tre plates vid hover · spotlight som följer
pekaren över arket · marquee med exempelsajternas namn · ritrutnät som "andas" bakom allt ·
magnetisk mailto i avslutet. **Behallen som bärande:** ledarlinjen som ritas från legenden
till aktivt kapitel, därför att den är navigationen och inte en effekt.
**Byggarens kandidater, R1.** Fyra till, alla övervägda och alla avvisade.

| Kandidat | Frekvens | Syfte | Hastighet | Funktion | Dom |
|---|---|---|---|---|---|
| Papperstexturen parallaxar långsammare än innehållet | Konstant, hela sidan | Djup i grunden | Kontinuerlig | Ingen. Ett ark har inget djup bakom sig, och lagret skulle behöva `transform` eller `background-attachment: fixed` | **Avvisad.** ASSETS.md § B.1 förbjuder båda uttryckligen; `performance.md` § 3 (isolera en kontinuerlig animation, promovera inte ett helskärmslager) |
| Måttsiffrorna räknar om vid varje ändring av viewportbredden | Vid varje resize | "Sanning i realtid" | 1,4 s per omräkning | Skulle visa ett tal utanför den tillåtna listan så fort viewporten inte är exakt 1440 | **Avvisad.** PRODUCT.md § Absences (inga påhittade tal). Utropen beskriver **den ritade sidan**, inte pappret, vilket är hela poängen med `SKALA 1:1` (ASSETS.md § A.1) |
| Hover på en legendrad tänder dess ledarlinje i förväg | Varje pekarpassage över marginalen | Förhandsvisa kapitlet | ~120 ms | Dubblerar den status scrollen redan ger, och gör navet pekarberoende | **Avvisad.** ASSETS.md § A.9 Avoid ("hover-beroende status"); stress-personan är på telefon utan pekare, och `feel-and-fingerprint.md`: en teknik som bara finns på desktop får inte bära sidans mening |
| Skrafferingen växer eller tätnar när dess kapitel är aktivt | En gång per akt | Markera aktiv zon | ~300 ms | Konkurrerar med legendens ledarlinje om exakt samma jobb | **Avvisad.** Två statusmarkörer är ingen; TASTE § 1 (en auktoritet), F-003 (ett displayelement per skärm) tillämpat på status |

**Behållen, oförändrad:** ledarlinjen från legenden till aktivt kapitel. Den är navigationen.

## Delight-tes

Ritningen blir sidan.

## Asset-lock per medieplats

Sex platser. Fullständiga block, geometri och ritordning i `runs/K3/assets/ASSETS.md`
§ A.9. Ingen av dem är en generate-prompt; **noll genererat material ingar i K3**
(`assets/credits.json`). Saknas något: skriv `[needs asset: ...]` och ga vidare, generera
aldrig.

| # | Asset role | Slot | Media strategy |
|---|---|---|---|
| 1 | Sektionsritningen, inline-SVG | `viewBox="0 0 1440 900"`, hela a1:s pinnade scen | drawn system |
| 2 | Ritpapperstexturen, procedurell | fixed full viewport, `z-index: -1`, 256×256 tile | drawn system |
| 3 | Calyx i den ritade öppningen | rect x480 y240 w880 h495 i ritningens koordinatrum, 16:9 | product surface |
| 4 | Tre plates, a3 | tre ritade ramar 16:9, en per exempelsajt | product surface |
| 5 | Teckenförklaringen i vänstermarginalen | sticky, x 0 till 120 i ritningens koordinatrum | drawn system |
| 6 | Ordmärket i specifikationsramen, a6 | `logo-black.svg` inline, `currentColor` = `--ink`, en förekomst | drawn system |

## Fem live-rubriker i kategorin, ordagrant

Hämtade i R1, 2026-09-10. Sökning: `digital byrå webbdesign Sverige`. De fem bästa träffar
som är en byrås **egen** startsida togs; en katalogsida (`sverigesbyraer.se`) och två
undersidor uteslöts eftersom en undersidas H1 inte är kategorins skyltfönster. Varje rubrik
är hämtad ur den levande sidan, inte ur sökresultatets titel.

| # | Rubrik, ordagrant | Källa |
|---|---|---|
| 1 | `Webbyrå i Stockholm` | `frojd.se` |
| 2 | `Limetta är en digitalbyrå` | `limetta.se` |
| 3 | `Digitalbyrå / Webbyrå i Stockholm` | `ead.se` |
| 4 | `Webbyrå i Kalmar och Stockholm` | `wilsoncreative.se` |
| 5 | `En kreativ fullservice webbyrå innovativ webbyrå marknadsföringsbyrå som hjälper företag lyckas på marknaden` | `digitalwebbyra.se` (sidan har ingen `<h1>`; detta är den största synliga hero-rubriken, noterat som avvikelse) |

**Vad ribban faktiskt är, i en mening:** fyra av fem säger sitt eget yrke plus sin ort och
ingenting mer, och den femte säger yrket tre gånger i samma mening, så kategorins rubriknivå
är så låg att `Er hemsida är nutidens visitkort` slår hela fältet på att över huvud taget
handla om besökaren.

**Belägget för att detta inte är ett urvalsartefakt:** den låsta katalogposten `insign` är
samma kategori och samma land, och dess rubrik är `Din fullservicebyrå – Allt du behöver, på
ett ställe` (läst som pixlar i `entries/insign/fold.webp`), alltså samma form: yrket plus ett
löfte om bredd. Den räknas inte som en av de fem, eftersom den är en katalogfångst och inte
en R1-webbläsning, men den bekräftar mönstret ur en oberoende källa.

**Konsekvensen för copy-planen, som är hela skälet att transkribera dem:** kategoriformen
"substantiv plus ort" är förbjuden för varje ny sträng på sidan. Det träffar konkret
legendens fem kapitelnamn, som därför är ritnings- och liggarord (`TESEN`, `DETALJER`,
`LIGGAREN`, `STYCKLISTA`, `TITELBLOCK`) och inte tjänste- eller ortsord.

Regeln som gäller oavsett utfall: Alunix ordagranna rubrik `Er hemsida är nutidens
visitkort` ändras inte, och ingen ny sträng på sidan får falla tillbaka till
kategoriformen "substantiv plus ort".

## Copy-plan

**Ordagrant, ändras aldrig** (PRODUCT.md § Brand Commitments): `Er hemsida är nutidens
visitkort` · `Vi skapar skräddarsydda webbplatser som hjälper er att exponera
verksamheten.` · `VI BYGGER ERT VARUMÄRKE.` · `Webbdesign, design och system. Allt på ett
ställe.` · `Design` / `Utveckling` / `System` · de tre paketraderna med `26 900 kr`,
`38 900 kr` och `Pris vid förfrågan` · `Alla har rätt till bra design.` ·
`kontakt@alunix.se` · `Exempelsida: Calyx, florist i Stockholm` · `Exempelsida: Hōrai,
Asian fusion-koncept` · `Exempelsida: Hyperborea, konferens i Lund`.

**Nya strängar i K3, alla i registerrollen och alla underkastade copy-gatens fem pass i
R3.** De är fa med avsikt: ett ritark får bara bära ord som står på en ritning.

- Titelblockets tre fält: `ALUNIX` · `SEKTION A-A` · `SKALA 1:1`.
- Zonnamn, tre stycken: `marginal` · `spalt` · `fold`.
- Måttutrop, sex stycken, alla sanna: `320` · `768` · `1440` · `7 rem` · `96 px` · `16:9`.
- Snittmarkeringens två bokstäver: `A` och `A`.
- Legendens fem kapitelnamn, ett ord vardera, uppifrån och ner: `TESEN` · `DETALJER` ·
  `LIGGAREN` · `STYCKLISTA` · `TITELBLOCK`. Alla fem är rit- eller liggarord; inget är ett
  verb, ett löfte eller ett tjänstenamn, och inget faller i kategoriformen "substantiv plus
  ort". `TITELBLOCK` binder s11 tillbaka till s1.
- Tjänsternas tre underrader: `Vi ritar sidan innan vi bygger den.` · `Koden skriver vi
  själva.` · `Vi kopplar in CMS, bokning och betalning.` Tre olika satsformer, alla i
  byråröst, ingen med ett tal, en kund eller ett resultat.

**Förbjudet i copy:** tankstreck i synlig text, "jag", pahittade tal, ord som `Utforska`,
`Scrolla`, `Läs mer`, och varje etikett som beskriver ett gränssnitt som inte finns.

**Varje ny sträng på sidan, ordagrant och uttömmande, R1.** Listan är stängd: en sträng som
inte står här skrivs inte i R2 utan en ny rad i decision ledger. Nitton strängar, samtliga i
registerrollen utom tjänsternas tre underrader, som är röst.

| # | Sträng | Roll | Var |
|---|---|---|---|
| 1 | `ALUNIX` | register, `margin 12`, `--ink` | `#title-block` rad 1, s1 |
| 2 | `SEKTION A-A` | register | `#title-block` rad 2. **Bindestreck, aldrig tankstreck** |
| 3 | `SKALA 1:1` | register | `#title-block` rad 3 |
| 4 | `A` | register | Snittmarkeringens vänstra ände, x = 48 |
| 5 | `A` | register | Snittmarkeringens högra ände, x = 1392 |
| 6 | `320` | register, `display 72`, `--blue` | `#dim-width`, station vid x = 320 |
| 7 | `768` | register, `display 72`, `--blue` | `#dim-width`, station vid x = 768 |
| 8 | `1440` | register, `display 72`, `--blue` | `#dim-width`, högerställd mot x = 1430 |
| 9 | `7 rem` | register | `#dim-gutter`s utrop |
| 10 | `96 px` | register | `#dim-row`s utrop, och åter i a4:s marginal |
| 11 | `16:9` | register | `#lead-16-9`s utrop |
| 12 | `marginal` | register, zonnamn | `#lead-marginal` |
| 13 | `spalt` | register, zonnamn | Inuti spaltavståndet, ingen ledare |
| 14 | `fold` | register, zonnamn | Vid arkets underkant, ingen ledare |
| 15 | `TESEN` | register | Legendrad 1 |
| 16 | `DETALJER` | register | Legendrad 2 |
| 17 | `LIGGAREN` | register | Legendrad 3 |
| 18 | `STYCKLISTA` | register | Legendrad 4 |
| 19 | `TITELBLOCK` | register | Legendrad 5 |
| 20 | `Vi ritar sidan innan vi bygger den.` | **röst**, Chivo 300 / 15 px | Underrad till `Design`, a4 |
| 21 | `Koden skriver vi själva.` | **röst** | Underrad till `Utveckling`, a4 |
| 22 | `Vi kopplar in CMS, bokning och betalning.` | **röst** | Underrad till `System`, a4 |
| 23 | `01` `02` `03` | register | Radnummer i liggaren, a4 |

Kontrollerat mot förbudslistan: noll tankstreck, noll `jag`, noll tal utanför den tillåtna
listan, noll etikett som beskriver ett gränssnitt. Kontrollerat mot rollregeln: sträng 20 till
22 är de enda som sätts i Chivo, och ingen av dem står inuti `<svg>`-blocket, så
`grep -c Chivo` innanför blocket ger 0.

## Prestandaplan

`performance.md` § 1, rad för rad, med de två svara posterna utskrivna först.

**Svar post 1: tre live-iframes.** Alla tre monteras av en IntersectionObserver ungefär en
viewport i förväg, med `loading="lazy"` på varje `<iframe>` som andra spärr. Monteringen är
serialiserad: nästa ram sätter sin `src` först när den föregaende har fyrat `load`, sa
högst en ram laddar at gangen. En monterad ram rivs aldrig ner, transformeras aldrig och
tonas aldrig (PRODUCT.md § Operating Context). `content-visibility: auto` med
`contain-intrinsic-size` på a3:s tre plate-sektioner och på a5.

**Mätt i R1, inte antaget.** Kommandot, kört från repo-roten mot den egna servern på 3302,
vid ramens egen storlek 880 × 495 och 4× CPU:

```
python ~/.claude/skills/design/scripts/serve.py --port 3302 --root .
python ~/.claude/skills/design/scripts/perf_probe.py --url http://127.0.0.1:3302/sites/<sajt>.html --cpu 4 --width 880 --height 495 --json
```

| Exempelsajt | Överföring | Varav bild | Varav typsnitt | LCP (4× CPU) | CLS | DOM |
|---|---|---|---|---|---|---|
| Calyx | **1,48 MB** | 1 436 737 B, 4 filer | 61 904 B, 3 filer | 7 496 ms | 0,0006 | 147 |
| Hōrai | **2,90 MB** | 2 422 184 B, 5 filer | 590 864 B, 13 filer | 2 896 ms | 0,025 | 210 |
| Hyperborea | **0,40 MB** | 0 B, 0 filer | 378 348 B, 13 filer | 2 388 ms | 0,156 | 389 |
| **Summa** | **4,78 MB** | | | | | |

**Fyndet, rapporterat till lead.** Ramarnas summa ensam är **4,78 MB mot budgetens tak
2,5 MB**, alltså 191 % av taket innan K3:s eget skal räknats med. Tre följdfakta som lead
äger, och som inte är K3:s att fixa:

1. Calyx och Hōrai **hotlänkar sina tyngsta bilder från `images.unsplash.com`**, den största
   1 122 865 B. Det är exakt sidofyndet i F-013 och ett brott mot `performance.md` § 6 rad 1,
   i kedjans egna exempelsajter. Vendorade och WebP-omkodade skulle de två tillsammans
   sannolikt falla under en fjärdedel.
2. Hōrai och Hyperborea drar **13 typsnittsfiler var**, mot taket 3. Det är Noto Serif JP i
   många subset-block. Hyperborea har noll bilder och ändå 0,40 MB: allt är typsnitt.
3. Hyperborea mäter **CLS 0,156**, mer än tre gånger taket 0,05. Inuti en `<iframe>` påverkar
   det inte K3:s egen CLS, men det syns för besökaren i ramen.

**Vad K3 gör åt det, och vad K3 inte gör.** Serialiseringen och `content-visibility` flyttar
kostnaden i tid, inte i byte; de gör att ingen ram konkurrerar med en annan och att ingen
laddar före sin viewport, men de kan inte få 4,78 MB att bli 2,5. **Ingen ram byts mot en
skärmbild utan leads beslut** (PRODUCT.md § Operating Context: beviset ska gå att använda).
Nästa konkreta steg för lead: antingen vendora och WebP-omkoda Calyx och Hōrais hotlänkade
bilder och subsätta Noto Serif JP i de två sajterna, vilket sannolikt räcker för att komma
under taket, eller besluta att K3 mäts mot en egen budgetrad där ramarnas transfer redovisas
separat, på samma sätt som en scrubbad klipp redan har en egen rad i `performance.md` § 1.
Jag antar det första tills lead säger annat, och mäter om i R2.

**Svar post 2: den procedurella texturen.** Den rastreras **en gang** och animeras aldrig
per frame. Mekaniken: filtret ligger i en `data:`-URI-SVG som används som
`background-image` på ett `position: fixed; inset: 0; z-index: -1; pointer-events: none`-lager
med `background-repeat: repeat` och `background-size: 256px 256px`. Webbläsaren rastrerar
SVG-bilden en gang till sin bildcache och kaklar sedan bara den cachade bitmappen. Det är
alltså **inte** en `filter:`-egenskap på ett element, vilket hade brutit budgetens rad
"`filter` / `backdrop-filter` på > 50 % av viewporten: 0". `background-attachment` får
aldrig vara `fixed`. Lagret får ingen `transform`, ingen `will-change` och ingen animation.

| Budgetpost | Gräns | Plan i K3 |
|---|---|---|
| LCP | ≤ 1,8 s | **LCP-elementet är titelblockets textblock** i övre vänstra hörnet, satt i Martian Mono. Det finns ingen bild på LCP-vägen: ritningen är inline-SVG utan `<image>`, och texturen är en `data:`-URI utan natverksrunda. Skulle Chrome i stället välja texturlagret som kandidat kostar det ändu ingen begäran |
| CLS | ≤ 0,05 | `aspect-ratio` på varje ritad öppning och varje plate; metric-matchad fallback med `size-adjust` för bada snitten; ritningens `<svg>` har fast `viewBox` och reserverar sin hojd i förväg |
| Langa tasks under scroll | 0 | Ritningen skrivs aldrig från JS: varje bana är ett `calc()` i CSS mot `--sc-ps`. Enda JS på sidan utover motorn och shimen är IntersectionObserver-monteringen och `count`, bada utanför scroll-handlern |
| Frametid under scroll | p95 ≤ 20 ms, ingen > 33 ms | `stroke-dashoffset` på ≤ 60 banor i **en** `<svg>`; `will-change: stroke-dashoffset` bara medan `0 < ps < 1`; skrafferingen är den enda banan som avslöjas med `clip-path` i stället för dash |
| Overföring vid 1440 | ≤ 2,5 MB | Se svar post 1. Skalet självt (HTML + SVG + två snitt + textur) ska ligga under 400 kB. **Prognos ur kända tal, R1:** texturen ~0,7 kB som `data:`-URI, ritningen 25 banor plus 14 textnoder inline, alltså inga nätverksrundor alls, och de två variabla `.woff2`-filerna som lead vendorar är den enda posten som kan flytta talet, med tak 300 kB. Prognosen är alltså ~310 kB, med god marginal till 400. `[needs: mätning i R2]`. Talet mäts på den byggda filen med `perf_probe.py`, aldrig skattat vidare. Ramarnas 4,78 MB är mätta och står ovan |
| Hero-bild | ≤ 250 kB WebP | Ingen hero-bild finns. Posten är noll: heron är linje och typ |
| Typsnitt | ≤ 3 filer, ≤ 300 kB | Exakt två filer, bada variabla `.woff2`, self-hostade: Chivo (viktaxel 300 till 700) och Martian Mono (vikt- och breddaxel). Ingen Google Fonts-länk, ingen `preconnect`. Subsätts med `pyftsubset` till latin plus `å ä ö Å Ä Ö` om summan överstiger 300 kB. `font-display: swap`. **`<link rel="preload" as="font" crossorigin>` bara på Martian Mono**, därför att titelblocket är det enda som står i folden vid `--sc-ps` = 0 och det är satt i mono. Chivo preloadas inte |
| DOM | ≤ 1500 noder | Ritningen är ~25 stroke-banor plus ~14 textnoder; legenden 5 rader; liggaren 3 rader; specifikationen 3 rader |
| Vilande `will-change` | 0 element | Ingen klassniva-promovering nagonstans. Shimen sätter och tar bort `will-change` per akt |
| `filter` / `backdrop-filter` > 50 % av viewporten | 0 | Noll `backdrop-filter` på sidan. Texturens `feTurbulence` körs inuti en `data:`-URI-bild, aldrig som en `filter:`-egenskap på ett element |

Dessutom: `min-height: 100dvh`, aldrig `100vh`. Ingen `transition: all`. Alla `<img>` och
`<iframe>` har `width` och `height`.

Maltal som ska vara sanna innan rundan lämnas, mätt vid 4× CPU (F-014,
`motion-smoothness.md` § The bar): `staircase = 0`, `max_step ≤ 3 %`, frametid
p95 ≤ 20 ms, noll frames > 33 ms, **bada scrollriktningarna mätta**, LCP ≤ 1,8 s,
CLS ≤ 0,05.

## `?preview=`-plan

Alla lägen sätter `window.__scFreezeMotion = true` sa att shimen sparar det raa värdet
exakt och skärmbilden visar det formade läget, inte en lerp i flykten.

| Läge | Vad det tvingar | Varför det behövs |
|---|---|---|
| `?preview=sheet` | `--sc-ps: 0` i a1: tomt ark, bara titelblocket | Baslinjen för folden och för den författade tystnaden |
| `?preview=drawn` | **Tvingar det ritade läget:** varje banas lokal `--l` = 1, hela ritningen färdig, måttsiffrorna landade på sina sanna tal, men öppningen ännu **inte** fylld | Det är detta läge F-007-kontrollen läser bild för bild mot gate 47/79: varje `<rect>` och `<path>` ska ga att namnge som kontur, måttlinje, hjälplinje, skraffering eller utrop |
| `?preview=filled` | `--sc-ps: 1` i a1: Calyx monterad i öppningen, konturen kvar som ram, siffrorna nedskalade till 12 px | Kontrollen av F-010: att bläcket ligger kvar ovanpa och att ramen inte blivit ett kort |
| `?preview=mid` | `--sc-ps: 0.94`, siffrorna halvvägs i nedskalningen | Legibilitetskontrollen: vid halva vägen är siffran ~42 px och måste fortfarande läsas som en siffra, inte som en suddig form |
| `?preview=spec` | a6:s ram fullt indragen | Skärmbild av avslutet i vila |
| `?preview=legend` | Tvingar legendens ledarlinje **fullt utdragen** från en namngiven rad ut till det kapitlets kontur, med raden i sitt aktiva tillstånd. Läget tar ett kapitelnamn: `?preview=legend:LIGGAREN` | Ledarlinjen **är** navigationen och den finns i inget av de fem lägena ovan. Utan detta läge kan sidans enda statuskvittens aldrig skärmbildas i vila, och en granskare kan inte kontrollera att den slutar i en punkt och inte i en pilspets (ASSETS.md § A.3) |
| `?preview=plates` | Tvingar a3:s tre `reveal` till 1: alla tre plate-ramar färdigritade och alla tre sajter monterade innanför sina konturer | Gate 47/79-kontrollen måste kunna köras på a3 med samma bild-för-bild-metod som på a1. Utan läget granskas bara en av fyra ritade öppningar på sidan, och a3:s tre ramar är exakt där en enhetsattrapp skulle smyga sig in |

## Fingerprint

Cellens rad i registrets sex dimensioner, ordagrant ur `concepts-K3.md` (4). Lead för in
den i `wiki/projects/_index/design-fingerprints.md` efter Antons dom, inte byggaren.

```text
K3 · Ritningen | Chaptered editorial | Nav: ritad teckenförklaring i vänstermarginalen,
sticky, ingen topprad alls: fem rader med symbolprov (hårlinje, måttpil, skraffering) plus
kapitelnamn, och en ledarlinje som ritas från den aktiva raden ut till kapitlets egen
kontur | Hero-device: en måttsatt sektionsritning av en webbsida i inline-SVG som ritar sig
själv ur stroke-dashoffset drivet av --sc-ps i en pinnad akt, span 2,4; måttsiffrorna
räknas upp till sanna värden; akten slutar med att Calyx fold maskas in i den öppning
bläcket just ritat | Aktform: 6 akter, ~13 vh: pin 2,4 -> kinetic lines -> reveal ×3 ->
flow+in -> count -> reveal (avslut). Noll scrub, noll drift, noll pan, noll pekar-devices |
Avslut: ett specifikationsblad på samma kalla papper: paketen som stycklista med
ledarpunkter och sanna priser, manifestraden och en mailto, allt inuti en ritad ram vars
linjer dras in sist; ingen inversion, sidan slutar stilla | Signatur: ritningen blir sidan:
konturen ritas, den riktiga kundsidan maskas in i öppningen konturen skapat, bläcket står
kvar som ram
```

Gaten är körd mot alla 36 byggrader i registret i `concepts-K3.md` (4). **Lägsta summa
5/6**, mot nio rader (Calyx, Hyperborea, Vintergatan, Vinterspelen, r1 K4, r2 R2, r2 R3,
r2 R4, r4 M2), och i samtliga fall är den delade dimensionen grammatik, som målbilden själv
laser. Ingen rad faller under 4/6.

**Byggarens verifiering, R1.** Jag har läst hela
`C:\Users\Anton L\OneDrive\Dokument\Obsidian\Knowledge Base\wiki\projects\_index\design-fingerprints.md`,
alla rader: sju seedrader plus tjugonio Alunix-rader, alltså **36**, vilket stämmer med
arkitektens räkning. Ingenting i registret motsäger cellens rad. Tre iakttagelser som
skärper eller bekräftar den:

1. **Registrets egen varningstext pekar åt K3:s fördel.** § "Reading this table" säger att
   nav och hero-device är de kolumner som oftast kolliderar igen bland
   chaptered-editorial-raderna, och namnger de två mönster som redan är förbrukade:
   folio- eller edition-strip-nav, och type-in-photo- eller split-poster-heron. K3 använder
   ingetdera: navet är en ritad legend utan topprad, och heron är en självritande SVG utan
   fotografi. De två dimensionerna som var mest utsatta är alltså de två K3 skiljer sig
   tydligast på.
2. **Två nav-mönster är utskrivna som "used up"** i § "What these rows share": den tunna
   scrollande topprad som M1, V1, V2, V3 och V3b delar, och den fixerade minimala baren i
   r6 A-K1, B-K1, B-K1-nogate och r7 B-K1. K3 delar inget av dem, vilket bekräftar
   nav-kolumnen mot nio rader på en gång.
3. **Continuous world är den mättade familjen, inte chaptered editorial.** Registret noterar
   att M1, V1, V2, V3 och V3b klarar gaten mot varandra på exakt 3 av 5 icke-fria
   dimensioner och att "a sixth build in that family would have nowhere left to differ".
   K3 ligger inte i den familjen, och den delade grammatiken (chaptered editorial, nio rader)
   kostar K3 en dimension mot var och en av dem, aldrig fler, eftersom nav, hero, aktform,
   avslut och signatur alla skiljer sig mot samtliga nio.

**Rad som ännu inte finns i registret:** K3 själv. Lead för in raden efter Antons dom, inte
byggaren (`feel-and-fingerprint.md`: rader är append-only och en plan som faller ändras,
aldrig registret).

## Vad jag måste slå

En rad per låst referens. Full tabell med mätpunkter i `concepts-K3.md` (7).

**Varje rad namnger sitt belägg** (leads R1-granskning, 2026-09-10): den slice, eller den
rad i referensens `entry.md`, som påståendet vilar på. En rad utan pekare stryks ur låset i
fas 2. Tre påståenden gick inte att belägga ur folden ensam; de raderna säger det rakt ut
och pekar på `entry.md` i stället.

- `squarespace`: reservationen är strukturell, inte bara kromatisk. Det enda mättade i vyn
  är en kundsajt inne i den ritade öppningen, och det enda kromatiska på arket är en sann
  mått-siffra.
  **Belägg:** `entry.md` § Why it works, *"reserving all colour for the user-built sites
  shown in screenshots and video makes the product itself the only vivid thing on the
  page"*, plus § Reference lock raden `Media strategy`. **Inte belagt ur folden ensam:**
  `fold.webp` är en varm, kromatisk dokumentärvideo, alltså motsatsen till det akromatiska
  påståendet. Det akromatiska gäller UI-lagret och inte fotografiet, och det syns först i
  `slices/01.webp` (svart statband) och `slices/06.webp` (hårlinjeaccordion på svart).
  `steps(1, start)`-lånet är belagt i `extract/squarespace-com-design-language.md`
  § Transitions, `transition: opacity 0.3s, visibility 0.3s steps(1)`.
- `insign`: navigationen bärs av ett system som läses före texten, men systemet är ritade
  symboler och inte färg, och det finns noll bevisapparat att slå: inga betyg, inga
  omdömen, ingen teamgrid.
  **Belägg:** `slices/05.webp` bär hela bevisapparaten i **ett** viewport: `5.0/5.0` ·
  `180+` · `2002` över ett kontorsfoto av ett leende team, följt av en nio märken bred
  logotypvägg. `slices/01.webp` bär chipet `5/5 baserat på 130+ omdömen`. `slices/06.webp`
  bär sex svartvita porträtt under `En långsiktig partner`. Färgbanden som navigation:
  `slices/02.webp`. Att systemet läser som mall är dessutom mekaniskt mätt i
  `extract/insign-se-design-language.md`: 24 färger i inventariet, tio radievärden, nio
  `box-shadow`, och sex typsnittsfamiljer där `Times New Roman` sätter 105 element.
- `aevi-wellness`: varje linje har en namngiven roll (kontur, måttlinje, hjälplinje,
  ledare, skraffering) och en linje utan roll ritas inte. Noll `box-shadow` i filen.
  **Belägg:** `entry.md` § Why it works, *"Elevation is banned outright — no shadow, no
  glow, no blur anywhere in the system"*, och § Reference lock raden `Role rules`.
  **Inte belagt ur folden ensam, och kan inte bli det:** posten har varken `slices/` eller
  `extract/` (`extract: none`), så `fold.webp` visar bara heron med presslogoraden.
  Hårlinjen som enda strukturmedel är ett textpåstående i posten, inte en pixelläsning, och
  posten behandlas därför som yt- och regelkälla och aldrig som rörelsekälla.
- `beautiful`: accentregeln är granskningsbar och hårdare: ett blått moment per viewport,
  och momentet är alltid ett verkligt uppmätt tal.
  **Belägg:** `entry.md` § What to borrow punkt 1, ordagrant: *"Cap a rationed accent to a
  literal one-per-screen rule. 'One coral moment per viewport maximum' is concrete enough
  to audit"*, plus § Reference lock raden `Preserve`. **Folden bekräftar att regeln hålls i
  praktiken:** `fold.webp` bär exakt ett korallmoment, den fyllda pillknappen, plus en
  tracked-out korall-eyebrow. Posten saknar `slices/` och `extract/`.
- `mode`: inhägnaden går från komponent till innehållstyp, och legenden styr sidan i
  stället för att förklara en bild.
  **Belägg:** legend-mönstret är pixelläst i `slices/04.webp` och `slices/05.webp`: fem
  rader `swatch + versalt namn` (`MODERN BI`, `TRANSFORMATION`, `WAREHOUSE`, `INGESTION`,
  `RAW DATA`) bredvid den isometriska lagerillustrationen. Komponentinhägnaden står i
  `entry.md` § Why it works, *"the only filled button color in the system"*. **Och den är
  mätbart svagare än posten påstår:** `extract/mode-com-design-language.md` § Full Color
  Inventory visar chartreuse `#c8f169` i kontexterna `background, text, border`, alltså
  inte bara som fylld knapp. Det är precis skälet att K3 binder accenten till en
  **innehållstyp**: en komponentregel kan drifta när en ny komponent uppstår, och här har
  den redan gjort det.
- `before-ai-slop`: ritningen ritar form, aldrig innehåll. Varje siffra på sidan är sann.
  Den enda ytan som visar ett gränssnitt är ett riktigt gränssnitt.
  **Belägg:** filen läst som kod, 155 rader. Låtsas-dashboardet rad 71 till 94 (fyra
  påhittade stat-tiles plus en `<path>`-sparkline); gradientordet rad 50 (`.grad-text` på
  `all-in-one`); logotypväggen rad 98 till 103; de tre ikonkorten rad 111 till 127; de tio
  påhittade talen rad 66, 78 till 81 och 135 till 138. K3:s motsvarighet är verifierad i
  `shots/r2/drawn-1440.png` mot elementtabellen i `NOTES.md` § R2, bana för bana: nitton
  ritade element, var och en namngiven som kontur, snittmarkering, måttlinje, hjälplinje,
  ledare, skraffering eller utrop.

## Lästa referenser

Tre rader per fil, i den ordning jag läste dem: **vad den gör · vad jag tar · vad jag
lämnar.** Bilder är lästa som pixlar, inte som filnamn. Arkitektens egen digest står i
`concepts-K3.md` § Lästa referenser och ersätter inte den här. **Trettiofem filer plus
tjugoåtta bilder.**

### Smak och återkoppling

**`design-catalogue/TASTE.md`** (hel) · Beskriver harmonin i 89 sparade källor: en auktoritet
per sida, och vad de tre andra gör när den fjärde bär. · **Tar:** § 1 rad 3, ytan som
auktoritet, med typ medelstor, bild tyst och yta som bär allt genom ton på ton och hårlinjer;
§ 4.9, siffror får vara textur bara om de är sanna, vilket är Alunix-regeln namngiven i
profilen själv; § 2.4, storlekskontrast 5× eller mer, som ger K3:s 72/15/12 i stället för en
32 px-mellannivå. · **Lämnar:** § 3 editorial-raden (serif tillåten och vanlig), eftersom K3:s
ämne är precision och inte en tidskrift; § 4.10 (ordmärket får vara heron), eftersom K3:s
hero är en ritning och ordmärket sparas till a6.

**`design-catalogue/FEEDBACK.md`** (alla 14 poster) · Antons domar över kedjans egna bygg, en
regel per post med citatet oredigerat. · **Tar:** F-006 (glaskort och telemetri-chrome är
slop, stoppas i målbildsgrinden), F-010 (innehållet maskas in i objektets **verkliga**
öppning och materialet ligger kvar ovanpå), F-011 (rörelsen spelar alltid, ingen
reduced-motion-gren), F-012 och F-014 (hackighet är två fel och båda mäts före någon ändring;
allt ögat ser förflytta sig läser `--sc-ps`), F-003 (ett displayelement per skärm), F-007
(avvikelse från signaturakten stoppar rundan), F-009 (orkestreraren äger assets, byggaren
genererar inget). · **Lämnar:** F-001 och F-002, uttryckligen upphävda av F-011, och F-004
och F-005, som gäller K2:s typburna hero och inte den här cellen. Noterat för egen del:
F-014:s efterspel säger att `--sc-ps` registrerad med `inherits: false` gör att ett **barn**
som läser den får 0. Ritningens banor är barn till akten, så det är den enskilt farligaste
fällan i R2.

### De fem låsta katalogposterna

**`entries/squarespace/entry.md`** (hel, inkl. § Motion och § Reference lock) · Deklarerar
0 % colourfulness som **strategi**: eftersom produkten är webbplatser reserveras all mättnad
för kundernas egna sajter, och marknadsföringsytan hålls akromatisk. · **Tar:** reservationen,
flyttad från kromatisk till strukturell; och `steps(1, start)` ur den uppmätta motion
language, lånad enbart som räknarbeteende, en måttsiffra landar på ett heltal. · **Lämnar:**
den akromatiska paletten (K3:s papper och bläck är kalla men kromatiska), radiesplitten
0/8/100 px (K3 har radie 0 och inga knappar), vikt 300 på display (K3:s display är mono 500).

**`entries/squarespace/fold.webp`** + **`slices/00` till `08`** (10 bilder) · Folden är
fullbleed dokumentärvideo i **varm** ton med en vikt-300-rubrik centrerad i bilden och tre
kundsajter som lutande plattor längs nederkanten; `01` är ett svart statband `14M+` `$36B+`
`200+`; `05` är en avatarstack över `Trusted by 14 million entrepreneurs worldwide`; `06` är
tre hårlinjeledda accordionrader på svart; `07` är en partikelsfär bakom slut-CTA:n; `08` en
femspaltig svart footer. · **Tar:** `06`:s hårlinjeledger som strukturspråk, och den
bekräftade observationen att det **enda** färgstarka i varje vy är en kundsajt. · **Lämnar:**
allt siffrornas innehåll (`14M+`, `$36B+`, `200+`, `14 million` är precis PRODUCT.md:s
absences-lista), avatarstacken, pill-flikarna i `01`, partikelsfären, den centrerade heron
och de lutande plattorna. Rättelse mot minnet: folden är **inte** svartvit, den är varm och
kromatisk; det akromatiska gäller UI-lagret, inte fotografiet.

**`entries/squarespace/extract/squarespace-com-design-language.md`** · Uppmätt token-dump:
sex neutraler dominerar (`#000000` 3 585 gånger, `#ffffff` 2 722), Clarkson 300 vid 60 till
70 px med −3,5 px tracking, och `steps(1, start)` i den dokumenterade transitionlistan. ·
**Tar:** bekräftelsen att `steps()`-tickningen finns i källan och inte är min tolkning;
skalan 70/60/50 mot body 16, alltså ~4,4×, som jag höjer till 4,8× (72/15). · **Lämnar:** de
nio gradienterna, de fem `box-shadow`-posterna, `transition: all` (som står först i
listan och som `performance.md` § 6 kallar en defekt), radie 30/50/100 px.

**`entries/insign/entry.md`** · Svensk fullservicebyrå: tre tjänster som tre fullmättade
färgband så att paletten **är** navigationen, allt utanför banden vitt eller nästan svart,
och bevisen varierade i format i stället för upprepade. · **Tar:** principen att navet bärs av
ett enda konsekvent system som läses före texten. · **Lämnar:** att systemet är färg (K3
navigerar med ritade symboler), pillformerna, och hela bevisapparaten.

**`entries/insign/fold.webp`** + **`slices/00` till `07`** (9 bilder) · `00` och folden:
`Din fullservicebyrå – Allt du behöver, på ett ställe` i två rader över en mosaikremsa av
kundarbeten; `01` bär ett Google-betygschip `5/5 baserat på 130+ omdömen` och visar rubriken
`Webbdesig / n` bruten mitt i ordet; `02` de tre färgbanden med varsin enhetsbild; `03` ett
projektarkiv med `80 projekt`; `05` ett mörkt statband `5.0/5.0` · `180+` · `2002` över ett
kontorsfoto av ett leende team, följt av en nio märken bred logotypvägg; `06` sex svartvita
porträtt bredvid `En långsiktig partner`; `07` nyhetsremsa och mörk kontaktsektion med fyra
pill-knappar. · **Tar:** att varje tjänst får exakt **en** konkret bild av en verklig leverans
och aldrig en ikon. · **Lämnar:** `05` i sin helhet, som är den tätaste enskilda bilden av
allt PRODUCT.md § Absences förbjuder: betyg, antal omdömen, år i branschen, antal projekt,
team, kontor, logotypvägg, i ett och samma viewport. Och den brutna rubriken i `01`, som
posten flaggar själv, är den konkreta anledningen att K3:s legendnamn har ett mätt takmått.

**`entries/insign/extract/insign-se-design-language.md`** (läst tillsammans med entryts
§ Motion) · Rörelsen är stock-chrome ur en WordPress-byggare: `fadeIn`,
`ball-scale-multiple`, `dipi_fade`, plus en enda overshoot-kurva. · **Tar:** varningen. En
sida vars rörelse är bibliotekets keyframes läser som mall, oavsett hur ytan ser ut. Varje
rörelse i K3 är namngiven i device-tabellen och härledd ur `--sc-ps`. · **Lämnar:** overshoot
helt (fjädring hör inte hemma på ett ritark) och tredje person (Alunix röst är vi-form).

**`entries/aevi-wellness/entry.md`** · Nästan akromatiskt system med exakt en kromatisk
accent på en enda knapp; **varje** textstorlek från 10 till 54 px kör vikt 300, så hierarkin
bärs av grad och radavstånd; elevation är förbjuden rakt av och djupet kommer ur bandväxling
och hårlinjer. · **Tar:** hårlinjen som **enda** strukturmedel, och det uttryckliga
skuggförbudet, skärpt ett steg i K3: en linje utan namngiven roll ritas inte alls. ·
**Lämnar:** enviktssystemet (K3 behöver två för att skilja utrop från måttsiffra),
pill-knappen, och den fullbleed produktfotografi hela systemet vilar på.

**`entries/aevi-wellness/fold.webp`** · Ordmärket `AEVI` som ett översiktligt genomskinligt
lager ovanpå produktfotot, versal underrubrik i vikt 300, en tunn outlinad pill, och direkt
under folden en pulverblå **presslogorad** med fyra magasinmärken. · **Tar:** ingenting av
kompositionen. · **Lämnar:** ordmärket som vattenstämpel, presslogoraden (Alunix har inga
presslogotyper), fotot som grund. Posten saknar `slices/` och `extract/`, så dess § Motion är
**inferred** och behandlas som yt- och strukturkälla, aldrig som rörelsekälla.

**`entries/beautiful/entry.md`** · Gräddlinne som canvas överallt i stället för vitt;
korallen ransonerad till en bokstavlig, granskningsbar regel, ett korallmoment per viewport;
radie har exakt två värden bundna till funktion; tracking **öppnar** när graden växer. ·
**Tar:** den granskningsbara accentregeln, ordagrant överförd som ett blått moment per
viewport, och sedan hårdare bunden: momentet är alltid ett verkligt uppmätt tal. · **Lämnar:**
cream (K3:s papper är kallt, AB09-lärdomen, låst av lead), pillspråket, den centrerade
logotypen, och den öppnande trackingen, eftersom måttsatt typografi vill ha stram tracking.

**`entries/beautiful/fold.webp`** · Centrerad serif-logotyp flankerad av svartkantade
nav-piller, asymmetrisk hero 60/40 med produktfoto till vänster och en korallpill till höger,
allt på gräddlinne; en tracked-out korall-eyebrow `BEST-SELLERS` ovanför rubriken. · **Tar:**
ingenting av kompositionen. Bekräftar bara att korallen faktiskt förekommer en gång i vyn,
alltså att regeln hålls i praktiken och inte bara i entryts text. · **Lämnar:** hela
pillspråket, produktfotot, gräddlinnet. Posten saknar `slices/` och `extract/`; samma
behandling som aevi.

**`entries/mode/entry.md`** (wildcard, `split stage`, utanför kategorin) · Inhägnar accenten
till exakt en komponenttyp, "the only filled button color in the system", och bygger djup ur
en färgstack i stället för skugga; serifen låst till 36 px och uppåt i en enda vikt. ·
**Tar:** inhägnadsprincipen, skärpt ett steg: K3 inhägnar accenten till en **innehållstyp**
(ett sant uppmätt tal), inte till en komponent, eftersom en komponentregel kan drifta när en
ny komponent uppstår och en innehållsregel inte kan. · **Lämnar:** färgstacken, serifen,
16 px-radien, chartreusen, och den andra fenced accenten för dataviz.

**`entries/mode/fold.webp`** + **`slices/00` till `10`** (12 bilder) · `04` och `05` bär det
enda jag är här för: en isometrisk lagerillustration med en **färgkodad teckenförklaring**
bredvid sig, fem rader `swatch + versalt namn` (`MODERN BI`, `TRANSFORMATION`, `WAREHOUSE`,
`INGESTION`, `RAW DATA`), som gör bilden läsbar utan en enda bildtext. Resten: `00` chartreuse
pratbubbleformer över ett dokumentärt teamfoto plus ett `8.2K`-statkort; `06` logotypvägg och
citatkort med porträtt, namn och titel; `08` ett bento av sex ikonkort; `09` och `10` ordmärket
i jättegrad över en femspaltig footer. · **Tar:** exakt en sak, legend-mönstret. K3:s
marginallegend är samma idé, ritad i stället för färgad, och den styr sidan i stället för att
förklara en bild. · **Lämnar:** allt annat, och särskilt `08`:s ikonbento och `06`:s
citatkort, som båda är troplistan.

**`entries/mode/extract/mode-com-design-language.md`** (läst tillsammans med entryts § Motion)
· Overshoot-kurva, en `scroll`-keyframe som är en marquee, och postens egna anmärkningar
"4 font families" och "75 % av CSS oanvänd". · **Tar:** varningen mot fyra typsnittsfamiljer.
K3 kör två, och rollerna korsar aldrig. · **Lämnar:** overshoot, marquee, de två box-shadows.

### Anti-referensen

**`sites/before-ai-slop.html`** (hel, 155 rader, som kod) · Sticky flytande pill-nav med
`backdrop-blur`; centrerad hero med badge-rad och pulserande prick, ett `.grad-text`-satt ord
mitt i rubriken, två pill-CTA och en avatarstack av fyra gradientcirklar; till höger ett
div-byggt "Dashboard preview"-kort med fyra påhittade stat-tiles och en SVG-sparkline; sedan
`Trusted by teams at` med sex påhittade ordmärken, tre likadana ikonkort med emoji i
gradientrutor, ett fyrfältsstatband (`10x`, `99.99%`, `50%`, `10k+`), en centrerad CTA och en
enradsfooter med en hjärt-emoji. · **Tar:** ingenting. · **Lämnar:** allt.

**De fem drag jag aktivt bygger bort**, ett per konstruktionsbeslut och inte per intention:

1. **Den flytande pill-navraden** (rad 22 till 40). K3 har **ingen topprad över huvud taget**.
   Navet är en ritad legend i vänstermarginalen vars enda status är en ledarlinje som dras,
   inte en färg som tänds. Kontrollen: noll `position: sticky` eller `fixed` på något element
   ovanför `y = 0` i ritningens koordinatrum, och noll `border-radius` över hela filen.
2. **Det div-byggda dashboardkortet** (rad 71 till 94): ett låtsasgränssnitt av `<div>` med
   fyra påhittade nyckeltal och en `<path>`-sparkline i en `<linearGradient>`. K3:s enda yta
   som visar ett gränssnitt är ett **riktigt** gränssnitt, en Alunix-exempelsajt live i en
   `<iframe>` på samma origin. Ritningen ritar form och aldrig innehåll: varje `<rect>` och
   `<path>` ska kunna namnges som kontur, måttlinje, hjälplinje, skraffering eller utrop.
   Kontrollen är `?preview=drawn` och `?preview=plates`, lästa bild för bild mot gate 47/79.
3. **De påhittade talen.** Filen bär `51%`, `16%`, `17`, `1.8%`, `10,000+`, `200+`, `10x`,
   `99.99%`, `50%`, `10k+`, alltså tio tal, varav noll är sanna. K3 har **nio tillåtna
   strängar med siffror i hela filen** och listan är stängd: `320`, `768`, `1440`, `7 rem`,
   `96 px`, `16:9`, `26 900 kr`, `38 900 kr`, `01` till `03`. Måttkedjan är därför en
   stationskedja och inte en vanlig kedja, eftersom en vanlig hade producerat `448` och
   `672`, två tal som inte finns.
4. **Gradientordet i rubriken** (rad 50, `.grad-text` på `all-in-one`), plus de fem
   gradienterna i övrigt. K3 har **noll** `linear-gradient`, `radial-gradient` och mesh; en
   enda kromatisk färg på hela arket; och den färgar bara måttsiffror i displaygrad, aldrig
   ett ord i en rubrik. Kontrollen: `grep -c gradient` över filen = 0.
5. **Logotypväggen och de tre likadana ikonkorten** (rad 98 till 128): sex påhittade
   ordmärken och tre `rounded-2xl`-kort med emoji i gradientrutor. K3 har noll kunder utöver
   de tre exempelsajterna, noll ikoner, och tjänsterna 01 till 03 är tre **hårlinjerader med
   olika radlängd** i en liggare, aldrig tre lådor bredvid varandra. Samma sak i avslutet:
   paketen är en stycklista i **en** ritad ram, aldrig tre priskort med ett märkt
   "populärast".

### Kedjans referenser

**`references/reference-lock.md`** · Sätter lockens sju fält, decision ledger som villkor för
att skeppa ett val, asset-locken före sökning, och tre persona-skisser med situationella
villkor. · **Tar:** anti-averaging-testen (identitet, editorial, screenshot), som jag kör mot
locken nedan; kravet att `Memorable detail`-raden finns och är ifylld; regeln att media
strategy är en **enum** per plats och inte prosa. · **Lämnar:** ingenting; filen är
tillämplig i sin helhet. Not: § Transcribe the category's live headlines är den paragraf som
gjorde `[needs: live-rubriker]` till en R1-uppgift, och den är nu stängd.

**`references/scroll/devices.md`** · De nio devicefamiljerna med span, cue-kontrakt och de
fem reglerna som en riktig bugg ligger bakom var. · **Tar:** cue-kontraktet i sin helhet, och
särskilt "endast sista akten får hålla" (a6 har ett värde, `0.25`) och "ground or greet"
(a1 har `0 1 0 0` **och** en ground, arket); § 7, endast sanna tal får en count; § 9, `magnet`,
`parallax` och `cue` kan inte dela element, vilket gäller a5 där parallaxen ligger på
marginalspalten och cuen på innehållet. · **Lämnar:** `scrub` (noll på sidan), `pan` (noll),
`iris` (sparad och oanvänd), alla tre pekar-devices, och § "Layered scenes", som är en
fotografisk teknik utan motsvarighet på ett plant ark.

**`references/scroll/feel-and-fingerprint.md`** · Feeling curve före akter, en enda topp,
tell-someone-testet, signaturmovet, embodiment som krydda, pacing som känsla, och
fingerprint-gaten. · **Tar:** § The peak (toppen får störst span, tystnaden före, och en sida
med tre toppar har ingen) som är skälet att a3 avsiktligt degraderades; § Pacing, "silence
must be authored", som är skälet att den författade tystnaden står utskriven; § Being in it,
"one or two per page", som ger exakt en embodiment. · **Lämnar:** pointer-parallax,
scrollhastighet som intensitet, sidan som tilltalar "du", och "a trace of where they have
been", alltså fyra av fem embodiment-tekniker, eftersom en är taket.

**`references/scroll/pace.md`** · `rate = weight / clip_seconds`, spridningen 36 % som läser
som defekt mot 6 % som läser som en rörelse, och de olika lerp-värdena för worldflight. ·
**Tar:** insikten som **inte** handlar om film: en ojämn takt läser som ett fel i sidan, inte
som pacing. K3:s motsvarighet är ritstegens fönster, och de är 0,10 · 0,06 · 0,08 · 0,08 ·
0,04 · 0,07 · 0,09 · 0,04 · 0,04 · 0,03 · 0,03, alltså medvetet **ojämna** eftersom de mäter
banlängd och inte tid. `pathLength="1"` är vad som gör dem jämförbara, och det är den
kontroll R2 ska läsa på kontaktarket. · **Lämnar:** hela worldflight-halvan, `data-sc-lerp`
0,12 och `data-sc-seam` 0,16, eftersom K3 inte har ett enda klipp.

**`references/motion-smoothness.md`** · De två felen bakom samma mening, med fixturmätningen
som visar identisk bildtid och 18 mot 0 trappsteg. · **Tar:** regeln ordagrant (bespoke
rörelse läser `--sc-ps`, cue-opacitet får läsa `--sc-p`); att `--sc-p` är oregistrerad och
därför en sträng, vilket är varför varje `--l`-lokal måste `@property`-registreras; baren vid
4× CPU i båda riktningarna. · **Lämnar:** ingenting. Not: filen dokumenterar att
`scrollcraft.css` rad 98 fortfarande bär en `prefers-reduced-motion`-fråga för
`scroll-behavior`. Den rör ingen akt, motorn redigeras aldrig, och den står kvar; det är
inte ett F-011-brott i K3.

**`references/performance.md`** · Budgeten i tio rader (gate 93), laddningsreglerna,
renderingsreglerna och sex saker som aldrig görs. · **Tar:** § 2:s iframe-rad ordagrant, tre
live-iframes monterade vid load är det tyngsta en marknadsföringssida kan göra mot sig själv;
§ 6:s "an iframe mounted at load" och "a hero image on someone else's CDN", varav den andra
är exakt vad mätningen ovan hittade i två av tre exempelsajter. · **Lämnar:** raden om
scrubbade klipp (K3 har inget), `preconnect` (K3 self-hostar båda snitten), och `srcset`
(K3 har inga `<img>`).

**`references/lift.md`** · Ersätter "kör polish" med sju numrerade pass, reviewerkontraktet i
fem sektioner, och stoppvillkoret. · **Tar:** reviewerkontraktets form (`persistence`,
`fidelity`, `ceiling`, `material_fixes`, `keep`) med **ceiling per låst referens**, vilket är
varför § Vad jag måste slå har en rad per referens och inte ett samlat omdöme; ordningen
broken → states → flow → visual → code. · **Lämnar:** passen 5c, 5e, `bolder`, `quieter` och
`distill`, som alla kräver ett fynd bakom sig och inte får köras spekulativt.

### Registret och cellens eget underlag

**`wiki/projects/_index/design-fingerprints.md`** (alla 36 rader plus båda lästexterna) ·
Se § Fingerprint ovan för utfallet. · **Tar:** de två "used up"-nav-mönstren och de två
"used up"-hero-mönstren som explicita förbud. · **Lämnar:** ingenting; registret är en
begränsning och inte en meny.

**`tests/alunix-r8/PRODUCT.md`** (hel) · Beviskassan och § Absences. · **Tar:** hela den
ordagranna copy-listan, § Operating Context-raden att en visad ram aldrig får transformeras
eller tonas, och Product Principle 2, varje siffra är en siffra vi kan stå för. · **Lämnar:**
ingenting. **Spänning jag noterar och löser här:** Principle 2 skriver "Vi har två priser och
en numrering. Fler tal finns inte, så fler tal skrivs inte", medan målbilden kräver
måttutropen. De två är förenliga och skillnaden är kategorin: priserna och numreringen är
**påståenden om verksamheten**, måtten är **påståenden om sidan**, kontrollerbara av
besökaren mot den egna skärmen. Därför är `SKALA 1:1` en granskningsbar utfästelse och inte
en dekoration, och därför utgår stationen `1440` under 1024 px, eftersom talet då inte längre
är sant om den sidan. Ingen ny siffra tillkommer i något fall.

**`tests/alunix-r8/concepts-K3.md`** (hel, båda sidorna) · Arkitektens målbildsgrind:
auktoritet, troplista, elva skärmar, 36 fingerprintrader, rörelsen, färg och typ, vad
referenserna gör, och rut-testet. · **Tar:** hela grinden som bindande, inklusive de sex
ändringarna mot planen och deras källor. · **Lämnar:** ingenting. **En rättelse jag för
vidare, redan noterad av arkitekten själv:** filen skriver `SEKTION A–A` med tankstreck i
löpande prosa; strängen på sidan är `SEKTION A-A` med bindestreck.

**`tests/alunix-r8/malbilder/K3.md`** (hel) · Planens § 7.5 ordagrant. · **Tar:** allt utom de
två punkter som ändrats med källa. · **Lämnar:** den förväntade referenslistan (ersatt av
`select.py`s rad) och sjuskärmsindelningen (ersatt av elva, eftersom den pinnade akten är
fyra granskningsbara vyer).

**`tests/alunix-r8/runs/K3/assets/ASSETS.md`** (hel, § 0, § A.1 till A.9, § B, § C) ·
SVG-specen: koordinatrum, tre linjebredder, en pilspets, två monoinställningar, hela
elementinventariet med koordinater, ritordningen i fjorton steg, mask-in-mekaniken, den
reducerade planschen, sex asset-lock, papperstexturen och dess fem körbara kontroller. ·
**Tar:** allt, ordagrant. Detta är cellens mest bindande fil efter målbilden. · **Lämnar:**
ingenting. Noterat som R2-arbete: A.8 lämnar koordinaterna för de två reducerade planscherna
till mig.

**`tests/alunix-r8/runs/K3/assets/credits.json`** · Redovisar noll genererat material, noll
krediter, noll jobb, och ett arvat objekt. · **Tar:** raden att `logo-black.svg` används i
**exakt en förekomst**. · **Lämnar:** `logo-white.svg`, som inte ärvs, eftersom sidan inte har
en mörk grund.

**`tests/alunix-r8/runs/K3/NOTES.md`** (arkitektens 26 rader) · Ett beslut per rad med källa. ·
**Tar:** listan över vad jag är skyldig att skriva in under § Byggarens rader, som jag för in
allteftersom mätningarna finns. · **Lämnar:** ingenting; jag tar aldrig bort en rad ovanför.

**`tests/alunix-r8/runs/K3/BRIEF-draft.md`** · Arkitektens poängsättningsunderlag för
`select.py`, uttryckligen inte cellens brief. · **Tar:** förklaringen till avvikelsen i
§ catalogue-select ovan. · **Lämnar:** dess fritext som direktiv; briefen är den här filen.

**`tests/alunix-r8/QUESTIONS.md` § Q6** · Tjänsternas tre underrader är öppna och skrivs av
byggaren, godkänns av Anton. · **Tar:** mandatet att skriva dem, vilket jag gjort. ·
**Lämnar:** varje frestelse att skriva mer än en rad per tjänst.

**`~/.claude/skills/design/SKILL.md`** (hel, laddad som sessionens första verktygsanrop) ·
Kedjans ytterdörr: sex discipliner, hantverksgolvet, verbet, scope, grinden, Step 2b, och
exit-baren. · **Tar:** disciplin 2 (ingen påhittad copy), 3 (låsta tokens, ingen inline-hex
eller `font-family` förbi tokenblocket), 4 (omritat chrome förbjudet) och 6 (inga
reflexkursiver); hantverksgolvets krav på ett namngivet lane före första raden kod. ·
**Lämnar:** bake-offen (briefen låser riktningen, så bara punkt 5 i Step 2b hoppas över),
Tier 3-katalogerna, och de tre demoterade skills som hårdkodar paletter.

### Två avvikelser i den här läsningen, utskrivna i stället för tystade

1. **`aevi-wellness` och `beautiful` har varken `slices/` eller `extract/`.** Deras
   `entry.md` anger `extract: none`, så deras § Motion är märkt **inferred**. Jag har därför
   inte kunnat läsa dem som pixlar utöver folden, och jag använder dem uteslutande som yt-
   och regelkällor, aldrig som rörelsekällor. Det är samma behandling arkitekten valde, och
   jag har verifierat frånvaron på disk snarare än antagit den ur posten.
2. **Anti-referensen lästes som kod, inte som pixlar.** `sites/before-ai-slop.html` har ingen
   sparad skärmbild i repot, och referensgolvet begär filen som text. Jag har därför läst
   alla 155 rader och citerat radnummer i de fem punkterna ovan, vilket är starkare belägg
   för den här filen än en skärmbild: felen sitter i markupen (`.grad-text`, `rounded-full`,
   de påhittade `stat-tiles`), och de går att `grep`-kontrollera i R2 på ett sätt en bild
   inte gör.

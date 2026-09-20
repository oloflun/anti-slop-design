# BRIEF — Alunix r8, cell V3c · Plåt i grunden · kortet vänds

Skelettet är skrivet av arkitekten. Fält märkta `[fylls i R1]` fyller **byggaren** i runda
1. Fält utan den märkningen är låsta och ändras bara med en ny rad i decision ledger som
namnger källan (F-post, TASTE-§, katalogpost, planparagraf).

Målbilden är `tests/alunix-r8/malbilder/V3c.md` (planens § 7.5, ordagrant) och den är
bindande. Målbildsgrinden i sin helhet: `tests/alunix-r8/concepts-V3c.md`.

---

## catalogue-select

```
catalogue-select: oryzo-ai, dope-security, mattis-studio, monologue, planhat
```

Skriven av `python scripts/catalogue/select.py --brief tests/alunix-r8/runs/V3c/BRIEF-draft.md --k 4 --wildcard --explain`
till `.impeccable/design-session.jsonl`. Wildcard = `planhat`. Full utdata och poäng står i
`concepts-V3c.md` § catalogue-select. **Byggaren kör om samma kommando i sin egen session**
(skälet står i R1-prompten) och rapporterar avvikelse; vid avvikelse gäller raden ovan.

### Byggarens egen körning, R1 (2026-09-10)

R1-prompten sa `--brief tests/alunix-r8/runs/V3c/BRIEF.md`. Den körningen **avviker** från den
låsta raden. Hela utdata, ordagrant:

```
$ python scripts/catalogue/select.py --brief tests/alunix-r8/runs/V3c/BRIEF.md --k 4 --wildcard --explain
Brief: tests\alunix-r8\runs\V3c\BRIEF.md  ->  4 poster

    6  aarke                    warm photographic      gallery/catalog
       +6 fritext (cta, hero, photo, product)
    6  aevi-wellness            modern clean           chaptered editorial
       +6 fritext (accent, giant, hairline, hero)
    6  alet                     editorial print        gallery/catalog
       +6 fritext (accent, only, primary, section)
    6  altitude-beverages       editorial print        chaptered editorial
       +6 fritext (dark, display, itself, mono)

Mediastrategi ur posternas egna falt (Photo search) - locken ska inte gissa:
  - aarke: Unsplash first, Pexels second. - "kitchen counter natural light product styled" - "coffee maker steel kitchen morning light" - "marble count
  - aevi-wellness: Unsplash first, Pexels second. - "skincare bottles overlapping flat lay natural light" - "dropper bottle apothecary product close up" - "min
  - alet: Unsplash first, Pexels second. - "editorial product photography warm natural light" - "interior photography natural light desaturated" - "pa
  - altitude-beverages: Unsplash first, Pexels second. - "beverage can product shot gradient background studio" - "condensation can drink close up" - "rosemary garn

catalogue-select skriven: aarke, aevi-wellness, alet, altitude-beverages  ->  C:\Users\Anton L\anti-slop-design\.impeccable\design-session.jsonl
```

**Avvikelsens orsak är inputfilen, inte skriptet.** `BRIEF.md` är skelettet och deklarerar
inga `Register:`/`Grammar:`/`Category:`-fält; utan dem faller varje post till samma
fritextpoäng 6 och skriptet returnerar de fyra alfabetiskt första. Arkitekten körde mot
`BRIEF-draft.md`, som bär fälten, och det står utskrivet i den här filens egen text ovanför
(`--brief tests/alunix-r8/runs/V3c/BRIEF-draft.md`) och i `concepts-V3c.md` § catalogue-select.

Samma kommando som arkitektens, kört i byggarens egen session, ger den låsta raden exakt:

```
$ python scripts/catalogue/select.py --brief tests/alunix-r8/runs/V3c/BRIEF-draft.md --k 4 --wildcard --explain
   14  oryzo-ai                 cinematic dark         continuous world
       +3 register | +3 grammatik | +2 category2 | +6 fritext (accent, black, button, display)
   12  dope-security            cinematic dark         split stage
   12  mattis-studio            cinematic dark         split stage
   12  monologue                cinematic dark         split stage
   12  planhat                  cinematic dark         split stage   | wildcard: utanfor kategorin

catalogue-select skriven: oryzo-ai, dope-security, mattis-studio, monologue, planhat  ->  C:\Users\Anton L\anti-slop-design\.impeccable\design-session.jsonl
```

Sessionsledgerns sista `catalogue-select`-rad i byggarens session bär därmed de fem låsta
sluggarna. **Referenserna byts inte; arkitektens rad gäller**, och den är den enda rad någon
del av den här filen vilar på.

## Design Read (en rad)

Lågexponerad gråskalescen i registret `cinematic dark` och grammatiken `continuous world`:
ett enda visitkort ligger på ett bord under en snedställd lampa och vänds medan besökaren
scrollar, med rubriken stilla utanför kortet i affischgrad.

Kategorin är `portfolio` med `product-focused` som andrakategori, båda låsta av
`BRIEF-draft.md` och bekräftade av `select.py`s egen poängrad (`+3 register | +3 grammatik
| +2 category2` på `oryzo-ai`).

## Dial-deklaration

Arkitektens tre riktvärden behålls oförändrade. Ingen avvikelse.

| Ratt | Siffra | En mening |
|---|---|---|
| **variance** | **4** | Grammatik, nav, värld, palett och typsnitt är oförändrade från V3b och tre dimensioner ändras av ett och samma ingrepp, att plåten blir ett kort med två sidor; en femma skulle ha krävt ett nytt hero-motiv och en trea vore ren polering. |
| **motion** | **7** | En pinnad akt bär hela toppen med en kontinuerlig bespoke-rotation och tre andra ställen kör bespoke paint, men sex av sju skärmar är `flow` med kort stagger, det finns noll scrub-akter och ingen andra `pin`. |
| **density** | **3** | Sju skärmar, ett displayelement per skärm, liggarrader i stället för kort, högst fyra monoetiketter på hela sidan, och två hela sektioner tas bort utan att ersättas av något nytt. |

## Reference lock (7 fält)

```text
Primary reference/direction: tests/alunix-concepts-r5/cells/V3b-chain/index.html — den låsta
  byggnad V3c itererar. reference-lock.md, Tier 0: "Primary = the locked system itself."
Preserve: kontinuerlig svartvit fotografisk grund (k4-cabin-desk.webp) med --sc-canvas-drift
  i tre stopp; R5-världen vänster (Geist, #0b0c0e/#1e5e9c) och R6-världen höger (Public Sans,
  #fdfbf4); rubriken utanför plåten i affischskala; Hyperborea-plåten som bleeder förbi sin
  egen kant; ordscrubben i liggaren; Calyx och Hōrai live i iframe, aldrig transformerade
  efter att de visats.
Borrow only: (1) oryzo-ai — ett fysiskt objekt som vrider sig i ett mörkt tomrum, där
  materialet och kanten under ett snedljus är det som gör rotationen läsbar. (2) mattis-studio
  — konsolkortet, lånat som AVVISNING: V3c:s kort är ett fysiskt kort med två sidor, inte en
  ritad ram med hörnmarkeringar, versionstagg och klocka.
Role rules: #1e5e9c gör exakt en sak och förekommer exakt två gånger på sidan (tesplåtens
  grund inklusive dess drift-mål #123f68, och understrykningen i "Boka ett möte ->"); aldrig
  ram, aldrig knappfyllning, aldrig i liggaren. Geist Mono är enbart register, max fyra
  monoetiketter på hela sidan. Public Sans 300 är enbart display och brödtext. Rollerna
  korsar aldrig. Hårlinje `--frame-line` är plåtens enda kant; radie 0 överallt.
Media strategy: product surface (Calyx, Hōrai och Hyperborea är byråns egna, live eller
  skärmbild) + vendored grayscale still (grunden och hero-plåten, ärvda ur r5, se
  assets/ASSETS.md). Enum, ett värde per plats. INTE photo:unsplash, INTE generated.
Reject: glaskort och konsol-chrome (F-006); ritad webbläsar- eller telefonram (gate 47);
  fabricerad produkt-UI (gate 79); scroll-cue-text (gate 88); tidsstämpel eller
  "2026 · SVERIGE" på kortbaksidan; en andra lede i folden; tre lika tjänstekort;
  logotypvägg, omdömen, betyg, kundantal, år i branschen; en andra accent; skugga.
Token commitments: canvas #0b0c0e; paper #fdfbf4; accent #1e5e9c (ett bruk, två förekomster);
  thesis drift #123f68; hairline --frame-line; radie 0 (skalan {0-3}); pricing: ledger
  (hårlinjerader, display-siffror); services: numbered ledger 01-03, aldrig kort;
  display Public Sans 300 ~130px hero / Geist 700 ~81px kortbaksida; body 16px; register
  Geist Mono 10.5px, tracking .22em.
```

## Decision ledger

En rad per materiellt val. Ett val utan rad skeppas inte.

| Area | Decision | Source | Source rule | Why |
|---|---|---|---|---|
| **Palett** | `#0b0c0e` grund, `#fdfbf4` papper, `#1e5e9c` accent; inget nytt val görs | Målbilden (planens § 7.5) + V3b:s eget lås | TASTE § 4.4, ett papper och en accent som gör en sak | V3c är en iteration; att öppna paletten vore ett nytt bygge |
| **Accentens frekvens** | `#1e5e9c` förekommer exakt två gånger: tesplåtens grund och understrykningen i `Boka ett möte ->` | Katalogposten `dope-security` § What to borrow | "State an accent's frequency as a number, not a feeling" | Ett tal är granskningsbart; "sparsamt" är det inte |
| **Typ** | Geist (röst + kortbaksida), Geist Mono (register), Public Sans 300 (display + brödtext); rollerna korsar aldrig | Målbilden + V3b | TASTE § 4.2, två snitt och rollerna korsar aldrig | Ärvt från en godkänd cell; `brand.md`:s fyra steg körs inte om |
| **Nav** | Tunn topprad med ordmärke och kontakt som scrollar bort; oförändrad från V3b | V3b:s registerrad | `feel-and-fingerprint.md` dimension 2 | Nav är en av de tre dimensioner som INTE ändras, vilket är vad som gör V3c till en iteration |
| **Hero-device** | `section.hero` blir `data-sc-act="pin" data-sc-span="2.2" data-sc-dwell="0.35"`; motorns stage-markup ur `template.html`, aldrig restylade `.sc-*`-klasser | Målbilden | AB06, motorn redigeras aldrig | Vändningen behöver scrollrum som en `flow`-akt inte har |
| **Aktform** | Sju skärmar: en pinnad akt plus sex flow; `panel-open` och `panel-services` tas bort | Målbilden | TASTE § 5 (tre lika kort) och F-006 | Konsolkortets innehåll bor nu på kortbaksidan; tjänstepanelen dubblerade liggaren |
| **Avslut** | Prisliggaren och `kontakt@alunix.se` som en typsatt rad; inget formulär, ingen sticky CTA | r7 § Alunix, fakta | "inget formulär som skickar någonstans" | Rut-testet: kategorins default är ett formulär i botten |
| **Memorable detail** | Kortet vänds: `--flip = smoothstep(0.12, 0.72, --sc-ps)` driver `rotateY` på `.plate-card`, framsidan är fotografisk, baksidan matt svart med ordmärket | `oryzo-ai` (objektet som vrider sig i tomrum), omtolkat till Alunix eget visitkort | `reference-lock.md`: Memorable detail-raden är obligatorisk | Rubriken säger "nutidens visitkort"; sidan låter besökaren vända det |
| **Hero-plåtens stillbild** | Omtagning av hero-plattan utgår -> koreografin ändras så att den bild som finns bär flippen (`assets/ASSETS.md` § 3 väg (d)) · Källa: planens § 10.6 fallback steg 3 · Orsak: Higgsfield 0 credits, free plan, mätt 2026-09-09 av lead | Planens § 10.6 steg 3 | "byt deviceform, aldrig kvaliteten" | F-007-kontrollen visade att ljuspölen inte bär flippen; två rena opacity-tillägg löser två av tre skäl utan att importera ett nytt motiv |
| **Rörelsens datakälla** | Allt som förflyttar sig läser `--sc-ps`; cue-opacitet och drift-ton får läsa `--sc-p` | F-014 punkt 1 | `motion-smoothness.md` § The rule | V3b:s bespoke rörelse läste rå `--sc-p` och stegade (staircase 9 och 16) |
| **Prestanda** | Se § Prestandaplan nedan; varje post i F-013 har ett målvärde | F-013 + `performance.md` § 1 | Gate 93 | V3b sköt 4,9 MB, 19 typsnittsfiler och 17 långa tasks |

### Byggarens rader, R1

En rad per ytterligare materiellt val. Fem av dem är rättelser av något som V3b faktiskt
gör i dag och som bryter mot ett lås i den här filen; de är markerade **rättelse**.

| Area | Decision | Source | Source rule | Why |
|---|---|---|---|---|
| **Accenttalet, rättelse 1** | `.thread-fill` (liggarens självritande tråd) byter från `var(--c-accent)` till `var(--c-ink)` i 2 px mot 1 px `--c-line-on-paper` | Reference lock § Role rules i den här filen | "aldrig i liggaren" | V3b ritar tråden i `#1e5e9c`. Det är accentens tredje förekomst och den ligger precis där låset förbjuder den. Värdekontrast i stället för kulörkontrast håller kvar V3b:s runda 2-fynd att tråden ska läsa som ett ritverktyg, inte som en ram |
| **Accenttalet, rättelse 2** | Fokusringen slutar vara `--c-accent`. Två värden, ett per grund: `#f4f2ef` på den mörka grunden, `#16140f` på papperet, 2 px, offset 2 px | `house-physics.md` "Every muted tone needs a value per ground" + WCAG 1.4.11 | Icke-textkontrast >= 3:1 | Mätt: `#1e5e9c` mot `#0b0c0e` ger **2,93:1** och underkänns; mot `#fdfbf4` ger 6,46:1. `#f4f2ef` mot `#0b0c0e` ger **17,5:1**. Fixen tar samtidigt bort accentens fjärde förekomst |
| **Accenttalet, kvarvarande** | Efter de två raderna ovan förekommer `#1e5e9c` exakt två gånger: tesplåtens grund (med `#123f68` som dess drift-mål, samma roll) och understrykningen i `Boka ett möte →` | `dope-security` § What to borrow | "State an accent's frequency as a number, not a feeling" | Talet är nu granskningsbart mot koden och inte bara mot avsikten. Motorns egen `--sc-accent` räknas inte: inget synligt element läser den |
| **Hero-rubrikens skala, rättelse 3** | `.hero-headline`s tak höjs från `7rem` till `7.5rem`; `.plate-card`s `ALUNIX` behåller `clamp(3.2rem, 9cqw, 7.5rem)` | `concepts-V3c.md` (1), måltalen kvot <= 0,70 och baksida >= 5x brödtext | TASTE § 1 och § 2.4 | Aritmetiken går inte ihop med V3b:s eget tak. Vid 1440 är `9cqw` av sidcontainern 129,6 px men `7rem` = **112 px** binder, så rubriken renderar 112 px och inte de ~130 px `concepts-V3c.md` räknar med. Baksidan blir `9cqw` av plåtens 896 px = **80,6 px**. Kvoten blir **0,72**, över taket 0,70. Att i stället sänka baksidan bryter 5x-golvet (5 x 16 px = 80 px). `7.5rem` = 120 px ger kvot **0,67** och baksidan **5,04x** brödtexten, och kostar 16 px extra höjd i en fold som mäter ~823 px av 900 |
| **Kortets container** | `figure.hero-plate` får eget `container-type: inline-size` | Målbildens `9cqw` på kortbaksidan | `cqw` löser mot närmaste query-container | V3b har `container-type` på `.hero`, inte på plåten. Utan den här raden mäter `9cqw` mot 1440 och baksidans ordmärke renderar 129,6 px i stället för 80,6 px, alltså större än rubriken. `container-type: inline-size` ger `contain: layout style inline-size` och klipper inget, så `perspective` och `preserve-3d` är opåverkade |
| **Låst copy, rättelse 4** | `Webbdesign, design och system. Allt på ett ställe.` flyttas ordagrant till platsen under `VI BYGGER ERT VARUMÄRKE.` och ersätter V3b:s `.giant-sub` | `PRODUCT.md` § Brand Commitments, listan över låst copy | Copy-gate: bevara, skriv aldrig om | Raden bor i dag inuti `section.panel-services`, som målbilden tar bort. Utan den här raden försvinner en av sidans låsta strängar med sektionen. Den text som ersätts (`En sammanhållen process ... med samma team hela vägen.`) är dessutom påhittad och påstår ett team, vilket `PRODUCT.md` § absences förbjuder |
| **Borttagen copy, rättelse 5** | `panel-open`s brödtext (`Vi designar och bygger webbplatser, i nära dialog med verksamheten som ska leva i dem.`) återinförs inte någonstans | Målbilden: "Ingen tidsstämpel, ingen `2026 · SVERIGE`, ingen lede" | En lede i folden, inte två | Den försvinner med `panel-open` och underraden under plåten bär redan leden |
| **Cue-kontraktet i heron** | Heron får ingen `data-sc-cue`. Rubrik, plåt och underrad är stagens ground och är synliga från p = 0 | `scroll/devices.md` § The cue contract, "Ground or greet" | Gate 88 | Kravet är uppfyllt via ground, inte via en greet-cue, och därför behövs ingen cue-text alls |
| **Flow direkt efter pinnen** | `.stagger` får `padding-top: 0` på desktop; seamen mellan hero och första panelen bärs av `.col > * + *`-gapet | `scroll/devices.md` § The premium fade-in, sista stycket | "A flow section directly after a pinned act takes reduced padding" | Pinnens spacer tar redan en hel viewport att scrolla bort; V3b:s `clamp(28px,4.6vw,56px)` ovanpå den lägger en halvtom skärm till som `scroll_verify.py` inte kallar dead scroll men som läsaren ser |
| **Iframe-montering** | `loading="lazy"` plus IntersectionObserver med `rootMargin: 100% 0px` som sätter `src` först vid montering; ingen `transform` och ingen `opacity` på ramen eller någon förfader efter att den visats | `performance.md` § 2 Iframes + `PRODUCT.md` § Operating Context | "An iframe mounted at load" står på Never-listan | Två live-ramar monterade vid load är den enskilt tyngsta posten i F-013:s 4,9 MB. Regeln att ramen aldrig transformeras efteråt är M1:s egen lärdom och står i `PRODUCT.md` |
| **`content-visibility`** | `.price` får `content-visibility: auto; contain-intrinsic-size: 1px 800px`; `.horai-wrap` får `1px 620px` | `performance.md` § 2 | "the cheapest single win" | Utan `contain-intrinsic-size` byter sidan höjd när blocket målas och CLS-taket 0,05 går inte att hålla |
| **`--flip` och frysningen** | `--flip` skrivs på `.plate-card` från sidans egen rAF-loop som `smoothstep(0.12, 0.72, ps)` där `ps` är `--sc-ps`; `window.__scFreezeMotion` blir en **boolean**, inte V3b:s funktionspar | F-014 punkt 1 + `motion-smoothness.md` § The rule | "Bespoke motion reads `--sc-ps`, never raw `--sc-p`" | V3b exponerar `__scFreezeMotion` som en funktion. `sc-smooth.js` läser flaggan som ett värde, så `?preview=`-lägena spårar inte det råa värdet förrän API:t byts |
| **Typsnittsfilerna** | `[needs asset: Geist 700, Geist Mono 400 och Public Sans 300 som self-hostade `.woff2` under `runs/V3c/assets/fonts/`, plus en metrikmatchad fallback-`@font-face` per familj]` | `performance.md` § 2 Fonts + prestandaplanens rad om 19 typsnittsfiler | F-009: arkitekten specificerar, lead vendorar | `ASSETS.md` § 1 listar tio filer och ingen av dem är ett typsnitt. Prestandaplanen kräver att Google Fonts-länken tas bort och ersätts av exakt tre `.woff2`. Byggaren varken hämtar eller genererar material, så posten skrivs här och i `NOTES.md` § R1 och rundan går vidare |
| **Kolumnvikten** | Priset ligger kvar i vänsterspalten enligt målbilden; ingen flytt görs i R2 | Målbilden, sista stycket i "Under heron" | "Arkitekten läser kolumnvikten som pixlar" | Domen är uttryckligen arkitektens och den fattas på pixlar efter R2, inte på en gissning i R1 |
| **Pilen i `Boka ett möte →`** | Skrivs med Unicode-pilen `→` enligt målbilden; strängen går genom copy-gaten i R3 tillsammans med gate 97 | Målbilden § "Kortet", ordagrant | Gate 97 (pilsuffix på länk eller knapp) | Två saker krockar och båda redovisas i stället för att tystas: målbilden föreskriver strängen, gate 97 förbjuder formen. Skelettets § Copy-plan skriver dessutom `->` medan målbilden skriver `→`. Se § Copy-plan för den öppna frågan |

### Byggarens rader, R2

Varje rad är en avvikelse från målbilden eller från V3b som R2 faktiskt byggde, och varje rad
har ett mätvärde bakom sig. Full mätning i `NOTES.md` § R2.

| Area | Decision | Source | Source rule | Why |
|---|---|---|---|---|
| **Plåtens bakgrund** | `figure.hero-plate` får ingen `background`. V3b:s `#08090a` tas bort | Egen pixelläsning av vändningen i R2 | F-007: signaturakten jämförs mot målbilden bild för bild | Med bakgrunden låg en statisk svart rektangel kvar i plåtens fulla bredd medan kortet vändes inuti den. Det läser som ett kort i ett fönster, inte som ett kort som vänds, och det är precis `mattis-studio`-avvisningen igen |
| **Kortets tjocklek** | `.plate-edge` hängs i den ledande kanten (`right:0`, `transform-origin:100% 50%`), inte i mitten, och opaciteten är parabeln upphöjd till tre | `ASSETS.md` § 3 väg (d) 2 | "byt deviceform, aldrig kvaliteten" | Mitt på kortet läste tjockleken som ett veck genom en plan yta. Ett kort är tjockt vid kanten. Vid `?preview=mid` syns nu en hårlinje och ingenting annat, vilket är `mattis-studio`-ribbans mätpunkt |
| **Ljuspölens mekanism** | Vandringen körs på `transform: translate3d` på en bild som är 112 % av ytans höjd, inte på `object-position` | `performance.md` § 3 | "Animate transform, opacity and filter. Everything else costs layout or paint per frame" | Målbilden låser att pölen vandrar på `--sc-ps`, inte vilken egenskap som bär den. `object-position` ritade om en 896x504 bild per bildruta: p95 föll 50,0 -> 33,4 ms av den ändringen ensam. Samma vandring, samma motiv, på kompositorn |
| **Grundens containment** | `.ground` får `contain: strict` | Egen attributionsmätning, sju varianter, `NOTES.md` § R2 | Gate 93 | Den enda av sju kandidater som tog bort kostnaden: p95 33,4 -> 16,8 ms. Filtret, blandningen och antalet akter var alla oskyldiga, och `will-change` fördubblade antalet tappade bildrutor |
| **Grundens ton** | Tonen är ett eget bakgrundslager med `background-blend-mode: color` i stället för V3b:s `::after` med `mix-blend-mode: color`; `transition: background 1.1s` tas bort | `performance.md` § 3 | Blur och blend kostar i proportion till yta | `mix-blend-mode` läser sidans backdrop; `background-blend-mode` blandar bara elementets egna lager. Transitionen målade om ett helskärmslager i 1,1 s efter varje drift-steg utan att synas, ovanpå en interpolation motorn redan gör |
| **Toppraden ur flödet** | `header.topline` är `position:absolute` | Egen mätning av folden vid 1440x900 | Folden ska rymma rubrik, kort och underrad | I flödet börjar den pinnade stagen 57 px ned och folden tappar sina understa 57 px. Nav-beteendet är oförändrat: den scrollar bort med sektionen |
| **Stagens märkning** | Stagen märks med attributet `data-sc-stage`, aldrig med klassen `.sc-stage` | `scroll/NOTE.md` + AB06 | Motorn redigeras aldrig, `.sc-*` restylas aldrig | Motorn sätter klassen vid mount. Utan JS finns då ingen `position:sticky` och sidan faller tillbaka till ett vanligt staplat hero i stället för ett stickande tomrum |
| **`--flip` i CSS, inte i JS** | Smoothstep räknas i `clamp()` och `calc()` ur `--sc-ps`; sidans JS rör aldrig `--flip` utom i `?preview=` | F-014 punkt 1 + F-013 | "17 långa tasks under scroll", tak 0 | `--sc-ps` är registrerad som `<number>` av shimen, så CSS kan räkna på den. Vändningen kostar noll JS-bildrutor |
| **Sidans egen loop** | `is-turning` och `inert` styrs av progress räknad ur `scrollY`, inte av `getComputedStyle` per bildruta | `performance.md` § 3 | "No layout reads in a scroll handler" | Shimen läser redan `getComputedStyle` en gång per akt och bildruta. De två gränserna tål skillnaden mellan rått och lerpat: ansiktsbytet sker 13 px scroll senare, vilket bara rör `inert` |
| **Bortvänd yta är `inert`** | Den yta som inte syns hålls `inert` och `aria-hidden` | `a11y-audit`, fokusordning | Ingenting fokuserbart utanför skärmen | Baksidans länk finns i DOM:en från början. En fokusbar länk som inte syns är ett fel, och utan JS är framsidan uppe och baksidan inert |
| **Mobilens kortbudget** | Under 640 px härleds kortets bredd ur 48svh och stagen centrerar sitt innehåll | Egen mätning på 320x568 och 390x844 | `responsive.md` § Mobile | En 4:5-ruta i full spaltbredd spränger en 568 px hög skärm. Toppställt innehåll lämnade 284 px död yta under underraden på 390x844 |
| **Platshållarnas höjd** | Båda spalterna har ett `flex:1`-block, Calyx till vänster och Hōrai till höger | Egen `scroll_verify`-körning | `blankBands` | Utan det slutade höger spalt 651 px före vänster och proben rapporterade hålet, korrekt. Höjderna är R3-uppskattningar, inte designbeslut |
| **Gate 93, filtret** | `filter` på ett helskärmselement behålls, och avvikelsen skrivs ut i stället för att döljas | Gate 93 + `ASSETS.md` § 1 | "filter på > 50 % av viewporten: 0" | Grunden måste vara gråskala och byggaren vendorar inget (F-009). Mätningen visar att filtret inte kostar något efter `contain: strict`, så det är en gate-avvikelse utan mätbar kostnad. `[needs asset: förgråskalad k4-cabin-desk.webp]` tar bort den helt |
| **Bildernas sökvägar** | Hero-bilden och grunden refereras på `/tests/alunix-concepts-r3/build/assets/`, samma origin | `ASSETS.md` § 1, som inte är vendorad | `SKILL.md` Step 5b | Regeln gäller ett annat företags CDN, inte det egna repot. Alla fyra filer svarar 200 över `serve.py`. Sökvägarna byts till `assets/` i R3 när lead har vendorat |
| **Två `?preview=`-lägen skjuts** | `?preview=ledger` och `?preview=bleed` byggs i R3 | BRIEF.md § `?preview=`-plan, egna rader från R1 | Ett läge utan mål är ett läge utan mening | Deras mål, ordscrubben och Hyperborea-bleeden, är R3-platshållare i den här rundan. De tre obligatoriska lägena finns, är byggda och är skärmbildade |

### Byggarens rader, R4

En rad per materiellt val i fixrundan efter kvartetten. Full mätning i `NOTES.md` § R4.

| Area | Decision | Source | Source rule | Why |
|---|---|---|---|---|
| **Kortbaksidans kicker, prövad och återställd (plan 006)** | `Webbyrå i Sverige` provades i en tidigare runda, dömdes tillbaka till målbildens `Digital byrå`, oförändrad Geist Mono 10,5 px / tracking .22em | Plan `006-kickern-tillbaka-till-malbilden.md`; arkitektens och kritikerns dom | Målbilden är kontraktet; ett byte utan ledgerrad skeppas inte | Tre skäl, alla arkitektens: (1) målbilden är kontraktet och bytet saknade en rad här; (2) kortets tes är att sajten är nutidens visitkort, och ett visitkort bär yrkesbeteckningen, inte sökfrasen; (3) versal mono i formen substantiv + ort är kategorins SEO-default, vilket rut-testet i `concepts-V3c.md` punkt 8 håller utanför |

### Arkitektens rader, fas A (2026-09-15)

Skrivna av arkitekten efter den visuella genomgången (`HELHET.md`). Varje rad är ett beslut
för r9 med källa; byggaren utför dem via planerna 010 och framåt, aldrig på egen hand.

| Area | Decision | Source | Source rule | Why |
|---|---|---|---|---|
| **Antons namngivna referenser** | `insign`, `highwaymedia` och `hoy` står i låset som användarnamngivna referenser för helheten (struktur, balans, processbeskrivning), utan att ersätta primärkällan V3b eller de fem select-sluggarna | Antons instruktion 2026-09-15; `reference-lock.md` § Sources ("User-supplied URL … valid at any tier as a borrowed-detail source") | Borrowed detail, aldrig primär | `select.py --k 4 --wildcard` rankar dem inte (register `modern clean`, grammatik `chaptered editorial` mot briefens `cinematic dark` / `continuous world`), inte heller vid `--k 8`. De lånas som princip: Highways fasordning, Insigns testadress och CMS, Hoys helbredds grundbyten och WCAG-princip |
| **Processakten** | Ny full-bredd `#process` på `var(--bg)` efter `.stagger`, före `footer.close`, `data-sc-act="flow"`, ett sticky ark i sju tillstånd; plan 010 | Antons beställning; planens § Designbeslut | Heron är sidans enda motor-`pin`; arket är page-authored `position: sticky`, ingen spacer, ingen `.sc-stage` | K3:s ritning lånad som form, aldrig som sida; ger H-02 och H-06 |
| **Kortvändningens tempo** | `data-sc-span` 4,8 → **3,4**, `data-sc-dwell` 0,35 → 0,2, smoothstep-fönstret 0,12 till 0,72 → **0,10 till 0,78** (plan 011, Q25) | `HELHET.md` § 2, ramsekvensen `shots/fasA/v3c-flip/` och `scroll_verify` (1 273 px dead scroll vid 4,8) | Peaken får mest scrollrum men aldrig dead scroll | 2,2 = 648 px vändning (för fort), 4,8 = 2 052 px + 1 273 px stillastående; 3,4 med vidgat fönster = 1 469 px + 655 px |
| **Accentens tredje roll** | `#1e5e9c` får förekomma en tredje gång: de sanna måtten i processarket, ett blått moment per skärm, alltid ett sant tal (T-2, Q26) | Antons lättnad 2026-09-15; K3:s regel (beautiful-regeln via `concepts-K3.md` § (6)) | Frekvensen är fortfarande ett tal: tre roller, utskrivna | Nekar Anton: `var(--ink)`, inget annat ändras |
| **Monobudgeten** | fyra etikettfamiljer → fem: stegindexen 01 till 07 i `.ledger-num` (T-7) | `HELHET.md` § 4 | Register, aldrig röst | Liggarens 01 till 03 och arkets 01 till 07 är samma register |
| **Prisblockets material** | ny token `--c-graphite: oklch(0.27 0.012 250)` för `.price` i stället för `--invert` (T-3, Q27) | `HELHET.md` § 2 (`v3c-1440--s06.png`: blocket läser som ett hål) | TASTE § 4.5: material, inte grå sektion | `#0c0b08` mot grunden `#0b0c0e` är ingen växling |
| **Kortbaksidans högra halva** | ordmärkets A-glyf som hårlinjekontur, 60 % av korthöjden, högerställd, `--frame-line` (T-4) | R2/R3:s öppna fråga, `v3c-preview/v3c-1440-back--fold.png` | Ritad form, inte innehåll (gate 47/79) | Samma objekt, två sidor: fylld fram, kontur bak |
| **Jätterubriken** | `.giant` tak 4,8rem → 6rem (T-5) | TASTE § 2.4, Hoys avdelare 100 till 132 px | Display ≥ 6 gånger body | 80 px är golvet, inte ett beslut |
| **Avslutet** | `.close` min-height 62 svh, mailto upp till 6rem, en hårlinje som dras in på `--sc-ps` (T-8, plan 007 + H-25) | `HELHET.md` § 2 | Sista akten håller och rör sig en gång | Sista skärmen saknar i dag rörelse |
| **Mobilordningen** | vid ≤ 900 px: tes → Calyx → jätterubrik/liggare → Hōrai → pris → process → avslut (Q28) | `v3c-390--s02..s06.png` | Berättelsens ordning s4 → s7 håller på alla bredder | I dag kommer Hōrai och liggaren före tesen |

### Byggarens rader, R5

Utfört: plan 010 (`#process`) och plan 011 (kortvändningens tempo) i sin helhet. Plan
010:s övriga Fas A-rader (T-3 prisblockets material, T-4 kortbaksidans A-glyf, T-5
jätterubriken, T-8 avslutets hårlinje, mobilordningen Q28) rörs inte: R5-uppdraget
namngav bara planerna 010 och 011, och de raderna hör till en senare runda.

| Area | Decision | Source | Source rule | Why |
|---|---|---|---|---|
| **Processarkets titelblock, avvikelse** | `#p-title`/`#p-rev` flyttade från plan 010:s y 447 till y 439 | Egen geometri­kontroll före skärmbild | Arkets viewBox är bara 495 hög | En 3-radig 60×18-stapel (54 hög) som börjar vid y 447 slutar vid 501, 6 units förbi viewBoxens 495. y 439 ger samma tre-rads-konvention (ISO 7200, som K3:s eget titelblock) med 2 units marginal kvar |
| **Ordmärkets A-glyf, avvikelse** | `#p-mark` byggd som `<use href="#alunix-mark-path">` (återanvänder den befintliga wordmark-pathen på kortbaksidan) med en opacitetston, inte dash-draw | Egen SVG-kontroll | `pathLength` är odefinierat på `<use>` (SVG-specen) | Att duplicera hela path-strängen (ett par kB) som en andra literal `<path>` var alternativet; en opacitetston, samma enhet som utropen, är den ärliga förenklingen för ett 36-units hörnmärke som inte är ett av arkets sanna mått |
| **`motion_probe.py`:s riktningsflagga** | Ingen finns; "båda riktningarna" i planernas Verification kunde inte köras separat, bara `reversals`-fältet (0 i varje körning) fungerar som ersättare | `motion_probe.py --help`, bekräftat R4 och igen R5 | — | Samma begränsning som redan loggad i R4:s Plan 005; upprepas här för fullständighet |

### Byggarens rader, R6

Sex fixplaner (018-023) efter R5-granskningens kvartett + codex-review. Fullständig
verdikt per plan i `NOTES.md § R6`.

| Area | Decision | Source | Source rule | Why |
|---|---|---|---|---|
| **Ramarnas viloläge** | `.frame-wrap.is-asleep{content-visibility:hidden}` styrd av en beständig (aldrig `unobserve`:ad) IntersectionObserver vid `rootMargin:'40% 0px'`; reveal flyttad från `<figure>` till wrappern | perf-rapportens fynd 1-2 | Plan 018 | Ramarna bar 66 % av processaktens tasktid; `content-visibility` sover undan layout/paint/style utan att röra `transform`/`opacity` på en visad ram (PRODUCT.md § absences) |
| **Processakten, formbeslut** | Sju steg som stående prosa i flödet (aldrig korsfading), arket sticky bredvid (>=1280) eller ovanför (<=1279) texten, banfönster ankrade i varje `<li>`:s uppmätta läge (`measureAct`, fjorton `--s1..--e7`-tal på `#process`) i stället för en tabell | Anton 2026-09-16; a11y 3/5/8, Astra 3/4/7/8, critic 1/2/4/5, heuristik 1-3/5-7, perf 3/4/7 | Plan 019 | Löser PageDown (var 4/7, nu 7/7), steg 07 utanför sticky-hållet, tom 504px ankomstskärm och 390-planschen samtidigt, genom att göra höjden textens i stället för ett hållfönster |
| **"Hur vi tänker"** | Eget avsnitt på papper efter akten: tre stycken (Design/Utveckling/System) som hairline-liggare utan nummer | PROCESS-UNDERLAG.md § 5 | Plan 019 steg 9-10 | Ledgerns tre underrader (Step 10) behövde en egen yta i stället för att packas in i processaktens sjunde steg |
| **Arkets geometri, rättelse** | `7 rem`-linjen flyttad till öppningens sanna kant (x 195,6→264, var `226→270`); dimensionslinjen visar nu det avstånd texten faktiskt påstår | Astra 5, critic 3/6 | Plan 020 A | Talet var korrekt som text men fel som ritad linje: linjen mätte 4,5 rem samtidigt som brödtexten sa 7 |
| **Ordmärkets A-glyf** | Byggd som egen `<path pathLength="1">` med `d` kopierad ur kortbaksidans path, dash-draw i stället för opacitetston | Astra 6, critic 01 | Plan 020 C | `<use>` saknar `pathLength`-stöd (samma fynd som R5:s Plan 010-avvikelse); en egen path gör glyfen till en riktig bana i stället för en maskerad kopia |
| **Accenttalet, R6** | `.card-cta`s understrykning byter från `var(--c-accent)` till `currentColor`; accenten lämnar kortet helt. Efter 020 (arkets sanna mått i accent) och 021 står accenten kvar i exakt två roller: tesplåtens grund (inkl. driftmålet `#123f68`) och arkets sanna mått (320/768/1440/7rem/96px/16:9) | a11y fix 1-2 | Plan 021 steg 4 | `.card-cta`s understrykning mätte 2,92:1 mot kortets grund, under 3:1-golvet; `currentColor` (17,5:1) löser kontrasten och håller kvar talet som en räknebar rad i stället för en känsla |
| **Bildtexternas grund** | `.frame-cap` flyttas till papperets valör (`background:var(--bg);color:var(--ink)`) i en egen rad under ramen, i stället för vit text ovanpå det fotografiska underlaget | a11y fix 1 | Plan 021 steg 1 | Mätt värsta lapp 3,06:1 på den fotografiska grunden; 17,9:1 på papper oavsett grunddrift (house physics: ett värde per grund) |
| **Kortets fokusparkering** | `figure.hero-plate` får `tabindex="-1"`; `setFace()` flyttar fokus dit innan den gömda sidan blir `inert`, i stället för att låta webbläsaren nollställa till `body` | a11y fix 4 | Plan 022 steg 1-2 | Chromium tappar fokus till `body` när en förälder till `document.activeElement` blir `inert`; en programmatisk parkeringsplats håller tabbordningen intakt |
| **Baksidans strängar i tillgänglighetsträdet** | `.sr-only`-kopia av kortets fyra strängar läggs direkt efter `<figure>`, eftersom `inert` gömmer subträdet för AT i Chromium oavsett `aria-hidden` | a11y fix 7 | Plan 022 steg 3 | En skärmläsare som läser linjärt vid p=0 hörde annars aldrig namnet, tjänsterna eller kontaktvägen |
| **Liggartrådens fönster, rättelse** | `--scrub` ankrat om till `0,364 / 0,315` (uppmätt) i stället för planens citerade `0,62 / 0,33`; egen bisektionssökning gav ps 0,364 vid liggarens överkant +600px (scrollY 2748) och ps 0,679 vid +90px (scrollY 3258) | perf fix 5 | Plan 023 steg 2 | Planens egen ommätningsregel (avviker mer än 0,05: justera) slog in — 0,62/0,95 avvek med över 0,25 från det uppmätta R6-läget, sannolikt en R5-era mätning mot en annan sektionshöjd |

### Fynd, dokumenterade men inte lösta i R6 (arkitektens att döma)

| Fynd | Var upptäckt | Detalj |
|---|---|---|
| **`.process-grid`s andra kolumn renderar 825,6px, inte 880px, vid 1440** | Egen mätning under plan 020:s verifiering | `minmax(0,880px)` + `padding-inline:var(--rail-x)` (86,4px) + `column-gap` (57,6px) lämnar 825,6px kvar av en 1440px viewport efter `--rail-x`-marginalerna; "7 rem" och "96 px" är BÅDA de sant ritade linjerna (plan 020 A rättade var linjen pekar), men rendrerar ~93,8 % av sitt nominella värde eftersom hela arket skalas ned för att få plats. "16:9" är en ren kvot och påverkas inte. Ingen klippning (högerkantsmätning ren vid 1024/1180/1280/1366/1440); flaggas, inte fixat — grid-spannet kommer direkt ur plan 019 steg 2, som byggaren följde exakt |
| **Sidvikt 441 781 B, över README:s 425 kB-tak** | `perf_probe.py` i R6-grinden | ~17 kB över; ingen enskild ny tillgång i R6 (arkets nya rader är SVG/CSS, ingen bild), sannolikt `#p-glyph`s ~2kB path-sträng (020) plus `#process`s nya CSS-block (019) tillsammans |

### Arkitektens rader, helhetsloopen runda 1 (2026-09-17)

| Area | Decision | Source | Source rule | Why |
|---|---|---|---|---|
| **Dwell-arithmetiken** | HELHET § 2:s tabell (svans 655, vändning 1 469) ersätts av motorns kurva: vändning 1 602 px, svans 393 px vid 900 vh; H-17 håller, H-18 bockas inom tolerans (2 px) | `scroll/scrollcraft.js:159` (`dwell` är en mittremapp), Astra loop 1 | Tal ur källan, aldrig ur antagandet | Fas A antog dwell som slut-hållning |
| **Bleeden mot rubriken** | `.stagger` gap 3,2vw → 4vw (58 px), bleedens tak 34 → 33 % (100 px överhäng, 5 px före `VI BYGGER`); plan 017 D | `shots/loop-1/diag2` (103 px överhäng, plåten 9 px in i textkanten) | H-20 ≥ 96 px och ingen kollision, båda | 017 B lägger rubriken i plåtens höjdspann |
| **Seams 160 px** | bandets luft mot pinnen och mellan panelerna 160 px (var 96/120 i plan 017) | HELHET H-05 (a), Astra loop 1 | Planen får inte ligga under sitt eget golv | 16vh = 144 px vid 900 |
| **Avslutet 100 svh** | `.close` min-height 62 → 100 svh, hårlinjen 0 till 0,46, mailto `min-height:44px` | `slices-1440/…--s10.png` (principerna i sista viewporten), `diag2` (mailto 30 px vid 390), Astra loop 1 | H-12 "ensamt", gate 62 | 62 svh lämnade 38 svh av föregående akt |
| **Stegens ankare** | `--s1` i arkets ankomst (95 %), `--sN` vid 65 % (1440) / 95 % (390), `--eN` vid li:s mitt (1440) / li:s överkant vid arkets underkant (390); hysteres 0,03 på gruppernas `data-on`; arket ≤ `(100svh − 200px)·320/360` vid ≤ 1279 | `diag.json stepVars` (överlapp 0,02 vid 1440, fel tecken 0,084 vid 390), previews, Astra loop 1 | H-30 (preview N = steg N), H-28, H-35 | R6:s "teckenrättelse" gjorde previewn konsekvent med en felvänd formel |
| **Railmarginalen** | `--panel-pad-y` deklareras lokalt på `.principles`; `.process > .kicker-sans` får `padding-inline:var(--rail-x)` | `diag.json principlesPadding 0px`, leadens R6-fynd | En `var()` mot en odefinierad egenskap ogiltigförklarar hela deklarationen | Kickers vid x 0 på båda papperssektionerna |
| **H-10** | uppfyllt i R6-läget (95,5 % / 86,4 %); plan 024 (kanten 2 → 4 px) skriven men utanför R7 | `diag.json flips` | Golvet mäts, inte läses | Fas A:s "linje i tomrum" var kortets tjocklek |
| **Bandets komposition** | Q30 till Anton; ingen omkomposition i R7 | Astra loop 1 (H-02/H-03), BRIEF § STORY | Målbilden ändras bara av Anton | Två spalter är målbildens s4 till s6 |
| **Ramarnas montering** | `mountFrame` idempotent, `__visible`/`__pending` per ram (plan 026) | Astra loop 1 fix 7, verifierad mot rad 1547-1575 | En navigering per ram; sömn även för en ram som lämnade före luckan | `f.src = null` navigerar till `/null` |

### Arkitektens rader, helhetsloopen runda 2 (2026-09-17)

| Area | Decision | Source | Source rule | Why |
|---|---|---|---|---|
| **Ramarnas observer** | observern observerar `.frame-wrap`, inte ramen (plan 027) | `shots/loop-2/diag/diag3.json A_cv_hidden_blind` (IFRAME inter false h 0, DIV inter true h 855), `diagA2.json` (12/12 sovande stopp → 0/12) | Ett element i ett `content-visibility:hidden`-subträd har ingen box; en observer på det vaknar aldrig | Leadens R7-fynd 1: båda sajterna tomma plattor |
| **Bildtiden, attribution** | stilomräkning är 65 till 76 % av tasktiden; en `--sc-ps`-skrivning kostar 1,8/2,1/2,2 ms (hero/jätten/arket, cpu 1) i subträdsomräkning; shimen tvingar 1,7 till 4,6 omräkningar per frame; `:root --sc-canvas` (motorn) 9 ms per ändring | `shots/loop-2/profile/profile*.json`, scratch `synth*.py` | Mät före ändring (F-013 regel 2) | Loop 1 lämnade bildtiden till en profileringsrunda |
| **Shimen** | läser `--sc-p` ur inline-stilen, batchar skrivningarna, registrerar `--sc-p` `inherits:false` (plan 028 A, B) | `profile4.json`: cpu 1 hero p95 35,5 → 18,8 ms, omräkningar/frame 1,7 till 4,6 → 1,2 till 1,4; `synth3`: 1,84 → 0,27 ms per motorskrivning | Shimen är sidans egen fil; motorn rörs inte; ingen regel läser `var(--sc-p)` (grep) | Forced synchronous recalc per akt och frame |
| **Ordscrubben** | fronten som gradient per block (`background-clip:text`), sex element i stället för 60 spann (plan 028 C) | `synth3`: 2,10 → 0,84 ms per skrivning på jätten; samma valörer 62 → 100 % bläck | TASTE § 4.8, F-014: samma `--scrub`, samma läsning | Den dyraste konsumenten som kan bli billig utan att ögat ser skillnad |
| **Grunddriften** | tonlagret 62 → 40 % (plan 029) | `diag3.json B_summary`: 40 % ger delta 13 (H-19 ≥ 12), chroma 19; 62 % färgade rännan (58,86,111) mot gråskalans (80,80,80) | En accent, två roller; grunden är ett gråskalefoto i kallt ljus, inte ett blått | Leadens R7-fynd 2 |
| **Jätterubriken** | 88 px vid −0,04em, `hyphens:manual` (plan 030); H-07 omskriven till "≥ 88 px, ordet helt"; Q31 | `diag3.json C_giant`, `synth3` (1 rect vid 901/1024/1280/1440) | Låst copy delas aldrig; 96 px kräver 606 px spalt | Leadens R7-fynd 3 |
| **Stegens ankare** | `--s1` ur `.process-grid`:s överkant, inte ur sticky-rect; prosan utan `data-sc-in` (plan 034) | `verify_astra2.py`: `--s1` 0,4847 > `--e1` 0,2292 i preview-05; `li 01` opacity 0 / translateY(14px) vid 390 life-01 | En mätning får inte bero på scrollläget; texten är alltid synlig (019) | Astra loop 2 fix 1, 3 |
| **Ramarnas reveal** | sidans egen latch `--rv` ur shimens lerpade `cur`, aldrig baklänges (plan 031) | `scrollcraft.js` 947-957 (rått `a.p`, båda riktningarna) | House physics: en reveal som gömmer sig igen är en defekt; gate 94 | Astra loop 1 fix 8 (uppskjuten hit) |
| **Priset** | liggarens fyra hårlinjer dras på `--sc-ps` (plan 033) | H-25; `process-1440/v3c-1440-life-00.png` | Varje skärm bär en scroll-läst förändring; samma språk som avslutets linje | Priset var sista stilla skärmen |
| **Folden 390 och mobilseams** | `.hero-stage` bottenställd med 10 svh; `.stagger` gap 96 till 120 px under 900 (plan 032) | `preview-390-front.png` (137 px = 16,3 %), `geom390` (84 px slitsar) | H-13 ≤ 12 %, H-05 ≥ 96 px | Astra loop 2 bild 18/20 |
| **H-01** | 12,09 vh vid 1440 lämnas (0,09 över raden, inom 8 till 14) | `geom1440 docH 10880` | Talet står som det är | Q30 skulle lägga ~2 vh till |

### Byggarens rader, R7

Åtta fixplaner (025, 017, 012, 013, 014, 015, 016, 026) utförda i README-ordning.
Fullständig verdikt per plan i `NOTES.md § R7`. Raderna nedan är exekveringsfynd som
arkitektens rader ovan inte (och inte kunde) förutse — uppmätta under bygget, inte
planerade i förväg.

| Area | Decision | Source | Source rule | Why |
|---|---|---|---|---|
| **Arkets golv vid låga viewports, rättelse** | Plan 025 D:s formel `(100svh - 200px) * 320/360` rättad till `(100svh - 224px) * 320/360` | Egen mätning: `.process-stick` height vid 1024x640/900x600/720x450 | Målet var uttryckligen "≥200px text kvar under arket" | Planens formel räknade inte med sin egen `padding-block:12px` (24px); uppmätt lämnade den bara 176px, inte 200, vid alla tre viewports (samma 24px-underskott varje gång) |
| **Jätterubrikens radbrytning** | `.giant` får `hyphens:auto` (lang="sv" finns på `<html>`) | Egen mätning: "VARUMÄRKE." ensamt ord mäter 601px, bredare än den faktiska 555px textkolumnen | Plan 014:s eget mål "högst 3 rader" | Vid 96px font-size i den nu uppmätta ~555px-spalten (inte planens antagna ~640px) bröt `overflow-wrap:anywhere` ordet mitt itu ("VARUMÄRK/E."), 4 rader; `hyphens:auto` ger en riktig stavelsedelning ("VARU-MÄRKE"), 3 rader |
| **Kortbaksidans glyf vid 320px, andra fallback-steget** | `.card-glyph`s mobila `height` sänkt vidare 28% → 24% | Egen mätning: överlapp mot `.card-services` 308 kvadrat-px vid 320x568 efter planens egen första fallback (34%→28%) | Plan 016 steg 4:s eget "Är den inte 0: sänk ... och mät om" | 28% räckte inte vid den kortaste testade höjden (kortet är bara 272,6px högt vid 320x568); en andra sänkning tar bort den sista 5,6px-flisan |
| **Avslutets fönster, ingen justering behövdes** | `--sc-ps` max på `footer.close` uppmätt 0,5002 vid både 1440 och 390 | Egen mätning, plan 015 steg 4 | ≥ 0,46 (planens eget villkor för att INTE justera nämnaren) | Bekräftar planens egen formel (vh/(vh+vh)=0,50) exakt; ingen av de justeringsstegen plan 015 skrev in behövde köras |
| **Ramarnas idempotens, reproduktion** | Plan 026:s egna repro-steg (dubbelscroll in/ut/in, sömnkontroll) körda: exakt en `calyx.html`-post, 0 `/null`-träffar, `is-asleep=true` med bevarad `src` efter att ramen lämnat 40%-zonen | Egen Playwright-reproduktion | Plan 026 steg 2-3 | Bekräftar båda felen (dubbelmontering, vaken-utanför-skärmen) stängda utan att skriva om reproduktionsmetodiken |

### Fynd, dokumenterade men inte lösta i R7 (arkitektens att döma)

| Fynd | Var upptäckt | Detalj |
|---|---|---|
| **`--sc-ps` max_step vid uppåtscroll överskrider 3%-baren, även vid cpu 1 (otryckt)** | `motion_probe`-matrisen i R7-grinden | Nedåt (cpu1, 100:60): hero max_step 1,41/2,12%, håller. Uppåt (cpu1, 100:60, samma spår): 4,54/8,69%, över baren, trots att ingen av de åtta R7-planerna rör heron-pinnens mekanik, motorn eller `sc-smooth.js`. Sannolikt en egenskap hos lerp-smoothingens respons på snabb riktningsomkastning, inte en R7-regression — flaggas för arkitekten snarare än gissad bort |
| **Sidvikt 452 879 B, fortsatt över README:s 425 kB-tak (R6: 441 781 B)** | `perf_probe.py` i R7-grinden | +11 kB sedan R6: `#alunix-mark-path`s ~2kB `d`-sträng duplicerad in i kortbaksidans nya `<svg class="card-glyph">` (016), plus ny CSS (`.close-rule`, `.card-glyph`, `--c-graphite`, arkets nya ankarlogik) |

### Byggarens rader, R8

Åtta fixplaner (027, 028, 034, 031, 033, 029, 030, 032) utförda i README-ordning.
Fullständig verdikt per plan i `NOTES.md § R8`. Raderna nedan är exekveringsfynd som
arkitektens rader ovan inte (och inte kunde) förutse.

| Area | Decision | Source | Source rule | Why |
|---|---|---|---|---|
| **`window.__scSmooth.acts`, rättelse i sc-smooth.js** | Egenskapen `acts: acts` bytt till en getter `get acts(){ return acts; }` | Egen mätning: plan 031:s revealkod läste `window.__scSmooth.acts` och fick alltid en tom array, `--rv` stod fast vid 0 för alltid | Plan 031:s eget kontrakt kräver att `.acts` speglar det aktuella värdet | Objektlitteralen kördes synkront direkt efter `ScrollCraft.mount`, innan `collect()` (som väntar på `DOMContentLoaded` om dokumentet fortfarande parsas) hunnit fylla den lokala `acts`-variabeln; `acts: acts` fångade då den ursprungliga TOMMA arrayen för alltid (en JS-egenskap kopierar värdet vid tilldelningstillfället, den uppdateras inte när källvariabeln senare pekas om). `settle()` påverkades aldrig (en funktion stänger över variabeln själv, inte ett kopierat värde) |
| **Plan 031, `R.act` löst lazy** | `readState`:s reveal-loop försöker lösa `R.act` på nytt varje anrop tills den lyckas, i stället för en engångsupplösning vid mount | Samma mätning som ovan | — | Löser samma tajmingsproblem från JS-sidan också: även efter getter-fixen skulle en engångsupplösning DIREKT efter `ScrollCraft.mount` fortfarande kunna hinna före `collect()` på en långsam maskin |
| **Plan 028 E, mätsteg, inte behållet** | `--k1..--k7` provflyttade till `.process-stick`, mätt (`synth`-metod, tre körningar): 1,24 / 1,87 / 3,26 ms per skrivning FÖRE flytten mot 1,52 ms EFTER — variansen mellan de tre "före"-körningarna (2 ms) överskriver planens egen 0,3 ms-tröskel för att döma. Återställd till `#process` (planens egen konservativa instruktion: "behåll bara om vinsten är ≥ 0,3 ms, annars återställ") | Egen isolerad synth-mätning, tre körningar | Plan 028 steg E, egen tröskel | Maskinen för brusig för att en 0,3 ms-skillnad ska vara mätbar med denna metod idag; ingen funktionell risk kvarstår eftersom flytten aldrig behölls |
| **Plan 028 C, dämpad kontrast ommätt** | Gradientens dämpade slutfärg (`color-mix(in srgb, var(--ink) 62%, var(--bg))`, oförändrad formel) mätt till 5,08:1 mot papperet, inte kodkommentarens tidigare citerade 6,3:1 | Egen pixelmätning av den faktiska renderade `color()`-outputen (109,8/107,8/102,0) | — | Samma färgformel som innan (bara leveransmekanismen bytt från 60 ordspann till en gradient), så 6,3:1 var sannolikt mätt under andra villkor i ett tidigare skede; 5,08:1 håller ändå planens egen 4,5:1-golv med marginal |
| **Plan 029, STOPPAD vid planens egen gräns** | 44 % (planens enda eskaleringssteg) mätt: delta 11 (mål ≥12), chroma 21 vid papperstoppet (mål ≤12) — båda under plan 029:s egna golv. Planens egen instruktion ("ligger 44 % också under 12: STOPPA och skriv talen") tillämpad; 44 % behållen (bättre än 40 %:s delta 10, ingen sämre) | Egen pixelmätning, flera skanningspunkter för att utesluta ett tajmingsfel | Plan 029 steg 2, egen STOPPA-klausul | Troligen en annan färgprofil/Chrome-version än loop 2:s mätning (samma klass av avvikelse som plan 029 själv förutsåg som möjlig) |
| **Plan 030, korrigerad egen kommentar** | En första kommentar påstod att R7:s `hyphens:auto` "aldrig delade i praktiken" - fel, ett R7-screenshot visar uttryckligen en fungerande delning ("VARU-MÄRKE", 3 rader). Kommentaren skriven om till att bara citera planens egen (arkitektens) mätning om att en `hyphens:auto`-brytning inte kan garanteras över webbläsare/plattform, utan att påstå att just den lokala körningen misslyckades | Egen granskning av tidigare skärmbild i samma session | — | En rättelse av mig själv upptäckt innan den skrevs in i filen, inte en ny mätning |
| **`scroll_verify.py`, `contrastUnderMedia`-falsklarm** | "Boka ett möte" rapporterad 3,95:1 vid 390 (golv 4,5:1); verifierad FALSK: samma sträng mäter 17,51:1 när kortet faktiskt är vänt (`?preview=back`) | Egen `contrast_over_media.py`-körning mot `?preview=back` | — | `scroll_verify` mäter textens DOM-position mot underliggande bild oavsett `backface-visibility`; `.face--back` upptar samma 2D-yta som `.face--front` (roterad 180° i 3D) och är osynlig vid vila, så verktyget samplar framsidans foto i stället för baksidans faktiska mörka grund. Verktygsskuld, inte sidans |
| **`scroll_verify.py`, blankBands vid 390 korrelerar med ramarnas position** | Två av sex band (3330-4031, 4803-5473) täcker exakt Calyx (top 3459) och Hōrai (top 4934); egna skärmbilder med 3s väntan bekräftar båda ramarna renderar fullt innehåll vid samma positioner | Egen skärmbildskontroll, `p027-calyx-1440.png`/`p027-horai-1440.png`-motsvarigheter vid 390 | — | `scroll_verify`s egen scanningstakt väntar sannolikt inte tillräckligt länge per position för att en riktig extern sajt (nätverk + rendering) ska hinna färdigt, till skillnad från en 3s-väntan i en riktad skärmbild. Verktygsskuld, inte en regression från plan 027 |

### Fynd, dokumenterade men inte lösta i R8 (arkitektens att döma)

| Fynd | Var upptäckt | Detalj |
|---|---|---|
| **`--sc-ps` max_step vid uppåtscroll på hero överskrider 3%-baren, återigen** | `motion_probe` i R8-grinden | cpu1, 100:60, uppåt: 4,61/8,81% - i linje med R7:s ursprungliga 4,54% och OLIKT loop 2:s citerade "reproducerades inte, 1,48%". Tre mätningar över tre rundor ger nu två höga (R7, R8) och en låg (loop 2); det låga talet kan vara det avvikande. Ingen av R8:s åtta planer rör heron-pinnens mekanik, motorn eller `sc-smooth.js`s lerp-matematik |
| **`.process-grid`s andra kolumn renderar kortare än sitt nominella mått vid 1440 (R6-fynd, oförändrat)** | Ärvt från R6/R7 | Se BRIEF § Byggarens rader, R6/R7; ingen R8-plan rör gridets spann |
| **Sidvikt 462 081 B, fortsatt över 425 kB-taket (R7: 452 879 B)** | `perf_probe.py` i R8-grinden | +9 kB sedan R7: `--rv`/`@property`-registreringen, `.price-ledger`s nya pseudoelement-CSS, `.hero-stage`s nya rader |

### Arkitektens rader, helhetsloopen runda 3 (2026-09-17)

| Area | Decision | Source | Source rule | Why |
|---|---|---|---|---|
| **Revealens latch** | samplas av sidan per bildruta tills shimen landat, aktobjektet löses per tick, exakt 1 (plan 035) | `shots/loop-3/latch_diag.json`: samma scrollY ger `--rv` 0,98 (hjul), 0,21 (PageDown), 0 (`scrollTo`); med samplern ≥ 0,9988 på alla fyra | F-014, gate 94: det ögat ser läser det lerpade värdet, och en reveal ska nå 1 oavsett scrollsätt (a11y F-03) | Leadens R8-fynd 1; `readState` körs bara per scroll-händelse, shimen lerpar 30 bildrutor till |
| **Revealen över en levande ram** | ingen `clip-path`/`mask` på en wrapper som innehåller en monterad iframe; irisen som `border-radius:50%` + `scale(--rv)` på en inre box med ramen kontraskalad `scale(1/--rv)`, uppdragningen som `translateY` på en inre box med ramen kontratranslaterad; `--rv` `inherits:true` (plan 036) | `shots/loop-3/probe/ab/`: cpu 1, prisfönstret, ramarna förmonterade: clip-path 101 till 303 ms p95, `mask-image` 65 till 86, `will-change:clip-path` 71 till 142, transformreceptet 35,6 / 46,7, ingen klippning 35 till 62 | Ramen transformeras aldrig efter att den visats (PRODUCT.md); under revealen står innehållet pixelstilla (skala × 1/skala = 1) och efter revealen är transformen identitet | K7: bandets bildtid är klippningen, inte omräkningen; mätt i fem A/B-omgångar |
| **Previewlägena** | `aimPreview()` vid skripttid, på `load` och på `fonts.ready` (plan 037) | `shots/loop-3/preview_check.json`: 1440 process-02 `--k2` 0,19, 390 process-01 `--k1` 0,67 | `?preview=` visar det formade läget (BRIEF § `?preview=`-plan) | Astra loop 3 fix 5; typsnitten flyttar li 02 till 07 efter att målscrollen räknats |
| **Sidans lägen** | kortsidan (`inert`), `is-turning` och `data-on` av läser shimens `cur` via 035:s sampler (plan 039) | `index.html` 1660, 1666, 1708; `scrollcraft.js` 835 (dwell-remapp) | F-014; performance.md (ingen vilande `will-change`); 025 B4:s avsikt (baklängesritning, aldrig klipp) | Astra loop 3 fix 2, 3 |
| **Processentrén** | konturen över `--k1` 0 till 0,30, glyfen 0,30 till 0,70 (plan 040) | `slices-1440/v3c-1440--s06.png`, `process-390/v3c-390-life-01.png` | House physics: en öppen spalt bär en helhöjdslinje eller stänger; H-15 | Astra loop 3 fix 6 |
| **Grunddriften** | tonlagret 44 → 24 %; H-19 omskriven på mellantonen (chroma 12 till 24 på träpanelen vid tesen, ≤ 2 i folden) (plan 038) | `shots/loop-3/drift2/drift2.json`: 44 % chroma 38, 24 % chroma 21, 0 % 0 på (720,180); `d44-thesis.png` mot `d24-thesis.png` | TASTE § 4.4: accenten gör en sak; `mix-blend-mode:color` skalar kulör med luminans, så ett golv på svärtan tvingar en tvätt | Leadens R8-fynd 2 |
| **Driften på `.ground`** | sidan äger de tre stoppen och skriver `--sc-canvas` på `.ground`, behålls bara med ≥ 3 ms p95 vinst i tes- och jättefönstret (plan 041) | loop 2 `synth3` 9,13 → 0,24 ms per skrivning; loop 3 `probe/ab/mount-noclip*` mot `*-nodrift*`: ingen skillnad i prisfönstret | Mät före ändring (F-013 regel 2) | Astra loop 3 fix 4; 028 D |
| **H-01, H-05, H-19** | raderna omskrivna med källa och mätning (kedjans budget 8 till 14 vh; 390-golvet 96 px; mellantonen) | `geom3.json`, `drift2.json` | Golvet är kontrollerbara påståenden; ett tal utan källa byts mot talet med källa | Fas A:s 12 vh saknade källa; H-05 (a) och 032 B stod i konflikt; H-19:s mätpunkt var fel |
| **Skivfångsten** | `slices_fix.py` (035:s sampler injicerad) är loopens skivfångst tills 035 är byggd; `scrollTo`-skivorna visar klippta ramar som inte är sovande | `slices-1440/v3c-1440--s04.png` mot `slices-1440-fix/…s04.png` | Verktyget får inte mäta en väg sidan inte täcker utan att säga det | K5 |

### Arkitektens rader, helhetsloopen runda 4 (2026-09-17)

| Area | Decision | Source | Source rule | Why |
|---|---|---|---|---|
| **Prisblockets platshållare** | `content-visibility:auto; contain-intrinsic-size:auto 760px` bort från `.price` (plan 042): dokumenthöjden konstant från load, motorns akttoppar = DOM:ens utan resize | `shots/loop-4/mountshift.json` (docH 10 880 → 10 582, `#process` 5 637 → 5 340 vid första målningen; motorn kvar på 5 637), `pricefix_ab.json` (390-previews 01/02: 1 av 3 → 3 av 3), `probe/ab/` (pris 53,0 → 35,3, jätte 94,1 → 81,7 ms median) | gate 93 (CLS), H-30, H-15; performance.md: en platshållare som inte matchar innehållet är ett skifte, inte ett skydd | R9:s "motorbunden gräns" (037) var sidans egen: platshållaren är 297 px högre än blocket; Astra loop 4 fix 1, funnen oberoende av arkitekten (C1) |
| **Calyx-öppningen** | `.calyx-wrap .rv{overflow:clip}` och riktningen uppifrån (`translateY((rv − 1)·100%)` på `.rv`, `(1 − rv)·100%` på ramen) (plan 043) | `shots/loop-4/astra-verify/verify_astra4.json`: ramens top 40 px vid `--rv` 0 / 0,25 / 0,5 / 1, wrapperbakgrund 0,1 % synlig i alla fyra; `calyx-rv0.png` | PRODUCT.md: reveal en gång på wrappern; F-002: målet tyst i vila och tänds vid scroll; 036:s egen regel (innehållet pixelstilla, identitet vid 1) | Astra loop 4 fix 2: 036 A:s Calyx-halva var en no-op (wrapperns klipp sitter på den stillastående boxen); loop 3:s A/B mätte samma no-op |
| **Driftens överlämning** | leg 2 räknas från överlämningen: `k = smooth((g − gH) / 0,35)` med `gH` = jättens råa progress när tesen når 1, mätt i `measureAct` (plan 044) | `astra-verify/verify_astra4.json`: `--sc-canvas` rgb(18,63,104) vid 3 600, rgb(244,242,238) vid 3 620; träet chroma 21 → 2 | gate 94 (kontinuitet), H-19 (kallt ljus utan klipp); TASTE § 4.5 (materialbyte, inte hopp) | Astra loop 4 fix 3; motorns egen loop gjorde samma hopp i R7/R8, 041 ärvde kurvan |
| **Bildtiden, golvet** | H-21/H-22/H-32 redovisas som arkitektoniskt golv utanför cellen (de två levande ramarnas montering och målning, motorns läsning) med talen; det som är kvar i filen är 042 | `probe/ab/hero-pin18-*` (pinnen ensam 18,4 ms = kontrollen, tre körningar), `hero-mount-*` (förmonterad 89,4), `hero-pricefix-*` (64,7); loop 2:s profilering | F-013 regel 2: mät före ändring; gate 93 | Herofönstrets försämring mot R8 (36 → 78 ms) är 036 B:s tidigare montering i fönstret, inte 035:s sampler |
| **H-23 återöppnad** | `--sc-ps` max_step 3,12 % (jätten) och 3,52 % (tesfönstret) vid cpu 1 i fönster där ramarna monteras och sidan lägger om 297 px; mäts om efter 042, ingen egen plan | `probe/giant-down-100-cpu1/`, `thesis-down-100-cpu1/`, `probe/ab/giant-fix-*` (2,86 till 3,13) | gate 94 punkt 2 | loop 2: korta flow-akter stegar när bildtiden faller |
| **Skivfångsten** | plain `scrollTo` med 3 s väntan är loopens skivfångst från loop 4 (035 byggd: `--rv` 1 / 1 i alla skivor); `slices_fix.py` pensioneras | `shots/loop-4/capture-log.txt` (`rv calyx=1 horai=1` från s04/s06) | Verktyget mäter den väg sidan täcker | K5 stängd |
## Direction contract

- **THESIS:** Alunix säljer webbdesign, och sidan bevisar påståendet i stället för att göra
  det: den är byråns eget visitkort, och besökaren vänder det själv.

- **OWN-WORLD:** Ett mörkt rum med ett bord, en snedställd lampa och ett kort som ligger
  där, plus tre sajter byrån faktiskt äger och kör live i spalterna. Ingen annan svensk
  webbyrå kan visa Calyx, Hōrai och Hyperborea som körbara sidor, och ingen rad i
  fingerprint-registret har ett hero-objekt med två sidor.

- **STORY**, sju skärmar, en mening var, i ordning:
  1. Kortet ligger stilla i mörkret och ljuspölen vandrar över det.
  2. Kortet börjar vändas kring sin egen mittaxel i takt med handen.
  3. Baksidan landar och bär namnet, vad byrån gör och en väg in.
  4. Sidan byter material till blått och Hyperborea-plåten bryter sin egen kant.
  5. Calyx laddar som en riktig sajt medan liggarens rader skrubbas fram bredvid.
  6. Priserna står utskrivna i mörkret mot Hōrai i samma spalthöjd.
  7. En rad, en adress, ingenting mer.

- **FIRST VIEWPORT**, 1440x900 vid ps = 0, element för element, med `--rail-x` = 86,4 px
  (`clamp(16px, 6vw, 96px)` vid 1440):
  1. Toppraden: ordmärket `ALUNIX` vänsterställt på railen, `kontakt@alunix.se` högerställt
     på samma rail. Scrollar bort.
  2. Rubriken `Er hemsida är nutidens visitkort` i två rader, vänsterställd på railen,
     Public Sans 300, 120 px efter rättelse 3.
  3. `figure.hero-plate`: 896 x 504 px, 16:9, vänsteranknuten på railen, en hårlinje
     `--frame-line`, framsidan med ljuspölen.
  4. Logo-docken helt innanför plåtens övre vänstra hörn, aldrig över hårlinjen.
  5. Underraden högerställd under plåten.

  Ingenting annat. **Fyra textelement**, vilket är precis taket i `garden-eight`-ribban
  (§ Vad jag måste slå), inte under det. Läggs ett femte till faller ribban.

- **FORM:** Sidan har inga plan, bara hårlinjer: radie 0 överallt, noll `box-shadow`, och
  djupet kommer av att materialet byts inuti spalten (blått block, papper, mörkt prisblock)
  medan grunden förblir ett och samma fotografi hela vägen ner.

## Persona-skisser

`reference-lock.md` § Three persona sketches. Villkoren är situationella, inte bara
permanenta.

```text
Primary: Verksamhetsägare i Sverige, 35 till 55, som ska beställa sin första riktiga
  webbplats · bärbar dator, 1440 bredd, kontorsuppkoppling, mitt på dagen · kom för att
  se om byrån kan något och vad det kostar.
Edge:   Samma person med markörprecision nedsatt av en handskada, som scrollar med
  tangentbord i stället för hjul · Page Down flyttar i hopp, inte i hack · det som bryter
  först är signaturakten, om vändningen bara läses vid små steg.
Stress: Samma beställare på en telefon, 390 bredd, utomhus i höstsol med en hand upptagen,
  som ska bestämma på fem minuter om hen ska mejla · har inte råd att tappa priserna eller
  mejladressen; kortet blir 4:5 och måste fortfarande vändas och fortfarande vara läsbart
  mot solreflexen.
```

Intersektionen som betalar två gånger: kontrastkravet som gör kortbaksidan läsbar i
höstsol är samma fix som gör den läsbar för nedsatt syn, och tangentbordsscrollens hopp är
samma problem som ett trögt hjul.

Den persona som är obekvämast: **Edge**, därför att den ställer signaturakten mot en
inmatningsmetod som flyttar `--sc-p` i stora hopp, och det är den som lättast designas
runt i stället för för. Konkret krav: `motion_probe` körs med `--wheel 20:120` **och**
`--wheel 100:60`, och `staircase` ska vara 0 i båda.

## Motion-tes

Låst, ur `concepts-V3c.md` (5). Byggaren skriver om den med sina egna ord och lägger till
värden.

- **Focal:** Plåtens egen vertikala mittaxel. `.plate-card` roterar kring
  `transform-origin: 50% 50%` inuti en `figure.hero-plate` med `perspective: 1600px`, så det
  som rör sig är exakt den yta som redan bar blicken vid ps = 0. Perspektivet är det som gör
  rotationen läsbar: den närmaste lodräta kanten växer medan den bortre förkortas, och det
  är den förkortningen `oryzo-ai`s skiva 02 visar mätt att ögat faktiskt läser en Y-rotation
  med.

- **Continuity:** Rubriken och underraden bär noll transform genom hela akten, inte en
  reducerad utan ingen. De är stagens ground, och de är hela skälet till att vändningen
  läses som att *kortet* vänds och inte som att sidan byter scen. Ljuspölen fortsätter
  vandra genom vändningen, så framsidan är i rörelse ända fram till att den försvinner.

- **Feedback:** `--flip = smoothstep(0.12, 0.72, ps)` där `ps` är `--sc-ps`, lerpad 0,16 per
  bildruta av shimen, så varje hjulhack ger utslag inom en bildruta utan att stega. Vid
  `--flip` = 0,5 står kortet 90 grader från betraktaren och det enda som återstår är
  hårlinjen `--frame-line`. Kortet har ingen tjocklek, så hårlinjen ensam är det ärliga
  svaret på var kortet är, och den är samtidigt `mattis-studio`-ribbans mätpunkt.

- **Budget:** En `pin` på hela sidan, span 2,2 och dwell 0,35, alltså ~2,55 vh av sidans
  9-11 vh, och den största spannet på sidan med god marginal. Noll `scrub`-akter (taket är
  två). Övriga sex skärmar är `flow` med stagger 30-80 ms. `will-change: transform` sätts på
  `.plate-card` och bara medan `0 < ps < 1`.

## Feeling curve

| Akt | Känsla | Vad på skärmen orsakar den |
|---|---|---|
| s1 hero, ps 0 till 0,12 | Igenkänning | Kortet ligger stilla, ljuspölen vandrar |
| s2 hero, ps 0,12 till 0,72 | Nyfikenhet | Kortet vänds; vid 90 grader bara hårlinjen |
| s3 hero, ps 0,72 till 1 | Erkännande | Baksidan landar: namnet, vad de gör, en väg in |
| s4 tes | Övertygelse | Materialbyte till blått, Hyperborea bryter sin kant |
| s5 bevis | Tillit | En riktig sajt laddar och går att titta på |
| s6 pris | Lättnad | Tre priser utskrivna utan att man behöver fråga |
| s7 avslut | Beslut | En rad, en adress, ingenting mer |

Aldrig två lika i rad. Toppen är s2.

### Byggarens bekräftelse, R1

Alla sju rader bekräftas oförändrade. Ingen känsla ändras, ingen rad flyttas.
Kontrollerat: inga två intilliggande rader delar känsla, och toppen s2 har sidans enda `pin`
och dess största spann, vilket är precis vad `feel-and-fingerprint.md` § The peak kräver att
peaken får på övriga akters bekostnad. Skälet till att kurvan håller är att s1 till s3 är tre
faser av **samma** akt och ändå får tre olika känslor: igenkänning är stillhet, nyfikenhet är
rörelse, erkännande är landning. En akt som bara hade haft "nyfikenhet" hade varit en akt för
lång.

### Den författade tystnaden

Skrivs här så att `scroll_verify.py`s `blankBands` i R2 kan skilja avsikt från fel.

| Var | Vad som står stilla | Varför det är avsiktligt |
|---|---|---|
| ps 0 till 0,12 i heron | Kortet står still; enbart `object-position` på `#heroPoolImg` rör sig | Pacing-tabellens "silence before the drop": toppen behöver något att vara en förändring **från**. Skärmen är aldrig tom, den bär rubrik, plåt och underrad |
| ps 0,72 till 1, dwell 0,35 | Baksidan i vila; ingenting rör sig alls | Landningen. `dwell` finns för att låta det formade läget stå kvar innan pinnen släpper |
| Hela akten | Rubriken och underraden | Kontinuitetsankaret, se § Motion-tes |

**Det band som kan larma falskt:** vid ps ≈ 1 är kortets baksida matt svart mot en mörk
grund, och i en helsidesskärmbild kan det bandet läsas som nästan enfärgat. Det är
avsiktligt och det är **inte** enfärgat: baksidan bär `ALUNIX` i 80,6 px, en monokicker, en
hårlinje, tjänsteraden och den typsatta länken, och rubriken står kvar utanför plåten hela
tiden. Träffar `blankBands` ändå det bandet är tröskeln fel, inte sidan, och fyndet ska
avfärdas med den här raden som källa.

**Ingen tystnad är kvar över.** Seamen mellan pinnens spacer och första flow-panelen är
uttryckligen kapad (`.stagger` får `padding-top: 0`, se decision ledger), just för att den
sortens halvtomma skärm är oavsiktlig tystnad och inte författad.

## Tell-someone

> Det är sidan där byråns visitkort ligger på bordet och vänds när man scrollar, och
> baksidan är deras riktiga kort.

## Device-tabell

Kolumnen **läser** anger `--sc-p` eller `--sc-ps` per device. F-014: allt som ögat ser
förflytta sig läser `--sc-ps`.

| # | Akt | Device | Familj | Läser | Varför |
|---|---|---|---|---|---|
| 1 | s1-s3 hero | `pin` span 2.2 dwell 0.35 + bespoke `rotateY` på `.plate-card` | pin | `--sc-ps` | Sidans topp får mest scrollrum |
| 2 | s1 hero | bespoke `paintHeroPool`, `object-position` på `#heroPoolImg` | bespoke paint | `--sc-ps` | `object-position` förflyttar sig |
| 3 | s4 tes | `drift` mot `#123f68`, `reveal="up"`, Hyperborea-bleed | drift | `--sc-p` för drift-tonen, `--sc-ps` för bleed-transformen | Tonen förflyttar sig inte; bleeden gör det |
| 4 | s5 liggaren | bespoke ordscrub + självritande tråd | bespoke paint | `--sc-ps` | Orden och trådens `scaleY` förflyttar sig |
| 5 | s5 Calyx | `reveal="up"` en gång, sedan ramen orörd | reveal | `--sc-p` (cue-opacitet) | En iframe transformeras aldrig efter att den visats |
| 6 | s6 Hōrai | `reveal="iris"` en gång | reveal (iris) | `--sc-p` (cue-opacitet) | Samma regel |
| 7 | s6 jätterubriken | ren CSS `scale(0.92 -> 1)` | kinetic type | `--sc-ps` | V3b läste `--sc-p` här; det är ett av felen V3c rättar |
| 8 | s1-s7 grunden | `drift` i tre stopp | drift | `--sc-p` | Grunden byter ton, den förflyttar sig inte |

Sex familjer, aldrig samma två i rad. `will-change` bara på `.plate-card` och bara medan
`0 < ps < 1`; `.giant`:s permanenta `will-change` tas bort.

## Rejected-lista

Ur `find-animation-opportunities`-gaten, fyra frågor per kandidat. Full tabell i
`concepts-V3c.md` (5). Avvisade: kortet vänder vid hover · ljuspölen följer pekaren ·
liggarrader lyfter vid hover · prisrader räknar upp · hårlinjer ritar sig in.
Behållna som bärande: framsidan mörknar under vändningen · specular-hårlinje på den ledande
kanten.

### Byggarens kandidater, R1

Fem till, övervägda och avvisade. Fyra frågor per kandidat: frekvens, syfte, hastighet,
funktion.

| Kandidat | Frekvens | Syfte | Hastighet | Funktion | Dom |
|---|---|---|---|---|---|
| Kortet kastar en skugga på grunden medan det vänds | En gång, inuti akten | Fysisk trovärdighet | Följer `--flip` | Ingen. En skugga är dessutom den enda djupmekanism sidan har förbjudit | **Avvisad.** TASTE § 4.7 (djup utan skugga) och `dope-security`-låset noll `box-shadow`. Framsidans mörkning gör samma jobb inom paletten |
| Grunden parallaxar bakom kortet under vändningen | Kontinuerligt genom hela akten | Djup | 0,3x sidans hastighet | Negativ. Grunden är sidans kontinuitetsankare; rör den sig läser kortet som stillastående och vändningen tappar sin referens | **Avvisad** |
| Underraden byter text när baksidan landat | En gång | Belöning för att ha scrollat | 300 ms | Fel. Den skulle lägga en andra lede i folden, och baksidan bär redan sin egen rad | **Avvisad.** Målbilden: "två leder i folden vore dubbelt" |
| Topplinjens ordmärke tonar bort när baksidans `ALUNIX` landar | En gång | Undvika två ordmärken samtidigt | 200 ms | Marginell. Toppraden scrollar redan bort av sig själv innan ps når 0,72 | **Avvisad.** Mät i R2: om de två ändå överlappar är det ett layoutfel, inte ett rörelsebehov |
| Prisraderna får sina hårlinjer inritade vid reveal | Tre gånger | Struktur | 300 ms | Ingen; strukturen finns redan i vila, och det är samma kandidat som arkitektens avvisade hårlinjerad en skärm längre ner | **Avvisad**, samma skäl som arkitektens rad |

Noterat om de två behållna: båda är rena `opacity`-kompositioner utan `filter` och utan
layout, båda drivs av samma `--flip` som redan finns, och båda ligger inuti målbildens egen
fysik. De adderar noll nya filer och noll nytt innehåll, vilket är hela skälet till att
`ASSETS.md` § 3 rekommenderar väg (d) framför en ny bild.

## Delight-tes

Kortet vänds.

## Asset-lock per medieplats

Fyra platser, fullständiga block i `runs/V3c/assets/ASSETS.md` § 4: hero plate front ·
page ground · Hyperborea plate · wordmark. Ingen av dem är en generate-prompt; allt
material är redan vendorat. `demo-calyx.webp` och `demo-horai.webp` är reserver, inte
medieplatser. Saknas något: skriv `[needs asset: ...]` och gå vidare, generera aldrig.

## Fem live-rubriker i kategorin, ordagrant

Webbsök `digital byrå webbdesign Sverige`, de fem bästa träffarna, H1 hämtad från varje
sida 2026-09-09 och citerad exakt.

| # | Rubrik, ordagrant | Källa |
|---|---|---|
| 1 | `Webbyrå i Stockholm` | frojd.se |
| 2 | `Limetta är en digitalbyrå` | limetta.se |
| 3 | `Webbyrå i Kalmar och Stockholm` | wilsoncreative.se/webbyra |
| 4 | `Webbdesign - vi gör inget lagom` | digitalwebbyra.se/webbdesign |
| 5 | `Digitalbyrå / Webbyrå i Stockholm` | ead.se |

Vad ribban faktiskt är: fyra av fem säger bara vad företaget är och var det ligger. Alunix
ordagranna rubrik, `Er hemsida är nutidens visitkort`, säger i stället något om läsaren.
Den ändras inte, och ingen ny rubrik på sidan får falla tillbaka till kategoriformen
"substantiv plus ort".

## Copy-plan

**Ordagrant, ändras aldrig** (r7 § Copy som ska användas ordagrant): hero-rubriken,
underraden, tesrubriken, raden `Webbdesign, design och system. Allt på ett ställe.`,
tjänsterna `Design` / `Utveckling` / `System` med 01-03, de tre paketraderna med priser,
prisrubriken, `kontakt@alunix.se`.

**Nya strängar i V3c** (går genom copy-gatens fem pass i R3): kortbaksidans kicker
`Digital byrå`, kortbaksidans tjänsterad, den typsatta länken `Boka ett möte ->`, och
eventuella bildtexter som ändras när `panel-open` och `panel-services` försvinner.
### Byggarens stränglista, R1

Varje sträng som står på sidan efter V3c, ordagrant, sorterad efter status. Ingen sträng
skrivs i R2 som inte står här.

**A. Ordagrant låst, ändras inte ett tecken** (`PRODUCT.md` § Brand Commitments):

```
Er hemsida är nutidens visitkort
Vi skapar skräddarsydda webbplatser som hjälper er att exponera verksamheten.
VI BYGGER ERT VARUMÄRKE.
Webbdesign, design och system. Allt på ett ställe.
Design
Utveckling
System
Standardpaket. Webbplats med CMS för egna ändringar och en första SEO-optimering.
26 900 kr
Paket med bokningssystem, betalning och kunddatabas.
38 900 kr
Helt skräddarsydda lösningar för produktkataloger, specialbyggda system med mera
Pris vid förfrågan
Alla har rätt till bra design.
kontakt@alunix.se
```

**B. Flyttad låst copy.** `Webbdesign, design och system. Allt på ett ställe.` bor i dag inuti
`section.panel-services`, som tas bort. Den flyttas ordagrant till platsen under
`VI BYGGER ERT VARUMÄRKE.` och ersätter V3b:s `.giant-sub`. Se decision ledger, rättelse 4.

**C. Ärvd från V3b, oförändrad, flyttad till kortets baksida.** Ingen av de tre är ny text;
de går ändå genom copy-gaten i R3 eftersom deras **plats** och därmed deras funktion är ny:

```
Digital byrå
Design  Utveckling  System
Boka ett möte →
```

Ordningen `Design  Utveckling  System` följer liggarens 01-03 så att de två listorna inte
motsäger varandra. **Öppen fråga till Anton, ur målbilden ordagrant:** hans meddelande
listade "utveckling, design, system": är den ordningen avsiktlig? Tills svaret finns gäller
liggarens ordning.

**D. Ärvd från V3b, oförändrad, står kvar där den står:** liggarens tre rubriker och deras
underrader, tesplåtens kicker och rubrik och stödtext, Hyperborea-bildtexten, prisingressen,
`Kontakt`-kickern, samt `Exempelsida` som kicker. Ingen av dem skrivs om i V3c.

**E. Genuint nya strängar i V3c: noll.** Det är ett resultat, inte en lucka. Kortets baksida
byggs helt av strängar som redan finns, och de två sektioner som tas bort tar sin egen text
med sig. Copy-gaten i R3 kör därför på lista B och C, inte på ny prosa.

**F. Öppen fråga, pilens tecken.** Skelettets § Copy-plan skriver `Boka ett möte ->` med
ASCII-pil; målbilden i planens § 7.5 skriver `Boka ett möte →` med Unicode-pil. R2 bygger med
`→` eftersom målbilden är den bindande källan, och skillnaden redovisas här i stället för att
väljas tyst. Gate 97 (pilsuffix på en länk) träffar strängen oavsett tecken; se decision
ledger, sista raden.

**Borttaget:** `2026 · SVERIGE`, den levande klockan, och hela `panel-services`-texten.
Ingen tidsstämpel återinförs.

**Borttaget utöver skelettets lista:** `panel-open`s brödtext
`Vi designar och bygger webbplatser, i nära dialog med verksamheten som ska leva i dem.` och
V3b:s `.giant-sub` `En sammanhållen process, från första skiss till lanserad sajt, med samma
team hela vägen.` Den senare är dessutom påhittad copy som påstår ett team, vilket
`PRODUCT.md` § absences förbjuder; den ersätts av låst copy enligt B ovan.

## Prestandaplan

F-013:s fem poster mot budgeten i `performance.md` § 1. Varje rad har ett målvärde.

| F-013-post | Mätt på V3b | Budget | Åtgärd i V3c |
|---|---|---|---|
| 4,9 MB överföring vid 1440 | 4,9 MB | <= 2,5 MB | `loading="lazy"` + IntersectionObserver-montering på båda iframes (de mäts inte förrän de monteras); `content-visibility:auto` med `contain-intrinsic-size` på `.price` och `.horai-wrap`; inga ovendorade resurser |
| 19 typsnittsfiler / 732 kB | 19 / 732 kB | <= 3 filer / <= 300 kB | Self-hostade `.woff2`, exakt tre filer: Geist 700, Geist Mono 400, Public Sans 300. Google Fonts-länken och `preconnect` tas bort. `<link rel="preload" as="font" crossorigin>` **bara** på Public Sans 300, som är folden. `font-display: swap` plus metric-matchad fallback med `size-adjust` |
| 17 långa tasks under scroll | 17 | 0 | En passiv scroll-lyssnare som bara schemalägger, en rAF-loop som läser och skriver, deadband som stoppar loopen i vila. Inga layoutläsningar i scroll-handlern. `sc-smooth.js` kopieras in oförändrad |
| Vilande `will-change` på fyra element | 4 | 0 | `.giant`, `h1.hero-headline`, `.calyx-wrap` och `#projekt` får ingen permanent promovering. `will-change` sätts bara på `.plate-card` medan `0 < ps < 1` |
| Hotlänkad 1,1 MB Unsplash-hero | 1,1 MB, extern CDN | <= 250 kB WebP, vendorad | Ingen extern bild finns kvar. Hero-plåtens bild är `assets/k1-stage-pool.webp`, 65 kB, vendorad i cellen. `width`/`height` + `decoding="async"` + `fetchpriority="high"` på den; `loading="lazy"` på allt under vecket |

Dessutom: `min-height: 100dvh`, aldrig `100vh`. Ingen `transition: all`. Ingen
`backdrop-filter`. `text-wrap: balance` på rubriker. Alla `<img>` har `width` och `height`.

Målvärden som ska vara sanna innan rundan lämnas, mätt vid 4x CPU: `staircase = 0`,
`max_step <= 3 %`, frame p95 <= 20 ms, noll frames > 33 ms, båda scrollriktningarna,
LCP <= 1,8 s, CLS <= 0,05.

## `?preview=`-plan

| Läge | Vad det tvingar | Varför det behövs |
|---|---|---|
| `?preview=back` | `--flip: 1` på `.plate-card` | Lead ska kunna skärmbilda kortbaksidan i vila utan att scrolla |
| `?preview=front` | `--flip: 0` | Baslinjen för folden |
| `?preview=mid` | `--flip: 0.5` | Kontrollen att bara hårlinjen syns vid 90 grader |
| `?preview=ledger` | Ordscrubbens alla ord till `opacity: 1` och `--thread` till `scaleY(1)` | Liggarens formade läge är sidans andra bespoke paint. Utan ett läge går det inte att skärmbilda den i vila, och R3:s granskare får då bedöma ordscrubben mitt i en lerp, vilket är exakt det `shoot.mjs` finns för att undvika |
| `?preview=bleed` | Hyperborea-plåtens `translateX` till sitt slutläge (11 %) | Bleeden är den enda transform på sidan som kan hamna utanför dokumentet. Måttet ska gå att läsa på en stillbild vid 1440 och 768, inte uppskattas i rörelse |

Alla lägen sätter `window.__scFreezeMotion = true` så att shimen spårar det råa värdet
exakt och skärmbilden visar det formade läget, inte en lerp i flykten.

## Fingerprint

Fingerprint-gaten (>= 4/6 mot varje registerrad) **gäller inte V3c**: cellen är en
iteration av V3b och tar över registrets V3-linje. Den föreslagna uppdaterade registerraden
står i `concepts-V3c.md` (4) och förs in av lead efter Antons dom, inte av byggaren.

### Byggarens läsning av registret, R1

Hela `wiki/projects/_index/design-fingerprints.md` läst: 7 seedrader plus 29 Alunix-rader ur
rundorna 1 till 7. **Två saker i registret motsäger den föreslagna raden.** Ingen av dem är
byggarens att lösa, båda redovisas.

**1. "Registrets V3-rad uppdateras till V3c" krockar med append-only.**
`feel-and-fingerprint.md` § The fingerprint gate är uttrycklig: *"Rows are append-only ... A
build that has been superseded stays in the table, because the space it occupies is still
occupied"* och *"never edit a row to make room for it"*. Registret upprepar regeln i sin egen
ingress. V3b:s rad beskriver en yta som fortfarande är tagen: ljuspölens vandring som
signatur, plåten som ram, åtta `flow`-akter utan `pin`. V3c tar inte den ytan, den tar en
annan. **Föreslagen läsning:** `concepts-V3c.md` (4):s rad läggs till som en **ny** rad och
V3b:s rad står kvar oförändrad; formuleringen "uppdateras" byts mot "läggs till". Fingerprint-
gaten (>= 4/6) är fortfarande inte tillämpad på cellen, så tillägget kostar ingenting. Domen
är arkitektens och lead:s, inte byggarens, och raden förs in efter Antons dom som skelettet
säger.

**2. Continuous world är den mest uttömda familjen i registret, och registret säger det
själv.** Ingressen till Alunix-blocket: *"Continuous world är en femradsfamilj (M1, V1, V2,
V3, V3b) som också delar nav-behandling och avslutsmönster ... de fem raderna klarar grinden
mot varandra bara på hero-device, aktform och signaturdrag, vilket är exakt 3 av 5 icke-fria
dimensioner, det bara nödvändiga. Ett sjätte bygge i den familjen skulle inte ha någonstans
kvar att skilja sig."* V3c blir det sjätte. Det är **förenligt** med att cellen är en
iteration och undantagen från grinden, men det betyder att ingen framtida cell kan ta samma
familj igen utan att byta grammatik, nav eller värld. Skrivs här så att det står i klartext
innan någon planerar en r9-cell i samma linje.

**Inget annat i registret motsäger raden.** Kontrollerat mot de två uppslitna nav-mönstren
och de två uppslitna hero-devicerna som registret listar som förbrukade: V3c ärver den tunna
toppraden med ordmärke och kontakt (femradsmönstret), vilket är avsiktligt delat och står i
decision ledger som "nav är en av de tre dimensioner som INTE ändras"; hero-devicen är ny och
kolliderar varken med den blå timmens fotografi eller med det krossade affischordmärket.

## Vad jag måste slå

En rad per låst referens. Full tabell med mätpunkter i `concepts-V3c.md` (7).

- `garden-eight`: heron innehåller exakt tre element, inget mer.
- `mattis-studio`: kortet är fysiskt, inte en ritad ram; vid ps = 0,5 syns bara hårlinjen.
- `squarespace`: inversionerna görs utan ett enda kort.
- `oryzo-ai`: framsidan bär material över hela ytan och en ljusrespons som ändras med vinkeln.
- `dope-security`: accenttalet är utskrivet (två förekomster) och det finns noll `box-shadow`.
- `monologue`: hårlinjerna ligger på `--rail-x`-rastret, inte på egna värden.
- `planhat`: rubriken ligger på den mörka grunden, aldrig över ljuspölen.

## Lästa referenser

Arkitektens egen digest står i `concepts-V3c.md` § Lästa referenser och ersätter inte den
här. **87 filer**, alla lästa i den här sessionen: bilder som pixlar med `Read`, text som
text, aldrig med `cat`. Arkitektens öppna punkt (att bara 6 av 12 respektive 7 av 12 skivor
lästs för `oryzo-ai` och `mattis-studio`, och bara folden för de tre övriga) är **stängd**:
alla 48 befintliga skivor är lästa nedan. `planhat` har ingen `slices/`-katalog på disk, bara
`fold.webp` och `shot.webp`; det är en egenskap hos posten, inte en utebliven läsning.

### Smak och återkoppling

| Fil | Gör | Tar | Lämnar |
|---|---|---|---|
| `design-catalogue/TASTE.md` | Beskriver harmonin i 89 sparade källor: en auktoritet per sida, fem återkommande relationer, per kategori vad som bär, tio beslutsregler, och en avvisningslista med förekomsttal | § 1 (auktoriteten namnges före koden, allt annat går ner ett steg), § 2.4 (skalkontrast 5-15x), § 4.4 (ett papper, en accent som gör en sak), § 4.7 (djup utan skugga), § 4.8 med r6-preciseringen (i set-piecet är rörelsen auktoriteten) | § 3:s kategoriprofiler för hospitality, consumer-brand, playful och luxury-craft; § 4.1:s typsnittsval, eftersom V3c ärver ett godkänt typsystem och inte väljer om |
| `design-catalogue/FEEDBACK.md` | Fjorton poster, en regel per dom, med Antons ord oredigerade | F-006 (glas och konsol-chrome är slop), F-007 (avvikelse från målbilden stoppar rundan), F-009 (orkestreraren äger assets), F-010 (fönster i fasaden, inte ruta utanpå), F-011 (rörelsen spelar alltid), F-012 och F-014 (`--sc-ps`, och att "hackigt" är två fel som mäts var för sig) | F-001 och F-002 i sak: de är uttryckligen upphävda av F-011 och det finns ingen reservlägesväg kvar att göra rätt |

### Katalogposten `oryzo-ai` (topprankad, 14 poäng; samma register och samma grammatik)

| Fil | Gör | Tar | Lämnar |
|---|---|---|---|
| `entry.md` | Låser varm walnut-tomrum, versal-500 som enda röst utom en brödröst, orange enbart till credits, 100vh per sektion, streckade hårlinjer, och en fjäder-easing `cubic-bezier(0.3,0,0.66,-0.3)` | "Fence an accent colour to editorial credit only" som princip (V3c: accenten gör en sak) och "compress display leading until letterforms overlap" (kortbaksidans `line-height:.9`) | 100vh-låset per sektion, streckade avdelare, radie 12 px, hela den varma paletten, den fjädrande overshooten (ett visitkort som studsar tillbaka är inte ärligt) |
| `extract/oryzo-ai-design-language.md` | Mäter 3577 element: `#ffedd7` 6070 förekomster mot `#dc5000` 175, 35 distinkta typgrader, 4 typsnittsfamiljer, scroll-linked motion, fyra durationssteg 150-500 ms | Talet som metod: att en accent kan redovisas som en kvot mellan förekomster i stället för som en känsla | Durationstabellen (V3c:s rörelse har ingen egen tid, den följer scrollen), de fyra gradienterna, glödskuggorna på modalen |
| `fold.webp` | Ovanifrånfoto av korkunderlägget på skärbräda, ordmärket i affischgrad uppe till vänster, halvtransparent creditkort nere till vänster, "SCROLL TO CONTINUE" i botten | Att ett ordmärke i affischgrad kan dela fold med ett objekt utan att konkurrera, därför att objektet ligger i en annan ljushet | Scroll-cuen (gate 88), creditkortet som lager ovanpå fotot, den varma paletten |
| `slices/00.webp` | Samma vy som folden, fångad en gång till | Ingenting utöver folden | Samma som folden |
| `slices/01.webp` | Objektet rakt uppifrån, centrerat i mörkt tomrum, rubriken i två rader vänster, brödtext höger | Kompositionen tre spalter runt ett objekt som äger mitten | De tre textspalterna: V3c:s hero har rubriken **utanför** objektet, inte omkring det |
| `slices/02.webp` | Objektet lutar i tomrummet; kanten och det spräckliga materialet fångar ett snedljus | **Kärnlärdomen för hela cellen:** rotationen läses genom att materialet och den raka kanten förkortas under ett riktat ljus, inte genom att rotationen finns | Walnut-grunden, versal-500-rösten |
| `slices/03.webp` | Objektet vridet så att insidan syns; typen har tonats ner till grått medan objektet är ljust | Att typen viker i värde exakt när objektet tar rörelsen (TASTE § 4.8) | Att låta rubriken tona: V3c:s rubrik står kvar i full styrka som kontinuitetsankare |
| `slices/04.webp` | "Powered by AI" i display, objektet mindre och i luften, händer på väg in underifrån, orange kredit `ORYZO-1` | Att objektet får en enda ljuskälla och att bakgrunden är helt tom runt det | Händer (Alunix visar inga människor), orange, hela "AI"-tonläget |
| `slices/05.webp` | Handen håller objektet; tre rader versal mikrocopy nere till höger | Mikrocopyns plats: registergrad i ett hörn, aldrig i mitten | Handen, och att mikrocopy blir en poäng; V3c har fyra monoetiketter totalt |
| `slices/06.webp` | En kromatisk regnbågsram runt hela viewporten i hover-läge, med "TRY TO HOVER HAND" | Ingenting | Hela greppet: en kulörram runt viewporten är gate 89-territorium och bryter "ett papper, en accent" |
| `slices/07.webp` | Samma ram, starkare mättnad | Ingenting | Samma |
| `slices/08.webp` | Objektet ensamt i tomrum, texten delvis utskuren av objektet | Överlappet objekt-över-typ som djup utan skugga | Den nästan tomma skärmen som eget steg; V3c har inte råd med 100vh per sats |
| `slices/09.webp` | Objektet i en streckad mätram med cirkel och tick-märken, "SO PORTABLE," vänster, scroll-cue | Ingenting | Mätramen är ritad UI-chrome (gate 47) och cuen är gate 88 |
| `slices/10.webp` | Objektet i en röd folieförpackning, mitt i den jättetypografiska raden "it's wearable" | Att objektet skär genom raden i stället för att ligga bredvid den | Färgen, förpackningen, de streckade markeringsramarna |
| `slices/11.webp` | Samma rad nu självlysande vit, objektet ovanför den, ramen kvar | Att en jätterad kan byta värde utan att byta plats | Glöden runt typen: sidan har noll `box-shadow` och noll `text-shadow` |

### Katalogposten `mattis-studio` (låst av `select.py` och ärvd ur V3b:s eget lås)

| Fil | Gör | Tar | Lämnar |
|---|---|---|---|
| `entry.md` | Beskriver hero-kortet som "a UI component being inspected" och kräver att fotot är svartvitt där det möter färgblocket | Rollregeln "photography stays black-and-white wherever it meets a saturated colour block" (V3c: Hyperborea-plåten mot den blå tesen) och "only one saturated flat-colour section per page" | Hela konsolvokabulären: versionstagg, klocka, hörnmarkeringar, slot-räknare. F-006 och gate 47 träffar den rakt av |
| `extract/mattis-framer-website-design-language.md` | Mäter 1909 element: Geist genomgående, `#000000` 2217 förekomster, `#ff4500` 10, radie 7-100 px, en enda easing `cubic-bezier(0.44,0,0.56,1)` i 15 användningar | Att ett helt bygge kan bäras av **en** easingfamilj; V3c har en enda rörelselag och behöver ingen andra kurva | Radieskalan (V3c ligger på 0), skuggstacken på kortet, de tre saturerade sekundärfärgerna |
| `fold.webp` | Svart hero med hörnmarkerad ram runt ordmärket, versionstagg, grundarfoto, orange signatur, tre tjänsteord på en rad, slot-räknare i botten | Att tjänsteorden står som **en rad i registergrad**, inte som tre kort; det är precis vad V3c:s kortbaksida gör | Konsolramen, versionstaggen, klockan, slot-räknaren, grundarfotot, signaturen, orange |
| `slices/00.webp` | Samma fold utan den nedre chrome-raden | Bekräftar att ramen är ritad och platt: den har ingen tjocklek och ingen baksida | **Hela ramen.** Det är den här bilden V3c lånar som avvisning |
| `slices/01.webp` | Ett helt orange fullbleed-block med tesen, en gråtonad plåt i mitten, "12+ Industries" nere till höger | Att en tes får äga ett helt materialbyte (V3c: den blå tesen) | Den mättade orangen, den påhittade statistiken, "24+ PROJECTS" |
| `slices/02.webp` | Ljus sektion med en svartvit editorial-plåt i högerspalten och jätterubrik vänster, sedan ett fullbredds boxmockup-foto | Svartvitt foto mot ett färgblock i stället för färgfoto (TASTE § 2.1) | Boxmockup-rutnätet, showreel-knappen, "SEE THE WORK"-cuen |
| `slices/03.webp` | Fullbredds plåtrader med case-etiketter `(01)` och en helt svart tyst remsa mellan två plåtar | Den svarta tysta remsan som andrum mellan två bilder | Case-galleriet; Alunix har tre exempelsajter, inte ett portföljflöde |
| `slices/04.webp` | Räfflad teal-bild, svart remsa, svartvit löparplåt, case-etikett "WE RUN BRAND" | Att den tysta remsan upprepas som system, inte som engångsgrepp | Den räfflade bilden och färgen; V3c är gråskala |
| `slices/05.webp` | "BUILT ON REPUTATION" med ett svart kort som bär "/2.7+ average client rating on Google & Clutch" | Ingenting | **Allt.** Omdömen, betyg och kundantal är exakt det `PRODUCT.md` § absences förbjuder |
| `slices/06.webp` | Ljus grund med ett vitt kort "/36%" och "Start a Project", sedan en svart SERVICES-sektion | Ingenting | Ett andra påhittat tal, och kortformen igen |
| `slices/07.webp` | Orange sektion "HOW WE DO IT" med tre siffror (22+, 2.2S, 30%) som textur | Formen (displaygrad, liten etikett) enligt TASTE § 4.9 | Innehållet; V3c har inga sanna sådana tal, alltså inga tal |
| `slices/08.webp` | 66%-talet, ett omdöme med porträtt, sedan en ljus FAQ "BEFORE WE GET STARTED." med dragspel | Att en FAQ kan vara en liggare med hårlinjer i stället för kort | Omdömet, porträttet, procenttalet, och FAQ:n i sig: V3c har ingen |
| `slices/09.webp` | Citat med foto och signatur, sedan "PRICING." med flikar och en jämförelsetabell med kryss och streck | Att priset får vara sidans egen liggare | Citatet, personen, tabellen med kryss, `$4,800/MONTH`, och tankstrecket i citatet |
| `slices/10.webp` | Tabellslut med "GET STARTED", sedan ljus "WHAT OUR CLIENTS SAY." med karusell och citat | Ingenting | Karusellen och omdömena |
| `slices/11.webp` | Svartvit porträttplåt, logotypvägg med sju kundmärken, sedan "NEWS AND UPDATES." | Ingenting | Logotypväggen är uttryckligen förbjuden i r7:s § Förbjudet |

### Katalogposten `dope-security`

| Fil | Gör | Tar | Lämnar |
|---|---|---|---|
| `entry.md` | Anger accentfrekvensen som ett tal ("en glöd, en fyllning, en linje per sida"), kapar skugga till en enda 1 px hårlinje, och ger tre typsnitt tre uteslutande roller | **"State an accent's frequency as a number, not a feeling."** V3c skriver ut sitt accenttal i decision ledger. Och "cap shadow to a single 1px hairline, everywhere else use line weight" | Tre typsnitt, violett, pill-radien 1584 px, GrandSlang-regeln, koordinatfoten |
| `extract/dope-security-design-language.md` | Mäter 5000 element: `#af50ff` **3** förekomster mot `#f7f9fa` 9140, tio gradienter, sex `box-shadow`-nivåer trots låsets "shadowless" | Att låsets påstådda disciplin går att verifiera mot mätningen: tre förekomster är tre, och den siffran är granskningsbar | Gradienterna och skuggnivåerna; mätningen visar att posten själv inte håller sin egen skuggregel, vilket är skäl att inte ärva den |
| `fold.webp` | Skymningsfoto som hero, ett frostat "boarding pass"-kort till höger med två inloggningsknappar, kursiv display-serif blandad med grotesk | Ingenting ur folden | Glaskortet (F-006 rakt av), violett, kursiv serif i rubriken, två knappar i heron |
| `slices/00.webp` | Samma fold med kortets rubrik utbytt till "Deploys on device in minutes" | Bekräftar att glaskortet är sidans bärande grepp och därmed inte kan lånas | Samma |
| `slices/01.webp` | Nästan svart sektion med sju monostämpelrader i 74 px, tracking 0.2 em, pil till höger, typen övergår från fylld till konturerad nedåt | Att en lista kan vara **rader i registergrad** i stället för kort, och att en enda typografisk parameter (fyllning) kan bära en gradient av betoning | Pilarna på varje rad (gate 97), 74 px-monostämpeln, konturtypen |
| `slices/02.webp` | "BEAUTIFUL UX"-stämpel, sedan "There's a problem with swgs today." med en streckad understrykning under ett ord | Ingenting | Den streckade understrykningen: V3c:s enda understrykning är accenten på den typsatta länken |
| `slices/03.webp` | Samma rubrik, ett flygplan på ett streckat spår, GEN 1/2/3-räls till höger | Rälsen som en beständig positionsindikator i marginalen | Rälsen i sak; V3c har sju skärmar och behöver ingen |
| `slices/04.webp` | Samma vy med ett jätteord "GEN 1" som textur bakom typen i mycket låg kontrast | Ett enda ord i grunden som textur bakom typen, som djup utan skugga | Det platta produktfotot bakom, monostämpeln, koordinatfoten |
| `slices/05.webp` | "A proxy "box" was installed in-office." med en roterande cirkeltext-sigill över ett mörkt produktfoto | Att ett objekt får ligga i fotots eget mörker i stället för på ett lager ovanpå | Cirkeltexten (sigillet är dekoration som inte identifierar, lokaliserar eller möjliggör något) |
| `slices/06.webp` | "Internet is re-routed to a data center." med serverfoto och ghost-ordet GEN 2 | Att samma greppet upprepas identiskt per akt, vilket gör serien läsbar | Kursiven mitt i rubriken (`re`), som är exakt den reflexitalic SKILL.md förbjuder |
| `slices/07.webp` | "It's like taking a stopover flight." centrerad, planet på en böjd streckad bana | Ingenting | Centrerad rubrik; V3c:s allt ligger på `--rail-x` |
| `slices/08.webp` | Nästan tom skärm: bara den streckade flygbanan och planet | **Att en avsiktligt tom skärm är läsbar bara om något rör sig i den.** Det är samma resonemang som § Den författade tystnaden bygger på | Den tomma skärmen i sig; V3c:s budget är 9-11 vh och har inte råd |
| `slices/09.webp` | "The proxy is on your device." med en linjeritad laptop, violett glöd och sigillet | Ingenting | Den ritade laptopen är fabricerad produkt-UI (gate 79) plus re-drawn chrome (gate 47); glöden är skugga |
| `slices/10.webp` | Samma vy med en förstoringscirkel över laptopens hörn | Ingenting | Samma |
| `slices/11.webp` | Samma vy, något scrollad | Ingenting | Samma |

### Katalogposten `monologue`

| Fil | Gör | Tar | Lämnar |
|---|---|---|---|
| `entry.md` | Mörk grund, serif-display mot mono-register, cyan kapad till 2-3 förekomster per skärm, komplex skuggstack reserverad för **ett** objekt | Principen att den komplexa materialbehandlingen reserveras för exakt ett objekt på sidan; V3c:s enda sådana objekt är kortet | Hela typsystemet (V3c har Geist och Public Sans låsta), cyan, skuggstacken, det ghostade 400 px-ordmärket |
| `extract/monologue-to-design-language.md` | Mäter 1596 element: **49 unika skuggor**, 38 gradienter, 26 typgrader, 7 typsnittsfamiljer, designsystempoäng 75 (C) | Kontraexemplet, mätt: en sida kan se disciplinerad ut och ändå bära 49 skuggor. Det är skälet till att V3c:s accenttal och skuggtal skrivs som tal i ledgern | I stort sett allt: skuggorna, gradienterna, typgraderna. Posten är ett varningsexempel på mätvärdena, inte en förebild |
| `fold.webp` | Mörk grund med hårlinjeraster, serif-rubrik centrerad, mono-brödtext, en fylld pillknapp, fyra flikar med färgade appikoner under | Hårlinjerastret som håller sidans marginaler synliga (V3c: hårlinjerna på `--rail-x`) | Centrerad hero, badge-raden ovanför rubriken, ikonfliksraden, mono som brödtext |
| `slices/00.webp` | Samma fold med fliken "Meetings" aktiv och en produktskärm under | Bekräftar att rastret löper genom hela sidan, inte bara i folden | Fliksystemet |
| `slices/01.webp` | Produktskärmar i teal, sedan "Used by builders at companies including" med sju kundlogotyper | Ingenting | Logotypväggen, förbjuden i r7:s § Förbjudet |
| `slices/02.webp` | Mono-stycke med inline färgade appikoner, sedan "Use your voice wherever you type" med applista | Ingenting | Ikoner inuti brödtext; V3c har noll ikoner |
| `slices/03.webp` | Fliken Coding, en produktskärm med kod, "Give your coding agent the whole task" | Ingenting | Fabricerad produkt-UI (gate 79) |
| `slices/04.webp` | Fliken Team chat, en chattskärm, "Say the list. Skip the formatting." | Ingenting | Samma |
| `slices/05.webp` | Fliken Messages, en iMessage-skärm, "Text like you talk" | Ingenting | Samma |
| `slices/06.webp` | Fliken Email, en mejlskärm, sedan "A notes app built for builders" | Ingenting | Samma |
| `slices/07.webp` | Fyra numrerade lodräta paneler 01 Capture / 02 Summarize / 03 Share / 04 Build med roterade serif-etiketter över bilder | Numreringen 01-04 som en lodrät liggare i stället för fyra kort | De roterade etiketterna, färgpanelerna, bildernas kulörer |
| `slices/08.webp` | MCP-rutor med leverantörschips (Codex, Gemini, ChatGPT, Cursor, Claude, GitHub), sedan tre funktionskort | **Tre lika feature-kort**, TASTE § 5:s egen avvisningslista, som förekomst i naturen | Hela rutnätet; det är exakt formen `panel-services` tas bort för att undvika |
| `slices/09.webp` | Offline- och lägesrutor, sedan "Platforms We Support" och en enhetsrendering | Ingenting | Enhetsrenderingen |
| `slices/10.webp` | Enhetsrendering, ett omdöme med porträtt, en fliksrad med fyra logotyper, sedan "Pricing" | Ingenting | Omdömet och porträttet |
| `slices/11.webp` | Prissättning som två kort, `$0` och `$12/month`, med en gul "BEST OPTION"-badge | Ingenting | Priset som kort med badge. V3c:s pris är en liggare med hårlinjerader, vilket är hela `squarespace`-ribbans poäng |

### Katalogposten `planhat` (wildcard, utanför kategorin)

| Fil | Gör | Tar | Lämnar |
|---|---|---|---|
| `entry.md` | Ransonerar fotografi till **exakt ett** på hela sidan, eskalerar negativ tracking med grad, ersätter all skugga med 1 px hårlinjer, och stänger in en funktionell accent till produkt-UI | Att fotografiet är auktoriteten och att typen då viker helt; och hårlinjen som fullständig ersättning för skugga | Paletten, "agentic platform"-rösten, knappformen, den femdelade stilalternativsuppsättningen i displaysnittet |
| `extract/planhat-com-design-language.md` | Mäter 2003 element: `#000000` 2610 förekomster, `#c0ff66` 2, tracking -0.06 em vid 117 px, två `box-shadow` totalt | Talet -0,06 em vid 117 px som belägg för att tight tracking är en mätbar egenskap och inte en känsla | Tracking-kurvan i sak: V3c:s rubrik är Public Sans 300 på -0,01 em och ärvd, den räknas inte om |
| `fold.webp` | Ett enda måleriskt, räfflat foto bär hela folden; rubriken i vikt 300 ligger i fotots mörka vänsterdel; en liten kicker ovanför; en vit knapp | Bekräftar TASTE § 2.1 mätt: vikt 300 i stor grad ligger alltid i fotots **mörka** parti. V3c:s rubrik ligger på den mörka grunden, aldrig över ljuspölen | Det varma gröngula motivet, den vita fyllda knappen, kickern över rubriken |
| *(ingen `slices/`)* | Posten har `fold.webp` och `shot.webp` på disk och ingen skivkatalog | Ingenting | Redovisas som en egenskap hos posten, inte som en oläst fil |

### Kedjans referenser

| Fil | Gör | Tar | Lämnar |
|---|---|---|---|
| `reference-lock.md` | Definierar låsblocket i sju fält, decision ledger med obligatorisk `Memorable detail`-rad, asset-lock per medieplats, tre persona-skisser, anti-averaging-testerna, och Tier 0:s "Primary = the locked system itself" | Tier 0-raden som gör V3b till primärkälla; regeln att en referens utan "lämnar"-rad är dekoration; kravet att fem live-rubriker citeras ordagrant före copyarbetet | Tier 2-flödet (V3c har ingen användarlämnad URL) och Refero MCP-steget, som inte är konfigurerat |
| `scroll/devices.md` | Nio devicefamiljer, cue-kontraktet med fem regler, den lerpade playheaden, lagerscener, premium-fade-in:ens exakta värden, och AB06-regeln att motorns klasser aldrig restylas | "Ground or greet" (heron behöver ingen cue), regeln att en flow-sektion direkt efter en pinnad akt tar reducerad padding, och `pin`-spannets golv 1,2 | Lagerscenernas planvärden, `pan`-rälsen, `count`-devicen (V3c har inga tal att räkna upp), hela pekarfamiljen |
| `scroll/feel-and-fingerprint.md` | Feeling curve före akterna, en peak per sida, tell-someone-testet, signaturdragets definition, embodiment som krydda, pacing som känsla, och fingerprint-gatens sex dimensioner med append-only-regeln | Peakens tre privilegier (assetbudget, tystnaden före, mest scrollrum), kravet att författad tystnad skrivs i BRIEF, och append-only-regeln som gav § Fingerprints första motsägelse | Fingerprint-gatens 4/6-tröskel, som uttryckligen inte gäller den här cellen |
| `scroll/pace.md` | `rate = weight / clip_seconds` inom några procent, 36 % läses som defekt och 6 % som en rörelse, 0,21 vh per sekund film som golv, `data-sc-lerp` 0,12 på en worldflight | Insikten att takt är ett tredje fel skilt från stegning och tappade bilder | Hela worldflight-apparaten: V3c har noll klipp, noll legs och noll `data-sc-window`, så `rate`-aritmetiken har inget att räkna på |
| `motion-smoothness.md` | Skiljer stegningsfelet från det tappade-bildrutor-felet med mätvärden ur F-013, ger `--sc-ps`-kontraktet, och sätter baren staircase 0 / max_step <= 3 % / p95 <= 20 ms / noll frames > 33 ms i båda riktningarna | Hela regeln, ordagrant, som cellens rörelsekontrakt; och varningen att en prob som kan godkänna en död sida är sämre än ingen prob | Den kända inkonsekvensen på rad 98 i `scrollcraft.css`: motorn redigeras aldrig |
| `performance.md` | Budgeten i gate 93, laddningsreglerna, renderingsreglerna, och en Never-lista på nio punkter | Hela budgeten som cellens målvärden, plus tre Never-punkter som V3b bryter mot i dag: iframe monterad vid load, `will-change` på klass, hero-bild på annat företags CDN | Klippbudgeten (32 MiB desktop): V3c har inget scrubbat klipp |
| `lift.md` | Sju passsteg med mekanisk grind emellan, reviewer-kontraktet i fem sektioner, och stoppvillkoret "beats" per låst referens | Reviewer-kontraktets form, som R3:s granskare ska svara i, och triageordningen trasigt före tillstånd före flöde före visuellt | Passen 5c, 5e och 3 i sak; de körs bara på ett fynd, och R1 har inga fynd att köra dem på |

### Registret

| Fil | Gör | Tar | Lämnar |
|---|---|---|---|
| `wiki/projects/_index/design-fingerprints.md` | 7 seedrader plus 29 Alunix-rader, med en ingress som säger vilka grammatiker, nav-mönster och hero-devicer som är uppslitna | De två motsägelserna i § Fingerprint ovan, och listan över förbrukade nav-mönster som bekräftar att V3c:s ärvda topprad är ett medvetet delat drag | Gatens 4/6-tröskel, som inte gäller cellen |

### Cellens eget underlag

| Fil | Gör | Tar | Lämnar |
|---|---|---|---|
| `tests/alunix-r8/PRODUCT.md` | Beviskassan: tre exempelsajter, tre paket med pris, en adress, listan över ordagrann copy, och § Absences | Hela § Absences som en avvisningslista, och listan över låst copy som gav § Copy-plan dess rättelse | Ingenting; filen är bindande i sin helhet |
| `tests/alunix-r8/concepts-V3c.md` | Arkitektens målbildsgrind: auktoritet, troplista, ett displayelement per skärm, registerrad, rörelse, färgstrategi, ribborna, rut-testet, F-007-kontrollen | Allt utom en sak | **En sak lämnas, och den redovisas:** § (1):s påstående att hero-rubriken är ~130 px vid 1440. `7rem`-taket i V3b binder vid 112 px. Se decision ledger, rättelse 3 |
| `tests/alunix-r8/runs/V3c/BRIEF.md` | Skelettet med sju låsta fält, decision ledger, personor, device-tabell, prestandaplan och ribbor | Alla låsta fält oförändrade | Ingenting rörs som inte var märkt `[fylls i R1]`, utom två tillägg som R1-prompten uttryckligen beställer (egen `select.py`-körning, författad tystnad) |
| `tests/alunix-r8/runs/V3c/assets/ASSETS.md` | Tio filer att kopiera in, tre att inte ärva med skäl, F-007-kontrollen, fyra vägar med rekommendation (d), och asset-lock per medieplats | Väg (d) som cellens beslut, och de fyra asset-lock-blocken oförändrade | Väg (a) och (c), som filen själv avråder från |
| `tests/alunix-r8/runs/V3c/assets/credits.json` | `generated_material.present: false`, åtta ärvda filer, tre `[needs: credits]`-rader | Att noll krediter spenderats och att det står skrivet | Ingenting; luckan i ursprunget är lead:s att fylla och gissas aldrig |
| `tests/alunix-r8/runs/V3c/NOTES.md` | Elva Fas 0-beslut med källa per rad | Beslutet att prestandaskulden tas i V3c och inte senare, och att byggaren kör `select.py` själv | Ingenting; byggarens rundanteckningar läggs till under `## R1` |

### Föregående cell och kedjans egen skill

| Fil | Gör | Tar | Lämnar |
|---|---|---|---|
| `tests/alunix-concepts-r5/cells/V3b-chain/index.html` (910 rader) | Den byggnad V3c itererar: kontinuerlig grund, två världar i två spalter, plåten med ljuspölen, ordscrubben, två live-ramar, prisliggaren | Grunden, spaltvärldarna, `--rail-x`-rastret, `--panel-pad-y`, de två hårlinjetokens per grund, ordscrubben, prisliggaren, iframe-regeln | `section.panel-open` och `section.panel-services` i sin helhet; `prefers-reduced-motion`-grenarna på fyra ställen (F-011); `reduced`-flaggan i skriptet; `will-change` på `.giant`; `--c-accent` på fokusringen och på `.thread-fill`; Google Fonts-länken; `__scFreezeMotion` som funktionspar; rå `--sc-p` i `paintHeroPool`, `paintMotion` och ordscrubben |
| `.../V3b-chain/shots/desktop-1440--fold.png` | Den byggda folden vid 1440x900, läst som pixlar | Bekräftar F-007-domen med egna ögon: plåtens övre band och högra tredjedel ligger på ren svart, ljuspölen är en mjuk kantlös ellips utan rak struktur, och logo-docken sitter på ett parti helt utan textur | Ingenting; bilden är belägget, inte en förebild |
| `~/.claude/skills/design/SKILL.md` | Kedjans dörr: hantverksgolvet, verbrutten, de fem stegen, exit-baren | Hantverksgolvet och F-011-raden i § Motion | Steg 2b:s bake-off (riktningen är låst), Tier 1-3 (cellen är Tier 0) |

### De fem live-rubrikerna, egen hämtning

Skelettets tabell är låst och ändras inte. Byggaren hämtade om alla fem 2026-09-10 och citerar
utfallet här som kontroll.

| # | Skelettets rad | Byggarens hämtning | Stämmer |
|---|---|---|---|
| 1 | `Webbyrå i Stockholm` | `Webbyrå i Stockholm` (frojd.se) | ja |
| 2 | `Limetta är en digitalbyrå` | `Limetta är en digitalbyrå` (limetta.se, satt över två rader) | ja |
| 3 | `Webbyrå i Kalmar och Stockholm` | `Webbyrå i Kalmar och Stockholm` (wilsoncreative.se/webbyra) | ja |
| 4 | `Webbdesign - vi gör inget lagom` | `Webbdesign - vi gör inget lagom` (digitalwebbyra.se/webbdesign) | ja |
| 5 | `Digitalbyrå / Webbyrå i Stockholm` | `Digitalbyrå / Webbyrå i Stockholm` (ead.se) | ja |

Fem av fem stämmer ordagrant. Ingen rubrik är fabricerad, ingen rad ändras, och sökningen
`digital byrå webbdesign Sverige` returnerade samma fem domäner som arkitektens.

### Byggarens rader, R9

Sju fixplaner (035, 036, 037, 039, 040, 038, 041) utförda i README-ordning. Fullständig
verdikt per plan i `NOTES.md § R9`. Raderna nedan är exekveringsfynd arkitektens rader inte
(och inte kunde) förutse — tre genuina buggar hittade och fixade under bygget, en genuin
motorbunden gräns dokumenterad.

| Area | Decision | Source | Source rule | Why |
|---|---|---|---|---|
| **035, revealens sampler** | `latchTick`/`kickLatch` byggda exakt enligt Target; `R.fig`-identitet löst per tick (aldrig cachat `R.act`) | Plan 035 Target + Astra loop 3 fix 1 | Plan 035 | Åtta av åtta scrollmetoder (hjul/PageDown/`scrollTo`/smooth `scrollTo`) landar nu `--rv=1`; R8 lämnade `scrollTo`-metoderna på 0/0 |
| **036, transformreceptet och `--rv-s`-geometrin** | Hōrais iris byggd som en kvadrat (`measureFrames()`, mätt en gång vid mount/load/resize) i stället för `.rv{inset:0}`: en icke-kvadratisk box med `border-radius:50%` ger en ellips, inte R8:s cirkel | Egen geometrisk härledning (`sqrt(w²+h²)`-formeln CSS `calc()` inte kan uttrycka utan container query-enheter) + pixelkontroll | Plan 036 Target, egen tolkning av "Skriv den valda geometrin i NOTES" | `--rv-s` uppmätt (1305,8px vid 1440) matchar den analytiska formeln exakt; pixelkontroll bekräftar en genuint cirkulär iris och pixelidentisk position vid `--rv=1` |
| **036, `.rv`-regressionen i sömn/vakna-kontraktet** | `f.parentNode` (använd av `mountFrame`s `is-asleep`-sättning och `io.observe()`) bytt till `f.closest('.frame-wrap')` på båda ställena | Egen sömn/vakna-kontroll (`at_bottom asleep` visade `[False,False]`, skulle vara `[True,True]`) | Plan 027/036, "observern på wrappern" | `.rv` lades mellan ramen och wrappern (plan 036 A); `f.parentNode` pekade därmed plötsligt på `.rv` i stället för `.frame-wrap`, en tyst regression i 026/027:s redan verifierade kontrakt |
| **037, tre lager i `aimPreview`** | En självrättande settle-slinga (rAF, upp till 20 försök) + ett generations-ID (`aimGen`, förhindrar tre samtidiga anrop från skript/load/fonts.ready att race:a varandra) + `overflow-anchor:none` (defeat:ar webbläsarens egen scroll anchoring) | Egen iterativ mätning: ett fast antal extra rAF löste 1440 steg 1 men FÖRSTÖRDE 390 steg 3 (redan rätt) | Plan 037 Target (grundidén), egen utökning | Racet mellan de tre triggerna var instabilt, inte en fast bildrutefördröjning; en debouncad `scroll`-lyssnare krävdes för att upptäcka sen scroll anchoring EFTER att slingan redan konvergerat |
| **037, mobilgränsen lämnad, inte forcerad** | 390 steg 02 (`ps=0,2753` mot `e=0,3311`) lämnad som best-effort; `window.ScrollCraft.instances[0]` inte använt för att tvinga motorns `layout()` | Rotorsak funnen i `scrollcraft.js` rad 1186 (`isMobile()`-resize-guard) | Motorns egen kod, aldrig redigerad; `instances`-API dokumenterat "inte ett API för sidan" | En syntetisk resize-dispatch gör ingenting på mobil (`isMobile()` sant + `innerWidth` oförändrat); att kringgå med `instances[0].layout()` hade brutit den dokumenterade gränsen för det API:t |
| **039, `is-turning`/`setFace`/`data-on` flyttade till `latchTick`** | Läser `heroAct.cur`/`procAct.cur` (shimens lerpade värde) i stället för rå scrollY/`processPs()` för av-villkoret | Astra loop 3 fix 2, 3, verifierade mot filen | Plan 039 Target | Kortsidans synk nu ±1 bildruta (mätt); `data-on` ritar baklänges kontinuerligt (max_step 0,032%) i stället för att klippas till `display:none` vid ett PageUp-hopp |
| **039, `findAct`-optimeringen** | `acts.filter(function(a){...})[0]` (fyra separata anrop/tick, varje allokerar en array+stängning) bytt till en delad `findAct(acts, el)` (vanlig for-loop) | Egen `motion_probe`-mätning: p95 70,6 ms → 58,6 ms genom heron | — | En genuin, mätt regression från den nya per-bildruta-arkitekturen (delad med 035); optimeringen minskade men eliminerade inte gapet mot R8:s 36 ms — kvarstår som best-effort, talen skrivna |
| **041, `--c-paper` i stället för `--bg`** | Tredje driftstoppet läst ur `--c-paper` (`#f4f2ee`), inte `--bg` (`#fdfbf4`, en annan färg) | Egen jämförelse mot det hårdkodade värdet i det borttagna `data-sc-drift="#f4f2ee"` | Plan 041 Target, egen rättelse av en namngivningsinkonsekvens i planens prosa | Planens text namngav `--bg` men citerade hexvärdet `#f4f2ee`, som faktiskt är `--c-paper`s värde; `--c-paper` är den token som ger samma resultat som R8:s hårdkodade attribut |
| **041, växlingsvillkoret `if (t < 1)` i stället för `if (g > 0)`** | Driften prioriterar tesens egen övergång tills den är KLAR (`t>=1`), byter först då till jättens | Rotorsak funnen i `scrollcraft.js` rad 972-984 (motorns egen "background drift"-loop, DOM-ordning, första ofärdiga målet vinner) | Plan 041 Target (egen bugfix i den föreslagna koden) | Planens egen `if (g > 0)` bytte till pappersblandningen nästan direkt (jätten börjar 108px efter tesen); tesens blå ton visades ALDRIG. Efter fixen: pixel för pixel identiskt med plan 038:s redan verifierade tal |

### Fynd, dokumenterade men inte lösta i R9 (arkitektens att döma)

| Fynd | Var upptäckt | Detalj |
|---|---|---|
| **`scrollcraft.js`s mobila `isMobile()`-resize-guard blockerar en syntetisk `dispatchEvent('resize')` från att trigga motorns egen `layout()`** | Plan 037:s felsökning (390 steg 02) | Rad 1186: `if (innerWidth === lastW && isMobile()) { vh = innerHeight; return; }`. Gäller varje sida som förlitar sig på en synkron resize-dispatch för att tvinga motorn att mäta om `#process`-liknande akter på mobil efter en sen layoutförskjutning — inte unikt för denna cell |
| **`#giant-section`s egen, utanför-R9 rapporterade skala 0,92→1** | Plan 036 B:s jättefönstermätning (106,6 ms median, inte det uttalade ≤60 ms-målet) | README § "Utanför R9" listar detta redan som en känd, oplanerad kostnad; delar troligen samma mätfönster som B:s egen förmonteringsvinst |
| **Sidvikt (grov jämförelse mot R8:s 462 081 B, inte omätt i denna grind)** | — | `perf_probe.py` i R9-grinden visade 476 kB vid båda breddarna — +14 kB sedan R8, rimligt givet sju planers nya JS/CSS (särskilt 036:s `.rv`-geometri och 041:s `driftColor()`) |

### Byggarens rader, R10

Tre fixplaner (042, 043, 044) utförda i README-ordning. Fullständig verdikt per plan i
`NOTES.md § R10`.

| Area | Decision | Source | Source rule | Why |
|---|---|---|---|---|
| **042, prisblocket utan platshållare** | `content-visibility:auto` och `contain-intrinsic-size:auto 760px` borttagna från `.price`; dokumenthöjden konstant från load (10 582 / 11 326 px), motorns akttoppar matchar DOM:en utan något resize | Plan 042 Target, egen mätning (`docH`, `engTop`/`realTop`, `--sc-p`) | Plan 042 | Platshållaren var 297px (1440) / 262px (390) högre än blockets verkliga innehåll; sidan krympte första gången blocket målades, och motorns cachade akttoppar för `#process`/`#principer`/`footer.close` stod kvar fel tills ett riktigt resize-event, som en mobil läsare aldrig utlöser |
| **042, 390-previews löst** | `?preview=process-01..07` formas nu 21/21 (tre laddningar var) vid 390, mot R9:s dokumenterade 1-av-3-race | Egen mätning (`preview390.py`-metoden) | — | R9 (plan 037) skrev racet som en motorbunden gräns (`isMobile()`-resize-vakten); den verkliga orsaken var prisplatshållarens geometrisnedvridning, inte motorn. Löst av samma rad som fixar H-15/H-30 |
| **042, prestandasiffrorna kräver sammanflätad A/B** | Den officiella före/efter-mätningen (icke-sammanflätade 3-körningar, separata processtarter) visade AVIGT resultat (regression); en sammanflätad A/B (återinjicerad gammal regel vs borttagen, omväxlande i samma session, kontrollsida mätt samtidigt) visade planens egen förväntade riktning (jättefönstret tydligt bättre, prisfönstret tvetydigt inom projektets egna ±50%-brusnivå) | Egen utredning efter ett oväntat mätresultat | — | Separata `motion_probe_ab.py`-anrop startar en NY webbläsarprocess varje gång, vilket introducerar maskinlaststörningar mellan mätningarna som en sammanflätad, samma-sessions-A/B kringgår. Kontrollsidan (`tests/motion/smooth.html`, 18,3 ms/0 rutor) bekräftade att maskinen själv inte var upptagen — bruset satt i metoden |
| **043, Calyx-öppningen: transformriktningen vänd, `overflow:clip` på `.rv`** | `.calyx-wrap .rv` fick `overflow:clip`; boxens transform bytte tecken (`(var(--rv)-1)*100%`) och ramens likaså (`(1-var(--rv))*100%`), så öppningen kommer uppifrån i stället för att vara ett no-op | Plan 043 Target, egen pixelkontroll (bgFraction 100/74,9/50/0,1% vid rv 0/0,25/0,5/1) | Plan 043 | R9:s recept saknade `overflow:clip` på `.rv` helt, så wrapperns egen (stillastående) `overflow:clip` aldrig fick något att klippa mot — ramen stod alltid på wrapperns topp oavsett `--rv`. Astra loop 4 hittade detta oberoende (fix 2), arkitekten verifierade det, planen fixar det |
| **044, driftens handoff räknas från överlämningspunkten** | `driftHand` (jättens råa progress när tesens `t` når exakt 1) läggs till i `measureAct()`; leg 2 räknar `smooth((g − driftHand)/0,35)` i stället för rå `g` | Plan 044 Target, egen 20px-stegs svepning (max_step 30/22 vid 1440, 25 vid 390, alla under 40-baren) | Plan 044 | Jätten börjar bara 108px efter tesen, så dess råa progress `g` var redan långt in i sin egen `smooth(g/0,35)`-kurva (ofta redan mättad vid k=1) i samma ögonblick tesen blev klar — färgen hoppade blått till papper i ett enda 20px-scrollsteg i stället för att tona kontinuerligt |

### Fynd, dokumenterade men inte lösta i R10 (arkitektens att döma)

| Fynd | Var upptäckt | Detalj |
|---|---|---|
| **Icke-sammanflätade `motion_probe_ab.py`-körningar över separata processtarter kan visa en missvisande riktning** | Plan 042:s prestandamätning | Varje `motion_probe_ab.py`-anrop startar en ny Chromium-process; mätt (042) att detta introducerar tillräcklig brusvariation för att dölja eller invertera en verklig, mindre skillnad. En sammanflätad A/B i samma session, med en kontrollsida mätt parallellt, är den tillförlitliga metoden — värt att bära vidare till framtida rundors egna prestandamätningar, inte bara denna cells |
| **`#giant-section`s egen, utanför-R10 rapporterade skala 0,92→1 (ärvt från R9)** | Oförändrat | README § "Utanför R10" (implicit, samma post som R9:s "Utanför R9") — ingen R10-plan rör detta |

### Byggarens rader, R11

Plan 045 (Antons beställning, inte ett fynd). Fullständig verdikt i `NOTES.md § R11`.

| Area | Decision | Source | Source rule | Why |
|---|---|---|---|---|
| **`?process=invert` som ett läge i samma fil, aldrig en andra cell** | `data-process="invert"` satt på `:root` via en fristående URL-parameter; ett additivt CSS-block (efter `.principles`) skriver om fyra tokens (`--bg`/`--ink`/`--c-line-on-paper`/`--c-accent`) plus `--hair-ink` inom `#process`/`.principles`s eget scope; en JS-rad i `?preview=`-blocket. Pappersläget bevisligen byte-identiskt (renderidentitet `getComputedStyle` på tolv selektorer, `identical: True`; filen tillfälligt återställd till R10:s exakta md5 `d3491b4a` för en sann före/efter-mätning på samma fil) | Plan 045 Target, egen renderidentitetskontroll | Plan 045, planens egen hårdaste gräns ("ingen befintlig rad redigeras") | Registret är redan byggt på fyra tokens (`.contour`/`.measure`/`.ledger` läser `--ink`/`--hair-ink`/`--c-accent`/`--c-line-on-paper`), så att skriva om dem villkorat på en attributselektor vänder hela aktens ritregister utan att röra en enda befintlig rad — Anton kan jämföra samma sida i två lägen, inte två sidor |
| **`--c-accent-on-dark:#3286d8`** | Samma hue/mättnad som `--c-accent` (#1e5e9c, HSL H 0,582 S 0,677), ljushet höjd från L 0,365 till L 0,52 | Egen mätning (colorsys HSL-sökning + WCAG-formel) | Plan 045 villkor c, gate 48 (token, aldrig inline-hex), gate 60 | `--c-accent` mäter 2,93:1 mot `--c-black` (dokumenterat i R1 rättelse 2) — underkänt för `.measure`s siffror i invert-läget. Samma hue/mättnad höjd tills kontrasten nådde 5,16:1, en komfortabel marginal över 4,5:1-golvet (den exakta gränsen, L 0,485, låg för nära kanten för säkert bruk) |
| **`.ledger-num`-scopet utökat till `#process, .principles`** | Genuin bugg hittad under bygget: `#process` återanvänder `.ledger-num`-klassen för sina egna sju stegnummer (01-07), vilket planens ursprungliga `.principles .ledger-num`-selektor missade — kontrasten mätte 1,06:1 innan fixen | Egen `contrast_over_media.py`-körning, upptäckte felet direkt | Plan 045:s egen "additivt block, ingen befintlig rad redigeras"-gräns höll (fixen är en utökning av MITT EGET nya block, rör ingen tidigare rad) | Samma klassnamn återanvänds i två olika delar av sidan (`#process`s stegnummer och `#giant-section`s tjänsteliggare, den senare korrekt utanför scope) — en enda selektor som antog EN användning täckte inte den andra |

### Fynd, dokumenterade men inte lösta i R11

| Fynd | Var upptäckt | Detalj |
|---|---|---|
| **Δ L vid pris→process-seamen (12,0 mätt) skiljer sig från planens egen uppskattning (≈19)** | Egen H-11-metodmätning | Riktningen och slutsatsen (`--c-black` behåller seamen, `--c-graphite` skulle tappa den helt) står orörda; troligen olika samplingspunkter i grunden mellan planens egen skattning och denna mätning. Värt att notera för Anton om han vill se exakta pixelpositioner innan han väljer |
| **Antons dom väntar** | — | Byggaren levererar två jämförbara lägen, mätta och skärmbildade parvis i `shots/r11/papper/` och `shots/r11/invert/`. Väljer Anton inverteringen är grundväxlingen (tesbandet, prisblocket, avslutet, per villkor d) en egen plan i en framtida runda, per plan 045s egen text |

### Byggarens rader, R12

Plan 046 (Antons beställning, inte ett fynd). Fullständig verdikt i `NOTES.md § R12`.

| Area | Decision | Source | Source rule | Why |
|---|---|---|---|---|
| **Calyx får sin färg vid `--k6`, Target A byggd (inte Target B)** | `<image id="p-live-img">`s `href` bytt till `assets/demo-calyx-1440-color.webp`; `.process-sheet .p-live`s `filter` bytt till `grayscale(calc(1 - var(--k6))) contrast(1.05)`. Två `Edit`, ingen ny DOM, ingen `@property` | Plan 046 Target A, egen sammanflätad A/B (3 par, två fönster, cpu 1) | Plan 046, kostnadsgränsen 5 ms p95 | A översteg B med −0,1 ms (steg 06) och −0,2 ms (steg 05, kontrollfönstret) — inom brus, ingenstans nära 5 ms-gränsen. `max_step` ≤3 %/staircase 0 i alla tolv körningar. Planens egen förutsägelse (A billigare eftersom B skulle lägga en andra rasterkomposition i steg 05:s redan upptagna `clip-path`-fönster) höll vid mätning |
| **Invert-lägets dämpning: `brightness(0.6)`, ingen `saturate()`** | Tillagd i mitt eget additiva block från plan 045 (`:root[data-process="invert"] .process-sheet .p-live`), rör ingen tidigare rad | Egen binärsökning mot målvärdet (mean ≤0,34, p95 ≤0,80, BÅDA bredderna) | Plan 046, "det minsta som får texten att behålla skärmen", 0,34 som tak, inte mål | `brightness(0,62)` klarade 1440 (mean 0,338) men inte 390 (mean 0,3403); 0,6 klarar båda (1440: 0,326/0,577; 390: 0,330/0,577) med marginal. `saturate()` prövades onödig — bilden läste lugn, inte skrikig, mot `--c-black` vid 0,6, granskad i pixlarna |
| **`scroll_verify.py` kunde inte köras; ersatt av likvärdig täckning från andra verktyg** | Fyra försök (tre protokollfel, en hängning stoppad efter ~19 min); en ren sanity-check med samma Chrome/server lyckades, så felet är skriptets egen ~35-bildrutorloop mot en 10 534 px-sida under detta maskintillstånd, inte koden | Egen felsökning | Step 5:s fallback-kedja ("om fångst genuint är omöjlig, säg det uttryckligen") | `motion_probe` (staircase 0 på `--sc-ps`), `reflow.py` (0 unrevealed) och `contrast_over_media` (PASS båda lägena vid steg 06:s scrollposition) täcker samma sak scroll_verify skulle mätt (dead scroll, unrevealed-räkning, kontrast under media) — `blankBands` och en helsides cue-svep mättes inte separat, skrivet öppet i NOTES i stället för att antas passerat |

### Fynd, dokumenterade men inte lösta i R12

| Fynd | Var upptäckt | Detalj |
|---|---|---|
| **Tolvramssekvensens pixelbaserade chroma-mätning visar 20,7-21,0 % värsta steg (gräns 20 %), medan den drivande `--k6`-kurvan själv mäter 19,2 %** | Egen dubbelmätning (pixelchroma + extraherad `--sc-ps`-kurva ur `calc()`-texten) | Chroma är olinjär i gråskale-mixfraktionen och tolv jämna steg över 800 px lägger bara ~5 av dem inne i det verkliga ~380 px-övergångsfönstret; den underliggande övergången är bevisat kontinuerlig (`staircase 0`). En finare samplingsgrid (fler ramar, eller ett fönster som matchar `[s6,e6]` exakt) skulle sannolikt föra pixelmåttet under 20 % också — inte gjort denna runda |
| **`preflight_taste`s `cta-radbrytning`-fynd på `a.topline-contact`/`a.card-cta`** | Mekanisk körning i R12:s grind | Utanför R12:s scope (ingen markup/copy i sidhuvud eller CTA rörd av plan 046); troligen pre-existing sedan tidigare rundor, samma mönster som den återkommande `overused-font: Geist`-flaggan i R9-R11 |

### Byggarens rader, R13

Ett fel, en plan (047), hittat av lead i exit-granskningens pixlar (inte arkitekten, inte
Anton). Fullständig verdikt i `NOTES.md § R13`.

| Area | Decision | Source | Source rule | Why |
|---|---|---|---|---|
| **`.process-steps` får `.process-stick`s eget `width`/`justify-self`, ordagrant** | En `Edit` i `@media (max-width:1279px)`: `.process-steps{width:min(100%,480px,calc((100svh - 224px) * 320 / 360));justify-self:center;}`, direkt efter `.process-stick` | Plan 047 Target, egen 147-par-per-läge sweep (7 bredder × 3 scrollpositioner × 7 steg) | Plan 047, lead 2026-09-17 | Arket (480px, centrerat) och listan (full kolumnbredd, vänsterjusterad) delade grid-rad men inte bredd: 230px horisontellt överlapp vid 768px gjorde att text stack ut på båda sidor om arkets ogenomskinliga grund och klipptes mitt i ordet mellan 640 och 1279px. Samma bredduttryck som arket redan bär eliminerar glappet vid varje viewport-höjd, inklusive kortviewport-tredjetermen |
| **Verifieringens "noll överlapp" tolkad som "inget PARTIELLT överlapp", inte "inget överlapp"** | Full containment (`li` helt innanför `stick`s x-spann) eller nollöverlapp räknas som SÄKERT; fel bara när `li` sticker ut förbi `stick`s vänster/högerkant MED samtidigt vertikalt överlapp | Egen mätning: en ordagrann "0 överlapp >4px i båda dimensionerna"-tolkning gav 10 falska träffar, alla med `hx=480,0` (full breddmatchning) | Egen precisering av planens egen verifieringstext | Arket är avsett att täcka texten som passerar (samma mönster som redan gällde vid 320/414 före denna plan) — total täckning är success, inte en bugg. Den riktiga defekten (text som sticker ut förbi arkets kant) mättes separat och gav 0 fel i båda lägena |
| **Kritikerns fix 2 bedöms täckt; fix 3 lämnas öppen** | Ingen ytterligare kod ändrad utöver plan 047:s enda `Edit` | Egen läsning av `NOTES.md § Exit-granskningen` mot plan 047:s uppmätta resultat | Plan 047:s Boundary ("Rör inte SVG:ns planschgeometri") | Fix 2 ("styckets kanter mot arket i samma media query") delar rotorsak med 768-felet och är löst av samma regel. Fix 3 (`16:9`-ledaren skär en glyf vid 1024px) kräver att röra SVG-planschgeometrin, uttryckligen utanför denna plans Boundaries — kvarstår öppen |

### Fynd, dokumenterade men inte lösta i R13

| Fynd | Var upptäckt | Detalj |
|---|---|---|
| **Vertikal linjegränsartefakt: en textrads överkant klipps där den råkar korsa arkets nederkant** | Egen skärmbildsläsning vid 1024px ("webbläsare, på er telefon...") | Inneboende i sticky-ark-över-passerande-text-mönstret (radhöjden align:ar sällan exakt med arkets pixel-nedre-kant); bekräftat identisk i en återställd kontrollkörning på R12-läget, alltså orört av plan 047. Vertikal, inte horisontell — utanför denna plans scope (bara bredd/centrering) |
| **`scroll_verify`s `deadScroll`/`blankBands` vid processaktens slutläge och hjältens öppning** | Egen körning vid 768 och 1440 | Bekräftat pre-existing (samma mönster på den återställda R12-filen); sannolik orsak är `--kN`s egen klamring efter steg 07:s fönster (plan 046:s dokumenterade, avsedda beteende) och hjältens statiska öppningsskärm — ingendera rörd av plan 047 |
| **Kritikerns fix 3 (`16:9`-ledaren skär en glyf vid 1024px) och fix 4 (decision ledger-talet, R1)** | `NOTES.md § Exit-granskningen`, ej byggarens egen mätning denna runda | Fix 3 kräver SVG-planschgeometri, uttryckligen utanför plan 047:s Boundaries. Fix 4 är journalföring (R1:s decision ledger, hero renderar 115,2px vid 1440 inte 120, kvot 0,700 inte 0,67), inte pixlar — ingen kodändring väntad |

### Byggarens rader, V3d R1

Plan 048, den inverterade varianten. Fullständig verdikt i `NOTES.md § V3d R1`.

| Area | Decision | Source | Source rule | Why |
|---|---|---|---|---|
| **`--c-drafting`** | `oklch(0.21 0.022 250)` (kall blåsvart, chroma 0,022) som `#process`s enda grund, aldrig `--c-black` eller `--c-graphite` | Plan 048 § Tokens, C | Gate 48 (token i `:root`, inga inline-hex) | Ett tredje mörkt material bredvid fotot och jättens svarta plåt (`--c-black`); samma hue/lightness-familj som `--c-accent-deep` men egen chroma så den aldrig läses som en andra accent. Mätt: `--c-paper` 15,8:1, `--c-accent-on-dark` 4,67:1 mot den |
| **`--scrim-close`** | `color-mix(in srgb, var(--c-black) 64%, transparent)`, vänsterjusterad gradient på skrivbord, heltäckande under 767px | Plan 048 § Tokens, A | Gate "type over media only on a plate or scrim" | Priset och adressen står på samma fotografiska grund som resten av avslutet (`.ground`); scrimmen bär kontrasten i stället för en egen ogenomskinlig yta. Uppmätt: brödtext 15,2–19,3:1, adress 17,2–18,4:1, båda bredder |
| **Kameran (`#p-cam`, `--cam`)** | `translate(-93px*cam,0) scale(1+0.5*cam)` på en `<g>` som omsluter allt utom `#p-frame`; `--cam = 0,35*k5 + 0,65*k6` | Plan 048 § Steps E9 | Ramen (`#p-frame`) skalas aldrig, bara innehållet | Öppningen går från 52 % av arket (steg 05, delvis inzoomad) till 84 % (steg 06–07, `--cam`≈1) utan att arkets egen ram (`p-outline`) rör sig — samma teknik som mattis-greppets bleed, fast på en kamera i stället för ett objekt |
| **Bandet (`.step-band`, sticky-ticker)** | Varje `<li>` bär sitt eget `position:sticky;top:0` band; `--band-h` mätt (`max(.step-band.scrollHeight)`), skriven på `#process` FÖRE li-rektanglarna läses | Plan 048 § Steps F13/F16 | Rullande scroll, pixelbunden, ingen JS per bildruta | Ticker-effekten (band N ut, band N+1 in) uppstår av den rena CSS-mekaniken, inte av script; verifierat med `motion_probe` (`staircase 0` i båda riktningar, cpu 1 och 4) |
| **Calyx sticky (`.calyx-fig`)** | `position:sticky;top:clamp(24px,5svh,48px)` ersätter `flex:1`; `position:static` under 900px | Plan 048 § Steps G17 | PRODUCT.md: en visad ram transformeras eller tonas aldrig — sticky är ingen transform | Priset lämnade ett hål på 729 px i vänsterspalten när det flyttades till avslutet; Calyx som håller kvar sin egen höjd (849 px) genom hela högerspaltens (jätten + Hōrai) passage fyller det utan ny yta eller ny text |
| **Principerna på papper (`.principles`)** | `#process` inverteras (C), `.principles` rörs INTE av samma tokenbyte; blir i stället en tvåspaltig grid ≥900 med kickern i displaystorlek vänster | Plan 048 § Steps C6 + G18 | Plan 048 § Beslut G punkt 2 | Med processen mörk och jätten svart är "Hur vi tänker" den enda kvarvarande helbredda ljusa ytan mellan heron och avslutets foto; tre material i följd (foto → mörkt → papper → foto) i stället för fyra mörka i rad |
| **Adressens storlek (`.close-mailto`)** | `clamp(1.75rem,3.2vw,3rem)` (46,1 px vid 1440, 28 px vid ≤768) ersätter `clamp(2rem,6vw,6rem)` (86,4 px) | Plan 048 § Steps B5 | Hoy/insign-referensernas kapitelrubrik- resp. frågestorlek | Adressen är en handling, inte en rubrik: den tar kapitelrubrikens storlek och lämnar displayskalan åt `Alla har rätt till bra design.` (kvot 1,9 mot statement vid 1440) |

**Två byggfel hittade och lagade i samma runda (inte plan-avvikelser — planens egna CSS-rader krävde en motsvarande reset i mobil-mediet som saknades i första passet):**

| Fel | Fix | Mätt |
|---|---|---|
| `.process-stick` ärvde skrivbordsregelns `height:calc(100svh - var(--band-h))` under 767px (`--band-h` har ett CSS-fallback, så uttrycket blev aldrig ogiltigt) — arket fick 641 px hög behållare för en 322 px hög SVG, ett dött tomrum på ~320 px per steg | `height:auto` tillagt i `@media(max-width:767px)` | Före: `stickHeight` 641,4 px. Efter: 301,9 px (matchar `--sheet-h`) |
| `.process-stick` ärvde skrivbordsregelns `padding-inline:var(--rail-x)` (23,4 px per sida) eftersom mobil-regeln bara nollade `padding-block` | `padding:12px 0` (fullständig reset) i samma media-block; `.process-sheet` fick uttrycklig `width:100%;max-width:none` (ärvde annars skrivbordets höjdbaserade calc-formel) | Före: arket 296,4 px (76 % vw). Efter: 343,2 px (88 % vw, matchar `.process-stick`s egen bredd fullt ut) |

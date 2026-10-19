fix

## persistence

Allt underlag läst i den här körningen, mot den här builden, på den här värden. Server:
`serve.py` på 127.0.0.1:3321 (svarar 200 på cellens URL), aldrig `python -m http.server`.

**Lästa indata:** `skills/design/references/performance.md` (§ 1 budget, gate 93, § 6 Never),
`skills/design/references/motion-smoothness.md` (`--sc-ps`-kontraktet, ribban),
`skills/impeccable/reference/optimize.md` § NEVER, `tests/alunix-r8/runs/V3c/BRIEF.md`
(inkl. § Prestandaplan, § Device-tabell, § `?preview=`-plan), målbilden
`tests/alunix-r8/malbilder/V3c.md`, källan `runs/V3c/index.html` (979 rader),
`runs/V3c/scroll/scrollcraft.js` och `sc-smooth.js`. Bilder lästa som bilder:
`shots/r3/contact-1440.png`, `preview-mid.png`, `fold-375.png`, samt varje sparkline jag
själv skrev (`frame-times.png`, `track-0.png`, `track-1.png` i tre körningar).

**Kontrollfixturen kördes omedelbart före varje sidmätning** (`tests/motion/smooth.html`,
cpu 1, spår `#act:--sc-ps` och `#card:transform`): p95 16,8 ms, 0 rutor > 33 ms, max_step
1,37 %, staircase 0 — fyra gånger, identiskt. Fönstret var tyst hela sessionen. Proben är
dessutom bevisad i BÅDA riktningarna på den här värden vid cpu 4 denna körning:
`smooth.html` PASS (16,8 ms, 0 > 33), `staircase.html` FAIL (staircase 18, max_step 5,56 %,
p95 16,7 ms). Ingen mätning nedan är uppskattad; rått `--sc-p` spårades aldrig.

| Körning | cpu | wheel | exit | utdata |
|---|---|---|---|---|
| `motion_probe` snabb | 4 | 100:60 | 1 | `shots/r3/rev-motion-fast/` |
| `motion_probe` snabb, omkörning | 4 | 100:60 | 1 | scratchpad |
| `motion_probe` långsam (Edge) | 4 | 20:120 | 1 | `shots/r3/rev-motion-slow/` |
| `motion_probe` enbart heron, 15 tick | 4 | 100:60 | 1 | `shots/r3/rev-motion-hero15/` |
| `motion_probe` ledens kadens | 1 | 100:60 | 1 | `shots/r3/rev-motion-cpu1/` |
| `motion_probe` nedströmsspår | 4 | 100:60, 70 tick | 1 | `shots/r3/rev-motion-downstream/` |
| `perf_probe` 1440x900 | 4 | — | 1 | `shots/r3/rev-perf-1440/perf_probe.json` |
| `perf_probe` 390x844 | 4 | — | 1 | `shots/r3/rev-perf-390/perf_probe.json` |
| `perf_probe` calyx, horai, V3b-chain | 4 | — | 1 | attributionsmätning, stdout |

**Ledens tal, verifierat och motsagt.** Vid cpu 1 mäter jag `section.hero:--sc-ps` p95
**37,5 ms, 49 rutor > 33 ms, max_step 3,67 %, staircase 0** — samma dom som ledens
33,4 / 36 / 3,38 / 0, marginellt sämre. Men ribban är 4x CPU, och där mäter samma akt
**p95 133,3-144,2 ms med 74-109 rutor > 33 ms** (två körningar). Ledens siffra är alltså
inte fel, den är omätt vid rätt strypning: ett cpu-1-tal citerat mot en cpu-4-ribba.

**Attribution, mätt var för sig på samma server och samma strypning.** Cellens egen markup
innehåller noll Unsplash- och noll Google Fonts-referenser (enda träffen är ordet i en
kommentar, rad 22). `/sites/calyx.html` ensam = 1 514 773 B, 3 typsnittsfiler, hotlänkad
hero 1 122 865 B. `/sites/horai.html` ensam = 3 044 543 B, 13 typsnittsfiler / 590 864 B,
hotlänkad hero 673 953 B. Sidan vid 1440 = 4 893 258 B, vid 390 = 3 378 379 B. Differensen
är **334 kB vid båda viewporterna** (333 942 B resp. 333 836 B) — det är cellens hela egen
vikt, 13 % av budgetens 2,5 MB, med 3 typsnittsfiler / 37 792 B och en egen hero på 65 kB
WebP med `width`, `height`, `decoding="async"` och `fetchpriority="high"`. `perf_probe`s
`transfer`, `font-files`, `font-bytes` och `hero-image` är därmed **ärvd skuld ur de
inbäddade exempelsajterna**, inte cellens, och står inte i `material_fixes`.

## fidelity

Signaturakten mot målbilden (`malbilder/V3c.md` § Kortet, § Koreografin), akt för akt, mätt
vid 1440x900, cpu 4, kontrollen ren.

| Akt (målbild) | Mätt i den här builden | Dom |
|---|---|---|
| ps 0-0,12: kortet stilla, ljuspölen vandrar | `#heroPoolImg:transform` lever: max_step 3,51 %, staircase 0, ingen DEAD | Håller |
| ps 0,12-0,72: vändningen på `--sc-ps` | `#plateCard:transform` max_step 4,30-4,52 %, staircase 0; `--flip` räknas i ren CSS ur `--sc-ps`, rått `--sc-p` driver ingenting i källan | Håller i värdet (härlett spår: rapporteras, gatear inte, Q22) |
| ps = 0,5: bara hårlinjen | `preview-mid.png` läst som bild: en enda lodrät hårlinje, ingen platta, ingen ram | Håller, mattis-ribban är slagen |
| ps 0,72-1: baksidan landar, dwell | Heron mäter 1980 px = 2,20 vh, ps når 1 vid y = 1150, dwell därefter | Håller |
| Rubrik och underrad utan transform genom akten | Bekräftat i källan och i `track-0.png` (ren ramp, inga hack) | Håller |
| s4: Hyperborea-plåten bryter sin kant på `--sc-ps` (§ Device-tabell rad 3) | `.thesis-figure` har KONSTANT `matrix(1,0,0,1,33.3111,0)` vid varje mätt scrollposition 0-3000 px; `?preview=bleed` skrollar bara dit. `motion_probe` rapporterar spåret DEAD | **Defekt.** Akten renderar men rör sig inte; device-tabellen lovar en `--sc-ps`-driven bleed |

**Två DEAD-utslag är probens blindfläck, inte sidans fel, och ska smalnas av i stället för
att waivas:** `.giant:transform` och `#threadFill:transform` rapporteras DEAD, men lästa
direkt lever båda (`.giant` skalar 0,92 -> 0,9913 över y 0-2700; `#threadFill` går
`scaleY` 0 -> 1). `motion_probe` dekomponerar bara rotation och translation, så ett spår som
enbart skalar läser som dött. Enbart `.thesis-figure` är genuint stilla.

Rörelsens *klocka* är däremot en avvikelse från prestandaplanens egna målvärden (frame p95
<= 20 ms, noll frames > 33 ms, båda scrollriktningarna): nedåt 133-144 ms p95, uppåt 66,8 ms
p95 med 64 rutor > 33 ms och en enskild ruta på 1 716 ms. Sparklinen skiljer de två felen åt
precis som `motion-smoothness.md` säger att den ska: `track-0.png` är en jämn ramp utan hack
(**staircase 0 i varenda körning**, värdet stegar inte), medan `frame-times.png` visar en
platt kurva med en enorm spikklunga. Det är Fault 2, inte Fault 1: sidan är genuint
långsam, den stegar inte.

Vid 390 tillkommer ett fel som inte syns vid 1440: **CLS 1,038** mot budgetens 0,05, två
skift, 0,285 vid 225 ms och 0,753 vid 324 ms, med källorna `figure.hero-plate`,
`img#heroPoolImg`, `div.stagger`, `svg` respektive `div.col.col-left`, `span`. Med
typsnitten blockerade: 1,0355. Med bilderna blockerade: 1,0383. Alltså varken swap eller
bilddekod — det är hero-stagens höjd som ändras när motorn monterar pinnen. Samma sida vid
1440 mäter 0,003.

Två mindre driv mot BRIEF:en, ingen av dem blockerande: dokumentet mäter 4 378 px = 4,86 vh
vid 1440 (§ Motion-tes säger "sidans 9-11 vh"), och hero-bilden ligger på
`/tests/alunix-concepts-r3/build/assets/` i stället för prestandaplanens `assets/` — samma
origin, alltså ingen Step 5b-överträdelse, bara ovendorad i cellen.

## ceiling

- **`V3b-chain` (primary, låst)** — `slår`. Mätt i dag, samma värd, samma cpu 4: V3b ger p95
  175,1 ms, 84 rutor > 33 ms, **staircase 9**, max_step 11,79 %, LCP 1 000 ms, 4 vilande
  `will-change`, hero utan `fetchpriority`, `<img>` utan `width`/`height`. V3c: staircase 0,
  max_step 3,5 %, LCP 208 ms, noll vilande `will-change`, egen vikt 334 kB. V3c slår sin
  primärreferens på varje post cellen själv äger, och ärver dess enda kvarvarande skuld
  (de inbäddade sajterna) oförändrad.
- **`oryzo-ai` (borrow: objektet som vrider sig i tomrummet)** — `står sig bredvid`. Ingen
  körbar build finns i katalogen (`entries/oryzo-ai/` är `fold.webp`, `shot.png`, `slices/`,
  statiska fångster), så dess bildrutetid går inte att mäta och jag påstår ingen. Det som
  går att läsa i mitt fack är att dess scroll-länkade fjädring bärs av ett enda objekt;
  V3c bär sitt objekt på ren CSS ur `--sc-ps` med noll JS-bildrutor i vändningen, vilket är
  den billigare konstruktionen av de två.
- **`mattis-studio` (borrow som AVVISNING)** — `slår`. Ingen körbar build att mäta. I mitt
  fack är mätpunkten `preview-mid.png`: vid 90 grader finns en hårlinje och ingenting annat,
  alltså noll extra lager att komposita i aktens dyraste ruta — den ritade ramen med
  hörnmarkeringar hade kostat paint per bildruta utan att bära rörelsen.
- **`dope-security`** — `står sig bredvid`. Ingen körbar build att mäta. Noll `box-shadow`
  och en accent med utskriven frekvens är också ett prestandalöfte: inga skuggor betyder
  inga oskarpa ytor att måla om under scroll, och V3c håller det (`perf_probe` flaggar varken
  `big-blur` eller `backdrop-filter`).
- **`monologue`** — `står sig bredvid`. Ingen körbar build att mäta. Hårlinjer på
  `--rail-x`-rastret kostar ingenting per bildruta; V3c betalar inget för sin struktur heller.
- **`planhat` (wildcard)** — `förlorar`. Ingen körbar build att mäta, och därför läser jag
  den på det enda sätt jag ärligt kan: dess grepp är rubrik på mörk grund utan
  helskärmsfilter. V3c bär i stället ett helskärmselement med `filter: grayscale(1)
  contrast(1.08) brightness(.5)` över 100 % av viewporten, vilket är gate 93:s uttryckliga
  nollpost. Kostnaden är mätt till noll i dag (`filter:none` flyttade inte p95), men posten
  står kvar tills den förgråskalade bilden är vendorad.

## material_fixes

1. Bildrutetid i signaturakten, snabb kadens, cpu 4: **p95 144,2 -> 20 ms** och **109 -> 0
   rutor > 33 ms**. Med `**/sites/**` blockerat är den fortfarande 83,3 ms / 86 rutor, så
   målet är cellens eget arbete, inte ramarnas.
2. Stilomräkningen är kostnaden, inte paint och inte script: med ramarna blockerade,
   `Performance.getMetrics`-delta över samma 2,4 s scroll, **RecalcStyle 3 768 -> <= 400 ms**
   (i dag 73 % av 5 134 ms task; Layout 5 ms, Script 332 ms). Ingen enskild konsument bär
   det — ablation av ordscrubben (3 451), jätterubriken (3 244), vändningen (2 800), tråden
   (3 547) och alla fyra samtidigt (3 056) tar inte bort det, så fixen är att skära antalet
   element som räknas om per rotskrivning (motorn skriver `--sc-canvas` på `documentElement`
   varje bildruta under drift, `scrollcraft.js:983`, och cellen hänger tre drift-stopp på den).
3. CLS vid 390x844: **1,038 -> <= 0,05**. Två skift, 0,285 vid 225 ms och 0,753 vid 324 ms;
   varken typsnitt (blockerade: 1,0355) eller bilder (blockerade: 1,0383). Reservera
   hero-stagens höjd innan motorn monterar pinnen, så att `figure.hero-plate` och
   `div.col-left` står still vid p = 0.
4. Långa tasks under scroll: **25 -> 0** vid 1440 (**20 -> 0** vid 390). Den enskilt största
   är en ruta på **1 899,9 ms** när Calyx och Hōrai monteras INUTI den pinnade akten
   (blockerad körning: största ruta 116,7 ms). Flytta monteringen ur aktens resa: utlös
   först vid `--sc-ps` >= 1, inte på `rootMargin: 100%` mitt i vändningen.
5. Uppåtriktningen, som Edge-personan är skriven för: **p95 66,8 -> 20 ms** och **64 -> 0
   rutor > 33 ms** (30 hjulhack a -50 px från y = 1400, cpu 4, största ruta 1 716 ms).
   Prestandaplanen kräver båda riktningarna; bara nedåt var mätt före den här rundan.
6. `max_step` på spelhuvudet `section.hero:--sc-ps` vid 100:60: **3,51 -> <= 3,00 %**
   (omkörning 3,69 %). Vid 20:120 är samma tal 0,86 % och passerar, och staircase är 0 i
   varenda körning: värdet stegar inte, det är kadensen som tar för stora kliv per ruta.
7. Hyperborea-bleeden i s4 rör sig inte: `.thesis-figure` har konstant `translateX` 33,3 px
   vid varje mätt scrollposition 0-3000 px. Driv den **0 -> 11 % över `--sc-ps` 0 -> 1**, som
   § Device-tabell rad 3 föreskriver, eller stryk raden ur tabellen.
8. Gate 93, filtret: **1 -> 0 element med `filter` över > 50 % av viewporten**. `.ground`
   bär `grayscale(1) contrast(1.08) brightness(.5)` över hela ytan. Mätt kostnad i dag: noll
   (`filter:none` flyttade inte p95), så posten stängs av den förgråskalade
   `k4-cabin-desk.webp` som redan står som `[needs asset:]`, inte av ett nytt grepp.

## keep

Behåll att vändningen räknas i ren CSS ur `--sc-ps` med noll JS-bildrutor och noll
layoutläsningar i scroll-handlern: staircase 0 i varje körning, i båda kadenserna och båda
riktningarna, är det enda F-013-talet som redan är stängt, och varje fix ovan som frestas
att flytta `--flip` tillbaka in i en rAF-loop för att "spara omräkningar" öppnar det igen.

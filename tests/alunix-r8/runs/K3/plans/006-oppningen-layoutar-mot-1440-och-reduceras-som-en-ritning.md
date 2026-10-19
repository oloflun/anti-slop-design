# 006 — Öppningen layoutar mot 1440 och reduceras som en ritning, inte mot 320 där exempelsajten själv kollapsar

- **Status**: TODO
- **Commit**: b2e1ecd
- **Severity**: HIGH
- **Category**: funktionsfel (F-007-avvikelse, s4 vid 390; ersätter plan 001, vars *Done when* inte nås med den valda layoutbredden)
- **Estimated scope**: 1 fil (`tests/alunix-r8/runs/K3/index.html`), en CSS-regel plus dess kommentar

## Problem

Plan 001 levererade sin mekanik exakt som den var skriven — `clientWidth` 320,
`matrix(0.85, 0, 0, 0.85, 0, 0)`, `transform-origin: 0 0`, statiskt i CSS, en
gång, på `.opening-live > iframe` — och nådde ändå inte sitt eget *Done when*.
Felet ligger i **planens val av layoutbredd**, inte i utförandet.

Läst som pixlar i `tests/alunix-r8/review/r3/K3-filled-390.png`, beskuret och
förstorat: innanför bläcket står

```
VOⅠNDEX      STUDIO       COMMISSION
   ·         (under "Calyx")
SPRING
```

`Vol. ix · spring` ligger ovanpå `Index`, och `Studio` ligger ovanpå ordmärket
`Calyx`. Byggaren mätte orsaken i stället för att gissa den och attribueringen
är riktig: `sites/calyx.html` laddad naken i 320 px överlappar sina egna
rubrikelement (`shots/r3/p001-calyx-bare-320.png`, som jag har läst som pixlar
och bekräftar). Orsaken är att Calyx header är en `grid-cols-12` **utan enda
responsiv brytning** (`sites/calyx.html:61`–`68`): de tre cellerna behåller
3/6/3 spår vid varje bredd, så navposternas 230 px innehåll trycks in i ett spår
på 60 px. Calyx har alltså inget 320-golv att träffa; den kollapsar kontinuerligt
under ungefär 1100 px.

**Ett andra målvärde i plan 001 föll av samma orsak, och byggaren rapporterade
det inte:** planens Target-rad *"Vad som ska synas vid ps = 1 vid 390: Calyx
navrad utan kollision **och början av fotografiet**"*. I bilden syns inget
fotografi alls — hela öppningens inre är gräddvit navplatta och tomt fält.
Ramens layouthöjd är 180 px och Calyx hero-fotografi börjar först efter headern
och sträcker sig neråt; 180 px räcker till headern och nästan ingenting mer.

Plan 001 är därmed **kvarstående**, och orsaken är min egen målsättning: 320 var
fel bredd. K4:s plan 001 löste samma problem åt andra hållet och är mätt och
verifierad — fast layoutvyport **1440** plus en statisk skala — och samma svar
gäller här.

Nuvarande kod:

```css
/* tests/alunix-r8/runs/K3/index.html:437 — current, i @media (max-width: 767px) */
  .opening-live > iframe {
    width: 320px;                                             /* Calyx layoutgolv */
    height: calc(320px * var(--op-h-m) / var(--op-w-m));      /* = 180px, samma 16:9 */
    transform: scale(calc(var(--op-w-m) / 320));              /* = 0.85 */
    transform-origin: 0 0;
  }
```

## Target

Öppningens ram layoutar mot **1440 px**, den bredd exempelsajten faktiskt är
byggd för, och reduceras med en statisk skala till öppningens ritade mått. Det är
inte en nödlösning: en inzoomad detalj på ett ark är alltid **reducerad**, aldrig
omlayoutad, och en reduktion som visar en hel sida är sannare mot både målbilden
(*"den riktiga Calyx-sidan tonar in innanför den ritade konturen"*) och mot
ritningsgrammatiken än en omlayoutad sida som kollapsar.

| Storhet | Målvärde |
|---|---|
| Ramens layoutbredd i den reducerade planschen | `1440px` |
| Ramens layouthöjd | `810px` (`1440 × 153/272`, samma bildförhållande som öppningen) |
| Skala | `272 / 1440 = 0.18889` |
| `transform-origin` | `0 0` |
| När skalan sätts | statiskt i CSS, aldrig ur `--sc-ps`, aldrig per bildruta |
| Var regeln står | **en** gång, på `.opening-live > iframe`, och den bär a3:s tre plates i innehållsrundan |
| Öppningens ritade kontur | oförändrad, `M24 150 H296 V303 H24 Z` |
| 1440-planschens öppning (`880 × 495`) | **oförändrad.** Den renderar redan rätt och rörs inte |

Mätbara utfall vid 390 × 844 och `?preview=filled`:

| Mätpunkt | Målvärde |
|---|---|
| Överlappande rubrikelement inuti ramen, skärningstest på `getBoundingClientRect` | **0 par** |
| Andel av öppningens inre yta som bär fotografi | **≥ 55 %** |
| Ramens renderade mått | `272 × 153` user units, ± 1 unit på varje sida mot `#opening` |
| Calyx navrad | tre poster på **en** rad, ordmärket fritt emellan |

**Läsbarhet är inte ett målvärde här och ska inte jagas.** Vid 0,18889 blir
Calyx navtyp cirka 2,5 CSS-px. Det som ska läsas är *att det är en riktig
webbplats*, inte vad som står i dess nav — precis som K4:s två miniatyrsidor vid
390, som är mätta och godkända i samma runda. En reduktion som går att läsa ord
för ord är ingen reduktion.

## Repo conventions to follow

- Ramen monteras av `IntersectionObserver`, serialiserat, aldrig vid load
  (`index.html:538`-kommentaren och `performance.md` § 6). Ändra inte det.
- Öppningens fyra tal bor på **ett** ställe, `--op-*` (F-010). Härled `810` och
  `0.18889` ur samma tal med `calc()`, inte som två nya konstanter.
- Precedensen finns redan mätt i grannens ark:
  `tests/alunix-r8/runs/K4/NOTES.md` § *Plan 001, i detalj* (layoutbredd 1440,
  skala 0,2708, satt en gång vid montering och vid `resize`). Skriv in
  hänvisningen i `NOTES.md` så att valet är spårbart och inte ser ut som en
  gissning.
- Byt ut kommentaren över regeln. Den påstår i dag att 320 är Calyx eget golv.
  Det är mätt falskt och en falsk kommentar är värre än ingen.

## Steps

1. Ersätt regeln i § Target-kodblocket. Skriv de två talen som `calc()` ur
   `--op-w-m` och `--op-h-m`.
2. Skärningstest inuti ramen vid 390: hämta `getBoundingClientRect` för Calyx
   `header`s tre celler och räkna överlappande par. Skriv ut talet. Kravet är 0.
3. Mät fotografiets andel av öppningens inre yta (fotografiets översta y-linje i
   ramens koordinater mot ramens höjd). Skriv ut talet.
4. Mät bläckets glapp mot ramens fyra kanter vid 390 och vid 320. Högst 1 unit
   per sida.
5. Kontrollera att 1440-planschens öppning är **bit för bit oförändrad** mot
   `review/r3/K3-filled-1440.png`.
6. Kör om `perf_probe` vid 390. `LCP`, överföring och antalet långa tasks får
   inte försämras mot R3 (`580 ms`, `1677 kB`, `4`). En bredare layoutvyport
   ritar samma dokument; om något av talen stiger, skriv ut hur mycket och varför.

## Boundaries

- Rör INTE `sites/calyx.html`. Exempelsajten redigeras aldrig (Q23).
- Ändra INTE öppningens ritade kontur, dess koordinater eller dess ordning i
  dokumentet (F-010).
- Skalan får ALDRIG animeras, interpoleras eller skrivas per bildruta, och får
  aldrig stå i en `calc()` som innehåller `--sc-ps` eller `--sc-p`.
- Rita INTE en enhetsram, ett webbläsarfält, en flikrad, en adressrad eller en
  trafikljusprick runt ramen (gate 47).
- Lägg INTE till en `zoom`, en `@media`-baserad omlayout av Calyx, ett
  `<style>`-injekt i ramen eller något annat som får exempelsajten att rendera
  annorlunda än den gör naken vid 1440.
- Ändra INTE 1440-planschens öppning.
- Rör INTE motorn eller `sc-smooth.js`.

## Verification

- **Mekaniskt**:
  - Skärningstestet i steg 2: `0` överlappande par vid 320, 375, 390, 414 och 767.
  - Överflödessvep vid samma fem bredder: `scrollWidth == clientWidth`.
  - `motion_probe` på aktens `--sc-ps`, hjul `100:60` och `20:120`: `staircase = 0`
    och `max_step ≤ 3 %`, oförändrat mot R3 (`2,02 %` / `0,98 %`).
  - `node scripts/detect.mjs --json`: fortfarande 0 fynd.
- **Feel check**: ladda `?preview=filled` vid 390 × 844 och läs i pixlar:
  - innanför bläcket står en hel webbplats i reduktion — navband, ordmärke och
    fotografi under det — och inget ord ligger på ett annat;
  - bläcket ligger kvar som ram och sajten flyttar sig aldrig innanför den;
  - scrolla akten 0 → 1 → 0: konturen ritas, öppningen fylls, och ingenting inuti
    öppningen skalar, glider eller tonar efter att sajten visats.
- **Done when**: en skärmbild vid 390 vid `?preview=filled` visar samma sak som
  1440-bilden gör — en riktig webbplats innanför en ritad kontur, med sitt
  fotografi — skärningstestets `0` och fotografiandelen står utskrivna i
  `NOTES.md`, och 1440-bilden är oförändrad.

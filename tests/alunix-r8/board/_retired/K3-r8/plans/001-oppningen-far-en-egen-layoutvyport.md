# 001 — Ge den levande öppningen en egen layoutvyport, så att den fylls med en sida och inte med en kollapsad rubrikrad

- **Status**: TODO
- **Commit**: b2e1ecd
- **Severity**: HIGH
- **Category**: funktionsfel (F-007-avvikelse, s4 vid 390, signaturaktens utbetalning)
- **Estimated scope**: 1 fil (`tests/alunix-r8/runs/K3/index.html`), monteringsfunktionen plus en regel

## Problem

Signaturakten är *ritningen blir sidan*. Vid 390 blir den inte det.

Läst som pixlar i `tests/alunix-r8/review/r2/K3-filled-390.png`: öppningen är
272 × 153 user units, och ramen inuti får därför en layoutvyport på **272 px**,
alltså under Calyx egna 320 px-golv. Det som syns innanför bläcket är Calyx
kolumntitel med sig själv ovanpå sig själv:

```
INDEX  VOL. IX · STUDIO COMMISSION      ← alla fyra posterna staplade
       IX ·                                 på varandra, plus ordmärket
       SPRING                               "Calyx" ovanpå dem
```

Fotografiet syns inte alls. Öppningen läser som en trasig rubrikrad, inte som en
webbplats. `malbilder/K3.md` säger *"den riktiga Calyx-sidan tonar in innanför
den ritade konturen"* och `concepts-K3.md` § (3) s4 kallar den fyllda öppningen
skärmens displayelement. Vid 390 är displayelementet en kollision.

Vid 1440 är samma öppning 880 × 495 och fungerar
(`review/r2/K3-filled-1440.png`), så felet sitter i den reducerade planschens
geometri, inte i mekaniken.

Byggaren mätte och namngav felet själv (`NOTES.md` § Öppet efter R2, punkt 4) och
föreslog fixen; den här planen sätter målvärdena och gränserna.

Nuvarande kod:

```css
/* tests/alunix-r8/runs/K3/index.html:390 — current */
foreignObject { x: 24px; y: 150px; width: 272px; height: 153px; }
```

```html
<!-- :538 — current -->
<foreignObject x="480" y="240" width="880" height="495">
  <div xmlns="http://www.w3.org/1999/xhtml" class="opening-live" data-live="calyx">
```

## Target

Ramen layoutar mot **320 px** och skalas ner med **en statisk `scale()` satt vid
montering**, aldrig under akten. Öppningens ritade kontur står kvar oförändrad;
det är bara innehållet inuti den som byter layoutbredd.

| Storhet | Målvärde |
|---|---|
| Ramens layoutbredd i den reducerade planschen | `320px` |
| Ramens layouthöjd | `180px` (`320 × 153/272`, samma bildförhållande som öppningen) |
| Skala | `272 / 320 = 0.85` |
| `transform-origin` | `0 0` |
| När skalan sätts | en gång i `IntersectionObserver`-monteringen, och vid `resize` |
| Öppningens ritade kontur | oförändrad, `M24 150 H296 V303 H24 Z` |
| Vad som ska synas vid ps = 1 vid 390 | Calyx navrad **utan kollision** och början av fotografiet |

```css
/* target */
@media (max-width: 767px) {
  .opening-live > iframe {
    width: 320px;
    height: 180px;
    transform: scale(0.85);
    transform-origin: 0 0;
  }
}
```

Samma ingrepp gäller a3:s tre plates när de byggs i R3. Gör det **en gång**, som
en regel på `.opening-live`, inte fyra gånger.

## Repo conventions to follow

- Ramen monteras av `IntersectionObserver`, serialiserat, aldrig vid load
  (`index.html:538`-kommentaren och `performance.md` § 6). Ändra inte det.
- Öppningens fyra tal finns på **ett** ställe, `--op-*`, så att sajten inte kan
  hamna utanför sin egen kontur (F-010). Ramens layoutbredd härleds ur samma tal
  — skriv `320` som `calc()` ur `--op-w` om det går, annars som en konstant med
  en kommentar som pekar på `--op-w`.
- Precedensen och formuleringen finns redan i `NOTES.md` § Öppet efter R2:
  *"En statisk skala satt vid montering är inte samma sak som att transformera en
  ram efter att den visats."* Skriv in den som en rad i `BRIEF.md` § decision
  ledger, med `PRODUCT.md` § Operating Context som Source rule.

## Steps

1. Lägg regeln ur § Target i `@media (max-width: 767px)`-blocket
   (`index.html:371`–`400`).
2. Låt monteringsfunktionen sätta skalan **efter** att ramen fått sin `src`, och
   aldrig igen medan akten är live. Skalan får inte läsas ur `--sc-ps` och får
   inte stå i någon `calc()` som innehåller `--sc-ps` eller `--sc-p`.
3. Kontrollera att `#opening`-konturen och `foreignObject` fortfarande delar
   koordinater exakt: skärmbilda vid 390 och mät att bläcket ligger på ramens
   kant med högst 1 px glapp på alla fyra sidor.
4. Kontrollera att samma regel bär a3:s tre plates när de byggs i R3, och skriv
   in det som en rad i `NOTES.md` så att R3 inte gör om samma sak fyra gånger.
5. Kör om `perf_probe` vid 390 och skriv in `LCP`, överföring och antal långa
   tasks. Skalan får inte öka någon av dem.

## Boundaries

- Rör INTE `sites/calyx.html`. Exempelsajten redigeras aldrig.
- Ändra INTE öppningens ritade kontur, dess koordinater eller dess ordning i
  dokumentet. Bläcket ska ligga kvar exakt där det låg (F-010).
- Skalan får ALDRIG animeras, interpoleras eller skrivas per bildruta.
- Rita INTE en enhetsram, ett webbläsarfält, en flikrad, en adressrad eller en
  trafikljusprick runt ramen (gate 47).
- Montera INTE ramen vid load.
- Rör INTE motorn eller `sc-smooth.js`.

## Verification

- **Mekaniskt**:
  - `python ~/.claude/skills/design/scripts/perf_probe.py --url http://127.0.0.1:3311/tests/alunix-r8/runs/K3/index.html --width 390` — `LCP`, överföring och långa tasks får inte försämras mot R2 (`LCP 672 ms`, `1641 kB`, `9`).
  - `motion_probe` på `#page-outline:stroke-dashoffset` och på aktens `--sc-ps`, hjul `100:60` och `20:120`, 4× CPU: `staircase = 0` i alla fyra, oförändrat.
  - Överflödessvep vid 320, 375, 390, 414, 767: `scrollWidth == clientWidth`.
- **Feel check**: ladda `?preview=filled` vid 390 × 844 och kontrollera i pixlar:
  - Calyx navrad står som **en** rad utan överlappande ord, och fotografiet syns innanför bläcket;
  - bläcket ligger kvar som ram runt sajten och sajten flyttar sig aldrig innanför den;
  - scrolla akten från 0 till 1 och tillbaka: konturen ritas, öppningen fylls, och ingenting inuti öppningen skalar, glider eller tonar efter att sajten visats.
- **Done when**: en skärmbild vid 390 vid ps = 1 visar samma sak som 1440-bilden gör — en riktig webbplats innanför en ritad kontur — och inget ord inuti öppningen ligger ovanpå ett annat.

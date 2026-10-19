# 003 — Skilj utropet `16:9` från snittpilens spets

- **Status**: TODO
- **Commit**: b2e1ecd
- **Severity**: MEDIUM
- **Category**: funktionsfel i typen (F-007-avvikelse, s3 och s4 vid 1440)
- **Estimated scope**: 1 fil (`tests/alunix-r8/runs/K3/index.html`), två koordinater

## Problem

Utropet `16:9` ligger vid `x = 1412, y = 206` med `text-anchor="end"`, och
snittmarkeringens högra ben `#cut-AA` slutar med en pilspets vid ungefär
`x = 1392, y = 220`. Pilspetsen skjuter upp i och genom siffran.

Läst som pixlar i `runs/K3/shots/r2/drawn-1440.png` och i
`tests/alunix-r8/review/r2/K3-filled-1440.png`: raden renderas som

```
1 :9        ← sexan är övertäckt av pilspetsen
```

`concepts-K3.md` § (2), gate 79-raden, sätter kontrollen själv: *"varje
`<rect>`/`<path>` i ritningen ska kunna namnges som 'kontur', 'måttlinje',
'hjälplinje', 'skraffering' eller 'utrop' — kan den inte det ska den bort."* Ett
utrop som inte går att läsa har ingen roll, och `NOTES.md` § Beslut har redan en
rad om exakt den principen: *"Ett utrop som ett annat element täcker är ett utrop
utan roll"* — den skrevs när `#c-marginal` flyttades från y 396 till y 268. Samma
regel gäller här och tillämpades inte.

Bevakaren såg samma sak och gav målvärdet (`NOTES.md` § Bevakarens observation,
punkt 2).

Nuvarande kod:

```html
<!-- tests/alunix-r8/runs/K3/index.html:621 — current -->
<path id="lead-16-9" class="leader draw" pathLength="1" d="M1360 240 L1396 214 H1412"/>
<text id="c-169" class="callout" x="1412" y="206" text-anchor="end">16:9</text>
```

## Target

Utropet flyttas ut ur pilens rörelseväg. Ledaren följer med, så att den fortsatt
går från öppningens hörn till etiketten och inte pekar i tomma luften.

| Storhet | Nuvärde | Målvärde |
|---|---|---|
| `#c-169` `x` | `1412` | `1412`, oförändrat |
| `#c-169` `y` | `206` | `186` |
| `#lead-16-9` `d` | `M1360 240 L1396 214 H1412` | `M1360 240 L1392 196 H1412` |
| Minsta avstånd glyfram → pilspetsens ram | ~0 (överlapp) | **≥ 10 user units** |
| Utropets grad, färg, ankare, register | 12 px, `--ink-hair`, `end`, mono | oförändrade |
| `#cut-AA` | `M48 220 V180 H1392 V220` | oförändrad |

Alternativet — att korta snittbenet — är **inte** tillåtet: `#cut-AA` är en enda
obruten bana just för att båda pilspetsarna ska få sin markör ur
`orient="auto-start-reverse"` (`NOTES.md` § Avvikelser, rad 2). Att korta benet
skulle flytta snittets ände från arkets kant och göra snittmarkeringen osann.
Det är etiketten som flyttar sig.

## Repo conventions to follow

- Ledare ritas alltid från målet mot etiketten, med en punkt i måländen och
  aldrig en pilspets (`index.html:615`-kommentaren och `#dot-16-9`). Behåll
  punkten vid `1360, 240`.
- Ledarens knäckvinkel ska följa samma vinkelfamilj som `#lead-marginal`; en
  tredje vinkelfamilj är en ny form på arket.
- Koordinatbyten motiverade av en mätning skrivs som en kommentar med talet, i
  samma stil som `index.html:646`.
- Den reducerade planschens motsvarande koordinater ligger i utropstabellen
  (`index.html:746`) och i `@media`-blockets `#lead-16-9`-regel (`:393`).
  Kontrollera att de fortfarande stämmer — där finns ingen snittmarkering, så
  där ska ingenting ändras.

## Steps

1. Flytta `#c-169` till `y = 186` och `#lead-16-9` till
   `d="M1360 240 L1392 196 H1412"`, med en kommentar som anger mätningen.
2. Mät avståndet mellan `#c-169`s `getBBox()` och pilspetsens ram vid 1440 och
   skriv ut talet.
3. Kontrollera att `#c-169`s ritfönster (`index.html:332`,
   `--t: clamp(0, calc((var(--sc-ps) - 0.74) / 0.02), 1)`) är oförändrat: utropet
   ska tona in vid samma akt-koordinat som förut.
4. Kontrollera att flytten inte lägger utropet ovanpå arkets överkant eller
   ovanpå `#page-outline`; minst 10 units luft till båda.
5. Skriv in ändringen som en rad i `NOTES.md` med bilden som källa.

## Boundaries

- Korta INTE `#cut-AA` och dela den INTE i flera banor.
- Lägg INTE till en andra pilspetsform, en andra linjebredd eller en andra
  dash-form. Arket har ett `<marker>` och tre linjebredder, och det är låst
  (`NOTES.md` § Varje ritad bana och dess roll).
- Ge INTE ledaren en pilspets. Ledare får en punkt i måländen.
- Flytta INTE öppningens kontur för att göra plats.
- Rotera INTE texten. Noll roterad text på arket.

## Verification

- **Mekaniskt**: `node scripts/detect.mjs --json` — inga nya träffar. Räkna `<marker>`-element: fortfarande exakt 1.
- **Feel check**: ladda `?preview=drawn` vid 1440 × 900 och läs i pixlar:
  - `16:9` läses som fyra tecken, ingen glyf är övertäckt;
  - ledaren går från öppningens övre högra hörn till etiketten och pekar dit den ska;
  - snittmarkeringens båda pilspetsar sitter kvar och pekar nedåt;
  - scrolla akten: utropet tonar in vid samma ställe som förut, och ingen ny överlappning uppstår mellan `--sc-ps` 0,72 och 0,80.
- **Done when**: en skärmbild vid 1440 vid `?preview=drawn` och en vid `?preview=filled` båda visar `16:9` helt läsbart, och det mätta avståndet ≥ 10 units står i `NOTES.md`.

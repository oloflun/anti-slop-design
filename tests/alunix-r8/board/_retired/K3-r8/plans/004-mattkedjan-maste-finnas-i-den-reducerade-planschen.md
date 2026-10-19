# 004 — Ge den reducerade planschen tillbaka måttkedjan, som är s3:s displayelement

- **Status**: TODO
- **Commit**: b2e1ecd
- **Severity**: MEDIUM
- **Category**: flöde och hierarki (F-007-avvikelse, s3 vid 390)
- **Estimated scope**: 1 fil (`tests/alunix-r8/runs/K3/index.html`), en mediafråga och tre koordinater

## Problem

`concepts-K3.md` § (3) s3 låser skärmens displayelement:

> | s3 | a1, p 0,55–0,78 | **Måttkedjan** `320 · 768 · 1440` i displaygrad, i blått | Konturen står stilla och går ner till hårlinjevikt |

och `malbilder/K3.md` säger *"utrop med **sanna** värden: 320/768/1440, `7 rem`,
`96 px`, `16:9`"*. Under 768 döljs två av tre måttsiffror:

```css
/* tests/alunix-r8/runs/K3/index.html:379 — current */
#m-768, #m-1440 { display: none; }
```

Läst som pixlar i `runs/K3/shots/r2/drawn-390.png`: den reducerade planschen bär
**ett** tal, `320`, plus `16:9`. Kedjan är borta, `7 rem` och `96 px` är borta,
skrafferingen är borta, snittmarkeringen är borta. Kvar är en rektangel med en
etikett och ett tal. Skärmens displayelement — kedjan av tre sanna mått — finns
inte, och den mätta uppräkningen som är aktens andra höjdpunkt (`count`, tre
stationer i tur och ordning, `NOTES.md` § kontaktarket ruta 8) sker bara på en
station.

Reduktionen i sig är sanktionerad (`ASSETS.md` § A.8) och regeln bakom den är
riktig: *"en station visas bara på en sida vars bredd den faktiskt beskriver"*.
Men regeln är tillämpad på fel objekt. `320`, `768` och `1440` är inte tre
stationer på **den här** sidans bredd — de är de tre brytpunkter Alunix bygger
mot, alltså ritningens ämne. De är sanna på varje skärm, precis som `7 rem` är.

## Target

Måttkedjan finns på båda planscherna. På den reducerade planschen sitter den som
en kedja under arket, inte som stationer på arkets egen bredd, så att inget tal
påstår sig mäta något det inte mäter.

| Storhet | Målvärde vid 390 |
|---|---|
| Antal måttsiffror | **3** (`320`, `768`, `1440`) |
| Grad | `40px` (kedjan är tre tal på 320 units, inte ett på 320) |
| Färg | `--blue`, oförändrad, enda kromatiska på arket |
| Placering | en rad, `y = 600`, `x` = 40 / 160 / 288, ankare `middle` / `middle` / `end` |
| Radetikett ovanför kedjan | ingen. Talen bär sig själva; en etikett vore en fjärde typnivå |
| Måttlinjen `#dim-width` | mäter fortfarande arkets egen bredd, oförändrad |
| Kopplingen tal → linje | tas bort på den reducerade planschen: kedjan är ett **utrop**, inte en stationskedja, och får därför inga stationsstreck |
| `count`-fönstren | oförändrade (`0.58 0.66`, `0.64 0.72`, `0.70 0.77`) |
| Största glyfhöjd i vyn | kedjan, 40 px — den ska fortfarande vara skärmens displayelement |

```css
/* target — ersätter #m-768, #m-1440 { display: none } */
@media (max-width: 767px) {
  #m-320, #m-768, #m-1440 { font-size: 40px; }
  /* stationsstrecken hör till 1440-planschen; på den reducerade är kedjan
     ett utrop och inte en stationskedja, så inget streck pekar på ett tal. */
  #stations { display: none; }
}
```

Om de tre talen inte ryms läsbart på 320 units vid 40 px i Martian Mono: sänk
till 34 px, mät, och skriv ut det mätta talet. Under 34 px faller kedjan ur
displaygrad och då gäller i stället golvet i § Boundaries.

## Repo conventions to follow

- `x`/`y` på `<text>` sätts i utropstabellen i JS (`index.html:739`–`750`), inte
  i CSS. Lägg `m-768` och `m-1440` i tabellen med sina reducerade koordinater;
  `m-320` finns redan där (`:749`).
- `font-size` är en riktig CSS-egenskap på `<text>` och sätts i mediafrågan, som
  `#m-320` redan gör (`:397`).
- `data-sc-count` läses av motorn; talen står i markupen och inget tal får
  uppstå som inte redan står där (`NOTES.md` § Beslut, previewlägena).
- Kommentaren på `index.html:395`–`396` säger att `320` är sann *"just därför att
  planschen ÄR 320 bred"*. Den motiveringen faller när kedjan blir ett utrop;
  skriv om kommentaren så att den säger vad talen nu är: Alunix tre brytpunkter.

## Steps

1. Ta bort `#m-768, #m-1440` ur `display: none`-listan (`index.html:379`).
2. Lägg deras reducerade koordinater i utropstabellen (`index.html:739`).
3. Sätt graden i mediafrågan och mät att alla tre talen ryms med minst 8 units
   luft till arkets kanter och minst 8 units mellan talen. Skriv ut de mätta
   talen.
4. Dölj `#stations` på den reducerade planschen och skriv om kommentaren på
   `:395`.
5. Skärmbilda `?preview=drawn` vid 390 och 320 och läs kedjan i pixlar.
6. Skriv in ändringen som en rad i `NOTES.md` med `concepts-K3.md` § (3) s3 som
   källa.

## Boundaries

- Hitta ALDRIG på ett tal. De tre talen är `320`, `768` och `1440` och de står
  redan i markupen; ingen fjärde station får läggas till.
- Lägg INTE till en etikett, en enhet (`px`) eller en punktkedja mellan talen.
- Låt INTE kedjan bli en stationskedja på den reducerade planschen: inget streck
  och ingen förlängningslinje får peka från arkets bredd upp till ett tal som
  inte mäter den bredden.
- Golv: faller kedjan under 34 px för att rymmas, bygg den INTE ändå. Skriv då i
  stället en rad i `NOTES.md` om att den reducerade planschen inte kan bära s3:s
  displayelement, och lyft frågan till arkitekten i stället för att leverera tre
  små tal som varken är display eller register.
- Rör INTE `count`-fönstren och rör INTE motorn.

## Verification

- **Mekaniskt**:
  - `scroll_verify.py --width 390`: `unrevealed` fortsatt tom, `cuesNeverFull` fortsatt tom.
  - `motion_probe` på aktens `--sc-ps`, hjul `100:60` och `20:120`, 4× CPU: `staircase = 0`, oförändrat.
  - Överflödessvep vid 320 och 390: `scrollWidth == clientWidth`.
- **Feel check**: scrolla akten vid 390 × 844 från ps = 0,50 till ps = 0,80 och läs i pixlar:
  - de tre talen räknar upp en i taget, i ordning, och landar på `320`, `768` och `1440`;
  - talen är det tyngsta i vyn medan de räknar, och konturen har gått ner till hårlinjevikt bakom dem;
  - inget tal rör vid ett annat och inget rör vid arkets kant;
  - inget streck pekar på ett tal.
- **Done when**: en skärmbild vid 390 vid ps ≈ 0,72 visar tre blå tal i displaygrad på en rad, och de mätta luftavstånden står i `NOTES.md`.

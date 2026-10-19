# 003 — Låt inte sömmen halvera ett ordmärke eller en navpost vid ps = 0

- **Status**: TODO
- **Commit**: b2e1ecd
- **Severity**: MEDIUM
- **Category**: visuellt (F-007-avvikelse, s1 vid 1440 och 390)
- **Estimated scope**: 1 fil (`tests/alunix-r8/runs/K4/index.html`), ett tal

## Problem

Vid ps = 0 ligger sömmen på exakt 50 % av scenens bredd. Läst som pixlar i
`tests/alunix-r8/review/r2/K4-fold-1440.png`:

- Calyx **centrerade ordmärke** ligger på scenens mittlinje, så det som syns
  till höger om sömmen är `lyx`. Ordmärket är det mest läsbara objektet i
  foldens högra halva, och det står som ett halvt ord.
- Mallsidans navpost `Customers` skärs på samma linje och läser `Custo`.

Vid 390 upprepas felet (`review/r2/K4-fold-390.png`: `lyx` över `Flowstack`).

`concepts-K4.md` § (3) s1 säger att foldens displayelement är tvåtonsrubriken och
att *"de två sajterna står helt stilla"*. En sida vars mest läsbara märke är ett
halvt ord står inte stilla, den läser som fel. Och `malbilder/K4.md` § (2)
neutraliserar jämförelseslider-klichén bland annat med att *"'före' är ärligt
märkt"* — ett `Custo` är motsatsen till ärlig märkning.

Nuvarande kod:

```js
/* tests/alunix-r8/runs/K4/index.html:64 — current */
initial-value: 0.5;

/* :582 — current, resans startvärde */
return 0.5 * (1 - clamp01((ps - SILENCE) / (1 - SILENCE)));

/* :709 — current */
var MODES = { before: 1, split: 0.5, after: 0, mid: 0.25, degraded: 0.10, drag: 0.5 };
```

## Target

Startvärdet för `--split` flyttas från 0,5 till ett **mätt** värde som lägger
sömmen i dödyta på båda sidor. Kandidatfönstret är 0,54–0,60: Calyx ordmärke
slutar vid ungefär x = 757 av 1440 (`= 0,526`) och mallsidans navrad slutar vid
ungefär x = 730 (`= 0,507`), så en söm strax till höger om båda missar dem båda.

Måltal:

| Mätpunkt | Målvärde |
|---|---|
| `--split` vid ps = 0 | mätt värde i intervallet **0,54–0,60** |
| Avstånd sömmen → närmaste glyfkant, Calyx sida, 1440 | **≥ 12 px** |
| Avstånd sömmen → närmaste glyfkant, mallsidan, 1440 | **≥ 12 px** |
| Samma två avstånd vid 390 efter plan 001 (skalad scen) | **≥ 4 px** |
| Andelen "före" som syns vid ps = 0 | **≥ 0,54** — före-sidan får aldrig se ut att redan ha förlorat |
| `Före`- och `Efter`-etiketternas läge | oförändrat relativt sömmen, 20 px offset som idag |

Startvärdet skrivs på **ett** ställe och läses av de tre andra:

```js
/* target */
var SPLIT_START = 0.57;   /* mätt, se NOTES.md § R3 */
```

`@property --split { initial-value }`, `splitTarget()`, `.split { --d: … }` och
`MODES.split` / `MODES.drag` ska alla härledas ur samma konstant, så att
startvärdet inte kan hamna på fyra ställen som glider isär.

## Repo conventions to follow

- `--d`-formeln (`index.html:212`) är normerad mot 0,5; den ska normeras mot
  `SPLIT_START` i stället, annars börjar degraderingen på ett värde skilt från 0
  vid folden. Kontrollera i pixlar att rubrikens före-halva vid ps = 0 har
  **exakt** samma vikt och tracking som i R2:s `fold-1440.png`.
- Mätta tal skrivs som en kommentar bredvid konstanten, i samma stil som
  `index.html:411`.
- Motorn och `sc-smooth.js` rörs aldrig.

## Steps

1. Mät i pixlar var Calyx ordmärke och mallsidans sista navpost slutar vid 1440,
   och skriv ut de två x-värdena.
2. Inför `SPLIT_START` som en konstant och härled `@property --split`s
   `initial-value`, `splitTarget()`s toppvärde, `--d`-normeringen och
   `MODES.split` / `MODES.drag` ur den.
3. Kör om plan 002:s kurvmätning med det nya startvärdet — de två planerna delar
   samma funktion och måste mätas tillsammans, inte var för sig.
4. Kontrollera `Före`/`Efter`-etiketterna vid 390 med ett överflödessvep: `.tag`
   är 44 % bred (`index.html:426`) och etiketten till vänster om en söm vid 0,57
   får mer plats, inte mindre, så den ska fortsatt rymmas.
5. Skriv in de mätta talen och beslutet som en rad i `BRIEF.md` § decision ledger
   och i `NOTES.md`.

## Boundaries

- Rör INTE `sites/calyx.html` eller `sites/before-ai-slop.html`. Ordmärket
  flyttas aldrig; det är sömmen som flyttar sig.
- Sätt INTE ett startvärde över 0,60. Då börjar folden med en synbar övervikt åt
  "före", och sidans argument börjar med fel hälft.
- Lägg INTE till en mask, en toning eller en ram vid sömmen för att dölja
  skärningen. Delaren är en linje, inte en list (`malbilder/K4.md`: delaren är
  sidans enda form).
- Ändra INTE etiketternas offset från sömmen.

## Verification

- **Mekaniskt**: överflödessvep vid 320, 375, 390, 414, 768, 1440 — `scrollWidth == clientWidth` på var och en. `motion_probe` på `--split` oförändrad mot plan 002:s utfall.
- **Feel check**: ladda vid 1440 × 900 och vid 390 × 844 och kontrollera i pixlar:
  - inget ordmärke, ingen navpost och inget helt ord skärs av sömmen vid ps = 0; det enda sömmen får skära är tvåtonsrubriken, vilket är devicen;
  - rubrikens före-halva ser vid ps = 0 exakt lika oförändrad ut som i `shots/r2/fold-1440.png` — degraderingen börjar på noll;
  - `?preview=split` visar samma bild som ps = 0.
- **Done when**: en skärmbild vid ps = 0 vid 1440 och en vid 390 visar två hela märken, ett per sida, och avstånden i måltabellen är uppmätta och utskrivna i `NOTES.md`.

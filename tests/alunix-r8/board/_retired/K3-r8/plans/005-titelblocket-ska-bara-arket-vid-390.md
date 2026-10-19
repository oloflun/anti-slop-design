# 005 — Låt titelblocket bära arket vid 390, så att tystnaden läses som papper och inte som en sida som inte laddat

- **Status**: TODO
- **Commit**: b2e1ecd
- **Severity**: MEDIUM
- **Category**: visuellt (F-007-avvikelse, s1 vid 390)
- **Estimated scope**: 1 fil (`tests/alunix-r8/runs/K3/index.html`), titelblocket i mediafrågan

## Problem

`concepts-K3.md` § (3) s1 beskriver skärmen: *"**Titelblocket** i arkets övre
vänstra hörn (`ALUNIX` · `SEKTION A-A` · `SKALA 1:1`), satt i mono | Arket är
annars tomt: författad tystnad före toppen."*

Vid 1440 fungerar det. Läst som pixlar i
`tests/alunix-r8/review/r2/K3-fold-1440.png`: tre monorader upptar ungefär 1,4 %
av fältet och sitter i ett hörn, och proportionen mellan ett litet block och ett
stort fält **är** ritpappersgrammatiken. Tystnaden är författad och läses så.

Vid 390 faller den. Läst som pixlar i `review/r2/K3-fold-390.png`: samma tre
rader spänner 31 % av bredden och sitter i **överkanten**, inte i ett hörn — vid
390 finns ingen andra axel som gör hörnet till ett hörn. Papperet bleeder till
alla fyra kanter på båda bredderna, så arkets egen kant har aldrig burit
"ark"-läsningen; det enda som gjorde det var proportionen, och proportionen finns
bara vid 1440. Kvar vid 390 är tre små rader i toppen och en blågrå rektangel
under dem, vilket är formen på en sida som inte laddat sitt innehåll.

`scroll_verify`s `deadScroll` 0 → 300 px och `blankBands` från y = 128 pekar åt
samma håll, men de är **inte** belägget: samma band täcker R3-platshållarna, som
är tomma med avsikt i den här rundan. Belägget är bilden.

Nuvarande kod:

```html
<!-- tests/alunix-r8/runs/K3/index.html:525 — current -->
<g id="title-block">
  <text id="t1" class="titlefield" x="48" y="68">ALUNIX</text>
  <text id="t2" class="titlefield" x="48" y="98">SEKTION A-A</text>
  <text id="t3" class="titlefield" x="48" y="128">SKALA 1:1</text>
</g>
```

Vid 390 flyttas de tre raderna av utropstabellen, men de förblir tre lösa rader.

## Target

Under 768 blir titelblocket det ett titelblock är på en riktig ritning: en
**rutad ruta** i arkets nedre högra hörn (ISO 7200), med de tre fälten i var sin
cell. Rutningen är en del av titelblocket, inte ett nytt element, så
`BRIEF.md` § FIRST VIEWPORT står kvar oförändrad: papperet och titelblocket, två
saker.

| Storhet | Målvärde vid 390 × 844 |
|---|---|
| Titelblockets form | ruta med 3 celler, ritad i `--ink-hair`, `stroke-width` 0.75, radie **0** |
| Bredd | `184` user units |
| Höjd | `66` user units (3 celler à 22) |
| Placering | nedre högra hörnet av första vyporten, ytterkant `x = 296`, underkant `y = 596` |
| Avstånd till arkets kanter | ≥ 24 units åt båda hållen — samma marginal som resten av arket |
| Fältens grad | 12 px mono, oförändrad |
| Tomt fält ovanför blocket | ≥ 62 % av vyporten — det ska fortfarande vara mest papper |
| Antal saker i första vyporten | **2**: papperet och titelblocket |
| Vid ≥ 768 | oförändrat: tre lösa rader uppe till vänster, exakt som i R2 |

Ritningen som helhet börjar fortfarande ritas först på scroll. Ingenting av
konturen, snittet eller måtten förinkas.

## Repo conventions to follow

- Rutningen ritas med samma tre tillåtna linjebredder som resten av arket
  (`NOTES.md` § Varje ritad bana och dess roll: 1.5 kontur, 0.75 hjälplinje och
  måttlinje, 2.5 snitt). Titelblockets ruta är en **kontur** kring ett utrop och
  tar `0.75`, samma som ledarna och måttlinjerna. Ingen fjärde bredd.
- Rutningen ska kunna namnges i gate 79-tabellen. Lägg till en rad i
  `NOTES.md` § Varje ritad bana och dess roll med rollen **utrop, rutat**.
- Geometri sätts i mediafrågan där den är en CSS-geometriegenskap (`<rect>`,
  `<path>` via `d:`), och i utropstabellen där det är `<text>`.
- Precedensen finns i samma fil: legendens rader har papperskulör bakom sig och
  motiveras uttryckligen som *"inte ett kort … ingen radie, ingen kant, ingen
  skugga, ingen elevation"* (`NOTES.md` § Avvikelser). Titelblockets ruta är
  ritade linjer, inte en yta: ingen fyllning, ingen skugga, ingen radie.

## Steps

1. Lägg en `<path id="title-frame" class="guide">` **inuti** `#title-block`,
   dold vid ≥ 768 och given sin `d` i mediafrågan under 768: ytterram plus två
   vågräta delare.
2. Flytta de tre `<text>`-fälten till rutans celler via utropstabellen
   (`index.html:739`), vänsterställda med 8 units indrag.
3. Mät i pixlar vid 390 × 844 hur stor andel av vyporten som är tomt papper
   ovanför blocket och skriv ut talet. Under 62 %: flytta blocket längre ned.
4. Kontrollera vid 320 × 568 att blocket ryms med ≥ 24 units marginal; om inte,
   skala rutan proportionellt och skriv ut det mätta talet.
5. Lägg raden i gate 79-tabellen i `NOTES.md` och en beslutsrad i
   `BRIEF.md` § decision ledger (Area: hero-device, Source: F-007-kontrollen R2,
   Source rule: `concepts-K3.md` § (3) s1).

## Boundaries

- Lägg INTE till ett tredje element i första vyporten. Ingen cue, ingen
  greet-text, ingen pil, ingen "scrolla"-rad, ingen prick (gate 88).
- Förinka INTE konturen, snittmarkeringen, måttlinjerna eller öppningen.
  Ritningen ska fortfarande vara ett tomt ark innan handen börjar.
- Ge INTE rutan en fyllning, en radie, en skugga eller en egen ytfärg. Den är
  ritade linjer på papperet.
- Ändra INTE fältens text. `ALUNIX`, `SEKTION A-A` och `SKALA 1:1` står
  oförändrade, och `SEKTION A-A` skrivs med bindestreck, aldrig med tankstreck.
- Ändra INTE 1440-vyn. Detta är en regel under 768.
- Rör INTE motorn eller aktens spann.

## Verification

- **Mekaniskt**:
  - Kodpunktssvep på synlig text: noll U+2010–U+2015 och noll U+2212.
  - `scroll_verify.py --width 390`: `deadScroll`-bandet vid arkets topp får inte växa.
  - `node scripts/detect.mjs --json`: inga nya träffar, särskilt ingen radie och ingen skugga.
- **Feel check**: ladda `?preview=sheet` vid 390 × 844 och vid 320 × 568 och läs i pixlar:
  - vyn läser som ett ark med ett titelblock i hörnet, inte som en sida som inte laddat;
  - blocket ser ut som ett ritningstitelblock: rutat, tre fält, hårlinjer, inga runda hörn;
  - fältet ovanför blocket är tomt och känns avsiktligt tomt;
  - scrolla en tumsbredd: den första linjen börjar ritas och tystnaden slutar där den ska.
- **Done when**: en skärmbild vid 390 × 844 vid ps = 0 visar exakt två saker, papperet och ett rutat titelblock i nedre högra hörnet, det mätta tomrumstalet ≥ 62 % står i `NOTES.md`, och 1440-bilden är bit för bit oförändrad mot `review/r2/K3-fold-1440.png`.

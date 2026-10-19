# K3, assetpaket · Ritningen

F-009: arkitekten specificerar, **lead vendorar**. Byggaren kopierar ingenting hit och
genererar ingenting (Higgsfield är spärrat pa byggarens argv).

Skriven av arkitekten. Leads Higgsfield-mätning gjordes 2026-09-09.

**K3 har inga foton.** Noll fotografier, noll människor, noll ansikten. Media strategy för
cellen är `product surface` (de tre exempelsajterna, live i `<iframe>` fran samma origin)
plus `drawn system` (ritningen och papperstexturen). Det finns ingen `photo:*`-plats och
ingen `generated`-plats i den här cellen.

Filen har tva delar:

- **§ A — SVG-specen för ritningen.** Geometri, linjehierarki, pilspets, typregister,
  ritordning, mask-in. Byggaren ska kunna rita efter den utan att gissa.
- **§ B — Ritpapperstexturen som procedurell CSS/SVG**, med sömkravet som en körbar
  kontroll.

---

## § 0 · Varför ingen generering, och varför det inte är en nödlösning

`generation.md` § 1 rangordnar källorna: produktens egen yta, riktig fotografi, genererat
material, **ett bespoke ritat identitetssystem**, kurerade komponentkällor. Den skriver
ocksa ut undantaget som gäller precis här: *"in a drawn register (zero photography, an
identity built from line) a drawn system beats both."* K3 **är** det registret. Ett ritat
system är alltsa inte tredje bästa vägen i den här cellen, det är den första.

Tre skäl till, alla mätbara:

1. **Sömlöshet.** En genererad kakling maste sömkontrolleras i efterhand
   (`upstream/higgsfield/game-textures.md` Fas 3 finns bara därför att den kontrollen
   behovs), och även en tile med sömkvot ≈ 1,0 kan visa synlig repetition över en stor
   yta. Ett `feTurbulence`-fält med `stitchTiles="stitch"` är sömlöst **genom
   konstruktion**: filtret beräknar brusfältet sa att kaklets kanter fortsätter i varandra,
   och det finns ingen söm att kontrollera bort.
2. **Konsistens.** Ett genererat material har ingen regel bakom sig. En ritning haller
   ihop av att varje linje, varje pilspets och varje utrop kommer ur **en** namngiven
   uppsättning. Det som en stilnyckelbild skulle ha gett K3 uttrycks här i stället som
   regel: en hårlinjebredd (§ A.2), en pilspetsform (§ A.3), ett utropsregister (§ A.4).
   En regel gar att granska med `grep`; en stilnyckelbild gar bara att titta pa.
3. **Budget.** Texturen kostar ~700 byte markup i stället for en fil pa
   överföringsbudgeten (`performance.md` § 1), och ritningen kostar noll natverksrundor.

Kreditläget bekräftar samma väg utan att vara skälet till den: Higgsfield `balance` ger
`{"credits":0,"subscription_plan_type":"free"}`, en enda privat workspace, matt av lead
2026-09-09. Planens § 10.6 steg 1 (Higgsfield) faller pa krediter. Steg 2 (Codex
`image_gen`) **hoppas över för K3**, inte för att det är dyrare utan för att steg 3 är
strikt bättre här: en bildmodell kan inte producera vare sig en sömlös kakling genom
konstruktion eller en linjehierarki som gar att granska mot en regel.

Följden i decision ledger, ordagrant:
`Genererat material -> procedurell SVG/CSS · Källa: planens § 10.6 fallback steg 3 ·
Orsak: Higgsfield 0 credits, free plan, mätt 2026-09-09 av lead`

**Inga generate-prompter skrivs i den här filen.** `credits.json` redovisar noll jobb och
noll krediter.

---

## § A · SVG-specen för sektionsritningen

### A.1 Koordinatrum och skala

```
<svg id="drawing" viewBox="0 0 1440 900" preserveAspectRatio="xMidYMid meet"
     width="100%" role="img" aria-label="Sektionsritning av en webbsida">
```

**En user unit = en CSS-pixel vid referensvyn 1440 × 900.** Det är vad titelblockets
`SKALA 1:1` pastar, och det är kontrollerbart: byggaren mäter `#page-outline`s renderade
bredd med `measure.py` och far 1440 CSS-px vid en 1440 bred viewport. Under 1440 skalas
arket likformigt och utropen behaller sina värden, precis som en 1:1-ritning som kopieras
mindre fortfarande säger 1:1 och fortfarande säger 1440: utropen beskriver **den ritade
sidan**, inte pappret.

Arket **är** viewporten. Det finns ingen separat arkram: `#page-outline` är den ritade
sidans egen ytterkontur och löper i viewportens kant. Marginalen syns i stället genom
skrafferingsbandet innanför (§ A.5, SK1).

### A.2 Linjehierarki — tre bredder, en dash-form, inget annat

Alla värden i user units, alltsa CSS-px vid 1440.

| Roll | `stroke-width` | Färg | Dash | Terminator | Var |
|---|---|---|---|---|---|
| **Snittmarkering** | `2.5` | `--ink` | solid | `#arrow` i bada legarnas ändar | En enda: `#cut-AA` |
| **Kontur** | `1.5` | `--ink` | solid | ingen (sluten bana) | `#page-outline`, `#opening`, a3:s tre plate-ramar, a6:s fyra ramlinjer |
| **Hårlinje: måttlinje** | **`0.75`** | `--ink-hair` | solid | `#arrow` i bada ändar | `#dim-width`, `#dim-gutter`, `#dim-row` |
| **Hårlinje: hjälplinje / förlängningslinje** | **`0.75`** | `--ink-hair` | `4 3` | ingen | `#guide-col-a-l`, `#guide-col-a-r`, `#guide-gutter-r`, `#ledger-1..3`, `#ext-320`, `#ext-768` |
| **Hårlinje: ledare** | **`0.75`** | `--ink-hair` | solid | `r=1` fylld punkt i maländen, ingenting i etikettänden | `#lead-16-9`, `#lead-marginal`, legendens aktiva ledarlinje |
| **Hårlinje: skraffering** | **`0.75`** | `--ink-hair` | solid, 45°, delning 8 | ingen | `#hatch-marginal` |

**Den enda hårlinjebredden är `0.75 px`.** Den deklareras en gang som `--hair: 0.75px` och
gäller **ocksa utanför `<svg>`**: varje `border`, varje `<hr>`, varje avdelare, varje
understrykning och varje ramlinje i HTML pa hela sidan har exakt den bredden. Det finns
ingen andra hårlinje. Kontrollen: `grep -oE "(border[^;]*|stroke-width:)\s*[0-9.]+px"`
över filen ska bara ge `0.75px`, `1.5px` och `2.5px`.

**Tre bredder totalt, i förhallandet 1 : 2 : 3,33.** Skillnaden mellan måttlinje,
hjälplinje och ledare är alltsa aldrig bredden utan **dash-formen och terminatorn**, vilket
är hur en riktig ritning skiljer dem at.

**Den enda dash-formen är `stroke-dasharray: 4 3`.** Ingen andra streckform finns pa arket:
ingen kedjelinje, ingen punktlinje, ingen `dashoffset` som dekor. (Att `stroke-dasharray`
ocksa används som ritmekanik i § A.6 är en annan sak: där är den `1` per bana, satt av
`pathLength`, och den är aldrig synlig som en streckad linje.)

`stroke-linecap: butt` och `stroke-linejoin: miter` överallt. `vector-effect` används
**inte**: linjerna ska skalas med arket, det är vad som gör dem till en ritning och inte
till chrome. Följden för mobilen star i § A.8.

### A.3 Pilspetsen — en enda form, ett enda element

```svg
<marker id="arrow" markerUnits="userSpaceOnUse" markerWidth="9" markerHeight="6"
        refX="9" refY="3" orient="auto-start-reverse">
  <path d="M0 0 L9 3 L0 6 Z" fill="currentColor" stroke="none"/>
</marker>
```

**Sluten, fylld triangel, 9 lang och 3 bred vid basen, alltsa 3:1** — ISO 129:s
`closed filled`-form, den enda pilspets som finns pa arket. Den fylls med `currentColor` sa
att den ärver linjens färg och aldrig kan hamna i fel ton. `markerUnits="userSpaceOnUse"`
gör att den **inte** skalar med `stroke-width`: samma fysiska pilspets sitter pa en
måttlinje (0.75) och pa snittmarkeringen (2.5), vilket är exakt vad en ritning gör.
`orient="auto-start-reverse"` gör att samma `<marker>` fungerar i bada ändar.

Regeln, granskningsbar: **det finns exakt ett `<marker>`-element i hela filen.** Varje pil
pa sidan är `marker-start="url(#arrow)"` eller `marker-end="url(#arrow)"`. En pil ritad som
tva `<line>` eller som ett `<path>` är ett fel. En ledare far **aldrig** en pilspets: det är
vad som skiljer en ledare fran en måttlinje, och ledaren slutar i stället i en fylld punkt
med `r=1`.

### A.4 Utropens typregister — Martian Mono, exakt tva inställningar

Varje ord i ritningen är ett **utrop** och sätts i registerrollen. Chivo förekommer aldrig
inuti `<svg>`-blocket; kontrollen är `grep -c Chivo` innanför blocket = 0.

| Inställning | Var | Snitt | Vikt | Bredd | Grad | Tracking | Färg |
|---|---|---|---|---|---|---|---|
| **`display 72`** | Enbart måttsiffrorna `320`, `768`, `1440` i a1 | Martian Mono | 500 | 112.5 % | 72 px | 0.02em | `--blue` |
| **`margin 12`** | Allt annat mono pa hela sidan: titelblockets tre fält, zonnamnen, `7 rem`, `96 px`, `16:9`, snittbokstäverna `A`, legendens rader, folio, radnumren 01 till 03, ledarpunkterna, prisradernas etiketter | Martian Mono | 400 | 87.5 % | 12 px | 0.14em, versal | `--ink-hair`, utom titelblocket som är `--ink` |

**Det finns ingen tredje inställning.** Ingen 14 px, ingen 18 px, ingen halvväg. Nedskalningen
i s4 (§ A.6 steg 14) är en `transform: scale()` pa `display 72`-elementen, inte en tredje
grad: det är samma siffra som krymper, inte en ny siffra som byts in.

**Ingen text pa arket är nagonsin roterad.** Inte legendens rader, inte de vertikala
måttens siffror, inte folion. Roterad typ är en produktionstell, och en ritning som kräver
att man vrider pa huvudet är en ritning ingen läser. `#dim-row`s siffra `96 px` sätts
vagrätt till höger om sin lodräta måttlinje.

`text-rendering: geometricPrecision` pa `<text>` inuti ritningen, `dominant-baseline`
sätts explicit per element, aldrig `alignment-baseline`.

### A.5 Elementinventarium — geometrin, exakt

Alla koordinater i user units. Ordningen i tabellen är ritordningen (§ A.6).

**Statiskt, finns vid `--sc-ps` = 0, ritas inte:**

| id | Roll | Geometri |
|---|---|---|
| `#title-block` | Utrop, `margin 12` | Ram-lös textgrupp i övre vänstra hornet. Tre rader, vänsterställda vid x = 48, baslinjer y = 68, 98, 128. Raderna: `ALUNIX` · `SEKTION A-A` · `SKALA 1:1`. **Bindestreck, aldrig tankstreck** (PRODUCT.md: inga tankstreck i synlig text) |

**Konturer (1.5, `--ink`):**

| id | Roll | Geometri |
|---|---|---|
| `#page-outline` | Den ritade sidans ytterkontur | `M 0.75 0.75 H 1439.25 V 899.25 H 0.75 Z`, en enda bana, ritad medurs fran övre vänstra hornet. Den geometriska rektangeln är exakt 1440 bred, vilket är vad `1440`-utropet mäter |
| `#opening` | Den måttsatta öppningen som Calyx maskas in i | `M 480 240 H 1360 V 735 H 480 Z`. **880 × 495 = 16:9 exakt.** Ritad medurs fran sitt övre vänstra horn |

**Snittmarkering (2.5, `--ink`, `#arrow` i bada legarnas ändar):**

| id | Roll | Geometri |
|---|---|---|
| `#cut-AA` | Snittlinjen A-A som titelblocket refererar | Vagrät linje y = 180, x 48 → 1392. Vid varje ände en lodrät ben 40 langt nedat (x = 48 respektive x = 1392, y 180 → 220), vardera avslutad med `#arrow` som pekar nedat: betraktningsriktningen är nedat, alltsa mot resten av ritningen. Bokstaven `A` i `margin 12` vid (48, 168) vänsterställd och vid (1392, 168) högerställd |

**Hjälplinjer (0.75, `--ink-hair`, dash `4 3`):**

| id | Roll | Geometri |
|---|---|---|
| `#guide-col-a-l` | Spalt A, vänsterkant | Lodrät x = 120, y 176 → 812 |
| `#guide-col-a-r` | Spalt A, högerkant | Lodrät x = 368, y 176 → 812 |
| `#guide-gutter-r` | Spaltavstandets högerkant | Lodrät x = 480, y 176 → 812. **Avstandet 368 → 480 = 112 = `7 rem` vid rotgrad 16 px**, vilket är vad `#dim-gutter` mäter |
| `#ledger-1` | Liggarens rad 1 | Vagrät y = 560, x 120 → 368 |
| `#ledger-2` | Liggarens rad 2 | Vagrät y = 656, x 120 → 368 |
| `#ledger-3` | Liggarens rad 3 | Vagrät y = 752, x 120 → 368. **Delningen 96 är vad `#dim-row` mäter, och samma `96 px` utropas igen i a4:s marginal** |
| `#ext-320` | Förlängningslinje | Lodrät x = 320, y 760 → 802 |
| `#ext-768` | Förlängningslinje | Lodrät x = 768, y 760 → 802 |

Vid x = 0 och x = 1440 tjänar `#page-outline` självt som förlängningslinje, vilket är
korrekt ritpraxis och sparar tva banor.

**Skraffering (0.75, `--ink-hair`, 45°, delning 8):**

| id | Roll | Geometri |
|---|---|---|
| `#hatch-marginal` | Marginalzonen | `<rect x="0.75" y="176" width="119.25" height="636">` fylld med `<pattern id="hatch" patternUnits="userSpaceOnUse" width="8" height="8" patternTransform="rotate(45)">` som innehaller en `<line x1="0" y1="0" x2="0" y2="8">`. Ingen kontur runt rektangeln: skraffering är en yta, inte en form |

**Måttlinjer (0.75, `--ink-hair`, `#arrow` i bada ändar):**

| id | Roll | Geometri | Utrop |
|---|---|---|---|
| `#dim-width` | Totalbredden med tva stationer | Baslinje y = 790, x 0 → 1440, `#arrow` i bada ändar. Stationsstreck: 0.75-lodräter y 782 → 798 vid x = 320 och x = 768 | Tre siffror i `display 72`, baslinje y = 880: `320` centrerad vid x = 320 (upptar x 240 till 400), `768` centrerad vid x = 768 (x 688 till 848), `1440` högerställd mot x = 1430 (x 1230 till 1430). **Detta är en stationskedja: varje siffra anger avstandet fran vänsterkanten, inte segmentets längd.** Det är den enda kedjeform vars samtliga etiketter är sanna värden ur den tillatna listan; en vanlig kedja hade gett 320, 448 och 672, varav tva är pahittade tal |
| `#dim-gutter` | Spaltavstandet | Vagrät y = 200, x 368 → 480, `#arrow` i bada ändar | `7 rem` i `margin 12`, centrerad vid x = 424, baslinje y = 192 |
| `#dim-row` | Liggarens raddelning | Lodrät x = 140, y 560 → 656, `#arrow` i bada ändar | `96 px` i `margin 12`, vänsterställd vid x = 152, baslinje y = 612. Vagrät, aldrig roterad |

**Ledare (0.75, `--ink-hair`, solid, punkt `r=1` i maländen, ingen pilspets):**

| id | Fran | Till | Utrop |
|---|---|---|---|
| `#lead-16-9` | Punkt vid (1360, 240), öppningens övre högra horn | En knäck vid (1400, 214), sedan vagrät stump till x = 1424 | `16:9` i `margin 12`, högerställd mot x = 1424, baslinje y = 208 |
| `#lead-marginal` | Punkt vid (60, 396) | Lodrät stump uppat till (60, 386), ingen knäck | `marginal` i `margin 12`, centrerad vid x = 60, baslinje y = 380 |

**Zonnamn utan ledare** (regeln: ett zonnamn som sitter **inuti** sin egen zon behöver
ingen ledare; ett som sitter utanför far en):

| Text | Placering |
|---|---|
| `spalt` | `margin 12`, centrerad vid x = 424, baslinje y = 224, alltsa inuti spaltavstandet |
| `fold` | `margin 12`, vänsterställd vid x = 48, baslinje y = 884, precis ovanför `#page-outline`s underkant. Foldens läge **är** arkets underkant, sa ingen egen foldlinje ritas: en linje som duplicerar en kontur är en linje utan roll |

**Summa stroke-banor i a1: 18.** Plus a3:s tre plate-ramar och a6:s fyra ramlinjer ger 25
för hela sidan, mot budgetens tak 60 (`concepts-K3.md` (5) Budget). Textnoder i ritningen:
14.

### A.6 Ritordningen — `stroke-dashoffset` ur `--sc-ps` i den pinnade akten

**Mekaniken.** Varje ritad bana far `pathLength="1"` som attribut. Det normaliserar banans
längd sa att **ett enda CSS-uttryck** fungerar för alla banor oavsett verklig längd, och sa
att rithastigheten blir jämn per bana i stället för per pixel:

```css
@property --l1 { syntax: "<number>"; inherits: false; initial-value: 0; }
/* ... en registrering per bana, --l1 till --l14 ... */

#page-outline {
  --l1: clamp(0, calc((var(--sc-ps) - 0.12) / 0.10), 1);
  stroke-dasharray: 1;
  stroke-dashoffset: calc(1 - var(--l1));
}
```

**`@property`-registreringen är obligatorisk, inte kosmetik.** `motion-smoothness.md`
§ Fault 1: *"`--sc-p` is an unregistered custom property. To CSS it is a string, so it never
interpolates."* En oregistrerad `--l1` gör `clamp()`-resultatet till en sträng och ritningen
stegar bana för bana. `--sc-ps` registreras redan av `sc-smooth.js`; lokalerna maste
registreras av sidan.

**F-014:** varje bana läser `--sc-ps`, aldrig `--sc-p`. Cue-opacitet pa utropen far läsa
`--sc-p`. `will-change: stroke-dashoffset` sätts bara medan `0 < ps < 1`.

**Fönstren.** `--sc-ps` löper 0 → 1 över hela a1 (`pin`, span 2,4, dwell 0,35). Ingen bana
överlappar en annan: **en linje at gangen**, vilket är vad s2 kräver.

| Steg | Element | `--sc-ps`-fönster | Skärm | Not |
|---|---|---|---|---|
| 0 | `#title-block` | statiskt | s1 | Ritas inte. Enda saken pa arket i 0 → 0,12. Detta är den författade tystnaden |
| 1 | `#page-outline` | 0,12 → 0,22 | s2 | Medurs fran övre vänstra hornet. Handen börjar där ögat redan star |
| 2 | `#cut-AA` med sina tva ben | 0,22 → 0,28 | s2 | Fran vänster till höger, sedan benen nedat. Bokstäverna `A` tonar in med `--sc-p` vid 0,27 |
| 3 | `#guide-col-a-l`, `#guide-col-a-r`, `#guide-gutter-r` | 0,28 → 0,36 | s2 | I ordning fran vänster, uppifran och ner, en at gangen |
| 4 | `#opening` | 0,36 → 0,44 | s2 | Medurs fran sitt övre vänstra horn |
| 5 | `#hatch-marginal` | 0,44 → 0,48 | s2 | **Undantaget:** ett `<pattern>` kan inte dash-ritas. Skrafferingen avslöjas med `clip-path: inset(0 calc((1 - var(--l5)) * 100%) 0 0)` pa dess `<rect>`, alltsa vänster till höger. Det är den **enda** banan pa arket som avslöjas med clip i stället for dash, och skälet star här sa att det inte kan spridas |
| 6 | `#ledger-1`, `#ledger-2`, `#ledger-3` | 0,48 → 0,55 | s2 | Uppifran och ner, en at gangen |
| 7 | `#dim-width` med `#ext-320` och `#ext-768` | 0,55 → 0,64 | s3 | Baslinjen dras vänster till höger, sedan de tva förlängningslinjerna, sedan stationsstrecken. Konturen `#page-outline` gar samtidigt ner till hårlinjevikt: `stroke-width: calc(1.5px - 0.75px * var(--l7))` — det är s3:s "konturen star stilla och gar ner till hårlinjevikt" |
| 8 | `#dim-gutter` | 0,64 → 0,68 | s3 | Utropet `7 rem` tonar in vid 0,67 |
| 9 | `#dim-row` | 0,68 → 0,72 | s3 | Utropet `96 px` tonar in vid 0,71 |
| 10 | `#lead-16-9` | 0,72 → 0,75 | s3 | Punkten sätts först, sedan dras ledaren utat. En ledare ritas alltid **fran malet mot etiketten**: det är riktningen ögat läser den i |
| 11 | `#lead-marginal`, `spalt`, `fold` | 0,75 → 0,78 | s3 | Zonnamnen, sist av utropen |
| 12 | Räknaren | 0,58 → 0,76 | s3 | `count`-devicen, motorns egen. `320` startar vid 0,58, `768` vid 0,64, `1440` vid 0,70, alla landade före 0,78. **`steps(1, start)`-tickning**, lanad ur `squarespace`s uppmätta motion language: siffran landar pa heltal, den glider aldrig. Den startar tom, inte pa 0, och far aldrig visa ett tal större än sitt mal |
| 13 | Öppningen fylls | 0,78 → 0,88 | s4 | `clip-path: inset(0 0 calc((1 - var(--l13)) * 100%) 0)` pa den levande wrappern: en svep uppifran och ner. Se § A.7 |
| 14 | Siffrorna faller | 0,88 → 1,0 | s4 | `transform: scale(calc(1 - 0.8333 * var(--l14)))` med `transform-origin` vid varje siffras egen baslinje, alltsa 72 px → 12 px. Färgen gar `--blue` → `--ink-hair` med `color-mix(in oklch, var(--blue), var(--ink-hair) calc(var(--l14) * 100%))`. **`font-size` ändras aldrig** — det hade kostat layout per frame. Vid `--l14` = 0,5 är siffran ~42 px och maste fortfarande läsas som en siffra; `?preview=mid` finns för just den kontrollen |

**Bakat.** Att scrolla uppat kör exakt samma uttryck baklänges: `--sc-ps` sjunker,
`--l`-lokalerna sjunker, linjerna suddas i omvänd ordning. Ingen bana har en enkelriktad
`transition` och ingen har en `animation`. Detta är vad `motion_probe` maste mäta i bada
riktningarna.

**Efter a1.** `#page-outline` och `#opening` star kvar som kontur; hela ritningen är den
grund a2 till a6 ligger pa. Ingenting suddas för att ge plats.

### A.7 Mask-in: hur Calyx hamnar innanför konturen med bläcket kvar som ram

F-010-principen: *innehallet maskas in i objektets verkliga öppning, materialet ligger kvar
ovanpa.* Konkret:

1. **En sanning om öppningens matt.** Fyra tal deklareras en gang, i `:root`:
   `--op-x: 480; --op-y: 240; --op-w: 880; --op-h: 495;`. `#opening`s `d`-attribut skrivs ur
   dem, och den levande wrappern positioneras ur dem:
   `left: calc(var(--op-x) / 1440 * 100%)`, `top: calc(var(--op-y) / 900 * 100%)`,
   `width: calc(var(--op-w) / 1440 * 100%)`, `height: calc(var(--op-h) / 900 * 100%)`.
   Talen finns aldrig pa tva ställen. Om de skulle drifta isär hamnar sajten utanför sin
   egen kontur, vilket är exakt det fel F-010 varnar för.
2. **Lagren.** `.opening-live` (HTML, innehaller `<iframe src="/sites/calyx.html">`) ligger
   pa `z-index: 1`. `<svg id="drawing">` ligger pa `z-index: 2` med
   `pointer-events: none` pa allt utom sina egna länkar (den har inga). **Bläcket ligger
   alltsa bokstavligt talat ovanpa den levande sidan**, och konturens 1.5 px `--ink` är en
   ram och inte en `border`.
3. **Svepet.** `clip-path: inset(0 0 calc((1 - var(--l13)) * 100%) 0)` pa `.opening-live`,
   uppifran och ner. Riktningen matchar läsordningen och motsäger inte handen: konturen
   ritades medurs och slutade i vänsterkanten pa väg upp, sa nästa rörelse fortsätter
   nedat.
4. **Ramen far aldrig efterbehandlas.** När `--l13` nar 1 tas klippet bort helt en gang av
   aktens slutkallback (`clip-path: none`), och `pointer-events` gar fran `none` till
   `auto`. Fran den punkten transformeras, tonas eller skalas ramen aldrig igen
   (PRODUCT.md § Operating Context: *"En ram som visats far aldrig transformeras eller tonas
   efterat. Den ska ga att använda."*). Innan `--l13` = 1 är `pointer-events: none` sa att
   ingen kan klicka pa en halvavslöjad sida.
5. **Gate 47.** Runt öppningen finns **ingen** ritad enhetsram: inget webbläsarfält, ingen
   flikrad, ingen adressrad, ingen trafikljusprick, ingen telefonbezel. Konturen bär
   måttlinjer och ett utrop (`16:9`), och det är vad som gör den till en öppning i en
   ritning i stället för en enhetsattrapp. Kontrollen ligger i `?preview=drawn`.

Samma konstruktion, med samma fyra-tal-regel, används för a3:s tre plates. Där ritas ramen
i en kort `reveal` utan `count` och utan `pin`: a3 är avsiktligt nedgraderad sa att sidan
har en topp och inte tre (`feel-and-fingerprint.md` § The peak).

### A.8 Den reducerade planschen under 768

`vector-effect` används inte, sa hårlinjen 0.75 skalas med arket. Vid 390 bred viewport blir
den 0.20 px, alltsa under en enhetspixel: halva ritningen skulle försvinna eller aliasa till
gratt. Svaret är inte att lata linjen bli sallad utan att **rita en annan plansch**:

| Viewport | `viewBox` | Vad som ritas |
|---|---|---|
| ≥ 1024 | `0 0 1440 900` | Hela inventariet i § A.5 |
| 768 till 1023 | `0 0 768 900` | `#page-outline`, `#cut-AA`, `#opening` (omräknad till 16:9 inom den smalare sidan), `#dim-width` med stationerna `320` och `768` (`1440` utgar: det talet gäller inte den här sidbredden), `#hatch-marginal`, `#lead-16-9`. Hjälplinjerna och liggarlinjerna utgar |
| < 768 | `0 0 320 640` | `#page-outline`, `#opening`, `#dim-width` med den enda stationen `320`, `#lead-16-9`. Ingen skraffering, ingen snittmarkering, inga hjälplinjer |

Regeln bakom tabellen: **en station visas bara pa en sida vars bredd den faktiskt beskriver.**
Det är därför reduktionen är sann och inte bara en förenkling. `--hair` höjs till `1px` under
768 sa att den ritade linjen aldrig hamnar under en enhetspixel; det är cellens enda
bredd-undantag och det skrivs som en egen rad i decision ledger av byggaren.

`[fylls i R1]`: byggaren skärper koordinaterna för de tva reducerade planscherna och
skärmbildar bada med `shoot.py` vid 390 och 320 innan R2 lämnas.

### A.9 Asset-lock per medieplats

Ingen av dessa är en generate-prompt. Formatet är `generation.md` § 5:s, ifyllt för ett
ritat system.

```
Asset role:    Sektionsritningen, handförfattad inline-SVG
Slot:          viewBox 0 0 1440 900, hela a1:s pinnade scen, en user unit = en CSS-px
               vid 1440x900
Art direction: Konturer, snittmarkering, hjälplinjer, skraffering, måttlinjer, ledare och
               utrop enligt inventariet i A.5. Tre linjebredder (0.75 / 1.5 / 2.5), en
               dash-form (4 3), en pilspetsform (#arrow, 9x3 sluten fylld triangel), ett
               utropsregister (Martian Mono i display 72 och margin 12). Bläck och
               hårlinje ur locken; blatt endast pa de tre måttsiffrorna
Avoid:         rektanglar som föreställer knappar; textblock eller gra staplar som ska
               "vara" text; lorem; navrad; formular; graf; sparkline; webbläsarram;
               flikrad; adressfält; telefonbezel; trafikljusprickar; varje siffra som inte
               är 320, 768, 1440, 7 rem, 96 px, 16:9, 26 900 eller 38 900; roterad text;
               en andra pilspetsform; en fjärde linjebredd; box-shadow; gradient; radie
```

```
Asset role:    Ritpapperstexturen, procedurell
Slot:          position fixed, inset 0, z-index -1, background-size 256px 256px,
               background-repeat repeat
Art direction: feTurbulence fractalNoise med stitchTiles="stitch", avmättad, alfa-tak
               0.055, över den plana --paper-färgen. Kall, lag chroma, ingen färgövergang.
               Rastreras en gang som data-URI-bild och animeras aldrig. Full spec i § B
Avoid:         en genererad kakling; en JPEG- eller PNG-fil; background-attachment fixed;
               filter: pa ett element; animation av baseFrequency eller seed; en textur som
               ändrar kontrasten mellan --ink och --paper med mer än 0.01 dL; synlig
               repetition; papperskorn i en varm ton
```

```
Asset role:    Calyx i den ritade öppningen, sidans signaturmoment
Slot:          rect x480 y240 w880 h495 i ritningens koordinatrum, 16:9, positionerad ur
               de fyra --op-*-talen
Art direction: sites/calyx.html live i <iframe> fran samma origin, monterad lazy av en
               IntersectionObserver, avslöjad med clip-path uppifran och ned mellan ps
               0,78 och 0,88. Konturen ligger kvar ovanpa pa z-index 2. Bildtexten är den
               ordagranna raden "Exempelsida: Calyx, florist i Stockholm" i margin 12
Avoid:         en skärmbild i stället för den levande sidan; en ritad enhetsram runt
               ramen; transform, opacitet eller filter pa ramen efter att den visats;
               pointer-events auto före ps 0,88; en ram som rivs ner när den lämnar vyn
```

```
Asset role:    Tre plates, a3, en per exempelsajt
Slot:          tre ritade ramar i 16:9, en per skärm (s6, s7, s8), var och en positionerad
               ur sina egna fyra --op-*-tal
Art direction: sites/calyx.html, sites/horai.html, sites/hyperborea.html live i <iframe>.
               Ramen ritas i en kort reveal (up), sedan wipeas sajten fram innanför den.
               Ingen count, ingen pin: a3 är avsiktligt nedgraderad mot a1. Bildtexterna är
               de tre ordagranna raderna i margin 12, som marginaletikett ovanför ramen
Avoid:         tre likadana ramar i ett rutnät; hover-tilt; en fjärde plate; en
               logotypremsa; kundnamn utover de tre; en ram som transformeras efter att
               den visats
```

```
Asset role:    Teckenförklaringen i vänstermarginalen, sidans enda nav
Slot:          sticky i vänstermarginalen, x 0 till 120 i ritningens koordinatrum, fem
               rader
Art direction: Varje rad är ett symbolprov plus ett kapitelnamn i margin 12: en hårlinje,
               en måttpil (samma #arrow), en skraffering, en kontur, en ledare. När ett
               kapitel blir aktivt ritas en ledarlinje fran dess rad ut till kapitlets egen
               kontur, 0.75, punkt i maländen, ~240 ms, driven av --sc-ps
Avoid:         en topprad; en pill; en CTA-knapp; färg som statusmarkör; hover-beroende
               status; en scroll-cue-text; ett folionummer som byter grad
```

```
Asset role:    Ordmärket i specifikationsramen, a6
Slot:          en förekomst, inuti a6:s ritade ram, övre vänstra hornet av ramen
Art direction: logo-black.svg inline, fill currentColor = --ink, ingen egen färg, ingen
               ram, ingen halo. Det är ritningens titelblock som ateruppstar i avslutet
Avoid:         ett andra ordmärke nagon annanstans pa sidan; logo-white.svg (sidan har
               ingen mörk grund); en glow; en hårlinjeram runt märket; ordmärket i
               displaygrad
```

---

## § B · Ritpapperstexturen som procedurell CSS/SVG

### B.1 Specen

```svg
<svg xmlns="http://www.w3.org/2000/svg" width="256" height="256" viewBox="0 0 256 256">
  <filter id="p" x="0" y="0" width="100%" height="100%"
          filterUnits="userSpaceOnUse" color-interpolation-filters="sRGB">
    <feTurbulence type="fractalNoise" baseFrequency="0.9" numOctaves="3"
                  seed="7" stitchTiles="stitch" result="n"/>
    <feColorMatrix in="n" type="saturate" values="0" result="g"/>
    <feComponentTransfer in="g" result="t">
      <feFuncA type="table" tableValues="0 0.055"/>
    </feComponentTransfer>
  </filter>
  <rect width="256" height="256" filter="url(#p)"/>
</svg>
```

Den SVG:n URL-kodas och används som `background-image` i CSS:

```css
.paper-texture {
  position: fixed; inset: 0; z-index: -1; pointer-events: none;
  background-color: var(--paper);
  background-image: url("data:image/svg+xml,%3Csvg ... %3E");
  background-repeat: repeat;
  background-size: 256px 256px;
  background-attachment: scroll;   /* aldrig fixed */
}
```

**Parametrarna, med skäl:**

| Parameter | Värde | Varför |
|---|---|---|
| `type` | `fractalNoise` | `turbulence` ger celliga klumpar som läser som marmor; `fractalNoise` ger den jämna kornighet ett ritark har |
| `baseFrequency` | `0.9` | Vid 256 px kakel ger det en kornstorlek pa ~1,1 px, alltsa korn och inte moln. Justeras i intervallet 0,8 till 1,0 mot pixelläsningen i B.3, aldrig utanför |
| `numOctaves` | `3` | Tva ger ett för rent brus, fyra kostar rastreringstid utan synlig vinst |
| `seed` | `7` | Fast. Ett slumpat seed gör bilden oreproducerbar mellan körningar och därmed omöjlig att sömkontrollera |
| `stitchTiles` | **`stitch`** | **Detta är hela poängen.** Filtret beräknar brusfältet sa att kaklets kanter fortsätter i varandra. Sömlösheten är en egenskap hos konstruktionen, inte ett resultat av en efterbehandling |
| `feColorMatrix saturate 0` | — | `feTurbulence` producerar färgat brus i alla fyra kanalerna. Utan avmättning far det kalla papperet färgade prickar, alltsa en andra kromatisk sak pa arket, vilket bryter accentregeln |
| `feFuncA tableValues "0 0.055"` | tak 0,055 | Alfa-taket. Över ~0,07 börjar bruset äta kontrast mellan `--ink` och `--paper`; under ~0,03 syns det inte pa en vanlig skärm |
| `background-size` | `256px 256px` | Kakelperiod. Kontrolleras i B.3 |

### B.2 Varför procedurellt och inte genererat

- **Sömlöshet genom konstruktion.** `stitchTiles="stitch"` gör kanterna kontinuerliga i
  filtrets egen beräkning. En genererad kakling maste i stället sömkontrolleras i efterhand
  (`game-textures.md` Fas 3), och även en tile med sömkvot ≈ 1,0 kan visa **repetition** som
  sömkvoten inte mäter alls.
- **Reproducerbarhet.** Fast `seed` ger identisk textur i varje bygge och varje skärmbild.
  En genererad fil ger det ocksa, men bara sa länge filen inte byts; en parameter i markup
  gar att läsa i en diff.
- **Kostnad.** ~700 byte markup mot en fil pa överföringsbudgeten.
- **Register.** `generation.md` § 1: i ett ritat register slar ett ritat system bade sourcad
  och genererad bild. K3 är det registret.
- **Kreditläget** bekräftar vägen men är inte skälet till den: 0 credits, free plan, matt av
  lead 2026-09-09.

### B.3 Sömkravet som en kontroll byggaren kör

Detta är inte en förhoppning. Det är tre steg med ett godkänt-värde vardera, och de körs
innan R2 lämnas. Resultaten skrivs in i `runs/K3/NOTES.md`.

**Steg 1 — extrahera kaklet som pixlar.** Skriv den raa `<svg>`-filen ovan till
`runs/K3/shots/paper-tile.svg`, öppna den i den lokala servern och skärmbilda den vid exakt
256 × 256 med `python skills/design/scripts/shoot.py --url http://localhost:<port>/tests/alunix-r8/runs/K3/shots/paper-tile.svg --width 256 --height 256 --out runs/K3/shots/paper-tile.png`.
Skärmbild, inte en biblioteksrendering: det är webbläsarens egen rastrering som kommer att
sitta pa sidan.

**Steg 2 — kakla minst 3 × 3, skjut bilden, läs den som pixlar.**

```bash
python - <<'EOF'
from PIL import Image
t = Image.open("tests/alunix-r8/runs/K3/shots/paper-tile.png").convert("RGB")
w, h = t.size
g = Image.new("RGB", (w*3, h*3))
for i in range(3):
    for j in range(3):
        g.paste(t, (i*w, j*h))
g.save("tests/alunix-r8/runs/K3/shots/paper-3x3.png")
# skjut halva kaklet i bada axlar sa att bada sömmarna hamnar i ett centrumkors
r = g.crop((w//2, h//2, w//2 + w*2, h//2 + h*2))
r.save("tests/alunix-r8/runs/K3/shots/paper-3x3-rolled.png")
EOF
```

Läs **bada** filerna med Read-verktyget, som pixlar. Godkänt: inga synliga vagräta eller
lodräta linjer i `paper-3x3.png`, inget centrumkors i `paper-3x3-rolled.png`, ingen
ljushetstrappa vid fogarna, inget igenkännbart mönster som aterkommer var 256:e pixel.

**Steg 3 — tva tal.**

*Sömkvot*, formeln ur `game-textures.md` Fas 3. Godkänt: **≤ 1,10.** (Filens egen
flaggniva är 1,3; K3 kräver hardare, därför att `stitchTiles` ska ge ≈ 1,00 och allt över
1,10 betyder att kaklet blivit omsamplat nagonstans i kedjan.)

```bash
python - <<'EOF'
import numpy as np
from PIL import Image
a = np.asarray(Image.open("tests/alunix-r8/runs/K3/shots/paper-tile.png").convert("RGB")).astype(float)
seam = abs(a[0]-a[-1]).mean() + abs(a[:,0]-a[:,-1]).mean()
base = abs(np.diff(a,axis=0)).mean() + abs(np.diff(a,axis=1)).mean()
print("seam_ratio", round(seam/base, 3))
EOF
```

*Repetitionstopp.* Sömkvoten mäter fogen, inte upprepningen. Läs rad- och
kolumnmedelvärdena över 3 × 3-bilden och kontrollera att det inte finns en periodisk topp
vid 256-pixelsperioden. Godkänt: **toppen vid period 256 ≤ 0,5 % av medelluminansen.**

```bash
python - <<'EOF'
import numpy as np
from PIL import Image
g = np.asarray(Image.open("tests/alunix-r8/runs/K3/shots/paper-3x3.png").convert("L")).astype(float)
for name, prof in (("rows", g.mean(axis=1)), ("cols", g.mean(axis=0))):
    p = prof - prof.mean()
    sp = np.abs(np.fft.rfft(p))
    k = round(len(p)/256)                      # index for perioden 256 px
    peak = sp[k-1:k+2].max() / (len(p)/2)
    print(name, "period-256 peak %", round(100*peak/prof.mean(), 3))
EOF
```

**Steg 4 — kontrasten far inte flytta sig.** Kör `python skills/design/scripts/contrast.py`
för `--ink` pa plan `--paper` och kör
`python skills/design/scripts/contrast_over_media.py --url <sidan>` för `--ink` pa den
texturerade grunden. Godkänt: skillnaden i dL **< 0,01**. Faller den utanför sänks
`tableValues`-taket, aldrig kontrasten.

**Steg 5 — prestanda.** Bekräfta i `perf_probe.py` att texturlagret inte förekommer bland
paint-posterna under scroll. Texturen rastreras en gang och animeras aldrig per frame:
ingen `animation` pa `baseFrequency`, `seed` eller `background-position`, ingen `transform`
pa lagret, ingen `will-change`, och `background-attachment` är `scroll` och aldrig `fixed`.

### B.4 Vad texturen inte far göra

Den far inte "andas" (avvisad kandidat i `concepts-K3.md` (5): TASTE § 3 product-focused,
*"Rörelse: subtil, aldrig breathing"*). Den far inte drifta i ton mellan akter — det gör
`--paper-fold` i a3 och a6, som är ett materialbyte i spalten och inte i grunden. Den far
inte ligga i en varm ton: papperet är kallt, AB09-lärdomen, last av lead.

---

## § C · Filer som ska kopieras in

Kontrollerat pa disk. `ls -l tests/alunix-concepts-r3/build/assets/logo-*.svg`:

```
-rw-r--r-- 1 Anton L 197121 3522 Sep  4 12:43 tests/alunix-concepts-r3/build/assets/logo-black.svg
-rw-r--r-- 1 Anton L 197121 3522 Sep  4 12:43 tests/alunix-concepts-r3/build/assets/logo-white.svg
```

| # | Roll | Källsökväg | Malsökväg | Finns |
|---|---|---|---|---|
| 1 | Ordmärket i a6:s specifikationsram, inline, `currentColor` = `--ink` | `tests/alunix-concepts-r3/build/assets/logo-black.svg` | `tests/alunix-r8/runs/K3/assets/logo-black.svg` | ja, 3 522 B |
| 2 | Motorn, JS | `~/.claude/skills/design/scripts/scroll/scrollcraft.js` | `tests/alunix-r8/runs/K3/scroll/scrollcraft.js` | ja |
| 3 | Motorn, CSS | `~/.claude/skills/design/scripts/scroll/scrollcraft.css` | `tests/alunix-r8/runs/K3/scroll/scrollcraft.css` | ja |
| 4 | Utjämningsshimen (`--sc-ps`) | `~/.claude/skills/design/scripts/scroll/sc-smooth.js` | `tests/alunix-r8/runs/K3/scroll/sc-smooth.js` | ja |
| 5 | Chivo, variabel `.woff2` | `[needs: vendor]` — lead hämtar och self-hostar | `tests/alunix-r8/runs/K3/assets/chivo-var.woff2` | nej |
| 6 | Martian Mono, variabel `.woff2` | `[needs: vendor]` — lead hämtar och self-hostar | `tests/alunix-r8/runs/K3/assets/martian-mono-var.woff2` | nej |

**Inte ärvda, med skäl:**

- `logo-white.svg` (3 522 B): K3 har ingen mörk grund nagonstans. Arket är kallt papper i
  alla sex akter, avslutet inverterar inte, och en vit logotyp har därför ingen yta att
  ligga pa. Kopieras inte.
- Alla `demo-*.webp`: K3 visar de tre sajterna **levande**. En skärmbild som reserv skulle
  vara en tyst väg tillbaka till en statisk platta, och beslutet att byta ut en ram mot en
  bild ska kosta ett leadbeslut, inte ett filbyte. Kopieras inte.
- Alla `k1-*` och `k4-*`-stillbilder: noll fotografier i cellen.
- Motorns `template.html`: läses av byggaren pa plats för stage-markupen, kopieras inte in.

**Öppet.** Posterna 5 och 6 är de enda `[needs: vendor]`-raderna i cellen. Nästa konkreta
steg: lead hämtar Chivo (Google Fonts, variabel) och Martian Mono (Google Fonts, variabel
bredd) som `.woff2`, kontrollerar att summan ligger under 300 kB och subsätter med
`pyftsubset` till latin plus `å ä ö Å Ä Ö` om den inte gör det. Byggaren far inte hämta dem
fran ett CDN vid körning: `performance.md` § 2 kräver self-hostade filer utan
`preconnect`.

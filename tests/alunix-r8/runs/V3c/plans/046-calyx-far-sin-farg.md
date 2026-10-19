# 046 · Calyx får sin färg i sista steget: mättnaden är en funktion av aktens progress

- **Status**: TODO (R12, loop 5)
- **Commit**: R10-läget av `runs/V3c/index.html`, md5 `d3491b4a`. **OBS:** en copy-agent
  arbetar i samma fil parallellt med att den här planen skrivs. Radnumren nedan är
  ungefärliga; hitta varje ankare med `Grep` på dess kod, aldrig på radnummer, och STOPPA
  (skriv i NOTES § R12) om koden inte matchar i sak.
- **Severity**: ingen (inte ett fynd). Antons beställning 2026-09-17: Calyx ska inte vara
  svartvit; den får vara gråskala under ritningsprocessen men ska få sin färg i den färdiga
  versionen i sista steget.
- **Category**: Visuellt / rörelse, processakten. Rör H-25 och H-33 i andan (en scroll-läst
  förändring till på aktens sista skärmar, och ett moment som drar sig tillbaka när
  ritningen blir sida). Öppnar ingen H-rad och får inte sänka någon.
- **Estimated scope**: 1 fil, **två `Edit`** (`href` och `filter`), plus ett villkorat
  tillägg i 045:s invert-block. Assetet är vendorat av lead 2026-09-17 och kontrollmätt av
  arkitekten: blockeraren är stängd.
- **Källor**: `index.html` rad ~952 till 954 (`.process-sheet .p-live`), ~1447 till 1449
  (`<g class="p-live">` och `<image id="p-live-img" … width="538" height="303">`), ~1097
  (`#p-live-img` vid den smala brytpunkten: 272x153), ~930 till 943 (`.measure`: tonbytet
  och skalan på `--k6`), ~960 (`#p-guides,#p-ledgers,#p-hatch` opacitet på `--k6`), ~954
  (`.contour` viktfall på `--k6`), ~968 till 985 (`#process`, `--s1..--e7` och `--k1..--k7`).
  Pixlar: `shots/loop-5/preview/preview-1440-process-05.png` och `-06.png`.
  Mätningar: `shots/loop-5/geom5.json`, `probe/`, och mätningen av assetet nedan.

## Assetet: vendorat och kontrollmätt

`assets/demo-calyx-1440-color.webp`, vendorat av lead 2026-09-17, omkodat ur
`board/cells/K4-r8/assets/demo-calyx-1440.webp` (originalet var färg; gråskalan i arbetsfilen
var leads egen omkodning för perf-fynd 6). Provenance i `assets/ASSETS.md`.

Arkitektens egen mätning av **båda** filerna, Pillow, 1 297 jämnt spridda pixlar:

| Fil | Storlek | Bytes | Mean chroma | Max chroma | Mean rel. luminans | p95 luminans |
|---|---|---|---|---|---|---|
| `demo-calyx-1440-color.webp` | 1076x606 | 79 178 | **20,69** | 129 | **0,545** | 0,941 |
| `demo-calyx-1440.webp` (grå, står kvar) | 1076x606 | 59 520 | 0,01 | 1 | 0,544 | 0,941 |

Två saker följer direkt ur tabellen och de styr resten av planen:

1. **Luminansen är i praktiken identisk** (0,545 mot 0,544, p95 0,941 mot 0,941). Färgfilen är
   samma bildruta med samma tonkurva; bara kulören skiljer. Grå-ekvivalenskontrollen (steg 2)
   ska därför passera med marginal, och stegen 01 till 05 ska se ut exakt som i dag. Gör de
   inte det är det ett fel i implementationen, inte i assetet.
2. **Invert-lägets risk är nu mätt på den riktiga filen, inte uppskattad ur den grå.**
   Mean luminans 0,545 mot `--c-black` (L ≈ 0,004) ger ≈ **11,0:1**. Bilden blir en lampa i
   ett mörkt fält om ingenting görs. Se § Båda lägena.

Den grå filen raderas inte: den är Target B:s basskikt och referensen för steg 2.

## Problem

```css
/* index.html ~952-954, som den står */
.process-sheet .p-live{
  clip-path:inset(0 0 calc((1 - var(--k5)) * 100%) 0);
  filter:grayscale(1) contrast(1.05);}
```

Mättnaden är en konstant. Allt annat i arket som rör sig läser aktens progress; den här
egenskapen gör det inte. Aktens tes säger något annat än bilden gör: steg 05:s not är
"Strukturen får sitt material. Ritningen blir er sida.", steg 06:s är "Bläcket står kvar som
ram. Ritningen och sidan är samma sak." Sidan blir alltså en riktig sida inne i akten, och
bilden påstår hela vägen att den fortfarande är ritningsmaterial.

## Target A (primär): mättnaden är en funktion av `--k6`

```css
/* target, samma deklaration */
.process-sheet .p-live{
  clip-path:inset(0 0 calc((1 - var(--k5)) * 100%) 0);
  /* PLAN 046: gråskalan är ritningens material; färgen kommer när ritningen
     blir sida. Samma fönster som resten av steg 06:s tillbakadragning
     (.measure tonbyte och skala, #p-guides/#p-ledgers/#p-hatch opacitet,
     .contour viktfall) - en gest i fyra egenskaper, inte fyra gester. */
  filter:grayscale(calc(1 - var(--k6))) contrast(1.05);}
```

Och `<image>`:s `href` byter till `assets/demo-calyx-1440-color.webp`.

Ingen JS per bildruta. Ingen `transition`. Ingen ny token (en `filter`-funktion är inte en
färg, så gate 48 gäller inte; ingen hex tillkommer).

### Varför `--k6` och inte `--k5` eller `--k7`

Läst i pixlarna, `preview-1440-process-05.png` mot `-06.png`:

| | steg 05 (`--k5` = 1) | steg 06 (`--k6` = 1) |
|---|---|---|
| Måtten 320 · 768 · 1440 | 44 px, i accent | 12 px, i `--hair-ink` |
| Hjälplinjer, liggare, skraffering | full opacitet | 0,35 |
| Konturens vikt | 1,5 px | 0,75 px |
| Bilden | ligger i öppningen, hel | oförändrad, men nu ensam auktoritet |

Vid 05 är ritningen som högljuddast: två 44 px-mått i accent väger ungefär lika tungt som
bilden på samma skärm. Färg där ger skärmen två dominerande element och river H-08 för just
den skärmen. Vid 06 drar sig **varje annan markering i arket tillbaka**. Färg exakt där är
samma gest i en fjärde egenskap: ritningen viker undan, sidan träder fram. Det är
ordagrant vad 06:s not säger.

Koden stagar dessutom redan auktoriteten i två takter, och 06 är den andra: `.measure`
opacitet är `calc(var(--p-t) * (1 - 0.3 * var(--k5)))` med kommentaren "TASTE § 4.8: bilden
är skärmens auktoritet" - alltså dämpas måtten redan när bilden landar vid 05. Färg vid 05
hade lagt båda takterna på samma slag. Färg vid 06 ger 05 = materialet kommer, 06 = sidan
är färdig.

`--k7` är förvaltningens fönster (revisionsfältet fylls, "En bokstav, aldrig ett datum").
Färg där påstår att sidan blir verklig under förvaltningen, vilket motsäger 06:s not.

**Följd som byggaren inte ska "rätta":** `--kN` är klamrad till 1 efter sitt fönster, så
`?preview=process-07` och allt scrollande därefter visar bilden i full färg. Det är rätt:
den färdiga sidan förblir färdig.

### Om `--kN` och `@property` (en rättelse till beställningens antagande)

`--k1` till `--k7` är **inte** `@property`-registrerade i den här filen, och de behöver inte
vara det. `@property`-listan är rad ~196 till 200 (`--p-l`, `--p-t`, `--p-thin`, `--p-fill`,
`--p-fall`) plus `--rv` (~680). `--kN` är normalt deklarerade (`#process`, ~971 till 977) och
substitueras textuellt in i `calc()`; det som måste vara registrerat för att kedjan inte ska
stega är `--sc-ps`, och det är det (shimen registrerar den som `<number>`, F-014).

Beviset ligger i filen: `--k6` driver redan `color-mix(… calc(100% * var(--k6)))` och
`scale(calc(1 - 0.7273 * var(--k6)))` på `.measure`, och `--k5` driver redan `clip-path:
inset(… calc((1 - var(--k5)) * 100%) …)` på **samma element som den här planen rör**. Alla
tre är mätt jämna: `#process:--sc-ps` max_step 0,67 % ned och 0,76 % upp vid cpu 1, staircase
0 (loop 5), och tolvstegssekvenserna visar kontinuerlig rörelse.

Registrera alltså **inte** `--k6` som en del av den här planen. Skulle mätningen ändå visa
stegning är registrering första spaken, och då gäller: **`inherits: true`**. `--kN` deklareras
på `#process` och ärvs av arkets alla barn; en registrering med `inherits: false` tar värdet
från varje barn och släcker hela ritningen.

## Vägvalet: Target A byggs, Target B är fallback. Skälet.

Två vägar finns, och att byta `href` mitt i akten är utesluten för båda (en andra hämtning
mitt i ett scrollfönster är en tom ruta i värsta fall och en ny dekodning i bästa).

**Target B, för fullständighetens skull:** två `<image>` i samma `<g class="p-live">`, den
grå underst med sitt nuvarande statiska `filter:grayscale(1) contrast(1.05)`, färgfilen
överst med `opacity:var(--k6)`. Bara opacitet animeras, och opacitet komponeras på GPU:n.

**Arkitektens beslut: bygg Target A.** Tre skäl, i fallande vikt:

1. **B lägger sin kostnad i det fönster som redan arbetar.** Båda bilderna ligger inne i
   `<g class="p-live">`, och gruppen bär `clip-path:inset(… var(--k5) …)`. Under steg 05
   animeras alltså klippningen, och med B animeras den över **två** raster i stället för ett.
   A lägger i stället sin kostnad i steg 06, ett fönster där `.p-live` i dag inte gör
   någonting alls. B ser billigare ut för att opacitet är billigt, men den flyttar arbete
   till den enda del av aktens liv som redan är upptagen.
2. **Sidvikten.** A kostar +19 658 B (59 520 → 79 178). B kostar +79 178 B, alltså båda
   filerna, 138 698 B, och sidan låg på 476 kB vid R9. Gate 93 och `performance.md` § 1
   gäller, och processakten är redan sidans tyngsta parti.
3. **A är två `Edit` och ingen ny DOM.** B lägger ett element, en z-ordning och en andra
   dekodning av en 1076x606-raster till ett 538x303-hål. `performance.md` § 3 har `filter`
   på listan över egenskaper som får animeras; A stannar inom den listan.

Mätningen nedan kan kullkasta beslutet och ska köras oavsett. **Bygg B bara om A faller på
gränsen.** Väljer byggaren B efter mätning gäller: den **grå** filen är basskiktet och den
som ska ladda först (den är det som syns vid `--k6` = 0, alltså genom hela steg 01 till 05);
färgfilen läggs ovanpå och får gärna dekodas senare, men måste vara klar innan `--s6`.

## Kostnaden: mät, med en gräns

Ett animerat `filter` på ett 538x303-raster (163 k px vid 1440, 272x153 = 42 k px vid 390)
filtreras om per bildruta i sitt fönster. `performance.md` § 3 har `filter` på listan över
egenskaper som får animeras, men samma element bär redan en `clip-path` som komponeras om
under `--k5`, så det här lägger ett pass till i ett angränsande fönster.

**Mätning, sammanflätad A/B, loop 4:s och loop 5:s metod:**

- Fönster: steg 06:s eget. Vid 1440 ligger `--s6` = 0,6335 och `--e6` = 0,7144 av akten;
  akten börjar sitt liv vid `scrollY` = `#process` top − vh = 5 340 − 900 = 4 440 och lever
  4 696 px, alltså ≈ scrollY 7 415 till 7 795. **Start 7 200, 18 ticks, 100:60.** Vid 390:
  `--s6` 0,6072, `--e6` 0,6905, liv 4 702 från 5 308, alltså ≈ 8 163 till 8 555; start
  8 000. Härled om talen ur `geom5.json` om geometrin har rört sig.
- **Ett andra fönster, steg 05**, som svarar på invändningen att A "lägger filtret på hela
  aktens liv": `--s5` 0,5444 till `--e5` 0,6177 vid 1440, alltså ≈ scrollY 6 997 till 7 341;
  **start 6 800, 12 ticks**. Där animeras klippningen och `--k6` står stilla på 0. A får inte
  vara mätbart dyrare än B i det fönstret; är den det är filtret inte gratis i vila och
  beslutet ovan faller.
- Spår: `#process:--sc-ps`.
- A = som byggd. B = filtret återinjicerat som konstant
  (`--pre` med `.process-sheet .p-live{filter:grayscale(1) contrast(1.05)!important;}`),
  alltså dagens beteende i samma session.
- **Tre par, omväxlande, med `tests/motion/smooth.html` ren omedelbart före varje par.**
  Median, inte enstaka körning. `shots/loop-5/scripts/probes5c.sh` är mallen.
- Redovisa cpu 1 och cpu 4, p95 och rutor > 33 ms, för A och B.

**Gränsen:** medianen för A får inte överstiga medianen för B med mer än **5 ms p95 vid
cpu 1**, och `#process:--sc-ps` ska ligga kvar på `max_step ≤ 3 %` och `staircase 0` i båda.
Håller inte gränsen: bygg Target B i stället och mät om den mot samma B-baslinje. Håller
inte heller den: **STOPPA, rapportera båda mätserierna, bygg ingenting**, och skriv i NOTES
§ R12 att beställningen kostar mer än det redovisade golvet tål. Det är ett ärligt utfall,
inte ett misslyckande.

Loop 5:s tal att ställa det mot: `#process` cpu 1 17,1 ms ned / 17,0 upp (14 respektive 13
rutor > 33), cpu 4 83,2 / 50,1 (140 / 85). Det redovisade golvet står i `HELHET.md` H-21,
H-22 och H-32.

## Båda lägena

Färgen ska komma i **både** pappersläget och `?process=invert` (plan 045). Target A ger det
gratis: `--k6` är samma i båda lägena och 045 rör bara färgtokens, inte `filter`.

**Risken i invert-läget är mätt på färgfilen själv, inte befarad.** Mean relativ luminans
**0,545**, p95 **0,941**. Mot pappersgrunden (#fdfbf4, L ≈ 0,94) är bilden mörkare än sitt
omland. Mot invert-lägets grund (`--c-black`, L ≈ 0,004) blir förhållandet ≈ **11,0:1**:
bilden blir en lysande fläck som tar skärmen från de sju styckena. Det är precis vad Anton
vill att vi kontrollerar.

**Målvärde i invert-läget:** bildrektangelns **mean relativ luminans ≤ 0,34** och **p95
≤ 0,80**, mätt på pixel i det renderade läget med `--k6` = 1 (`?process=invert&preview=
process-06`), vid 1440 och 390. Nås det inte av bilden som den är, dämpas den **bara i
invert-blocket**:

```css
:root[data-process="invert"] .process-sheet .p-live{
  filter:grayscale(calc(1 - var(--k6))) contrast(1.05)
         brightness(<mätt>) saturate(<mätt>);}
```

`brightness()` och `saturate()` är filterfunktioner, inte färger: ingen ny token, ingen hex.
Sänk `brightness` först (den flyttar luminansen, som är det som mäts), `saturate` bara om
bilden därefter läser som skrikig mot den mörka grunden. Skriv båda de valda talen och de
fyra uppmätta luminanserna (före/efter, 1440/390) i NOTES § R12. **Pappersläget dämpas
aldrig**: dess två luminanstal ska vara oförändrade.

**Talet 0,34 är en gräns, inte en dom.** Det är arkitektens, satt mot de uppmätta 0,545 och
inte mot en referens. Bygg mot det, men **lead dömer på de parvisa bilderna, inte på talet**,
och dämpningen ska vara **det minsta som får texten att behålla skärmen**. Är en
`brightness()` nära 1 nog för att de sju styckena håller blicken, är det rätt svar även om
0,34 inte nås; krävs mer än talet för att bilden ska sluta läsa som en lampa, är det också
rätt svar. Skriv i NOTES vilket som blev fallet och varför, så att lead dömer på underlag.

## Previews

`?preview=process-05`, `-06` och `-07` ska visa rätt mättnad i sitt eget steg, vid 1440 och
390, i **båda** lägena, alltså tolv lägen. Förväntat: 05 grå (`--k6` = 0), 06 full färg
(`--k6` = 1), 07 full färg (klamrad). Vid 06 mäts mättnaden, inte bara ögas: sampla
bildrektangelns **mean chroma** (max−min per pixel) i den renderade skärmbilden.
Förväntat: **05 ≤ 2, 06 och 07 ≥ 12**. Golvet är 12 och inte 20 därför att filens egna
20,69 mäts på 1076x606 medan `<image>` renderas i 538x303: nedskalningen medelvärdesbildar
grannpixlar och sänker chroman något. Samma tre tal i invert-läget (där en eventuell
`saturate()` sänker dem ytterligare; skriv talen, ändra inte golvet).

## Repo conventions to follow

- Motorn (`scroll/scrollcraft.js`, `scrollcraft.css`) och `scroll/sc-smooth.js` orörda.
  `sites/*.html` orörda (assetet skjuts av lead, inte av byggaren, och sidan redigeras inte).
- F-011: ingen `prefers-reduced-motion`, ingen statisk fallback.
- F-014: mättnaden rör sig för ögat och läser därför `--sc-ps` via `--kN`. Aldrig rå `--sc-p`.
- **Gate 47/79 står:** bilden är en riktig produktyta och får aldrig bli en ritad sida.
  Ingen `<path>` läggs till, ingen banräkning ändras, `pathLength="1"` orört.
- Gate 48 och 60: inga nya hex, inga värden ur demoterade skills. En filterfunktion är inte
  en färg; `brightness()`/`saturate()` är tillåtna utan token.
- Gate 93: sidvikten mäts om efter assetbytet och skrivs bredvid R9:s 476 kB.
- Låst copy (femton strängar) och de sju processtyckena orörda, i båda lägena.
- Radie 0 står. Inga nya element i Target A. Ett extra `<image>` bara i Target B.

## Steps

1. Kontrollera assetet mot tabellen i § Assetet: `assets/demo-calyx-1440-color.webp`,
   1076x606, 79 178 B, mean chroma ≈ 20,7 över minst 1 000 spridda pixlar. Avviker filen
   från tabellen: **STOPPA** (någon har bytt den).
2. Grå-ekvivalensen: rendera det nya assetet genom `grayscale(1) contrast(1.05)` och jämför
   bildrektangeln mot dagens rendering av det grå assetet i samma läge
   (`?preview=process-05`, 1440). **Mean |Δ| per kanal ≤ 6/255.** Faller det utanför har
   beskärningen eller tonkurvan ändrats och stegen 01 till 05 har tyst blivit en annan bild:
   **STOPPA** och rapportera talet.
3. Byt `href` till färgfilen och ändra `filter`-deklarationen enligt Target A. Två `Edit`,
   inget mer.
4. Mätningen och gränsen ovan, **båda fönstren** (steg 06 och kontrollfönstret steg 05).
   Faller gränsen: Target B, mät om mot samma B-baslinje.
5. Invert-lägets luminansmätning och, om den behövs, dämpningen.
6. Previews och ramsekvensen enligt Verification.

## Boundaries

- Rör inte `--k5`-klippningen, `<clipPath id="p-open">`, `<image>`:s `x`/`y`/`width`/`height`
  eller brytpunktsregeln vid ~1097. Bara `href` och `filter`.
- Registrera inte `--k6` (se Target A). Måste du ändå: `inherits: true`, aldrig `false`.
- Lägg ingen `transition` och ingen JS som skriver `filter` per bildruta.
- Ändra inget i steg 01 till 05:s ritordning, fönster eller banor.
- **`filter:grayscale(1) contrast(1.05)` finns på TVÅ ställen i filen.** Rad ~637 är
  `.thesis-photo-box img` (Hyperborea-plåten i tesbandet) och den rörs aldrig av den här
  planen. Ankaret är `.process-sheet .p-live` (~952) och ingenting annat. En `Edit` som
  matchar filterraden ensam träffar fel element: matcha hela regelblocket.
- Matchar inte ankarna i sak (copy-agenten arbetar i filen): **STOPPA**.

## Verification

- **Mekaniskt:** steg 1, 2, 4, 5; previewens chroma-tal (sex vid 1440, sex vid 390, båda
  lägena); `a11y_scan` 0 och `reflow.py` rent i båda lägena; sidvikten mot 476 kB;
  `grep` `prefers-reduced-motion` 0 och inline-hex-antalet oförändrat.
- **Skärmbilder, parvis, det lead lägger bredvid varandra för Anton:**
  - `shots/r12/papper/` och `shots/r12/invert/`, samma filnamn i båda:
    `?preview=process-05`, `-06`, `-07` vid 1440 och 390 (sex bilder per mapp).
  - **En tolvstegs ramsekvens genom övergången** vid 1440 i båda lägena
    (`shots/loop-5/scripts/frames.py life`-metoden, men begränsad till scrollY 7 200 till
    8 000 i tolv jämna steg), så att lead ser att mättnaden kommer jämnt och inte i ett
    hopp. Mät dessutom bildrektangelns mean chroma i varje ram och skriv de tolv talen:
    kurvan ska vara monoton och inget steg större än 20 % av totalspannet.
  - Hela sidan i skivor vid 1440 i båda lägena, så att steg 05 till 07 syns i sitt sammanhang.
- **Feel check:** hjul långsamt genom 7 200 till 8 000 och tillbaka upp: färgen kommer och
  går jämnt, och i uppåtriktningen tappar bilden sin färg i samma takt.
- **Done when:** färgen kommer i `--k6`:s fönster i båda lägena, kostnaden ligger inom
  gränsen (eller Target B gör det), invert-lägets två luminanstal ligger under målvärdet,
  och ingen H-rad i `HELHET.md` har sänkts.

## Vad jag själv ser i pixlarna

Beställningen är rätt läst mot akten: gråskalan ÄR ritningens material och bilden är den
enda ytan i arket som i dag inte deltar i aktens egen berättelse. Två saker att vara vaken på
när lead tittar på resultatet.

**Öppen rad, byggs inte bort i förväg:** färgen kommer i den skärm där allt annat tonas ned,
så skärmen får ett nytt centrum precis när den tappar sina gamla. Det är avsikten, men det
gör steg 06 till aktens starkaste skärm, starkare än steg 07 som är aktens slut. Om akten
därmed kulminerar en skärm för tidigt är det ett kompositionsfynd för Antons öga på boarden,
inte något den här planen ska kompensera för. Byggaren gör ingenting åt det och ska inte
försöka; raden står här för att lead ska veta vad han tittar efter i de parvisa bilderna.

Det andra är invert-läget, och det är det jag tror kommer kräva arbete. En färgbukett med
mean luminans 0,544 i ett fält på L ≈ 0,004 är inte en bild i ett mörkt rum, det är en lampa.
Målvärdet 0,34 är satt för att den ska läsa som en upplyst yta i stället, men talet är mitt
och inte uppmätt mot en referens: det är det första lead ska ifrågasätta med bilderna i
handen.

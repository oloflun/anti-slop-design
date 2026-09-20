# 061 · V3d: Blåkopian (övergången tes → ritning) och stegtexten i läsbar storlek

- **Status**: TODO (V3d R18, en byggrunda, högst två fixrundor). Byggs **efter** R17 (plan 060).
- **Beställning**: Anton 2026-09-19. (1) Kanten mellan det blå tesbandet och kapitelskärmen är
  "extremt platt": blått fält, fyra tickstreck, en rak kant, mörk grund. "Vi behöver fortfarande
  något där": en övergång med scrolleffekt, utan att någon rubrik någonsin halvklipps (057:s krav
  står kvar). (2) Processtegen i större text: kortare stegtexter från copy-agenten, typografin
  planeras så att texten blir det ögat dras till i varje fas.
- **Ordning**: steg 2 (stegen) först, eftersom `--band-h` och arkets bredd ändras av den och
  övergångens linjer läser arkets x-läge. Därefter steg 1. **Ett djärvt drag backas aldrig för att
  laga ett fel** (`runs/V3c/RAPPORT-LOOPEN.md` fel 5); följdfel lagas i samma runda.
- **Copy**: stegtexterna skrivs av copy-agenten i `runs/V3d/COPY-V3d-r18-steg.md` (12 till 22 ord,
  högst två meningar per steg). Byggaren skriver in kolumnen **final** ordagrant. **Finns filen
  inte när bygget når steg 2.3: STOPPA och vänta. Byggaren hittar aldrig på en sträng.** Steg 1
  har ingen copy alls (inga etiketter på linjerna, F-016).
- **Låst copy**: oförändrad mot R17 (12 synliga rader, plan 060). `Webbdesign, design och system.
  Allt på ett ställe.` står kvar ordagrant i `.process-locked`.
- **Estimated scope**: 1 fil, `runs/V3d/index.html`. `scroll/*.js`, `scrollcraft.css`, `sites/*`
  orörda. Ingen ny typsnittsfil (stegtexten står i den vendorade Public Sans 300). En ny token i
  `:root` (`--seam-on-blue`).
- **Underlag, läst som bilder denna session** (egen fångst, Playwright `mouse.wheel` en femtedels
  viewport per steg genom kanten, scratchpad `a061/`): 1920x930 (`w1920-03`, `-05`, `-08`),
  390x844 (`w390-05`), `?preview=process-03` vid 1920 och 390; referenserna
  `highway-1440/hw-hemsida-1440--s03`, `highway-390/hw-hemsida-390--s05`,
  `hoy-1440/hoy-home-1440--s02`, `insign-1440/insign-1440--s02`. Filen var mitt i R17 när den
  fångades; alla selektorer nedan verifieras med Grep efter R17 (§ Repo conventions).

## Uppmätt nuläge (R16/R17 under arbete)

| | 1920x930 | 1440x900 | 390x844 |
|---|---|---|---|
| Kanten | blått (`--c-accent`) med `--frame-line`-hårlinje rakt mot `--c-drafting`; inget annat händer när plåten lyfter (`w1920-05`) | samma | samma (`w390-05`) |
| Kant → kapitelrubrikens överkant | **392 px** tom mörk grund (`w1920-05`: rubriken ensam i nederkanten, 400 px tomt ovanför) | 391 px | 381 px |
| Fri blå yta ovanför kanten (fotots underkant → kanten) | 214 px | 344 px | 26 px (fotot fyller stagen) |
| Tickstrecken | x 96..254, 50 px ovanför kanten | x 86..244, 48 px | 588 px ovanför kanten (under meningen) |
| Arket (`.process-sheet`) | x 351, b 1218; stationerna 320/768 på x 622 och 1001 | x 136, b 1168; 396, 759 | x 16, b 358; 96, 207 |
| Stegbandet | `--band-h` 217; siffra 168 px, rubrik 52 px, text **17 px** i 672 px spalt, 78 % bläck (`p1920-process-03`) | 216; 168 / 51,8 / **17 px** | band i flödet; siffra 86, rubrik 32, text **17 px** |

Kapitlet är sedan R14 `min-height:120svh` i flödet direkt under tesen, så kanten och rubriken
rör sig tillsammans med konstant avstånd (057 B2). Det är därför rubriken aldrig halvklipps, och
det är också därför skärmen känns platt: det enda som händer över 392 px är att en kant glider.

## Problem

1. Kanten är ett materialbyte utan händelse. Blått upp, mörkt ned, och 400 px tom mörk grund
   innan rubriken kommer. Sidans idé (det blå är tesen, ritningen är hur vi arbetar) syns inte i
   kanten: ingenting förs över från det ena till det andra.
2. Stegtexten står i 17 px, 78 % bläck, fem rader i en 672 px spalt, bredvid en 168 px siffra och
   en 52 px versalrubrik. Ögat går till siffran och rubriken; texten läses som bildtext. Med
   marginalnoterna borta (R17) och kortare texter (12 till 22 ord) kan texten bära bandet.

## Idé: Blåkopian

Det blå är en blåkopia. När tesens plåt lyfter ritas ritningens egna linjer (arkets två kanter
och stationerna 320 och 768, på exakt de x-lägen där de står på arket i steg 01 till 03) i vitt
på det blå, korsar kanten utan avbrott och fortsätter som ritbläck ned över ritbordet. Där de
landar dras en vågrät linje, och under den bläcks kapitelrubriken in, vänster till höger. Samma
penna, samma fart, tre material: tesen blir ritning i ett drag.

Grepp lånat, inte pixlar: Highway (`hw-hemsida-1440--s03`) låter en scrollritad tråd leda in i
"Så arbetar vi"; vi tar tråden men gör den till ritningens egna konstruktionslinjer, i sidans
hårlinjeregister, utan prick och utan färg. Hoy (`hoy-home-1440--s02`) byter mättad grund mot
nästa kapitel; vi behåller bytet men syr ihop det.

## Target, en rad per beställningspunkt

Allt mäts i skärmbild (Playwright `mouse.wheel`, aldrig `scrollTo` utom i preview-hookarna) eller
`getBoundingClientRect`/`getComputedStyle` på den byggda sidan. `tx` = övergångens progress (steg
1.2), 0 när kanten står på 0,846 vh, 1 när den står på 0,208 vh.

| | Synligt mål | 1920x930 / 1440x900 | 390x844 |
|---|---|---|---|
| **1** | linjerna korsar kanten | `?preview=tes-till-ritning-2`: minst två av de fyra lodräta linjerna syns **både** över kanten (vitt på blått) och under den (bläck på mörkt), och pixelkolumnen på linjens x är obruten över kanten (±1 px i x, inget glapp > 2 px i y) | bara under kanten (ingen fri blå yta, se Beslut B3): fyra linjer, samma x som arket |
| **1** | linjernas x = arkets | linje N:s `left` = arkets motsvarande x (kant vänster, 320, 768, kant höger) **±1 px**, mätt mot `.process-sheet` i `?preview=process-03` | samma |
| **1** | lager i följd, ett drag | `tx` 0 → 0,30: blå del ritas uppifrån och ned till kanten; 0,30 → 0,75: mörk del från kanten ned till landningslinjen; 0,70 → 0,85: vågrät linje vänster → höger; 0,78 → 1: rubriken bläcks in (62 % → 100 %). Mätt: i `tes-till-ritning-1` blå del delvis, mörk del 0; i `-2` blå del hel, mörk del delvis; i `-3` rubriken delvis bläckt; i `-4` allt format | samma, utan blå del |
| **1** | formad skärm | `?preview=chapter` och `tes-till-ritning-4`: fyra lodräta linjer och den vågräta synliga, rubriken 100 % bläck, landningslinjen **40 px** ovanför rubrikens överkant (±2), ingen linje under den | samma |
| **1** | scrubbad, båda riktningarna | hjul 20 px-steg ned och upp genom kanten: `motion_probe` på `.process-chapter:--sc-ps` staircase 0, max_step ≤ 3 %; samma `scrollY` ned som upp ger samma bildruta (pixeldiff ≤ 1 % efter att `--sc-ps` satt sig) | samma |
| **1** | F-011 | grep `prefers-reduced-motion` 0 träffar; linjerna ritas oavsett OS-inställning | samma |
| **1** | ingen rubrik halvklippt | 057:s `elementFromPoint`-svep (`shots/r12/scripts/sweep.py`) hjul 20 px-steg hela sidan vid 1920, 1440, 768, 390: **0 träffar**. **Plus** en geometrisk kontroll, eftersom `elementFromPoint` hoppar över `pointer-events:none`: i varje bildruta är snittet mellan varje `.seam *`-rektangel och varje rubrikrektangel (`h1, h2, h3, .ts, .statement, .close-mailto`) tomt | samma |
| **1** | inget nytt ljud | inga etiketter, siffror eller bildtexter på linjerna (F-016); accenten `#1e5e9c` fortfarande exakt två förekomster; inga skuggor | samma |
| **1** | kontrast | rubriken vid `tx` 0 (62 % bläck på `--c-drafting`) ≥ 3:1; vid 1 ≥ 7:1 | samma |
| **2** | textens storlek | `getComputedStyle(.process-p).fontSize`: 1920 **32 px**, 1440 **28,2 px** (±0,5), 1280 ~26, 1024 24, 768 24 | 390 ~21,9 px, 320 ≥ 20 px |
| **2** | texten är fokus | full bläck (`color` = `--ink`, inte 78 %); textblockets yta ≥ 2× siffrans glyfyta i varje steg; i 5 px-oskärpa läses textblocket som bandets största ljusa massa (läst som bild, P07 till P13) | texten störst i steget under arket |
| **2** | hör ihop | rubriken i **samma storlek** som texten (Geist 700 versaler), direkt ovanför den i samma spalt; rubrikens överkant = siffrans versalhöjdslinje ±6 px; siffran oförändrad 168 px (P07 ≥ 150) | siffra 86, rubrik = text-storlek |
| **2** | mått | `.process-p` max 46ch; radantal (Range, `getClientRects` per rad) **≤ 4 vid 1440, ≤ 3 vid 1920** i alla sju steg | ≤ 7 rader |
| **2** | bandets höjd | `--band-h` **≤ 240 px** vid 1440x900 och 1920x930; varje `.step-band` `scrollHeight ≤ --band-h` (ingen text under bandets underkant) | – (bandet i flödet) |
| **2** | arket krymper inte under golvet | `.process-sheet` bredd ≥ **76 % vw** vid 1440x900 (P11) | oförändrat |
| **2** | ticker utan glyfspringa | hjul 20 px-steg ned och upp genom alla sju band vid 1920, 1440, 768: (a) pixelraderna mellan `--band-h` och arkets överkant är enfärgade `--bg` (luminansspridning ≤ 2 %) i **varje** bildruta; (b) högst två band har synlig area > 0 samtidigt, och när två syns har det inkommande `--slit-p` ∈ (0,1); (c) bytesbildrutorna 02→03 och 06→07 lästa som bild | 390: inga band, sticky ark; kontroll (a) mot arkets underkant: ingen glyf klipps av arkets bakgrund utom av arkets underkant |

## Beslut

**B1 · Övergången bor i kapitlet, med kapitlets egen klocka.** `.process-chapter` får
`data-sc-act="flow"`. Motorn räknar då `p = (y + vh − top) / (höjd + vh)` för just kapitlet och
`sc-smooth.js` publicerar `--sc-ps` på det (båda samlar `[data-sc-act]` generiskt; en nästlad
flow-akt i `#process` fungerar eftersom inga cues eller reveals finns i kapitlet och inget i
kapitlet läser `#process`:s `--sc-ps` i dag). Kapitlets höjd är exakt 120svh (R14), så livet är
2,2 vh och fönstret kan skrivas som konstanter: kant på 0,846 vh ↔ `p` 0,07, kant på 0,208 vh ↔
`p` 0,36. Ingen JS per bildruta, ingen ny mätning av klockan.
Vägt mot: (a) ett eget 0 px-element mellan sektionerna som akt: rubriken är då inte dess ättling
och får en andra klocka; (b) `#process`:s `--sc-ps` omräknad med `--seam-a/--seam-b` ur
`measureAct`: fungerar, men fönstret blir 3 % av ett 10 000 px långt liv och varje ändring i
stegens höjd flyttar det. B1 är minst kod och en klocka för alla tre lagren.

**B2 · Linjerna målar ovanför det blå.** Den blå delen står i `.process-chapter` men ritas
ovanför kapitlets överkant (`bottom:100%`). `#tes` har `z-index:2` (kvar från 054:s ridå) och
`.process` `z-index:1`; `.process` höjs till **3**. Inget annat överlappar: `#tes` och `#process`
möts bara i kanten sedan 057 B2, stagen är sticky inom `#tes`. Kontrolleras med pixeldiff (§
Verification B6).

**B3 · Den blå delen finns bara där det blå är tomt.** Per linje skriver `measureAct`
`--upN = 0` om linjens x ligger inom tickstrecken ±16 px (de fyra `i`-rektanglarna, inte
flexbehållaren) eller om den fria ytan (kanten − max(fotots underkant, alla fyra `.ts`
underkanter)) är < 64 px; annars `min(fri − 32, 22svh)`. Följd: 1920 alla fyra linjer (strecken 96..254 ligger väster om
dem); 1440, 1280 och 1024 tre linjer (arkets vänsterkant ligger inom strecken och får ingen blå
del); 768 och under: fri yta 49/26/21 px, **ingen blå del**, linjerna börjar i kanten. Det är
mobilens form, inte ett fel: på en smal skärm är det blå helt upptaget av meningen och Hyperborea.

**B4 · Streckform och bläck som arket.** Arkets kanter heldragna, stationerna streckade `4 3`
(`--contour-dash`), 1 px. Under kanten `--hair-ink` (arkets egna hjälplinjer, `#process`-skopet).
Över kanten ny token `--seam-on-blue: color-mix(in srgb, var(--c-white) 62%, var(--c-accent))`,
samma blandning som tickstrecken når när de tänds, så linjerna hör till tesens register och inte
till ett tredje. Linjerna **avslöjas med `clip-path`**, aldrig `scaleY` (streck skulle töjas).

**B5 · Rubriken bläcks in som stegrubrikerna redan gör.** Samma grepp som
`#process .step-band .process-step-title` (`--edge`-gradient, `background-clip:text`, 62 % → 100 %),
under `.js` så att no-JS visar full bläck. Ingen opacity, ingen letter-spacing-ändring (bredden
får inte ändras: rubriken bryts på två rader och ett radbyte mitt i övergången vore ett hopp).
`.process-locked` rörs inte.

**B6 · Linjerna står kvar.** Den formade kapitelskärmen har ritningens konstruktion i sin
övre halva, där det i dag är 392 px tomt. De scrollar bort med kapitlet; ingen uttoning.
Antagande, se Q1.

**B7 · Stegbandet: två spalter, rubrik och text i samma storlek.** Från 768 och uppåt:
`grid-template-columns:auto minmax(0,1fr)`, siffran i spalt 1 över två rader, rubriken rad 1 och
texten rad 2 i spalt 2. Rubriken och texten delar storleken `--step-fs`; rubriken bär vikten
(Geist 700 versaler), texten bär massan (Public Sans 300, fullt bläck, 3 till 4 rader). Siffran
behåller 168 px och sitt `--k`-grepp (P07). Så läses steget som en rad: **03 · DESIGN · texten**,
och texten är det största läsbara blocket. Vägt mot att behålla tre spalter (siffra | rubrik |
text): textspalten blir då 650 px vid 1440 och 28 px text ger 4 till 5 rader och `--band-h` ~250,
vilket tar arket under 76 % vw. Tvåspalt ger 710 till 810 px spalt och `--band-h` ~195 till 220.
768 till 1023-överstyrningen (`grid-row:3`) rivs: samma tvåspalt gäller där.

**B8 · Stegtextens skala.** `--step-fs: clamp(1.5rem, .5rem + 1.4vw, 2rem)` ≥ 768 (1024 24 px,
1440 28,2, 1920 32); under 768 `clamp(1.25rem, 1rem + 1.5vw, 1.375rem)` (320 20,8, 390 21,9).
`line-height:1.25` (text), `.95` (rubrik). Public Sans 300 är det enda vendorade snittet och bär
28 till 32 px väl; ingen ny fil.

## Steps

### 2 · Stegbandet (först)

2.1 CSS, ersätter `.step-band`s grid (i dag rad ~1131 till 1138) och `.process-step-title`/
`.process-p`-storlekarna (rad ~1142 till 1147):

```css
/* PLAN 061 B7. Två spalter: siffran | rubrik över text. Rubrik och text i
   samma storlek, texten är massan. INTE siffra | rubrik | 17 px bildtext. */
#process{--step-fs:clamp(1.5rem,.5rem + 1.4vw,2rem);}
.step-band{grid-template-columns:auto minmax(0,1fr);grid-template-rows:auto 1fr;
  row-gap:clamp(8px,1.2svh,14px);}
.step-band > .ledger-num{grid-column:1;grid-row:1 / span 2;}
.step-band > .process-step-title{grid-column:2;grid-row:1;}
.step-band > .process-p{grid-column:2;grid-row:2;}
.process-step-title{font-size:var(--step-fs);line-height:.95;letter-spacing:.01em;}
.process-p{font-size:var(--step-fs);line-height:1.25;max-width:46ch;}
#process .process-p{color:var(--ink);}
```

   Övriga egenskaper på `.step-band` (sticky, höjd, padding, kantlinje) står kvar. `column-gap`
   står kvar. `#process .process-p`s 78 %-regel (rad ~1425) ersätts av raden ovan.
2.2 Riv `@media (max-width:1023px) and (min-width:768px)`-blocket för `.step-band` (rad ~1149 till
   1157). Mobilen (`max-width:767px`, `.step-band{display:block}`) får
   `#process{--step-fs:clamp(1.25rem,1rem + 1.5vw,1.375rem);}`; `.ledger-num` mobilstorlek orörd.
2.3 Markup: de sju `p.process-p` får copy-filens **final** ordagrant. STOPP om filen saknas.
2.4 `measureAct` mäter `--band-h` som högsta `scrollHeight` (orörd kod). Kör `?preview=process-01`
   till `-07` vid 1920, 1440, 1024, 768, 390: landar som förut (varje `--sc-ps` ≥ `--eN`), och läs
   P07 och P10 som bild.
2.5 Mät: Target 2 (storlek, radantal, `--band-h` ≤ 240, arket ≥ 76 % vw). Går `--band-h` över
   240 vid 1440: sänk `row-gap` till 6 px och bandets övre padding till `clamp(16px,2.4svh,28px)`; räcker det inte, STOPP (§ Boundaries).

### 1 · Blåkopian

1.1 Markup, första barn i `.process-chapter` (före `#process-title`):

```html
<!-- PLAN 061. Blåkopian: ritningens egna linjer ritas ur det blå, korsar
     kanten och landar ovanför kapitelrubriken. INTE en ren kant, INTE en
     gradient mellan blått och mörkt, INTE etiketter på linjerna (F-016). -->
<div class="seam" aria-hidden="true">
  <i class="seam-up" data-l="1"></i><i class="seam-up dash" data-l="2"></i>
  <i class="seam-up dash" data-l="3"></i><i class="seam-up" data-l="4"></i>
  <i class="seam-dn" data-l="1"></i><i class="seam-dn dash" data-l="2"></i>
  <i class="seam-dn dash" data-l="3"></i><i class="seam-dn" data-l="4"></i>
  <i class="seam-h"></i>
</div>
```

   och `data-sc-act="flow"` på `div.process-chapter`.
1.2 CSS (nytt block efter `.process-locked`):

```css
/* PLAN 061 B1. Kapitlets egen klocka: kant på 0,846vh -> tx 0, på 0,208vh -> 1. */
.process{z-index:3;}                                   /* B2, var 1 */
.process-chapter{--tx:clamp(0,calc((var(--sc-ps,0) - .07) / .29),1);}
.seam{position:absolute;inset:0;pointer-events:none;}
.seam i{position:absolute;display:block;width:1px;}
.seam [data-l="1"]{left:var(--x1);} .seam [data-l="2"]{left:var(--x2);}
.seam [data-l="3"]{left:var(--x3);} .seam [data-l="4"]{left:var(--x4);}
.seam-up{bottom:100%;background:var(--seam-on-blue);
  clip-path:inset(0 0 calc((1 - clamp(0,calc(var(--tx) / .30),1)) * 100%) 0);}
.seam-up[data-l="1"]{height:var(--up1,0px);} /* ... --up2..--up4 likadant */
.seam-dn{top:0;height:var(--dn,0px);background:var(--hair-ink);
  clip-path:inset(0 0 calc((1 - clamp(0,calc((var(--tx) - .30) / .45),1)) * 100%) 0);}
.seam .dash{background:repeating-linear-gradient(to bottom,currentColor 0 4px,transparent 4px 7px);}
.seam-up.dash{color:var(--seam-on-blue);} .seam-dn.dash{color:var(--hair-ink);}
.seam-h{top:var(--dn,0px);left:var(--x1);width:calc(var(--x4) - var(--x1) + 1px);height:1px;
  background:var(--hair-ink);
  clip-path:inset(0 calc((1 - clamp(0,calc((var(--tx) - .70) / .15),1)) * 100%) 0 0);}
.js .process-title{--edge:calc(clamp(0,calc((var(--tx) - .78) / .22),1) * 130%);
  background-image:linear-gradient(100deg,var(--ink) 0 calc(var(--edge) - 12%),
    color-mix(in srgb,var(--ink) 62%,var(--bg)) calc(var(--edge) + 12%) 100%);
  -webkit-background-clip:text;background-clip:text;color:transparent;}
html:not(.js) .seam{display:none;}
```

   `:root` får `--seam-on-blue:color-mix(in srgb,var(--c-white) 62%,var(--c-accent));` (gate 48).
   `.process-chapter` har redan `position:relative`. Kontrollera att varken `.process`,
   `.chapter-hold` eller `.process-chapter` har `overflow` annat än `visible` (då klipps den blå
   delen); `main`s `overflow-x:clip` påverkar inte y.
1.3 JS, i `measureAct` (inom `if (process)`, efter att `--band-h` skrivits så att arkets mått är
   slutliga): läs `.process-sheet`s rect (`L`, `W`), `.process-chapter`s rect (`C`), `#process-title`
   (`T`), `.thesis-stage`, `.thesis-photo-box`, alla `.ts`, alla `.thesis-ticks i`. Skriv på
   `.process-chapter`:
   - `--x1..--x4` = `L`, `L + W·195,6/880`, `L + W·469,3/880`, `L + W − 1`, minus `C.left`, i px
     (arkets egna stationstal, samma som `#p-open`/måttkedjan);
   - `--dn` = `T.top − C.top − 40` px;
   - `--upN` enligt B3: `fri = stage.bottom − max(photo.bottom, max(ts.bottom))` (mätt i samma
     bildruta, stagen och kapitlet har samma koordinatsystem via `getBoundingClientRect`, men
     stagen är sticky: räkna `fri` som avstånd till stagens EGEN underkant, inte till kapitlet);
     0 om `fri < 64` eller om x krockar med strecken ±16 px, annars `min(fri − 32, 0,22·innerHeight)`.
   En gång per mätning, som `--band-h` och `--life`; aldrig per bildruta.
1.4 `?preview=`: nya lägen `tes-till-ritning-0` … `-4` (tabellen nedan). `curtain` (ridaY(50))
   visar nu `tx` ≈ 0,54 (mörk del på väg), `chapter` (ridaY(100)) formad skärm; båda oförändrade i
   kod.
1.5 Kommentarerna vid `.process` (rad ~1094 till 1101) och i markup (rad ~1661 till 1663) får en
   mening om 061: kanten är inte längre ren, den är sydd av linjer; rubriken fortfarande i flödet.

### `?preview=`-hookar

| Läge | Mål | Visar |
|---|---|---|
| `tes-till-ritning-0` … `-4` | `__scFreezeMotion`; `p = .07 + .29·K/4`; `scrollTo(0, C.top + scrollY − vh + p·(C.height + vh))`; vänta som `aimPin` tills `.process-chapter`s `--sc-ps` = `p` ± 0,002 (ny hjälpare `aimFlow(el, p)`, samma settle-slinga, flow-formeln i stället för pin-formeln) | `-0` kanten på 0,85 vh, inga linjer; `-1` blå del halvvägs; `-2` blå del klar, mörk del på väg; `-3` vågrät linje klar, rubriken halvbläckt; `-4` formad |
| `curtain`, `chapter` | oförändrade (ridaY 50/100) | se 1.4 |
| `process-01` … `-07` | oförändrade | nya band (steg 2) |

## Device-tabell

| Bredd | Blå del (B3) | Mörk del `--dn` | Linjernas x | Stegtext | `--band-h` (mål) |
|---|---|---|---|---|---|
| **1920x930** | fri 214 → `--up` 182 på alla fyra (x 351, 622, 1001, 1569 ligger alla utanför strecken 96..254) | 352 | 351 · 622 · 1001 · 1569 | 32 px, ≤ 3 rader, spalt ≤ 46ch | ≤ 240 (i dag 217) |
| **1440x900** | fri 344 → `--up` 198 (22svh) på 396, 759, 1304; **0** på 136 (inom strecken) | 351 | 136 · 396 · 759 · 1304 | 28,2 px, ≤ 4 rader | ≤ 240; arket ≥ 76 % vw |
| **1280x800** | fri 305 → `--up` 176 på 352, 675, 1159; **0** på 121 (strecken 77..235) | 307 | 121 · 352 · 675 · 1159 | ~26 px | ≤ 240 |
| **1024x768** | fri 352 → `--up` 169 på 262, 542, 961; **0** på 61 (strecken 61..219) | 306 | 61 · 262 · 542 · 961 | 24 px | mät; arket läses som bild |
| **768x1024** | fri 49 → **ingen blå del** | 473 | 46 · 196 · 407 · 721 | 24 px, tvåspalt (B7) | mät |
| **390x844** | fri 26 → ingen | 341 | 16 · 96 · 207 · 373 | 21,9 px under arket | – |
| **320x568** | fri 21 → ingen | 152 | 16 · 80 · 170 · 303 | 20,8 px | – |

Talen för x och `fri` är uppmätta i nuläget (R16/R17); efter steg 2 ändras arkets bredd något
(`--band-h`), så `measureAct` räknar, byggaren skriver aldrig in dem. Noll horisontell scroll 320
till 1920 (elementrektanglar, gate 34): linje 4 står på `L + W − 1`, innanför arket.

## Repo conventions

- **Selektorer att Grep-verifiera efter R17** (planen skrevs medan R17 byggdes): `.process-chapter`,
  `#process-title`, `.process-locked`, `.chapter-hold`, `.step-band`, `.step-band > .ledger-num`,
  `.process-step-title`, `.process-p`, `#process .process-p`, `.process-note` (**ska ge 0**),
  `.thesis-stage`, `.thesis-photo-box`, `.thesis-ticks i`, `.ts`, `.process-sheet`,
  `function measureAct`, `function ridaY`, `function aimPin`, `__scFreezeMotion`,
  `@media (max-width:1023px) and (min-width:768px)`. Radnumren i planen är R16/R17-läget; lita på
  selektorn, inte numret.
- Motorn och `sites/*` orörda; motorns `.sc-*`-klasser stylas aldrig. Ingen
  `prefers-reduced-motion` (F-011). Allt som rör sig läser `--sc-ps` (F-014), ingen `transition`
  på något som scrubbas.
- Kommentarer: varje nytt block börjar med `PLAN 061 N.` och en INTE-rad.
- Gate 48: `--seam-on-blue` i `:root`, ingen färg utanför token-blocket. Gate 75: inga tankstreck.
  Radie 0, inga skuggor. Accenten två förekomster.

## Boundaries (STOPPA och skriv i NOTES)

- `COPY-V3d-r18-steg.md` saknas, eller en stegtext har fler än 22 ord eller två meningar.
- `--band-h` > 240 vid 1440x900 efter 2.5, eller arket < 76 % vw.
- En stegtext kräver > 4 rader vid 1440 eller > 3 vid 1920 vid 46ch.
- Motorn eller `sc-smooth.js` publicerar inget `--sc-ps` på `.process-chapter` (nästlad akt
  fungerar inte): stoppa, ändra inte motorn; lead väljer mellan B1:s alternativ (a) och (b).
- Den blå delen syns inte ovanför kanten trots `z-index:3` (något klipper eller målar över).
- Svepet eller den geometriska kontrollen hittar en linje över en rubrik.
- Någon `?preview=process-0N` landar inte på sitt `--eN` efter steg 2.

## Verification

**A. Synligt, det som avgör.** `PARITET.md` P04 (omskriven) och P07 till P13: par-bilder vid 1440
och 390 i `shots/r18/par/`, lästa som bilder. P04 skjuts dessutom som **fem bilder**
(`tes-till-ritning-0` … `-4`) vid **1920x930** och 390x844. Lead läser själv P04 vid 1920 och 390,
och P07/P10 vid 1920, innan rundan räknas klar.

**B. Mätt.**
1. **Hjulsekvens 20 px båda riktningar** vid 1920x930, 1440x900, 768x1024, 390x844: från
   `ridaY(-40)` (tesen pinnad, mening 4) till `ridaY(140)` och tillbaka, en skärmbild per 5:e steg
   och vid varje `tx`-gräns (0,30 / 0,70 / 0,78). Kontaktark per bredd, läst som bild.
2. `motion_probe.py --url …/index.html --track ".process-chapter:--sc-ps" --wheel 20:120` ned och
   upp: staircase 0, max_step ≤ 3 %, frame p95 ≤ 20 ms vid cpu 1. Samma `scrollY` ned/upp →
   pixeldiff ≤ 1 %.
3. **Rubriktäckning**: `shots/r12/scripts/sweep.py` (057 B2) hela sidan, 20 px-steg, fyra bredder →
   0 träffar. **Kör den först mot en injicerad trasig variant** (`.seam-dn{height:150vh}` via
   `add_style_tag`, så att linjerna korsar rubriken): den geometriska kontrollen ska slå till,
   annars mäter den fel. Sedan den riktiga sidan: 0.
4. Linjernas x mot arkets (±1 px) i `process-03`; blå delens och mörka delens kolumn obruten över
   kanten i `tes-till-ritning-2` (pixelkolumn, glapp ≤ 2 px).
5. Stegen: font-size per bredd; radantal per steg (Range); `--band-h`; `scrollHeight ≤ --band-h`;
   arkets bredd/`innerWidth` vid 1440; textblockets yta mot siffrans; glyfspringekontrollen (a)
   och (b) i Target 2, 20 px båda riktningar vid 1920, 1440, 768.
6. Pixeldiff mot R17 för `?preview=front`, `thesis-01` … `-04`, `cases`, `case-calyx-01`, `pris`:
   oförändrade (B2:s z-index får inte flytta något).
7. Låst copy 12/12; `.process-note` 0; F-016-skanning (`microtext_scan.py`) inga nya fynd.

**C. Grinden.** `scroll_verify` 1440 och 390 (inga nya `blankBands`: kapitlets övre halva har nu
linjer); `a11y_scan` + `reflow` vid 390 och 1440 (`.seam` `aria-hidden`, rubriken fortfarande
`h2`, kontrast rubrik vid `tx` 0 ≥ 3:1); `tab_walk`; grep `prefers-reduced-motion` 0; noll
horisontell scroll 320 till 1920.

**Done when:** varje Target-rad har ett uppmätt värde som når målet, täckningssvepet och den
geometriska kontrollen är 0 vid fyra bredder, P04 och P07 till P13 håller nivån i sina
par-bilder, och grinden är ren eller varje avvikelse namngiven.

## Frågor till Anton (bygget stoppar inte; antagandet gäller tills svar)

| # | Fråga | Antagande |
|---|---|---|
| Q1 | Linjerna står kvar på kapitelskärmen när de ritats (ritningens konstruktion ovanför rubriken), eller tonas de bort när rubriken är bläckt? | Står kvar (B6) |
| Q2 | Kapitelrubriken kommer upp i 62 % bläck och bläcks in först när linjerna landat. Ok att den är dämpad de första ~300 px? | Ja; ≥ 3:1 hela vägen |
| Q3 | Stegrubriken krymper från 52 till samma storlek som texten (28 till 32 px) så att texten blir fokus. Siffran behåller 168 px. Ok? | Ja |

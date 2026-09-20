# 057 · V3d: Hyperborea som huvudperson, ridån som ren kant, case-rubriker, prisbron, ramar utan rullningslister, fyra meningar

- **Status**: TODO (V3d R12, en byggrunda, högst två fixrundor)
- **Beställning**: Anton 2026-09-19 ("ser bra ut på det stora hela, men…"), punkterna 1 till 5,
  plus punkt 6 (tillägg samma dag via koordinatorn). Golvet, inte ett förslag.
- **Ordning**: visuellt först, punkterna i Antons ordning. **Ett djärvt drag backas aldrig för att
  laga ett fel** (`runs/V3c/RAPPORT-LOOPEN.md` fel 5); följdfel lagas i samma runda.
- **Copy**: case-rubrikerna (punkt 3) och prisbron (punkt 4) skrivs av copy-agenten i
  `runs/V3d/COPY-V3d-case-v1.md`. Byggaren skriver in dem ordagrant. **Finns filen inte när
  bygget når steg 3 eller 4: STOPPA och vänta. Byggaren hittar aldrig på en sträng.**
- **Låst copy**: Anton har uttryckligen strukit `VI BYGGER ERT VARUMÄRKE.` från V3d (punkt 6,
  redan noterat i `tests/alunix-r8/PRODUCT.md` rad 105). Låst-copy-kontrollen räknar därför
  **14 rader, inte 15**. Den strykningen är det enda undantaget; alla andra låsta strängar står
  ordagrant.
- **Estimated scope**: 1 fil (`runs/V3d/index.html`) + två typsnittsfiler i `runs/V3d/assets/fonts/`
  (punkt 3, se Q2). `sites/*`, `scroll/*.js`, `scrollcraft.css` orörda. Ingen ram transformeras.
- **Underlag, läst som bilder denna session** (egen fångst, `mouse.wheel`, scratchpad `a057/`):
  hela sidan vid **1920x930** (69 skärmar, 465 px/steg), 1440x900 (450 px/steg), 390x844
  (422 px/steg); ramarna med **riktiga rullningslister** (`ignore_default_args=['--hide-scrollbars']`)
  vid 1920 och 390, med och utan `scrolling="no"`; referenserna `hoy-home-1440--s01`,
  `hoy-webb-1440--s02`, `hoy-home-1440--s08`.

## Uppmätt nuläge (R11)

| | 1920x930 | 1440x900 | 390x844 |
|---|---|---|---|
| Hyperborea-plåten | 725x453 = **37,8 % vw**, topp y 394, botten 847, flush höger | 534x334 = 37,1 % vw, topp 484 | 343x483, under meningen (R9 till R11) |
| `.ts` font-size | 96 px | 88 px | 35,5 px |
| Ridån | vid scrollY 7905 står stagens underkant på y 372; kapitelrubriken står på 262..500: **110 px av rubriken under blått**, "lanserad sida." syns ensamt under kanten (`a057/w1920/1920-0017.png`) | samma fel, rubrik 265..472, kant på 360 | samma fel, rubrik 273..442, kant på 338 (`w390/390-0017.png`) |
| Ramarnas rullningslister | Calyx och Hōrai: `clientWidth` 1215 mot `innerWidth` 1230 = **lodrät list 15 px** i båda | (samma mekanism) | Calyx `scrollWidth` 384 > `clientWidth` 365, Hōrai 675 > 365: **vågrät + lodrät list** (`a057/sb-default-case-horai-390.png`) |

**Varför elva rundor missade punkt 5:** headless Chromium startas med `--hide-scrollbars`. Varje
fångst i R1 till R11 var headless, så listerna fanns aldrig i en enda skärmbild. Med flaggan
bortslagen syns de direkt. All verifiering av punkt 5 görs därför utan den flaggan.

## Problem

1. Hyperborea sitter lågt i högra hörnet (topp 394 av 930 vid 1920, botten 847) och är 37 % av
   bredden; den läses som en bildtext till meningen, inte som en jämbördig bild. Hoy, vår
   referens för skärmen (`hoy-home-1440--s01`), gör motsatsen: bilden är 44 % vw, har **samma
   överkant som rubriken** och står fri från kanten med samma luft höger som vänster.
2. Ridån (`.process-chapter` sticky under en blå stage som lyfter) klipper kapitelrubriken i
   mitten i varje bredd. Den sticky rubriken står still medan kanten sveper över den; det går
   inte att undvika med en statisk rubrik under en rörlig kant.
3. `Calyx` och `Hōrai` är ett platt ord i Geist 120 px. Rubriken säger inget om caset och
   skiljer inte de två sajterna åt; det gör bara ramen.
4. Hōrai-caset slutar på svart plåt och priset börjar direkt på fotot: en hård kant och sedan
   "Alla har rätt till bra design." utan förberedelse (`1920-0065.png`). Det finns ingen bro
   från "så gjorde vi" till "så mycket kostar det".
5. Native rullningslister i ramarna, vid alla bredder, i en riktig webbläsare.
6. Tesbandet har fem meningar; Anton vill att det slutar på "Vi hjälper er att synas på rätt sätt."

## Target, en rad per beställningspunkt

Allt mäts i skärmbild (Playwright `mouse.wheel`, aldrig `scrollTo`) eller
`getBoundingClientRect`/`getComputedStyle` på den byggda sidan. "≥ 1024" betyder 1024, 1280,
1440 och 1920.

| | Synligt mål | 1920x930 / 1440x900 | 390x844 |
|---|---|---|---|
| **1** | Hyperborea-plåtens bredd | **≥ 45 % vw** (1920: ~908 px = 47,3 %; 1440: ~660 px = 45,8 %). Samma andel vid 1280 och 1024 | oförändrad från R11 (pixelidentisk, se 6 för texten) |
| **1** | plåtens överkant = meningens överkant | `photo.top` − `.ts(aktiv).top` inom **±8 px** i alla fyra meningarna (meningarna hänger från samma linje, bilden står där) | oförändrat |
| **1** | plåten står fri från kanten, full ram | höger luft = `--rail-x` (±1 px), `border-right` synlig, ingen bleed | oförändrat |
| **1** | plåten står still | `photo.top` spridning **0 px** genom hela pinnen, 20 px-steg ned och upp | R11:s 0 px behålls |
| **1** | meningarna lika stora, ingen ordbrytning | alla fyra `.ts` samma font-size per bredd: 1920 **96 px**, 1440 **~77 px**, 1280 ~68, 1024 ~55 (se beslut B1); rubrikskriptet (R3) 0 delade ord vid 1024/1280/1440/1920; widest ord (`ARGUMENTET.`) ryms i spalten med ≥ 8 px marginal | R11 oförändrat |
| **1** | 768 till 1023 | R11-geometrin orörd (`.7fr`, bleed), pixelidentisk mot R11 med undantag av att mening 5 och tick 5 är borta | – |
| **2** | ingen rubrik halvklippt av en annan yta | i en hjulsekvens med **20 px-steg** genom hela sidan vid **1920, 1440, 768, 390**: **0 bildrutor** där en rubrik (listan i § Verification B2) har en synlig punkt vars `elementFromPoint` är ett element utanför rubrikens egen sektion | samma |
| **2** | kanten tes → kapitel | tesens `border-bottom` (`--frame-line`) och kapitelskärmens ritbordsgrund möts utan glapp: stagens underkant = `.process-chapter` överkant ±1 px i varje bildruta där båda syns | samma |
| **2** | kapitelskärmen | `?preview=chapter`: kapitlet äger hela viewporten, rubriken ≥ 100 px vid 1440, inget blått och inget av band 01 synligt | rubrik ≥ 56 px |
| **3** | case-rubrik i två delar | `h2.case-title` = namnet i sajtens egen displayröst (Calyx: Cardo kursiv; Hōrai: Cinzel versaler) + copy-agentens rad på 3 till 8 ord i Public Sans 300. Båda i samma `h2` | samma, mindre skala |
| **3** | namnens storlek | båda namnen spänner **samma mått** (90 % av textspalten ±4 %, tak 9 rem); Calyx ~144 px, Hōrai ~80 px vid 1440 | namn 36 px |
| **3** | raden | font-size 1440: ~37 px, 1920: 44 px; högst 4 rader; max-width 20ch | 17 px, högst 3 rader |
| **3** | allt ryms | `.case-text` innehåll inom stagen minus padding i **alla steg** vid 1920x930, 1440x900, 1280x800, 1024x768 (ingen text under stagens underkant, ingen text över) | sista glyfen i `.cs p` ≤ stagens underkant − 8 px i alla steg vid 390x844 och 375x812, annars STOPP (§ Boundaries) |
| **4** | prisbron finns | `section.price-bridge#bro` direkt efter `#case-horai` och direkt före `#pris` | samma |
| **4** | grunden | överkant = `--c-black` (samma som Hōrais stage: 0 px kant, ΔE 0); underkant = exakt `#pris`-övergångens scrim: pixelrad 2 px ovan och 2 px under skarven `#bro`/`#pris` skiljer sig **≤ 2 %** i luminans (ingen synlig kant) | samma |
| **4** | skala | rubrik i tesrösten: Geist 700 versaler, **samma clamp som `.ts`** (1920 96 px, 1440 88 px); stycket 20 px; mikroraden 15 px | rubrik 35,5 px |
| **4** | rörelse | en hårlinje i prisliggarens bredd (`min(100%,1040px)`) dras in på `--sc-ps` och står färdig innan `.statement` når viewportens övre halva; delad reveal på text | samma |
| **4** | luft före priset | avstånd bronns hårlinje → `.statement` överkant **35 till 60 svh** (fotot får andas, inte ett tomt band) | samma |
| **4** | kontrast | varje sträng i bron ≥ 4,5:1 (rubriken ≥ 3:1) mätt med `contrast_over_media.py` mot den renderade grunden, ljusaste 5 % | samma |
| **5** | inga rullningslister | i en riktig (inte headless-dold) Chromium: i båda ramarna `clientWidth === innerWidth` och `clientHeight === innerHeight`, vid 1920/1440/1280/1024/768/390/320, i `case-*-01`, `-03` och sista steget; och skärmbild utan list | samma |
| **5** | synken fungerar | `?preview=case-calyx-0N`/`case-horai-0N`: ramens `scrollY` = ankaret ±2 px; hjulsekvens 20 px-steg: ramens `scrollY` monoton ned och upp | samma |
| **5** | 1920 i helhet | varje skärm i en hjulsekvens (465 px/steg) vid 1920x930 läst som bild: inget tomt band > 60 % vh, inget element som ser trasigt ut, och Calyx-ramens vänsterkant (se steg 5.3) ren | – |
| **6** | fyra meningar | exakt 4 `.ts` och 4 `.thesis-ticks i`; `VI BYGGER ERT VARUMÄRKE.` = 0 träffar i `document.body.innerText` | samma |
| **6** | samma takt per mening | tesens pinnade scroll per mening oförändrad (**0,9 vh**, 810 px vid 1440): `data-sc-span` 5,5 → **4,4** | samma |
| **6** | förhandslägen | `?preview=thesis-01` … `-04` visar mening N ensam; `thesis-05` finns inte | samma |

## Beslut

**B1 · Hyperborea följer hoy: fri från kanten, överkant i linje med meningen, 1fr/1,2fr, från 1024.**
Hoy (`hoy-home-1440--s01`) sätter bilden på 44 % vw, överkant = rubrikens överkant, lika luft
höger och vänster. Antons "bleeder ut" läses som en del av felet, och sidan har redan sitt
gridbrott i casen (Calyx-ramen möter högerkanten, Hōrai vänsterkanten), så tesen behöver inte
bära ett till. Top-linjering i stället för centrering: meningarna är 2 till 5 rader höga; en
gemensam överkant låter varje mening hänga från samma linje som bilden, och ingenting flyttar
sig när meningen byts (centrering skulle flytta textblockets överkant vid varje byte).
**Kostnaden, namngiven:** med 45 % bild och full `--rail-x` på båda sidor blir textspalten vid
1440 ~550 px. Det bredaste ordet, `ARGUMENTET.`, är uppmätt 6,82 em (600 px vid 88 px). Meningens
storlek begränsas därför av spalten: `min(clamp(…), 14cqi)` ger ~77 px vid 1440 (i dag 88), 96 px
vid 1920 (oförändrat). Hoys rubrik på samma skärm är ~80 px. Alternativet, att behålla bleed
och 88 px, står som Q1.
Scope ≥ 1024: vid 768 till 1023 skulle samma andel ge ~41 px meningar; där behålls R11:s
geometri orörd. Under 768 orört (R9 till R11:s mobillösning; Anton: "behåller … om den inte
blir sämre").

**B2 · Ridån blir en ren materialkant. Kapitlet är inte längre sticky.**
Varje variant där kapitelrubriken står still under en rörlig blå kant korsas av kanten; det är
geometri, inte en bugg att laga. Tre vägar vägda:

| | Sticky kapitel + rubriken tänds när stagen lämnat (`--sc-ps`) | Sticky kapitel + CSS `animation-timeline: view()` | **Kapitlet i flödet direkt under tesen** |
|---|---|---|---|
| Halvklippt rubrik | ja, uppåt: shimens lerpade `--sc-ps` ligger efter verklig scroll, så rubriken är fortfarande tänd när stagen glider ned över den | nej | **nej, per konstruktion**: rubriken följer kanten upp med konstant avstånd |
| Husregler | F-014 ok | bryter F-014 (rå scroll, trappsteg per hjulklick, F-013) | inget rörligt alls |
| Tomt band | risk (1 vh ritbord utan innehåll medan stagen lyfter) | samma risk | nej |
| Kod | JS + två mått i `measureAct` | CSS | **tar bort kod** (margin −100svh, 240svh-hållaren, sticky) |

Valt: kapitlet i flödet. Den blå plåten lyfter och drar ritbordet med sig; kapitelrubriken
står centrerad på sin egen skärm och kommer upp ur viewportens underkant (klippt av
viewporten, aldrig av en annan yta). Kanten är tesens hårlinje, som i dag. Det är Antons första
exempel ("kapitelskärmen syns först när ridån helt lämnat") i den enda form som håller i båda
riktningarna.

**B3 · Case-rubriken: namnet citerat i sajtens egen röst, raden i Alunix statementröst.**
- Namnet sätts i sajtens egen displayröst, ordagrant som sajten själv sätter det: Calyx-sajtens
  ordmärke är Cardo kursiv (`sites/calyx.html` rad 9 och headern i `1920-0042.png`), Hōrais är
  Cinzel i versaler med spärr (`sites/horai.html` rad 42 och 107). Namnet är ett **citat ur
  exempelsajten**, samma sak som ramen bredvid: det visar att Alunix ger varje verksamhet en
  egen röst, i stället för att säga det. Det är den enda platsen två främmande familjer får stå,
  exakt ett ord var.
- Raden (copy, 3 till 8 ord) står i Public Sans 300, samma röst som heron och
  "Alla har rätt till bra design.", i fullt bläck. Tre röster i caset, var och en med sin
  roll: serifnamnet (vems sida), den lätta raden (vad vi gjorde), stegen i Geist 700 versaler
  (hur). Två tonalt mixade delar i samma `h2` (house-physics: two-tone inside the headline),
  utan kursiv i en sans (gate 38a: kursiven är Cardo-snittets egen, i en serif, sajtens
  signatur).
- Namnen får **samma bredd**, inte samma storlek: Cardo kursiv `Calyx` är ~2,3 em, Cinzel
  `HŌRAI` med spärr ~4,2 em. Lika storlek skulle göra Hōrai dubbelt så brett som Calyx; lika
  bredd ger lika tyngd i spalten.
- Ingen ny färg. Namnet står i `--ink` (papper) respektive `--c-paper` (svart plåt); accenten
  (`#1e5e9c`) stannar på två förekomster. Monobudgeten orörd (inget nytt mono).
- Löpande index ("1 av 2"): möjligt i kickern `Exempelcase`, men det är en sträng; copy-agenten
  avgör (Q3). Planen lämnar kickern som den är om copy-filen inte ändrar den.
- Gate 48: två nya tokens i `:root`, `--f-quote-calyx` och `--f-quote-horai`, med fallback;
  ingen `font-family` utanför token-blocket.

**B4 · Prisbron: svart plåt som löses upp i fotot, tesrösten tillbaka, en hårlinje som leder ned i prisliggaren.**
- Grunden börjar i Hōrais svarta plåt (ingen kant, bron läses som att Hōrai-kapitlet
  andas ut) och tonar till exakt prisets scrim i underkanten, så priset tas emot på fotot utan
  en skarv. Materialbytet sker **genom** bron i stället för i en kant: det är den enda
  gradienten på sidan och den har en uppgift.
- Rubriken i tesens röst (Geist 700 versaler, samma storlek som `.ts`): sidan öppnade sitt
  argument i den rösten på blått, bron sluter det på svart innan priset. Samma röst, annan
  grund; ingen ny skala.
- Rörelsen är prisets egen: en hårlinje i prisliggarens bredd dras in på `--sc-ps`, samma
  anordning som `.price-ledger::before` (plan 033). Ögat följer den ned till liggarens första
  linje. Plus den delade revealen. Ingen ny set-piece (sidan har sin i heron och tesen).
- Anatomi: vänsterställd spalt vid `--rail-x`, som priset; skiljer sig från `.case-bridge`
  (centrerad på `place-content:center`).

**B5 · Ramarna: `scrolling="no"` på båda iframe.** Prövat denna session i Chromium med riktiga
rullningslister: utan attributet 1215/1230 (1920) och vågrät list vid 390; med attributet
`clientWidth === innerWidth` vid båda bredderna, inga lister i bilden, och ramen skrollas
fortfarande av `contentWindow.scrollTo` (Calyx `scrollY` 1346 i båda fallen vid 1920).
`scrolling="no"` sätter ramens viewport till `overflow:hidden`, som tillåter programmatisk
scroll. Ramens bredd, transform och `sites/*` rörs inte. Följd: ramens dokument blir 15 px
bredare, så ankarna mäts om (det gör `measureCase` redan vid `load` och `ResizeObserver`).
Hōrais kända vågräta överflöde vid 390 (675 px, sajtens eget, r3 fix 7) klipps nu tyst i
stället för att visa en list.

**B6 · Fyra meningar.** `VI BYGGER ERT VARUMÄRKE.` tas bort på Antons uttryckliga beslut; låset i
`PRODUCT.md` § Brand Commitments är hävt för just den strängen (rad 105 säger det redan).
Intervallet per mening hålls (0,9 vh), så aktens span krymper 5,5 → 4,4. Alla `/ 5` i tesens
formler blir `/ var(--n)` med `--n:4` på `.thesis`.

## Steps

Radnummer är R11:s, verifierade med Grep denna session. Kirurgiska `Edit`.

### 6 · Fyra meningar (görs först, allt nedan räknar med fyra)

6.1 Markup rad 1510: ta bort `<p class="ts" style="--i:4">VI BYGGER ERT VARUMÄRKE.</p>`. Rad
1512: ta bort `<i style="--i:4"></i>`. Rad 1502: `data-sc-span="5.5"` → `"4.4"`.
6.2 CSS: `.thesis{position:relative;z-index:2;}` (rad 588) får `--n:4;`. Rad 615:
`calc(var(--i) / 5)` och `calc((var(--i) + 1) / 5)` → `/ var(--n)`. Rad 626:
`(var(--i) + .5) / 5) * 10)` → `(var(--i) + .5) / var(--n)) * (2 * var(--n)))`.
Bildens färg (rad 633) kom med mening 3 i fönstret 0,4 till 0,6 (fem meningar); med fyra
börjar mening 3 vid 0,5: `(var(--sc-ps,0) - .4) / .2` → `(var(--sc-ps,0) - .5) / .2`.
6.3 JS rad 2465 till 2467: regex `thesis-0[1-5]` → `thesis-0[1-4]`, `(tesN - 0.5) / 5` → `/ 4`.
6.4 Kommentaren rad 811 till 812 (jättesektionens rader) uppdateras: raden är struken, inte flyttad.

### 1 · Hyperborea, ≥ 1024

1.1 Ta bort bokstavsspärrens animering på alla bredder (i dag bara låst under 768, rad 674):
i `.js .ts` (rad 615 till 620) ersätt `letter-spacing:calc(-.02em + (1 - var(--in)) * .06em);`
med `letter-spacing:-.02em;` och ta bort den nu överflödiga raden i mobilmediet (rad 674 till
675). Skäl: med en spalt som är tätt dimensionerad mot det bredaste ordet får ett ord aldrig
bli 0,66 em bredare mitt i bytet (samma mekanism som R10:s hopp). Bytet bärs av clip-path och
translate, som i dag.

1.2 Nytt block efter tesens `@media (max-width:767px){…}` (efter rad 676):

```css
/* PLAN 057 1. Hyperborea som jämbördig huvudperson (hoy-home-1440--s01):
   bilden 1,2fr = 45,8 % vw, fri från kanten med --rail-x på båda sidor,
   överkant i linje med meningens överkant. INTE en plåt lågt i hörnet
   som bleeder ut. Meningen begränsas av spalten (14cqi): bredaste ordet
   ARGUMENTET. är 6,82 em, 14cqi ger >= 4 % marginal. */
@media (min-width:1024px){
  .thesis-stage{grid-template-columns:minmax(0,1fr) minmax(0,1.2fr);
    padding:clamp(96px,16svh,168px) var(--rail-x) clamp(28px,5svh,48px);}
  .thesis-lines{align-self:start;container-type:inline-size;}
  .ts{font-size:min(clamp(2rem,5vw + 1rem,6rem),14cqi);}
  .thesis-figure{grid-row:1;align-self:start;}
  .thesis-photo-box{border-right:1px solid var(--frame-line);}
  .thesis-caption{padding-right:0;}
  .thesis-ticks{align-self:end;}
}
```

   Byggaren mäter `ARGUMENTET.` i den byggda sidan (`Range.getBoundingClientRect` på ordet)
   och justerar `14cqi` om ordet inte har ≥ 8 px marginal i spalten vid 1024/1280/1440/1920;
   värdet och mätningen skrivs i NOTES. `.thesis-figure` flyttas till rad 1 (i dag `1 / span 2`,
   rad 628) så att dess överkant = radens överkant = `.ts`-cellens överkant. Ticken står kvar i
   rad 2 längst ned till vänster.
1.3 Kontrollera att `transform:scale(1 + .06 * ps)` på bilden (rad 634) stannar inne i
   `overflow:clip` (det gör den) och att bildtexten inte krockar med tickarna vid 1024x768.

Device-värden, räknade (mät om):

| Bredd | text­spalt | `.ts` | plåt | plåtens topp |
|---|---|---|---|---|
| 1920x930 | 756 px | 96 px | 908x567 (47,3 %) | 149 |
| 1440x900 | 550 px | ~77 px | 660x412 (45,8 %) | 144 |
| 1280x800 | 489 px | ~68 px | 586x366 (45,8 %) | 128 |
| 1024x768 | 391 px | ~55 px | 469x293 (45,8 %) | 123 |

### 2 · Ridån som ren kant

2.1 CSS rad 948 till 951:

```css
/* PLAN 057 2, river plan 054:s sticky ridå. Kapitlet står i flödet direkt
   under tesen: den blå plåten lyfter och kapitelskärmen följer kanten upp.
   INTE en sticky rubrik under en rörlig kant (den korsas alltid). */
.process{background:var(--bg);color:var(--ink);position:relative;z-index:1;}
.chapter-hold{height:auto;}
.process-chapter{position:relative;min-height:100svh;display:flex;
  flex-direction:column;justify-content:center;padding-block:clamp(72px,12svh,120px);}
```

   (`margin-top:-100svh`, `height:calc(200svh + 40svh)` och `position:sticky;top:0;height:100svh`
   försvinner.) `.chapter-hold`-omslaget i markup (rad 1547) får stå kvar (inget läser det
   utom CSS) eller tas bort med sin kommentar; välj det som ger minst diff.
2.2 Kommentarerna rad 940 till 947 och rad 1545 till 1546 skrivs om till B2 i en mening.
2.3 JS: `ridaY` (rad 2474 till 2479) står kvar oförändrad; `curtain` = `ridaY(50)` (halv plåt,
   kapitlet på väg upp), `chapter` = `ridaY(100)` (kapitlets överkant i viewportens överkant).
   Rad 2481 till 2486: `ridaY(120)` → `ridaY(100)`, kommentaren uppdateras.
2.4 `measureAct` mäter om processens ankare vid load/resize (oförändrad kod). Kontrollera alla
   sju `?preview=process-0N` vid 1440 och 390: landar som före, band 01 syns inte i `chapter`.

### 3 · Case-rubrikerna

3.1 Typsnitt (Q2): vendra två woff2 till `runs/V3d/assets/fonts/`, OFL, delmängd latin +
   U+0100-017F (för Ō/ō): `cardo-400-italic-latin.woff2` och `cinzel-600-latin-ext.woff2`.
   `@font-face` efter Geist Mono (rad ~118), `font-display:swap`, `unicode-range` som filen.
   Tokens i `:root` efter `--font` (rad 160):
   `--f-quote-calyx:'Cardo',Georgia,serif; --f-quote-horai:'Cinzel',Georgia,serif;`
   med kommentaren: citat ur exempelsajterna, exakt ett ord var, aldrig för annan text.
3.2 Markup rad 1794 och 1835:

```html
<h2 id="calyx-title" class="case-title"><span class="case-name">Calyx</span>
  <span class="case-line">(COPY-V3d-case-v1, Calyx-rubriken)</span></h2>
<h2 id="horai-title" class="case-title"><span class="case-name">Hōrai</span>
  <span class="case-line">(COPY-V3d-case-v1, Hōrai-rubriken)</span></h2>
```

   Kickern (rad 1793, 1834) ändras bara om copy-filen säger det (Q3).
3.3 CSS, ersätter `.case-title` (rad 874 till 875) och mobilens rad 924:

```css
/* PLAN 057 3. Case-rubriken i två delar: namnet CITERAT i sajtens egen
   displayröst (Calyx: Cardo kursiv, som sajtens ordmärke; Hōrai: Cinzel
   versaler med spärr, som sajtens), raden i Alunix statementröst.
   INTE ett platt ord i Geist. Båda namnen spänner samma mått. */
.case-title{margin-top:12px;container-type:inline-size;}
.case-name{display:block;line-height:.9;font-size:min(9rem,var(--name-fit));}
.case--calyx .case-name{font-family:var(--f-quote-calyx);font-style:italic;font-weight:400;
  --name-fit:39cqi;letter-spacing:-.01em;}
.case--horai .case-name{font-family:var(--f-quote-horai);font-weight:600;
  text-transform:uppercase;letter-spacing:.06em;--name-fit:21cqi;}
.case-line{display:block;margin-top:clamp(14px,2svh,22px);max-width:20ch;
  font-family:var(--font);font-weight:300;font-size:clamp(1.75rem,2.3vw,2.75rem);
  line-height:1.08;letter-spacing:-.015em;text-wrap:balance;}
@media (max-width:767px){
  .case-name{font-size:2.25rem;}
  .case-line{font-size:1.0625rem;line-height:1.3;margin-top:6px;max-width:none;}
}
```

   `39cqi`/`21cqi` är räknade (0,9 / 2,3 em och 0,9 / 4,2 em); byggaren mäter namnens
   bredd och justerar så att båda ligger på 90 % ±4 % av spalten vid 1440 och 1920. Taket
   9 rem gäller Calyx vid bred spalt.
3.4 Mät höjdbudgeten (Target 3, "allt ryms") vid 1920x930, 1440x900, 1280x800, 1024x768 och
   390x844, 375x812 i varje steg. Vid 1024x768: om det inte ryms sänks `.case-steps`
   margin-top först, sedan `.case-line` till `1.5rem` i `@media (max-height:800px)`. Vid 390:
   § Boundaries.

### 4 · Prisbron

4.1 Markup mellan `</section>` för `#case-horai` (efter rad 1850) och `#pris` (rad 1854):

```html
<!-- PRISBRO: svart plåt som löses upp i prisets foto. Tesrösten tillbaka,
     en hårlinje som leder ned i prisliggaren. INTE en tredje brygga på
     place-content:center, INTE en hård kant mot priset. -->
<section class="price-bridge" id="bro" data-sc-act="flow" aria-labelledby="bro-title">
  <h2 id="bro-title" class="bro-title" data-sc-in>(COPY-V3d-case-v1, bron: rubrik)</h2>
  <p class="bro-p" data-sc-in>(rad 1 … 3, ett <p> per rad om copy-filen delar dem)</p>
  <div class="bro-rule" aria-hidden="true"></div>
  <p class="bro-micro" data-sc-in>(mikroraden, bara om copy-filen har en)</p>
</section>
```

4.2 CSS, efter `.price-row .value` (rad ~803):

```css
/* PLAN 057 4. Bron till priset. Överkant = Hōrais svarta plåt, underkant =
   exakt prisets scrim (::before delar regeln med .price/.close), så priset
   tas emot på fotot utan skarv. */
.price-bridge{position:relative;isolation:isolate;color:var(--invert-ink);
  min-height:100svh;padding:clamp(120px,20svh,220px) var(--rail-x) 0;
  background:linear-gradient(180deg,var(--c-black) 0,var(--c-black) 42%,transparent 100%);}
.bro-title{font-family:var(--f-display);font-weight:700;text-transform:uppercase;
  font-size:clamp(2rem,5vw + 1rem,6rem);line-height:.98;letter-spacing:-.02em;
  max-width:15ch;text-wrap:balance;overflow-wrap:normal;}
.bro-p{font-size:1.25rem;line-height:1.5;max-width:44ch;margin-top:clamp(20px,3svh,32px);
  color:color-mix(in srgb,var(--c-paper) 84%,var(--c-black));}
.bro-rule{height:1px;width:min(100%,1040px);margin-top:clamp(40px,6svh,64px);
  background:var(--hairline-dark);transform-origin:left center;
  transform:scaleX(clamp(0,calc((var(--sc-ps,0) - .30) / .25),1));}
.bro-micro{font-size:.9375rem;margin-top:14px;
  color:color-mix(in srgb,var(--c-paper) 78%,var(--c-black));}
```

   Rad 780: `.price::before,.close::before` → `.price::before,.close::before,.price-bridge::before`
   (samma scrim, ingen ny regel); samma sak i mediet rad 1431. I en egen stapelkontext målas
   `::before` (z −1) ovanpå elementets egen bakgrund: scrim på svart är fortfarande svart, och
   i underkanten, där gradienten är genomskinlig, finns bara scrimmen kvar, samma som `#pris`
   överst. Mät ΔE vid Hōrai/bro-skarven = 0.
4.3 Luft: mät avståndet `.bro-rule` → `.statement`; ligger det utanför 35 till 60 svh justeras
   `.price-bridge` `min-height` (inte `#pris`, som är orört).
4.4 Kontrast över media (Target 4) i `?preview=pris-bro` och i hjulsekvensens ljusaste
   bildruta. Faller mikroraden: höj till 84 %, flytta aldrig texten längre ned i gradienten.

### 5 · Ramarna och 1920

5.1 Markup rad 1808 och 1828: lägg `scrolling="no"` på båda `<iframe>`. Kommentar vid
   `.frame-wrap iframe` (rad 724): varför, och att headless-fångster döljer listerna.
5.2 Inget annat i ramkoden ändras. `measureCase` mäter om vid `load` (ramen blir 15 px bredare).
5.3 1920-genomgången denna session, att bekräfta eller laga i samma runda:
   - Calyx-ramens vänsterkant vid 1920 (`1920-0042.png`, `-0045.png`, x ≈ 683) visar korta
     mörka streck längs ramkanten. Troligen `frame-poster`-bilden som skymtar i en pixelspringa
     eller sajtens eget innehåll. Byggaren tar en zoomad skärmbild vid 1920 och 1440, med och
     utan `frame-poster`; är det vår sida lagas det, är det sajten skrivs det i NOTES.
   - Prisliggaren står på `max-width:1040px` och lämnar ~780 px foto till höger vid 1920
     (`1920-0066.png`). Läst som avsiktligt (fotot bär skrivbordet), inget ändras.
   - Processakten, heron och caskapitlet vid 1920 lästa: inga tomma band, inget trasigt.

### `?preview=`-hookar

| Läge | Mål | Visar |
|---|---|---|
| `thesis-01` … `thesis-04` | `aimPin(#tes, (N − 0,5) / 4)` | mening N ensam, bilden i linje med dess överkant |
| `curtain` | `ridaY(50)` | halv blå plåt, kapitelskärmen på väg upp, rubriken hel eller under viewportens underkant, aldrig under blått |
| `chapter` | `ridaY(100)` | kapitelskärmen ensam |
| `case-calyx-01` … `-05`, `case-horai-01` … `-06` | oförändrade | nu med tvådelad rubrik, utan rullningslist i ramen |
| **`pris-bro`** (ny) | `#bro` `scrollIntoView({block:'start'})` + 0,35 vh, `__scFreezeMotion`, vänta tills `#bro`:s `--sc-ps` ≥ 0,55 (hårlinjen färdig) | bron formad: rubrik, stycke, hårlinjen dragen |
| **`pris-bro-skarv`** (ny) | scrollY = `#pris` överkant − 0,5 vh | skarven bro/pris mitt i bild, för Target 4 grunden |

## Device-tabell

| Bredd | 1 · Tesbandet | 2 · Kanten tes → kapitel | 3 · Case-rubrik | 4 · Prisbron | 5 · Ramarna |
|---|---|---|---|---|---|
| **1920x930** | 4 meningar i 96 px, spalt 756; plåt 908x567 = 47,3 % vw, topp 149 = meningens topp, `--rail-x` 96 höger | ren hårlinje; rubrik 120 px följer kanten | Calyx ~144 px Cardo kursiv, HŌRAI ~103 px Cinzel, rad 44 px ≤ 4 rader i ~490 px | rubrik 96 px ≤ 3 rader, grund svart → scrim | ingen list; ram 1236 bred |
| **1440x900** | ~77 px, spalt 550; plåt 660x412 = 45,8 %, topp 144 | samma | Calyx ~144, HŌRAI ~80, rad ~37 px | 88 px | ingen list |
| **1280x800** | ~68 px; plåt 586x366 = 45,8 % | samma | Calyx ~125, HŌRAI ~68, rad ~31 px; höjdbudgeten mäts | 80 px | ingen list |
| **1024x768** | ~55 px; plåt 469x293 = 45,8 % | samma | Calyx ~98, HŌRAI ~54, rad 28 px; höjdbudgeten mäts, se 3.4 | 67 px | ingen list; Calyx i sin smala layout (väntat) |
| **768x1024** | R11-geometrin orörd (`.7fr`, bleed, 54 px), 4 meningar | samma | text ~290 px: Calyx ~90, HŌRAI ~50, rad 28 px | 54 px | ingen list |
| **390x844** | R11 orört (4 meningar, fotot 16 px under tickarna, 0 px hopp) | samma, rubrik 56 px | namn 36 px, rad 17 px ≤ 3 rader, steget under; budget mätt | 35,5 px, grund samma | ingen list, varken lodrät eller vågrät (Hōrais 675 px klipps tyst) |
| **320x568** | R11 orört | samma | namn 36 px; mät, § Boundaries om texten inte ryms | 32 px | ingen list |

Noll horisontell scroll 320 till 1920 (element­rektanglar, gate 34). 200 % zoom på 1440 =
720 css-px = mobilraden.

## Repo conventions

- Motorn och `sites/*` orörda; ramen transformeras aldrig; ingen `prefers-reduced-motion` (F-011);
  allt som rör sig läser `--sc-ps` (F-014). Gate 75: noll tankstreck i synlig text. Radie 0,
  inga skuggor. Gate 48: de två citattypsnitten bara via `--f-quote-*`.
- Kommentarer: varje nytt block börjar med `PLAN 057 N.` och en INTE-rad (in-situ negation).
- Accenten `#1e5e9c` exakt två förekomster (tesen, "Boka ett möte"). Inline-hex utanför `:root`
  inte fler än R11 (CSS 16, markup/JS 2).

## Boundaries (STOPPA och skriv i NOTES)

- `COPY-V3d-case-v1.md` saknas eller saknar en sträng steg 3/4 behöver.
- En låst sträng utom `VI BYGGER ERT VARUMÄRKE.` skulle behöva ändras.
- Case-texten ryms inte vid 390x844 eller 375x812 efter 3.3 (lead väljer mellan att låta raden
  bara synas i steg 1, sänka ramens rad, eller kortare copy; byggaren väljer inte).
- `scrolling="no"` bryter synken (ramens `scrollY` rör sig inte) i någon bredd.
- Nedladdningen av typsnitten är inte godkänd (Q2): bygg då steg 3 med Geist för namnet och
  resten av planen som skriven, och skriv det i NOTES.
- Någon `?preview=process-0N` landar inte längre på sitt `--eN` efter steg 2.

## Verification

**A. Synligt, det som avgör.** `PARITET.md` rader P03, P04, P17, P19, P20, P21: par-bilder vid
1440 och 390 i `shots/r12/par/`, lästa som bilder, "håller nivån" eller lagade i samma runda.
Plus enskilda skärmbilder vid **1920x930** för P03 (alla fyra meningarna), P04, P17-1, P19-1,
P21. Lead läser själv P03, P04, P21 vid 1920 och 390 innan rundan räknas klar.

**B. Mätt.**
1. Tesen: `photo.top − ts.top` per mening; `photo.width / innerWidth`; `photo.top`-spridning i
   20 px-hjul ned och upp vid 1024/1280/1440/1920 (och 390/375, oförändrat 0 px);
   `getComputedStyle(.ts).fontSize` lika för alla fyra per bredd; rubrikskriptet på `.ts`,
   `.case-name`, `.case-line`, `.bro-title`, `.process-title`, `.cases-title`, `.bridge-title`;
   `.ts`-antal 4, tick-antal 4, `VI BYGGER` 0 träffar.
2. **Rubriktäckning, hela sidan**, hjul 20 px-steg från toppen till botten vid 1920x930,
   1440x900, 768x1024, 390x844. Per bildruta, per rubrik i `h1, h2, h3, .ts, .statement,
   .close-mailto`: ta 9 punkter i rubrikens rektangel ∩ viewporten, hoppa över rubriker med
   `opacity` < 0,05 och punkter som rubrikens egen `clip-path` döljer (`.ts`/`.cs` mitt i
   bytet); `document.elementFromPoint` ska vara rubriken själv eller en ättling. Utgå från
   `shots/astra-r10/sweep.py`. **Kör först mot R11** (före ändringen): skriptet ska hitta ridåns
   fel vid alla fyra bredderna, annars mäter det fel. Mål efter bygget: 0 träffar. Träffar
   utanför 057:s sektioner skrivs i NOTES med bild och stoppar inte rundan.
3. Ramarna: Playwright med `chromium.launch(ignore_default_args=['--hide-scrollbars'])`. Kör
   först **utan** `scrolling="no"` (injicera bort attributet): probet ska rapportera
   `clientWidth < innerWidth`. Sedan med: `clientWidth === innerWidth`,
   `clientHeight === innerHeight` i båda ramarna vid 1920/1440/1280/1024/768/390/320;
   skärmbild av ramen vid 1920 och 390 läst som bild. Synk: `case-*-0N` ankare ±2 px;
   hjul 20 px-steg genom båda casen, ramens `scrollY` monoton.
4. Bron: ΔE vid Hōrai/bro-skarven; luminans 2 px ovan/under bro/pris-skarven; avstånd
   hårlinje → `.statement` i svh; `contrast_over_media.py --url` på `pris-bro`.
5. Låst copy: **14/14** (15 minus den strukna tesrubriken).

**C. Grinden.** `scroll_verify` 1440 och 390 (inga nya `blankBands` utöver de dokumenterade
pinnade akterna); `motion_probe` på `#tes` och `#bro` ned och upp, `staircase 0`, `max_step` ≤ 3 %;
`perf_probe` (två nya woff2, LCP oförändrad ±10 %); `a11y_scan` + `reflow` vid 390 och 1440;
`tab_walk`; grep `prefers-reduced-motion` 0; noll horisontell scroll 320 till 1920.

**Done when:** varje Target-rad har ett uppmätt värde som når målet, rubriktäckningen är 0 vid
alla fyra bredderna, inga rullningslister i en riktig Chromium, P03/P04/P17/P19/P20/P21 håller
nivån i sina par-bilder, och grinden är ren eller varje avvikelse namngiven.

## Frågor till Anton (bygget stoppar inte; antagandet gäller tills svar)

| # | Fråga | Antagande |
|---|---|---|
| Q1 | Hyperborea fri från högerkanten (som hoy) kostar meningarna ~12 % vid 1440 (88 → ~77 px; 1920 oförändrat 96). Alternativet är att behålla bleed mot högerkanten och 88 px, med samma ≥ 45 % bild. | Fri från kanten |
| Q2 | Case-namnen i sajternas egna typsnitt kräver att två OFL-typsnittsfiler (Cardo kursiv, Cinzel) laddas ned och läggs i `assets/fonts/` (~20 till 40 kB var). Ok? | Ja, efter ditt ok; annars Geist |
| Q3 | Ett löpande index i kickern, "Exempelcase 1 av 2" / "2 av 2"? Det är copy, copy-agenten föreslår. | Kickern oförändrad om copy-filen inte ändrar den |
| Q4 | Ridån blir en ren kant: den blå plåten lyfter och kapitlet följer, i stället för att kapitlet står still under den. Det är den enda formen där rubriken aldrig halvklipps åt båda hållen. Ok? | Ja |

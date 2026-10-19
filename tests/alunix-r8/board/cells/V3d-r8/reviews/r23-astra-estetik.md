fix

## persistence
**Egna bilder, `shots/astra-r23/`.** 48 skarmbilder, Chromium med
`ignore_default_args=['--hide-scrollbars']`, varje lage natt med `mouse.wheel` i en
ren sida, **en skarmbild per sida**, inga kontaktark. 1920x930 och 390x844.
`shots23.py` (A01-A17 resp. A01-A15 genom tes till ritning i 40-160 px steg, dar
A02/A04/A06/A09/A11 resp. A02/A04/A06/A08/A10 ligger exakt pa
`?preview=tes-till-ritning-0…-4`; C01-C06 in i och genom case-kapitlet; P01-P02
priset). `shots23.json` loggar mal, landat och `hscroll` 0 i alla 48.

**Matningar.** `sweep23.py`: 40 px-hjul i ett svep, 93 bildrutor vid 1920 (y5600-9280)
och 73 vid 390 (y5000-7880). Per bildruta: summan av alla LEVANDE textnoders
`Range.getClientRects`, klippta mot varje forfaders `clip-path:inset()` och mot
viewporten, plus planets synliga rektangel. `ink23.py`: exakt glyfyta (Range, inte
elementets box) for sidans alla rubriker vid 1920/1440/390. `anchors23.py`: luft och
storlekar i case-kapitlet och priset. Pixelavlasningar direkt i PNG-filerna for
linjekolumner och liggarens harlinjer.

**Codex** (`gpt-6-astra`, medium, read-only) kordes en gang med **13 parbilder**
(`prompt.txt`, `Q01-Q13.png`, `codex-out.txt`). Uppdraget var uttalat estetiskt, inte
en specgranskning; F-011 och forbudet mot en ny konstnarlig riktning lag i prompten.
Den levererade en sammanhangande dom i tre delar. **Jag tog 11 pastaenden, slappte 2
och korrigerade 3.**
- **Slappt: "align the first description baseline with the price baseline in every
  row".** Det ar redan sant. Uppmatt i `P02-1920.png`: etikettens forsta rad 515-530
  mot siffrans 478-529 i rad 1, och 635-650 mot 598-659 i rad 2. Baslinjerna ligger
  ratt. Det som verkligen skaver ar nagot annat, se fidelity punkt 3.
- **Slappt: "kr" vid 60-65 % av siffran.** Det ger ett 30 px stort "kr" bredvid en
  48 px siffra, alltsa en enhet i displaystorlek. En liggare satter enheten i
  textstorlek.
- **Korrigerat: Codex rankar Q07 (390, y6080) som varst.** Min matning sager att golvet
  ligger strax intill: vid y5960-6080 finns **noll textrutor** pa hela skarmen. Jag
  behaller rangordningen men med det talet.
- **Korrigerat: "reduce mobile to 100-140 px".** For kort; en hjulflick ar ~100 px, sa
  draget skulle lasa som ett hopp. Se fidelity.
- **Korrigerat: siffrornas storlek 52-56 px.** Jag gar lagre, med skal i fidelity.

**Ett eget fynd som jag dodade sjalv.** Jag trodde forst att landningslinjen ritas
UTANFOR arket (en ljus stump i den bla ytan till vanster om arket i A05/A07/A09/A11).
Pixelavlasning: stumpen ligger pa x 96-254 och ar `.thesis-ticks` (fyra 32x2 px-streck,
`index.html:661-664`), inte `.seam-h`. Landningslinjen ritas korrekt inne pa arket.
Fyndet blev ett annat och mindre, se material_fixes 4.

**Sokvagsrattelse:** `~/example-design-system/sites/` finns inte pa maskinen. Jag laste
`C:\Users\Anton L\anti-slop-design\sites\hyperborea.html` och `horai.html` via
localhost:3090 och fangade 36 referensbilder (`REF-hyp-*`, `REF-hor-*`).

## fidelity
**Domen: kunden har ratt, och jag hade fel av ett skal som ar vart att namna.** I r21
matte jag att den klippta rektangeln ager 44 % av viewportens area vid t3 och kallade
det en hel yta som forandras. Jag matte **arean pa formen** och tog den for narvaro.
En stor tom rektangel ar inte narvaro, det ar franvaro i skala. Ju storre den ar, desto
tydligare ar det att det inte star nagot i den. Det ar precis vad kunden ser.

**1. Overgangen tes till ritning.**

*Var den ar tom, matt.* Vid 1920 gar sidans synliga textyta fran **43,6 % av viewporten
vid y6520** (15 textlopor, tesens sista mening) ned till **8,2 % vid y6800** (3 lopor,
alla klippta av viewportens over- eller underkant) och kommer inte over 21 % igen
forran y7600. Det ar **1 080 px scroll, 1,16 viewport, dar sidan bar under en femtedel
av sin normala text**. Vid 390 ar det brutalare: vid **y5960, 6000, 6040 och 6080 finns
noll textrutor pa skarmen** (160 px), och fran y5900 till y6160 (260 px) finns
ingenting lasbart alls. Sjalva ritdraget kostar 594 px vid 1920 och 539 px vid 390;
kapitelrubriken ar lasbar forst ytterligare 400 px senare.

*Varfor ogat laser det som fel, bildruta for bildruta.*
- **A02 (t0):** tesens rubrik uppe till vanster, Hyperborea-bilden uppe till hoger, och
  nedre 40 % av skarmen ar en **naken bla rektangel utan ett enda marke i sig**.
  Kompositionen har ingen mitt. Det lasar som att sidan tagit slut mitt i en sektion.
- **A05/A07 (t2, y6720-6800):** den ljusare bla plattan ager 51-55 % av viewporten och
  bar fyra harlinjer. Linjerna slutar dessutom **mitt i plattan**: de spanner y 348-656
  av en rektangel som gar till y 806, sa nedersta 150 px ar tom bla. Ovanfor ligger ett
  tomt bla falt, till hoger en Hyperborea-bild klippt till en 240 px remsa. Tre olika
  blatoner i samma bildruta, ingen av dem med nagot i sig. **Detta ar den fulaste
  desktopbildrutan.**
- **A11/A14 (t4 och efter, y7061-7440):** arket har stelnat till en **1 213 px bred
  harlinjelada med tva streckade lodrata linjer och ingenting inuti**, som star kvar i
  bildrutans ovre 30-45 % i 440 px scroll. Codex satter ord pa det jag missade:
  ankomsten laser som ett **forsvinnande**. Vi har spenderat 600 px pa att titta pa
  nagot som blir mindre substantiellt, och slutlaget ar en tom platshallare ovanfor
  rubriken, inte en ram runt nagot.
- **A10-390 (t4):** landningen ger **tva staplade tomma lador**, y 180-297 och 297-515,
  tillsammans 40 % av viewporten. Det ar inte en ritning, det ar tva brutna bilder.
- **A03-390 och A05-390:** demobilden ar en 1440 bred skarmdump beskuren till skarmens
  vanstra 40 %, sa beviset visas som ett halvt ord, och under den ligger 250-350 px ren
  bla yta utan ett tecken. Codex kallar det cropped image texture och det ar ratt: det
  fungerar som struktur, inte som innehall.

*Geometrin ar inkoherent, och det ar en egen fulhet.* Vid y6720 spanner arkets
**fyllning** x 117-1792 medan de linjer som ska VARA arkets kanter star pa x 348 och
1 560, alltsa **231 px innanfor pa vanster sida och 232 px innanfor pa hoger**. Genom
hela tx 0,3-0,85 ser ogat en fylld rektangel med fyra godtyckliga streck i, inte ett
ark. Strecken star dessutom pa x 348 / 618 / 995 / 1 560, alltsa mellanrum
**269 / 377 / 565 px**. Det ar varken jamna delar eller en lasbar spalt; det ar tre
olika avstand i rad, vilket ar exakt hur ett oga laser slumpmassighet.

*Fargdraget syns inte.* Blandningen fran accentblatt mot ritbordets ton pa tx betyder
att plattan vid halva draget ar en dov skiffer som varken ar accentblaen ovanfor eller
ritbordets ton under. A07 ar tre narliggande blagra toner i samma bildruta.
Forandringen ar mekaniskt sann och optiskt osynlig.

*Kapitelskarmen arver sjukdomen.* A16 (y7700): rubrik och tvaradig ingress i ovre
290 px, sedan **390 px dod svart** innan steg 01. Samma tomma ark, en skarm senare.

*Vad som skulle gora det vackert.* Ett ritningsark ar aldrig tomt: det har en
**stampelruta**. Det ar hela svaret.
- **Lagg kapitelrubriken INNE i arket**, nere till vanster, med den lasta raden under
  sig och landningslinjen som stampelrutans overlinje. Da har rektangeln ett skal att
  finnas, konturen ramar in nagot, landningslinjen far en funktion, och bildrutan kan
  aldrig bli textlos, for rubriken ar med fran det ogonblick arket har en kant. Ett
  drag loser fyra fel.
- **Korta draget till ungefar halften:** 260-300 px vid 1920 och 220-260 px vid 390
  (Codex ville ned till 200-240 och 100-140; 100-140 px pa mobil ar under en enda
  hjulflick och skulle lasa som ett hopp, inte som ett scrubbat drag).
- **Overlappa i stallet for att koa.** Rubriken ska vara inne i bildrutan och lasbar
  vid tx ungefar 0,45, medan arket fortfarande konvergerar. Ingen bildruta i passagen
  far ha under ungefar 18 % textyta, och pa 390 aldrig noll.
- **Lat strecken ha ett arbete.** Fyra namnlosa lodrata linjer med tre olika mellanrum
  ar dekor. Antingen lat dem vara arkets faktiska spaltdelning (samma 4/8 som
  stegarket under) med jamna mellanrum, eller lat dem sluta i stampelrutans overlinje
  sa de laser som matlinjer till en ruta.
- **Lat kanten vara kanten.** Konturen och fyllningen ska sammanfalla genom hela
  draget, inte bara vid tx = 1.
- **Lat fargen gora ett riktigt hopp.** Hall arket pa accentblaen till tx ungefar 0,75
  och vand det till ritbordets ton over sista fjardedelen. En synlig forandring sent
  slar en osynlig forandring hela vagen.

**2. Exempelcase-kapitlet. Kunden har ratt, och tva av de tre sakerna gar att visa i tal.**

| | 1920 | 1440 | 390 |
|---|---|---|---|
| Exempelcase | 136 px, ordbild **860 x 192** | 129,6 px, 820 x 183 | 40 px, 253 x 57 |
| Calyx | 171 px, ordbild **468 x 223** | 122,5 px, 334 x 159 | 36 px, 98 x 47 |
| Hōrai | 135 px, 470 x 176 | 96,5 px, 336 x 125 | 36 px, 125 x 47 |
| tesens mening | 96 px | 76,3 px | 35,5 px |
| processrubriken | 120 px | 103,7 px | 56 px |
| prisets statement | 96 px | 86,4 px | 40 px |

- **Exempelcase ar sidans storsta ord.** 136 px slar hjaltens tesmening (96), prisets
  statement (96) och processkapitlets rubrik (120). En **etikett** ar satt storre an
  varje pastaende sidan gor. Det ar hierarkifelet i en rad.
- **Mot caset den introducerar ar den storre, inte mindre.** Ordbilden ar **1,84 ganger
  bredare** an Calyx vid 1920, **2,45** vid 1440 och **2,57** vid 390, vid narmast samma
  glyfhojd. Vid 1440 och 390 ar den dessutom storre i punkter (129,6 mot 122,5; 40 mot
  36). Nominella 136 mot 171 spelar ingen roll for ogat, och kunden har last det ratt.
  Se `C03-1920.png`, dar bada star i samma bildruta: introt ager den, caset ar klippt i
  underkanten.
- **Luften ar symmetrisk och darfor fel.** 333,3 px over rubriken och 333,3 px under
  ingressen vid 1920 (321,9/321,9 vid 1440; 324,5/324,5 vid 390). Blocket sjalvt ar
  263,5 px, alltsa **28 % black och 72 % tom mark** (23 % vid 390). En symmetrisk
  inramning sager utstallningsforemal. En introduktion ska luta framat: mer luft
  ovanfor an under, sa ogat faller in i det som kommer.
- **Avstandet till caset ar en hel skarm.** Fran ingressens underkant till overkanten
  pa Calyx ar det **538,7 px vid 1920 och 905,6 px vid 390**. Sidan presenterar
  etiketten, tommer skarmen, och presenterar sedan foremalet. Tva entreer for en
  sektion.

*Mal.* Satt Exempelcase till **64 px vid 1920, 48-50 px vid 1440, 26 px vid 390**
(ungefar `clamp(1.625rem, 3.4vw, 4rem)`). Da ar den cirka 37 % av Calyx glyfhojd pa
desktop och tydligt under den pa mobil, och den upphor att vara sidans storsta ord. Ta
bort helskarmshojden och lat blocket bli sin egen hojd: **luft over 120-140 px, rubrik
till ingress 22-24 px, ingress till casets overkant 56-72 px** vid 1920 (motsvarande
56-64 / 16-20 / 32-40 vid 390). Hela introblocket landar da pa 340-380 px vid 1920 och
260-290 px vid 390, och **Calyx forsta bildruta ska synas i samma skarm som introt**.
Rytmen blir: introduktion, sedan bevis, i ett andetag.

**3. Prissektionens typografi.**

*Vad som skaver i dag, utover serifen.* Siffrorna star i Young Serif 64 px mot
etiketter i Public Sans 600 pa 17 px: **3,8:1**. Baslinjerna ar ratt (matt ovan), men
en 64 px siffras versalhojd nar 51 px over baslinjen medan etikettens x-hojd bara nar
15 px, sa **siffrans optiska tyngdpunkt ligger cirka 26 px hogre an etikettens** i
samma rad. De delar baslinje men inte mitt, och vid 3,8:1 racker inte baslinjen for att
halla ihop dem. Radbanden ar dessutom ojamna: harlinjerna ligger pa y 461 / 580 / 677 /
768, alltsa **119 / 97 / 91 px**, och tredje radens varde ar halva siffran, sa det
tredje bandet har varken samma hojd eller samma inre placering som de tva forsta. Och
39 px under liggarens sista 1 040 px linje ligger en **527 px lang linje** (avslutets),
tva harlinjer av olika langd nastan i varandra.

*Vad som ska bara hierarkin nar serifen forsvinner.* Inte en ersattningsdisplay. Fyra
saker, i den har ordningen:
- **Spaltpositionen.** Siffrorna ar redan hogerstallda mot x 1 135; gor den kanten
  absolut med en fast vardespalt (`min-width` cirka 11ch, `text-align:right`) sa alla
  tre raderna slutar pa exakt samma lodrata, aven nar vardet ar en fras.
- **Tabulara siffror.** Young Serifs siffror ar proportionella, sa 26 900 och 38 900 har
  olika teckenbredd och tusentalsluckan hamnar pa olika x i de tva raderna. I
  brodtextens snitt med `tabular-nums lining-nums` staplar de sig siffra for siffra.
  **Det ar den enskilt viktigaste detaljen i hela bytet** och den kostar ingenting: det
  ar den som gor att kolumnen laser som ett instrument i stallet for en uppstallning.
- **Storleken, men lagre an man tror.** Public Sans 400 pa **48 px vid 1920, 36 vid
  1440, 28 vid 390**, radhojd 1,0, sparr -0,01em. Codex ville 52-56; jag gar lagre for
  att 48 ger 2,5:1 mot en etikett som lyfts till 19 px, och 2,5:1 ar en liggare medan
  3,3:1 fortfarande ar en annons. Vikten ska vara **400**, inte halvfet: beslutet ger
  fetstil bara at rubriken, och en 48 px siffra behover ingen vikt for att vinna en rad
  mot 19 px.
- **Harlinjerna.** De blir strukturen nar serifen gar. Lika radband: **24-28 px luft
  over och under varje rad** i stallet for dagens 12,8, sa alla tre banden blir lika
  hoga och siffran far en mitt att sitta i. Alla linjer till samma hogerkant som
  siffrorna. Kapa eller forlang avslutets 527 px linje sa det inte star tva olika langa
  harlinjer 39 px fran varandra.

*Resten.* Rubriken i brodtextens snitt **700**, **84 px vid 1920 / 66 vid 1440 / 36 vid
390**, radhojd 1,0, sparr -0,03em: en grotesk pa 96 px bar mer massa an en serif pa
96 px, sa den ska ned nagot nar snittet byts. Enheten kr pa **etikettstorlek** (19 px
vid 1920, 17 vid 390), samma baslinje, 8 px lucka, tonad till cirka 72 %: beloppet ar
figuren, valutan ar enheten. Frasen Pris vid forfragan pa **27 px** (Codex tal, battre
an mitt: halva siffran flyter, full siffra konkurrerar), hogerstalld mot samma kant, sa
kolumnen laser 48 / 48 / 27 och frasen tydligt inte ar ett tal. Pa mobil behalls
stapeln vansterstalld med 8-12 px mellan etikett och belopp och 20-24 px ned till nasta
linje, sa paret hor ihop tatare an raderna gor.

## ceiling
- **highway `/tjanster/hemsida/` (s03).** Referensen **namnger destinationen forst**:
  rubriken star satt, och den rosa traden med sin fyllda nod borjar cirka 100 px under
  den, i samma bildruta. Rubrik och forsta innehall delar alltid skarm. Vi ritar
  linjerna **innan** de har nagot syfte, och rubriken kommer 400-900 px efter dem.
  Rubrikstorleken ar dessutom cirka 66 px vid 1440, halften av vart kapitelnamn pa
  129,6.
- **insign `/webbdesign-wordpress/` (s03).** Referensen ger aldrig en skarm at en
  overgang. Nasta sektions rubrik kliver in i UNDERKANTEN av den foregaende sektionens
  sista rad. Struktur visas genom sitt innehall: ikon, rubrik, stycke, upprepat. Vi
  visar stallningen och ber stallningen halla uppmarksamheten.
- **hoy `/tjanster/webbdesign` (s03).** Den HAR en skarm dar ett enda foremal ager allt
  och det ar vackert, men foremalet ar **typografi pa 100+ px som man laser**.
  Referensen licensierar ett skarmagande **pastaende**, inte en skarmagande **tom
  platta**. Det ar den lasningen jag gjorde fel i r21.
- **`sites/hyperborea.html` (REF-hyp-1920-3).** Var egen systemreferens gor
  kapitelingangen exakt ratt: liten versalkicker med harlinje ut at hoger, tvaradig
  displayrubrik pa cirka 72 px pa samma axel, och **forsta innehallsraden (fyra paneler
  med egna harlinjer over sig) redan i samma bildruta**, cirka 140 px under rubrikens
  baslinje. Harlinjerna sitter dar innehall borjar och har darfor ett jobb. Vart ritark
  har harlinjer utan jobb. (Kickern i sig ar inte kopierbar hit, F-016; det ar narheten
  mellan rubrik och forsta innehall som ar taket.)
- **`sites/horai.html` (REF-hor-1920-4).** Var egen systemreferens ar en prisliggare som
  gor allt det vi nu ska gora: rangmarkering langst ut i vanster ral, namnet, en liten
  versallinje, brodtexten, och **beloppet stort och hogerstallt i egen spalt med
  enheten satt som en liten versalrad UNDER siffran**, plus fullbreddade harlinjer over
  och under raden. Vart kr star i siffrans storlek bredvid siffran, var liggare slutar
  688 px innanfor ralen, och avslutets harlinje har en annan langd an liggarens. Det
  korrekta priskortet finns redan i huset och vi anvander det inte.
- **Kanda rester, noterade och inte domda har:** arket 63,4 % vw vid 1920, fyra
  typsnittsfiler mot budget tre, och 260-532 ms uppgiften i `sites/horai.html`.

## material_fixes
1. **Kapitelrubriken in i arket.** `index.html:1827-1840`: lagg `#process-title` och
   `.process-locked` INNE i den landade rektangeln, nere till vanster, med
   landningslinjen som overlinje. Expected: i varje bildruta fran det att konturen syns
   (tx 0,6 och uppat) till att kapitlet lamnar skarmen innehaller rektangeln lasbar
   text; A14-laget (y7440, 1920) far aldrig visa en tom harlinjelada. Kontroll: noll
   bildrutor med arket synligt och noll textlopor inuti det, vid 1920 och 390.
2. **Korta draget och overlappa rubriken.** `index.html:1136` (tx-fonstret 0,29) och
   `.process-chapter{min-height:120svh}` (rad 1134): expected tx 0 till 1 pa
   **260-300 px vid 1920 och 220-260 px vid 390** (i dag 594 respektive 539), och
   rubriken lasbar (hela forsta raden inne i viewporten) vid tx hogst 0,45. Kontroll:
   `sweep23.py` ska ge **minst 18 % textyta i varje bildruta** genom hela passagen vid
   1920 och **aldrig noll textlopor** vid 390 (i dag 8,2 % respektive fyra bildrutor pa
   noll).
3. **Lat konturen vara fyllningens kant genom hela draget.** Uppmatt vid y6720 och 1920:
   fyllningen x 117-1792, linjerna x 348 och 1 560, alltsa 231 respektive 232 px
   innanfor. Expected: arkets kantlinjer sammanfaller med den klippta rektangelns
   kanter inom 2 px i varje tx-lage, inte bara vid tx = 1.
4. **Slack tesens progressprickar nar tesen ar slut.** `index.html:661-664`:
   `.thesis-ticks i` har grundton 38 % vit och slacks aldrig, sa fyra 32x2 px streck pa
   x 96-254 blir det enda market i ett tomt bla falt genom hela overgangen (A05, A07,
   A09, A11 vid 1920). Expected: prickarna tonar till 0 nar tesens sista mening lamnar
   bildrutan.
5. **Exempelcase ned och ur helskarmslaget.** `index.html:930-935` och `923-924`:
   `font-size` fran `clamp(2.5rem,9vw,8.5rem)` till cirka `clamp(1.625rem,3.4vw,4rem)`
   (**64 / 49 / 26 px** vid 1920 / 1440 / 390), och `min-height:100svh` bort. Expected:
   rubriken ar mindre an `.case-name` vid alla tre bredderna och inte langre sidans
   storsta ord (i dag 136 px mot processrubrikens 120 och hjaltens 96).
6. **Luften asymmetrisk och caset upp.** Samma regel: **over 120-140 px, rubrik till
   ingress 22-24 px, ingress till casets overkant 56-72 px** vid 1920 (56-64 / 16-20 /
   32-40 vid 390), i dag 333,3 / 27,9 / 538,7. Expected: hela introblocket 340-380 px
   vid 1920 och 260-290 px vid 390, och Calyx forsta bildruta synlig i samma skarm som
   introt (C03-laget ska inte langre visa 340 px tom mark mellan dem).
7. **Prisets siffror och rubrik i brodtextens snitt.** `index.html:860-887`: rubriken
   Public Sans **700** pa **84 / 66 / 36 px**; siffrorna Public Sans **400** pa
   **48 / 36 / 28 px** med `font-variant-numeric: tabular-nums lining-nums`, radhojd 1,
   sparr -0,01em, i en hogerstalld spalt med fast `min-width` cirka 11ch; enheten kr pa
   etikettstorlek (19 / 17 px) pa samma baslinje med 8 px lucka; frasen Pris vid
   forfragan pa 27 px mot samma hogerkant. Etiketterna till vikt **400** och till
   19 px vid 1920. Expected: tusentalsluckan i 26 900 och i 38 900 hamnar pa samma x.
8. **Liggarens rytm.** `index.html:876-881`: radluft **24-28 px** over och under varje
   rad i stallet for `.8rem`, sa banden blir lika hoga (i dag 119 / 97 / 91 px mellan
   harlinjerna pa y 461 / 580 / 677 / 768). Expected: lika radband inom 4 px, alla
   harlinjer till samma hogerkant som siffrorna, och ingen 527 px lang linje 39 px
   under en 1 040 px lang.

## keep
- **Ritningsiden sjalv.** Att tesens bla plan krymper till ett ark och blir sidans
  ritbord ar ratt bild for en byra som saljer vagen fran samtal till lanserad sida.
  Felet ar att arket ar tomt och draget ar langt, inte att draget finns. Byt inte
  metafor.
- **Att arket rullar ut i normalt flode** (R21:s borttagning av `position:fixed`).
  Verifierat igen denna runda i varje matning: ingen stapling vid 1920, inga streck
  genom text. Backa inte.
- **Kapitelrubrikens inblackning** (62 till 100 % pa tx efter landningen) och
  `.cases-title`:s gradientkant. Bada ar tysta och bra; de ska folja med nar
  storlekarna andras, inte tas bort.
- **Prisenheten pa en skarm.** Rubrik, ingress, tre rader och kontakten ryms i en
  bildruta vid 1920, 1440 och 390. Den vinsten far inte ga forlorad nar radluften okas;
  ta hojden ur ingressens och rubrikens marginaler i stallet.
- **Casens egna roster.** Calyx kursiv och Hōrai versal i sina respektive sajtroster,
  med `.case-line` i Alunix lata statementrost. Det ar sidans basta typografiska ide
  och den ska inte roras nar kapitelrubriken over den krymper.
- **Ramarna och overgangarna runt casen.** Flush mot kanten, 0 px rullningslist, ingen
  kantlinje, 223 px svart andrum mellan Calyx och Hōrai, slojan som framkallar fotot in
  i priset. Allt stod sig i denna rundas bilder.

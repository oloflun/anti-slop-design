fix

## persistence

Pass. Allt underlag den här granskningen vilar på finns och är läst i den här körningen.

Standarden: `skills/design/references/house-physics.md`, `production-tells.md` (66-88 och
97-98), `gates.md`, `design-catalogue/TASTE.md` § 4 och § 5, `verbs/critique.md` (sju
dimensioner, skelett-, kort- och squinttestet), `verbs/review.md` § 6 (tio kategorier,
vikterna, A-F-betydelserna).

Cellens egen standard: `runs/V3c/BRIEF.md` i sin helhet (724 rader: lane-meningen i
§ Design Read, låsblockets sju fält, decision ledger R1 och R2, ribborna i § Vad jag måste
slå), målbilden `malbilder/V3c.md` ordagrant, `concepts-V3c.md` § (2) troplistan, § (3) ett
displayelement per skärm, § (4) registerraden, samt `NOTES.md` § R3.

Pixlar, lästa som bilder och inte ur kod (18 filer): `review/r3/` V3c-fold-1440,
V3c-back-1440, V3c-scroll-0 till V3c-scroll-4, V3c-full (1440x4019), V3c-fold-320, -375,
-390, -414, -768, V3c-back-390; `runs/V3c/shots/r3/` preview-mid, preview-ledger,
preview-bleed, close-1440, forcedcolors-1440. Lästa referensfolds: `oryzo-ai/fold.webp`,
`mattis-studio/fold.webp`, `dope-security/fold.webp`, `monologue/fold.webp`,
`planhat/fold.webp`. `planhat` har ingen `slices/`-katalog; det är en egenskap hos posten,
inte en utebliven läsning.

Fem mätningar gjorda på pixlarna i den här körningen, inte uppskattade: kortets framsida vid
1440 ligger till **77,6 %** under L = 12 (nära ren svart) av 893 x 498 px, mot 64,5 % i
4:5-beskärningen vid 390; kortets baksida är ett **helt platt plan**, stdev 0,00 över ett
450 x 140-utsnitt av #0b0c0e, mot stdev 10,9 i grunden bredvid; grunden under underraden
mäter medianluminans 0,008, alltså ca 13:1 mot texten och **inget** kontrastfynd; dokumentet
är 4019 px högt vid 1440 x 900, alltså **4,5 vh**; Hyperborea-plåtens bleed mäter 33 px förbi
det blå blockets kant inuti en 46 px spaltränna.

Ej mätt av mig och inte påstått: `perf_probe`, `motion_probe`, `scroll_verify`. Deras siffror
står i `NOTES.md` § R3 och ägs av perf-granskaren. Kontexten jag väger in utan att mäta om:
lokala typsnitt, 15/15 låst copy ordagrant, `detect.mjs` 4 träffar alla `overused-font:
Geist`, pilen borttagen enligt gate 97 (verifierad i pixlar: filen innehåller noll
pilglyfer, och back-1440 visar understrykning utan pil).

Rundans siffror, skrivna till `runs/V3c/scores.json` med `round: 3` som baseline:
**Design Score B (3,20)**, **AI Slop Score A-**.

## fidelity

Mot målbilden `malbilder/V3c.md` och `concepts-V3c.md` § (3), skärm för skärm.

**s1, heron vid ps = 0** (fold-1440, fold-320/375/390/414/768). Topologin stämmer exakt:
topprad med ordmärke vänster och kontakt höger, rubriken i två rader vänsterställd på railen,
plåten 896 x 504 under den, underraden högerställd under plåten. Fyra textelement, precis
taket. Rubriken mäter 120 px efter rättelse 3 och ligger på den mörka grunden, aldrig över
ljuspölen. Logo-docken ligger innanför hörnet och rör aldrig hårlinjen. Läsordningen är
rubrik, kort, underrad, och den håller på alla fem bredder. **Drift, defekt:** framsidan bär
material på ca 22 % av sin yta. Det övre bandet och den högra tredjedelen mäter medelvärde
L = 1,1, alltså ingen yta alls, och `BRIEF.md` § Vad jag måste slå kräver av just den ytan
att den bär material över hela ytan och en ljusrespons som ändras med vinkeln.
`ASSETS.md` § 3 väg (d) säger själv att de två opacity-tilläggen löser två av tre skäl. Det
tredje är fortfarande öppet, och det är det som mäts här.

**s2, vändningen** (preview-mid). Signaturakten är intakt och är sidans starkaste beslut. Vid
`--flip` 0,5 står exakt en lodrät hårlinje kvar och grunden bakom öppnar sig: lampan, bordet,
rummet. Ingen ram, ingen hörnmarkering, ingen tjocklek som veck. `mattis-studio`-ribban är
därmed uppfylld i pixlar och inte bara i avsikt. Ingen drift.

**s3, baksidan landar** (back-1440, back-390, scroll-1). Fokalskala och z-ordning stämmer:
ALUNIX i 80,6 px mot rubrikens 120 px ger kvot 0,67 och 5,04x brödtexten, kickern 10,5 px,
hårlinjen, monoraden, den typsatta länken med accenten som understrykning och utan pil.
**Drift, defekt:** kickern är `Webbyrå i Sverige`, inte målbildens `Digital byrå`. Det är en
avvikelse från målbilden i signaturaktens egen belöning, den saknar den rad i decision ledger
som `BRIEF.md` kräver (Ett val utan rad skeppas inte, och `NOTES.md` § R3 skriver själv att
raden behövs), och strängen är exakt den kategoriform sidans egen ribba förbjuder: fyra av
fem live-rubriker säger bara vad företaget är och var det ligger, och `Webbyrå i Sverige`
skiljer sig med ett ord från frojd.se:s `Webbyrå i Stockholm`. Låsblockets Reject-fält
förbjuder dessutom SVERIGE på kortbaksidan. **Drift, defekt:** baksidan är ett matematiskt
platt plan, stdev 0,00, mot en grund som mäter 10,9. Två material möts och det ena har ingen
materialitet alls.

**s4, tesen** (scroll-2, preview-bleed). Materialbytet till blått sker, accenten förekommer
exakt två gånger på hela sidan (tesplåtens grund och understrykningen), noll `box-shadow`,
noll `border-radius`. **Drift, defekt:** de två spalterna toppjusterar. `.col` är
`flex:1 1 50%` med `align-items:stretch` och ingen lodrät förskjutning, så blått och papper
börjar på samma y (mätt i preview-ledger: båda vid y = 100). House physics § Structural är
uttrycklig: paired columns never top-align. **Drift, mindre:** bleeden mäter 33 px förbi
kanten inuti en 46 px spaltränna, alltså dör den i rännan och når aldrig grunden. Klassad som
defekt, men under skärningspunkten för de åtta.

**s5, beviset** (scroll-3, preview-ledger). Calyx laddar som riktig sajt, ordscrubben och den
självritande tråden går i bläck och inte i accent, vilket är rättelse 1 utförd. Liggarens tre
rader ligger på registergrad med mononumren. Ingen drift.

**s6, priset** (scroll-4, close-1440). Prisliggaren är hårlinjerader med utskrivna priser,
aldrig kort. **Drift, defekt:** skärmens utpekade displayelement, `Alla har rätt till bra
design.`, renderar 30,4 px, alltså 1,9x brödtexten. TASTE § 4.6 ger två lägen och bara två:
kicker eller display, aldrig en 32 px-mellannivå. `.thesis-headline` ligger i samma band vid
38,4 px. Squinttestet gör det värre: högerspalten bär Hōrais eget 70 px-ordmärke i samma
höjd, så demot slår värdsidans display på dess egen skärm.

**s7, avslutet** (close-1440, full). **Drift, defekt.** Målbilden säger att mailto-raden står
ensam på skärmen och ingenting annat. `.close` är ca 327 px hög och ligger sist i ett 4019 px
högt dokument, så den sista viewporten alltid bär prisblocket och Hōrai-ramen ovanför
adressen. Skärm sju existerar som sektion men inte som skärm.

**Hela sidans takt, defekt.** Dokumentet mäter 4019 px vid 1440 x 900 = **4,5 vh**. Pinnen tar
2295 px av dem, så sex flow-skärmar delar på 1724 px, ca 0,32 vh var. `concepts-V3c.md` § (3)
räknar själv med 9-11 vh inom budgeten 8-14 vh. Konsekvensen syns i pixlar och inte bara i
aritmetiken: scroll-2 visar s4 och s5 samtidigt, scroll-4 visar s6 och s7 samtidigt, och en
feeling curve vars regel är att aldrig två känslor får ligga lika i rad kan inte läsas när
tre akter delar viewport. Densitetsratten säger 3; det byggda läser tätare.

TASTE § 4, rad för rad, som gapstabell:

| Element | Taste expectation | Current state | Gap |
|---|---|---|---|
| § 4.1 auktoritet först | En auktoritet per sida; bär fotot, välj ett snitt som tål vikt 300 i 80 px | Rörelsen bär set-piecet, Public Sans 300 i 120 px utanför kortet | Ingen |
| § 4.2 två snitt, rollerna korsar aldrig | Geist röst, Geist Mono enbart register, Public Sans display och body | Håller i koden; mono i fyra grupper, precis taket | Ingen |
| § 4.3 bilden vald efter typlast | Typ över foto kräver mörkt parti eller vikt 700 | Rubrik och underrad ligger i mörka partier, mätt 13:1 | Ingen |
| § 4.4 ett papper, en accent, en sak | Accenten gör en sak | #1e5e9c exakt två förekomster, verifierade i koden | Ingen |
| § 4.5 sektioner byter material | Färgband, inversion, papper till foto | Blått band, papper, mörkt prisblock, foto hela vägen | Ingen |
| § 4.6 kontrast i skala | Display minst 5x body, aldrig en 32 px-mellannivå | 30,4 px prisrubrik och 38,4 px tesrubrik i det förbjudna bandet | Två element |
| § 4.7 djup utan skugga | Hårlinjer, ton på ton, överlapp | Noll box-shadow, noll radie, hårlinjen är kortets enda kant | Ingen |
| § 4.8 rörelse där typ och bild är tysta | I set-piecet är rörelsen auktoriteten | Rubriken står stilla i full styrka, kortet vänds | Ingen |
| § 4.9 siffror bara om de är sanna | Formen får tas, innehållet måste vara systemets eget | Tre priser ur PRODUCT.md, inga uppfunna tal | Ingen |
| § 4.10 ordmärket får vara heron | Namnet i viewportbredd är tillåtet | ALUNIX bär baksidan i 80,6 px | Ingen |

Grindarna 66-88 och 97-98, gångna: noll versionsetiketter, noll numrerade eyebrows (01-03 är
en riktig liggare, licensierad av house physics), noll scroll-cue, noll fabricerad produkt-UI
(ramarna är byråns egna sajter, inte ritade), noll statusprickar, noll tankstreck, en enda
mittpunkt och den står i `<title>`, noll pilsuffix, `color-scheme` och `theme-color` satta.
Gate 92: noll `border-radius` i hela filen, en enda radieskala och den är 0. Den enda
kvarvarande tellen i det blocket är kickerns ortform.

## ceiling

- `oryzo-ai` (primär): **förlorar**. Referensens objekt bär material över hela sin yta, kork
  mot skärmatta mot trä, och kanten läser under snedljuset var som helst i rotationen. V3c:s
  framsida ligger till 77,6 % under L = 12 vid 1440, så tre fjärdedelar av kortet är tomrum
  utan yta, och rotationen får sin läsbarhet bara ur hårlinjen och ur pölen i nedre vänstra
  hörnet. Det är precis den mätpunkt cellens egen ribba satte mot den här posten.
- `mattis-studio`: **slår**. Referensens hero är en ritad ram med hörnprickar, versionstagg,
  slot-räknare och lokal tid, alltså platt chrome utan baksida. V3c:s kort är ett fysiskt
  objekt som vänds, och vid 90 grader återstår en hårlinje, verifierat i preview-mid. Det
  referensen ändå gör bättre: dess svarta bär filmkorn, så planet är ett material, och dess
  ordmärke fyller ramens bredd i stället för en tredjedel av den.
- `dope-security`: **slår**. Glaskortet, de två fyllda knapparna och den kursiva serifen i
  rubriken är tre grepp V3c avstår, och accenttalet är utskrivet som en siffra och stämmer i
  koden. Det referensen gör bättre: dess fotografiska grund har en riktad ljusramp som
  organiserar hela folden, medan V3c:s ljusstråk går diagonalt bakom rubriken utan att någon
  del av kompositionen använder det.
- `monologue`: **slår**. Centrerad hero med badge-rad, mono som brödtext och 49 mätta skuggor
  är tre saker V3c inte gör. Det referensen gör bättre: hårlinjerastret löper genom hela sidan
  och gör marginalerna synliga, så varje element sitter på en läsbar kolumn. V3c:s
  `--rail-x`-raster är underförstått, och de två blockstaplarna flyter på grunden utan att
  rastret någonstans blir läsbart.
- `planhat`: **slår**. Rubriken ligger i grundens mörka parti och aldrig över ljuspölen, vilket
  var ribban, och V3c avstår den vita fyllda knappen och pilen. Det referensen gör bättre:
  dess fold bärs av ett enda författat fotografi vars ljusstruktur valdes för typen, medan
  V3c:s fold täcker sitt eget motiv med ett svart kort och först visar rummet vid 90 grader.

## material_fixes

- Takten: dokumentet mäter 4019 px vid 1440 x 900 = 4,5 vh mot `concepts-V3c.md` § (3):s egna
  9-11 vh. Höj flow-akterna så att dokumentet landar på minst 8,0 vh (7200 px vid 900), golvet
  i `feel-and-fingerprint.md` § Pacing som cellen själv citerar.
- Kortbaksidans kicker: `Webbyrå i Sverige` bryter mot målbildens `Digital byrå`, mot
  Reject-fältets förbud mot SVERIGE på baksidan och mot ribban att ingen ny rubrik faller
  tillbaka till substantiv plus ort. Sätt strängen till `Webbyrå` (10,5 px, .22 em), som
  behåller copy-gatens eget fynd och tar bort ortformen, eller återställ `Digital byrå`.
- Skärm sju: `.close` är 327 px och delar sista viewporten med prisblocket och Hōrai. Ge
  `.close` `min-height: 82svh` (738 px vid 900) så att adressen står ensam på skärmen, vilket
  är vad målbilden skriver.
- Kortets framsida: 77,6 % av 893 x 498 px ligger under L = 12. Lyft den obelysta ytans golv
  till L 18-24 så att kornet syns, eller vidga pölen, tills högst 55 % av ytan ligger under
  L = 12. Det är `oryzo-ai`-ribban och det tredje av `ASSETS.md` § 3 väg (d):s tre skäl.
- Spalternas toppjustering: `.col` saknar lodrät förskjutning, så blått och papper börjar på
  samma y. Ge den ena spalten 56-96 px `margin-top` på desktop (house physics § Structural,
  paired columns never top-align; editorial-invarianternas egna värden är 96 och 176 px).
- s6:s displayelement: `.price .statement` renderar 30,4 px = 1,9x brödtexten. Ta den till
  minst 80 px (5x 16 px, TASTE § 2.4 och § 4.6) eller ned till kickergrad; `.thesis-headline`
  ligger i samma förbjudna band vid 38,4 px och följer samma dom.
- Kortets baksida och prisblocket är platta plan, mätt stdev 0,00. Lägg house physics eget
  värde för mörka register, korn på 4-5 % opacitet, som fast `pointer-events:none`-lager på
  `.face--back` och `.price`. Inget `filter`, så gate 93:s halvviewportregel rörs inte.
- Gate 62: `.card-cta` mäter ca 19 px hög och `.topline-contact` ca 14 px vid 390. Ge båda
  `padding-block` upp till en 44 x 44 px träffyta under 640 px, utan att flytta
  understrykningens 5 px offset.

## keep

Vändningen rörs inte: `--flip = smoothstep(0.12, 0.72, --sc-ps)` i ren CSS, hårlinjen ensam
vid 90 grader, rubriken och underraden utan transform genom hela akten, och accenttalet två.
Det är sidans enda oersättliga beslut, och varje fix ovan ska gå att göra utan att röra det.

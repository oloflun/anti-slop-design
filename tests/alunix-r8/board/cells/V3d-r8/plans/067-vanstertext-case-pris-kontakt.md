# 067 · V3d: vänstertexten, case-kapitlet, priset och kontakten

- **Status**: TODO (V3d R23, en byggrunda, högst två fixrundor). Byggs efter R22 (plan 066).
- **Beställning**: Anton 2026-09-20, nio punkter. Punkt 3 (tes → ritning) bygger på
  `reviews/r23-astra-estetik.md` (dom `fix`) och ligger som **steg 7**.
- **Estimated scope**: 1 fil, `runs/V3d/index.html`. `scroll/*.js`, `scrollcraft.css`,
  `sites/*` orörda. Exakt två levande iframes, ramarna transformeras aldrig. Inga nya
  typsnittsfiler; **en tas bort** (steg 3).
- **Copy**: `COPY-V3d-r23.md` är klar. Stegtexterna är **35–44 ord, tre meningar** (R18:s var
  18–22 — det ändrar `--band-h` och radantalen i steg 2, talen nedan är räknade mot de
  faktiska längderna). Case-ingressen är **alternativ A**, ordagrant. Kontaktsektionens
  strängar ligger i samma fil. **Byggaren hittar aldrig på en sträng.**
- **Underlag, läst som bilder**: egen fångst (Playwright, Chromium med
  `ignore_default_args=['--hide-scrollbars']`, `mouse.wheel`, en skärmbild per sida, aldrig
  kontaktark): 1920x930 och 390x844 genom folden, processakten, case-ingången, priset och
  sidfoten. Astras egna 48 bilder och mätskript i `shots/astra-r23/`
  (`sweep23.py`, `ink23.py`, `anchors23.py`, `shots23.json`).
- **Sökvägsrättelse**: `~/example-design-system/sites/` finns inte på maskinen.
  Referenssajterna ligger i repots egen `sites/`: `sites/hyperborea.html`,
  `sites/horai.html`, `sites/calyx.html`. `sites/*` **rörs aldrig**.
- **Rättelse till ett tidigare fynd**: den ljusa stumpen till vänster om arket är
  `.thesis-ticks i` (`index.html:661–664`), inte landningslinjen. Astra dödade fyndet
  själv; det blev material_fix 4 och ligger i steg 7 (C9).

## Uppmätt nuläge (R22)

| | 1920x930 | 1440x900 | 390x844 |
|---|---|---|---|
| `.hero-sub` | 15,2 px, 330 px bred, högerställd i foldens nederkant (x 1484–1814, y 833–902) | samma, x 1014–1344 | 15,2 px, två rader under kortet, y 714–760 |
| `.hero-stage` | `justify-content:center`, padding 52,1/20,5 | center, 50,4/19,8 | `flex-end`, padding-bottom 84,4 |
| `.process-stick` | sticky `top:219px`, höjd 711, padding `9,3px 96px 18,6px` | `top:216`, 684 | `top:0`, 241,5, padding `12px 0` |
| `.process-sheet` | 1214,4 x 683 = **63,4 % vw** (höjdbunden) | 1168 x 657 = **81,1 % vw** | 348 x 217,5 = 89,2 % vw |
| `.step-band` | full bredd, `--band-h` 219, siffra 168, rubrik 32, text 32 px | 216 / 168 / 28,16 / 28,16 | statisk i flödet, 243 / 85,8 / 21,85 / 21,85 |
| Död yta i steg 03 | ~255 px tom grund på **vardera** sidan om arket + 680 px tom grund till höger om bandets text | ~50 px per sida + 300 px | – |
| `#case` | 930 hög; **333,3 px tom grund över rubriken, 333,3 px under ingressen**; innehållsblocket 263,4 px = 28,3 % av skärmen | 321,9 / 321,9, 256,2 = 28,5 % | 324,5 / 324,6, 194,9 = 23,1 % |
| Ingress → casets överkant | **538,7 px** | – | **905,6 px** |
| `Exempelcase` | Young Serif 400, **136 px**, ordbild **860 x 192** | 129,6, 820 x 183 | 40, 253 x 57 |
| `.case-name` Calyx / Hōrai | Geist kursiv **171,4**, ordbild **468 x 223** / Geist versaler 135,0, 470 x 176 | 122,5, 334 x 159 / 96,5, 336 x 125 | 36, 98 x 47 / 36, 125 x 47 |
| Ordbildens breddkvot intro ÷ Calyx | **1,84x** | **2,45x** | **2,57x** |
| `.case-line` | Public Sans 300 **44 px** ("fick bli ett vårnummer.") | 33,12 | **17** |
| Övergång ritning → case | hård kant: arkets underkant 24 px över skarven, sedan 333 px tom grädde innan rubriken | samma | samma |
| `.price .statement` | Young Serif 400 **96 px**, 2 rader | 86,4 | 40 |
| `.price-row .value` | Young Serif 400 **64 px**, x 838 | 48,96, x 899 | 32 |
| `.price-row .label` | Public Sans **600** 17 px — **syntetisk fetstil** (enda vendorade Public Sans-vikten är 300) | samma | samma |
| Liggarens hårlinjer | y 461 / 580 / 677 / 768 → radband **119 / 97 / 91 px**, tre olika | – | – |
| `.price-ledger` | 1040 px bred i en 1728 px innehållsruta = 60 %; avslutets hårlinje 527 px ligger 39 px under liggarens 1040 px | 1040 av 1267 = 82 % | 333 |
| `<footer class="close">` | delar prisets fotografiska grund, `.close-mailto` Geist 700 21,1 px | 19,4 | 17 |
| Typsnitt | 3 vendorade filer (Public Sans 300, Geist 700, Geist Mono 400) **+ Young Serif via Google Fonts** = 4 familjer mot budget 3; Young Serif på exakt 3 ställen: `.cases-title`, `.price .statement`, `.price-row .value` | | |
| Dokumenthöjd | 30 598 | 29 641 | 25 033 |

### Nuläge i övergången tes → ritning (Astras `sweep23.py`, 93 bildrutor vid 1920, 73 vid 390)

| | 1920x930 | 390x844 |
|---|---|---|
| Synlig textyta, y6520 → y6800 | **43,6 % → 8,2 %** av viewporten; över 21 % igen först vid y7600 | – |
| Sträcka under en femtedel av normalt bläck | **1 080 px = 1,16 viewport** | – |
| Bildrutor med **noll** textrektanglar | 0 | **4 i rad** (y5960, 6000, 6040, 6080); 260 px utan något läsbart (y5900–6160) |
| Ritsträckan `tx` 0 → 1 | **594 px** | **539 px** |
| Fyllningens kanter mot linjernas, y6720 | fyllning x 117–1792, linjer x 348 och 1560 → **231 / 232 px isär** | – |
| Mellanrum mellan de fyra linjerna | **269 / 377 / 565 px** — tre olika i rad | – |
| Linjernas slut | y 348–656 i en rektangel som går till y 806 → **150 px tom botten** | – |
| Landningen | 1 213 px hårlinjelåda, två streckade lodräta linjer, **ingenting i sig**, 30–45 % av bildrutan i **440 px** scroll | **två staplade tomma lådor**, y 180–297 och 297–515 = 40 % av viewporten |
| Kapitelskärmen (A16, y7700) | rubrik + ingress i övre 290 px, sedan **390 px död svart** före steg 01 | – |
| Färgdraget | `color-mix` på `--tx` ger en döv skiffer vid halva draget; A07 är tre närliggande blågrå toner i samma bildruta — mekaniskt sann, **optiskt osynlig** | – |
| `.thesis-ticks i` | grundton 38 % vit, **släcks aldrig** → fyra 32x2 px-streck på x 96–254 är det enda märket i ett tomt blått fält genom hela övergången (A05, A07, A09, A11) | – |

## Problem, punkt för punkt

1. Underraden är en liten beskrivande text i ett hörn — samma kategori som allt F-016 redan
   rensat, och den enda kvar i folden.
2. Processakten har **två tomma sidomarginaler** kring arket och en tom högerhalva i bandet.
   Texten står över arket, inte bredvid det, och på mobilen rullar sju textblock förbi i
   flödet utan byte.
3. Astra erkänner sitt eget fel i r21: hon **mätte formens area och tog den för närvaro**.
   En stor tom rektangel är inte närvaro, det är frånvaro i skala, och ju större den är
   desto tydligare syns det att ingenting finns i den. Codex bästa rad, som hon tog:
   **ankomsten läses som ett försvinnande.**
4. Case-kapitlet är 930 px högt för 263 px innehåll: 72 % tom grädde, symmetriskt inramat.
   **`Exempelcase` är sidans största ord** — 136 px slår hjältens tesmening (96), prisets
   statement (96) och processkapitlets rubrik (120). En etikett satt större än varje
   påstående sidan gör. Ordbilden är 1,84 / 2,45 / 2,57 ggr bredare än Calyx. Övergången in
   i kapitlet är en rak kant under arket, och avståndet till caset är en hel skärm.
5. `.case-line` är skriven som en sats i satsstorlek (44 px). Som etikett konkurrerar den
   med namnet; vid 390 står den redan i 17 px, alltså i småtextens register.
6. Den gamla ingressen upprepar det case-etiketterna nu säger.
7. Serifen bär hela prisenheten. Tas den bort finns ingen bärare kvar av skillnaden
   pris/beskrivning — och etiketterna står redan i en syntetisk 600-vikt som inte finns i
   filen. Radbanden är dessutom ojämna och två olika långa hårlinjer ligger 39 px isär.
8. Kontakten är en understruken adress i sidfoten. Det finns ingen sektion att drivas till.
9. Sidan slutar på samma fotografiska grund den började på, utan en sista växling.

---

## Beslut

**B1 · Heron får ingenting i stället.** `.hero-sub` tas bort helt, med sin egen
marginalregel och sin 640-överstyrning. `.hero-stage` är `justify-content:center` ≥ 641 och
`flex-end` ≤ 640 — layouten omcentrerar sig själv, ingen ny regel behövs. Rubriken behåller
sin clamp: `--h1-hrate`-budgeten (`index.html:206–217`) är räknad **med** underradens
68,4 px, så en större rubrik skulle spränga foldens summa och P01:s kvot mot kortbaksidan.
Den frigjorda ytan går till luft; vid 1920/1440 avslöjar den mer av studiofotot i
högerkanten, vid 390 flyttar den luften upp över rubriken.

**Låst copy.** `Vi skapar skräddarsydda webbplatser som hjälper er att exponera
verksamheten.` är låst i `PRODUCT.md` § Brand Commitments. Anton har hävt låset för just
den strängen 2026-09-20 — samma mekanism som `VI BYGGER ERT VARUMÄRKE.` och de tre
`Exempelsida:`-bildtexterna 2026-09-19. **Låst-copy-räkningen går 12 → 11 synliga rader.**
`PRODUCT.md` redigeras av lead, inte av byggaren.

**B2 · Processakten blir två spalter ≥ 1024, arket flush mot högerkanten.**
`.process-grid` får `grid-template-columns: clamp(18rem,23vw,28.75rem) minmax(0,1fr)`,
`padding-left:var(--rail-x)`, **ingen** högerpadding. `.process-steps` flyttar till spalt 1,
`.process-stick` till spalt 2 med `top:0;height:100svh;padding:clamp(12px,2svh,24px) 0`.
Arket är därmed **breddbundet i stället för höjdbundet** vid varje bredd — det är den
mekaniska orsaken till dagens 63,4 % vid 1920, och den försvinner. Gridbrottet (arket möter
viewportens kant) är husets eget drag, redan dömt i P17/P19.

**B3 · Bytesmekaniken är den befintliga, inte en ny.** `.step-band` behåller
`position:sticky;top:0;height:var(--band-h);background:var(--bg)` och `--slit-p`-klippet
(`index.html:1341–1347`). Det avgående blocket skjuts av sticky-mekaniken förbi `y=0` exakt
när det inkommande öppnar ur sin springa — precis den geometri som gav **0 glyfspringor** i
R18, R21 och R22. Inget nytt fönster, ingen ny formel, ingen ny klocka.
Vägt mot `.cs`-grammatiken ur case-sektionerna: den skulle kräva att slotten centreras
vertikalt och att `--s1..--e7`/`--k1..--k7`-ankringen räknas om — fyra rundors tuning
(plan 048 F, 051 fix 1, 053 fix 3) i spel för noll synlig vinst.

**B4 · Slotten står i spaltens överkant, arket centrerat i sin.** Textslotten är `top:0`;
arket är vertikalt centrerat i sin 100svh-spalt. Spalterna toppjusterar alltså **inte** —
det är avsiktligt (house-physics: paired columns never top-align). Slotten är en enspalt:
siffran (168 px, P07 ≥ 150) överst i full spaltbredd, rubriken under, texten under den.
Vägt mot en vertikalt centrerad slot: då reser sig det avgående blocket genom skärmens övre
halva medan det inkommande öppnar — två texter i samma bildruta, exakt det kunden inte vill
ha.

**B5 · Bandets vågräta hårlinje blir spaltens lodräta.** `.step-band{border-bottom}` gällde
full bredd och skulle nu skära tvärs över arkets spalt. Den flyttas till
`.process-steps li{border-right:1px solid var(--c-line-on-dark)}` — en marginallinje som
löper genom exakt de sju stegen och slutar med steg 07. Ritningsregistret får sin egen
snittlinje och det kostar noll bredd (rännan finns redan).

**B6 · 768–1023 rörs inte.** Tvåspaltsreglerna ligger i `@media (min-width:1024px)`. Vid 768
skulle spalt 2 bli 400 px (52,8 % vw) och arket 400x225 — sämre än dagens. Bandformen
768–1023 är verifierad i R18/R21/R22 och står kvar oförändrad.

**B7 · Mobilen: arket över texten, och texten byts.** Ordningen är dagens
(`.process-stick{order:-1}`, arket sticky i överkanten) och den är rätt: ritningen är
objektet och måste synas medan dess steg läses, och det är den enda ordning P07–P13 hållit
vid 390. Det nya är att `.step-band` blir **sticky under arket** (`top:var(--sheet-h)`) med
egen höjd och samma `--slit-p`-klipp, som i dag är skopat `min-width:768px`. Sju textblock
som rullar förbi blir sju scener.

**B8 · Young Serif tas bort.** Efter steg 3 används den på **ett enda ord** på hela sidan.
Kostnaden är sidans enda tredjepartsförfrågan, två `preconnect`, en fjärde familj mot budget
tre, och ett beroende som gör att kapitelrubriken renderar i Georgia om nätet sviktar.
Nyttan är en egen röst åt ett ord som punkt 4 samtidigt gör **underordnat**. `Exempelcase`
sätts i `--f-display` (Geist 700) — samma röst som `#process-title`, alltså Alunix egen
kapitelröst, medan de två case-namnen behåller sajternas röster. Trerösterslogiken vid
`index.html:975–981` står kvar; det är kapitlets röst som återgår till husets.
**Öppna posten "fyra typsnittsfiler mot budget tre" stängs av detta steget.**

**B9 · Prisrubriken sätts i Geist 700, inte i syntetisk Public Sans-fet.** Kundens order är
"samma som brödtexten med fetstil endast på rubriken". Public Sans finns i exakt **en** vikt
i repot (300). En `font-weight:700` på den familjen ger syntetisk fetstil — en
renderingsdefekt, inte en typografi. Geist 700 **är** den här sidans fetstil och bär redan
varenda annan rubrik. Samma skäl åt andra hållet: `.price-row .label{font-weight:600}` är
också syntetisk i dag och går till 300. Astras "vikt 400" på siffror och etiketter betyder
"inte halvfet"; i den här filen skrivs det `font-weight:300`, som renderar identiskt och
**inte ljuger i CSS:en**.

**B10 · Hierarkin i liggaren bärs av fyra saker i stället för av ett snitt**, i Astras
ordning: (1) **spaltpositionen** — en fast, högerställd värdekolumn (`min-width:11ch`,
`text-align:right`) så alla tre raderna slutar på exakt samma lodräta även när värdet är en
fras; (2) **tabulära versalsiffror** — `tabular-nums lining-nums`, den enskilt viktigaste
detaljen i hela bytet, eftersom Young Serifs proportionella siffror lägger tusentalsluckan
på olika x i de två raderna; (3) **storleken, lägre än man tror** — 48 px mot en 19 px
etikett är 2,5:1, alltså en liggare, medan 3,3:1 fortfarande är en annons; (4)
**hårlinjerna som struktur** — lika radband på 24–28 px. Taket är `sites/horai.html`, som
redan sätter beloppet högerställt i egen spalt med enheten liten.

**B11 · Kontakten är en egen sektion på papper, och sidfoten följer med dit.** `#kontakt`
läggs mellan `#pris` och `</main>`, på `--bg`/`--ink` — sidans ljusaste grund, den som ger
formulärfälten högst kontrast och sidan sin sista materialväxling. Sidfoten byter till samma
grund och blir därmed formulärets **alternativa väg in**: hårlinjen och `kontakt@alunix.se`
står direkt under knappen. Ingen ny adressrad skrivs, antalet `mailto` på sidan står kvar
på två (toppraden + sidfoten).

**B12 · Papperet framkallas ur mörkret, spegelvänt mot P20.** Skarven pris → kontakt får
samma grepp som den som redan håller: `#kontakt::before` är en svart slöja vars opacitet går
1 → 0 på sektionens eget `--sc-ps` (0,02 → 0,24), och innehållsblocket skärps ur oskärpa på
samma klocka (0,06 → 0,26), exakt som `.price::after` + `#pris-title` gör åt andra hållet.
Ingen ny grammatik, F-014, reversibelt, inget `prefers-reduced-motion` (F-011).

**B13 · Formuläret har ingen backend och ljuger inte om det.** `submit` avbryts,
`reportValidity()` sköter valideringen (webbläsarens egen, inga egna felsträngar), en
`mailto:`-URL med ifyllt ämne och brödtext öppnas i besökarens **egen** e-postklient, och en
`role="status"`-rad säger vad som hände. Fälten töms aldrig. Knappen döljs utan JS
(`html:not(.js)`), så sidan visar aldrig en knapp som inte gör något; utan JS är den synliga
adressen vägen in. Ingen `action`, ingen `fetch`, ingen tredje part.

**B14 · Inga hjälptexter, men riktiga `<label>`.** F-016 förbjuder *beskrivande* småtext. En
`<label>` **identifierar** fältet och klarar funktionstestet — men den sätts i
brödtextstorlek (19/18/17 px), aldrig i 10,5 px mono, och den säger bara fältets namn.
`placeholder=" "` (ett blanksteg, aldrig synlig text) finns enbart som CSS-krok för
ifyllt-tillståndet. Statusraden är resultatet av en handling, inte en stående rad, och visas
först efter submit.

### Beslut för steg 7 (övergången tes → ritning)

**C1 · Rektangeln är arkets bredd plus ett titelfält, inte 16:9.** Plan 062:s "landar exakt
på arkets rektangel" var ett planbeslut, inte en § keep-post, och Astra har nu dömt dess
resultat. Den landade rektangeln behåller **arkets exakta bredd** (`--x1`…`--x4`, samma tal
`measureAct` redan skriver) — det är x-kontinuiteten ögat faktiskt spårar in i steg 01 — och
får höjden `--dn-draw + --stamp-h`:
- `--dn-draw = min((--x4 − --x1) × aspect, 0.46 × vh)` (aspect 495/880 ≥ 768, 200/320 därunder)
- `--stamp-h` = stämpelrutans uppmätta höjd (rubrik + låst rad + inre luft), skriven av `measureAct`

Rektangelns **underkant** är stämpelrutans botten; landningslinjen ligger vid `--dn`, alltså
mellan ritytan och stämpelrutan. `--pl-b` är fortfarande 0, så R22 fix 2:s geometri
(`--pl-l`/`--pl-r` mot planets **egen** `getBoundingClientRect()`) och R22 fix 1:s
`::after`-kontur är orörda — § keep hålls.

**C2 · Rubriken stannar utanför `.tes-plane`, positioneras mot den.** `.tes-plane` är
`aria-hidden` och `pointer-events:none`; en `h2` får aldrig ligga i den. Stämpelrutan är en
egen box i `.process-chapter`, absolut positionerad mot **samma** `--x1`/`--x4`/`--dn`-tal,
med `#process-title` och `.process-locked` flyttade in i den. Rubriken är fortfarande en
`h2` i flödesordning, `.process-locked` fortfarande den låsta raden ordagrant.

**C3 · Draget halveras och klockan räknas, inte gissas.** `measureAct` skriver `--tx-a` och
`--tx-b` ur den uppmätta kapitelhöjden, så kravet 260–300 px (1920) / 220–260 px (390)
håller vid **varje** bredd utan att byggaren skriver in ett tal:

```
DRAW     = (vw >= 768) ? clamp(240, .30 * vh, 300) : clamp(210, .28 * vh, 260)
life     = chapterH + vh
--tx-b   = DRAW / life                       /* fönstrets bredd */
--tx-end = (--dn + .14 * vh) / life          /* tx = 1 när landningslinjen står på .86 vh */
--tx-a   = --tx-end - --tx-b
```

Plan 061 B1:s hårdkodade `(--sc-ps − .07) / .29` faller — den var giltig bara så länge
kapitlet var exakt 120svh.

**C4 · R14:s dröjfönster rivs, på Astras bevis.** `.process-chapter{min-height:120svh}`
(plan 059 R14) skapades för att kapitlet skulle stå **ensamt** i ett 20svh-fönster. Astras
tre referenser säger raka motsatsen: rubrik och första innehåll delar alltid skärm, och vår
egen A16 mäter 390 px död svart mellan dem. `min-height` går till
`clamp(560px, 86svh, 920px)`. R14:s kommentar rättas i samma steg — beslutet är
**omkullkastat av mätning**, inte glömt.

**C5 · De två textplatserna är en överlämning i samma skärm, inte två platser i samma scen.**
- Under kapitlet bor texten **inne i arket**, i stämpelrutan, på x ≈ `--x1 + inset`.
- Under stegen bor texten i **vänsterspalten**, på x = `--rail-x`.
- De är aldrig samtidigt bärande. Men de ska ses lämna över: C4 gör kapitlet kort nog att
  steg 01:s slot redan öppnat i vänsterspalten i den bildruta där stämpelrutans rubrik når
  100 % bläck. Texten kliver alltså **ut ur ritningen och ställer sig bredvid den**, i en
  bildruta, och vänsterspalten som annars stått tom genom hela skarven får sitt innehåll i
  samma ögonblick arket får sitt. Det är ett **förebud**, och det mäts som ett (Target 7:5).

**C6 · Konturen är fyllningens kant genom hela draget** (material_fix 3). Linjernas x
interpolerar på samma `--tx` som klippet:
`left: calc(var(--sxN) + (var(--xN) - var(--sxN)) * var(--tx))`, där `--sx1` = planets egen
vänsterkant, `--sx4` = dess högerkant − 1, och `--sx2`/`--sx3` på 195,6/880 och 469,3/880 av
planets **fulla** bredd. Vid `tx` 0 är linje 1 och 4 planets egna kanter; vid `tx` 1 är de
arkets. Uppmätt avvikelse mot den klippta rektangelns kanter **≤ 2 px i varje tx-läge** — i
dag 231/232 px vid tx ≈ 0,5.

**C7 · Strecken får ett arbete.** De behåller arkets egna stationer (320 och 768 av 1440, de
tal ritningen själv skyltar i steg 02 — en jämn spaltdelning vore en lögn om ritningen) men
**slutar i stämpelrutans överlinje**: `.seam-dn{height:var(--dn)}`. Då läser de som fyra
mätlinjer ned till en ruta i stället för som fyra streck som tar slut 150 px för tidigt i en
tom yta.

**C8 · Färgen gör ett hopp sent.** `color-mix` på rå `--tx` ger en döv skiffer i mitten som
varken är accenten ovanför eller ritbordets ton under. Arket hålls på `--c-accent` till
`tx` 0,75 och vänder över sista fjärdedelen.

**C9 · Tesens prickar släcks när tesen är slut** (material_fix 4). `.thesis-ticks i` har
grundton 38 % vit och släcks aldrig, så fyra 32x2 px-streck är det enda märket i ett tomt
blått fält genom hela övergången. En rad, på tesens egen `--sc-ps`, F-014, reversibel.

**C10 · Ingen ny konstnärlig riktning.** Metaforen (§ keep: "byt inte metafor"), R21:s
borttagning (`position:absolute`, aldrig `fixed`), R22:s två fixar, rubrikens inbläckning
62 → 100 % efter landningen, och `--p-edge`-fönstret 0,6 → 0,9 står alla kvar. Steget
flyttar text in i en form som redan finns; det uppfinner ingen.

---

## Steps, i byggordning

### Steg 1 · `.hero-sub` bort (punkt 1)

1.1 Markup: radera `<p class="hero-sub">…</p>` (`index.html:1766`).
1.2 CSS: radera `.hero-sub`-regeln (`:576–578`) och dess `@media (max-width:640px)`-överstyrning (`:594–595`).
1.3 Kommentaren vid `--h1-hrate` (`:206–217`) rättas: höjdbudgetens underrad finns inte längre, rate-paret står kvar oförändrat och varför.
1.4 Låst-copy-kontrollen går **12 → 11** rader. Lead uppdaterar `PRODUCT.md` (inte byggaren).

**Target 1**

| Mätvärde | 1920x930 | 1440x900 | 390x844 |
|---|---|---|---|
| `document.querySelectorAll('.hero-sub').length` | 0 | 0 | 0 |
| Strängen `exponera verksamheten` i `document.body.innerText` | 0 träffar | 0 | 0 |
| Luft under kortets underkant till foldens underkant | 40–110 px | 40–110 px | **≤ 96 px** |
| Luft över `h1`:s överkant | ≥ 90 px | ≥ 88 px | ≥ 120 px |
| `h1` font-size | **oförändrad** 119,04 | 115,2 | 46 |
| Kortets rektangel | **oförändrad ±2 px i bredd/höjd** | samma | samma |
| Pixeldiff mot R22, `?preview=back` | endast underradens rektangel skiljer | samma | samma |
| Låst copy | 11/11 synliga rader | 11 | 11 |

---

### Steg 2 · Processakten i två spalter (punkt 2) — rundans största drag

Byggs **före** steg 5 och 7: `measureAct` läser `.process-sheet`s rektangel för
`--x1..--x4`, `--dn`, `--pl-t/-r/-l`, och de talen ändras av det här steget. *Ett djärvt drag
backas aldrig för att laga ett fel* — följdfel lagas i samma runda.

2.1 CSS, nytt block, skopat `@media (min-width:1024px)`. Ersätter `.process-grid`,
`.process-stick` (`:1250–1256`) och `.step-band`s gridplacering (`:1286–1302`):

```css
/* PLAN 067 B2/B3/B4. Två spalter: stegtexten VÄNSTER om ritningen, arket
   flush mot viewportens högerkant. Arket är breddbundet, aldrig höjdbundet
   (det var --band-h i höjdformeln som gav 63,4 % vw vid 1920).
   INTE en rullande lista, INTE ett band över arket, INTE en ny bytesformel
   - sticky top:0 + --slit-p är R18/R21/R22:s egen, med 0 glyfspringor. */
@media (min-width:1024px){
  .process-grid{grid-template-columns:clamp(18rem,23vw,28.75rem) minmax(0,1fr);
    column-gap:clamp(28px,3.2vw,64px);padding-left:var(--rail-x);}
  .process-steps{grid-area:auto;grid-column:1;}
  .process-steps li{border-right:1px solid var(--c-line-on-dark);}   /* B5 */
  .process-stick{grid-area:auto;grid-column:2;top:0;margin-top:0;
    height:100svh;padding:clamp(12px,2svh,24px) 0;justify-content:flex-end;}
  .process-sheet{width:min(100%,calc((100svh - 2 * clamp(12px,2svh,24px)) * 880 / 495));}
  .step-band{grid-template-columns:minmax(0,1fr);grid-template-rows:auto auto 1fr;
    padding-right:clamp(14px,1.6vw,32px);border-bottom:0;}
  .step-band > .ledger-num{grid-column:1;grid-row:1;}
  .step-band > .process-step-title{grid-column:1;grid-row:2;}
  .step-band > .process-p{grid-column:1;grid-row:3;max-width:none;}
  .process-steps li{min-height:calc(var(--band-h) + 72svh);}          /* 2.4 */
  .process-steps{padding-bottom:calc(80svh + var(--band-h));}         /* 2.4 */
}
```

2.2 Mobilen (`@media (max-width:767px)`), B7. `.step-band{position:static;height:auto;display:block;border:0}`
(`:1579`) ersätts av en sticky slot under arket, och `--slit-p`-klippet (`:1341–1347`) skopas
om från `min-width:768px` till **alla** bredder:

```css
/* PLAN 067 B7. Samma byte som på skrivbordet, roterat: arket sticky överst
   (order:-1, oförändrat), textslotten sticky direkt under det. INTE sju
   block som rullar förbi i flödet. */
@media (max-width:767px){
  .step-band{position:sticky;top:var(--sheet-h);height:var(--band-h);
    background:var(--bg);display:block;border:0;overflow:hidden;}
  .process-steps li{min-height:calc(var(--band-h) + 48svh);}
}
```

`--band-h` mäts i dag bara på skrivbordet (`:2480–2489` skriver `--sheet-h` på mobil).
Mätblocket utökas: på mobil skrivs **både** `--sheet-h` och `--band-h` (högsta
`.step-band`s `scrollHeight`), i den ordningen, före li-rektanglarna läses.

2.3 Markup: de sju `p.process-p` får `COPY-V3d-r23.md`:s kolumn **final** ordagrant
(P01–P07, 35–44 ord, tre meningar). STOPP om filen saknas.

2.4 Släpppunkten räknas om. `.process-stick` är nu `100svh` i stället för
`100svh − var(--band-h)`, alltså släpper den `--band-h` px **tidigare** relativt band 07.
`padding-bottom` höjs med exakt samma tal. `li{min-height}` är `band-h + 72svh` (inte 90svh):
med den nya copyns längd ger 90svh +26 % aktlängd. Plan 053 fix 3:s villkor står kvar och
**mäts**, gissas aldrig: stickens släpp ska ligga efter band 07:s eget.

2.5 Kommentarerna vid `.process-grid`, `.step-band` och `#process .ledger-num` får en
`PLAN 067 N.`-rad med sin INTE-rad.

**Target 2**

| Mätvärde | 1920x930 | 1440x900 | 390x844 |
|---|---|---|---|
| Arkets bredd | **≥ 1300 px och ≥ 67 % av `clientWidth`** (i dag 1214,4 / 63,4 %) | **≥ 950 px och ≥ 66 %** (i dag 1168 / 81,1 %, se Q1) | oförändrat 348 / 89,2 % |
| Arkets högerkant mot viewportens | **0 px** (flush) | 0 px | – |
| Arkets höjd | ≥ 730 px = ≥ 78 % vh | ≥ 535 = ≥ 59 % vh | oförändrad |
| Textspaltens bredd | 420–460 px | 320–345 px | – |
| Textens mått | 26–30ch, `.process-p` **32 px** (får ej regressera) | 23–26ch, **28,16 px** | **21,85 px** |
| Radantal `.process-p`, längsta steget (P03, 44 ord) | **≤ 10** | **≤ 12** | **≤ 16** |
| Siffran | 168 px (P07 ≥ 150) | 168 | 85,8 |
| `--band-h` | **≤ 640 px** | **≤ 660 px** | **≤ 420 px** |
| Textspaltens fyllnadsgrad (slottens höjd ÷ vh) | **0,55–0,72** | **0,60–0,78** | – |
| Varje `.step-band` `scrollHeight` | ≤ `--band-h` | ≤ | ≤ |
| **Glyfspringa**: hjul 20 px ned **och** upp genom alla sju band | högst två band med synlig area > 0 samtidigt, och när två syns har det inkommande `--slit-p` ∈ (0,1); bytesbildrutorna 02→03 och 06→07 lästa som bild | samma | **samma — nytt krav vid 390** |
| Ingen text under slottens underkant i någon bildruta | 0 | 0 | 0 |
| Lodrät hårlinje | finns, 1 px, löper exakt sju steg och slutar med 07 | samma | ingen (enspalt) |
| Död yta: bredaste tomma lodräta remsa som löper hela viewporthöjden i `?preview=process-03` | **≤ 96 px** (i dag 255 px på två ställen) | ≤ 80 px | – |
| Varje `?preview=process-0N` landar på sitt `--eN` | 7/7 | 7/7 | 7/7 |
| `.process-stick` släpper **efter** band 07 | ja, mät i px | ja | – |
| Aktens höjd `#process` | **≤ +15 %** mot R22 | ≤ +15 % | ≤ +15 % |
| Dokumenthöjd | ≤ +10 % mot R22 | ≤ +10 % | ≤ +10 % |
| Horisontell scroll (elementrektanglar, gate 34) | 0 vid 320–1920 | | |
| 768x1024 | **pixeldiff 0 mot R22** i `?preview=process-01/-03/-07` | | |

**Lever om `--band-h` eller aktens höjd spräcker taket:** sänk `li{min-height}` till
`band-h + 64svh`, därefter `row-gap` till 6 px. Räcker inte det: **STOPPA**.

---

### Steg 3 · Prissektionens typsnitt och hierarki, och typsnittsbudgeten (punkt 7)

3.1 `.price .statement` → `--f-display` (Geist 700), `letter-spacing:-.03em`, `line-height:1`,
`font-size:clamp(2.25rem,4.4vw,5.25rem)` → **84 / 66 / 36 px**, `max-width:15ch`.
3.2 `.price-row .value` → `var(--font)`, `font-weight:300`, `--fig:clamp(1.75rem,2.5vw,3rem)`
→ **48 / 36 / 28 px**, `line-height:1`, `letter-spacing:-.01em`,
`font-variant-numeric:tabular-nums lining-nums`, `min-width:11ch`, `text-align:right`,
`color:var(--invert-ink)`. `.value--text` (`Pris vid förfrågan`) → **27 / 22 / 17 px**, mot
samma högerkant, på radens baslinje (F-017).
3.3 `.price-row .label` → `font-weight:300`, `font-size:clamp(1.0625rem,.85rem + .28vw,1.1875rem)`
→ **19 / 18 / 17 px**, `color:color-mix(in srgb,var(--invert-ink) 82%,transparent)`,
`max-width:58ch`.
3.4 Enheten `kr` i etikettstorlek: `26 900 kr` → `26 900 <span class="unit">kr</span>`.
`textContent` oförändrat, låst copy orörd. `.unit{font-size:19px/17px;margin-left:8px;
color:color-mix(in srgb,var(--invert-ink) 72%,transparent)}` på samma baslinje.
3.5 Radbanden: `.price-row{padding:clamp(24px,3svh,28px) 0}` och
`.price-row::after{margin-top:clamp(24px,3svh,28px)}` — lika höga band i stället för dagens
119 / 97 / 91 px. `.price-ledger{max-width:min(100%,max(1040px,62vw))}`; alla hårlinjer till
samma högerkant som siffrorna. Vid ≤ 768: `.price-row{flex-direction:column;align-items:stretch}`
och `.value{align-self:flex-end}`.
3.6 Avslutets hårlinje: `.close-rule{align-self:stretch}` (kollapsar i dag till 527 px av
`align-items:flex-start`) och samma högerkant som liggaren.
3.7 **Young Serif bort** (B8): `--f-serif`-token, Google Fonts-`<link>`, de två
`<link rel="preconnect">` (`:93–95`) och kommentaren `:87–92`. `.cases-title` →
`font-family:var(--f-display)` (storleken sätts i steg 4).
3.8 Kommentarerna `:850–852` och `:925–929` skrivs om.

**Target 3**

| Mätvärde | 1920x930 | 1440x900 | 390x844 |
|---|---|---|---|
| `Young Serif` i någon `font-family` på sidan | **0 element** | 0 | 0 |
| Nätverksförfrågningar till `fonts.googleapis.com`/`fonts.gstatic.com` | **0** | 0 | 0 |
| Typsnittsfiler totalt | **3** | 3 | 3 |
| `.price .statement` | Geist 700, **84 px** (±2), 2 rader | **66** (±2), 2 rader | **36**, 3 rader |
| `.price-row .value` | Public Sans 300, **48 px** (±1) | **36** (±1) | **28** |
| `.value--text` | **27 px** (±1), radens baslinje | **22** | **17** |
| `.price-row .label` | Public Sans 300, **19 px** (±0,5) | 18 | 17 |
| Enheten `kr` | 19 px, 8 px från beloppet, samma baslinje, ~72 % ton | 18 px | 17 px |
| Syntetisk fetstil någonstans i `#pris` | **0** | 0 | 0 |
| Siffra ÷ etikett, font-size | **2,5:1** (±0,15) | 2,0:1 | 1,65:1 |
| **Tusentalsluckans x i rad 1 och rad 2** | **identisk ±0,5 px** | ±0,5 | ±0,5 |
| De tre värdenas högerkant | samma x ±1 px | ±1 | ±1 |
| Radbanden (avstånd mellan hårlinjer) | **lika inom 4 px** (i dag 119/97/91) | ±4 | ±4 |
| Alla hårlinjer till samma högerkant som siffrorna | ja | ja | ja |
| Ingen hårlinje inom 80 px av en annan hårlinje med annan längd | ja | ja | ja |
| Liggarens bredd | 1160–1200 px | 1040 | 333 |
| Prisenheten på en skärm (§ keep) | rubriken ≥ 48 px från toppen, liggarens underkant ≥ 24 px från botten, allt i en bild; höjden tas ur rubrikens och ingressens marginaler, aldrig ur radbanden | samma | samma |
| Kontrast, all text i `#pris` mot renderad grund | ≥ 4,5:1 | ≥ 4,5:1 | ≥ 4,5:1 |
| `.price-row .value` `textContent` mot `PRODUCT.md` | ordagrant, inkl. blanksteg | samma | samma |
| Delade ord i `.price-row` | 0 vid 320–1920 | | |
| Liggarens fyra hårlinjer når `scaleX(1)` medan liggaren är i viewporten | ja | ja | ja |
| Inline-hex i filen | ≤ R22:s antal | | |

---

### Steg 4 · Case-kapitlet: storlek, luft, etiketter, ingress (punkterna 4, 5, 6)

4.1 `.cases-chapter`: `min-height:100svh` **bort helt**,
`padding:clamp(56px,14svh,140px) var(--rail-x) clamp(32px,7svh,72px)`.
4.2 `.cases-title`: `font-size:clamp(1.625rem,3.4vw,4rem)` → **64 / 49 / 26 px**,
`--f-display`, `font-weight:700`, `letter-spacing:-.03em`. `white-space:nowrap` och
`--edge`-gradienten (§ keep) står kvar oförändrade.
4.3 `.cases-lead`: **alternativ A**, ordagrant ur `COPY-V3d-r23.md`:
`Vi har ingen husstil. Formen kommer ur verksamheten, och därför valde vi de två projekt som ligger längst ifrån varandra.`
`font-size:1.25rem`, `max-width:44ch`, `margin-top:clamp(16px,2.4svh,24px)`. STOPP om filen saknas.
4.4 Case-etiketterna (kundens ordalydelse, låst):
`#calyx-title` `.case-line` → `Florist, Stockholm`; `#horai-title` `.case-line` → `Restaurang, Asian Fusion`.
`.case-line{font-size:clamp(1.3125rem,1.7vw,2rem);max-width:24ch;margin-top:clamp(10px,1.6svh,18px)}`;
mobilöverstyrningen som ger 17 px vid 390 höjs till **21 px**. `.case-name` mobilstorlek
(`:1060`) **2,25rem → 2,75rem** (36 → 44 px). H2:ens tillgängliga namn är fortfarande
`case-name + case-line`.
4.5 Kommentaren `:918–924` får en `PLAN 067 4.`-rad.

**Target 4**

| Mätvärde | 1920x930 | 1440x900 | 390x844 |
|---|---|---|---|
| `Exempelcase` font-size | **64 px** (±2), i dag 136 | **49** (±2), i dag 129,6 | **26** (±1), i dag 40 |
| **Ordbildens bredd ÷ Calyx ordbild** | **≤ 0,90** (i dag 1,84) | **≤ 0,95** (i dag 2,45) | **≤ 0,95** (i dag 2,57) |
| Glyfhöjd ÷ Calyx glyfhöjd | ≈ 0,37 | ≈ 0,37 | tydligt < 1 |
| `Exempelcase` är inte längre sidans största ord | < processrubrikens 120 och tesens 96 | < 103,7 / 76,3 | < 56 / 35,5 |
| `Exempelcase` på en rad | ja | ja | ja |
| Luft **över** rubriken | **120–140 px** (i dag 333,3) | 110–130 (i dag 321,9) | **56–64** (i dag 324,5) |
| Rubrik → ingress | **22–24 px** | 20–22 | **16–20** |
| Ingress → casets överkant | **56–72 px** (i dag 538,7) | 52–68 | **32–40** (i dag 905,6) |
| Kvoten luft över ÷ under | **≥ 1,7** (i dag 1,00) | ≥ 1,7 | ≥ 1,7 |
| Hela introblocket inkl. luft | **340–380 px** | 320–360 | **260–290** |
| **Calyx första bildruta synlig i samma skärm som introt** | ja | ja | ja |
| `.case-line` | 32 px (±1,5) | 24,5 (±1,5) | **21** (±1) |
| `.case-line` ÷ `.cs p` | **≥ 1,5** | ≥ 1,2 | ≥ 1,4 |
| `.case-line` ÷ `.case-name` | ≤ 0,20 | ≤ 0,21 | ≤ 0,50 |
| `.case-name` Calyx / Hōrai | 171,4 / 135,0 oförändrade | 122,5 / 96,5 | **44 / 44** |
| Strängarna ordagrant | `Florist, Stockholm`, `Restaurang, Asian Fusion`, 1 förekomst vardera | | |
| Ingressen ordagrant | 20 ord, 2 meningar, `COPY-V3d-r23.md` C-A | | |
| H2:ens `accessibleName` | innehåller både namn och etikett | | |
| Horisontell scroll i `#case`, `#case-calyx`, `#case-horai` | 0 vid 320–1920 | | |
| P17/P19 ramarna | oförändrade; vid 390 ramen ≥ 50 % vh, **mät om** efter 4.4 | | |

---

### Steg 5 · Övergången ritning → case (punkt 4, andra halvan)

Bygg **efter** steg 2 (arkets rektangel) och steg 4 (kapitlets höjd). Draget är Blåkopian
**baklänges**: det blå planet krympte in i arket, arket öppnar sig ut i kapitlets papper.

5.1 Markup: `<div class="chapter-plate" aria-hidden="true"></div>` som första barn i `.cases-chapter`.
5.2 CSS, på `#case`s egen flow-akt:

```css
/* PLAN 067 5. Ritningsarket öppnar sig till kapitlets papper. Samma
   inset()-grammatik och samma --pl-*-mönster som .tes-plane, spegelvänd.
   INTE en hård kant, INTE en gradient, INTE en fjärde mekanik. */
.cases-chapter{--cx:clamp(0,calc(var(--sc-ps,0) / .34),1);position:relative;}
.chapter-plate{position:absolute;left:50%;width:100vw;transform:translateX(-50%);
  top:calc(-1 * var(--cp-up,0px));height:calc(var(--cp-up,0px) + 100%);
  pointer-events:none;z-index:0;
  background:color-mix(in oklab,var(--c-drafting),var(--bg) calc(var(--cx) * 100%));
  clip-path:inset(calc((1 - var(--cx)) * var(--cp-t,0px))
                  calc((1 - var(--cx)) * var(--cp-r,0px))
                  calc((1 - var(--cx)) * var(--cp-b,0px))
                  calc((1 - var(--cx)) * var(--cp-l,0px)));}
.cases-chapter > :not(.chapter-plate){position:relative;z-index:1;}
html:not(.js) .chapter-plate{display:none;}
```

5.3 JS, i `measureAct` direkt efter `--pl-*`: läs `.process-sheet`s rektangel i dess
**vilande** läge (steg 07, `.process-stick` släppt) och `.cases-chapter`s egen rektangel,
skriv `--cp-t/-r/-b/-l` mot plattans **egen** `getBoundingClientRect()` — aldrig mot
`window.innerWidth` (plan 066 fynd 2). Kapitlet är efter steg 4 bara ~352 px högt, så
plattan måste sträcka sig **uppåt**: `--cp-up` = avståndet upp till ritningsarkets vilande
underkant, **begränsat av samma fria yta som `--pl-h` redan bevisat är fri från levande
text** (plan 062:s egen säkerhetsmarginal). En gång per mätning.
5.4 Landningshårlinjen: `.cases-chapter::after`, 1 px `--c-line-on-paper`, bredd = plattans
klippta bredd, `top` = rubrikens överkant − 40 px, avslöjad med
`clip-path:inset(0 calc((1 - clamp(0,calc((var(--cx) - .62) / .2),1)) * 100%) 0 0)`.
**Ingen etikett, ingen siffra** (F-016).
5.5 `.cases-title`s `--edge`-bläckning flyttas till
`calc(clamp(0,calc((var(--cx) - .70) / .30),1) * 260%)`.

**Target 5**

| Mätvärde | 1920x930 | 1440x900 | 390x844 |
|---|---|---|---|
| Ingen hård kant ritbord/papper i någon bildruta | hjul 20 px ned och upp: **0 bildrutor** där två material möts i en kant med ΔL > 18 över en pixelrad | samma | samma |
| Plattans rektangel vid `--cx` 0 | = arkets vilande rektangel **±2 px** på alla fyra sidor | ±2 | ±2 |
| Plattans rektangel vid `--cx` 1 | hela viewportens bredd, fyllning = `--bg` (ΔE ≤ 1) | samma | samma |
| Landningslinjen | 1 px, 40 px (±2) ovanför rubrikens överkant, avslöjad vänster → höger | samma | samma |
| Rubriken bläckas efter landningen | första 100 %-bildrutan vid `--cx` ≥ 0,70 | ja | ja |
| Ingen rubrik halvklippt | svep + geometrisk kontroll: **0 träffar**, **körd mot en trasig variant först** (`.chapter-plate{clip-path:none;height:+900px}`) | samma | samma |
| Ingen text i eller bakom plattan | `plane21.py`-motsvarighet, båda riktningarna: 0 | 0 | 0 |
| Scrubbat, båda hållen | `motion_probe` på `#case:--sc-ps`: staircase 0, max_step ≤ 3 %; pixeldiff ned/upp ≤ 1 % | samma | samma |
| `position` på `.chapter-plate` | `absolute` i varje bildruta, `fixed` aldrig | samma | samma |
| Tom grund mellan arkets underkant och rubriken | **≤ 140 px** (i dag 357) | ≤ 130 | ≤ 110 |
| `blankBands` (`scroll_verify`) | inga nya | inga nya | inga nya |
| F-011 / F-014 | `prefers-reduced-motion` 0; ingen `transition` på något scrubbat | | |

---

### Steg 6 · Kontaktsektionen och sidfoten (punkt 8)

6.1 Markup, mellan `</section>` (`#pris`) och `</main>`:

```html
<!-- PLAN 067 6 (B11-B14). Kontakten är en EGEN sektion på papper, dit
     besökaren drivs - inte en adress i sidfoten. Riktiga <label> (de
     identifierar, F-016:s funktionstest), INGA hjälptexter, ingen
     placeholder-text, ingen backend. Sidfoten under är formulärets
     alternativa väg in och byter till samma grund. -->
<section class="contact" id="kontakt" data-sc-act="flow" aria-labelledby="kontakt-title">
  <div class="contact-veil" aria-hidden="true"></div>
  <div class="contact-inner">
    <div class="contact-head">
      <h2 id="kontakt-title">Berätta om er verksamhet.</h2>
      <p class="contact-lead">Så säger vi vad en sida kan göra för den.</p>
    </div>
    <form class="contact-form">
      <p class="field"><label for="k-namn">Namn</label>
        <input id="k-namn" name="namn" type="text" autocomplete="name" placeholder=" " required></p>
      <p class="field"><label for="k-verk">Verksamhet</label>
        <input id="k-verk" name="verksamhet" type="text" autocomplete="organization" placeholder=" "></p>
      <p class="field field--wide"><label for="k-text">Vad ni behöver</label>
        <textarea id="k-text" name="text" rows="5" placeholder=" " required></textarea></p>
      <div class="contact-actions">
        <button class="contact-send" type="submit">Skicka</button>
      </div>
      <p class="contact-status" role="status" aria-live="polite"></p>
    </form>
  </div>
</section>
```

6.2 CSS. Grund `--bg`/`--ink`. Anatomin är en **diptyk**: rubrik vänster, formulär höger
≥ 1024; en spalt under. Formuläret är ett eget grid: `namn | verksamhet` rad 1, fritexten
full bredd rad 2, knappen rad 3.

```css
.contact{position:relative;isolation:isolate;background:var(--bg);color:var(--ink);
  min-height:100svh;display:flex;align-items:center;
  padding:clamp(72px,12svh,140px) var(--rail-x) clamp(40px,6svh,80px);}
.contact-veil{position:absolute;inset:0;z-index:-1;pointer-events:none;
  background:var(--c-black);
  opacity:calc(1 - clamp(0,calc((var(--sc-ps,0) - .02) / .22),1));}      /* B12 */
.js .contact-inner{--k:clamp(0,calc((var(--sc-ps,0) - .06) / .20),1);
  opacity:var(--k);filter:blur(calc((1 - var(--k)) * 4px));}
.contact-inner:focus-within{opacity:1;filter:none;}
@media (min-width:1024px){
  .contact-inner{display:grid;grid-template-columns:minmax(0,5fr) minmax(0,7fr);
    column-gap:clamp(48px,6vw,112px);align-items:start;width:100%;}
  .contact-form{display:grid;grid-template-columns:1fr 1fr;
    column-gap:clamp(24px,2.4vw,44px);row-gap:clamp(24px,3.4svh,40px);}
  .field--wide,.contact-actions,.contact-status{grid-column:1 / -1;}
}
.field{position:relative;margin:0;}
.field label{display:block;font-family:var(--font);font-weight:300;
  font-size:clamp(1.0625rem,.85rem + .28vw,1.1875rem);line-height:1.3;
  color:color-mix(in srgb,var(--ink) 72%,var(--bg));margin-bottom:8px;}
.field input,.field textarea{-webkit-appearance:none;appearance:none;
  width:100%;background:transparent;border:0;border-radius:0;
  border-bottom:1px solid var(--c-line-on-paper);
  font-family:var(--font);font-weight:300;
  font-size:clamp(1.125rem,.95rem + .45vw,1.5rem);line-height:1.35;
  color:var(--ink);padding:10px 0 12px;min-height:52px;}
.field textarea{resize:vertical;min-height:132px;}
.field input:not(:placeholder-shown),.field textarea:not(:placeholder-shown){
  border-bottom-color:color-mix(in srgb,var(--ink) 44%,var(--bg));}
.field::after{content:"";position:absolute;left:0;right:0;bottom:0;height:2px;
  background:var(--ink);transform:scaleX(0);transform-origin:left center;
  transition:transform .2s var(--ease);}
.field:focus-within::after{transform:scaleX(1);}
.field input:focus-visible,.field textarea:focus-visible{
  outline:2px solid var(--ink);outline-offset:4px;}
.contact-send{font-family:var(--f-display);font-weight:700;
  font-size:clamp(1.0625rem,.9rem + .35vw,1.375rem);line-height:1;
  color:var(--ink);background:transparent;border:1px solid var(--ink);
  border-radius:0;min-height:52px;padding:0 clamp(24px,2.4vw,40px);
  justify-self:start;cursor:pointer;
  transition:background-color .16s var(--ease),color .16s var(--ease),transform .14s var(--ease);}
@media (hover:hover) and (pointer:fine){
  .contact-send:hover{background:var(--ink);color:var(--bg);}
}
.contact-send:active{transform:scale(.98);}
.contact-send:focus-visible{outline:2px solid var(--ink);outline-offset:4px;}
.contact-status:empty{display:none;}
.contact-status{font-family:var(--font);font-weight:300;
  font-size:clamp(1.0625rem,.85rem + .28vw,1.1875rem);line-height:1.45;
  color:var(--ink);max-width:48ch;}
html:not(.js) .contact-send{display:none;}                               /* B13 */
```

6.3 Sidfoten byter grund (B11): `.close{background:var(--bg);color:var(--ink)}`,
`.close::before` tas bort ur selektorlistan `:857` och ur `:1703`,
`.close-rule{background:var(--c-line-on-paper);align-self:stretch}`,
`.close-mailto{color:var(--ink)}` och `:active{color:var(--ink)}`. **Två inline-hex
(`#f7f5f0`, `#ffffff`) försvinner.** `#pris` får `padding-bottom:clamp(48px,8svh,96px)`.
`Eller mejla kontakt@alunix.se` sätts i sidfoten; adressen ordagrant.

6.4 JS, i det befintliga IIFE:t (B13):

```js
var kf = document.querySelector('.contact-form');
if (kf) kf.addEventListener('submit', function(e){
  e.preventDefault();
  if (!kf.reportValidity()) return;                 /* webbläsarens egen validering */
  var v = function(n){ return (kf.elements[n].value || '').trim(); };
  var body = [v('namn'), v('verksamhet'), '', v('text')].join('\n');
  location.href = 'mailto:kontakt@alunix.se'
    + '?subject=' + encodeURIComponent(SUBJECT)     /* COPY-V3d-r23.md */
    + '&body=' + encodeURIComponent(body);
  kf.querySelector('.contact-status').textContent = STATUS;  /* COPY-V3d-r23.md */
});
```

**Copy-krav (strängarna är copy-agentens, kraven är planens):** knappens etikett `Skicka`
lovar inget svar; statusraden säger att mejlet är **förberett** och skickas när besökaren
skickar det, och nämner `kontakt@alunix.se` som direkt väg om ingenting öppnades. Fälten
töms aldrig. Ingen "Tack"-vy ersätter formuläret.

**Target 6**

| Mätvärde | 1920x930 | 1440x900 | 390x844 |
|---|---|---|---|
| `#kontakt` ligger mellan `#pris` och `</main>` | ja | ja | ja |
| Grund | `--bg` vid `--sc-ps` ≥ 0,26, ΔE ≤ 1 | samma | samma |
| Skarv pris → kontakt | **0 bildrutor** med hård kant (ΔL > 18 över en pixelrad), hjul 20 px ned och upp | samma | samma |
| Kontrast i `#kontakt` vid `--sc-ps` 0,10 / 0,20 / 0,30 / 0,50 | ≥ 4,5:1 (kroppstext), ≥ 3:1 (rubrik ≥ 24 px) i varje mätpunkt | samma | samma |
| Hårlinjens kontrast | vila ≥ 1,8:1, ifylld ≥ 3:1, fokusstapel ≥ 3:1 | samma | samma |
| `<label for>` kopplad till `id` | 3/3 | 3/3 | 3/3 |
| **Hjälptexter under fält** | **0** | 0 | 0 |
| Synlig `placeholder`-text | **0** | 0 | 0 |
| Etikettstorlek | 19 px (±0,5) | 18 | 17 |
| Inmatad text ÷ etikett | ≥ 1,25 | ≥ 1,2 | ≥ 1,05 |
| Fältens / knappens `min-height` | ≥ 52 px | ≥ 52 | ≥ 52 |
| Tab-ordning | namn → verksamhet → fritext → knapp → `kontakt@alunix.se`, ingen fälla, inget fokus utanför skärmen | samma | samma |
| Fokusring synlig på varje stopp | 4/4 | 4/4 | 4/4 |
| Fokusstapeln | `transform:scaleX`, 200 ms, `--ease`; ingen `width`/`height`/`border-width` animeras | samma | samma |
| `:active` på knappen | `scale(.98)`, 140 ms | samma | samma |
| Hover bakom `@media (hover:hover) and (pointer:fine)` | ja | ja | ja |
| Submit utan JS | knappen renderas inte; adressen i sidfoten fungerar | samma | samma |
| Submit med JS | `location.href` börjar med `mailto:kontakt@alunix.se?`; fältens värden **oförändrade**; statusraden får text | samma | samma |
| Nätverksanrop vid submit | **0** | 0 | 0 |
| Sidfoten | grund `--bg`, `.close-mailto` `--ink`, kontrast ≥ 7:1, ingen scrim, `.close-rule` full bredd | samma | samma |
| Inline-hex i filen | **≤ R22 − 2** | | |
| Horisontell scroll | 0 vid 320–1920 | | |
| `a11y_scan` + `reflow` vid 390/1440 | 0 violations | | |
| Sektionens höjd | ≤ 110 svh | ≤ 110 svh | ≤ 140 svh |

---

### Steg 7 · Övergången tes → ritning (punkt 3)

Byggs **sist**, efter steg 2 (arkets rektangel), steg 4 (kapitlets höjd) och steg 5.
Astras dom är `fix`. Metaforen är rätt (§ keep: "byt inte metafor"), arket är tomt och
draget är långt. **Ett ritningsark är aldrig tomt — det har en stämpelruta.**

Grepp lånat ur våra egna systemreferenser, inte ur en ny konstnärlig riktning:
`sites/hyperborea.html` låter kapitelrubriken och **första innehållsraden dela bildruta**,
~140 px isär, med hårlinjer där innehåll börjar; `sites/horai.html` och insign ger aldrig en
hel skärm åt en övergång; highway namnger destinationen **först** och låter tråden börja
~100 px under rubriken, i samma bildruta.

7.1 **Markup.** `#process-title` och `.process-locked` flyttas in i en ny stämpelruta, före
`.seam` i källordningen så att linjerna ritas över papperet men under texten:

```html
<!-- PLAN 067 C1/C2 (Astra r23 material_fix 1). Ett ritningsark är aldrig tomt:
     det har en stämpelruta. Kapitelrubriken och den låsta raden bor INNE i den
     landade rektangelns nedre vänstra kvadrant, med landningslinjen som
     överlinje. INTE en tom hårlinjelåda ovanför en rubrik (R22: ankomsten
     läste som ett försvinnande), INTE en etikett på rutan (F-016).
     Rubriken ligger UTANFÖR .tes-plane: planet är aria-hidden. -->
<div class="chapter-stamp">
  <h2 id="process-title" class="process-title">Från samtal till lanserad sida.</h2>
  <p class="process-locked">Webbdesign, design och system. Allt på ett ställe.</p>
</div>
```

7.2 **CSS**, ersätter `.process-chapter{min-height}` (`:1134`), `--tx`-raden (`:1136`),
`.tes-plane`s `height`/`background` (`:1178–1183`), `.seam-dn`/`.seam [data-l]`s `left`:

```css
/* PLAN 067 C3/C4. Kapitlets klocka räknas av measureAct: draget är
   260-300 px vid 1920 och 220-260 vid 390, inte 594/539. R14:s
   120svh-dröjfönster är rivet - Astra r23 mätte 390 px död svart mellan
   rubriken och steg 01, och våra tre referenser låter rubrik och första
   innehåll dela bildruta. INTE ett hårdkodat fönster. */
.process-chapter{min-height:clamp(560px,86svh,920px);
  --tx:clamp(0,calc((var(--sc-ps,0) - var(--tx-a,.07)) / var(--tx-b,.29)),1);}

/* PLAN 067 C1. Rektangeln = arkets bredd + ritytan + stämpelrutan. */
.tes-plane{height:calc(var(--pl-h,0px) + var(--dn,0px) + var(--stamp-h,0px));
  background:color-mix(in oklab,var(--c-accent),var(--c-drafting)
    calc(clamp(0,calc((var(--tx) - .75) / .25),1) * 100%));}   /* C8 */

/* PLAN 067 C6. Konturen ÄR fyllningens kant genom hela draget: linjernas x
   interpolerar på samma --tx som klippet. INTE fyra streck 231 px innanför
   en fylld rektangel. */
.seam [data-l="1"]{left:calc(var(--sx1) + (var(--x1) - var(--sx1)) * var(--tx));}
.seam [data-l="2"]{left:calc(var(--sx2) + (var(--x2) - var(--sx2)) * var(--tx));}
.seam [data-l="3"]{left:calc(var(--sx3) + (var(--x3) - var(--sx3)) * var(--tx));}
.seam [data-l="4"]{left:calc(var(--sx4) + (var(--x4) - var(--sx4)) * var(--tx));}
.seam-dn{height:var(--dn,0px);}      /* C7: slutar i stämpelrutans överlinje */

/* PLAN 067 C1/C2. Stämpelrutan: nedre vänstra kvadranten, landningslinjen
   som överlinje, rektangelns underkant som botten. */
.chapter-stamp{position:absolute;left:var(--x1);top:calc(var(--dn) + 1px);
  width:min(82%,calc(var(--x4) - var(--x1)));
  padding:clamp(18px,2.6svh,32px) clamp(20px,2vw,44px) clamp(16px,2.2svh,28px);}
.process-title{padding:0;max-width:16ch;}
.process-locked{padding-inline:0;margin-top:clamp(14px,2svh,24px);}
@media (max-width:767px){ .chapter-stamp{width:calc(var(--x4) - var(--x1));} }

/* PLAN 067 C9 (Astra r23 material_fix 4). Prickarna var det enda märket i
   ett tomt blått fält genom hela övergången. Släcks när tesens sista
   mening lämnar bildrutan. */
.js .thesis-ticks{opacity:clamp(0,calc((.96 - var(--sc-ps,0)) / .04),1);}
```

`.js .process-title`s inbläckningsfönster (`:1240–1243`) flyttas till `0,38 → 0,70` så att
rubriken är **läsbar vid `tx` ≈ 0,45** medan arket fortfarande konvergerar. `--p-edge`
(0,6 → 0,9) rörs inte, § keep.

7.3 **JS**, i `measureAct`, i samma block som `--x1..--x4`/`--dn`/`--pl-*`:
- `--stamp-h` = `.chapter-stamp.scrollHeight`, skrivs **före** `--dn` läses igen (samma ordningsskäl som `--band-h`);
- `--dn-draw = Math.min((x4 − x1) * aspect, 0.46 * vh)`; `--dn = dnDraw + kapitlets övre luft`, chapter-relativt;
- `--sx1..--sx4` ur `.tes-plane`s **egen** `getBoundingClientRect()` (aldrig `window.innerWidth`): `sx1 = 0`, `sx4 = planeBox.width − 1`, `sx2 = planeBox.width * 195.6/880`, `sx3 = planeBox.width * 469.3/880`, alla minus `planeBox.left − C.left`;
- `--tx-a` / `--tx-b` enligt C3;
- `--pl-t` räknas mot rektangelns nya höjd (`dnDraw + stampH`), `--pl-b` fortfarande 0.

En gång per mätning, som `--band-h` och `--life`, **aldrig per bildruta**.

7.4 **`?preview=`**: `tes-till-ritning-0` … `-4` oförändrade i kod; målpunkterna följer
automatiskt med `--tx-a`/`--tx-b`. `chapter` visar nu kapitelskärmen **med** steg 01 i
underkanten — det är avsikten, inte ett fel.

7.5 **Kommentarer**: `.process-chapter` (`:1110–1134`), `.tes-plane` (`:1160–1177`), `.seam`
(`:1136–1159`) och markupens block får var sin `PLAN 067 C-N.`-rad med INTE-rad. R14:s
kommentar rättas uttryckligen: dröjfönstret är rivet, av vilken mätning, och av vem.

**Target 7**

| # | Synligt mål | 1920x930 | 1440x900 | 390x844 |
|---|---|---|---|---|
| **1** | Rektangeln är aldrig tom | `tes-till-ritning-3`, `-4`, `chapter` och hjulsvep 20 px: **0 bildrutor** där arkets kontur är synlig och antalet `Range`-textlöpor **inuti** rektangeln är 0. A14-läget (y ≈ 7440) visar rubrik + låst rad | samma | samma; **inga två staplade tomma lådor** |
| **2** | Textytan faller aldrig under golvet | `sweep23.py`, 40 px-hjul: synlig textyta **≥ 18 % av viewporten i varje bildruta** (i dag 8,2 % vid y6800) | ≥ 18 % | **aldrig noll textlöpor**, ≥ 12 % i varje bildruta (i dag fyra bildrutor på noll) |
| **3** | Draget är halverat | `tx` 0 → 1 över **260–300 px** (i dag 594) | 260–300 px | **220–260 px** (i dag 539) |
| **4** | Rubriken kommer före kön | hela rubrikens första rad inne i viewporten vid **`tx` ≤ 0,45**; 100 % bläck vid `tx` ≥ 0,70 | samma | samma |
| **5** | Överlämningen syns (C5) | i bildrutan där `#process-title` når 100 % bläck finns **≥ 1 glyflöpa från steg 01** i vänsterspalten; stämpelrutans och stegslottens rektanglar **överlappar aldrig i y** | samma | steg 01:s slot ≥ 1 glyflöpa i samma bildruta (under arket) |
| **6** | Död grund mellan rubrik och steg 01 | **≤ 120 px** (i dag 390) | ≤ 110 px | ≤ 90 px |
| **7** | Konturen är fyllningens kant | i varje tx-läge (0,2 / 0,4 / 0,6 / 0,8 / 1,0): linje 1 och 4 **≤ 2 px** från den klippta rektangelns kanter (i dag 231 / 232 px) | ≤ 2 px | ≤ 2 px |
| **8** | Strecken slutar i överlinjen | de fyra lodrätas underkant = `.seam-h`s y **±1 px**; ingen linje som tar slut i tom yta (i dag 150 px för tidigt) | ±1 px | ±1 px |
| **9** | Landningslinjen har ett jobb | `.seam-h`s y = stämpelrutans överkant ±1 px, bredd = `--x4 − --x1 + 2` (R22 fix 1, får ej regressera) | samma | samma |
| **10** | Färgen gör ett hopp | ΔE mellan `tx` 0,70 och 1,0 **≥ 12**; ΔE mellan 0,10 och 0,70 ≤ 4 | samma | samma |
| **11** | Prickarna släcks | `.thesis-ticks` `opacity` = 0 i varje bildruta där någon del av arkets kontur är synlig | samma | samma |
| **12** | Ingen rubrik halvklippt | `sweep.py` (057 B2) + geometrisk kontroll, hjul 20 px: **0 träffar**, **körd mot en trasig variant först** (`.chapter-stamp{top:0}` ska ge träffar) | 0 | 0 |
| **13** | Ingen text i eller bakom planet | Astras `plane21.py` oförändrad, båda riktningarna: `hits` 0, `fixed_seen` false, `edge_max` 1 | 0 / false / 1 | 0 / false / 1; `two_sheets_frames` ≤ 16 |
| **14** | Scrubbat, båda hållen | `motion_probe` på `.process-chapter:--sc-ps`: staircase 0, max_step ≤ 3 %, frame p95 ≤ 20 ms vid cpu 1; pixeldiff ned/upp ≤ 1 % | samma | samma |
| **15** | Klockan räknas, inte gissas | `--tx-a` och `--tx-b` finns som inline custom properties på `.process-chapter`; inget hårdkodat `.07`/`.29` kvar i filen | samma | samma |
| **16** | Låst copy och F-016 | `Webbdesign, design och system. Allt på ett ställe.` ordagrant, 1 förekomst; **inga etiketter, siffror eller bildtexter** på rektangeln, linjerna eller stämpelrutan | samma | samma |
| **17** | F-011 / F-014 / gate 48 | `prefers-reduced-motion` 0; allt scrubbat läser `--sc-ps`/`--tx`, ingen `transition`; inga nya inline-hex; accenten exakt 2 förekomster | samma | samma |
| **18** | P06 håller | `#process-title` ≥ 100 px vid 1440 (mät: 103,68), ≥ 56 px vid 390; rubriken bryts aldrig mitt i ett ord | samma | samma |
| **19** | Kapitlets höjd | 780–860 px (i dag 1116) | 740–820 (i dag 1080) | 620–720 (i dag 1013) |

---

### Steg 8 · Helheten (punkt 9)

| Ändring | Följd för rytmen | Åtgärd |
|---|---|---|
| Underraden bort | Folden blir ett displayelement, ett objekt och ett foto. En röst mindre i öppningen. | Ingen. Det är förbättringen. |
| Processakten två spalter | Aktens sju skärmar går från "band över tomt ark" till komponerade skärmar. Med 35–44-ordstexter bär vänsterspalten 0,55–0,72 av viewporthöjden. | `li{min-height}` som lever; taket ≤ +10 % på dokumentet. |
| Case-kapitlet 100svh → ~352 px | Sidan förlorar en tyst zon. | Den stora tysta zonen är fortfarande processens kapitelskärm och `.case-gap` (18svh svart). Case-kapitlet blir ett **andetag** — precis vad kunden beställde. |
| Skarven ritning → case | En hård kant mindre. | – |
| Övergången tes → ritning | Ankomsten läses som en ankomst, inte som ett försvinnande. Kapitelskärmen och steg 01 delar bildruta. | – |
| Serifen bort | Fyra röster blir tre: Geist 700, Public Sans 300, Geist Mono. Rollerna korsar aldrig. | – |
| Kontaktsektionen på papper | Sidans **sista materialväxling** och dess ljusaste yta hamnar där besökaren ska handla. Materialrytmen: foto → blått → ritbord → **papper** → svart → svart → svart → foto → **papper**. | Sidfoten följer med till papperet, så slutet är **en** yta. |
| Toppen | Sidans topp är fortfarande ramarna. Kontakten är sidans **handling**, inte dess topp. | Knappen är en 1 px-kontur. Ingen andra accentförekomst. |

**Target 8**

| Mätvärde | 1920x930 | 1440x900 | 390x844 |
|---|---|---|---|
| Helsidessvep, en bild per skärm (aldrig kontaktark) | ingen skiva där två material möts i en hård kant | samma | samma |
| Tomt band > 60 % vh i helsidesfångsten | **0** | 0 | 0 |
| Accenten `#1e5e9c` | exakt **2** förekomster | | |
| Inline-hex | ≤ R22 − 2 | | |
| Tankstreck i synlig text | 0 | | |
| Radie ≠ 0 / skuggor | 0 / 0 | | |
| Mono-etiketter | 4 (kortbaksidan), oförändrat | | |
| `microtext_scan.py` | **inga nya fynd** mot R22 | | |
| Levande iframes | exakt 2 | | |
| `prefers-reduced-motion` | 0 träffar | | |
| Dokumenthöjd | ≤ +10 % mot R22 | ≤ +10 % | ≤ +10 % |

---

## Device-tabell (steg 2)

| Bredd | `clientWidth` | Textspalt | Ränna | Ark (bredd / % vw / höjd) | `--band-h` mål | Form |
|---|---|---|---|---|---|---|
| **1920x930** | 1910 | 439 | 61 | **1314 / 68,8 % / 739** | ≤ 640 | två spalter |
| **1600x900** | 1590 | 366 | 51 | **1077 / 67,7 % / 606** | ≤ 650 | två spalter |
| **1440x900** | 1430 | 329 | 46 | **970 / 67,8 % / 545** | ≤ 660 | två spalter |
| **1280x800** | 1270 | 292 | 41 | **861 / 67,8 % / 484** | ≤ 620 | två spalter |
| **1024x768** | 1014 | 288 (golv 18rem) | 32 | **633 / 62,4 % / 356** | ≤ 560 | två spalter |
| **768x1024** | 758 | – | – | oförändrat R22 | oförändrat | **bandform, orörd** |
| **390x844** | 380 | – | – | 348 / 89,2 % / 217,5 | ≤ 420 | ark över sticky slot |
| **320x568** | 310 | – | – | oförändrat | ≤ 380 | ark över sticky slot |

`measureAct` räknar arkets faktiska rektangel; **byggaren skriver aldrig in dem.**

## Repo conventions

- **Selektorer att Grep-verifiera före bygget** (radnumren är R22:s läge, lita på selektorn):
  `.hero-sub`, `.hero-stage`, `--h1-hrate`, `.process-grid`, `.process-stick`,
  `.process-steps`, `.process-steps li`, `.step-band`, `.step-band > .ledger-num`,
  `.process-step-title`, `.process-p`, `#process .process-p`, `.process-sheet`,
  `#process{--band-h`, `--slit-p`, `@media (min-width:768px)`, `.process-chapter`,
  `.process-title`, `.process-locked`, `.tes-plane`, `.seam`, `.seam-dn`, `.seam-h`,
  `.thesis-ticks`, `.cases-chapter`, `.cases-title`, `.cases-lead`, `.case-title`,
  `.case-name`, `.case-line`, `.price .statement`, `.price-ingress`, `.price-ledger`,
  `.price-row`, `.price-row .label`, `.price-row .value`, `.value--text`, `.close`,
  `.close-rule`, `.close-mailto`, `--f-serif`, `Young+Serif`, `function measureAct`,
  `function aimOnce`, `function aimFlow`, `__scFreezeMotion`.
- Motorn (`scroll/*.js`, `scrollcraft.css`) och `sites/*` orörda. Motorns `.sc-*`-klasser
  stylas aldrig.
- F-011: ingen `prefers-reduced-motion`, ingen andra statisk gren. F-014: allt som scrubbas
  läser `--sc-ps`, ingen `transition` på något scrubbat. Fokus- och hover-övergångar är
  **inte** scrubbade och får sina 140–200 ms.
- Gate 48: varje färg via token. Inga nya färgtokens behövs; `--f-serif` **tas bort**.
- Gate 75: inga tankstreck. Gate 99 / F-016: inga bildtexter, inga hjälptexter, inga
  dekorativa etiketter. Radie 0, inga skuggor, accenten två förekomster.
- Varje nytt block börjar med `PLAN 067 N.` (eller `PLAN 067 C-N.`) och en INTE-rad.

## Boundaries (STOPPA och skriv i NOTES)

- `COPY-V3d-r23.md` saknas när bygget når 2.3, 4.3 eller 6.4.
- `--band-h` > 640 px vid 1920 / 660 vid 1440 efter steg 2:s levrar, eller aktens höjd > +15 %.
- Arket < 1300 px vid 1920 eller < 950 px vid 1440 efter steg 2.
- Glyfspringekontrollen vid 390 hittar en springa efter en fixrunda: fall tillbaka till
  R22:s statiska mobillista, skriv det i NOTES och lyft till lead. Backa **inte**
  tvåspaltsakten för det.
- `.process-stick` släpper före band 07 efter 2.4.
- Någon `?preview=process-0N` landar inte på sitt `--eN`.
- Rubriktäckningssvepet eller den geometriska kontrollen hittar en träff i steg 5 eller 7.
- Kontrasten i `#kontakt` går under 4,5:1 i någon mätpunkt: justera `--k`-fönstret, aldrig
  veilens existens; håller det inte, ta bort veilen och lämna en ren papperssektion.
- `--stamp-h` > 0,50 × rektangelns höjd vid 1440 efter att `.chapter-stamp{width}` höjts
  till 86 %: rubriken ryms inte inne i arket utan att bryta P06:s ≥ 100 px. Stoppa; lead
  väljer mellan att sänka P06:s golv och att lägga stämpelrutan **under** rektangeln med
  samma x-span (Astras kontroll "textlöpor inuti rektangeln" måste då skrivas om).
- Målet 260–300 px och målet "rubriken läsbar vid tx ≤ 0,45" går inte att nå samtidigt utan
  att inbläckningen blir ett hopp (ΔL > 30 mellan två 20 px-bildrutor).
- `motion_probe` staircase ≠ 0 efter att `--tx-a`/`--tx-b` blivit räknade tal.
- `plane21.py` ger `hits` > 0 eller `fixed_seen` true: **backa aldrig R21:s borttagning.**

## Verification

**A. Synligt, det som avgör.** `PARITET.md` P01, P04, P07–P13, P14, P15, P17, P19, P21, P24,
P25: par-bilder vid 1440 och 390 i `shots/r23/par/`, lästa som bilder. P04 skjuts som fem
bilder (`tes-till-ritning-0` … `-4`) plus `chapter`; P07, P09, P13, P14, P21, P24, P25 skjuts
dessutom vid **1920x930**. Lead läser själv P04 och P07 vid 1920 och 390, P14 vid 1920, och
P24 vid alla tre, innan rundan räknas klar. Varje bild tagen i Chromium **utan**
`--hide-scrollbars`, målläget nått med `mouse.wheel`, en skärmbild per sida.

**B. Mätt.**
1. Hjulsekvens 20 px **båda riktningarna** vid 1920/1440/768/390 genom (a) passagen tes → ritning, (b) hela processakten, (c) skarven ritning → case, (d) skarven pris → kontakt. En bild per 5:e steg och vid varje fönstergräns.
2. `sweep23.py` (Astras, oförändrad) genom passagen tes → ritning: textyta ≥ 18 % i varje bildruta vid 1920/1440, aldrig noll textlöpor vid 390.
3. `motion_probe.py` på `.process-chapter:--sc-ps`, `#case:--sc-ps` och `#kontakt:--sc-ps`: staircase 0, max_step ≤ 3 %, frame p95 ≤ 20 ms vid cpu 1. Samma `scrollY` ned/upp → pixeldiff ≤ 1 %.
4. Rubriktäckning: `shots/r12/scripts/sweep.py` hela sidan, 20 px-steg, fyra bredder → 0. **Kör först mot injicerade trasiga varianter** (`.chapter-stamp{top:0}` och `.chapter-plate{clip-path:none;height:+900px}`), som ska ge träffar.
5. Astras `plane21.py`, oförändrad, som regressionsvakt: 0 träffar, `fixed_seen:false`, `edge_max:1` vid alla fyra bredder.
6. Steg 2:s hela Target-tabell per bredd. Plus glyfspringekontroll (a) och (b) vid 1920, 1440, 768 **och 390**.
7. `ink23.py` för ordbildsmåtten i steg 4; `anchors23.py` för luft och storlekar i case-kapitlet och priset.
8. `tab_walk.py`, `a11y_scan.py`, `reflow.py` vid 390 och 1440.
9. Submit-provet: fyll i tre fält, klicka, verifiera `mailto:`-URL:en, att fälten är oförändrade, att statusraden fick text och att **0** nätverksanrop gick ut. Samma prov med JS av.
10. Pixeldiff mot R22 för `?preview=front`, `thesis-01`…`-04`, `case-calyx-01`, `case-horai-01`, `case-seam`, och **768x1024** `process-01/-03/-07`.
11. Låst copy **11/11**. `microtext_scan.py` inga nya fynd. `detect.mjs --json`. Grep: `prefers-reduced-motion` 0, `Young Serif` 0, `fonts.g` 0, tankstreck 0, inline-hex ≤ R22 − 2.
12. `perf_probe`: LCP och CLS efter borttagen Google Fonts-förfrågan — förväntad **förbättring**, mät och skriv talet.

**C. Grinden.** `scroll_verify` vid 1440 och 390 (inga nya `blankBands`); noll horisontell
scroll vid 320, 375, 390, 414, 768, 1024, 1280, 1440, 1920; 0 JS-fel vid laddning och genom
hela scrollen; exakt två iframes.

**Done when:** varje Target-rad har ett uppmätt värde som når målet, svepen är 0 vid fyra
bredder, varje omskriven PARITET-rad kan läsas "håller nivån" i sin par-bild, och grinden är
ren eller varje avvikelse namngiven.

## Frågor till Anton

| # | Fråga | Svar / antagande |
|---|---|---|
| **Q1** | Arket går 63,4 → 68,8 % vw vid 1920 men **81,1 → 67,8 %** vid 1440. En tvåspaltig akt kan inte ge 76 % vw vid 1440 — det är aritmetik. | **Accepterat** (lead 2026-09-20). P07–P13 skrivs om till 67 % vw som golv. 1440-regressionen rapporteras till Anton i klartext. |
| **Q2** | Young Serif tas bort helt och `Exempelcase` sätts i Geist 700. Stänger posten "fyra typsnittsfiler mot budget tre" och tar bort sidans enda tredjepartsförfrågan. | **Ja.** |
| **Q3** | "Samma som brödtexten med fetstil endast på rubriken": Public Sans finns i en vikt (300), så fet Public Sans blir syntetisk. Rubriken sätts i Geist 700. | **Ja.** Syntetisk fetstil är en renderingsdefekt, inte en typografi. |
| **Q4** | Sidfoten flyttar med kontaktsektionen till gräddgrunden, så `kontakt@alunix.se` står direkt under knappen. Antalet `mailto` står kvar på två. | **Ja.** |
| **Q5** | Case-kapitlets ingress: utfall A eller B. | **Utfall A**, ordagrant ur `COPY-V3d-r23.md` C-A. Den upprepar inte etiketterna. |
| **Q6** | Vid 390 höjs `.case-name` från 36 till 44 px. Det äter 8 px av textspalten under ramen (P17 390). | **Ja**, mäts mot P17:s ≥ 50 % vh. |
| **Q7** | F-017 säger att `Pris vid förfrågan` står i **halva siffran**. Astra mäter halva siffran (24 px) som flytande och sätter **27 px**: full siffra konkurrerar, halva flyter. F-017:s avsikt (frasen är tydligt inte ett tal) håller vid 27 px. | 27 px, baslinjekravet orört. **Öppen.** |

ship

## persistence
Avgränsad bekräftelserunda: bara r21:s två material_fixes plus de § keep-mätningar som
de två ändringarna faktiskt kan ha påverkat. Egna bilder och skript i
`shots/astra-r22/`. Chromium med `ignore_default_args=['--hide-scrollbars']`, en
skärmbild per sida, aldrig kontaktark.

**Fix 1, pixelprovet — min första detektor kastades.** `column22.py` letade efter en
run av pixlar ljusare än fönstrets botten. Den slog ihop konturen med fyllningens egen
ljustrappa (grunden 17,25,34 → planets fyllning 26,50,74) och rapporterade 8–11 px
breda "kolumner" vid t3, alltså ett falskt negativt. Ersatt av `ridge22.py`, som kräver
en RIDGE: ljusare än pixeln 3 px åt BÅDA håll, ≥20 luminansenheter. 5 rader per kant,
3 bredder, t3 och t4, tre lägen = 18 sidor och 18 bilder. **Två medvetet trasiga
kontroller, inte en:**
- `nocontour` (`.tes-plane::after{display:none}`) — kolumnen måste FÖRSVINNA.
- `noseam` (`.seam{display:none}`) — kolumnen måste FINNAS KVAR. Den behövs därför att
  vid t4 ligger arkets egna konstruktionslinjer ovanpå planets kant; utan den kan
  t4-kolumnen inte tillskrivas konturen alls.

| Läge | real | nocontour (kontroll) | noseam (kontroll) |
|---|---|---|---|
| 1920 t3 | V och H 5/5 rader, 2 px, Δ −0,1 | **ingen ridge alls**, 0/5 | 5/5, Δ −0,1 |
| 1440 t3 | 5/5, 2 px, Δ 0,0 / −0,3 | **ingen ridge alls**, 0/5 | 5/5, Δ 0,0 / −0,3 |
| 390 t3 | två 2 px-linjer 5 px isär | bara seam-linjen kvar | 5/5, 2 px, Δ +0,2 / +0,5 |
| 1920 t4 | 5/5, Δ 0 (V) / 1 (H) | seam kvar (sammanfaller) | 5/5, 2 px, Δ 0 / 0 |
| 1440 t4 | 5/5, Δ 0 / 1 | seam kvar | 5/5, Δ 0 / 0 |
| 390 t4 | 5/5, Δ 0 / 1 | seam kvar | 5/5, Δ 0 / 0 |

Rå pixelrad, 1920 t3, y 409, kring den klippta vänsterkanten 258,1: `real` ger
256–257 (17,25,34) → **258 (123,136,148) och 259 (140,152,164)** → 260 (26,50,74);
`nocontour` går rakt från (17,25,34) till (26,50,74), ingen linje någonstans i
fönstret. Vid 390 t3 (y 524, klippt kant 10,8) ligger konturen på x 11–12
(141,153,165) och arkets egen kantlinje på x 16–17 (158,160,161): två 2 px-linjer
5,2 px isär, och i `nocontour` finns bara den senare kvar. Konturen är alltså ritad,
2 px bred, på rätt x, vid alla tre bredderna — och den försvinner när jag tar bort
just den regeln. Provet mäter det jag påstår att det mäter.

**Fix 2, `contour2.py` oförändrad** (md5 `2a2e29d0…`, bitidentisk med r21:s fil), vid
t4: `sideGapLeft` **0** och `sideGapRight` **−1** vid 1920, 1440 och 390 — kravet
≤1 px håller vid alla tre bredderna (r21 mätte +5 / −6). `keep22.py` läser de skrivna
talen: vid 1920 skriver `measureAct` `--pl-l` 351,0 och `--pl-r` 352,0 mot planets
egen box −5…1915, vilket ger klippt vänsterkant 346,0 = `--x1` och högerkant 1563,0
= `--x4`, exakt; 136/137 vid 1440 och 21/22 vid 390 ger samma exakthet.

**Regressionsvakt, `plane21.py` oförändrad** (md5 `41872dc8…`, bitidentisk med r21:s
fil), 20 px-hjul i båda riktningarna genom tes → ritning → steg 01:

| Bredd | Bildrutor | hits | fixed_seen | positions | two_sheets_frames | edge_max |
|---|---|---|---|---|---|---|
| 1920 | 500 | 0 | false | ['absolute'] | 0 | 1 |
| 1440 | 486 | 0 | false | ['absolute'] | 0 | 1 |
| 390 | 454 | 0 | false | ['absolute'] | 16 | 1 |
| 768 | 554 | 0 | false | ['absolute'] | 0 | 1 |

Identiskt med r21 på varje rad, inklusive bildrutantalet. 390:s 16 bildrutor ligger i
samma svep (scrollY 6780–6880) och i motsatta kanter — planets rest 44–144 px i
överkanten, arket 728–828 px ned, ~684 px isär — alltså samma bild r21 dömde som
accepterad, inte en ny stapling. `edge_max` 1 vid alla fyra bredderna: konturen når
full opacitet i svepet, så nollan är inte ett blint prov.

**§ keep, de mätningar de två ändringarna kan ha påverkat** (`keep22.py`):
- **Landningslinjen (r18 fix 1)** delar `--x1`/`--x4` med fix 2:s geometri. `.seam-h`
  mäter 1219 / 1169 / 349 × 2 px vid 1920 / 1440 / 390, och invarianten
  `--x4 − --x1 + 2` stämmer exakt i alla tre (1563−346+2, 1298−131+2, 363−16+2).
  (1920 mätte 1215,4 i r21; talet följer arkets uppmätta bredd i det exakta
  scrollägret, formeln är densamma.)
- **Horisontell scroll:** `documentElement.scrollWidth − clientWidth` = **0** vid 320,
  375, 390, 414, 768, 1024, 1280, 1440 och 1920. Det nya `::after` ligger med
  `inset ≥ 0` inuti ett element som redan fanns och kan inte skapa ny overflow.
- **Konturens egen linjevikt och kontrast** (r18 fix 2:s 3:1-krav gäller nu en NY
  linje): 2 px överallt, och på renderade pixlar **3,62:1** mot fyllningen och
  **4,88:1** mot grunden vid t3 (1920), **17,71:1** vid t4 (ren vit mot ritbordets
  ton). Över kravet i varje läge där den syns.
- **Kostnaden per bildruta.** Det nya `::after` interpolerar `inset` med `--tx`,
  alltså en layout av pseudoelementet varje bildruta genom hela akten. A/B med samma
  svep, med och utan regeln (`cost22.py`): **0 långa uppgifter (>50 ms) i båda lägena**
  vid både 1920 och 390; rAF-deltan p50/p90/p99 identiska (16,7 / 16,8 / 33,4 vid
  1920), bildrutor >25 ms 54 mot 46 vid 1920 och 0 mot 2 vid 390 — brus, och med
  motsatt tecken vid de två bredderna. Ingen mätbar kostnad.
- **Medvetet bortvalda:** stegbanden, ramarna (`edges21`), prisenheten, delade ord,
  case-skarven, Hōrai-monteringen, `microtext_scan`. Båda `Edit`-anropen ligger på
  `.tes-plane` respektive `--pl-l`/`--pl-r`; `grep` visar att `var(--pl-*)` bara läses
  av de två `.tes-plane`-reglerna (1181, 1183–1184, 1199–1200) och `--p-edge` bara av
  1197 och 1201. Inget utanför `.process-chapter` kan nå dem, så de mätningarna kan
  inte ha rört sig, och att köra om dem hade varit tid utan information.

**Codex** (`gpt-6-astra`, low, headless, read-only, en körning, `prompt.txt` /
`codex-out.txt`),
avgränsad till de två ändrade ställena: **0 fynd.** Den bekräftade att `clip-path` och
`::after` delar samma interpolerade rektangel och att föräldern saknar border/padding
som skulle förskjuta referensboxarna, att `clamp(0,…,1)` är giltig där den
substitueras in i `calc(… * 100%)`, att pseudoelementet varken skapar stackningskontext
eller träffyta, att `getBoundingClientRect()`-läsningen ligger efter föregående
layoutskrivningar och därför inte kan ge en inaktuell box, och att `querySelector` inte
ligger på scroll-/rAF-vägen (`measureAct` körs vid init, `resize`, `load` och en
relayout — verifierat i källan, rad 2608–2610 och 3062). Den lämnade **en** reservation:
under 4 px kvarvarande bredd kan två 2 px-ramar inte längre sammanfalla. Den **släpps** —
den smalaste klippta rektangel jag har mätt är 347 px (390 vid t4), och `--pl-l`/`--pl-r`
är `Math.max(0, …)`-klampade mot arkets egen bredd. Codex noterade också att sidans enda
em-streck sitter i en CSS-kommentar (rad 430); verifierat, ingen synlig text berörs.
**1 reservation kom tillbaka, 0 överlevde, 0 fynd att vidarebefordra.**

**Hygien, inte ett sidfynd:** bygget skrev över två av r21:s bevisfiler i min egen
katalog (`shots/astra-r21/contour2.json` 01:14 och `plane21-1920.json` 01:17, mot
rapporten 01:03). r21:s baslinje går därför inte längre att läsa ur filerna, bara ur
rapporttexten. Nästa runda: kör om granskarskript i en egen katalog, skriv aldrig i
en tidigare rundas.

## fidelity
**Fix 1 — konturen sluter sig. Klar.** `index.html:1197–1201`: `--p-edge` och
`.tes-plane::after` med `inset` byggd på exakt samma `--tx`- och `--pl-*`-tal som
`clip-path` på rad 1183–1184, och `border:2px solid` i stället för `box-shadow:inset`.
Konturen sitter nu på en box som krymper med planet i stället för på elementets fasta
100vw-box. Mätt: 2 px ljus kolumn inom ±1 px av den klippta vänster- och högerkanten vid
t3 och t4, vid 1920, 1440 och 390 (≤0,5 px överallt utom högerkanten vid t4, där konturen
och arkets egen linje går ihop till ett 3 px-band, Δ 1) — och ingen kolumn alls i
kontrollen. Planet
läses som en sluten rektangel, inte som två vågräta streck.

**Fix 2 — slutrektangeln landar rätt. Klar.** `index.html:2555–2558` läser planets egen
`getBoundingClientRect()` och räknar `--pl-l`/`--pl-r` mot DEN boxens kanter.
`sideGapLeft` 0 och `sideGapRight` −1 vid alla tre bredderna, mot r21:s +5 / −6. Det är
vad fix 1 gjorde nödvändigt: nu när konturen syns på sidorna hade felet blivit en dubbel
kant vid landningen, och den finns inte.

**Om t2.** Uppdraget flyttade målet från r21:s "t2 och t3" till "t3 och t4", och det är
rätt flytt: `--p-edge` är `clamp(0,(tx − 0,6)/0,3,1)` och t2 ligger på tx 0,50, alltså
opacitet exakt 0. Uppmätt: t3 tx 0,750 → edge 0,50, t4 tx 1,000 → edge 1,00.
Toningsfönstret 0,6→0,9 är oförändrat och tillhör § keep:s klocka; frånvaron vid t2 är
inte en följd av någon av de två ändringarna.

**Akten, mekaniskt:** `--tx` kommer fortfarande ur `--sc-ps` (den utjämnade), linjernas
x ur arkets egna stationer, de tre klippfönstren för `.seam-up`/`.seam-dn`/`.seam-h` är
orörda, rubrikens bläckning (`--edge`, rad 1240–1243) orörd. R22 lade till fem rader CSS
och fyra rader JS, inga nya lyssnare, ingen ny observer, ingen ny rAF-loop, ingen
`will-change`.

**Min dom om övergången: den står fast som fin nog, och ett snäpp bättre än i r21.**
Ändringen är finish, inte styrka, precis som r21 skrev — men det är den finish som gör
plan 062:s egen formulering sann. Vid t3 (1920) är den klippta rektangeln nu en sluten
figur med 2 px kontur på alla fyra sidor, 88 px utanför arkets egna kantlinjer, och de
två rektanglarna dras mot varandra tills de sammanfaller vid landningen. Det läses som
ett ark som STELNAR i rätt storlek. Förut såg man en fylld yta vars sidor låg 84–178 px
utanför de två vita linjer som skulle vara arkets kanter, alltså ingen figur alls. Inget
i finishen drar åt andra hållet: ingen ny linje som konkurrerar med arket, ingen ny kant
vid landningen, ingen kostnad i rörelsen.

Två mätta detaljer som jag inte kallar fynd: (1) vid landningen mäter högerkanten 3 px
och vänsterkanten 2 px, därför att `.seam [data-l="4"]` är centrerad på `--x4`
(`left:calc(var(--x4) − 1px)`, rad 1226) medan `[data-l="1"]` börjar PÅ `--x1` — planets
kant landar exakt på `--x4`, så konturen och linjen överlappar med 1 px i stället för att
sammanfalla. Det är en förbefintlig detalj i `.seam`, inte i R22:s aritmetik. (2) Vid 390
ligger kontur och kantlinje 5,2 px isär vid t3 och 2,1 px vid tx 0,9 (`21 × (1 − tx)`),
alltså en kort dubbelkontur strax före landningen; vid 1920 är samma avstånd 35 px och
läses som konvergens. Ingen av de två syns i något mått jag har satt en gräns för.

## ceiling
- **highway s03 (P04):** r21:s enda kvarvarande punkt mot referensen var att dess tråd
  är ett SLUTET objekt hela vägen medan vår kontur var öppen i sidorna genom hela
  tx 0,6–1,0. Den skillnaden är borta: konturen är sluten om alla fyra sidor i varje
  läge där den har opacitet, mätt på pixlar och inte bara i källan. Kvar mot referensen
  finns inget jag kan mäta upp den här rundan.
- **Motor och shim:** n/a. `scrollcraft.js` och `scrollcraft.css` orörda, fortfarande
  exakt två iframes, F-011 respekterad, och R22 lade till nio rader totalt utan en enda
  ny lyssnare eller tillståndsvariabel.
- **Kända rester, noterade och inte fynd (oförändrade, hos Anton):** arket 63,4 % vw vid
  1920, fyra typsnittsfiler mot budget tre, Hōrais 390-överflöd i `sites/horai.html`,
  och den enskilda 260–532 ms-uppgiften i `sites/horai.html` vid Calyx-progress
  0,94–0,98.

## material_fixes
Inga. Båda r21-fixarna håller på renderade pixlar vid alla tre bredderna,
regressionsvakten ger samma tal som r21 på varje rad, och Codex gav 0 fynd.

Noterat, inte fynd, om lead vill ha total symmetri vid landningen: `index.html:1226`
centrerar den högra kantlinjen på `--x4` medan den vänstra börjar på `--x1`, vilket ger
3 px höger mot 2 px vänster i landat läge. Ett `--pl-r` räknat mot `x4 + 1`
(`index.html:2557`) skulle lägga de två 2 px-banden exakt på varandra. 1 px, inom den
beställda toleransen, och inte värt en runda för egen del.

## keep
- **De två R22-fixarna.** `.tes-plane::after` med samma `--tx`/`--pl-*`-tal som
  `clip-path` (1197–1201), och `--pl-l`/`--pl-r` räknade mot planets egen
  `getBoundingClientRect()` (2555–2558). Båda verifierade på pixlar; `box-shadow:inset`
  på elementets egen box och `window.innerWidth`-räkningen får aldrig komma tillbaka.
- **R21:s borttagning.** `.tes-plane` i normalt flöde: `position:absolute` i 1994
  bildrutor vid fyra bredder, `fixed` aldrig, 0 träffar av text i eller bakom konturen,
  ingen stapling. Nu dessutom mätt med en kontur som FAKTISKT ritas där provet letar.
- **Blåkopians mekanik.** `--tx` ur `--sc-ps`, linjernas x ur arkets egna stationer, de
  tre klippfönstren, rubrikens bläckning, och toningsfönstret 0,6→0,9 för `--p-edge`.
- **r18:s fyra fixar.** Landningslinjen i full bredd (`--x4 − --x1 + 2`, mätt 1219 /
  1169 / 349 × 2 px), 2 px linjevikt och ≥3:1 kontrast (nu 3,62–17,71:1 även för den nya
  konturen), Hōrai-ramens tidiga `src`, `SEO-optimering` utan radbrytning.
- **Noll horisontell scroll** vid alla nio bredderna, och noll extra kostnad per bildruta
  för det nya `::after` (0 långa uppgifter i A/B vid 1920 och 390).
- **Stegbanden, ramarna, prisenheten och case-övergångarna** — orörda av denna runda, och
  per § keep i r21 fortfarande de som gäller.

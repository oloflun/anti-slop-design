fix

## persistence
Egna bilder och mått i `shots/astra-r15/`. Alla fångster är gjorda i Chromium med `ignore_default_args=['--hide-scrollbars']`. Varje läge nåddes med `mouse.wheel` från toppen i en ren sida, med en skärmbild per sida och ramarna laddade (`capture.py`, r10:s verktyg utökat med 1920x930, fyra tesmeningar, P21 och ett mått på ramarnas rullningslister). Par-bilderna `Pxx-{1920,1440,390}.png` täcker alla PARITET-rader (P05 är utgången; P06 är samma läge som `P04-chapter`). 1920-paren har 1440-referensen till höger, eftersom det inte finns några referenser vid 1920. Överlapp är dömda i enskilda bilder under `ours/`. P16 är dömd på kontaktarket `sheet-1920.png`, som byggts av 34 hjulsteg i en sida. Det kontaktarket är inte underlag för någon överlappsdom.

Mätsvep (`measure15.py` → `measure15.json`, `fit390.py` → `fit390.json`, `gtr.py`, `probe_h3.py`):
- **Ramarnas rullningslister:** `innerWidth-clientWidth` och `innerHeight-clientHeight` är 0 i båda iframes, i alla fångster vid 1920, 1440 och 390 (`positions-*.json`, `framebars`).
- **Ridån, 20 px-hjul från tesens pinslut till kapitlet +1,3 vh:** 154/149/140 bildrutor vid 1920/1440/390 och **0** träffar där en rubrik är delvis dold av en annan yta (r12:s `SWEEP_JS`, clip-medveten).
- **Casen, 20 px-hjul genom hela sektionen:** 0 bildrutor med två synliga steg, vid alla tre bredderna och i båda casen. Vid 390 finns 0 bildrutor där caselinjen syns samtidigt med steg 2 eller senare. Vid desktop står caselinjen alltid, vilket är avsiktligt. Bildrutorna där steg-h3 inte syns hel är bytesfönstren (`--out`/`--in`), alltså avsiktliga.
- **Delade ord** (`.ts`, `.case-name`, `.case-line`, `.cs h3`, rubriker, `.statement`): 0 vid 1920, 1440 och 390. Skriptet mäter bara rubriker. Det delade beloppet i ingressen hittades i bilden (fix 3).
- **Horisontell scroll:** 0 vid 320, 375, 390, 414, 768, 1024, 1280, 1440 och 1920.

Codex (`gpt-6-astra`, medium, read-only) körde en gång med 24 par (`prompt.txt`, `imgs.txt`, `codex-out.txt`). Det gav 12 par vid 1920, 4 vid 1440 och 8 vid 390. Codex gav en rad per par: 18 håller och 6 håller inte. Det gav också 3 fynd, och alla tre överlevde verifieringen, varav ett i omformulerad form:
- **Fynd 1 (Hōrais h3):** stämmer mot `index.html:965` och `2672`, och syns i PNG:erna.
- **Fynd 2 (Hōrai steg 1 ryms inte vid 390):** bara delvis sant. Bilden fångades med en synlig rullningslist, så `clientWidth` var 380, och där är marginalen −1 px. På en riktig 390-telefon utan rullningslist är marginalen +21 px (`fit390.json`). Den verkliga orsaken är en annan: caselinjen fälls aldrig ihop (fix 2). Det är den som gör att texten inte ryms vid 375. Fyndet är därför omskrivet till fix 2 med den uppmätta orsaken.
- **Fynd 3 (26 900 kr):** stämmer mot `index.html:1995` och bild `P21-bro-390`.

0 fynd släpptes. Fix 4 (arket vid 1920) är mitt eget, mätt i PNG.

**Leadens fynd är bekräftat.** Vid 390 syns inte Hōrais h3 "Namnet står en gång" i `case-horai-01`, medan Calyx h3 syns. Samma sak gäller vid 1440 och 1920, och i varje `case-horai-0N` utom -06. Orsaken beskrivs i fix 1.

## fidelity
Antons feedback, punkt för punkt:
- **Hyperborea upp och större:** stängd. Vid 1920 är plåten ~47 % vw med överkanten i linje med meningen (`P03-1-1920`), och den står still genom alla fyra meningarna.
- **Blått → ritning:** stängd. Hjulsvepet ger 0 halvklippta rubriker, och kapitelrubriken klipps bara av viewportens underkant (`P04-curtain-1920`, `-390`).
- **Case-rubrikerna:** bär vid desktop (`P17-1-1920`, `P19-1-1920`). Vid 390 visas meningen bara i steg 1, enligt beslut.
- **Casetexten:** copy-gaten är körd, och den döms inte här.
- **Tesbandet slutar på "Vi hjälper er att synas på rätt sätt.":** stämmer, med fyra meningar och fyra streck.
- **Prisblocket:** rubriken, säljtexten och liggaren läses som ett avslut vid 1920 och 1440 (`P21-bro`, `P15a`). Vid 390 bryts beloppet (fix 3).

**PARITET, rad för rad (1920 / 1440 / 390):**
- **P01 fold:** håller vid alla tre bredderna.
- **P02 kortets baksida:** håller vid alla tre bredderna.
- **P03 tesbandet:** håller vid alla tre bredderna.
  - Vid 1920 är Hyperborea en jämbördig motpart, med gemensam överkant och luften `--rail-x` till höger.
  - Detalj som inte är ett fynd: vid mening 4 har bildens egen zoom (`scale(1.06)`, origin 70 % 40 %) klippt bort sajtens vänstra kant i bilden ("ITION MMXXVI", `P03-4-1920`). Det är en beskärning av ett foto, ingen rubrik.
- **P04 kanten tes → kapitel:** håller vid alla tre bredderna. Kanten är ren och har 0 träffar i svepet.
- **P06 kapitelskärmen:** håller vid alla tre bredderna (`P04-chapter-1920`). Ingenting ur band 01 syns.
- **P07 steg 01 och P11 steg 05:** håller vid 1440 (arket 81,0 % vw) och vid 390. **Håller inte vid 1920x930:** arket är 63,2 % vw (`ours/P07-1920.png`) mot PARITET:s ≥ 76 %. Det är höjdbundet, med ~350 px tomt mörkt fält på var sida (fix 4).
- **P08–P10 och P13:** håller vid alla tre bredderna. Processen är orörd sedan R12.
- **P12 steg 06:** håller vid 1440 och 390. Vid 1920 gäller samma höjdbundna ark som i P07, med ramen ~60 % vw (fix 4).
- **P14 case-kapitlet:** håller vid alla tre bredderna.
- **P15 pris + kontakt:** håller vid 1920 och 1440 (`P15a-1920`). Vid 390 håller den som skärm. Ingressens delade belopp hör till fix 3.
- **P16 hela sidan:** håller vid 1920. Materialrytmen på `sheet-1920.png` är foto, blått, ritbordet, papper, svart, foto. Det finns inget tomt band över 60 % vh och ingen hård kant utom de avsedda. De saknade Hōrai-h3:orna syns även där (fix 1).
- **P17 case Calyx:** håller vid alla tre bredderna. Ramarna har ingen rullningslist, steget ryms och marginalen vid 390 är ≥ 49 px.
- **P18 bryggan:** håller vid alla tre bredderna.
- **P19 case Hōrai:** håller **inte** vid någon bredd.
  - Steg-h3 är bortklippt eller halvklippt i -01 och -03, vid 1920, 1440 och 390 (fix 1).
  - Vid 390 finns dessutom ett tomt, osynligt caselinjeband mellan namnet och texten i steg 2–6 (`ours/P19-3-390.png`, fix 2).
  - Resten håller: citatet är format i -03, och -06 är komplett.
- **P20 Hōrai → pris:** håller. Skarven är ren (`P21-skarv-1920`).
- **P21 prisenheten**, dömd mot `#pris` eftersom bron är borta: håller vid 1920 och 1440. **Håller inte helt vid 390:** "26 / 900 kr" bryts över två rader (fix 3).

## ceiling
- **Motor och shim:** n/a. Motorn är orörd, `sites/*` är orörda och det finns exakt två iframes. F-011 respected.
- **Referenserna:** hoy låter varje kapitelskärm bära hela sin viewport vid varje bredd. Vid 1440 gör V3d:s process samma sak, men vid 1920x930 gör den det inte, eftersom arket har fast bildförhållande och bara skalar med höjden (fix 4).
- **Hōrais och Calyx egna mobillayouter:** Hōrais högerkant klipps (675 px) och Calyx nav krockar vid 390. Båda noteras enligt leadens beslut och är inga fynd.

## material_fixes
1. **Hōrais preview-mål hamnar i stegets `--out`-fönster, så steg-h3 klipps i varje par-bild av P19.** Det gäller `index.html:2672` (`aimPin(chEl, (chN - 1 + 0.8) / 6, …)`) och samma `p` i `caseY` på raden under. Med n=6 är `(N-1+.8)/6` = 0,1333 för steg 1. `--out` börjar vid `b-f` = 1/6−0,04 = 0,1267 (`index.html:965–970`). `.cs` klipps därför 16,6 % uppifrån, och det tar hela h3 (21 av 131 px vid 390, 33 av 261 vid 1440). Calyx klarar sig: 0,8/5 = 0,16 = exakt `b-f`. Expected: siktet ligger inom `[a+f, b-f]` för varje N, till exempel `Math.min((N-1+.8)/n, N/n - .045)` för båda casen. Kontroll: `case-horai-01…06` vid 1920, 1440 och 390 visar hela h3 (h3:s rect inom `.cs`-klippet). R9:s citatvillkor i `-03` håller fortfarande: `#quote-text` står inom ramens ih vid 390 och 375.
2. **Caselinjen fälls aldrig ihop på mobil: deklarationen är ogiltig.** Det gäller `index.html:1025`, `grid-template-rows:calc((1 - var(--out)) * 1fr)`. `fr` får inte stå i `calc()`. `CSS.supports('grid-template-rows','calc(0.5 * 1fr)')` ger `false`. Uppmätt i `case-horai-03` vid 390: `gridTemplateRows` 22,09 px, opacitet 0 och höjd 22 px. Raden blir alltså osynlig men tar fortfarande plats: 22 px vid 390 och 44 px vid 375, i steg 2–6 i båda casen. Följden vid 375 utan rullningslist: Hōrais sista glyf står 5–10 px **under** stagens underkant i alla sex stegen (`fit390.json`). R12 hade ≥ 8 px. NOTES R15:s "faller ihop" stämmer inte. Expected: raden kollapsar på riktigt, till exempel `max-height:calc((1 - var(--out)) * 2.6em)` med `overflow:hidden` i stället för grid-tracket. Det ska ge höjden 0 vid `--out=1`. Därefter ska Hōrais och Calyx sista glyf stå ≤ stagens underkant −8 px i varje steg vid 390 och 375. Steg 1 vid 375 (−10 px med två rader caselinje) behöver en egen åtgärd i spacing, utan att copy eller ramraden rörs.
3. **Beloppet bryts över två rader i ingressen vid 390.** Det gäller `index.html:1995`, "kostar 26 900 kr" med vanliga mellanslag, och syns i `P21-bro-390.png` ("26" / "900 kr."). Expected: `26&nbsp;900&nbsp;kr`. Ordvalet är oförändrat, och beloppet ska stå på en rad vid 320–1920.
4. **Processarket når inte P07:s ≥ 76 % vw vid 1920x930.** Uppmätt i PNG: 63,2 % vw vid 1920 (`ours/P07-1920.png`, x 348–1561) mot 81,0 % vid 1440. P12:s ram är ~60 % vid 1920. Orsaken: arket har fast bildförhållande och är höjdbundet under bandet, så de tomma sidofälten blir ~350 px vardera. Felet fanns före R12, eftersom processen inte har rörts i R12–R15. Det blir materiellt nu när 1920 är en dömd bredd. Expected: arkets bredd är ≥ 76 % vw vid 1920x930 i P07, P11 och P12, utan att bandet eller rubriken klipps. Vägen dit är leadens val, till exempel ett bredare bildförhållande på arket vid ≥ 1600 px eller ett lägre band. 1440 och 390 ska vara oförändrade.

## keep
- **R12:s Hyperborea-rad:** kolumnen `1.2fr`, `.thesis-figure{grid-row:1;align-self:start}` och `letter-spacing` låst till −.02em. Plåten står still och i linje med meningen vid 1024–1920.
- **R12:s ridå i flödet:** `.process-chapter{position:relative}` och R14:s `min-height:120svh`. Det ger 0 rubrikklipp i 20 px-hjul vid 1920, 1440 och 390, och kapitlet står ensamt vid 1920.
- **`scrolling="no"` på båda iframes:** 0 px rullningslist i en riktig Chromium vid alla bredder.
- **R14:s namn plus meningens rest i samma `h2`:** det tillgängliga namnet är den låsta meningen ordagrant.
- **R13:s prisenhet:** tonövergången från svart till foto är sömlös, och ingressen i 24 px ligger över `.label` i hierarkin.
- **R15:s idé att visa caselinjen i steg 1 och tona ut den med `--out`:** fönstret är rätt och överlappar 0 bildrutor. Bara kollapsmekanismen behöver bytas (fix 2).

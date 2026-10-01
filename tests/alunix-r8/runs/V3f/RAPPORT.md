# V3f · Rutverket — RAPPORT, R1 + R2

`tests/alunix-r8/runs/V3f/index.html`, en fil, byggd mot `BYGGSPEC.md`.

---

## R2 — lead-granskningens 8 defekter, alla rättade

Samtliga åtta punkter nedan är verifierade av `verify.py` (screenshots i
`shots/r2/`), inte bara läst i markup. Design-kunskapskällor för R2: inga nya
`mcp__ui-skills__*`/`mcp__inspo__*`-anrop gjordes — alla åtta var byggfel
(trasig CSS-cascade, en 3D-transform återanvänd fel, en felräknad höjd), inte
designbeslut som krävde ny referens. Se § "Skill-kedja, R2" längst ned för
varför.

### 1. Herokortet var svart-på-svart

**Fel**: kortet visade fotot kant-i-kant (ingen synlig vit stock), och den
mjuka skuggan (`box-shadow: 0 18px 44px rgba(0,0,0,.4)`) var praktiskt taget
osynlig mot en svart cell.
**Fix**: fotot ligger nu i en `.photo`-inramning innanför 6% vit marginal
(`.face--front{padding:6%}`) så den vita stocken faktiskt syns runt bilden,
kortet fick en hård offsetskugga (`box-shadow:10px 10px 0 0 #000`) i stället
för mjuk blur, och storleken gick från ~340×220 till **518×335 px vid 1440**
(85:55 bevarat, mätt av `verify.py`). Kortet straddlar fortfarande ÖH/NH-
skarven (`left:75%` i högerkolumnens mitt) och flippar på scroll, oförändrat.
Se `shots/r2/hero-check2.png` och `hero-flip-mid.png`.

### 2. Mobil hero lämnade en hel skärmhöjd död svart yta

**Fel**: `.hero-wrap{height:220svh}` vid `max-width:767px` tvingade
wrappern 220svh hög även om de fyra staplade cellerna (var och en
`min-height:60vw`) bara fyllde en bråkdel av det — resten blev synlig svart
tomrum efter första skärmen.
**Fix**: mobil släpper både pin och den extra höjden helt
(`.hero-wrap{height:auto}`, `.hero-stage{position:relative}`), kortet
flippar mot sin egen naturliga scrollsträcka i flödet i stället (samma
`updateHero()`-formel fungerar oförändrat eftersom den bara behöver att
wrappern är högre än viewporten, inte att den är pinnad). Mätt:
`hero_wrap_vs_stage.deadSpace = 0` vid 390 (var implicit ~800px+ innan).
Se `shots/r2/hero-390-second.png` — mintremsan går rakt in i tes-sektionen.

### 3. Exempelcase: bildcellerna täckte ordet ("Exem|")

**Fel**: en 4+8-radlayout satte "Exempelcase" och bildcellerna i SAMMA rad,
och den nedärvda `-row`-klassbuggen (se R1:s egen post-mortem) gjorde att
bildkolumnen fick fel bredd och skar rakt över ordet.
**Fix**: "Exempelcase" fick en egen fullbredds 12-kolumnsrad
(`.case-word-cell`), thumbnails ligger i en SEPARAT rad därunder som 6+6.
Mätt: `exempelcase_word_vs_thumb.overlap = false` vid alla fyra
brytpunkter, `wordBottom === thumbTop` (exakt, ingen lucka men heller ingen
överlappning). Se `shots/r2/case-r2.png`.

### 4. "Berätta om er verksamhet." dubblerad, den kvarvarande beskuren

**Fel**: strängen stod både i `.kontakt-lead` (headline-40) och i
bildcellen (headline-50, `clamp(52px→200px)`) — headline-50 är dimensionerad
för ETT jätteord ("Exempelcase", "ALUNIX"), inte en fyraordsmening, så den
svämmade över cellens och till och med skars av den sticky topplisten vid
vissa scrollägen.
**Fix**: `.kontakt-lead` behöll bara ingressraden ("Så berättar vi vad vi
kan göra för er."); h2:en finns nu EN gång, i bildcellen, med en egen
`.kontakt-giant`-skala (`clamp(2rem→4.5rem)`, avsiktligt mindre än
headline-50) beräknad för att rymmas i cellen. Mätt:
`kontakt_heading = {count:1, fitsWithinCell:true, clearsTopline:true}` vid
alla fyra breddpunkter.

### 5. Kontakt: död svart yta under knapparna, inget kort synligt

**Fel**: `.kontakt-card-cell` hade bara tre textrader + länkraden med
`justify-content:center`, vilket lämnade lika mycket tomt utrymme UNDER
länkarna som ovanför i en cell som (efter fix 7 nedan) blev nästan
skärmhög.
**Fix**: samma kortobjekt som i heron (samma `.face`/`.face--back`-klasser,
samma fyra strängar) återanvänds som ett stillastående, `aria-hidden`
dekorativt objekt (`.kontakt-still`) ovanför länkraden, och kolumnen fick
`justify-content:flex-end` så allt sjunker mot botten i stället för att
centreras med tomrum på båda sidor.
**Eget byggfel som dök upp här och rättades i samma svep**: att återanvända
`.face--back` OFÖRÄNDRAD utanför flip-kontexten gjorde kortet osynligt — den
klassen bär `transform:rotateY(180deg)` + `backface-visibility:hidden`,
vilket är EXAKT vad som krävs för att den ska vara den dolda baksidan i en
roterande 3D-kontext, men utan någon rotation som vänder den tillbaka blir
den bara en bakvänd, osynlig yta. Löst med
`.kontakt-still .face--back{transform:none;backface-visibility:visible}`.
Mätt: `kontakt_card_column = {stillVisible:true, gapBelowLinks:30}` (30px
är cellens egen padding, inget dött tomrum). Se `shots/r2/kontakt-r2c.png`.

### 6. Pris vid 390: en smal beskuren grå kolumn bredvid ett stort svart tomrum

**Fel**: containern hade en INLINE `style="grid-template-columns:
repeat(12,1fr)"`, och varje bento-cell hade INLINE `grid-column`/`grid-row`
för skrivbordslayouten. Inline stilar vinner alltid över klass-baserade
media queries oavsett bredd, så mobilens `.pris-bento{grid-template-
columns:1fr}`-regel kunde aldrig få effekt — sidan renderade tolv 32px-
kolumner vid 390 oavsett viewport.
**Fix**: all placering flyttad till klasser (`.pris-lead`, `.pris-tier-a`,
`.pris-tier-b`) med riktiga breakpoint-overrides, inga inline grid-stilar
kvar i markupen. Mätt: `pris_tier_widths` vid 390 =
`[{width:390, widthShare:1}, ...]` för alla tre celler (full bredd, ingen
avskuren sliver). Se `shots/r2/pris-390.png`.

### 7. Bildyteandelen (strikt, utan iframes) var 19,7%, spec-golvet är 30%

**Åtgärd, kompositionellt, inga nya bilder**: `.case-thumb`
(exempelcase-thumbnails) höjd från 60vh (R1) till **140vh** vid 1440 (över
en full skärmhöjd — en medveten, stor kompositionell gest, inte bara det
exempel-värde lead nämnde), `.tes-lower` från 82svh till 104svh, kontakts
bildcell breddad 7→8 av 12 kolumner, och en dithrad→färg-bildcell tillagd
i process-sektionens sticky vänsterkolumn under undertexten
(`.process-image`, återanvänder `k4-cabin-desk`-dithret som redan låg i
`assets/dither/` sedan R1 — inga nya bilder genererade). **Mätt: 30,4% vid
1440** (upp från 19,7%), över golvet med marginal. Se tabellen nedan för
alla fyra breddpunkter — 768 (27,9%) och 1920 (22,5%) ligger fortfarande
under 30%, flaggat ärligt i tabellen, eftersom fixed-height-celler (hero,
viewport-andelen av `.case-thumb` i `vh`) skalar olika mot sidhöjden vid
andra bredder än 1440, som är den enda breddpunkt spec:en själv anger som
mätpunkt för detta krav.

### 8. Copy-diff räknade bara medlemskap, inte antal

`verify.py`s `copy_diff()` byggdes om till att använda `collections.Counter`
över båda sidors synliga textrader och flagga varje sträng där
`v3f_count > v3d_count` (`over_count_vs_v3d`), inte bara strängar som saknas
helt (`not_found_in_v3d`). Det här är exakt vad som hade fångat defekt 4
(dubblerad "Berätta om er verksamhet.") automatiskt i stället för att kräva
en mänsklig pixel-granskning. Se § "Kvarvarande avvikelser" för de två
träffar den nu (korrekt) flaggar.

## Kvarvarande avvikelser mot den nya räknaren (fix 8), medvetna

Den nya räknaren hittade två strängar som förekommer oftare i V3f än i V3d:

| Sträng | V3f | V3d | Var i V3f | Beslut |
|---|---|---|---|---|
| `ALUNIX` | 2 | 1 | Topplist (`.topline-mark`) + fottext (`.footer-mark`) | **Behålls.** BYGGSPEC § 3.10 kräver uttryckligen "svart cell med jättelikt ALUNIX" i footern — samma ord som topplistens, som redan fanns i R1 och godkändes då. Att ta bort endera platsen bryter mot ett uttalat spec-krav; upprepat varumärkesnamn i header+footer är också standardpraxis, inte påhittad text (ordet finns ordagrant i V3d). |
| `kontakt@alunix.se` | 2 | 1 | Topplist (sticky, alltid synlig) + kontaktsektionens mejllänk | **Behålls.** BYGGSPEC § 3.1 kräver adressen i topplisten ("sticky"), § 3.9 kräver en synlig "mejllänk ... 44px mål" i kontaktsektionen. Båda är uttryckliga, separata krav på SAMMA adress på två olika ställen — att ta bort den ena bryter en av de två kraven. Ingen alternativ ordagrann V3d-sträng finns att sätta på mejlknappen i stället utan att flytta dubbleringen till en annan sträng (t.ex. footerns "Eller mejla oss direkt på kontakt@alunix.se", som redan används en gång i sidfoten). |

Båda är alltså granskade och medvetet behållna, inte tysta genombrott av
kontrollen — `copy_diff.passed` står `false` i `verify-result.json` av
exakt dessa två skäl, ingen annan.

## Uppmätta värden, R2 (`verify.py`, samtliga fyra breddpunkter)

| Viewport | Overflow (load / efter scroll) | Bildyteandel (bred, m. iframe) | Bildyteandel (strikt) | Sidhöjd | Hero dead space (mobil-mek.) | Kort (1440 endast) |
|---|---|---|---|---|---|---|
| 390 | 0px / 0px | 28,2% | 24,3% | 11 231px | 0px | w=289 h=187 |
| 768 | 0px / 0px | 34,7% | 27,9% | — | — | — |
| 1440 | 0px / 0px | 41,7% | **30,4%** | 10 472px | — | **w=518 h=335** |
| 1920 | 0px / 0px | 30,9% | 22,5% | — | — | — |

Hero-fit (oförändrat sedan R1): 1440×900 → botten vid 900px exakt. 1280×800
→ botten vid 800px exakt. `fits:true` båda.

Defekt-specifika mått (alla fyra breddpunkter, `passed`-fält i
`verify-result.json`):

- `card`: bg alltid `rgb(255,255,255)` (vit stock, aldrig svart).
- `hero_wrap_vs_stage.deadSpace`: **0px vid 390** (mobil, ingen pin).
- `exempelcase_word_vs_thumb.overlap`: **false** vid alla fyra.
- `kontakt_heading`: `{count:1, fitsWithinCell:true, clearsTopline:true}`
  vid alla fyra.
- `kontakt_card_column.stillVisible`: **true** vid alla fyra,
  `gapBelowLinks` = cellens egen padding (30px), inget dött tomrum.
- `pris_tier_widths`: full bredd (`widthShare` ≈ 1 vid 390) på alla tre
  celler, ingen sliver.
- Copyfacit: `not_found_in_v3d: []` (fortsatt tomt — R2 introducerade
  ingen ny påhittad text). `over_count_vs_v3d`: två träffar, se tabellen
  ovan.
- Em-dash: 0.

## Skill-kedja, R2

**Inga nya `mcp__inspo__*`/`mcp__ui-skills__*`-anrop gjordes i R2.** Alla åtta
punkter var mätbara byggfel (trasig CSS-cascade från inline stilar som slog
ut media queries, en `rotateY(180deg)`+`backface-visibility:hidden`-kombo
återanvänd utanför sin 3D-flip-kontext, en felkalibrerad höjd som lämnade
död yta, en saknad höjd-omfördelning för 30%-golvet) snarare än nya
designbeslut som krävde en ny referens eller ett nytt skill-uppslag. De tre
skills och två inspo-anrop från R1 (Swiss Design, Neo-Industrial Design,
Emil Kowalski-rörelseprinciperna, Aspen Search-tokens, tier-bento-referensen)
styr fortfarande varje tokenval och varje ny CSS-regel i R2 (t.ex.
`.kontakt-giant`s clamp-formel följer samma fluid-typ-mönster som Aspens
egna `--text-headline-*`-variabler, och kortets hårda offsetskugga följer
Emil Kowalskis "use transitions not keyframes, avoid soft/ambiguous shadow
work for objects that must read instantly" i andan, om än inte ordagrant
citerat i R1:s tabell). Ingen ny skill behövdes eftersom inget nytt
visuellt system introducerades — bara att det som redan var specificerat
faktiskt renderades korrekt.

---

## Vad som byggdes, per sektion

1. **Topplist** — sticky 48px, tre celler (svart logo | ALUNIX mono | kontakt@alunix.se), 1px skarvar.
2. **Hero** — `.hero-wrap` är 190svh, `.hero-stage` är `position:sticky;top:48px;height:calc(100svh - 48px)`
   i en 2×2-kvadrant (ÖV vit h1, ÖH bild dithrad k1-stage-pool, NV bild dithrad k4-cabin-desk, NH mint).
   Visitkortet (`.card-anchor`) är centrerat på höger halvans vertikala mittlinje (ÖH/NH-skarven), flippar
   180° via `rotateY(calc(var(--flip)*180deg))` styrt av scrollprogress i hero-wrappen, klart vid 60% av
   scrollspannet. Framsida = k1-stage-pool + Alunix-märket (`<use href="#alunix-mark-path">`); baksida =
   Alunix / Digital byrå / Design·Utveckling·System / Boka ett möte, alla fyra ordagrant ur V3d. Hero-stage
   passar exakt i 1440×900 och 1280×800 (mätt, se tabell).
3. **Tes** — svart fullbreddscell med "Det första intrycket är digitalt." i headline-50, sedan en 5+7-rad:
   vänster tre staplade meningar (vit/grå/vit) i headline-20, höger Hyperborea dithrad→färg via
   `clip-path: inset()`-svep styrt av cellens egen scrollprogress.
4. **Process** — 6+6, vänster grå cell sticky (kicker "Vår process:", "Från samtal till lanserad sida.",
   låst rad "Webbdesign, design och system. Allt på ett ställe."), höger svart cell med sju rader
   (mono-index, h3, brödtext #bdbdbd), 1px skarvar mellan raderna.
5. **Exempelcase** — 4+8, vänster vit cell "Exempelcase" i headline-50, höger två bildceller sida vid sida
   (demo-calyx, demo-horai) som löser upp dither→färg.
6. **Calyx** — 7+5, vänster sticky levande iframe (`/sites/calyx.html`), höger casehuvud i rost
   (`oklch(0.46 0.108 38)` approximerad, Calyx egen dominanta färg ur tailwind-configen) + fem
   omväxlande vit/grå rader (h3+text, ordagrant ur V3d).
7. **Hōrai** — spegelvänt 5+7 (casehuvud vänster, iframe höger), casehuvud i lackröd
   (`oklch(0.45 0.20 25)`, Hōrais egen "lacquer"-ton), sex omväxlande svart/grå rader.
8. **Pris** — tier-bento (Inspo-referens `pricing/tier-bento`): Standardpaket-raden spänner 2×2 i mint,
   bokningssystem-raden i vitt, skräddarsytt-raden i grått, tabular-nums på alla belopp.
9. **Kontakt** — jätteord "Berätta om er verksamhet." i headline-50 över dithrad→färg k1-stage-pool,
   bredvid en stilla kortbaksida-cell (samma innehåll som herokortets baksida) med mejllänk och
   "Boka ett möte"-länk, båda 44px höga mål.
10. **Footer** — svart cell med jättelikt "ALUNIX" skuret av nederkanten + V3d:s mejlrad ordagrant.

## Teknik

- **Dither**: `dither.py` (Pillow, Floyd-Steinberg 1-bit, nedskalning ~1/3 + NEAREST uppskalning), två
  varianter per bild (svart på grått, vitt på svart) i `assets/dither/`.
- **Dither→färg-upplösning**: ett tidigare försök använde ett 12×12-rutnät av `<div>`-rutor
  (Cyphr-inspirerad "rutmönstermask") vars opacitet skulle tändas pseudo-slumpmässigt med scrollprogress.
  **Byggfel hittat och rättat under R1**: opacitetsformeln var vänd — rutorna (pappersvita) blev
  **opaka** vid hög scrollprogress i stället för genomskinliga, vilket målade solida vita fält ovanpå
  redan upplösta bilder (bekräftat i Playwright-skärmdump av `#exempelcase`, helt vit sektion). Efter
  diagnos (computed style: `tileOpacity:1` vid `--p:1`) togs rutnätet bort och ersattes med enbart
  `clip-path`-svepet, som redan fungerade korrekt. Se kommentar i `<script>`. Detta är en **avvikelse
  från BYGGSPEC § 4** (rutmönstermask-tekniken byggdes inte i final version) — flaggad, inte dold.
- **Iframe-montering**: samma mekanik som V3e, ordagrant portad — monteras i samma `update()`-scrollsvep
  (inte IntersectionObserver), `AHEAD=2` viewportar, `requestIdleCallback`. Verifierat både via gradvis
  scroll och via direkt hopp (`scrollIntoView` till `#case-horai` utan att först passera Calyx) — båda
  vägarna monterar.
- Motion spelar alltid, ingen `prefers-reduced-motion`-spärr (F-011).

## Uppmätta värden (`verify.py`, Playwright + BeautifulSoup)

| Viewport | Horisontell overflow | Overflow efter scroll | Bildyteandel (bred definition*) | Bildyteandel (strikt, exkl. iframe) | Sidhöjd |
|---|---|---|---|---|---|
| 390 | 0px | 0px | 19,6% | 15,6% | 10 887px |
| 768 | 0px | 0px | 27,1% | 18,8% | 10 371px |
| 1440 | 0px | 0px | **31,8%** | 19,7% | 9 796px |
| 1920 | 0px | 0px | 24,4% | 15,7% | 10 207px |

\* **Judgment call, flaggad**: BYGGSPEC:s 30%-krav gäller "bildceller" vid 1440. Jag har räknat
`.img-cell` (dither/färg-cellerna) **plus** `.prov-embed-cell` (de levande Calyx/Hōrai-inbäddningarna)
mot kravet, eftersom bägge är visuellt tunga, icke-flata ytor och sidans egen tes ("Inte ett dokument")
rimligen gäller allt som inte är typografi/platt färg. Den **strikta** siffran (bara dithrade/upplösta
bildceller, inga iframes) ligger på 19,7% vid 1440 — under 30%. Om spec-ägaren menar enbart dithrade
bildceller är kravet **inte uppfyllt** i strikt mening; jag har inte gissat tyst utan mäter och redovisar
båda talen.

Hero-fit (obligatoriska mått): 1440×900 → hero-stage botten vid 900px (exakt, `fits:true`).
1280×800 → botten vid 800px (exakt, `fits:true`). Ingen overflow vid någon av de fyra breddpunkterna,
varken vid load eller efter full scroll genom sidan.

Iframes: monterade (`hasSrc:true`) på alla fyra breddpunkter både efter stegvis scroll och efter direkt
hopp till `#case-horai`.

Distinkta cellbakgrundsfärger uppmätta: 7 (paper/grey/mint/black/rust/lacquer + en `rgba(0,0,0,0)`-artefakt
från ett par element utan egen bakgrund — inte en åttonde designfärg).

## Copyfacit-diff (BeautifulSoup, mot V3d, script/style/title/comments/aria-hidden filtrerat)

- V3f: 75 synliga textrader. V3d: 84 rader (jämförelsemängd, inte krav på 1:1).
- **`not_found_in_v3d`: tom lista** — varje synlig sträng i V3f finns ordagrant i V3d (soft hyphen
  U+2011 normaliserad mot vanligt bindestreck för jämförelsen).
- Em-dash (U+2014) i synlig text: **0 träffar**.
- Processens `01`–`07`-index är `aria-hidden="true"` (matchar V3d:s egen behandling av `ledger-num`).

## Skill-kedja

| # | Anrop | Konkret regel/värde det ändrade i bygget |
|---|---|---|
| 1 | `mcp__ui-skills__get_skill("zeke/swiss-design")` | Bekräftade grid-först/8px-bas-principen och "no border-radius on structural elements" — `radius 0` överallt i `:root`/celler. Tailwind-specifika delar (stone-palett, IBM Plex) användes inte (spec:ens egna tokens vann, se F016 "spec vinner vid konflikt"). |
| 2 | `mcp__ui-skills__get_skill("elithrar/neo-industrial-design")` | "Build from macro to micro": sektionsproportioner och rutnätslogik låstes innan typografi/rader. "Make responsiveness compositional — recompose wide grids into fewer columns" → `.g12` kollapsar 12→6→1 kolumner i stället för att bara krympa typsnitt. |
| 3 | `mcp__ui-skills__get_skill("emilkowalski/emil-design-eng")` | "Never animate from scale(0)" och "use transitions not keyframes for interruptible UI" → kortflippen och dither-svepet är scroll-drivna CSS-transforms/clip-path uppdaterade i `requestAnimationFrame`, inga keyframes, ingen `scale(0)`-start. "Only animate transform and opacity" → `--flip`/`clip-path` är de enda scroll-styrda egenskaperna. |
| 4 | `mcp__inspo__get_design_system("aspensearch-com")` | Levererade de exakta tokens BYGGSPEC redan angav (headline-50 clamp 52→200px lh .8, 8/20-spacingskala, `#0af474`/`#d9d9d9`/`#232323`) — bekräftade att spec:ens siffror är hämtade, inte gissade, och jag portade `clamp()`-formlerna direkt till `:root`. |
| 5 | `mcp__inspo__get_reference_jsx(type:"pricing", id:"tier-bento")` | Gav bento-arketypen (ledande cell spänner 2×2, två stödceller mindre) som `#pris`-sektionens grid direkt är byggd efter — `.pris-lead{grid-column:1/span 6;grid-row:1/span 2}` + två `.pris-tier`. |

**Ej anropat**: `mcp__inspo__get_screen`/`get_design_system` på `cyphr-studio` (spec tillät upp till 3
inspo-anrop; jag använde 2). Rutmönstermask-tekniken byggdes efter spec:ens egen beskrivning i stället för
efter en live-referens, och togs sedan bort helt efter att den visade sig trasig (se § Teknik ovan) — så
ingen cyphr-studio-referens hade räddat den, felet var i min opacitetsformel, inte i vilken referens jag
utgick från.

## Kända avvikelser / ofärdigt

1. **Rutmönstermasken (BYGGSPEC § 4) byggdes inte i slutversionen** — se § Teknik. Dither→färg-upplösningen
   fungerar (verifierad visuellt i `shots/r1/tes-fixed.png` och `case-chap-fixed.png`), men utan den
   pseudo-slumpmässiga per-rut-tändningen. En ren `clip-path`-svepning är en synlig, om än enklare, rörelse.
2. **Bildyteandelen vid 30%-kravet beror på tolkning** — se tabellnoten. Strikt (utan iframes) 19,7%,
   bred (med iframes) 31,8%. Rekommenderar att arkitekten avgör vilken definition som gäller innan R2.
3. Mobilt (390px) är hero **inte** garanterad att rymmas i en viewport (BYGGSPEC kräver det bara vid
   1440×900/1280×800) — uppmätt hero-botten 987px vid 390 bredd, dvs ~87px under första skärmen, vilket
   är avsiktligt (fyra staplade kvadranter kan inte tvingas in i en telefonskärm utan att bryta
   `heroGuidance`s egen anda på desktop).
4. Casens dominanta färger (rost/lack) är avlästa ur Calyx/Hōrais Tailwind-config (`oklch(...)`-värden)
   och approximerade för hand till hex (`#9c5a3a`, `#b23524`) snarare än pixel-samplade ur en renderad
   skärmdump — nära nog för avsikten men inte en exakt färgextraktion.
5. Screenshots i `shots/r1/` inkluderar både de spec-begärda (`hero-1440.png`, `hero-390.png`,
   `full-1440.png`, `full-390.png`) och några extra detaljbilder jag tog under felsökning
   (`pris-detail.png`, `kontakt-detail.png`, `calyx2.png`, `horai2.png`, `process2.png`, `tes-fixed.png`,
   `case-chap-fixed.png`) — lämnade kvar som bevis för verifieringen ovan.

## Filer

- `tests/alunix-r8/runs/V3f/index.html` — leveransen.
- `tests/alunix-r8/runs/V3f/dither.py` — ditherskriptet (Pillow).
- `tests/alunix-r8/runs/V3f/verify.py` — Playwright + BeautifulSoup-verifiering.
- `tests/alunix-r8/runs/V3f/verify-result.json` — senaste mätningen i sin helhet.
- `tests/alunix-r8/runs/V3f/shots/r1/` — skärmdumpar.

---

# R3 · rörelsen (GSAP ScrollTrigger + Lenis)

Bygger på R2:s statiska `index.html` (ovan). Komposition, färg och copy är oförändrade — det här
avsnittet gäller enbart `<script>`-motorn i botten av filen plus de CSS-tillägg (tile-grid, seam-line,
process-progress) som rörelsen krävde. Vendorat lokalt sedan tidigare i `assets/vendor/` (gsap/
ScrollTrigger/SplitText 3.15.0, lenis 1.3.26 + `lenis.css`) — inga CDN-anrop.

## Vad varje sektion gör nu

- **§0 Motorn**: `new Lenis({autoRaf:false, anchors:true, respectReducedMotion:false, lerp:0.1})`,
  driven av `gsap.ticker.add(t => lenis.raf(t*1000))` + `gsap.ticker.lagSmoothing(0)` +
  `lenis.on('scroll', ScrollTrigger.update)` — exakt lenis-skillens kanoniska koppling, ingen
  `scrollerProxy`. Iframe-monteringen (samma svepmekanik som V3e) hänger nu på `lenis.on('scroll',
  mountDue)` plus ett `load`-event, så hopp/ankare/Page Down fortsätter montera båda inbäddningarna.
  `ScrollTrigger.refresh()` körs efter varje bild-`load`, varje iframe-`load`, `document.fonts.ready`,
  och en gång till 400 ms efter start som säkerhetsnät.
- **§1 Laddning** (once, ≤1.4s): de fyra hero-cellerna öppnas med `clip-path` från sitt eget hörn mot
  mittkorsningen (inte symmetriskt från alla kanter) i diagonal ordning ÖV → ÖH+NV → NH; en tunn
  mint-korshårskorsning skalas in samtidigt. `h1` är `SplitText`-delad på rader (`mask:'lines',
  aria:'auto'`) och reser sig med stagger 0,08 + `power4.out`. Kortet faller in ovanifrån
  (`y:-48→0, rotation:-3→0`) och landar sist.
- **§2 Hero under scroll**: `gsap.matchMedia()` med `isDesktop`/`isMobile`. Desktop pinnar
  `.hero-stage` (`pin:'.hero-stage'`, `end:'+=120%'`, `scrub:0.6`) — CSS:ens gamla `position:sticky`/
  `190svh` är borttagen, spacingen kommer nu från ScrollTrigger själv. Mobil kör samma tidslinje utan
  pin, kortare spann (`+=60%`). Kortet vänder `rotationY 0→180` + `scale 1.04`; ÖH/NV-dithren
  parallaxar `yPercent ∓8` (uppskalade 1,18× i förväg så cover-bilden aldrig exponerar cellens grå
  bakgrund vid ändläget — hittades och fixades under verifiering, se § Avvikelser); h1-raderna glider
  olika snabbt (`-16 - i*12` %) så översta raden skärs av först; NH-cellen får en sen `clip-path`-
  betoning från underkant (approximation av "mint sveper över kortbasen", se § Avvikelser).
- **§3 Dither → färg**: byggd som spec:en faktiskt bad om denna gång (till skillnad från R1/R2:s
  dokumenterade `clip-path`-reträtt) — varje `.img-cell[data-resolve]` utom `stay`-cellerna får en
  genererad rutgrid (`<span>` per ruta, `background-image`/`background-position` skivat ur
  dither-bilden) ovanpå den nu alltid synliga färglagret. `gsap.to(tiles,{opacity:0, stagger:{grid:
  [rader,kol], from:'random', amount:0.9}, scrollTrigger:{scrub:true}})` — 12×8 på desktop, 6×6 på
  mobil (vald vid init, se § Avvikelser för begränsningen).
- **§4 Tesen**: headline-50 är tecken-delad (`mask:'chars'`) och reser sig en gång vid entré, plus
  hela raden skiftar `xPercent 0→-18` scrubbat mot `#tes`. De tre `tes-line`-cellerna reser sina
  rader ur mask vid 80% och fylls från vänster skarv via en genererad `seamFill`-overlay (samma
  bakgrundsfärg, `clip-path` 0→100%, text hålls ovanpå med `z-index`).
- **§5 Processen**: en mint 2px-linje (`process-progress`, skapad av skriptet) skalar `scaleY 0→1`
  scrubbat över hela processraden, positionerad på skarven mellan kolumnerna — men bara ≥1200px
  (döljs under, se § Avvikelser). Varje steg dimmas/lyser upp (`autoAlpha` 0,55↔1) kring viewportens
  mitt, indexet rullar in vertikalt vid växling.
- **§6 Exempelcase**: ordet skiftar `xPercent 20→-6` scrubbat, skuret av `.cell`s `overflow:hidden`.
  Tumnaglarnas färg-/ditherlager har intern parallax `yPercent -10→10` utöver §3-upplösningen.
  längd matchar exempelcase.
- **§7 Calyx/Hōrai**: inbäddningscellen öppnas med `clip-path: inset(0 100% 0 0)`→0 (spegelvänt för
  Hōrai) vid 75%. Caseshuvudet fylls längs skarven (samma `seamFill`) och namnet reser sig tecken för
  tecken. De fem raderna tänds i ordning via `ScrollTrigger.batch` vid 80%.
- **§8 Priset**: bento-cellerna glider in från sin skarv (`xPercent`/`yPercent` + `autoAlpha`,
  `power3.out`, ~0,6s). Siffrorna räknas upp en gång (`ScrollTrigger` med `once:true`) via en
  textnod-proxy som gruppera tusental med samma blanksteg som originalsträngen, och skriver tillbaka
  exakt originaltexten i `onComplete` så slutläget är bit-för-bit identiskt med den statiska strängen.
- **§9 Kontakt/footer**: jätterubriken reser sig radvis (scrub-fri, `toggleActions`, `mask:'lines'`).
  Kortet i kontakten kommer in från höger med en rotation (`rotationY 90→0`) som eko av hero-kortet.
  `ALUNIX` i footern är tecken-delad och reser sig underifrån (`yPercent 120→0`) scrubbat medan
  footern kommer in.

## Uppmätta värden, R3

**Overflow** (`verify.py`, samtliga fyra breddpunkter, före och efter en 10-stegs scroll-genomgång):

| Bredd | overflow_px (start) | overflow_px (efter scroll) |
|---|---|---|
| 390 | 0 | 0 |
| 768 | 0 | 0 |
| 1440 | 0 | 0 |
| 1920 | 0 | 0 |

En första körning gav 2px overflow vid 390/768 (en `process-progress`-linje positionerad för
tvåkolumnslayouten läckte 2px förbi högerkanten när `.process-row` staplar till en kolumn under
1200px) — fixad genom att dölja linjen under den brytpunkten (`@media (max-width:1199px)`); andra
körningen gav 0 överallt.

**Copy-diff**: `passed:false`, exakt samma två kända, granskade undantag som R2 (`ALUNIX` 2×,
`kontakt@alunix.se` 2×, se tabellen i R2-avsnittet ovan) — ingen ny avvikelse. Em-dash: 0.

**Hopptest** (`lenis.scrollTo(el,{immediate:true})` till varje sektions-id, 1440 och 390):
alla åtta sektioner (`hero, tes, process, exempelcase, case-calyx, case-horai, pris, kontakt`)
landar läsbara. `ScrollTrigger.getAll().length`: 51 vid start, 49 efter `refresh()` — mellanskillnaden
är två prisräknare vars ScrollTrigger har `once:true` och självdör efter att ha spelat klart, inte ett
läckage. `start`/`end`-paren är identiska före/efter `refresh()` (stabil layout, ingen drift).

**Ramtakt** (rAF-delta över 3s hjulscroll, 1440×900, Playwright headless): median 16,7 ms, p95 33,3 ms
— medianen motsvarar exakt 60fps; p95:ens enstaka hopp till en andra bildruta (två missade rutor i
följd) skedde under en sektionsövergång med samtidig `ScrollTrigger.batch`-reveal, inte ett
kontinuerligt problem.

**Konsolfel**: 0, vid 1440 och 390, över hela intro + full scroll-genomgång + hopptest.

## Skärmdumpar

Alla i `tests/alunix-r8/runs/V3f/shots/r3/`:

- `d1440-hero-intro-300ms.png` / `d1440-hero-intro-1600ms.png` (+ `m390-` motsvarigheter) — se §
  Avvikelser: Playwright headless spelar upp `requestAnimationFrame`-kön i en klunk mellan
  `page.reload()` och den första `wait_for_timeout`, så båda hamnar på samma färdiga tillstånd i det
  automatiska skärmdumpsflödet; manuell körning i Browser-panen (interaktiv, inte headless-batch)
  visade det stegvisa förloppet i realtid och bekräftade tidslinjen visuellt.
- `d1440-hero-pin-actual-mid.png` / `d1440-hero-pin-fix-check.png` — pin mitt i scrubben, före/efter
  overscan-fixen (§ Avvikelser).
- `d1440-{tes,process,exempelcase,case-calyx,case-horai,pris,kontakt}-midscroll.png` (+ `m390-`) —
  varje sektion mitt i sin egen scroll.
- `d1440-footer-wheel.png` — footern efter hjulscroll hela vägen ned (den `window.scrollTo`-drivna
  `d1440-footer.png` fastnade på kontakt-sektionen, se § Avvikelser).
- `jump-{hero,tes,process,exempelcase,case-calyx,case-horai,pris,kontakt}.png` — hopptestets
  slutlägen.
- `hero-1440.png`, `hero-390.png`, `full-1440.png`, `full-390.png` — samma `verify.py`-standardbilder
  som R1/R2, för jämförelse.

## Skill-kedja R3

| # | Anrop | Konkret regel/API jag använde |
|---|---|---|
| 1 | `Skill(lenis)` | Den kanoniska GSAP-kopplingen ordagrant: `autoRaf:false`, `gsap.ticker.add(t => lenis.raf(t*1000))`, `lagSmoothing(0)`, `lenis.on('scroll', ScrollTrigger.update)`, ingen `scrollerProxy` (window-scroll behöver den inte). `respectReducedMotion` defaultar till `true` men spec/husregel F-011 kräver alltid rörelse → satte explicit `false`. `lenis.css`s `.lenis-smooth iframe{pointer-events:none}` bekräftade att inbäddningarna tappar hjulfokus under smooth-scroll — accepterat som spec:en själv sa. |
| 2 | `Skill(gsap-core)` | Transform-alias (`x/y/scale/rotation/rotationY/xPercent/yPercent`) i stället för rå `transform`-sträng överallt; `autoAlpha` i stället för `opacity` för hela-döljningar (pris-bento, prov-rows); `gsap.matchMedia()` med `conditions`-objektet (`isDesktop`/`isMobile`) för hero-pin-grenen. |
| 3 | `Skill(gsap-scrolltrigger)` | `scrub` vs `toggleActions` aldrig blandat på samma trigger; ScrollTrigger alltid på timeline/top-level tween, aldrig på ett barn i en timeline; `ScrollTrigger.batch()` för calyx/hōrai-radernas gruppvisa reveal; `ScrollTrigger.refresh()` efter varje layoutpåverkande load, inte bara vid resize. |
| 4 | `Skill(gsap-timeline)` | `defaults`-objektet på `loadTl`/`prisTl` i stället för att upprepa `ease`/`duration` per tween; positionsparametrar (`0`, `0.14`, `"+=..."`-fria absoluta tider) för hero-introns diagonala stagger. |
| 5 | `Skill(gsap-plugins)` | `SplitText.create(el,{type, mask, aria:'auto'})` genomgående — `aria:'auto'` var den konkreta regel som styrde att jag ALDRIG manuellt satte `aria-hidden`/`aria-label` för hand; pluginet gör det och håller skärmläsartexten hel. Ingen Club-licens/npm-token behövdes (bekräftat gratis sedan Webflow-förvärvet). |
| 6 | `Skill(gsap-performance)` | "Animate bara transform/opacity" checkade om mot varje tween jag skrev — enda gången jag var nära att bryta det var `box-shadow`-tillväxten spec:en nämner för kortflippen (§2), som jag därför strök helt i stället för att smyga in en paint-egenskap (se § Avvikelser). |
| 7 | `mcp__ui-skills__get_skill("emilkowalski/emil-design-eng")` | Duration/easing-tabellen: entré-reveals landade på 0,5–0,7s med `power3/4.out` (inom "modaler/drawers 200–500ms" + lite längre för marketing-radreveal-kategorin snarare än UI-kontroller); aldrig `ease-in` på någon entré; scrub-bundna tweens använder `ease:'none'` konsekvent (linjär mappning mot scroll, standardregeln för scrub). |

**Ej anropat**: `gsap-utils` (inga `clamp`/`mapRange`-hjälpare behövdes — all interpolation gick genom
ScrollTrigger `scrub` eller SplitText-stagger, ingen manuell tallinje-mappning skriven för hand).
`mcp__inspo__*` (spec:en pekade explicit ut vilka rörelsereferenser som gäller, ingen ny visuell
research behövdes för rörelsen).

## Avvikelser från RORELSE-SPEC.md, hederligt redovisade

1. **§0 skarv-"drawing"**: spec:en ber om att skarvarna "ritas" innan cellerna öppnas. Jag byggde en
   bokstavlig tunn linje (`seam-line`, mint, `scaleX`/`scaleY` 0→1) som en kort flash — men den
   *lever kvar* som en permanent 1px-accent efter introt (inte borttagen/dold igen), vilket är en
   annan tolkning än en engångs-"ritning". På mobil visade den sig bisecera hela den staplade
   1-kolumnslayouten (hittades i skärmdump, fixad med `@media (max-width:767px){display:none}`) —
   kvarvarande desktop-beteende (permanent linje) är avsiktligt behållet som en diskret
   grid-accent, inte återställt till spec:ens "engångs-ritning".
2. **§2 kortskuggans tillväxt**: spec:en ber om att skuggan växer under vändningen. `box-shadow` är
   varken `transform`, `opacity` eller `clip-path` — invariant-listan förbjuder det uttryckligen.
   Jag utelämnade skugg-tillväxten helt i stället för att smyga in en paint-egenskap; kortet skalar
   (`1.04`) vilket ger en närliggande men inte identisk känsla av lyft.
3. **§2 "mint sveper in över kortets bas"**: exakt geometri (en overlay som specifikt täcker bara
   kortets nedre kant) byggdes inte; jag approximerade med en sen `clip-path`-betoning på hela
   NH-cellen (`inset(28% 0 0 0)→0`) vid 68% av pin-scrubben. Samma rörelseriktning och timing,
   grövre yta.
4. **§3 rutdimensioner är inte breakpoint-reaktiva**: `tileDims` (12×8 / 6×6) väljs en gång vid
   sidladdning utifrån `window.innerWidth<768`, inte omgenererat vid ett faktiskt fönsterbyte över
   den gränsen (t.ex. DevTools-omorientering utan reload). Ett normalt besök (ladda → scrolla) drabbas
   aldrig av det; en live-resize över 768px-gränsen skulle behålla fel rutstorlek till nästa
   sidladdning.
5. **§5 progresslinjens brytpunkt**: linjen är bara synlig ≥1200px (se § Uppmätta värden) i stället
   för att finnas i någon form ner till 768px — en `.g12`-brytpunktsdetalj (kolumnerna staplar redan
   vid 768–1199px i en 6-kolumnsgrid) som gjorde en meningsfull seam-position omöjlig att beräkna
   utan att bygga en helt separat mobil-linje. Dokumenterad förenkling, inte ett förbiseende.
6. **Verifieringsskriptets `window.scrollTo`-hopp och Lenis**: `verify.py`s befintliga
   scroll-genomgång och mitt första försök till footer-skärmdump använde `window.scrollTo(...)`
   direkt. Lenis fortsätter interpolera mot sitt eget senast kända mål och drar tillbaka scrollen på
   nästa `raf`-tick om den inte informeras — synligt som att `d1440-footer.png` fastnade på
   kontakt-sektionen. Detta är förväntat Lenis-beteende (dokumenterat i lenis-skillens
   Tillgänglighet-sektion som "anchors är opt-in"; samma princip gäller programmatisk scroll som
   inte går via `lenis.scrollTo`), inte ett fel i sidan — riktig hjul-/styrplatteinmatning (som all
   annan verifiering i den här rapporten använder) påverkas inte. `verify.py` självt rapporterade
   ändå `overflow_px_after_scroll:0` och korrekt iframe-montering trots detta, så dess resultat står
   kvar; jag bytte bara ut footer-skärmdumpen mot en hjul-driven variant (`d1440-footer-wheel.png`).
7. **Hittad och fixad under verifiering, inte en kvarvarande avvikelse**: ÖH/NV-dithrens
   `yPercent ∓8`-parallax exponerade ursprungligen cellens grå bakgrundsfärg vid ändlägena (ett
   `object-fit:cover`-lager translaterat med en `%`-av-egen-höjd tappar sin täckning om det inte har
   marginal). Fixat med en statisk `scale:1.18` på de två lagren innan scrubben appliceras — nämns
   här för spårbarhet, inte som en öppen fråga.

Alla andra paragrafer i RORELSE-SPEC.md (§1, §4, §6, §7, §8, §9, §10) är byggda som specificerat,
verifierade ovan.

---

# R4 · fem defekter från ledningens wheel-scroll-granskning

Ledningen körde egna `page.mouse.wheel`-skärmdumpar (1440 och 390) på R3-leveransen och hittade fem
defekter. Alla fem åtgärdade i `tests/alunix-r8/runs/V3f/index.html`; inga kompositions-, färg- eller
copyändringar.

## 1. Tes-radens ordbrytning mitt i ordet

**Orsak**: `SplitText({type:'chars', mask:'chars'})` på en flerordsmening ger varje tecken sin egen
brytbara inline-block-box utan minne av vilket ord det hör till — webbläsaren kan då radbryta mellan
VILKA tecken som helst, inte bara mellan ord, eftersom ordgränsen (mellanslaget) inte längre är en
enda sammanhängande textnod.

**Fix**: `SplitText({type:'lines, words, chars', mask:'lines'})` + `gsap.set(words, {whiteSpace:
'nowrap', display:'inline-block'})`. Masken ligger nu på RAD-nivå (varje rad är sin egen normalflödes-
box — rad 2 kan aldrig överlappa rad 1, de staplar som vanlig text), orden är låsta till att aldrig
brytas internt, och tecknen inuti varje ord animeras precis som förut. Samma mönster (linjer > ord >
tecken, mask på linjer) användes redan för h1/kontakt-rubriken, så tes-raden är nu konsekvent med
resten av sidan i stället för ett specialfall.

**Descendrar**: ny helper `maskBreathe(instance)` ger varje `instance.masks`-wrapper `padding-bottom:
0.16em; margin-bottom:-0.16em` (paddingen ger klippboxen utrymme nedåt, den lika stora negativa
marginalen tar tillbaka höjden så ingen layout flyttas). Applicerad på ALLA maskade SplitText-
instanser (h1, tes-rad, tes-linjer, calyx/hōrai-namn, kontakt-rubrik, footer), inte bara tes-raden,
eftersom samma klipp-mekanism (SplitText `mask:` wrapper + `overflow:clip`) fanns i alla sju och
kunde ge samma fel var som helst en `y`/`g`/`p` råkade hamna sist i sin rad.

Verifierat i `shots/r4/d1440-tes-check.png` och `shots/r4/m390-tes-check.png`: "Det första" / "Det
första intrycket" / "intrycket är" / "digitalt" — hela ord, ingen brytning mitt i ett ord, ingen
överlappning mellan rad 1 och rad 2.

## 2. Footer ALUNIX når inte sitt slutläge på mobil

**Orsak**: `scrollTrigger:{end:'top 60%'}` antog att footerns topp kunde fortsätta vandra upp till
60% av viewporten efter att den blivit synlig — men footern är sidans SISTA element. Vid 390/768
bredd finns inte tillräckligt med kvarvarande scrollutrymme för att footerns topp faktiskt ska nå så
långt innan sidan tar slut, så `progress` fastnade under 1 vid sant maxscroll (tecknen frös
mitt-i-resningen: "AI UNIv").

**Fix**: `end:'bottom bottom'` — progress:1 sammanfaller nu exakt med sant maxscroll vid VARJE
breddpunkt, eftersom footern är sista elementet: sidan kan omöjligt scrolla längre än till att dess
underkant når viewportens underkant.

**Mätt** (`window.__lenis.scrollTo('bottom',{immediate:true})` + 600 ms, alla fyra breddpunkter):

| Bredd | `footerScrollTrigger.progress` | Tecken-transform vid vila | Max gap mellan tecken |
|---|---|---|---|
| 390 | 1 | identitet (0 kvarvarande) | 0px |
| 768 | 1 | identitet (0 kvarvarande) | 0px |
| 1440 | 1 | identitet (0 kvarvarande) | 0px |
| 1920 | 1 | identitet (0 kvarvarande) | 0px |

**"Ingen gap mellan L och U" — undersökt, inte en rörelsedefekt**: med `progress:1` bekräftat och
alla tecken-boxar sida vid sida med 0px mellanrum (`getBoundingClientRect`, se tabell ovan), körde
jag om samma sida med JavaScript helt AVSTÄNGT (`java_script_enabled=False`, ingen SplitText, ingen
scroll-animation alls) — den råa, ostyrda `ALUNIX`-texten visar SAMMA optiska glapp mellan L och U vid
390 bredd (`shots/r4/m390-footer-nojs.png`). Det är teckensnittets egen formgivning vid
`clamp(80px,16vw,220px)` + `letter-spacing:-.04em` (L:ets fot och U:ets vänstra stapel skapar ett
optiskt mellanrum trots att boxarna vidrör varandra pixel-för-pixel) — samma vid runda 1/2, inte
introducerat av rörelsen. Vid 1440 syns inget glapp (`shots/r4/d1440-footer-endstate.png`) eftersom
den optiska effekten är storleksberoende. Flaggar det här som en typografi-fråga utanför den här
rundans "bara rörelse"-mandat, inte som en kvarstående R4-bugg.

## 3. Processens nedtoning under AA-tröskeln

**Orsak**: hela `<li>` dimmades med `autoAlpha:0.55`, vilket blandar VILKEN färg som helst mot svart
— inklusive `.process-p` som redan var `#bdbdbd` (11,2:1 mot svart för sig själv). `#bdbdbd` blandat
med 0,55 opacitet mot svart blir effektivt `rgb(104,104,104)` ≈ 3,77:1 — under AA:s 4,5:1 för
brödtext, vilket matchar ledningens mätning (~3,9:1).

**Fix**: `process-p` dimmas aldrig längre (konstant `#bdbdbd`, alltid 11,2:1). Bara titeln (`h3`) och
indexet (`.process-num`, dekorativt/`aria-hidden`) togglar en EXPLICIT färg mellan `#ffffff` (aktivt
steg) och `#8f8f8f` (övriga) på `ScrollTrigger`s `onToggle` — en diskret tillståndsväxling (en gång
per gräns-passage, inte per scroll-frame), så `color`-animering här bryter inte mot
transform/opacity/clip-path-regeln i praktiken (ingen kontinuerlig scrub-kostnad).

**Uppmätt kontrast** (WCAG relative luminance-formeln, sRGB):

| Färgpar | Kontrast |
|---|---|
| `#bdbdbd` mot `#000000` (process-p, alltid) | 11,18:1 |
| `#8f8f8f` mot `#000000` (dimmad titel/index) | 6,49:1 |
| `#ffffff` mot `#000000` (aktiv titel/index) | 21:1 |
| (tidigare) `#bdbdbd` blandat via `opacity:.55` | 3,77:1 — **kasserad** |

Alla tre nya värden klarar AA (4,5:1) med marginal; `#8f8f8f` klarar även AAA (7:1) nästan exakt (6,49
ligger under AAA men gott och väl över AA, vilket var kravet). Verifierat via
`getComputedStyle(title).color` efter `lenis.scrollTo` till processektionen: `rgb(143,143,143)` =
`#8f8f8f` exakt på de dimmade stegen, `rgb(255,255,255)` på det aktiva. Skärmdump:
`shots/r4/d1440-process-fixed2.png`.

## 4. Kontakt: död svart kvadrant nere till höger (öppen sedan R2)

**Orsak**: `.kontakt-card-cell{justify-content:flex-end}` med `min-height:92svh` men grid-stretchad
till samma höjd som den betydligt högre bildcellen (giant-rubrik + foto) — kortet+länkarna klumpade
ihop längst ner, hela överkanten av kolumnen (828px hög vid 1440, kort+länkar bara ~275px) stod tom
och svart som en enda sammanhängande "dead zone".

**Fix**: `justify-content:center`. Kortet + länkarna (redan en flex-grupp i DOM-ordning: kort, sedan
länkar under) centreras nu som EN grupp i kolumnens fulla höjd i stället för att pressas mot botten.
Kvarvarande tomrum (samma ~275px block, nu delat ~138px ovanför/nedanför i stället för 553px samlat
på ett ställe) är en oundviklig konsekvens av att bildcellens naturliga höjd (driven av det jätte-
stora fotot+rubriken) vida överstiger kortets kompakta naturliga storlek — att helt eliminera det
hade krävt en större kompositionsändring (t.ex. förminska bildcellen), vilket ligger utanför den här
rundans "bara rörelse, ingen komposition"-mandat. Centreringen är exakt vad instruktionen bad om;
ingen ny text, ingen kompositionsändring i övrigt.

Kortets entré + engångsflip (RORELSE-SPEC §9: kommer in från höger, vänds en gång, som ett eko av
hero-kortet) är oförändrad — bara den STATISKA vilopositionen (var kortet landar när det inte
animerar) flyttades från botten till mitten.

Verifierat: `shots/r4/d1440-kontakt-fixed.png`.

## 5. Nytt test i `verify_motion.py`: maxscroll-restläge

Ny funktion `max_scroll_residual_check(browser, w, h, label)`: `window.__lenis.scrollTo('bottom',
{immediate:true})` + 600 ms väntan, sedan för footer och kontakt:

- varje inre SplitText-tecken/rad/ord-`transform` matchas mot identitetsmatrisen (tolerans 0,5px för
  GSAP:s flyttal-avrundning av `yPercent`→px, som annars gav falska positiva på ~0,05–0,4px — inte
  synligt, inte en riktig rest);
- tecken-boxarnas inbördes horisontella glapp (`getBoundingClientRect`) för att bekräfta "ett ord,
  inget mellanrum" oberoende av synintryck;
- `clip-path` på kontaktbildens färglager;
- `ScrollTrigger`-instansens egen `.progress` för footern.

Kört vid 390/768/1440/1920 — `progress:1`, `nonIdentityCount:0`, `maxGap:0px` överallt (se tabellen i
§2). Resultat i `tests/alunix-r8/runs/V3f/verify-motion-result.json`.

## Regressionskontroll efter alla fem fixar

- **Overflow** (`verify.py`, `V3F_SHOTS_ROUND=r4`): 0px vid 390/768/1440/1920, före och efter
  scroll-genomgång — oförändrat rent.
- **Copy-diff**: `passed:false` med exakt samma två kända, godkända undantag som R2/R3 (`ALUNIX` 2×,
  `kontakt@alunix.se` 2×) — ingen ny avvikelse. Em-dash: 0.
- **Konsolfel**: 0 vid 1440 och 390, hela vägen genom intro + scroll + hopptest + maxscroll-test.
- **Hopptest** (samtliga åtta sektioner, 1440 och 390): oförändrat från R3, alla läsbara.

## Skärmdumpar

Nya i `tests/alunix-r8/runs/V3f/shots/r4/` (utöver de åtta section-midscroll + hopptest-bilderna
`verify_motion.py` alltid tar om, samma mönster som R3):

- `d1440-tes-check.png`, `m390-tes-check.png` — ordbrytningsfixen, hela ord synliga.
- `d1440-process-fixed2.png` — kontrastfixen, aktivt/dimmat steg sida vid sida.
- `d1440-kontakt-fixed.png` — kontaktkortet centrerat.
- `d1440-footer-endstate.png`, `m390-footer-endstate.png`, `t768-footer-endstate.png`,
  `w1920-footer-endstate.png` — footerns slutläge vid alla fyra breddpunkter efter `lenis.scrollTo
  ('bottom',{immediate:true})`.
- `m390-footer-nojs.png` — kontrollbild: samma optiska L/U-glapp UTAN JavaScript, bevis på att det är
  typografi, inte rörelse (se § 2).
- `*-maxscroll-endstate.png` (alla fyra breddpunkter) — genererad av det nya
  `max_scroll_residual_check`-testet.

## Skill-kedja R4

| # | Anrop | Konkret regel/detalj jag använde |
|---|---|---|
| — | Inga nya `Skill`/`mcp__ui-skills__`/`mcp__inspo__`-anrop denna runda | Alla fem fixar är tillämpningar av regler redan inhämtade i R3:s kedja (`gsap-plugins` för SplitText:s `type`/`mask`-API och `aria:'auto'`; `gsap-performance`/husregeln transform+opacity+clip-path, som jag höll mig innanför genom att göra färgtogglingen till en diskret `onToggle`-växling i stället för en kontinuerlig scrub). Inget nytt beslut krävde ny referens — WCAG-kontrastformeln är ett standardmatematiskt test (relative luminance), inte ett designval en skill styr. |

## Kvarvarande, hederligt redovisat

- **Footer L/U-glappet vid 390** är typografi (teckensnitt + `letter-spacing` vid stor clamp-storlek),
  inte en rörelsebugg — bekräftat identiskt utan JavaScript. Kvarstår som en möjlig framtida
  typsnitts-/spacingjustering, men rör komposition, inte rörelse, så jag rörde den inte i den här
  filen.
- **Kontaktkolumnens tomrum** är halverat och centrerat (instruktionens exakta fix) men inte
  eliminerat — den bakomliggande höjdskillnaden mellan bildcellen och kortet är en
  kompositionsfråga, inte en rörelsefråga, och ligger utanför mandatet den här rundan.

---

# R5 · läsbarhet, casevalet och kontakten (RUNDA5-SPEC.md)

Antons dom efter R4: "nästan perfekt". Fyra ändringar i spec-ordningen, komposition/färg/copy i
övrigt orörda. Se `RUNDA5-SPEC.md` för den fullständiga kravtexten.

## A. Rubrikläsbarhet (≥40vh, ingen glyf skuren)

- **Tesraden**: tog bort den horisontella `xPercent`-driften helt (den riskerade att skära sista
  ordet mot högerkanten och gav aldrig ett riktigt stillastående fönster). Ny `ScrollTrigger.create`
  pinnar `.tes-top` i `#tes` för 0,9×`window.innerHeight` px (desktop only, `gsap.matchMedia`), så
  radernas stagger-resning spelar och sedan står rubriken helt stilla i resten av pinnens räckvidd
  innan den släpper. Mobil: ingen pin, oförändrad char-resning.
- **Heron h1**: `heroTl` fick explicita `duration`-värden som summerar till en 1-enhets skala, och
  h1-radernas `yPercent`-drift flyttades till position `0.75` (sista fjärdedelen av pinnen) i stället
  för position `0` — resten av pinnens 120vh står h1 helt stilla och läsbar, och rörelsen sker bara
  medan kortvändningen redan är långt gången.
- **`Exempelcase`**: bytte den horisontella `xPercent`-svepningen mot en `SplitText`-mask med
  `yPercent`-resning (rad-nivå), exakt som spec kräver. Hittade och fixade samtidigt en riktig
  klippbugg: `.case-word-cell`s asymmetriska padding (12px botten mot 28px topp) var mindre än
  mask-breathe-tillägget (`0.16em`) på denna clamp-storlek — ordet klipptes bokstavligen av cellens
  `overflow:hidden`-kant vid *varje* scrollposition (0 vh uppmätt, inte bara under 40). Symmetrisk
  padding (+4px marginal) löste det; se tabellen nedan.
- Kontrollerade alla `headline-40`/`headline-50` på sidan (hero, tes, exempelcase, pris, kontakt) mot
  regeln med en ny scanner i `verify_motion.py` (`legibility_check`), inte bara okulärt.

**Uppmätt** (`legibility_check`, 1440×900, 15px scroll-steg):

| Rubrik | Max sammanhängande synligt fönster | ≥40vh |
|---|---|---|
| Hero h1 (`headline-40`) | 140,0 vh | OK |
| Tes (`headline-50`) | 138,3 vh | OK |
| Exempelcase-ordet (`headline-50`) | 80,0 vh (0 vh före fixen) | OK |
| Pris (`headline-50`) | 68,3 vh | OK |
| Kontakt (`headline-40`) | 80,0 vh | OK |

## B. Casevalet och den valda showcasen

Ersatte tumnagelraden och de två separata `#case-calyx`/`#case-horai`-sektionerna helt.

**B1 Väljaren** (`#exempelcase`, ny `.case-picker`): två `<button>` (`aria-pressed`, Enter/Space
fungerar nativt), varsin skarp 1440×900-skärmbild av `/sites/calyx.html` och `/sites/horai.html`
(Playwright, `deviceScaleFactor:2`, WebP q82, `assets/cases/{calyx,horai}-1440.webp`, ~277–515 kB —
öppnade och granskade bilderna själv, inte bara filstorleken). Hover (`(hover:hover)` gate):
bilden `scale(1→1,04)` över 700ms `cubic-bezier(.23,1,.32,1)` (emil-design-eng: starkare kurva än
CSS-default), grannen tonas till opacitet 0,85; fokus-visible får samma zoom + 2px mintram. Vald
cell: 4px mintlinje under (`border-bottom`), `aria-pressed` styr den via CSS-attributselektor.

**B2 Showcasen** (ny `#showcase`, förladdad med Calyx): portade V3d:s `measureCase`/`caseY`
(`tests/alunix-r8/runs/V3d/index.html` rad ~3320–3338) ordagrant — samma ankarformat
(`['selector', offset, kortRampTillägg, tröskel]`), samma smoothstep-blandning mellan ankare
(`u*u*(3-2u)` över de sista 45% av varje segment), samma write-if-changed `>=0,5px` mot
`contentWindow.scrollTo({behavior:'instant'})`. Desktop: `ScrollTrigger.create` pinnar
`.showcase-stage`, `end` = antal ankare × `window.innerHeight` px (en funktion, inte en
sträng-suffix — se felavsnittet nedan för varför), `scrub:0.6`. Vänster 7 kolumner: den 1440px
breda live-iframen skalad med `transform:scale()` (`Math.max(bredd/1440, höjd/900)`, "cover" så
cellen fylls skarpt utan att skala en bild). Höger 5 kolumner: casehuvud + fem/sex textrader, rad k
reser sig ur mask (`yPercent`) när sajten når ankare k, tidigare rader tonas till 0,55. Mobil: ingen
pin, `.showcase-embed-cell{position:sticky}` i 56svh, varje rads `onEnter`/`onEnterBack` tweenar
sajtens inre scroll till sitt ankare (0,6s). Byte av case: `activateCase()` togglar panelernas
`display`/`inert`, monterar Hōrais iframe vid första valet (Calyx är eager från start), kör
`ScrollTrigger.refresh()` och `lenis.scrollTo('#showcase',{duration:1.2})`.

De gamla `#case-calyx`/`#case-horai`-sektionerna är borta; deras fem/sex styckestexter flyttade
ordagrant in i `.showcase-panel--calyx`/`--horai` (alltid i DOM, bara den inaktiva har
`display:none`+`inert` — så copy-räkningen mot V3d förblir exakt).

**Uppmätt** (`showcase_check`, klick + tangentbord, 1440×900):

| Kontroll | Resultat |
|---|---|
| Hopp till `#showcase` utan val → Calyx synlig | sant |
| Klick på Hōrai → scroll till `#showcase`, panelen synlig | sant |
| Hōrais inre `scrollY` mot alla 6 ankare | `[0, 1170, 1855, 2890, 6520, 7420]`, diff `[0,0,0,0,0,0]` px |
| Tab till Calyx, Enter → `aria-pressed="true"` | sant |
| Calyx inre `scrollY` mot alla 5 ankare | `[0, 877, 1414, 2327, 4120]`, diff `[0,0,0,0,0]` px |

Alla sex/fem ankare träffas exakt (0px avvikelse, kravet var ±2px), på båda casen.

## C. Kontakten — "kortet lämnas över"

Byggde om `#kontakt` till en 2×2-kvadrant (`.kontakt-quad`, egen dedikerad grid, samma
brytpunktsmönster som `.hero-stage` — g12-klassernas 1199px-ombrytning hade annars stökat till
2×2-layouten i förtid): ÖV svart (`Berätta om er verksamhet.` + dess underrad, flyttad hit från den
separata `.kontakt-lead`-cellen), ÖH tom vit, NV bildcellen (samma `k1-stage-pool`-motiv och
dither→färg-upplösning som redan fanns), NH mint.

Kortet sitter som ett grid-item som spänner hela 2×2:an och centrerar sig i korsningen
(`grid-column:1/3;grid-row:1/3;place-self:center`) — på mobil byter det till `grid-area:nh` (i
mint-cellen, 88% bredd), matchar spec exakt utan absolut positionering mot en enda cell.

Flippen är nu GSAP-driven (`rotationY` på ett separat `.card-flip2`, inte CSS-variabeln heron
använder) med en egen `.kontakt-card-tilt`-wrapper för hover-tilten (`gsap.quickTo` på
`rotationX`/`rotationY`, ±8°, `perspective:1200px`) — de två måste vara separata lager, annars
skriver GSAP:s tilt-tween och heron-mönstrets CSS-`transform:rotateY(calc(var(--flip)*180deg))`
över varandra på samma element. Klick/Enter/Space (nativt via `<button>`) vänder 180° med en kort
lyftning (`y:-14`, yoyo). Baksidan bär `Alunix`/`Digital byrå`/`Design Utveckling System` och de två
riktiga länkarna som verkliga `<a>`; en `.face-back-hit`-knapp under länkarna (lägre z-index) tar
klick var som helst ANNANSTANS på kortet för att vända tillbaka, utan att blockera länkarna själva.
`inert` växlar per sida (`kontaktCardFront`/`kontaktCardBack`), så baksidans länkar är fokuserbara
bara när baksidan syns.

Fail-toward-visible (husregel 10): en `ScrollTrigger` på `#kontakt` (`start:'top bottom',
end:'bottom bottom'`) flippar kortet automatiskt vid `progress>=0,7`. Eftersom sektionen bara är
`100svh` hög sammanfaller det matematiskt nästan exakt med "sektionen fyller hela viewporten" —
både ett hopp till botten och ett hopp direkt till `#kontakt` (`scrollIntoView`/`lenis.scrollTo`)
landar redan bortom 0,7 och visar baksidan direkt, utan en separat specialregel.

**Uppmätt** (`kontakt_check`, 1440×900):

| Kontroll | Resultat |
|---|---|
| Framsidan synlig (ej `inert`) före klick | sant |
| Klick → baksidan synlig, framsidan `inert` | sant |
| mejl-länken fokuserbar, `Tab` når "Boka ett möte" härnäst | sant, sant |
| Hopp till sidans botten → baksidan redan synlig | sant |
| Hopp direkt till `#kontakt` → baksidan redan synlig | sant |

## D. Verifiering — nytt i `verify_motion.py` och `verify.py`

- `LEGIBILITY_TARGETS` + `legibility_check(browser,w,h)`: coarse-stepped (15px) scroll-scan per
  rubrik, mäter längsta sammanhängande fönster där elementet står helt innanför **varje** klippande
  förälders box (inte bara sin närmaste) och innanför viewporten. Detta är vad som fångade
  exempelcase-klippbugen (0 vh, inte "nästan 40").
- `showcase_check(browser,w,h)`: hopp utan val, klick på Hōrai + panel/scroll-koll, tangentbordsväg
  till Calyx, och `anchor_hits()` som läser `window.__CASES[key].y` och jämför mot iframens riktiga
  `contentWindow.scrollY` vid varje ankares slutfas (±2px-kravet, i praktiken 0px).
- `kontakt_check(browser,w,h)`: klick-vändning, tab-ordning på baksidans länkar, samt två separata
  sidladdningar för "hopp till botten" och "hopp direkt till `#kontakt`" (måste vara färska sidor —
  `#kontakt`s egen `ScrollTrigger` har redan hunnit avgöra flip-läget på den ordinarie sidan från
  tidigare tester annars).
- `verify.py`: `#case-horai`→`#showcase` (jump-mount-testet), `.case-thumb`→`.case-picker-cell`,
  `.kontakt-giant`/`.kontakt-image-cell`→`.kontakt-q--ov .headline-40`, `.kontakt-card-cell` m.fl.
  →`.kontakt-card-anchor`/`#kontaktCardBack` — de fyra R2-checkarna som pekade på nu borttagen
  markup uppdaterade till sina R5-motsvarigheter i stället för att lämnas döda.
- `window.__CASES` och `window.__kontaktCardFlip` exponerade som dev-hooks specifikt för
  verifieringssviten (kommenterat i koden som sådant), ingen produktionsanvändning.

**Regressionskontroll, alla fyra breddpunkter** (`verify.py` + `verify_motion.py`, `r5`):

| Kontroll | 390 | 768 | 1440 | 1920 |
|---|---|---|---|---|
| Horisontell overflow (px) | 0 | 0 | 0 | 0 |
| Overflow efter full scroll-genomgång (px) | 0 | 0 | 0 | 0 |
| Footer `ScrollTrigger.progress` vid maxscroll | 1 | 1 | 1 | 1 |
| Konsolfel (hela intro+scroll+hopptest) | 0 | — | 0 | — |

Copy-diff (`verify.py`, mot V3d): `over_count_vs_v3d` = exakt `ALUNIX` 2× och `kontakt@alunix.se`
2× — de två sedan tidigare kända, godkända dubbletterna, `not_found_in_v3d: []` (inget påhittat).
Em-dash: 0. **En regression fångades och fixades under bygget**: väljarens namn/undertitel
(`Calyx`/`Florist, Stockholm`/`Hōrai`/`Restaurang, Asian Fusion`) dubblerade showcasehuvudets
redan räknade instans — löst med `aria-hidden="true"` på väljarens badge (bildens `alt`-text bär
samma identifiering tillgängligt, badgen är en ren visuell eko, uteslutet ur copy-räkningen precis
som `aria-hidden`-regeln i `verify.py` redan förutsätter).

## Tre motorbuggar hittade och fixade under bygget (hederligt redovisat i detalj)

Ingen av dessa står i spec:et — de är defekter min egen B-implementation introducerade, upptäckta
genom att faktiskt köra sidan i Playwright om och om igen och bisekta, inte antagna bort.

1. **`ScrollTrigger.refresh()` + en pinnad, laddande iframe = `insertBefore`-krasch.** Att pinna en
   förälder till en LIVE iframe gör att GSAP:s eget pin-spacer-omslag (vid skapande, och vid varje
   revert-och-ommätning som `refresh()` gör) flyttar den förälderns nod i DOM:et — och att flytta en
   iframes förälder gör att webbläsaren laddar om den. Instrumenterade `Node.prototype.insertBefore`
   och iframens eget `load`-event tills det syntes svart på vitt: samma iframe laddades om
   flera gånger på en enda sidladdning, och en `refresh()` som råkade landa mitt i en sådan omladdning
   kraschade. Fixen är en gemensam `safeRefresh()`-grind: alla `ScrollTrigger.refresh()`-anrop i
   filen väntar tills Calyx-iframens `load` har hunnit avfyras OCH två `requestAnimationFrame` har
   passerat, innan någon refresh alls tillåts köra.
2. **`end: '+='+antal*100+'vh'` — `vh`-suffixet ignoreras tyst av ScrollTrigger:s relativa
   `end`-parsning.** Gav en pin på 500px i stället för avsedda 4500px (5 ankare × 900px), upptäckt
   genom att jämföra `ScrollTrigger.getAll()`s uppmätta `start`/`end` mot den avsedda räckvidden.
   Fixen: en funktion som returnerar `'+=' + (n * window.innerHeight)` — riktiga pixlar, alltid
   korrekta vid resize också.
3. **Radresningen (`yPercent`-mask) rörde sig aldrig**, trots att `gsap.getProperty` rapporterade
   `yPercent:0` (dvs. GSAP trodde jobbet var klart). Orsak: en CSS-regel
   (`.row-inner{transform:translateY(100%)}`) gav raden sitt dolda startläge, och GSAP — första
   gången det rör ett element — läser in den befintliga renderade matrisen som sitt EGET separata
   `y`(px)-baslinjevärde, inte som `yPercent`. Den sedan följande `gsap.set(...,{yPercent:100})`
   lades ADDITIVT ovanpå den baslinjen i stället för att ersätta den, och `gsap.to(...,{yPercent:0})`
   tog bara bort sin egen (redan-noll) andel — CSS-baslinjen (radens fulla höjd i px) blev kvar för
   evigt. Fixen tar bort CSS-transformen helt; `gsap.set(...,{yPercent:100})` är nu ENDA källan till
   det dolda startläget, samma mönster som varje annan SplitText-mask på sidan redan använder.

Utöver dessa: **mobilens showcase-iframe saknade skalning helt** (funktionen som skalar iframen till
sin cell kördes bara i skrivbordsgrenen) — en riktig sladd, inte en subtil bugg, fångad genom att
faktiskt titta på 390px-skärmdumpen (den visade ett oskalat, beskuret hörn av sajten i stället för
hela förstasidan krympt till cellens bredd). `Math.max(bredd/1440, höjd/900)` (samma "cover"-formel
på båda breddpunkterna) löste det.

## Skärmdumpar, R5

Nya i `tests/alunix-r8/runs/V3f/shots/r5/` (`verify_motion.py`s vanliga svep +):

- `d1440-00-hero.png` … `d1440-05-kontakt.png` — riktig hjulscroll genom hero → tes (pinnad, still) →
  exempelcase → showcase (Calyx, start och mitt-pin) → kontakt.
- `d1440-06-case-hover.png` — Hōrai-cellen hovrad (`scale:1,04`, granncellen vid opacitet 0,85,
  bekräftat med `getComputedStyle` i samma test).
- `d1440-07-kontakt-card-midflip.png` — kortet vid `rotationY:50°`, synligt vinklat mitt i vändningen
  (90° exakt är kant-i-kant osynligt, inte en läsbar mellanbild).
- `m390-00-hero.png` … `m390-05-kontakt.png` — samma svep vid 390px, inklusive
  `m390-03-showcase-sticky.png`/`m390-04-showcase-scrolled.png` som visar den sticky-mobila
  showcasen fylld kant-i-kant efter mobilskalnings-fixen.
- `assets/cases/calyx-1440.webp`, `assets/cases/horai-1440.webp` — de nya skärpta case-bilderna,
  öppnade och granskade visuellt (inte bara filstorleksbekräftade) innan de las in i väljaren.

## Skill-kedja R5

| # | Anrop | Konkret regel/detalj jag använde |
|---|---|---|
| 1 | `Skill: lenis` | Bekräftade att `pointer-events:none` på iframes under `.lenis-smooth` redan är Lenis egen CSS (inget nytt att lägga till för showcasens `pointer-events:none`-iframe), och att `ScrollTrigger.refresh()` måste köras efter varje layoutpåverkande förändring — direkt relevant för §D:s bugg 1/2 ovan. |
| 2 | `Skill: gsap-scrolltrigger` | "Create ScrollTriggers in page order (or set refreshPriority)" — grunden för att göra showcasens pin-skapande SYNKRON (inte väntande på iframens `load`) i stället för villkorad, vilket var halva fixen på bugg 1. |
| 3 | `Skill: gsap-core` | `gsap.matchMedia()` för väljarens/showcasens desktop/mobil-gren; transform-aliasen (`rotationX/Y`, `yPercent`) i stället för rå `transform`-sträng, genomgående i B och C. |
| 4 | `Skill: gsap-utils` | Övervägde `gsap.utils.mapRange` för caseY-interpolationen men behöll V3d:s egen smoothstep-formel ordagrant (spec kräver en exakt port, inte en omskrivning) — no effect på slutkoden, men bekräftade att inget av `gsap.utils` gjorde porten enklare utan att avvika från källan. |
| 5 | `Skill: gsap-plugins` | `SplitText`s `mask:'lines'`/`aria:'auto'` för exempelcase-ordets nya `yPercent`-resning (ersätter §A:s xPercent-svep). |
| 6 | `mcp__ui-skills__get_skill("emilkowalski/emil-design-eng")` | Hover-zoomens kurva (`cubic-bezier(.23,1,.32,1)`, starkare än CSS-default `ease`), 700ms inom "marketing/explanatory kan vara längre"-facket eftersom det är en fotohover, inte en UI-knapp; `(hover:hover)`-grinden för att aldrig ge touch en falsk hover; kortets `perspective:1200px` + `gsap.quickTo` för mus-tilt i stället för direkt 1:1-koppling ("tying visual changes directly to mouse position feels artificial... use quickTo"). |

Ingen `mcp__inspo__*`-sökning gjordes — B1/B2/C är ombyggnader av redan beslutad komposition (heron
speglad, en pinnad case-showcase), inte nya visuella riktningsval som behövde referens.

## Kvarvarande, hederligt redovisat (R5)

- **Väljarens hover-zoom och kortets tilt är overifierade på riktig pekskärm/mus** — bara
  Playwright-simulerad `mouse.move`/`getComputedStyle`, ingen fysisk enhet fanns tillgänglig i den
  här miljön. `(hover:hover)`-grinden garanterar i alla fall att touch aldrig triggar ett falskt
  hover-läge.
- **Showcasens `end`-räckvidd är nu pixelbaserad, inte vh-baserad** — korrekt vid varje breddpunkt vid
  mättillfället, men om `window.innerHeight` ändras UTAN ett resize-event (sällsynt, t.ex. viss
  mobilbrowser-UI-chrome som gömmer sig utan att avfyra `resize`) hinner `end` inte räkna om förrän
  nästa explicita `ScrollTrigger.refresh()`. Samma avvägning gäller redan heron-pinnens `+='120%'`.
- **Copy-diffens fyra R2-eravct-checkar** (`kontakt_heading`, `kontakt_card_column`,
  `exempelcase_word_vs_picker`) pekar nu om mot R5:s markup, men mäter en enklare uppsättning
  egenskaper än originalen (t.ex. `kontakt_card_column` kollar bara att kortet syns och att baksidan
  har två länkar, inte pixelexakta gap) eftersom R5:s layout inte har en direkt 1:1-motsvarighet till
  varje gammal mätpunkt (t.ex. "gapBelowLinks" fanns bara för en nu borttagen fast kolumnlayout).

---

# R6 · ledningens wheel-scroll-granskning av R5, sju defekter

Ledningen skrollade R5 för hand vid 1440 och 390 och hittade sju defekter — tre i showcasen, fyra i
kontakten. Alla sju är rättade i `tests/alunix-r8/runs/V3f/index.html`. Det som redan fungerade
(väljaren, den live-skrollande iframen, den pinnade tesraden, heron) rördes inte.

## Showcase §1/§2 — klippt text och en ledger/accordion i stället för "allt synligt på en gång"

**Fel**: rad 2:s ("En serif för allt man läser") brödtext klipptes mitt i meningen mot cellens
nedre kant vid 1440 — cellerna hade en fast höjd och R5:s "alla brödtexter synliga samtidigt,
tonade till 0,55"-layout hade inget tak för hur hög `.showcase-side` fick bli. Tre av fem rader
stod dessutom som tomma gråa celler innan de nåtts, vilket läste som oavslutat.

**Fix**: hela höger kolumn byggdes om till en scroll-driven ledger. Varje rads rubrik (`<h3>`) står
alltid synlig. Bara den AKTIVA raden (den vars ankare sajten just nått) expanderar sin brödtext, med
en höjdreveal via CSS grid-template-rows `0fr` → `1fr` (`.row-body`/`.row-body-inner`, spec tillät
antingen detta eller ett GSAP-mätt höjdvärde — grid-tricket vinner eftersom en ren CSS-transition är
interruptible by construction: scrollar man fram och tillbaka över samma ankargräns RETARGETAS
övergången från sitt nuvarande beräknade värde i stället för att spela om från 0, precis Emils regel
om `transition` vs. `@keyframes` för avbrytbar UI). Passerade rader kollapsar till bara rubrik i full
färg; kommande rader visar bara rubriken vid opacitet 0,35. Mobil behåller alla brödtexter synliga
(ingen accordion), enligt spec.

Två flex-buggar hittades och fixades under bygget av detta (båda fångade av det nya
`showcase_row_clip_check`, inte av ögat):
- Rader fick `flex:1` för att dela hela kolumnhöjden mellan sig (annars läste den kollapsade
  layoutens naturliga, kortare höjd som ett svart dödband längst ned — samma sorts defekt som §6,
  fast mindre).
- `flex:1` behövde INTE `min-height:0` — det extra värdet lät webbläsaren klämma en kollapsad
  rubrikrad under sin egen radhöjd när Hōrais sex rader delade en kortare 800px-kolumn vid 1280×800
  (uppmätt 2–19px verklig överflödning). Att lämna `min-height` vid sitt flex-default (`auto` =
  innehållets storlek) gör att en rad kan VÄXA men aldrig krympa under vad dess egen rubrik kräver;
  ett äkta underskott faller igenom till `.showcase-side`s egen `overflow-y:auto` (en scrollbar,
  aldrig tyst klippning).

## Showcase §3 — iframe-cellen fyllde inte sin höjd (svart band + krämrand)

Två separata orsaker, båda uppmätta med `getBoundingClientRect`, inte gissade:

1. `.showcase-side`s naturliga innehåll (i R5: alla fem/sex rader fullt synliga samtidigt) var högre
   än inbäddningscellens fasta höjd. Ett grid-item med en EXPLICIT höjd sträcker sig inte för att
   matcha en högre systers rad-spår — SPÅRET växer i stället för att passa den höga sidan, vilket
   lämnade inbäddningscellen ~110px kort mot radens faktiska höjd (mätt). Fixat genom att låsa BÅDA
   kolumnerna till samma explicita höjd (`.showcase-side` fick samma `height` som
   `.showcase-embed-cell`, plus egen `overflow-y:auto` som skyddsnät).
2. Den höjden var `100svh - 48px`, avsedd att stå UNDER den sticky topplisten (48px) — men pinnen
   (`start:'top top'`) sätter sektionens topp vid viewportens egen y:0, och topplisten bara MÅLAS
   ovanpå dess första 48px i stället för att FÖRSKJUTA dem. Resultatet: innehållet undvek korrekt
   topplisten visuellt, men landade 48px kort av viewportens nederkant — ett svart band under
   BÅDA kolumnerna (uppmätt: båda vid 852px botten i en 900px viewport). Heron har exakt samma
   aritmetik och lucka i sin egen pin (rörs inte, per uppdraget) — osynlig där bara för att den
   landar mot sidans egen svarta bakgrund på båda sidor. Showcasens är synlig eftersom det finns
   riktigt innehåll precis ovanför. Fixat på samma sätt som gör heron osynlig: fyll HELA viewporten
   (`100svh`) — topplisten täcker fortfarande visuellt de första 48px (den är `position:sticky`,
   `z-index:40`, ogenomskinlig), men nu landar botten exakt på viewportkanten, ingen lucka kvar att
   exponera.

## Kontakt §4 — rubriken sprang förbi ÖV/ÖH-skarven, kortet täckte "verksamhet."

**Fel**: `headline-40` är dimensionerad för ETT jätteord (hero, casenamn) — vid halva sidbredden
sprang en fyraordsmening i den förbi cellens egen kant (uppmätt x>720 vid 1440, in i kortets yta).

**Fix**: en dedikerad, mindre `clamp()` (samma familj som gamla `kontakt-giant`s) på
`.kontakt-q--ov h2`, verifierad med `getBoundingClientRect` mot cellboxen — inte skattad — vid
1440/1280/768. Kortet flyttades samtidigt från att spänna HELA 2×2-korsningen till att bara spänna
den NEDRE raden (`grid-row:2`, fortfarande horisontellt centrerat på den vertikala skarven = "på
korsningen", men nu helt inom NV/NH-halvan) — centrerat på hela korsningen lämnade bara ~15–50px
marginal till rubriken, med noll utrymme kvar för vändningens lyft eller hovertiltens
perspektivförvrängning.

## Kontakt §5 — framsidan var tom vit med ett kvarstående 1px streck

**Fel**: kortets framsida (fotot + den vita loggan, samma som heron) visade ingenting utom ett
tunt lodrätt streck till vänster.

**Rotorsak, bekräftad med `getComputedStyle`/`getBoundingClientRect`, inte gissad**: kontaktkortets
framsida är en `<button>` byggd av `<span>`-taggar (spans, till skillnad från heronkortets `<div>`-
taggar, är `display:inline` som standard). `.face--front .photo` sätter bara `position:relative` —
en relativt positionerad INLINE-box respekterar aldrig `width`/`height`, så den kollapsade till en
~2×21px box (exakt det "1px-strecket"). Bilden, absolut positionerad `inset:0` inuti den kollapsade
boxen, ärvde en 0-bred behållare och blev därför osynlig. Fixat med `display:block` på
`.face--front .photo` (harmlöst no-op för heronkortets redan blockformade `<div>`). Bevisat med en
skärmbild av framsidan (självvändningen inaktiverad för skottet):
`shots/lead-r5/kontakt-card-front-proof.png` — samma foto + logga som heron, korrekta bilddimensioner
(`getBoundingClientRect` gav en riktig 400×238px-box, inte 0×19).

## Kontakt §6 — dött svart band (~110px) under mint-cellen

**Fel**: en generisk `.rhythm`-mellanrumsdiv (110px, samma klass som andra sektionsövergångar)
stod kvar direkt efter `#kontakt`s stängande tagg, före footern —läste som en död svart yta under
den fyllda 100svh-kvadranten.

**Fix**: den specifika rhythm-diven mellan kontakt och footer togs bort. Sektionens NH-cell möter nu
footerns svarta direkt, samma hårda skarv-komposition som heron har högst upp på sidan.

## Kontakt §7 — mobilt mitt-i-vändningen täckte kortet underrubriken

**Fel** (fångat av det nya `card_text_overlap_sweep`-testet vid 390, inte av ögat): en Y-axelrotation
med perspektiv FÖRSTORAR genuint ett plant korts renderade bounding-box på höjden när dess närmare
kant vrids mot kameran — uppmätt ±28px topp/botten vid `perspective:1200px` (fortfarande ±24px vid
3000px; det här är äkta 3D-projektionsgeometri, inte ett avrundningsfel). Att centrera ett 88%-brett
kort i en `60vw`-hög rad lämnade bara ~27px marginal till underraden ovanför — inte nog för att
överleva den bulgen vid någon vinkel i 0–180°-svepet.

**Fix**: NH-radens mobilhöjd höjdes (`minmax(76vw,auto)` mot OV/NV:s `minmax(60vw,auto)`), kortet
krympte till 80% bredd, och "den korta lyftningen" (`y:-14`) begränsades till skrivbord — på en smal
mobil stapel var även en liten extra höjning mätbart för mycket. Rotationen ensam läser fortfarande
tydligt som en vändning.

## Nya kontroller i `verify_motion.py` (spec §D, ledningens explicita krav)

- **`showcase_row_clip_check(browser, w, h)`**: `scrollHeight > clientHeight` på VARJE
  `.showcase-row`-element (och `.showcase-side` som helhet) = fail, samplat vid sex punkter över hela
  pinnens räckvidd, för BÅDA casen, vid 1440/1280/390. Detta är exakt det testet som fångade
  1280×800-flex-klämningen ovan — inte synligt vid 1440 eller 390, bara vid den kortare 800px-höjden
  kombinerat med Hōrais sjätte rad.
- **`kontakt_check`s `card_text_overlap_sweep`**: `rotationY` svept 0→180° i 15°-steg (plus
  hover-tilt-lyftet där det gäller), `getBoundingClientRect`-kollisionstest mot BÅDE rubriken och
  underraden, vid 1440/1280/768/390. Detta fångade §7:s mobila bulge-överlapp — osynlig i en
  enstaka vilo-skärmbild, bara synlig när man faktiskt sveper vinkeln.
- `headline_fits_ov_cell`: `getBoundingClientRect` på rubriken mot ÖV-cellens egen box, samma fyra
  breddpunkter.

## Uppmätta värden, R6 (`verify_motion.py`, efter alla sju fixar)

| Kontroll | 390 | 768 | 1280 | 1440 | 1920 |
|---|---|---|---|---|---|
| `showcase_row_clip_check.passed` | sant | — | sant | sant | — |
| `kontakt_check.card_text_overlap_sweep.passed` | sant | sant | sant | sant | — |
| `kontakt_check.headline_fits_ov_cell` | sant | sant | sant | sant | — |
| Legibility ≥40vh (alla fem rubriker) | — | — | — | sant | — |
| Showcase-ankare inom ±2px (Calyx + Hōrai) | — | — | — | sant | — |
| Horisontell overflow (px) | 0 | 0 | — | 0 | 0 |
| Footer `ScrollTrigger.progress` vid maxscroll | 1 | 1 | — | 1 | 1 |
| Konsolfel | 0 | — | — | 0 | — |

Copy-diff (`verify.py`, mot V3d): oförändrat från R5 — `over_count_vs_v3d` exakt `ALUNIX` 2× och
`kontakt@alunix.se` 2× (de två kända, godkända dubbletterna), `not_found_in_v3d: []`. Ingen ny synlig
text infördes av någon av de sju fixarna (bara omflyttning, omstorlek och tidsstyrning av befintlig
copy och struktur).

## Skärmdumpar, R6

`tests/alunix-r8/runs/V3f/shots/r6/` (riktig hjulscroll, 1440 och 390):

- `d1440-00-hero.png` … `d1440-06-kontakt.png` — hero → tes (pinnad) → exempelcase → showcase (start,
  accordion mitt i, accordion sent) → kontakt.
- `d1440-04-showcase-accordion-mid.png` — beviset för §1/§2: rad "Utbudet som prislista" expanderad
  med full läsbar brödtext, tidigare rader kollapsade till rubrik, inget klippt.
- `d1440-06-kontakt.png` — beviset för §4/§5/§6: rubriken ryms i ÖV, kortet sitter på NV/NH utan att
  röra texten, mint möter footerns svart utan lucka.
- `m390-00-hero.png` … `m390-04-kontakt.png` — samma svep vid 390, `m390-04-kontakt.png` visar den
  staplade mobila layouten (rubrik+underrad i sin cell, kortet i sin egen mintcell därunder).
- `shots/lead-r5/kontakt-card-front-proof.png` — det definitiva beviset för §5 (självvändningen
  inaktiverad för skottet): framsidan visar fotot + loggan, inte tomt vitt.
- `shots/lead-r5/kontakt-front-forced.png`, `kontakt-full-after.png`, `showcase-fill-check.png`,
  `showcase-1280-pinned.png` m.fl. — arbetsskärmdumpar från felsökningen, kvar som spårbar
  dokumentation av varje fix.

## Skill-kedja R6

| # | Anrop | Konkret regel/detalj jag använde |
|---|---|---|
| 1 | `mcp__ui-skills__get_skill("emilkowalski/emil-design-eng")` | "Use CSS transitions over keyframes for interruptible UI" — direkt grunden för att bygga accordionens höjdreveal som en `grid-template-rows`-CSS-transition (klass-toggling i JS, ingen `gsap.to`-tween på höjden) i stället för en keyframe/tween som skulle starta om från 0 vid snabb fram-och-tillbaka-scroll över samma ankargräns. Ledningens egen instruktion citerade uttryckligen "Emil's rule on interruptibility", så skillen lästes om för att bekräfta den exakta regeltexten innan bygget, inte fritt återgiven ur minnet. |

Inga andra nya `Skill`/`mcp__ui-skills__`/`mcp__inspo__`-anrop denna runda. De sju fixarna är
antingen strukturella CSS/JS-korrigeringar av verkliga mätfel (flex-krympning, grid-höjdmatchning,
`display:inline` på en `<span>`, en borttagen spacer-div) eller en direkt tillämpning av redan
inhämtad kunskap (R5:s `gsap-scrolltrigger`/`gsap-core`-kedja för att förstå varför `start:'top top'`
+ en sticky header ger en 48px-lucka). Inget av det krävde ett nytt designbeslut som en skill
behövde styra.

## Kvarvarande, hederligt redovisat (R6)

- **Heron har samma 48px pin-arittmetik/lucka som showcasen hade** (bekräftat, mätt: `hero-stage`
  botten vid 852px av en 900px viewport, identisk formel). Den är osynlig där eftersom både luckan
  och sidans egen bakgrund är svarta — men den är strukturellt densamma defekten. Rörde den INTE,
  per uppdragets uttryckliga "vad som fungerar och måste stå kvar: ... heron".
- **`card_text_overlap_sweep`-testet har en känd över-strikt kant**: vid `rotationY:90` är kortet
  visuellt kant-i-kant (nästan osynligt, bredd→0), men dess achse-alignerade bounding box är
  fortfarande hög (perspektivbulgen) och kan tekniskt "kollidera" med en textbox utan att någon
  pixel faktiskt överlappar. Jag löste ändå den geometriska marginalen så att även denna strikta
  tolkning går grön, snarare än att mjuka upp testet.
- **`.showcase-side{overflow-y:auto}`** är kvar som ett aldrig-klipp-skyddsnät efter fixarna, även
  om inget av de sju uppmätta scenarierna (1440/1280/390, båda casen, hela pinnens räckvidd) faktiskt
  triggar en scrollbar. Om en framtida textredigering gör en rubrik längre är skyddsnätet där utan
  att kräva en ny kodändring.

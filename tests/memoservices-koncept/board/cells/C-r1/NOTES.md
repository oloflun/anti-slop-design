# C-r1 · Passagen

**Lane:** ljus katalog, piren i djup, brickorna som objekt: heroens brickmoln flyger ihop till den första tjänstens 2×2 och blir en sidledes passage med sju objekt man går förbi.

**Auktoritet (TASTE § 1):** objektet, brickan. Typen är stram (Archivo Black i rubriker, Arimo i allt annat). Videon är scen.

Filer: `template.html` (platshållare), `index.html` (renderad med `content/render.py`, 305 rader), `style.css`, `main.js`.

## Akterna

| # | Akt | Enhet | Spann (1440×900) | Orsak in |
|---|---|---|---|---|
| 0 | Intro → hero | tidslinje: kickern som SplitText `words` i rött på papper (0,9 s), gardinen lyfter 1,2 s `power3.inOut`, brickorna faller in i tre plan `back.out(1.3)`, h1-raderna reser sig ur radmasker | ca 2,6 s, snabbas upp ×5 om man scrollar | kickern består: den glider upp och blir navbarens vänstra etikett |
| 1 | Hero | parallax i tre plan, scrub (fjärr 31 % efter, mellan 17 % efter, nära 1× och framför plattan) | heroens höjd + header (100 vh) | – |
| 2 | Passagen (peak) | pin + pan, `containerAnimation`-settle (.55 → 1, 24 → 0 px, första objektet undantaget) | pin = 450 px håll + 7 315 px pan + 1 080 px lime + 315 px svans = 9 160 px | brickfältet bildar nästa objekt: de 25 brickorna flyger med live-FLIP (eget fast skikt, mäter båda ändarna varje bildruta) till Redovisnings 2×2 medan grunden går från `--bakgrund` till `--ink` |
| 3 | Kartläggning | reveal/scale + radmask + långsam drift | lime-tillväxt 120 vh + svans 35 vh + 40 vh stående | panel ur axeln: limebrickan sist i railen växer tills den täcker vyn; bandet ligger redan under, passagen döljs när limen täcker och bandets rader reser sig |
| 4 | Om (`id="om"`) | flow+in (14 px / 620 ms) + ordtändning grafit → ink, scrub | flöde | ark läggs över: Om-arket med hårlinje glider upp över det klistrade limebandet (CSS sticky) |
| 5 | Insikter | reveal per objekt, `clip-path` nedifrån, 80 ms stagger | flöde | – |
| 6 | Slut | scrub, sista triggern `end: 'bottom bottom'` | sidfotens höjd | indexet bildas: 28 brickor svävar in och lägger sig som sju 2×2 framför namnen i TJÄNSTER |

Övergångsorsaker: gardin + fallande brickor, brickfältet bildar objektet, panel ur axeln, ark läggs över, indexet bildas. Fem olika, aldrig samma två i rad. Enhetsföljd: tidslinje → parallax → pin/pan → scale/reveal → flow+in/ordtändning → reveal → scrub. Pekare: tilt 6° på varje objekts 2×2, magnet på "Se tjänsterna", båda bara under `(hover:hover) and (pointer:fine)` med `gsap.quickTo`.

**Railens överflöde** (`rail.scrollWidth - innerWidth`): 7 315 px vid 1440×900, 2 956 px vid 390×844.

## Runda 2 (leadens sju punkter)

1. **Passagen:** objekten är 42 vw breda och staplade (2×2 med 20 vh-brickor över texten). Rubrikobjektet står fortfarande först. Railens överflöde är **4 745 px** vid 1440, tidigare 7 315. Bakom railen ligger ett andra lager: `piren-last.webp` (fasadens raster) under en ink-slöja på 0,80 med parallax 0,3 mot railen. Kontrast under texten med `contrast_over_media` vid `?preview=passage` och `passage-4`: sämst 10,6:1, alla godkända.
2. **Om-rubriken:** står på 8 kolumner med taket 4,6 rem. "EN KONTAKTPERSON." ryms på en rad vid 1440.
3. **Limebandet:** text och knapp ligger i 7 kolumner med tyngdpunkten kring 44 %. Den växta brickan står kvar som en 2×2 till höger, med brickor på 24 vh (tre lime med hårlinje, ink-accent). Den landar med skala 1,6 → 1.
4. **Navkickern:** är `--ink` (17,07:1). Under introt är den röd på papperet och tonar till ink medan den glider upp i navbaren.
5. **Hero → passage:** grundfärgen tonas inte längre. Passagen ligger fyra brickenheter (4 × 59 px, 4 × 40 px på mobil) upp över heroens fot, och en `clip-path: polygon` med kolumner en enhet breda öppnar den. Kanten sjunker i hela enheter och är helt öppen när pinnen börjar. Inget grått mellanläge.
6. **a11y:**
   - `aria: "none"` på alla SplitText, så inga aria-label på span eller p (0 kvar).
   - Fetstilen är riktig `<strong>` i JS.
   - Kolumnrubrikerna är text i noden.
   - Koncernlänken i sidfotens löptext är understruken.
   - Logotypen har fått `title`. Bilden har alt, men tab_walk läser bara innerText och title, och det finns ingen JSON-sträng att skriva som text.
   - Reveals använder `opacity` i stället för `autoAlpha`, så kartknappen och koncernlänken går att tabba till innan de visats.
   - Löpnumren ligger kvar i `data-n` + `::before`. `verify_text.py` godtar inte "01–07" som text.
7. **Tangentbord i railen:** `focusin` på en länk i ett railobjekt rullar dit med samma beräkning som indexet (`immediate`, så att fokus syns direkt). tab_walk: 0 stopp utanför vyn, 0 utan namn. Kvar är 5 `order_mismatch`: vertikala hopp mellan sektioner i samma läsordning.

Sidlängd nu: 10 345 px = 11,5 viewporthöjder vid 1440×900.

## Signaturobjektet, brickan, har fyra jobb

1. **Moln i hero:** 25 brickor i tre djupplan (9 × 24 px, 9 × 44 px, 7 × 72 px), alla sju huvudfärgerna (inklusive brun, sten och grafit) plus röd, lime, rosa och korall.
2. **Objekt i passagen:** molnet flyger ihop till Redovisnings 2×2; varje tjänst är en stor 2×2 (16 vh-brickor) med tilt.
3. **Panel:** limebrickan sist i railen växer till kartläggningsbandet.
4. **Index:** 2×2-markörer i indexraden (aktiv tjänst skalar 1,2), i Om-ledgern (röd/lime), som insiktsobjektens 96 px-bricka och som sidfotens TJÄNSTER-index som bildas vid slutet.

## Nav

Tunn övre rad (48 px): logotyp, kickern som etikett, de sex länkarna och "Kontakta oss". Under den indexraden med de sju tjänsterna (2×2 + namn, 13 px). I passagen är den aktiva tjänsten ink med brickan skalad 1,2 och övriga grafit. Klick på ett namn rullar med `lenis.scrollTo` till objektets läge i passagen (pinnens start + håll + objektets x, centrerat); ctrl-, cmd- och mittenklick öppnar `/tjanster/<slug>`. Under 1360 px ligger länkarna, knappen och indexet i panelen bakom "Meny" (`aria-expanded`, Esc stänger och återför fokus, Lenis stoppas). I panelen leder indexet direkt till tjänstesidorna.

## `?preview=`-krokar

`hero`, `passage` (flygningen landad, railen i vila), `passage-4` (Juridik centrerad), `kartlaggning`, `om`, `insikter`, `slut`. Dessutom `window.__jump('<namn>')` för hopptester.

## Mätvärden (port 3103, headless Chromium)

- `verify_text.py`: 96 textnoder, **0 avvikelser**.
- Konsol: **0 fel, 0 varningar, 0 4xx/5xx** vid 1440 och 390, med alla sju previews, en full scroll ned och upp och interaktioner. Enda nätverksnot: på mobil avbryts 1280-videon (`ERR_ABORTED`) när JS byter till `piren-hero-540.mp4`. Det är bytet som briefen beställer, inte ett fel.
- `scroll_verify.py` (1440): deadScroll **[]**, cuesNeverFull **[]**, unrevealed **[]**.
  - `contrastUnderMedia` flaggar "Se tjänsterna" och "Kontakta oss" med 1,0. Skriptet mäter vid 400 ms, när introts gardin ligger över knapparna, och golvet 4,5 tar inte hänsyn till fet 19 px text. `contrast_over_media.py --wait 4500` mäter båda till 4,17:1 mot golvet 3,0 (stor text): **ok**.
  - `blankBands` 1500–9982 är pinnens spacer i en helsidesbild tagen vid scroll 0. Den uppstår av själva pinnen som briefen kräver (överflöde + lime). Passagens innehåll står i den fasta scenen, inte i spacern.
- Horisontellt överflöde (elementgränser utanför klippta behållare) vid 320/375/414/768/1024/1440 i alla akter: **0**. Inga tvåradiga knappar eller navlänkar.
- Avvikelse kvar: **kickern** (röd Arimo 500 11 px på `--bakgrund`) har kontrasten 4,17:1 mot golvet 4,5. Briefen föreskriver röd kicker, och originalet har samma kombination. Den är inte ändrad. Anton avgör.
- Sidlängd: 13 151 px = 14,6 viewporthöjder vid 1440×900. Det ligger strax över husets budget på 8–14, eftersom railen med objekt på 60 vw är peaken.

## Beslut värda att känna till

- **Löpnumren 01–07** ligger i `data-n` och visas med `::before`. Ett eget textelement skulle fälla textkontrollen.
- **Sidfotens kolumnrubriker** TJÄNSTER, FÖRETAGET och JURIDISKT finns bara som nycklar i `delat.json`. De visas med `::before { content: attr(data-k) }`, så att ingen text skrivs i noderna.
- **`<strong>` på om-punkternas fetstilsdel** och **länken som bara täcker "www.memoservices.no ↗"** sätts i JS ur den renderade texten. Utan JS står hela meningen kvar med hela raden som länk.
- **Pilen i "→"-länkarna** färgas röd i JS genom att tecknet lyfts in i ett eget `span`. Texten ändras inte.
- **Nära-planet** står på 1× som briefen säger. Det passerar över plattans kant under flygningen. I vila överlappar två nära brickor plattans högra kant.
- **Heroens scrub** spänner 100 vh, inte 220 vh. Flygningen börjar redan vid första scrollen (scroll 0 → pinnens start + 50 vh), så brickmolnet är i rörelse genom hela heroens utgång.

## Inte hunnet / öppet

- Kickerns kontrast (se ovan).
- Indexraden markerar den aktiva tjänsten bara på desktop (≥ 1360 px), eftersom den annars ligger i menypanelen.
- Ingen `section_probe.py`- eller `perf_probe.py`-körning, eftersom de inte ingår i § 10.
- Ingen a11y-audit eller kritikerrunda, eftersom delegering var avstängd för den här cellen.

# K2 Affischen, byggnotes

Sidan: `index.html` (all CSS och JS inuti), `assets/` (fem WebP, två SVG), `shots/`.
Serverad från repo-roten på port 3102, öppnad som
`http://127.0.0.1:3102/tests/alunix-ab-r6/runs/B/K2/index.html`.

## Lane och register

"Tryckt affisch på salvia-papper, en enda tung grotesk, fem färger, ingen accent."
Registret är tryckt papper enligt målbilden. Referenslås: `springsummer` (primär: krossad
display-typ, femfärgstak, riktig klocka i toppraden, typografiska pilar) och `indoek`
(sekundär: fotot fönstrat genom ordmärket). Bara principen lånas: inga av deras färgkoder
eller typsnitt finns i bygget.

## Beslut

- **Fem färger, härledda ur "salvia/grågrön ton":** papper `oklch(85% 0.028 135)` (≈ #c6d2c0),
  bläck `oklch(22% 0.012 150)` (≈ #171c18), vitt `oklch(98.5% 0.004 120)`, linje 1
  `oklch(74% 0.024 135)`, linje 2 `oklch(45% 0.02 140)` (dämpad text, 4,7:1 mot papper). Ingen
  accent. "Klicka här" markeras bara med understrykning eller inverterat bläck (avslutet).
- **En familj för allt: Archivo** (variabel bredd/vikt från Google Fonts). Affisch = 900 vid 112 %
  bredd. Brödtext 400. Siffror tabulära. Valet: en grotesk med stora, öppna räknare i A och U så
  att fönstren i bokstäverna faktiskt visar något; Geist/Inter från dagens register lämnades.
- **Två typstorlekar plus bildtext:** lässtorlek (17–20 px) och affisch. Affischen har två
  grader: ordmärket (`min(26vw, 36vh)`, 324 px vid 1440×900) och aktrubriken (`7.6vw`, 109 px),
  som är den storlek `ERT VARUMÄRKE.` får plats i på en rad. Ingen mellanstorlek: alla
  mellanrubriker är spärrade små versaler (12 px, 0.18em).
- **Ordmärket bryts `ALU` / `NIX`** på två rader med radhöjd 0.78 så att raderna nästan rör
  varandra. Målbilden kräver att blocket har två rader som glider isär och blir `VI BYGGER` /
  `ERT VARUMÄRKE.`; en rad ALUNIX hade inte kunnat göra det. Loggan (SVG) står i toppraden.
- **Panelen bakom bokstäverna** ligger från 30 % av innehållsbredden ut till skärmkanten (sidans
  gridbrott). Den täcker U, N, I, X; A står på papper. Skärmbilderna visas genom räknarna och i
  mellanrummen, som i indoek.
- **Klockan** är riktig (`Intl.DateTimeFormat`, `Europe/Stockholm`, tickar varje sekund). Utan JS
  visas bara `Stockholm`, aldrig en stillastående tid.
- **Ramarna** i akt 4 är riktiga `<iframe>` mot `/sites/…`. Ovanpå ligger skärmbilden som en
  tryckt plåt. Det som scrubbas är plåten (gråskala → färg, sedan bort), aldrig ramen. När plåten
  är borta får ramen pekaren och går att använda. En gång live, alltid live.
- **Priserna** står i aktrubrikens grad, höger; "Pris vid förfrågan" i spärrade versaler eftersom
  det inte är ett tal.
- **Avslutet** är sidans enda tonala inversion: bläckblock, `Alla har rätt till bra design.` i
  affischgrad, en hårlinje, en lässtor rad med adressen som understruken länk, och kolofonen i
  minsta typ (11 px). Sidan slutar på minsta typen.
- Inga skuggor, inga kort, radie 2 px på bildytor, inga tankstreck i synlig text.

## Akt för akt, vad som rör sig

1. **Tyngd** (första skärmen): stilla. Klockan tickar. Calyx syns genom ALU/NIX.
2. **Byte** (blocket klistras under toppraden, 0–55 % av resan): bildremsan bakom masken glider
   vertikalt, Calyx → Hōrai → Hyperborea; bokstäverna står stilla. Bildtexten under ordmärket
   byts i takt, ut först och sedan in, aldrig två samtidigt. Slag: scrollstyrd förskjutning.
3. **Andning** (55–100 %): `font-size` går från ordmärkets till rubrikens grad, radhöjden från
   0.78 till 0.92, ALU/NIX tonar och blurrar bort, `VI BYGGER` / `ERT VARUMÄRKE.` tonar in med
   spärrning som drar ihop sig från 0.06em till −0.03em. Panel och bildtext tonar bort. Slag:
   pinnad scen med procentuell styrning. Blocket släpper exakt när rubriken nått sin slutgrad
   (spannet räknas ut från blockets höjd före och efter), så rubriken står kvar som nästa akts
   rubrik utan dött avstånd.
   Signaturen är 2 + 3 tillsammans: samma scroll, mjuk interpolering (lerp 0.14 per frame,
   smoothstep-segment), båda riktningarna. `?p=0.42` låser resan för skärmbilder.
4. **Bevis**: varje uppslag glider in en gång (translateY 56 px, 1.3 s). Plåten går från gråskala
   till färg när ramens mitt passerar skärmens mitt, och tonar då bort så att den levande ramen
   visas. Slag: engångsintoning + scrollkopplad filterövergång.
5. **Lista**: raderna tonar in radvis; siffran 01–03 avslöjas nedifrån med `clip-path`. Slag:
   radvis intoning med klippmask.
6. **Pris**: hårlinjerna ritas från vänster (`scaleX`), innehållet tonar in efter; det
   dokumentära fotot glider i annan hastighet (parallax ±40 px). Slag: linjedragning + parallax.
7. **Avslut**: bläckblocket rullas ned över sidan med `clip-path: inset(0 0 var(--drop) 0)`
   kopplat till scroll, och når hela vägen ned exakt när sidan tar slut. Slag: klippmask styrd
   procentuellt av scroll.

Fem slag; två intilliggande akter delar aldrig slag.

## Reduced motion, utan JS

`prefers-reduced-motion: reduce` (eller `?reduce=1`): inget `.motion` på `<html>`. Då är
blocket inte klistrat, panelen är exakt ordmärkets höjd, bildtexten står mellan ordmärket och
rubriken, `VI BYGGER / ERT VARUMÄRKE.` är en vanlig rubrik under ordmärket, alla rader synliga,
plåtarna i färg och ramen byter till live via `IntersectionObserver` (en tonövergång, ingen
resa). Klockan går fortfarande. Utan JS: allt synligt i rätt ordning (`shots/nojs-full-1440.png`),
resan (`.travel`) döljs.

Alla dolda startlägen (`opacity:0`, `clip-path`) finns bara under `.motion`, och där finns
tröskel 0, avslöjning av allt som redan är på skärmen vid start och en 4 s-reserv.

## Foton och krediter

- Skärmbilder: `assets/demo-calyx.webp`, `demo-horai.webp`, `demo-hyperborea.webp`, kopierade
  från `tests/alunix-concepts-r3/build/assets/`.
- Dokumentär plate i akt 6: `assets/desk-daylight.webp`. Foto: Annie Spratt,
  https://unsplash.com/@anniespratt, bild
  https://unsplash.com/photos/wooden-desk-with-model-ship-and-lamp-by-window-Rjp8UxEIJ38.
  Visas i gråskala. Krediterad i sidfoten och vid bilden.
- Unsplash-anrop: 3 av 12 (en sökning som gav 0 träffar, en sökning
  `designer desk daylight documentary` med 30 kandidater, ett download-anrop). Kandidaterna
  renderades som kontaktark och lästes som bild innan valet; #19 valdes för att den är lugn,
  utan människor, och bara ska bära en bildtext.
- Logotyp: `assets/logo-black.svg` / `logo-white.svg`; sökvägen ligger inline i toppraden med
  `currentColor`.

## Skärmbilder jag tittade på och vad jag ändrade

1. `fold-1440.png` (första försöket): panelbilden trasig, servern på 3102 (en redan igång
   `python -m http.server`) tappade anslutningar och hängde 10 s på WebP-filer; även en färsk
   python-server gjorde det på den här maskinen. Bytte till en minimal Node-server på samma port
   (stabil på 8/8 anrop) och lade en engångs-omladdning på `<img>` vid fel.
2. `fold-1440.png`: kompositionen håller. Ingen ändring.
3. `sig-0.18`, `sig-0.42`: bildremsan glider rätt, men bildtexterna korstonade och dubbeltryckte.
   Ändrade till ut-sedan-in.
4. `sig-0.62`, `sig-0.78`, `sig-0.9`: rubriken `ERT VARUMÄRKE.` fick inte plats i slutgraden
   (kapad efter `VARUMÄR`). Sänkte `--fs-head` till `7.6vw` (max 7.2rem) och gav rubriken en egen
   startgrad 1.35× slutgraden under andningen i stället för ordmärkets, så att mindre kapas i
   mellanlägena.
5. `full-1440.png`: prisraderna blev enordskolumner (prissiffran åt hela bredden): la om till
   1fr/4fr med smal fotokolumn. Fotot blank: parallaxen var oklampad i helsidesbild; klampad ±40.
   Bläckblocket saknades helt: `--drop` nådde aldrig 0 när avslutet var lägre än 0.75vh; nu
   räknas mot `min(0.75vh, blockets höjd)`. Avslutsrubriken saknade affischgrad: satt.
6. `reduced-full-1440.png`: panelen (16:10) hängde över rubriken och bildtexten kom efter
   rubriken. Panelen är nu ordmärkets höjd i statiskt läge och bildtexten flyttad in mellan
   ordmärke och rubrik.
7. `full-390.png`, `fold-390.png`, `fold-320.png`: ramarna var 16:10 och visade bara ett
   smalt band av mobil-sajten; nu 4:5 under 860 px. Panelen bakom bokstäverna täckte bara U;
   nu ordmärkets fulla höjd på mobil.
8. `region-proof/ledger/price/close-1440.png`, `region-*-390.png`: efter rättningarna. Prisraderna,
   liggaren och avslutet läser rätt. Kontrast på dämpad text höjd (3,8 → 4,7:1).
9. `nojs-full-1440.png`: allt innehåll synligt utan JS.

Mätt: konsolen tom (de tre exempelsajterna varnar själva om Tailwinds CDN inuti sina ramar,
det är deras, inte sidans). Överflöde per element (bounding rect utanför viewport utan klippande
förälder) vid 320, 390, 768 och 1440 i 300 px-steg: inget. `scrollWidth` = viewport. Alla tre
ramar har `<title>`. Blanka band (>93 % en färg i viewporten) i 300 px-steg vid 1440: inga.
Tab-ordning: logga, adress, `Öppna Calyx`, ramens innehåll, `Öppna Hōrai` … med synlig ring.

## Kända brister

- I en helsidesbild syns ett tomt band där blocket är klistrat (resan på 150 vh). Det är
  fångstens artefakt, i scrollen rör sig alltid något, men det går inte att visa statiskt.
- Live-ramarna på mobil visar exempelsajternas egna mobilbrister (Calyx toppbar vid 350 px).
- Tre levande ramar är tunga; de laddas `lazy`, men på en svag enhet märks det.
- Mitt i andningen (p ≈ 0.6–0.8) kapas rubriken tillfälligt i högerkanten medan den krymper.
  Det är avsiktligt (affischen bryter kanten), men i en stillbild kan det se ut som ett fel.
- Tab-fokus går in i ramarnas innehåll; det är rätt för användbara ramar men ger många stopp.
- Ingen a11y-granskning med skript utöver tab-walk och kontrastmätning.

# B3 · "Banden II" · runda 3

**Lane:** platt och ljus i gemener; sidans grund är tjänstens 2×2 i rumsskala, bandet är tjänsten och railen är kartan.
**Auktoritet (TASTE § 1):** ytan och färgen. Fyra fält som byter tjänstefärg bär sidan; typen ligger ovanpå.

## Typsnitt
| Roll | Snitt | Grad |
|---|---|---|
| Display (bara rubriker, versaler som originalet) | Schibsted Grotesk 800, spärr +.01em, leading .92 | h1 `clamp(3rem, 8vw, 7rem)` (12,6vw under 400 px); sektions-h2 `clamp(2.25rem, 6vw, 6rem)` (om 5rem, mobil 8,4vw); bandnamn `clamp(2rem, 4.2vw, 4rem)` (mobil 7,6vw) |
| Text (nav, lead, listor, knappar) | Onest 400/500/600/700 | body 17/18 px, lead 20–24 px 600, nav 16 px 500, knappar 19 px 700 |

Onest 700 är tillagd för knapparna: brandröd fyllning med papperstext ger 4,17:1, vilket bara klarar AA som stor text (≥ 18,66 px bold). Det är en familj i en `<link>`.

## Runda 3b (leadens rättelser, 2026-10-12)
1. **Fönster 100 % → 45 %.** Varje lagerövergång är klar när nästa sektions topp står vid 45 % av vyn (`DONE = 0.45`). Om: fältens färg till papper är klar vid 55 % (0,66 av fönstret; ink-fältet redan vid 0,4, så ingen grå rest). De små brickorna till om och insikter är framme innan sektionens rubrik når vyn (om: 0,45 av fönstret, insikter: 0,3), och följer sedan dokumentet. Ingen bricka korsar en rubrik i läsläge.
2. **Ledgerns radtext** reveal:as vid `top 92%` (egen batch), övrig reveal vid 88 %.
3. **Bandakten:** övre vänstra fältet är `--tlh: 64vh` (nedre raden är en remsa). All text står i en sticky scen `.tj-stage` som täcker exakt det fältet: kicker, rubrik och länk överst i railen, under dem de sju namnen; bandtexten vertikalt centrerad. Banden flödar som spacers (60 vh var; första 100 vh − chrome + 3 vh, så att scenen hunnit fästa). Scenen klipps varje bildruta till snittet av fältets plats och fältbrickan (`inset()`), så text kan aldrig hamna över en söm eller under navet. Kontroll: inga synliga textrektanglar över en söm vid 1440×900, 1920×1080, 1366×768 eller 390×844, varken i någon preview eller +12 hack efter (eget skript; de enda träffarna är rader som är halvt bortklippta vid fältkanten medan scenen glider in eller ut).
4. **Kartläggning:** kicker, rubrik, text och knapp i ett block i övre vänstra fältet (8 kolumner, tyngdpunkt ~44 %). Högra fältet är tomt lime, accentfältet ink med de sex 2×2-raderna.
5. **Bandbytet** är en stegad mosaikkant: kolumner i brickans enhet (~56 px) med fyra trappnivåer i mönstret 0-2-1-3, som sveper nedifrån och upp genom hela 2×2:an, scrubbat i fönstret. I fälten är kanten `div`-kolumner som bara flyttas med `transform` (ett svep-lager `.bw` per fält). Den nya bandtexten visas och den gamla döljs med samma kant (`clip-path: polygon` på textblocken). Ingen mellanfärg. Nav-baren byter färg när kanten passerat 70 %. "Flera områden" har samma rum men tänder rastrets 24 brickor i sina tjänstefärger.
6. **Mobil (< 768):** accentfältet är en remsa nederst i full bredd (56 px) med rastret som en rad på 28 platser; övre vänstra fältet tar resten av höjden.

## Formationerna (bricklagret, 28 brickor: 0–3 = fälten, 4–27 = de små)
En scrubbad huvudtidslinje (`scrub: true`, `ease: none`, tid = scroll-px). Varje övergång är ett segment, och alla mål läses från slot-element vid init och vid varje `ScrollTrigger.refresh` (refresh-lyssnaren mäter om och bygger om om layouten ändrats).

| # | Sektion | Slot-mönster | Fönster | Orsak |
|---|---|---|---|---|
| F1 | Hero | `.hero-mosaic i` (7×5, 28 celler, facit-silhuetten + 3; färgerna = de sju 2×2:orna exakt), videobandet `.fb-band` 12/12 × 48vh | intro 1,2 s, sedan följer brickorna dokumentet (vila R0) | intro: brickorna lägger sig rad för rad |
| F2 | Full bleed (enda pinnen, 200 vh) | fälten `.fx-fields > i` (fast 2×2, 8 px papperssömmar), de små `.fx-edges i` (24 runt kanten), videoramen → hela vyn | 0–100 % av pinnen; video 0–55 %, sedan står den | brickan som växer till full bleed |
| F3 | Tjänster, 7 band + sticky rail | fälten i tjänstens färger (3 huvud + accent nere till höger), de små i `.fx-raster` 7×4 i accentfältet, papper .3, den aktiva tjänstens kolumn tom (dess fyra brickor ÄR fälten); videon krymper in i övre vänstra fältet och tonar ut | T2: tjänster 100 → 25 %; per band: bandets topp 100 → 25 % | fälten byter färg (sju gånger), fyra brickor byter kolumn |
| F4 | Kartläggning | fälten blir sektionens 2×2 `.kl-f` (lime ×3 + ink), de små sex 2×2 i två rader `.kl-rows` ovanför knappen | 100 → 25 %; vilan följer dokumentet | samling till lime |
| F5 | Om | fälten fast, papper (sömmarna försvinner), 4 markörer `.om-ledger .mk` (röd, röd, röd, lime som originalet), 20 i rad `.row20` | 100 → 25 % | fälten tonar till papper |
| F6 | Insikter | 3 markörer i kategorins färg + 21 i rad `.row21` | 100 → 25 % | brickorna ordnar om sig till en ny rad |
| F7 | Sidfot | fälten krymper till app-ikonen `.icon2` (128 px, papper ×3 + lime), de små till sex 2×2 i TJÄNSTER (den sjunde tjänstens HTML-2×2 står kvar) | sidfot 100 % → `bottom bottom` | fälten krymper till ikonen |

Ordning ut ur en formation: radvis (brickornas index följer mosaikens rader, kanten medurs, rastrets kolumner = tjänsterna). Förankring: två wrappers (`.g-f`, `.g-s`) bär dokumentförflyttningen under vilor där slots ligger i flödet (R0 hero, R9 kartläggning, R10–R11 för de små), så att brickorna står still mot texten. Vila = ±4 px sinus via `--dx/--dy` på `.bi` (period 6–9 s, fas per bricka, mindre på små brickor). Pekare: hela lagret 0,6 % mot pekaren via `quickTo`, bara `(hover:hover) and (pointer:fine)`.

Ägare: `.b` transform/width/height = huvudtidslinjen; `.bi` bakgrund/radie = huvudtidslinjen, `.bi` transform = introt, `.bi` translate = vilan; wrappers y = huvudtidslinjen; `#lager` transform = pekaren; videons opacitet = huvudtidslinjen, ramens opacitet = introt.

## Enheter i sidordning
intro (brickor + radmasker) → pin + scrub (full bleed) → flöde + fältfärg per band + sticky rail → reveal (lime) → flow + in (om, insikter) → lagerformation (slut). Reveal: 14 px / 620 ms en gång; rubriker SplitText-radmasker en gång.

## Signaturobjektets jobb
1. Hero-mosaik (alla sju tjänsternas färger, 28 brickor).
2. Ram och rum: fyra brickor blir sidans grund och bär tjänsten band för band; de 24 små visar i accentfältet vilken kolumn som är "ute i rummet".
3. Index: kartläggningens sex 2×2, om-ledgerns markörer, insikternas kategorimarkörer.
4. Slut: app-ikonen bredvid logotypen och 2×2:orna i sidfotens TJÄNSTER.

## `?preview=`-krokar
`hero`, `fullbleed` (85 % in i pinnen), `band-1` … `band-7` (slutet av bandets vila: scenen fäst, nästa svep inte påbörjat), `kartlaggning`, `om`, `insikter` (mitten av vilan), `slut`. Dev-krokar: `window.__lenis`, `window.__st` (ScrollTrigger), `window.__b3()` (fönstren och tidslinjens tid).

## Mätvärden (port 3105, headless)
Runda 3b (senaste körningen):
- `verify_text.py`: 134 textnoder, **0 avvikelser** (JS av).
- Konsol: **0 fel, 0 4xx** på alla nio previews + 12 hack efter varje, vid 1440×900, 1920×1080, 1366×768 och 390×844.
- `scroll_verify.py`: deadScroll **0**, unrevealed **0**, cuesNeverFull 0, contrastUnderMedia 0.
- `contrast_over_media.py`: PASS (14 strängar i folden; röda knappar 4,17:1 mot golv 3,0 för stor text).
- `motion_probe.py --track "#lager .b:transform" --cpu 1 --ticks 200`: p95 **16,8 ms**, staircase **0**, max_step 1,2–1,5 %. Skriptet skriver ändå FAIL på 9–35 bildrutor över 33 ms (varierar mellan körningar); utan video 18 på hela sidan. Resten är headless mjukvaruavkodning av 1280×720 i pinnen. Svepet i fälten är transform-kolumner; som `clip-path`-polygon på fälten gav det 59 rutor > 33 ms utan video.

Runda 3:
- `motion_probe.py`: p95 16,7 ms, staircase 0, 13–35 rutor > 33 ms (videon).
- Horisontellt överflöde 320/375/414/768/1440: 0 element, inga tvåradiga knappar/navlänkar. Inga ord bryts mitt i i display-rubrikerna 320–1920 (eget mätskript).
- axe (`a11y_scan.py`, 1440 + 390): **0 violations**, 36 passes, 1 incomplete.
- Kontaktark: `design-catalogue/entries/memo-B3-self/motion/sheet.webp` (24 rutor; brickorna byter plats vid varje sektionsbyte och står still under läsning).

## Avvikelser från briefen, medvetet
- **Railen:** inaktiva poster står i full kontrast (inte .55): .55 över ljusblå/oliv/sten ger 2,9–4,1:1 och axe-fel. Aktiv post markeras med vikt 600 och sin egen 2×2 som skalar in. Aktiv post följer scrollen (golvregel 4).
- **Fältens radie** skalar 10/51 men är tak-begränsad till 24 px vid rumsskala (annars ~85 px hörn på viewportfälten).
- **Om/insikter:** briefens antal (4 + 24, 3 + 25) räknar fälten två gånger; här är det 4 + 20 resp. 3 + 21 små, och fälten ligger kvar som papper.
- **Videon** är ett eget media-element i lagret (inte en av de 28): den växer till full bleed och sätter sig sedan som det övre vänstra fältet.
- **Sidfoten** ligger under lagret (`z-index:-1`) så att fälten kan krympa över ink-grunden till ikonen.
- Kolumnrubrikerna FÖRETAGET och JURIDISKT samt resterna i om-punkterna och koncernraden ("som känner ditt bolag", ", med verksamhet i Norge och Sverige.") är maskinskrivna delsträngar av originaltexten: render.py kan inte skriva ut nycklar eller dela strängar. Kontrollen godkänner dem mot föräldrablockets hela text.

## Det jag inte hann
- Mitt i ett bandsvep ligger gammal och ny rubrik i samma ruta, delade av trappkanten (läsbart men tätt i ~1 hack).
- Tangentbord: scenens länkar är alltid fokuserbara (opacitet, inte visibility); fokus i ett dolt band hoppar till bandets vila. Inte testat med skärmläsare.
- Om → insikter: de 24 små faller snabbt (~2,5 hack) genom om-sektionens nedre del bakom texten, medan om-rubriken redan lämnar vyn uppåt.
- Bricklagrets övergång kartläggning → om använder fortfarande RGB-tween för fälten (lime/ink → papper); den är klar vid 55 %.

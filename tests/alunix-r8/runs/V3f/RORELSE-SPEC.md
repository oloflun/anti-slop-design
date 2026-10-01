# V3f · runda 3 · rörelsen

**Greppet, i en mening:** rutverket **monterar sig självt**. Skarvarna ritas, cellerna
fylls, rastret löses upp i färg ruta för ruta, och den stora typen glider förbi
viewportkanten, allt bundet till scrollen och drivet av Lenis och GSAP ScrollTrigger.

Rörelsen hämtar från fler referenser än kompositionen gjorde:
- `aspensearch-com` (primär): cellen som enhet. Allt rör sig *i* sin cell eller *längs*
  sin skarv, aldrig fritt över sidan.
- `cyphr-studio`: rutmönsterupplösningen mellan platt yta och foto. Här blir det
  dither → färg via GSAP:s grid-stagger.
- `exoape-com` (V3e-studien): monumental typ som skärs av viewportkanten och rör sig
  horisontellt med scrollen.
- `area17-com`: ett stort fotofält som redan står stilla medan typen rör sig över det.

## 0. Motorn (en gång, överst i skriptet)

- Vendorat: `assets/vendor/{gsap,ScrollTrigger,SplitText}.min.js` (3.15.0), `lenis.min.js`
  + `lenis.css` (1.3.26). Inga CDN-anrop i runtime.
- Lenis med `autoRaf:false`, driven av `gsap.ticker`, `lagSmoothing(0)`,
  `lenis.on('scroll', ScrollTrigger.update)`. Följ **lenis-skillen** ordagrant för
  kopplingen. `scroll-behavior:smooth` får inte finnas i CSS.
- Ankarlänkar går via `lenis.scrollTo`. Iframes får `data-lenis-prevent` om skillen
  säger att det behövs för att hjul över en inbäddning ska rulla inbäddningen.
- `ScrollTrigger.refresh()` efter `document.fonts.ready`, efter att varje bild laddats och
  efter varje iframe-`load`.
- `gsap.matchMedia()` med två grenar: `(min-width:768px)` och `(max-width:767px)`.
  På mobil: ingen pin, samma koreografi fast kortare och bara scrub.
- Rörelse spelar alltid (F-011). Ingen `prefers-reduced-motion`-grind.
- Animera bara `transform`, `opacity` och `clip-path`. Inga layoutegenskaper.
- Den nuvarande egna `update()`-loopen ersätts. Iframe-monteringen ligger kvar, men den
  anropas nu från Lenis scroll-event (samma svep-princip: alla iframes som är inom ±1
  viewport monteras, också vid hopp).

## 1. Laddning · heron sätts ihop (≤ 1,4 s, spelas en gång)

1. Skarvarna (1 px) ritas från korsningen i mitten, `scaleX`/`scaleY` från 0.
2. De fyra cellerna tänds i en diagonal (ÖV, sedan ÖH+NV, sedan NH) med `clip-path`
   som öppnar sig från skarven, inte från kanten.
3. h1: SplitText på rader med mask. Raderna reser sig ur sin mask med stagger 0,08
   och `power4.out`.
4. Kortet faller in ovanifrån, landar på skarven med en kort övertagning (−3° → 0°).

## 2. Heron under scroll (pin på desktop, ~120 % viewport)

Ersätter den nuvarande CSS-sticky-scenen på 190svh. En scrubbad tidslinje (`scrub:0.6`):
- Kortet vänds 180° (`rotateY`) och lyfts mitt i vändningen (skala 1,04, skuggan växer).
- ÖH- och NV-rastren parallaxar åt motsatta håll (`yPercent` ±8), inuti sina celler med
  overflow hidden.
- h1-raderna glider uppåt i olika takt, så att översta raden skärs av cellens överkant
  först (exoape).
- Sist: mintcellen (NH) sveper in över kortets bas. Kortet står då kvar som ett objekt på
  mint, och pinnen släpper.

## 3. Upplösningen · dither → färg (alla bildceller utom heron)

Varje bildcell får ett rutnät av tiles över färglagret (12×8 desktop, 6×6 mobil). Varje
tile är ett utsnitt av dithervarianten (`background-position`). GSAP:
`stagger:{grid:[rows,cols], from:'random', amount:0.9}` på `opacity` → 0, bundet till
cellens scroll (`start:'top 85%'`, `end:'center 55%'`, `scrub:true`). Tillbakascroll
bygger rastret igen. Detta ersätter clip-path-svepet.

## 4. Tesen

- `Det första intrycket är digitalt.`: SplitText på ord. Hela raden förskjuts
  horisontellt med scrollen (`xPercent` 0 → −18, scrub), så att sista ordet skärs av
  högerkanten och glider in. Tecknen reser sig en gång vid entré.
- De tre meningscellerna: raderna reser sig ur mask när cellen når 80 %, med stagger. Varje
  cells bakgrund fylls från sin vänstra skarv (`clip-path`).

## 5. Processen

- Vänsterkolumnen står sticky som nu. En mintfärgad **framstegslinje** på 2 px längs
  skarven mellan kolumnerna fylls med scrollen genom de sju stegen (`scaleY`, scrub).
- Varje steg: aktivt steg (närmast viewportens mitt) har vit text, övriga dimmas till
  `#6b6b6b`. Indexet (01–07) byts med en kort vertikal rullning.
- Processbilden löses upp enligt § 3.

## 6. Exempelcase

- Ordet `Exempelcase` kommer in från höger med scrollen (`xPercent` 20 → −6, scrub) och
  skärs av kanterna under rörelsen.
- Tumnaglarna har inre parallax (bilden `yPercent` −10 → 10 i sin cell) plus upplösning
  enligt § 3.

## 7. Calyx och Hōrai

- Inbäddningscellen öppnas från skarven mot sidotexten (`clip-path: inset(0 100% 0 0)`
  → 0, eller spegelvänt för Hōrai) när sektionen når 75 %.
- Caseshuvudets färgcell fylls längs samma skarv. Namnet reser sig tecken för tecken.
- De fem raderna tänds i ordning när de passerar 80 % (`ScrollTrigger.batch`).

## 8. Priset

- Bento-cellerna glider på plats från sin gemensamma skarv: huvudcellen från vänster,
  stödcellerna från ovan och nedan. Kort och tätt, `power3.out`.
- Siffrorna `26 900` och `38 900` räknas upp en gång vid entré. Mellanslaget som
  tusentalsavgränsare och `tabular-nums` bevaras, så bredden står still.

## 9. Kontakten och footern

- Jätterubriken reser sig på rader (scrub). Bildcellen löses upp enligt § 3.
- Kortet i kontakten kommer in från höger och vänds en gång från framsida till baksida
  vid entré, som ett eko av heron.
- `ALUNIX` i footern: bokstäverna reser sig underifrån, skurna av nederkanten, i stagger
  med scrub medan footern kommer in.

## 10. Spärrar

- Slutläget för varje animation är exakt den statiska layouten från runda 2. Ingen text
  får bli kvar dold om man stannar mitt i sidan. Verifiera genom att hoppa direkt
  (`lenis.scrollTo(target,{immediate:true})`) till varje sektion.
- Ingen horisontell overflow vid 390/768/1440/1920, varken under eller efter animation.
  Typ som glider förbi kanten klipps av `overflow:clip` på sin sektion.
- Copy-diffen från runda 2 ska fortfarande vara ren. SplitText får inte ändra den synliga
  texten (kontrollera att `aria-label`/sr-texten finns kvar eller att SplitText körs med
  `aria:'auto'`).
- Rör inte komposition, färg eller copy. Bara rörelse.

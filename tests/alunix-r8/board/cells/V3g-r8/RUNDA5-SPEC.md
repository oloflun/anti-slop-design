# V3f · runda 5 · läsbarhet, casevalet och kontakten

Antons dom 2026-09-24 efter R4: "nästan perfekt", bättre och mer unik än V3d. Fyra
ändringar, i den här ordningen. Komposition, färg och copy i övrigt rörs inte.

## A. Rubriker ska gå att läsa

Fel: de stora rubrikerna klipps, och `Det första intrycket är digitalt.` hinner man knappt se.

Regel för hela sidan: **varje rubrik står helt synlig, utan att någon glyf skärs av en kant,
under minst 40 vh scroll.** Rörelse får ske före och efter det fönstret, aldrig i det.

- **Tesraden:** pinna tesens övre cell på desktop i ~90 vh. Raderna reser sig och står sedan
  stilla och hela i minst 50 vh. Därefter släpper pinnen. Den horisontella drivningen tas
  bort helt, och inget ord skärs av högerkanten i något läge. Mobil: ingen pin, raderna
  reser sig och står.
- **Heron:** h1 får inte drivas ut ur sin cell förrän kortvändningen är klar (sista 25 % av
  pinnen). `visitkort` ska synas helt under hela vändningen.
- **`Exempelcase`:** får aldrig skäras av vänster- eller högerkanten. I viloläget ryms hela
  ordet i sin cell, och inslaget sker med `yPercent` ur mask, inte med `xPercent`.
- Kontrollera alla `headline-40`/`headline-50` på sidan mot regeln, även pris och kontakt.

## B. Casevalet och den valda showcasen

Fel: tumnaglarna är statiska, suddiga och inzoomade (lågupplösta skärmbilder uppskalade till
140 vh). Calyx-sektionen efteråt blir en konstig dubblett, och inbäddningarna scrollar inte
nedåt i sajterna medan texten löper, som de gjorde i V3d.

Ny form, som ersätter både tumnagelraden och de två separata case-sektionerna:

### B1. Väljaren (sektionen `#exempelcase`)
- `Exempelcase` på egen rad, som nu (se A).
- Under ordet står två celler 6+6. Varje cell är en **knapp** (`<button>`, `aria-pressed`,
  Enter/Space) med:
  - en **skarp, utzoomad** bild av sajtens första vy: hela 1440×900-vyn syns, ingen beskärning
    som zoomar in.
  - namnet och undertiteln under bilden, exakt samma strängar som V3d (`Calyx` /
    `Florist, Stockholm`, `Hōrai` / `Restaurang, Asian Fusion`).
- **Bilderna:** ta nya skärmbilder av `/sites/calyx.html` och `/sites/horai.html` med
  Playwright i 1440×900, `deviceScaleFactor:2`. Spara som WebP (kvalitet ~82) i
  `assets/cases/`. Kontrollera skärpan genom att öppna bilden, inte genom filstorleken.
- **Hover** (bara `(hover:hover)`): bilden skalas 1,00 → 1,04 inuti sin cell (overflow
  hidden), ~700 ms ease-out, och grannen tonas till 0,85. Fokus-visible får samma zoom och
  en 2 px mintram. Ingen hover på touch.
- Vald cell markeras med en 4 px mintlinje längs cellens nederkant.

### B2. Showcasen (ny sektion `#showcase`, direkt efter väljaren)
- Förladdad med **Calyx**, så att den som scrollar förbi utan att välja ändå får en showcase
  och ingen död väg finns. Ett val byter innehåll.
- Vid val: markera cellen, byt panel, montera iframen, kör `ScrollTrigger.refresh()` och
  sedan `lenis.scrollTo('#showcase', {duration:1.2})`. Användaren låses in, eftersom
  showcasen är pinnad.
- **Desktop:** pinnad scen, `end: '+=' + (antal ankare × 100) + 'vh'`.
  - Vänster 7 kolumner: den levande sajten i en 1440 px bred iframe, skalad med
    `transform:scale()` så att den fyller cellen skarpt (ingen omskalning av en bild).
    `pointer-events:none`, så att hjulet går till sidan.
  - Sajtens **inre scroll** styrs av pinnens progress. Porta V3d:s `measureCase` och `caseY`
    och deras ankare exakt:
    - Calyx: `['top',0], ['#studio',0], ['#studio + section',0,48,700], ['#index',0], ['#commission',0]`
    - Hōrai: `['top',0], ['#hero-section + section',0.30], ['#quote-section','center',-100,700], ['#quote-section + section',0], ['#reservations',-1], ['#reservations',0]`

    (V3d: `tests/alunix-r8/runs/V3d/index.html` rad ~3248–3345.) Skriv med
    `contentWindow.scrollTo({top:y, behavior:'instant'})`, bara när y ändrats ≥ 0,5 px, och
    mät om vid iframe-`load` och resize.
  - Höger 5 kolumner: casehuvudet (namnet i `headline-40`, undertiteln mono, casets färg som
    fyllning) och under det casets textrader (5 för Calyx, 6 för Hōrai). **Rad k dyker upp
    när sajten når ankare k**: den reser sig ur mask. Tidigare rader står kvar men tonas till
    0,55, så att den aktiva syns. Rad 0 är synlig från start.
- **Mobil (<768):** ingen pin. Iframen står `position:sticky` överst i 56 svh, och raderna
  scrollar under den. Varje rads `onEnter`/`onEnterBack` tweenar sajtens inre scroll till
  radens ankare (0,6 s).
- Den inaktiva panelen har `display:none` men ligger kvar i DOM, så att copy-räkningen mot
  V3d blir oförändrad. De gamla `#case-calyx`- och `#case-horai`-sektionerna tas bort. Deras
  text flyttar in i panelerna, ordagrant.
- Ankarlänkar eller hopp till `#showcase` ska fungera, och iframen ska monteras vid hopp.

## C. Kontakten · "kortet lämnas över"

Fel: ingen tydlig tanke, bara en stor rubrik, ett kort och död svart yta.

Greppet: kontakten är **heron speglad**, ett bokstöd. Sidan öppnar med att visa vårt kort
och stänger med att lämna över det. Här är det besökaren som vänder kortet.

- Sektionen är en 2×2-kvadrant i `100svh`, samma proportioner som heron men inverterad:
  - ÖV svart: `Berätta om er verksamhet.` (headline-40, vit) plus dess befintliga underrad.
  - ÖH vit, tom.
  - NV bildcell: `k1-stage-pool` som löses upp dither → färg (samma motiv som heron, nu i
    färg: ramen var rastrerad, avslutningen är skarp).
  - NH mint.
- **Kortet** ligger på korsningen av skarvarna, i samma storlek och med samma skugga som i
  heron, med framsidan upp.
  - Det är en `<button aria-label="Vänd kortet">`. Etiketten är ett tillgänglighetsnamn, inte
    synlig text, och räknas inte i copy-diffen.
  - Hover (desktop): kortet lutar mot pekaren i 3D, ±8° (`rotateX`/`rotateY` via
    `gsap.quickTo`, perspective 1200 px).
  - Klick, Enter eller Space vänder det 180° med en kort lyftning.
  - **Baksidan** bär `Alunix`, `Digital byrå`, `Design Utveckling System` och de två
    **riktiga länkarna** `kontakt@alunix.se` (mailto) och `Boka ett möte`. Den separata
    knappraden under kortet tas bort; länkarna bor på kortet.
- **Fail toward visible (husregel 10):** har kortet inte vänts när sektionens scroll-progress
  når 0,7, vänder det sig självt. Vid hopp direkt till `#kontakt` eller till sidans botten
  visas baksidan. Länkarna får aldrig vara oåtkomliga.
  - Baksidans länkar är fokuserbara bara när baksidan syns (`inert` på den dolda sidan).
- Mobil: kvadranten staplas (ÖV, kortcell på mint, NV). Kortet är 88 % av bredden, tryck vänder
  det, och samma självvändning gäller.

## D. Verifiering (byggaren först, sedan leaden i pixlar)

- Läsbarhetstest för A: för varje `headline-*`, mät hur många px scroll den står helt inom
  viewport med alla glyfer oklippta (`getBoundingClientRect` på varje rad mot sin närmaste
  klippande förälder). Krav ≥ 40 vh.
- Väljaren: klick på Hōrai ska ge scroll till `#showcase`, pinnen aktiv, Hōrai-panelen synlig
  och sajtens inre `scrollY` ändras över pinnen och träffar alla sex ankare (±2 px). Tangent:
  Tab till Calyx, Enter, samma kontroll. Hopp direkt till `#showcase` utan val ska visa Calyx.
- Kontakt: klick vänder kortet, och länkarna blir klickbara. Hopp till botten visar baksidan.
  Tab når båda länkarna.
- 0 px överflöd vid 390/768/1440/1920, 0 konsolfel, copy-diffen oförändrad eller bättre.
- Skärmbilder med riktig hjulscroll i `shots/r5/` (1440 och 390), plus hovertillstånd och en
  mellanbild av kortvändningen.

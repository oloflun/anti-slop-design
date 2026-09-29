# V3g · showcasen blir mjuk · spec R1

V3g är en kopia av V3f. **Bara `#exempelcase` → `#showcase` rörs.** Komposition, färg, copy och
alla andra sektioner är orörda. V3f står kvar som arm A.

Antons dom 2026-09-24: rubrikerna och kontakten blev bättre. Men klicket ger en hård övergång,
besökaren låses in i ett hackigt scroll-fängelse där exempelsidan hoppar, och listan bredvid
är statisk trots att markeringen byts. Han vill att allt blir mjukare och att det provas med en
**ruta med text bredvid som byts ut och tonar över till nästa**, som i V3d men i V3f:s stil.

## Grundorsaker i V3f (rättas alla)

| # | Orsak | Var | Rättning |
|---|---|---|---|
| 1 | `activateCase` dödar och återskapar pinnen synkront vid klicket, före `lenis.scrollTo` | `setupDesktopEngine`, r. ~1306–1360 | Pinnen skapas EN gång vid init och dödas aldrig |
| 2 | Hōrai-iframens `src` sätts först vid klick, vilket ger en navigation under övergången | `activateCase` | Båda iframes laddas vid `requestIdleCallback` efter `load` |
| 3 | Två utjämningslager: Lenis `lerp:0.1` + `scrub:0.6` | ScrollTrigger.create | `scrub:true`. Lenis är det enda lagret |
| 4 | `caseY` rör sig på 45 % av segmentet och står still 55 %, vilket ger ryck och stopp | r. 1265–1270 | Ny kurva, se B |
| 5 | Listan är ett dragspel som knäpper med klass vid heltalsgränser | `setRowState` + CSS `.row-body` | Textrutan i C, skrubbad övertoning |
| 6 | Pinlängden räknas om per case, så ett byte kräver `refresh` | `end: n × innerHeight` | Fast längd, se A |

## A. Pinnen och entrén

- **En** ScrollTrigger för `#showcase` skapas vid init (desktop ≥ 768, via `gsap.matchMedia`):
  `pin:'.showcase-stage'`, `scrub:true`, `start:'top top'`,
  `end: () => '+=' + Math.round(6 * 0.75 * window.innerHeight)`, `invalidateOnRefresh:true`.
  - Längden är densamma för båda casen: 6 segment à 75 vh. Calyx med 5 ankare fördelar sina
    segment över samma längd.
  - `onUpdate` läser ett **aktuellt case** `C` ur en variabel. Ett casebyte byter variabeln, och
    pinnen rörs aldrig.
- **Klick på ett case** (`activateCase`):
  1. `aria-pressed`, `inert` och panelernas synlighet sätts.
  2. Panelen och iframen tonas över: den gamla ut på 0,3 s, den nya in på 0,35 s,
     `power2.out`, interruptibelt (`overwrite:'auto'`). Ingen `display:none` förrän utgången
     är klar.
  3. `C` byts och `updateShowcase(C, st.progress)` körs.
  4. `lenis.scrollTo('#showcase', {duration:1.4, easing: t => 1 - Math.pow(2, -10*t)})`.
  5. **Ingen `ScrollTrigger.refresh()` i klicket.** Behövs en mätning görs den i iframens
     `load` och vid resize, som i dag via `safeRefresh`.
- **Om iframen inte hunnit ladda vid klick:** casets skärmbild (`assets/cases/<case>-1440.webp`)
  står som affisch i ramen tills `load`. Därefter tonas iframen in på 0,3 s.
- Hopp direkt till `#showcase` utan val visar Calyx, som i V3f.

## B. Sajtens rörelse: `caseY` utan ryck

- Segment k (k = 1 … n−1) äger progressintervallet [k/n, (k+1)/n] och löper så här:
  - **första 50 %:** sajten glider från ankare k−1 till ankare k med `sine.inOut`. Hastigheten
    är noll i båda ändar, så inga ryck;
  - **sista 50 %:** sajten står still på ankare k, i läsfönstret.
  - Segment 0 är bara vila på ankare 0.
- Skrivningen behåller V3f:s `contentWindow.scrollTo({top:y, behavior:'instant'})` med
  0,5 px-tröskeln och drivs från ScrollTriggerns `onUpdate`. Ingen egen rAF-loop.
- **Experiment, bara om p95 i D inte nås:** flytta iframe-dokumentets rot med `transform` i
  stället för att scrolla. Mätt 2026-09-25: klientsajterna har `vh`-höjder (calyx.html:74,
  horai.html:157, 287) och en `position:fixed`-kornyta, så en iframe i full dokumenthöjd är
  utesluten. Välj inte experimentet utan mätning.

## C. Textrutan (ersätter dragspelet, bara desktop)

Högerkolumnens casehuvud (`.showcase-head`, rost/lack) står kvar. Under den ersätts
`.showcase-rows` av **en enda cell**, rutan, som fyller resterande höjd.

- **Rutans yta:** Calyx på `--paper`, svart text. Hōrai på `--black`, `--paper`-text och
  brödtext `#bdbdbd`. `padding: var(--cellpad)`, radie 0.
- **Överst i rutan:**
  - en mono-räknare `01 / 05`, uppdaterad när steget byts;
  - under den ett spår, 1 px svart linje (på Hōrai `--paper` på 30 %), där en 4 px mintfyllning
    skalas med `scaleX` kontinuerligt med pinnens progress, alltså alltid levande.
  - Båda är `aria-hidden="true"` (dekor, inte copy).
- **Stegen:** alla `h3` + `p` står staplade i samma gridcell (`display:grid` på behållaren,
  `grid-area:1/1` på varje steg), vertikalt centrerade i rutans resterande höjd.
  - `h3` behåller klassen `h3`, och `p` har samma text och `max-width:52ch`.
  - **Texten ändras inte med ett tecken.** Copy-diffen ska vara oförändrad.
- **Övertoningen** är en GSAP-tidslinje som skrubbas av samma pin via `onUpdate`, eller en
  tidslinje med `scrollTrigger` på samma trigger och `scrub:true`. Inte klass-toggle.
  - Steg k tonas ut i första 25 % av segment k+1 (`opacity 1→0`, `y 0→−12px`).
  - Steg k+1 tonas in i nästa 25 % (`opacity 0→1`, `y 12→0`).
  - Steget står helt still i resten av segmentet. Varje steg syns helt i ≥ 40 vh
    (75 vh × 75 %).
  - Bara `opacity` och `transform` animeras.
- **Tillgänglighet:** inaktiva steg får `aria-hidden="true"` och `visibility:hidden` när deras
  opacity är 0, så att skärmläsare och Tab bara når det synliga steget.
  - Växlingen görs i `onUpdate` när steget byts, inte per bildruta.
  - Under `prefers-reduced-motion` gäller F-011 (rörelse spelar alltid) som i V3f. Behåll V3f:s
    beteende.
- **Mobil (< 768):** V3f:s staplade rader under den sticky iframen behålls. Den aktiva raden står
  i opacity 1 och de andra i 0,45, med `opacity`-tween 0,35 s i `onEnter`/`onEnterBack`.
  Kontrast: 0,45 får inte ge brödtext under 4,5:1 — mät; höj till den nivå som klarar det.

## D. Verifiering (byggaren först, sedan leaden i pixlar)

Server: `python "C:/Users/Anton L/.agents/skills/design/scripts/serve.py" --port 3305 --root .`
från `C:\Users\Anton L\anti-slop-design`.

1. `python tests/alunix-r8/showcase_probe.py http://127.0.0.1:3305/tests/alunix-r8/runs/V3g/index.html tests/alunix-r8/runs/V3g/shots/probe-r1-1440 --width 1440 --headed`,
   och samma på 390. Jämför med `runs/V3f/shots/probe-baseline-*/result.json`. Krav:
   - p95 bildrutetid i klickfönstret och genom showcasen ≤ 20 ms, eller tydligt bättre än
     baslinjen om miljön inte når 20 ms;
   - största enskilda `scrollY`-hopp i klickfönstret under baslinjens;
   - `stall-then-lurch` = 0.
2. `python tests/alunix-r8/runs/V3g/verify_motion.py`, där `showcase_check` visar:
   - alla ankare ±2 px;
   - tangentbordsvägen (Tab till Hōrai, Enter);
   - hopp direkt till `#showcase`.
   Uppdatera kontrollen där den förutsätter dragspelets `is-active`-rader, så att den i stället
   läser vilket steg som syns i rutan.
3. `python tests/alunix-r8/runs/V3g/verify.py`: copy-diffen `passed: true`, 0 px överflöd vid
   390/768/1440/1920, 0 konsolfel.
4. Bildsekvensen efter klick (60/150/250/400/800/1400 ms) och `sheet.png` ur proben.
   `lead_motion_capture.py` 1440 och 390 mot board-cellen.
5. Rapportera siffrorna före och efter i `runs/V3g/RAPPORT.md`. Leaden läser bilderna själv.

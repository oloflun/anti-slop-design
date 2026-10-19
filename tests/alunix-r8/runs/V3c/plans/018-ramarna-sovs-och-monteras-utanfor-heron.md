# 018 · Ramarna: sövs när de är utanför skärmen, monteras utanför heron, reveal på rätt element

- **Status**: TODO (R6, först)
- **Commit**: R5-läget av `runs/V3c/index.html`, 1 520 rader, md5 `fcbee8f1`
- **Severity**: HIGH (funktion: sidan tappar bildrutor; två deklarerade devices döda)
- **Category**: Performance + Purpose (H-21, H-22, H-24)
- **Estimated scope**: 1 fil, ~12 rader CSS/JS, 4 attributflyttar
- **Källor**: design-perf-reviewer fix 1, 2 (rotorsak mätt: ramarna 8 648 av 13 164 ms tasktid, 66 %; layout 2 374 → 117 ms med ramarna sövda); codex-review (Astra) fynd 2a (båda ramarnas `data-sc-reveal` registreras aldrig, motorn söker bara efterkommande, `scroll/scrollcraft.js:392`)

## Problem

Perf-rapportens attribution (median av tre, cpu 4, 100:60, 3 000 px genom `#process`):
som byggd task 13 164 ms, 93 av 110 rutor > 33 ms; med ramarna sövda (`content-visibility:
hidden` på wrapparna) task 4 516 ms, layout 2 374 → 117 ms, script 1 150 → 218 ms. R4:s och
R5:s rotorsaksjakter kördes med `/sites/**` blockerat och såg därför aldrig posten. Ramarna
monteras vid `rootMargin: '100% 0px'`, alltså vid scrollY ≈ 2 560, 500 px inne i
kortvändningen (p95 genom heron 435,9 ms med ramarna, 66,7 ms utan), och observern kopplar
bort sig (`obs.unobserve(f)`) så inget söver dem igen. Calyx och Hōrai kör sina egna
scrollmotorer på huvudtråden resten av sidan.

Dessutom: `data-sc-reveal` sitter på samma `<figure>` som `data-sc-act`. Motorn letar
reveal-mål bland aktens efterkommande, aldrig på aktelementet, så båda ramarnas reveal är
döda (två DEAD-rader mot H-24). `?preview=`-bilderna visade ramarna ändå, eftersom ett
oregistrerat reveal-element aldrig göms.

```css
/* index.html:557-559 - current */
  .frame-wrap{position:relative;line-height:0;overflow:clip;flex:1;}
  .calyx-wrap{min-height:90dvh;background:#e9e5da;
    content-visibility:auto;}
/* index.html:673-674 - current */
  .horai-wrap{min-height:80dvh;background:var(--invert);
    content-visibility:auto;}
```

```html
<!-- index.html:988-989 - current -->
      <figure class="frame-fig calyx-fig" data-sc-act="flow"
              data-sc-reveal="up" data-sc-reveal-at="0.02 0.3">
        <div class="frame-wrap calyx-wrap">
<!-- index.html:1063-1064 - current -->
      <figure class="frame-fig horai-fig" id="projekt" data-sc-act="flow"
              data-sc-reveal="iris" data-sc-reveal-at="0.1 0.55">
        <div class="frame-wrap horai-wrap">
```

```js
/* index.html:1378-1385 - current */
      var io = new IntersectionObserver(function(entries, obs){
        for (var i = 0; i < entries.length; i++){
          if (!entries[i].isIntersecting) continue;
          var f = entries[i].target;
          obs.unobserve(f);
          defer(mountFrame.bind(null, f));
        }
      }, { rootMargin: '100% 0px' });
```

## Target

Tre saker, mätbara var för sig.

**A. Sova.** En ram som är mer än en viewport från skärmen får `content-visibility:hidden`
på sin wrapper (klassen `.is-asleep`), satt och borttagen av observern, som aldrig kopplas
bort. `content-visibility` är varken `transform` eller `opacity`, så PRODUCT.md:s regel att
en visad ram aldrig transformeras eller tonas står (perf-rapporten säger samma sak).
`min-height` på wrapparna står kvar så att en sovande ram inte ändrar höjd (CLS 0).

```css
/* target, efter index.html:559 */
  /* PLAN 018. En ram som är mer än en viewport bort sövs: content-visibility
     hindrar dess dokument från att layouta och måla, utan att röra ramen
     (ingen transform, ingen opacity, ingen src-ändring). Mätt av
     perf-granskaren R5: task 13 164 -> 4 516 ms, layout 2 374 -> 117 ms. */
  .frame-wrap.is-asleep{content-visibility:hidden;}
```

```js
/* target, index.html:1378-1385 */
      var io = new IntersectionObserver(function(entries){
        for (var i = 0; i < entries.length; i++){
          var f = entries[i].target, wrap = f.parentNode;
          if (entries[i].isIntersecting){
            wrap.classList.remove('is-asleep');
            if (f.hasAttribute('data-src')) defer(mountFrame.bind(null, f));
          } else if (!f.hasAttribute('data-src')){
            wrap.classList.add('is-asleep');
          }
        }
      }, { rootMargin: '40% 0px' });
```

En ram som ännu inte monterats får aldrig klassen (den kostar inget), och en monterad ram
får den bara när den är utanför marginalen. Ingen ram avmonteras någonsin.

**B. Montera utanför heron.** `rootMargin` 100 % → **40 %**: Calyx-ramen monteras då vid
scrollY ≥ ~3 100 vid 1440x900, alltså när heron har `--sc-ps` ≥ 1,0 (pinnad resa 2 160 px
efter plan 011 + fold), aldrig inne i vändningen. Mål: p95 genom heron (`--wheel 100:60`,
45 ticks, cpu 4) ≤ 70 ms.

**C. Reveal på rätt element.** `data-sc-reveal`/`data-sc-reveal-at` flyttas från
`<figure>` till `.frame-wrap` inuti figuren; `data-sc-act="flow"` står kvar på figuren.
Motorn rörs inte. Ramen själv transformeras fortfarande aldrig: revealen ligger på
wrappern, som den alltid var tänkt (`index.html:551-556` kommentar).

```html
<!-- target, index.html:988-990 -->
      <figure class="frame-fig calyx-fig" data-sc-act="flow">
        <div class="frame-wrap calyx-wrap" data-sc-reveal="up" data-sc-reveal-at="0.02 0.3">
<!-- target, index.html:1063-1065 -->
      <figure class="frame-fig horai-fig" id="projekt" data-sc-act="flow">
        <div class="frame-wrap horai-wrap" data-sc-reveal="iris" data-sc-reveal-at="0.1 0.55">
```

Motorns reveal-regel promoverar `[data-sc-reveal]` med `will-change` (R3-fyndet, rad
549-556): `.frame-wrap{will-change:auto}` läggs till på rad 557 så promoveringen inte
vandrar från figuren till wrappern.

## Repo conventions to follow

- Ramarna: `loading="lazy"` + `data-src` + IntersectionObserver + `requestIdleCallback`
  (`index.html:1358-1385`) behålls; bara callbacken och marginalen ändras.
- `content-visibility:auto` finns redan på `.calyx-wrap`/`.horai-wrap` (rad 559, 674) och
  `.price` (rad 589); `hidden` är samma mekanism i tvingat läge.
- Ledgerrad: skriv i `BRIEF.md` § Byggarens rader, R6: "ramarna sövs utanför 40 %,
  monteras utanför heron; reveal på wrappern; källa perf-rapport R5 fix 1-2, Astra 2a".

## Steps

1. **Mät före** med kontrollen ren (perf-rapportens protokoll: `tests/motion/smooth.html`
   0 rutor > 33 ms omedelbart före): `motion_probe.py --url … --cpu 4 --wheel 100:60
   --ticks 75 --track "section.hero:--sc-ps,#process:--sc-ps"`; spara p95 och rutor > 33 ms
   i NOTES.md. Samma sak med `--ticks 45` (bara heron).
2. Lägg `.frame-wrap.is-asleep{content-visibility:hidden;}` efter rad 559 och
   `will-change:auto` i `.frame-wrap` (rad 557).
3. Byt observern (rad 1378-1385) mot Target A/B.
4. Flytta `data-sc-reveal`/`data-sc-reveal-at` (rad 989, 1064) till respektive
   `.frame-wrap` (rad 990, 1065).
5. **Mät efter**, samma tre körningar. Kontrollera att `[scrollcraft]` i konsolen är tyst
   och att `motion_probe --track ".calyx-wrap:clip-path,.horai-wrap:clip-path"` inte
   rapporterar DEAD (revealen lever).
6. Kontrollera att en sovande ram vaknar: scrolla till Calyx, förbi den till footern,
   tillbaka; ramen är synlig och användbar (musen kan rulla Calyx: nej, ramen är `inert`
   och `pointer-events:none` enligt plan 002; den ska bara synas och animera internt).

## Boundaries

- `src` sätts aldrig om; ingen ram tas bort ur DOM; ingen `transform`/`opacity` på ramen
  eller dess förfäder efter montering.
- `inert` och `pointer-events:none` på ramarna (plan 002) rörs inte.
- Motorn och `.sc-*` rörs inte.
- Matchar inte raderna 557-559, 673-674, 988-990, 1063-1065 eller 1378-1385: STOPPA.

## Verification

- **Mekaniskt:** cpu 4, 100:60, 75 ticks: task-tid (CDP `Performance.getMetrics`, om
  byggaren har perf-granskarens `ablate.py`, annars probens p95) mål p95 ≤ 70 ms genom
  heron och ≤ 110 ms genom `#process`, rutor > 33 ms 196 → ≤ 80 (perf-rapportens
  räkning: ramarna står för ~120 av dem); `perf_probe.py` `long-task-under-scroll` 1 → 0,
  CLS 0,000 vid 390; `scroll_verify.py` 1440: ramarna syns i skivorna där de ska (inga nya
  `unrevealed`).
- **Skärmbilder:** s5 och s6 vid 1440 och 390 med ramarna monterade och vakna; en bild
  vid footern som visar att `.is-asleep` sitter på båda wrapparna
  (`document.querySelectorAll('.is-asleep').length === 2`).
- **Feel check:** vändningen i heron går utan hack när ramarna inte monteras inne i den;
  scrolla ned till Calyx och upp igen två gånger: ramen syns varje gång, inget blinkar.
- **Done when:** talen före/efter i NOTES.md, H-24 bockad för de två reveal-raderna,
  och 019 mäts ovanpå den här (aldrig tvärtom).

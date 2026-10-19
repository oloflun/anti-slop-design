# 027 · Ramarna vaknar aldrig: observern flyttas från ramen till wrappern

- **Status**: TODO (R8, loop 2)
- **Commit**: R7-läget av `runs/V3c/index.html`, md5 `d30355da`
- **Severity**: HIGH (funktionsfel: båda levande sajterna renderas som tomma plattor på hela sidan)
- **Category**: Funktion (livscykel), H-08, H-25, H-27, plan 018/026:s kontrakt; leadens R7-fynd 1
- **Estimated scope**: 1 fil, ~10 rader JS, 0 rader CSS
- **Källor**: leadens pixelläsning R7 (`shots/r7-lead/frames-wait-4600.png`); loop 2: `shots/loop-2/slices-1440/v3c-1440--s04.png`, `s05.png` (Calyx som beige platta, Hōrai som svart platta), `slices-390/v3c-390--s04.png`, `s05.png`; `shots/loop-2/diag/diag3.json` (`A_reader_iolog`, `A_cv_hidden_blind`), `diagA2.json` (12 av 12 stopp med sovande ram i viewporten vid 1440, 10 av 15 vid 390; efter fixen 0 av 12 och 0 av 15), `diag/A2-1440-fix-calyx.png`, `A2-1440-fix-horai.png`, `A2-390-fix-horai.png`

## Problem

Observern (plan 018, 026) observerar **ramen** (`iframe`), men sömnen sätts på **wrappern**
(`.frame-wrap.is-asleep{content-visibility:hidden}`, rad 639). Ett element inne i ett
`content-visibility:hidden`-subträd har ingen box, så `IntersectionObserver` rapporterar
det som inte-korsande med `boundingClientRect` 0x0, oavsett var wrappern står. Loggen
(`diag3.json A_reader_iolog`) visar sekvensen exakt: ramen får `isIntersecting:true` när
den kommer in i 40 %-zonen (t 3052, top 1002, h 810), monteras, och i **samma** callback-
batch en andra post `isIntersecting:false` med `top 0, h 0`: wrappern hade under
föregående frame hunnit få `is-asleep` av en tidigare post, och från den stunden är ramen
boxlös. Callbacken sätter då `is-asleep` igen (`else if (!f.hasAttribute('data-src'))`) och
observern får aldrig mer en korsning: ramen är sövd för resten av sidans liv, även när
wrappern står mitt i viewporten (leadens `frames-wait-4600`: Hōrai top −172, höjd 855,
`is-asleep`). Kontrollen `A_cv_hidden_blind` bekräftar mekanismen isolerat: med wrappern
sövd på skärmen rapporterar en färsk observer `IFRAME: inter false, h 0` men
`DIV.frame-wrap: inter true, ratio 1, h 855`.

Det var plan 026:s korrekta idempotens som gjorde felet permanent: i R6 vaknade ramen av
en slump när `data-src` fortfarande satt kvar (montering utan sömnvillkor); efter 026 finns
ingen sådan väg.

```js
/* index.html:1676-1688 - current */
      var io = new IntersectionObserver(function(entries){
        for (var i = 0; i < entries.length; i++){
          var f = entries[i].target, wrap = f.parentNode;
          f.__visible = entries[i].isIntersecting;
          if (f.__visible){
            wrap.classList.remove('is-asleep');
            if (f.hasAttribute('data-src') && !f.__pending){ f.__pending = true; defer(mountFrame.bind(null, f)); }
          } else if (!f.hasAttribute('data-src')){
            wrap.classList.add('is-asleep');
          }
        }
      }, { rootMargin: '40% 0px' });
      frames.forEach(function(f){ io.observe(f); });
```

## Target

Observern observerar wrappern (`.frame-wrap`), som alltid har en box (`min-height` på rad
631 och 777 står kvar), och läser ramen som `wrap.querySelector('iframe')`. Monteringen,
idle-luckan, `__pending`/`__visible` och `is-asleep`-regeln är oförändrade; `mountFrame`
tar fortfarande ramen.

```js
/* target, index.html:1676-1688 */
      var io = new IntersectionObserver(function(entries){
        for (var i = 0; i < entries.length; i++){
          var wrap = entries[i].target, f = wrap.querySelector('iframe');
          if (!f) continue;
          f.__visible = entries[i].isIntersecting;
          if (f.__visible){
            wrap.classList.remove('is-asleep');
            if (f.hasAttribute('data-src') && !f.__pending){ f.__pending = true; defer(mountFrame.bind(null, f)); }
          } else if (!f.hasAttribute('data-src')){
            wrap.classList.add('is-asleep');
          }
        }
      }, { rootMargin: '40% 0px' });
      frames.forEach(function(f){ io.observe(f.parentNode); });
```

`mountFrame` (rad 1655-1662) rörs inte: `f.parentNode.classList.add('is-asleep')` när
`!f.__visible` är fortfarande rätt, eftersom `__visible` nu sätts från wrapperns korsning.

Uppmätt i sidan med exakt denna logik (`diagA2.py`, observern på ramen avstängd,
wrapperobserver i stället): läsarvandring i 300 px-steg från pinnens slut till
processakten, 1440x900: 0 av 12 stopp med sovande wrapper i viewporten (var 12 av 12);
390x844: 0 av 15 (var 10 av 15). Tillbaka till Calyx efter vandringen: `calyx-wrap` vaken,
`content-visibility:auto`, ramen renderar (`A2-1440-fix-calyx.png`). Vid Hōrai: vaken,
renderar (`A2-1440-fix-horai.png`, `A2-390-fix-horai.png`). Vid scrollY 0 efter allt: båda
`is-asleep` (sömnen fungerar fortfarande). Resurser: exakt en `calyx.html` och en
`horai.html`, ingen `/null` (026 står).

## Repo conventions to follow

- `.is-asleep` på wrappern, aldrig på ramen (PRODUCT.md: ramen rörs aldrig efter visning).
- `rootMargin: '40% 0px'` (plan 018) och `defer` (idle-lucka) står.
- `__visible`/`__pending` som expando på ramen (plan 026) står.
- Ledgerrad i `BRIEF.md` § Byggarens rader, R8: "Ramarnas observer på wrappern".

## Steps

1. Byt rad 1676-1688 enligt Target (två rader ändras: destrukturering av `entries[i].target`
   och `io.observe(f.parentNode)`).
2. **Reproduktion före/efter** (Playwright, 1440x900, riktig Chrome): ladda sidan, scrolla
   i 300 px-steg med 250 ms paus från `.stagger.top − 900` till `#process.top`, vänta 2,5 s;
   läs för varje `.frame-wrap`: `className`, `getComputedStyle(w).contentVisibility`,
   `getBoundingClientRect()`. Före: minst ett stopp där en wrapper med `top < 900 &&
   bottom > 0` bär `is-asleep`. Efter: noll sådana stopp. Samma vid 390x844 (844 i stället
   för 900).
3. Sömnkontroll: `scrollTo(0, 0)` efter vandringen, vänta 1,5 s: båda wrapparna `is-asleep`
   med `src` bevarad.
4. Plan 026:s repro (dubbelscroll in/ut/in vid Calyx): fortfarande exakt en `calyx.html`-
   resurspost, 0 `/null`.
5. Skärmbild vid Calyx centrerad och vid Hōrai centrerad efter en vandring uppifrån (3 s
   väntan): ramarna renderar sitt innehåll, inte en platta.

## Boundaries

- Rör inte `mountFrame`, `defer`, `rootMargin`, `.is-asleep`-regeln (rad 639), `min-height`
  på wrapparna, `inert`/`pointer-events` på ramarna eller reveal-attributen.
- Matchar inte raderna 1676-1688: STOPPA.

## Verification

- **Mekaniskt:** steg 2 till 4 med talen i NOTES.md § R8; `a11y_scan.py` 0 violations;
  `motion_probe.py` heron (cpu 4, 100:60, 40 ticks) före/efter: inte sämre (ramarna vakna
  kostar mer än sovande, det är avsett; H-21 mäts av plan 028).
- **Skärmbild:** `slices-1440/…--s04.png` och `s05.png` (motsvarande i `shots/r8/`): Calyx
  visar sin fold, Hōrai sin; `slices-390/…--s04..s06.png` likaså.
- **Feel check:** scrolla långsamt från kortet till priset och tillbaka upp till Calyx: båda
  ramarna är levande sajter varje gång de står på skärmen; ingen tom platta, ingen
  ommontering (Calyx' egen reveal spelar bara första gången).
- **Done when:** steg 2 ger 0 sovande wrappers i viewporten vid båda bredderna; steg 3 ger
  sömn vid toppen; H-08/H-25-skivorna visar ramarnas innehåll.

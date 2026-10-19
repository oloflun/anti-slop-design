# 026 · Ramarnas montering idempotent: en navigering per ram, sömn även för en ram som lämnade före monteringen

- **Status**: TODO (R7, loop 1)
- **Severity**: MEDIUM (kodfel med synlig konsekvens: `src="null"` och en vaken ram utanför skärmen)
- **Commit**: R6-läget av `runs/V3c/index.html`, md5 `424cdd46`
- **Category**: Kod (livscykel), H-27, plan 018:s kontrakt
- **Estimated scope**: 1 fil, ~8 rader JS
- **Källor**: Astra loop 1, material_fix 7 (verifierad mot rad 1547-1575 av arkitekten)

## Problem

Plan 018 (R6) gjorde observern beständig och lade monteringen i en idle-lucka. Två hål:

1. **Dubbel montering.** Varje `isIntersecting`-post som kommer medan `data-src` ännu sitter
   kvar (idle-luckan är upp till 600 ms) köar ett nytt `mountFrame`. Det första anropet
   sätter `src` och tar bort `data-src`; det andra läser `getAttribute('data-src')` = `null`
   och skriver `f.src = null`, som navigerar ramen till `/null`. En snabb scroll in och ut
   över Calyx-ramen räcker.
2. **Vaken ram utanför skärmen.** `.is-asleep` sätts bara i `else`-grenen, och bara när
   `data-src` redan är borta. Lämnar ramen 40 %-zonen innan idle-luckan hunnit montera den,
   monteras den ändå (callbacken ligger i kön) och står sedan vaken utanför skärmen tills
   nästa gränsövergång. Det är precis den kostnad 018 tog bort (ramarna 66 % av tasktiden).

```js
/* index.html:1547-1550, 1566-1575 - current */
      var mountFrame = function(f){
        f.src = f.getAttribute('data-src');
        f.removeAttribute('data-src');
      };
      ...
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

## Target

En synlighetsflagga per ram, monteringen läser den, och `mountFrame` är ofarlig att anropa
två gånger.

```js
/* target, index.html:1547-1550 */
      var mountFrame = function(f){
        var s = f.getAttribute('data-src');
        if (!s) return;                       /* redan monterad: andra callbacken gör inget */
        f.src = s;
        f.removeAttribute('data-src');
        f.__pending = false;
        if (!f.__visible) f.parentNode.classList.add('is-asleep');   /* lämnade före monteringen */
      };
/* target, index.html:1566-1575 */
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
```

Förväntat: exakt en navigering per ram (`performance.getEntriesByType('resource')` visar
`/sites/calyx.html` och `/sites/horai.html` en gång var, aldrig `/null`); en ram som
scrollats förbi innan luckan slog sover (`is-asleep`) direkt efter monteringen.

## Repo conventions to follow

- Ramen rörs aldrig efter visning (PRODUCT.md): planen ändrar bara när `src` sätts och
  när wrappern sover, inte ramen.
- `.is-asleep` (rad 583) och `rootMargin: '40% 0px'` (plan 018) står.
- Expando-egenskaper (`__pending`, `__visible`) i samma stil som `window.__scFreezeMotion`.
- Ledgerrad i `BRIEF.md` § Byggarens rader, R7: "Ramarnas montering idempotent".

## Steps

1. Byt rad 1547-1550 och 1566-1575 enligt Target.
2. Reproduktion före/efter (Playwright): ladda sidan vid 1440x900, `scrollTo(0, 2300)`
   (Calyx-ramen inne i 40 %-zonen), vänta 50 ms, `scrollTo(0, 0)`, vänta 50 ms,
   `scrollTo(0, 2300)`, vänta 1 500 ms. Läs `[...performance.getEntriesByType('resource')]
   .map(e=>e.name).filter(n=>/sites\/|\/null$/.test(n))`. Före: förväntat att `/null`
   eller en dubbel calyx-post kan uppträda; efter: exakt en `calyx.html`, ingen `/null`.
3. Sömnkontroll: `scrollTo(0, 2300)`, direkt `scrollTo(0, 0)`, vänta 1 500 ms:
   `.calyx-wrap.classList.contains('is-asleep')` = true och ramen har `src`.

## Boundaries

- Rör inte `rootMargin`, `defer`, `.is-asleep`-regeln eller reveal-attributen.
- Matchar inte raderna 1547-1550 eller 1566-1575: STOPPA.

## Verification

- **Mekaniskt:** steg 2 och 3 med talen i NOTES.md § R7; `motion_probe.py` heron (`section.hero:--sc-ps,.plate-card:transform`, cpu 4, 100:60, 40 ticks) före/efter: inte sämre; `a11y_scan.py` 0 violations.
- **Skärmbild:** `slices-1440/…--s04.png`-motsvarighet: Calyx och Hōrai renderar som förut.
- **Done when:** en resurspost per ram i steg 2, `is-asleep` i steg 3.

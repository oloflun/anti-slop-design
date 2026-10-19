# 022 · Kortet: fokus flyttas före inertering, träffytor 44 px, baksidan i tillgänglighetsträdet, `?preview=back` auktoritativt

- **Status**: TODO (R6)
- **Commit**: R5-läget av `runs/V3c/index.html`, md5 `fcbee8f1`
- **Severity**: MEDIUM (WCAG 2.4.3, 2.5.8, 1.3.1)
- **Category**: Interaction states
- **Estimated scope**: 1 fil, ~10 rader CSS, ~8 rader JS, 1 attribut
- **Källor**: design-a11y-reviewer fix 4 (fokus tappas till `body` när ytan inerteras), fix 6 (träffyta 104x23 px vid 390), fix 7 (`aria-hidden` på baksidan gömmer fyra strängar för linjär skärmläsare); codex-review (Astra) fynd 2b (`?preview=back` gör baksidan nåbar, `readState` inerterar den nästa bildruta)

## Problem

```js
/* index.html:1271-1277 - current */
  function setFace(showBack){
    if (backLive === showBack) return;
    backLive = showBack;
    faceBack.inert = !showBack;
    faceFront.inert = showBack;
    faceBack.setAttribute('aria-hidden', showBack ? 'false' : 'true');
    faceFront.setAttribute('aria-hidden', showBack ? 'true' : 'false');
  }
```

```css
/* index.html:257 - current */
  .topline-contact{font-weight:300;font-size:12px;letter-spacing:.04em;color:rgba(244,242,239,.84);
/* index.html:443-446 - current */
  .card-cta{font-family:var(--f-display);font-weight:700;
    font-size:clamp(.95rem,1.9cqw,1.2rem);color:#f4f2ef;text-decoration:underline;
```

Fokus på `.card-cta`, scroll uppåt: `faceBack.inert = true` och `document.activeElement`
blir `body`; nästa Tab börjar om från toppen. Träffytorna: `.card-cta` 104x23 px vid 390
och 320, `.topline-contact` 109x19. `aria-hidden="true"` på baksidan vid vila: kortets
fyra strängar finns aldrig för en skärmläsare som läser linjärt vid p = 0. I `?preview=back`
sätter previewläget baksidan nåbar (rad 1449) men `readState` (rad 1335) kör `setFace(false)`
i nästa bildruta vid scrollY 0.

## Target

```js
/* target, index.html:1271-1277 */
  function setFace(showBack){
    if (backLive === showBack) return;
    backLive = showBack;
    var hiding = showBack ? faceFront : faceBack;
    if (hiding.contains(document.activeElement)) heroPlate.focus({ preventScroll:true });
    faceBack.inert = !showBack;
    faceFront.inert = showBack;
  }
```

`heroPlate` = `document.querySelector('.hero-plate')` med `tabindex="-1"` i markupen (rad
~925). `aria-hidden` sätts inte längre: `inert` tar bort fokus- och pekarvägen, och
baksidans text ligger kvar i tillgänglighetsträdet från p = 0 (a11y fix 7; `inert` gör
ändå subträdet otillgängligt för AT i Chromium, så lägg dessutom en `.sr-only`-kopia av de
fyra strängarna direkt efter `figure.hero-plate`? Nej: `inert` döljer för AT per spec, så
`.sr-only`-kopian är den väg som faktiskt fungerar. Mål: `<p class="sr-only">Alunix.
Webbyrå i Sverige. Design, utveckling, system. Boka ett möte: kontakt@alunix.se.</p>` efter
`</figure>` (rad ~955), och `aria-hidden="true"` permanent på `.face--back` tas bort).
`.sr-only` finns inte på sidan: lägg standardregeln (`position:absolute;width:1px;height:1px;
overflow:hidden;clip:rect(0 0 0 0);white-space:nowrap`).

Träffytor (a11y fix 6): `.card-cta{display:inline-flex;align-items:center;min-height:44px;
margin-block:-10px 0;}` (baslinjen flyttas inte: negativ marginal äter den extra höjden
uppåt; mät); `.topline-contact{display:inline-flex;align-items:center;min-height:44px;
padding-inline:4px;margin-inline:-4px}`. Båda ≥ 24x24 golv och 44 px höjd utan överlapp.

Preview: `readState` respekterar previewläget: `if (previewFace !== null) { setFace(previewFace); }
else { setFace(ps >= 0.44); }` där `previewFace` sätts i preview-blocket (rad 1447-1450:
`previewFace = MODES[mode] >= 0.5`). `p1440-back.png` visar då `Boka ett möte` nåbar.

## Steps

1. `tabindex="-1"` på `figure.hero-plate`; `.hero-plate:focus{outline:none}` (fokus är
   programmatisk parkering, inte en tabbstopp; ringen på länken räcker).
2. Skriv om `setFace` (rad 1271-1277); ta bort `aria-hidden`-raderna.
3. Lägg `.sr-only`-regeln och `<p class="sr-only">` efter figuren; behåll `aria-hidden`
   bara på det som är dekor (`.logo-dock`, `.plate-edge`).
4. Träffytorna (rad 257, 443-446).
5. `previewFace` i previewblocket (rad 1447-1450) och i `readState` (rad 1335).
6. Mät: fokus på `.card-cta` (`?preview=back`), scrolla till 0: `document.activeElement`
   är `figure.hero-plate`, inte `body`; `getBoundingClientRect()` på `.card-cta` vid 390
   och 320: höjd ≥ 44, bredd ≥ 104; `tab_walk.py` 0 issues.

## Boundaries

- `inert` på den bortvända ytan står (plan från R2).
- Kortets typografi, ordning och strängar rörs inte (plan 006 och 016 äger dem).
- Matchar inte raderna 257, 443-446, 1271-1277 eller 1447-1450: STOPPA.

## Verification

- **Mekaniskt:** `a11y_scan.py` 0; `tab_walk.py` 2 stopp 0 issues; `activeElement`-testet;
  träffytemätningen vid 320, 390, 1440; en skärmläsarkontroll (NVDA i Firefox eller
  Chromes accessibility tree): baksidans fyra strängar hörs vid p = 0.
- **Skärmbilder:** `?preview=back` med `Boka ett möte` nåbar (`inert` false) och
  understrykningen (plan 021) vit; folden oförändrad i pixlar (träffytorna flyttar ingen
  baslinje: diff mot `p1440-back.png` och foldbilden ≤ 1 px).
- **Done when:** a11y-rapportens fix 4, 6, 7 och Astra 2b stängda.

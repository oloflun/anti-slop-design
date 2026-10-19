# 031 · Ramarnas reveal: sidans egen latch på det lerpade värdet, aldrig baklänges

- **Status**: TODO (R8, loop 2)
- **Commit**: R7-läget av `runs/V3c/index.html`, md5 `d30355da`
- **Severity**: MEDIUM (house physics: en reveal som gömmer sig igen vid scroll uppåt är en defekt; gate 94: clip-path drivs av rått `--sc-p`)
- **Category**: States / flöde (reveal), H-27, F-014, gate 94; Astra loop 1 fix 8 (uppskjuten till loop 2)
- **Estimated scope**: 1 fil, ~8 rader CSS, ~14 rader JS, 2 attribut i markup
- **Källor**: `reviews/loop-1-astra.md` fix 8 och H-27-noten; `scroll/scrollcraft.js` rad 947-957 (`R.el.style.clipPath` ur `a.p`, motorns råa progress, båda riktningarna); loop 2: efter plan 027 blir effekten synlig varje gång läsaren scrollar upp över Calyx eller Hōrai

## Problem

Wrapparna bär motorns `data-sc-reveal="up"` (Calyx, rad 1134) och `"iris"` (Hōrai, rad
1208). Motorn skriver `clip-path` per frame ur `a.p`, det **råa** aktvärdet (scrollcraft.js
rad 949-956), i båda riktningarna: scrollar läsaren upp över Hōrai stängs irisen igen,
och vid ett snabbt hjul stegar klippningen (F-013 orsak 1, gate 94 punkt 1: allt som
ögat ser röra sig läser `--sc-ps`). Loop 1 tog fyndet som H-27-not och sköt planen till
loop 2 eftersom Q30 kunde ändra vilka wrappers som finns; bandet står, wrapparna finns.

```html
<!-- index.html:1134, 1208 - current -->
        <div class="frame-wrap calyx-wrap" data-sc-reveal="up" data-sc-reveal-at="0.02 0.3">
        <div class="frame-wrap horai-wrap" data-sc-reveal="iris" data-sc-reveal-at="0.1 0.55">
```

## Target

Attributen tas bort (motorn rör då inte wrapparna). Sidan äger revealen: en variabel
`--rv` (0 till 1) per wrapper, satt av `readState` ur shimens **lerpade** aktvärde
(`window.__scSmooth.acts[i].cur`, ingen `getComputedStyle`), och som aldrig minskar.
Samma smoothstep-fönster som i dag, samma former (`inset` uppåt för Calyx, `circle` för
Hōrai), samma `clip-path`-egenskap (plan 018: ramen rörs inte, wrappern klipps).

```css
/* target, index.html efter rad 639 */
  /* PLAN 031. Revealen ägs av sidan: --rv skrivs av readState ur shimens lerpade
     aktvärde och bara uppåt (latch), så klippningen är mjuk (gate 94) och aldrig
     baklänges (house physics: en reveal som gömmer sig igen är en defekt). */
  @property --rv { syntax: "<number>"; inherits: false; initial-value: 1; }
  .calyx-wrap{clip-path:inset(0 0 calc((1 - var(--rv)) * 100%) 0);}
  .horai-wrap{clip-path:circle(calc(var(--rv) * 78%) at 50% 50%);}
```

`initial-value: 1` är no-JS-golvet: utan skript står ramarna oklippta (ingen tumnagel,
inget dolt innehåll: gate "reveal fails toward visible").

```js
/* target, index.html: i readState (rad 1583-1624), efter setFace-raden */
  /* PLAN 031. Latch: --rv = max(tidigare, smoothstep(from, to, ps)) ur shimens
     lerpade cur (ingen stilläsning). Skrivs bara när värdet ökar, så efter
     revealen sker noll skrivningar. */
  for (var r = 0; r < reveals.length; r++){
    var R = reveals[r], act = R.act;
    var cur = act && !isNaN(act.cur) ? act.cur : 0;
    var t = Math.min(1, Math.max(0, (cur - R.from) / (R.to - R.from)));
    t = t * t * (3 - 2 * t);
    if (t > R.v + 0.002){ R.v = t; R.el.style.setProperty('--rv', t.toFixed(4)); }
  }
```

med, en gång vid mount (efter `ScrollCraft.mount` och shimens `start`):

```js
  var reveals = [
    { el: document.querySelector('.calyx-wrap'), sel: '.calyx-fig', from: 0.02, to: 0.30, v: 0 },
    { el: document.querySelector('.horai-wrap'), sel: '.horai-fig', from: 0.10, to: 0.55, v: 0 }
  ].filter(function(R){ return R.el; });
  reveals.forEach(function(R){
    R.act = (window.__scSmooth && window.__scSmooth.acts || []).filter(function(a){ return a.el.matches(R.sel); })[0] || null;
    R.el.style.setProperty('--rv', '0');
  });
```

`?preview=`: inget läge tvingar ramarna i dag; ingen ändring. `readState` körs redan per
scroll-frame (rAF-skyddad) så ingen ny lyssnare tillkommer.

## Repo conventions to follow

- `@property`-rad för varje `--p-*`-liknande tal (R5 keep): `--rv` registreras.
- Ramen rörs aldrig; wrappern klipps (plan 018, PRODUCT.md).
- `window.__scSmooth.acts` är shimens exponerade handtag (`sc-smooth.js` rad 129-142);
  efter plan 028 heter fältet fortfarande `cur`.
- Ledgerrad i `BRIEF.md` § Byggarens rader, R8: "Ramarnas reveal latchad på `--sc-ps`".

## Steps

1. Ta bort `data-sc-reveal` och `data-sc-reveal-at` på rad 1134 och 1208.
2. Lägg CSS-blocket efter rad 639 och JS enligt Target (mount-listan efter rad 1460,
   loopen i `readState`).
3. Verifiera att motorn inte längre skriver `clip-path` på wrapparna: efter en scroll
   genom bandet är `getComputedStyle(w).clipPath` ett värde ur `--rv` (`inset(0px 0px 0%
   0px)` respektive `circle(78% at 50% 50%)` vid `--rv` 1) och `w.style.clipPath` tomt.
4. Tolv ramar genom `.calyx-fig` och `.horai-fig` (som `frames.py life`): revealen löper
   0 → 1 i samma fönster som förut. Sedan scrolla från priset tillbaka upp till tesen:
   `--rv` står på 1 på båda; ramarna är hela hela vägen.
5. `motion_probe.py --track ".horai-wrap:clip-path"` (cpu 4, 100:60, start vid
   `.horai-fig.top − 900`): staircase 0 (proben läser `circle()`-radien som tal; är
   spåret DEAD enligt proben, läs `--rv` per frame i en egen rAF-logg i stället och skriv
   max_step).

## Boundaries

- Motorn rörs inte; `.sc-*` restylas inte. `is-asleep`/`content-visibility` (plan 027)
  rörs inte: en sovande wrapper behåller sitt `--rv`.
- Ingen `transition` på `clip-path` (F-014: allt som rör sig läser det lerpade värdet).
- Matchar inte rad 1134, 1208, 639 eller `readState`: STOPPA.

## Verification

- **Mekaniskt:** steg 3 till 5; `a11y_scan.py` 0; `reflow.py` 320 + 200 % rent (clip-path
  påverkar inte layout).
- **Skärmbild:** skivorna `s04`/`s05` vid 1440 identiska i innehåll med efter plan 027;
  ramar 1 till 12 genom Hōrai visar irisen öppna sig mjukt.
- **Feel check:** scrolla ner genom Hōrai, sedan upp igen: irisen stänger sig inte; snabbt
  hjul över Calyx: klippkanten glider, stegar inte.
- **Done when:** H-27 står bockad utan not; steg 4 visar `--rv` 1 efter uppåtscroll.

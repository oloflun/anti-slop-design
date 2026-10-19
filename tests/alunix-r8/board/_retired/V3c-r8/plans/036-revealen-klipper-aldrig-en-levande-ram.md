# 036 · Revealen klipper aldrig en levande ram: irisen och uppdragningen som transform på en inre box, ramen kontraskalad

- **Status**: TODO (R9, loop 3)
- **Commit**: R8-läget av `runs/V3c/index.html`, md5 `70214a22`
- **Severity**: HIGH (bildtiden i bandet: H-21, H-22, H-32; F-013 orsak 2, gate 94 punkt 2)
- **Category**: Funktion (bildtid), H-21, H-22; Astra loop 3 K7; plan 031/035:s `--rv`
- **Estimated scope**: 1 fil, 2 inre `<div>` i markup, ~10 rader CSS, 1 rad `@property`, ~2 rader JS (mount-tidpunkten, del B)
- **Källor**: loop 3 `shots/loop-3/probe/ab/` (sex A/B-omgångar, `scripts/ab_band*.sh`, `motion_probe_ab.py --pre`), `probe/price-down-100-cpu1/`, `probe/giant-down-100-cpu1/`; loop 2 `profile/` (bandet med ramarna vakna 7,02 s task mot 5,36 blockerade)

## Problem

Bandets bildtid vid cpu 1 (100 px / 60 ms): `.price`-fönstret (3 873 till 5 673, där Hōrais
iris öppnar sig) p95 143,7 ms, `#giant-section`-fönstret (2 700 till 5 500, båda ramarna
monteras och avslöjas) 128 ms; kontrollen 18,4. Ablation i prisfönstret, cpu 1, tre
körningar där inget annat sägs (`probe/ab/`):

| variant (ramarna förmonterade 5 s före hjulet om inget annat sägs) | p95 ms | rutor > 33 |
|---|---|---|
| som byggd, **utan** förmontering (ramen monteras i fönstret) | 109 / 127 | 14 / 13 |
| `clip-path: circle()` på wrappern över **levande** Hōrai | 187 / 139 / 101 (202 / 303 i omgång 1) | 15 till 20 |
| `clip-path: inset()` (rektangel) i stället för cirkel | 124 / 214 | |
| `will-change: clip-path` på wrappern | 71 / 142 | |
| `contain: paint` på wrappern | 183 / 164 | |
| `mask-image: radial-gradient` i stället för `clip-path` | 70 / 68 / 72 | 13 till 16 |
| ramen `visibility:hidden` under samma `clip-path` | 139 / 157 | |
| **ingen klippning** (`--rv` tvingad till 1) | **35 / 36 / 62** | 8 till 14 |
| **irisen som transform**: inre box `border-radius:50%; overflow:clip; transform:scale(t)`, ramen `scale(1/t)` | **35,6 / 46,7** | 11 |
| samma utan kontraskalning av ramen | 125 / 138 | 23 / 31 |
| uppdragning som `translateY` på inre box utan kontratransform | 98 / 119 | |
| irisen som transform, **utan** förmontering | 48,7 / 35,6 | 14 / 11 |

Jättefönstret (2 700 till 5 500, 28 ticks): som byggd 123 / 208 ms; hela receptet (Calyx
`translateY` + kontratranslate, Hōrai iris-transform) utan förmontering 121 / 88,5; **med**
förmontering 57,7 / 53,0. Slutsats, mätt: (A) en `clip-path` eller `mask` på en wrapper som
innehåller en monterad iframe kostar 70 till 300 ms p95 per bildruta den ändras, oavsett
form; en transform på en inre box med ramen kontratransformerad kostar ingenting utöver
det omonterade fallet. (B) Monteringen av de två sajterna i bandet kostar ~40 till 60 ms
p95 i jättefönstret; den ligger i dag vid rootMargin 100 % (Calyx ≈ scrollY 2 860, mitt i
bandets entré).

```css
/* index.html:651-658 - current */
  @property --rv { syntax: "<number>"; inherits: false; initial-value: 1; }
  .calyx-wrap{clip-path:inset(0 0 calc((1 - var(--rv)) * 100%) 0);}
  .horai-wrap{clip-path:circle(calc(var(--rv) * 78%) at 50% 50%);}
```

## Target

**A. Transformreceptet.** En inre box `.rv` i varje wrapper (mellan wrappern och ramen);
wrappern behåller `overflow:clip` (rad 641) och blir aldrig klippt med `clip-path`. `--rv`
registreras `inherits:true` så `.rv` och ramen läser den (två element; inget annat ärver
den, wrappern har inga andra barn). Under revealen står ramens innehåll pixelstilla:
transform × kontratransform = identitet; vid `--rv` 1 är båda identitet.

```html
<!-- target, rad 1180 och 1254: en inre box, ramen orörd i attribut -->
        <div class="frame-wrap calyx-wrap"><div class="rv">
          <iframe data-src="/sites/calyx.html" loading="lazy" inert title="…"></iframe>
        </div></div>
```

```css
/* target, index.html:651-658 */
  /* PLAN 036 (loop 3): en clip-path eller mask på en wrapper med en levande iframe
     kostar 70 till 300 ms p95 per ändrad bildruta (probe/ab/); en transform på en inre
     box med ramen kontratransformerad kostar inget. Innehållet står pixelstilla under
     revealen (t × 1/t = 1), och efter revealen är transformen identitet. */
  @property --rv { syntax: "<number>"; inherits: true; initial-value: 1; }
  .frame-wrap .rv{position:absolute;inset:0;}
  .calyx-wrap .rv{transform:translateY(calc((1 - var(--rv)) * 100%));}
  .calyx-wrap .rv iframe{transform:translateY(calc((var(--rv) - 1) * 100%));}
  .horai-wrap{--rvs:max(var(--rv), 0.02);}
  .horai-wrap .rv{border-radius:50%;overflow:clip;transform:scale(var(--rvs));}
  .horai-wrap .rv iframe{transform:scale(calc(1 / var(--rvs)));transform-origin:50% 50%;}
```

Irisens radie: cirkeln med `border-radius:50%` på en box som är wrapperns storlek ger en
ellips inskriven i boxen; R8:s `circle(78%)` var en cirkel med radie 78 % av
referensboxen. Bygg `.rv` som en **kvadrat** centrerad i wrappern (`width:max(100%, …)`
eller `aspect-ratio:1; width:calc(156% * …)`) så att skalan 1 täcker hela wrappern och
skalan `--rv` ger samma synliga cirkel som förut vid `--rv` 0,5 (jämför mot
`shots/r8/horai12-1440-05.png`, ± 8 px i radie); ramen fyller då kvadraten med
`inset` som placerar den på wrapperns yta (kontraskalan gäller fortfarande). Skriv den
valda geometrin i NOTES. `.rv iframe{position:absolute}` med samma box som förut
(`.frame-wrap iframe`-reglerna på rad 641 till 650 gäller ramen oförändrat).

`.calyx-wrap .rv` `translateY((1 − rv)·100%)`: procenten är boxens egen höjd (= wrappern),
ramen `translateY((rv − 1)·100%)` i sin egen höjd (= samma): innehållet står stilla,
wrapperns `overflow:clip` visar den övre delen: samma bild som `inset(0 0 (1−rv)·100% 0)`.

Observern (027) hittar ramen via `wrap.querySelector('iframe')` (rad 1774): oförändrat.
`is-asleep` på wrappern: oförändrat. Ramen bär inga nya attribut; `inert` och
`pointer-events:none` står.

**B. Monteringen före bandet.** Efter A återstår monteringens ~40 till 60 ms p95 i
jättefönstret. Montera båda ramarna när heron står i sin landade svans (`--sc-ps` på heron
≥ 0,80, författad stillhet: scroll_verify:s döda band 1 800 till 2 100), i stället för vid
wrapperns rootMargin 100 % (Calyx ≈ scrollY 2 860). Sovandet (`is-asleep` utanför 40 %) rör
inte monteringen. Implementation: i 035:s `latchTick` (som redan läser heroaktens `cur`
för 039): `if (heroAct.cur >= 0.80) frames.forEach(mountFrame)` en gång (`data-src` tas bort
av `mountFrame`, så anropet är idempotent per 026). R6:s "förvärmning vid load" mätte sämre
för att proben scrollar direkt efter load; det här är inte load utan svansen, och mäts
med proben från 1 500 (35 ticks) före och efter.

## Repo conventions to follow

- Ramen transformeras aldrig **efter** att den visats (PRODUCT.md): under revealen är
  innehållet pixelstilla och efter revealen identitet; skriv det i markupkommentaren.
- Reveal en gång på wrappern (035:s latch), `is-asleep`, observern på wrappern (027), en
  resurspost per ram (026): orörda.
- Inga nya tokens; `--rv` byter bara `inherits`.
- Ledgerrad i `BRIEF.md` § Byggarens rader, R9: "Revealen som transform på inre box, ramen kontraskalad; monteringen i heroens svans" (eller B:s utfall om B återställs).

## Steps

1. **Mät före** (scratch `motion_probe_ab.py`, cpu 1, 100:60, tre körningar var, median p95 och rutor): prisfönstret (`--start 3873 --ticks 18`, `.price:--sc-ps`), jättefönstret (`--start 2700 --ticks 28`, `#giant-section:--sc-ps`), och bandet från svansen (`--start 1500 --ticks 35`, `#giant-section:--sc-ps`), utan `--pre`.
2. A: markup (rad 1180, 1254), CSS (rad 651 till 658), kvadratgeometrin för irisen.
3. Pixelkontroll A: `?preview=` finns inte för ramarna; skriv en scratchfångst som sätter `--rv` 0,25 / 0,5 / 0,75 / 1 inline på `.horai-wrap` (och Calyx) med ramarna monterade och vakna, jämför mot `shots/r8/horai12-1440-*.png` (irisens radie ± 8 px, innehållet i cirkeln identiskt: samma tallrik på samma plats) och `shots/r8/calyx12-1440-*.png`. Vid `--rv` 1: pixelidentisk med R8 (diff 0 i wrapperns yta).
4. **Mät efter A** som steg 1. Mål: prisfönstret ≤ 50 ms median (mätt 35,6 / 48,7 utan förmontering), jättefönstret ≤ 100.
5. B: monteringen i heroens svans. **Mät efter B** som steg 1. Mål: jättefönstret ≤ 60 (mätt 53 / 58 med förmontering); bandet från svansen inte sämre än efter A. Ingen vinst ≥ 10 ms i jättefönstret: återställ B, skriv talen.
6. Ramarnas vandring (027 steg 2, 3) och 026:s repro: 0 stopp, en resurspost per ram, sömn vid scrollY 0 (B monterar men söver ändå utanför 40 %).
7. `motion_probe.py --track ".horai-wrap .rv:transform"` cpu 1, start `.horai-fig.top − 900`: staircase 0 (proben dekomponerar transformen).

## Boundaries

- Ingen `clip-path`, `mask` eller `filter` på `.frame-wrap`, `.rv` eller ramen.
- `sites/*` och motorn orörda; `sc-smooth.js` orörd.
- Matchar inte rad 641, 651 till 658, 1180, 1254 eller 1735 till 1790: STOPPA.

## Verification

- **Mekaniskt:** steg 1, 4, 5 (tre körningar, median, båda fönstren); steg 6, 7; `a11y_scan.py` 0; `reflow.py` 320 + 200 % rent.
- **Skärmbild:** steg 3:s fyra lägen per ram mot R8:s tolv ramar; skivorna `s04`, `s05` (1440, `scrollTo`) identiska med `shots/loop-3/slices-1440-fix/v3c-1440--s04.png`, `s05.png`.
- **Feel check:** hjul genom bandet vid cpu 4 i devtools: irisen öppnar sig utan att bildrutorna faller bort; Hōrais tallrik står stilla medan cirkeln växer.
- **Done when:** H-22:s bandtal (`#giant-section`, `.price`) ≤ 25 ms p95 vid cpu 1 eller, om inte, talen före/efter A och B i NOTES § R9 med kvarvarande orsak namngiven.

# 034 · Processakten: ankare oberoende av sticky-läget, prosan alltid synlig

- **Status**: TODO (R8, loop 2)
- **Commit**: R7-läget av `runs/V3c/index.html`, md5 `d30355da`
- **Severity**: HIGH (F-007: `?preview=process-0N` visar inte steg 01 till N; steg 01:s kontur och glyf försvinner i varje preview vid båda bredderna)
- **Category**: Funktion (mätning, reveal-kontrakt), H-15, H-28, H-30; Astra loop 2 fix 1 och 3, verifierade av arkitekten
- **Estimated scope**: 1 fil: ~3 rader JS, 1 attributrad i markup
- **Källor**: `reviews/loop-2-astra.md` fix 1, 3; scratch `verify_astra2.py` (loop 2): `?preview=process-05` ger `--s1` 0,4847 > `--e1` 0,2292 vid 1440 och 0,4449 > 0,2510 vid 390, `#p-outline`/`#p-glyph` `stroke-dashoffset: 1px` (osynliga) i `process-03` och `process-05` vid båda bredderna; `shots/loop-2/diag/astra1-1440-process-05.png`, `astra1-390-process-05.png` (arket utan ram och glyf); `process-390/v3c-390-life-01.png`-motsvarande mätning: `li 01` opacity 0, `translateY(14px)`, `<ol>` opacity 0; li-topparna 28 px lägre före revealen än efter (390)

## Problem

**A. `--s1` mäts från ett fastnat sticky-element.** `measureAct` (rad 1547) ankrar steg 01
i arkets ankomst med `stick.getBoundingClientRect().top + scrollY − top`. När arket är
fastnat (varje gång sidan står inne i akten) är `getBoundingClientRect().top` sticky-
offseten (202 px vid 1440, 0 vid 390), inte arkets naturliga läge, så `stickY0` växer med
scrollY. `measureAct` körs på `load` (rad 1567) och `resize` (rad 1566, som också
`document.fonts.ready` utlöser via `relayout`, rad 1466-1468). I `?preview=process-0N`
scrollar skriptet (rad 1780) innan `load` hinner fira, så den sista mätningen görs med
arket fastnat: `--s1` hamnar över `--e1` (0,4847 mot 0,2292 vid 1440), `--k1`:s nämnare blir
negativ, `--k1` klämms till 0, och konturen (`#p-outline`) och glyfen (`#p-glyph`) står
oritade (`stroke-dashoffset: 1px`) i varje preview från 02 och uppåt. Samma sak drabbar en
läsare som byter fönsterstorlek (eller får ett sent typsnitt) medan hen står i akten:
steg 01 raderas. R7:s preview-läckagekontroll mätte bara att steg N+1 saknades, inte att
01 till N fanns.

```js
/* index.html:1547 - current */
      var stickY0 = stick ? stick.getBoundingClientRect().top + window.scrollY - top : 0;
```

**B. Prosan deltar i motorns reveal.** `<ol class="process-steps" data-sc-in
data-sc-stagger="70">` (rad 1230) ger listan och varje `li` motorns flödesreveal
(`scrollcraft.css` rad 286-291: `opacity:0; transform:translateY(14px)` tills `.sc-in`).
Formbeslutet (plan 019, rad 784): "texten är alltid synlig och ligger i flödet, ingen
opacitet". Mätt vid 390 i ramen `life-01`: `li 01` opacity 0, `translateY(14px)`; vid 1440
fångas stycket mitt i sin toning (`process-1440/v3c-1440-life-01.png`, "01 UPPSTART"
utgråat nederst). Dessutom mäter `measureAct` vid `load` li-rektanglar som fortfarande bär
translateY: topparna ligger 28 px (ol 14 + li 14) lägre än efter revealen vid 390, så alla
`--sN`/`--eN` är 28 px fel.

```html
<!-- index.html:1230 - current -->
      <ol class="process-steps" data-sc-in data-sc-stagger="70">
```

## Target

**A.** Ankaret läses ur gridets överkant, som är arkets naturliga läge på båda sidor om
1279 (`align-self:start` vid ≥ 1280, `order:-1` som första rad vid ≤ 1279) och aldrig rör
sig med sticky:

```js
/* target, index.html:1547 */
      /* PLAN 034 A: gridets överkant, inte det (eventuellt fastnade) sticky-elementets
         rect: getBoundingClientRect på ett fastnat sticky-element ger sticky-offseten,
         så --s1 växte med scrollY och hamnade över --e1 (Astra loop 2, verifierat). */
      var grid = process.querySelector('.process-grid');
      var stickY0 = grid ? grid.getBoundingClientRect().top + window.scrollY - top : 0;
```

`sheetH` (rad 1537) läser `stick`:s **höjd**, som sticky inte ändrar; står kvar.

**B.** Attributen tas bort; prosan är alltid synlig, arket bär rörelsen:

```html
<!-- target, index.html:1230 -->
      <ol class="process-steps">
```

`#principer`s liggare (rad 1405, `data-sc-in`) står: den är inte processakten och har
inga ankare.

## Repo conventions to follow

- `measureAct` mäter en gång vid mount/resize, fjorton tal på `#process` (plan 019/025).
- Motorn rörs inte; attributet är sidans.
- Ledgerrader i `BRIEF.md` § Byggarens rader, R8: "Stegens ankare ur gridet", "Prosan
  utan reveal".

## Steps

1. Byt rad 1547 enligt A; ta bort de två attributen på rad 1230 enligt B.
2. `?preview=process-01..07` vid 1440 och 390: läs `--s1..--e7` (`--s(N) < --e(N)` för
   alla N), `#p-outline` och `#p-glyph` `stroke-dashoffset: 0px` i preview 02 till 07
   (steg 01 färdigritat), preview 01 visar konturen på väg (0 < dashoffset < 1px) eller
   färdig.
3. Resize-provet: ladda sidan, scrolla till `#process.top + 2000`, `dispatchEvent(new
   Event('resize'))`, läs `--s1`: samma tal (± 0,001) som vid scrollY 0.
4. Prosan: vid `#process.top − 900 + (h + 900)/11` (ramen `life-01`) är `li 01` opacity 1,
   transform none, vid båda bredderna; li-topparna vid `load` är samma som efter 2 s.
5. R7:s preview-läckagekontroll om igen, nu i båda riktningarna: preview N visar steg 01
   till N och inte N+1.

## Boundaries

- Rör inte fönsterformlerna (`0.05`/`0.35`, `vh − sheetH`), hysteresen (025 B4),
  `--eN`-tecknet eller stegens copy.
- Matchar inte rad 1547 eller 1230: STOPPA.

## Verification

- **Mekaniskt:** steg 2 till 5 med talen; PageDown-vandringen 7/7 (a11y fix 3) igen.
- **Skärmbild:** `?preview=process-05` vid 1440 och 390: arkets ram, glyf, hjälplinjer,
  mått, öppning och Calyx-bild alla på plats (jämför `shots/loop-2/diag/astra1-*-process-05.png`
  som felet); `life-01` vid 390: stycket 01 fullt bläck.
- **Feel check:** stå i akten, dra fönstret smalare och bredare: ritningen behåller sina
  steg; scrolla in i akten: prosan är där när arket kommer, den tonar inte in.
- **Done when:** H-30 bockad (preview N = steg 01..N, båda bredderna), H-28 utan not.

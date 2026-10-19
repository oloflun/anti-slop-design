# 042 · Prisblockets reserverade höjd: sidan krymper 297 px när blocket målas första gången, och motorns akttoppar under bandet står kvar på fel värde

- **Status**: TODO (R10, loop 4)
- **Commit**: R9-läget av `runs/V3c/index.html`, md5 `909916d1`
- **Severity**: HIGH (funktion: layoutskifte inne i läsarens viewport, och processaktens, principernas och avslutets `--sc-p` räknas ur en akttopp som är 297 px fel för varje hjul- och tangentbordsläsare vid 1440, 262 px vid 390, tills ett riktigt resize-event; H-30:s 390-previews formas bara i ~1 av 3 laddningar)
- **Category**: Funktion (layout, akternas position), H-30, H-15, H-16, H-05, H-01; gate 93 (CLS); arkitektens loop 4-fynd C1 = Astra loop 4 fix 1 (samma rad, samma mekanism, oberoende funnen)
- **Estimated scope**: 1 fil, 1 rad CSS (två deklarationer bort), en kommentar
- **Källor**: loop 4 `shots/loop-4/shiftprobe.json`, `shiftprobe2.json`, `mountshift.json`, `pricefix_ab.json`, `preview390.json`, `preview390b.json`; `index.html` rad 725 till 731 (`.price{… content-visibility:auto;contain-intrinsic-size:auto 760px;}`), rad 546 till 555 (`.stagger` flex, `.col` med `flex:1 1 50%`, `.horai-fig{flex:1}`); `scroll/scrollcraft.js` rad 557 (`layout()`), rad 1182 till 1187 (resize-vakten `innerWidth === lastW && isMobile()`); R9 NOTES § Plan 037 ("motorns EGEN layout()-cache för #process släpar 262px")

## Problem

`.price` bär `content-visibility:auto` med `contain-intrinsic-size:auto 760px` (rad 731,
R2/R3: "håller höjden så att CLS inte betalar för hoppet"). Blockets verkliga innehåll är
463 px vid 1440 (567 med padding) och 450 px vid 390 (554): platshållaren är 297 respektive
262 px **högre** än blocket. Så länge blocket aldrig målats (läsaren ovanför bandet) är
`.price` 864 px och vänsterspalten 2 415 px; högerspaltens `.horai-fig{flex:1}` sträcks
till samma höjd (Hōrai-wrappern 1 286 px). När blocket kommer in i viewporten första
gången målas det, `auto` byter till den verkliga storleken, och hela bandet krymper:

| mått (1440x900) | före första målningen | efter | diff |
|---|---|---|---|
| `.price` | 864 | 567 | −297 |
| `.horai-wrap` (sträckt) | 1 286 | 989 | −297 |
| `.stagger` | 2 577 | 2 280 | −297 |
| `#process` top | 5 637 | 5 340 | −297 |
| dokumenthöjd | 10 880 | 10 582 | −297 |
| 390x844: `.price` / `#process` top / dokument | 816 / 6 415 / 11 588 | 554 / 6 152 / 11 326 | −262 |

(`shiftprobe.json`: skiftet sker inte vid montering, inte vid `is-asleep`, inte vid
`content-visibility:visible` på ramarna, bara när `.price` själv når viewporten;
`shiftprobe2.json`: `.price`:s barn är 108 + 46 + 260 px i båda lägena.)

Tre följder, alla mätta:

1. **Layoutskifte inne i viewporten** när prisblocket kommer in (blockets underkant och
   processaktens kicker flyttar 297 px uppåt medan de är synliga). Det är exakt det
   platshållaren skulle förhindra.
2. **Motorns akttoppar står kvar.** `layout()` mäts vid load och på `resize`. Skiftet ger
   inget resize-event, så `#process` (5 637), `#principer` (9 433) och `footer.close` (9 980)
   räknar sin `--sc-p` ur toppar som är 297 px för höga. Mätt (`mountshift.json`, hjul till
   scrollY 4 800, 1440): motorn `--sc-p` 0,0134 mot sant 0,0767 (= efter ett riktigt
   resize). Ritningen, principernas reveal och avslutets linje ligger 297 px efter prosan
   för varje läsare som inte råkar ändra fönsterstorlek. Sidans egna `--sN/--eN` är
   kvoter av aktens liv ur `processTop`, som också mäts vid load: konsekvent med varandra,
   men 297 px fel mot DOM:en. Vid 390 kan inte ens ett syntetiskt resize rätta det
   (`scrollcraft.js` rad 1186).
2b. **Ritningen ligger 297 px efter prosan i en fångst som redan passerat prisblocket.**
   `process-1440/v3c-1440-life-01.png` (scrollY 5 164 efter ett hopp från 0): steg 01:s
   rubrik och prosa står nere till vänster, högerspalten är tom fastän `--k1` med sann
   topp vore 0,39 och konturen (040: 0 till 0,30) hel; motorn räknar `--sc-p` 0,091 mot
   sant 0,154. Astra loop 4 (bild 77) läste det som H-15 öppen; det är den här raden.
   Loop 4:s A/B (`shots/loop-4/probe/ab/`, cpu 1, tre körningar, median): prisfönstret
   53,0 → 35,3 ms, jättefönstret 94,1 → 81,7 ms med platshållaren neutraliserad (omlayouten
   på 297 px sker annars mitt i fönstret); herofönstret 78,2 → 64,7 (brus).
3. **`?preview=process-0N` vid 390 är ett race** (`preview390.json`, `pricefix_ab.json`): 01
   formades i 1 av 3 laddningar, 02 i 1 av 3, 03 i 2 av 3; utfallet beror på om
   `aimOnce` mätte `processTop` före eller efter att prisblocket målats. R9 skrev det som
   motorbunden gräns (plan 037); gränsen är den här platshållaren.

```css
/* index.html:729-731 - current */
  .price{background:var(--c-graphite);color:var(--invert-ink);
    padding:var(--panel-pad-y) clamp(20px,4vw,44px);
    content-visibility:auto;contain-intrinsic-size:auto 760px;}
```

## Target

De två deklarationerna tas bort. Blocket är text på ett platt plan; att hoppa över dess
målning sparar inget mätbart (A/B i prisfönstret, se Steps 1) och kostar ett skifte på
297 px. Utan platshållare är dokumenthöjden 10 582 px vid 1440 och 11 326 vid 390 från
load, motorns toppar stämmer med DOM:en utan resize, och 390-previews formas 3 av 3
(`pricefix_ab.json` B_fix: `engTop` = `realTop` = 6 152, `ps` ≥ `--eN` i 6 av 6).

```css
/* target, index.html:729-731 */
  /* PLAN 042 (loop 4): ingen content-visibility på prisblocket. Platshållaren
     (760px) var 297px högre än blocket (463px vid 1440), så sidan krympte
     297px första gången blocket målades och motorns akttoppar under bandet
     stod kvar 297px fel tills ett riktigt resize (mountshift.json). */
  .price{background:var(--c-graphite);color:var(--invert-ink);
    padding:var(--panel-pad-y) clamp(20px,4vw,44px);}
```

## Repo conventions to follow

- Ramarnas `content-visibility:auto` + `.is-asleep` (018, 027) rörs inte: de har
  `min-height` i dvh och absolut placerat innehåll, så deras höjd ändras inte av sömn
  (`shiftprobe.json`: 810 / 989 i alla lägen).
- `--c-graphite`, prisliggarens linjer (033), `.price`:s padding: orörda.
- Ledgerrad i `BRIEF.md` § Byggarens rader, R10: "Prisblocket utan platshållare; dokumenthöjden konstant från load".

## Steps

1. **Mät före** (scratch `motion_probe_ab.py`, cpu 1, 100:60, tre körningar, median p95): prisfönstret (`--start 3873 --ticks 18`, `.price:--sc-ps`) och jättefönstret (`--start 2700 --ticks 28`, `#giant-section:--sc-ps`), som byggd och med `--pre` som neutraliserar de två deklarationerna (`.price{content-visibility:visible!important;contain-intrinsic-size:none!important}`). Loop 4:s tal: se `shots/loop-4/probe/ab/` och NOTES § Loop 4.
2. Ta bort de två deklarationerna på rad 731; skriv kommentaren.
3. Geometri (1440x900 och 390x844, `wait_until="load"` + 2 s, sedan hjul till scrollY 4 800 / 4 900 + 3 s): `document.documentElement.scrollHeight` lika vid load och i bandet (10 582 / 11 326); `#process` top lika (5 340 / 6 152); motorns `ScrollCraft.instances[0].acts` topp för `#process` = `getBoundingClientRect().top + scrollY` utan något resize; `#process` inline `--sc-p` vid scrollY 4 800 (1440) = 0,077 ± 0,002.
4. `?preview=process-01..07` vid 390, tre laddningar var, `load` + 2 s: `--sc-ps` ≥ `--eN` − 0,0005 i 21 av 21. Vid 1440: 7 av 7 (som R9).
5. `perf_probe.py --cpu 4` vid 1440 och 390: CLS ≤ 0,05; skriv talet bredvid R9:s 0,000.
6. **Mät efter** som steg 1: prisfönstret och jättefönstret inte sämre än median före (±5 ms är brus).
7. `scroll_verify.py` vid 1440 och 390 (H-16): inga nya döda band; `blankBands` läses om mot de nya positionerna.

## Boundaries

- Inga andra element får eller mister `content-visibility` i den här planen.
- Motorn och `sc-smooth.js` orörda; ingen `instances`-läsning i sidans kod (mätningen i steg 3 sker i skript, inte i `index.html`).
- Matchar inte rad 729 till 731: STOPPA.

## Verification

- **Mekaniskt:** steg 3, 4, 5, 6, 7.
- **Skärmbild:** skivorna `s05` och `s06` vid 1440 (`scrollTo`, 3 s): processaktens kicker står 237 px under skivans överkant i `s06` med `#process` top 5 340 (i R9-läget stod den vid y 18 för att sidan redan krympt, `shots/loop-4/slices-1440/v3c-1440--s06.png`); `preview-390-process-01.png` och `-02.png` formade i tre laddningar i rad.
- **Feel check:** hjul genom bandet vid 1440: inget hopp när prisblocket kommer in; processarkets kontur sluter sig medan rubriken läses (040) och inte 300 px senare.
- **Done when:** H-30 bockad vid båda bredderna utan "best-effort"; H-01 och H-05 omräknade på den konstanta dokumenthöjden; `PROMPT-R10`:s grind punkt 9 (previews i båda riktningarna) grön 3 av 3 vid 390.

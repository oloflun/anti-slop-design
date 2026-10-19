# 025 · Processakten i helheten: railmarginalen, arkets ankomst, stegens kadens, steg 07:s hållning

- **Status**: TODO (R7, loop 1)
- **Commit**: R6-läget av `runs/V3c/index.html`, md5 `424cdd46`
- **Severity**: HIGH (A är ett layoutfel; B är F-007 vid 390: arket ritar ett steg för sent)
- **Category**: Funktion (A, B), flöde (C); H-08, H-25, H-30, leadens tre fynd R6 + arkitektens loop 1
- **Estimated scope**: 1 fil: ~6 rader CSS, ~8 rader JS
- **Källor**: leadens pixelläsning R6 (`"Hur vi tänker" utan railmarginal`, `tomt fält ~550 px vid 390`, `steg 04:s skraffering i preview 03`, `arket glider ut vid 07`); arkitektens loop 1: `shots/loop-1/slices-1440/v3c-1440--s05.png` (kickern vid x 0), `slices-390/v3c-390--s07.png` (tomt fält 500 px), `preview/preview-1440-process-01..06.png` (steg N+1 läcker in i varje preview), `preview/preview-390-process-01..07.png` (texten under arket är steg N+1), `diag/diag.json` (`principlesPadding: 0px`, `--s2 0.2158 < --e1 0.2365` vid 1440, `--s2 0.2612 < --e1 0.3450` vid 390), `diag/diag-1440-step07-read.png`

Fyra fynd, samma sektion, fyra små ändringar. Varje steg mäts för sig.

## Problem

**A. Railmarginalen saknas på papperet.** `#principer` renderar `padding: 0px` (mätt): regeln
`padding:var(--panel-pad-y) var(--rail-x)` refererar `--panel-pad-y`, som bara är
deklarerad på `.panel-pad` (rad 519). En `var()` mot en egenskap som inte finns på
elementet gör hela deklarationen ogiltig vid beräkning, så både lodrät och vågrät padding
faller till 0: kickern `HUR VI TÄNKER`, rubrikerna och hårlinjerna börjar vid x = 0
(`s1440-09.png`, `slices-390/v3c-390--s11.png`). Samma sak för processaktens kicker:
`.process > .kicker-sans` har ingen padding alls (`process-title` och `process-lead` har
`var(--rail-x)`), så `SÅ GÅR DET TILL` står vid x = 0 (`v3c-1440--s05.png`, `v3c-390--s06.png`).

```css
/* index.html:881-883 - current */
  .principles{background:var(--bg);color:var(--ink);
    padding:var(--panel-pad-y) var(--rail-x);}
  .principles .ledger{max-width:64ch;}
```

**B. Arkets fönster: ankomsten är tom och stegen läcker.** `measureAct` (rad 1438-1461)
ankrar `--sN` i att `li N`:s överkant når 85 % (1440) respektive 95 % (390) av
viewporthöjden, och `--eN` i att `li N`:s mitt når viewportens mitt (1440) respektive
`yc + 0,5·(vh + sheetH)` (390). Två fel följer:

1. **Fönstren överlappar.** Vid 1440 är `--s2` 0,2158 och `--e1` 0,2365: steg 2:s banor
   börjar ritas innan steg 1:s är klara, i varje steg (skillnaden är ~0,02 = ~90 px).
   Villkoret för överlapp är `h_li / 2 < 0,35·vh`, och stegen är 394 till 490 px höga mot
   315 px. Det är leadens "steg 04:s skraffering synlig i preview 03", och det syns i alla
   sex previews (`preview-1440-process-01`: x 24-guiden ur steg 02; `-02`: öppningens
   överkant ur 03; `-03`: skrafferingen ur 04; `-04`: Calyx-bilden ur 05; `-06`:
   titelblockets ram ur 07).
2. **Vid 390 har `--eN` fel tecken.** `e = (yc + 0,5·(vh + sheetH)) / life` löst för
   scrollY sätter `li N`:s mitt på viewport-y `0,5·(vh − sheetH)` = 217 px, alltså **under
   det sticky arket** (0 till 410 px). Steg N:s ritning blir därför klar när steg N:s
   rubrik redan gått in under arket, och texten som syns under arket är steg N+1
   (`preview-390-process-01.png` visar PLANERING under ett ark som ritar steg 01, och så
   vidare för alla sju). R6:s "teckenrättelse" gjorde preview-scrollen konsekvent med en
   redan felvänd formel. Överlappen blir samtidigt 0,084 (~380 px) per steg.
3. **Ankomsten är tom.** `--s1` ankras i `li 01`:s överkant. Vid 390 ligger arkets
   reserverade rad (410 px, `order:-1`) ovanför `li 01`, så arket är 606 px in i
   viewporten innan första linjen ritas: `v3c-390--s07.png` visar ~500 px tomt papper
   mellan ingressen och steg 01, `process-390/v3c-390-life-02.png` bara arkets överkant.
   Vid 1440 samma sak, mildare: högerspalten är tom tills gridets topp nått 85 %.

```js
/* index.html:1455-1459 - current */
        var s = (y0 + vh * (mobile ? 0.05 : 0.15)) / life;
        var e = (yc + (mobile ? 0.5 * (vh + sheetH) : 0.5 * vh)) / life;
        process.style.setProperty('--s' + (i + 1), s.toFixed(4));
        process.style.setProperty('--e' + (i + 1), e.toFixed(4));
        stepAnchors.push({ s: s, yc: yc });
```

**C. Steg 07 läses medan arket lämnar.** Sticky-hållet för `.process-stick` slutar där
gridets rad slutar, och raden är `<ol>`:s höjd; `li 07` är kortast (394 px vid 1440). Mätt
(`diag.json`, `step07_1440`): med `li 07`:s överkant vid −143 px står arkets överkant vid
−213 px; arkets och `li 07`:s underkanter sammanfaller (251 px). `diag-1440-step07-read.png`
och `s1440-09.png`: arket är kapat i överkant medan 07 läses; skärmen har tre halva saker
(07:s text, arkets nedre kant, "Hur vi tänker") och inget dominerande element (H-08).

## Target

**A.** Padding som inte kan bli ogiltig, och kickern i railen.

```css
/* target, index.html:881-883 */
  .principles{background:var(--bg);color:var(--ink);
    --panel-pad-y:clamp(28px,4.6vw,52px);
    padding:var(--panel-pad-y) var(--rail-x) clamp(64px,10vh,120px);}
  .principles .ledger{max-width:64ch;}
/* target, ny rad efter index.html:741 (.process-lead) */
  .process > .kicker-sans{padding-inline:var(--rail-x);}
```

Mätbart: `getComputedStyle(document.querySelector('#principer')).paddingLeft` = `--rail-x`
(86,4 px vid 1440, 23,4 px vid 390); kickerns text i `#process` och `#principer` börjar
på samma x som `.process-title`:s text (86,4 / 23,4 px).

**B.** Tre ankare i stället för två, samma JS-funktion.

- `--s1` (båda bredderna): arkets överkant (`.process-stick`) når 95 % av viewporthöjden.
  Konturen ritas alltså när arket kommer in, inte när steg 01 gör det.
- `--sN`, N ≥ 2: 1440: `li N`:s överkant når **65 %** av viewporthöjden (var 85 %); 390:
  oförändrat 95 %.
- `--eN`: 1440 oförändrat (`li N`:s mitt i viewportens mitt); 390: `li N`:s **överkant
  når arkets underkant** (viewport-y = `sheetH`), så rubriken står precis under arket när
  ritningen är klar.

```js
/* target, index.html:1449-1459 (inne i for-slingan; stickY0 räknas en gång före den) */
      var stickY0 = stick ? stick.getBoundingClientRect().top + window.scrollY - top : 0;
      ...
        var y0 = lr.top + window.scrollY - top, yc = y0 + lr.height / 2;
        var sTop = (i === 0) ? stickY0 : y0;
        var s = (sTop + vh * ((mobile || i === 0) ? 0.05 : 0.35)) / life;
        var e = (mobile ? (y0 + (vh - sheetH)) : (yc + 0.5 * vh)) / life;
        process.style.setProperty('--s' + (i + 1), s.toFixed(4));
        process.style.setProperty('--e' + (i + 1), e.toFixed(4));
        stepAnchors.push({ s: s, yc: yc, y0: y0 });
```

**B4, hysteres på gruppernas synlighet** (Astra loop 1, fix 2 och H-28): `readState` slår
`data-on` av så snart den råa `pps < s`, medan `--sc-ps` (lerpad, 0,16 per ruta) fortfarande
ligger över `s` och banan håller på att dra sig tillbaka; vid scroll uppåt försvinner steget
alltså i ett klipp i stället för att ritas baklänges. Rad 1515: `var on = pps >= stepAnchors[i].s;`
→ `var on = groupsOn[stepNum] ? pps >= stepAnchors[i].s - 0.03 : pps >= stepAnchors[i].s;`
(0,03 av `life` ≈ 135 px vid 1440, mer än lerpen hinner släpa). Mätbart: scrolla från
`?preview=process-03` uppåt 400 px i 20 px-steg med 60 ms mellanrum; `#p-opening`s
`stroke-dashoffset` ska passera minst fem mellanvärden mellan 0 och 1 px innan gruppen
försvinner (läs `getComputedStyle` per steg).

`sheetH` är redan `stick.getBoundingClientRect().height` (410 px vid 390, inklusive
`padding-block:12px`); på 1440 är den 0 och används inte. Preview-scrollen (rad 1667-1670)
följer det nya `--eN`: mobil `target = stepAnchors[pi].y0 - sheetHPrev` (li:s överkant vid
arkets underkant), 1440 oförändrad.

Räknat mot `diag.json`: vid 1440 blir `--s(N+1) − --eN` = (h_N/2 − 0,15·vh)/life ≥ (197 −
135)/4552 > 0 för det kortaste steget (07, 394 px): inga överlapp. Vid 390 blir villkoret
`h_N < 0,95·vh − sheetH` = 392 px; alla sju li är 357 till 453 px, steg 07 (357) ger en
överlapp på 35 px mot ett steg utan grupp (06), alltså ingen synlig läcka. Konturens fönster
(`--k1` 0 till 0,55) ritas vid 390 medan arket vandrar från 95 % av viewporten upp till sitt
sticky-läge (802 px scroll), vid 1440 från 95 % till 50 % (~630 px).

**C.** Låt gridets rad räcka förbi steg 07.

```css
/* target, index.html:733-734 */
  .process{background:var(--bg);color:var(--ink);position:relative;
    padding-block:clamp(48px,8vh,88px) clamp(40px,6vh,64px);}
/* target, index.html:746 (.process-steps) */
  .process-steps{list-style:none;margin:0;padding:0 0 clamp(160px,22vh,220px);}
```

Räknat: arkets underkant i sticky-läge är 202 + 464 = 666 px vid 1440x900. Med `li 07`:s
överkant vid 20 % (180 px) är `<ol>`:s underkant 180 + 394 + 198 = 772 ≥ 666: arket står
kvar helt synligt medan 07 läses. Sektionens totala höjd växer med ≤ 120 px. Vid ≤ 1279
(arket sticky ovanför) ändrar paddingen ingenting synligt: hållet släpper först när
`<ol>`:s underkant passerar arkets, alltså efter att 07 gått in under arket.

**D. Arket vid låga viewports ≤ 1279** (Astra loop 1, fix 4; H-35): `.process-stick{width:min(100%,480px)}`
med `aspect-ratio:320/360` ger 540 + 24 px = 564 px vid 480 px bredd: vid 1024x640 återstår 76 px
för texten under det sticky arket, vid 720x450 täcker arket hela viewporten. Rad 891-893:

```css
/* target, index.html:891-893 */
    .process-stick{order:-1;position:sticky;top:0;z-index:2;
      background:var(--bg);padding-block:12px;justify-self:center;
      width:min(100%,480px,calc((100svh - 200px) * 320 / 360));}
```

Arket lämnar då alltid ≥ 200 px text under sig: vid 640 px höjd blir arket 391 px brett
(440 + 24 högt), vid 450 px höjd 222 px brett. Mät `.process-stick` height + 200 ≤ innerHeight
vid 1024x640, 900x600 och 720x450; `reflow.py --extra-viewport` på samma tre.

## Repo conventions to follow

- `--rail-x` (rad 156) är sidans enda railmått; `.process-title`/`.process-lead` använder
  det redan.
- `measureAct` är den enda platsen som skriver `--s1..--e7` (plan 019); CSS-fallbacken på
  `#process` (rad 826-829) rörs inte.
- `?preview=process-0N` (rad 1655-1670) läser `stepAnchors`; håll formen `{s, yc, y0}`.
- Ledgerrad i `BRIEF.md` § Byggarens rader, R7: "Stegens ankare" med de tre reglerna och
  varför 390:s `--eN` byter tecken (li:s överkant vid arkets underkant, inte li:s mitt under
  arket).

## Steps

1. A: byt rad 881-883, lägg `.process > .kicker-sans`-raden efter rad 741. Mät
   `paddingLeft` på `#principer` och kickerns x vid 1440 och 390.
2. B: skriv om rad 1449-1459 enligt Target (stickY0 före slingan, tre ankare, `y0` i
   `stepAnchors`); byt mobilgrenen på rad 1667-1669 till `stepAnchors[pi].y0 - sheetHPrev`.
3. B, mät: läs `--s1..--e7` ur `getComputedStyle(process)` vid 1440x900 och 390x844 och
   skriv alla fjorton tal i NOTES.md § R7; villkor `--s(N+1) > --eN` för N = 1..6 vid 1440,
   och för N = 1..5 vid 390 (N = 6 får överlappa, 06 saknar grupp). Faller villkoret vid
   1440 för något N: höj 0,35 till 0,40 och mät om; faller det ändå: STOPPA, skriv talen.
4. B, bild: `?preview=process-01..07` vid 1440 och 390. 1440: i preview N får ingen bana ur
   `g[data-step="0(N+1)"]` vara synlig (kontrollera med `getComputedStyle` att gruppens
   `--p-l`/`--p-t` är 0 eller att gruppen saknar `data-on`). 390: `li N`:s överkant ligger
   inom ±12 px från `.process-stick`:s underkant, och rubriken under arket är steg N:s.
5. B, ankomst: tolv ramar genom `#process` vid 390 (som `shots/loop-1/process-390/`): i
   ingen ram där `li 01`:s rubrik syns är arkets kontur mindre än halvritad.
6. C: byt rad 733-734 och 746. Mät vid 1440x900: scrolla så att `li 07`:s överkant står
   vid y = 180; `.process-sheet` top ≥ 0 och bottom ≤ 900.
7. PageDown-vandringen (a11y fix 3) om igen: 7/7 steg.

## Boundaries

- Rör inte stegens copy, arkets banor, fönsterandelarna per bana (rad 838-870) eller
  `--k1..--k7`-kedjan.
- Rör inte `.process-stick`:s `top` eller 1279-brytpunkten.
- Matchar inte raderna 733-734, 741, 746, 881-883, 891-893, 1449-1459, 1515, 1667-1670: STOPPA.

## Verification

- **Mekaniskt:** paddingLeft-mätningen (A); de fjorton talen och villkoret (B); rect-mätningen
  (C); `reflow.py` 320 + 200 % och `--extra-viewport` 1280x800, 1366x640 (arket klipps inte);
  `a11y_scan.py` 0 violations; `motion_probe.py --track "#process:--sc-ps" --cpu 4
  --wheel 100:60 --ticks 45 --start 4900`: staircase 0, tal före/efter sida vid sida.
- **Skärmbild:** `preview-1440-process-01..07` och `preview-390-process-01..07` lästa som
  bilder mot steg 4; `v3c-1440--s05`/`s09`-motsvarigheter: kickern i railen, arket helt
  synligt bredvid 07; 390-ramsekvensen mot steg 5.
- **Feel check:** vid 390 kommer arket in med sin kontur ritande, texten följer under det;
  vid 1440 ritas varje steg medan dess rubrik står i övre halvan av skärmen och inget ritas
  i förväg.
- **Done when:** H-30 bockad (preview N visar bara steg N), H-08 för skärm 07, leadens tre
  R6-fynd stängda, B4:s mellanvärden lästa, D:s tre viewports mätta.

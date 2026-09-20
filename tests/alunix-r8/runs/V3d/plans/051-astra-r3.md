# 051 · V3d R4: Astras andra granskning (r3-astra.md)

- **Status**: TODO (V3d R4, en runda)
- **Beställning**: `reviews/r3-astra.md` § material_fixes (8 fynd). Lead tar 7, släpper fynd 7
  (Hōrai-overflow, ligger i `sites/horai.html`, rörs aldrig). Ordning: funktionsfel (1,2,3,4)
  före skala/typografi (5,6) före rest (8).
- **Bindande**: ingen fix löses genom att backa ett djärvt drag (arket, siffrorna, rubrikerna,
  Calyx mindre). Låst copy 15/15. Noll tankstreck. F-011/F-014. Motorn, `scroll/*.js`,
  `scrollcraft.css`, `sites/*` orörda. Ingen tredje iframe.

## Fix 1 · P13 steg 07 står aldrig still

**Problem.** `--e7` (`:1175`, `.69`/`.76` CSS-fallback, JS-mätt i measureAct) sätter k7=1 vid
ps≈0,944, men `.process-stick` (den sticky bildrutan) släpper sitt grepp när
`.process-steps`-gridet tar slut, vid ps≈0,90 — 07 hinner aldrig stå stilla i ett färdigt ark.
Revisionsfältet (`#p-rev`, steg 07) hamnar samtidigt över Calyx nedre vänstra hörn vid en
mellanposition.

**Target (Astra).** Organisk hjulscroll ger minst ett läge med k7=1 OCH arkets top=`--band-h`
(dvs `.process-stick` fortfarande i sitt stickade viloläge). `#p-rev`s rect ska ligga innanför
arket och utanför `.p-live`s rect (bilden).

**Fix.** Förläng `.process-steps`s totala scrollhöjd med ≥0,6×vh EFTER sista `<li>` (steg 07),
så stickens släpp (styrd av gridets totalhöjd) inträffar EFTER att k7 hunnit nå 1. Minsta
ändring: lägg till `padding-bottom` eller en sista tom höjd på `.process-steps` (inte en ny
kod-scen, bara mer scrollutrymme för samma färdiga bild) — mätt mot den faktiska releasepunkten,
inte gissat.

## Fix 2 · P04 jättens bredd nås för sent

**Problem.** `--scrub` (`:871`, start 0,364 bredd 0,315) mättes INNAN R2:s
`margin-top:820px` (`:918`) sköt upp `.panel-giant`s naturliga scrollposition — konstanterna
är inaktuella. Full bredd (`--scrub`=1) nås först vid ps som redan skurit av rubrikens
överkant. `?preview=ledger` tvingar `--scrub:1` oavsett scroll, vilket visar ett läge organisk
scroll aldrig producerar.

**Target.** Mät om start/bredd så att `--scrub`=1 exakt när `.panel-giant` har top≈80-120px
(rubriken fortfarande helt i viewporten). Plåten ≥1150px bred medan hela
"VI BYGGER ERT VARUMÄRKE." är synlig.

**Fix.** Bisektionssökning (Playwright) för scrollY där `.panel-giant.getBoundingClientRect().top`
ligger i [80,120], läs `--sc-ps` där, sätt det som ny slut-konstant för `--scrub`s `clamp(...)`.
Behåll samma STRUKTUR (en `clamp` mellan start och bredd), bara talen omräknade.

## Fix 3 · P06 kapitelskärmen delar aldrig ensam

**Problem.** `.process-lead{margin-bottom:clamp(96px,16svh,180px)}` (`:1000`) är för kort —
band 01 (siffra+titel+stycke) syns redan i kapitelskärmens nedre tredjedel vid 1440. Vid 390
står rubriken i övre tredjedelen och nedre halvan är tom.

**Target.** P06-1440 visar ingen del av band 01. Vid 390: rubrik ≥56px, vertikalt centrerad,
ingen tom nedre halva. `P16`s kontaktark får högst fyra mörka skivor i följd (kapitelskärmen
får ETT ljust materialtoken — papper eller blått — INTE en ny ljus scen i processakten:
Anton beställde akten inverterad, ingen ljus yta stoppas in mitt i den. Lösningen är
kapitelskärmens EGEN grund, inte en scen i flödet).

**Fix.** `margin-bottom` räknat mot uppmätt `calc(100svh - <titelblockets uppmätta höjd>)` i
stället för den fasta clampen. Kapitelskärmens egen bakgrund (`.process > .kicker-sans` +
`.process-title` + `.process-lead`s block, INNAN `.process-grid` börjar) får ett ljust
materialtoken (papper) via en scoped bakgrundsregel på det blocket, inte på hela `.process`.

## Fix 4 · P10/P12 mobilarket vid 390

**Problem.** `#p-c-row` (`:1794`) positioneras med SVG `x=102 y=333` (skrivbord), men
`plansch()`s mobilblock (`:1360-1371`) sätter CSS `x/y` på `#p-hatch`/`#p-dim-row` men INTE på
`#p-c-row` — en `<text>` ignorerar CSS `x`/`y` (bara SVG-attribut gäller), och `#p-c-row`
saknas dessutom i `MOBILE_TEXT` (`:2490`), så texten "96 px" hamnar kvar på skrivbordskoordinaten,
utanför viewBox 320×300. `#p-hatch` mobil (16×16px, `:1360`) är för liten för att läsas som en
synlig ändring. Steg 06: Calyx fyller bara ~56% av ett 358×335 ark (stor tom rand runt).

**Target.** `process-04` vid 390 visar "96 px" INOM arket. `process-06` vid 390 visar Calyx på
≥80% av arkets yta ("utan lika mycket luft" — Antons krav).

**Fix.** Lägg `p-c-row` i `MOBILE_TEXT` med mobilkoordinater inom viewBox. Ta bort de
verkningslösa CSS `x`/`y` på `#p-c-row` (`:1362`, ersätts av `MOBILE_TEXT`s SVG-attribut-sättning).
Höj `#p-hatch` mobil till ≥48px hög. Ge `#p-live-img`/`#p-open-rect` (Calyx-bilden i steg 06)
mobilarkets fulla höjd/bredd i stället för dagens mindre yta.

## Fix 5 · P03 tesrubriken för liten

**Problem.** `.thesis-headline` (`:635`, `clamp(1.4rem,2.7vw,2.4rem)`) mäter bara 38,4px vid
1440 mot referensens ~80px, läses som en bildtext, inte en rubrik. Den blå panelen täcker bara
~55% av viewportens höjd.

**Target.** Rubrik ≥64px vid 1440. Bilden fortsatt ≥40%vw. **0 delade ord vid 1024/1280/1440**
— R3:s regression (14ch-golvet som alltid vann) får INTE återkomma. Panelen ≥80% av
viewportens höjd i tesintervallet.

**Fix.** Höj clampen (t.ex. `clamp(2rem,4vw,4rem)` eller liknande, räknat mot 64px-golvet vid
1440). Mät radantal/delade ord med SAMMA skript som R3 vid alla fem breddar (768-1920) efter
ändringen — om spalten (`minmax(340px,1fr)`, R3:s fix) inte räcker vid den nya, större
fontstorleken, bredda spalten ytterligare (aldrig smalare). Panelens höjd: `--panel-pad-y`
eller `.panel-thesis`s egen min-height justerad mot uppmätt 80%-mål.

## Fix 6 · P02 kortbaksidans ordmärke för litet

**Problem.** `.card-mark{font-size:clamp(3.2rem,9cqw,7.5rem)}` (`:503`) mäter 80,6px vid 1440,
tar en tredjedel av kortets bredd. Referensen låter ordet äga mitten.

**Target.** ALUNIX ≥100px vid `?preview=back`, 1440. Ordet ~50% av kortets bredd. Ordmärket
klipps aldrig vid någon bredd (kollisionskoll mot `.card-glyph`/`.card-services` som redan har
en dokumenterad avvikelse för smala viewports, `:494-501`).

**Fix.** Höj clampens golv/mitt (9cqw → större cqw-faktor, eller ett större rem-golv), mätt
mot 100px vid 1440 och kontrollerat mot `.card-glyph`/`.card-services` vid alla breddar.

## Fix 7 · Hōrai-demon svämmar över vid 390 — TAS INTE

`sites/horai.html` har `scrollWidth` 675px i en 390px ram. Filen ligger utanför denna runda
scope (motorn/`sites/*` rörs aldrig). Noteras i NOTES, ingen kodändring.

## Fix 8 · Glyffragment vid aktens utgång + föräldralösa linjer i steg 05

**Problem A.** Band 07:s `--slit-p`-klipp (`:1075-1078`) gäller bara INKOMMANDE band (klipper
in från botten när `--sc-ps` når `--slit-start`), men klipper ALDRIG UT när bandet lämnar i
den andra änden av sin egen `<li>` — vid scrollY≈13100-13160 (aktens absoluta slut) skärs
glyfer av "FÖRVALTNING" och "--" kvar synliga, delvis klippta av viewportkanten, inte av
`clip-path`.

**Target.** Inget partiellt glyf i någon hjulbild genom hela akten (båda riktningar).

**Fix.** Utöka `--slit-p`-formeln med en motsvarande UTGÅENDE klippning nära aktens slut (band
07 specifikt, eftersom det är sista bandet och saknar ett "band 08" som skulle ha tryckt det
ur syn via den normala mekanismen). Mätt mot den faktiska scrollY-positionen där fragmentet
uppstår.

**Problem B.** `#p-ledgers,#p-hatch{opacity:calc(1 - 0.65 * var(--k6))}` (`:1154`) saknar
`--cam-fade` (som `#p-c-gutter`/`#p-dim-gutter` m.fl. redan har, `:1242-1244`) — de tre
streckade `#p-ledgers`-linjerna (steg 04:s materialgräns) förblir synliga vid full opacitet
genom hela steg 05 eftersom `--k6` är 0 där, och kamerans egen zoom/pan (förbi steg 04) gör att
de driver iväg från sina ursprungliga koordinater, syns "föräldralösa" (utan etiketter) i
Calyx-bildens kant.

**Target.** Inga streckade linjer utan etikett i `process-05`.

**Fix.** `#p-ledgers,#p-hatch{opacity:calc((1 - 0.65 * var(--k6)) * var(--cam-fade));}` —
samma multiplikativa mönster som `#p-guides` redan använder (`:1164`), en rad, ingen ny
variabel.

## Verifiering

- Varje fix mätt mot Astras "Expected" med skript OCH bild (screenshot läst personligen).
- Par-bilder P02, P03, P04, P06, P10, P12, P13, P16 i `shots/r4/`, en skärm per sida via
  `mouse.wheel`, 1440 och 390.
- Hjulscrollsekvenser genom HELA processakten vid 1440 och 390, var 150:e px, lästa: rent
  mellan band, varje steg ändrar arket.
- Hela grinden: `scroll_verify`, `motion_probe` (kontroll först, båda riktningar),
  `contrast_over_media --url`, `a11y_scan`+`reflow` vid 390/768, 0 horisontell scroll
  320-1920, rubrikskriptet (0 delade ord), låst copy 15/15, grep (tankstreck,
  prefers-reduced-motion, inline-hex-tillväxt).

**Done when:** alla 7 tagna fynd mätta mot Expected, fynd 7 noterat men orört, grinden ren
eller varje avvikelse namngiven.

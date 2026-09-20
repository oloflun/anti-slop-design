# 062 · V3d: Blåkopian, arket — det blå planet blir ritningens ark

- **Status**: TODO (V3d R19, en byggrunda). Svar på `reviews/r18-astra.md`: `fix`, fyra
  material_fixes, plus Antons egen dom ("extremt platt" står kvar, för återhållsam).
- **Beställning**: Anton/lead 2026-09-19. Övergången tes → ritning byggs om i grunden: det blå
  tesplanet krymper, scrubbat på `--sc-ps` båda riktningarna, från helbredd till exakt
  ritningsarkets rektangel i steg 01. Blåkopians konstruktionslinjer (R18) står kvar som ett
  andra lager, men rättade (Astra fynd 1–2). Plus Astra fynd 3 (Hōrai-montering fryser
  Calyx→Hōrai) och fynd 4 (delat ord i prisliggaren).
- **Ordning**: fynd 4 (en rad) → fynd 3 (monteringstajming) → övergången (störst) → verifiering.
  Ett djärvt drag backas aldrig för att laga ett fel; R18:s stegband och ramarbete rörs inte.

## Nuläge (R18/Astra)

- `.seam-up`/`.seam-dn` (fyra 1px-linjer, `index.html:1160–1176`): kontrast 2,86:1 mot det blå,
  under 3:1. `.seam-h` (landningslinjen) är 1×1px — `.seam i{width:1px}` (specificitet 0,1,1)
  vinner över `.seam-h{width:calc(...)}` (0,1,0).
- Ingen yta krymper. Fyra lösa streck "hänger i luften" (Astra), ingen ark-form landar.
- Hōrais `mountFrame` triggas av en IntersectionObserver (`rootMargin:'40% 0px'`,
  `index.html:~2704`) som råkar slå till mitt i Calyx→Hōrai-övergången (lager 2, grundbytet
  papper→svart): 383/646/485 ms huvudtrådsblock vid 1440/1920/390.
- `.price-row .label` "SEO-optimering" bryts "SEO-" / "optimering." vid alla tre bredderna
  (`index.html:~2106` i markupen, `Standardpaket…SEO-optimering.`).

## Idé: arket landar, inte bara linjer

Det blå planet ÄR inte tesbandets egen DOM (den är en separat, redan pinnad sektion som slutar
innan kanten når sitt eget slut — mätt R16/R18: 214px ren blå yta ovan kanten vid 1920, alltså
sista meningen och fotot har redan lämnat bildrutan innan `--tx` någonsin börjar). Planet är i
stället en ny, syntetisk yta i `.process-chapter` (samma trick som `.seam`: målad ovanför
kapitlets egen överkant med `bottom:100%`, samma `z-index:3`-lager som redan vunnit över `#tes`).
Den startar som en hel skärm blått (samma `--c-accent` som tesen) rakt ovanför kanten — vid `tx=0`
alltså exakt där tesens sista, redan orörliga bildruta skulle synas — och täcker den ytan helt
(opak), så inget separat uttoningsgrepp på `#tes`s egna `.ts`/`.thesis-photo-box` behövs eller
rör motorn.

**Geometri.** Planet: `position:absolute; left:50%; width:100vw; transform:translateX(-50%);
bottom:100%; height:100vh;` — en hel viewport bred och hög, liggande direkt ovanpå kanten. Det är
läsbart som "den sista skärmen blått" utan att vara beroende av tesens egen scrollposition.
Målet: arkets rektangel i steg 01, mätt av `measureAct` (samma mönster som `--x1..--x4`):
`--p-t/--p-r/--p-b/--p-l` = hur många px planet måste klippas in från topp/höger/botten/vänster
för att dess synliga yta ska bli EXAKT `.process-sheet`s rect. Räknat direkt i viewport-koordinater
(planet spänner alltid exakt 0..100vw och `chapterTop-100vh..chapterTop`, så inga extra
koordinatbyten behövs):
```
sheetR = .process-sheet.getBoundingClientRect()
chapterR = .process-chapter.getBoundingClientRect()
--p-t = sheetR.top - (chapterR.top - vh)
--p-r = vw - sheetR.right
--p-b = chapterR.top - sheetR.bottom
--p-l = sheetR.left
```
`clip-path: inset(calc(tx*--p-t) calc(tx*--p-r) calc(tx*--p-b) calc(tx*--p-l))` — vid `tx=0` hel
skärm, vid `tx=1` exakt arkets rektangel. Ren `calc()` på `--tx` (F-014), reversibel per
konstruktion (samma klocka som B1/R18, ingen ny mätning per bildruta).

**Två koordinerade lager, som krävt:**
1. **Planet** (nytt): bakgrund tonas `--c-accent` → `--c-drafting`
   (`color-mix(in oklab, var(--c-accent), var(--c-drafting) calc(var(--tx)*100%))`), klipps in
   mot arkets rektangel. En vit kontur (`box-shadow:inset 0 0 0 2px …`) tonas in sent
   (`tx` 0,6→0,9) så den läses som att arket "stelnar" när planet landar, inte som en ram som
   funnits hela tiden.
2. **Linjerna** (R18, rättade): kvar oförändrade i mekanik (`--x1..--x4`, `--up/--dn`, samma
   `--tx`-fönster 0,30/0,75/0,70–0,85), men:
   - Fix 1: `.seam .seam-h{width:…}` i stället för att låta `.seam i{width:1px}` vinna.
   - Fix 2: arkets kantlinjer (`data-l="1"`/`"4"`) och landningslinjen 2px; stationerna
     (`data-l="2"`/`"3"`) 1px kvar (de är arkets egna hjälplinjer, tunnare per K3-registret).
     `--seam-on-blue` byts mot ett mörkare, mättare blandningstal så kontrasten mot `--c-accent`
     (`#1e5e9c`) mäts ≥3:1 (uppmätt, inte gissat — se Verification).

**Rubriken** kommer fortfarande först när arket landat (`tx` 0,78→1, R18 orörd).

## Beslut

- **B1 (nytt).** Planet byggs som en helt ny yta, inte en omritning av `.seam`. Ingen ny akt: samma
  `--tx` från `.process-chapter`s nästlade flow-akt (R18 B1, orörd).
- **B2.** Tesens egna `.ts`/`.thesis-photo-box` rörs inte. Vid `tx=0` är kanten redan 214px (1920)
  under fotots underkant (uppmätt R16/18) — planet, som är opakt och ligger ovanpå (`z-index:3`
  mot `#tes`s 2), täcker bara ren blå yta från första bildrutan. Inget separat fade behövs.
- **B3.** Under 1024 (768, 390): planet krymper till mobilarkets rektangel på samma sätt (samma
  `--p-t/--p-r/--p-b/--p-l`-formel, mätt mot `.process-sheet` i dess mobila läge). Ingen
  förenkling behövs — geometrin är bredd-agnostisk.
- **B4 (fynd 3).** Hōrais `mountFrame` får ett extra, tidigare triggervillkor i `latchTick`:
  när Calyx (`CASES[0]`) egen `cAct.cur >= .4` (inom steg 1–3 av 5, god marginal före
  övergångens 0,80–1,0) och Hōrai-iframen fortfarande har `data-src`, köa montering med samma
  `requestIdleCallback`/`defer`-mönster som IO redan använder. `mountFrame` är idempotent
  (`if (!s) return`), så IO:s egen 40%-trigger kan stå kvar oförändrad som fallback (t.ex. vid en
  snabb direktlänk till Hōrai-sektionen som hoppar över Calyx-svepet).
- **B5 (fynd 4).** `SEO-optimering` → `SEO&#8209;optimering` (icke-brytande bindestreck, U+2011).
  Ordvalet oförändrat.

## Target

| # | Synligt mål | 1920/1440 | 390 |
|---|---|---|---|
| 1 | Planet krymper till arket | `tes-till-ritning-0`: hel skärm blått, ingen kontur. `-2`: klippt till ~50% väg mot arket. `-4`: klippt exakt till `.process-sheet`s rect ±2px, kontur synlig | samma |
| 1 | Färgton | `-4`: planets bakgrund = `--c-drafting` (samma som ritbordet) | samma |
| 1 | Kontur | Osynlig vid `tx<0,6`, tonad in `0,6→0,9`, 2px vit (`≥3:1` mot `--c-drafting`) vid `tx=1` | samma |
| 1 | Linjekontrast | `--seam-on-blue` mot `--c-accent` ≥3:1 (rasteriserad pixel) | samma |
| 1 | Landningslinjen | `.seam-h`s renderade bredd = `--x4 - --x1` (±1px), inte 1px | samma |
| 1 | Ingen halvklippt rubrik | `elementFromPoint`-svep + geometrisk kontroll: 0, båda kontrollerna körda mot en trasig version först | samma |
| 1 | Scrubbat, båda hållen | `motion_probe` på `.process-chapter:--sc-ps`: staircase 0, max_step ≤3% | samma |
| 1 | F-011/F-014 | 0 `prefers-reduced-motion`; alla nya regler läser `--tx`/`--sc-ps`, ingen `transition` | samma |
| 3 | Hōrai fryser inte | 0 uppgifter >50ms mellan Calyx `--sc-ps` 0,80 och Hōrai steg 1, vid 1440/1920/390 | samma |
| 4 | Ordet bryts inte | 0 delade ord i `.price-row` vid 320–1920 | samma |

## Steps

1. Fynd 4: markup, `SEO-optimering` → `SEO&#8209;optimering` i `.price-row .label`.
2. Fynd 3: JS, `latchTick`s CASES-loop — extra villkor för Hōrai-montering vid Calyx `cur>=.4`.
3. Övergången:
   1. CSS: nytt `.tes-plane`-element + regler (klipp, tona, kontur).
   2. Markup: `<div class="tes-plane" aria-hidden="true"></div>` i `.process-chapter`, före
      `.seam`.
   3. JS: `measureAct` skriver `--p-t/--p-r/--p-b/--p-l` (samma plats som `--x1..--x4`/`--dn`).
   4. CSS-fix: `.seam-h`-specificitet, linjebredd 2px på kant+landning, `--seam-on-blue`
      kontrastjustering.
4. Verifiering: se plan-huvudets Target-tabell + rundans egna instruktioner (svep+geometrisk
   kontroll mot trasig version först, `motion_probe` med kontroll först, pixeldiff mot R18,
   `perf_probe`, `microtext_scan`, rubrikskript, `a11y_scan`, 0 horisontell scroll).

## Boundaries

- Kontrasten för konturen eller linjerna går inte att nå 3:1 utan att byta bort `--c-accent`
  (låst token): STOPPA, skriv i NOTES, föreslå ett alternativt blandningstal som lead godkänner.
- Hōrai-monteringen fortsätter blockera >50ms trots tidigareläggning: STOPPA, mät var uppgiften
  faktiskt går (nätverk vs. DOM-arbete) i stället för att gissa på en till tajmingjustering.

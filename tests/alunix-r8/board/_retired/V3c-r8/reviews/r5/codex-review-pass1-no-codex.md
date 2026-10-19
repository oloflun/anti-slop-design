fix

(Pass 1: Codex körde INTE. `codex-cli 0.148.0` avvisar `gpt-6-astra` med "requires a newer version of Codex", och alla fallback-modeller är spärrade för kontot. Rapporten nedan är wrapperns egen granskning mot fil och PNG. Lead uppgraderade CLI:t till 0.154.0 och körde om agenten; se `codex-review.md` för passet med Astra.)

## persistence

Codex did not run. `codex exec -m gpt-6-astra -c model_reasoning_effort="medium"` with all 20 images attached returned HTTP 400: "The 'gpt-6-astra' model requires a newer version of Codex." Installed CLI was `codex-cli 0.148.0`. Fallbacks `gpt-5.1-codex-max`, `gpt-5.1-codex`, `gpt-5-codex`, `gpt-5.1` all returned "is not supported when using Codex with a ChatGPT account". Findings from Codex: 0 returned, 0 verified, 0 dropped. Everything below is the wrapper's own first-pass review, each item verified in `index.html` at the cited line and in the named PNG, or by arithmetic against the engine's flow formula `p = (y + vh - top) / (height + vh)` (`scroll/scrollcraft.js:37`, reproduced by `processPs()` at `index.html:1315-1321`).

## fidelity

Akten är byggd som planen beskriver den mekaniskt: sektionen mellan `.stagger` och `footer.close` (`index.html:1079`), `data-sc-act="flow"`, 300 svh, sticky-ark, sju `<li>` med `--step-start/--step-end`, sju `?preview=process-0N`, allt rörligt läser `--sc-ps` (H-28). Måttfönstren är förskjutna ett steg, och 390-målbilden är i praktiken inte byggd.

1440: s-01 avviker (A-glyfen saknas helt, tom kontur); s-02 avviker (320 · 768 · 1440 syns inte, fönster 0,35 mot mitt 0,325); s-03 avviker (`7 rem`, `16:9` saknas, fönster 0,43/0,46 mot mitt 0,415); s-04 avviker (`96 px` saknas, fönster 0,52/0,55 mot mitt 0,505); s-05 matchar; s-06 matchar; s-07 avviker (arket klippt 135 px upptill, footern äger 60 % av skärmen; sticky släpper vid ps 0,806, previewens mitt är 0,90).

390: alla sju avviker av tre orsaker: (a) texten ligger över arket, inte under; (b) alla sju stegtexter syns samtidigt (`opacity:1 !important`); (c) arket är inte sticky och kommer in i vy först vid ps ≈ 0,52, redan färdigritat (`proc-390-05.png`).

Gate 47/79 ren (12 banor, alla namnbara). Gate 88 ren. Gate 75 ren i synlig text (två träffar i kommentarer, `index.html:343`, `:1457`).

## ceiling

- Motorn (`scroll/scrollcraft.js:37`, `sc-smooth.js`): progress monoton och stegfri över hela `height + vh`; aktens egna fönster använder bara 0,19 till 0,81 av livet, de första och sista 684 px är ritmässigt tomma.
- K3 (`board/cells/K3-r8/index.html`): håller utropet uppe inom den skärm måttet hör till (siffrorna räknas upp medan banan ritas), och dess mobila plansch är sticky med texten under. V3c lånade tekniken korrekt men inte kadensen och inte den mobila formen.
- Sidans egen `.plate-card` (`index.html:361-372`): hela uttrycket i ren CSS utan hårdkodad viewporthöjd; processens scen skriver `top:202px; height:495px` (`:691`) som konstant.

## material_fixes

1. `index.html:802, :807, :808, :817`: varje skärms sanna mått tänds ett fönster för sent. Mål: varje `--p-t`-fönster är helt (värde 1) vid sitt stegs mittvärde: siffrorna 0,30 till 0,32, `7 rem` 0,395 till 0,41, `16:9` 0,40 till 0,415, `96 px` 0,48 till 0,50; banfönstren (`:799-816`) komprimeras så att varje bana är färdigritad före sitt utrop.
2. `index.html:1473-1474`: `?preview=process-07` står utanför sticky-hållet (`PROCESS_MID['07'] = 0.90`, hållet släpper vid 0,806). Mål: `'07': 0.785`, och `#p-c-rev`s fönster (`:821`) från 0,81 till 0,77.
3. `index.html:835-841`: 390-målbilden är inte byggd. Mål: (a) `.process-sheet{order:-1}`; (b) ta bort `opacity:1 !important` på `.process-steps li`, mobila fönster 01 0,17-0,26 … 07 0,71-0,83; (c) arket `position:sticky; top:12svh` inuti scenen.
4. `index.html:691, :695, :720`: arket klipps mellan 900 px och ~1404 px bredd (384 + 880 + padding kräver 1404 px; `overflow-x:clip` döljer spillet). Mål: `width:min(880px, 100% - 384px - 140px)`, `height:auto`, `aspect-ratio:880/495`, eller planschbrytpunkten flyttad från 899 till 1400 px. H-35.
5. `index.html:931` + `:1176` + `:794-797`: A-glyfen ritas vitfylld (`fill="#ffffff"` som presentationsattribut vinner över ärvd `fill:none`), syns som en spökfläck på papperet. Mål: `fill="currentColor"` på originalbanan, eller en egen `<path>` i arket som hårlinjekontur.
6. `index.html:796`: `#p-mark`s fönster börjar exakt på previewens mittvärde (0,235). Mål: fönster 0,205 till 0,225.
7. `index.html:691`: `top:202px; height:495px` är 1440x900 som konstant. Mål: `top:calc((100svh - 495px) / 2)` med golv `max(24px, …)`.
8. `index.html:783` och `:723`: `.process-sheet .guide,.process-sheet .hatch{opacity:…}` träffar även `#p-rev` (klass `hatch`), som därför aldrig syns i full vikt; `stroke-width:var(--contour-line)` på `:723` är död kod. Mål: selektorn till `#p-hatch, #p-guides, #p-ledgers`.

## keep

`--sc-ps` genomgående, ingen JS-stil per bildruta, `readState` rAF-skyddad med deadband; `will-change` bara via `.is-drawing`; höjdmekaniken ren CSS (`min-height:300svh` + sticky); ritmekaniken (`pathLength="1"`, `*1px`, `transform-box:fill-box`, `markerUnits="userSpaceOnUse"`); de fem `@property`-raderna (`:187-191`) och det utskrivna `clamp()`-uttrycket där `inherits:false` bryter kedjan; `<image>` med `width`/`height`, filtret på 538x303, ingen tredje iframe; `role="img"` med `<title>`/`<desc>`, stegen som `<ol>`; `--hair-ink` 4,89:1 och `.process-a` 8,75:1 mot papperet; skärmarna 05 och 06 matchar målbilden rakt av.

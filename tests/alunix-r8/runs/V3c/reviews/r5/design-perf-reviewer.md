fix

## persistence

**PASS.** Every input this review rests on was read or measured in this run, on this build.

Read this run: `~/.claude/skills/design/references/performance.md` (budget § 1, Never § 6), `motion-smoothness.md`, `~/.claude/skills/impeccable/reference/optimize.md` § NEVER, `runs/V3c/BRIEF.md` (§ Prestandaplan rad 522–539, device-tabellen rad 377–389), `malbilder/V3c.md`, `plans/010-process.md` § Verification, `NOTES.md` § R4 Plan 005 (rad 990–1052) och § R5 Mekaniska grinden (rad 1433–1532), `HELHET.md` H-21/H-22/H-32, `index.html` (1 520 rader, CSS 160–890 och JS 1 280–1 500 rad för rad).

Servern var uppe på 3090 (`serve.py`). Kontrollprotokollet, `tests/motion/smooth.html`, cpu 4: **6 kontrollkörningar**; körning 1 (2 rutor > 33 ms) och 3 (1 ruta) kasserades; 2, 4, 5, 6 rena (p95 16,7 ms / 0 rutor / staircase 0). Kontrollen vid cpu 1 ren (16,8 / 0). Varje sidmätning nedan togs med ren kontroll omedelbart före.

| Probe | Viewport / cpu | Exit | Utfall |
|---|---|---|---|
| `perf_probe.py` | 1440×900, cpu 4 | 1 | LCP 840 ms · CLS 0,000 · 9 långa tasks (1 under scroll) · 573,0 kB · 222 noder · inbäddat 48 kB. Enda fynd: `long-task-under-scroll 1` |
| `perf_probe.py` | 390×844, cpu 4 | 0 | LCP 696 ms · CLS 0,000 · 5 långa tasks (0 under scroll) · 573,0 kB |
| `motion_probe.py` 100:60, 75 ticks | 1440, cpu 4 | 1 | p95 **100,1 ms** · **196** rutor > 33 ms · staircase 0 på alla `--sc-ps`/`transform`-spår |
| `motion_probe.py` 20:120, 380 ticks | 1440, cpu 4 | 1 | p95 **50,1 ms** · **1 151** rutor > 33 ms · staircase 0 på alla fem spår |
| `motion_probe.py` 100:60 | 1440, cpu 1 | 1 | p95 **50,0 ms** · 51 rutor > 33 ms (H-22 faller) |
| `motion_probe.py` 20:120 | 1440, cpu 1 | 1 | p95 16,8 ms · 79 rutor > 33 ms |
| `motion_probe.py` (döda spår) | 1440, cpu 4 | 1 | `#heroPoolImg:transform` levande (max_step 1,55 %); `#threadFill`/`.giant` rapporterade DEAD, proben är blind på ren `scale()`, se fidelity |
| `perf_probe.py` + `motion_probe.py` på V3b | 1440, cpu 4 | 1 / 1 | referensmätning, se ceiling |

Uppåtriktningen mättes med en scratchdrivare som importerar probens egen `PROBE_JS` och `analyse()`: uppåt 100:60 cpu 4, heron staircase 0, `.plate-card:transform` max_step 2,80–3,05 %; `#process` staircase 0, dashoffsetspåren staircase 1 (samma kadensartefakt som nedåt). Uppåt 20:120: max_step 0,42 %, staircase 0. Inget spår stegar i någon riktning.

Sparklines lästa som bilder: `frame-times.png` bär i båda kadenserna en enda stor topp en tredjedel in, följd av ett permanent förhöjt band; toppen ligger där den första iframen monteras (rootMargin 100 % → scrollY ≈ 2 560, inuti den pinnade akten). Motorn rördes aldrig; `index.html` rördes aldrig; ablationer via route-interception mot en cachad kopia i scratchpad. Artefakter i scratchpad `perf/` (`perf-1440`, `perf-390`, `perf-v3b`, `motion-*`, `control-1..6`, `control-cpu1`) och `ablate.py`.

## fidelity

| Akt | Målbilden / plan 011 | Mätt | Dom |
|---|---|---|---|
| s1 0–0,10, ljuspölen | på `--sc-ps` | `#heroPoolImg:transform` levande, max_step 1,55 %, staircase 0 | Håller |
| s2 0,10–0,78, vändningen | `--flip` i ren CSS ur `--sc-ps`, båda riktningarna | `section.hero:--sc-ps` max_step 1,73 % / 0,27 %, staircase 0 i alla sex körningar; `.plate-card:transform` obruten ramp | Håller i värdet, faller i klockan |
| s3 0,78–1, vila | dwell 0,2 | platt på 1 | Håller |
| `#process` | banorna ur `--sc-ps` | `#process:--sc-ps` max_step 1,36 % / 0,20 %, staircase 0 | Håller i värdet |
| `#process`, rittempo | "linjen ska följa handen som en penna" | `#p-outline` max_step **25,3 %**, `#p-opening` **31,0 %** vid 100:60, staircase 1; vid 20:120 3,3 %/6,0 % | **Defekt.** Vid 100 px/hack ritas hela konturen på ~4 bildrutor: den snäpper. Fönstren 0,03–0,045 är för smala |

**Två DEAD-flaggor som är probens fel.** Proben dekomponerar `transform` via `atan2(b,a)` och faller tillbaka på translationen; ren `scale()` har b = 0 och läses som 0. Direkt matrisläsning visar båda levande: `.giant` 0,92 → 1, `#threadFill` scaleY 0 → 1. Proben ska smalnas av, inte waivas.

**Trådmätningen avslöjade en aktdefekt.** `.thread-fill` går scaleY 0 → 1 mellan scrollY 2 400 och 3 200, då `#projekt`s överkant står 1 374 → 574 px under viewportens överkant: tråden är färdigritad innan liggaren är läsbar. `--scrub` (index.html:617) är ankrad i `.panel-giant`s akt 0,15–0,60, inte i liggarens läge.

**Attribution, mätt.** 3 000 px hjuldrag genom `#process`, 1440×900, cpu 4, 100:60, median av 3, CDP `Performance.getMetrics`:

| Sidans tillstånd | recalc | layout | script | task | rutor > 33 ms / rutor |
|---|---|---|---|---|---|
| som den skeppas | 4 988 | 2 374 | 1 150 | **13 164** | 93 / 110 |
| ramarna dolda (`content-visibility:hidden` på wrapparna) | 3 449 | **117** | **218** | **4 516** | 93 / 128 |
| `/sites/**` blockerat | 4 741 | 115 | 305 | 6 070 | 102 / 114 |
| + `.process-sheet` `display:none` | 2 978 | 23 | 305 | 3 896 | 38 / 187 |
| + `.process-sheet` `content-visibility:hidden` | 3 080 | 138 | 254 | 4 115 | 66 / 161 |
| + `--sc-ps` fryst i hela `#process` | 2 210 | 6 | 318 | 3 117 | 43 / 167 |
| + `--sc-ps` fryst på alla 8 akter | 1 025 | 4 | 260 | 1 786 | 21 / 187 |
| + `.ground`s helskärmsfilter borttaget | 943 | 3 | 243 | 1 675 | 17 / 188 |
| `will-change: stroke-dashoffset` borttagen (mot blockerad baslinje) | 4 529 | 138 | 257 | 5 922 | 98 / 118 |

**Byggarens rotorsak är bekräftad som mekanism och motbevisad som ursäkt.** Bekräftat: den ärvda `--sc-ps`-skrivningen är det enda som rör stilomräkningen; `visibility:hidden` på ritningen ändrar inget, frysta banor ändrar inget, `contain` hjälper inte. Motbevisat: (1) **den största posten är de två levande iframarna, 8 648 ms av 13 164 ms (66 %), och hela layoutkostnaden 2 374 → 117 ms**; byggarens rotorsaksjakter kördes med `/sites/**` blockerat och maskerade posten. Ramarna monteras lazy + IO men **avmonteras aldrig** (`obs.unobserve(f)`, index.html:1381), och Calyx och Hōrai kör sina scroll-motorer på huvudtråden resten av sidan. (2) **`content-visibility: hidden` skär av det `contain` inte kan**: recalc 4 741 → 3 080, task 6 070 → 4 115, rutor 102 → 66. Aldrig testat av byggaren. (3) "≤ 60 banor" är fel storhet: arket har 35 element och 7 `.draw`-banor; kostnaden skalar med antalet deklarationer som läser `--sc-ps`. Resten när båda fixarna är gjorda: ~1 185 ms för de sju andra akternas ärvda skrivning plus ett golv ~1 700 ms, motorns och utanför cellen. Noll rutor > 33 ms vid cpu 4 är därför inte nåbart i den här rundan, men 196 → ~40 är det.

**Övriga grindar.** Ingen extern CDN. Ingen `transition: all`. Ingen `backdrop-filter`. Noll vilande `will-change`. Ingen layoutläsning i scroll-handlern (`readState` räknar ur `scrollY` mot cachade mått). `height:100vh` följs av `100svh`. `.ground`s helskärmsfilter (`:245`) är en utskriven gate 93-avvikelse, ommätt: 111 ms av 13 164, inom brus.

## ceiling

- **V3b-chain (Tier 0)**: står sig bredvid. V3b i dag: LCP 1 112 ms, CLS 0,005, 28 långa tasks (13 under scroll), 4 vilande `will-change`, 4 559 kB inbäddat. V3c slår på varje laddningsrad (13 → 1 lång task under scroll, 4 → 0 promoveringar, 4 559 → 48 kB, CLS 0,000) men **förlorar på klockan**: V3b p95 50,0 ms / 71 rutor, V3c 100,1 ms / 196 över samma drag. Helt och hållet de två posterna ovan.
- **oryzo-ai, dope-security, mattis-studio, monologue, planhat, insign, highwaymedia, hoy**: kan inte öppnas som byggen; katalogposterna och fas A-skivorna är stillbilder. Ingen prestandarad kan hämtas ur dem.

## material_fixes

1. **`index.html:1377–1385`: söv ramarna i stället för att avmontera observern.** Behåll observern (inte `obs.unobserve(f)`, rad 1381) och sätt `content-visibility: hidden` på `.calyx-wrap`/`.horai-wrap` när ramen är mer än en viewport bort. Mätt: task 13 164 → 4 516 ms, layout 2 374 → 117 ms, frame p95 890 → 66,7 ms. Mål: layout under scroll ≤ 130 ms, task ≤ 5 500 ms, `long-task-under-scroll` 1 → 0. `content-visibility` är varken `transform` eller `opacity`, så ledgerns M1-regel står.
2. **`index.html:1384`: flytta monteringen ut ur signaturakten.** `rootMargin: '100% 0px'` utlöser vid scrollY ≈ 2 560, 500 px inne i vändningen; p95 genom heron 435,9 ms med ramarna, 66,7 ms utan. Mål: `rootMargin: '40% 0px'` så monteringen sker vid heronts `--sc-ps` ≥ 1,0 (scrollY ≥ 3 100), p95 genom heron ≤ 70 ms.
3. **`index.html:1137–1221` + `:788–821`: håll banorna utanför stilträdet tills deras fönster öppnat.** `content-visibility: hidden` på varje ritgrupp vars `--p-l`-fönster inte börjat, växlad av `data`-attribut som `readState` (`:1337–1344`) sätter vid stegets gräns; sju skrivningar totalt. Mätt tak: recalc 4 741 → 3 080 ms, rutor 102 → 66. Mål: recalc ≤ 3 400 ms, rutor > 33 ms i 75-tickskörningen 196 → ≤ 60.
4. **`index.html:788–821`: vidga varje banas fönster.** 0,03–0,045 ger max_step 25,3 %/31,0 % och staircase 1 vid 100:60. Mål: fönsterbredd ≥ 0,075 av `--sc-ps`, max_step ≤ 12 % och staircase 0 vid 100:60, med "ingen bana ritas samtidigt som en annan" bevarad genom färre banor per steg.
5. **`index.html:617`: ankra trådens fönster i liggaren.** `--scrub` 0,15–0,60 → **0,62–0,95**, så att scaleY 0 → 1 löper medan `#projekt`s överkant är mellan +600 och +90 px (mätt: 0,62 ↔ scrollY 3 160, 0,95 ↔ 3 680).
6. **`index.html:1168`: `assets/demo-calyx-1440.webp` är 206 966 B, renderas 538×303.** 36 % av sidans vikt, under vecket, `<image>` i SVG har ingen `loading="lazy"`. Mål: omkoda till 1076×606 → ≤ 60 000 B, sidvikt 573 → ≤ 425 kB, och sätt `href` i den IO-montering som finns. Riktad till lead (F-009).
7. **`index.html:825`: ta bort `will-change: stroke-dashoffset`.** Inte kompositerbar; mätt recalc 4 741 → 4 529 och task 6 070 → 5 922, inom spridning ±15 %. Mål: raden borta, p95 oförändrad inom 2 %.

## keep

`--sc-ps`-kontraktet och dämpningen: staircase 0 på varje gated spår i varje körning, båda kadenserna, båda riktningarna, cpu 1 och 4; max_step på `--sc-ps` 0,20–1,73 % mot taket 3 %. Rör inte det när bildtiden fixas: aldrig tillbaka till rå `--sc-p`, aldrig `--flip` eller banorna i en JS-skrivning per bildruta, aldrig kapad lerp. Behåll `.ground`s `contain: strict` (`:235`) med dess filter (`:245`): 111 ms av 13 164, inom brus.

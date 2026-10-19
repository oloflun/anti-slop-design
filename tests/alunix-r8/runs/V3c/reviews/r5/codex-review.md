fix

## persistence

Codex ran on the second attempt: `codex exec -m gpt-6-astra -c model_reasoning_effort="medium"`, CLI 0.154.0, all 20 PNGs attached, ~6 min, exit 0. (First attempt, CLI 0.148.0, died on "The 'gpt-6-astra' model requires a newer version of Codex"; every fallback model was blocked for this ChatGPT account, so that pass produced nothing; see `codex-review-pass1-no-codex.md`. Transcripts in the session scratchpad: `codex-out2.txt`, prompt in `codex-prompt.txt`.)

Codex returned **12 numbered findings plus 6 gate conclusions**. **12 survived verification, 0 dropped.** Every cited line in `tests/alunix-r8/runs/V3c/index.html` and every cited region in the named PNG was checked, and each piece of arithmetic re-derived against the engine's own flow formula (`scroll/scrollcraft.js:37`).

Two corrections applied during verification, both against the wrapper's own first pass, not against Codex:
- **Clipping magnitude.** The first-pass number (141 px cut at 1280) was wrong: the overflow eats the 80 px right padding first, so the visible cut is **60,8 px at 1280**, 301 px at 1024, 418 px at 900. Codex's arithmetic is the correct one and was adopted.
- **Finding 6's wording.** Codex's "emphasize the measurement assigned to the current screen" is one step from a styling opinion, so it was re-anchored to the two lines that actually demand it (plan 010's s-process-06 row, "byter till `--hair-ink`", and H-33).

Six findings are **Codex's alone** and were not in the wrapper's own pass: the step-text crossfade that overprints two texts (#8), the `7 rem` callout that is not a true measurement (#5), the measure numbers that never demote to `--hair-ink` (#1), both iframe reveals silently never registering (#2), `?preview=back` losing its accessible state on the next frame (#2), and the second half of the A-glyph cause (the `.75px` stroke scaled to ~0,024 px by the `<use>` transform, #6). The recorded `motion_probe` numbers in `NOTES.md:1440-1443` were verified only after Codex pointed at them. Codex violated none of the invariants: no reduced-motion suggestion (F-011 respected), no engine edit proposed, no `--sc-p` inversion, no re-direction of the aesthetic.

## fidelity

Mekaniskt är akten byggd som `BRIEF.md` och plan 010 beskriver den: `#process` mellan `.stagger` och `footer.close` (`index.html:1079`), `data-sc-act="flow"`, 300 svh, sticky-ark, sju `<li>` med egna fönster, sju `?preview=process-0N`, allt rörligt ur `--sc-ps`, noll rå `--sc-p` (H-28 uppfylld). Fönstertalen och 390-formen är det som inte håller.

1440 (`proc-1440-01..07.png`):
- **s-process-01** avviker: A-glyfen saknas helt, arkets övre vänstra hörn. Två orsaker, båda verifierade (fix 6). Skärmen är en tom kontur utan displayelement.
- **s-process-02** avviker: radens sanna mått **320 · 768 · 1440 syns inte** (under arket); stationsstrecken saknas, måttlinjen halvritad.
- **s-process-03** avviker: bär s2:s siffror; egna utropen `7 rem` och `16:9` saknas.
- **s-process-04** avviker: `96 px` och den lodräta måttlinjen saknas; bär s3:s utrop.
- **s-process-05** matchar geometriskt (Calyx halvfylld, filter på 538x303), men de 44 px blå siffrorna är fortfarande skärmens tyngsta element, inte den fyllda öppningen.
- **s-process-06** avviker: siffrorna faller som de ska men **byter aldrig till `--hair-ink`**; de står blå i `proc-1440-06` och `-07`.
- **s-process-07** avviker: arket klippt 135 px upptill, footern äger nedre 540 px; revisionsfältets skraffering permanent nedtonad till 0,35.

390 (`proc-390-01..07.png`): **alla sju avviker**. Texten ligger över arket i stället för under det, alla sju steg syns samtidigt i full opacitet, arket är inte sticky och kommer in i vy först vid ps ≈ 0,52, alltså **färdigritat** (`proc-390-05.png`). Planschens geometri är rätt; kadensen och ordningen är inte byggda. Räknar leaden de raderna som mekanisk icke-leverans tippar dispositionen till `recapture`; wrappern stannar på `fix` eftersom varje rad är en avgränsad ändring i ett `@media`-block.

Device-tabellen: rad 1 till 8 lever och läser `--sc-ps`. **Utanför akten är två deklarerade devices döda**: båda ramfigurernas `data-sc-reveal` (fix 2), alltså två DEAD-rader mot H-24. H-32/H-21 är FAIL på inspelade tal (`NOTES.md:1440-1443`): p95 **116,7 ms / 190 rutor > 33 ms** vid 100:60 och **50,0 ms / 1163 rutor** vid 20:120, med ren kontroll (16,7 ms / 0) omedelbart före, och **staircase 1 på `#p-opening`**. Baren är p95 ≤ 20 och noll rutor.

Gates: 47/79 ren (varje bana namnbar; Calyx är en tillåten riktig produktyta). 88 ren. 75 ren i synlig text (två träffar, `:343` och `:1457`, båda i kommentarer). H-29 ren i anda (12 banor, alla dash-ritade normaliserade); sju element saknar `pathLength="1"` (`:1150, 1157, 1182, 1187, 1204, 1206, 1219`) men ritas med clip-path. H-31 ren på desktop, faller på 390.

## ceiling

- **Motorn (`scroll/scrollcraft.js:392`)** letar reveal-mål bland en akts **efterkommande**, aldrig på aktelementet självt. Sidans egen markup hänger `data-sc-act` och `data-sc-reveal` på samma `<figure>` (`:988-989`, `:1063-1064`), så motorns reveal-kontrakt är uppfyllt men sidans användning av det är det inte.
- **Motorn + shimen ger en monoton, stegfri progress** över hela `height + vh`. Akten använder bara 0,19 till 0,81 av det livet, och de sju fönstren inuti missar tre av sju sanna mått med exakt ett fönster.
- **K3 (`board/cells/K3-r8/index.html`)** håller varje utrop uppe **inom** den skärm måttet hör till, och dess mobila plansch är sticky med texten under. V3c lånade K3:s teknik korrekt men inte kadensen och inte den mobila formen. K3:s p95 218 ms är ett underkänt tal, inte ett tak; V3c:s 116,7 ms underskrider K3 och missar ändå baren med en faktor 5,8.
- **Sidans egen `.plate-card` (`:361-372`)** räknar hela sitt uttryck i ren CSS utan hårdkodad viewporthöjd. Processens scen skriver in 900 px viewport som konstant (`top:202px; height:495px`, `:691`).
- **`NOTES.md:1444-1447` namnger rotorsaken själv**: `--sc-ps` är `inherits:true` och skrivs per bildruta, så 12 banor + 7 `<li>` + 5 siffror tvingar en stilomräkning av hela underträdet varje ruta. Samma fel R4:s plan 005 mätte, nu med fler prenumeranter.
- **`.stagger` (`:484`)** ger 21,6 px slitsar av rå grund mellan panelerna vid 900 px höjd (`s1440-05.png`), och `:486-489` lägger högerspalten först vid ≤900 px. H-05 och H-14 står kvar oberoende av akten.

## material_fixes

1. **`index.html:802, :807, :808, :817` + `:753-760`.** Varje skärms sanna mått tänds ett fönster för sent, och faller aldrig i ton. Mål: varje `--p-t` är 1 vid sitt stegs mitt (siffrorna 0,30-0,32, `7 rem` 0,395-0,41, `16:9` 0,40-0,415, `96 px` 0,48-0,50), banfönstren (`:799-816`) komprimeras så att banan är färdig före sitt utrop; `.measure{fill}` byter till `--hair-ink` i steg 06: `fill:color-mix(in srgb, var(--c-accent), var(--hair-ink) calc(100% * var(--p-fall)))` eller motsvarande, så att det blå momentet är **ett per skärm** (H-33).
2. **`index.html:988-989` och `:1063-1064`.** Båda ramarnas reveal registreras aldrig: `data-sc-reveal` sitter på samma element som `data-sc-act`, motorn söker bara efterkommande (`scroll/scrollcraft.js:392`). Två rader i device-tabellen DEAD (H-24). Mål: flytta `data-sc-reveal`/`data-sc-reveal-at` till `.frame-wrap` inuti varje figur; motorn rörs inte. Samma runda: `?preview=back` sätter baksidan nåbar på `:1440`, men `readState` (`:1349`) kör `setFace(false)` i nästa bildruta vid scrollY 0, så "Boka ett möte" i `p1440-back.png` är `inert` medan den syns. Mål: previewläget auktoritativt (flagga som `readState` respekterar).
3. **`index.html:835-841`.** 390-målbilden är inte byggd. Mål: (a) `.process-sheet{order:-1}` så att texten hamnar under arket; (b) ta bort `opacity:1 !important`, behåll fönsteruttrycket med mobila fönster 01 0,17-0,26 … 07 0,71-0,83; (c) arket `position:sticky; top:12svh`. Sektionen 320 svh enligt planen.
4. **`index.html:1474` + `:821` + `:783`.** Skärm 07 står utanför sticky-hållet (släpper vid ps 0,806; `PROCESS_MID['07']` 0,90). Mål: `'07': 0.785`, `#p-c-rev`-fönstret 0,77. `.process-sheet .guide,.process-sheet .hatch{opacity:…}` träffar även `#p-rev`; mål: selektorn snävas till `#p-guides, #p-ledgers, #p-hatch`.
5. **`index.html:1196` + `:1198`. `7 rem` är inte ett sant mått.** Måttlinjen spänner x 226 till 270 = 44 units; arkets skala är 880 units = 1440 px, alltså 72 px = **4,5 rem**. H-33 tål inte ett falskt tal. Mål: `d="M201.6 80 H270"` (68,44 units = 112 px = 7 rem) med utropet centrerat, eller utropet ändrat till det mått linjen visar. Felet kommer ur plan 010 § Målbild rad s-process-03; planen behöver samma rättelse.
6. **`index.html:931` + `:1176` + `:794-796`.** A-glyfen är osynlig av två skäl: `fill="#ffffff"` som presentationsattribut slår ärvd `fill:none`, och den ärvda `.75px`-stroken skalas av `scale(0.031607)` till ~0,024 px. Mål: en egen `<path>` i arket (eller `fill="currentColor"` på originalet plus `stroke-width:23.7` i `<use>`:ns units) som `--contour-hair`-kontur. `:796`: fönstret börjar exakt på 0,235 = `PROCESS_MID['01']`; mål 0,205 till 0,225.
7. **`index.html:691, :695, :720`.** Arket klipps bort mellan 900 och ~1404 px bredd: **60,8 px** vid 1280 (inklusive `1440`-siffran), 301 px vid 1024, 418 px vid 900; `overflow-x:clip` döljer spillet. Mål: `width:min(880px, 100% - 384px - 140px); height:auto; aspect-ratio:880/495`, eller planschbrytpunkten till 1400 px. `top:202px` är 1440x900 som konstant; mål `top:max(24px, calc((100svh - 495px) / 2))`. Dödkod: `stroke-width` på `:723` överskrivs av `:782`.
8. **`index.html:712-716`.** Två stegtexter överlappar i samma box vid varje fönstergräns (ps 0,29: steg 01 och 02 båda opacitet 0,5; samma vid 0,38, 0,47, 0,56, 0,65, 0,74). Mål: ut-klampen slutar där in-klampen börjar (ut 0,275-0,285, in 0,285-0,295 och så vidare), noll rutor med två läsbara rubriker ovanpå varandra.

## keep

- `--sc-ps` genomgående i akten; rå `--sc-p` bara i två kommentarer; ingen JS-stil per bildruta; `readState` (`:1324-1349`) rAF-skyddad med deadband, återanvänder heron befintliga läsare.
- `will-change` bara via klass (`.process.is-drawing .draw`, `:825`).
- Höjdmekaniken ren CSS: `min-height:300svh` + `position:sticky`.
- Ritmekaniken är K3:s, korrekt kopierad: `pathLength="1"`, `*1px`, `transform-box:fill-box`, snäpp-opaciteten på pilspetsarna (`:740-747`), `markerUnits="userSpaceOnUse"` med `fill="context-stroke"`.
- De fem `@property`-raderna (`:187-191`) och det utskrivna `clamp()`-uttrycket där `inherits:false` bryter kedjan (`:766-777`).
- `proc-1440-05` och `-06` är målbildens skärmar 05 och 06 (bortsett från tonbytet).
- `<image>` med `width`/`height` (`:1168`), filtret på 538x303, ingen tredje iframe, båda ramarna `loading="lazy"` + `data-src` + IntersectionObserver.
- Tillgänglighet: `role="img"` med `<title>`/`<desc>`, stegen som `<ol>`/`<li>`, `--hair-ink` 4,89:1 och `.process-a` 8,75:1 mot papperet.
- `96 px` är sant (58,7 units × 1440/880 = 96,06 px) och `16:9` exakt (538x303). Bara `7 rem` faller ur.

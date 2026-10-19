fix

## persistence

Läst denna körning, i ordning: `~/.agents/skills/design/references/house-physics.md`, `production-tells.md` (66–88, 97–98), `gates.md` (58–98). Projektets standard: lane-mening finns (`BRIEF.md` § Design Read, "lågexponerad gråskalescen i registret cinematic dark ... ett enda visitkort ... vänds medan besökaren scrollar"), reference-lock finns (`BRIEF.md` § Reference lock, 7 fält + catalogue-select-raden + arkitektens Fas A-rad för insign/highwaymedia/hoy). Målbild för akten: `plans/010-process.md` § Målbild skärm för skärm (1440 och 390) och `plans/011-*.md` § Target, båda lästa i sin helhet. Golvet: `HELHET.md` § 3 H-01…H-35, läst. `BRIEF.md` båda halvorna lästa. `NOTES.md` § R5 + leadens pixelläsning lästa.

Pixlar lästa denna körning: `shots/r5-lead/proc-1440-01..07.png`, `proc-390-03.png`, `proc-390-06.png`, `p1440-mid.png`, `p1440-back.png`; `shots/r5/frames-process-02.png`, `-04.png`, `-09.png`, `-10.png`, `preview-process-07-1440.png`. Källa lästa rader: `index.html:676-855` (processblocket), `:1075-1131` (markup), `:361-375` (flip). Referenspixlar denna körning: `design-catalogue/entries/highwaymedia/fold.webp`, `hoy/fold.webp`, `insign/fold.webp`.

Inte läst som pixlar denna körning, redovisat i stället för dolt: `oryzo-ai`, `mattis-studio`, `dope-security`, `monologue`, `planhat` — deras verdict nedan vilar på `BRIEF.md` § Lästa referenser (fil-för-fil-digesten, gör/tar/lämnar) och `HELHET.md` § 1, inte på egna pixlar. Saknas på disk: någon `scroll_verify`-utdata från R5 (bara `shots/fasA/probe/`), vilket är varför H-17/H-18 inte kan bockas; se `material_fixes` 8. Ingen av bristerna hindrar domen i min domän.

## fidelity

Mot `plans/010-process.md` § Målbild, skärm för skärm vid 1440. Topologi (papper i full bredd, vänsterspalt 86–470 med index/titel/fråga/svar, ark 880×495 sticky x 480–1360) stämmer på alla sju. Läsordning vänster→höger stämmer. Överlapp/z-ordning: inga, rätt. Densitet: ett displayelement per skärm håller i 01–04 och 07, inte i 05–06 (nedan).

| Skärm | Drift | Avsiktlig / defekt |
|---|---|---|
| 01 | Kontur dragen, ark tomt. `#p-mark` (A-glyfen, 36 units) är 0 % vid fönstrets mitt 0,235 — målbilden ger den till 01 | defekt, lätt (ligger inuti fix 3:s fönsterförskjutning) |
| 02 | Måttkedjan **320 · 768 · 1440** syns inte (`--p-t` start 0,35, mitt 0,325). Skärmen har därmed varken sitt sanna mått eller sitt blå moment. H-33, H-30 | defekt |
| 03 | `7 rem` och `16:9` syns inte (start 0,43 resp. 0,46, mitt 0,415). Målbilden ger båda till 03 | defekt |
| 04 | `96 px` syns inte (start 0,55, mitt 0,505). Målbilden ger det till 04 | defekt |
| 05 | Calyx halvfylld, gråskala, rätt. Men de tre 44 px accent-siffrorna är fortfarande skärmens tyngsta märke när bilden landar; `--p-fall` börjar först 0,64. TASTE § 4.8 (i akten är den sak som rör sig auktoriteten), H-08 | drift, kräver arkitektrad om värdet ska flyttas (planen låser 0,64) |
| 06 | Siffrorna faller i storlek men förblir `--c-accent`; målbildens rad 6 säger byte till `--hair-ink` | defekt, lätt |
| 07 | **Blockerande.** Akten sista tillstånd hålls aldrig i helbild: `#p-c-rev` (`A`) börjar ps 0,81, `.process-stage` släpper sticky vid ps 0,806 (`min-height:300svh` − 495 − 202 → scrollY = top+2003, liv 3600). I `frames-process-09/10.png` och `proc-1440-07.png` är arket kapat vid y 340 och fotern äger nedre 560 px. Två akter i samma viewport | defekt |
| Ingång, ps ≈ 0,14–0,19 | `frames-process-02.png` är en hel viewport krämvitt papper med enbart 11 px-kickern och en 25,6 px h2 i övre kanten. Ingen författad tystnad i `BRIEF.md` § Den författade tystnaden täcker `#process` | defekt |

390, mot `plans/010-process.md` § Målbild 390 ("texten ligger **under** arket i flödet, en stegtext i taget, cued på samma fönster; arket sticky `top: 12svh`"): **materiell avvikelse.** `index.html:836-841` gör stagen `position:static`, `opacity:1 !important` på varje `<li>`, och `<ol>` ligger kvar före `<svg>`. Utfall i `proc-390-03.png`: sju likadana textblock i rad, inget ark i bild; i `proc-390-06.png` kommer arket först efter alla sju. Akten degraderas till en punktlista plus en färdigritad bild på exakt den enhet där Stress-personan ska bestämma sig på fem minuter. Byggarens skäl (tomma luckor vid fönstrad opacity i flöde) är korrekt observerat men löser fel problem: planens form är sticky ark + text som passerar under det, vilket inte lämnar luckor. F-007: avvikelse från signaturaktens målbild är blockerande, inte kosmetisk.

Gate-genomgång, det som fires och det som inte gör det: gate 47/79 **rent** — arket bär bara kontur, måttlinje, hjälplinje, skraffering, ledare, utrop; ingen browserram, ingen fabricerad UI, Calyx är en riktig skärmbild av byråns egen sajt maskad i öppningen, inte en tredje live-ram. Gate 78 **rent** — hårlinjerna organiserar sanna mått, de är inte dekor. Gate 69/72 **waived med rad**: `01`–`07` i mono är licensierade av `HELHET.md` § 4 T-7 och speglar liggarens egna 01–03; titlarna är Uppstart/Planering/…/Förvaltning, aldrig "Steg 1". Gate 75 **rent** (0 träffar, verifierat i NOTES § R5 punkt 7). Gate 97 **rent** — `Boka ett möte` står utan pil i `p1440-back.png`. Gate 92 **rent** — radie 0 genomgående. Gate 48/60 **rent** i de nya raderna. Gate 94 punkt 1 **rent** — allt som förflyttar sig läser `--sc-ps`, inklusive utropens opacitet. Gate 94 punkt 2 **fail**, se fix 7.

Utanför R5:s uppdrag, noterat utan fix: `p1440-mid.png` visar fortfarande en hårlinje i ett 896 px brett tomrum (H-10 saknar plan) och `p1440-back.png` visar kortets högra halva tom (H-09, T-4/plan 016).

## ceiling

- **V3b-chain (primary, Tier 0)** — `slår`. V3b har ingen processakt och två anatomier efter heron; V3c har nu en fjärde anatomi som svarar på beställarens egna frågor i klartext. Läst som text (`HELHET.md` § 2), inte som egna pixlar denna körning.
- **insign** — `slår`. Insigns fold är en servicemall med nivåkort och kryssrader; löftena (testadress, redigerbart CMS) står i klartext men i kortform. V3c säger samma sak som fråga och svar utan ett enda kort. Pixlar lästa (`fold.webp`).
- **highwaymedia** — `står sig bredvid`. Highways lodräta tidslinje har en början och ett slut man ser på en gång; V3c:s ark är bättre material men dess sista fas landar aldrig hel (fix 1), och vid 390 läser Highways tidslinje fortfarande som en sekvens medan V3c:s läser som en lista. Pixlar lästa (`fold.webp`).
- **hoy** — `förlorar`. Hoy ger varje kapitel en egen skärm med ett helbrett hårt grundbyte och en kapitelrubrik på 100–132 px som utan tvekan äger skärmen. V3c:s akt äger sin viewport i 01–06 men delar den med fotern i 07, och dess egen `h2` på 25,6 px är mindre än stegrubrikerna den ska ranka över. Pixlar lästa (`fold.webp`).
- **mattis-studio (lånad som avvisning)** — `slår`. Konsolvokabulären är fortfarande borta: ingen versionstagg, ingen klocka, inga hörnmarkeringar, ingen slot-räknare. Arket är en ritning, inte en ritad ram. Digest, inte egna pixlar.
- **oryzo-ai** — `står sig bredvid`. Lärdomen (materialet och kanten under snedljus bär rotationen) bor i heron och rörs inte av R5. Oryzos fold gör ändå en sak akten inte gör: där är den tomma skärmen ägd av ett objekt, medan `frames-process-02.png` är tom utan att något äger den. Digest, inte egna pixlar.
- **dope-security** — `står sig bredvid`. Accentfrekvensen är fortfarande ett tal (tre roller, utskrivna) och arket bär noll `box-shadow`. Men dopes "rader i registergrad" håller ihop som ett system vid liten grad, vilket V3c:s sju vänsterspaltsblock inte gör vid 390 där de staplas till en odifferentierad lista. Digest, inte egna pixlar.
- **monologue** — `slår`. Monologues 49 skuggor, tre feature-kort och prisbadge är precis formerna den här akten undviker: ett ark i sju tillstånd, inte sju kort. Digest, inte egna pixlar.
- **planhat** — `förlorar`. Planhat ransonerar fotografiet till exakt ett och låter typen vika helt för det; i `proc-1440-05.png` står de tre 44 px accent-siffrorna kvar i full vikt medan Calyx fylls, så fotografiet är inte auktoriteten när det anländer. Digest + den här sidans pixlar.

## material_fixes

1. `index.html:819-821` + `:1128` — steg 07:s sista beat faller efter sticky-släppet vid ps 0,806. Flytta `#p-title` 0,73 → **0,70**, `#p-rev` 0,77 → **0,74**, `#p-c-rev` 0,81 → **0,78** och `li[data-step="07"] --step-start` 0,73 → **0,70**, så utropet `A` är klart vid ps 0,80. Höj inte `min-height` i stället: 453svh krävs och bryter H-01.
2. `index.html:836-841` — 390 följer inte målbilden. `.process-sheet{position:sticky;top:12svh;order:-1}`, `.process-steps{order:1}`, behåll `opacity:1`; arket ska stå kvar i bild medan de sju texterna passerar under det (`proc-390-03.png`, `-06.png`).
3. `index.html:802, 807, 808, 812, 817` — varje utrop landar ett steg för sent. `#p-m320/768/1440` 0,35 → **0,305**; `#p-c-gutter` 0,43 → **0,395**; `#p-c-169`/`#p-dot-169` 0,46 → **0,425**; `#p-c-row` 0,55 → **0,50**. Då bär skärm 02, 03 och 04 sitt sanna mått vid sin egen fönstermitt (H-33, H-30).
4. `index.html:686-689` — sektionsrubriken rankas under sina egna steg (25,6 px mot stegtitlarnas 32 px vid 1440). `.process-title` font-size → **`clamp(2.2rem,3.4vw,3rem)`** (48 px vid 1440, 3× brödtext). House physics, § Structural: hierarki genom skala.
5. `index.html:788` + `:1086` — en hel tom viewport vid aktens ingång (`frames-process-02.png`). `#p-outline` fönster 0,19 → **0,12** (0,12–0,165) och `li[data-step="01"] --step-start` 0,19 → **0,15**, så konturen ritas medan kicker och rubrik fortfarande står i bild. H-08, H-15.
6. `index.html:753-754` — måttsiffrorna behåller `--c-accent` efter fallet. `fill` ska interpolera till **`var(--hair-ink)`** över det befintliga fönstret 0,64 → 0,73 (målbildens rad s-process-06).
7. `index.html:683-825` (hela akten) — bildtid: p95 **116,7 ms** / 190 rutor > 33 ms vid 100:60 och 1 163 rutor > 33 ms vid 20:120, cpu 4. Målvärde H-21/gate 94: **p95 ≤ 20 ms, 0 rutor > 33 ms**, med kontrollen ren omedelbart före. `contain` är omprövad och verkningslös; nästa lever är att minska antalet `--sc-ps`-läsande efterkommande (12 banor + 7 `<li>` + 5 siffror). Primärt design-perf-reviewerns lane, tas med här för att gate 94 inte får passera tyst.
8. Ingen R5-`scroll_verify` finns på disk och heron-spåret kördes inte om. Kör `scroll_verify.py` vid 1440×900 och 390×844 och bocka **H-17 (statisk svans ≤ 700 px, beräknat 655)** och **H-18 (vändning 1 300–1 600 px, beräknat 1 469)**; plan 011 § Done when är inte stängd förrän det talet finns.

## keep

Arkets disciplin rörs inte medan ovanstående fixas: 12 banor under 60-taket, varje märke namnbart som kontur, måttlinje, hjälplinje, skraffering, ledare eller utrop (gate 47/79 rent), Calyx maskad som bild och aldrig en tredje live-ram, vänsterspaltens 153 px stagger mot arkets överkant (H-04), radie 0, noll skugga, noll tankstreck och `Boka ett möte` utan pil.

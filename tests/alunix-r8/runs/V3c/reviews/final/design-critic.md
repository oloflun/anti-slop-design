fix

*(Exit-granskning av slutläget, `design-critic`, 2026-09-17. Sparad av lead ordagrant ur agentens rapport.)*

## persistence

Read this run, all of it against the live page at `http://localhost:3090/tests/alunix-r8/runs/V3c/index.html` (HTTP 200, 141 976 B, md5 `ee0999d4`, byte-identical to `board/cells/V3c-r8/index.html`):

| Input | Status |
|---|---|
| `~/.agents/skills/design/references/house-physics.md`, `production-tells.md` (66–88, 97–98), `gates.md` (58–96) | read in full |
| Target image `tests/alunix-r8/malbilder/V3c.md` (planens § 7.5, bindande) | read in full |
| `runs/V3c/BRIEF.md` § reference lock, dial-deklaration, decision ledger R1–R6 + Fas A | read |
| `HELHET.md` § 3, alla 35 H-rader med status | read; 29 `[x]`, 6 öppna (H-02/H-03/H-08 = Q30, Antons; H-21/H-22/H-32 = redovisat bildtidsgolv) |
| `NOTES.md` § R12 + `## Leadens avslutning`, `COPY-GATE.md`, `PROCESS-UNDERLAG.md` §§ 1–2, `reviews/loop-5-astra.md` | read |
| `shots/r12/papper/page--s00..s09`, `preview-1440-process-05/06/07`, 12 `frames/` | read as pixels; alla daterade efter sista redigeringen (22:49 → 22:55–23:22) |
| `shots/r12/invert/` (s00–s09, previews, frames), `shots/final-widths/` 320/375/414/768 | read as pixels, 23:30 |
| Låsta referensers folds: `oryzo-ai`, `dope-security`, `mattis-studio`, `monologue`, `planhat`, `insign`, `highwaymedia`, `hoy`, + primärkällan V3b (`desktop-1440--fold.png`) | read as pixels |

Two gaps, named rather than smoothed over. **(1)** `shots/r12/` covers ten slices; the last ~1 600 px of the 10 534 px document (avsnittet `Hur vi tänker` och `footer.close`) was not re-captured this round. I read them in `shots/loop-5/slices-1440/v3c-1440--s10/--s11.png` (20:34, 2 h 15 min före sista redigeringen) and verified by grep that R12:s två `Edit`-anrop är scopade till `#process`-SVG:ns `.p-live` och kan inte nå dem. Judgment is not suspended on that basis. **(2)** `scroll_verify.py` kunde inte köras i R12 (fyra försök, protokollfel); `blankBands` och opacitetskontrollen över hela sidan är därför omätta denna runda — redovisat ärligt i NOTES § 2.6, inte tigit ihjäl. Jag körde egna Playwright-mätningar vid 900 och 1024 för att täcka det band ingen skärmbild i uppdraget täcker.

## fidelity

Mot målbilden, skärm för skärm vid 1440 (papper), sedan 320/375/414/768 och 900/1024.

**s00–s02, signaturakten.** Topologi, läsordning, fokusskala och z-ordning matchar målbilden exakt: rubrik i affischgrad utanför plåten (115,2 px uppmätt), kortet 896 px brett vänsteranknutet vid `--rail-x` 86, underraden nere till höger med sin högerkant på 1354 mot toppradens 1358 (optiskt samma rail, inte en miss). Vändningen genom tolv ramar (`shots/loop-5/flip-1440/`) är kontinuerlig, läser som ett fysiskt kort vänt med handen, och vid 0,45–0,55 står bara en kant kvar — `mattis-studio`-avvisningen är infriad i pixlar, inte i prosa. Baksidan bär ordmärket, kickern `DIGITAL BYRÅ`, hårlinjen, tjänsteraden och `Boka ett möte` med A-glyfen som kontur i höger halva. **Ingen avvikelse från signaturakten. F-007 är uppfylld.**

**Två avsiktliga avvikelser från målbildens bokstav, båda med ledgerrad och båda rätt:** (a) målbilden föreskriver `Boka ett möte →`; byggd utan pil — gate 97 slår en ordagrann sträng; (b) målbilden säger understrykning i accent; byggd i `currentColor` — `#1e5e9c` mot `#0b0c0e` mäter 2,92:1, under WCAG 1.4.11:s 3:1. Båda är klassade som defekter i målbilden, inte i bygget.

**s03–s05, bandet.** Vänster blå tes med Hyperborea-bleed → Calyx → pris; höger jätterubrik + liggare → Hōrai. Exakt målbildens kolumnfördelning. Ingen slits av rå grund i skarven (mätt vid y 700: plåten 7,7,7 fram till x 740, papper 253,251,244 från 750). **s03 är sidans enda skärm med två likvärdiga auktoriteter** — det är H-02/H-03/H-08, Q30, arkitektens eskalering till Anton, och jag räknar det som öppen fråga, inte som fynd.

**s06–s09, processakten.** Ritningen ritar form och aldrig innehåll: varje bana är kontur, måttlinje, hjälplinje, skraffering, ledare eller utrop, och det enda innehållet i öppningen är en verklig skärmbild av byråns egen Calyx — gate 47 och gate 79 båda rena. Färgen anländer i steg 06 och står i 07 medan måtten drar sig tillbaka till `--hair-ink`; tolv ramar bekräftar att övergången är monoton. Blått är ett sant mått per skärm och ingenting annat. `?process=invert` håller samma geometri med accenten lyft till `#3286d8` och bilden dämpad till `brightness(0.6)` — läser som en bild i ett mörkt rum, inte som en lampa.

**s10–s11.** Principerna som hårlinjeliggare i vänster halva med höger halva tom där arket stod: den tomheten läser som att ritningen är avslutad, inte som en obemannad spalt, och den upplöses av avslutet — `kontakt@alunix.se` typsatt i displaygrad över fotot med en hårlinje som dras in. Husets regel (CTA är en typsatt mailto, aldrig en knapp) i sin renaste form på hela sidan.

**Defekt, blockerande, 768 till 1279 px.** I planschläget (`@media (max-width:1279px)`) är `.process-stick` `position:sticky; top:0; z-index:2` med ogenomskinlig `background:var(--bg)` och `width:min(100%,480px,…)`, `justify-self:center`, medan `.process-steps` tar full spaltbredd. Under ~640 px sammanfaller de och texten passerar snyggt under arket; över det är arket smalare än textblocket och stycket klipps mitt i ordet. Uppmätt av mig denna runda: **768 → steg 01 överlappas 480 × 413 px** (rubriken renderar `UPPSTAR`, brödtexten klipps vid x 145); **900 → steg 01 480 × 379 px, steg 02 480 × 185 px**; **1024 → steg 02 480 × 255 px, steg 03 480 × 309 px** (hela stycket sväljs, bara `inte sett.` kommer ut under arket). Detta är den enda materiella defekten jag hittar, och den träffar just de bredder sidans egen copy lovar att verifiera (`320, 768 och 1440. Varje sida verifieras vid alla tre.`). Leads exit-läsning har redan mätt samma sak och skrivit `PROMPT-R13-V3c-fix768.md`; jag bekräftar den oberoende.

**Produktionstell, redovisad utan fix.** Kortets `DESIGN UTVECKLING SYSTEM` i mono-versaler är formmässigt gate 68:s `DESIGN · BUILD · SHIP`-remsa och sitter i nedre tredjedelen av folden. Den är ordagrant föreskriven av målbilden och är äkta innehåll på ett visitkort som depikteras, alltså brief-övertrumfad enligt `gates.md` § Waiving a gate — men **waiverraden är aldrig skriven**. Det är pappersarbete, inte en pixel; jag lägger den inte bland fixarna eftersom den saknar målvärde.

**Gatevandring, allt annat rent.** Gate 75: noll tankstreck i synlig text (enda träffen ligger i en CSS-kommentar). Gate 97: noll pilar i länk- eller knapptext. Gate 98: `color-scheme` och `theme-color` deklarerade. Gate 92: en radievokabulär, radie 0 överallt plus Hōrais cirkulära iris som maskform. Gate 73: noll mittprickar i synlig text. Gate 88: ingen scroll-cue; grund-kontraktet bär den. Gates 66/67/74/76/77/80/81/83/85/87: noll. Gate 86: liggarna bär `border-top` på gruppen och hårlinje mellan raderna, vilket är husets egen liggaranatomi och inte tio rader `divide-y`. Gate 69: 01–03 och 01–07 är liggarnumreringar som `house-physics` uttryckligen licensierar, inte numrerade eyebrows. Gate 91: `#1e5e9c` står i exakt tre utskrivna roller. F-011: noll träffar på `prefers-reduced-motion`. Låst copy 15/15 orörd.

**Talavvikelse i ledgern.** Rad R1 rättelse 3 anger hero 7,5rem = 120 px och kvot 0,67. Renderat vid 1440 binder mellantermen 8vw: **115,2 px, kvot 80,6/115,2 = 0,700**, alltså precis på taket i stället för under det. Inget lås brutet (baksidan 5,04 × brödtext står kvar), men talet i ledgern beskriver inte pixlarna.

## ceiling

- **V3b** (primärkälla, Tier 0) — `slår`. V3b:s plåt är en tavla i full sidbredd; V3c:s är ett föremål med två sidor som ligger i rummet. Det enda V3b gör bättre är att dess plåt visar mer av ljuspölen på en gång, eftersom den är 1 269 px bred mot V3c:s 896 — större, inte bättre.
- **oryzo-ai** — `slår`. Samma lån (ett föremål som vrids i ett mörkt tomrum) utan oryzos scroll-cue, versionsflik och flytande play-badge. Oryzo är fortfarande bättre på ren materialåtergivning: korkens kornighet och skärpeavfall är renderad i 3D och kan svara på varje vinkel, medan V3c:s stillbild måste vara ärlig med en hårlinje vid 90°.
- **dope-security** — `slår`. V3c anger accentens frekvens som ett tal i tre utskrivna roller; dope låter sin accent bli en hel himmel. Dope gör en sak bättre: dess boarding-pass ligger som en verklig produktartefakt redan i folden, medan V3c:s bevis (Calyx, Hōrai, Hyperborea) kommer först efter heron.
- **mattis-studio** — `slår`, och lånet som avvisning är infriat. Mattis folden bär `(EST. 2019 — VERSION 1.0.4)`, lokal tid, `SLOTS FOR APR: 2 LEFT`, hörnmarkeringar och en VD-avatar: gate 66, 80, 81 och 85 i ett enda hopp. Mattis gör en sak bättre: dess filmiska grain ligger genomgående över hela sidan, V3c:s ton ligger bara på grunden.
- **monologue** — `slår`. Monologues mörka grund är välgjord, men folden är en centrerad hero med badge-pill och en fyrikonsrad — TASTE § 5 två gånger. Monologue gör en sak bättre: dess mono-brödtext håller ett stramare register än V3c:s fem etikettfamiljer.
- **planhat** — `slår`. Planhat sätter `→` på båda knapparna (gate 97) och en generisk versaletikett över rubriken; V3c gör ingetdera. Planhat gör en sak bättre, och det är den enda platsen någon referens slår V3c på bildhantverk: dess strimmiga, målade hero är bildmaterial som är gjort för sidan, medan V3c:s grund är en vendorad gråskalestill.
- **insign** — `slår`. Insigns fold är en stockmosaik under en generisk rubrik med en påklistrad tillgänglighetswidget; V3c:s sju stycken säger allt insign säger, i prosa, med tre riktiga exempelsajter som bevis. Insign gör en sak bättre: dess tre nivåer och tolvpunktsförvaltning är skanningsbara som lista, V3c:s samma innehåll måste läsas.
- **highwaymedia** — `slår`, med bred marginal. Deras fold bär stockfoto i rundat kort, en teal-blobb, en rosa chattbubbla med statusprick (gate 74) och en cookiepanel. Highway gör en sak bättre: varje fas inleds med sitt villkor (`när strategin är satt`) och slutar i en namngiven person med telefon, alltså en väg in; V3c:s väg in är en mailto.
- **hoy** — `står sig bredvid`. Överallt utom en plats slår V3c den (hoys fold är teamstockfoto, pill-nav och en `Invert`-toggle i navet). Platsen är bandets entré: hoy ger varje kapitel en egen helbredd med hårda grundbyten, V3c visar tesen och jätterubriken på samma skärm vid s03. Det är H-02/H-03/H-08 och Q30 — Antons beslut, inte ett fynd ur den här granskningen.

## material_fixes

1. `@media (max-width:1279px)`: ge `.process-steps` samma breddyttryck och `justify-self:center` som `.process-stick`. Målvärde: inget par `.process-stick` / `.process-steps li` med både horisontellt och vertikalt överlapp > 4 px vid 640/768/900/1024/1180/1279, mätt vid `--sc-ps` 0,45 / 0,62 / 0,80. Nu: 480 × 413 px (768), 480 × 379 px (900), 480 × 309 px (1024).
2. Samma media query: styckeblockets vänsterkant ≥ arkets vänsterkant och högerkant ≤ arkets högerkant vid varje bredd 640–1279, så att 34ch-måttet passerar helt under arket som det redan gör vid 320 och 414. Nu: stycket börjar på x 44 och klipps på x 145 vid 768.
3. Reducerade planschen (≤ 1279): utropet `16:9` och dess ledare ska stå fritt från `#p-opening`s hörn med ≥ 8 px vid varje bredd 640–1279. Nu skär ledaren genom glyfens `9` vid 1024.
4. Rätta talet i decision ledger R1 rättelse 3, eller talet i CSS:en: `.hero-headline` renderar **115,2 px vid 1440**, inte 120 px, och kvoten mot kortbaksidan är **0,700**, inte 0,67. Antingen höj clampens mellanterm till 8,35vw så att 120 px binder vid 1440, eller skriv om raden till de uppmätta talen.

## keep

Kortvändningen orörd i alla tolv ramar (tyst vid vila, tänds på första scroll, ärlig hårlinje vid 90°, span 3,4 / fönster 0,10–0,78), det kumulativa arket med färgen som anländer i steg 06 medan måtten drar sig tillbaka, det typsatta mailto-avslutet ensamt på fotot, accenten i exakt tre räknade roller, `--sc-ps`-kontraktet på allt som rör sig, och noll pilar, noll tankstreck, noll scroll-cue.

fix

## persistence

**Pass.** Read this run, in full: `tests/alunix-r8/runs/V3c/BRIEF.md` (lines 1–433: catalogue-select, reference lock, decision ledger inkl. arkitektens fas A-rader och byggarens R5-rader, direction contract, persona-skisser, motion-tes, device-tabell), `plans/010-process.md` (hela, inkl. målbildstabellen 1440 och 390, device-tabellen, token-tabellen, Verification), `HELHET.md` §§ 0–5 (golvet H-01…H-35 i sin helhet), `NOTES.md` § R5 rad 1306–1569 och leadens pixelläsning rad 1570–1589, samt målbilden `tests/alunix-r8/malbilder/V3c.md` (sidnivå; noterat att den föregår processakten och att plan 010 § Målbild är aktens bindande målbild).

Bilder lästa som pixlar: `shots/r5-lead/proc-1440-01…07.png`, `proc-390-01.png`, `-03.png`, `-06.png`; referensramarna `shots/fasA/highway-1440/hw-goteborg-1440--s03.png` och `shots/fasA/k3-act/k3-1440-pin-08.png`.

Levande bygge: servern på 3090 svarade 200 och den kognitiva genomgången kördes mot den, inte mot rapporten — sju mätpass (Playwright, 1440x900, 390x844 och 900/1024/1180/1280/1366) som gav aktens verkliga geometri (`#process` top 5183, höjd 2700, liv 3600 vid 1440; top 6023, höjd 2532 vid 390), `--sc-ps` per scrollposition, per-steg-opaciteter, arkets synliga pixlar, tabbordningen och den horisontella klippningen. Talen nedan är mätta, inte lästa ur NOTES.

## fidelity

### Heuristiktabell (Nielsen, mot `#process` och mot uppgiften heron → mailto)

| # | Heuristik | Dom | Nyckelfynd |
|---|---|---|---|
| 1 | Synlighet av systemstatus | **fail** | Inget visar att akten har sju steg. `01` står ensamt i mono 10,5 px; ingen "av sju", ingen kvarvarande markering. Läsaren vet aldrig om hen är i början eller slutet. |
| 2 | Överensstämmelse med verkligheten | **caution** | Frågorna är verksamhetsägarens egna ord, rätt register. Men `320 · 768 · 1440` i 44 px accent är sidans tyngsta element på tre skärmar, och meningen som förklarar dem är samtidigt uppe i endast 144 px scroll. |
| 3 | Kontroll och frihet | **pass** | Ren scrollakt, inga lägen att fastna i, inget som kapar scrollen; back-navigering suddar ritningen i omvänd ordning (verifierad i feel check). |
| 4 | Konsekvens och standarder | **caution** | Steg 04:s index och titel ligger 12 px lägre än de sex andra (mätt: num top 163 mot 151). Utan transition hoppar paret vid två av sex korsningar. |
| 5 | Felprevention | **fail** | Arket är 880 px hårdkodat mot ett flex-bo som minst kräver 1 430 px. Mellan 900 och ~1 340 px klipps ritningens högra kant bort utan scrollbar och utan varning. |
| 6 | Igenkänning framför minne | **fail** | `Så går det till` / `Från samtal till lanserad sida.` lämnar viewporten vid ps 0,157; första linjen ritas vid 0,19. Etiketten och det den etiketterar är aldrig på skärmen samtidigt. K3, referensen som lånats som form, gör tvärtom: dess titelblock sitter i arkets övre vänstra hörn från första bildrutan. |
| 7 | Flexibilitet och effektivitet | **caution** | Ingen väg att hoppa i akten; 3 600 px scroll krävs för sju svar. Vid 390 är det 2 532 px ren text. |
| 8 | Estetisk och minimalistisk design | **caution** | Rätt instinkt (ett displayelement per skärm), men ankomstskärmen är tom i 504 px scroll och arkets nedre tredjedel är oanvänd på alla sju skärmar. |
| 9 | Fel: känna igen, diagnostisera, återhämta | **n/a** | Ingen inmatning, inga feltillstånd på ytan. |
| 10 | Hjälp och dokumentation | **pass** | Akten *är* dokumentationen, och den är ärlig: inga tider, inga villkor, inga påhittade tal. |

### Kognitiv genomgång, akt för akt mot plan 010 § Målbild

**Uppgift:** verksamhet vill veta hur ett webbprojekt går till och vad det kostar, heron → mailto. **Persona:** Primary (1440, laptop). De fyra frågorna per steg; varje "nej"/"osäkert" blir en rad i `material_fixes`.

| Steg | Rätt effekt? | Ser hen handlingen? | Kopplar handling → effekt? | Ser hen framsteg? |
|---|---|---|---|---|
| Vänder kortet (ps 0→0,905 i heron) | ja | ja | ja | ja — vändningen är läsbar hela vägen |
| Läser tes, Calyx, liggare, pris | ja | ja | ja | delvis — priset finns, men H-08 (pris + Hōrai i samma vy) är opåverkad denna runda |
| **Anländer till `#process`** (ps 0,05) | ja | **nej** | osäkert | **nej** — mätt vid ps 0,10: arkets box ligger [362, 857], varje bana `--p-l:0`, alla sju `<li>` opacitet 0. Skärmen bär en 11 px kicker och en 25,6 px rubrik på 1440x900 kräm. 504 px scroll utan att något händer, direkt efter ett helbrett materialbyte som lovar en ny akt |
| **Steg 01 Uppstart** (0,19–0,28) | ja | ja | ja | ja — konturen dras, texten tonar in synkront. Aktens bästa ögonblick |
| **Steg 02 Planering** (0,28–0,37) | ja | ja | **nej** | Svaret säger "320, 768 och 1440". Siffrorna tänds först vid ps 0,35 (`index.html:802`) och texten börjar tona ut vid 0,37. Samexistens: 0,04 ps = 144 px ≈ 1,5 hjulhack. Leadens F-007 läste samma sak som "siffrorna syns inte förrän i 03" |
| **Steg 03 Design** (0,37–0,46) | ja | ja | osäkert | Öppningen ritas, men skärmens tyngsta element är `320 768 1440` i 44 px accent — ett svar på föregående fråga, medan texten handlar om testadressen |
| **Steg 04 Utveckling** (0,46–0,55) | ja | ja | **nej** | `96 px`-utropet (`:817`, fönster 0,55) tänds exakt när steg 04:s text tonar ut. Måttet landar på steg 05:s skärm. Dessutom hoppar index+titel 12 px vid in- och utgång |
| **Steg 05 Innehåll** (0,55–0,64) | ja | ja | ja | ja — Calyx-svepet är aktens andra riktigt bra beat |
| **Steg 06 Lansering** (0,64–0,73) | ja | ja | delvis | Siffrorna faller 44→12 px men behåller `fill:var(--c-accent)`; planens rad 6 kräver byte till `--hair-ink`. "Arket som blev sidan" levereras till hälften: den blå kedjan konkurrerar fortfarande med den färdiga sidan |
| **Steg 07 Förvaltning** (0,73→håll) | ja | delvis | osäkert | **Mätt: sticky släpper vid ps 0,806.** Vid maxscroll ligger arket [−153, 342] och `footer.close` [342, 900]. Aktens mest förtroendebärande svar ("finns ni kvar?") delar skärm med mailto-raden, och arkets övre hälft är utanför bild. Sex steg får varsin hel skärm; det sjunde får en halv |
| **Mailto** | ja | ja | ja | ja — 67,2 px, en rad, hittas direkt. Tabbvandring: två stopp, båda mailto |

**Stress-persona, 390x844 — den materiella avvikelsen.** Mätt: arket har **0 synliga pixlar** tills `--sc-ps` ≈ 0,46 (scrollY 6822; arkets topp 7703, sektionens topp 6023). Ritfönstren 0,19 → 0,55 — steg 01 till 04 plus halva 05 — exekverar helt utanför skärmen. Läsaren får först 1 531 px staplad text i sju identiska block (index, versal titel, fråga, svar, x7), sedan ett 686 px ark där konturen, hjälplinjerna, öppningen, skrafferingen och liggarraderna redan är färdigritade, utan någon stegtext i närheten. **Signaturformen existerar inte vid 390.** Plan 010 § "Målbild skärm för skärm, 390x844" föreskriver motsatsen ordagrant: arket sticky `top: 12svh`, texten under arket, en stegtext i taget. Byggaren dokumenterade avvikelsen (NOTES § Sammanfattning punkt 6) med skälet "tomma luckor i flödet" — skälet är riktigt men lösningen löste fel ände: det är arket som ska hållas, inte texten som ska fönstras. **F-007: avvikelse från aktens målbild, blockerande, inte kosmetisk.**

**Den kritiska bredd-driften.** Mätt `.process-sheet` högerkant mot viewportbredd: 900 → 1204 (304 px utanför), 1024 → 1325 (301 px), 1180 → 1335 (155 px), 1280 → 1341 (61 px), 1366 → 1346 (ok). Ingen horisontell scrollbar. Vid 1180 (bekräftat i bild) saknas `1440`-siffran, `16:9`-ledaren och måttlinjens högra pil: kedjan läser "320 · 768 · …". Den enda siffra som svaret i steg 02 pekar på är borta, och ett ark utan högerkant läser inte längre som ett ark. `reflow.py` mäter 320 och zoom 200, H-35 listar 320/375/390/414/768/1440 — intervallet 900–1366 finns inte i någon grind, och därför gick det igenom en ren mekanisk runda.

**Avsiktligt vs defekt.** Avsiktligt och rätt: att akten ligger på papper efter `.stagger`; att arket är page-authored sticky och inte en andra `pin`; att Calyx maskas som bild och inte som tredje iframe; `#p-title`-flytten y 447→439 (geometriskt korrekt); `#p-mark` som `<use>` med opacitetston. Defekt: klippningen 900–1340, mobilordningen, steg 07:s halva skärm, utropens fasförskjutning, den tomma ankomsten, steg 04:s 12 px-hopp, måttsiffrornas uteblivna tonbyte.

## ceiling

- **`V3b-chain/index.html` (primary, låst)** — **slår**. V3b svarar inte på "hur går det till"; V3c gör det nu med sju frågor kunden faktiskt ställer. Den fjärde anatomin (H-06) finns och den sekventiella akten efter heron (H-02) finns.
- **`oryzo-ai`** — **står sig bredvid**. Akten rör inte det lånet (objektet som vrider sig i tomrum) och skadar det inte; kortvändningen efter plan 011 är fortfarande sidans peak med störst spann.
- **`mattis-studio`** (lånad som AVVISNING) — **förlorar under 1 340 px**. Ett 880 px ark med hårlinjeram, hörnmärke och titelblock som klipps av på högerkanten läser som ritad chrome, inte som en ritning — precis den läsning avvisningen finns för att förhindra. Vid ≥ 1 366 px håller avvisningen.
- **`K3-r8`** (intern referens för ritningen, `HELHET.md` § 1) — **förlorar**. K3:s ark äger hela viewporten och deklarerar sig själv i sitt eget titelblock från bildruta ett (`k3-1440-pin-08.png`: `ALUNIX / SEKTION A-A / SKALA 1:1` uppe till vänster). V3c:s ark är inboxat i ett 1440-fält, oetiketterat medan det ritas, och dess nedre tredjedel bär ingenting på någon av de sju skärmarna.
- **`highwaymedia`** (Antons namngivna, ledgerrad 2026-09-15) — **slår vid 1440, förlorar vid 390**. Deras tidslinje är trubbigare men rubriken `Arbetsprocessen` står kvar över sekvensen, och den läser lika bra på telefon som på laptop. V3c:s form är bättre och dess mobilutfall sämre.
- **`insign`** (Antons namngivna) — **slår**. Insign skriver löftena som kryssrader i tre nivåkort; V3c skriver dem som fråga och svar, utan kort, utan rutnät, med testadressen och CMS:et i klartext på samma ställe.
- **`hoy`** (Antons namngivna) — **står sig bredvid**. Hoy ger varje kapitel en egen skärm med en auktoritet; V3c gör det för sex av sju steg. Det sjunde delar skärm med footern, vilket är exakt det Hoy aldrig gör.
- **`dope-security`, `monologue`, `planhat`** — **öppnades inte denna runda**. Ingen dom avges; de tre står i select-raden men ingen av dem bär processakten i låsets `Borrow only`-fält.

## material_fixes

1. `index.html:720` `.process-sheet{width:880px;flex:none}` — arket klipps på högerkanten 900→1340 px (mätt: högerkant 1204 vid 900, 1325 vid 1024, 1335 vid 1180, 1341 vid 1280; ingen scrollbar). Mål: `width:min(880px, calc(100vw - var(--rail-x) - 384px - 112px)); height:auto; aspect-ratio:880/495` → högerkant ≤ viewport − 24 px vid 900, 1024, 1180, 1280, 1366.
2. `index.html:836-841` (mediablocket ≤ 899 px) — arket har 0 synliga px till `--sc-ps` 0,46; ritfönstren 0,19→0,55 spelar utanför skärmen. Mål enligt plan 010 § 390: `.process-sheet{position:sticky;top:12svh}` med arket före `<ol>` i källordning vid ≤ 899, `.process-steps li` kvar i flödet → arket ≥ 90 % synligt från ps 0,17 till 0,83, mätt som synliga px / arkhöjd.
3. `index.html:691` `.process-stage{top:202px}` + `:683` `min-height:300svh` — sticky släpper vid ps 0,806, så steg 07 delar viewport med `footer.close` (mätt vid maxscroll: ark [−153, 342], close [342, 900]). Mål: `min-height:340svh` och `top:150px` → sticky-hållet slutar vid ps ≥ 0,88 och steg 07 äger en hel viewport i ≥ 400 px scroll innan `.close` bryter in (H-05, H-08).
4. `index.html:802`, `:807`, `:817` — utropen tänds efter att sin egen stegtext börjat tona ut (`#p-m*` 0,35 mot stegfönster som slutar 0,37 = 144 px samexistens; `#p-c-row` 0,55 = noll samexistens med steg 04). Mål: `#p-m320,#p-m768,#p-m1440` 0,35 → **0,305**; `#p-c-gutter` 0,43 → **0,415**; `#p-c-row` 0,55 → **0,515** → varje steg har sitt sanna mått uppe ≥ 0,03 ps (108 px) innan texten tonar ut.
5. `index.html:685-689` + `:1080-1082` — aktens rubrik lämnar viewporten vid ps 0,157, första banan ritas vid 0,19; etiketten och ritningen är aldrig samtidigt på skärmen, och h2:n (25,6 px) är aktens minsta displayelement. Mål: kicker + h2 flyttas in i `.process-stage` (eller `SÅ GÅR DET TILL` ritas i arkets övre vänstra hörn, 12 px `--hair-ink`, som K3:s titelblock) och `.process-title` → `clamp(1.8rem, 2.6vw, 2.4rem)` → rubriken synlig vid varje ps mellan 0,19 och 0,81.
6. `index.html:788` `#p-outline` fönster 0,19 och `:1086` `--step-start:0.19` — ankomstskärmen är tom i 504 px scroll (mätt ps 0,10: alla banor `--p-l:0`, alla `<li>` opacitet 0). Mål: `#p-outline` 0,19 → **0,07**, steg 01 `--step-start` 0,19 → **0,09**, efterföljande fönster oförändrade → konturen ritar inom 150 px från att sektionen äger viewporten.
7. `index.html:698` `.process-steps li{justify-content:center}` — steg 04 (2-radigt svar) ligger 12 px lägre än de sex andra (mätt: num top 163 mot 151, titel 193 mot 181) och paret hoppar vid två korsfadningar. Mål: `justify-content:flex-start; padding-top:151px` → index-topp identisk, Δ **0 px**, över alla sju.
8. `index.html:753-760` `.measure{fill:var(--c-accent)}` — siffrorna faller 44→12 px men byter aldrig till `--hair-ink` (plan 010 § målbild rad 06); mätt i `proc-1440-06.png` är den blå kedjan fortfarande skärmens näst tyngsta märke när Calyx är fylld. Mål: `fill` interpolerad till `--hair-ink` över samma fönster 0,64→0,73 → noll accent i arket vid ps ≥ 0,73 (H-33: ett blått moment per skärm, inte ett kvarglömt).

## keep

Fråga-och-svar-copyn ordagrant — sju frågor en verksamhetsägare faktiskt ställer, besvarade i vi-form utan tider, villkor eller tal utöver de sex sanna måtten; och ritningen som form (kontur, måttlinje, hjälplinje, skraffering, ledare) i stället för fyra ikonkort eller en tidslinje med punkter. Steg 01:s inritning och steg 05:s Calyx-svep är aktens två färdiga ögonblick och ska inte röras när de åtta fixarna läggs.

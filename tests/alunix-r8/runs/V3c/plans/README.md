# Planer, V3c

Uppdaterad av arkitekten 2026-09-17 i helhetsloopens runda 1 (fas C). Status läses ur
NOTES.md; en plan är DONE först när leadens grind är grön på pixlar. R7-planerna refererar
R6-läget av `runs/V3c/index.html` (md5 `424cdd46`); matchar raderna inte när byggaren öppnar
filen, stoppar byggaren. (018 till 023 refererade R5-läget `fcbee8f1` och är byggda.)

## R13, i ordning (EN plan; taket är åtta)

Skriven av lead 2026-09-17 mot R12-läget av `runs/V3c/index.html` (md5 `ee0999d4`), hittad
i exit-granskningens pixlar, inte av arkitekten och inte en av Antons egna beställningar.

| # | Titel | Allvar | Ordning | Källor |
|---|---|---|---|---|
| 047 | Arket täcker stegtexten mellan 768 och 1279: `.process-steps` får samma bredd och centrering som `.process-stick` | HIGH, visuellt/layout | 1 | Leads egen pixelmätning, `shots/final-widths/process-768.png` mot `-414.png`/`-320.png` |

`.process-grid` blir en enkolumnsgrid i planschläget (≤1279px); `.process-stick` (arket)
är centrerat och smalare (480px) än kolumnen, men `.process-steps` fyller hela kolumnens
bredd vänsterjusterat. Textblocket (x 46–374 vid 768px) och arket (x 144–624) överlappar
horisontellt i 230px — texten går in under arkets ogenomskinliga bakgrund och klipps mitt
i ordet, i remsan 641–1279px där kolumnen är bredare än arket men ännu inte tvåspaltig.

Fixen kopierar `.process-stick`s eget `width`-uttryck (`min(100%,480px,calc((100svh -
224px) * 320 / 360))`) och `justify-self:center` till `.process-steps`, så listan
centreras till exakt samma box som arket vid varje viewport-höjd. `.process-p`/
`.process-note`s egna `max-width:34ch` är oförändrade och redan smalare än 480px — bara
blockets position flyttas, ingen radbrytning ändras.

**Utanför R13:** allt annat. Tvåspaltsläget (≥1280px) och SVG:ns planschgeometri rörs inte.

## R12, i ordning (EN plan; taket är åtta)

Skriven av arkitekten 2026-09-17 mot R10-läget av `runs/V3c/index.html` (md5 `d3491b4a`).
**En copy-agent arbetade i filen när planen skrevs**, så radnumren i planen är ungefärliga;
byggaren hittar varje ankare med `Grep` på dess kod och stoppar om koden inte matchar i sak.

Som R11 finns inte heller den här rundan för att stänga ett fynd. Loopens slutvillkor nåddes
i runda 5. R12 är Antons andra beställning 2026-09-17: Calyx ska inte vara svartvit, den får
vara gråskala under ritningsprocessen men ska få sin färg i den färdiga versionen i sista
steget.

| # | Titel | Allvar | Ordning | Källor |
|---|---|---|---|---|
| 046 | Calyx får sin färg i sista steget: mättnaden blir en funktion av `--k6`, aktens egen progress | ingen (inte ett fynd) | 1, visuellt / rörelse | Antons beställning 2026-09-17; `shots/loop-5/preview/preview-1440-process-05.png` mot `-06.png`; arkitektens mätning av `assets/demo-calyx-1440.webp`; loop 5:s probtal för `#process` |

**Assetet är vendorat och blockeraren stängd** (lead 2026-09-17):
`assets/demo-calyx-1440-color.webp`, 1076x606, 79 178 B, omkodad ur
`board/cells/K4-r8/assets/demo-calyx-1440.webp`; originalet var färg, och gråskalan i
arbetsfilen var leads egen omkodning för perf-fynd 6. Arkitekten kontrollmätte båda filerna:
färgfilen mean chroma **20,69** (max 129), grå 0,01 (max 1), och **luminansen är i praktiken
identisk** (mean 0,545 mot 0,544, p95 0,941 mot 0,941). Samma bildruta, samma tonkurva, bara
kulören skiljer. Den grå filen står kvar som Target B:s basskikt och som referens för
grå-ekvivalenskontrollen.

**Vägvalet är avgjort i planen: Target A** (färgfilen ensam,
`filter:grayscale(calc(1 - var(--k6)))`), med Target B (två `<image>`, grå under och färg
över på `opacity:var(--k6)`) som fallback bara om A faller på kostnadsgränsen. Skälet, i
fallande vikt: B lägger sin kostnad i steg 05, det enda fönster på det elementet som **redan**
animerar (gruppens `clip-path` på `--k5` skulle då komponera två raster i stället för ett),
medan A lägger sin i steg 06 där `.p-live` i dag inte gör någonting; B kostar +79 178 B i
sidvikt mot A:s +19 658 B, på en sida som låg på 476 kB vid R9; och A är två `Edit` utan ny
DOM, ny z-ordning eller andra dekodning. Mätningen körs ändå och kan kullkasta beslutet;
därför har planen två A/B-fönster, steg 06 (start 7 200) och ett kontrollfönster i steg 05
(start 6 800) som prövar just invändningen att filtret skulle kosta i vila.

Fönstret är `--k6` (steg 06, lansering), inte `--k5` eller `--k7`, med skälet läst i pixlarna
och skrivet i planen: vid 05 väger de två 44 px-måtten i accent lika tungt som bilden, vid 06
drar sig varje annan markering i arket tillbaka (måtten till 12 px och `--hair-ink`,
hjälplinjer och skraffering till 0,35 opacitet, konturen till halv vikt). Färg där är samma
gest i en fjärde egenskap, och ordagrant vad steg 06:s not säger: "Bläcket står kvar som ram.
Ritningen och sidan är samma sak."

Planen rättar också ett antagande i beställningen: `--k1` till `--k7` är **inte**
`@property`-registrerade och behöver inte vara det. Det som måste vara registrerat för att
kedjan inte ska stega är `--sc-ps`, och det är det. Beviset står i filen: `--k6` driver redan
`color-mix()` och `scale()` på `.measure`, och `--k5` driver redan `clip-path` på **samma
element** planen rör, alla tre mätt jämna (`#process:--sc-ps` max_step 0,67 / 0,76 % vid
cpu 1, staircase 0, loop 5). Registreras `--k6` ändå måste det vara `inherits: true`.

Planen har en mätbar gräns för kostnaden (sammanflätad A/B i steg 06:s eget fönster, tre par,
median; A får inte överstiga B med mer än 5 ms p95 vid cpu 1), en specificerad fallback
(två `<image>`, grå under och färg över på `opacity:var(--k6)`, så bara opacitet animeras),
och ett målvärde för invert-läget (bildrektangelns mean relativa luminans ≤ 0,34 och p95
≤ 0,80; den är i dag 0,544 / 0,941 och skulle mot `--c-black` ge ≈ 11:1 och läsa som en lampa).

**Utanför R12:** allt annat. Q30/Q31 väntar på Anton. H-21/H-22/H-32 står som redovisat golv.
Faller kostnadsgränsen även för fallbacken stoppar byggaren och rapporterar båda mätserierna
i stället för att bygga.

## R11 (helhetsloopen runda 5), i ordning (EN plan; taket är åtta)

Skriven av arkitekten 2026-09-17 mot R10-läget av `runs/V3c/index.html` (md5 `d3491b4a`);
matchar raderna inte när byggaren öppnar filen, stoppar byggaren.

**Loopen nådde sitt slutvillkor i runda 5**: Astra svarade `ship` med noll `material_fixes`,
29 av 35 H-rader är bockade och de sex öppna är exakt de som inte kan bockas i loopen (tre
väntar på Anton via Q30, tre är bildtidens redovisade arkitektoniska golv), och
smoothness-grinden är grön i båda riktningarna inom det golvet. **R11 finns därför inte för
att stänga ett fynd.** Den finns för en enda sak: Antons beställning 2026-09-17 att få se
processakten inverterad och jämföra den mot papperet.

| # | Titel | Allvar | Ordning | Källor |
|---|---|---|---|---|
| 045 | Processakten inverterad som ett läge i samma fil (`?process=invert`), som jämförelseunderlag mot papperet | ingen (inte ett fynd) | 1, visuellt | Antons beställning 2026-09-17; `shots/loop-5/contrast/` (pappersläget mätt), `BRIEF.md` § Byggarens rader R1 rättelse 2 (accenten mot mörkt, 2,93:1) |

Planen är avsiktligt additiv: ett CSS-block, en token, en rad JS. **Ingen rad i
pappersvägen redigeras**, så pappersläget är bevisligt det som nådde golvet, och de två
mapparna `shots/r11/papper/` och `shots/r11/invert/` är två lägen av samma sida och inte två
sidor. Planen öppnar och stänger ingen H-rad; den rör H-03 och H-06 åt fel håll och skriver
ut varför i sitt eget avsnitt "Vad jag själv ser i pixlarna, för och emot", som underlag åt
Anton. Väljer han inverteringen är grundväxlingen (tesbandet, prisblocket, avslutet) en egen
plan i runda 6.

**Utanför R11:** allt annat. Q30/Q31 väntar fortfarande på Anton. H-21/H-22/H-32 står som
redovisat golv med loop 5:s tal (varje fönster lika med eller bättre än loop 4:s). Ingen ny
mekanism, ingen ny geometri, inga nya banor, ingen rörelse.

## R10 (helhetsloopen runda 4), i ordning (tre planer; taket är åtta)

Skrivna av arkitekten 2026-09-17 mot R9-läget av `runs/V3c/index.html` (md5 `909916d1`);
matchar raderna inte när byggaren öppnar filen, stoppar byggaren. Ordningen är kontraktets:
funktion → states → flöde/hierarki → visuellt → kod. Källor: `HELHET.md` § 3 (loop 4-raderna),
`NOTES.md` § Loop 4, `reviews/loop-4-astra.md` (tre fynd, alla tagna), arkitektens egna
mätningar i `shots/loop-4/`.

| # | Titel | Allvar | Ordning | Källor |
|---|---|---|---|---|
| 042 | Prisblockets platshållare (760 px mot 463) krymper sidan 297 px vid första målningen; motorns akttoppar under bandet står kvar fel; 390-previews ett race | HIGH | 1, funktion | arkitektens C1 = Astra loop 4 fix 1; `shots/loop-4/mountshift.json`, `shiftprobe*.json`, `preview390*.json`, `pricefix_ab.json`, `probe/ab/price-*`, `giant-*`; `process-1440/v3c-1440-life-01.png` |
| 043 | Calyx-revealen har ingen öppning: `.rv` klipper inte, ramen står hel vid varje `--rv` | HIGH | 2, funktion / states | Astra loop 4 fix 2; `shots/loop-4/astra-verify/verify_astra4.json`, `calyx-rv0.png` |
| 044 | Driftens överlämning tes → jätte hoppar blå → papper i en bildruta vid 3 600 | MEDIUM | 3, visuellt | Astra loop 4 fix 3; `astra-verify/verify_astra4.json`, `drift-3580.png`, `drift-3620.png` |

042 först: H-15, H-30 och bildtiden i bandet mäts mot den konstanta dokumenthöjden, och 043:s
Calyx-fönster ligger i samma band. 043 mäts före och efter i Calyx-fönstret (2 862 + 20 ticks)
med tre körningar och median, som 036. 044 är oberoende och en fyraradersändring.

**Utanför R10:** Q30/Q31 (bandets omkomposition och 96 px; H-02/H-03/H-08 s03, väntar på
Anton), H-21/H-22/H-32 (bildtiden vid cpu 4 och i bandet: arkitektoniskt golv redovisat i
NOTES § Loop 4, pinnen ensam 18,4 ms; det som är kvar i filen är 042), H-23 (3,12 / 3,52 % i
fönster där ramarna monteras; mäts om efter 042), H-24 (verktygsskuld: `.rv:transform` läses
DEAD för ren `scale()`), H-34 (leadens grind; folden 7/7 mätt), jättens skala 0,92 → 1,
sidvikten (476 kB), a11y-skulden, `sites/calyx.html`:s nav vid 390 (referenssajten).

**Verktygsfynd loop 4:** `frames.py life` och `slices4.py` laddar vid scrollY 0 och hoppar,
så prisblocket målas först när fönstret passerar det: alla fångster efter 5 340 (1440) står
på den krympta sidan medan motorns toppar står på den ursprungliga; kickern i `s06` vid y 18
i stället för 237 är den skillnaden, inte en ny geometri. `motion_probe.py --start` scrollar
direkt till startpositionen, så ett fönster med start ≥ 1 920 får 036 B:s montering i sin
första bildruta (tesfönstret 142 ms); 036:s mätningar förmonterade av det skälet.
`.horai-wrap .rv:transform` läses DEAD (ren `scale()`, atan2-blindheten, README § Verktyg);
`.horai-wrap:--rv` spåras i stället.

## R9 (helhetsloopen runda 3), i ordning (sju planer; taket är åtta)

Skrivna av arkitekten 2026-09-17 mot R8-läget av `runs/V3c/index.html` (md5 `70214a22`);
matchar raderna inte när byggaren öppnar filen, stoppar byggaren. Ordningen är kontraktets:
funktion → states → flöde/hierarki → visuellt → kod. Källor: `HELHET.md` § 3 (loop 3-raderna),
`NOTES.md` § Loop 3, `reviews/loop-3-astra.md`, leadens pixelläsning R8 (två fynd, båda först).

| # | Titel | Allvar | Ordning | Källor |
|---|---|---|---|---|
| 035 | Revealens latch samplar shimens lerp tills den landat (aktobjektet löses per tick, exakt 1) | HIGH | 1, funktion | leadens R8-fynd 1; `shots/loop-3/latch_diag.json`, `slices-1440-fix/`; Astra loop 3 fix 1 |
| 036 | Revealen klipper aldrig en levande ram: irisen och uppdragningen som transform på en inre box, ramen kontraskalad | HIGH | 2, funktion (bildtiden) | `shots/loop-3/probe/ab/` (clip-path över levande Hōrai 101 till 303 ms, transformreceptet 35 till 47, ingen klippning 35 till 62); Astra loop 3 K7 |
| 037 | `?preview=process-0N` siktar om efter `load` och `fonts.ready` | HIGH | 3, funktion | `shots/loop-3/preview_check.json`; Astra loop 3 fix 5 |
| 039 | Kortsidan, `is-turning` och `data-on` av läser shimens `cur` | MEDIUM | 4, states | Astra loop 3 fix 2, 3; `index.html` 1660, 1666, 1708 |
| 040 | Arkets kontur hel medan steg 01 läses | LOW | 5, flöde/hierarki | H-15; `slices-1440/v3c-1440--s06.png`, `process-390/…life-01.png`; Astra loop 3 fix 6 |
| 038 | Grunddriften 44 → 24 %, H-19 omskriven på mellantonen | MEDIUM | 6, visuellt | leadens R8-fynd 2; `shots/loop-3/drift2/` |
| 041 | Driften skrivs på `.ground` av sidan, mätgrindad | LOW | 7, kod | loop 2 `synth3` (9,13 → 0,24 ms per skrivning); loop 3 `probe/ab/` (ingen vinst i prisfönstret); Astra loop 3 fix 4 |

035 först: 036 bygger på samma `--rv` och samma sampler, 039 hänger tre konsumenter till
på 035:s `latchTick`. 036 mäts med `shots/loop-3/scripts/motion_probe_ab.py --pre` i
prisfönstret (3 873, 18 ticks) och jättefönstret (2 700, 28 ticks) före och efter, tre
körningar var, median. 037 är oberoende. 040 och 038 är enradsändringar. 041 sist och bara
med mätt vinst (som 028 E).

**Utanför R9:** Q30 (bandets omkomposition; H-02/H-03/H-08 s03), H-24 (verktygsskuld),
H-34 (leadens grind), jättens skala 0,92 → 1 (oläsbar, redundant mot ordscrubben,
rapporterad), sidvikten (462 kB), a11y-skulden, K3-mallens `.process-grid`-spann (R6-fynd).

**Verktygsfynd loop 3:** `slices.py`/`shoot_slices` når sina positioner med `scrollTo`,
alltså exakt den väg latchen inte täcker (K5): skivor 04/05 visade klippta ramar utan att
ramarna var sovande. `slices_fix.py` injicerar 035:s sampler före fångsten och är
helhetsloopens skivfångst tills 035 är byggd. `motion_probe_ab.py --pre "<js>"` (scratchkopia)
kör en ablation efter `load` + 5 s före hjulet; A/B-talen svänger ±50 % mellan identiska
körningar, så tre körningar och median.

## R8 (helhetsloopen runda 2), i ordning (åtta planer; taket är åtta)

Skrivna av arkitekten 2026-09-17 mot R7-läget av `runs/V3c/index.html` (md5 `d30355da`);
matchar raderna inte när byggaren öppnar filen, stoppar byggaren. Ordningen är kontraktets:
funktion → states → flöde/hierarki → visuellt → kod. Källor: `HELHET.md` § 3 (loop 2-raderna),
`NOTES.md` § Loop 2, `reviews/loop-2-astra.md`, leadens pixelläsning R7 (tre fynd, alla först).

| # | Titel | Allvar | Ordning | Källor |
|---|---|---|---|---|
| 027 | Ramarna vaknar aldrig: observern på wrappern i stället för ramen | HIGH | 1, funktion | leadens R7-fynd 1; `diag3.json A_*`, `diagA2.json` (12/12 sovande → 0/12) |
| 028 | Bildtiden: shimen läser inline och batchar, `--sc-p` utan arv, ordscrubben som gradientfront | HIGH | 2, funktion (profileringsrundan) | `profile*.json`, `synth*.py`; Astra loop 2 fix 3 |
| 034 | Processakten: ankare ur gridet (inte sticky-rect), prosan utan reveal | HIGH | 3, funktion | Astra loop 2 fix 1, 2; `verify_astra2.py`, `astra1-*.png` |
| 031 | Ramarnas reveal: sidans egen latch på det lerpade värdet | MEDIUM | 4, states | Astra loop 1 fix 8 (uppskjuten), H-27, gate 94 |
| 033 | Priset: liggarens fyra hårlinjer dras på `--sc-ps` | MEDIUM | 5, flöde/rörelse | H-25; `life-00`, `s05` |
| 029 | Grunddriften 62 → 40 %: ton, inte tvätt | MEDIUM | 6, visuellt | leadens R7-fynd 2; `diag3.json B_summary`, `B*-giant.png` |
| 030 | Jätterubriken 88 px / −0,04em, ordet helt | MEDIUM | 7, visuellt | leadens R7-fynd 3; `C_giant`, `synth3` |
| 032 | Folden vid 390 (H-13) och bandets mobilseams 96 px (H-05) | LOW | 8, visuellt | `preview-390-front`, `s390-02/03`; Astra loop 2 bild 18/20 |

027 först: allt som rör bandets balans (H-08) och bildtidens mätning i bandet förutsätter
levande ramar. 028 mäts **efter** 027 (ramarna vakna är det verkliga läget) med samma
harness före och efter sina egna steg. 034 före 031: båda rör `readState`; 031 läser
shimens `acts[i].cur`, som 028 A behåller. 029/030/032 är oberoende enradsändringar.

**Utanför R8:** Q30 (bandets omkomposition, obesvarad; ger också H-07:s 96 px och H-02/H-03),
H-01 (12,09 vh, 0,09 över raden, ingen plan), H-24 (proben blind för `scale()`, verktygsskuld),
H-34 (leadens grind), sidvikten (452 kB mot 425; glyfens `d` dubblerad i 016, ~2 kB, räcker
inte ensam), `--sc-canvas` på `:root` (motorns skrivning, 9 ms per ändring, kan inte flyttas
utan motorredigering; redovisad i 028 D), 024 (kanten 4 px, golvet uppfyllt), a11y-skulden.

**Verktygsfynd loop 2:** `previews.py`/`shoot_slices`-fångster med `networkidle` + 1,5 s kan
fånga ett läge före `load`-mätningen (previews 1440 visade arkets ram som en färsk fångst
inte visar); byggaren tar previews med `wait_until="load"` + 1,5 s. Kontrollen
`tests/motion/smooth.html` gav 0 till 2 rutor > 33 ms i varje körning; cpu 4-tal svängde
±100 ms mellan identiska körningar (hero-down-100 817 ms mot 72 ms i profilen) och cpu 1-talen
är loopens bar för före/efter.

## R7 (helhetsloopen runda 1), i ordning (åtta planer; taket är åtta)

Ordningen är kontraktets: funktion → states → flöde/hierarki → visuellt → kod. Källor:
`HELHET.md` § 3 (bockat av arkitekten 2026-09-17), `NOTES.md` § Loop 1, `reviews/loop-1-astra.md`,
leadens pixelläsning R6.

| # | Titel | Allvar | Ordning | Källor |
|---|---|---|---|---|
| 025 | Processakten i helheten: railmarginalen (ogiltig `padding` på `.principles`, kickern utan rail), arkets ankomst, stegens fönster (överlapp 1440, fel tecken 390), steg 07:s hållning | HIGH | 1, funktion | leadens tre R6-fynd + "arket glider ut vid 07"; loop 1 `diag.json`, previews 1440/390 |
| 017 | Grunddriften synlig, spaltoffset ≥ 96 px, seams utan slitsar, bleeden mot rubriken (steg D) | HIGH | 2, funktion + flöde (ändrar bandets geometri som resten läser) | H-04, H-05, H-19, H-20; loop 1 `s1440-03`, `diag2` |
| 012 | Mobilordningen vid ≤ 900 (samma mediablock som 017) | MEDIUM | 3, flöde | H-14, Q28; loop 1 `s390-03..06` |
| 013 | Prisblockets grafitplan `--c-graphite` | MEDIUM | 4, visuellt | H-11, T-3, Q27; loop 1 `s1440-05` |
| 014 | Jätterubriken 6rem | LOW | 5, visuellt | H-07, T-5; loop 1 `giantFont 76,8 px` |
| 015 | Avslutet: hårlinje på `--sc-ps`, mailto 2rem till 6rem (`min-height:62svh` finns redan) | MEDIUM | 6, flöde + rörelse | H-12, H-25, T-8; loop 1 `s1440-10`, `mailto390 25,6 px` |
| 016 | Kortbaksidans A-glyf i hårlinje | MEDIUM | 7, visuellt | H-09, T-4; loop 1 `preview-*-back` |
| 026 | Ramarnas montering idempotent (`src=null`, vaken ram utanför skärmen) | MEDIUM | 8, kod | Astra loop 1 fix 7, verifierad rad 1547-1575 |

025 först: A är ett layoutfel (hela `padding`-deklarationen ogiltig), B rättar
fönsterformeln som alla previews och 390-planschen bygger på. 017 före 012 eftersom båda
skriver `@media (max-width:900px)`-blocket på rad 510-515; byggaren skriver blocket en gång
med båda planernas rader. 015 delar `.close` med plan 007 (R4), som redan satt
`min-height:62svh` och `display:flex`; planen är justerad mot det.

**Efter Astra (2026-09-17):** 012 rättad (marginalnollning), 015 rättad (100 svh, 0 till 0,46, 44 px),
017 höjd till 160 px luft + steg D (bleeden), 025 utökad med B4 (hysteres) och D (arket vid låga
viewports); 024 (H-10 kant, LOW; golvet redan uppfyllt) lämnar R7 för 026 (kodfel). Q30
(bandets omkomposition, H-02/H-03) till Anton.

**Utanför R7 (loop 2 eller senare):** 024 (kanten 4 px), Q30:s omkomposition om ja, wrapperns
reveal-latch på `--sc-ps` (Astra fix 8, H-27-not), H-13 (folden vid 390 har 16,3 % död grund under
underraden, mätt `diag2`; kräver en egen höjdbudget för 4:5-kortet), H-21/H-22 bildtiden vid
cpu 4 (arkitektonisk, samma rotorsak sedan R4: RecalcStyle mot `--kN`-kedjan; loop 1 mätte
cpu 1 heron p95 35 ms men processakten p95 18,5 ms), H-23 (`#process` max_step 3,59 % i en
körning vid cpu 4, 0,73 % vid cpu 1), H-34 (`contrast_over_media` över hela sidan, leadens
grind), a11y-skulden (`.impeccable/a11y-debt.md`).

## R6, i ordning (sex planer; taket är åtta)

| # | Titel | Allvar | Ordning | Källor |
|---|---|---|---|---|
| 018 | Ramarna sövs utanför 40 %, monteras utanför heron, reveal på wrappern | HIGH | 1, funktion | perf 1, 2; Astra 2a |
| 019 | Processakten i ny form: prosa i flödet, arket sticky, ankrade fönster, copy v1, "Hur vi tänker", 390-planschen | HIGH | 2, funktion + flöde | Anton 2026-09-16; underlaget § 3-5; a11y 3, 5, 8; Astra 3, 4, 7, 8; critic 1, 2, 4, 5; heuristik 1, 2, 3, 5, 6, 7; perf 3, 4, 7; lead F-007 |
| 020 | Arkets geometri och utrop: 7 rem sant, ingen klippning, A-glyf, tonbyte, ett blått moment per skärm | HIGH | 3, flöde + visuellt | Astra 1, 4b, 5, 6, 7; critic 3, 6; heuristik 8; lead F-007 02/04/06 |
| 021 | Kontrast: bildtexterna på papper, CTA-understrykningen i `currentColor` | HIGH (WCAG) | 4, states | a11y 1, 2 |
| 022 | Kortet: fokus före inertering, träffytor 44 px, baksidan i tillgänglighetsträdet, preview auktoritativt | MEDIUM | 5, states | a11y 4, 6, 7; Astra 2b |
| 023 | Liggartråden ankrad i liggaren | MEDIUM | 6, flöde | perf 5 |

018 mäts före 019: processaktens bildtid ska läsas mot en sida där ramarna inte längre
kostar 66 % av tasktiden. 019 och 020 rör samma element och byggs som en diff, 019 först.

**Formbeslutet (019), i tre rader.** Stegen är prosa i flödet, alltid synliga, ingen
korsfadning: det löser PageDown, textmarkering och överlappande rubriker utan hållfönster.
Arket är sticky bredvid texten (≥ 1280) eller ovanför den (≤ 1279) och ritas i takt med
att stegen passerar viewportens mitt; sektionens höjd är textens, så steg 07 kan inte
hamna utanför sticky-hållet. Fönstren ankras i stegens uppmätta läge (JS en gång vid
mount/resize, fjorton tal på `#process`), inte i en tabell.

## Fynd över de fem rapporterna: taget eller förkastat

| Fynd | Rapport | Dom | Var / skäl |
|---|---|---|---|
| Ramarna 66 % av tasktiden; söv med `content-visibility:hidden` | perf 1 | taget | 018 |
| `rootMargin` 100 % monterar inne i vändningen; 40 % | perf 2 | taget | 018 |
| Banor utanför stilträdet tills fönstret öppnat | perf 3 | taget, i `display:none`-form på `<g data-step>` (`content-visibility` gäller inte SVG-barn) | 019 device-rad 8 |
| Banfönster ≥ 0,075, max_step ≤ 12 % | perf 4 | taget, via ankrade fönster med tillåten halvöverlappning | 019 steg 3 |
| Liggartråden ritas innan liggaren syns | perf 5 | taget | 023 |
| `demo-calyx-1440.webp` 207 kB → ≤ 60 kB | perf 6 | **stängd av lead** före R6: omkodad till 1076x606 gråskala under 60 kB | ingen plan |
| `will-change: stroke-dashoffset` bort | perf 7 | taget | 019 device-rad 9 |
| Probens blindhet för ren `scale()` (`.giant`, `#threadFill` DEAD) | perf fidelity | inte byggarens; verktygsskuld till lead (`motion_probe.py` läser `atan2(b,a)` och faller till translation) | README § Verktyg |
| `.frame-cap` 3,06:1 | a11y 1 | taget | 021 |
| `.card-cta` understrykning 2,92:1 | a11y 2 | taget | 021 |
| PageDown renderar aldrig 02/04/06; ≥ 800 px per steg | a11y 3 | taget, löst av formen (text i flödet) i stället för hållfönster | 019 |
| Fokus tappas till `body` vid inertering | a11y 4 | taget | 022 |
| `elementFromPoint` returnerar osynligt steg | a11y 5 | taget, moot genom formen | 019 |
| Träffytor 104x23 | a11y 6 | taget | 022 |
| `aria-hidden` på baksidan | a11y 7 | taget, med `.sr-only`-kopia eftersom `inert` ändå döljer för AT | 022 |
| Arket under vikningen vid 1366x640 | a11y 8 | taget: `top` ur `svh` | 019/020 |
| Dubblerade h3, hero-bildens alt, DOM-ordning vid tvåspalt | a11y skuld | köade till `.impeccable/a11y-debt.md` som rapporten föreslår; DOM-ordningen ägs av plan 012 | fas C |
| Utropen ett fönster för sent, siffrorna byter inte ton | Astra 1, critic 3, 6, heuristik 8, lead 02/04/06 | taget | 020 |
| Ramarnas reveal registreras aldrig | Astra 2a | taget | 018 |
| `?preview=back` inerteras nästa bildruta | Astra 2b | taget | 022 |
| 390-målbilden inte byggd | Astra 3, critic 2, heuristik, lead | taget, i 019:s form (arket sticky ovanför, texten under) | 019 |
| Steg 07 utanför sticky-hållet | Astra 4, critic 1, heuristik 3, lead | taget, löst av formen (sektionshöjd = textens) | 019 |
| `.guide,.hatch`-selektorn träffar `#p-rev` | Astra 4b | taget | 020 E |
| `7 rem` är 4,5 rem | Astra 5 | taget; plan 010 rättad med fotnot | 020 A, 010 § Rättelse |
| A-glyfen osynlig (fill-attribut + skalad stroke) | Astra 6, critic 01 | taget, egen `<path>` med `stroke-width` i pathens enheter | 020 C |
| Arket klipps 900 till 1 340 px; `top:202px` som konstant | Astra 7, heuristik 1 | taget | 019 grid + 020 B |
| Två stegtexter ovanpå varandra vid fönstergräns | Astra 8 | taget, moot genom formen | 019 |
| Sektionsrubriken 25,6 px rankar under stegen | critic 4 | taget, 48 px | 019 steg 2 |
| Tom ankomstskärm 504 px | critic 5, heuristik 6, 8 | taget, moot genom formen (stycke 01 står överst från början, konturen ritas när det kommer in) | 019 |
| Kör `scroll_verify` för plan 011:s H-17/H-18 | critic 8 | inte en byggarplan: leadens grind i R6 | README § Grindar |
| "01 av sju"-status, väg att hoppa i akten | heuristik 1, 7 | **förkastat**: alla sju rubriker ligger nu i flödet och syns i följd, vilket är statusen; en räknare är gate 69/81-territorium och en hoppnav är ett fjärde chrome-element sidan inte har | 019 löser i sak |
| Steg 04 ligger 12 px lägre | heuristik 4 | **förkastat som eget fynd**: moot, inga absolut positionerade li | 019 |
| Arkets nedre tredjedel oanvänd | heuristik 8 | **förkastat**: måttkedjan (y 455 till 476) och titelblocket (y 439 till 493) ligger där; efter 020 även tonbytet | ingen |
| Hoppnav / "Så går det till" som titelblock i arket | heuristik 5 (alternativ b) | **förkastat**: kickern och h2 står i flödet ovanför kolumnerna och arket bär bara form; K3:s titelblock var sidans nav, V3c har en annan | 019 väljer h2 48 px |
| Stegen som fråga och svar | Anton 2026-09-16 | taget: copy v1, ett stycke per steg, underlagets § 4-antaganden inskrivna | 019 |
| "Hur vi tänker" behöver plats | underlaget § 5 | taget: eget kort avsnitt på papper efter akten, före avslutet, som hairline-liggare utan nummer | 019 |
| Priset läser som ett hål, H-10 tunn linje i tomrum, kortets högra halva tom | critic, a11y (utanför R5:s uppdrag) | står i fas C: 013, 016; H-10 saknar fortfarande plan | fas C |

## Fas C, ursprunglig ordning (2026-09-16, ersatt av § R7 ovan)

017 → 012 → 013 → 014 → 015 → 016 → 024 (att skriva). 024 är skriven i loop 1 med den
uppmätta H-10-domen (golvet var redan uppfyllt: 95,5 %) men står utanför R7; 025 tillkom ur
leadens R6-fynd och 026 ur Astras kodläsning.
a11y-skulden (dubblerade h3, hero-alt, DOM-ordning, forced-colors) står kvar i
`.impeccable/a11y-debt.md`.

## Grindar och verktyg för lead i R6

- **Stängt:** `assets/demo-calyx-1440.webp` omkodad av lead till 1076x606 gråskala under
  60 kB (perf 6); sidvikt ska mätas ≤ 425 kB efter R6.
- **Plan 011:s H-17/H-18** (critic 8): `scroll_verify.py` vid 1440 och 390 på R6-läget;
  statisk svans ≤ 700 px, vändning 1 300 till 1 600 px.
- **`motion_probe.py`** läser ren `scale()` som DEAD (atan2 på b=0 faller till
  translation); `.giant` och `#threadFill` ska mätas med matrisläsning tills proben
  smalnas av. `scroll_verify.py` nedskalar till 64x36 innan diff och rapporterar en
  gles ritning som dead scroll (R5 bevisade det med `deadcheck-*.png`); båda är
  verktygsskuld, inte sidans.
- **`contrast.py`** har URL hårdkodad (rad 77); `contrast_over_media.py --url` används.
- **Kontrollprotokollet** (kontrollen ren omedelbart före varje mätning) gäller varje
  probkörning i R6; perf-rapporten kasserade två av sex kontroller.

## Tidigare planer

| # | Titel | Status |
|---|---|---|
| 001 till 008 | R4 | byggda, granskade R4 |
| 010 | Processakten | byggd R5; **superseded** av 019 och 020 (fotnot i filen) |
| 011 | Kortvändningens span 3,4 | byggd R5; H-17/H-18 mäts av lead i R6 |

fix

## persistence

Codex `gpt-6-astra` (CLI 0.154.0, `model_reasoning_effort=medium`) kördes av arkitekten
2026-09-17 01:04 till 01:14 UTC (9 min 34 s, inom tio minuter) med 96 bilder bifogade i
ordning (`shots/loop-1/`: 11 + 13 helsidesskivor, 12 + 12 previews, 12 + 12 flip-ramar,
12 + 12 processramar), HELHET.md i sin helhet, femsektionskontraktet, invarianterna (F-011,
motorn, `--sc-ps`, gate 75, låst copy, `sites/*`) och de sex frågorna. Prompt och rå
utdata: scratch `astra-prompt.txt`, `astra-out.txt`.

Astra svarade `rebuild` med åtta material_fixes och en H-radstabell för alla 35 rader.
Arkitekten verifierade varje fynd mot filen (`index.html`, md5 `424cdd46`) och bilderna:
**sju av åtta tagna** (tre av dem korrigerar arkitektens egna planer eller HELHET:s
arithmetik), **en delvis förkastad** (helbreddsomkompositionen av bandet är ett
målbildsbeslut, inte ett kodfel; går som fråga Q30 till Anton, inte som R7-plan), och av
tabellens 35 rader **fyra förkastade** (H-04 process-spalterna, H-07 glyfhöjd, H-29
`pathLength` på wipe-element, H-33 måttens skala) med skäl i fidelity.

Dispositionen sänks från `rebuild` till `fix`: kontraktets `rebuild` betyder "koden är
osund i grunden", och heron, processakten, tokens, motorn och shimen står (Astras eget
`keep` säger detsamma). Det Astra kallar rebuild är bandets komposition (H-02/H-03), en
akt, inte grunden.

Från R6 överlevde: plan 018 till 023 (ramarnas viloläge, prosa i flödet, arkets geometri,
kontrast, fokus, liggartråden), bekräftat i pixlarna (`slices-1440/…--s06..s09`,
`preview-*-process-*`).

## fidelity

Koden gör vad BRIEF.md säger (aktsekvens, `?preview=`-lägena, device-tabellen) med tre
avvikelser som Astra fann och arkitekten bekräftade:

1. **`display:contents` och `.col > * + *`** (index.html:509, 512): selektorn matchar DOM,
   inte layout, så plan 012:s antagande "träffar inte längre under 900" var fel; efter 017
   skulle panelerna få 160 px extra marginal vid 390. Plan 012 nollar nu marginalen.
2. **Dwell är en mittremapp** (`scroll/scrollcraft.js:159`), inte en hållning i slutet.
   HELHET § 2:s tabell (655 px svans, 1 469 px vändning) räknade fel; med kurvan blir
   vändningen 1 602 px och svansen 393 px. H-17 håller, H-18 ligger 2 px över sitt övre tal
   (inom tolerans). HELHET § 3 rättad.
3. **Ramarnas montering** (index.html:1547-1550, 1566-1575): dubbla idle-callbacks ger
   `f.src = null` (`/null`), och en ram som lämnar 40 %-zonen före monteringen sover inte.
   Verifierat i koden, inte återspelat i webbläsaren; plan 026 återspelar före/efter.

Pixlarna, skärm för skärm (1440, `slices-1440/`): s00 fold matchar; s01 kortet på kant
matchar; s02 baksidan matchar (halvtom, 016); **s03 avviker**: tes och jätterubrik
toppalignade och lika tunga, slitsar av rå grund (017); **s04 avviker**: Calyx + Hōrai-iris
utan dominant; **s05 avviker**: pris (hål) + Hōrai + tomt papper, kickern vid x 0 (013,
025); s06 till s08 matchar (arket dominerar, måtten i accent, Calyx maskad); **s09 avviker**:
steg 07 + arkets kapade kant + principerna vid x 0 (025); s10 matchar delvis (avslutet
utan rörelse, delar viewport med principerna: 015). 390: **s03 till s06 avviker** i ordning
(012), **s07 avviker** (tomt fält 500 px, 025), s08 till s12 matchar.

Previews: `process-01..06` vid 1440 läcker steg N+1:s första bana; vid 390 står steg N+1:s
rubrik under arket i alla sju (025 B). Flip-ramarna: kontinuerlig geometri, kanten 2 px vid
90° (024, utanför R7). Processramarna 390: arket 606 px in i viewporten före första linjen.

Astras H-radstabell mot arkitektens bockar:

| H | Astra | Arkitekten | Dom |
|---|---|---|---|
| H-01, H-10, H-26 | met | [x] | överens |
| H-02, H-03 | not met | [ ] | överens; helbreddsomkompositionen är Q30, inte R7 |
| H-04 | not met + "process-spalterna kräver tolkning" | [ ] | tagen för bandet; **förkastad** för processakten: text + sticky ark är rail-och-innehåll (label-rail-anatomi), inte parade innehållsspalter |
| H-05 | 144 px < 160 | [ ] | **tagen**: 017 höjd till 160 px (luft) på båda seams |
| H-06 | partial | [x] | arkitekten står: sex anatomier finns; sekvensen är H-02:s fråga |
| H-07 | "font-size är inte glyfhöjd" | [ ] | **förkastad**: HELHET:s konvention är teckenstorlek (H-07:s "~80 px i dag" = 76,8 px font-size; Hoys 100 till 132 är teckenstorlekar) |
| H-08, H-09, H-11, H-14, H-19 | not met, planer finns | [ ] | överens (013, 016, 012, 017) |
| H-12 | 62 svh isolerar inte | [ ] | **tagen**: 015 till 100 svh, linjen 0 till 0,46, träffyta 44 px |
| H-13 | 17 %, mål 101 px | [ ] | överens, loop 2 |
| H-15 | processentré + principernas högra halva | [ ] | tagen för entrén (025 B); **förkastad** för principerna: en 64ch-liggare på papper är ett mått, inte en öppen spalt |
| H-16 | inte certifierad ur stillbilder | [x] | arkitekten står: `scroll-verify` körd, banden förklarade |
| H-17 | 393 px | [x] | **tagen**: HELHET rättad (Astras tal) |
| H-18 | 1 602 px | [x] | **tagen** som tal, bockad inom tolerans (2 px) |
| H-20 | partial | [x] | arkitekten står: mätt vid `--sc-ps` 1 (`diag2`), 103 px, kollisionen tas i 017 D |
| H-21, H-22, H-23, H-32 | not met | [ ] | överens; bildtiden är loop 1:s största öppna post, ingen R7-plan (se material_fixes 3) |
| H-24, H-34 | unverified | [ ] | överens |
| H-25 | priset saknar device | [ ] | överens, loop 2 |
| H-27 | wrapperns klipp reverserar | [x] | tagen som observation: engine-reveal på `--sc-p` reverserar vid scroll uppåt; ramen rörs inte, wrappern gör det. Egen plan i loop 2 (sidans egen latch på `--sc-ps`), inte R7 |
| H-28 | rå progress kan släcka gruppen | [x] | **tagen**: 025 B4 (hysteres) |
| H-29 | `pathLength` saknas på wipe-element | [x] | **förkastad**: `wipe` (streckade hjälplinjer, skraffering, revisionsfält) avslöjas med `clip-path` per plan 010 eftersom dash-draw inte kan rita en redan streckad linje; H-29:s "alla" gäller `draw`-banorna |
| H-30 | not met | [ ] | överens (025 B) |
| H-31 | prosa | [x] | överens |
| H-33 | "7 REM" ritas 64 px | [x] | **förkastad**: arket är en skalritning av en 1440-sida (viewBox 880 = 1440, skala 0,938 vid 825,6 px); måtten är sidans, som på en ritning i 1:1,75, inte pappersytans. R6:s flagga står som dokumenterad skala |
| H-35 | sticky-arket vid låga viewports, 44 px på footerlänken | [x] → [ ] | **tagen**: 025 D och 015; H-35 öppnas igen |

## ceiling

- insign: allt innehåll läsbart vid varje offset; V3c:s processentré (tom skärm) och
  390-arket som täcker texten bryter det till 025 är byggd.
- highwaymedia: sekvensen läses som framsteg före detaljerna; V3c:s ritning ligger efter sin
  text (025 B).
- hoy: helbredds grundbyten och en auktoritet per kapitel; V3c:s band har två lika tunga
  spalter (017 lindrar, Q30 avgör).
- K3: en ritning, ett koordinatsystem; V3c:s 390-plansch behöver samma konsekvens (025 D
  begränsar arket, skalan står i ledgern).

## material_fixes

1. **Processaktens rail, ankare och hållning** (index.html:881-883 `padding` ogiltig via
   odefinierad `--panel-pad-y`; :1139 kickern utan `--rail-x`; :1455-1456 fönstren
   överlappar vid 1440 och `--eN` har fel tecken vid 390; :1515 rå progress släcker
   gruppen; :733/746 steg 07 utan hållning; :891-893 arket 564 px högt vid 640 px viewport).
   Bilder 10, 11, 19, 30 till 35, 42 till 48, 86 till 87. Mål: `paddingLeft` = `--rail-x`
   på båda papperssektionerna; preview N visar bara steg N; `--s(N+1) > --eN`; arket
   lämnar ≥ 200 px text vid 640 px höjd. **Plan 025 (A till D).**
2. **Bandets seams och offset till H-05:s riktiga golv** (index.html:505-509): 160 px luft,
   inte 96/120 (Astra fix 1, andra halvan); grunddriften (`:245`); bleeden 33 % med rännan
   58 px (`:560`, `diag2`: 103 px överhäng men 9 px in i rubriken). **Plan 017.**
3. **Bildtiden är fortfarande sidans största brist** (H-21/H-22/H-32): cpu 4 hero p95
   217 ms (115 rutor), `#process` 446 ms (120 rutor, staircase 1); cpu 1 hero 35,8 ms
   (26 rutor). Samma rotorsak sedan R4 (RecalcStyle mot `--kN`-kedjan och `.ground`). Ingen
   R7-plan: kräver en egen profileringsrunda (loop 2, första plan) med `perf_probe`-attribuering
   före någon ändring. Målet är HELHET H-21, inte en gissning.
4. **Mobilordningen med marginalnollning** (index.html:509-515): `display:contents` matchar
   fortfarande `.col > * + *`; `margin-top:0` i blocket. **Plan 012 (rättad).**
5. **Avslutet äger sista viewporten** (index.html:919-928, 1354-1356): 100 svh, linjen
   0 till 0,46, mailto 2rem till 6rem med `min-height:44px`. **Plan 015 (rättad).**
6. **Ramarnas montering idempotent** (index.html:1547-1550, 1566-1575): en navigering per
   ram, sömn även för en ram som lämnade före luckan. **Plan 026 (ny).**
7. **Prisblockets material och kortbaksidan** (index.html:130/627, 399/441-443/995-996):
   `--c-graphite`, A-glyfen i `--frame-line`. **Planer 013, 016** (oförändrade, Astra:
   "retain").
8. **Helbreddsomkomposition av bandet (H-02/H-03)**: Astras fix 1, första halvan.
   Verifierad som brist mot golvet (bilder 4 till 6: tre akter i ett band), men det är en
   ändring av målbildens s4 till s6 (BRIEF § STORY: två spalter som byter material), inte
   ett kodfel. **Q30 till Anton** (`QUESTIONS.md`): stapla tes, Calyx, jätterubrik + liggare,
   Hōrai och pris som fem helbredds akter med egna grundbyten, eller behåll bandet med 017:s
   luft och offset. Byggs i loop 2 om ja; 017 och 012 är inte bortkastade i något av fallen.

Wrapperns reveal på `--sc-p` som reverserar (Astra fix 8) tas som observation (H-27-not),
plan i loop 2 efter Q30, eftersom en omkomposition ändrar vilka wrappers som finns.

## keep

Kortet som fysiskt objekt med tjocklek och parabel, den kontinuerliga fotografiska grunden
med `contain:strict`, radie 0, en accent i två roller, de tre levande sajterna som bevis, det
kumulativa arket i sju tillstånd med tolv namnbara banor och Calyx som maskad bild, de sju
prosastyckena (copy v1, låsta för loopen), `--sc-ps`-kontraktet (staircase 0 på alla
hero-spår i båda riktningarna och båda kadenserna), `@property`-raderna, `pathLength="1"` med
`*1px`, ramarna `inert` + `pointer-events:none` + `content-visibility` i vila, `<ol>` med
text i DOM, reveal på wrappern, skärmarna 05 och 06 i akten (bilder 80 till 81) som redan
läser som målbilden. Inga nya färger eller element behövs utöver `--c-graphite` (013) och
`--panel-pad-y` på `.principles` (025); Astra föreslog inga heller.

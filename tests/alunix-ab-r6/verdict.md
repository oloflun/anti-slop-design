# Alunix r6 — verdict (Claude, pixlar och loggar; utan favorit)

Boarden: `http://127.0.0.1:4624/board.html` (launch: `alunix-board-r6`). Motorerna heter `1` och `2`
och är slumpade per koncept; `python tests/alunix-ab-r6/run.py reveal` visar mappningen efter ditt
omdöme. Det här dokumentet är skrivet med armarna synliga, så läs det **efter** boarden om du vill
döma blint.

## 1. Vad som faktiskt kördes

| Cell | Arm | Varv | Kostnad | Tid | Skill-anrop | Hook-händelser | Referenser lästa | Bilder lästa | Unsplash |
|---|---|---|---|---|---|---|---|---|---|
| A-K1 | native | 101 | $9.85 | 32 min | 0 | 0 | 0 | 42 | 4 anrop |
| A-K2 | native | 71 + 22 | $17.50 | 36 + 14 min | 0 | 0 | 0 | 27 | 3 |
| A-K3 | native | 58 | $8.51 | 26 min | 0 | 0 | 0 | 27 | 3 |
| B-K1-nogate | kedja, gate uteblev | 79 | $9.70 | 34 min | 0 | 55 | 0 | 40 | 2 |
| B-K1 | kedja, gate aktiv | 23 + 73 | $13.00 | 9 + 15 min | 4 (`design`, `humanizer-svenska`, `emil-design-eng`, `imagegen-frontend-web`) | 68 | **0** | 29 | 2 |
| B-K2 | kedja | 83 | $10.75 | 34 min | 1 (`design`) | 49 | **0** | 29 | 3 |
| B-K3 | kedja | 78 | $9.01 | 26 min | 1 (`design`) | 47 | **0** | 35 | 3 |

A-K2 avbröts av användningsgränsen efter 71 varv (index.html fanns, NOTES.md saknades) och
fortsattes i samma session (`--resume`, samma flaggor) i 22 varv till. Kostnaden är summan.

Modell `claude-fable-5-1`, effort `high`, i alla sju processer (bekräftat i init-raden och
transkriptens `effort`-fält). Prompten identisk (sha256 i README), tre platshållare per cell.

**Kedjebytets bevis.** Prov A (`probes/A.jsonl`): `skills: []`, `plugins: []`, inget Skill-verktyg,
0 hook-händelser, ledgern orörd. Prov B2 (`probes/B2.jsonl`): pluginet `anti-slop-design` laddat,
`Skill(design)` som första anrop, route-hook efter varje Write/Edit, stop-hooken blockerade tills
rapport skrivits, 13 ledgerrader. Arm A-cellernas init-rader: 0 skills, 0 plugins. Arm B:
`anti-slop-design` + 4 övriga plugins, `super-intelligence` (cachen) avstängd.

## 2. Tre kedjefynd som testet tvingade fram

1. **`NEGATIVE_GUARD` tystade gaten för hela arm B.** `design_hook_lib.classify()` returnerade
   `none` för byggprompten eftersom ordet `commit` ("Ingen commit.") förekom, och `none` för
   provprompten eftersom `skills` förekom. Ett enda ord ur negativlistan, var som helst i en
   110-raders brief med verb + objekt + UI-bevis, nollade allt. B-K2 och B-K3 laddade `design`
   ändå (skillens beskrivning räckte för modellen), B-K1 gjorde det inte och byggde utan kedjan.
   Fix (efter att arm B var klar, inte under): negativlistan avgör bara tveksamma prompter
   (`hooks/design_hook_lib.py`, `classify`). Korpusen `tests/intent_corpus.jsonl` 42/42 efter
   fixen, två nya rader. B-K1 kördes om med gaten aktiv (`probes/`-loggen visar `<design-gate>` i
   hook-svaret och `Skill(design)` som första anrop); första bygget sparat som `runs/B/K1-nogate/`.
2. **Skillen laddades, referenserna lästes aldrig.** B-K2 och B-K3 läste noll filer under
   `~/.agents/skills/design/references/` efter `Skill(design)`, och anropade ingen annan skill:
   ingen `copywriting`, ingen `copy-editing`, ingen `humanizer-svenska`, ingen `design-verify`,
   ingen `a11y-audit`, inga kritikeragenter. B-K3 skriver det själv i sina anteckningar:
   "Kopiepassen kördes inte som skills; de få egna raderna lästes för hand mot deras regler."
   Stop-hookens route gap-rapporter från de här sessionerna säger samma sak. Kedjan var alltså
   "på" i betydelsen SKILL.md i kontext + hookar vid skrivning, inte i betydelsen hela
   procedurkedjan. Det är inte ett mätfel; det är hur kedjan beter sig på Fable high i headless
   läge med en fullständig brief.
3. **Två praktiska hinder utanför kedjan.** npm-CLI:n (2.1.241) avvisar Fable; skrivbordsappens
   2.1.260 användes. `--plugin-dir <repo>` laddar ingenting eftersom manifestet har
   `defaultEnabled: false`; ett skal med manifestet utan flaggan + junctions till `hooks/` och
   `agents/` löste det (`run.py plugin_shim`). Båda dokumenterade i README.

Plus ett fynd om byggmiljön som alla sex agenter hittade oberoende: `python -m http.server`
(HTTP/1.0) tappar WebP-svar mot Chromium på den här maskinen; fyra av sex skrev en egen
HTTP/1.1-server, två la in omhämtning på bilder. Prompten pekade på `http.server`; det bör bytas.

## 3. Mätvärden per cell (min fångst, `review.py` + `scroll_verify.py` + `a11y_scan.py`)

| Cell | Överflöde 320/390/768/1440 | Ramar med titel | Konsol | Dött scroll | Blanka band | Cues ej fulla | axe |
|---|---|---|---|---|---|---|---|
| A-K1 | 0/0/0/0 | 1/1 | ren (Hōrais Tailwind-varning) | 2 segment (ramen i helskärm) | 1 (pinnad hero) | 0 | 0 |
| A-K2 | 0/0/0/0 | 3/3 | ren | 3 (första 13 vh avsiktlig stillhet) | 2 (pinnad hero, mörkt avslut) | 0 | 0 |
| A-K3 | 0/0/0/0 | 2 live + 2 lata | ren | 3 (Hōrai-scenens slut) | 1 (pinnad scen) | 0 | 1 serious (`link-name` på loggalänken) |
| B-K1-nogate | 0/0/0/0 | 1/1 | ren | 4 | 2 | 1 | ej skannad |
| B-K1 | 0/0/0/0 | 1/1 | ren | **0** | 1 (pinnad hero) | 0 | 0 |
| B-K2 | 0/0/0/0 | 3/3 | ren | 1 | 2 | 0 | 0 |
| B-K3 | 0/0/0/0 | 4/4 | ren | **0** | 1 (pinnad scen) | 0 | 0 |

"Blanka band" i pinnade akter är fångstens artefakt (en pinnad scen kan inte fotograferas i en
helsidesbild); alla agenter noterade det själva. Dött scroll räknas i 300 px-steg där bilden inte
ändras; i K1 är det ramen som fyller skärmen (Hōrai får användas), i K2 en avsiktlig stillhet.

## 4. Koncept för koncept, A mot B (på pixlarna)

### K1 Skymning

Båda hittade **samma foto** (Julian Terenzio, Riddarholmen i blå timmen, `5UDPVmIdXUo`) ur samma
sökning, båda satte en ljus serif i himlen med guldstreck under `visitkort`, båda avslutar på
en nattbild med `kontakt@alunix.se` i stor grad. Skillnaderna är hantverk:

- **A-K1** har en renare första skärm (loggan inline i toppraden, bevisraden i vattnet). Fönstret i
  fasaden tänds först när man scrollar (agenten såg det som en gul lapp i vila och rättade).
  Mellanläget i zoomen är svagast: plåten läses som en rektangel i en uppförstorad fasad, inte
  som ett fönster. Vita bevissektionen: tre uppslag, skärmbild glider från sin sida, text från
  motsatt. 42 lästa skärmbilder, fyra rättningsomgångar i anteckningarna.
- **B-K1-nogate** har Hōrai-plåten synlig i fasaden redan i vila (den bugg A rättade) och loggan i
  en vit kvadrat uppe till vänster. Bevisraden nere till höger med kickern
  `TRE EXEMPELSIDOR, BYGGDA AV OSS` (ett påstående mer än briefen). Vita sektionen använder
  serif-rubriker (`Utveckling`, `System`) i stället för grotesk, vilket ger ett lugnare, mer
  redaktionellt mellanparti. En cue som aldrig når full opacitet i `scroll_verify`.
- **B-K1 (gate aktiv)** är den mest egna av de tre K1-byggena: ett annat foto (Rafael Peier,
  Skeppsholmen/Strandvägen i skymning), rubriken **vänsterställd i fotots mörka vattenband** med
  guldstreck, bevisraden under underraden, loggan liten i toppraden. Fönstret i fasaden syns
  dock redan i vila (samma sak som B-K1-nogate; A-K1 rättade den). Efter klippet: cream i
  stället för hårt vitt, `VI BYGGER ERT VARUMÄRKE.` i serif, gyllene serifnumeraler 01–03,
  skärmbild bredvid varje tjänst, `Alla har rätt till bra design.` i serif, nattlandning med
  adressen i display. Noll dött scroll, noll cues som fallerar, axe 0. Gaten gjorde skillnad i
  **procedur**: fyra skills laddade i stället för en, och anteckningarna redovisar
  `emil-design-eng`-passet (namngivna transition-egenskaper, reduced motion) och
  `humanizer-svenska` på de egna strängarna. Referenserna lästes ändå inte.

### K2 Affischen

Här skiljer sig armarna mest.

- **A-K2** gör exakt det målbilden beskriver: ALUNIX i 300 px+ på salviapapper, Calyx **genom**
  bokstävernas räknare (masken står, bilden bakom glider), klocka som går i toppraden, uppslag
  med levande ramar som går från gråskala till färg, liggare 01–03, priser, mörkt avslut med
  `Alla har rätt till bra design.` i affischgrad. Mobilen håller. Den enda avvikelsen från
  målbilden är att avslutet inverterar till ett mörkt band i stället för att krympa till minsta
  typen; det är ett bättre beslut än briefens.
- **B-K2** har samma papper, samma tunga grotesk, samma klocka, men bokstäverna ligger **ovanpå**
  en levande Calyx-ram (svart typ över sidan) i stället för att fönstra den; panelen bakom
  bokstäverna täcker U/N/I/X och A står på papper, så "fönstren" blir ett överlapp. Rubriken
  `Er hemsida är nutidens visitkort` står som fet lässtorlek uppe till vänster i stället för
  som en av sidans två grader. Numeralerna 01/02/03 i affischgrad är sidans starkaste akt.
  Avslutet är samma mörka band som A:s. Anteckningarna är utförliga (nio lästa skärmbilder,
  sju rättningar) men signaturen är inte den som beställdes.

### K3 Konsolen

Jämnast. Båda: skrivbordsfoto, glaskort som läser Hōrais sektion och procent, pinnad scen där
scrollen styr ramen, dragspel som byter ram, typsatt pristabell, riktigt fält mot mailto.

- **A-K3**: tyngre oskärpa på fotot (bokeh, läses mer generiskt), kortet som chip i toppraden
  efter släppet, chip på mobilen med mätare. Tre dödsegment i scrollen där Hōrai-scenen är slut.
  Ett axe-fel: loggalänken saknar tillgängligt namn i något läge.
- **B-K3**: ljusare foto med fönster och lampa, svagare slöja, kortet med `LIVE`-märke och blått
  procenttal, flikar med understrykning. Öppnar med **två knappar** (`Provkör en exempelsida`,
  `Se paketen`), en klassisk SaaS-hero-rörelse som målbilden inte bad om ("ingen knapp i heron"
  stod i K1, inte i K3, så det är tillåtet men inte begärt). Noll dött scroll, noll cues som
  fallerar, fyra ramar med titel. Anteckningarna redovisar ärligt att kopiepassen inte kördes.

## 5. Fingerprint (sex dimensioner) per cell

| Cell | Grammatik | Toppbar | Första skärm | Aktsekvens | Avslut | Signatur |
|---|---|---|---|---|---|---|
| A-K1 | filmic one-shot | fast, transparent, mörk botten över ramen | fullbredd skymning, centrerad ljus serif, bevisrad i vattnet | stillhet → zoom → ram → vitt (3 uppslag) → priser → natt | nattbild, adress i display | kamerazoom in i fönster som är Hōrai live |
| B-K1-nogate | filmic one-shot | fast, logga i vit ruta | samma foto, spärrat ALUNIX ovan, bevisrad höger | samma | samma | samma zoom, plåt synlig i vila |
| A-K2 | typographic poster | tunn rad, klocka | ALUNIX 324 px, Calyx genom räknarna | byte → andning → uppslag → liggare → pris | mörkt band, affischgrad | bilden bakom masken glider; blocket andas isär till rubrik |
| B-K2 | typographic poster | tunn rad, klocka | ALUNIX över Calyx-ram | byte → andning → uppslag → 01/02/03 → pris | mörkt band | panel bakom bokstäver, plåt gråskala → färg |
| A-K3 | live surface | app-chrome, chip efter släpp | foto + glaskort, ingen knapp | pin → släpp → dragspel+ram → tabell → fält | fält + `Alla har rätt…` liten | scroll styr ramen, kort läser telemetri |
| B-K3 | live surface | app-chrome, understruken flik | foto + glaskort + två knappar | pin → släpp → dragspel+ram → tabell → mörkt fält | mörkt band med fält | samma, tvåvägssynk ram ↔ sida |

Mot r5 V3b (kontinuerlig grund, konsolkort i vänsterspalt, inramad plåt, ordscrubb, prisruta):
alla sex skiljer på ≥ 4/6.

## 6. Unsplash

Nyckeln i `~/.secrets/.env`, verifierad 200, demo-läge (50 anrop/h). Alla sju processer höll sig
under taket på 12 (2–4 anrop var); tre av dem valde samma sökning och två samma foto. Alla sju
anropade download-endpointen före hämtning och krediterade fotografen. Produktionsansökan hos
Unsplash lyfter gränsen till 5 000/h; det är Antons sak.

## 7. Det ärliga omdömet om testet självt

- Kedjan (som den faktiskt beter sig) gav **inte** en mätbar kvalitetsskillnad i K1 och K3, och
  i K2 var den native-cellen närmare målbilden. Det som skilde var enskilda agenters
  hantverksbeslut, inte armen.
- Anledningen är fynd 2: skillen laddades men procedurerna kördes inte. Testet mäter alltså
  "SKILL.md i kontext + hookar vid skrivning" mot "frontend-design i systemprompt", och där är
  skillnaden liten. Det är ett resultat om **kedjans ingrepp**, inte om dess innehåll.
- Vad som skulle ge ett annat test: en arm B där hookarna *tvingar* Step 5/6 (stop-hooken
  blockerade ju faktiskt B2-provet tills rapporten fanns, men inte bygget, eftersom bygget
  läste bilder), eller en arm B med kritikertrion inkopplad som subagenter. Det är nästa
  experiment, inte det här.

## 8. Vad som inte gjordes

- **Kritikertrion kördes inte.** Fem `design-critic`-agenter (Fable) startades på de färdiga
  cellerna och dog alla på användningsgränsen (429) innan de levererat. De togs inte om: de
  konkurrerar om samma kvot som byggena, och min egen pixelläsning plus mätvärdena ovan täcker
  det som planen bad kritikerna om. Vill du ha dem ändå går de att köra på sex celler i en
  omgång när kvoten är fri (~$2–4 per cell).
- **Fingerprintrader** har inte lagts i valvets register (`design-fingerprints.md`); tabellen i
  § 5 är underlaget om något av de sex ska vidare.
- **Ingen commit, ingen push** (Antons regel). `git status` visar bara r6-filerna, Unsplash-
  skripten, guard-fixen, korpusraderna, `board.py`-spegeln, `launch.json` och `.gitignore`.

## 9. Om B-K1 mot B-K1-nogate: vad gaten faktiskt köpte

Samma prompt, samma modell, samma flaggor, en enda skillnad: gaten injicerad eller inte.
Med gate: fyra skills, ett eget foto, ett ärligare mellanparti (cream, serif, numeraler), noll
dött scroll. Utan gate: samma foto som arm A, plåten synlig i vila, loggan i en vit ruta, en
cue som aldrig når full opacitet. Det är den tydligaste enskilda effekten av kedjan i hela
testet, och den kom av en rad hooktext, inte av referenserna.

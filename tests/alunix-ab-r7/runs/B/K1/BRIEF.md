# K1 Skymning — BRIEF, runda 1 (referenspaket, ingen kod)

Arm B, koncept K1. Skriven efter läsning av 43 filer/bilder enligt uppdragets ordning
(fullständig lista i sammanfattningen längst ned). Ingen HTML/CSS/JS skriven. Riktningen
är låst av orkestrerarens målbild (`tests/alunix-ab-r7/concepts.md` § K1 Skymning v2); den
här briefen preciserar den till en byggbar spec och fyller i reference-lock,
grammatik/känslokurva/enhetstabell och fingerprint som `design/SKILL.md` Step 2b kräver.

---

## 1. Referensdigest

Tre rader per fil: vad den säger som spelar roll här · vad jag tar med · vad jag avvisar
och varför.

**SKILL.md** (Step 0, 1, 1b, 2, 2b, 4, § Motion)
Säger: auktoritet-först-disciplinen, fyra-tiers-grinden, att Step 2b:s fyra första punkter
är obligatoriska även när riktningen är låst, att set-piecet ska ha ≥2 koordinerade lager
och ett `?preview=`-nav. Tar med: hela arbetsordningen nedan följer exakt detta recept.
Avvisar: inget — det här är kontraktet, inte ett smakval.

**TASTE.md**
Säger: en auktoritet per sida (§1), tyst typ på starkt foto vid vikt 300 (§2.1), ett
papper-en-accent (§2.2), skala 5–15× (§2.4), rörelse bara där typ/bild är tysta utom i
set-piece-akten där rörelsen själv är auktoritet (§4.8-preciseringen). Tar med: hela
strukturen för K1 — fotot bär, typen viker till 300 i vattnets mörka band, en enda
kromatisk accent, rörelsen tar över just i akt 2–3. Avvisar: ingenting av innehållet, men
noterar att §4.8-preciseringen är den rad som gör set-piecet tillåtet över huvud taget —
utan den hade regel 8 lästs som ett förbud mot hela idén (precis det F-007 varnar för).

**FEEDBACK.md** (F-001 till F-009)
Säger: reservläget måste bära sekvensen som egna sektioner (F-001), målets vilostatus får
aldrig förhandsvisa slutläget (F-002), en auktoritet gäller även när typ bär (F-003, K2),
glaskort/telemetri är förbjudet (F-006, K3), avvikelse från målbilden stoppar rundan
(F-007), referenser måste faktiskt läsas (F-008). Tar med: F-001 och F-002 är bindande för
K1 specifikt (kap. 9 nedan); F-007 betyder att signaturaktens beskrivning i den här briefen
måste matcha målbildens ordval, inte min egen tolkning. Avvisar: F-003/F-004/F-005/F-006 är
K2/K3-poster, refereras men styr inte K1:s beslut direkt.

**reference-lock.md**
Säger: tier-oberoende lås, en dominant referens, 1–2 lånade detaljer, anti-averaging-testen
(identitet/redaktionell/skärmbild), token-roll-bevarande. Tar med: hela formatet i kapitel
3 nedan, plus de tre anti-averaging-testen körda i kapitel 3. Avvisar: temakatalogen
(`themes/`) — inte aktuell, det här är inte Tier 3.

**house-physics.md** (Structural, Motion)
Säger: exakt en mättad accent i displayskala, hårlinjer utan skugga, set-piecets mål är
tyst i vila och tänds vid första scroll, reduced motion visar formade lägen som egna
sektioner. Tar med: målets tysta-i-vila-regel styr kapitel 9 direkt; hårlinje-liggaren i
akt 5 i stället för kort. Avvisar: kicker-mikroformatet och grain film är
editorial-print-invarianter (Calyx/Hōrai/Hyperborea) — K1 är cinematic dark men inte print,
så ingen kicker-rad läggs på sidan bara för att den finns i huset.

**scroll/README.md**
Säger: scope-regeln (Persuade-sidor kräver ≥4 enhetsfamiljer, aldrig samma två i rad, ett
signaturdrag), motorn är opt-in per grammatik. Tar med: eftersom akt 2/3 kräver scrub+pin
används motorn (`scripts/scroll/`), kopierad oförändrad. Avvisar: inget.

**scroll/grammars.md**
Säger: åtta grammatiker, registrets passform per grammatik. Tar med: filmic one-shot är
raden för cinematic dark + hospitality/launch-liknande argument, se kapitel 4 för varför de
andra sju förlorar. Avvisar: chaptered editorial (K1 har inga kapitel att bläddra i),
gallery/catalog (exempelsajterna är bevis i en linjär kurva, inte ett rum att gå runt i).

**scroll/devices.md**
Säger: nio enheter, cue-kontraktet (greet på hero, hold bara på sista akten, ground-or-greet,
aldrig samma familj två gånger i rad). Tar med: hela enhetstabellen i kapitel 7 bygger
direkt på den här filens regler, inklusive fällan "bara sista akten får hålla" som styr att
akt 3:s cue måste vara tvåvärd trots att fönstret känns som en kulmen.
Avvisar: `magnet`/`spotlight`/`tilt` — inga pekarenheter i K1, ingen CTA-knapp att magnetisera.

**scroll/feel-and-fingerprint.md**
Säger: känslokurvan skrivs före akterna, en topp får resten av budgeten, tell-someone-
testet, fingerprint-grinden (≥4 av 6 mot varje rad). Tar med: hela kapitel 5, 6 och 8.
Avvisar: inget, men registret `VAULT/wiki/.../design-fingerprints.md` ligger utanför det här
repot och kunde inte läsas — se öppen fråga i kapitel 12.

**scripts/scroll/NOTE.md**
Säger: motorn kopieras byte-identisk, temas via sex tokens + två typsnitt, signaturdrag
skrivs i sidans egen CSS/JS mot `--sc-p`, aldrig i motorfilen. Tar med: temavariablerna i
kapitel 11 är exakt de sex + två filen namnger. Avvisar: ingen egen ändring av
`scrollcraft.js`/`.css` någonsin.

**scripts/scroll/template.html**
Säger: skelettets aktordning är ett exempel, inte en mall att kopiera rakt av; regler som
överlever: ≥4 familjer, aldrig samma två i rad, ≤2 scrub, sista elementet på sidan är
avslutningsakten. Tar med: exakt datastruktur för `data-sc-act`, `data-sc-cue`,
`data-sc-stage` som specen i kapitel 7 skriver mot. Avvisar: skelettets konkreta sex akter
(recognition/tension/turn/substance/range/commitment) kopieras inte — K1 har sin egen kurva.

**concepts.md § K1 Skymning v2**
Säger: den låsta målbilden i sin helhet — auktoritet, idé, akter, förbjudet, fingerprint,
målbildsgrind. Tar med: hela idén, ordagrant där den ger exakta tal (span 2,6, span 2,4
existerar inte här utan bara i K2, drift ≤2 % skala, 60 vh pin). Avvisar: inget — det här är
låset, inte ett förslag; den här briefen preciserar utan att motsäga den.

**rogo/entry.md**
Säger: ett enda skymningsfoto bär rubrik + bevis i samma andetag, registret byter helt vid
fållen (mörkt/foto → vitt/plant), varje påstående bredvid en riktig skärmbild, betoning med
vikt i stället för kursiv. Tar med: hela registerbytet och alternerande skärmbildsraderna i
akt 4 är rakt härlett härifrån. Avvisar: logotypväggen (Alunix har inga kunder att visa —
skärmbilderna av Calyx/Hōrai/Hyperborea gör samma jobb utan att hitta på kunder), den vita
pillerknappen (K1 har inga knappar — auktoriteten är foto/typ), cookiepanelen som konkurrerar
med CTA:n på första skärmen.

**rogo/fold.webp**, **slices/00–07.webp**
Säger (som bild): rubriken ligger i himlens öppna band centrerat, inte i vattnet; registret
byter till ljusgrå/vit med en enkel serif-rubrik ("Helping finance teams…"), sedan
kundcitat i gråa rutor, sedan par av påstående + verklig skärmdump, sedan en svart sektion
med siffror ("50 000+", "150 000+") som liggare med tunna linjer, sist ett mörkt sidfotsblock.
Tar med: liggarformen för "By the numbers" (siffra vänster, etikett höger, hårlinjer mellan
raderna) är precis den form K1:s akt 5 (paketpriser) ska ha. Avvisar: kundcitaten med namn
och titel (fabricerade referenser är förbjudna för Alunix), plus-knappen för att expandera
loggor.

**rogo/extract/rogo-com-DESIGN.md**
Säger (mätt): h1 96px/400/128px, kroppstext 12px, en enda radie (6px), inga skuggtokens,
83 träffar Inter mot 43 Times New Roman mot 14 ABC Arizona Mix — dvs. även "seriffet" Rogo
är till största delen en sans-sajt med serif bara på display. Tar med: bekräftar TASTE §4.1
— tyst typ (här: en smal serif) bara på display, sans/grotesk gör allt registerarbete.
Avvisar: 6px-radien — K1:s "rundning är ett beslut"-regel (TASTE §2.5) landar på 0–2px, inte
Rogos 6px-default.

**groupemontoni/entry.md**
Säger: ordmärket står direkt på flygfotot utan platta bakom, bara storlek/spärrning håller
det läsbart mot den stökiga bilden under; mörkningen läggs bara vid textens nedre kant,
aldrig hela bilden; sourcade ESG-påståenden som fem-färgad mosaik. Tar med: principen att
typ kan stå rakt i fotot utan platta bakom — K1:s rubrik i vattnets mörka band gör samma
sak, inte centrerat som Montoni utan nere till vänster där bandet faktiskt är mörkt. Avvisar:
den centrerade uppställningen (K1:s foto har sitt öppna mörka band nere till vänster, inte
i mitten), räknarna i menyn (Alunix har inga verkliga driftsiffror att visa — skulle bli
påhittade), femfärgsmosaiken (K1:s palett är medvetet smal: två gråtoner, vitt, natt, en
accent).

**groupemontoni/fold.webp**, **slices/00–06.webp**
Säger (som bild): MONTONI i seriftyp, en vikt, centrerat direkt på flygfotot; scrollar man
vidare kommer mörka projektkort med mjuk gradient bara i nederkant och bildtext ovanpå;
sedan den flerfärgade ESG-mosaiken; sist en varm sidfot med nyhetsbrev och kontaktuppgifter
på riktig gatuadress. Tar med: gradient-bara-vid-textkant-principen till K1:s akt 6
(adressraden mot nattfotot ska ha mörkning bara där texten står, inte hela bilden). Avvisar:
projektkortgridet (K1 har inget kortgrid någonstans, per TASTE §2.3: hårlinjer och ton-på-ton,
aldrig kort).

**groupemontoni/extract/groupemontoni-com-DESIGN.md**
Säger (mätt): två typsnitt med strikta roller (studiopro 452 träffar mot fkroman 16 träffar
— fkroman är alltså strikt sparsam, bara wordmark/stora påståenden), spacing-bas 2px,
radie antingen 6px eller "full" (pillerknappar) — inget mellanläge. Tar med: bekräftar
"två snitt, rollerna korsar aldrig"-regeln kvantitativt: 452:16 är en extremt sparsam
andra-typsnitt-användning, exakt vad K1:s Newsreader-som-display/Schibsted-som-allt-annat
ska efterlikna i proportion. Avvisar: "full" (999px) pillradien — hör inte till K1:s
0–2px-beslut.

**r6 B/K1/NOTES.md**
Säger: fotot bär, rubriken låg i vattnets mörka band (uppmätt luminans 31/255) inte
centrerad, fönstret var Nationalmuseum-liknande fasad till höger i bilden, hela zoomen var
en CSS-transform-skalning av en enda stillbild (ingen video/bildsekvens), iframe:n blev
klickbar/scrollbar bara vid full skärm. Tar med: luminansargumentet för rubrikplacering
återanvänds rakt av (kapitel 3), och zoom-mot-fönster-idén i stort. Avvisar: CSS-transform-
zoomen som teknik — r7 v2 har en riktig genererad bildsekvens (`assets/push/`), vilket är
själva skillnaden fingerprint-grinden kräver (kapitel 8).

**r6 A/K1/NOTES.md**
Säger: samma grundidé byggd av en annan agent, med fönstret som tänds först vid scroll
(F-002:s "rätta" lösning enligt Antons dom), en `motion`-klass satt av JS så att reduced
motion aldrig börjar dolt, ett andra försök vid bildladdningsfel. Tar med: F-002:s lösning —
fönstret mörkt i vila, tänds vid första scroll — är precis vad r7 v2 kräver, och den här
körningen bevisar att mönstret redan fungerat en gång. Avvisar: `python -m http.server`
som testserver (dokumenterad trunkeringsbugg i båda r6-körningarna) — runda 2 använder
`scripts/serve.py` per uppdraget.

**assets/push/README.md**
Säger: 100 rutor à 10/s, genererade med Higgsfield (Kling 3.0) från `dusk.webp` som
startbild, `push-last.webp` är sista rutan, `push.mp4` är en all-intra-reserv. Orkestreraren
äger materialet. Tar med: sekvensen är motorns `canvas[data-sc-sequence]`-data för akt 2:s
scrub, `push-last.webp` är den bild reduced motion visar som formad slutstat. Avvisar: inget
— redan färdigt material, ingen ny bildkälla behövs.

**assets/credits.json**
Säger: fotograferna (Rafael Peier för dusk, Julian Terenzio för night) och att push/ är
Higgsfield-genererat. Tar med: exakt de här krediterna till sidfoten i runda 3. Avvisar:
inget.

**assets/dusk.webp** (bild)
Säger: Stockholms innerstad i blå timme, en byggnad med grönpatinerade torn/kupoler mitt i
bilden, en vit ångbåt förtöjd, vattnet mörkast nere till vänster, en ljus rosa-lila himmel
uppe till vänster — det öppna bandet för rubriken är alltså snarare vattnet nere till
vänster ELLER himlen uppe till vänster, inte mitten. Tar med: bekräftar r6:s luminansmätning
— rubriken hör hemma nere till vänster i vattnet. Avvisar: ingenting, det här är
källfotot.

**assets/push/push-last.webp** (bild)
Säger: en extrem närbild av ett tänt, välvt fönster i ljus sandsten med ett brunt
träfönsterbågverk och en glimt av en takrosett/ljuskrona i det varma ljuset innanför.
Tar med: det här är målets "formade" slutläge — exakt den bild reduced motion ska visa som
egen sektion (kapitel 9) och `?preview=window` ska tvinga fram (kapitel 10). Avvisar: inget.

**assets/night.webp** (bild)
Säger: en bredare, mörkare vy av samma stad senare på kvällen, med en spetsig kyrktorn-
silhuett och en lugn djupblå himmel utan moln — annorlunda kadrering än dusk.webp, inte
samma vinkel. Tar med: som landningsbild fungerar den ändå, eftersom akt 6 inte kräver
pixelkontinuitet med akt 1–3, bara samma stad, senare. Avvisar: inget.

**assets/demo-horai.webp, demo-calyx.webp, demo-hyperborea.webp** (bilder)
Säger: tre färdiga, olika skärmdumpar (Hōrai: mörk matbild med serifwordmark; Calyx: ljus
blombukett med serif "Botanical architecture,"; Hyperborea: mörk konferenssida med
"Systems with warmth"). Tar med: dessa är de riktiga skärmbilder akt 4:s tre uppslag ska
använda, redan i tre distinkt olika register vilket gör alternerande sidbyte (bild
vänster/höger) läsbart. Avvisar: inget, redan rätt material.

**Kontinuitetskontroll (utöver listan, gjord för att verifiera målbildens sekvensbeskrivning):**
`push/f001.webp` matchar `dusk.webp` pixel för pixel i komposition; `push/f050.webp` visar
kameran halvvägs in mot den ljusa, valvbågade fasaden till höger om det gröna tornet (inte
Nationalmuseum till namnet, men samma sorts belyst arkitektur som r6 syftade på);
`push/f100.webp` är identisk med `push-last.webp`. Sekvensen är alltså en äkta, sammanhängande
kamerarörelse ur det riktiga fotot, inte en löst kopplad bildväxling. Ingen öppen fråga här.

---

## 2. Auktoriteten

**Fotot.** I set-piece-akten (akt 2–3): **rörelsen**, enligt TASTE §4.8-preciseringen —
där viker typ och foto åt sidan (typen till vikt 300, fotot får bli suddigt/resa) och
rörelsen själv bär skärmen.

Vad som viker för auktoriteten, genomgående:
- Typen: vikt 300, serif, ljus, ligger i vattnets mörka band — aldrig skrikande.
- Färgen: en enda kromatisk ton (fönsterbärnsten), gör exakt två saker.
- Knappar: inga alls. Länkar är typsatta.
- Ytan: ingen platta bakom foto eller text; foto är ytan i akt 1–3, papper i akt 4–6.
- Kort: förekommer aldrig. Bevis och priser är liggare.

---

## 3. Reference-lock

```text
Primary reference/direction: Rogo — ett skymningsfoto som bär rubrik och bevis i samma
  andetag, ett hårt, fullständigt registerbyte vid fållen (mörkt/foto → vitt/plant), varje
  påstående nedanför parat med en riktig, oredigerad skärmbild, alternerande sida.
Preserve: ett enda fullbredds-skymningsfoto som bär rubriken i seriftyp, satt i fotots eget
  mörka band; ett hårt och fullständigt registerbyte vid fållen; varje påstående under
  fållen parat med en verklig skärmbild, sida alternerande nedåt sidan; betoning genom
  vikt, aldrig kursiv, inom en och samma serif; en fast toppbar (logga/kontakt), inte
  Rogos annonsrad.
Borrow only: från Groupemontoni — typ satt rakt på fotot utan platta bakom, läsbar enbart
  genom skala/spärrning mot bildens stökiga partier (K1: rubriken i vattnet, inte
  centrerad som Montonis ordmärke); mörkning läggs bara vid textens kant, aldrig som scrim
  över hela bilden (K1: adressraden mot nattfotot i akt 6).
Role rules: accenten (fönsterbärnsten) gör exakt två saker — understrykningen under
  "visitkort", strecket under kontaktadressen vid hover — aldrig knappfyllning, aldrig
  sektionsbakgrund. Skärmbilderna av Calyx/Hōrai/Hyperborea ersätter Rogos logotypvägg och
  Montonis projektkortgrid: riktigt gränssnitt, aldrig påhittade kundnamn eller logotyper.
Media strategy: photo:unsplash för dusk.webp och night.webp (vendrat, krediterat i
  credits.json); generated:higgsfield för push-sekvensen (Kling 3.0 image-to-video från
  dusk.webp, 100 rutor, vendrat i assets/push/); product-surface för demo-*.webp (riktiga
  skärmdumpar av egna sajter, aldrig illustration).
Reject: Rogos logotypvägg (skulle kräva påhittade kunder), Rogos vita pillerknapp (K1 har
  inga knappar), Rogos cookiepanel/annonsrad-krock; Montonis räknare i navigationen (inga
  riktiga driftsiffror att visa), Montonis femfärgade ESG-mosaik (K1:s palett är smal med
  en accent), Montonis centrerade ordmärkesplacering (K1:s rubrik ligger i vattnets mörka
  band, nere till vänster, inte i bildens mitt).
Token commitments: night (mörk blånatt, mätt ur dusk.webp:s vattenparti, familjen kring
  #0b1424); paper/white #ffffff för det hårda klippet i akt 4–5; ink (nästan svart) för
  brödtext på vitt; ink-soft (dämpad grå, egen uppmätt tabellvärde per grund — house-
  physics-regeln); amber (fönsterljuset, mätt ur push-last.webp/dusk.webp, familjen kring
  #f2c46b) — enda kromatiska accenten, display-roll: understrykning + hover-streck; amber-
  ink (mörkare variant) för siffrorna 01–03 på vit grund, så kontrasten håller mot papperet.
  Typroller: display/serif (rubriker, priser, adressrad) vs register/grotesk (nav, etiketter,
  brödtext, bildtexter) — rollerna korsar aldrig.
```

### Decision ledger

| Beslut | Källa | Roll att bevara | Varför |
|---|---|---|---|
| Fotot bär, hårt registerbyte vid fållen | Rogo (primär) | hero = foto+rubrik; nästa sektion = plant vitt med skärmbildspar | Alunix mål: visa vad byrån kan genom riktiga exempel, inte påhittade kunder — Rogos struktur gör exakt det bevisjobbet utan logotyper |
| Rubriken i vattnets mörka band, nere till vänster | Egen mätning av `dusk.webp` + r6 B:s luminansmätning (31/255) | display-typ ligger alltid i fotots tystaste parti | Centrerat (Montoni-stil) hade lagt texten över båten och de ljusa fasaderna; TASTE §4.1 kräver att tyst typ sitter på fotots mörka del |
| Typ satt direkt i fotot, ingen platta bakom | Groupemontoni (lånad detalj) | typografisk läsbarhet kommer av skala/spärrning, aldrig av en bakgrundsplatta | K1 har inga plattor eller kort någonstans (TASTE §2.3) |
| Skärmbilder av Calyx/Hōrai/Hyperborea ersätter logotypvägg/kortgrid | Rogo + Groupemontoni (struktur), Alunix-fakta (innehåll) | bevis = riktigt gränssnitt bredvid varje påstående | Förbjudet att hitta på kunder; de tre exempelsajterna är de enda "kunderna" som får synas |
| Mörkning bara vid textens kant i akt 6, aldrig hela bilden | Groupemontoni (lånad detalj) | scrim-roll: läsbarhet för en rad, aldrig en filter över hela fotot | TASTE §4.3: aldrig scrim över hela bilden som räddning |
| Liggarform (siffra/pris höger, hårlinjer, ingen kortram) för akt 5 | Rogo "By the numbers"-sektionen (struktur, ej siffrorna) | pris- och stats-anatomi | TASTE §1: hårlinjer och ton-på-ton, aldrig kort; Rogos egen liggare bevisar formen fungerar i just det här registret |
| Fönsterbärnsten som enda accent, två roller | Egen mätning av push-last.webp/dusk.webp (ej hämtad från någon av referenssajterna) | accent-roll: understrykning + hover, aldrig fyllning eller bakgrund | TASTE §2.2 "ett papper, en accent, och accenten gör en sak" |
| Newsreader (display) / Schibsted Grotesk (register), roller korsar aldrig | Rogos serif-på-display-mönster (83 Inter mot 14 ABC Arizona Mix) + Montonis 452:16-proportion (studiopro:fkroman) | typroll: display vs register | Kvantitativt bekräftat i båda extraherade DESIGN.md: andra-typsnittet används extremt sparsamt, bara på stora påståenden |
| Riktig genererad bildsekvens för zoomen (inte CSS-transform) | `assets/push/` (orkestrerarens material) + r6 B:s kända begränsning | scrub-enhetens `canvas[data-sc-sequence]`-data | Fingerprint-grinden (kapitel 8) kräver att hero-enheten skiljer sig från r6 B:s CSS-skalning |

**Anti-averaging-testen:**
- **Identitetstestet.** Ett foto av en svensk huvudstad i blå timme med tre namngivna
  exempelsajter och svensk copy kan inte bytas ut mot ett annat företag utan att hela
  bevisstrukturen (Calyx/Hōrai/Hyperborea) följer med — identiteten sitter i innehållet,
  inte bara i paletten. Håller.
- **Redaktionella testet.** Byt loggan mot ett kafé eller en bokhandel: skulle fållens
  registerbyte och skärmbildsparen fortfarande kännas rimliga? Nej — ett kafé har inga
  produktskärmbilder att visa. Sidan är omöjlig att förväxla med calm-editorial-slop
  eftersom hela mittdelen kräver just den här sortens bevis (webbyråns egna byggen).
- **Skärmbildstestet.** Mot Rogo och Montoni själva: K1 delar registerbytet och
  liggarformen med Rogo, men har en helt annan geografi (Stockholm, inte Manhattan), ingen
  logotypvägg, och en signaturrörelse (genererad kamera-in-i-fönster som blir en riktig
  sida) som ingen av dem har. Håller.

---

## 4. Grammatik

**Filmic one-shot** (redan låst i concepts.md). De andra sju, en mening var:

- **Chaptered editorial** förlorar: K1 är en enda sammanhängande känslokurva mot en kulmen,
  inte kapitel att bläddra mellan.
- **Live surface** förlorar: sidans första akter är ren atmosfär/fotografi, vilket denna
  grammatik uttryckligen förbjuder, trots att en riktig sajt visas live senare.
- **Continuous world** förlorar: det finns ett hårt klipp till vitt efter avslöjandet, och
  hårda klipp är precis det den här grammatiken bannlyser.
- **Typographic poster** förlorar: bannlyser fotografisk grund helt, och K1:s auktoritet
  är fotot.
- **Gallery/catalog** förlorar: exempelsajterna visas som bevis i en linjär argumentation,
  inte som ett rum besökaren vandrar runt i på egen takt.
- **Split stage** förlorar: det finns ingen tvåsidig jämförelse att lösa upp.
- **Rhythmic cutlist** förlorar: bannlyser precis de enheter (pin, dwell, spotlight-liknande
  vila) som den långsamma inzoomningen och avslöjandet behöver.

---

## 5. Feeling curve

| Akt | Känsla | Vad på skärmen orsakar den |
|---|---|---|
| 1 Stillhet | Lugn, nyfikenhet | Fotot i vila, rubriken i vattnets mörka band, sajtnamnen som text, en knappt märkbar andning i bilden |
| 2 Drag | Dragning, förväntan | Scrollen driver en kontinuerlig, exponentiell inzoomning mot fönstret; rubriken tonar och blurras bort utan att flytta sig |
| 3 Avslöjande (**toppen**) | Överraskning, förtjusning | Fönstret fyller ramen och visar sig vara en riktig, klickbar sida — Hōrai, live |
| 4 Klarhet | Skärpa, förtroende | Hårt klipp till vitt, `VI BYGGER ERT VARUMÄRKE.` radvis, tre uppslag där varje påstående möter en riktig skärmbild |
| 5 Räkning | Trygghet, konkretion | Hårlinjerna i prisliggaren dras i takt med scrollen, priserna i displaygrad |
| 6 Landning | Ro, avslut | Grunden driftar till natt, fönstret öppnar sig som en klippmask, allt står stilla, ingenting tonar bort |

**Toppen:** akt 3, "Avslöjande" — får den längsta scrollsträckan (60 vh pin efter en
2,6-spanns scrub), tystnaden före den (rubriken redan bortblurrad, sajtnamnen redan
bortdöda vid 80 % av akt 2), och det enda momentet på sidan där en genererad bild blir en
riktig, fungerande produkt.

**Tell-someone-meningen:** "du zoomar in mot ett tänt fönster över vattnet, och när
kameran når fram visar det sig vara en riktig sajt du kan klicka i."

---

## 6. Signaturrörelsen

Kameran (en förrenderad, 100-ruters bildsekvens från samma foto som bär första skärmen)
zoomar kontinuerligt mot ett enda tänt fönster tills fönstret *blir* en riktig, levande
webbplats — precis det löfte rubriken gör ordagrant ("Er hemsida är nutidens visitkort"):
det som från håll ser ut som ett vackert foto visar sig, vid närmare granskning, vara något
verkligt och fungerande. Rörelsen är alltså inte dekoration ovanpå budskapet, den *är*
budskapet, utspelat i bild.

---

## 7. Device-tabell

≥4 familjer (scrub, pin, kinetic, reveal, flow = 5), aldrig samma familj två akter i rad,
1 scrub-akt (≤2 tillåtna). Cue-kontrakt: greet i akt 1, tvåvärt i mellanakter, håll bara i
akt 6 (sista elementet på sidan).

| Akt | Device | Varför | Cue-form |
|---|---|---|---|
| 1 Stillhet | *ingen* (ground) + `drift` som egenskap | Fotot är redan på plats vid landning — ground-or-greet-regeln kräver ingen tom scen | Rubriken: greet (`0 0.3 0`), full vid start, tonar innan akt 2 tar över |
| 2 Drag | `scrub` (`data-sc-act="scrub" data-sc-span="2.6" data-sc-dwell≈0.32"`) på `canvas[data-sc-sequence]` med `assets/push/f001–f100.webp` | Enda scrub-akten (regel: ≤2, K1 använder 1); rubrik och sajtnamn är två koordinerade lager på samma scen | Sajtnamnsraden: tvåvärt, håller till ~0.8 sedan tonar (mellanakt, får inte hålla) |
| 3 Avslöjande | `pin` (`data-sc-act="pin" data-sc-span≈1.3"`, ~60 vh) — iframe-omslag som tar över från canvasen | Ramen måste stå stilla för att vara klickbar/scrollbar; `pin` är den enda enheten som håller en scen orörlig medan innehåll (etikett i toppbaren) korsar den | Etikettraden i toppbaren: tvåvärt (`0.1 0.85`) — mellanakt, håller inte |
| 4a Klarhet (rubrik) | `kinetic` (`data-sc-kinetic="lines"`) på `VI BYGGER ERT VARUMÄRKE.` | Radvis intoning är exakt vad kinetic lines är byggd för; skiljer sig från akt 3:s pin | Standard kinetic-cue vid sektionens reveal-tröskel |
| 4b Klarhet (uppslag) | `reveal` (`left`/`right` alternerande per uppslag) | Skärmbild och text glider in från motsatt håll, en gång per uppslag; skiljer sig från 4a:s kinetic | Tvåvärt, `reveal-at` runt `0.15 0.6` per uppslag |
| 5 Räkning | `flow`+`in` (stagger på raderna) + bespoke hårlinje-uppritning driven av `--sc-p` | Liggarraderna faller in i tur och ordning (kit-enhet); hårlinjens uppritning är sidans egen, aldrig en kit-parameter | Standard flow-cue; bespoke linje har ingen egen `data-sc-cue`, den läser `--sc-p` direkt |
| 6 Landning | `reveal` (`iris`/`inset`, klippmask som öppnar sig från horisonten) + `drift` (`data-sc-drift` mot nattens ton) | Sista akten på sidan — reveal skiljer sig från akt 5:s flow, drift är en egenskap ovanpå | **Måste hålla**: envärt (`0.06`) eller greet-and-hold (`0 1 0 0`) så kontaktraden aldrig tonar bort innan sidan tar slut |

**Ground-or-greet-kontroll:** akt 1 har fotot redan synligt (ground). Akt 3 tar vid där
akt 2:s scrub slutar — scenen är redan full i bild när pin börjar, inget tomt ögonblick.

---

## 8. Fingerprint mot r6 B-K1

Sex dimensioner, verifierade mot `tests/alunix-ab-r6/runs/B/K1/NOTES.md` (läst i sin
helhet, kapitel 1).

| # | Dimension | r6 B-K1 | K1 v2 (den här briefen) | Skiljer? |
|---|---|---|---|---|
| 1 | Grammatik | Filmic one-shot | Filmic one-shot | Nej |
| 2 | Nav | Fast toppbar, transparent över foto, logga vänster/adress höger | Samma mönster | Nej |
| 3 | Hero-device | CSS-`transform`-skalning av en enda stillbild | Riktig genererad 100-ruters bildsekvens (`canvas[data-sc-sequence]`, Higgsfield/Kling) | **Ja** |
| 4 | Aktform | Scrub-liknande zoom → hårt klipp → radvis intoning → riktad inglidning → procentstyrd linjedragning → klippmask (handrullat, ingen kit-`pin`) | `scrub` → `pin` (iframe-omslag) → `kinetic` → `reveal` → `flow`+bespoke → `reveal`+`drift` (kit-enheter, uttalad `pin`-akt för avslöjandet) | **Ja** |
| 5 | Avslut | Nattfoto öppnas via `clip-path: inset()` 50→0, sedan stillhet | Nattfoto öppnas via `reveal` (iris/inset) **plus** en `data-sc-drift`-färgövergång till natt, med tvingat hållande cue | **Ja** (samma grundfigur, men driften och det bindande hold-kontraktet är nya) |
| 6 | Signaturdrag | Ett skalat foto som avslöjar en overlay-skärmbild, sedan en klickbar ram | En förrenderad kamerarörelse som *blir* en levande sida — fiktionen (genererat foto) upplöses till fakta (en riktig produkt) | Fri per definition |

**4 av 6 skiljer** (dimension 3, 4, 5, plus den fria dimension 6) → godkänt enligt
fingerprint-grinden. Dimension 1 och 2 delas medvetet: grammatiken är låst av målbilden och
navmönstret är ett husgemensamt element (logga/kontakt i fast bar), inte en frihetsgrad
den här rundan äger.

---

## 9. Reduced motion-planen (F-001, F-002)

Ingen resa, formade lägen visas i ordning som egna 100vh-sektioner, aldrig en tumnagel av
slutläget och aldrig ett hopp:

1. **Första skärmen** som vanlig sektion: fotot i vila (`dusk.webp`), rubriken, underraden,
   sajtnamnen. Fönstret är **inte** markerat eller framhävt här (F-002).
2. **Fönstret, format** som egen sektion: `push-last.webp` i full bredd, bildtext
   "Fönstret är Hōrai" — den enda platsen slutläget visas innan ramen kommer.
3. **Hōrai-ramen** som egen 100vh-sektion: den riktiga `iframe`:n mot `/sites/horai.html`,
   med bildtexten `Exempelsida: Hōrai, Asian fusion-koncept`.
4. **Resten i vanligt flöde:** `VI BYGGER ERT VARUMÄRKE.`, de tre uppslagen (statiska,
   redan i färg), prisliggaren (hårlinjer redan fullt dragna), landningen (nattfoto redan
   öppet, ingen klippmaskanimation).

Ingenting startar dolt utan JavaScript eller under `prefers-reduced-motion: reduce` — exakt
samma ordning gäller i båda fallen, per house-physics reveal-guards.

---

## 10. `?preview=`-planen

- `?preview=window` — tvingar fram akt 2:s slutruta (fönstret fyller ramen, `push-last.webp`
  eller sista canvas-frame) för skärmbild, utan att kräva scroll.
- `?preview=horai` — tvingar fram akt 3:s pinnade tillstånd med den riktiga `/sites/horai.html`-
  ramen synlig och klickbar.
- `?preview=ledger` — tvingar fram akt 5 med hårlinjerna fullt dragna (annars bara synliga
  mitt i en scrollrörelse, svårt att fånga i en enda skärmbild).

Övriga akter (1, 4, 6) behöver ingen tvingad parameter: de är antingen redan synliga vid
vila (akt 1) eller vanliga scroll-reveals som syns korrekt vid vilken scrollposition som
helst efter sin tröskel (akt 4, 6).

---

## 11. Typsnitt och palett

**Typsnitt, två, roller som aldrig korsar:**
- **Newsreader**, vikt 300 (display-roll): rubrik, priser, adressraden i landningen. Ljus
  serif som lägger sig i fotots mörka band utan att skrika (TASTE §4.1: tyst typ på starkt
  foto = vikt 300 vid 64–110px). Redan bevisat två gånger oberoende i r6 (A och B valde
  samma snitt för samma jobb).
- **Schibsted Grotesk** (register-roll): nav, etiketter, brödtext, bildtexter, siffrorna
  01–03. Ett skandinaviskt tidningsgrotesk, motsvarar Rogos Inter- och Montonis studiopro-
  roll (register/UI), aldrig display.

Ingen tredje font. Serifen gör aldrig etikettarbete; grotesken bär aldrig en rubrik.

**Palett, namngivna tokens, härledda ur det egna fotomaterialet (inga hexkoder lånade från
Rogo eller Montoni):**

| Token | Ton | Källa | Roll |
|---|---|---|---|
| `--night` | Mörk blånatt, familjen kring `#0b1424` | Mätt ur `dusk.webp`:s vattenparti | Grund i akt 1–3, grund i akt 6 efter driften |
| `--paper` / `--white` | Rent vitt `#ffffff` | Beslut (hårt klipp, ej fotomätt) | Grund i akt 4–5 |
| `--ink` | Nästan svart | Beslut, kontrast mot vitt | Brödtext på vit grund |
| `--ink-soft` | Dämpad grå, **eget värde per grund** | Mätt separat mot natt respektive vitt (house-physics-regeln: en gråton håller inte över en tonal inversion) | Bildtexter, sekundär text |
| `--amber` | Varmt fönsterljus, familjen kring `#f2c46b` | Mätt ur `push-last.webp`/`dusk.webp`:s fönsterljus | Understrykning under "visitkort"; hover-streck under kontaktadressen — inga andra jobb |
| `--amber-ink` | Mörkare amber-variant | Mätt för kontrast mot `--paper` | Siffrorna 01–03 i tjänsteraden, enda stället accenten syns på vit grund |

Exakta hex-värden mäts och låses i runda 2 med `scripts/contrast.py` mot de faktiska
bildfilerna — värdena ovan är avlästa för hand ur bilderna i den här läsningen och ska
verifieras, inte antas.

---

## 12. Öppna frågor till orkestreraren

1. **Ingen post i den här briefen kräver ett svar innan runda 2 kan börja.** Målbilden,
   referenserna och materialet i `assets/` räckte för att låsa alla tolv punkterna ovan.
2. Ett litet observationspunkt, inte en blockering: `assets/push/f050.webp` visar kameran
   på väg mot en ljus, valvbågad fasad som ligger till höger om det gröna tornet i
   `dusk.webp` — arkitektoniskt en annan byggnadstyp än "Nationalmuseum" som nämndes i
   r6:s anteckningar, men fotografiskt en korrekt, sömlös fortsättning av samma foto. Jag
   utgår från att det är rätt byggnad eftersom sekvensen är genererad från just den bilden;
   säg till om en annan fasad var avsedd.
3. `VAULT/wiki/projects/_index/design-fingerprints.md` (den vault-baserade registerfilen
   `scroll/feel-and-fingerprint.md` ber om) ligger utanför det här repot och kunde inte
   läsas härifrån. Fingerprint-jämförelsen i kapitel 8 är därför gjord mot r6 B-K1 direkt,
   per uppdragets egen instruktion — men om vault-registret ska uppdateras efter runda 3
   behöver orkestreraren göra det steget, jag har ingen skrivväg dit.

---

## Sammanfattning

**43 filer/bilder lästa**, i uppdragets ordning: SKILL.md (via `Skill(design)`), TASTE.md,
FEEDBACK.md, reference-lock.md, house-physics.md, scroll/{README,grammars,devices,
feel-and-fingerprint}.md, scripts/scroll/{NOTE.md,template.html}, concepts.md (§K1),
rogo/{entry.md, fold.webp, 8 slices, extract/rogo-com-DESIGN.md}, groupemontoni/{entry.md,
fold.webp, 7 slices, extract/groupemontoni-com-DESIGN.md}, r6 {B,A}/K1/NOTES.md,
assets/push/README.md, assets/credits.json, samt bilderna dusk.webp, push-last.webp,
night.webp, demo-{horai,calyx,hyperborea}.webp och en egen kontinuitetskontroll av
push/f001, f050, f100.webp mot dusk.webp.

**BRIEF.md ligger i:** `tests/alunix-ab-r7/runs/B/K1/BRIEF.md`.

**Öppna frågor:** en observationspunkt (byggnadsidentitet i f050, ej blockerande) och en
notering om att vault-fingerprintregistret ligger utanför repot — se kapitel 12. Inget
kräver svar innan runda 2.

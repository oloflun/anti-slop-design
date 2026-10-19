# Alunix r8, målbilder

Sammanslagen 2026-09-10 av lead ur `concepts-V3c.md`, `concepts-K3.md` och `concepts-K4.md`,
som står kvar som källfiler. Faller den här filen och en källfil isär gäller källfilen, och
den här rättas. Faller den här filen och planen isär gäller planen
(`C:\Users\Anton L\.claude\plans\trots-den-senaste-design-system-federated-raven.md` § 7.5).

## Leadens godkännande, per cell

| Cell | Målbild godkänd | Låsta referenser lästa som pixlar av lead | Anmärkning |
|---|---|---|---|
| V3c | ja | `oryzo-ai` (primär), `mattis-studio` | Iteration av V3b. Fingerprint-gaten gäller inte. Registerraden för V3 → V3c förs in efter Antons dom |
| K3 | ja, med ett villkor | `squarespace` (primär), `aevi-wellness`, `beautiful`, `insign`, `mode` | Villkoret står under "Om K3:s lås" nedan |
| K4 | ja | `paper` (primär) | Aktformraden mot K3 är cellens tunnaste punkt och är utskriven som sådan |

## Om K3:s lås, och varför primärposten inte är en riktningskälla

`select.py` gav K3 `squarespace` som topprankad post. Jag har läst folden som pixlar:
Squarespace är en fotografisk sida med centrerad rubrik, vit knapp och lutande kundkort.
K3 är ett kallt ritpapper utan ett enda fotografi, utan knapp, utan centrerad rubrik och med
en ritad teckenförklaring i marginalen som nav. `reference-lock.md` säger att primärkällan
äger stämning, täthet och struktur. Squarespace äger ingen av dem i K3.

Det är ändå inte ett fel i urvalet, och lösningen är inte att jag väljer om ur minnet, vilket
är precis det `catalogue-first.md` § 5 finns för att stoppa. Alunix ligger på **Tier 1**:
riktningen härleds ur varumärkets egna belägg (ordmärket, `#1E5E9C`), inte ur en referens.
På Tier 0 och 1 är låset enligt `reference-lock.md` **kvalitetsribban som det härledda
systemet ska klara**, inte riktningen. Läst så är låset korrekt: Squarespace är den bästa
sidan i kategorin, och K3:s uppgift är att slå den, inte att likna den. Avsnitt (7) i
`concepts-K3.md` är därför cellens operativa innehåll, inte avsnitt (6).

**Villkoret, som går in i R1 som en byggaruppgift.** Tre av K3:s fem rader i avsnitt (7)
påstår saker jag inte kan se i folden: att `insign` låter tre mättade färgband vara
navigationen, att `aevi-wellness` bygger djup ur bandväxling med hårlinjen som enda
strukturmedel, och att `mode` inhägnar accenten till en enda fylld knapp. I `mode`:s fold är
den syrgröna färgen tvärtom rubrikens överstrykningsblock. Påståendena kan mycket väl stämma
längre ned på sidorna, som folden inte visar. Därför: varje rad i avsnitt (7) ska i R1 förses
med den slice eller den rad i `entry.md` den vilar på. En rad utan belägg stryks ur låset.
Samma krav gäller V3c:s och K4:s avsnitt (7).

## Gemensam fingerprint

Varje cell bär sin egen fullständiga tabell mot registrets 36 byggrader i sin källfil:
`concepts-K3.md` § (4) och `concepts-K4.md` § (4). V3c undantas gaten som iteration av V3b
och bär i stället sin föreslagna uppdaterade registerrad i `concepts-V3c.md` § (4).

Lägsta utfall mot registret:

| Cell | Lägsta summa | Mot vilken rad | Kommentar |
|---|---|---|---|
| K3 | ingen rad under 4/6 | redovisad i källfilen | |
| K4 | 5/6 | r1 K2 Tjänsteledger, r2 R5 Konsolram, r3 build | alla tre delar bara grammatik, som målbilden själv låser |

### K3 mot K4, sex dimensioner plus temperatur och typsnitt

Det här är kravet som registret inte kan ställa, eftersom ingen av cellerna finns i det ännu.
Tabellen är hämtad ur `concepts-K4.md` § (4) och gäller som den står.

| Dimension | K3 | K4 | ≠? |
|---|---|---|---|
| Grammatik | Chaptered editorial | Split stage | ≠ |
| Nav | Ritad teckenförklaring i vänstermarginalen, sticky | En enda lodrät gräns i bildens mitt som är hela chromen | ≠ |
| Hero-device | Måttsatt sektionsritning i inline-SVG som ritar sig själv | Två färdiga, levande sajter från första bildrutan | ≠ |
| Aktform | pin 2,4 dwell 0,35, tre reveal i följd, kinetic tidigt | pin 2,4 dwell 0,22, tvåriktad reveal, kinetic sent, pekardriven bespoke-rörelse i pin-akten | ≠, tabellens tunnaste rad |
| Avslut | Specifikationsblad i en ritad ram vars linjer dras in sist | Kollaps till en kolumn, ingen ram, ytan fylls | ≠ |
| Signatur | Ritningen blir sidan | Delaren tippar | ≠ |
| Temperatur | Kallt, `oklch(0.95 0.012 230)`, hue 230 | Varmt, `oklch(0.957 0.013 85)`, hue 85 | ≠, 145 grader isär |
| Typsnitt | Chivo + Martian Mono | Switzer + Reddit Mono | ≠, noll överlapp |

**8/8.** Aktformraden är den svagaste: båda öppnar med `pin` span 2,4 och båda innehåller
`flow`, `count` och `reveal`. Jag flyttar inte span 2,4, eftersom målbilden låser den och
gaten inte faller på den. Raden bevakas i R2:s F-007-kontroll: skiljer sig de två akterna inte
i pixlar, inte bara i markup, byter K4 dwell eller aktordning.

## Genererat material

Ingen cell i r8 har genererat material. Higgsfield mättes av lead 2026-09-09 till 0 krediter
på free plan, med en enda privat workspace, så steg 1 och 2 i planens § 10.6 faller.
Codex-fallbacken hoppades över för K3 därför att steg 3 är strikt bättre där, inte bara
billigare: en procedurell textur är sömlös genom konstruktion. Beslutet står som en rad i
varje cells `NOTES.md`, i varje `credits.json` och i varje decision ledger.

---

# Alunix r8, målbild V3c (arkitektens del)

Denna fil äger **bara** cell V3c. Lead slår ihop V3c, K3 och K4 till `concepts.md`.
Källa: planens § 7.5, ordagrant speglad i `tests/alunix-r8/malbilder/V3c.md`, som är
bindande. Varje avvikelse nedan har en rad i `runs/V3c/BRIEF.md` § decision ledger med
källa.

---

## § sweep_raw

```
$ python scripts/catalogue/sweep_raw.py
sweep: rent - varje kalla under raw/ och processed/ har en post (0 ignorerade).
EXIT=0
```

Kört av arkitekten 2026-09-09, bekräftar leads körning. Grinden är öppen.

## § catalogue-select

Brieffilen: `tests/alunix-r8/runs/V3c/BRIEF-draft.md` (arkitektens utkast, skrivet enbart
för att skriptet ska ha deklarerade fält att poängsätta mot; den är inte cellens brief).

```
$ python scripts/catalogue/select.py --brief tests/alunix-r8/runs/V3c/BRIEF-draft.md --k 4 --wildcard --explain
Brief: tests\alunix-r8\runs\V3c\BRIEF-draft.md  ->  5 poster

   14  oryzo-ai                 cinematic dark         continuous world
       +3 register | +3 grammatik | +2 category2 | +6 fritext (accent, black, button, display)
   12  dope-security            cinematic dark         split stage
       +3 register | +2 category | +1 mode | +6 fritext (accent, button, glass, hairline)
   12  mattis-studio            cinematic dark         split stage
       +3 register | +2 category | +1 mode | +6 fritext (agency, beside, black, display)
   12  monologue                cinematic dark         split stage
       +3 register | +2 category | +1 mode | +6 fritext (colour, display, headline, mono)
   12  planhat                  cinematic dark         split stage
       +3 register | +2 category | +1 mode | +6 fritext (cards, cinematic, dark, display) | wildcard: utanfor kategorin

Mediastrategi ur posternas egna falt (Photo search) - locken ska inte gissa:
  - oryzo-ai: Unsplash first, Pexels second. - "craft tools top down workbench flat lay" - "cutting mat pencil knife top down" - "product design workshop
  - dope-security: Unsplash first, Pexels second. - "dramatic twilight sky purple clouds horizon" - "dusk sky gradient clouds wide format" - "airplane light tr
  - mattis-studio: Unsplash first, Pexels second. - "black and white fashion editorial studio" - "monochrome portrait high contrast studio" - "editorial fashio
  - monologue: Unsplash first, Pexels second. - "dark texture ripple abstract background" - "black fabric wave texture close up" - "dark water surface ripp
  - planhat: Unsplash first, Pexels second. - "misty forest golden hour light" - "sunlight through trees atmospheric" - "moody forest landscape warm tone

catalogue-select skriven: oryzo-ai, dope-security, mattis-studio, monologue, planhat  ->  C:\Users\Anton L\anti-slop-design\.impeccable\design-session.jsonl
```

**Låst rad:** `catalogue-select: oryzo-ai, dope-security, mattis-studio, monologue, planhat`
(`--k 4 --wildcard`, wildcard = `planhat`).

**Urvalet motsäger planens gissning, och skriptet vinner.** Planens § 7.5 skrev
"förväntat: `garden-eight`, `mattis-studio`, `squarespace`, ev. `creative-giants`" men
säger samtidigt att referenserna "låses via `select.py`". Bara `mattis-studio` överlappar.
Orsaken är mekanisk och kontrollerad: `garden-eight` och `creative-giants` står som
`editorial print` / `typographic poster` och `squarespace` som `modern clean` /
`chaptered editorial` i `index.json`, medan V3c ärver V3b:s värld, som är `cinematic dark`
/ `continuous world`. Gissningen beskrev vad V3c ska **slå**, inte vilken värld den bor i.

Konsekvens, skriven som beslut och inte som tyst avvikelse:

- **Låset (`reference-lock.md` Tier 0, "Primary = the locked system itself"):** primär
  riktning är V3b själv, `tests/alunix-concepts-r5/cells/V3b-chain/index.html`. V3c är en
  iteration; det är den enda ärliga primärkällan.
- **Lånade detaljer (max två, per `reference-lock.md`):** `oryzo-ai`:s fysiska objekt som
  vrider sig i ett mörkt tomrum, och `mattis-studio`:s konsolram, som lånas **som
  avvisning** (V3c:s kort är ett fysiskt kort, inte en platt ram).
- **`garden-eight` och `squarespace` behåller sina rader i § 7 som ribbor** eftersom
  målbilden namnger dem, med källan utskriven: planens § 7.5, inte `select.py`.
  `creative-giants` faller helt; ingen källa stödjer den.

## § Lästa referenser

Tre rader per fil: vad den gör, vad jag tar, vad jag lämnar. Bilder lästa som pixlar med
`Read`, text som text.

### oryzo-ai (topprankad; samma register OCH samma grammatik som V3c)

| Fil | Gör | Tar | Lämnar |
|---|---|---|---|
| `fold.webp` | Ovanifrån-foto av korkunderlägget på skärbräda, ordmärke i affischgrad uppe till vänster, halvtransparent creditkort nere till vänster, "SCROLL TO CONTINUE" i botten | Ordmärke i affischgrad som får dela fold med ett objekt utan att konkurrera, därför att objektet ligger i en annan ljushet | Scroll-cuen (gate 88), creditkortet som lager över fotot, den varma paletten |
| `slices/02.webp` | Objektet lutar i ett mörkt tomrum, rubriken i två rader vänster, brödtext höger, inget annat | **Kärnlärdomen för V3c:** ett fysiskt objekt läses som roterande därför att dess *material och kant* fångar ett snedljus, inte därför att rotationen finns | Den varma walnut-grunden, versal-500-rösten, tre textkolumner runt objektet |
| `slices/04.webp` | Samma objekt hålls i en hand, rubriken "Powered by AI" i display, orange kredit under | Att objektet får en enda ljuskälla och att bakgrunden är helt tom runt det | Händer (förbjudet på Alunix, `generation.md` § Never), orange, "AI"-tonläget |
| `slices/06.webp` | Regnbågsram runt hela viewporten vid hover-läge, samma objekt | Ingenting | Hela greppet: en kromatisk ram runt viewporten är gate 89-territorium och bryter "ett papper, en accent" |
| `slices/08.webp` | Objektet ensamt i tomrum, texten utskuren av objektet | Överlappet objekt-över-typ som djup utan skugga (TASTE § 4.7) | Den nästan tomma skärmen som eget steg; V3c har inte råd med 100vh per sats |
| `slices/10.webp` | Objektet i en röd folieförpackning, mitt i en jättetypografisk rad "it's wearable" | Objektet som skär genom raden i stället för att ligga bredvid den | Färgen, förpackningen, streckade markeringsramar (re-drawn chrome, gate 47) |
| `entry.md` | Låser walnut-tomrum, versal-500 som enda röst, orange enbart till credits, 100vh per sektion, streckade hårlinjer | "Fence an accent to one role" (V3c: `#1e5e9c` gör en sak) och "compress display leading until letterforms overlap" (kortets baksida, `line-height:.9`) | 100vh-låset per sektion, streckade avdelare, tolvpixlars radie, hela paletten |

### mattis-studio (målbildens namngivna referens; ärvd ur V3b:s eget lås)

| Fil | Gör | Tar | Lämnar |
|---|---|---|---|
| `fold.webp` | Svart hero med hörnmarkerad ram runt ordmärket, versionstagg, grundarfoto, signatur i orange, tre tjänsteord på en rad, slot-räknare i botten | Att tjänsteorden står som **en rad i registergrad**, inte som tre kort; det är precis vad V3c:s kortbaksida gör | Konsolramen, versionstaggen, klockan, slot-räknaren, grundarfotot, signaturen, orange |
| `slices/01.webp` | Ett helt orange fullbleed-block med tesen, en gråtonad plåt i mitten, "12+ industries" nere till höger | Att en tes får äga ett helt materialbyte (V3c: den blå tesen) | Den mättade orangen, den påhittade statistiken, "24+ PROJECTS" |
| `slices/02.webp` | Svartvit editorial-plåt i högerspalten mot ljus grund, jätterubrik i vänsterspalten | Svartvitt foto mot ett färgblock i stället för färgfoto (TASTE § 2.1) | Boxmockup-rutnätet, showreel-knappen, "SEE THE WORK"-cuen |
| `slices/03.webp` | Fullbredds plåtrader med case-etiketter, en helt svart tyst remsa mellan två plåtar | Den svarta tysta remsan som andrum mellan två bilder | Case-galleriet; Alunix har tre exempelsajter, inte ett portfölj-flöde |
| `slices/05.webp` | "BUILT ON REPUTATION" med ett svart kort som bär "/2.7+ average client rating on Google & Clutch" | Ingenting | **Allt.** Omdömen, betyg och kundantal är exakt det PRODUCT.md-frånvarolistan förbjuder |
| `slices/07.webp` | Orange sektion med tre siffror (22+, 2.2S, 30%) som textur | Formen (display-grad, liten etikett) enligt TASTE § 4.9 | Innehållet; V3c har inga sanna sådana tal, alltså inga tal |
| `slices/09.webp` | Citat med foto och signatur, sedan "PRICING." och en jämförelsetabell med kryss och streck | Att priset får vara sidans egen liggare | Citatet, personen, tabellen med kryss, `$4,800/MONTH`, tankstrecket i citatet |
| `slices/11.webp` | Logotypvägg med sju kundmärken, sedan "NEWS AND UPDATES." | Ingenting | Logotypväggen är uttryckligen förbjuden i r7:s § Förbjudet |
| `entry.md` | Beskriver hero-kortet som "a UI component being inspected" och kräver att fotot är svartvitt där det möter färgblocket | Regeln "photography stays black-and-white wherever it meets a saturated colour block" (V3c: Hyperborea-plåten mot den blå tesen) | Konsolvokabulären i sin helhet; F-006 och gate 47 träffar den rakt av |

### dope-security

| Fil | Gör | Tar | Lämnar |
|---|---|---|---|
| `fold.webp` | Skymningsfoto som hero, ett frostat "boarding pass"-kort till höger med två inloggningsknappar, kursiv display-serif blandad med grotesk | Ingenting ur folden | Glaskortet (F-006 rakt av), violett, kursiv serif i rubriken, två knappar i heron |
| `slices/04.webp` | Nästan svart skärm, en rubrik vänster, ett jätteord "GEN 1" i grunden som textur bakom typen | Ett enda ord i grunden som textur bakom typen, i låg kontrast, som djup utan skugga | Det platta produktfotot bakom, mono-stämpeln, koordinatfoten |
| `entry.md` | Anger accentfrekvens som ett tal ("en glöd, en fyllning, en linje per sida") och kapar skugga till en enda 1 px hårlinje | **"State an accent's frequency as a number, not a feeling."** V3c skriver ut sitt accenttal i ledgern | Tre typsnitt, violett, pill-radien 1584 px, GrandSlang-regeln |

### monologue

| Fil | Gör | Tar | Lämnar |
|---|---|---|---|
| `fold.webp` | Mörk grund med hårlinjeraster, serif-rubrik centrerad, mono-brödtext, en fylld knapp, fyra flikar med färgade appikoner under | Hårlinjerastret som håller sidans marginaler synliga (V3c: hårlinjerna på `--rail-x`) | Centrerad hero, badge-raden ovanför rubriken, ikonfliksraden, mono som brödtext |
| `slices/05.webp` | Produktskärmar i teal renderade som stora rundade rutor med app-chrome inuti | Ingenting | Fabricerad produkt-UI (gate 79) och re-drawn chrome (gate 47); teal |
| `entry.md` | Mörk grund, serif-display mot mono-register | Ingenting utöver rastret | Hela typsystemet; V3c har Geist och Public Sans låsta |

### planhat (wildcard, utanför kategorin)

| Fil | Gör | Tar | Lämnar |
|---|---|---|---|
| `fold.webp` | Ett enda målerisk, räfflat foto bär hela folden; rubriken i vikt 300 ligger i fotots mörka vänsterdel; en liten kicker ovanför; en vit knapp | Bekräftar TASTE § 2.1 mätt: vikt 300 i stor grad ligger alltid i fotots **mörka** parti. V3c:s rubrik ligger på den mörka grunden, aldrig på plåtens ljuspöl | Det varma gröngula grundmotivet, den vita fyllda knappen, kickern över rubriken |
| `entry.md` | Fotot är auktoriteten och typen viker helt | Att endast en av typ och foto får bära | Paletten, "agentic platform"-rösten, knappformen |

**Öppen punkt, redovisad som avvikelse:** av `dope-security`, `monologue` och `planhat`
lästes folden plus en (respektive noll, för `planhat` som saknar `slices/`) skiva som
pixlar, inte alla tolv. `oryzo-ai` lästes med sex av tolv skivor, `mattis-studio` med sju
av tolv. Skälet är kostnadstaket på den här körningen, inte att filerna saknas. Nästa
konkreta steg: lead eller byggaren läser återstående skivor i R1 och rapporterar om någon
av dem ändrar en rad ovan. Ingen slutsats i den här filen vilar på en oläst fil.

---

## V3c · Plåt i grunden · kortet vänds

### (1) Auktoritet och vad som viker

**Auktoriteten är typen** (TASTE § 1, raden "Typen (ordmärke eller rubrik i
viewport-bredd)"): rubriken `Er hemsida är nutidens visitkort` i affischgrad utanför
plåten bär sidan, och den står kvar genom hela den pinnade akten som stagens ground.

Vad som viker, en mening var: **fotot** viker genom att stanna lågexponerat inuti plåten
och aldrig gå fullbleed. **Ytan** viker genom att vara en enda kontinuerlig svartvit grund
utan sektionsfärger, så materialbytet sker i spalterna och inte i grunden. **Färgen**
viker genom att `#1e5e9c` bara gör en sak, den blå tesplåten, och aldrig blir knapp,
ram eller understryk. **Rörelsen** viker på hela sidan **utom i signaturakten**, där
TASTE § 4.8:s r6-precisering gäller: i set-piecet är rörelsen auktoriteten, och där är
typen redan vikt 300 och fotot redan lågexponerat.

**Mätningen som gör "ett displayelement" sant genom hela akten:** vid 1440 är plåten
`min(1440 - 2*rail, 56vh*16/9)` = 896 px bred, och kortbaksidans `ALUNIX` klampar på
`9cqw` av plåtens egen container = 81 px (taket `7.5rem` = 120 px binder inte).
Hero-rubriken ligger på ~9cqw av sidans container = ~130 px. Kvoten är 0,62, alltså det
"ett steg ner" TASTE § 1 kräver, och 81 px mot 16 px brödtext är 5,1x, alltså över
TASTE § 2.4:s golv. **Byggaren mäter och rapporterar båda talen vid 1440; målvärde
kvot <= 0,70 och baksidans display >= 5x brödtexten.**

### (2) Troplistan, avprickad

TASTE § 5, punkt för punkt:

| Trop | V3c |
|---|---|
| Ikongrid | Frånvarande. Sidan har noll ikoner; tjänsterna är en liggare med siffror. |
| Gradient-mesh | Frånvarande. Grunden är ett fotografi, tonad genom `--sc-canvas`-drift, aldrig en gradient. |
| Glasmorfism | Frånvarande. Ingen `backdrop-filter` någonstans; `panel-open`, det svarta konsolkortet, **tas bort**. |
| Centrerad hero med badge-rad | Frånvarande. Rubriken är vänsterställd på `--rail-x`, ingen badge finns. |
| Lila/indigo-accent | Frånvarande. Enda accenten är `#1e5e9c`. |
| Skuggade 8 px-kort | Frånvarande. Noll `box-shadow`. Plåtens enda kant är en hårlinje `--frame-line`. **Radie 0 överallt** (Shape Consistency Lock, skalan {0-3}). |
| Stockfoto av leende team | Frånvarande. Inga människor, inga ansikten, inga händer. |
| "h1 48 / h2 32"-skala | Frånvarande. Display 130 px / 81 px mot brödtext 16 px; inget ligger på mellannivån. |
| Dekorativa blobbar | Frånvarande. |
| Tre lika feature-kort | Frånvarande. `panel-services` **tas bort** som dubblett av liggaren, vilket är hela skälet. |

Utöver listan:

- **F-006 (glaskort med telemetri över foto):** frånvarande. Det svarta konsolkortet med
  `2026 · SVERIGE` och den levande klockan är den närmaste släktingen på V3b och det är
  precis den sektion V3c tar bort. Kortbaksidan får **ingen tidsstämpel och ingen
  `2026 · SVERIGE`**, uttryckligen enligt målbilden.
- **Gate 47 (re-drawn chrome):** frånvarande. De tre exempelsajterna visas i riktiga
  `<iframe>`, aldrig i en ritad webbläsarram, och kortet har ingen ram som imiterar UI.
  **Risken sitter i själva kortmetaforen:** ett "visitkort" med hårlinje är ett fysiskt
  objekt, inte en ritad UI-ram, och skiljer sig från Mattis konsolram genom att det saknar
  hörnmarkeringar, versionstagg och klocka. Byggaren får inte lägga tillbaka någon av dem.
- **Gate 79 (fabricerad produkt-UI):** frånvarande. Ingenting på sidan simulerar en skärm.
- **Gate 88 (scroll-cue):** frånvarande, och uttryckligen: stagens ground är synlig från
  p = 0, så "ground or greet" är uppfyllt utan cue-text.

### (3) Ett displayelement per skärm (1440x900)

| Skärm | Vad som syns | Displayelementet | Allt annat |
|---|---|---|---|
| s1 | Hero vid ps = 0: rubrik i affischgrad, kortets framsida med ljuspölen, underraden under plåten | `Er hemsida är nutidens visitkort` (~130 px) | Plåten lågexponerad, underraden 16 px, logo-docken i registergrad |
| s2 | Hero vid ps ~ 0,42: kortet mitt i vändningen, rubriken kvar | **Vändningen själv** (TASTE § 4.8, r6-preciseringen: rörelsen bär set-piecet) | Rubriken kvar men vikt 300, ingen ny text tillkommer |
| s3 | Hero vid ps >= 0,72: kortbaksidan i vila, rubriken kvar | `ALUNIX` på baksidan (81 px, kvot 0,62 mot rubriken) | Kicker `Digital byrå` 10,5 px, hårlinje, tjänsteraden i mono, `Boka ett möte ->` som typsatt länk |
| s4 | Vänster: blå tesplåt med Hyperborea-bleeden. Höger: jätterubriken över liggarens rad 01 | `VI BYGGER ERT VARUMÄRKE.` i högerspalten | Tesargumentet i brödgrad, Hyperborea-plåtens bildtext i registergrad |
| s5 | Vänster: Calyx som ljus iframe. Höger: liggarens rader 02-03 som scrubbas fram | Calyx-ramen (den levande sajten är skärmens objekt) | Liggarraderna är registergrad med siffror, aldrig display |
| s6 | Vänster: prisblocket, mörkt. Höger: Hōrai som mörk iframe | `Alla har rätt till bra design.` | Prisraderna som fetstilsrader i brödgrad, paketpriserna som liggarsiffror |
| s7 | Avslut: `kontakt@alunix.se` som textrad mot grunden | Mailto-raden, ensam på skärmen | Ingenting annat; ingen formulärkomponent, ingen upprepad CTA |

Sju skärmar. Total scrollhöjd: heron 2,2 span + 0,35 dwell = ~2,55 vh, plus sex
flow-skärmar, landar i intervallet 9-11 vh, inom budgeten 8-14 vh
(`feel-and-fingerprint.md` § Pacing).

**Kolumnviktsvarning som lead ska squinta på efter R2:** s6 lägger prisblocket (mörkt,
tungt) i vänsterspalten samtidigt som högerspalten bär Hōrai (också mörk). Målbilden ger
arkitekten rätt att flytta priset tillbaka till höger om vänster blir för tung. Domen
skjuts till pixelläsningen; ingen kolumn får bära mindre vikt än sin bredd.

### (4) Registerraden för V3 -> V3c (förslag; lead för in den efter Antons dom)

Fingerprint-gaten (>= 4/6) gäller **inte** V3c: cellen är en iteration av V3b och tar över
registrets V3-linje i stället för att öppna en ny yta. Radformatet är
`feel-and-fingerprint.md` § Row format.

```
| r8 V3c Plåt i grunden, kortet vänds | Continuous world, loose reading inherited from M1 via V3b | Thin top row with wordmark and contact that scrolls away, inherited chrome | The same framed plate, now a two-faced card in a pinned act: headline outside it at poster scale, subline under it, and the plate itself turning on its Y axis from photographic front to matte black back | 7 screens, 1 pinned act (span 2.2, dwell 0.35) plus 6 flow acts; panel-open and panel-services removed, their content moved onto the card's back and into the ledger; two columns that swap material against each other | The price ledger and a mailto set as a line of type, no form, no repeated CTA | The hero plate is a physical card: `--flip = smoothstep(0.12, 0.72, --sc-ps)` turns `.plate-card` on rotateY so the light-pool front becomes a matte black back carrying the wordmark, hairline only at 90 degrees | Cinematic dark | Geist + Public Sans; `--sc-canvas` #0b0c0e, paper #fdfbf4, accent #1e5e9c | `anti-slop-design/tests/alunix-r8/runs/V3c/index.html` |
```

**Varför detta fortfarande är en iteration och inte ett nytt bygge.** Grammatik, nav,
värld, palett och typsnitt är oförändrade från V3b, och de tre dimensioner som ändras
(hero-device, aktform, signatur) ändras alla av **samma** ingrepp: plåten blir ett kort med
två sidor. Ett nytt bygge skulle ha ändrat minst en av grammatik, nav eller värld; V3c
ändrar ingen av dem. Registrets V3-linje är därmed fortfarande upptagen av samma yta, nu
med en mer specifik signatur. Två saker tas dessutom **bort** utan att ersättas av något
nytt (`panel-open`, `panel-services`), vilket är iterationens signatur, inte nybyggets.

### (5) Rörelsen

**Motion-tes.**

- **Focal:** ögat äger plåtens mittlinje. Vändningen sker runt plåtens egen vertikala
  mittaxel, så det som rör sig är exakt det som redan var i fokus vid ps = 0.
- **Continuity:** rubriken och underraden står stilla genom hela akten. De är stagens
  ground och de är kontinuitetsankaret som gör att vändningen läses som att *kortet*
  vänds och inte som att sidan byter scen.
- **Feedback:** varje scrollhack flyttar `--flip` med en lerpad andel, så handen får
  omedelbart svar; vid 90 grader syns bara hårlinjen, vilket är det ärliga svaret på
  "var är kortet nu".
- **Budget:** en pinnad akt på hela sidan, span 2,2 + dwell 0,35. Ingen annan akt får
  `pin`. Sidans övriga sex skärmar är `flow` med korta stagger.

**Feeling curve** (en känsla per akt, aldrig två lika i rad):

| Akt | Känsla | Vad på skärmen orsakar den |
|---|---|---|
| s1 hero, ps 0 till 0,12 | Igenkänning | Ett visitkort ligger stilla på ett bord i ett mörkt rum; ljuspölen vandrar långsamt över det |
| s2 hero, ps 0,12 till 0,72 | Nyfikenhet | Kortet börjar vändas av sig självt i takt med handen; vid 90 grader finns bara en hårlinje kvar |
| s3 hero, ps 0,72 till 1 | Erkännande | Baksidan landar och det är Alunix eget kort: namnet, vad de gör, och en väg in |
| s4 tes | Övertygelse | Ett helt materialbyte till blått, med Hyperborea-plåten som bryter sin egen kant |
| s5 bevis | Tillit | En riktig sajt laddar och går att titta på, inte en skärmbild |
| s6 pris | Lättnad | Tre priser står utskrivna utan att man behöver fråga |
| s7 avslut | Beslut | En rad, en adress, ingenting mer att göra |

**Tell-someone-meningen:** *"Det är sidan där byråns visitkort ligger på bordet och vänds
när man scrollar, och baksidan är deras riktiga kort."*

**Delight-tes, en mening:** kortet vänds.

**Device-tabell** (>= 4 familjer, aldrig samma två i rad):

| # | Akt | Device | Familj | Läser | Varför |
|---|---|---|---|---|---|
| 1 | s1-s3 hero | `pin` span 2.2 dwell 0.35 + bespoke `rotateY` på `.plate-card` | pin | **`--sc-ps`** | Vändningen är sidans topp och måste få mest scrollrum (`feel-and-fingerprint.md` § The peak) |
| 2 | s1 hero, inuti akten | bespoke `paintHeroPool` (`object-position` på `#heroPoolImg`) | bespoke paint | **`--sc-ps`** | `object-position` är något ögat ser förflytta sig, alltså F-014 punkt 1 |
| 3 | s4 tes | `drift` mot `#123f68` + `reveal="up"` på tesrubriken | drift | `--sc-p` för drift-tonen (ingen förflyttning), **`--sc-ps`** för Hyperborea-plåtens bleed-transform | Materialbytet är en ton, inte en rörelse; bleeden är en rörelse |
| 4 | s5 liggaren | bespoke ordscrub + självritande tråd | bespoke paint | **`--sc-ps`** | Orden och trådens `scaleY` förflyttar sig; F-014 punkt 1 |
| 5 | s5 Calyx | `reveal="up"` en gång, sedan ramen orörd | reveal | `--sc-p` (bara cue-opacitet) | En iframe får aldrig transformeras eller tonas efter att den visats (M1:s egen lärdom) |
| 6 | s6 Hōrai | `reveal="iris"` en gång | reveal (iris) | `--sc-p` (bara cue-opacitet) | Samma regel; iris öppnar ramen, rör den inte sedan |
| 7 | s6 jätterubriken | ren CSS `scale(0.92 -> 1)` | kinetic type | **`--sc-ps`** | Skalan är en transform; V3b läste `--sc-p` här och det är en av felen V3c rättar |
| 8 | s1-s7 grunden | `drift` i tre stopp | drift | `--sc-p` | Grunden byter ton, den förflyttar sig inte |

Åtta poster, sex familjer (pin, bespoke paint, drift, reveal, iris-reveal, kinetic type),
aldrig samma två i rad.

**`will-change`:** sätts på `.plate-card` (elementet som roterar, inte akt-behållaren)
enbart medan `0 < ps < 1`, tas bort i vila. `.giant`:s permanenta `will-change` **tas
bort**; det är en av de fyra vilande promoveringarna F-013 mätte.

**Rejected-lista** (find-animation-opportunities-gaten; fyra frågor per kandidat:
frekvens, syfte, hastighet, funktion):

| Kandidat | Frekvens | Syfte | Hastighet | Funktion | Dom |
|---|---|---|---|---|---|
| Kortet vänder sig också vid hover | Varje gång pekaren passerar plåten, alltså många gånger per besök | Inget; vändningen har redan hänt i akten | Skulle behöva vara snabb för att inte kännas trög, vilket motsäger aktens tempo | Ingen; den tar bort aktens engångskänsla | **Avvisad** |
| Ljuspölen följer pekaren (`--sc-mx`) | Kontinuerligt medan pekaren är i heron | Närvaro | Omedelbar | Ingen; den konkurrerar med scrollens egen koreografi om samma element | **Avvisad.** `feel-and-fingerprint.md`: "Embodiment is seasoning. One or two per page", och akten är redan sidans en |
| Liggarraderna lyfter vid hover | En gång per rad, ofta | Att visa att raden är interaktiv | 150 ms | Fel; raderna är inte länkar | **Avvisad** |
| Prisraderna räknar upp till sitt tal | En gång | "Dynamik" | 800 ms | Ingen; talen är fasta priser och en uppräkning gör dem svårare att läsa | **Avvisad.** TASTE § 4.9: siffror får vara textur bara som form, aldrig som föreställning |
| Hårlinjerna ritar sig in vid scroll | Sju gånger, en per skärm | Struktur | 300 ms | Marginell; strukturen finns redan i vila | **Avvisad.** Rörelse bara där typ och bild är tysta (TASTE § 4.8), och hårlinjerna sitter överallt |
| Kortet får en specular-hårlinje på den ledande kanten under vändningen | En gång, inuti akten | Att göra rotationsriktningen läsbar | Följer `--flip`, ingen egen tid | **Bärande.** Se § 7 och `runs/V3c/assets/ASSETS.md`: det är den ena rörelse som kompenserar för att stillbilden inte bär flippen | **Behållen** |
| Framsidan mörknar när planet vrider sig bort från ljuset | En gång, inuti akten | Fysisk trovärdighet | Följer `--flip` | **Bärande**, samma skäl | **Behållen** |

### (6) Färgstrategi

**Nivå: Restrained.** Sidan är en kontinuerlig svartvit fotografisk grund plus papper, och
exakt en kromatisk färg som gör exakt en sak.

**Den fysiska scenen, i en mening:** ett mörkt rum där ett enda visitkort ligger på ett
bord under en snedställd lampa, och där ljuset längre in i sidan faller på en pappersark
i stället.

**Låset, utskrivet, inget nytt val görs:** målbilden låser paletten till `#0b0c0e`
(grunden), `#fdfbf4` (papperet, R6-världen), `#1e5e9c` (accenten) och typsnitten till
**Geist** (röst: kortbaksidans ordmärke, liggarrubrikerna, den typsatta länken; Geist Mono
enbart som register, max fyra monoetiketter på sidan) och **Public Sans** (hero-rubriken i
vikt 300, jätterubriken, brödtext). Rollerna korsar aldrig. Ingen tredje familj.
Font-proceduren i `brand.md` körs inte om: valet är ärvt från en godkänd cell och att
öppna det vore ett nytt bygge, inte en iteration.

**Accentens frekvenstal, skrivet som ett tal och inte som en känsla** (lånat från
`dope-security`): `#1e5e9c` förekommer **två** gånger på sidan: tesplåtens grund
(`data-sc-drift="#123f68"` är dess mörkare drift-mål, samma roll) och understrykningen i
`Boka ett möte ->` på kortbaksidan. Ingen tredje förekomst. Aldrig som ram, aldrig som
knappfyllning, aldrig i liggaren.

### (7) Vad referenserna gör som cellen måste slå

| Referens | Vad den gör | Vad V3c måste göra för att slå den |
|---|---|---|
| `garden-eight` (målbildens ribba, planens § 7.5) | Ett typografiskt moment och ett skulpturalt moment, åtskilda av tystnad, och ingenting annat ovanför vecket | V3c:s hero innehåller **exakt tre** element: rubrik, kort, en underrad. Ingen kicker, ingen cue, ingen tidsstämpel, ingen andra CTA. Mätbart: `preflight_taste.py` hero-regeln, textelement <= 4 |
| `mattis-studio` (låst av `select.py` OCH av V3b) | Konsolkortet med hörnmarkeringar är **platt**; det är en ritad ram runt typ | V3c:s kort är ett **fysiskt** kort som vänds: det har en baksida, en tjocklek läst ur hårlinjen vid 90 grader, och en ljuskälla som svarar på vinkeln. Mätbart: vid ps = 0,5 syns hårlinjen och ingenting annat av kortet |
| `squarespace` (målbildens ribba, planens § 7.5) | Svarta och vita band som byter genom skala, inte genom färg, med ett statistikblock och noll accent | V3c:s inversioner ska vara lika rena och göras **utan ett enda kort**: materialbytet sker i spalten själv (blått block, papper, mörkt prisblock), och det enda "statistikblocket" är tre sanna priser |
| `oryzo-ai` (topprankad av `select.py`) | Ett fysiskt objekt vrider sig i ett tomt mörkt rum, och det som gör rotationen läsbar är materialet och kanten under ett snedljus | V3c:s kort får inte vara två svarta rektangler som byter plats. Framsidan måste bära **material över hela ytan** och en ljusrespons som ändras med vinkeln. Detta är exakt fyndet i F-007-kontrollen nedan |
| `dope-security` | Anger accentens frekvens som ett tal och kapar skugga till en hårlinje | V3c skriver ut sitt eget accenttal (två förekomster) i decision ledger och har noll `box-shadow` |
| `monologue` | Håller sidans marginaler synliga med ett hårlinjeraster | V3c:s hårlinjer ligger på `--rail-x`-rastret, samma rutnät som rubriken och plåten, inte på egna värden |
| `planhat` (wildcard) | Vikt 300 i stor grad ligger alltid i fotots mörka parti | V3c:s rubrik ligger på den mörka grunden utanför plåten, aldrig över ljuspölen. Mätbart: `contrast_over_media.py --url` per grund |

### (8) Rut-testet

**Kategorins default för "digital byrå", i tre rader**, hållen utanför:

1. Centrerad hero med en badge över rubriken, en fylld primärknapp och en spökknapp
   bredvid, ovanpå en mörk gradient eller ett suddigt kontorsfoto.
2. En logotypvägg med kundmärken, tre lika tjänstekort med ikoner, och en sifferrad med
   "200+ projekt / 15 år / 98 % nöjda kunder".
3. Ett citat med porträtt och ett kontaktformulär i botten, plus en sticky knapp som följer
   med hela vägen.

Var målbilden möter defaulten, och vad som ändras:

| Punkt där målbilden riskerar defaulten | Vad som ändras |
|---|---|
| **Tre tjänster.** Byråer räknar alltid upp tre tjänster; V3b gjorde det två gånger (liggaren och `panel-services`) | `panel-services` **tas bort**. Kvar är liggaren, som är rader med siffror på papper, inte kort med ikoner. Och tjänsteorden repeteras en tredje gång på kortbaksidan, men i **monoregister på 10,5 px**, alltså som en signatur och inte som en tjänstelista |
| **En CTA i heron.** Defaulten sätter "Boka ett möte" som en fylld knapp direkt under rubriken | `Boka ett möte ->` finns bara på **kortets baksida**, alltså först efter att besökaren scrollat genom hela akten, och den är en **typsatt länk** med understrykning i accenten, inte en knapp. Ingen sticky CTA finns |
| **Ordmärket i heron.** Defaulten sätter loggan uppe till vänster i en navrad | Ordmärket finns två gånger: i den tunna toppraden som scrollar bort, och i affischgrad på kortets baksida. Den andra förekomsten är hela akten's poäng, inte chrome |
| **Sifferraden.** Defaulten fyller ut med tal | V3c har **noll** tal utom de tre priserna, som är sanna. TASTE § 4.9 tillåter formen bara med sant innehåll |
| **Kontaktformuläret** | Ersatt av `kontakt@alunix.se` som en textrad och en mailto. Inget formulär, inget fält, ingen skickaknapp |
| **Mörk gradient som grund** | Ersatt av ett kontinuerligt fotografi i gråskala som tonas via `--sc-canvas`-drift. Materialet är en riktig yta, inte en färgövergång |

---

## F-007-kontrollen av hero-plattans nuvarande stillbild

Läst som pixlar: `tests/alunix-concepts-r3/build/assets/k1-stage-pool.webp` (1600x1067,
65 kB) och den byggda folden `tests/alunix-concepts-r5/cells/V3b-chain/shots/desktop-1440--fold.png`.

**Dom: nej, ljuspölen bär inte flippen.** Tre mätbara skäl, i fallande materialitet:

1. **Fram- och baksida delar värde.** Cirka 60 % av bildens yta (hela övre bandet och
   högra tredjedelen) ligger på eller nära ren svart, och baksidan är
   `background: var(--c-black)`. Vändningen går alltså från "svart rektangel" till
   "svart rektangel med text". Det ögat ska läsa som två sidor av ett kort läser som
   samma sida två gånger.
2. **Ingen kant och ingen struktur att förkorta.** Motivet är en mjuk, kantlös ellips av
   ljus på tyg. En Y-rotation blir läsbar genom att raka linjer och kanter förkortas i
   perspektiv; en gradientfläck har inga. `oryzo-ai`:s skivor 02 och 08 visar motsatsen
   mätt: där bär korkens kant och spräckliga material hela rotationen.
3. **Logo-docken sitter på död svart.** I den byggda folden ligger ordmärket i plåtens
   övre vänstra hörn, på ett parti utan textur. Framsidan har alltså inget material där
   ögat landar först.

**Ingen omtagning beställs.** Higgsfield har 0 krediter (free plan, mätt av lead
2026-09-09), så generering är ute; se `runs/V3c/assets/ASSETS.md` för de kvarvarande
vägarna i planens § 10.6 steg 3-ordning och den rekommenderade vägen, och
`runs/V3c/BRIEF.md` § decision ledger för raden som skriver in bytet.
# Alunix r8 — målbildsgrind, cell K3

Skriven av arkitekten 2026-09-09. Denna fil äger **bara** K3. Lead slår ihop V3c, K3 och K4
till `concepts.md`; den här filen skrivs aldrig in i den av mig.

---

## catalogue-select

`python scripts/catalogue/sweep_raw.py` kördes om av mig innan urvalet:

```
sweep: rent - varje kalla under raw/ och processed/ har en post (0 ignorerade).
EXIT=0
```

`python scripts/catalogue/select.py --brief tests/alunix-r8/runs/K3/BRIEF-draft.md --k 4 --wildcard --explain`,
hela utdatan ordagrant:

```
Brief: tests\alunix-r8\runs\K3\BRIEF-draft.md  ->  5 poster

   13  squarespace              modern clean           chaptered editorial
       +3 register | +3 grammatik | +2 category2 | +1 mode | +2 auktoritet | +2 fritext (accent, surface)
   11  aevi-wellness            modern clean           chaptered editorial
       +3 register | +3 grammatik | +2 category2 | +1 mode | +2 fritext (accent, editorial)
   10  beautiful                warm photographic      chaptered editorial
       +3 grammatik | +2 category2 | +1 mode | +4 fritext (accent, category, mono, per)
   10  insign                   modern clean           chaptered editorial
       +3 register | +3 grammatik | +2 category | +1 mode | +1 fritext (per)
   10  mode                     modern clean           split stage
       +3 register | +2 category2 | +1 mode | +2 auktoritet | +2 fritext (accent, mode) | wildcard: utanfor kategorin

Mediastrategi ur posternas egna falt (Photo search) - locken ska inte gissa:
  - squarespace: Unsplash first, Pexels second. - "candid documentary portrait natural light" - "small business owner at work authentic" - "creative studio c
  - aevi-wellness: Unsplash first, Pexels second. - "skincare bottles overlapping flat lay natural light" - "dropper bottle apothecary product close up" - "min
  - beautiful: Unsplash first, Pexels second. - "kitchen countertop natural light warm styling" - "ceramic kitchenware wooden counter lifestyle" - "breakfa
  - insign: Unsplash first, Pexels second. - "tablet mockup website design display" - "phone mockup app interface hand" - "branded delivery van signage"
  - mode: Unsplash first, Pexels second. - "team collaborating desk candid natural light" - "coworkers reviewing screen office documentary" - "data an

catalogue-select skriven: squarespace, aevi-wellness, beautiful, insign, mode  ->  C:\Users\Anton L\anti-slop-design\.impeccable\design-session.jsonl
```

**Avvikelse mot målbildens förväntan, och varför raden ändå gäller.** Planens § 7.5 gissade
`caractere-bois`, `hyperborea`, `wild`, `garden-eight`, `tidvatten`. Ingen av dem föll ut.
Orsakerna är mekaniska och kontrollerade i `index.json`:

- `hyperborea` och `tidvatten` står i `select.py`s `OWN_SITES` och poängsätts negativt —
  de är kedjans egen output, inte referens. Det är avsiktligt och rätt.
- `caractere-bois` är `editorial print` + `gallery/catalog`; målbilden låser själv
  `modern clean` + `chaptered editorial`, så posten får noll på de två tyngsta axlarna.
- `garden-eight` är `editorial print` + `typographic poster` — samma sak.
- `wild` är `modern clean` + `chaptered editorial` + `portfolio` och ligger strax under
  strecket (9 + fritext mot `insign`s 10). Den föll på ett poäng, inte på en princip.

`catalogue-first.md` § 5 gör skriptets rad till den som referensgolvet läser, och § 7 säger
att en tom eller svag träff ska mötas med bredare fråga, inte med minnesarbete. Träffen är
varken tom eller svag. **De fem valda posterna är alltså cellens låsta referenser.** Jag har
läst `caractere-bois` och `wild` som *icke-låsta* jämförelser är tillåtna (r7-promptens rad
"Katalogens övriga poster behöver du inte läsa, men inget förbjuder det") — men de får ingen
rad i reference-locken och ingen rad i "vad cellen måste slå", eftersom en referens som inte
är vald inte får styra bygget. Frågan om planens förväntningslista ska rättas ligger som Q8
i `QUESTIONS.md`.

---

## Lästa referenser

Tre rader per fil: vad den gör · vad jag tar · vad jag lämnar.

### squarespace (primär)

- `entry.md` (hela, inkl. § Motion och § Reference lock) — deklarerar "0 % colourfulness by
  design": sex tokens, alla svarta, vita eller grå, och en uttalad regel att kromatisk färg
  aldrig introduceras på marknadsföringsytan; all mättnad reserveras för användarens egna
  sajter. Clarkson kör hela systemet i vikt 300 vid 60–70 px med −0,05 till −0,06 em.
  **Tar:** reservationen som *struktur* — den enda kromatiska färgen på arket är den ena
  blå, och det enda mättade i bild är kundsajten inne i den ritade öppningen.
  **Lämnar:** achromatisk palett (K3:s papper och bläck är kalla men kromatiska), 0 px-radie
  på knappar (K3 har inga knappar), dokumentärfoto som hero.
- `fold.webp` — fullbleed dokumentärvideo (en frisör), vikt 300-rubrik centrerad i bilden,
  vit skarp knapp, och tre kundsajter som lutande plattor längs nederkanten.
  **Tar:** att kundsajterna är det enda färgstarka i vyn. **Lämnar:** centrerad hero, lutande
  plattor (kortgest), fotot som grund.
- `slices/00–08.webp` — svarta och vita band som växlar utan grå övergång; ett svart
  statband (14M+ / $36B+ / 200+) i vikt 300 vid ~80 px med små versaletiketter under;
  pill-flikar som filter; en accordion med hårlinjer och `+`-tecken; en helsvart footer.
  **Tar:** statbandets form (displaygrad, liten etikett, linjal under) och hårlinje-accordion
  som strukturspråk. **Lämnar:** siffrornas *innehåll* (Alunix har inga sådana tal —
  TASTE § 4.9), pill-flikarna, avatarstacken, partikelsfären i avslutet.
- `extract/squarespace-com-design-language.md` — Motion Language: feel "mixed",
  scroll-linked ja; fem varaktigheter 100–750 ms; två egna kurvor dominerar (216 använd\
  ningar), och en `steps(1, start)` förekommer 49 gånger, alltså en diskret, icke-inter\
  polerad tickning. Material Language: `flat`, avg saturation 0,126, max radie 100 px.
  **Tar:** `steps()`-tickningen som idé för måttsiffrornas uppräkning — en måttsiffra ska
  landa på ett heltal, inte glida. **Lämnar:** de nio gradienterna, de fem box-shadows,
  radie 30/50/100 px.

### insign (sekundär, samma kategori och samma land)

- `entry.md` — svensk fullservicebyrå: tre tjänster som tre helbreda, fullmättade färgband
  (chartreuse, lavendel, orange) så att paletten *är* navigationen; allt utanför banden
  hålls vitt eller nästan svart; bevisen varieras i format (siffror, ansikten, datum).
  **Tar:** principen att navigationen bärs av ett enda konsekvent system som läses före
  texten. **Lämnar:** att systemet är färg (K3 navigerar med ritade symboler), och hela
  bevisapparaten — betygschip, 180+ omdömen, teamgrid, logotypvägg: Alunix har inget av det
  och får inte hitta på det (PRODUCT.md § absences).
- `fold.webp` + `slices/00–07.webp` — vit hero med serif-logotyp och en grotesk rubrik i två
  rader, sedan en mosaikremsa av kundarbeten, tre färgband med varsin liten enhetsbild,
  projektarkiv, ett mörkt statband (5.0/5.0 · 180+ · 2002) över ett kontorsfoto, sex svartvita
  porträtt, nyhetsremsa, mörk kontaktsektion med fyra pill-knappar.
  **Tar:** att varje tjänst får exakt *en* konkret bild av en verklig leverans, aldrig en ikon.
  **Lämnar:** färgbanden, pillformerna, porträttrutnätet, betygschipet, logotypremsan, och
  rubriken som bryts mitt i ordet ("Webbdesig / n") — posten flaggar det själv.
- `extract/insign-se-design-language.md` — Motion: feel "springy", `ease` på 121 ställen,
  en enda overshoot-kurva `cubic-bezier(0.68,-0.55,0.265,1.55)`, plus `fadeIn`,
  `ball-scale-multiple` och `dipi_fade` — alltså stock-chrome ur en WordPress-byggare, inte
  ett författat system. Brand Voice: neutral ton, tredje person.
  **Tar:** varningen — en sida vars rörelse består av bibliotekets keyframes läser som mall.
  Varje rörelse i K3 är författad och namngiven i device-tabellen. **Lämnar:** overshoot
  helt (fjädring hör inte hemma på ett ritark), och tredje person (Alunix röst är vi-form).

### aevi-wellness (sekundär)

- `entry.md` — nästan akromatiskt system med exakt en kromatisk accent reserverad för en enda
  knapp; *varje* textstorlek från 10 px bildtext till 54 px display kör vikt 300, så hierarkin
  bärs av storlek och radavstånd i stället för vikt; elevation är förbjuden rakt av, djupet
  kommer från växlande band och hårlinjer i bläck eller pulverblått.
  **Tar:** hårlinjen som *enda* strukturmedel och det uttryckliga skuggförbudet.
  **Lämnar:** enviktssystemet (K3 behöver två vikter för att skilja utrop från måttsiffra),
  pill-knappen, och den fullbleed produktfotografin som hela systemet vilar på.
- `fold.webp` — ordmärket AEVI satt som ett översiktligt genomskinligt lager ovanpå
  produktfotot, versal underrubrik i vikt 300, en tunn outlinad pill, och en pulverblå
  presslogorad direkt under folden. **Tar:** ingenting av kompositionen. **Lämnar:** ordmärket
  som vattenstämpel, presslogoraden (Alunix har inga presslogotyper), fotot som grund.
- Posten har varken `slices/` eller `extract/` (`extract: none`, `origin: refero`), vilket
  betyder att dess § Motion är **inferred**, inte uppmätt. Jag behandlar den därför som en
  yt- och strukturkälla, aldrig som en rörelsekälla.

### beautiful (sekundär)

- `entry.md` — gräddlinne som canvas överallt i stället för vitt; korallen ransonerad till en
  bokstavlig regel, "ett korallmoment per viewport", vilket är granskningsbart; radie har
  exakt två värden (999 px = klickbart, 0 px = innehåll) och 1 px svart hårlinje ersätter
  både ram och skugga; tracking *öppnar* när graden växer, tvärtemot konventionen.
  **Tar:** den granskningsbara accentregeln, ordagrant överförd: ett blått moment per
  viewport, och det momentet är alltid en sann måttsiffra. **Lämnar:** cream (K3:s papper är
  kallt, AB09-lärdomen och lead-låset), pillformerna, den centrerade logotypen, och den
  öppnande trackingen (måttsatt typografi vill ha stram tracking).
- `fold.webp` — centrerad serif-logotyp flankerad av svartkantade nav-piller, asymmetrisk
  hero 60/40 med produktfoto till vänster och en korallpill till höger, allt på gräddlinne.
  **Tar:** ingenting av kompositionen. **Lämnar:** hela pillspråket och produktfotot.
- Posten saknar `slices/` och `extract/`. Samma behandling som aevi: yta och regel, inte rörelse.

### mode (wildcard, `split stage`, utanför kategorin)

- `entry.md` — inhägnar accenten till exakt en komponenttyp ("the only filled button color in
  the system"), och bygger djup ur en färgstack sage → forest → chartreuse i stället för
  skugga; serifen är låst till 36 px och uppåt i en enda vikt, med tracking som skärps med
  graden. **Tar:** inhägnadsprincipen, skärpt ett steg: K3 inhägnar accenten till en
  *innehållstyp* (en sann uppmätt siffra), inte till en komponent — en komponentregel kan
  drifta när en ny komponent uppstår, en innehållsregel kan inte. **Lämnar:** färgstacken,
  serifen, 16 px-radien, och hela chartreusen.
- `fold.webp` + `slices/00–10.webp` — mörkgrön grund, rubriken satt i chartreusegula
  pratbubbleformer som överlappar ett dokumentärt teamfoto, ett mörkt statkort ("8.2K"), en
  isometrisk lagerillustration med färgkodad teckenförklaring, logotypvägg, citatkort med
  porträtt, och en footer där ordmärket sätts i jättegrad.
  **Tar:** exakt en sak — den färgkodade teckenförklaringen bredvid lagerillustrationen är
  ett *legend*-mönster som gör bilden läsbar utan bildtext. K3:s marginallegend är samma idé,
  ritad i stället för färgad. **Lämnar:** allt annat: bubbelformerna, statkortet, teamfotot,
  logotypväggen, citatkortet.
- `extract/mode-com-design-language.md` — Motion: feel "springy", `ease` 102 gånger, en
  overshoot `cubic-bezier(0.75,0,0.29,1.01)`, en `scroll`-keyframe (translateX 0 → −100 %,
  alltså en marquee). Design System Score 83/100, med "4 font families" och "75 % av CSS
  oanvänd" som egna anmärkningar. **Tar:** varningen mot fyra typsnittsfamiljer — K3 kör två.
  **Lämnar:** overshoot, marquee, och de två box-shadows.

### Anti-referens: `sites/before-ai-slop.html`

Läst som kod, 155 rader. Vad den gör: sticky flytande pill-nav med `backdrop-blur`; centrerad
hero med badge-rad (`inline-flex … rounded-full` med en pulserande prick), ett gradient-satt
ord mitt i rubriken (`.grad-text`, `#1E40AF → #6366F1`), två pill-CTA, en avatarstack av fyra
gradientcirklar; till höger ett **div-byggt "Dashboard preview"-kort** med fyra påhittade
stat-tiles (51 %, 16 %, 17, 1,8 %) och en SVG-sparkline; sedan "Trusted by teams at" med sex
påhittade ordmärken, tre likadana ikonkort med emoji i gradientrutor, ett fyrfältsstatband,
en centrerad CTA och en enradsfooter.

**Vad K3 gör i stället, punkt för punkt:** ingen topprad alls (navigationen är en ritad legend
i marginalen) · ingen badge, ingen pill, ingen gradient, ingen avatar · **ingen låtsasyta
någonstans** — det enda "gränssnitt" som syns på sidan är en riktig Alunix-exempelsajt i en
`<iframe>` på samma origin, och ritningen är uttryckligen inte en UI-mock: den har konturer,
måttlinjer och utrop, aldrig en låtsasknapp, aldrig en låtsasetikett, aldrig lorem · inga
påhittade tal (varje siffra på sidan är 320, 768, 1440, `7 rem`, `96 px`, `16:9`, 26 900,
38 900 eller `Pris vid förfrågan`) · ingen logotypvägg och inga kunder utöver de tre
exempelsajterna · tre tjänster som hårlinjerader i en liggare, aldrig tre kort · tre paket som
en stycklista i en ritad ram, aldrig tre priskort med "populärast" · avslutet är ett
specifikationsblad som blir stilla, aldrig en centrerad CTA som rinner ut i en copyrightrad.

---

## K3 · "Ritningen"

### (1) Auktoritet och vad som viker

**Auktoriteten är ytan** — kallt ritpapper och ett bläck (TASTE § 1 rad 3): allt djup på sidan
kommer av hårlinjer, ton på ton och överlapp mellan ritade lager, aldrig av kort eller skuggor.

**Vad viker, en mening var.** *Typen* viker: den är medelstor, max ~72 px, i två vikter, och
den enda typ som får displaygrad är måttsiffrorna som hör till ritningen. *Bilden* viker till
noll: det finns inga fotografier på sidan, och de tre exempelsajterna visas levande *inuti*
ritade öppningar, aldrig fullbleed och aldrig som skärmbildsplattor ovanpå något. *Färgen*
viker: ett papper, ett bläck och exakt en kromatisk accent som gör exakt en sak. *Rörelsen*
viker överallt utom i signaturakten a1, där den enligt TASTE § 4.8:s r6-precisering är
auktoriteten och typ och innehåll i sin tur viker för den.

### (2) Troplistan

TASTE § 5 punkt för punkt, plus F-006 och gate 47/79.

| Trop | Status i K3 |
|---|---|
| Ikongrid | **Frånvarande.** Tjänsterna 01–03 är hårlinjerader i en liggare; ingen ikon finns i bygget. |
| Gradient-mesh | **Frånvarande.** Grunden är en plan oklch-färg plus en procedurell papperstextur utan färgövergång; ingen `linear-gradient`, ingen `radial-gradient`, ingen mesh. |
| Glasmorfism | **Frånvarande.** Noll `backdrop-filter`, noll halvgenomskinliga paneler. Uttryckligen dödad av F-006. |
| Centrerad hero med badge-rad | **Frånvarande.** Heron är vänsterställd på ett ark med titelblock i övre vänstra hörnet; ingen badge, ingen pill, ingen underrad med prickar. |
| Lila/indigo-accent | **Frånvarande.** Enda accenten är `#1E5E9C`, hue ≈ 252 — Alunix eget Tier 1-bevis, inte en indigoglöd. |
| Skuggade 8 px-kort | **Frånvarande.** Noll `box-shadow` i hela filen, och radien är 0 överallt utom den ritade ramens hörnradier som är 0 de också. Ramar är ritade linjer, inte kort. |
| Stockfoto av leende team | **Frånvarande.** Noll fotografier, noll människor, noll ansikten (Hyperborea-precedensen plus `generation.md` § 8). |
| "h1 48 / h2 32"-skala | **Frånvarande.** Skalan är 5×+ enligt TASTE § 2.4: display 72 px (måttsiffror) mot brödtext 15 px; mellannivån 32 px existerar inte, mellanrubriker är utrop i 12 px mono med tracking. |
| Dekorativa blobbar | **Frånvarande.** Varje sluten form på arket är en kontur som betyder något (en sektion, en öppning, en marginal); inget ritas som dekoration. |
| Tre lika feature-kort | **Frånvarande.** Tre tjänster = tre rader i en liggare med olika radlängd; tre paket = tre rader i en stycklista med ledarpunkter. Aldrig tre lådor bredvid varandra. |
| **F-006** — glaskort, dashboard-över-foto, "live"-punkter, telemetri-chrome | **Frånvarande.** Inget glas, ingen dashboard, ingen live-prick, ingen procentavläsning, ingen statuschip. Cellen har ingen `Live surface`-grammatik och får inte låna dess chrome. |
| **Gate 47** — omritat chrome (webbläsarfält, telefonram) | **Frånvarande.** Exempelsajterna visas i en `<iframe>` utan ritad webbläsarram, utan flikrad, utan URL-fält och utan telefonbezel. Den ritade konturen runt en sajt är en **måttsatt öppning i ritningen**, inte en enhetsram: den bär måttlinjer och ett utrop, den bär aldrig en trafikljusprick eller en adressrad. |
| **Gate 79** — div-byggd låtsas-UI | **Frånvarande, och detta är cellens känsligaste punkt.** Regeln som gäller i R2/R3: **ritningen får rita form, aldrig innehåll.** Tillåtet i SVG: konturer, måttlinjer med pilspetsar, hjälplinjer, snittmarkeringar, skrafferingar och utrop som anger ett mått eller ett namn på en zon (`fold`, `marginal`, `spalt`). Förbjudet i SVG: rektanglar som föreställer knappar, textblock som föreställer text (ingen lorem, inga grå staplar som ska "vara" text), ingen navrad, inget formulär, ingen graf, ingen sparkline, ingen siffra som inte är ett verkligt mått. **Kontrollen:** varje `<rect>`/`<path>` i ritningen ska kunna namnges som "kontur", "måttlinje", "hjälplinje", "skraffering" eller "utrop" — kan den inte det ska den bort. Arkitektens F-007-kontroll i runda 2 läser folden som pixlar och prickar av detta bild för bild. |

### (3) Ett displayelement per skärm (1440 × 900)

Elva skärmar. Ett displayelement var, namngivet. Allt annat i vyn går ner ett steg i grad,
vikt eller mättnad (F-003).

| # | Akt / p | Displayelementet | Vad som viker i samma vy |
|---|---|---|---|
| s1 | a1, p 0–0,12 | **Titelblocket** i arkets övre vänstra hörn (`ALUNIX` · `SEKTION A–A` · `SKALA 1:1`), satt i mono | Arket är annars tomt: författad tystnad före toppen |
| s2 | a1, p 0,12–0,55 | **Sektionskonturen** som ritar sig, en enda linje åt gången | Titelblocket faller till 12 px mono; inga utrop ännu |
| s3 | a1, p 0,55–0,78 | **Måttkedjan** `320 · 768 · 1440` i displaygrad, i blått | Konturen står stilla och går ner till hårlinjevikt |
| s4 | a1, p 0,78–1,0 | **Den fyllda öppningen**: Calyx fold monterad innanför konturen, bläcket kvar som ram | Måttsiffrorna faller till 12 px mono i marginalen |
| s5 | a2 | **Kapitelrubriken** `VI BYGGER ERT VARUMÄRKE.` | Legenden i marginalen dämpas till hårlinje |
| s6 | a3 plate 1 | **Calyx-platen**: ritad ram, hela sidan levande innanför | Rubrikraden ovanför är 12 px mono-etikett |
| s7 | a3 plate 2 | **Hōrai-platen** | Samma |
| s8 | a3 plate 3 | **Hyperborea-platen** | Samma |
| s9 | a4 | **Tjänstenamnen** `Design` / `Utveckling` / `System`, ett per rad, radhöjd `96 px` utropad i marginalen | Underraderna 15 px, radnumren 01–03 i 12 px mono |
| s10 | a5 | **Priskolumnen** `26 900` / `38 900` / `Pris vid förfrågan`, i bläck, inte i blått | Paketraderna 15 px med ledarpunkter |
| s11 | a6 | **`Alla har rätt till bra design.`** innanför den ritade ramen | `kontakt@alunix.se` som 15 px mailto under raden |

### (4) Fingerprint

**Cellens egen rad**, i registrets sex dimensioner:

| Dimension | K3 |
|---|---|
| Grammatik | Chaptered editorial |
| Nav | Ritad teckenförklaring i vänstermarginalen, sticky, ingen topprad alls: fem rader med symbolprov (hårlinje, måttpil, skraffering) plus kapitelnamn, och en ledarlinje som *ritas* från den aktiva raden ut till kapitlets egen kontur |
| Hero-device | En måttsatt sektionsritning av en webbsida i inline-SVG som ritar sig själv ur `stroke-dashoffset` drivet av `--sc-ps` i en pinnad akt, span 2,4; måttsiffrorna räknas upp till sanna värden; akten slutar med att Calyx fold maskas in i den öppning bläcket just ritat |
| Aktform | 6 akter, ~13 vh: `pin` 2,4 → `kinetic` lines → `reveal` ×3 → `flow`+`in` → `count` → `reveal` (avslut). Noll `scrub`, noll `drift`, noll `pan`, noll pekar-devices |
| Avslut | Ett specifikationsblad på samma kalla papper: paketen som stycklista med ledarpunkter och sanna priser, manifestraden och en mailto, allt inuti en ritad ram vars linjer dras in sist; ingen inversion, sidan slutar stilla |
| Signatur | *Ritningen blir sidan*: konturen ritas, den riktiga kundsidan maskas in i öppningen konturen skapat, bläcket står kvar som ram |

**Gaten mot alla 36 byggrader i registret.** `≠` = skiljer sig, `=` = delad. Summan räknar
antal `≠` av sex. Kravet är ≥ 4/6 mot **varje** rad.

| registerrad | grammatik ≠? | nav ≠? | hero ≠? | aktform ≠? | avslut ≠? | signatur ≠? | summa |
|---|---|---|---|---|---|---|---|
| Calyx | `=` båda chaptered editorial | ≠ marginallegend utan topprad vs statiskt border-b-huvud i 3 kolumner | ≠ självritande SVG-sektion vs fullbleed botaniskt foto med scrim | ≠ 6 motorakter med pin 2,4 vs 8 handrullade sektioner med fotoduo och immersion | ≠ ritad specifikation på papper vs mörkinverterad mailto i jättekursiv | ≠ ritningen blir sidan vs ingen (bara IO-fade) | **5/6** |
| Hōrai | ≠ chaptered editorial vs filmic one-shot | ≠ marginallegend vs fixerad bar som mörkblurrar | ≠ ritning vs fullbleed JS-parallaxfoto med jätteordmärke | ≠ pin+kinetic+reveal+flow+count vs scrubbat citatkapitel | ≠ specifikation vs mörk sektion med book.horai.se i jättegrad | ≠ vs bell-curve-scrubbat citat | **6/6** |
| Hyperborea | `=` båda chaptered editorial | ≠ marginallegend, ingen topprad vs sticky header under edition strip med amber CTA-pill | ≠ måttsatt ritning som ritar sig vs statiskt lagrat sol- och skyline-SVG | ≠ motordriven pin 2,4 + count vs 8 sektioner, marquee, ingen motor | ≠ specifikation i ritad ram vs mörk kolofon "write us a letter" | ≠ vs ingen (sol-diskarna är ett system, inte en interaktion) | **5/6** |
| Tidvatten | ≠ chaptered editorial vs filmic one-shot | ≠ marginallegend vs fixerad bar med "Bli medlem"-länk | ≠ ritning vs fullbleed havsfoto med ordmärket satt över hela ramen | ≠ 6 akter utan scrub vs 7 sektioner med pinnat gradscrub | ≠ specifikation på papper vs mörk inverterad mailto i jättegrad | ≠ vs två temperatursiffror som konvergerar | **6/6** |
| Vintergatan | `=` båda chaptered editorial | ≠ marginallegend vs statiskt huvud under edition strip, centrerat ordmärke | ≠ ritning vs typ satt direkt i fotografiet | ≠ 6 akter, ~13 vh vs 11 sektioner med pinnad ordavslöjning | ≠ specifikation vs mörk sektion med kursiv mailto och öppettider | ≠ vs tre ord som förgylls i sekvens | **5/6** |
| Vinterspelen | `=` chaptered editorial (gallery-inflekterad, men samma familj) | ≠ marginallegend vs sticky header med ljuslågemärke och biljettknapp | ≠ ritning vs delat anslag med en inramad målning | ≠ 6 akter utan scenbyte vs 10 sektioner med pinnat kulissbyte | ≠ specifikation i ritad ram vs papperssektion "resan" som matar en mörk 3-kolumnsfooter | ≠ vs sex kulissremsor i vågrörelse | **6/6** |
| before-ai-slop | ≠ chaptered editorial vs ingen av de åtta | ≠ marginallegend vs sticky flytande pill med backdrop-blur | ≠ ritning vs centrerad split med badge, gradientord och div-byggt dashboardkort | ≠ 6 koreograferade akter vs 7 statiska sektioner utan en enda reveal | ≠ specifikation som blir stilla vs centrerad CTA och enradsfooter | ≠ vs ingen alls | **6/6** |
| r1 K1 Svart scen och vit sal | ≠ chaptered editorial vs rhythmic cutlist | ≠ marginallegend vs minimal fixerad toppremsa med ordmärke och mailto | ≠ ritning på kallt papper vs mörk scen med en ljuspöl i fotot | ≠ 6 motorakter vs 4 hårda klipp utan motor | ≠ specifikation vs vit sal med mailto i displaygrad | ≠ vs tre demorutor som lyfter med underglöd | **6/6** |
| r1 K2 Tjänsteledger | ≠ chaptered editorial vs split stage | ≠ marginallegend vs sticky vänsterskena med roterat ordmärke | ≠ ritning vs vitt papper med jättefråga i grotesk och en solid ink-knapp | ≠ 6 akter vs 3 sektioner med fast vänsterspalt | ≠ ritad ram vs mörkt band med systemtexturlinje och tre färgprickar | ≠ vs kapitelfärg som fördjupas via color-mix | **6/6** |
| r1 K3 Instrument | ≠ chaptered editorial vs typographic poster | ≠ marginallegend vs kickerremsa utan nav | ≠ ritning vs displaypåstående på onyx med ett blått handlingsord | ≠ 6 akter med pin vs 5 sektioner på en värdestegsgrund | ≠ specifikationsblad vs en enda påståenderad | ≠ vs siffror som räknar upp med linjal under | **6/6** |
| r1 K4 Journal | `=` båda chaptered editorial | ≠ marginallegend med symbolprov vs enkel toppkickerrad med ordmärke och mailto | ≠ självritande måttritning vs vikt-300-serifrubrik med en atmosfärsplate bredvid | ≠ 6 motorakter, ~13 vh vs 4 handrullade romerska kapitel | ≠ stycklista med sanna priser i ritad ram vs tryckt kolofon som krediterar typsnitt, foto och person | ≠ vs `NN / 03`-räknare på varje plate | **5/6** |
| r1 K5 Affisch | ≠ chaptered editorial vs gallery/catalog | ≠ marginallegend vs textnav i foldens underkant | ≠ ritning vs ordmärket i viewportbredd på en flat färg | ≠ 6 akter vs 3 numrerade helbreda plates | ≠ specifikationsblad vs kontakt som en enda rad | ≠ vs ordmärket som fast bakgrundslager | **6/6** |
| r1 K6 Kortlek | ≠ chaptered editorial vs live surface | ≠ marginallegend vs fixerad flytande pill | ≠ ritning vs solfjäder av tre skärmbilder som foldens huvudobjekt | ≠ 6 akter vs 4 sektioner i drift-parallaxfamiljen | ≠ ritad ram vs ingen egen avslutsform alls | ≠ vs kortleken som blandas om på scroll | **6/6** |
| r2 R1 Squarespace scen | ≠ chaptered editorial vs rhythmic cutlist | ≠ marginallegend vs svart topprad med spökknapp | ≠ ritning vs fullbleed mörkt spotlightfoto med centrerad rubrik | ≠ 6 akter med pin vs 5 helbreda band med hårda klipp, ingen pin | ≠ specifikation vs vit sal med mailto i 72 px | ≠ vs rutor som glider in underifrån | **6/6** |
| r2 R2 Vit remsa | `=` båda chaptered editorial | ≠ marginallegend utan topprad vs vit topprad plus pill-filterrad under heron | ≠ ritning vs vitt typband utan bild | ≠ 6 akter, ~13 vh vs 5 sektioner med mörka projektkort | ≠ ritad specifikation vs tyst vitt kontaktblock utan kolofon | ≠ vs pill-flikar som `:target`-markerar rätt kort | **5/6** |
| r2 R3 Färgband | `=` båda chaptered editorial | ≠ marginallegend med symbolprov vs vit topprad med seriflogotyp och fyra länkar | ≠ måttritning vs vit grund med gemen grotesk rubrik och ingen bild alls | ≠ 6 motorakter vs mosaikremsa plus tre mättade tjänsteband | ≠ specifikation på papper vs mörkt band med manifestrad och mailto | ≠ vs färgbanden som *är* tjänsterna | **5/6** |
| r2 R4 Numrerad process | `=` båda chaptered editorial | ≠ marginallegend, ingen topprad vs mörk topprad med tre länkar och en blå pill-CTA | ≠ ritning på kallt papper vs fullbleed mörkt texturfoto med komprimerad tung rubrik | ≠ 6 akter med pin och count vs 4 sektioner med 01–05 i schweizisk rytm | ≠ ritad specifikation vs mörkt band plus en pill | ≠ vs mono-numren 01–05 som genomgående spår | **5/6** |
| r2 R5 Konsolram | ≠ chaptered editorial vs split stage | ≠ ritad marginallegend vs konsolram med versionstagg, klocka och hörnmärken | ≠ ritning vs ordmärket i en konsolram över ett gråskalefoto | ≠ 6 akter vs 3 sektioner | ≠ specifikation vs vitt block med jätterubrik | ≠ vs hörnmärken fixerade i viewporten | **6/6** |
| r2 R6 Affischordmärke | ≠ chaptered editorial vs typographic poster | ≠ marginallegend vs fixerad minimal rad med cirkelmärke och kontaktpill | ≠ ritning vs ordmärket i viewportbredd med ett fullbleed dokumentärfoto under | ≠ 6 akter vs 5 sektioner utan motor | ≠ ritad ram med stycklista vs off-white kolofon som stänger på mailto som text | ≠ vs tre 12 px färgprover, ett per demorad | **6/6** |
| r3 build (R5+R6) | ≠ chaptered editorial vs split stage | ≠ marginallegend vs fyra fasta hörnmärken som enda chrome | ≠ en ritning vs två heron sida vid sida | ≠ 6 akter med pin vs 9 rena flow-akter i två parallella spalter | ≠ ett specifikationsblad vs Calyx-ram och prisruta som stänger samtidigt i två spalter | ≠ vs sömlinjen som dras från det dockade märket | **6/6** |
| r4 M1 Kontinuerlig grund | ≠ chaptered editorial vs continuous world (lös läsning) | ≠ ritad marginallegend vs tunn topprad som scrollar bort | ≠ ritning vs en helbred levande Tidvatten-iframe som hela första akten | ≠ 6 akter med pin, kinetic och count vs 8 rena flow-akter över en fast grund | ≠ ritad specifikation vs Calyx-ram och prisruta, avsiktligt osynkade | ≠ vs +50 vh-förskjutningen som låter grunden lysa igenom | **6/6** |
| r4 M2 Kapitel med pinnad scen | `=` båda chaptered editorial | ≠ upprätt ritad legend med symbolprov och ledarlinje vs fast folio `0X/05` plus roterad kapitelskena | ≠ självritande måttritning på kallt papper vs ett stilla konsoltitelkort över en gråskalegrund | ≠ 6 akter (pin 2,4, kinetic, reveal ×3, flow, count) vs 3 motorakter (pin 3,2 och två flow) i fem kapitel | ≠ ritad specifikation med stycklista på papper vs inverterad prisruta ensam i kapitel 05 | ≠ vs kapitelskenan som scrollhuvud (`-scrollY` på inre spår) | **5/6** |
| r4 M3 Galleri med rail | ≠ chaptered editorial vs gallery/catalog | ≠ marginallegend vs indexnav med fyra mono-hopplänkar | ≠ ritning vs affischordmärke staplat över konsolkortet | ≠ 6 akter utan pan vs 6 akter med en inbäddad horisontell `pan`-rail span 4,2 | ≠ specifikation i ritad ram vs en prisruta som katalogens sista objekt | ≠ vs ordskrubben med SVG-tråd i marginalen | **6/6** |
| r5 V1 Dokumentär band | ≠ chaptered editorial vs continuous world | ≠ marginallegend vs ärvd tunn topprad som scrollar bort | ≠ ritning vs band med krämpanel 38 % och färgfoto 62 % | ≠ 6 akter med pin vs 8 rena flow-akter | ≠ ritad specifikation vs ärvd Calyx-ram och prisruta, osynkade | ≠ vs krämpanelen som växer över fotot | **6/6** |
| r5 V2 Cinematisk tvätt | ≠ chaptered editorial vs continuous world | ≠ marginallegend vs ärvd tunn topprad | ≠ ritning vs fullbleed ljusstrålefoto under en svart tvätt | ≠ 6 akter, ingen drift vs 9 akter med drift och parallax | ≠ ritad specifikation vs Hyperborea-ram och prisruta, osynkade | ≠ vs tvättlyftet i en rad CSS | **6/6** |
| r5 V3 Plåt i grunden | ≠ chaptered editorial vs continuous world | ≠ marginallegend vs ärvd tunn topprad | ≠ ritning vs inramad plåt med hårlinje på mörk grund och affischrubrik ovanför | ≠ 6 akter vs 8 flow-akter i två spalter | ≠ ritad specifikation vs Calyx-ram och prisruta, osynkade | ≠ vs ljuspölen som vandrar via object-position | **6/6** |
| r5 V3b Plåt i grunden, polerad | ≠ chaptered editorial vs continuous world | ≠ marginallegend vs ärvd tunn topprad | ≠ ritning vs samma inramade ljuspölsplåt, kapad till en fold | ≠ 6 akter med pin och count vs 8 flow-akter | ≠ ritad specifikation vs ärvd Calyx-ram och prisruta | ≠ vs samma ljuspölsvandring | **6/6** |
| r6 A-K1 Skymning (native) | ≠ chaptered editorial vs filmic one-shot | ≠ marginallegend vs minimal fixerad topbar som växlar över grunderna | ≠ ritning vs fullbleed blåtimmesfoto med ljus serifrubrik | ≠ 6 akter utan zoom vs CSS-dolly skala 1 → 22 och pinnad iframe-avslöjning | ≠ ritad specifikation vs nattfoto som landar och håller | ≠ vs kameran som flyger in i ett fönster | **6/6** |
| r6 A-K2 Affischen (native) | ≠ chaptered editorial vs typographic poster | ≠ marginallegend vs tryckt topprad med tickande klocka | ≠ ritning vs ordmärket brutet ALU / NIX med fönster i bokstävernas punsar | ≠ 6 akter vs 7 akter med 320 vh pinnad hero | ≠ ritad specifikation vs bläckark som rullas ner med clip-path | ≠ vs bildremsan som passerar genom bokstäverna | **6/6** |
| r6 A-K3 Konsolen (native) | ≠ chaptered editorial vs live surface | ≠ marginallegend vs app-chrome med 56 px bar och tre numrerade flikar | ≠ ritning vs fullbleed skrivbordsfoto med glaskort som läser tillstånd | ≠ 6 akter vs 6 akter med iframe-scrollTop-växling | ≠ ritad specifikation vs riktigt inmatningsfält som öppnar mailto | ≠ vs scrollen som driver kundsajten i ramen | **6/6** |
| r6 B-K1 Skymning (kedjan) | ≠ chaptered editorial vs filmic one-shot | ≠ marginallegend vs fixerad bar som byter grund per akt | ≠ ritning vs blåtimmesfoto med retuscherad skylt och ljus serifrubrik | ≠ 6 akter vs handrullad lerpad zoom utan kit-pin | ≠ ritad specifikation vs nattfoto som öppnas med clip-path | ≠ vs kameran in i ett riktigt tänt fönster | **6/6** |
| r6 B-K1-nogate | ≠ chaptered editorial vs filmic one-shot | ≠ marginallegend vs fixerad bar plus separat nav i ramen med toggle-knapp | ≠ ritning vs blåtimmesfoto där målfönstret redan syns i vila | ≠ 6 akter vs 6 akter med 3,8 vh heroloop | ≠ ritad specifikation vs andra nattfotot som håller stilla | ≠ vs samma zoom men med opt-in-ram | **6/6** |
| r6 B-K2 Affischen (kedjan) | ≠ chaptered editorial vs typographic poster | ≠ marginallegend vs tunn topprad med `Intl`-klocka | ≠ ritning vs ALU / NIX i variabel Archivo 900 med bildpanel bakom bokstäverna | ≠ 6 akter vs 7 akter med pinnad bildremsa 0 → 55 % | ≠ ritad specifikation vs bläckblock rullat med clip-path till sidans slut | ≠ vs panelglid plus andande block | **6/6** |
| r6 B-K3 Konsolen (kedjan) | ≠ chaptered editorial vs live surface | ≠ marginallegend vs 56 px app-bar med statuschip | ≠ ritning vs dagsljusfoto med krämslöja och glaskort | ≠ 6 akter vs 6 akter med 1:1 scrollTop-mappning | ≠ ritad specifikation vs mörkt avslut med riktigt textfält | ≠ vs besökaren som provkör kundsajtens scroll | **6/6** |
| r7 B-K1 Skymning v2 | ≠ chaptered editorial vs filmic one-shot | ≠ marginallegend vs fixerad topbar med logotypväxling och etikettslot | ≠ ritning i inline-SVG vs 100-bilders förrenderad dolly på `canvas[data-sc-sequence]` | ≠ 6 akter, ingen sekvens vs 4 motorakter med pin span 5,0 | ≠ ritad specifikation vs nattfoto som `reveal` plus färgdrift | ≠ vs kameraåkning som blir en levande sida via `window-track.json` | **6/6** |
| r7 B-K2 Affischen v2 | ≠ chaptered editorial vs typographic poster | ≠ marginallegend vs tunn topprad med klocka och stad | ≠ ritning vs bild maskad genom bokstävernas uppmätta öppningar plus en svartvit plate | ≠ 6 akter vs 5 akter med pin span 3 och diskret radhöjdssteg | ≠ ritad specifikation på oförändrat papper vs grunden som driftar från papper till bläck | ≠ vs papper bakom masken plus andande block | **6/6** |

**Lägsta summa: 5/6**, mot nio rader — Calyx, Hyperborea, Vintergatan, Vinterspelen, r1 K4,
r2 R2, r2 R3, r2 R4 och r4 M2 — och i samtliga fall är den delade dimensionen *grammatik*,
som målbilden själv låser. Ingen rad faller under 4/6.

**Vad jag bytte i planen, och varför.** Ingen ändring krävdes av gaten; alla ändringar nedan
har andra källor.

1. **Referensvalet.** Målbildens förväntade slugs ersattes av `select.py`s faktiska rad
   (`squarespace`, `aevi-wellness`, `beautiful`, `insign`, `mode`). Källa:
   `catalogue-first.md` § 5 — urvalet ska komma ur katalogen, inte ur minnet. Skälen per
   utesluten slug står i § catalogue-select ovan.
2. **Toppen och signaturen slogs ihop till en enda akt.** Målbilden namnger a1 (pin 2,4) som
   toppen *och* lägger "konturen ritas, sedan tonar den riktiga sajten in" i a3. Källa:
   `feel-and-fingerprint.md` § The tell-someone test — "if the tell-someone sentence and the
   signature move point at different moments, one of them is decoration", och § The peak —
   "a page with three peaks has none". Åtgärd: a1 innehåller hela signaturen (linjen ritas →
   måtten räknas → Calyx fold maskas in i öppningen), och a3:s tre plates degraderas
   avsiktligt till kortare `reveal`-akter utan count och utan pin. Toppen ligger kvar där
   målbilden satte den.
3. **Kapitelrubrikens form.** Målbilden citerar `Vi bygger ert varumärke.`; r7-promptens
   § Alunix, fakta anger den ordagranna strängen som `VI BYGGER ERT VARUMÄRKE.`. Källa:
   copy-gate — ordagrann copy bevaras. Versalformen gäller. Se Q9.
4. **a5 tappade `flow`.** Målbilden skriver `flow+in` (liggaren) följt av `count+flow`
   (specifikationen), vilket sätter samma familj två gånger i rad. Källa: `devices.md`
   § device kit — "never the same one twice running". Åtgärd: a5 är `count` (med `parallax`
   på marginalspalten, vilket chaptered editorial uttryckligen lutar sig mot), a6 är `reveal`.
5. **Assetvägen.** Higgsfield är ute (lead mätte `balance` = 0 credits, free plan,
   2026-09-09). Källa: planens § 10.6 fallback steg 3. Papperstexturen blir procedurell
   SVG/CSS och de ritade elementen handförfattad inline-SVG. Se `runs/K3/assets/ASSETS.md`.
6. **Reduced motion utgår.** r7-briefens fält "Reduced motion-planen" finns inte i K3:s
   skelett. Källa: F-011.

### (5) Rörelse

**Motion-tes.**

- **Focal.** Ögat ska följa **linjespetsen** — den punkt där konturen just nu ritas. Allt
  annat i vyn står stilla medan den rör sig. När linjen är klar flyttas fokus en gång, till
  måttkedjan, och en gång till, till öppningen som fylls. Tre fokusskiften i hela akten.
- **Continuity.** Ritordningen är en enda obruten hand: yttre kontur → hjälplinjer →
  måttlinjer → utrop. Ingenting hoppar in i vy, ingenting tonar in ur intet; varje element
  har en startpunkt på arket som redan var synlig som en linjeände. Öppningen som fylls är
  samma rektangel som konturen ritade, inte en ny ruta ovanpå (F-010).
- **Feedback.** Scrollen *är* pennan: 1 % scroll = 1 % ritad linje, båda riktningarna,
  ingen låsning, ingen hijack utöver motorns egen pin. Att scrolla uppåt suddar linjen i
  exakt omvänd ordning. Marginallegendens ledarlinje dras när ett kapitel blir aktivt — det
  är sidans enda hover-oberoende statuskvittens.
- **Budget.** Ritningen är **en** `<svg>` med ≤ 60 `path`/`line`-element och ett enda
  `stroke-dashoffset`-uttryck per bana, alla drivna av **`--sc-ps`** via `calc()` i CSS —
  ingen per-frame JS-skrivning per bana. `will-change: stroke-dashoffset` sätts bara medan
  `0 < ps < 1`. Två typsnittsfiler, båda variabla, båda preloadade, tak 300 kB totalt.
  Iframes monteras via IntersectionObserver, `loading="lazy"`, aldrig fler än en igång
  samtidigt. Måltal (F-014, `motion-smoothness.md` § The bar, vid 4× CPU): `staircase = 0`,
  `max_step ≤ 3 %`, bildtid p95 ≤ 20 ms, noll frames > 33 ms, båda scrollriktningarna mätta.

**Feeling curve** — en känsla per akt, orsaken i andra kolumnen, aldrig två lika i rad.

| # | Känsla | Vad på skärmen orsakar den |
|---|---|---|
| a1 | **Fascination** ← TOPPEN | Ett tomt kallt ark håller stilla i 0,12 av akten, sedan börjar en enda linje färdas, en sidas anatomi växer fram ur ingenting, måtten landar på sina riktiga tal, och öppningen linjen just ritat fylls av en verklig webbplats |
| a2 | **Beslutsamhet** | Kapitelrubriken anländer rad för rad under en linjal som dras samtidigt |
| a3 | **Tillit** | Tre riktiga sajter, en i taget, var och en innanför sin egen ritade ram, i en grad där man kan läsa dem |
| a4 | **Klarhet** | Tre rader, tre ord, en utropad radhöjd `96 px`, ingenting annat i vyn |
| a5 | **Trygghet** | Priserna kommer in som en stycklista och räknas upp till 26 900 och 38 900, med ledarpunkter fram till kolumnen |
| a6 | **Ro** | Ramens fyra linjer dras in runt manifestraden och sidan slutar röra sig |

**Författad tystnad** (måste stå i BRIEF.md så `scroll_verify.py`s `blankBands` inte larmar
falskt): de första 0,12 av a1 är ett medvetet nästan tomt ark med bara titelblocket. Det är
tystnaden före toppen, inte död scroll.

**Tell-someone-meningen.** *"Det är sajten där man ser hemsidan ritas som en ritning, och sen
blir ritningen sidan på riktigt."*

**Device-tabell.** Fem familjer (`pin`, `kinetic`, `reveal`, `flow`, `count`), aldrig samma
två i rad, noll `scrub`, noll pekar-devices. Kolumnen **läser** anger vad varje rörlig sak
läser: `--sc-ps` för allt ögat ser förflytta sig, `--sc-p` bara för cue-opacitet, och
"motorns egen" där motorn själv äger transformen (F-014 regel 1).

| Akt | Sektion | Device (familj) | Span / cue | Vad som rör sig | Läser | Varför just denna |
|---|---|---|---|---|---|---|
| a1 | Ritningen | `pin` (+ `count` staplad) | span 2,4 · dwell 0,35 · cue `0 1 0 0` (greet och håll, ground finns) | `stroke-dashoffset` på varje kontur, hjälplinje och måttlinje; `mask-position`/`clip-path` på öppningen som fylls | **`--sc-ps`** (ritningen, masken); `--sc-p` (utropens opacitet); motorns egen (`count`) | Ramen måste hålla stilla medan en enda idé korsar den — `grammars.md`, pin |
| a2 | Tesen | `kinetic` lines | cue `0.1 0.9 0.15 0.4` | Rubrikens rader ur en mask; linjalen under dem | motorns egen (raderna); **`--sc-ps`** (linjalens `scaleX`) | En kinetisk rubrik per akt, rader nästan alltid rätt — `devices.md` § 5 |
| a3 | Tre plates | `reveal` ×3, riktning `up` | `data-sc-reveal-at="0.15 0.55"` per plate | Ramkonturen ritas, sedan wipeas sajten fram innanför den | **`--sc-ps`** (konturen och wipe-masken) | `clip-path`-wipe = tillståndsbyte; `iris` sparas och används inte alls på sidan |
| a4 | Liggaren 01–03 | `flow` + `in` | stagger 70 ms, reducerad blockpadding (akten följer inte direkt på en pin, men ligger nära) | Tre rader stiger 14 px och tonar in | `--sc-p` (opacitet); motorns egen (14 px-lyftet) | Administrativt innehåll komprimeras, aldrig pinnas — `feel-and-fingerprint.md` § Pacing |
| a5 | Specifikationen | `count` (+ `parallax` på marginalspalten, rate 0,4) | `data-sc-count-at="0.1 0.5"`, 1,4 s, cubic ease-out | Prissiffrorna räknar; marginallegenden driver långsammare än spalten | motorns egen (`count`); **`--sc-ps`** (parallaxen) | Endast sanna tal får en count — `devices.md` § 7; parallax i en spalt är chaptered editorials egen |
| a6 | Avslutet | `reveal` (sidans sista akt) | cue `0.25` (ett värde: sista akten måste hålla) | Ramens fyra linjer dras in i ordning: överkant, höger, underkant, vänster | **`--sc-ps`** | Avslutet ska lösa upp, inte tona ut — `feel-and-fingerprint.md` § The peak |

**Embodiment, en enda** (`feel-and-fingerprint.md` § Being in it: "one or two per page"):
dwell-triggad detalj i a1. Står `--sc-ps` stilla över några frames medan akten är pinnad,
ritas ett extra utrop in i marginalen — spaltavståndet `7 rem` — som aldrig behövdes för att
förstå ritningen. Belöning för att stanna. Inget annat på sidan reagerar på besökaren.

**Rejected-lista** (`find-animation-opportunities`-gaten, fyra frågor per kandidat).

| Kandidat | Frekvens | Syfte | Hastighet | Funktion | Dom |
|---|---|---|---|---|---|
| Tilt på de tre plates vid hover | Varje pekarpassage, alltså mycket ofta | Dekor | ~150 ms | Ingen — och den får ramen att läsa som ett kort i stället för som papper | **Avvisad.** TASTE § 2.3 (aldrig kort), `devices.md` § 9 (tilt konkurrerar dessutom om `transform` med cue) |
| Spotlight som följer pekaren över arket | Konstant | Atmosfär | Kontinuerlig | Ingen | **Avvisad.** Chaptered editorial förbjuder `spotlight` uttryckligen; TASTE § 5 (spotlight noll i materialet) |
| Marquee med de tre exempelsajternas namn | Alltid, i loop | Fylla tomrum | Långsam loop | Ingen; Hyperborea äger redan marquee i registret | **Avvisad.** Fingerprint + TASTE § 3 (marquee hör till consumer-brand och ingen annanstans) |
| Ritrutnät som "andas" bakom allt | Alltid | "Liv" | ~8 s loop | Ingen | **Avvisad.** TASTE § 3 product-focused: "Rörelse: subtil, aldrig breathing". Texturen rastreras en gång och animeras aldrig |
| Magnetisk mailto i avslutet | Vid varje pekarnärmande | Dra blicken till handlingen | ~200 ms | Marginell; grammatiken förbjuder `magnet` | **Avvisad.** `grammars.md`, chaptered editorial bans |
| Ledarlinjen som ritas från legenden till aktivt kapitel | Fem gånger per besök | Säger vilket kapitel som är på skärmen | ~240 ms | **Ja — det är navigationen** | **Behållen.** Den är sidans nav, inte en effekt |

**Delight-tes, en mening.** *Ritningen blir sidan*: samma rektangel som bläcket nyss ritade
fylls med en levande webbplats medan bläcket står kvar som ram, så att besökaren ser
ritningen och det byggda vara samma sak.

### (6) Färg och typ

**Färgstrategi: Restrained.** Den fysiska scenen, i en mening: *ett A2-ark kallt blågrått
ritpapper på ett jämnt upplyst bord, ritat i mörkt petrolbläck, där bara måttsiffrorna är
inkade i en enda blå.*

Namngiven referens för strategin (brand.md: "unnamed ambition becomes beige"):
**Squarespace 0 %-colourfulness, flyttad ett hack** — Squarespace reserverar all mättnad för
användarens egna sajter och håller marknadsföringsytan akromatisk; K3 håller arket
enkromatiskt-kallt och släpper in **exakt ett** kromatiskt värde, inhägnat till en
innehållstyp. Att detta är Restrained och inte Committed är ett medvetet val mot brand.md:s
varning för det timida: mängden *linje* på arket är hög, tätheten är hög, och en drench på ett
ritark vore en osanning om vad en ritning är.

**Föreslagna tokens** (byggaren får skärpa värdena mot uppmätt kontrast, aldrig flytta rollen):

| Token | Värde | Roll |
|---|---|---|
| `--paper` | `oklch(0.95 0.012 230)` | Arket. Kallt, låg chroma, *inte* cream (AB09-lärdomen, låst av lead) |
| `--paper-fold` | `oklch(0.925 0.018 230)` | Andra arket: bara i a3:s plate-marginaler och a6:s ram, som materialbyte mellan akter (TASTE § 4.5) |
| `--ink` | `oklch(0.30 0.055 245)` | Bläcket: all typ, alla bärande konturer. Mörk petrol/ultramarin |
| `--ink-hair` | `oklch(0.52 0.035 240)` | Hjälplinjer, måttlinjer, skrafferingar. Aldrig typ |
| `--blue` | `oklch(0.47 0.13 252)` (= `#1E5E9C`) | **Enda accenten.** Bara måttsiffror i displayskala. Aldrig en yta, aldrig en länk, aldrig en ram |

Rollregler, formulerade så att de går att granska: *ett blått moment per viewport*
(beautiful-regeln, ordagrant övertagen), och *det momentet är alltid en sann uppmätt siffra*
(mode-inhägnaden, skärpt från komponent till innehållstyp). Noll `box-shadow`, noll
`backdrop-filter`, noll gradient, radie 0 överallt.

Kontrast som byggaren måste mäta, inte anta: `--ink` på `--paper` ≈ ΔL 0,65 (godkänt med bred
marginal); `--blue` på `--paper` ligger nära AA-gränsen för normal text och används därför
**bara** i displaygrad — kör `contrast_over_media.py --url` per grund i R3 och skriv siffran
i NOTES.md.

**Typsnitt — brand.md:s fyra steg, utförda.**

1. **Tre varumärkesord, fysiska objekt-ord:** *uppmätt · handrullad · kall.* (Inte "modern",
   inte "elegant". Objektet är ett arkitektritat snitt på blått ritpapper.)
2. **Reflexlistan, alltså de tre jag skulle gripa efter först:** Inter, Space Grotesk,
   IBM Plex Sans/Mono. **Alla tre avvisade** — de står i brand.md:s reflex-reject-lista och
   dessutom i r1–r7-listan.
3. **Katalogen, med objektet i huvudet:** ritningens titelblock, stencilbokstäverna i en
   måttsatt sektion, en verkstadsritnings utrop. Det pekar mot grotesker med mekaniskt,
   mallritat drag och mot en mono som är ritad för teknik, inte för kod-nostalgi.
4. **Korskontroll:** förstavalen sammanfaller inte med reflexen — annars börjar om.

**Förbjudet** (reflexlistan + allt använt i r1–r7): Fraunces · Newsreader · Lora · Crimson ·
Crimson Pro · Crimson Text · Playfair Display · Cormorant · Cormorant Garamond · Syne ·
IBM Plex Mono · IBM Plex Sans · IBM Plex Serif · Space Mono · Space Grotesk · Inter · DM Sans ·
DM Serif Display · DM Serif Text · Outfit · Plus Jakarta Sans · Instrument Sans ·
Instrument Serif · Geist · Geist Mono · JetBrains Mono · Public Sans · Familjen Grotesk ·
Literata · Fragment Mono · Hanken Grotesk · Archivo · Figtree · Cardo · PT Mono · Cinzel ·
Vollkorn · Italiana · Bricolage Grotesque · Manrope · Schibsted Grotesk · Bodoni Moda ·
Noto Serif JP.

**Röst — grotesk med teknisk karaktär. Fem kandidater, rangordnade.**

| # | Snitt | Källa | Varför den passar objektet | Risk |
|---|---|---|---|---|
| **1** | **Chivo** (Omnibus-Type) | Google Fonts, variabel | Vågrätt avskurna terminaler och kvadratiska bukter — bokstäverna läser som dragna med vinkelhake, inte som humanistiska. Äkta 300 och 700 i samma variabla fil, så hela vikthierarkin kostar en fil | Kan läsa som neutral neo-grotesk i små grader; motverkas med stram tracking i display |
| 2 | **General Sans** (Indian Type Foundry, Fontshare) | Fontshare, variabel | Nära geometrisk, mycket jämn färg i text, tydliga öppningar — ett ritbords-neutralt snitt utan mall-doft | Neutraliteten är också dess svaghet: mindre karaktär i 72 px |
| 3 | **Sora** (Jonny Pinhorn) | Google Fonts, variabel | Geometriskt-tekniskt, låga kontraster, mycket rena bågar; sitter bra ihop med en mono | Något kall även i brödtext, vilket kan bli enformigt över hela sidan |
| 4 | **Anybody** (Etcétera) | Google Fonts, variabel bredd | Breddaxeln gör att utrop kan komprimeras som i ett titelblock utan att byta snitt | Karaktärsstark nog att konkurrera med ritningen om uppmärksamheten |
| 5 | **Darker Grotesque** | Google Fonts, variabel | Hög x-höjd och smala former, effektiv i marginallegendens trånga spalt | Displaygraderna blir smalare än ritningens luft vill ha |

**Förstavalet, motiverat enligt de fyra stegen:** **Chivo**. Steg 1:s ord är *uppmätt,
handrullad, kall* — Chivos vågrätt avskurna terminaler och kvadratiserade bukter är precis den
mallritade känslan, och den behåller den i 72 px. Steg 2: den står inte på någon av
förbudslistorna. Steg 3: det fysiska objektet är ett titelblock, inte en tidskriftsrubrik, och
Chivo är ritad för rubriker med stark viktkontrast inom en familj, vilket är exakt vad ett
titelblock gör. Steg 4: den sammanfaller inte med reflexen (Inter / Space Grotesk / Plex).
Praktiskt: en variabel fil täcker 300–700 och håller typsnittsbudgeten (≤ 3 filer, ≤ 300 kB,
`performance.md` § 1).

**Register — mono. Fem kandidater, rangordnade.**

| # | Snitt | Källa | Varför | Risk |
|---|---|---|---|---|
| **1** | **Martian Mono** (Evil Martian) | Google Fonts, variabel bredd | Ritad för tekniska gränssnitt, med bred, stencilaktig ton som läser som påstämplade siffror på en ritning; breddaxeln låter måttsiffrorna sättas brett i displaygrad och smalt i marginalen utan snittbyte | Tung färg; får aldrig sättas i löpande text |
| 2 | **Chivo Mono** (Omnibus-Type) | Google Fonts, variabel | Perfekt metrisk syskonskap med förstavalet i röstrollen | Samma superfamilj kan läsa som *ett* snitt och därmed försvaga registerkontrasten |
| 3 | **Spline Sans Mono** | Google Fonts, variabel | Lugn, smal, mycket läsbar i 11–13 px etiketter | Mindre karaktär i displaygrad, vilket accenten behöver |
| 4 | **Azeret Mono** | Google Fonts, variabel | Kantig och mekanisk, stark i siffror | Egensinnig nog att slåss med ritningen |
| 5 | **Sometype Mono** | Fontshare | Varm och rundad mono med gott siffermaterial | Värmen drar åt fel håll mot ett kallt ark |

**Förstavalet:** **Martian Mono**, i register-rollen och ingen annan: måttsiffror, utrop,
folio, radnummer 01–03, ledarpunkter, titelblockets fält. Rollerna korsar aldrig (TASTE
§ 4.2): Chivo sätter aldrig ett mått, Martian Mono sätter aldrig en rubrik eller brödtext.

**Krock-hantering (lead löser ur listorna).** Om K4 väljer Chivo tar K3 General Sans; om K4
väljer Martian Mono tar K3 Spline Sans Mono (inte Chivo Mono, eftersom superfamiljerisken
kvarstår oavsett).

### (7) Vad referenserna gör som cellen måste slå

| Låst referens | Vad den gör | Vad K3 måste göra bättre |
|---|---|---|
| **squarespace** (primär) | Deklarerar 0 % colourfulness och reserverar all mättnad för kundernas egna sajter, med vikt 300 vid 60–70 px på ett fullbleed dokumentärfoto | Göra reservationen strukturell i stället för bara kromatisk: det enda mättade i vyn är kundsajten *inne i den ritade öppningen*, och det enda kromatiska på arket är en sann måttsiffra. Squarespace visar kundsajter som lutande plattor bredvid heron — K3 visar dem i det hål bläcket ritade, vilket är det Squarespace inte gör |
| **insign** (sekundär) | Låter tre fullmättade färgband *vara* navigationen, så tjänsten känns igen på färg före text; varierar bevisformaten | Navigera med ritade symboler i stället för färg — legendens hårlinje, måttpil och skraffering säger vilket kapitel som är aktivt utan en enda färg — och slå insigns bevisapparat genom att inte ha någon: tre riktiga sajter, inga betyg, inga omdömen, ingen teamgrid |
| **aevi-wellness** (sekundär) | Hårlinjen är enda strukturmedlet, skugga är förbjuden, djup kommer ur bandväxling | Ge hårlinjen betydelse: i aevi är den en ram, i K3 är varje linje antingen en kontur, en måttlinje, en hjälplinje eller en ledare, och en linje utan sådan roll får inte ritas |
| **beautiful** (sekundär) | Ransonerar accenten till en granskningsbar regel: ett korallmoment per viewport | Behålla regelns granskningsbarhet men flytta den till en hårdare grund: ett blått moment per viewport **och** momentet måste vara ett verkligt uppmätt tal, vilket gör regeln omöjlig att drifta in i dekor |
| **mode** (wildcard) | Inhägnar accenten till en komponenttyp (enda fyllda knappen) och bygger djup ur en färgstack utan skugga; färgkodad teckenförklaring gör en illustration läsbar | Skärpa inhägnaden från komponent till innehållstyp, och göra legenden till sidans nav i stället för en bildtext — mode:s legend förklarar en bild, K3:s legend styr sidan |
| **before-ai-slop** (anti-referens) | Bygger ett låtsas-dashboard av `<div>`, sätter ett gradientord i rubriken och möblerar med badge, pill, logotypvägg och tre ikonkort | Aldrig rita innehåll. Ritningen ritar form: kontur, mått, utrop. Varje siffra på sidan är sann. Den enda ytan som visar ett gränssnitt är ett riktigt gränssnitt |

### (8) Rut-testet

**Kategorins default för "digital byrå", tre rader, hållen utanför:**

1. Centrerad hero med en badge-rad ovanför, ett gradientfärgat ord mitt i rubriken, två
   pill-CTA och en avatarstack, över en vit-till-lila grund, med ett dashboardkort till höger.
2. Logotypvägg av kundmärken, tre likadana ikonkort för tjänsterna, ett statband med fyra tal,
   tre priskort där ett bär "populärast".
3. Teamporträtt i rutnät, omdömeskarusell med stjärnor, kontaktformulär, och ett mörkt
   CTA-band som avslutning.

**Var målbilden möter defaulten, och vad som ändras:**

| Punkt där K3 riskerar att sammanfalla | Vad som ändras |
|---|---|
| Tre tjänster i rad (01–03) = samma *form* som tre ikonkort | Tre hårlinjerader i en liggare på ett ark, olika radlängd, radhöjden `96 px` utropad i marginalen. Aldrig tre lådor, aldrig en ikon, aldrig lika bredd |
| Tre paket med priser = samma *form* som tre priskort | En stycklista i **en** ritad ram: rad, ledarpunkter, en kolumn med figurer. Ingen ram runt varje pris, ingen "populärast", ingen jämförelsetabell |
| Att visa kundarbete = samma *form* som logotypvägg eller projektgrid | Tre plates, en i taget, varje plate en **levande** sajt innanför en ritad, måttsatt öppning, etiketterad med de ordagranna raderna. Noll logotyper, noll kundnamn utöver de tre sajterna |
| Sticky topprad med länkar och en CTA-knapp = kategorins reflex | Ingen topprad alls. Navigationen är en ritad teckenförklaring i marginalen, och kontakten är en mailto i löpande text i avslutet |
| "Vi är bäst"-bevis (betyg, antal projekt, år i branschen) | Existerar inte i K3. PRODUCT.md § absences förbjuder dem, och `devices.md` § 7 förbjuder en count utan verifierad siffra. De enda tal på sidan är mått och priser |
| Ett dashboard/produktkort i heron som visar "verktyget" | Heron visar en **ritning**, inte ett gränssnitt. Gate 47/79-kontrollen i troplistan är den mekaniska spärren |

---

## Öppet

- **Q8** (`QUESTIONS.md`): planens § 7.5-lista över förväntade katalogposter för K3 stämmer
  inte med `select.py`s deterministiska utfall. Antagande tills svar: skriptets rad gäller.
- **Q9** (`QUESTIONS.md`): tesrubrikens form, versal eller gemen. Antagande tills svar:
  `VI BYGGER ERT VARUMÄRKE.`, den ordagranna strängen ur r7-promptens § Alunix, fakta.
- **Q10** (`QUESTIONS.md`): de fem live-rubrikerna i kategorin kunde inte hämtas i den här
  sessionen (ingen webbsökning tillgänglig här). Fältet står som `[needs: live-rubriker]` i
  `runs/K3/BRIEF.md` och byggaren fyller det i R1.
# Alunix r8 — målbildsgrind, cell K4

Skriven av arkitekten 2026-09-09/10. Denna fil äger **bara** K4. Lead slår ihop V3c, K3 och
K4 till `concepts.md`; den här filen skrivs aldrig in i den av mig.

Målbilden är `tests/alunix-r8/malbilder/K4.md` (planens § 7.5, ordagrant) och den är
utgångspunkten. Varje avvikelse står utskriven med källa i § (4) *Vad jag bytte i planen*.

---

## catalogue-select

`python scripts/catalogue/sweep_raw.py` kördes om av mig innan urvalet:

```
sweep: rent - varje kalla under raw/ och processed/ har en post (0 ignorerade).
EXIT=0
```

`python scripts/catalogue/select.py --brief tests/alunix-r8/runs/K4/BRIEF-draft.md --k 4 --wildcard --explain`,
hela utdatan ordagrant:

```
Brief: tests\alunix-r8\runs\K4\BRIEF-draft.md  ->  5 poster

   14  paper                    modern clean           split stage
       +3 register | +3 grammatik | +2 category | +1 mode | +2 auktoritet | +3 fritext (accent, chrome, product)
   12  gocanopy                 modern clean           chaptered editorial
       +3 register | +2 category | +1 mode | +2 auktoritet | +4 fritext (bar, nav, pill, product)
   12  harkcap                  modern clean           split stage
       +3 register | +3 grammatik | +1 mode | +5 fritext (flat, gradient, kickers, nav)
   12  mode                     modern clean           split stage
       +3 register | +3 grammatik | +2 category | +1 mode | +3 fritext (accent, mode, tracking)
   11  customer-io              modern clean           live surface
       +3 register | +2 category | +1 mode | +2 auktoritet | +3 fritext (pill, product, under) | wildcard: utanfor kategorin

Mediastrategi ur posternas egna falt (Photo search) - locken ska inte gissa:
  - paper: Unsplash first, Pexels second. - "software interface mockup minimal desk" - "laptop screen design tool workspace" - "minimal desk setup natu
  - gocanopy: Unsplash first, Pexels second. - "city skyline dusk aerial teal" - "financial district buildings evening light" - "downtown skyscrapers blue
  - harkcap: Unsplash first, Pexels second (for the team/office secondary imagery only — the hero itself is a bespoke 3D render, not stock photography). 
  - mode: Unsplash first, Pexels second. - "team collaborating desk candid natural light" - "coworkers reviewing screen office documentary" - "data an
  - customer-io: Unsplash first, Pexels second. - "desk plant natural light soft focus interior" - "home office daylight blurred background" - "minimal works

catalogue-select skriven: paper, gocanopy, harkcap, mode, customer-io  ->  C:\Users\Anton L\anti-slop-design\.impeccable\design-session.jsonl
```

**Avvikelse mot målbildens förväntan, mekaniskt kontrollerad i `index.json`.** Till skillnad
från K3 föll **tre av fem** förväntade slugar faktiskt ut: `paper` (14, högst av alla),
`harkcap` (12) och `mode` (12). Två föll bort. Poängen nedan är körda med samma funktioner
som skriptet självt (`select.score` mot samma brief och samma `prior_primaries`), inte
uppskattade:

| Förväntad slug | Poäng | Registerfält i `index.json` | Varför den föll bort |
|---|---|---|---|
| `paper` | **14** | `modern clean` · `split stage` · `product-focused` / `editorial` | Föll inte bort. Högsta poäng i hela katalogen mot den här briefen. Primär referens |
| `harkcap` | **12** | `modern clean` · `split stage` · `institutional` | Föll inte bort |
| `mode` | **12** | `modern clean` · `split stage` · `product-focused` / `editorial` | Föll inte bort |
| `future-fur` | 11 | `modern clean` · `split stage` · `consumer-brand` | **Ett poäng under k=4-strecket.** Fyra poster ligger på 12 eller mer, så `--k 4` skär av vid 12. Den var dessutom kandidat till wildcard-platsen (kategorin `consumer-brand` ligger utanför briefens `portfolio`), men wildcard-slingan går igenom `ranked` som är sorterad `(-poäng, slug)`, och vid oavgjort 11 kommer `customer-io` före `future-fur` alfabetiskt. Den föll alltså på en bokstav, inte på en princip |
| `dovetail` | 8 | `editorial print` · `split stage` · `institutional` / `editorial` | **Sex poäng under strecket.** Registret är `editorial print`, inte `modern clean`, så den tappar hela `+3 register`; kategorierna är `institutional` / `editorial` mot briefens `portfolio` / `product-focused`, så den tappar hela `+2 category`. Den fick `+3 grammatik | +1 mode | +4 fritext (accent, flat, nav, pill)`. Målbilden låser själv `modern clean`, alltså är det målbildens eget lås som stänger ute den |

**Skillnaden mot K3 är värd att notera:** K3:s förväntade lista föll helt, K4:s föll till 60 %
rätt. Orsaken är att K4:s målbild deklarerar `split stage`, vilket är en ovanlig grammatik i
katalogen, medan K3:s `chaptered editorial` är den vanligaste. Ingen av K4:s förväntade slugar
ligger i `OWN_SITES` (det var K3:s problem), så den mekanismen spelar ingen roll här.

`catalogue-first.md` § 5 gör skriptets rad till den referensgolvet läser. **De fem valda
posterna är cellens låsta referenser.** `future-fur` och `dovetail` får ingen rad i
reference-locken och ingen rad i § (7) — en referens som inte är vald får inte styra bygget.
Frågan om planens förväntningslista ska rättas ligger som **Q11** i `QUESTIONS.md`.

---

## Lästa referenser

Tre rader per fil: vad den gör · vad jag tar · vad jag lämnar.

**Vad jag faktiskt öppnade som pixlar** (jag redovisar det exakt i stället för att påstå
fullständighet): `fold.webp` för alla fem posterna, plus `paper/slices/00, 03, 06, 09`,
`harkcap/slices/02, 04, 08, 11`, `mode/slices/05`, `gocanopy/slices/04`,
`customer-io/slices/03`. Övriga slices är inte lästa och ingen digest nedan påstår något om
dem. Texten är läst i sin helhet för alla fem `entry.md` inklusive § Motion och
§ Reference lock, samt `extract/*-design-language.md` § Motion Language och § Material Language
för alla fem.

### paper (primär, 14 poäng)

- `entry.md` (hela, inkl. § Motion och § Reference lock) — bygger hela sidan på **tvåtons\
  rubriken**: identiska Matter-metriker (samma grad, samma vikt 400, samma tracking) delade på
  två fyllnadsfärger, bläck `#181818` på första raden och skiffer `#83837e` på fortsättningen,
  och posten är uttrycklig om att blanda grader eller snitt mellan raderna förstör devicen.
  Den enda kromatiska accenten, studioblått `#5d8cd7`, är inhägnad till märket och
  kodsyntax — aldrig en knapp, aldrig en länk, aldrig stor text — och den fyllda CTA:n är
  alltid neutralt bläck. Trelagersskuggan är reserverad **enbart** för produktskärmbilden;
  marknadsföringskort hålls platta med 1 px hårlinje.
  **Tar:** tvåtonsdevicen ordagrant som foldens rubrikform, och inhägnadsprincipen flyttad ett
  hack: K4:s enda kromatiska värde bor på **ett enda geometriskt objekt**, delaren, som
  samtidigt är sidans nav, dess chrome och dess signatur.
  **Lämnar:** krämkanvasen (K4:s papper är varmt men inte kräm), radie 4/8/12–24 px (K4 kör
  radie 0), trelagersskuggan helt (K4 har noll `box-shadow`), och det isometriska
  linjerastret i hörnet.
- `fold.webp` (pixlar) — krämgrund, ordmärke vänster med fem gemena textlänkar och `sign up`
  höger; rubriken vänsterställd i tre rader där rad 1 är bläck och rad 2–3 är skiffer; en
  fylld mörk knapp bredvid en spöklänk; under folden ett elevat produktfönster med
  trafikljusprickar, filträd och egenskapspanel; ett svagt isometriskt raster i övre höger.
  **Tar:** att rubrikens tvåtonsbrytning ligger på en *semantisk* gräns, inte en radbrytning.
  **Lämnar:** hela topplänkraden, den fyllda knappen, trafikljusprickarna (gate 47).
- `slices/00, 03, 06, 09` (pixlar) — 00 är folden med de tre mobilartboardsen synliga inne i
  produktfönstret; 03 och 06 visar samma produktfönster i två tillstånd med en överlappande
  terminalpanel och en macOS-liknande dock; 09 är avslutet: två textkolumner med `build log →`
  och `read the announcement →`, sedan en footer där ordmärket `Paper` ligger i jättegrad som
  ett nästan osynligt präglat lager bakom `© 2026` och `team@paper.design`.
  **Tar:** avslutets form — sidan slutar på en textrad och en adress, inte på en CTA-remsa.
  **Lämnar:** det präglade jätteordmärket i footern, docken, och hela produktfönstret
  (K4:s "produktfönster" är två riktiga sajter, inte ett ritat).
- `extract/paper-design-design-language.md` — Motion Language: feel `springy`, scroll-linked
  `yes`, fyra varaktigheter 100/300/500/800 ms, en snabbt avtagande `cubic-bezier(0.16,1,0.3,1)`
  i 32 bruk och en äkta overshoot `cubic-bezier(0.34,1.3,0.64,1)` i 5 bruk. Material Language:
  `flat`, avg saturation 0,226, shadow blur 0 px, max radie 9999 px, `backdrop-filter` nej,
  6 gradienter.
  **Tar:** `cubic-bezier(0.16,1,0.3,1)` som cue-kurva; den är rätt familj för ett kritiskt
  dämpat system. **Lämnar:** overshoot-kurvan helt (spring damping 1,0 betyder per definition
  ingen översläng), radie 9999 px, och de sex gradienterna.

### harkcap (sekundär, 12 poäng, `split stage`)

- `entry.md` — låter **ett enda renderat objekt** bära hela auktoriteten och håller rubriken
  liten i förhållande till det; kör hela sidan på en grotesk i alla grader så att typen aldrig
  konkurrerar; återvänder till heroобjektets exakta material **en gång**, för talen
  (2013 / $2.1B+ / 70+ / 4 lagda över en närbild av samma glas); och håller lagets identitet
  **undanhållen tills hover** — en lista med grå namn där raden under pekaren blir helsvart och
  ett porträtt tonar in bredvid. Postens egen § What to leave är hård mot sig själv: objektet
  "carries no explicit metaphor tied to NAV financing".
  **Tar:** undanhållandet som princip, flyttat från pekare till berättelse — K4 undanhåller
  inte identiteten hos en person utan **halva argumentet**: "efter"-sidan finns hela tiden på
  skärmen men blir inte hel förrän delaren passerat.
  **Lämnar:** 3D-renderingen (K4 har noll genererat material), talen över glaset (Alunix har
  inga sådana tal, PRODUCT.md § absences), hela laget, och `Click to Expand`-navet.
- `fold.webp` (pixlar) — nästan hela viewporten är ett blågrått glasblock i studioljus;
  ordmärket uppe till vänster, en halvgenomskinlig blå navpanel uppe till höger med
  `+ Click to Expand` och tre länkar, och rubriken `Pioneers in NAV financing` i vitt, lågt
  till vänster, satt **litet** mot objektet.
  **Tar:** proportionen — objektet stort, typen liten. K4:s objekt är två sajter, typen är en
  rad. **Lämnar:** hela panelnavet, glaset, den blå duotonen.
- `slices/02, 04, 08, 11` (pixlar) — 02: vit yta, två grå knappkort (`Our Story`, `Our Solutions`),
  en prickmärkt kicker `● Core Stats` och sedan statbandet lagt direkt på glasnärbilden;
  04: hover-listan med tolv namn i ljusgrått, `Emily Oppenheimer` i helsvart och ett porträtt
  centrerat över listan; 08: nyhetslistan med `News`/`Insights`-chips, datumrader och pilar,
  plus ett mörkblått fyllt kort `Explore More News & Insights`; 11: avslutet, glaset igen och
  sedan en helsvart footer i tre kolumner.
  **Tar:** exakt en sak — att en **lista med hårlinjer mellan raderna** kan bära ett helt
  avsnitt utan ett enda kort. K4:s skillnadsliggare är samma form.
  **Lämnar:** chipsen, det fyllda blå kortet, den svarta footern, porträtten.
- `extract/harkcap-com-design-language.md` — Motion: feel `smooth`, scroll-linked `yes`,
  varaktigheter 1 ms / 200 ms / 300 ms, nästan allt på ren `ease` (186 bruk), plus
  `--transition-smooth: all 400ms ease-out`. Material: `flat`, avg saturation 0,32,
  shadow profile `none`, 0 gradienter, `backdrop-filter` nej.
  **Tar:** `shadow profile: none` och `0 gradienter` som bevis på att ett tungt visuellt hero
  inte behöver ett enda djupknep under sig. **Lämnar:** `transition: all` (uttryckligen
  förbjuden i `performance.md`), och 1 ms-tillståndet.

### mode (sekundär, 12 poäng, `split stage`)

- `entry.md` — inhägnar accenten till **exakt en komponenttyp** ("the only filled button
  color in the system"), låser serifen till 36 px och uppåt i en enda vikt, ökar den negativa
  trackingen med graden (−0,72 px till −2,98 px), delar radien i exakt två roller (4 px
  klickbart, 16 px innehållande) och bygger djup ur en färgstack sage → forest → chartreuse
  i stället för skugga.
  **Tar:** inhägnadsprincipen, skärpt från komponent till **objekt**: `#1E5E9C` finns bara på
  delaren, och delaren är ett objekt som existerar exakt en gång på sidan. En komponentregel
  kan drifta när en ny komponent uppstår; ett objekt som bara finns en gång kan inte drifta.
  Tar också regeln att tracking skärps med graden.
  **Lämnar:** färgstacken, serifen, chartreusen, båda radievärdena, och `Signature move`
  (det mörkgröna statkortet med `8.2K`) helt: det är ett kort, och talet är inte Alunix.
- `fold.webp` + `slices/05` (pixlar) — mörkgrön grund, en vit navpanel med två pillknappar
  ovanpå; rubriken satt i tre överlappande chartreusegula pratbubbleformer; ett dokumentärt
  teamfoto och ett skärmfoto under; ett mörkgrönt statkort `8.2K ▲12.16%` med ett stapeldiagram;
  05 visar en isometrisk lagerillustration med färgkodad teckenförklaring
  (`TRANSFORMATION` / `WAREHOUSE` / `INGESTION` / `RAW DATA`) och därunder en logotypvägg
  (Atlassian, Bloomberg, Canva, Imperfect, Zillow).
  **Tar:** ingenting av kompositionen. **Lämnar:** bubbelformerna, teamfotot, statkortet,
  stapeldiagrammet, logotypväggen — hela raden är PRODUCT.md § absences.
- `extract/mode-com-design-language.md` — Motion: feel `springy`, `ease` 102 bruk, fem
  varaktigheter 150 ms–1 s, en overshoot `cubic-bezier(0.75,0,0.29,1.01)` i 3 bruk, en
  `scroll`-keyframe (marquee). Material: `flat`, avg saturation 0,425, max radie 50 px,
  1 gradient. Design System Score-anmärkningar: "4 font families", "75 % av CSS oanvänd".
  **Tar:** varningen mot fyra typsnittsfamiljer — K4 kör två, roller som aldrig korsas.
  **Lämnar:** overshoot, marquee (Hyperborea äger den i registret), och radie 50 px.

### gocanopy (sekundär, 12 poäng, ny mot målbildens lista)

- `entry.md` — duotonar en kategoridefault-bild (skyline) i produktens egen accentfärg så att
  ett välkänt auktoritetsmotiv dras in i varumärkets palett; använder en mono **enbart** för
  system-status-etiketter i versal och öppen tracking; gör hero-videon **klick-för-att-spela**
  i stället för autoplay; och bryter från heroets mörka fotografiska register till en ljus,
  ren sektion för processförklaringen, med motiveringen att stämning och klarhet är olika jobb.
  Signature move: att **rama in rubriken med två små monoetiketter**, en ovanför som anger
  publiken och en under som anger det tekniska påståendet, så att meningen flankeras av
  maskinröst i stället för att stöttas av en underrubrik.
  **Tar:** inramningen, roterad 90°. K4:s två monoetiketter `Före` och `Efter` sitter till
  **vänster och höger** om rubriken i stället för över och under, så att metadata namnger de två
  halvorna i stället för att flankera ett påstående. Det är exakt två monoetiketter på hela
  sidan, vilket håller målbildens tak (≤ 4).
  **Lämnar:** duotonen, skylinen, videon, den klibbiga annonsremsan, pillnavet.
- `fold.webp` + `slices/04` (pixlar) — folden är ett skymningsfoto av Chicagos skyline under
  en teal duoton, med ett flytande pill-nav i toppen, en outlinad monoetikett
  `PURPOSE-BUILT FOR INSTITUTIONAL REAL ESTATE INVESTORS`, en serifrubrik i två rader, en andra
  monoetikett `AI-NATIVE FROM DAY ONE`, och ett videokort med `Click to play`; nederst en
  neongrön annonsremsa. 04 visar en mörkgrön sektion med rubriken `Evidence from institutional
  investors` centrerad och ett svagt kort med `Decision-ready intelligence`.
  **Tar:** ingenting av kompositionen. **Lämnar:** duotonen, pillnavet, annonsremsan, videon,
  och den centrerade rubriken (split stage förbjuder centrerad copy uttryckligen).
- `extract/gocanopy-tech-design-language.md` — Motion: feel `responsive`, scroll-linked `yes`,
  tre varaktigheter 150/300/500 ms, `cubic-bezier(0.4,0,0.2,1)` (8 bruk) för färg och
  `cubic-bezier(0,0,0.2,1)` (16 bruk) för transform/scale/rotate, **noll keyframes** i
  stilmallen. Material: `flat`, avg saturation 0,384, shadow blur 0 px, max radie 16 px,
  0 gradienter.
  **Tar:** uppdelningen — en kurva för färg, en annan för förflyttning. K4 använder samma
  uppdelning: cue-opacitet får `cubic-bezier(0.16,1,0.3,1)`, delarens fjäder är kritiskt
  dämpad och har ingen bezier alls. **Lämnar:** radie 16 px.

### customer-io (wildcard, `live surface`, utanför kategorin)

- `entry.md` — låter rubriken göra varumärkesarbetet genom att färga om enstaka ord i
  produktens accentpalett; **iscensätter produktskärmbilden inne i ett fotograferat rum**
  (dashboard på ett verkligt skrivbord med växter och dagsljus) för att låna ett livsstilsfotos
  trovärdighet åt en skärmbild; svarar på invändningar i tre små bockar under CTA:n; och visar
  två produktytor i samma skärmbild för att hävda en andra förmåga utan ett andra hero.
  **Tar:** exakt en sak, som **avvisning**. Postens signaturdrag är att *låna* trovärdighet åt
  en skärmbild. K4 behöver inte låna någon: produkten körs live i ramen och går att använda
  (PRODUCT.md princip 1). Den posten är cellens tydligaste "vad vi slår".
  **Lämnar:** regnbågsorden i rubriken, pillknapparna, bockraden, logotypväggen, chattpanelen.
- `fold.webp` + `slices/03` (pixlar) — vit grund, topprad med två pillknappar varav en har en
  grön glödring; rubriken i två rader mörkt petrol; två pillknappar och tre grå bockar
  (`14-day free trial` · `No credit card required` · `Cancel anytime`); under folden ett
  produktfönster iscensatt i ett suddigt dagsljusrum. 03 visar en femdelad mörk bildremsa med
  produktnamn i nederkant, sedan en sektion `Meet your AI Agent` med en chattbubbla över ett
  grynigt beige fält.
  **Tar:** ingenting av kompositionen. **Lämnar:** allt: pillarna, glödringen, bockraden,
  bildremsan, chattbubblan (F-006).
- `extract/customer-io-design-language.md` — Motion: feel `responsive`, scroll-linked `yes`,
  två varaktigheter 200/400 ms, ease-out-familjen `cubic-bezier(0.19,1,0.22,1)` i 184 bruk;
  keyframes lutar åt ambient dekor (`marquee`, `text-gradient`, `shine`, `meteor`,
  `border-beam`). Material: `flat`, avg saturation **0,627** (högst av de fem), max radie 6 px.
  **Tar:** varningen. `meteor` och `border-beam` är precis den klass av rörelse
  `find-animation-opportunities`-gaten avvisar: hög frekvens, noll funktion.
  **Lämnar:** hela keyframe-uppsättningen.

### Anti-referens, som är **innehåll** på den här sidan: `sites/before-ai-slop.html`

Här skiljer sig K4 från alla andra celler i kedjan: anti-referensen står inte bredvid bygget,
den **körs live på vänstra halvan av folden**, ärligt etiketterad `En typisk mallsida`. Det är
avsiktligt och etiketterat, aldrig en påhittad kund.

Läst som kod och mätt, inte beskriven ur minnet (kommandon och utdata i § Mätning nedan):
sticky flytande pill-nav med `backdrop-blur`; centrerad hero med badge-rad, ett gradientsatt
ord mitt i rubriken (`.grad-text`, `#1E40AF → #6366F1`), två pill-CTA, en avatarstack av fyra
gradientcirklar; till höger ett **div-byggt "Dashboard preview"-kort** med fyra påhittade
stat-tiles och en SVG-sparkline; sedan sex påhittade ordmärken, tre ikonkort, ett
fyrfältsstatband, en centrerad CTA och en enradsfooter. Sju hexfärger, 20 `rounded-*`,
8 gradienter, **noll fotografier**.

**Vad K4 gör i stället, punkt för punkt:** ingen topprad alls (delaren är chromen) · ingen
badge, ingen pill, ingen gradient, ingen avatar i **K4:s eget lager** · ingen låtsasyta
någonstans — de enda gränssnitt som syns på sidan är riktiga gränssnitt, ett av dem är
antagonisten själv och det är utskrivet · inga påhittade tal: varje siffra i skillnadsliggaren
är mätt ur de två filerna på disk, och varje annan siffra är `26 900`, `38 900` eller `01–03` ·
ingen logotypvägg, inga kunder utöver de tre exempelsajterna · tre tjänster som rader i en
liggare, aldrig tre kort · tre paket som en stycklista, aldrig tre priskort · avslutet är en
kollaps till en kolumn på varmt papper, aldrig en centrerad CTA som rinner ut i en copyrightrad.

---

## Mätning

Skillnadsliggaren i § (5) och i `runs/K4/BRIEF.md` bygger **bara** på tal jag mätt själv.
TASTE § 4.9: siffror får vara textur bara om de är sanna.

Servern startades från repo-roten enligt PRODUCT.md § Operating Context:

```
python "C:/Users/Anton L/.claude/skills/design/scripts/serve.py" --port 3399 --root .
```

### `measure.py` mot mallsidan, ordagrant

```
python "C:/Users/Anton L/.claude/skills/design/scripts/measure.py" http://localhost:3399/sites/before-ai-slop.html
```

```json
{
  "http://localhost:3399/sites/before-ai-slop.html": {
    "height": 2016,
    "textElements": 61,
    "distinctFontSizes": 9,
    "fontSizeRange": [
      12,
      60
    ],
    "topSizes": [
      60,
      48,
      36,
      30,
      20,
      18,
      16,
      14
    ],
    "distinctTextColors": 9,
    "distinctWeights": 4,
    "families": {
      "Inter": 61
    },
    "serifTextElements": 61,
    "accentTextElements": 0,
    "accentAtDisplayScale": 0,
    "hairlineRules": 12,
    "distinctBackgrounds": 8,
    "contentLeft": 0,
    "contentRight": 1440,
    "contentWidthUsed": 1440,
    "images": 1
  }
}
```

### `measure.py` mot Calyx, ordagrant

```
python "C:/Users/Anton L/.claude/skills/design/scripts/measure.py" http://localhost:3399/sites/calyx.html
```

```json
{
  "http://localhost:3399/sites/calyx.html": {
    "height": 5020,
    "textElements": 68,
    "distinctFontSizes": 11,
    "fontSizeRange": [
      11,
      130
    ],
    "topSizes": [
      130,
      101,
      88,
      54,
      51,
      36,
      30,
      24
    ],
    "distinctTextColors": 4,
    "distinctWeights": 1,
    "families": {
      "PT Mono": 33,
      "Cardo": 35
    },
    "serifTextElements": 35,
    "accentTextElements": 0,
    "accentAtDisplayScale": 0,
    "hairlineRules": 10,
    "distinctBackgrounds": 2,
    "contentLeft": 32,
    "contentRight": 1408,
    "contentWidthUsed": 1376,
    "images": 0
  }
}
```

### Kompletterande källräkning, ordagrant

`measure.py` räknar inte kort, gradienter eller fotografier. De talen kommer ur en
deterministisk räkning i de två filerna:

```
python -c "
import re
for f in ['sites/before-ai-slop.html','sites/calyx.html']:
    t=open(f,encoding='utf-8').read()
    hexes=set(x.lower() for x in re.findall(r'#[0-9A-Fa-f]{6}\b',t))
    ok=set(re.findall(r'oklch\([^)]*\)',t))
    print('==',f)
    print('   distinkta hexfarger:',len(hexes), sorted(hexes))
    print('   distinkta oklch-varden:',len(ok))
    print('   shadow-utiliteter:',re.findall(r'[a-z-]*shadow-[a-z0-9\[\]_.,()#/-]*',t))
    print('   rounded-utiliteter:',sorted(set(re.findall(r'rounded-[a-z0-9]+',t))))
    print('   kortformer rounded-(lg|xl|2xl|3xl):',len(re.findall(r'rounded-(?:xl|2xl|3xl|lg)',t)))
"
```

```
== sites/before-ai-slop.html
   distinkta hexfarger: 7 ['#1e40af', '#1f2937', '#6366f1', '#8b5cf6', '#ec4899', '#f59e0b', '#fbfaf7']
   distinkta oklch-varden: 0
   shadow-utiliteter: ['shadow-sm', 'shadow-xl']
   rounded-utiliteter: ['rounded-2xl', 'rounded-full', 'rounded-lg']
   kortformer rounded-(lg|xl|2xl|3xl): 8
== sites/calyx.html
   distinkta hexfarger: 0 []
   distinkta oklch-varden: 11
   shadow-utiliteter: ['drop-shadow-[0_2px_30px_rgba(0,0,0,0.5)]']
   rounded-utiliteter: []
   kortformer rounded-(lg|xl|2xl|3xl): 0
```

Gradienter och fotografier, samma metod:

```
before-ai-slop.html:  gradient 8  (2 varumarkesfyllningar .grad/.grad-text,
                                   4 avatarcirklar bg-gradient-to-br,
                                   2 <linearGradient> i den falska sparklinen)
                      url() 1     (url(#g), referens till sparklinens gradient)
                      <img> 0     picture 0   srcset 0   unsplash 0
calyx.html:           gradient 2  (bada ar scrim over foto: en bakgrundsscrim,
                                   en bg-gradient-to-b fran ink/10)
                      url() 5     (1 data:image/svg+xml grain + 4 Unsplash-fotografier)
                      <img> 0     picture 0   srcset 0   unsplash 5
```

**En rad som målbilden namnger men mätningen inte bär.** Målbilden räknar upp `hårlinjer` som
en skillnadsrad. `measure.py` säger `hairlineRules` **12 för mallsidan och 10 för Calyx** —
alltså fler hårlinjer på den sida vi argumenterar emot. Raden är därför **struken ur
skillnadsliggaren**. Källa: TASTE § 4.9 och lead-instruktionens "sanna, mätta skillnader
bara". Att behålla den och vända på tolkningen vore precis den sortens tal-som-textur regeln
finns för att stoppa. Ersättningsraden är `Sidmarginal vid 1440`, som är mätt och entydig
(`contentWidthUsed` 1440 mot 1376, alltså 0 px mot 32 px gutter).

---

## K4 · "Före/Efter"

### (1) Auktoritet och vad som viker

**Auktoriteten är produkten** — de två sajterna som objekt, ofria i mitten av ramen
(TASTE § 1 rad 4): argumentet är inte en mening om design, det är två färdiga webbplatser i
samma rektangel, och besökaren avgör själv.

**Vad viker, en mening var.** *Typen* viker: den är nästan tyst, en enda rad i lässtorlek+
tvärs över sömmen plus två monoetiketter, och den enda typ som får displaygrad efter folden är
skillnadsliggarens mätta tal och de tre sista rubrikerna. *Bilden* viker till noll: det finns
inga fotografier i K4:s eget lager, och all fotografi som syns tillhör de sajter som visas.
*Färgen* viker: ett varmt papper, ett varmt bläck och exakt en kromatisk accent som bara får
finnas på delaren. *Rörelsen* viker överallt utom i a1, där den enligt TASTE § 4.8:s
r6-precisering är auktoriteten i set-piece-akten och typ och innehåll viker för den.

### (2) Troplistan

TASTE § 5 punkt för punkt, plus F-006 och gate 47/79. **Statusen gäller K4:s eget lager.** Det
som syns inuti `sites/before-ai-slop.html` är antagonistens egenskaper, inte K4:s, och är
utskrivet som sådant på skärmen.

| Trop | Status i K4 |
|---|---|
| Ikongrid | **Frånvarande.** Tjänsterna 01–03 är tre rader ur en mask i a4; ingen ikon finns i K4:s eget lager. |
| Gradient-mesh | **Frånvarande.** Grunden är en plan varm oklch-färg. Noll `linear-gradient`, noll `radial-gradient`, noll mesh i K4:s CSS. Antagonistens åtta gradienter är mätta och skrivs ut som ett tal i skillnadsliggaren, inte imiterade. |
| Glasmorfism | **Frånvarande.** Noll `backdrop-filter`, noll halvgenomskinliga paneler. Uttryckligen dödad av F-006. Delaren är en opak hårlinje, inte en glasremsa. |
| Centrerad hero med badge-rad | **Frånvarande, och dubbelt spärrad.** Rubriken är sömankrad och vänsterviktad, aldrig centrerad; `grammars.md` split stage förbjuder centrerad copy uttryckligen. Ingen badge, ingen pill, ingen prickrad. |
| Lila/indigo-accent | **Frånvarande.** Enda accenten är `#1E5E9C` = `oklch(0.47 0.13 252)`, Alunix eget Tier 1-bevis. Antagonistens `#6366F1` och `#8B5CF6` finns bara inuti dess egen ram och räknas i liggaren. |
| Skuggade 8 px-kort | **Frånvarande.** Noll `box-shadow` och radie 0 överallt i K4:s lager. Skillnadsliggaren är hårlinjerader, aldrig kort (harkcap-formen). |
| Stockfoto av leende team | **Frånvarande.** Noll fotografier, noll människor, noll ansikten i K4:s lager. Hela `harkcap`-postens porträttmekanik är avvisad. |
| "h1 48 / h2 32"-skala | **Frånvarande.** Skalan är ≥ 5× enligt TASTE § 2.4: display ~112 px (avslutsrubriken och liggarens tal) mot brödtext 15 px; mellannivån 32 px existerar inte, mellanrubriker är monoetiketter i 11 px med tracking. |
| Dekorativa blobbar | **Frånvarande.** Den enda formen i K4:s lager utöver typ är delarens hårlinje, och den är sidans nav. Inget ritas som dekoration. |
| Tre lika feature-kort | **Frånvarande.** Tre tjänster = tre rader i olika längd; tre paket = en stycklista med ledarpunkter. Aldrig tre lådor bredvid varandra, aldrig "populärast". |
| **F-006** — glaskort, dashboard-över-foto, "live"-punkter, telemetri-chrome | **Frånvarande i K4:s lager, och detta är den känsligaste punkten i cellen.** Antagonisten *innehåller* ett div-byggt dashboardkort. K4 får därför aldrig visa ett eget tal om delarens läge, aldrig en procentavläsning, aldrig en statuschip, aldrig en live-prick, aldrig en etikett som säger vilket läge sidan är i. **Kontrollen i R2/R3:** varje element i K4:s eget lager ska kunna namnges som *rubrik*, *monoetikett*, *liggarrad*, *hårlinje* eller *delare*. Kan det inte det ska det bort. |
| **Gate 47** — omritat chrome (webbläsarfält, telefonram) | **Frånvarande.** De två sajterna monteras som `<iframe>` utan ritad webbläsarram, utan flikrad, utan URL-fält, utan trafikljusprickar och utan telefonbezel. Delaren är en linje mellan två ytor, inte en ram runt någon av dem. `paper`-postens produktfönster med trafikljusprickar är uttryckligen lämnat. |
| **Gate 79** — div-byggd låtsas-UI | **Frånvarande.** K4 bygger noll gränssnitt. Varje gränssnitt på skärmen är en riktig fil som serveras från samma origin. Skillnadsliggaren är typografi, inte en graf, inte en sparkline, inte ett stapeldiagram — `mode`s statkort och `customer-io`s chattpanel är båda avvisade av det skälet. |
| **Jämförelseslider-klichén** (K4:s egen tillagda rad) | **Neutraliserad, på fyra mekaniskt kontrollerbara sätt.** (a) **Ingen affordans ritas:** ingen knopp, ingen ikon, ingen dubbelpil, ingen "dra"-text. Träffytan är 44 px bred och osynlig, och `cursor: col-resize` är hela affordansen (gate 88 + `apple-design` § fine pointer). (b) **Delaren är inte en widget, den är sidans chrome:** den är hela navigationen, den enda beständiga formen och det enda kromatiska värdet — en jämförelseslider är en komponent i en sida, K4:s delare *är* sidan. (c) **Den återgår aldrig till mitten.** En slider är en leksak som nollställer sig; K4:s delare har ett mål som ägs av scrollpositionen, och ett släpp lämnas vidare till det målet, inte till 50 %. (d) **Före-sidan är ärligt märkt.** Klichén bygger nästan alltid på ett påhittat "före" som är gjort fult med flit; här är "före" en verklig fil i repot, etiketterad `En typisk mallsida`, och varje påstående om den är ett mätt tal med kommandot utskrivet. |

### (3) Ett displayelement per skärm (1440 × 900)

Nio skärmar. Ett displayelement var, namngivet. Allt annat i vyn går ner ett steg i grad, vikt
eller mättnad (F-003).

Målbilden räknar sex skärmar (s1–s6). Jag delar den pinnade akten i tre skärmar, eftersom
2,4 spans vid 1440 × 900 är tre distinkta vyer som var och en måste kunna skärmbildas och
granskas var för sig, och lägger till tjänsteliggaren som egen skärm eftersom aktlistan
innehåller den men skärmlistan inte gör det. Källa: F-007 (målbildskontrollen körs skärm för
skärm, så varje granskningsbar vy måste finnas i listan).

| # | Akt / ps | Displayelementet | Vad som viker i samma vy |
|---|---|---|---|
| s1 | a1, ps 0–0,10 | **Tvåtonsrubriken** `Er hemsida är nutidens visitkort`, en rad, satt tvärs över sömmen: dämpad `--ink-2` över "före", `--ink` över "efter" | De två sajterna står helt stilla; `Före` / `Efter` som 11 px monoetiketter vid var sin sida av rubriken |
| s2 | a1, ps 0,10–0,68 | **Delaren** — den lodräta hårlinjen med `#1E5E9C`, på väg vänsterut | Rubrikens före-halva tunnas (`wght` 500 → 200) och tracking öppnar; mallsidans mättnad faller |
| s3 | a1, ps 0,68–1,0 | **"Efter"-ytan**: Calyx live, hel, fyller ramen | Rubriken faller till en 11 px monoetikett i övre vänstra hörnet; delaren har lämnat ramen |
| s4 | a2 | **Skillnadsliggarens tal** i displaygrad, ett par per rad, avdelade av hårlinjer | Tesraden `VI BYGGER ERT VARUMÄRKE.` sitter som löphuvud i 15 px; radetiketterna i 11 px mono |
| s5 | a3 objekt 1 | **Hōrai** som full-bleed objekt | Bildtexten `Exempelsida: Hōrai, Asian fusion-koncept` i 11 px mono i underkanten |
| s6 | a3 objekt 2 | **Hyperborea** som full-bleed objekt | Samma |
| s7 | a4 | **Tjänstenamnen** `Design` / `Utveckling` / `System`, en per rad, olika radlängd | Radnumren 01–03 i 11 px mono; underraderna i 15 px |
| s8 | a5 | **Priskolumnen** `26 900` / `38 900` / `Pris vid förfrågan`, i bläck, aldrig i blått | Paketraderna i 15 px med ledarpunkter fram till kolumnen |
| s9 | a6 | **`Alla har rätt till bra design.`** i displayskala, vänsterställd | `kontakt@alunix.se` som 15 px mailto under raden |

### (4) Fingerprint

**Cellens egen rad**, i registrets sex dimensioner:

| Dimension | K4 |
|---|---|
| Grammatik | Split stage |
| Nav | **Ingen bar, ingen meny, ingen pill, inget ordmärke i toppen: delaren är chromen.** En enda lodrät hårlinje som löper hela viewporthöjden, i bläck med `#1E5E9C` som sitt enda kromatiska värde; den är sidans enda beständiga form, dess enda gripbara element (`cursor: col-resize`, 44 px osynlig träffyta, ingen knopp, ingen ikon, ingen text) och dess enda navigation. `kontakt@alunix.se` står som 15 px text i "efter"-halvans övre högra hörn |
| Hero-device | **Två levande sajter i samma 1440 × 900-ruta**, staplade som två lager och åtskilda av en clip-gräns vid `--split`: `sites/before-ai-slop.html` underst, ärligt etiketterad `En typisk mallsida`, Calyx överst; över båda en enradig tvåtonsrubrik som korsar sömmen, dämpad över "före" och bläck över "efter" (paper.design-devicen). Ingen av ramarna transformeras eller skalas någonsin: bara clip-gränsen flyttas |
| Aktform | 6 akter, 9 skärmar: `pin` span 2,4 dwell 0,22 (delaren tippar, toppen) → `reveal` **per sida** (skillnadsliggaren, vänsterfiguren wipeas från vänster, högerfiguren från höger) → `flow`+`in` (Hōrai och Hyperborea som full-bleed objekt) → `kinetic` lines (tjänsterna) → `count` (paketen) → `reveal` (avslutet). Noll `pan`, noll `drift`, noll `spotlight`, noll `magnet`, noll `scrub` |
| Avslut | **Kollapsen till en kolumn.** Delaren har lämnat ramen åt vänster, "efter"-ytan fyller hela bredden, `Alla har rätt till bra design.` står i displayskala vänsterställd på varmt papper, `kontakt@alunix.se` som mailto under. Ingen inversion, ingen mörk CTA-remsa, ingen kolofon, ingen footerrad, och avsiktligt osymmetriskt (split stage förbjuder symmetriskt avslut) |
| Signatur | ***Delaren tippar.*** En enda lodrät gräns som besökaren både skrollar och drar: scrollen äger målvärdet, pekaren får sätta ett eget värde, och släppet lämnas vidare till målvärdet genom en kritiskt dämpad fjäder (damping 1,0, ingen översläng), avbrytbar mitt i rörelsen med behållen position och hastighet. Samtidigt **degraderas rubrikens före-halva av delaren**: `wght` faller 500 → 200 och `letter-spacing` öppnar 0 → 0,06 em längs `--sc-ps`, så paper.design-devicen (identiska metriker, bara färgen skiljer) som gäller vid ps = 0 bryts sönder av rörelsen |

**Gaten mot alla 36 byggrader i registret** (`wiki/projects/_index/design-fingerprints.md`,
7 exempelsajter + 29 Alunix-rader). `≠` = skiljer sig, `=` = delad. Summan räknar antal `≠` av
sex. Kravet är ≥ 4/6 mot **varje** rad, kontrollerat rad för rad, aldrig medelvärde.

| registerrad | grammatik ≠? | nav ≠? | hero ≠? | aktform ≠? | avslut ≠? | signatur ≠? | summa |
|---|---|---|---|---|---|---|---|
| Calyx | ≠ split stage vs chaptered editorial | ≠ delaren som enda chrome vs statiskt border-b-huvud i 3 kolumner | ≠ två levande sajter i en clip-split vs fullbleed botaniskt foto med scrim | ≠ 6 motorakter med pin 2,4 vs 8 handrullade sektioner | ≠ kollaps till en kolumn på varmt papper vs mörkinverterad mailto i jättekursiv | ≠ delaren tippar vs ingen (bara IO-fade) | **6/6** |
| Hōrai | ≠ split stage vs filmic one-shot | ≠ delaren vs fixerad bar som mörkblurrar | ≠ clip-split av två sajter vs fullbleed JS-parallaxfoto med jätteordmärke | ≠ pin+reveal+flow+kinetic+count vs scrubbat citatkapitel | ≠ kollaps till en kolumn vs mörk sektion med book.horai.se i jättegrad | ≠ vs bell-curve-scrubbat citat | **6/6** |
| Hyperborea | ≠ split stage vs chaptered editorial | ≠ ingen topprad alls vs sticky header under edition strip med amber CTA-pill | ≠ två sajter i clip-split vs statiskt lagrat sol- och skyline-SVG | ≠ 6 akter med pin och count vs 8 sektioner, marquee, ingen motor | ≠ kollaps vs mörk kolofon "write us a letter" | ≠ vs ingen (sol-diskarna är ett system, inte en interaktion) | **6/6** |
| Tidvatten | ≠ split stage vs filmic one-shot | ≠ delaren vs fixerad bar med "Bli medlem"-länk | ≠ två sajter i clip-split, noll eget foto vs fullbleed havsfoto med ordmärket över hela ramen | ≠ 6 akter utan scrub vs 7 sektioner med pinnat gradscrub | ≠ kollaps till en kolumn på papper vs mörk inverterad mailto i jättegrad | ≠ **en** gräns som färdas i **en** riktning, driven 1:1 av scroll och pekare, vs **två** tal som glider in från motsatta kanter och konvergerar på en bell-curve-scrub | **6/6** |
| Vintergatan | ≠ split stage vs chaptered editorial | ≠ delaren vs statiskt huvud under edition strip, centrerat ordmärke | ≠ två sajter i clip-split vs typ satt direkt i fotografiet | ≠ 6 akter vs 11 sektioner med pinnad ordavslöjning | ≠ kollaps vs mörk sektion med kursiv mailto och öppettider | ≠ vs tre ord som förgylls i sekvens | **6/6** |
| Vinterspelen | ≠ split stage vs chaptered editorial med gallery-inflektion | ≠ delaren vs sticky header med ljuslågemärke och biljettknapp | ≠ två levande sajter vs delat anslag med en inramad målning | ≠ 6 akter utan scenbyte vs 10 sektioner med pinnat kulissbyte | ≠ kollaps till en kolumn vs papperssektion "resan" som matar en mörk 3-kolumnsfooter | ≠ vs sex kulissremsor i vågrörelse | **6/6** |
| before-ai-slop | ≠ split stage vs ingen av de åtta | ≠ delaren som chrome vs sticky flytande pill med backdrop-blur | ≠ två riktiga sajter i clip-split vs centrerad split med badge, gradientord och div-byggt dashboardkort | ≠ 6 koreograferade akter vs 7 statiska sektioner utan en enda reveal | ≠ kollaps till en kolumn vs centrerad CTA och enradsfooter | ≠ vs ingen alls | **6/6** |
| r1 K1 Svart scen och vit sal | ≠ split stage vs rhythmic cutlist | ≠ delaren vs minimal fixerad toppremsa med ordmärke och mailto | ≠ två sajter i clip-split på varmt papper vs mörk scen med en ljuspöl i fotot | ≠ 6 motorakter vs 4 hårda klipp utan motor | ≠ kollaps på varmt papper vs vit sal med mailto i displaygrad | ≠ vs tre demorutor som lyfter med underglöd | **6/6** |
| r1 K2 Tjänsteledger | `=` båda split stage | ≠ delaren som enda chrome, ingen bar och inget ordmärke vs sticky vänsterskena med roterat ordmärke, tre länkar och mailto | ≠ två levande sajter under en tvåtonsrubrik vs vitt papper med jättefråga i grotesk och en solid ink-knapp | ≠ 6 motorakter med pin 2,4 vs 3 sektioner med fast vänsterspalt och färgbyte per kapitel | ≠ kollaps till en kolumn på varmt papper vs mörkt band med systemtexturlinje och tre färgprickar | ≠ delaren tippar vs kapitelfärg som fördjupas via color-mix | **5/6** |
| r1 K3 Instrument | ≠ split stage vs typographic poster | ≠ delaren vs kickerremsa utan nav | ≠ två sajter i clip-split vs displaypåstående på onyx med ett blått handlingsord | ≠ 6 akter med pin vs 5 sektioner på en värdestegsgrund | ≠ kollaps till en kolumn vs en enda påståenderad | ≠ vs siffror som räknar upp med linjal under | **6/6** |
| r1 K4 Journal | ≠ split stage vs chaptered editorial | ≠ delaren vs toppkickerrad med ordmärke och mailto | ≠ två levande sajter vs vikt-300-serifrubrik med en atmosfärsplate bredvid | ≠ 6 akter, pin 2,4 vs 4 handrullade romerska kapitel | ≠ kollaps till en kolumn vs tryckt kolofon som krediterar typsnitt, foto och person | ≠ vs `NN / 03`-räknare på varje plate | **6/6** |
| r1 K5 Affisch | ≠ split stage vs gallery/catalog | ≠ delaren vs textnav i foldens underkant | ≠ två sajter i clip-split vs ordmärket i viewportbredd på en flat färg | ≠ 6 akter vs 3 numrerade helbreda plates | ≠ kollaps till en kolumn vs kontakt som en enda rad | ≠ vs ordmärket som fast bakgrundslager | **6/6** |
| r1 K6 Kortlek | ≠ split stage vs live surface | ≠ delaren vs fixerad flytande pill | ≠ två sajter live i clip-split vs solfjäder av tre skärmbilder | ≠ 6 akter vs 4 sektioner i drift-parallaxfamiljen | ≠ kollaps till en kolumn vs ingen egen avslutsform alls | ≠ vs kortleken som blandas om på scroll | **6/6** |
| r2 R1 Squarespace scen | ≠ split stage vs rhythmic cutlist | ≠ delaren vs svart topprad med spökknapp | ≠ två sajter i clip-split vs fullbleed mörkt spotlightfoto med centrerad rubrik | ≠ 6 akter med pin vs 5 helbreda band med hårda klipp, ingen pin | ≠ kollaps på varmt papper vs vit sal med mailto i 72 px | ≠ vs rutor som glider in underifrån | **6/6** |
| r2 R2 Vit remsa | ≠ split stage vs chaptered editorial | ≠ delaren vs vit topprad plus pill-filterrad under heron | ≠ två levande sajter vs vitt typband utan bild | ≠ 6 akter med pin vs 5 sektioner med mörka projektkort | ≠ kollaps till en kolumn vs tyst vitt kontaktblock | ≠ vs pill-flikar som `:target`-markerar rätt kort | **6/6** |
| r2 R3 Färgband | ≠ split stage vs chaptered editorial | ≠ delaren vs vit topprad med seriflogotyp och fyra länkar | ≠ två sajter i clip-split vs vit grund med gemen grotesk rubrik och ingen bild alls | ≠ 6 motorakter vs mosaikremsa plus tre mättade tjänsteband | ≠ kollaps på varmt papper vs mörkt band med manifestrad och mailto | ≠ vs färgbanden som *är* tjänsterna | **6/6** |
| r2 R4 Numrerad process | ≠ split stage vs chaptered editorial | ≠ delaren vs mörk topprad med tre länkar och en blå pill-CTA | ≠ två sajter i clip-split vs fullbleed mörkt texturfoto med komprimerad tung rubrik | ≠ 6 akter med pin och count vs 4 sektioner med 01–05 i schweizisk rytm | ≠ kollaps till en kolumn vs mörkt band plus en pill | ≠ vs mono-numren 01–05 som genomgående spår | **6/6** |
| r2 R5 Konsolram | `=` båda split stage | ≠ **en naken hårlinje** som är sidans enda chrome vs **en konsolram** med versionstagg, levande klocka och fyra hörnmärken (K4 får per F-006 aldrig visa ett tillstånd om sig själv, vilket är precis vad konsolramen gör) | ≠ två riktiga sajter i clip-split vs ordmärket inne i en konsolram lagd över ett gråskalefoto | ≠ 6 motorakter med pin 2,4 vs 3 sektioner utan motor | ≠ kollaps till en kolumn på varmt papper vs vitt block med en jätterubrik | ≠ en gräns som färdas vågrätt och kan gripas vs hörnmärken som står fixerade i viewporten | **5/6** |
| r2 R6 Affischordmärke | ≠ split stage vs typographic poster | ≠ delaren vs fixerad minimal rad med cirkelmärke och kontaktpill | ≠ två sajter i clip-split vs ordmärket i viewportbredd med fullbleed dokumentärfoto under | ≠ 6 akter vs 5 sektioner utan motor | ≠ kollaps till en kolumn vs off-white kolofon som stänger på mailto som text | ≠ vs tre 12 px färgprover, ett per demorad | **6/6** |
| r3 build (R5+R6) | `=` båda split stage | ≠ delaren, som är **en rörlig gräns mellan två ytor**, vs fyra **fasta hörnmärken** i viewportens hörn | ≠ två **främmande** sidor renderade hela i samma ruta, utan en enda Alunix-komposition i folden vs **två egna heron** sida vid sida (konsolkort över gråskalefoto till vänster, Tidvatten-iframe till höger) med logotypmärket dockat på sömmen; K4 har inget märke på sömmen | ≠ 6 akter med `pin` 2,4 vs 9 rena `flow`-akter och aldrig pin | ≠ kollaps till **en** kolumn vs Calyx-ram och prisruta som stänger samtidigt i **två** spalter | ≠ delaren färdas **vågrätt** över hela bredden, driven av scroll **och** pekare, kritiskt dämpad, och degraderar rubrikens ena halva vs sömlinjen som **växer lodrätt** via `scaleY` ur ett dockat märke, utan pekare och utan följd för någon annan del av sidan | **5/6** |
| r4 M1 Kontinuerlig grund | ≠ split stage vs continuous world | ≠ delaren vs tunn topprad som scrollar bort | ≠ två sajter i en clip-split vs en helbred levande Tidvatten-iframe som hela första akten | ≠ 6 akter med pin, kinetic och count vs 8 rena flow-akter över en fast grund | ≠ kollaps till en kolumn vs Calyx-ram och prisruta, avsiktligt osynkade | ≠ vs +50 vh-förskjutningen som låter grunden lysa igenom | **6/6** |
| r4 M2 Kapitel med pinnad scen | ≠ split stage vs chaptered editorial | ≠ delaren vs fast folio `0X/05` plus roterad kapitelskena | ≠ två sajter i clip-split vs ett stilla konsoltitelkort över en gråskalegrund | ≠ 6 akter, pin 2,4 dwell 0,22 vs 3 motorakter med pin 3,2 i fem kapitel | ≠ kollaps till en kolumn vs inverterad prisruta ensam i kapitel 05 | ≠ vs kapitelskenan som scrollhuvud (`-scrollY` på inre spår) | **6/6** |
| r4 M3 Galleri med rail | ≠ split stage vs gallery/catalog | ≠ delaren vs indexnav med fyra mono-hopplänkar | ≠ två sajter i clip-split vs affischordmärke staplat över konsolkortet | ≠ 6 akter med **noll** `pan` (split stage förbjuder den) vs 6 akter vars spine är en inbäddad horisontell `pan`-rail span 4,2 | ≠ kollaps till en kolumn vs en prisruta som katalogens sista objekt | ≠ vs ordskrubben med SVG-tråd i marginalen | **6/6** |
| r5 V1 Dokumentär band | ≠ split stage vs continuous world | ≠ delaren vs ärvd tunn topprad som scrollar bort | ≠ två levande sajter vs band med krämpanel 38 % och färgfoto 62 % | ≠ 6 akter med pin vs 8 rena flow-akter | ≠ kollaps till en kolumn vs ärvd Calyx-ram och prisruta, osynkade | ≠ delaren som gräns mellan två **sidor** vs krämpanelen som växer över ett **foto** | **6/6** |
| r5 V2 Cinematisk tvätt | ≠ split stage vs continuous world | ≠ delaren vs ärvd tunn topprad | ≠ två sajter i clip-split vs fullbleed ljusstrålefoto under en svart tvätt | ≠ 6 akter, ingen drift vs 9 akter med drift och parallax | ≠ kollaps till en kolumn vs Hyperborea-ram och prisruta, osynkade | ≠ vs tvättlyftet i en rad CSS | **6/6** |
| r5 V3 Plåt i grunden | ≠ split stage vs continuous world | ≠ delaren vs ärvd tunn topprad | ≠ två sajter i clip-split vs inramad plåt med hårlinje på mörk grund | ≠ 6 akter vs 8 flow-akter i två spalter | ≠ kollaps till en kolumn vs Calyx-ram och prisruta, osynkade | ≠ vs ljuspölen som vandrar via object-position | **6/6** |
| r5 V3b Plåt i grunden, polerad | ≠ split stage vs continuous world | ≠ delaren vs ärvd tunn topprad | ≠ två sajter i clip-split vs samma inramade ljuspölsplåt, kapad till en fold | ≠ 6 akter med pin och count vs 8 flow-akter | ≠ kollaps till en kolumn vs ärvd Calyx-ram och prisruta | ≠ vs samma ljuspölsvandring | **6/6** |
| r6 A-K1 Skymning (native) | ≠ split stage vs filmic one-shot | ≠ delaren vs minimal fixerad topbar som växlar över grunderna | ≠ två sajter i clip-split vs fullbleed blåtimmesfoto med ljus serifrubrik | ≠ 6 akter utan zoom vs CSS-dolly skala 1 → 22 och pinnad iframe-avslöjning | ≠ kollaps till en kolumn på varmt papper vs nattfoto som landar och håller | ≠ en gräns som färdas i **bildplanet** vs en kamera som flyger **in i** ett fönster | **6/6** |
| r6 A-K2 Affischen (native) | ≠ split stage vs typographic poster | ≠ delaren vs tryckt topprad med tickande klocka | ≠ två sajter i clip-split vs ordmärket brutet ALU / NIX med fönster i bokstävernas punsar | ≠ 6 akter vs 7 akter med 320 vh pinnad hero | ≠ kollaps till en kolumn vs bläckark som rullas ner med clip-path | ≠ vs bildremsan som passerar genom bokstäverna | **6/6** |
| r6 A-K3 Konsolen (native) | ≠ split stage vs live surface | ≠ delaren vs app-chrome med 56 px bar och tre numrerade flikar | ≠ två sajter samtidigt i samma ruta vs fullbleed skrivbordsfoto med glaskort som läser tillstånd | ≠ 6 akter vs 6 akter med iframe-scrollTop-växling | ≠ kollaps till en kolumn vs riktigt inmatningsfält som öppnar mailto | ≠ besökaren flyttar **gränsen mellan** två sidor vs besökaren driver **innehållet i** en sida | **6/6** |
| r6 B-K1 Skymning (kedjan) | ≠ split stage vs filmic one-shot | ≠ delaren vs fixerad bar som byter grund per akt | ≠ två sajter i clip-split vs blåtimmesfoto med retuscherad skylt och ljus serifrubrik | ≠ 6 akter med kit-pin vs handrullad lerpad zoom utan kit-pin | ≠ kollaps till en kolumn vs nattfoto som öppnas med clip-path | ≠ vs kameran in i ett riktigt tänt fönster | **6/6** |
| r6 B-K1-nogate | ≠ split stage vs filmic one-shot | ≠ delaren vs fixerad bar plus separat nav i ramen med toggle-knapp | ≠ två sajter i clip-split vs blåtimmesfoto där målfönstret redan syns i vila | ≠ 6 akter vs 6 akter med 3,8 vh heroloop | ≠ kollaps till en kolumn vs andra nattfotot som håller stilla | ≠ vs samma zoom men med opt-in-ram | **6/6** |
| r6 B-K2 Affischen (kedjan) | ≠ split stage vs typographic poster | ≠ delaren vs tunn topprad med `Intl`-klocka | ≠ två sajter i clip-split vs ALU / NIX i variabel Archivo 900 med bildpanel bakom bokstäverna | ≠ 6 akter vs 7 akter med pinnad bildremsa 0 → 55 % | ≠ kollaps till en kolumn vs bläckblock rullat med clip-path till sidans slut | ≠ vs panelglid plus andande block | **6/6** |
| r6 B-K3 Konsolen (kedjan) | ≠ split stage vs live surface | ≠ delaren vs 56 px app-bar med statuschip | ≠ två sajter i clip-split vs dagsljusfoto med krämslöja och glaskort | ≠ 6 akter vs 6 akter med 1:1 scrollTop-mappning | ≠ kollaps till en kolumn vs mörkt avslut med riktigt textfält | ≠ besökaren flyttar en **gräns** vs besökaren provkör en **sidas scroll** | **6/6** |
| r7 B-K1 Skymning v2 | ≠ split stage vs filmic one-shot | ≠ delaren vs fixerad topbar med logotypväxling och etikettslot | ≠ två sajter live i clip-split vs 100-bilders förrenderad dolly på `canvas[data-sc-sequence]` | ≠ 6 akter, pin span 2,4 vs 4 motorakter med pin span 5,0 | ≠ kollaps till en kolumn vs nattfoto som `reveal` plus färgdrift | ≠ vs kameraåkning som blir en levande sida via `window-track.json` | **6/6** |
| r7 B-K2 Affischen v2 | ≠ split stage vs typographic poster | ≠ delaren vs tunn topprad med klocka och stad | ≠ två sajter i clip-split vs bild maskad genom bokstävernas uppmätta öppningar | ≠ 6 akter vs 5 akter med pin span 3 och diskret radhöjdssteg | ≠ kollaps till en kolumn på oförändrat varmt papper vs grunden som driftar från papper till bläck | ≠ vs papper bakom masken plus andande block | **6/6** |

**Lägsta summa: 5/6**, mot tre rader — **r1 K2 Tjänsteledger**, **r2 R5 Konsolram** och
**r3 build (R5+R6)** — och i alla tre fallen är den delade dimensionen *grammatik*, som
målbilden själv låser. Ingen rad faller under 4/6, och ingen rad delar mer än en dimension.

De tre split stage-raderna är också de enda i registret som kan kollidera, och de kollisioner
som ligger närmast till hands är avvärjda i formuleringen, inte i ordvalet:

- **r2 R5:s konsolram** och K4:s delare är båda "chrome i stället för en bar". Skillnaden är
  materiell och kontrollerbar: konsolramen *rapporterar ett tillstånd* (version, klocka,
  hörnmärken), vilket F-006 uttryckligen förbjuder K4 att göra. K4:s delare rapporterar
  ingenting; den är en gräns.
- **r3 builds sömlinje** och K4:s delare är båda en lodrät linje i en tvådelad komposition.
  Skillnaden är riktning, drivning och följd: r3:s linje **växer lodrätt** ur ett dockat märke
  via `scaleY`, är enbart scrolldriven och påverkar ingenting annat; K4:s linje **färdas
  vågrätt** över hela bredden, är både scroll- och pekardriven, och dess läge är det som
  degraderar rubrikens ena halva och som avgör hur mycket av varje sajt som syns.

**Extra tabell: K4 mot K3.** K3:s låsta värden är hämtade ur `concepts-K3.md` § (4) och § (6).
Sex dimensioner plus två: temperatur och typsnitt.

| Dimension | K3 | K4 | ≠? |
|---|---|---|---|
| Grammatik | Chaptered editorial | Split stage | **≠** |
| Nav | Ritad teckenförklaring i vänstermarginalen, sticky, fem rader symbolprov plus en ledarlinje som ritas till aktivt kapitel | Ingen marginal, ingen legend, inget symbolprov: en enda lodrät gräns i bildens mitt som är hela chromen, plus en mailto i övre högra hörnet | **≠** |
| Hero-device | En måttsatt sektionsritning i inline-SVG som ritar sig själv ur `stroke-dashoffset`; sajten maskas till sist in i öppningen bläcket ritat | Två färdiga, levande sajter som båda finns på skärmen från första bildrutan; ingenting ritas, ingenting byggs upp, gränsen mellan dem flyttas | **≠** |
| Aktform | 6 akter: `pin` 2,4 dwell 0,35 → `kinetic` → `reveal` ×3 (tre plates i följd) → `flow`+`in` → `count` → `reveal`. Noll `pan`, noll pekar-devices | 6 akter: `pin` 2,4 dwell 0,22 → `reveal` **per sida** (tvåriktad, en device K3 inte använder) → `flow`+`in` → `kinetic` → `count` → `reveal`. Ryggraden är en enda obruten upplösning, inte ett galleri av tre plates; a1 bär dessutom en pekardriven, avbrytbar bespoke-rörelse, vilket K3:s pin uttryckligen inte gör | **≠** (tunnaste raden i tabellen, se not) |
| Avslut | Ett specifikationsblad på kallt papper: stycklista med ledarpunkter inuti en ritad ram vars linjer dras in sist | En kollaps till en kolumn på varmt papper: ingen ram, inga linjer dras, ytan bara fylls och rubriken landar | **≠** |
| Signatur | *Ritningen blir sidan*: en kontur ritas och den riktiga sidan maskas in i öppningen | *Delaren tippar*: två färdiga sidor konkurrerar om samma rektangel och en gripbar gräns avgör | **≠** |
| **Temperatur** | Kallt: `--paper` `oklch(0.95 0.012 230)`, hue 230 | Varmt: `--paper` `oklch(0.957 0.013 85)`, hue 85 | **≠** 145° isär i hue, samma låga chroma. Ingen av dem är kräm |
| **Typsnitt** | Chivo (röst) + Martian Mono (register) | Switzer (röst) + Reddit Mono (register) | **≠** Noll överlapp, och K4 rör ingen av K3:s fyra reservval |

**8/8. Not om aktformraden:** det är tabellens tunnaste rad, eftersom båda cellerna öppnar med
`pin` span 2,4 och båda innehåller `flow`, `count` och `reveal`. Jag flyttar inte span 2,4,
eftersom målbilden låser den och gaten inte faller. Skillnaden jag hävdar är strukturell och
kontrollerbar i markupen: K3 har tre `reveal`-akter i följd och en `kinetic` rubrik tidigt;
K4 har noll `reveal` i följd, en tvåriktad `reveal`, `kinetic` sent, och en pekardriven
bespoke-rörelse i pin-akten. Lead bör läsa raden som den svagaste punkten i cellen och kan när
som helst be mig byta `dwell` eller aktordningen om den ska vara starkare.

**Vad jag bytte i planen, och varför.** Ingen ändring nedan tvingades fram av att gaten föll
under 4/6 — gaten håller på 5/6 som lägst. Alla ändringar har andra källor, som står utskrivna.

1. **`pan` ströks och ersattes.** Min första aktplan lade Hōrai och Hyperborea i en vågrät
   `pan`-akt, som en fortsättning på den axel delaren just lämnat. Källa som stoppade det:
   `scroll/grammars.md`, raden för **Split stage**, kolumnen *Bans*: `pan`, `spotlight`,
   `magnet`, > 1 `scrub`, `drift`. Åtgärd: a3 är `flow` + `in` med stagger. Det håller
   målbildens "i tur och ordning" och kostar ingenting.
2. **`flow` (paketen) blev `count`.** Målbilden skriver `flow` (liggaren 01–03) följt av
   `flow` (paketen), vilket sätter samma familj två gånger i rad. Källa: `devices.md`
   § device kit, "never the same one twice running". Åtgärd: a4 är `kinetic` lines
   (tjänsterna, tre rader ur en mask) och a5 är `count` (paketen). `count` är dessutom en av
   split stages tre egna lutningar, formulerad som **real `count`** — och Alunix har exakt två
   sanna tal, `26 900` och `38 900`, vilket `devices.md` § 7 kräver.
3. **Tesraden fick en plats.** Målbildens aktlista för K4 nämner aldrig
   `VI BYGGER ERT VARUMÄRKE.`, men strängen står i PRODUCT.md:s låsta copy-lista och lead
   bekräftar versalformen. Källa: copy-gate (ordagrann copy bevaras) + PRODUCT.md
   § Brand Commitments. Åtgärd: raden är a2:s löphuvud, satt i 15 px över skillnadsliggaren,
   alltså på den yta argumentet just vunnit. Den får ingen egen akt, eftersom en tredje topp
   är ingen topp (`feel-and-fingerprint.md` § The peak).
4. **`dwell` sänktes från K3:s 0,35 till 0,22.** Källa: `feel-and-fingerprint.md` § Pacing och
   F-002. K3:s pin öppnar med ett medvetet tomt ark; K4:s fold är redan full av innehåll vid
   ps = 0 och behöver ingen tystnad före toppen, bara en kort stillhet så att besökaren hinner
   se att det är två sidor.
5. **Skärmlistan växte från 6 till 9.** Källa: F-007, som körs skärm för skärm. Se § (3).
6. **`hårlinjer` ströks ur skillnadsliggaren.** Källa: TASTE § 4.9 och den egna mätningen:
   `hairlineRules` 12 mot 10, alltså tvärtemot vad målbilden antar. Ersatt av
   `Sidmarginal vid 1440`, som är mätt och entydig. Se § Mätning.
7. **Hōrai och Hyperborea visas som skärmbilder, inte som live-ramar.** Källa: målbilden själv
   (den kallar dem "full-bleed **objekt**", inte ramar) plus `performance.md` § 1: fyra
   samtidiga iframes är inte försvarbart inom 2,5 MB. Calyx förblir live, så PRODUCT.md
   princip 1 ("beviset ska gå att använda") är uppfylld på sidan. Se § Prestandaplan i
   `runs/K4/BRIEF.md`.
8. **Referensvalet.** Målbildens fem förväntade slugar ersattes av `select.py`s faktiska rad.
   Tre av fem stämde; `future-fur` och `dovetail` föll och skälen är utskrivna i
   § catalogue-select. Källa: `catalogue-first.md` § 5.
9. **Assetvägen: ingen generering.** Higgsfield är ute (lead mätte `balance` = 0 krediter,
   free plan, 2026-09-09). Källa: planens § 10.6 fallback steg 3. **K4 behövde ändå inget
   genererat material**, och skälet är principiellt, inte praktiskt: cellens hela premiss är
   att allt som visas är verkligt och mätbart. En genererad bild på den här sidan vore ett
   påhittat objekt i en sida vars argument är att den inte hittar på något. Material som letar
   efter en användning är inte tillåtet. Se `runs/K4/assets/ASSETS.md` och `NOTES.md`.
10. **Reduced motion utgår.** Fältet "Reduced motion-planen" finns inte i K4:s skelett.
    Källa: F-011.

### (5) Rörelse

**Motion-tes.**

- **Focal.** Ögat ska följa **delaren**, och bara den. Under hela a1 står allt annat i vyn
  helt stilla: de två sajterna rör sig inte en pixel, rubriken flyttar sig inte, kickerna
  flyttar sig inte. Det enda som ändrar läge är en lodrät linje. Ett enda fokusskifte i hela
  akten, vid ps ≈ 0,68, när linjen lämnar ramen och blicken faller på ytan som blev kvar.
- **Continuity.** Ingenting tonar in ur intet och ingenting hoppar in i vy. Båda sajterna är
  redan där vid ps = 0; det som ändras är hur mycket av var och en som är synlig. Delaren
  startar i mitten där den redan syntes, färdas monotont åt ett håll och lämnar ramen — den
  vänder aldrig, den studsar aldrig, den nollställs aldrig. Rubriken är samma rad hela vägen;
  den byter bara vikt och tracking på sin ena halva. Det som fyller ramen vid ps = 1 är
  **samma** Calyx-ram som stod till höger vid ps = 0, inte en ny ruta ovanpå (F-010).
- **Feedback.** Scrollen *är* handen på delaren: 1 % scroll = 1 % förflyttning, båda
  riktningarna, ingen låsning, ingen hijack utöver motorns egen pin. Pekaren får samma
  auktoritet: `pointerdown` på den 44 px breda osynliga träffytan tar över värdet direkt och
  1:1, `pointermove` skriver det, `pointerup` lämnar tillbaka det till scrollens värde genom en
  **kritiskt dämpad fjäder (damping 1,0)**, seedad med pekarens hastighet vid släppet
  (velocity-handoff). Rörelsen är **avbrytbar**: ett nytt `pointerdown` mitt i återgången tar
  vid i det läge och den hastighet fjädern hade — den nollställer inte och den hoppar inte.
  Det som målas är alltid fjäderns utvärde, aldrig pekarens råa x (`apple-design`
  § presentationsvärde). Att scrolla uppåt drar tillbaka delaren i exakt omvänd ordning.
- **Budget.** **En** `pin` på hela sidan, span 2,4, dwell 0,22. Den bespoke rörelsen är
  **ett** tal, `--split`, skrivet en gång per bildruta av **en** rAF-loop som stannar av sig
  själv i vila; `--split` driver tre `calc()`-uttryck i CSS (clip-gränsen, rubrikhalvans
  `font-variation-settings`/`letter-spacing`, mallsidans `filter: saturate()`) och noll
  layoutläsningar. Ingen `transition: all`, ingen `backdrop-filter`, ingen `filter` på något
  utom mallsidans wrapper. `will-change` sätts bara på delaren och på wrappern medan
  `0 < ps < 1`, aldrig i vila. Två typsnittsfiler, båda variabla, båda självhostade som
  `.woff2`, tak 300 kB. Iframes monteras via IntersectionObserver med `loading="lazy"`.
  Måltal (F-014, `motion-smoothness.md` § The bar, vid 4× CPU): `staircase = 0`,
  `max_step ≤ 3 %`, bildtid p95 ≤ 20 ms, noll frames > 33 ms, båda scrollriktningarna mätta,
  och `motion_probe` körd med **både** `--wheel 20:120` och `--wheel 100:60`.

**F-014, uttryckligt.** Allt ögat ser förflytta sig läser `--sc-ps`, aldrig rå `--sc-p`:
clip-gränsen, rubrikhalvans vikt och tracking, liggarradernas wipe, `kinetic`-radernas mask.
Endast cue-opacitet läser `--sc-p`. `--split` beräknas ur `--sc-ps` plus pekarens offset och
publiceras som ett registrerat `<number>` av samma slag som `sc-smooth.js` publicerar
`--sc-ps`, så att CSS kan interpolera det. `motion-smoothness.md` § Fault 1 är läst: den
lerpade fjädern löser fel 1, och prestandaplanen i BRIEF:en löser fel 2. De är olika fel och
båda mäts.

**Feeling curve** — en känsla per akt, orsaken i andra kolumnen, aldrig två lika i rad.

| # | Känsla | Vad på skärmen orsakar den |
|---|---|---|
| a1 | **Tillfredsställelse** ← TOPPEN | Två färdiga webbplatser står emot varandra i samma ruta, och sedan trycks den ena bokstavligen ut ur bild av den andra medan besökarens egen hand kan ta tag i gränsen och skjuta på |
| a2 | **Skärpa** | Känslan blir ett tal: sex mätta par i displaygrad, avdelade av hårlinjer, var och en avslöjad från sin egen sida |
| a3 | **Tillit** | Två sajter till, hela, i full bredd, en i taget, i en grad där man ser att de är riktiga |
| a4 | **Klarhet** | Tre ord, tre rader, olika längd, ingenting annat i vyn |
| a5 | **Trygghet** | Priserna räknas upp till 26 900 och 38 900, och det tredje står utskrivet i klartext i stället för att gömmas |
| a6 | **Ro** | En rad och en adress på ett papper som slutar röra sig |

**Författad tystnad** (måste stå i BRIEF.md så `scroll_verify.py`s `blankBands` inte larmar
falskt): de första 0,10 av a1 är avsiktligt orörliga — båda sajterna står helt stilla medan
besökaren läser rubriken. Det är stillheten före toppen, inte död scroll. Den är kortare än
K3:s (0,12) eftersom vyn redan är full av innehåll.

**Tell-someone-meningen.** *"Det är sajten där den dåliga hemsidan bokstavligen trycks ut ur
bild av den bra, och man kan ta tag i gränsen och skjuta på själv."*

**Device-tabell.** Fem familjer (`pin`, `reveal`, `flow`, `kinetic`, `count`), aldrig samma två
i rad, noll `pan`, noll `drift`, noll `spotlight`, noll `magnet`, noll `scrub` — alla fem
förbjudna av split stage. Kolumnen **läser** anger vad varje rörlig sak läser: `--sc-ps` för
allt ögat ser förflytta sig, `--sc-p` bara för cue-opacitet, och "motorns egen" där motorn
själv äger transformen (F-014 regel 1).

| Akt | Sektion | Device (familj) | Span / cue | Vad som rör sig | Läser | Varför just denna |
|---|---|---|---|---|---|---|
| a1 | Delaren | `pin` (+ bespoke `paintSplit`) | span 2,4 · dwell 0,22 · cue `0 1 0 0` (hälsa och håll, ground finns) | `clip-path: inset()` på "efter"-lagret; delarens `translateX`; rubrikhalvans `font-variation-settings` och `letter-spacing`; mallsidewrapperns `saturate()` | **`--sc-ps`** via `--split` (allt ovan); `--sc-p` (kickernas opacitet) | Split stages egen lutning är ordagrant "`pin` with divider"; ramen måste hålla stilla medan en enda idé korsar den |
| a2 | Skillnadsliggaren | `reveal` **per sida** | `data-sc-reveal-at="0.12 0.5"`, riktning `left` på före-kolumnen och `right` på efter-kolumnen | `clip-path`-wipe per tal, från sin egen sida in mot hårlinjen | **`--sc-ps`** | Split stages andra lutning är ordagrant "`reveal` per side"; att varje tal kommer från sin egen halva håller argumentets geometri levande efter att delaren är borta |
| a3 | Hōrai, Hyperborea | `flow` + `in` | stagger 90 ms, full blockpadding | De två objekten stiger 14 px och tonar in, ett i taget | `--sc-p` (opacitet); motorns egen (14 px-lyftet) | Efter upplösningen får full-bleed förekomma; objekten ska passera, inte pinnas (`feel-and-fingerprint.md` § Pacing) |
| a4 | Tjänsterna 01–03 | `kinetic` lines | cue `0.1 0.9 0.15 0.4` | Tre rader ur en mask, en i taget | motorns egen (raderna); **`--sc-ps`** (radnumrens hårlinje) | En kinetisk rubrik per sida, och rader är nästan alltid rätt form för den (`devices.md` § 5) |
| a5 | Paketen | `count` | `data-sc-count-at="0.1 0.5"`, 1,4 s, cubic ease-out | `26 900` och `38 900` räknar upp; `Pris vid förfrågan` skrivs, den räknar inte | motorns egen | Split stages tredje lutning är ordagrant "real `count`"; endast sanna tal får en count (`devices.md` § 7) |
| a6 | Avslutet | `reveal` (sidans sista akt) | cue `0.25` (ett värde: sista akten måste hålla) | Avslutsrubriken wipeas fram vänsterifrån, en gång | **`--sc-ps`** | Avslutet ska lösa upp, inte tona ut (`feel-and-fingerprint.md` § The peak) |

**Embodiment, en enda** (`feel-and-fingerprint.md` § Being in it: "one or two per page"):
**delaren är gripbar.** Det är sidans enda interaktion och den är dess signatur. Ingenting
annat på sidan reagerar på besökaren — ingen hover-lyft, ingen magnet, ingen tilt, ingen
pekarföljare. Att lägga till en andra embodiment vore att ge sidan två röster; målbildens egen
regel är att delaren är den enda formen som är sidans.

**Rejected-lista** (`find-animation-opportunities`-gaten, fyra frågor per kandidat: frekvens,
syfte, hastighet, funktion).

| Kandidat | Frekvens | Syfte | Hastighet | Funktion | Dom |
|---|---|---|---|---|---|
| Delaren snäpper tillbaka till 50 % när pekaren släpps | Varje släpp, alltså ofta | "Ordning" | ~300 ms | Ingen, och den motarbetar berättelsen: sidans hela argument är att balansen ska tippa, inte återställas | **Avvisad.** `apple-design` § velocity handoff: släppet lämnas vidare till det värde scrollen äger, aldrig till en godtycklig mittpunkt |
| Ett handtag med två pilar, en knopp eller texten "dra" på delaren | Alltid synligt | Affordans | Statisk | Ingen; `cursor: col-resize` bär affordansen | **Avvisad.** Gate 88 (varje scroll-cue) och lead-instruktionens uttryckliga förbud |
| Hover-lyft eller bakgrundstoning på skillnadsliggarens rader | Varje pekarpassage | Dekor | ~150 ms | Ingen, och den får raden att läsa som ett kort | **Avvisad.** TASTE § 2.3 (aldrig kort) och `devices.md` § 9 |
| Mallsidan "faller isär", skakar eller får sina element att glida ur läge | En gång per besök | Skämt | ~800 ms | Ingen, och den förvandlar en ärlig anti-referens till en karikatyr | **Avvisad.** Copy-gate och TASTE § 4.9: sidan får bara påstå det den mätt. Ett tal som säger 9 mot 4 är starkare än en animation som säger "ful" |
| Delaren rör sig av sig själv i vila, som en autospelande demo | Konstant loop | "Liv" | ~4 s loop | Ingen | **Avvisad.** TASTE § 3 product-focused, "Rörelse: subtil, aldrig breathing", och F-002: målet i vila får inte förhandsvisa slutläget |
| Marquee med de tre exempelsajternas namn | Alltid, i loop | Fylla tomrum | Långsam loop | Ingen; Hyperborea äger redan marquee i registret | **Avvisad.** Fingerprint + TASTE § 3 (marquee hör till consumer-brand) |
| Spotlight eller magnet på avslutets mailto | Vid varje pekarnärmande | Dra blicken till handlingen | ~200 ms | Marginell | **Avvisad.** `grammars.md`, split stage bans: `spotlight`, `magnet` |
| **Delaren som scroll- och pekardriven gräns** | Hela a1, sidans topp | Det **är** argumentet | 1:1 med hand och hjul | **Ja: den är sidans nav, dess chrome och dess signatur på en gång** | **Behållen.** Split stages egen lutning, ordagrant |
| **Rubrikens före-halva som degraderas längs delaren** | En gång per besök, längs a1 | Gör påståendet synligt i typen själv i stället för i en mening om typen | Bunden till delaren, ingen egen varaktighet | **Ja: den är påståendet, demonstrerat** | **Behållen.** Den bryter paper.design-devicen med avsikt, vilket är det enda sättet att slå en referens man har lånat |

**Delight-tes, en mening.** *Delaren tippar*: besökaren får ta tag i gränsen mellan den sida hen
har och den sida hen kunde ha, känner att den ger efter, släpper — och gränsen fortsätter dit
scrollen redan var på väg, så att den dåliga sidan trycks ut ur bild av den bra.

### (6) Färg och typ

**Färgstrategi: Restrained.** Den fysiska scenen, i en mening: *två utskrifter av samma format
ligger kant i kant på ett varmt pappersark under jämnt ljus, och ett enda blått streck markerar
var den ena slutar och den andra börjar.*

Namngiven referens för strategin (brand.md: "unnamed ambition becomes beige"):
**paper.design:s färginhägnad, flyttad ett hack.** Paper hägnar in sitt enda blå till
märket och kodsyntax, aldrig till en knapp eller en länk; K4 hägnar in sitt enda blå till
**ett enda geometriskt objekt** som existerar exakt en gång på sidan, delaren. Att det är
Restrained och inte Committed är ett medvetet val: sidan är redan full av färg, men all den
färgen tillhör de två sajter som visas. K4:s eget lager måste vara nästan färglöst, annars
konkurrerar det med sitt eget bevis, och då finns det två auktoriteter i vyn (TASTE § 1).

**Föreslagna tokens** (byggaren får skärpa värdena mot uppmätt kontrast, aldrig flytta rollen):

| Token | Värde | Roll |
|---|---|---|
| `--paper` | `oklch(0.957 0.013 85)` | Arket. **Varmt**, hue 85, låg chroma. Inte kräm, inte gräddlinne, och 145° från K3:s hue 230 |
| `--paper-2` | `oklch(0.928 0.018 78)` | Andra arket: bara i a2:s liggarrännil och a6:s grund, som materialbyte mellan akter (TASTE § 4.5) |
| `--ink` | `oklch(0.26 0.021 62)` | Bläcket: rubrikens "efter"-halva, liggarens tal, priserna, avslutsraden. **Varmt** nästan-svart, aldrig ett kallt `#111` på varmt papper |
| `--ink-2` | `oklch(0.62 0.014 70)` | Rubrikens "före"-halva och kickernas dämpade ton. Endast displaygrad och 11 px mono, aldrig brödtext |
| `--hair` | `oklch(0.80 0.010 78)` | Hårlinjer i skillnadsliggaren och under tjänsteraderna. Aldrig typ |
| `--blue` | `oklch(0.47 0.13 252)` (= `#1E5E9C`) | **Enda accenten. Bara delaren.** Aldrig en yta, aldrig en länk, aldrig en ram, aldrig ett tal, aldrig en knapp |

Rollregler, formulerade så att de går att granska: *accenten finns på exakt ett objekt, och
det objektet existerar exakt en gång på sidan* (mode-inhägnaden, skärpt från komponenttyp till
objekt) och *accenten är aldrig text* (paper-regeln, ordagrant övertagen: blått får aldrig
sättas som stor text eller som en länk). Noll `box-shadow`, noll `backdrop-filter`, noll
gradient, radie 0 överallt i K4:s eget lager.

Kontrast som byggaren måste mäta, inte anta: `--ink` på `--paper` ≈ ΔL 0,70, godkänt med bred
marginal. **`--ink-2` på `--paper` är den kritiska:** den ligger nära AA-gränsen och används
därför bara i displaygrad (rubrikens före-halva) och i 11 px mono med tracking, aldrig i
brödtext — kör `contrast.py` per par i R3 och skriv siffran i NOTES.md. `--blue` mäts inte mot
text alls, eftersom den aldrig sätter text; den mäts som yta mot `--paper` så att delaren syns
som en linje, inte som en skugga.

**Typsnitt — brand.md:s fyra steg, utförda.**

1. **Tre varumärkesord, fysiska objekt-ord:** *jämförd · tryckt · varm.* (Inte "modern", inte
   "premium". Objektet är två utskrifter kant i kant på ett varmt ark.)
2. **Reflexlistan, alltså de tre jag skulle gripa efter först:** Inter, Geist, Instrument Sans.
   **Alla tre avvisade** — de står på brand.md:s reflex-reject-lista och dessutom i
   r1–r7-listan. `before-ai-slop.html` kör dessutom hela sidan i Inter (mätt: `"Inter": 61`),
   så Inter är i den här cellen bokstavligen antagonistens typsnitt.
3. **Katalogen, med objektet i huvudet:** foldens rubrik är **en enda rad i två fyllnadsfärger
   med identiska metriker**. Devicen fungerar bara om snittet är så jämnt i färg att
   färgbrytningen är den enda händelsen på raden (paper-postens egen varning: blanda inte
   grader eller snitt). Det pekar mot en mycket jämn, karaktärssvag neo-grotesk — och den
   måste dessutom ha en **äkta viktaxel med lång väg**, eftersom rubrikens ena halva ska falla
   från 500 till 200 medan besökaren ser på.
4. **Korskontroll:** förstavalet sammanfaller inte med reflexen, det står inte i K3:s
   förbudslista, och det är inte K3:s val eller något av K3:s fyra reservval.

**Förbjudet** (lead-instruktionens lista, K3:s val, samt allt använt i r1–r7 och i
`sites/`): Chivo · Martian Mono · Fraunces · Newsreader · Lora · Crimson · Crimson Pro ·
Crimson Text · Playfair Display · Cormorant · Cormorant Garamond · Syne · IBM Plex Mono ·
IBM Plex Sans · IBM Plex Serif · Space Mono · Space Grotesk · Inter · DM Sans ·
DM Serif Display · DM Serif Text · Outfit · Plus Jakarta Sans · Instrument Sans ·
Instrument Serif · Geist · Geist Mono · JetBrains Mono · Public Sans · Familjen Grotesk ·
Literata · Fragment Mono · Hanken Grotesk · Archivo · Figtree · Cardo · PT Mono · Cinzel ·
Vollkorn · Italiana · Bricolage Grotesque · Manrope · Schibsted Grotesk · Bodoni Moda ·
Noto Serif JP. **Undviks dessutom** (K3:s reservkedja): Chivo Mono · General Sans · Sora ·
Spline Sans Mono.

Kontrollerat mekaniskt, inte antaget: `grep -rohiE "family=[A-Za-z+0-9]+" tests/alunix-*/
--include=*.html | sort -u` ger exakt de snitt som faktiskt laddats i r1–r7, och varken
Switzer, Onest, Host Grotesk, Satoshi, Anek Latin, Reddit Mono, Sono, Red Hat Mono,
Azeret Mono eller Sometype Mono finns i den listan. Ingen cell i r1–r7 länkar till Fontshare
över huvud taget.

**Röst — grotesk. Fem kandidater, rangordnade.**

| # | Snitt | Källa | Varför den passar objektet | Risk |
|---|---|---|---|---|
| **1** | **Switzer** (Indian Type Foundry) | Fontshare, variabel `wght` 100–900 | Extremt jämn färg i text och en ovanligt komplett viktaxel. Jämnheten är precis vad tvåtonsdevicen kräver: när metrikerna är identiska och bara fyllnadsfärgen skiljer får snittet inte ha någon egen händelse på raden. Och 100–900 ger rubrikhalvans degradering 500 → 200 gott om väg utan att någonsin nå axelns ände | Neutraliteten kan läsas som Inter-nära; motverkas av att den bara sätter **en** rad på hela sidan, i displaygrad, och att den raden alltid är tvåtonad |
| 2 | **Onest** | Google Fonts, variabel `wght` 100–900 | Samma axelbredd som Switzer men med lite varmare terminaler, vilket rimmar med det varma papperet. Enklare att vendora (Google Fonts) om Fontshare-vendoringen krånglar | Värmen i snittet plus värmen i papperet blir två värmekällor; TASTE § 1 vill ha en |
| 3 | **Host Grotesk** | Google Fonts, variabel `wght` 300–800 | Samtida grotesk med tydlig egen karaktär i displaygrad och full kursivaxel | Axeln stannar vid 300, så degraderingen 500 → 200 får inte plats; skulle behöva skrivas om till 700 → 300 |
| 4 | **Satoshi** | Fontshare, variabel `wght` 300–900 | Geometriskt neutral, mycket ren i stora grader, sitter bra ihop med en mono | Samma axelproblem som Host Grotesk, och den är närmare "SaaS-default" än jag vill vara på en sida som argumenterar mot SaaS-default |
| 5 | **Anek Latin** | Google Fonts, variabel `wdth` 75–125 + `wght` 100–800 | Breddaxeln skulle kunna låta rubriken komprimeras när halvan degraderar, alltså en andra degraderingsdimension utan snittbyte | Två axlar i rörelse samtidigt är svårt att hålla smakfullt, och breddaxeln flyttar sömmens position, vilket bryter continuity |

**Förstavalet, motiverat enligt de fyra stegen:** **Switzer**. Steg 1:s ord är *jämförd,
tryckt, varm* — jämförelsen kräver att de två halvorna av raden är mätbart identiska, och
Switzer är ritad för att inte ha någon egen händelse. Steg 2: den står inte på någon
förbudslista och är inte K3:s val eller reserv. Steg 3: det fysiska objektet är två utskrifter
kant i kant, inte en tidskriftsrubrik; ett snitt med karaktär skulle konkurrera med det bevis
som ligger under raden. Steg 4: den sammanfaller inte med reflexen (Inter / Geist /
Instrument Sans). Praktiskt: en variabel `.woff2` täcker 100–900 och håller typsnittsbudgeten
(≤ 3 filer, ≤ 300 kB, `performance.md` § 1). **Reservval om Fontshare-vendoringen faller:
Onest**, med en rad i decision ledger.

**Register — mono. Fem kandidater, rangordnade.** Rollen är liten och exakt: två kickers
(`Före` / `Efter`), skillnadsliggarens radetiketter, radnumren 01–03 och de tre bildtexterna.
Aldrig en rubrik, aldrig brödtext.

| # | Snitt | Källa | Varför | Risk |
|---|---|---|---|---|
| **1** | **Reddit Mono** | Google Fonts, variabel `wght` 200–900 | Ritad för läsning snarare än för kod, mycket jämn färg och entydiga siffror i 11 px med öppen tracking. Den läser som en etikett på ett tryckark, inte som en terminal, vilket är rätt för en sida vars ämne är två utskrifter | Liten karaktär i 11 px; motverkas av tracking 0,18 em och versal sättning |
| 2 | **Red Hat Mono** | Google Fonts, variabel `wght` 300–700 | Lugn, smal, mycket tydliga siffror; sitter neutralt bredvid en neutral grotesk | Ännu mindre karaktär än Reddit Mono |
| 3 | **Azeret Mono** | Google Fonts, variabel `wght` 100–900 | Kantig och mekanisk, stark i siffror, bred axel | K3 har den som fjärde reservval; att ta den kostar K3 ingenting (K3:s kedja är Martian Mono → Spline Sans Mono) men minskar K3:s marginal |
| 4 | **Sometype Mono** | Fontshare | Varm och rundad mono med gott siffermaterial, och värmen rimmar med papperet | Samma "två värmekällor"-invändning som Onest; dessutom K3:s femte reservval |
| 5 | **Sono** | Google Fonts, variabel `wght` 200–800 + `MONO`-axel | `MONO`-axeln låter etiketterna gå från proportionella till monospacade, vilket vore en fin teknisk detalj | En axel som ingen ser är en axel som inte är värd sin filstorlek |

**Förstavalet:** **Reddit Mono**, i register-rollen och ingen annan. Rollerna korsar aldrig
(TASTE § 4.2): Switzer sätter aldrig en etikett eller ett radnummer, Reddit Mono sätter aldrig
en rubrik, en brödtext eller ett pris.

**Krock-hantering mot K3.** K3:s val är **Chivo** (röst) och **Martian Mono** (register), och
dess reservkedja är General Sans → Sora → Anybody → Darker Grotesque respektive
Chivo Mono → Spline Sans Mono → Azeret Mono → Sometype Mono. **K4 rör ingen av dem.**
Switzer och Reddit Mono står varken som val eller som reserv i K3, så K3:s kedja är intakt och
K3:s egen krockregel ("om K4 väljer Chivo tar K3 General Sans; om K4 väljer Martian Mono tar
K3 Spline Sans Mono") **utlöses inte**. Skulle lead byta K4:s förstaval till reservkedjans
tredje eller fjärde plats (Azeret Mono, Sometype Mono) trampar K4 in i K3:s reserver, och då
måste K3 informeras med en rad i båda cellernas ledger.

### (7) Vad referenserna gör som cellen måste slå

| Låst referens | Vad den gör | Vad K4 måste göra bättre |
|---|---|---|
| **paper** (primär) | Delar en rubrik på två fyllnadsfärger med identiska metriker, och hägnar in sitt enda blå till märket och kodsyntax, aldrig till knapp eller länk | Ge de två tonerna en **betydelse**: hos Paper är brytningen retorisk (påstående mot fortsättning), hos K4 markerar den var den ena webbplatsen slutar och den andra börjar. Och sedan **förstöra devicen med avsikt**: när delaren passerar tunnas före-halvan och tappar sin identiska metrik, vilket är det enda sättet att låna en referens och ändå äga den. Paper:s device är statisk; K4:s konsumeras av berättelsen |
| **harkcap** (sekundär) | Undanhåller identitet tills pekaren är på plats (hover-reveal roster) och låter ett enda renderat objekt bära hela auktoriteten, med postens egen anmärkning att objektet saknar metafor | Flytta undanhållandet från pekaren till berättelsen, så att det händer även för den som aldrig hovrar: "efter"-sidan finns på skärmen från första bildrutan men blir inte hel förrän delaren passerat. Och ha ett objekt som **är** metaforen i stället för att sakna en: objektet är den sida kunden faktiskt kan köpa |
| **mode** (sekundär) | Hägnar in accenten till en komponenttyp och bygger ett mörkgrönt statkort kring `8.2K` med ett stapeldiagram | Skärpa inhägnaden från komponenttyp till **objekt** (delaren finns exakt en gång, en komponenttyp kan förökas), och slå statkortet genom att inte ha något: samma sorts tal, samma displaygrad, men mätta ur två filer på disk, med kommandot utskrivet, i en hårlinjeliggare utan ett enda kort |
| **gocanopy** (sekundär) | Ramar in rubriken med två små monoetiketter, en över med publiken och en under med det tekniska påståendet, så att meningen flankeras av maskinröst | Rotera inramningen 90°: `Före` till vänster, `Efter` till höger, så att metadata **namnger de två halvorna** i stället för att stötta ett påstående. Två etiketter, inte fler, och de säger bara vad man tittar på — aldrig ett värdeomdöme, aldrig ett tillstånd |
| **customer-io** (wildcard) | Iscensätter en produktskärmbild inne i ett fotograferat rum för att låna livsstilsfotots trovärdighet åt en skärmbild | Behöva noll lån. Produkten ligger inte i ett foto av ett rum, den körs i ramen och går att använda med musen (PRODUCT.md princip 1). Där customer.io lånar trovärdighet visar K4 upp den, och det är den enda referens i uppsättningen som cellen slår genom att **ta bort** ett steg |
| **before-ai-slop** (anti-referens, och här: innehåll) | Bygger ett låtsas-dashboard av `<div>`, gradientsätter ett ord i rubriken och möblerar med badge, pill, logotypvägg och tre ikonkort | Aldrig citera ett enda av dess drag i sitt eget lager, och aldrig påstå något om den som inte är mätt. Att visa den ärligt och sätta sex sanna tal bredvid den är ett hårdare argument än varje adjektiv, och det är kontrollerbart av vem som helst med kommandoraderna i § Mätning |

### (8) Rut-testet

**Kategorins default för "digital byrå", tre rader, hållen utanför:**

1. Centrerad hero med en badge-rad ovanför, ett gradientfärgat ord mitt i rubriken, två
   pill-CTA och en avatarstack, över en vit-till-lila grund, med ett dashboardkort till höger.
2. Logotypvägg av kundmärken, tre likadana ikonkort för tjänsterna, ett statband med fyra tal,
   tre priskort där ett bär "populärast".
3. Teamporträtt i rutnät, omdömeskarusell med stjärnor, kontaktformulär, och ett mörkt
   CTA-band som avslutning.

Kategorin har dessutom en fjärde default som gäller specifikt Sverige, och den är hämtad, inte
gissad: **de fem levande rubrikerna i § *Fem live-rubriker* i `runs/K4/BRIEF.md`** säger fyra
gånger av fem bara vad företaget är och var det ligger. Alunix ordagranna rubrik säger i
stället något om läsaren. Ingen ny rubrik i K4 får falla tillbaka till formen
"substantiv plus ort".

**Var målbilden möter defaulten, och vad som ändras:**

| Punkt där K4 riskerar att sammanfalla | Vad som ändras |
|---|---|
| En före/efter-slider är i sig ett byrå-default, ofta med handtag och "dra mig" | Fyra mekaniska motmedel, utskrivna i troplistans sista rad: ingen ritad affordans, delaren är sidans chrome och inte en komponent i den, den återgår aldrig till mitten, och "före" är en verklig etiketterad fil i repot |
| Ett dashboardkort i heron = kategorins reflex, och antagonisten har ett | K4 bygger noll gränssnitt. Varje gränssnitt på skärmen är en fil som serveras. Gate 47/79-kontrollen i troplistan är den mekaniska spärren, och K4:s eget lager får bara innehålla rubrik, monoetikett, liggarrad, hårlinje och delare |
| Tre tjänster i rad (01–03) = samma *form* som tre ikonkort | Tre rader ur en mask, olika radlängd, ett radnummer i 11 px mono i marginalen och en hårlinje under. Aldrig tre lådor, aldrig en ikon, aldrig lika bredd |
| Tre paket med priser = samma *form* som tre priskort | En stycklista med ledarpunkter fram till en prisokolumn. Ingen ram runt något pris, ingen "populärast", ingen jämförelsetabell, och `Pris vid förfrågan` skrivs i klartext i stället för att gömmas bakom en knapp |
| Att visa kundarbete = samma *form* som logotypvägg eller projektgrid | Calyx live i folden, Hōrai och Hyperborea som två full-bleed objekt, ett i taget, med de ordagranna bildtexterna. Noll logotyper, noll kundnamn utöver de tre sajterna |
| Sticky topprad med länkar och en CTA-knapp | Ingen topprad alls. Navigationen är delaren, och kontakten är en mailto i löpande text |
| Ett mörkt CTA-band som avslutning | Avslutet ligger på samma varma papper som resten av sidan och är avsiktligt osymmetriskt. Ingen inversion, ingen knapp, ingen footerrad |
| Siffror som "bevis" (betyg, antal projekt, år i branschen) | Existerar inte. PRODUCT.md § absences förbjuder dem. Varje tal på sidan är antingen mätt ur en fil på disk med kommandot utskrivet, eller `26 900`, `38 900` eller `01–03` |

---

## Öppet

- **Q11** (`QUESTIONS.md`): planens § 7.5-lista över förväntade katalogposter för K4 stämmer
  till 60 % med `select.py`s deterministiska utfall; `future-fur` föll på ett poäng och en
  alfabetisk tiebreak, `dovetail` på sitt register. Antagande tills svar: skriptets rad gäller.
- **Q12** (`QUESTIONS.md`): PRODUCT.md § Operating Context säger "en ram som visats får aldrig
  transformeras eller tonas efteråt", men K4:s signatur kräver att mallsidans mättnad faller.
  Antagande tills svar: regeln gäller de **tre Alunix-exempelsajterna**, inte antagonisten, och
  ingen ram transformeras eller skalas någonsin.
- **Q13** (`QUESTIONS.md`): demo-skärmbilderna i `tests/alunix-concepts-r3/build/assets/` är
  daterade 2026-09-04 och de tre sajtfilerna ändrades 2026-09-09 (F-011-borttagningen av
  `prefers-reduced-motion`-blocken, okommitterat i arbetskatalogen). Antagande tills svar:
  skärmbilderna ska skjutas om innan de används.

## V3d · Inverterad variant

Antons beställning 2026-09-18. En kopia av V3c (md5 `864c38aa`) där bara den nya versionen
ändras: processakten och jätterubriksektionen inverterade, prissektionen flyttad ned på
avslutets grund, adressen mindre, arket och Calyx större, varje fas en egen scen. V3c står
orörd som jämförelse. Planen: `runs/V3d/plans/048-*.md`.

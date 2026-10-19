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

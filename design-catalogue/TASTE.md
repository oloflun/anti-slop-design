# TASTE.md — Antons smakprofil, läst ur katalogen

Skriven 2026-09-04 av Claude efter egen läsning av alla 89 källor (55 råa skärmbilder Anton
sparat själv, 34 Refero-exporter) som bilder och text. Anteckningarna bakom:
`taste/notes-raw-read.md`, `taste/notes-refero-read.md`. Profilen beskriver **harmonin**, hur
typ, bild, yta och rörelse förhåller sig till varandra, inte vilka färger eller typsnitt som
ska användas. Färg och typsnitt härleds fortfarande ur varumärket (Tier 0–2); det här säger
hur de ska *samspela* när de väl är valda, och vad som aldrig får hända.

Hur den används: `design/SKILL.md` Step 1b läser den när beställaren är Anton eller när
briefen saknar referenser. Reference-lockens preserve-lista prövas mot avsnitt 4.
Bake-offens riktningar seedas ur avsnitt 3.

---

## 1. Det genomgående temat: en auktoritet per sida

Varje sparad sida låter **en enda sak** bära uppmärksamheten, och allt annat drar sig
tillbaka för den. Det är den enskilt tydligaste regeln i materialet, och den håller tvärs alla
kategorier:

| Auktoriteten | Då gör typen | Då gör bilden | Då gör ytan | Exempel |
|---|---|---|---|---|
| **Typen** (ordmärke eller rubrik i viewport-bredd) | 100–265 px, en vikt, stram | tyst: liten, bredvid, eller bakom typen som ett lager | flat papper eller flat färgblock | Garden Eight, Shelby Kay, SpringSummer, Busy Bee, Indoek, Studio Ag, Mattis, Magnetism |
| **Fotot** (fullbleed, mörkt eller överexponerat) | vikt 300, ljus, stor men luftig, lägger sig i fotots mörka del | allt | ingen: fotot är ytan | Squarespace, Planhat, Apollo, Amrit, Montoni, Geon, Rogo, Diamond Rose |
| **Ytan/materialet** (papper, linne, terrakotta, celadon) | medelstor, gärna serif, får ta plats men inte skrika | plates bredvid texten, aldrig under | bär allt: ton-på-ton, hårlinjer, inga skuggor | Raus, Beautiful, Palais, TOMO, alet, Miti, Caractère Bois, Kinhive |
| **Produkten** (objektet ofriat i mitten) | uppercase 500 i små grader, eller helt tyst | ett objekt i tomrum | mörk eller flat | ORYZO, Busy Bee, Hungry Tiger, Aarke, David, Altitude |
| **Rörelsen** | tyst | tyst eller suddig | ljus, luftig | Perplexity, dope.security, alet, Bumble, Comet |

Sidor där två av dessa konkurrerar finns inte i materialet. Det är därför Antons "för
snarlika"-kritik träffar de kedjebyggen som la stor serif *och* starkt foto *och* accentfärg
i samma fold: tre auktoriteter är ingen.

**Regel:** namnge auktoriteten innan koden. Allt som inte är auktoriteten går ner ett steg
i vikt, storlek eller mättnad.

## 2. Fem relationer som återkommer

1. **Tyst typ ↔ stark bild, stark typ ↔ tyst bild.** Weight 300 vid 64–110 px sitter alltid på
   ett foto eller ett tomt papper. Fet eller kondenserad display (Busy Bee 238 px, Shelby Kay
   265 px) sitter alltid på en flat yta. Undantaget som håller: tung grotesk *genom* ett orört
   foto (Indoek, What Matters, Go RVing, Mattis), men bara när typen är tung nog att tåla
   fotot. Tunn typ på ett ljust, brusigt foto förekommer noll gånger.
2. **Ett papper, en accent.** 69 av 89 har en varm eller kall "paper"-yta och exakt en
   kromatisk färg som gör en sak: CTA, understryk, ordmärke. Vit yta är sällsynt (Paper,
   Not Real, Andre Candido, Aarke) och då är den *varmvit* och typen är svart. Två accenter
   förekommer bara i consumer/playful (OLIPOP, Palais, Shepherd).
3. **Struktur med hårlinjer och ton-på-ton, aldrig med kort.** Skuggade kort: 0 av 89 där
   Anton valt (de finns i tre AI-mallar, som defaults). Djup kommer av cream-på-cream,
   1 px-linjer, överlapp och färgband som byter *material* mellan sektioner.
4. **Storlekskontrast 5–15×, inte 2–3×.** Display 64–265 px mot body 14–17 px. En sida med
   "h1 48 / h2 32 / p 16" finns inte i materialet. Mellanrubriker är antingen små uppercase
   kickers (11–13 px, tracking 0.1–0.2 em) eller lika stora som display. Mellanläget saknas.
5. **Rundning är ett beslut.** Antingen 0–3 px (Amrit, Apollo, alet, Not Real, Squarespace,
   NGLM) eller stor och avsiktlig (Raus 20/40, Bumble 16–24, pill-knappar 999). Ingen ligger
   på 8 px-default.

## 3. Per kategori: harmonin, och vad som bär

Kategorierna är de i `categories.md`. "Bär" = auktoriteten enligt avsnitt 1.

### product-focused (SaaS, verktyg)
Bär: **fotot som stämning** (Planhat, Sanity, Rogo, HappyRobot) eller **produkten som bild**
(Paper, Solva, customer.io, Operator). Typ: neo-grotesk 300–400 i stor grad, stram tracking,
eller en två-tons rubrik (Paper: mörk första rad, grå fortsättning). Ytan: mörk eller varmvit,
aldrig lila. Rörelse: subtil, aldrig "breathing". Siffror som textur (Hark, RRE, NGLM) i
display-grad med liten etikett, ruled. **Det Anton avvisar här:** feature-grid med ikoner,
"trusted by"-logg-rad som fyllning, tre lika kort. I mallarna han sparat (Nura, Solva, Areto)
är det heron han sparat, inte resten.

### portfolio / studio
Bär: **typen som verket.** Ordmärke eller påstående i viewport-bredd (Magnetism, Garden
Eight, Studio Ag, Mattis, Example, Orix). Arbetet i asymmetriskt grid, metadata i marginalen
(mono eller 11 px uppercase). Ingen CTA-fyllning; kontakt är en textrad. Ytan: papper eller
flat färgblock; Mattis och Lucci visar att ett helt orange eller rött band är tillåtet när
typen är tung grotesk.

### institutional
Bär: **lugn skala.** Få enheter, stor luft, en sats i taget (Hark, RRE, Montoni, Equity Fund).
Typ: grotesk 300–400 eller en lugn serif, aldrig kondenserad. Data som textur är kategorins
signatur. Foto: landskap eller material, mörkat. Rörelse: nästan ingen.

### editorial
Bär: **ytan + rytmen.** Papper, kolumner, kickers, plates bredvid texten, journal-rytm (Raus,
Indoek, Caractère Bois, Dovetail, Redbrick, Aevi). Serif tillåten och vanlig, men alltid med
en grotesk eller mono för etiketter, aldrig serif på etiketter.

### hospitality / plats
Bär: **fotot.** Typen anpassar sig: ljus 300-serif *i* fotots mörka del (Amrit, Apollo,
Montoni, Geon) eller display-serif på papper *bredvid* fotot (Raus, Miti, Diamond Rose).
Alltid en enda handling (boka/sök) i en enda färg. Ordmärke i viewport-bredd är vanligt
(Diamond Rose, Maloot, Miti-kurvan).

### consumer-brand
Bär: **produkten och färgen.** Flat färgblock, produkten ofriad i mitten, condensed/fet
display 100–240 px (Busy Bee, Hungry Tiger, David, Lucci, Deon Libra). Marquee-remsan som
avdelare hör hit och ingen annanstans. Färgen får vara lek; typen är sign-painting.

### luxury-craft
Bär: **ett objekt i tomrum.** Cream-typ, uppercase 500 i små grader, allt annat tyst (ORYZO,
Diabla, Dix Hectares, Aarke, Geon). Material före dekor: sten, kork, linne, stål.

### playful
Bär: **färgen eller rörelsen** (Bumble, OLIPOP, Palais, Andre Candido). Illustration bara som
teckning eller 3D-objekt, aldrig som ikon-set. Två accenter tillåtna, inte tre.

## 4. Beslutsregler för typsnitt och bild, så att de samspelar

Dessa är de regler kedjan ska pröva varje val mot. De gäller *utöver* varumärkets egna
tokens.

1. **Välj auktoritet först, typsnitt sedan.** Bär fotot: välj ett snitt som tål vikt 300 i
   80 px (neo-grotesk eller en serif med låg kontrast). Bär typen: välj ett snitt med
   karaktär i 150 px+ (kondenserad grotesk, didone, eller ett ovanligt display-serif) och
   håll fotot litet. Bär ytan: en lugn serif i 40–70 px och grotesk för allt annat.
2. **Två snitt, aldrig tre, och rollerna korsar aldrig.** Ett för röst (display + body eller
   bara display), ett för register (etiketter, siffror, nav). Mono får bara vara register.
   Serif får aldrig vara etikett.
3. **Bilden väljs efter hur mycket typ den ska bära.** Typ över foto kräver antingen ett
   mörkt/överexponerat parti där typen får stå (mät kontrasten under den ljusaste ramen,
   Step 5), eller en typvikt ≥ 700. Annars läggs fotot bredvid texten som en plate med
   caption. Aldrig scrim över hela bilden som räddning.
4. **Ett papper, en accent, och accenten gör en sak.** Bestäm vad (CTA, understryk,
   ordmärke, en siffra) och låt den inte göra något annat. Andra accenten kräver kategori
   consumer/playful och en motivering i beslutsledgern.
5. **Sektioner byter material, inte bara bakgrund.** När sidan behöver en ny akt: helt
   färgband, mörk-till-ljus inversion, eller papper-till-foto. Inte "grå sektion".
6. **Kontrast i skala, inte i vikt.** Display minst 5× body. Mellanrubriker antingen som
   kickers (små, tracking) eller lika stora som display. Aldrig en 32 px-mellannivå.
7. **Djup utan skugga.** Hårlinjer, ton-på-ton, överlapp, inversion. Skugga bara på en
   flytande komponent (modal, sökfält) och då knappt synlig.
8. **Rörelse bara där typ och bild är tysta.** Är auktoriteten typ eller foto: reveal och
   pin räcker. Är auktoriteten rörelsen: låt typen vara 300 och bilden suddig.
9. **Siffror får vara textur bara om de är sanna.** Formen (display-grad, liten etikett,
   ruled) tas; innehållet måste vara systemets eget (Alunix-regeln).
10. **Ordmärket får vara heron.** Namnet i viewport-bredd, sloganen liten, är en fullt
    tillåten fold i den här profilen och ofta den starkaste.

## 5. Avvisat, med belägg

Förekomst i 89 sparade källor: ikongrid 0 · gradient-mesh 1 (Brand Federation, sparad för
heroformen) · glasmorfism 0 · centrerad hero med badge-rad 0 (utom AI-mallar) · lila/indigo-
accent 1 (dope.security, som glöd) · skuggade 8 px-kort 3 (alla mall-defaults) · stockfoto av
leende team 0 · "h1 48 / h2 32"-skala 0 · dekorativa blobbar 1 (Palais, handritade) ·
tre lika feature-kort 4 (alla i AI-mallar Anton sparat för heron).

Slutsats: det Anton *inte* har sparat är lika entydigt som det han sparat. Ett bygge som
innehåller något ur listan ovan ligger utanför profilen oavsett hur välgjort det är.

## 6. Den korta versionen (för Step 1b)

En auktoritet per sida. Tyst typ på stark bild, stark typ på tyst yta. Ett papper, en accent
som gör en sak. Hårlinjer och material, inte kort och skuggor. Skala 5× eller mer. Namnet får
vara heron. Sanna siffror som textur. Rörelse bara där allt annat är tyst.

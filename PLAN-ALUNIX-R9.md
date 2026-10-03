# Plan · Alunix V3g, runda R9 (väntar på Antons ja)

Underlag: Antons nio skärmdumpar (2026-10-03), `tests/alunix-r8/runs/V3g/index.html`,
`EFFECTS.md` (skyddade effekter), `ANTON-VISION-OCH-FEEDBACK.md`. Inget under
`tests/alunix-r8/runs/V3g/` eller `sites/` är ändrat. Varje punkt: nuläge → orsak → åtgärd →
vad som skyddas → hur det verifieras.

Status för diagnoserna: **[PIXEL]** = reproducerad headless och mätt, **[KOD]** = läst i koden,
väntar på pixelbekräftelse.

---

## 1. "Er hemsida är nutidens visitkort" fragmenteras efter scroll ned → upp

**Nuläge.** Skärmdump 5: högst upp står bara små streck kvar av rubriken; raderna är utskjutna ur
sina masker.

**Orsak.** Två tweens äger samma egenskap på samma element: laddningstidslinjen tar
`h1Split.lines` från `yPercent:100` till `0`, och hero-scrubben (`heroTl`, position 0.75) driver
samma `yPercent` till `-16 − i·12`. Scrubbens `.to()` läser in sitt startvärde när ScrollTrigger
första gången renderar tidslinjen, vilket sker vid skapandet, innan laddningen är klar, medan
raderna fortfarande står på `100`. När besökaren scrollar tillbaka under 0.75 återställs raderna
till det inspelade startvärdet `100`, alltså gömda i masken.

**Åtgärd.** Dela ägarskapet: laddningen behåller raderna (`h1Split.lines`), scrubben flyttar i
stället maskerna (`h1Split.masks`) med `y`. Masken följer med texten, så rörelsen ser likadan ut,
men de två tidslinjerna rör aldrig samma egenskap. Ingen `fromTo`-lapp som bara flyttar felet.

**Skyddas.** Hero-laddningen (sömmarna, raderna som reser sig, kortet). Kortvändningen orörd.

**Verifiering.** Headless: ladda, vänta 3 s, scrolla förbi heron, scrolla till 0, skärmdump +
`getBoundingClientRect` per rad (ska ligga inom sin mask). Samma körning mot dagens fil först,
som ska fallera (bevis för att testet mäter felet).

## 2. Hyperborea-framen bort · ny tessekvens till "Vi hjälper er att synas på rätt sätt."

**Nuläge.** Under den pinnade tesrubriken ligger tre rader i en stapel ("Skärmen möter
besökaren…", "Innan ett ord är läst…", "Vi hjälper er…") bredvid en skärmdump av Hyperborea.

**Åtgärd.**
- Ta bort `.tes-lower` (stapeln och Hyperborea-bilden) och dess JS (`.tes-line`-loopen).
- Ny sekvens i samma svarta, pinnade cell: "Det första intrycket är digitalt." står hel och stilla
  (≥ 40 vh, som i dag), och **övergår** sedan i "Vi hjälper er att synas på rätt sätt." utan klipp:
  de första bokstäverna sjunker ned ur sina radmasker i samma ordning som de steg upp, samtidigt
  som den nya meningen reser sig bokstav för bokstav i samma masker. Två meningar, ett golv,
  samma mekanism som Anton godkänt (char-rise), nu i båda riktningarna. Den andra meningen står
  också hel och stilla ≥ 40 vh innan pinnen släpper till processen.
- Pinnens längd: 0,9 vh i dag → ca 2,2 vh (rubrik 1 håller, övergång, rubrik 2 håller). Scrubbad
  övergång (Lenis är enda utjämningen, F-020), inte en toggle som spelar på tid.
- Copy: Anton skrev "Vi hjälper er synas på rätt sätt." Sidan har i dag "…er **att** synas…".
  Jag behåller "att" om du inte säger annat.

**Skyddas.** Tesrubrikens signatur i EFFECTS.md: samma pin (`pinType:'transform'`), samma
char-rise, samma p95-gräns i `#tes` (≤ 33 ms). Rubriken står hel ≥ 40 vh, nu två gånger.

**Verifiering.** `section_probe.py` mot baslinjen för `#tes`; sheet med 20 steg genom sekvensen;
läsfönster mätt (andel av pinnen då varje mening är helt synlig).

## 3. Showcase-rutorna: bort med den undre texten, ny ingress som säger varför

**Nuläge.** Varje steg har rubrik + ingress (`.showcase-lede`) + ett mindre stycke
(`.showcase-more`). Flera ingresser beskriver det ögat redan ser ("Fotona står parvis, och det
högra ligger lite lägre…"), och Calyx-steg 3 nämner Hotel Pigalle och Drottninggatan.

**Åtgärd.**
- Ta bort alla 11 `.showcase-more` (och CSS:en för dem).
- Skriv om de 11 ingresserna: tänket bakom valet, vad som valdes bort och vad det betyder för
  besökaren. Aldrig en beskrivning av det som syns. Inga plats- eller personnamn (Stockholm ok).
- Utkast (går genom copywriting → copy-editing → humanizer-svenska vid bygget, och kontrolleras mot
  `sites/calyx.html` / `sites/horai.html` så att inget påstår något sidan inte gör, F-023):

**Calyx**
1. *Sidan öppnar som ett omslag* — Blommor väljs med ögonen innan någon läser ett pris. Därför fick
   fotot första skärmen och menyn fick vänta, så att det första besökaren möter är arbetet och inte
   en knapp. Omslaget ger också ateljén ett skäl att byta bild varje säsong, och då känns sidan ny
   utan att byggas om.
2. *En serif får bära allt* — Ett enda typsnitt genom hela sidan gör att den läses som en trycksak
   och inte som reklam. Ateljén levererar till hotell och restauranger som själva lägger pengar på
   sitt tryck, och de ser skillnaden direkt.
3. *Varje bild är ett uppdrag* — En bildtext som säger "vårbukett" upprepar bara bilden. Texten
   under varje foto säger i stället vad buketten var till för, en lobby, en middag, ett hem. Då ser
   besökaren vilka uppdrag ateljén tar och kan föreställa sig sitt eget bland dem.
4. *Veckans utbud på en rad var* — Ett utbud som byts varje vecka måste gå att ändra på en minut,
   annars blir det liggande. En lista i stället för ett rutnät av foton betyder att ateljén skriver
   om en rad, och att besökaren jämför buketter och priser utan att scrolla.
5. *Ett mejl räcker* — Den som beställer till ett rum vill beskriva ljuset och tillfället, och det
   ryms inte i formulärfält. Ett mejl tar längre tid än en bokningsknapp, men svaret kommer från den
   som ska binda buketten, och det är det en kund hos en liten ateljé betalar för.

**Hōrai**
1. *Ett namn, en gång* — En restaurang utan skylt mot gatan måste bli ihågkommen på skärmen. Namnet
   står ensamt och stort, och loggan i menyraden väntar tills det rullat förbi, så att namnet aldrig
   står två gånger samtidigt och tappar i tyngd.
2. *Ett tecken som stämpel* — Texten om huset tänds ord för ord och går inte att skumma. Den läses i
   samma takt som någon berättar vid bordet. Rött är sparat till tecken, rubriker och priser, så att
   ögat senare hittar priserna utan att leta.
3. *En mening som saktar in* — Mellan huset och menyerna behövs en paus, som mellan två rätter. En
   bild hade fyllt platsen. En mening som bara går att läsa när man stannar gör att menyerna inte
   läses i samma andetag som berättelsen.
4. *Priset står större än namnet* — Med en meny per kväll är det priset gästen jämför. Ett pris som
   står litet ser gömt ut, och den som måste leta efter det har redan börjat tvivla. Därför är det
   sidans största siffra.
5. *Rummet före bokningen* — De flesta restauranger visar matsalen först. Här kommer den sist,
   precis före bokningen, där den svarar på gästens sista fråga: var ska vi sitta?
6. *Knappen fanns där hela tiden* — Den som bestämmer sig tidigt ska inte behöva leta, så bokningen
   följer med hela vägen ned. Sidan säger också när veckans platser släpps, så att ingen skriver till
   en kväll som redan är full.

- **Namnen bort ur exempelsajterna också** (de visas i iframen och i förstoringsutsnitten):
  `sites/calyx.html` har Hotel Pigalle, Drottninggatan, Strandvägen 7B, Surbrunnsgatan 50,
  Vasastan, Djurgården; `sites/horai.html` har Hornsgatan. Ersätts med uppdragets syfte (lobby,
  middag, hem) respektive "Stockholm". Förstoringsutsnitten (`assets/steps/calyx-*.webp`,
  `horai-*.webp`) skjuts om med `loupe.py` efteråt, annars står namnen kvar i bilderna.

**Skyddas.** Showcase-mekanismen (en pin, övertoning, räknare + mintspår) och casebytet. Bara text
och en rad CSS ändras i rutan.

**Verifiering.** `microtext_scan.py` + en ny namnkontroll (se § 6) över boarden och båda
sajterna; skärmdump av varje steg; F-023-kontrollen mot källan.

## 4. Avstånd: "Alla har rätt till bra design." och visitkortet efter prispaketen

**4a Nuläge.** Skärmdump 7–8: g:et i "design." når nästan ingressen. **Orsak:** `.headline-50` har
`line-height:.8`, så descendern sticker ut ca 0,2 em under radboxen, och ingressen har bara
`margin-top:16px` (vid 1920 px är rubriken 200 px, descendern ~40 px). **Åtgärd:** avståndet räknas
från rubrikens storlek, `margin-top: calc(var(--headline-50) * .32)` (≈ 64 px vid 1920, ≈ 20 px på
mobil), som klassregel för all löptext direkt under en `headline-50`, inte bara här.

**4b Nuläge.** Skärmdump 2 och 6: efter priserna kommer ett svart band och sedan
kontaktsektionen, där rubriken står längst ned i sin ruta och visitkortet sitter i nedre halvan av
en 100svh-hög ruta, alltså vid skärmens underkant när rubriken väl syns. **Orsak (kod):**
`.kontakt-q--ov{justify-content:flex-end}` (rubriken i botten), `.kontakt-card-anchor{grid-row:2}`
(kortet centrerat i nedre raden, flyttat dit i R6 för att inte krocka med en bottenställd rubrik),
plus `.rhythm` 110 px mellan pris och kontakt. **Åtgärd:** rubriken i ÖV flyttas till optisk mitt
(§ 5), vilket frigör plats ovanför korsningen; kortet återgår till att sitta **på** korsningen av
de fyra rutorna (som i heron), med uppmätt fritt avstånd till "verksamhet." under hela vändningen;
rytmbandet före kontakten kortas eller tas bort. Exakta värden sätts efter mätning.

**Skyddas.** Kontaktkortet (vänder sig självt vid 0,7, heron speglad).

**Verifiering.** `getBoundingClientRect` för rubrik, ingress och kort vid 1440/1280/768/390 under
hela vändningen (minsta avstånd ≥ 24 px); skärmdump från "38 900 kr" ned till kortet.

## 5. Optisk mitt: text något ovanför mitten

**Nuläge.** Heron (`.hero-ov{align-items:flex-end}`) och kontakten ställer rubriken i botten av
sin ruta; tesrubriken står i toppen.

**Åtgärd.** I helskärmsvyer sätts textblockets tyngdpunkt 4–8 % ovanför den geometriska mitten
(45 % i stället för 50 %). Gäller hero-rubriken, tessekvensens två meningar, "Berätta om er
verksamhet." och prisrubriken. Regeln skrivs in i `house-physics.md` § Layout (och vision-
dokumentet uppdateras från "öppet" till "infört") först när den är verifierad i pixlar här.

**Skyddas.** Heron-sömmarna och kortet; hero-rubriken får inte hamna under kortet (mäts).

**Verifiering.** Mätt tyngdpunkt per vy (`(top+bottom)/2` av textblocket / viewporthöjden), mål
0,42–0,46.

## 5b. Priserna bort, paketen beskrivs (Antons tillägg 2026-10-03)

**Nuläge.** Tre rutor: mint med "Standardpaket…" + **26 900 kr**, vit med bokningspaketet +
**38 900 kr**, grå med skräddarsytt + "Pris vid förfrågan". Siffrorna räknas upp med `countUp`.

**Åtgärd.**
- Ta bort alla tre prisvärdena och `countUp`-anropen för dem.
- Där priset stod: paketets **namn** i samma visningsstorlek (det är fortfarande rutans
  tyngdpunkt, så hierarkin i bento-rutnätet håller), och under det en beskrivning i brödtext som
  säger vad paketet gör för verksamheten, inte en funktionslista.
- Rubriken "Alla har rätt till bra design." och ingressen ("…lika noga i alla tre…") står kvar.
- Utkast (copy-grinden körs vid bygget; inget lovas som inte redan stod i paketen):
  1. **Webbplats** — En sida som presenterar er verksamhet och som ni uppdaterar själva. Texter och
     bilder ändrar ni i ett enkelt redigeringsläge, och sidan är förberedd för att hittas på Google
     från första dagen.
  2. **Webbplats med bokning** — För verksamheter där besökaren ska kunna boka och betala direkt på
     sidan. Bokningar, betalningar och kunduppgifter hamnar på ett ställe, så att ni slipper föra
     över dem för hand.
  3. **Skräddarsytt** — När sidan behöver göra något som ingen färdig lösning gör, som en
     produktkatalog med många artiklar eller ett system byggt för just ert arbetssätt. Vi börjar
     med ett samtal om vad som behövs.
- Paketnamnen är förslag; säg till om ni redan har namn på dem.

**Skyddas.** Bento-inträdet (`prisTl`: ledaren från vänster, rutorna uppifrån/nedifrån) behålls.

**Verifiering.** Skärmdump av sektionen vid 1440/768/390; inga "kr" kvar på sidan (sökning i
DOM); text 4a-avståndet mätt.

## 6. Systemet, inte bara den här sidan

- `design/SKILL.md` "Copy is worldbuilding" säger i dag *specific proper nouns, real street
  addresses*. Det krockar med din regel. Ändras till: världen byggs med fakta om arbetet (syfte,
  material, tider, priser), aldrig med verkliga plats- eller personnamn på exempelsidor; staden får
  stå.
- Namnkontroll i `microtext_scan.py`: flaggar gatunamn (`-gatan`, `-vägen`, `-torget`, `-gränd`),
  stadsdelar och "Hotel X" i synlig text. Mekanisk grind i stället för "kom ihåg".
- Rubrik/ingress-avståndet (4a) och optisk mitt (5) in i `house-physics.md` efter verifiering.

## Ordning och omfattning

1 → 4a+5b (samma sektion) → 3 → 2 → 4b+5 (de två sista hör ihop). Filer som ändras: `runs/V3g/index.html`,
`sites/calyx.html`, `sites/horai.html`, `runs/V3g/assets/steps/*` (omskjutna), plus skill-filerna
i § 6. Inget raderas utöver `.tes-lower`-blocket och `.showcase-more`-styckena. Efter bygget:
tre granskare parallellt (critic, a11y, heuristics), `scroll_verify.py`, `section_probe.py` mot
EFFECTS-baslinjen, och du ser desktop + mobil innan något kallas klart.

**Svara ja (eller med ändringar per punkt) så börjar jag.**

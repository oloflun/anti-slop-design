# 060 · V3d: Exempelcase i serif, ramar utan kant, Calyx → Hōrai utan brygga, prissektionen på en skärm, all småtext bort, Hōrais bokning i ramen

- **Status**: TODO (V3d R17, en byggrunda, högst två fixrundor)
- **Beställning**: Anton 2026-09-19 ("ser bra ut och matchar visionen väldigt nära nu"), punkterna
  1 till 8. Golvet, inte ett förslag. FEEDBACK F-016 (småtext) och F-017 (prisliggarens
  displaystorlek) är nya regler i designsystemet samma dag och gäller hela planen.
- **Ordning**: steg 7 (småtexten) först, eftersom 1, 3, 4 och 6 räknar med att kickers, bildtexter
  och rail är borta. Därefter 3, 1, 2, 4, 6, 5, 8. **Ett djärvt drag backas aldrig för att laga ett
  fel** (`runs/V3c/RAPPORT-LOOPEN.md` fel 5); följdfel lagas i samma runda.
- **Copy**: `runs/V3d/COPY-V3d-r17-final.md` finns och är final. Byggaren skriver in kolumnen
  **final** ordagrant, inklusive § "Antons beslut 2026-09-19, efter copy-gaten" och § "Pristext,
  Antons andra beställning" (val A). Byggaren hittar aldrig på en sträng.
- **Låst copy**: `PRODUCT.md` § Brand Commitments är redan uppdaterad (de tre bildtexterna borttagna i
  V3d, F-016). Låst-copy-kontrollen räknar därför **12 synliga rader** (listan i PRODUCT.md utan
  `VI BYGGER ERT VARUMÄRKE.` och utan de tre `Exempelsida:`-raderna). De tre bildtexterna lever kvar
  ordagrant som tillgängliga namn: `iframe[title]` för Calyx och Hōrai (står redan så), och
  Hyperboreas `img[alt]` ("Startsidan för Hyperborea, en konferens i Lund", står redan).
- **Estimated scope**: 2 filer. `runs/V3d/index.html`, och i `sites/horai.html` **bara**
  `section#reservations` (rad 306 till 339; Anton har hävt låset för just den sektionen). Ingen
  typsnittsfil laddas ned: det nya snittet hämtas via Google Fonts `<link>`, som sajterna gör.
  `scroll/*.js`, `scrollcraft.css`, `sites/calyx.html`, `sites/hyperborea.html` och resten av
  `sites/horai.html` orörda. Ingen ram transformeras, tonas eller klipps.
- **Underlag, läst som bilder denna session** (egen fångst, Chromium med
  `ignore_default_args=['--hide-scrollbars']`, `mouse.wheel` halva viewporten per steg, scratchpad
  `a060/`): hela case-, Hōrai- och prissträckan vid **1920x930** (32 skärmar), 1440x900 (32) och
  390x844 (31); zoomade kantutsnitt av båda ramarna; ett typsnittsprov (`spec.png`, tio snitt på
  sidans två grunder); Hōrais bokningssektion öppnad direkt vid sju ramsbredder.

## Uppmätt nuläge (R16)

| | 1920x930 | 1440x900 | 390x844 |
|---|---|---|---|
| Ramkanten | Calyx: `.case-wrap` har `border:1px solid var(--c-line-on-paper)` (rgba .14): översta och vänstra pixelraden är (220,218,213) mot sajtens (244,240,231) och papperets (253,251,244), **en ljus/beige linje**, och där bården är halvgenomskinlig syns affischbilden (`frame-poster`) igenom som korta mörka streck (x 679, y 64 och y 300: (49,76,70)). Hōrai: bården (55,55,57) över/under ramen och en ljus högerkant där affischen lyser igenom. | samma | Calyx: bården under ramen (mobilens `border-bottom`) |
| Ramkanten, sprickan | Vid DPR 1,1 / 1,25 / 1,5 / 0,9 (webbläsarzoom 110/125/150/90 %) ligger ramens kanter på bråkdelspixlar (t.ex. 549,62 css-px × 1,25). Iframens lager snäpps till hela enhetspixlar och lämnar en **halvtäckt pixelrad där stagens papper eller affischen syns** (magenta-prov: (253,63,252), (228,162,221) längs kanten). | | |
| Bryggan | "Nästa sida säljer en kväll." på en egen 100svh svart sektion mellan casen (`1920-014`, `-015`) | samma | samma |
| Prissektionen, höjd | kicker-topp → adressens underkant = **1027 px** i en 930 px viewport: rubriken kapas upptill när liggaren syns (`1920-030`, `-031`) | 1003 px i 900 | ryms inte heller, men läses i följd |
| Prisvärdena | `26 900 kr` 40 px och `Pris vid förfrågan` **också 40 px**, kontakten 48 px: text i display (F-017) | 37 / 37 / 46 px | 24 / 24 / 28 px |
| Hōrais bokning (ramen) | ryms precis (ram 1230 bred) | `book.horai.se` 45,6 px slutar på x 971 i en 900 bred ram: **"BOOK.HORAI" klipps**, adressen slutar på 892 mot spaltens 852 | "RESERVATI / OPEN MON" klipps: sajtens 12-kolumnsgrid med `gap-x-12` (11 × 48 px) har ett minimum på 675 px |
| Hōrais 390-överflöd | | | `scrollWidth` 675 med `#reservations` och **675 även utan den** (`display:none`): överflödet kommer från sajtens andra 12-kolumnsgrids (hero, meny, rätter, citat). **Punkt 8 löser det inte.** |
| Småtext | microtext_scan.py: 22 fynd vid 1440 + 390; railen, processens marginalnoter och ingressraden fångas inte av skriptet men syns i bild | | |

## Problem

1. "Så blev ritningen en sida." + kickern `EXEMPELCASE` introducerar casen med en idé i stället för ett
   namn; Anton vill ha rubriken **Exempelcase** i serif och copy-agentens text under.
2. (Behåll) Case-namnen i Geist kursiv (Calyx) och Geist versaler med spärr (Hōrai) efterliknar
   sajterna utan att byta grundsnitt. Rörs inte; Cardo/Cinzel för namnen är avskrivet.
3. En tunn färgkant runt båda ramarna, med två orsaker: (a) den halvgenomskinliga hårlinjen på
   `.case-wrap`, som dessutom släpper igenom affischbilden; (b) bråkdelsgeometri vid andra
   zoomsteg än 100 %, där en halv enhetspixel av stagen syns mellan ramens lager och kanten.
4. Bryggan är en tredje sektion mellan två ramar, och övergången papper → svart är en hård kant.
5. Hōrai → pris har ingen rörelse; det svarta glider bara ut ur bild.
6. Prissektionen ryms inte på en skärm vid 1920x930/1440x900, `Pris vid förfrågan` och kontakten står
   i displaystorlek, och rubriken saknar karaktär.
7. Liten beskrivande text (F-016) på elva ställen plus sju marginalnoter.
8. Hōrais bokningssektion är för stor för ramen: `book.horai.se` och adressen klipps vid 1440 och
   1280, allt klipps under 768 px ramsbredd.

## Target, en rad per beställningspunkt

Allt mäts i skärmbild (Playwright `mouse.wheel`, aldrig `scrollTo`, Chromium **utan**
`--hide-scrollbars`) eller `getBoundingClientRect`/`Range`/`getComputedStyle` på den byggda sidan.

| | Synligt mål | 1920x930 / 1440x900 | 390x844 |
|---|---|---|---|
| **1** | `h2#case-title` = `Exempelcase` i `--f-serif` (Young Serif 400) | textContent exakt "Exempelcase"; `font-family` börjar med Young Serif och `document.fonts.check('1em "Young Serif"')` true; storlek 136 px (1920), ~130 (1440); ordets bredd (`Range`) ≤ spalten − 8 px vid alla sju bredderna, 0 radbrytningar | 40 px, ett ord, en rad |
| **1** | texten under | `.cases-lead` = copy-filens final ordagrant (28 ord), 20 px, ≤ 44ch; ingen kicker ovanför | samma |
| **1** | kapitlet äger skärmen | `?preview=cases`: rubrik + text centrerat i 100svh papper, inget annat synligt (PARITET P14) | samma |
| **2** | namnen oförändrade | `.case-name` computed style (family, style, weight, transform, spacing, size) **identisk** med R16 vid 1920/1440/390 | samma |
| **3** | ingen kantlinje | **Magentaprov** (Verification B3): iframens dokument färgas `#ff00ff`, varje enhetspixel längs de fyra inre kanterna av `.case-wrap` är magenta (R>235, G<20, B>235) och varje pixel precis utanför är stagens grund exakt. **0 avvikande pixlar** i båda ramarna, vid 320/390/768/1024/1280/1440/1920 × DPR 1, och vid DPR 0,9 / 1,1 / 1,25 / 1,5 / 1,75 / 2 (webbläsarzoom). Dessutom: `.case-wrap` `border-*-width` 0 på alla fyra sidor vid alla bredder | samma |
| **3** | synken orörd | `?preview=case-*-0N`: ramens `scrollY` = ankaret ±2 px; hjul 20 px-steg: monoton | samma |
| **4** | bryggan borta | `.case-bridge`, `#bridge-title`, "Nästa sida säljer en kväll." = 0 träffar i DOM och i `document.body.innerText` | samma |
| **4** | avståndet | mellan Calyx-stagens underkant och Hōrai-stagens överkant står `.case-gap` på **18svh** svart (167 px vid 930); avståndet ram → ram under övergången **200 till 260 px** vid 1920x930 (mät i `?preview=case-seam`) | 152 px gap |
| **4** | scrolleffekten, lager 1 | Calyx-textspalten lämnar genom sin överkant (samma springa som `.cs`: `clip-path` uppifrån + 32 px lyft) i fönstret `--sc-ps` **0,87 till 0,91**; vid 0,91 är spalten helt klippt | samma |
| **4** | scrolleffekten, lager 2 | Calyx-stagens grund går papper → `--c-black` i fönstret **0,91 till 0,99** (`color-mix` på `--sc-ps`), ramen står still och orörd (`transform`/`opacity`/`clip-path` på `.case-wrap`/`iframe` = none/1/none i varje bildruta) | samma |
| **4** | båda riktningarna | hjul 20 px-steg ned och upp genom 0,80 till 1,0: `motion_probe` staircase 0, max_step ≤ 3 %, samma bildruta vid samma `scrollY` ned som upp (pixeldiff ≤ 1 %) | samma |
| **4** | sömlöst | pixelrad 2 px ovan och under skarven Calyx-stage/gap och gap/Hōrai-stage i `?preview=case-seam`: ΔE 0 (båda `--c-black`) | samma |
| **4** | stegtakt oförändrad | Calyx `data-sc-span` 5,5 → **6,4** och stegformlerna skalade med `--t:.86`, så scroll per steg är oförändrad (±3 %) mot R16 | samma |
| **5** | Hōrai → pris, lager 1 | en svart slöja (`.price::after`, bara `opacity`) över fotot lyfts i `#pris` `--sc-ps` **0,05 till 0,40**: fotot framkallas ur det svarta; vid 0,05 är skarven Hōrai/pris ΔE 0, vid 0,40 är slöjan 0 | samma |
| **5** | lager 2 | `#pris-title` skärps: `filter:blur` 10 → 0 px, `opacity` 0 → 1, `translateY` .25em → 0 i **0,18 till 0,40**; rubriken är helt skarp innan dess överkant når 60 % av viewporthöjden (mät vid alla sju bredderna) | samma |
| **5** | båda riktningarna, jämnt | `motion_probe` på `#pris` ned och upp från `ps` 0: staircase 0, max_step ≤ 3 %, frame p95 ≤ 20 ms vid cpu 1 | samma |
| **6** | allt på en skärm | vid dokumentets slut (sista hjulsteget): `#pris-title` överkant **≥ 48 px** och `.close-mailto` underkant **≤ innerHeight − 24 px**; ingress, alla tre raderna och kontakten helt i bild, i **samma** bildruta, vid 1920x930 och 1440x900. Mål även vid 1280x800 och 1024x768 (se 6.6 om det inte går) | allt i en ren följd: varje element når bild helt innan föregående lämnar; mål: allt i samma bildruta vid 390x844 (räknat 670 px); 320x568 i följd |
| **6** | rubrik och siffror i Young Serif | `#pris-title` och `.price-row .value` (bara siffrorna) i `--f-serif`; rubrik 96 / 86 px, ≤ 2 rader, 0 delade ord | rubrik 40 px, ≤ 3 rader |
| **6** | F-017 i liggaren | siffrorna **64 / 49 px**; `Pris vid förfrågan` = `.value--text`, **hälften av siffran, aldrig under 17 px** (32 / 24,5 px), samma familj; baslinjen för `Pris vid förfrågan` = baslinjen för radens etikett, samma som siffrornas (Δ ≤ 1 px, mätt med en nollhög inline-markör per cell) | siffra 32 px, text 17 px |
| **6** | kontakten som handling | `.close-mailto` i sidans handlingsform (samma som `.card-cta`): Geist 700, **~21 / 19 px**, understruken 2 px, träffyta ≥ 44 px höjd, inte en rubrik | 17 px |
| **6** | copy | ingressen = val A ordagrant, `.price-short` och kickern borta; 20 till 22 px, ≤ 52ch | 17 px |
| **7** | småtext | `microtext_scan.py --url … --price-ledger` vid 1440 och 390: **4 fynd kvar, alla på kortets baksida** (`Digital byrå`, `Design`, `Utveckling`, `System`, se inventeringen), 0 annars; och varje rad i inventeringen nedan = 0 träffar i DOM | samma |
| **7** | tillgängligt namn | båda `iframe[title]` och Hyperboreas `img[alt]` oförändrade; `a11y_scan` 0 violations | samma |
| **8** | Hōrais bokning ryms | i `?preview=case-horai-06` och i sajten öppnad direkt i ramens egen bredd: varje textrad i `#reservations` (`Range`-rektangel) ≤ spaltens högerkant och ≤ `documentElement.clientWidth`, vid ramsbredderna för 1920 (1230), 1440 (915), 1280 (813), 1024 (649), 768 (485), 390 (390), 320 (320) | samma |
| **8** | vertikalt | vid 1920/1440/1280 står "Top floor · press the brass bell. *No sign on the street.*" helt ovanför ramens underkant − 16 px i `case-horai-06` | (sektionen staplas, bara vågrätt mål) |
| **8** | sajten själv | `sites/horai.html` direkt vid 1920x1080, 1440x900 och 390x844: bokningssektionen läst som bild, ser rätt ut; allt utanför `#reservations` pixelidentiskt med R16 | samma |
| **8** | 390-överflödet | redovisas, inte löst: `scrollWidth` 675 kvarstår (andra sektioner, se nuläget) | – |

## Beslut

**B1 · Ett nytt snitt, Young Serif, för två uppgifter: kapitlets namn och erbjudandet.**
Prov renderat denna session (`a060/spec.png`): Newsreader, Instrument Serif, Gloock, Young Serif,
Fraunces, Bricolage Grotesque, Libre Caslon Display, Hedvig Letters Serif, Bodoni Moda, med Cardo
som jämförelse, på papperet och på mörk grund, med "Exempelcase", "Alla har rätt till bra design." och
"26 900 kr · 38 900 kr".
- **Hör hemma i sidans system.** Young Serif är en tung, mjuk, upprätt old style i en vikt. Dess
  svärta ligger nära Geist 700, så den står i samma gråvärde som tesens och processens rubriker,
  som en varm motpart till den kalla grotesken; Public Sans bär fortfarande all text under den.
- **I ramarnas sällskap.** Calyx är Cardo, en lätt kalligrafisk old style (kursiven), Hōrai är
  Cinzel, en inskriptionsantikva i versaler, med Vollkorn. Young Serif är ingen av dem: tung, gemen,
  rak. "Exempelcase" läses därför som Alunix egen röst, inte som ett tredje citat ur en sajt.
- **Roligare i priset.** Kulterminaler och studsiga siffror: `26 900` får en form man minns, och
  tre siffror under varandra blir en rytm i stället för en tabell (F-017: kompakta figurer).
- **Inte AI-standarden.** Den generiska serifen bredvid Geist är tunn och högkontrastig
  (Instrument Serif, Fraunces, Playfair), alltså anti-patterns look #1 (krämfärgat papper + tunn
  serif). Young Serif avviker på vikt och form, och sidan har ingen terrakotta.
- **Ett snitt, inte två.** Samma familj för 1 och 6 håller sidan på fyra familjer med hårda roller:
  Geist (namn, tes, steg, handlingar), Public Sans (text), Geist Mono (kortets register), Young Serif
  (det sidan säger direkt till kunden: kapitlets namn, löftet och priset). Alternativet, Gloock bara
  i priset, står som Q1.
- Laddas via Google Fonts `<link>` med `display=swap` (som sajterna), token `--f-serif` i `:root`
  (gate 48). Kostnad, namngiven: sidans första externa förfrågan (huvudkommentaren "sidan hämtar
  ingenting över nätet" skrivs om) och en fjärde typsnittsfil mot performance.md:s tre; perf_probe
  mäter den. Ingen preload (snittet syns inte i folden).

**B2 · Ramkanten: bort med bården, och låt iframen täcka sin ruta med en pixel till godo.**
Prövat denna session i 16 konfigurationer (7 bredder vid DPR 1, plus DPR 0,9 / 1,1 / 1,25 / 1,5) med
magentaprovet: *bara bården bort* rensar DPR 1 men lämnar en halvtäckt rad vid 1,25 och 1,5 (Calyx
underkant vid 1536x744@1,25 (253,63,252), överkant vid 1280x620@1,5 (252,123,247)); *bården bort +
iframe `inset:-1px`, 2 px större* ger **0 avvikande pixlar i alla 16**. `.frame-wrap` har redan
`overflow:clip`, så pixeln till godo klipps vid rutans egen kant och det iframen ritar når alltid
ända ut. Affischbilden står kvar som laddningsgrund, den syns aldrig längre vid kanten. Kostnaden: en
pixel av sajten döljs på var sida, ingenting läsbart. **Ingen JS-snäppning** behövs; den hålls i
reserv (Boundaries) om magentaprovet hittar en kant vid DPR 1,75 eller 2.

**B3 · Calyx → Hōrai: grunden byts inne i Calyx-pinnen, sedan ett svart andrum, sedan Hōrai.**
Ramen får enligt PRODUCT.md aldrig transformeras, tonas eller klippas, så "en ram som lämnar" är
scrollens egen: ramen står still medan allt runt den byter material, och lämnar sedan uppåt.
- Lager 1: textspalten lämnar genom sin överkant (samma springa som stegen), **0,87 till 0,91**.
  Text först, så ingen text någonsin står på en grund halvvägs mellan papper och svart (kontrast).
- Lager 2: stagens grund papper → `--c-black`, **0,91 till 0,99**. Calyx-sajten står då som en ljus
  sida på svart, samma svart som Hōrai-stagen.
- Sedan släpper pinnen: den svarta Calyx-stagen med ramen glider upp, 18svh svart `.case-gap`,
  och Hōrai-stagen kommer in med ramen till vänster och namnet till höger. Ingen ny kant: tre svarta
  ytor i rad, ΔE 0.
- Stegen får sina fönster inom 0 till 0,86 (`--t:.86`), spannet 5,5 → 6,4 så att varje steg har
  samma scroll som i dag. Allt läser `--sc-ps` (F-014) utan `transition`: båda riktningarna per
  konstruktion. Ingen `prefers-reduced-motion` (F-011).
- Varför inte en egen övergångssektion: den skulle inte kunna läsa Calyx `--sc-ps` (syskon ärver
  inte), och en rå svart kant mellan papper och svart är just det Anton vill bort ifrån.

**B4 · Hōrai → pris: fotot framkallas ur det svarta, rubriken skärps.**
Samma bild som tidigare men scrubbad: `.price` behåller sin statiska toning (svart 0 → 10svh →
genomskinlig 45svh, som ger ΔE 0 mot Hōrai), och får en slöja `::after` i `--c-black` som bara
ändrar `opacity` (kompositorn, ingen ommålning av fotot eller `.ground`, se F-013 och kommentaren vid
`.ground`). Rubriken skärps ur oskärpa (`blur` + `opacity` + `translateY`, inte `letter-spacing`,
som bryter om raderna mitt i bytet, R10). Två lager, ett ögonblick: som ett foto i framkallningsbadet.
`#pris` får `min-height:100svh` med innehållet i nederkant, så `--sc-ps` beter sig lika vid alla
bredder (ps 0,5 när sektionens topp når viewportens topp, ~0,59 vid dokumentets slut vid 1920x930).

**B5 · Prissektionen på en skärm, genom att ta bort, inte genom att krympa.**
Kickern, `.price-short` och den gamla ingressen (fem meningar) går; val A (28 ord) står i stället.
Liggarens etiketter får bredare mått (en rad vid ≥ 1280), siffrorna radhöjd 1, kontakten blir en
handling i 21 px i stället för en 48 px-rubrik, och footerns utfyllnad krymper. Räknat vid 1920x930:
rubrik 192 + 24 + ingress ~132 + 46 + liggare ~280 + footer ~173 = **~847 px**, dvs. rubriken står
≥ 83 px under överkanten vid dokumentets slut. 1440x900: ~779 px. 390x844: ~670 px.
Rubriken och ingressen ligger kvar i vänsterspalten på scrimmen (ingen tvåspaltslayout: fotot till
höger är skrivbordets bild och scrimmen tonar ut vid 92 %).

**B6 · Småtexten: allt som bara beskriver sidan tas bort, inget flyttas till en annan liten plats.**
Kortets baksida är ett föremål (ett visitkort med sitt eget register och låst copy) och står kvar;
se inventeringen och Q3.

**B7 · Hōrais bokning: mindre text, och en enda gap-klass under md.**
Textstorlekarna i sektionen sänks (tabellen i steg 8). Det räcker vid ramsbredderna ≥ 768 (1920,
1440, 1280). Under 768 (Hōrai-ramen vid 1024, 768, 390, 320 är 649/485/390/320 bred) lägger sajtens
12-kolumnsgrid `gap-x-12` ut sektionen på 675 px oavsett textstorlek, så texten klipps ändå. Därför
`gap-x-12` → `gap-x-0 md:gap-x-12` på sektionens **egen** grid (rad 307): enklaste möjliga,
inne i den upplåsta sektionen, och ≥ md oförändrat. Detta är den enda ändringen som inte är en
textstorlek; om lead hellre vill hålla sig till storlekar strikt står det som Q4.

## Inventering av småtext (punkt 7)

**A. Tas bort (11 poster, 12 element)**

| # | Selektor (rad i R16) | Text | Anmärkning |
|---|---|---|---|
| 1 | `.thesis-caption .cap-line` (1639) | Exempelsida: Hyperborea, konferens i Lund | bildtext; namnet finns i `img[alt]` |
| 2 | `.process-chapter > .kicker-sans` (1668) | Så går det till | kicker |
| 3 | `.process-lead` (1675) | Sju steg, samma ordning i varje projekt, så att ni alltid vet var vi är. | liten grå förklarande rad (Antons beslut i copy-filen) |
| 4 | `#case > .kicker-sans` (1901) | Exempelcase | kicker; ordet blir rubriken |
| 5 | `#case-calyx .kicker-sans` (1912) | Exempelcase | kicker ovanför case-namnet |
| 6 | `#case-calyx .case-rail` (1934 till 1936) | Fotot bär rubriken · En serif för allt man läser · … | sidomeny med steglista |
| 7 | `#case-calyx figcaption.frame-cap` (1943) | Exempelsida: Calyx, florist i Stockholm | bildtext; namnet står i `iframe[title]` |
| 8 | `.case-bridge` (1950 till 1953) | Nästa sida säljer en kväll. + stycket | punkt 4 (inte småtext, men tas bort samtidigt) |
| 9 | `#case-horai figcaption.frame-cap` (1964) | Exempelsida: Hōrai, Asian fusion-koncept | bildtext; `iframe[title]` |
| 10 | `#case-horai .kicker-sans` (1967) | Exempelcase | kicker |
| 11 | `#case-horai .case-rail` (1984 till 1986) | Namnet står en gång · Stycket tänds i er takt · … | sidomeny |
| 12 | `#pris > .kicker-sans` (2000) | Från exempel till er sida | kicker |
| 13 | `.price-short` (2006) | Första steget är ett samtal om vad ni gör. | liten förklarande rad (ersätts inte) |

(Bryggan, rad 8, räknas under punkt 4; inventeringen av småtext är alltså **12 element**, rad 1 till
7 och 9 till 13.)

**B. Tas bort, listas separat för Anton: processens marginalnoter (7)**

| Steg | `.process-note` (rad) | Text |
|---|---|---|
| 01 | 1692 | Ett tomt ark. Inget ritas innan vi vet vad sidan ska säga. |
| 02 | 1701 | 320, 768 och 1440. Varje sida verifieras vid alla tre. |
| 03 | 1710 | 16:9, öppningen där ert innehåll ska sitta. Proportionen bestäms innan bilden finns. |
| 04 | 1719 | 96 px, radavståndet i liggaren. All rytm räknas ur det. |
| 05 | 1728 | Strukturen får sitt material. Ritningen blir er sida. |
| 06 | 1737 | Bläcket står kvar som ram. Ritningen och sidan är samma sak. |
| 07 | 1746 | Revisionsfältet fylls. En bokstav, aldrig ett datum. |

**C. Står kvar, med skäl (lead bekräftar, Q3)**

| Element | Varför det inte är F-016 |
|---|---|
| Kortets baksida: `.card-kicker` "Digital byrå", `.card-services` "Design · Utveckling · System" (10,5 px mono) | Tryck på ett föremål, visitkortets eget register; `Design`/`Utveckling`/`System` är låst copy. Skriptet flaggar dem (4 fynd), domen är att de identifierar. |
| `.topline` "ALUNIX" + `kontakt@alunix.se` (12 px) | Navigation och en handling (mailto), inte en beskrivning |
| `.price-row .label` (17 px) | Paketens innehåll, låst copy, säljer; inte om sidan |
| SVG-måttetiketter i processarket (`.measure`, `.callout`) | Ritningens egna mått, uttryckligen undantagna av Anton |
| Allt inne i Calyx- och Hōrai-ramarna | Sajternas egen typografi, uttryckligen undantagen |
| `.sr-only` i heron | Osynlig, tillgänglighet |

## Steps

Radnummer är R16:s, verifierade med Grep denna session. Kirurgiska `Edit`. Varje nytt block börjar
med `PLAN 060 N.` och en INTE-rad (in-situ negation). Gamla kommentarer som beskriver borttagen kod
förkortas till en mening om varför den är borta.

### 7 · Småtexten (först)

7.1 Markup: ta bort rad 1639 (`figcaption.thesis-caption`), 1668 (`p.kicker-sans` i
`.process-chapter`), 1675 (`p.process-lead`), 1692/1701/1710/1719/1728/1737/1746 (sju
`p.process-note`), 1901, 1912, 1967, 2000 (fyra `p.kicker-sans`), 1934 till 1936 och 1984 till 1986
(två `div.case-rail`), 1943 och 1964 (två `figcaption.frame-cap`), 2006 (`p.price-short`).
7.2 CSS som bara stylade dem: `.kicker-sans` (587), `.thesis-caption`/`.cap-line` (649 till 652,
683, 700), `.frame-cap` (796 till 798), `.price > .kicker-sans` (824), `.price-short` (837 till 838),
`.case-rail` (973 till 977, 1038), `.case-text > .kicker-sans` (1001), `.process-lead` (1083 till
1085, och ur selektorlistan på 1384), `.process-chapter > .kicker-sans` (1089), `.process-note`
(1138, 1148 till 1149). Kommentaren om monobudgeten (583 till 586) skrivs om: Geist Mono används
nu bara på kortets baksida (`.card-kicker` 516, `.card-services` 521); `.ledger-num`s mono (872)
skrivs över av `#process .ledger-num` (1140, Geist 700) och syns inte som mono.
7.3 Copy-filens beslut efter copy-gaten: Calyx steg 1 `p` (1928) och Hōrai steg 1 `p` (1977)
enligt tabellen, ordagrant.
7.4 Processen: `.step-band`s grid tappar sin rad 2-cell (`.process-note`). Kör `?preview=process-01`
till `-07` vid 1440, 768 och 390 och kontrollera att varje läge landar på sitt `--eN` (±0,002) och
att `--band-h` mäts om (measureAct gör det vid load/resize). Läs P07 och P10 som bild.

### 3 · Ramkanten

3.1 CSS 926 till 928: `.case-wrap{flex:1;min-height:0;}` (ingen `border`), och ta bort
`.case--calyx .case-wrap{border-right:0}` och `.case--horai .case-wrap{border-left:0}`. Mobilen
999 till 1000: `.case-wrap,…{border:0;}` utan `border-bottom`.
3.2 CSS 755 till 756, `.frame-wrap iframe`: `inset:-1px;width:calc(100% + 2px);height:calc(100% + 2px);`
(i stället för `inset:0;width:100%;height:100%`). Kommentar: B2 i två meningar, magentaprovet som
belägg. `overflow:clip` på `.frame-wrap` (723) står kvar och är förutsättningen.
3.3 `measureCase` läser `w.innerHeight` (nu 2 px högre); inget annat ändras. Kontrollera `case-horai-03`
(citatet) och `case-calyx-03` (figuren) vid 390 och 375 som bild.
3.4 Magentaprovet (Verification B3) vid alla konfigurationer. Hittar det en rad vid DPR 1,75 eller 2:
Boundaries.

### 1 · Exempelcase

1.1 `<head>`, efter rad 83:

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Young+Serif&display=swap">
```

   Kommentaren 74 till 81 och huvudkommentarens rad 11 skrivs om (en extern stilmall, varför).
1.2 `:root`, efter `--font` (160): `--f-serif:'Young Serif',Georgia,serif;` med kommentar: kapitlets
   namn, prisrubriken och prissiffrorna, aldrig brödtext (B1). `--f-quote-calyx/horai` orörda.
1.3 Markup 1902 till 1903: `h2#case-title` text → `Exempelcase`, `.cases-lead` → copy-filens final.
1.4 CSS 882 till 884 (`.cases-title`): `font-family:var(--f-serif);font-weight:400;
   font-size:clamp(2.5rem,9vw,8.5rem);line-height:1;letter-spacing:-.01em;max-width:none;
   overflow-wrap:normal;white-space:nowrap;` Gradientkanten (`--edge`, 885 till 887) står kvar.
   Byggaren mäter ordets bredd med `Range` vid 320 till 1920 och sänker `9vw`/taket om det inte har
   ≥ 8 px marginal; värdet skrivs i NOTES.

### 2 · Case-namnen

2.1 Ingenting ändras i `.case-name` (946 till 950). Kontroll: computed style identisk med R16.

### 4 · Calyx → Hōrai

4.1 Markup 1948 till 1953: ta bort bryggan (kommentar + `section.case-bridge`), sätt i stället
   `<div class="case-gap" aria-hidden="true"></div>` med en kommentar (B3, INTE en tredje sektion
   med text). Rad 1909: `data-sc-span="5.5"` → `"6.4"`.
4.2 CSS: ta bort `.case-bridge`, `.bridge-title`, `.bridge-p` (890 till 896). Nytt block efter 971:

```css
/* PLAN 060 4. Calyx -> Hōrai utan brygga (B3): stegen ryms i 0..--t,
   sedan lämnar textspalten (lager 1) och grunden blir svart (lager 2)
   medan ramen står still. INTE en tredje sektion, INTE en hård kant
   papper/svart, ramen transformeras/tonas/klipps aldrig. */
.case--calyx{--t:.86;} .case--horai{--t:1;}
.case-gap{height:clamp(96px,18svh,200px);background:var(--c-black);}
.js .case--calyx{
  --x1:clamp(0,calc((var(--sc-ps,0) - .87) / .04),1);
  --x2:clamp(0,calc((var(--sc-ps,0) - .91) / .08),1);}
.js .case--calyx .case-text{
  clip-path:inset(calc(var(--x1) * 100%) 0 0 0);
  transform:translateY(calc(var(--x1) * -32px));}
.js .case--calyx .case-stage{
  background:color-mix(in oklab,var(--bg),var(--c-black) calc(var(--x2) * 100%));}
```

4.3 Stegformlerna läser en skalad progress: i `.js .cs` (965 till 970) och mobilens `.js .case-line`
   (1027 till 1031), lägg `--q:min(1, var(--sc-ps,0) / var(--t,1));` och byt `var(--sc-ps,0)` mot
   `var(--q)` i `--in`/`--out`. Hōrai (`--t:1`) blir oförändrad per konstruktion.
4.4 JS: `CASES[0]` (Calyx, 2361) får `t:.86`, `CASES[1]` `t:1`. `latchTick` (2197):
   `caseY(C, Math.min(1, cAct.cur / (C.t || 1)))`. Preview (2677 till 2685): `aimPin` siktar på
   aktens progress `previewCaseP(ccN,5) * 0.86`, medan `caseY` får det oskalade
   `previewCaseP(ccN,5)` (stegets egen progress, samma sak som latchTick räknar fram ur
   `cur / t`). Hōrai oförändrad (`t:1`).
4.5 JS 2641 till 2644: ta bort läget `bridge`. Nya lägen, se `?preview=`-tabellen.
4.6 Mät: scroll per steg mot R16 (±3 %), `case-calyx-01` till `-05` landar som i R16, och
   `.case-wrap`/`iframe` har `transform:none`, `opacity:1`, `clip-path:none` i varje bildruta av
   hjulsekvensen genom 0,80 till 1,0.

### 6 · Prissektionen

6.1 Markup 1991 till 2022: kvar blir `h2#pris-title.statement`, `p.price-ingress` (val A,
   ordagrant) och `.price-ledger`. Tredje radens värde: `<span class="value value--text">Pris vid
   förfrågan</span>`. Kommentaren 1991 till 1998 skrivs om till B5 i två meningar.
6.2 CSS, ersätter 818 till 857 där det står:

```css
/* PLAN 060 6 (F-017). Rubrik och siffror i Young Serif; display bara för
   siffror, text i samma kolumn halva siffran, baslinjelinjerad; kontakten
   är en handling. INTE text i displaystorlek, INTE en kontakt som rubrik. */
.price{position:relative;isolation:isolate;color:var(--invert-ink);
  min-height:100svh;display:flex;flex-direction:column;justify-content:flex-end;
  padding:clamp(120px,18svh,200px) var(--rail-x) 0;
  background:linear-gradient(180deg,var(--c-black) 0,var(--c-black) 10svh,transparent 45svh);}
.price .statement{font-family:var(--f-serif);font-weight:400;
  font-size:clamp(2.5rem,6vw,6rem);line-height:1;letter-spacing:-.01em;
  max-width:14ch;text-wrap:balance;}
.price-ingress{font-size:clamp(1.0625rem,.9rem + .4vw,1.375rem);line-height:1.45;
  color:rgba(253,251,244,.84);max-width:52ch;margin-top:clamp(16px,2.4svh,24px);}
.price-ledger{margin-top:clamp(32px,5svh,56px);max-width:min(100%,1040px);position:relative;}
.price-row{display:flex;flex-wrap:wrap;justify-content:space-between;
  align-items:baseline;gap:6px 24px;padding:.8rem 0 0;position:relative;}
.price-row::after{width:100%;margin-top:.8rem;}
.price-row .label{font-size:1.0625rem;font-weight:600;color:var(--invert-ink);max-width:60ch;}
.price-row .value{font-family:var(--f-serif);font-weight:400;
  --fig:clamp(2rem,3.4vw,4rem);font-size:var(--fig);line-height:1;
  letter-spacing:0;color:var(--invert-ink);white-space:nowrap;}
.price-row .value--text{font-size:max(1.0625rem,calc(var(--fig) * .5));}
```

   Liggarens hårlinjer (`::before`/`::after`, `--d`): nya fönster `--d` .26/.30/.34/.38 med `/ .12`
   (i stället för `/ 0.14`); byggaren kontrollerar att alla fyra har `scaleX` 1 vid dokumentets slut
   vid alla sju bredderna (sektionen slutar nu på ps ~0,59 vid 1920x930).
   Mediet 1544 till 1546 (`.price-row` i kolumn ≤ 768) står kvar; där sitter texten under etiketten
   och baslinjekravet gäller inte.
6.3 Footern, 1524 till 1538: `.close` padding `clamp(24px,4svh,40px) var(--rail-x) clamp(32px,6svh,64px)`,
   `gap:clamp(16px,2.4svh,24px)`. `.close-mailto`: samma form som `.card-cta` (534 till 539):
   `font-family:var(--f-display);font-weight:700;font-size:clamp(1.0625rem,.9rem + .35vw,1.375rem);
   line-height:1.2;text-decoration:underline;text-underline-offset:5px;text-decoration-thickness:2px;`
   `border-bottom` och `padding-bottom` bort, `min-height:44px` kvar, hover/active: tjocklek 3px
   (samma som kortet). Kommentarerna 1517 till 1523 skrivs om (footern delar skärm med priset nu).
6.4 JS: läget `pris-bro` (2651 till 2663) siktar på dokumentets slut i stället (`scrollTo(0,
   document.documentElement.scrollHeight)`), och heter även `pris`.
6.5 Mät Target 6 vid 1920x930, 1440x900, 1280x800, 1024x768, 768x1024, 390x844, 320x568 vid
   dokumentets slut, i skärmbild och med rektanglar. Baslinjekontroll: en `<span style="display:
   inline-block;height:0;width:0">` i början av `.label` och av `.value` (injicerad av mätskriptet,
   inte i sidan); deras `top` ska vara lika (Δ ≤ 1 px) i alla tre raderna.
6.6 Ryms det inte vid 1280x800 eller 1024x768: först `.price` padding-top (0 kostnad, den ligger
   ovanför), sedan `.price-ledger` margin-top och `.close` padding i ett `@media (max-height:820px)`.
   Aldrig rubrikens eller siffrornas storlek. 1920x930 och 1440x900 är golvet.

### 5 · Hōrai → pris

5.1 CSS, efter 6.2:

```css
/* PLAN 060 5. Fotot framkallas ur det svarta (lager 1, bara opacity)
   och rubriken skärps (lager 2), båda på #pris --sc-ps (F-014), båda
   riktningarna. INTE en hård kant Hōrai/foto, INTE letter-spacing (R10),
   INTE en ommålning av .ground. */
.price::after{content:"";position:absolute;inset:0;z-index:-1;pointer-events:none;
  background:var(--c-black);
  opacity:calc(1 - clamp(0,calc((var(--sc-ps,0) - .05) / .35),1));}
.js #pris-title{--k:clamp(0,calc((var(--sc-ps,0) - .18) / .22),1);
  filter:blur(calc((1 - var(--k)) * 10px));opacity:var(--k);
  transform:translateY(calc((1 - var(--k)) * .25em));}
```

   Staplingsordning: `::before` (scrimmen, z −1) och `::after` (slöjan, z −1) i `.price`s egen
   stapelkontext; slöjan efter i källordningen, alltså ovanpå scrimmen och under texten. Vid ps < .05
   är sektionen helt svart ovanpå fotot: skarven mot Hōrai ΔE 0 (mät).
5.2 Mät med `motion_probe.py` på `#pris`, hjul `20:120` ned och upp från sektionens egen början (inte
   från `?preview=pris`, som startar efter scrubben: R12/R13:s artefakt). Blur på en 96 px rubrik:
   frame p95 ≤ 20 ms vid cpu 1; faller det, sänk 10 px → 6 px, ta aldrig bort lagret.

### 8 · Hōrais bokningssektion (`sites/horai.html`, bara rad 306 till 339)

| Rad | Element | R16 | R17 |
|---|---|---|---|
| 307 | sektionens grid | `gap-x-12` | `gap-x-0 md:gap-x-12` (B7) |
| 310 | `h2` RESERVATIONS / OPEN MONDAYS | `text-[clamp(3.2rem,6.4vw,6.8rem)]` | `text-[clamp(1.5rem,8.5vw,2.4rem)] md:text-[clamp(2.2rem,5.2vw,6.2rem)]` |
| 314 | stycket | `text-[clamp(1.3rem,1.8vw,1.6rem)]` | `text-[clamp(1.05rem,1.6vw,1.45rem)]` |
| 321 | `book.horai.se` | `text-[clamp(2.4rem,3.6vw,3.2rem)]` | `text-[clamp(1.2rem,7.5vw,2.2rem)] md:text-[clamp(1.2rem,2.6vw,2.6rem)]` |
| 322 | "Or write us…" | `text-[clamp(1.15rem,1.45vw,1.35rem)]` | `text-[clamp(1rem,1.35vw,1.25rem)]` |
| 328 | HORNSGATAN 58 / 118 49 STOCKHOLM | `text-[clamp(1.4rem,2vw,1.8rem)]` | `text-[clamp(.9rem,1.9vw,1.6rem)]` |
| 331 | "Top floor…" | `text-[clamp(1.1rem,1.45vw,1.3rem)]` | `text-[clamp(1rem,1.35vw,1.25rem)]` |

Räknat (sajtens rot är 19 px; Cinzel-versalerna mätta: RESERVATIONS 8,06 em, book.horai.se 8,25 em,
HORNSGATAN 58 11,2 em): vid 915 bred ram blir `book.horai.se` 23,8 px = 196 px i en 257 px spalt; vid
485 (mobillayout, spalt 405) 36 px = 300 px; vid 320 (spalt 240) 24 px = 198 px; RESERVATIONS vid
1230 64 px = 516 px i en 636 px spalt. Byggaren mäter varje rad med `Range` vid de sju ramsbredderna
och justerar bara `vw`-talet i den rad som inte ryms.
8.1 Inga andra klasser, ingen annan sektion, ingen `<style>`-ändring. Diff av `sites/horai.html` ska
   bara visa rad 307 till 331.
8.2 Tailwind-CDN:en (rad 10) genererar godtyckliga klasser vid körning: kontrollera att varje ny
   klass fått en regel (`getComputedStyle(el).fontSize` = räknat värde).
8.3 Ankaret `['#reservations', 0]` (index.html 2386) mäts om av `measureCase`; läs
   `case-horai-06` som bild vid 1920, 1440, 1280, 1024, 390.
8.4 Sajten direkt: skärmbild av `#reservations` vid 1920x1080, 1440x900, 390x844, och pixeldiff av
   hela sidan utanför sektionen mot R16 (0 % utanför sektionens rektangel).

### `?preview=`-hookar

| Läge | Mål | Visar |
|---|---|---|
| `cases` | oförändrat (`#case` `scrollIntoView` center) | Exempelcase i serif + texten, ensamt på papper |
| `case-calyx-01` … `-05` | `aimPin(#case-calyx, previewCaseP(N,5) * .86)` | steg N, utan kicker och rail |
| **`case-seam-text`** (ny) | `aimPin(#case-calyx, .89)` | textspalten halvvägs ut, grunden fortfarande papper |
| **`case-seam-ground`** (ny) | `aimPin(#case-calyx, .95)` | grunden halvvägs papper → svart, Calyx-ramen orörd |
| **`case-seam`** (ny) | `scrollY = .case-gap mitt − innerHeight / 2` | Calyx-stagen på väg upp, det svarta andrummet, Hōrai på väg in: avståndet ram → ram |
| `case-horai-01` … `-06` | oförändrade | `-06`: bokningssektionen hel i ramen |
| **`pris-in`** (ny) | `scrollY = #pris.top − innerHeight + .22 × (#pris.height + innerHeight)` | slöjan halvvägs, rubriken i oskärpa |
| `pris` / `pris-bro` | dokumentets slut | hela prissektionen och kontakten i en bild |
| `pris-bro-skarv` | oförändrat | skarven Hōrai/pris, slöjan full |
| `bridge` | **tas bort** | – |

Alla nya lägen sätter `__scFreezeMotion` (det gör redan varje `?preview=`) och väntar in aktens
`--sc-ps` ± 0,002 med `aimPin`s settle-slinga där de siktar på en akt.

## Device-tabell

| Bredd | 1 · Exempelcase | 3 · Ramkant | 4 · Calyx → Hōrai | 5 + 6 · Pris | 7 · Småtext | 8 · Hōrais bokning (ram) |
|---|---|---|---|---|---|---|
| **1920x930** | 136 px, ord ~870 px; text 20 px | 0 px bård, magenta 0 fel | gap 167 px, ram → ram ~223 px | rubrik 96 px 2 rader, siffror 64, text 32, kontakt 21 px; allt i en bild, rubrik ≥ 48 px från toppen (räknat ~83) | 0 utom kortet | ram 1230: RESERVATIONS 64 px, book 32 px, allt synligt ovanför ramens underkant |
| **1440x900** | ~130 px | samma | gap 162 | 86 / 49 / 24,5 / 19 px; en bild (räknat ~779 av 900) | samma | ram 915: book 23,8 px i 257 px spalt |
| **1280x800** | 115 px | samma | gap 144 | 77 / 43,5 / 21,8 / 18,6; en bild, annars 6.6 | samma | ram 813: book ~22,8 px |
| **1024x768** | 92 px | samma | gap 138 | 61 / 35 / 17,4 / 17,5; en bild, annars 6.6 | samma | ram 649 (sajtens mobillayout, `gap-x-0`): allt inom spalten |
| **768x1024** | 69 px | samma | gap 184 | 46 / 32 / 17 / 17; rader staplade | samma | ram 485, mobillayout |
| **390x844** | 40 px, ord ~256 i 358 | samma | gap 152 | 40 / 32 / 17 / 17; mål: en bild (räknat ~670) | samma | ram 390: RESERVATIONS 33 px, book 29 px, i 310 px spalt |
| **320x568** | 40 px, ord ~256 i 288 | samma | gap 102 | 40 / 32 / 17 / 17; ren följd | samma | ram 320: allt i 240 px spalt |
| **DPR 0,9 / 1,1 / 1,25 / 1,5 / 1,75 / 2** | | **magenta 0 fel** vid 1536x744@1,25, 1745x845@1,1, 1280x620@1,5, 2133x1033@0,9, 1097x531@1,75, 960x465@2 | | | | |

Noll horisontell scroll 320 till 1920 (elementrektanglar, gate 34). 200 % zoom på 1440 = 720 css-px =
mobilraden.

## Repo conventions

- Motorn och `sites/*` orörda utom `sites/horai.html` rad 306 till 339; ramen transformeras, tonas
  och klipps aldrig; ingen `prefers-reduced-motion` (F-011); allt som rör sig läser `--sc-ps` (F-014).
  Gate 75: noll tankstreck i synlig text. Radie 0, inga skuggor. Gate 48: Young Serif bara via
  `--f-serif`. Gate 38a: ingen kursiv i nya rubriker (Calyx-namnets Geist-kursiv är Antons uttryckliga
  beslut, punkt 2).
- Accenten `#1e5e9c` exakt två förekomster. Inline-hex utanför `:root` inte fler än R16 (17).
- F-016: inga nya kickers, bildtexter, rail eller små förklarande rader, någonstans.

## Boundaries (STOPPA och skriv i NOTES)

- En sträng behövs som inte står i `COPY-V3d-r17-final.md`.
- En låst sträng (PRODUCT.md, 12 synliga rader) skulle behöva ändras.
- Magentaprovet hittar en avvikande pixel efter 3.1 + 3.2 (då: skriv konfigurationen; lead väljer
  JS-snäppning av `.case-wrap` till enhetspixlar i `measureCase`).
- Prissektionen ryms inte vid 1920x930 eller 1440x900 efter 6.2, 6.3 och 6.6.
- `sites/horai.html` behöver ändras utanför `#reservations`, eller en textrad ryms inte efter att
  bara `vw`-talen justerats.
- Någon `?preview=process-0N` landar inte på sitt `--eN` efter 7.1, eller Calyx-stegen tar mer än
  ±3 % annan scroll än R16 efter 4.3.
- Google Fonts-stilmallen laddar inte (nätverk): bygg klart med Georgia-fallbacken, skriv det.

## Verification

**A. Synligt, det som avgör.** `PARITET.md` rader P03, P14, P15, P17, P19, P20, P21, P22, P23 och P16:
par-bilder vid 1440 och 390 i `shots/r17/par/`, plus enskilda skärmbilder vid **1920x930** för P14,
P17-1, P19-1, P19-6, P21, P22 och P23, lästa som bilder, "håller nivån" eller lagade i samma runda.
Lead läser själv P14, P21 och P22 vid 1920 och 390, och ramkanterna zoomade 4× vid 1920 och vid
1536x744@1,25, innan rundan räknas klar.

**B. Mätt.**
1. Exempelcase: text, familj, `fonts.check`, ordets bredd mot spalten vid sju bredder.
2. Namnen: computed style mot R16 (spara R16:s värden först).
3. **Magentaprovet** (skriptet finns i scratchpad `a060/mag.py`, kopieras till `shots/r17/`):
   injicera `html,body{background:#ff00ff!important}body *{visibility:hidden!important}` i båda
   ramarnas dokument i `case-calyx-01`/`case-horai-01`, ta skärmbild, klassificera 30 punkter per kant
   på den första helt inre enhetspixeln (magenta) och den första yttre (stagens grund). **Kör först mot
   R16**: provet ska hitta bården vid DPR 1 och sprickan vid 1,25/1,5, annars mäter det fel. Mål:
   0 avvikelser i alla konfigurationer i device-tabellen.
4. Calyx → Hōrai: `--x1`/`--x2` mot `--sc-ps` i ett hjulsvep 20 px ned och upp; ΔE vid båda
   skarvarna i `case-seam`; scroll per steg mot R16; ramens transform/opacity/clip-path per bildruta;
   `motion_probe` på `#case-calyx` från ps 0,8.
5. Pris: rektanglarna i Target 6 vid dokumentets slut, sju bredder; baslinjekontrollen; hårlinjernas
   `scaleX` 1 vid slutet; `contrast_over_media.py --url …?preview=pris` (alla strängar ≥ 4,5:1,
   rubriken ≥ 3:1, ljusaste 5 %); slöjan och rubriken mot ps; `motion_probe` på `#pris` från ps 0.
6. Småtext: `microtext_scan.py --url … --price-ledger` (4 fynd, alla på kortet); grep av varje sträng
   i inventeringen A och B: 0 träffar i `index.html`.
7. Hōrai: `Range`-mätningen vid sju ramsbredder i ramen och direkt; diff av `sites/horai.html`
   begränsad till rad 307 till 331; `scrollWidth` vid 390 (675, redovisat).
8. Låst copy: **12/12** synliga, plus de tre tillgängliga namnen ordagrant.

**C. Grinden.** `scroll_verify` 1440 och 390 (inga nya `blankBands`; `.case-gap` 18svh och prisets
fotoband < 60 % vh); `motion_probe` enligt B4/B5; `perf_probe` (en extern stilmall + en woff2, LCP
oförändrad ±10 %, CLS ≤ 0,02 när Young Serif byter in); `a11y_scan` + `reflow` vid 390 och 1440;
`tab_walk` (kontakten fortfarande ett tabbstopp med synlig ring); grep `prefers-reduced-motion` 0;
tankstreck i synlig text 0; noll horisontell scroll 320 till 1920.

**Done when:** varje Target-rad har ett uppmätt värde som når målet, magentaprovet är 0 i alla
konfigurationer, prissektionen står i en bild vid 1920x930 och 1440x900, inventeringens poster är 0
träffar, par-bilderna håller nivån, och grinden är ren eller varje avvikelse namngiven.

## Frågor till Anton (bygget stoppar inte; antagandet gäller tills svar)

| # | Fråga | Antagande |
|---|---|---|
| Q1 | Ett serifsnitt för både "Exempelcase" och priset (Young Serif), eller ett eget, ännu lekfullare för priset (Gloock, högkontrastig och fet)? Ett snitt håller sidan på fyra familjer. | Young Serif för båda |
| Q2 | Young Serif hämtas från Google Fonts, sidans första externa förfrågan (sajterna gör likadant). Ok, eller ska den vendras som de andra tre (en nedladdning)? | Google Fonts `<link>`, som beställt |
| Q3 | Kortets baksida ("Digital byrå" och "Design · Utveckling · System" i 10,5 px) står kvar som visitkortets eget tryck. Ok? | Står kvar |
| Q4 | Hōrais bokning ryms bara under 768 px ramsbredd (dvs. vid 1024, 768, 390, 320) om sektionens egen grid tappar sitt 48 px-mellanrum på mobil (`gap-x-0 md:gap-x-12`), en klass utöver textstorlekarna. Ok? | Ja |
| Q5 | Hōrais 390-överflöd (675 px) sitter i sajtens övriga 12-kolumnsgrids, inte i bokningen. Samma klass på de övriga sektionerna skulle lösa det, men låset gäller där. Vill du häva det? | Nej, redovisas bara |

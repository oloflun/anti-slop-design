fix

## persistence

**Pass.** Allt underlag den här granskningen vilar på finns och är läst i den här körningen.

- `tests/alunix-r8/malbilder/V3c.md` (16 rader, ordagrant) och `tests/alunix-r8/concepts-V3c.md`
  § V3c (1) till (8) plus § F-007-kontrollen, lästa som text.
- `tests/alunix-r8/runs/V3c/BRIEF.md`: § catalogue-select, Design Read, Dial, Reference lock,
  Decision ledger inkl. byggarens R1- och R2-rader, Direction contract, Persona-skisser,
  § Vad jag måste slå. `NOTES.md` § R2/R3 (tab_walk, a11y-passen 4-8, gate 97-raden, kickerbytet).
- Källan `runs/V3c/index.html` läst som kod: markup 609-800 och all CSS som bär interaktion
  (`.plate-card`, `.face`, `.plate-edge`, `.hero-sub`, `.stagger`, `.frame-wrap`, `.scrub-text`,
  `.price`, `.close`), plus sidans egen JS-loop och `scroll/scrollcraft.js` § `dwell()`.
- Skärmbilder lästa som pixlar: `review/r3/V3c-fold-1440`, `V3c-back-1440`, `V3c-fold-390`,
  `V3c-back-390`, `V3c-scroll-1/2/3/4`, `V3c-full`, `shots/r3/preview-mid`, `contact-1440`
  (femdelad filmremsa), `fold-768`, `close-375`, `paper-375`.
- Låsta referenser öppnade som pixlar den här körningen: `garden-eight`, `mattis-studio`,
  `oryzo-ai`, `squarespace`, `dope-security`, `monologue`, `planhat` (`fold.webp`), samt
  primärreferensen `tests/alunix-concepts-r5/cells/V3b-chain/shots/desktop-1440--fold.png`.
- Färskhet: `index.html` 05:47:02, alla lästa skärmbilder 05:47:40 till 05:56:04. Ingen bild
  är äldre än bygget. `sites/calyx.html` och `sites/horai.html` lästa som kod för att avgöra
  om ramarna har egen scrollhöjd (det har de: Calyx har åtta sektioner, Hōrai är 31 kB).
- Ingen URL gissad: alla sökvägar i rapporten är hrefs eller `data-src` ur källan.

## fidelity

Grunden håller. Sju skärmar i målbildens ordning, akterna kommer när målbilden säger att de
ska komma, och signaturakten gör exakt det den lovar: vid `?preview=mid` syns en hårlinje och
ingenting annat av kortet, vilket är `mattis-studio`-ribbans egen mätpunkt, och grunden syns
igenom där kortet nyss låg. Två driftposter i folden och en i avslutet är defekter, inte
avsikter, och två av sidans sju skärmar lämnar över scrollen till en annan sajt.

**Skärm för skärm mot `concepts-V3c.md` § (3).**

- **s1 (ps 0).** Topologi rätt: rubrik i affischgrad på railen, plåt 896x504 vänsteranknuten,
  logo-dock innanför hörnet, underrad under. Läsordningen rubrik, plåt, underrad håller.
  **Defekt:** underraden är högerställd mot *sidans* rail (högerkant 1267 px), inte "under
  plåten" som målbilden och § FIRST VIEWPORT punkt 5 skriver; plåtens högerkant är 982 px.
  V3b klarade kravet gratis eftersom plåten där var railbred (mätt i V3b:s egen fold). I V3c
  hamnar sidans enda rakt talande mening, den som svarar på "vad gör Alunix", på fotots
  ljusaste parti, den upplysta träväggen, medan rubriken har ett eget scrim. Fokalskala,
  z-ordning och densitet i övrigt: rätt, fyra textelement, inget femte.
- **s2 (ps ~0,42).** Signaturakten. Rörelsen är auktoriteten, rubriken står kvar som ground,
  ingen ny text tillkommer. `.plate-edge` hängd i den ledande kanten läser som tjocklek och
  inte som ett veck. Ingen drift.
- **s3 (ps 0,72 och uppåt).** Baksidan landar: `ALUNIX` ~81 px, kicker, hårlinje, raden
  DESIGN UTVECKLING SYSTEM, `Boka ett möte` understruken i accenten. Ordningen är densamma
  som liggarens 01-03, så de två listorna motsäger inte varandra; målbildens öppna fråga är
  stängd rätt. Kickerbytet `Digital byrå` till `WEBBYRÅ I SVERIGE` och den borttagna pilen är
  **avsiktliga** avvikelser med varsin rad i `NOTES.md` (copy-fyndet respektive gate 97).
  Kompositionellt sitter blocket i kortets vertikala mitt och lämnar ~190 px tom svart under
  länken; det läser som ett tryckt kort, inte som en tom platta. Godkänt.
- **s4 tes.** Blå plåt vänster, jätterubrik höger, Hyperborea bryter sin egen kant åt höger.
  Displayelementet är `VI BYGGER ERT VARUMÄRKE.` som målbilden säger. Ingen drift.
- **s5 bevis.** Calyx som ljus ram, liggaren scrubbas fram bredvid. Additiv färgscrubb i
  stället för opacitet är rätt lösning. **Kvarstående läsrisk:** i varje viloläge står radens
  senare hälft i dämpad bläckton, och för en beställare som stannar och läser ser det ut som
  två betydelserangordningar i samma mening, inte som en front som vandrar.
- **s6 pris.** Prisliggaren mörk till vänster, Hōrai mörk till höger. Kolumnvikten håller:
  spalterna slutar inom ~5 px av varandra i helsidesbilden, inget blankt band. Ingressen
  "Två av tre paket har ett pris utskrivet här" är exemplarisk förväntanssättning.
- **s7 avslut.** **Defekt mot målbilden.** § (3) skriver "Mailto-raden, ensam på skärmen.
  Ingenting annat". I bygget delar mailto-raden sista viewporten med prisblockets nedre
  halva och Hōrai-ramen (`contact-1440`, sista rutan): `.close` har bara `padding-top`
  clamp(64px,12vh,140px) = 108 px vid 900. Akten "Beslut" får aldrig sin tystnad.

**DOM-ordningen är en tredje berättelse.** `.col-left` (tes, Calyx, pris) står först i DOM,
`.col-right` (jätterubrik, liggare, Hōrai) sist, och under 900 px vänder `order:` på det.
Linjärt läst på desktop (skärmläsare, tangentbord, ingen CSS) kommer alltså **priset som post
3 av 6, före tjänsteliggaren som är post 5**: beställaren får prislappen innan hon vet vad de
tre tjänsterna är. På telefon är ordningen den omvända och riktiga. Tre olika ordningar för
samma innehåll är ett konsistensbrott, inte en responsiv finess.

**Nielsens tio, mot det byggda.**

| # | Heuristik | Dom | Nyckelfynd |
|---|---|---|---|
| 1 | Systemstatus | caution | Vändningen är ett utmärkt statussvar på handen, men aktens första ~158 px och sista ~420 px scroll (av 1980) ger en helt oförändrad skärm; `dwell(0,35)` mildrar båda men tar inte bort dem |
| 2 | Systemet och verkligheten | caution | `Boka ett möte` öppnar ett tomt mejlfönster utan ämnesrad: etiketten lovar ett möte, handlingen levererar en blank compose |
| 3 | Kontroll och frihet | **fail** | Hjul och tumme över Calyx (90dvh) och Hōrai (80dvh) scrollar den inbäddade sajten, inte sidan. Sidans enda navigationsmedel överlämnas till främmande dokument på två av sju skärmar |
| 4 | Konsistens och standard | caution | Tre olika innehållsordningar (visuell desktop, DOM, mobil) för samma sex block |
| 5 | Felförebyggande | pass | Inget formulär, inget fält, ingen destruktiv handling; "Pris vid förfrågan" sätter förväntan innan besökaren gissar |
| 6 | Igenkänning framför minne | caution | Raden som gör en okänd blomsterbutikssajt till *Alunix eget arbete* är sidans minsta text (12 px) under en 90dvh-ram |
| 7 | Flexibilitet och effektivitet | caution | Ingen navigation, ingen genväg, ingen ankarlänk; `#pris` och `#projekt` finns i DOM men inget pekar på dem. Medvetet val, men priset betalas av stress-personan |
| 8 | Estetik och minimalism | pass | Sju skärmar, ett displayelement per skärm, noll ikoner, noll kort, noll skugga, radie 0 |
| 9 | Fel: känna igen, diagnosticera, återhämta | n/a | Sidan har inga feltillstånd; enda felkällan vore en ram som inte laddar, och `background` på wrappern gör tomrummet till en avsiktlig yta |
| 10 | Hjälp och dokumentation | pass | Ingen behövs; prisingressen och bildtexterna är den enda förklaring uppgiften kräver |

**Kognitiv genomgång, uppgift för uppgift.**

*Uppgift 1, "förstå vad Alunix gör" (primär persona, 1440, mitt på dagen).*
Steg 1, landa: rätt effekt eftersträvad, ja, rubriken påstår något och kortet ligger där.
Steg 2, se handlingen: ja, den enda handlingen är att scrolla och stagens ground är synlig
från p = 0, så gate 88 löses utan cue. Steg 3, koppla handling till effekt: ja, kortet svarar
direkt och åt båda hållen. Steg 4, se framsteg: **osäkert**, de första ~158 px ger 4 px
ljuspölsvandring och ingen rotation; en beställare med ett tungt hjul hinner tvivla. Samma
fråga på slutet: ~420 px scroll efter att baksidan landat är skärmen helt stilla. Steg 5,
läsa vad byrån gör: **nej i folden**, meningen som säger det står i fotots ljusaste parti
285 px till höger om plåten. Fångas upp först på s4-s5, en akt senare än nödvändigt.

*Uppgift 2, "se bevis som går att använda".*
Steg 1: ja, en riktig sajt målas upp och är omedelbart trovärdig. Steg 2, förstå vems arbetet
är: **osäkert**, bildtexten är 12 px och ligger under ramen på det fotografiska underlaget.
Steg 3, titta närmare: **nej.** Pekaren över ramen ger scroll åt Calyx i stället för åt
sidan; besökaren skrollar och sidan står still medan en blomsterbutik rullar. Det finns ingen
skärm, inget `pointer-events:none`, ingen väg att öppna sajten för sig, och ingen indikation
om att ramen är levande eller stum. Steg 4, ta sig vidare: besökaren måste flytta pekaren ut
ur ramen, en åtgärd ingenting på skärmen berättar om. Samma sak med tumme på 390 px, där
ramen är 62-66dvh och full bredd.

*Uppgift 3, "hitta en kontaktväg".*
Steg 1: ja. Tre mailto på samma adress: toppraden (scrollar bort), kortbaksidan, avslutet.
Steg 2: ja, avslutets rad i displaygrad med understrykning läser som en länk. Steg 3, koppla
effekt: **osäkert på kortbaksidan**, `Boka ett möte` öppnar en tom compose utan ämne; för en
beställare som inte känner igen mailto-beteendet är svaret ett fönster hon inte bad om, utan
spår av vad hon skulle skriva. Steg 4, se framsteg: mejlklienten öppnas, vilket är tydligt nog.

*Edge-personan (tangentbord, Page Down i hopp).* Vändningen: **fungerar**, hela uttrycket är
en funktion av `--sc-ps`, och shimens lerp gör varje Page Down till en båge och inte till ett
klipp. Men tabbvägen: från liggaren leder nästa Tab **in i calyx.html:s hela dokument**,
därefter in i horai.html:s. Byggarens eget pass 7 noterar friktionen och kallar den "verklig
men inte blockerande"; för den här personan är det två hela främmande sajter mellan
tjänsterna och kontaktraden. Ingen väg att hoppa förbi finns.

*Stress-personan (390 px, en hand, fem minuter, höstsol).* Folden: fungerar, kortet är 4:5
och underraden ligger vänsterställd på railen, mobilen har alltså den placering desktop
saknar. Pinnen kostar ~2,5 svepcykler innan innehållet börjar, acceptabelt eftersom baksidan
betalar tillbaka med namn, tjänster och en väg in. Priserna hittas: liggaren staplar i rätt
ordning på mobil. **Bryter:** ett svep som börjar inuti Hōrai- eller Calyx-ramen rör inte
sidan alls. Det är precis den besökare som har minst tålamod för en skärm som inte svarar.

*Utan JS.* Kortet ligger kvar med framsidan upp och baksidan `inert`; besökaren får rubrik,
underrad, tes, liggare, pris och kontaktraden. Ingen återvändsgränd. Bra golv.

## ceiling

- `V3b-chain` (primärreferens, det låsta systemet självt): **slår.** V3b visar en platt plåt
  och en underrad; V3c ger samma besökare ett objekt som svarar på handen och en baksida som
  bär namn, tjänster och kontaktväg, tre saker V3b tvingade fram i separata sektioner. Det
  enda V3b gör bättre i mitt fack: dess railbreda plåt gav underraden rätt hemvist gratis.
- `garden-eight`: **står sig bredvid.** Den håller samma tystnad över vecket, men ger
  besökaren fem navdestinationer och en scroll-pil nere till höger; hon vet både var hon kan
  gå och att det finns mer. V3c vinner på renhet och förlorar på vägvisning.
- `mattis-studio`: **slår.** Kortet är fysiskt där Mattis ram är ritad, och V3c bär varken
  versionstagg, klocka eller "SLOTS FOR APR: 2 LEFT". Mattis är däremot en klick från kontakt
  från vilken scrollposition som helst; V3c:s enda alltid-nåbara kontakt scrollar bort.
- `squarespace`: **står sig bredvid.** Squarespace tar bort beslutsfriktion med mikrocopy
  ("Start for free. No credit card required.") och en Next-kontroll besökaren styr själv.
  V3c svarar med tre utskrivna priser, vilket är ärligare, men ger besökaren noll kontroller.
- `oryzo-ai`: **förlorar.** Samma grepp, ett fysiskt objekt som vrids i ett tomt rum, men
  oryzo understryker den aktiva navposten och skriver ut "SCROLL TO CONTINUE": besökaren vet
  hela tiden var i berättelsen hon står. V3c:s pinnade akt har inget motsvarande, och det är
  där mina två statusfynd sitter.
- `dope-security`: **står sig bredvid.** Accenttalet och noll skugga är V3c:s, mätbart. Dope
  ger däremot två namngivna vägar in ("Try now with Google", "Try now with Microsoft") och en
  tidsangivelse ("See how in 140s") som sätter förväntan på vad nästa handling kostar. V3c
  sätter förväntan bara på priset, aldrig på tiden.
- `monologue`: **står sig bredvid.** Hårlinjerastret är lika disciplinerat i V3c och ligger
  på `--rail-x`. Monologue ger dessutom en flikrad som låter besökaren välja vad hon vill se
  härnäst; V3c har ett enda tvingat flöde, vilket är avsiktligt och inte gratis.
- `planhat`: **slår.** Rubriken i vikt 300 ligger på grundens mörka parti och har eget scrim.
  Planhat lägger sin brödtext under samma disciplin, men gör det för *hela* textblocket. Det
  är precis den regel V3c:s underrad bryter, och därför är underradsfyndet inte kosmetiskt.

## material_fixes

- `.frame-wrap iframe` sätts `pointer-events:none` på båda ramarna: hjul och tumme över Calyx
  (90dvh) och Hōrai (80dvh) ska scrolla sidan 1:1 över 100 % av ramarnas yta, i dag 0 %.
  Ramarna förblir levande bevis att titta på, vilket är exakt vad device-tabellens "en riktig
  sajt laddar och går att titta på" begär. Gäller `--sc-p` 0,55 till 0,95.
- `.hero-sub` binds till plåtens högerkant i stället för sidans rail: högerkant 1267 till
  982 px vid 1440 (raden ärver plåtens eget spaltmått i stället för `margin-right:
  var(--rail-x)` plus `padding-right: var(--rail-x)`). Målbilden och § FIRST VIEWPORT punkt 5
  skriver "under plåten"; 285 px drift, och den lägger sidans enda rakt talande mening på
  fotots ljusaste parti. Gäller vid `--sc-ps` 0.
- DOM-ordningen rättas: `.col-right` skrivs först i markupen och `order:` flyttas till
  `@media (min-width:901px)`. Målvärde: tjänsteliggaren före prisblocket i DOM-ordning vid
  varje bredd, i dag pris = post 3 av 6 och liggare = post 5. En berättelseordning, inte tre.
- `tabindex="-1"` på båda ramelementen: tangentbordsvägen från liggaren till kontaktraden ska
  vara högst 3 Tab-tryck, i dag två kompletta främmande dokument. Vill a11y-granskaren hellre
  ha ramarna nåbara gäller i stället en visuellt dold länk "Hoppa förbi exempelsidan" före
  varje `figure.frame-fig`, med samma målvärde 3 Tab till kontakt.
- `.close` får `min-height:62vh` (558 px vid 900) med mailto-raden vertikalt centrerad, i dag
  bara `padding-top` 108 px. Målbilden § (3) s7: "Mailto-raden, ensam på skärmen. Ingenting
  annat"; i dag delar den viewport med prisblocket och Hōrai. Gäller vid `--sc-p` = 1.
- Alla tre `mailto:kontakt@alunix.se` får `?subject=Förfrågan%20om%20webbplats`: 3 av 3
  länkar ska öppna ett fönster som redan vet vad ärendet är, i dag 0 av 3. Ingen synlig copy
  ändras, så copy-gaten berörs inte.
- `.frame-cap` font-size 12 till 14 px (behåll `letter-spacing:.02em` och registerrollen):
  raden som gör en okänd sajt till Alunix eget arbete får inte vara sidans minsta text under
  sidans största block. Gäller båda bildtexterna, `--sc-p` 0,55 och 0,80.
- Vilotiden i signaturakten kortas: flipfönstret `smoothstep(0.12, 0.72)` till
  `smoothstep(0.10, 0.80)`, målvärde stillastående svans högst 300 px scroll (i dag ~420 px)
  och stillastående inledning högst 120 px (i dag ~158 px), mätt vid 1440x900 med
  `dwell(0,35)` inräknad. Bygget följer målbilden ordagrant här, så ändringen kräver en egen
  rad i decision ledger mot målbildens låsta smoothstep; den är arkitektens, inte byggarens.

## keep

Vändningen själv och dess ärlighet vid 90 grader: hårlinjen, den ledande kantens tjocklek och
att grunden syns igenom där kortet nyss låg, plus prisliggarens tre sanna rader med sin
förväntanssättande ingress. Ingen av fixarna ovan får kosta en enda bildruta av det.

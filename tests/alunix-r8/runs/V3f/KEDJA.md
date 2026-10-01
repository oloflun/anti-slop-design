# V3f · skill-kedjan per runda

Endast Inspo-MCP och UI-skills-MCP. Lokala designskills anropas inte.
Byggarnas anrop mäts med `tests/alunix-r8/chaintrace.py <session>` ur
subagent-transkripten, inte ur deras egen rapport.

## Runda 0 · studie (lead, Opus)

| # | MCP | Verktyg | Argument | Utfall | Landade i |
|---|---|---|---|---|---|
| L1 | inspo | get_filters | (inget) | enum-listan, täckning per macrostruktur | giltiga argument |
| L2 | inspo | recommend | formproblem-brief (levande kundsajter som bevis, visitkortet som objekt) | pick `marquee-hero` (majoritetsröst 7), heroGuidance, spacingGuidance, `cyphr-studio` bland exemplen | cyphr → lånet; guidance → spec §3, §5 |
| L3 | inspo | search_screens | "client websites as huge full-bleed screens…", industry agency | **aspensearch-com**, area17, nbstudio, generalcondition | aspensearch blev primär |
| L4 | inspo | search_screens | "physical object as hero, sliced imagery…" | 8 irrelevanta (lexikal rankning) | inget, spillsökning |
| L5 | inspo | compare | aspensearch, cyphr, area17, generalcondition | `sameRegister:false` | en dominerande riktning, cyphr bara som rörelselån |
| L6-8 | inspo | get_screen | aspensearch, cyphr, area17 | autopsier + fullsidor lästa (1440) | aspens 2×2-kvadrant och diagonalregel → hero; cyphrs rutmönsterupplösning → dithertekniken |
| L9 | inspo | get_design_system | aspensearch-com | riktiga tokens: #0af474, #a3fbcb, #232323, #d9d9d9, radie 0, weight 450, -4 %, fluid skala 52→200 | spec §2 |
| L10 | inspo | find_reference_components | macro "Split" | hero/split-screen | läst |
| L11 | inspo | get_reference_jsx | hero/split-screen | halv typ / halv panel | heroens kvadranter |
| L12 | inspo | find_reference_components | pricing | 7 arketyper | tier-bento valdes |
| L13 | inspo | get_reference_jsx | pricing/tier-bento | ledande nivå 2×2 | spec §3.8 |
| L14 | ui-skills | list_skills | query "grid" | swiss-design, neo-industrial-design, brandkit | två förskrivna till byggaren |

Budget: 2 search_screens (tak 2), 3 get_screen, 1 compare, 1 design system, 2 JSX.
Lokalt val: Geist 500 hämtades (fontsource) som närmaste till Aspens Suisse 450.

## Runda 1 · bygge (Sonnet), mätt ur transkriptet

| Tid | Verktyg | Argument | Vad byggaren säger att det ändrade | Leadens kontroll |
|---|---|---|---|---|
| 20:00:56 | ui-skills get_skill | zeke/swiss-design | radie 0, rutnät först | stämmer i pixlar (radie 0 överallt) |
| 20:00:56 | ui-skills get_skill | elithrar/neo-industrial-design | 12→6→1-kolumners omkomposition | stämmer vid 390, men pris-bento kollapsade inte (fel 6 i R2) |
| 20:01:03 | ui-skills get_skill | emilkowalski/emil-design-eng | scrollstyrd transform/clip-path, inga keyframes | stämmer; rutmaskens opacitetsfel var eget, inte skillens |
| 20:01:03 | inspo get_design_system | aspensearch-com | bekräftade specens tokens | redundant (leaden hade redan hämtat) |
| 20:01:08 | inspo get_reference_jsx | pricing/tier-bento | `.pris-lead` 2×2 | stämmer vid 1440 |

Alla tre skills laddades **före** första CSS-raden (inom 70 s från start). Inga lokala Skill-anrop.
Byggarens rapport och transkriptet stämmer överens: 5 kedjeanrop, 115 övriga verktyg.

**Leadens pixelgranskning R1** (egna skärmbilder 1440 + 390): kompositionen bär, inget
dokument. Åtta fel: kortet svart på svart; död svart viewport i mobilheron; `Exempelcase`
skuren av bildceller; `Berätta om er verksamhet.` duplicerad (copy-diffen räknade mängd, inte
antal) och överflödar sin cell; kontaktens högerhalva död; pris-bento trasig vid 390;
bildyta 19,7 % mot golv 30 %; verify.py räknar inte förekomster.

## Runda 2 · riktade fel (Sonnet, samma byggare återupptagen)

Kedjeanrop i runda 2, ur transkriptet: **0**. Totalen står kvar på 5, och antalet övriga
verktygsanrop gick från 115 till 200. Byggaren gjorde inga nya designval. Alla åtta punkter
var kaskad- och kontextfel, t.ex. inline-`grid-column` som slog ut mobilens media query,
och `.face--back` som återanvändes utanför flippens 3D-kontext.

**Leadens pixelgranskning R2** (egna skärmbilder 1440 + 390, 14 vyer var):
- Löst: kortet läses nu som vitt objekt med hård skugga över skarven. Mobilheron har ingen
  död viewport. `Exempelcase` står på egen rad. Kontaktrubriken finns en gång och ryms.
  Pris-bento staplas vid 390. Bildytan är 30,4 % strikt vid 1440 (byggarens mätning).
- Kvar till R3: kortets framsida är ett foto i passepartout, inte ett visitkort, eftersom
  motivet är mörkt och mattkanten tjock. Kontaktens högra nedre halva är fortfarande tom
  svart. Exempelcase-bilderna på 140vh är en höjning för att nå måttet, inte en
  kompositionsidé.

## Runda 3 · rörelse (GSAP + Lenis)

Kedjan vidgas på Antons uppdrag 2026-09-24: gsap-skillsen (lokala, `~/.agents/skills/gsap-*`)
och en ny `lenis`-skill, skriven ur primärkällorna (repot, npm, Lunardis artikel,
ScrollTrigger-dokumentationen), räknas nu till tillåtna källor. Inspo och UI-skills gäller
fortfarande.

**Svar på "varför en referens":** `compare` gav `sameRegister:false`, och leaden valde
en dominerande riktning i stället för att triangulera. Cyphr-lånet försvann när byggaren tog
bort rutmasken i R1, så kompositionen vilar på Aspen ensam. Instruktionen beskriver `compare`
som ett trianguleringsverktyg, och det användes som ett filter. Det rättas här:
rörelsespecen hämtar uttryckligen från Cyphr (rutupplösning), Exoape (typ som skärs av
kanten) och Area17 (typ över stilla fotofält).

Lead (Opus), före bygget: `Read gsap-scrolltrigger/SKILL.md` (scrollerProxy behövs inte för
Lenis på window, ScrollTriggers ska skapas i sidordning, scrub och toggleActions får inte
blandas). Vendorat: gsap 3.15.0 + ScrollTrigger + SplitText, lenis 1.3.26.
Lenis-skillen: Sonnet (djup 1) delegerade till en egen Sonnet (djup 2).

**Lenis-skillen** (`~/.agents/skills/lenis/`, 301 + 90 + 190 rader, live i skill-listan direkt).
Leaden läste SKILL.md i sin helhet. Kopplingsblocket stämmer mot README. Fyra punkter är
ärligt markerade UNVERIFIED: normalizeScroll, pin, `scroll-behavior` och tangentbordsscroll.
Två fynd gick direkt in i byggordern:
`respectReducedMotion` är `true` som standard och bryter F-011, så den sätts till `false`.
`anchors` är `false` som standard och tystar ankarlänkar, så den sätts till `true`.
Lenis egen CSS sätter `pointer-events:none` på iframes under smooth-scroll, och det accepteras.

### Runda 3 · bygge (Sonnet, ny byggare), mätt ur transkriptet

| Tid (UTC) | Anrop | Leadens kontroll i pixlar |
|---|---|---|
| 22:32:08 | Skill `lenis` | kopplingen stämmer: autoRaf false, gsap.ticker, lagSmoothing(0), inga CDN-anrop, `scroll-behavior` saknas (0 träffar) |
| 22:32:09 | Skill `gsap-core` | – |
| 22:32:11 | Skill `gsap-scrolltrigger` | pin på desktop, ingen pin på mobil via matchMedia: stämmer |
| 22:32:12 | Skill `gsap-timeline` | introt är en tidslinje: diagonal clip-path, raderna reser sig, kortet faller (bildrutor 60/150/250/400 ms) |
| 22:32:13 | Skill `gsap-plugins` | SplitText används, men radmasken skär av underhäng och bryter ett ord (fel 1 i R4) |
| 22:32:15 | Skill `gsap-performance` | bara transform/opacity/clip-path. Byggaren mätte median 16,7 ms och p95 33,3 ms (headless, räknas som indikation) |
| 22:32:18 | ui-skills `emil-design-eng` | easing och varaktigheter |

Sex skills, i föreskriven ordning, inom 3 minuter från start och före första kodraden. Inga
Inspo-anrop i R3; referenserna kom via specen.

**Leadens granskning R3** (hjulscroll 1440 och 390, 25 + 26 bildrutor, 0 konsolfel):
- Bär: introt, rastrets upplösning ruta för ruta, prisräknaren, kortvändningen i pinnen,
  tesraden som glider förbi kanten.
- Fel till R4: tesraden bryter *inuti* ordet (`intryc|ket`) och masken skär av underhäng.
  Footerns `ALUNIX` når aldrig slutläget på mobil. Processens dimmade text ligger på ca 3,9:1,
  under AA. Kontaktens döda kvadrant finns kvar. Slutlägestest vid maxscroll saknas.

### Runda 4 · riktade fel (samma R3-byggare)

Kedjeanrop i R4, ur transkriptet: **0** nya. Totalen står kvar på 7, och antalet övriga
verktygsanrop gick från 82 till 153. Byggaren använde regler den redan hade laddat: SplitText
`lines,words,chars` med radmask, och `end:'bottom bottom'`.

**Leadens granskning R4** (hjulscroll 1440 och 390):
- Löst: tesraden bryter bara mellan ord och underhängen syns. Processens dimmade rubriker
  ligger på 6,49:1 och brödtexten på 11,18:1. Kontaktkortet är centrerat. Maxscrolltestet finns.
- Byggarens diagnos av footern var **fel**. Den kallade glappet i `AL UNIX` för kerning. I
  själva verket klipptes nedre femtedelen av bokstäverna bort av `translateY(18%)` i en
  `overflow:hidden`-cell (leadens egen spec, "skuret av nederkanten"), så ordet lästes som
  `AI UNIX`. Leaden rättade det själv: translateY togs bort, och teckenmasken togs bort
  eftersom den kapade X:ets överhäng. Verifierat vid 390, 1440 och 1920: hela ordet syns, 0 px
  överflöd, 0 konsolfel.
- verify.py efter leadens rättning: 0 px överflöd på alla fyra bredder. Copy-diffen flaggar
  samma två kända dubbletter från specen (`ALUNIX` i topplist + footer, `kontakt@alunix.se` i
  topplist + CTA). Inget nytt.
- Skärmfångstfelet vid 390 under introt kom från miljön (boardfliken laddade parallellt).
  Isolerat: 0,08 till 0,57 s per bild, långa tasks högst 183 ms.

## Runda 5 · läsbarhet, casevalet, kontakten (ny Sonnet-byggare)

Antons dom efter R4, 2026-09-24: *"nästan perfekt på en gång och redan bättre och mer unikt än
v3d"*. Ändringarna han bad om står i `RUNDA5-SPEC.md` (A–D). Kontakten tillkom mitt i
turen: "ingen tydlig tanke där". Leadens grepp: kortet lämnas över, heron speglad som bokstöd.

| Tid (UTC) | Anrop | Leadens kontroll i pixlar |
|---|---|---|
| 00:42:18 | Skill `lenis` | oförändrad koppling; `window.__lenis` används i alla hopp |
| 00:42:21 | Skill `gsap-scrolltrigger` | tesens pin: raderna står helt i 68–140 vh (byggarens mätning), bekräftat i bildrutorna |
| 00:42:26 | Skill `gsap-core` | – |
| 00:42:26 | Skill `gsap-utils` | `quickTo` för kortets lutning mot pekaren |
| 00:42:26 | Skill `gsap-plugins` | `Exempelcase` reser sig ur mask (yPercent), inget klipp i sidled |
| 00:42:34 | ui-skills `emil-design-eng` | hover 1,00→1,04 i väljaren, lugn och inte studsig |

Sex kedjeanrop, alla inom 16 s från första läsningen och före koden. Inga Inspo-anrop, eftersom
formen redan var låst.

**Leadens granskning R5** (1440: 32 bildrutor, 390: 20 bildrutor, 0 konsolfel):
- Bär: väljaren är skarp och utzoomad. Showcasen scrollar Calyx genom alla fem ankare med
  riktig scroll, och byggaren mätte 0 px fel mot ankarna. Tesraden står stilla och läsbar.
- Fel till R6: showcasens rader klipper text vid fast cellhöjd. Kommande rader visas som tomma
  grå celler, vilket läses som ofärdigt; ersätts av en scrollstyrd liggare med rubrikindex.
  Iframen fyller inte sin cell. Kontaktrubriken går utanför ÖV och täcks av kortet. Kortets
  framsida är tom vit. Ett dött band ligger under mintcellen. På mobil täcker kortet texten
  mitt i vändningen.

### Runda 6 · riktade fel (samma R5-byggare)

| Tid (UTC) | Anrop | Leadens kontroll |
|---|---|---|
| 03:13:31 | ui-skills `emil-design-eng` (omläst) | liggaren i showcasen: aktiv rad expanderar via `grid-template-rows` 0fr→1fr, avbrytbar, och det syns som mjuk utfällning i bildrutorna |

Ett kedjeanrop, en omläsning inför höjdanimationen. Inga nya skills.

**Leadens granskning R6** (1440: 32 bildrutor, 390: 20 bildrutor, plus interaktionstest):
- Bär: showcasen är en scrollstyrd liggare utan klippt text och utan tomma celler, och iframen
  fyller sin cell. Klick på Hōrai i väljaren låser scrollen till showcasen, byter panel, och
  sajtens inre scroll rör sig (1763 px efter tre hjulsteg). Hover zoomar och dimmar grannen.
  Kontaktkortets framsida visar foto och logga. Kortet vänder sig självt vid progress 0,7 och
  vänds sedan fram och tillbaka med klick, med rätt `inert` på den dolda sidan. Kortet täcker
  ingen text vid 1440, och på mobil ligger det i egen mintcell.
- Leaden rättade själv: kommande rader i liggaren stod på opacitet 0,35, uppmätt 2,0–3,0:1.
  Höjt till 0,6, uppmätt 3,72–7,37:1 (stor text, AA 3:1).
- verify.py efter leadens rättning: 0 px överflöd på fyra bredder. Copy-diffen visar samma två
  kända dubbletter från specen.
- verify_motion.py kraschade i leadens omkörning ("Page crashed" efter tidsgräns). Isolerat:
  sex parallella sidor gick utan krasch. 30 casebyten gav heap 10,0 MB efter GC vid 0, 10, 20
  och 30 byten, och 31 ScrollTriggers hela vägen. Ingen läcka. Kraschen kommer från sviten,
  som öppnar 12+ sidor med levande iframes i en webbläsare. Sviten bör stänga varje sida och
  köra en ny webbläsare per kontroll.

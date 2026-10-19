# Anton — vision och feedback

Det här är riktningen: det Anton betonar brett eller systematiskt om vad sidorna ska vara och
hur de ska kännas. Inte enskilda ändringar (de bor i `design-catalogue/FEEDBACK.md`, en dom per
post, och i respektive runds BRIEF). När Anton säger något som gäller *alla* sidor, *alla*
byggen eller *hur vi arbetar*, skrivs det hit samma session, med datum och hans ord.

Läses i `design/SKILL.md` Step 1b tillsammans med `TASTE.md` och `FEEDBACK.md`, innan första
designbeslutet. En post = en riktning. Ta aldrig bort; en riktning som ändras får en ny post
som pekar på den gamla.

Format: **datum · rubrik** — Antons ord (citat) — vad det betyder i praktiken — var det är
infört (fil/regel) eller "bara här".

---

## 1. Resan — sidan är en tur, inte en stapel sektioner

**2026-10-03 · Era-resan är nivån.** *"Använd detta för att bryta ned och återskapa
era-residence.com, själva resan på sidan, inte den exakta layouten eller utseendet, men det är
en sån typ av visuell resa jag vill skapa åt användarna på de sidor vi producerar."*
→ Varje persuade/experience-sida byggs som en resa med en kamera: en dörr in (overturen lämnar
över till heron med något som består), akter som rör sig in i nästa med en materiell orsak,
en passage på en annan axel, ett material som korsar kapitlen, ett slut som svarar på öppningen.
De åtta egenskaperna står i `design/references/scroll/journeys/era-residence.md` § 3; receptet
på husets verktyg i § 4. Era ligger överst i `design-catalogue/ranking.txt`.
→ Infört: journeys/era-residence.md, showcase-floor.md § 1, ranking.txt (#1).

**2026-10-02 · Showcasen är golvet, inte taket.** *"Gå igenom dessa med dina egna ögon och
inspektera noggrant de olika UI- och scroll-animationerna … som golv för nivån på vad vi
tillåter."* (gsap.com/showcase, lenis.dev/showcase, 646 sajter)
→ Innan första raden rörelsekod: två `motion_floor: 2`-poster öppna bredvid bygget; under golvet
skeppas inte. Sju regler i `design/references/scroll/showcase-floor.md` § 2.
→ Infört: showcase-floor.md, `design-catalogue/entries/*/motion/`, `browse.html`.

**2026-10-02 · Verktygen används på riktigt.** *"Vi använder inte de faktiska programmatiska
shell-verktygen som är installerade. Jag vill att du bygger in användandet av dessa i det
faktiska workflowet."*
→ GSAP 3.15 + Lenis 1.3 länkas från den globala installationen (`link_motion.py`, hook
`motion_toolchain`), importeras bara från projektets `gsap.js`/`smooth-scroll.js`; varje plugin
har en läst referens i `~/.claude/skills/gsap-plugins/references/`. Aldrig `npm install gsap`.
→ Infört: toolchain.md, design-intent-hooken, gsap-*-skillsen.

## 2. Unikhet — ingen sida får vara den andra lik

**2026-10-03 · Olika stil- och formspråk varje gång.** *"… med olika stil- och formspråk i
övrigt, ingen sida får vara den andra lik, det är därför viktigt att vi också tar inspiration
av andra sidor."*
→ Resan är gemensam, allt annat varieras: tråd-form, dörr, kamera, material, passage,
reveal-grammatik, vilopunkt, slut (variationsluckorna i journeys/era-residence.md § 5).
Fingerprint-grinden (`feel-and-fingerprint.md`) mäter det efteråt; valet görs före.
→ Infört: journeys/era-residence.md § 5; feel-and-fingerprint.md (befintlig).

**2026-09-xx · En referens räcker inte som riktning** (FEEDBACK F-024). *"… den baseras enbart
på en referens istället för att ta inspiration från flera."*
→ Låset anger en dominerande referens och minst två lån (komposition, typ, rörelse) med vad som
lånas. `compare` triangulerar, väljer inte bort.
→ Infört: HANDOFF-V3f § 2/§ 6; ska in i inspo-mcp.md.

## 3. Copy — säg något nytt, låt som en byrå

**2026-10-03 · Berätta tänket, inte det självklara.** *"Fokusera mer på tänket bakom layout och
design och varför man valde att göra på det sättet istället för att bara säga att 'fotona står
parvis, det ena lite högre än andra', vilket även skriker AI, för att det säger något som är
självklart till användaren, låt den veta något nytt."*
→ En showcase-text beskriver *beslutet och dess skäl* (vad valdes bort, vad kostade det, vad det
gör för besökaren), aldrig det ögat redan ser. Testet: stryk meningen — tappar läsaren en insikt
eller bara en beskrivning av bilden bredvid?
→ Infört: Alunix V3g R9 (2026-10-03), alla 11 showcase-ingresser omskrivna, andra stycket borttaget,
tre copy-pass körda; hör ihop med F-016, F-018, F-023 och `copy-gate.md`.

**2026-10-03 · Inga namn på platser eller personer i exempelsajterna.** *"Var även noga med att
inte nämna namn på platser eller personer för dessa exempelsidor (Stockholm är okej)."*
→ Calyx/Hōrai/Hyperborea och deras texter i Alunix: inga gatunamn, hotellnamn, personnamn.
Stockholm får stå. Gäller bildtexter, löpnummer-apparat och copy.
→ Infört: `design/SKILL.md` § Copy is worldbuilding, `house-physics.md` (Structural), kontrollen
`microtext_scan.py --names` (gatunamn, stadsdelar, städer utom Stockholm, "Hotel X", postnummer,
signaturer, svenska efternamn, "by Förnamn Efternamn"; 39 träffar på de gamla sajterna, 0 nu).

**2026-09-19 · Liten beskrivande AI-text är förbjuden** (F-016) och **2026-09-20 · sidan får
aldrig berätta vad den strax ska göra** (F-018). *"All sån liten 'beskrivande' stiltypisk
AI-text är härmed helt förbjuden."*
→ Infört: anti-patterns.md § Descriptive microtext, gate 99, `microtext_scan.py`, copy-gate.md.

**2026-09-25 · Copyn ska låta som en byrå** (F-023): två stycken, situationen och valet med
orsaken först, sedan bortvalet och en detalj som syns i ramen; inga värdeord; tre pass
(copywriting, copy-editing, humanizer-svenska).

## 4. Komposition — var saker står

**2026-10-03 · Text något ovanför mitten.** *"Tänk på att generellt sett alltid lägga text lite
ovanför mitten för att undvika att det känns som att den ska 'ramla ned genom golvet', som jag
fått höra av en grafisk designer."*
→ Centrerade textblock och rubriker i en vy sätts med optisk mitt: tyngdpunkten 4–8 % över den
geometriska mitten (en vanlig tumregel är att dela den tomma ytan 45/55 ovan/under). Gäller
hero-rubriker, statements i pinnade akter, kort med text, tomma vyer.
→ Infört: `house-physics.md` (Structural, "Text sits a little above the middle"), mätt i Alunix R9:
tessekvensen .477 → .437.

**2026-10-03 · Rubrik och ingress får inte sitta ihop; ett block får inte hamna i källaren.**
(Alunix: "Alla har rätt till bra design" nästan mot texten under; visitkortsrutan långt under
prispaketen.)
→ Avståndet mellan display-rubrik och text under är minst en rubrik-x-höjd; ett efterföljande
block får inte lämna mer än ~1 vh tom yta mellan sig och föregående utan att det är en avsedd
paus. Mäts i pixelgranskningen.
→ Infört: `house-physics.md` (Structural, descender-regeln, `calc(rubrikstorlek * .5)`); Alunix R9:
`.5` (en x-höjd; `.32` räckte inte, mätt R9), kontaktkortet flyttat till sömmen i högra kolumnen och kommer nu in samtidigt som rubriken.

**2026-09-04 · En auktoritet per sida** (TASTE.md § 1, F-003): typen, fotot, ytan, produkten
eller rörelsen bär — aldrig två samtidigt.

**2026-09-25 · Varje sektion har en tanke** (F-026) och **dekorativa streck är ofärdig kod**
(F-022): tom yta är ett kompositionsproblem, löses med innehåll eller flytt, aldrig ornament.

## 5. Rörelse — alltid, mjukt, i läsbart tempo

**2026-09-07 · Rörelsen spelas alltid** (F-011). *"ALL animation ska fungera och visas oavsett
webbläsare och systeminställningar."* → Ingen `prefers-reduced-motion`-gren någonstans.

**2026-09-25 · Tempot är husets, mjukheten offras aldrig för farten** (F-020). *"Tvinga sakta
ned scrollen … var extra noga med att se till att den är mjuk och jämn hela vägen."*
→ `lerp .075`, `wheelMultiplier .6`; en pin vars innehåll ska ses spänner ≥ 200 vh; verifieras
med `section_probe.py`.

**2026-09-25 · Rubriken står still och hel** (F-025): minst 40 vh fullt synlig, oklippt, stilla.
**2026-09-25 · Godkända effekter skyddas** (F-021): en sektion som blir sämre av en ändring
någon annanstans blockerar rundan.

**2026-10-03 · Övergångar ska vara koreograferade, inte klipp.** (Alunix: "en till likadan
sekvens efter 'Det första intrycket …' som går över till 'Vi hjälper er synas på rätt sätt'.")
→ Bärande påståenden i följd får samma mekanism (sekvensen upprepas som ett mönster), och
övergången mellan dem är en rörelse, inte ett byte av sektion. Hör ihop med floor-regel 2.
→ Infört: Alunix R9 (tessekvensen, A sjunker ur raderna medan B reser sig i samma maskar);
house-physics har maskregeln som förhindrar fragment.

**2026-10-19 · Ytor kommer in på en fjäder, agenttext skrivs fram, tal räknas i bild, foton
står hela** (F-030–F-039, Snajps startsida i tre varv). *"de ska inte tonas, de ska röra på
sig mjukt … glida in stoppa och studsa tillbaka lite, men väldigt subtilt, tänk apple"* →
`spring(0.66, 0.95)`, en ruta i taget, texten efter landningen; 0,75/0,75 var för subtilt
("gör studsseffekten tydligare"). *"effekten att texten skrivs live, för alla
omgenereringar/knappval också"* och *"hero-texten skrivs ut på samma sätt som rutan, fast
långsammare och mer effektfullt, med betoning på sover"* → agenttext och rubrik skrivs med
markör, rubriken med paus före det betonade ordet. *"det måste ske naturligt vid scroll och
när de är helt i bild, det får inte gå för snabbt"* → räknare startar först helt i bild,
2,6 s. *"bilderna laddas hela, nu ser det ut som att de renderas"* → ingen avtäckning på
foton. *"skiljer sig från de konstruerade rutorna"* → produktytor är konstruerade, aldrig
skärmdumpar. Skills som bär beställning, fall och godkänt läge: `spring-arrival`,
`live-text-reveal`, `count-up-in-view`, `hero-on-photo`, `photo-stands-whole`,
`showcase-surfaces`, `showcase-copy-scope`, `motion-verification-preview`.

## 6. Arbetssätt — hur vi tar oss dit

**2026-10-03 · Planera, låt Anton godkänna, bygg sedan.** *"Skapa en plan för allt detta som
jag får godkänna innan du fortsätter … var noga med att inte sätta igång direkt."*
→ Ändringar i en levande sida (Alunix-boarden) presenteras som plan med per-punkt-lösning och
verifiering; bygget startar efter ett ja. Bakgrundsjobb (referensinsamling) löper under tiden.

**2026-10-02/03 · Leaden läser allt själv.** *"Gå igenom dessa med dina egna ögon."* /
*"Använd agenter för att hämta texterna, men gå igenom och skriv dem själv."*
→ Agenter hämtar och mäter; bedömning av bilder, referenser och dokumentation gör leaden. Står
också i `~/.claude/CLAUDE.md` § Delegering.

**2026-10-03 · Referenserna ska gå att ranka och bläddra.** *"Skapa ett sätt att ranka
referenserna i katalogen … se till att göra den enkelt navigerbar med att byta emellan
referenser och kunna klicka sig in på originalsidan."*
→ `design-catalogue/ranking.txt` (Antons ordning överst, sedan motion_floor), `index.py` skriver
`rank`, `scripts/catalogue/browse.py` → `design-catalogue/browse.html` (←/→, `o` öppnar
originalet, `/` filtrerar).

**2026-10-03 · Håll maskinen lean.** *"Håll allt lean och stäng när något är klart, bevaka så att
samma sak inte händer igen och blockerar annat."*
→ Varje capture-sajt i egen process med hård tidsgräns, minnesgolv 4 GB ledigt commit innan
nästa sajt startar, PID-låst "en webbläsare i taget". (`motion_capture.py`, 2026-10-03.)

## 7. Öppet — riktningar som nämnts men ännu inte formulerats som regel

- (Tomt efter Alunix R9, 2026-10-03.)

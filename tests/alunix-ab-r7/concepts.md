# Alunix r7 — målbild v2 för K1 Skymning och K2 Affischen (2026-09-06)

Skriven av Claude efter Antons dom på r6-boarden (`design-catalogue/FEEDBACK.md` F-001 till
F-009) och efter egen läsning av `design-catalogue/TASTE.md`, `references/scroll/*`,
`house-physics.md` och r6-cellernas kod och skärmbilder. Varje koncept har gått igenom
målbildsgrinden (`skill-orchestration.md § 12`); grinden står ifylld under varje koncept.

Gemensamt för båda: Alunix fakta och ordagrann copy enligt `PROMPT.md`; bara vår kedja;
byggaren är en Sonnet-agent i rundor; fotopaket och (för K1) rörelsematerialet levereras
färdigt i cellens `assets/`; ingen egen server, inga Unsplash-anrop.

---

## K1 Skymning v2

**Auktoritet:** fotot. **I set-piece-akten:** rörelsen (TASTE § 4.8, preciseringen). Allt
annat viker: typen ljus (vikt 300, serif) och luftig i vattnets mörka band, en enda
kromatisk färg som gör en sak (understrykningen under `visitkort`), inga knappar, ingen
platta bakom text.

**Idé.** Ett foto av Stockholm i blå timmen bär första skärmen. Scrollen är en kamera:
en riktig, förrenderad dolly-push-in (Higgsfield/Kling, 10 s) från kajen mot ett tänt
fönster i Nationalmuseum, scrubbad ruta för ruta av hjulet. När fönstret fyller skärmen är
det Hōrais egen sida, live. Sedan hårt klipp till vitt, tre bevisrader, en liggare, och natt.

**Första skärmen (i vila).** Fullbredd: videosekvensens första ruta (samma bild som r6:s
skymningsfoto, Rafael Peier/Unsplash). Rubriken `Er hemsida är nutidens visitkort` i ljus
serif nere till vänster i vattnet, underraden ordagrann, raden `Calyx · Hōrai · Hyperborea`
som text. Logga (vit SVG) uppe till vänster, `kontakt@alunix.se` som typsatt länk uppe till
höger. **Fönstret är mörkt i vila** (F-002): ingen ruta, ingen tumnagel, inget som avslöjar
slutläget. En svag drift i bilden (≤2 % skala över 10 s) som fasas ut när scrollen börjar.

**Signaturrörelsen: kameran åker in i fönstret, och fönstret är Hōrai.** Motorns
`scrub`-device på en pinnad hero (`data-sc-act="scrub" data-sc-span="2.6"`,
`canvas[data-sc-sequence]` med bildsekvensen i `assets/push/`, båda riktningarna, mjukt
lerpad). Lager, i ordning:
1. Sekvensen (kameran från kajen till bågfönstret).
2. Rubriken som tonar och blurrar (0 → 14 px) under sekvensens första 30 % utan att flytta sig;
   sajtnamnsraden ligger kvar längst ned till 80 %.
3. **Hōrai i fönsteröppningen, aldrig utanpå fasaden (FEEDBACK F-010).** Från den ruta där
   bågfönstret är stort nog att bära det (spårdata i `assets/push/window-track.json`: en
   polygon/bågform per ruta) maskas Hōrai (skärmbilden `demo-horai.webp`, senare den riktiga
   ramen) in i öppningens form med `clip-path`/SVG-mask som följer spåret ruta för ruta, med
   glaset kvar ovanpå: fönstrets egna reflex och karm ligger som ett halvgenomskinligt lager
   (`mix-blend-mode: screen`/`multiply` av rutan själv) så att Hōrai läses *bakom glas*. Innan
   dess är öppningen bara varmt ljus. Ingen platt rektangel över fotot, inte en pixel.
4. Sista rutan (fönstret fyller nästan ramen): en fortsatt inzoomning i CSS (samma
   scrubbvärde) för rutan + masken tills öppningen fyller viewporten; glaslagret tonar bort
   sist. Då byts skärmbilden mot den riktiga `iframe`:n (`/sites/horai.html`, samma origin,
   otransformerad, aldrig tonad efter det) utan synlig skarv, och den hålls pinnad ~60 vh med
   raden `Exempelsida: Hōrai, Asian fusion-koncept` i toppbaren.
5. **Utgången ur Hōrai är en egen rörelse, inte ett klipp (F-010).** När pinningen släpper
   krymper ramen (scrubbat, båda riktningarna) från helskärm till exakt platsen och storleken
   för skärmbildsplaten i bevisraden `Utveckling / Hōrai` i akt 4, medan den vita grunden
   sveper in underifrån (`clip-path: inset`) och rubriken `VI BYGGER ERT VARUMÄRKE.` reser
   sig radvis ovanför. Fönstret blev en sida, sidan blir ett bevis. Det som krymper är en
   skärmbild av ramen (ramen själv transformeras aldrig; den byts mot skärmbilden i samma
   ruta som rörelsen börjar). `?preview=window` tvingar fram fönstret-med-Hōrai,
   `?preview=horai` ramen, `?preview=exit` mitten av utgången.

**Akter (känsla → vad på skärmen gör det; device per akt, aldrig samma två i rad).**
1. Stillhet → första rutan, rubriken, sajtnamnen. *ground (ingen device), drift.*
2. Drag → scrubben; rubrik tonar/blurrar; raden stannar. *scrub.*
3. Avslöjande → Hōrai live, pinnad, copy korsar ramen (raden i toppbaren). *pin.*
4. Klarhet → utgången: ramen krymper till sin plate medan vitt sveper in; `VI BYGGER ERT
   VARUMÄRKE.` radvis. *bespoke scrub + reveal (inset) + kinetic (lines).*
   Tre bevisrader, påstående bredvid riktig skärmbild, bildsidan växlar: Design/Calyx,
   Utveckling/Hōrai, System/Hyperborea; skärmbilden glider in en gång från sin sida.
   *reveal (left/right).*
5. Räkning → paketen som typsatt liggare, pris höger i displaygrad; hårlinjerna dras i takt
   med scrollen (bespoke på `--sc-p`). `Alla har rätt till bra design.` som rubrik. *flow +
   bespoke.*
6. Landning → grunden driftar till natt (`data-sc-drift`), nattfotot (r6:s `night.webp`,
   Julian Terenzio/Unsplash) öppnar sig från horisonten (`clip-path`), `kontakt@alunix.se`
   i stor grad, adressraden. Stilla; inget tonar bort. *reveal (iris/inset) + drift.*
   Toppbaren: transparent över foto, papper med hårlinje över vitt, ljus igen över natt.

**Reduced motion (F-001).** Samma sekvens utan resa, som egna sektioner i ordning: (1)
första rutan med rubriken, (2) sista rutan (fönstret fyller ramen) med bildtext
`Fönstret är Hōrai`, (3) Hōrai-ramen som 100 vh-sektion med bildtext, (4) resten plant.
Ingen tumnagel, inget hopp.

**Foto och material.** `assets/dusk.webp` (2200 px, Rafael Peier, Unsplash `ZP5J5M3Q9qg`),
`assets/night.webp` (Julian Terenzio, Unsplash `5UDPVmIdXUo`), `assets/push/` (Kling 3.0
via Higgsfield, ~120 rutor WebP 1600 px + `push.mp4` all-intra + `push-last.webp`),
`assets/demo-*.webp`, `assets/logo-*.svg`. Kredit i sidfot och NOTES: fotograferna och
"rörelse genererad med Higgsfield (Kling 3.0)".

**Förbjudet.** Hōrai som platt ruta ovanpå fasaden (F-010); Hōrai synlig innan fönstret är
nära; hårt klipp ut ur Hōrai; fönstret synligt i vila; logotyper eller kundnamn i bevisraden; kort med
skugga; scrim över hela bilden; mer än en scrub-akt; egen server; Unsplash-anrop.

**Fingerprint mot r6 B-K1** (grammatik · nav · hero-device · aktform · avslut · signatur):
grammatik samma (filmic one-shot) · nav samma · hero-device **video-scrub** (var CSS-skalning)
· aktform **pin + kinetic + reveal-växling** (var fade/slide) · avslut **drift till natt +
iris** (var clip-mask) · signatur **förrenderad kamera som blir live sida** (var skalat foto)
→ 4/6 skiljer. Godkänt.

**Målbildsgrinden.** (1) Auktoritet: fotot; rörelsen i akt 2–3; viker: typ (300), färg (en),
knappar (inga). (2) TASTE § 5 / troplistan: inga kort, ingen badge-rad, inget glaskort,
ingen gradient, ingen spotlight; "trusted by"-rad ersatt av tre textnamn. (3) Ett display-
element per skärm: rubriken (skärm 1), Hōrai-ramen (skärm 2), `VI BYGGER…` (skärm 3),
priserna (skärm 4), adressen (skärm 5). (4) Fingerprint 4/6, se ovan.

---

## K2 Affischen v2

**Auktoritet:** typen. Allt annat viker: fotot är en dämpad svartvit plate i spalt, färgerna
är fem (papper, bläck, vitt, två gråa linjer), inga kort, inga skuggor, inga rundningar över
2 px. **Ett displayelement per skärm** (F-003).

**Idé.** Sidan är en tryckt affisch på salviapapper. ALUNIX i en enda tung grotesk i
affischskala med krossad radhöjd (SpringSummer mäter h1 332 px på radhöjd 249 px, ≈0,75;
`extract/springsummer-dk-DESIGN.md`). Bokstävernas öppningar är fönster där exempelsajterna
syns (indoek-principen, A-K2:s bevisade teknik: SVG-mask mätt ur bläcket). Bredvid
ordmärket, i högerspalten, står **en** svartvit dokumentär plate (Antons val, F-004), aldrig
under. Två snitt med roller som aldrig korsar; r6 B-K2:s blandning är förebilden (F-005):
läs `tests/alunix-ab-r6/runs/B/K2/index.html` för valen och motiveringen.

**Första skärmen.** Toppbar som tunn rad: liten SVG-logga + ordmärke i liten grad vänster,
riktig klocka `HH:MM:SS Stockholm` som text i mitten, `kontakt@alunix.se` höger, hårlinje
under. Beskrivningsraden `Webbdesign, design och system. Allt på ett ställe.` i lässtorlek.
ALUNIX i affischskala, vänsterställt på två rader (`ALU` / `NIX`), räknarna i A, U och X
som fönster med Calyx synlig i vila; platen i högerspalten med bildtext i små versaler;
under ordmärket raden `Exempelsida: Calyx, florist i Stockholm` i små versaler.

**Signaturrörelsen: papperet skjuts och blocket andas.** Bespoke på `--sc-p` från en pinnad
hero (`data-sc-act="pin" data-sc-span="2.4"`): (1) bilden bakom masken glider vertikalt medan
bokstäverna står stilla, Calyx → Hōrai → Hyperborea i tur och ordning, raden under byts i
takt; (2) när heron släpper öppnar sig det krossade blocket: radhöjden går från 0,75 till
1,0 och raderna glider isär till `VI BYGGER` / `ERT VARUMÄRKE.` som står kvar som nästa
akts rubrik (kinetic lines på resten av rubriken). `?preview=horai` och `?preview=open`
tvingar fram lägena. Ingen rail, ingen parallax på text.

**Akter.**
1. Tyngd → affischen, klockan går, Calyx i fönstren, platen bredvid. *ground.*
2. Byte → papperet glider bakom masken; tre sajter passerar. *pin + bespoke scrub.*
3. Andning → blocket öppnar sig till nästa rubrik. *kinetic (lines).*
4. Bevis → tre uppslag under varandra: skärmbild som plate i **spalt** (inte fullbredd),
   `Exempelsida: …` som bildtext i versaler, typsatt pil som länk; svartvitt tills mitten,
   sedan färg, en gång. *reveal (wipe/desaturate).*
5. Lista → tjänsterna 01–03 som liggare med hårlinjer; siffran som **kicker** (liten,
   spärrad), inte i ordmärkesgrad. *flow.*
6. Pris → paketen i samma liggare, pris höger i displaygrad (det enda displayelementet på
   den skärmen). *flow.*
7. Avslut → `Alla har rätt till bra design.` i affischskala, vänsterställt, grunden driftar
   till bläck (`data-sc-drift`), sedan kontaktadressen som vanlig länk i lässtorlek och
   sidfoten i minsta typ. *drift.*

**Reduced motion.** Fönstren visar Calyx statiskt, blocket står öppet från start (radhöjd
1,0 med `VI BYGGER` / `ERT VARUMÄRKE.` som egen rubrik under ordmärket), uppslagen i färg,
allt i ordning.

**Foto och material.** `assets/plate-desk.webp` (svartvit dokumentär, Unsplash, hämtad av
orkestreraren, kredit i `assets/credits.json`), `assets/demo-*.webp`, `assets/logo-*.svg`.

**Förbjudet.** En sjätte färg; rundade hörn över 2 px; skuggor; en rubrikstorlek mellan
lässtorlek och affisch; centrerad text; "trusted by"; klocka som inte går; siffror i
ordmärkesgrad; skärmbilder i fullbredd; foto under ordmärket; egen server; Unsplash-anrop.

**Fingerprint mot r6 B-K2**: grammatik samma (typographic poster) · nav samma · hero-device
**maskade bokstavsfönster + plate** (var panel bakom text) · aktform **pin + kinetic + wipe**
(var reveal-rader) · avslut **drift till bläck, minsta typ sist** (var inverterat block i
display) · signatur **papper bakom mask + blocket andas** (var panelglid) → 4/6 skiljer.
Godkänt.

**Målbildsgrinden.** (1) Auktoritet: typen; viker: foto (en dämpad plate), färg (ingen
accent), siffror (kickers). (2) TASTE § 5 / troplistan: inga kort, ingen badge-rad, ingen
gradient, inga tre lika kort, ingen spotlight. (3) Ett displayelement per skärm: ordmärket
(skärm 1), `VI BYGGER…` (skärm 2), en plate i taget (skärm 3–5), priserna (skärm 6),
slutraden (skärm 7). (4) Fingerprint 4/6, se ovan.

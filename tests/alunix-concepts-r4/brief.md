# Brief r4 — tre remixer av den färdiga r3-sidan (2026-09-04, Antons beställning)

Anton om r3 (`../alunix-concepts-r3/build/index.html`): "känns fortfarande lite off och matchar inte
min vision helt, även om du gjort enligt instruktionerna." Uppdraget: **utgå från den färdiga r3-sidan**
och gör **tre remixer med tydliga skillnader i upplägg och struktur**, inspiration ur katalogen, ändra
vad ni vill men **håll er inom samma koncept**. Varje remix får **skräddarsydda scrollanimationer som
påverkar både text och bild, i olika riktningar**, med inspiration ur katalogen. Jag (orkestratorn)
läser allt med egna ögon.

## Konceptet som ska hållas (det som INTE ändras)

- Alunix som digital byrå, byråröst i vi-form. **Copyn är färdig och behålls ordagrant** ur r3:
  rubrikerna (`ALUNIX / Digital byrå`, `DET FÖRSTA INTRYCKET ÄR DIGITALT.`, `VI BYGGER ERT VARUMÄRKE.`,
  `DESIGN / UTVECKLING / SYSTEM`, `Er hemsida är nutidens visitkort`, `Webbdesign, design och system.
  Allt på ett ställe.`, `Webbdesign / Design / System`, `Alla har rätt till bra design.`) och alla
  undertexter, prisraderna (10 990 kr, 15 990 kr, pris vid förfrågan), kontakt@alunix.se. Ingen ny
  copy skrivs; ingen copy-kedja behövs. Ordning och gruppering får ändras, texten inte.
- De två världarna ur R5 (Geist, konsolkort, blått tesblock, jätterubrik, mono-kickers) och R6
  (Public Sans 300, affischordmärke, hårlinjer, off-white, inverterad prisruta) finns kvar i varje
  remix, men **hur de möts är remixens fråga**: två spalter är inte längre ett krav.
- Tre levande sajter som kantlösa, interaktiva ramar: `/tests/alunix-concepts-r3/build/tidvatten-hero.html`
  (Tidvatten med byråns rubrik i folden), `/sites/horai.html`, `/sites/calyx.html`. Absoluta sökvägar.
- Antons logga (`/tests/alunix-concepts-r3/build/assets/logo-white.svg`, inline-SVG) på en tydlig plats.
- Bilder ur `/tests/alunix-concepts-r3/build/assets/` (hero-console.webp, demo-*.webp, k4-cabin-desk.webp).
- Förbjudet (oförändrat): påhittade tal utöver priserna, kunder utöver de tre demona, Klova,
  tankstreck i synlig text, "jag", foton som "vårt kontor/team", pointer-effekter på ramarna,
  transform/opacity på en ram efter att den öppnats.

## Tre riktningar (tilldelade, se contract.md)

| M | namn | grammatik | struktur i en mening | textens riktning | bildens riktning |
|---|---|---|---|---|---|
| M1 | Kontinuerlig grund · förskjutna spalter | continuous world (en grund som aldrig klipper) | Tidvatten-ramen öppnar fullbredd; därefter två spalter där den högra börjar en halv viewport lägre och en enda mörk grund löper under allt (rre-ventures, veloura) | text stiger snabbare än sidan | bilder sjunker (negativ parallax), avslöjas genom fönster i grunden |
| M2 | Kapitel · pinnad scen | chaptered editorial + en pinnad scen (vinterspelen, sanity, not-real) | En spalt i kapitel 01–05 med folio i marginalen; ett pinnat scenrum där de tre sajterna byter plats i takt med scrollen; en roterad löptext längs högerkanten bär kapitelnamnen | text glider in från höger | bilder wipas in från vänster (clip-path), scenen byter sajt med iris |
| M3 | Galleri · sidopanering | gallery/catalog (en samling objekt) + vintergatans ordscrubb | Affischordmärket över konsolkortet som öppning; sedan en horisontell rail där de tre ramarna är objekten med etiketter; ledgerns tre rader scrubbas ord för ord; prisrutan sluter som ett sista objekt | text panorerar åt vänster | ramar/bilder panorerar åt höger (motsatt), etikett stannar |

Fingerprint (grammatik · nav · hero-device · aktform · avslut · signature move): ≤ 2/6 delade mellan
två remixer, och ≤ 2/6 mot r3-sidan (split stage · ingen nav · två heros sida vid sida · spaltflöde ·
prisruta + Calyx samtidigt · skarven som ritar sig).

## Scroll: bindande

- Läs `~/.agents/skills/design/references/scroll/{grammars,devices,feel-and-fingerprint}.md`,
  `references/motion.md`, `scripts/scroll/NOTE.md` + `template.html`. Motorn kopieras in oförändrad.
- Känslokurva per akt skriven FÖRE bygget (NOTES.md), en topp, tell-someone-mening, ≥ 4 device-familjer,
  aldrig samma två i rad, **en signature move som bara finns i den remixen** (aldrig r3:s skarv).
- Text och bild ska bevisligen röra sig i **olika riktningar** i varje remix (tabellen ovan); det ska gå
  att se på två skärmbilder tagna 300 px isär.
- Katalogposter att läsa för rörelse och struktur: `design-catalogue/entries/{vintergatan,vinterspelen,
  rre-ventures,veloura,not-real,shelby-kay,mattis-studio,creative-giants,sanity,palais,garden-eight}/entry.md`
  (avsnitten Signature move, Motion, Why it works) och `design-catalogue/TASTE.md` §1, §4.
- Reduced motion: allt synligt, ingen resa. Inget dead scroll. Konsolen utan `[scrollcraft]`-varningar.

## Verifiering (agenten kör; jag läser pixlarna)

`shoot.py` (1440 fold + full efter skriptad genomscroll, mobil 390), `scroll_verify.py`, `a11y_scan.py`,
inget horisontellt överflöde vid 1440 och 390, tre ramar laddade med titel, konsol ren, plus **fem
viewport-skärmbilder i 300 px-steg genom den akt där text och bild går åt olika håll** (`shots/motion-0..4.png`)
som bevis. Server: `python -m http.server 3091` från repo-roten.

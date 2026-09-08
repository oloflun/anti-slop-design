# Uppdrag: Alunix, koncept {{KONCEPT}}, runda 1 av flera. Referenspaket, ingen HTML än.

Du bygger, i flera rundor, en färdig scrollkoreograferad landningssida i ren HTML/CSS/JS för
Alunix, en svensk webbyrå. En orkestrerare läser din leverans mellan varje runda och skickar
nästa rundas instruktion i samma session. **I den här rundan skriver du ingen HTML, CSS eller
JS.** Leveransen är `{{UT_MAPP}}/BRIEF.md`. Referensgolvet i kedjans hook nekar dessutom varje
UI-fil tills referenserna nedan är lästa; det är avsiktligt.

Skriv bara under `{{UT_MAPP}}`. Ingen commit. Kedjans skill `design` laddas först
(`Skill(design)`), och dess steg gäller; den här prompten säger vad som är låst.

## Läs i den här ordningen, allt, innan du skriver BRIEF.md

Alla sökvägar under `~/.agents/skills/design/` om inget annat sägs. Läs filer med `Read`
(inte `cat`), bilder som bilder.

1. `SKILL.md` via `Skill(design)`: Step 0, 1, 1b, 2, 2b, 4 och avsnittet Motion.
2. `~/anti-slop-design/design-catalogue/TASTE.md`, hela.
3. `~/anti-slop-design/design-catalogue/FEEDBACK.md`, hela. Posterna F-001 till F-009 handlar
   om exakt det här bygget.
4. `references/reference-lock.md`.
5. `references/house-physics.md` (Structural och Motion).
6. `references/scroll/README.md`, `references/scroll/grammars.md`, `references/scroll/devices.md`,
   `references/scroll/feel-and-fingerprint.md`.
7. `scripts/scroll/NOTE.md` och `scripts/scroll/template.html` (motorn, kopieras aldrig ändrad).
8. Målbilden: `tests/alunix-ab-r7/concepts.md`, avsnittet för {{KONCEPT}}. Riktningen är låst
   till den; ingen bake-off, men Step 2b punkt 1–4 (grammatik, feeling curve, fingerprint,
   device-tabell) är obligatoriska.
9. De två katalogposterna målbilden bygger på, under
   `~/anti-slop-design/design-catalogue/entries/<slug>/`: `entry.md` (hela, inklusive
   § Motion), `fold.webp`, alla `slices/*.webp`, och `extract/<sajt>-DESIGN.md`.
   K1: `rogo` och `groupemontoni`. K2: `springsummer` och `indoek`.
10. Föregående runda, som lärdom, inte som mall:
    K1: `tests/alunix-ab-r6/runs/B/K1/NOTES.md` och `tests/alunix-ab-r6/runs/A/K1/NOTES.md`
    (avsnittet om fönstret som tänds vid scroll).
    K2: `tests/alunix-ab-r6/runs/A/K2/index.html` (masktekniken, mätt ur bläcket) och
    `tests/alunix-ab-r6/runs/B/K2/index.html` (typsnittsvalen och deras motivering).
11. Materialet som redan ligger i `{{UT_MAPP}}/assets/` (lista mappen; öppna `credits.json`
    och, för K1, `push/README.md`).

Låna principen, aldrig pixeln: inga färgkoder eller typsnitt kopieras rakt av från
katalogposterna. Katalogens övriga poster behöver du inte läsa, men inget förbjuder det.

## Vad BRIEF.md ska innehålla

1. **Referensdigest.** För varje fil i listan ovan (bilder inräknade): tre rader. Vad den
   säger som spelar roll här; vad du tar med; vad du avvisar och varför. Citat får vara korta.
2. **Auktoriteten** (TASTE.md § 1) med namn, och listan över vad som viker för den.
3. **Reference-lock** enligt `reference-lock.md` (dominant källa, sekundära bidrag, avvisat,
   beslutsledger).
4. **Grammatik** (en av åtta) och varför de andra sju förlorade, i en mening var.
5. **Feeling curve**: en rad per akt, känsla → vad på skärmen orsakar den; toppen namngiven;
   "tell someone"-meningen.
6. **Signaturrörelsen** i en mening, och hur den hänger i sidans motiv.
7. **Device-tabell**: akt → device → varför (≥4 familjer, aldrig samma två i rad, ≤2 scrub),
   cue-kontraktet per akt (greet på heron, hold bara på sista akten).
8. **Fingerprint** mot r6-cellen (`tests/alunix-ab-r6/runs/B/{{KONCEPT}}`) på sex dimensioner,
   utskrivet, ≥4/6 måste skilja.
9. **Reduced motion-planen**: vilka formade lägen som visas som egna sektioner och i vilken
   ordning (FEEDBACK F-001).
10. **`?preview=`-planen**: vilka lägen som kan tvingas fram för skärmbild.
11. **Typsnitt** (två, roller som aldrig korsar) och palett (namngivna tokens) med skälen.
12. **Öppna frågor** till orkestreraren, om några.

## Alunix, fakta (inget annat får hittas på)

Alunix är en webbyrå i Sverige. Sidan säljer en tjänst: webbdesign. Byrån visar vad den kan
genom tre riktiga exempelsajter som ligger i samma repo och serveras live:

- `/sites/calyx.html`: florist i Stockholm. Rad att använda: `Exempelsida: Calyx, florist i Stockholm`
- `/sites/horai.html`: restaurang, Asian fusion. Rad: `Exempelsida: Hōrai, Asian fusion-koncept`
- `/sites/hyperborea.html`: konferens i Lund. Rad: `Exempelsida: Hyperborea, konferens i Lund`

Skärmbilder av dem ligger i `{{UT_MAPP}}/assets/demo-{calyx,horai,hyperborea}.webp`. Sajterna
får visas live i `<iframe>` (samma origin när sidan serveras från repo-roten). Ramar ska vara
användbara när de är öppna: transformera eller tona aldrig själva ramelementet efter att det
visats.

Logotyp: `{{UT_MAPP}}/assets/logo-white.svg` och `logo-black.svg` (får läggas inline).

Dagens Alunix-register, som jämförelse och inte som lås: kall nästan-svart `#17181B`, blå
`#1E5E9C` bara för handling, Geist för rubrik, Inter för brödtext, JetBrains Mono för data.
Konceptet får avvika helt.

Röst: byråröst i vi-form, korta satser, fakta före adjektiv. Svenska.

### Copy som ska användas ordagrant (copy-gate: bevara, skriv inte om)

- Rubrik: `Er hemsida är nutidens visitkort`
- Underrad: `Vi skapar skräddarsydda webbplatser som hjälper er att exponera verksamheten.`
- Tesrubrik: `VI BYGGER ERT VARUMÄRKE.`
- Rad: `Webbdesign, design och system. Allt på ett ställe.`
- Tjänster, numrerade 01–03: `Design`, `Utveckling`, `System` (en kort underrad var, i
  byråröst, utan påståenden om kunder eller resultat)
- Paket, som egna rader:
  - `Standardpaket. Webbplats med CMS för egna ändringar och en första SEO-optimering.` → `26 900 kr`
  - `Paket med bokningssystem, betalning och kunddatabas.` → `38 900 kr`
  - `Helt skräddarsydda lösningar för produktkataloger, specialbyggda system med mera` → `Pris vid förfrågan`
- Prisrubrik: `Alla har rätt till bra design.`
- Kontakt: `kontakt@alunix.se` (som text och mailto; inget formulär som skickar någonstans)

### Förbjudet, bindande

- Inga påhittade tal, kunder, omdömen, citat, logotypväggar, stjärnor, "nöjda kunder".
  De tre exempelsajterna är de enda kunderna som får synas. Aldrig namnet Klova.
- Inga tankstreck (varken – eller —) i synlig text.
- Inget "jag". Inga foton som läses som "vårt kontor" eller "vårt team".
- Inga hexfärger eller typsnitt hämtade från någon annan färdig mall; allt härleds ur målbilden.
- Inga egna Unsplash-anrop och ingen egen server: allt material ligger i `assets/`, och servern
  är `python ~/.agents/skills/design/scripts/serve.py --port {{PORT}}` från repo-roten (från
  runda 2).

## Kommande rundor (så att du planerar rätt)

Runda 2: fold + signaturakt i `index.html`, skärmbilder i båda rörelselägena, `?preview=`.
Runda 3: hela sidan. Runda 4–5: rättningar efter orkestrerarens pixelläsning och
kritikertrion. Motorn (`scripts/scroll/scrollcraft.js` + `.css`) kopieras in oförändrad när
grammatiken kräver scrub, pin eller pan; bespoke rörelse läser `--sc-p`.

Avsluta rundan med en kort sammanfattning: vilka filer du läste (räkna dem), var BRIEF.md
ligger, och dina öppna frågor.

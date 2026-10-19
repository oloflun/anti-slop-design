# V3e-r2 · Mätbordet — byggspec

**Greppet, i en mening:** ramen är ett kallt, monokromt instrument — en monumental
rubrik och en gigantisk konturordmärke som skärs av viewportkanten — och de två
levande kundsajterna samt priset är monterade som **helbredds mörka plattor**
(ljuslådor), där verkens egna färger är sidans enda kromatik.

Detta är en **ny visuell tappning av V3d**, inte en fjärde runda på V3e. Copyn är
ordagrant V3d:s (facit: `runs/V3d/index.html`, redan parity-verifierad i `runs/V3e/index.html`).
Det som byts är registret, layouten och rörelsen.

---

## 1. Formproblemet (vad sidan ska göra)

Alunix är en webbyrå. Beviset är två *riktiga, levande* exempelsajter inbäddade i
sidan, plus en tredje som stillbild. Formproblemet: **hur visar man två levande,
främmande sajter inuti en sida utan att ramen konkurrerar ut dem, och hur ger man
två verk skilda identiteter på en sida som ändå har en egen?**

V3d svarade med mörk botten + pinnade helskärmsinbäddningar. V3e svarade med ett
provark och blev ett dokument. V3e-r2 svarar med **mätbordet**: sidan är ett kallt
instrument vars enda uppgift är att *ställa ut* verken. Ramen är monokrom och
återhållsam; verken är de enda föremål med färg och liv.

## 2. Referenslåset (läst med Inspo-MCP, inte ur minne)

- **Primär (dominerande riktning): `exoape-com`.** Monumental lowercase display
  som skärs av viewportens nederkant, svalt ljust register, radie 0, grotesk,
  container 1200. Greppet: *typen är designen, och den får blöda ur vyn.*
- **Lån (teknik, inte register): `dversostudio-io`.** Gigantisk konturordmärke
  (stroke-only) som arkitektonisk stomme + Geist Mono som teknisk apparat. Dess
  varma kräm/orange-register **avvisas** — det är gate 89-territorium.
- **Lån (objekt-idé): `nbstudio-co-uk`.** Verket som ett *monterat fysiskt
  föremål*, inte en miniatyr. Dess terracotta **avvisas**.
- **Avvisad:** `christophrauscher-de` (varm editorial-serif) — kolliderar med
  gate 89 och med de tre vendorade snitten (ingen serif i katalogen).

`compare` visade `sameRegister: false` på kandidaterna — därför **en** primär
riktning, inget medelvärde (gate 90).

## 3. Registret

| Roll | Värde |
|---|---|
| Instrumentvitt (grund) | `oklch(0.955 0.004 250)` — kallt, nästan vitt. **Inte** cream/ivory. |
| Bläck | `oklch(0.16 0.012 255)` — kallt nästan-svart; är också plattans färg. |
| Dämpat bläck | `oklch(0.45 0.008 255)` |
| Hårlinje | `color-mix(in oklab, var(--ink) 16%, var(--ground))` |
| Plattbläck (på mörkt) | `oklch(0.955 0.004 250)` = grund |
| Platt-dämpat | `oklch(0.70 0.008 255)` |
| Platt-hårlinje | `color-mix(in oklab, var(--plate-ink) 20%, var(--ink))` |
| **Calyx färg** (verkets egen) | `oklch(0.52 0.11 42)` rost; på mörkt `oklch(0.72 0.12 45)` |
| **Hōrai färg** (verkets egen) | `oklch(0.53 0.16 28)` rött; på mörkt `oklch(0.68 0.16 30)` |

**Ramens accent: ingen.** Ramen är helt monokrom. Nummer, regler, markeringar,
länkar och fokus bär bläck, aldrig en färg. De två verkfärgerna är **de enda
hue på sidan**, och varje färg är låst till sitt verks platta (gate 91):
plattnumret + en 1 px registreringsregel på plattan. Ingenting annat, ingenstans
annars. Detta är inveteringen mot V3e: V3e hittade på en grön accent åt ramen;
V3e-r2 lånar ingen färg alls — färgen är verkens egen.

**Förbjudet register (aktivt undviken, husets gates):** cream/ivory + serif +
kursivt ordbyte + terracotta · lila/indigo · gradient-mesh · glasmorfism · tre
lika feature-kort · 8 px-radius · hårlinjegrid som ren dekoration · em-dash i
synlig text · beskrivande mikrotext.

**En radius-skala: 0.** Allt skarpt. Radius förekommer i exakt en deklaration
med värdet 0.

## 4. Typografi

Tre vendorade filer (`assets/fonts/`), inga nya. Rollerna skiftar mot monumental:

| Fil | Roll i V3e-r2 |
|---|---|
| `geist-700-latin.woff2` | **Display.** Monumental. h1, sektionsrubriker, verkens namn på plattan. |
| `geist-mono-400-latin.woff2` | **Apparaten.** Nummer, etiketter, mätskalan, konturordmärket, pris. |
| `public-sans-300-latin.woff2` | **Brödtext.** All löpande text. |

Språng: display `clamp(2.6rem, 11vw, 11rem)` med `line-height:.88`,
`letter-spacing:-.03em`; body `1.0625rem`; mono `0.75rem` med `letter-spacing:.14em`.
Rubriker **tunga** (Geist 700) — motsatsen till V3e:s lätta rubriker, som var en
del av dokumentfelet. `unicode-range` bär `U+014D` i alla tre (mätt i V3e § T2).

## 5. Layouten, sektion för sektion

### 5.1 `header.topline`
Tunn regel under. Vänster `ALUNIX` i mono versaler. Höger `kontakt@alunix.se`.
Ingen bakgrund, ingen sticky.

### 5.2 `#hero` — monumentet
`min-height: calc(100svh - topline)`, `overflow:hidden` (cropen sker här).
- **Konturordmärket:** ett gigantiskt `ALUNIX`, stroke-only (transparent fyll,
  1 px bläckkontur), förankrat i toppen, blöder ur nederkant/högerkant. Det är
  dverso-stommen och exoape-cropen i ett — ett slående designelement, inte ett
  textdokument.
- **h1** `Er hemsida är nutidens visitkort` i monumental Geist 700, en sträng
  som radbryts till tre rader, tight, negativ spärr. Fullt läsbar.
- **Provetiketten** (visitkortsbaksidan, fyra mono-rader i tunn ram) nere till
  vänster. Ingen CTA-knapp, ingen rotation.

### 5.3 `#tes`
Fyra meningar som numrerad utsaga (mono nummer i bläck, hårlinjer). Till höger:
Hyperborea-plåten i tunn ram, `loading="lazy"`. Monokrom.

### 5.4 `#process`
Registret: sju rader, mono nummer vänster, stegnamn i Geist 700, beskrivning
höger. Nummer i bläck (inte accent), underlinjen drar ut i bläck vid fokus.
Ingen SVG-ritning (K3 äger den).

### 5.5 `#case` — ljuslådorna (sidans hjärta)
Kapitelstämpel `Exempelcase` + helbreddsregel.

Två verk. Varje verk är **en helbredds mörk platta** (bryter ut ur `.shell` till
100vw, bakgrund `var(--ink)`):
- **Topplist** (på mörkt, Geist Mono ljus): `01` i verkets färg, namnet i Geist
  700, verksamheten i mono dämpat. En 1 px registreringsregel i verkets färg under.
- **Fönstret:** den levande sajten (iframe) i en stor, hög ruta — verket lyser
  inuti den mörka mattan. `position:sticky; top:0` i sin kolumn så läsaren läser
  varje liggarrad med den levande sajten framför sig (V3e:s bevarade grepp).
- **Liggaren** (på den mörka plattan, ljus text): punkterna som numrerade rader,
  mono nummer, titel i Geist 700, text i Public Sans 300 ljus, hårlinjer emellan.
- **Hörnmarkeringar** (registreringsmärken) i plattans fyra hörn, mono-hårlinjer.

Calyx: fönster vänster, liggare höger, färg rost. Hōrai: **spegelvänt** (liggare
vänster, fönster höger), färg röd. Inbäddningarna `data-src` + `loading="lazy"`
+ `title` ordagrant.

### 5.6 `#pris`
Samma mörka platta som verken (tredje förekomsten av samma enhet — konsekvent,
inte en separat inversion). Solid mörk, ljus text, `Alla har rätt till bra design.`,
ingress, tre prisrader i mono med hårlinjer. Priset är radens största tal.

### 5.7 `#kontakt`
Tillbaka på instrumentvitt. Rubrik + underrad, linjerade fält, skarp rektangel-
knapp, `.contact-status` tom med `role="status"`. Etiketten upprepad `aria-hidden`.

### 5.8 `footer.close`
Helbreddsregel, en mono-rad: mejladressen.

## 6. Copyn

Källan är `runs/V3e/index.html` (redan parity-verifierad mot `runs/V3d/index.html`).
Varje synlig sträng återanvänds **ordagrant**, inklusive:
- `SEO&#8209;optimering` (U+2011), en förekomst.
- `Eller mejla oss direkt på kontakt@alunix.se` (R24:s form).
- h1 som **en sträng** (inte delad i två — V3e:s delning var en avvikelse).
- `.sr-only`-kopian ordagrant.
- Hyperborea som bild i tesen, **inte** som case — inga påhittade liggarrader.

Sektionsordning: hero → tes → process → case → pris → kontakt → footer.

## 7. BORT (ur V3d)

1. Det vändbara visitkortet (rotationen) → provetiketten.
2. Den självritande SVG-ritningen → registret.
3. Grafitgrunden `#0b0c0e` + blå accent `#1e5e9c` → instrumentvitt + monokrom
   ram + verkens egna färger.
4. Helskärmsifyllda, scroll-pinnade inbäddningar → fullbredds mörka plattor med
   sticky fönster.
5. Interna spår i kommentarer (`PLAN`, `R-`, `F-`, `Astra`, `Target`, `gate`,
   `TASTE`, `C-8`, `COPY-V3d`, `cell V3c`, mätvärden).
6. `data-preview`/`?preview=` om den inte behövs för rörelsen.
7. Beskrivande mikrotext.

## 8. Rörelse

Rörelsen spelar **alltid** (F-011): ingen `prefers-reduced-motion`, inget
statiskt reservdokument. All bespoke-rörelse läser `--sc-ps` (dämpad), aldrig
rå `--sc-p` (husets gate 94).

- **Delad reveal:** rader och plattor tonar in när de passerar mitten (samma
  `data-reveal`-linje som V3e).
- **Signatur-set-piece (tre lager, en rörelse):** när en platta öppnar sig
  (1) registreringsregeln på topplisten drar ut från vänster (`wipe`), (2)
  fönstret och liggaren sätter sig med ett litet translate (`settle`), (3)
  hörnmarkeringarna och plattnumret tonar till verkets färg. Alla tre läser
  samma dämpade `--sc-ps`.

## 9. Leverans

1. `runs/V3e-r2/index.html` — hela sidan, en fil.
2. `runs/V3e-r2/BYGGSPEC.md` — denna fil.
3. `runs/V3e-r2/RAPPORT.md` — vad som byggdes, vilka strängar varifrån, vad som
   uteslöts, vad som är osäkert.
4. `runs/V3e-r2/assets/fonts/` + `runs/V3e-r2/scroll/` — kopierade från V3e,
   orörda.

Motorn (`scrollcraft.js/css`, `sc-smooth.js`) är kopierad, aldrig redigerad.

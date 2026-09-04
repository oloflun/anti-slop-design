# K5 "Affisch" — Alunix, webbdesign-tjänsten

Fil: `index.html` (338 rader, inline CSS + JS, inga ramverk, Google Fonts enda externa beroende).
Bevisbilder: `demos/{calyx,horai,hyperborea}.webp`, kopierade från `~/alunix/public/demos/`.

## Reference lock + decision ledger

Samma text som HTML-kommentaren i filens header. Återges här i sin helhet.

**Primary reference/direction:** Magnetism — ordmärke som arkitektur: ett 140px edge-to-edge
namn som hela hero, en strikt katalogrutnät av objekt där varje bild följs av en etikettrad
(aldrig text ovanpå bilden).

**Preserve:** ordmärket ensamt bär hela hero, ingen tagline i samma rad, ingen lockup;
etikettrad (nummer, namn, kategori, fakta, länk) alltid UNDER varje objekt, aldrig överlagd;
nav som en enkel indexlista av ord, inga ikoner, inga kort; radikalt begränsad
färganvändning (här: en (1) kulör i stället för Magnetismens noll).

**Borrow only:** studioagriculture — ett stort namn som delar ytan med annat innehåll i
samma vypunkt (här: ordmärket ligger bakom plåtarna i stället för att ett foto blöder genom
ordmärkets ascenders); garden-eight — total tystnad ovanför bilden, inget mellansteg mellan
läsläge och monumentläge i typskalan.

**Role rules:** canvas-kulören gör exakt en sak, den ÄR sidans enda yta, aldrig en
kapitelmarkör (K2 äger färgbyte per kapitel, förbjudet här); samma kulör återkommer bara
som länk/aktivt tillstånd på pappersytan, aldrig som en andra bakgrund.

**Media strategy:** product surface, tre skärmbilder av riktiga levererade sajter
(demos/*.webp), vendorade lokalt. Inga foton, ingen 3D, ingen stock, ingen illustration.

**Reject:** Magnetisms akromatiska UI (K5 ska bära en kulör, inte noll); Studio Ag:s runda,
kondenserade röda wordmark-grotesk (fel färg, fel formkänsla för en systembyggare); Garden
Eight:s blackletter-aktiga display-serif (fel röst); kortskugga någonstans; orange/röd som
blockfärg; K3:s nästan-svarta botten; K2:s färgbyte per kapitel.

**Token commitments:** canvas = en (1) flat blå genom hela sidan (Tier 1, härledd ur dagens
instrumentregisters handlingsblå, brief.md); paper = varmvit yta för plåtarnas kort;
ink-on-canvas = nästan vit; accent = samma blånyans i en mörkare valör, bara på
länkar/aktiva tillstånd på papper; display = IBM Plex Sans 700 (rak, saklig, ingen
kondenserad grotesk, ingen serif); register = IBM Plex Mono (etiketter, siffror, nav,
kickers); radius 0 överallt; inga skuggor.

### Decision ledger

| Decision | Source | Source rule/role | Why |
|---|---|---|---|
| Flat blå canvas hela sidan (inte akromatisk, inte färgbyte per kapitel) | brief.md dagens register (#1E5E9C handlingsblå) + contract.md K5 "flat färgblock" | Tier 1: accent blir hela ytan | Samma händer utan att kopiera K3:s roll för blått (accent-only) eller K2:s byte per kapitel |
| IBM Plex Sans/Mono, ingen kondenserad grotesk, ingen display-serif | Uppgiftens instruktion: en face som hör hemma hos Alunix, en systembyggare, svensk, saklig | Reject-raden i reference-locken | Plex ritades för ett systemföretag (IBM); rak och saklig, inte Studio Ag:s runda röda grotesk eller Garden Eight:s blackletter-serif |
| Ordmärket som fixerat bakgrundslager, plåtarna skrollar över | contract.md K5 fingerprint "signature move: ordmärket skrollar bakom plåtarna" | Fingerprint-raden är bindande | Egen mekanik, byggd för denna sida, ingen av de tre låsta källorna har den |
| Etikettrad under varje plåt, aldrig text på bilden | Magnetism (primär) | caption alltid i egen rad under bilden | Matchar gallery/catalog-grammatiken, tar bort kontrastfrågan mot skärmbilden helt |
| Textnav i botten, ingen topprad | contract.md K5 fingerprint "nav: textnav i botten" | Fingerprint-raden är bindande | Håller hero fritt från konkurrerande topprad; ordmärket får stå ensamt |
| 0px radius, inga skuggor, hårlinjer | TASTE.md §2 punkt 3 och 5 | Katalogens generella husregel, inte en enskild källas signatur | Delas av hela katalogen, låser inte K5 till en specifik referens |
| Whisper-raden namnger produkterna men bär inga siffror | Coordinator-fix 2026-09-04: data-som-textur är K3:s signatur, K5 delar den inte | Fingerprintraden (K5 ska skilja sig från K3) | 757/2 847/346/21/84 drogs ur whisper-raden; kvar står bara "Samma händer bygger Alunix OS och ett lagersystem för gods, bilar och följesedlar." |

## Fingerprint (contract.md K5, byggd som given)

grammar gallery/catalog · nav textnav i botten · hero device ordmärket i viewport-bredd ·
act shape numrerade plåtar i full bredd · close kontakt som en rad · signature move
ordmärket skrollar bakom plåtarna (fixerat bakgrundslager, positionerat och storleksatt
mot `.fold-spacer`s egen box, så det aldrig kan kollidera med topp-kickers eller
brödtexten på en kort/smal mobil).

## Feeling curve

1. **Tystnad** — en enda flat blå yta, inget annat än en kicker i varje hörn, innan ögat
   ens når ordmärket.
2. **Auktoritet** — ALUNIX i viewport-bredd, en enda vikt, ingen tagline i samma rad.
3. **Förtroende** — brödtexten (ingen mall, ingen delad palett) plus systemsiffrorna som
   viskar i marginalen: samma händer, sagt utan att bevisa användning.
4. **Granskning** — tre riktiga plåtar, en i taget, skärmbild följd av etikettrad; ordmärket
   skymtar i springorna mellan dem när sidan skrollar.
5. **Klarhet** — arbetssättet som en ledger, fem punkter, två av dem ärliga platshållare
   i stället för påhittade tal.
6. **Vila** — ett enda rad-svar, `hej@alunix.se`, understruket, inget formulär.

Peak: plåtarna (akt 4) bär det största scroll-utrymmet och det enda momentet där
ordmärket och innehållet delar samma vy.

## Full svensk copy (plain text)

**Fold**
- Webbdesign
- Enskild firma · Sverige
- ALUNIX (ordmärke)
- Alunix bygger sajter åt små företag, en i taget. Ingen delad mall, ingen delad palett
  mellan uppdragen. Designen kommer ur kundens eget material: logotyp, produkt, bransch,
  inte ett färdigt tema.
- Samma händer bygger Alunix OS och ett lagersystem för gods, bilar och följesedlar.
- Kontakt · hej@alunix.se

**Bevis**
- Bevis
- Tre levande sajter, i ordning.
- 01 Calyx · Florist · Cream-papper. Cardo och PT Mono. Prissatt index. · "Kursiv och rak
  i samma rad." · Öppna sajten anti-slop-design.vercel.app/calyx
- 02 Hōrai · Restaurang · Lackröd accent. Cinzel-kapitäler. · "Fotografiet bär hela
  sidan." · Öppna sajten anti-slop-design.vercel.app/horai
- 03 Hyperborea · Konferens · Midnattsblå, bärnsten. Kodritad SVG. · "Ett ritat solmotiv
  i åtta varianter." · Öppna sajten anti-slop-design.vercel.app/hyperborea

**Arbetssätt**
- Arbetssätt
- Fem punkter. Inget formulär mellan dem.
- 01 Underlag — Alunix startar i det som redan finns: logotyp, produkt, bransch. Inte i
  ett färdigt tema.
- 02 Svar — Den som ritar sidan svarar också i mejlen. Inget team, ingen mellanhand.
- 03 Besked — Ibland är svaret nej. Då säger Alunix det.
- 04 Pris — [behövs pris]
- 05 Leverans — [behövs leveranstid]

**Kontakt**
- Kontakt
- hej@alunix.se
- En enskild firma. Samma person som bygger svarar i mejlen.

**Nav (botten)**
- Bevis · Arbetssätt · Kontakt

Whisper-raden bär inga siffror (coordinator-fix 2026-09-04: data-som-textur är K3:s
signatur, K5 delar den inte), bara "Samma händer bygger Alunix OS och ett lagersystem
för gods, bilar och följesedlar." Ingen kund namnges. Klova nämns aldrig. Pris och
leveranstid är etiketterade platshållare, inga påhittade belopp. Inga tankstreck i
synlig text.

## Skill-kedja, i ordningsföljd

1. `Skill(design)` — SKILL.md, Steg 1b (referenslås redan läst från TASTE.md +
   garden-eight/studioagriculture/magnetism som text och pixlar), Steg 2b
   (grammar gallery/catalog vald ur contract.md, bake-off överhoppad enligt uppdrag),
   Steg 3-5.
2. `Skill(copywriting)` med röstregeln (tredje person, katalogton, etiketter/numrering,
   ingen fråga) som CONTENT FUNDAMENTALS.
3. `copy-gate.md` läst i sin helhet (Pass 1b radkälla + strukturregeln) och tillämpad:
   varje rad spårad till brief.md-fakta, inga påhittade tal, discrete facts (pris,
   leveranstid) på egen rad som etiketterade platshållare.
4. `Skill(humanizer-svenska)` kört på hela katalogtexten: tricolon-konstruktionen i
   fold-brödtexten skrevs om (från tre "ingen/inget X" i rad till aktiv röst med
   variation), passiv-liknande "hämtas ur" bytt mot aktivt "kommer ur"/"startar i",
   upprepningen av "material/tema" mellan fold och Arbetssätt-punkt 01 varierades,
   inga tankstreck någonstans.

## Verifiering

- `shoot.py` (fold + full, 3890px): körd två gånger. Första passet visade brödtext
  avklippt bakom den sticky bottennaven och en tom vänsterkolumn i Arbetssätt-sektionen;
  båda fixade (nav-h-medveten `.fold`-höjd, Arbetssätt omstrukturerad till en kolumn).
  Tredje passet (efter h1/JS-fix) rent på alla tre bevisbilder, ingen klippning.
- `scroll_verify.py`: `deadScroll: []`, `cuesNeverFull: []`, `unrevealed: []`,
  `contrastUnderMedia: []`, `blankBands: []`. Nollställt i alla tre körningar.
- `contrast.py`: 17 token-bakgrunder testade, 0 under golvet (sämsta värde 5.31:1 mot
  golv 4.5:1, whisper-texten på canvas; övriga 6.5–15:1).
- `a11y_scan.py`: 0 violations, 32 passes (en `incomplete`-post, `color-contrast`-heuristik
  som redan täcks manuellt av `contrast.py`). Ett fynd under vägen (`page-has-heading-one`)
  fixat genom att lägga en `sr-only` `<h1>` i `<main>`-landmärket (första försöket, utanför
  landmärke, gav en ny `region`-varning som också fixades).
- `tab_walk.py`: tabbordningen matchar DOM/visuell läsordning exakt (skip-link → fold-CTA →
  plåt 01/02/03 → kontakt-rad → bottennavens tre länkar). Verktyget flaggar ett
  `order_mismatch` mellan stopp 1 och 2 (fold-CTA på y=789 följt av plåt 1 uppmätt på
  y=188) men det är ett artefakt av att varje fokusstopp scroll-in-view-mäts mot den
  DÅVARANDE skrollpositionen, inte ett verkligt hopp i lässekvensen. Granskad och
  accepterad, inte en defekt.
- `reflow.py`: `overflow320: []`, `overflowZoom200: []`, inga dolda element under
  reducerad rörelse.
- Mobilbrytpunkter 320/375/414/768 kontrollerade visuellt via Playwright: ingen
  horisontell scroll (`scrollWidth == clientWidth` på alla fyra), plåtarna staplar
  bild-över-etikettrad under 820px, Arbetssätt-listan förblir läsbar i en kolumn.
  En bugg hittades och fixades under detta pass: ordmärkets fasta bakgrundslager var
  centrerat mot hela viewporten i stället för mot `.fold`s reserverade utrymme, vilket
  på korta/smala mobiler (320×700) kunde få glyferna att kollidera med brödtexten.
  Fixad genom att låta JS läsa `.fold-spacer`s egen `getBoundingClientRect()` och
  storleks-/positionsätta ordmärket mot den boxen (bredd- OCH höjdbegränsat), plus en
  `document.fonts.ready`-omkörning för att undvika ett typsnittsbytes-mätfel.
- `loading="lazy"` togs bort från de tre bevisbilderna: de är sidans enda innehåll och
  ska alltid vara omedelbart synliga, aldrig bero på en lazy-load-timing i något
  granskningsverktyg.

## Coordinator-fix 2026-09-04

Efter pixelgranskning: whisper-raden under ordmärket ("Samma händer bygger Alunix OS
och ett lagersystem för gods, bilar och följesedlar. 757 entiteter · 2 847 kopplingar
· 346 skills i 21 buntar · 84 agenter.") delade data-som-textur med K3, som äger det
draget i fingerprint-tabellen. Alla fem siffrorna drogs ur raden; kvar står bara
meningen om produkterna plus Kontakt-raden, oförändrad. `index.html` header-kommentar
och NOTES.md (copylistan och decision ledger) uppdaterade i samma steg. Fold
re-shots (`shots/…--fold.png`, `…--full.png`): whisper-blocket läser rent, ingen
kollision, ingen kvarvarande siffertextur någonstans på sidan.

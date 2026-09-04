# Contract r2 — sex byråkoncept, nära källornas balans (2026-09-04)

Brief: `brief.md`. Smakprofil: `../../design-catalogue/TASTE.md` §1, §4, §6. Varje koncept har EN
dominerande källa vars **layoutbalans** det följer (hero-typ, luft, sektionsrytm, bildbehandling),
plus ett typsnitt som är det närmaste Google Font-alternativet till källans. Lånet gäller balans
och proportioner; palett tas inte ordagrant (Alunix får sin egen), sektionsordning får likna men
inte vara identisk, copy är byråns egen. Mellan koncepten: fingerprint ≤ 2/6 delade dimensioner.

| R | Dominerande källa (slug) | Vad som lånas (balans) | Typsnitt (källa → Google) | Yta / accent | Grammatik |
|---|---|---|---|---|---|
| **R1** | `squarespace` | Fullbleed mörkt foto/video-hero, centrerad rubrik i vikt 300 vid 72 px, ghost-knapp under, underrad i 15 px; kundens sajter som svävande ramar i nederkant av heron; sedan svarta och vita band som växlar, varje band en enda sats i skala | Clarkson → **Inter** 300, tracking −0.05em | akromatisk: svart, vit, tre gråa; demona är enda färgen | rhythmic cutlist |
| **R2** | `squarespace` (andra läsningen) | Vitt band med rubrik 72 px 300 vänsterställd + pill-flikar (filter) under; rad av mörka "product cards" med pil; svart band med en enda rubrik i 64 px; vit band med tre kolumner text utan ikoner; ghost-knappar överallt | Clarkson → **Figtree** 300 | akromatisk + demona | chaptered editorial |
| **R3** | `insign` | Vit hero med logotyp i serif och stor grotesk-rubrik i sentence case (76 px, vikt 400) utan foto; mosaikremsa av arbeten; tre helbreda mättade tjänsteband (Webbdesign / Design / System) med enhetsbild per band; vitt projektarkiv; mörkt avslutsband | Neue Haas Grotesk RoundDots → **Hanken Grotesk** 400; logotyp i **Instrument Serif** | tre mättade flats: ett gulgrönt, ett lavendel, ett korall-liknande, men egna nyanser | chaptered editorial |
| **R4** | `sanity` | Fullbleed mörk texturbild i heron, komprimerad tätt spårad rubrik 96–112 px vänster, en pill-CTA i en enda accent; sedan vita numrerade sektioner 01–05 med riktiga skärmbilder i stället för illustrationer, Swiss-rytm | Waldenburg → **Archivo** 700 (tracking −0.04em) + **IBM Plex Mono** för nummer | svart + vit + en accent (Alunix blå, inte orange) | chaptered editorial |
| **R5** | `mattis-studio` | Svart hero inramad som en konsol (versionstagg, klocka, hörnmarkeringar), ordmärke stort + underrubrik i versaler; ett helbrett block i en mättad färg med tes i 96 px versaler bredvid ett svartvitt foto; sedan vitt block "WE BUILD WEBSITES"-skala | Geist → **Geist** (finns på Google Fonts) 700/400 | svart, vit, ett mättat block (inte orange: välj Alunix blå eller en djup grön) | split stage |
| **R6** | `creative-giants` | Varm off-white yta, ordmärke/rubrik i vikt 300 vid affischskala med tight tracking (−0.04em), fullbleed dokumentärt foto direkt under, sedan luftiga redaktionella sektioner där färg bara dyker upp som små mättade ytor | Switzer → **Public Sans** 300 | off-white, svart, små färgytor | typographic poster |

## Fingerprint (grammatik · nav · hero-device · aktform · avslut · signature move)

| R | grammatik | nav | hero-device | aktform | avslut | signature move |
|---|---|---|---|---|---|---|
| R1 | rhythmic cutlist | topprad svart, ghost-CTA | mörkt foto + centrerad 300-rubrik + svävande sajtramar | svart/vit-band | vit sal, mejl i 72 px | ramarna glider in från nederkanten |
| R2 | chaptered editorial | topprad vit + pill-flikar | vit yta, vänsterställd 300-rubrik | vit/svart/vit, kort-rad | svart band, en sats | pill-flikarna byter vilken sajt som visas |
| R3 | chaptered editorial | vit topprad, serif-logotyp | vit yta, grotesk-rubrik, ingen bild | mosaik → tre färgband → arkiv | mörkt band med kontakt | färgbanden är tjänsterna |
| R4 | chaptered editorial | mörk topprad, mono-nav | fullbleed texturfoto + komprimerad rubrik | 01–05 numrerade vita sektioner | mörkt band + pill | numren 01–05 i mono som spår |
| R5 | split stage | konsol-ram med tagg/klocka | ordmärke i konsolram över foto | svart → mättat block → vitt | vitt block med jätterubrik | hörnmarkeringarna följer med i skroll |
| R6 | typographic poster | minimal, pill-meny | rubrik i 300 vid affischskala | luft → fullbleed foto → redaktionella sektioner | off-white kolofon | små mättade färgytor som enda färg |

Parvis ≤ 2/6. R1/R2 delar källa men inte grammatik, nav, hero, aktform eller signature.

## Foton

Vendorade: `../alunix-concepts/_assets/k1-stage-pool.webp`, `k1-stage-beams.webp` (mörk scen),
`k4-cabin-desk.webp`, `k4-desk-overhead.webp`, `k4-paper-tan.webp`, `k4-paper-linen.webp`. Nya
foton hämtas bara via `scripts/catalogue/unsplash_sheet.py --ids-file` med ID:n som jag
levererar; agenten får inte skrapa själv. Foton är atmosfär och material, aldrig "vårt team".

## Copy (en byråröst för alla sex)

Vi-form, Insign-nivå, ur briefens rader. Kedjan: `Skill(copywriting)` med CONTENT FUNDAMENTALS =
"digital byrå, vi, självsäker, kort, professionell; alla har rätt till bra design; nutidens
visitkort; vårt enda mått: perfektion" → `copy-gate.md` Pass 1b (radkälla; Antons rader räknas
som källa 4, redan bra) → `Skill(humanizer-svenska)` (ta bort tell, inte ton). Koncepten får
variera betoning (R1 löftet, R3 tjänsterna, R4 processen, R6 filosofin) men inte registret.

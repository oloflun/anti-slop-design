# Kontrakt r4 — tre remixer, en agent per cell

Cellerna: `cells/M1-chain/index.html`, `cells/M2-chain/index.html`, `cells/M3-chain/index.html`, var och
en med `scrollcraft.js`/`.css` bredvid sig, `NOTES.md` och `shots/`. Ramar och bilder via absoluta
sökvägar (se brief.md). Fonter via Google Fonts som i r3 (Geist + Geist Mono, Public Sans; M2 får lägga
till en font ur sin källa om den bär strukturen).

## M1 · Kontinuerlig grund · förskjutna spalter

- Källor: `rre-ventures` (en enda bild/grund som löper hela sidan, omväxlande exponerad och täckt av
  opaka paneler), `veloura` (vinjetten som aldrig nollställs), `creative-giants` (R6:s proportioner).
- Struktur: (1) Tidvatten-ramen fullbredd som första akt, loggan över ramens övre kant, R6:s
  ordmärke som tunn topprad; (2) två spalter, R5-innehållet till vänster, R6:s tjänster/prisruta till
  höger, **högerspalten börjar 50vh lägre** så att sektionerna aldrig linjerar; (3) en mörk grund
  (hero-console.webp eller k4-cabin-desk.webp i gråskala, fixed/attachment) som syns i luckorna mellan
  panelerna; (4) Hōrai och Calyx som ramar i var sin spalt; (5) prisrutan sist i högerspalten, Calyx
  sist i vänster; sidan slutar när båda är slut (får vara olika höjd: grunden fyller resten).
- Rörelse: text i panelerna stiger med `data-sc-parallax` positiv (snabbare än scrollen), bilder/ramar
  sjunker (negativ rate, hundratals px); panelerna `reveal="up"`; grunden `drift` i tre stopp.
  Signature move (förslag): grundbilden **avslöjas genom fönster** som öppnas i panelerna när de passerar
  mitten av viewporten (clip-path från `--sc-p`), så att en och samma bild syns bit för bit.
- Nav: ingen fast bar; en tunn topprad med ordmärke + kontakt-länk som skrollar bort.

## M2 · Kapitel · pinnad scen

- Källor: `sanity` (numrerade sektioner 01–05, mono-spår), `vinterspelen` (den pinnade scenen med
  kulisser som glider isär), `not-real` / `shelby-kay` (roterad löptext längs kanten).
- Struktur: en spalt, max 1100 px. Kapitel: 01 `ALUNIX / Digital byrå` (konsolkortet som titelsida,
  R5), 02 `Er hemsida är nutidens visitkort` = **pinnad scen** (`data-sc-act="pin"`, span ≥ 3) där
  Tidvatten, Hōrai och Calyx byter plats med `iris`/wipe i takt med `--sc-p` och kapiteltexten
  (tjänsterna 01–03 ur R6) korsar scenen som cues, 03 `DET FÖRSTA INTRYCKET ÄR DIGITALT.` (blått block,
  R5), 04 `VI BYGGER ERT VARUMÄRKE.` + ledgern, 05 `Alla har rätt till bra design.` (inverterad
  prisruta med kontakt). Folio i vänstermarginalen (`01/05` i mono), löptext roterad 90° längs
  högerkanten som bär kapitelnamnen och loggan.
- Rörelse: text glider in från höger (`data-sc-reveal="left"` på textblock eller egen translateX), bilder
  wipas från vänster (`reveal="right"`); scenen pinnad, kulisserna (tre ramar) glider isär/ihop.
  Signature move (förslag): **löptexten längs kanten är scrollens spelhuvud**: den rullar i takt med
  `scrollY` och kapitelnamnet som står i höjd med loggan är alltid det aktiva kapitlet.
- Obs: ramarna får inte transformeras när de är synliga och interaktiva; låt scenen byta ram genom
  clip-path/opacity på ett **omslag** som sedan blir statiskt (`pointer-events` på när ramen är öppen).

## M3 · Galleri · sidopanering

- Källor: `vintergatan` (ord scrubbade ur scrollen, tråden som ritar sig), `palais` (kortvågen),
  `garden-eight` (en kurva, sex durationer), `mattis-studio` (konsolramen).
- Struktur: (1) öppning: R6:s affischordmärke `ALUNIX` i viewport-bredd **ovanför** R5:s konsolkort,
  loggan mellan dem; (2) `Webbdesign, design och system. Allt på ett ställe.` som etikettrad;
  (3) **horisontell rail** (`data-sc-act="pan"`, span ≥ 3, mätt overflow) där de tre ramarna är objekten
  med etiketter (Tidvatten · Hōrai · Calyx, plats + tjänst 01–03 ur R6 som etiketttext); ramarna ≈ 70vw
  breda, interaktiva när railen står stilla (pan-akten slutar med dwell); (4) det blå tesblocket
  fullbredd; (5) `VI BYGGER ERT VARUMÄRKE.` med ledgerns tre rader **scrubbade ord för ord** ur
  scrollen (vintergatan); (6) prisrutan som sista objekt, sluter i en kolumn.
- Rörelse: text panorerar åt vänster (etiketter/rubriker med egen translateX från `--sc-p`), ramarna
  panorerar åt höger (railens riktning); det blå blocket `reveal="iris"` (en gång); ordscrubben är
  signature move (får förbättras, inte bytas mot en kit-parameter).

## Gemensamt

- NOTES.md: reference lock (källor + vad som lånas/avvisas), decision ledger, känslokurva, topp,
  tell-someone, signature move, device-tabell per akt, fingerprint-rad, verifieringssiffror.
- `Skill(design)` laddas via Skill-verktyget (Steps 0–6; Tier 2: r3-sidan + källorna). Ingen copy-kedja
  (copyn är ordagrann ur r3). Inga sub-agenter. Inga ändringar utanför den egna cellen. Ingen commit.

# Verdict r3 — R5 + R6 kombinerade till en sida (2026-09-04)

Anton valde en kombination av R5 (vänster) och R6 (höger) enligt sin mosaik (`reference-mosaic.png`)
och gav sju ändringar (`brief.md`), sedan två rättningar: proportionerna ska vara referensens med
höjdskillnaderna intakta (`targets.md`), ingen rubrik över Hōrai, loggan 30 % större, och Tidvatten
i fotorutan under ordmärket. Bygget: `build/index.html`, öppnas via repo-roten
(`/tests/alunix-concepts-r3/build/index.html`), ramarna använder `/sites/…` som också gäller på Vercel.

## Fyra rundor

| runda | vad | resultat |
|---|---|---|
| 1 bygge | port av R5/R6 till två `cqw`-spalter, ramar, prisruta, logga, scroll-koreografi | sex fel vid min pixelläsning |
| 2 fix | ordmärket klipptes av fotot, loggans dockning trasig, kinetisk rubrik och fotorubrik tonade bort, tomband över prisrutan, tesblockets radbrytning | rättat; men hero och foto låg i `vh` |
| 3 proportion | alla höjder i `cqw`, måltabellen ur referensen, Tidvatten-ram, ingen rubrik över Hōrai, logga × 1,3 | 19 gränser inom ±0,03w, sidan = 2,69w exakt; fyra nya fel |
| 4 fix + copy | hero-kortets marginal, mjuk scrim, klippt Ä, avklippt kontaktrad; copy-kedjan med grep-bevis | rättat; kedjan bevisad |
| 5 mobil + scrim | hero-kortet, ledger och tjänster i en kolumn under 900/768 px; scrim som ljusfall | kontrast 11,1:1 / 8,9:1, desktopgränser byte-identiska |
| 6 Tidvatten upp | ordmärkesbannern bort, Tidvatten-ramen 0–0,83w, foldkopian `build/tidvatten-hero.html` med "Er hemsida är nutidens visitkort" (Familjen Grotesk 600, 70 % av Tidvattens h1) och underraden i Literata | kontrast 8,2:1 / 6,1:1 värsta fall; allt från 0,83w oförändrat |

Underraden efter kedjan: "Vi skapar skräddarsydda webbplatser som hjälper er att exponera verksamheten."
(Antons frö: "…digitala lösningar som hjälper er att exponera ert företag i dagens klimat"; "i dagens
klimat" ströks som tidsmarkör utan innehåll, "digitala lösningar" blev "webbplatser" eftersom ramen
visar en webbplats.) Tjänst 01 fick "visa upp" i stället för "exponera" så ordet står en gång.

## Kedjan fyrade (ledgern `.impeccable/design-session.jsonl`, sedan bygget startade)

| skill | laddningar | bevis |
|---|---|---|
| `design` | 1 | hook-ledgern |
| `copywriting` | 2 | grep-räknare 6 → 7 (runda 4), 7 → 8 (runda 6) |
| `humanizer-svenska` | 2 | grep-räknare 6 → 7 (runda 4), 7 → 8 (runda 6) |
| `copy-gate.md` Pass 1b | läst som fil, två gånger | NOTES.md |

Runda 1-agenten påstod sig ha laddat copy-skillsen, men ledgern visade bara `design`; därför fick
runda 4 kravet att bevisa laddningarna med räknaren före och efter. Det är ett mönster värt att
behålla: rapporten räcker inte, ledgern avgör.

## Mått mot referensen (1440 px, w = 720)

Alla nitton gränser i `targets.md` inom ±0,03w; sidhöjd 1937 px = 2,69w = referensens vänsterspalt.
Hero 0,52w, blått block till 0,99w, jätterubrik från 1,09w, ledger 1,41/1,53/1,65w, Calyx från 1,87w;
ordmärke 0,24w, Tidvatten till 0,83w, tjänster till 1,28w, Hōrai till 2,10w, prisrutan till 2,69w.
Proportionerna håller vid 1280 och 1920 eftersom allt är `cqw`.

## Scroll-koreografi

Grammatik split stage. Signature move: skarven mellan spalterna ritar sig nedåt från loggan i takt
med scrollen (`--seam-p` ur scrollposition, aldrig en kit-parameter). Devices: `reveal` (blått block,
Calyx), `iris` (Hōrai, en gång), `kinetic lines` (VI BYGGER ERT VARUMÄRKE.), `parallax` (borttagen på
ordmärket efter klippfelet), `in` + stagger (ledger, tjänster), greet-and-hold-cues. Toppen: de två
levande sajterna i samma scrollspann. Reduced motion: allt synligt, skarv och logga statiska.
`scroll_verify.py` rent, inga `[scrollcraft]`-varningar.

## Copy

Rubriker ordagranna (bytet "Vi bygger ert varumärke." gjort). Undertexterna omskrivna så att
"skräddarsydd", "exponera", "allt på ett ställe", "nutidens visitkort" och "från grunden" förekommer
högst en gång utanför rubrikerna. Dubbletten "behov som går längre / djupare" struken: ledger 03
namnger Alunix OS som teknisk höjd, tjänst 03 säger vad ett system gör för kunden. Priser som egna
rader (10 990 kr, 15 990 kr, pris vid förfrågan), kontakt kontakt@alunix.se överallt.

## Kvar / ärligt

- Tidvatten-rubriken kräver en scrim: vit text mät 2,4:1 utan, bläck 1,1:1; radiell scrim ger ≥ 7:1.
- Loggan ligger över Tidvattens lilla ordmärke i ramen; det följer av placeringen Anton bad om.
- Mobil (≤ 900 px) staplar spalterna; det är inte referensens layout och bedöms separat.

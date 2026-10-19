# C3 · "Väggen" · gallery/catalog, mosaiken som vägg man dyker in i

Cell `cells/C3-r1/` · port 3106 · `?preview=`: `hero`, `vagg`, `dyk-1`, `dyk-4`, `kartlaggning`, `om`, `insikter`, `slut`.

**Lane:** ljus katalog i gemener, brickorna som vägg och rum.
**Typsnitt:** display **Funnel Display** 500 (rubriker, versaler som originalet, spärr +.015em,
`clamp(2.8rem, 6.5vw, 5.5rem)`, leading .98) + text **Figtree** 400/600.
**Auktoritet:** objektet (brickan).
**Grund:** `--bakgrund`; dyken är tjänstefärgerna; sidfoten `--ink`.
**Referens för akten:** d2c-lifescience (kuben → väggen → dyk in i en bricka → golvet).

## Formationer (bricklagret, 28 brickor)
| # | Sektion | Formation | Fönster |
|---|---|---|---|
| F1 | Intro/hero | **moln i tre djupplan** över videon (9 × 24 px, 9 × 44 px, 10 × 72 px) | intro 1,2 s |
| F2 | Väggen | molnet ställer upp sig till en **vägg** mitt i vyn: **varje tjänst = en 2×2** (brickor 9 vh), de sju 2×2:orna i en 4+3-vägg (två rader, centrerad, slots i en grid); rubriken "DET DU BEHÖVER FÖR ATT VÄXA" ovanför väggen (centrerad, Funnel 500), kicker + länken | 100 → 25 % |
| F3 | Dyk 1–7 (sju sektioner, flöde) | när tjänst k:s sektion kommer in **växer dess 2×2 till att täcka vyn** (fyra brickor till fyra slots som tillsammans fyller vyn, sömmar 8 px papper) och blir sektionens grund; de andra sex 2×2:orna krymper till 16 px och lägger sig i en **rad överst i sektionen** (slots), den aktiva i full storlek; när sektionen lämnar krymper fälten tillbaka till väggens slot och nästa växer. Texten står på fältet: löpnummer, namnet (Funnel 500, 4 rem), `kort_pa_startsidan` 40 ch, "Läs mer →", vänster 6/12, tyngdpunkt 44 %. Färg per fältets ljushet | 100 → 25 % in, 25 → 0 % ut |
| F4 | Kartläggning | alla 28 bildar **ett golv**: ett 7×4-raster med fallande brickhöjd 48 → 20 px rad för rad (slots, perspektiv utan 3D) under limebandets text | 100 → 25 % |
| F5 | Om | fyra markörer i ledgern + 24 som en **lodrät kolumn** mellan rubrik och ledger | 100 → 25 % |
| F6 | Insikter | tre markörer (96 px) + 25 i rad | 100 → 25 % |
| F7 | Sidfot | sju små 2×2 framför TJÄNSTER-namnen (indexet bildas) | 100 → 0 % |

Övergångsorsaker: molnet blir väggen · 2×2 växer till rummet (sju gånger inom akten, det är aktens mekanik) · väggen blir golvet · golvet blir kolumnen · kolumnen blir indexet.

## Layout
- **Nav:** tunn rad 48 px (logotyp, länkar i Figtree 500, "Kontakta oss") + **indexrad** med de sju
  tjänsterna (2×2 12 px + namn); aktiv tjänst markeras under dyken; klick = scrollTo. Mobil: meny.
- **Hero:** full-bleed video; rubriken **nederst i vyn, vänster, på en ink-platta som är ett band
  12/12 × 34 vh** (ny: typen sitter i en mörk remsa i nederkant, videon ovanför; Filmbot-principen,
  grundbyte genom bilden): kicker, rubrik (Funnel 500, versaler), lead + ingress i två kolumner,
  knapparna. Molnet svävar i videodelen. Videon autoplay; scroll: videon zoomar 1 → 1,12 (scrub,
  ingen pin), remsan rider i 1×.
- **Väggen:** centrerad, 100 vh, rubrik ovanför. **Dyken:** sju sektioner à 100 vh, text 6/12.
- **Kartläggning:** lime, rubrik 7/12 + text, knapp; golvet under texten.
- **Om:** rubrik 7/12, text 40 ch, ledger 4/12. **Insikter:** tre plates i rad (bricka 96 px,
  kategori·datum, rubrik Figtree 600, utdrag, hårlinje). **Sidfot:** ink, index.

## Enheter
intro → parallax-zoom (hero, scrub, ingen pin) → lagerformation (vägg) → lagerfält per dyk + flow+in → lagerformation (golv) → flow+in → lagerformation (index).

## Skiljer C3
Grammatik gallery · nav tunn rad + index · hero video med ink-remsa nederst · 0 pinnar · slut = indexet · signatur = väggen man dyker in i, en tjänst i taget.

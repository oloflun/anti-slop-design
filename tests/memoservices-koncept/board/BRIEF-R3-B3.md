# B3 · "Banden II" · chaptered band, 2×2:an är rummet, sticky tjänsterail

Cell `cells/B3-r1/` · port 3105 · `?preview=`: `hero`, `fullbleed`, `band-1`, `band-4`, `band-7`, `kartlaggning`, `om`, `insikter`, `slut`.

**Lane:** platt och ljus i gemener, bandet är tjänsten, listan är kartan.
**Typsnitt:** display **Schibsted Grotesk** 800 (rubriker, versaler som originalet, spärr +.01em,
`clamp(3rem, 8vw, 7rem)`, leading .92) + text **Onest** 400/600 (nav, lead, listor, knappar).
**Auktoritet:** ytan/färgen.
**Grund:** `--bakgrund`; banden är tjänstefärgerna; sidfoten `--ink`.

## Formationer (bricklagret, 28 brickor)
| # | Sektion | Formation | Fönster |
|---|---|---|---|
| F1 | Intro/hero | **hero-mosaiken** (facit + brun + sten + grafit = 28) uppe till höger, 44 px brickor | intro 1,2 s |
| F2 | Hero → full bleed (pin 200 vh) | 24 brickor krymper och flyr ut mot kanterna; **4 brickor växer till en 2×2 i viewportskala** (sömmar 8 px papper) som ligger **bakom** videon; videon (i en bricka som växer, runda 1-greppet men ramen är nu ett av lagrets fyra stora fält) blir full bleed | 0–100 % av pinnen |
| F3 | Tjänster (7 band, **ett undantag från "ingen pin"**: en sticky vänsterrail, men banden flödar) | de fyra stora fälten är kvar som sidans grund och **byter färg per band** (tre fält huvudfärg, nedre högra accent) med en scrubbad `backgroundColor`-tween över varje bandgräns (fönster 100 % → 25 % av nästa band); de 24 små brickorna ligger som ett **7×4-raster i accentfältet** och **den aktiva tjänstens fyra brickor står i full färg**, övriga i papper .3 | per band |
| F4 | Kartläggning | fälten blir lime (tre) + ink (accent); de 24 bildar två rader av 12 ovanför knappen | 100 → 25 % |
| F5 | Om | fälten tonar till papper (grunden återställs, sömmarna försvinner genom att fälten får samma färg som grunden); fyra brickor blir ledgerns markörer, 24 en vågrät rad under rubriken | 100 → 25 % |
| F6 | Insikter | tre markörer + 25 i rad under rubriken | 100 → 25 % |
| F7 | Sidfot | de fyra fälten krymper till **en 2×2 på 128 px** bredvid logotypen (app-ikonen) och de 24 ställer sig som sex små 2×2 bakom namnen i TJÄNSTER (sjunde är ikonen) | 100 → 0 % |

Övergångsorsaker: brickan som växer till ram och full bleed · fälten byter färg (bandbyte, sju gånger inom akten) · samling till lime · fälten tonar till papper · fälten krymper till ikonen.

## Layout
- **Nav:** full bar 64 px som tar bandets färg (behålls, det fungerade), men länkarna i Onest 500
  gemener och "Tjänster"-panelen som en **rad av sju 2×2 med namn under** (sju kolumner).
- **Hero:** rubriken "RÄTT KOMPETENS. / NÄR NI BEHÖVER DEN." i Schibsted 800 **över hela bredden**
  (12/12), lead + ingress i 2 kolumner under (6/12 + 6/12, staggade 6 vh), knapparna under; mosaiken
  i lagret uppe till höger; videon i brickan **under** rubriken, 12/12 bred, 48 vh hög (ny: videon
  är ett band, inte en kolumn). Scroll: videon växer till full bleed.
- **Tjänster:** **sticky vänsterrail** (3/12): de sju tjänstenamnen som en lista (Onest 600, 18 px);
  aktiv = ink/papper beroende på band, resten .55; klick = `lenis.scrollTo`. Höger (9/12): varje
  band är en sektion med 100 vh min-höjd: löpnummer, namnet (Schibsted 800, 4 rem, versaler),
  `kort_pa_startsidan` i 44 ch, "Läs mer →". Textfärg per bandets ljushet, mätt.
- **Kartläggning:** lime; rubrik 8/12, text + knapp 4/12 till höger, 12 vh förskjutna.
- **Om:** rubrik 7/12, text 38 ch; ledger 5/12. **Insikter:** ledger. **Sidfot:** ink.

## Enheter
intro → pin+scrub (full bleed) → flöde + lagerfärg per band + sticky rail → reveal (lime) → flow+in → lagerformation (slut).

## Skiljer B3
Grammatik chaptered band · nav full bar som tar färg · hero rubrik 12/12 + videoband 12/12 · 1 pin · slut = fälten krymper till ikonen · signatur = sidans grund är fyra fält som byter färg per tjänst medan de 24 små brickorna visar vilken.

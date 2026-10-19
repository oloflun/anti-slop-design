# C3-r1 · "Väggen" (runda 3)

**Lane:** en ljus katalog i gemener där 28 brickor bildar en vägg, och man dyker in i en tjänst i taget när dess 2×2 växer till rummet.
**Auktoritet:** objektet (brickan). Typ och foto står tillbaka utom i heron.
**Referens:** d2c-lifescience (kub → vägg → dyk → golv), thewatch-60fps (inga pinnar, objektet glider medan typen passerar).

## Typsnitt
| Roll | Snitt | Grad |
|---|---|---|
| Display (rubriker, tjänstenamn) | Funnel Display 500 | `clamp(2.8rem, 4.9vw, 5.5rem)` (71 px vid 1440), leading .98, spärr +.015em; mobil 7,6vw. Dyknamn `clamp(2.2rem, 4.4vw, 4rem)` |
| Text (allt annat) | Figtree 400/500/600/700 | brödtext 17–18 px, nav 15 px 500, knappar 19 px 700 |

4,9vw i stället för 6,5vw: Funnel är brett (0,62 em/tecken). "NÄR NI BEHÖVER DEN." är 1000 px vid 88 px och skulle inte rymmas i 8/12. Figtree 700 används bara i knapparna: brandröd mot ljus text ger 4,17:1, så texten måste vara stor (≥18,66 px fet) för att klara AA.

## Formationer (bricklagret, 28 brickor, ett `#lager`)
Övergångsfönster = sektionens topp från 100 % till 25 % av vyn. Undantag (3b): dyken 100 → 45 %, och sidfoten 100 → 0 % men slutar 10 vh före max scroll eftersom Lenis stannar några px före max. Tidslinjens tid är scroll i px.

| # | Sektion | Slot-mönster | Fönster | Ordning ut |
|---|---|---|---|---|
| F1 | Hero | moln i tre djupplan: 10 × 5vw (72 px), 9 × 3vw (44 px), 9 × 1,67vw (24 px), alla sju huvudfärgerna i det stora planet | intro 1,2 s | n/a |
| F2 | Väggen | sju 2×2 (brickor 8,6vh) i en vägg 4+3, namn under | väggens topp 100 → 25 % | färg för färg (tjänst, sedan ruta) |
| F3 ×7 | Dyk 01–07 | tjänst k: fyra fält (kolumner 57/43; övre raden 64 vh, nedre en remsa min(120 px, 15 vh); 8 px papper i sömmar och kant; radie 10/51 med tak 28 px för fält bredare än 300 px). Sektionen är 64 vh + remsan + 24 px hög. Övriga sex 2×2 à 16 px i en rad överst till höger (den aktiva platsen står tom) | dykets topp 100 → 45 % | runda 3c: utgående och inkommande 2×2 flyttas som GRUPPER. Gruppens rektangel, sömmar och delningar interpoleras mellan de fyra slotsen i start- och slutläget, och de fyra brickorna läggs i rektangeln varje bildruta, så de kan aldrig överlappa varandra. Utgående krymper 0–60 % (yta linjär), inkommande växer 30–100 % (yta power3.out). Utgående dyks text tonar med fältets yta/startyta. Dyktexten visas när inkommande täcker 90 %. Stora fält ligger under de små brickorna (z-index), så indexraden syns ovanpå varje rum |
| F4 | Kartläggning | golv av kvadrater, 7 kolumner, radhöjd 36/28/22/16 px, radavstånd 14/10/7, centrerat under texten (spalt 1–7). Lime-accenterna blir ink-kontur på lime | 100 → 25 % | rad för rad (mål) |
| F5 | Om | juridikens fyra brickor blir ledgerns markörer (3 brandröda + 1 lime, som originalet); 24 som en lodrät kolumn av sex 2×2 | 100 → 25 % | rad för rad (källa) |
| F6 | Insikter | tre markörer à 96 px (Redovisning, Skatt, Nyhet = juridikens röda accent) och 25 i en rad över bredden | 100 → 25 % | kolumn för kolumn (källa) |
| F7 | Sidfot | sju 2×2 (9 px) framför TJÄNSTER-namnen | 100 → 0 % | kolumn för kolumn |

Övergångsorsaker: molnet ställer upp sig till väggen · en 2×2 växer till rummet (sju gånger) · rummen läggs ned till golvet · golvet reser sig till kolumnen · kolumnen blir raden · raden blir indexet.

## Akter och enheter
| Akt | Enhet | Spann | Orsak |
|---|---|---|---|
| Intro | kinetic (brickor skalas in plan för plan med back.out, rubrikens radmasker) | 1,2 s | molnet är kvar efter introt |
| Hero | parallax-zoom: videon 1 → 1,12, scrub, ingen pin. Remsan rider i 1× | heron ut ur bild | grundbyte genom bilden (ink-remsa) |
| Väggen | lagerformation (scrub) | 75 vh | molnet ställer upp sig |
| Dyk 1–7 | lagerfält (scrub) + flow+in | 7 × 75 vh | 2×2 → rum |
| Kartläggning | lagerformation (golv) | 75 vh | rum → golv |
| Om / Insikter | flow+in + lagerformation | 75 vh var | golv → kolumn → rad |
| Sidfot | lagerformation (index) | till slutet | rad → index |
| Hela sidan | pekare: lagret 0,6 % mot pekaren (`quickTo`, bara hover:hover) | | |

Regel 4 (text i lästempo): indexraden i sidhuvudet. Den aktiva tjänsten lyser i ink med en linje under, medan de andra står i grafit, och det drivs av scrollen genom dyken.
Regel 5 (typ och media i samma ram): heron, där rubriken står i ink-remsan i videons nederkant.
Tonal inversion: hero-remsan och sidfoten (ink).
Ett ögonblick som inte är information: golvet på limegrunden.
Pinnar: 0.

## Signaturobjektets jobb
1. **Moln** över piren (heron, tre djupplan).
2. **Vägg och register**: de sju 2×2:orna är tjänstelistans index och länkar till respektive dyk.
3. **Rum**: varje tjänsts 2×2 blir sektionens grund, och texten står på fältet.
4. **Golv, kolumn och markörer**: kartläggningen, om-ledgern (punktmarkörerna) och insikternas kategorimarkörer.
5. **Index** i sidfoten.

## Ägare per egenskap
- `.b`: x, y, width, height. Ägs av master-tidslinjen (en `ScrollTrigger`, `scrub: true`, `trigger: body`, `end: 'bottom bottom'`, byggs om vid varje refresh från slot-rektanglarna).
- `.b > i`: färg och radie ägs av master. `transform` ägs av introt. CSS `translate` (`--dx`/`--dy`) ägs av vilan (±4 px, ±0,8 px för fält, period 6–9 s).
- `.lager-scroll` (scroll-offset) och `#lager` (pekaren) har var sin ägare.

Ingen `will-change` på brickorna: när fälten bytte storlek allokerade varje lager om sin textur varje bildruta. Mätt med motion_probe: 7–30 bildrutor > 33 ms med will-change, 0 utan. Det är en medveten avvikelse från R3 § 1a.

## `?preview=`
`hero`, `vagg`, `dyk-1`, `dyk-4`, `kartlaggning`, `om`, `insikter`, `slut`. Alla landar i vilotillståndet. Dyken landar med sektionens botten i vyns botten, precis innan nästa fönster börjar.

## Mätvärden efter runda 3c (port 3106, headless)
- `verify_text.py`: 138 textnoder, **0 avvikelser**.
- `scroll_verify.py`: deadScroll 0, unrevealed 0, cuesNeverFull 0, vid både 1440 och 390.
  - Vid 1440 kvarstår artefakten i `contrastUnderMedia`: det opaka sticky-sidhuvudet ligger över videon.
  - `contrast_over_media.py`: **PASS**.
- `motion_probe.py --track "#lager .b:transform" --cpu 1 --ticks 200`: **PASS** två körningar i rad. p95 16,7 ms, >33 ms 0, staircase 0, dead false, max_step 1,1 %.
- `a11y_scan.py`: **0 violations**, 38 passes, 1 incomplete.
- Mellanlägen, mätt i 0,05-steg genom alla sju dykfönster:
  - Täckning av vyn: minst 34,6 % vid 1440×900 och 33,3 % vid 390. Inget tomt pappersläge.
  - Regeln 40 %/20 % (när utgående fält har 40 % kvar av sin yta ska inkommande redan täcka 20 %): 0 överträdelser. När utgående har 42 % kvar täcker inkommande 20 %, vid 33 % kvar täcker det 37 %.
  - Inom en grupp överlappar brickorna aldrig, eftersom de läggs i ett rutnät.
  - Mellan grupperna glider det utgående rummet under det inkommande eller ovanpå som en liten 2×2 på väg till sin indexplats.
- Konsol: 0 fel. Inget överflöde vid 320/375/414/768/1440. Sidfoten: 28/28 brickor på plats vid 1440 och 390.
- Dyktext mot sömmar (1440×900, 1920×1080, 1366×768, 390, 375): texten ligger inom det övre vänstra fältet med tyngdpunkt 44 %. Största radie 28 px.
- Juridik-felet från runda 1–3b är rättat: indexraden visade bara tre av sex minis, eftersom de lägre tjänsterna låg under fältet. Nu syns alla sex.
- Kontaktark: `design-catalogue/entries/memo-C3-self/motion/sheet.webp`.

## Handskriven text (ordagrann, kontrollerad av verify_text)
- Kolumnrubrikerna TJÄNSTER/FÖRETAGET/JURIDISKT. De är nycklar i `delat.json` och har inget värde att rendera.
- Om-punkternas resttext efter `<strong>`.
- Koncernradens början före länken.

render.py kan inte dela strängar, så de här bitarna skrevs av ordagrant ur `start.json`.

## Inte hunnet / öppet
- Övergången från sista dyket till golvet går fortfarande bricka för bricka, eftersom golvets kolumn inte är en 2×2. Texten tonar ändå ut med fältets yta.
- Mobilmolnet är litet (enheterna är i vw), men kompositionen är densamma.
- Ingen hover-tilt på brickorna (R3 tillåter bara lagerförskjutningen).

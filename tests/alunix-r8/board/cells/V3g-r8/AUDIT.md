# V3g · Opus-granskning av hela sidan · 2026-09-28

Fyra granskare, alla på Opus och utan delegering: `design-critic`, `design-heuristics`,
`design-a11y-reviewer` och `design-perf-reviewer`. De körde headless och delade webbläsarlåset.
Rapporterna ligger i `reviews/opus-*.md`, och perf-mätningarna i `shots/perf-review/`.

Leaden har kontrollerat varje fynd markerat ✔ själv, i pixlar eller i koden. Fynd utan ✔ bygger på
granskarens mätning och kontrolleras i rättningsrundan.

**Domar:** critic `fix`, heuristics `fix`, a11y **`Block`**, perf `fix`.

**Kunde inte göras:** jämförelsen mot de låsta referenserna (aspensearch, cyphr, exoape, area17).
De lästes bara via Inspo i V3f och finns inte fångade på disk, och granskarna hade inte Inspo-verktyget.
Taket mot referenserna är därför inte bedömt.

## HIGH, ska rättas i R7
| # | Fynd | Källa | Kontroll |
|---|---|---|---|
| H1 | Showcasens iframe är beskuren: den visar 61,6 % av sajtens bredd (1440) och 27 % (390). Citat och priser klipps i högerkanten. V3d visade hela bredden. | critic | ✔ pixlar (`critic-opus/1440-015`) |
| H2 | Tesrubrikens topp och prickarna över ö ligger under topplisten hela pinnen (skyddad effekt, "helt synlig") | critic | ✔ pixlar (`probe-tes-pinned-1440`) |
| H3 | Prisingressen refererar till sidan: "det ni just har sett … varje rad nedan" (F-018) | critic | ✔ index.html:830 |
| H4 | Kontrast i casehuvudet: 2,95:1 på rost, 2,57:1 på lack, och 1,34:1 mot svart vid inflygningen | critic, a11y | ✔ pixlar |
| H5 | Båda "Boka ett möte" är döda: kortets länk saknar `href`, kontaktens går till `#kontakt` | heuristics, a11y | ✔ index.html:587, 882 |
| H6 | Skärmläsare når 1 av 5 respektive 1 av 6 showcasesteg (inaktiva steg har `aria-hidden` och `visibility:hidden`) | a11y | kod |
| H7 | Den dolda iframen (opacity 0) ligger i tabbordningen: 3 och 5 osynliga stopp. Fokus inne i Calyx skrollar ramen 524 px i sidled permanent | a11y, heuristics | kod |
| H8 | SplitText `aria:'auto'` ger `aria-prohibited-attr` på `<p>`/`<span>`, och tesens meningar saknas som text i trädet | a11y | ✔ index.html:1112–2049 |
| H9 | Fokusringen på kortets baksida klipps bort helt (`overflow:hidden`). Fokus hamnar på `<body>` efter vändningen | a11y | kod |
| H10 | Vid 768 × 432 (200 % zoom) klipps stegtexten, och hjulet skrollar inte panelen | a11y | mätning |
| H11 | `will-change:opacity` ligger permanent på 728 rutspann: 211 lager i hero, median 50–67 ms vid 4× CPU. Utan det: 19 lager och 16,9 ms | perf | ✔ index.html:508 |
| H12 | Calyx-iframen laddas direkt vid sidladdning, med hotlänkad Unsplash och Tailwind-CDN. Sidan blir 2,89 MB mot budgeten 2,5 MB, med långa uppgifter på 1,2 och 1,4 s | perf | ✔ index.html:720 |
| H13 | CLS 2,85 vid 1440: tre refreshar vid laddning plus tes-pinnen. LCP rapporteras som 4,6–8,1 s | perf | mätning |
| H14 | Mobil: efter byte till Hōrai startar radernas triggers 1 155 px för sent (byggda innan Calyx döljs), och ramen är tom tills Hōrai laddats | heuristics, a11y | mätning |
| H15 | Sidfotslänken bryts på två rader vid 390 (grind 49) | critic | mätning |

## MEDIUM, rättas i R7 där rättningen är entydig
- Hero-pinnen lämnar ett svart band på 48 px under scenen (samma start `top+=48` som tesen).
- Casknapparnas tillgängliga namn skiljer sig från den synliga etiketten (2.5.3). Mintringen har
  1,48:1 och kortets framsidesring 1,05:1 (1.4.11).
- Kortets länkar är 17 px höga (mål ≥ 44 px). Ett tryck utanför en länk vänder tillbaka kortet och
  döljer länkarna.
- Fallbilderna är 2880 px breda (515/278 kB). Omkodade till 1680 px blir de 201/114 kB.
- `fetchpriority` sitter på kortfotot i stället för LCP-bilden.
- Layoutläsningar under scroll (`maybeLoadHorai`, förvärmningen av Hōrai) kostar 2–3 ms per bildruta.
- Döda rester: 42 kB kommentarer och oanvända tillgångar.
- Sidtiteln är bara "ALUNIX".
- Den aktiva mobilradens h3 glider in under den sticky ramen.

## Förslag som kräver Antons beslut (rörs inte i R7)
- **Casebyte inne i pinnen** (heuristics): i dag krävs cirka 110 hjulsteg tillbaka till väljaren.
- **Ankarlänkar i topplisten** till process, case, pris och kontakt (heuristics): priset ligger i dag
  cirka 234 hjulsteg ned.
- **En gemensam reveal-profil** för hela sidan, 14 px och 620 ms, som spelas en gång (critic): i dag
  finns sex olika, och vissa döljs igen vid scroll uppåt.
- **Priset:** siffror i 64–96 px högerställda, plus en rad om moms och period (critic, heuristics).
- **Kontaktens tomma övre högra cell** (critic).
- **Riktig bokningslänk:** R7 använder `mailto:` med ämnesraden "Boka ett möte" tills en finns.
- **`<nav>`-landmärket** (öppen skuld sedan 2026-09-22).

## Skyddat, bekräftat av granskarna
- Heron: kortet som vänds över fogen.
- Tesrubrikens resning.
- Showcase-mekanismen: en pin, övertoning, räknare, mintspår och luppen.
- Stegtexterna efter R6b.
- Kortet som lämnas över i kontakten.
- Radie 0 och två typsnittsfamiljer.
- Motorns regler: `scrub:true`, pin skapad en gång, `pinSpacer` och `lagSmoothing(500,33)`.

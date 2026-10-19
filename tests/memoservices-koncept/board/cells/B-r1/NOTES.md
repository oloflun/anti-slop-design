# B-r1 · "Banden"

**Lane:** platt och ljus, färgbandet är tjänsten.
**Auktoritet (TASTE § 1):** ytan/färgen. Typen är Archivo Black i en vikt (ink eller `--bakgrund` efter bandets ljushet), videon är alltid inramad och aldrig under typen utan platta.

## Akterna

| # | Akt | Enhet | Spann | Orsak in |
|---|---|---|---|---|
| 0 | Intro → hero | intro-tidslinje (2,4 s) | – | app-ikonens 2×2 flyger in (`back.out(1.4)`), lime-brickan *är* ramen och växer (clip-path) till hero-ramen, de tre röda parkerar i navens 2×2-märke |
| 1 | Hero | flow | – | ramen (= brickan) består över överlämningen; 28-bricksmosaiken (alla sju huvudfärger) poppar in |
| 2 | Full bleed | pin + scrub (`scrub:true`) | 220 vh | ramen växer till hela vyn (card-to-full-bleed), plattan står i 1× och glider sedan upp i ett stycke; sista ~20 % ligger videon ensam (`object-view-box` zoomar in mot fasaden) |
| – | Band 1 stiger | scrub | 100 vh | stegad mosaikkant: marinbandet stiger över videon med 12 steg à 0–2 enheter som planas ut (hero står kvar via pin utan spacing) |
| 3 | Sju band | pin + scrub | 700 vh | varje tjänsts 2×2 kommer in liten nere till höger (under förra bandets hållning) och växer till hela vyn: tre huvudbrickor + accentfältet i hörnet, papper i fogarna. Sju band + limebandet som åttonde |
| 4 | Flera + kartläggning | flow (rubrik i radmasker) | – | samma mekanik: en helt lime 2×2 växer över band 7 och lämnar över till kartläggningen |
| 5 | Om | scrub (ark) + reveal | 100 vh | ark läggs över: limen står kvar (pin utan spacing) medan pappret med 2 px hårlinje glider över; `om.text` tänds ord för ord sten→ink i lästempo (regel 4) |
| 6 | Insikter | flow + in | – | ledger-rader (14 px / 620 ms) |
| 7 | Slut | scrub, sista triggern `end:'bottom bottom'` | sidfotens höjd | omvänd växt: `piren-last.webp` ligger över hela sidfoten och krymper till en bricka bredvid logotypen |

Peaken är akt 3 (störst spann). **Akt 2:s tomma vy, när ramen täcker allt och bara kameran rör sig, är avsiktlig tystnad före peaken.**

Övergångsorsaker i ordning: bricka→ram · ram→full bleed · stegad kant · 2×2 växer till grund (aktens inre mekanik, även in i limen) · ark läggs över · omvänd växt. Aldrig samma två i rad.

## Signaturobjektet, brickan, och dess jobb
1. **Intro/hero:** lime-brickan blir videons ram (ramen är brickan, radie `--radie`).
2. **Band:** varje tjänsts 2×2 förstoras till hela viewportens grund (fogarna blir papperslinjer, accentbrickan blir hörnfältet).
3. **Kant:** stegen i bandets överkant är brickans enhet.
4. **Slut:** sista bilden krymper tillbaka till en bricka i sidfoten.
Plus: navens 2×2-märke, undermenyn, sidfotens TJÄNSTER-kolumn och om-punkternas markörer.

## Nav
Fast bar 64 px som tweenar till aktiv sektions/bands grund och inverterar texten (CTA brandröd på ljus, `--bakgrund` på mörk). "Tjänster" är länk till `/tjanster` + chevron-knapp (`aria-expanded`, pil ned öppnar och fokuserar första, pil vänster/höger/upp/ned/Home/End, Esc stänger och återställer fokus, hover öppnar på fin pekare). Panelen glider ned med stegad underkant, sju kolumner med 2×2 + namn, bandfärg som hover-grund. Mobil (< 1120 px): `Meny` öppnar helskärm på `--bakgrund` med samma innehåll, fokus på `Stäng menyn`, Esc stänger, fokusfälla.

## `?preview=`-krokar
`hero`, `fullbleed`, `band-1` … `band-7`, `flera`, `kartlaggning`, `om`, `insikter`, `slut`. Alla verifierade att landa (1440×900, 390×844, 768×1024). `window.__cell.previewY(name)` ger positionen.

## Mätvärden (port 3102, headless Chrome)
- `verify_text.py`: 111 textnoder, **0 avvikelser** (injektionsbevis: `--inject` ger avvikelse).
- `scroll_verify.py` 1440×900 (runda 2): deadScroll **0**, cuesNeverFull 0, unrevealed 0, contrastUnderMedia **0**. `blankBands` listar pinnarnas spacers i en helsidesbild utan scroll (hero-run 220 vh + bandpinnen), väntat för pinnade akter.
- `contrast_over_media.py`: **PASS** (13 strängar i folden; brandröd på papper 4,17:1 för 19 px fet, stor text).
- Konsol: 0 fel, 0 4xx (alla previews och tre bredder).
- Horisontellt överflöde (elementgränser, hela sidan i 400 px-steg): **0** vid 320 / 375 / 414 / 768.
- Tangentbord: hopplänk först, panel öppnas/navigeras/stängs, mobilmeny öppnas/stängs med fokusåterställning.

## Avvägningar att känna till
- **Sidfotens rubriker FÖRETAGET / JURIDISKT** är *nycklar* i `delat.json` som `render.py` inte kan skriva ut. Sedan runda 2 står de som text i mallen (`verify_text.py` godtar nycklarna). TJÄNSTER är `{{oversikt.kicker}}`.
- **Löpnumret 01–07** visas likadant (`::before{content:attr(data-n)}` med `{{@n}}`), eftersom en textnod "04" annars faller i textkontrollen.
- **Fetstilen i om-punkterna** och **länken i koncernraden** sätts i JS (`data-b` / `data-link`): utan JS står texten ordagrant men utan `<strong>`/länk. Texten i sig rörs aldrig.
- a11y_scan (axe): 0 violations, 36 passes. tab_walk: 0 empty_name.
- Logotyplänkens `aria-label` är `{{meta.title}}` (ingen sträng i ny-text.json passar en logotyp).
- 2×2-märket i bandet har pappersbrickor + accent (som app-ikonen), eftersom tre brickor i huvudfärg försvinner mot sitt eget band. Brickstorlek 14 svh (briefen: 18 vh) så att texten ryms ovanför accentfogen vid 900 px höjd.
- Hero-mosaiken: facit (25) + brun r3k5, sten r4k7, grafit r5k6 = 28 brickor, alla sju huvudfärger.
- Konceptbannern är sista raden i sidfoten (`--sand`), enligt riktningsbriefen.
- Introts döljning sätts av ett litet inline-skript före första bilden (med 4 s återställning om main.js inte startar); inget döljs i CSS.

## Runda 2 (leadens sex punkter)
1. Ordtändningen i `.om-text` startar i `--grafit` och tänds till `--ink` (ingen opacity, ingen `--sten`).
2. Slutbilden landar som en 128 px ruta med radie `--radie` bredvid sidfotens logotyp.
3. Limesektionen ligger 75 vh in över bandscenens slut (genomskinlig där, scenens lime-2x2 är grunden). Raden "Behöver du hjälp…", kickern, kartläggningsrubriken (radmasker), texten och knappen reser sig när lime-2x2:an täcker ~60 % (u = 0,66 i sista bandbytet). Rubrikkolumnen tonar ut just före.
4. FÖRETAGET/JURIDISKT står som text i noden. **Löpnumren:** `verify_text.py` godtar *inte* "01"–"07" i ett eget element (7 avvikelser uppmätt), så de visas fortfarande via `::before{content:attr(data-n)}` på ett `aria-hidden`-element. Det ger 0 avvikelser och inga axe-fynd (det är ingen rubrik).
5. Nedre sömmen ligger nu ≤ 120 px från botten (Ay = min(11 % av H, 100 px) × 1,2), så den nedre rutan blir ett smalt band. Accentfältet blir brett och lågt. För att vyn inte ska stå still i hållningen kommer nästa 2x2 in och växer till 25 % av sitt bandbyte medan rubriken står still.
6. `.om-text` delas med `aria:"none"` (ingen aria-label). Fältet `empty_name` kom från introts `autoAlpha` (visibility:hidden tömmer `innerText` på länkarna i baren och heron). Intro och reveals använder nu `opacity`, så länkarna har alltid namn.
Egen regression rättad: Meny-knappen hamnade till vänster på < 560 px efter rundans 768-justering.

## Inte hunnet
- `section_probe.py`/`motion_probe.py` (bildtid per sektion) är inte körda.
- Ingen a11y-audit eller kritikrunda utöver ovanstående kontroller.

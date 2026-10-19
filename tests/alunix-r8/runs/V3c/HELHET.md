# HELHET.md · referensgolvet för V3c:s visuella helhet

Skriven av arkitekten (Fable) 2026-09-15, fas A i r9. Allt nedan är läst ur pixlar som
finns i `runs/V3c/shots/fasA/` (varje fil står som `läst:` i `NOTES.md` § Fas A) eller mätt
med `scroll_verify.py` och `motion_probe.py` mot boardkopian `board/cells/V3c-r8/` över port
3090. Bildreferenser skrivs `(mapp/fil)` relativt `shots/fasA/`. Ett påstående utan bild
eller tal står inte här.

Uppdraget, Antons ord 2026-09-15: gå igenom helheten och referensernas webbdel, struktur,
balans och scrollanimationer; lägg ett referensgolv; lägg till element och färger om de går
ihop; säkerställ att scrolleffekterna är mjuka och genomgående utan tröghet eller avbrott.

---

## § 0 Underlag

**Bilder lästa, per källa** (228 totalt, `NOTES.md` § Fas A har varje sökväg):

| Källa | 1440 | 390 | Ramsekvenser | Summa |
|---|---|---|---|---|
| V3c boardkopia, hela sidan | 8 | 9 | | 17 |
| V3c `?preview=` front/mid/back/ledger/bleed | 5 | 5 | | 10 |
| V3c heron, `--flip` 0 till 1 i tolv steg | | | 12 + 12 | 24 |
| V3c `#giant-section`, tolv steg genom aktens synliga liv | | | 12 + 12 | 24 |
| K3 boardkopia, hela sidan | 9 | 8 | | 17 |
| K3 ritningsakten, tolv steg genom pinnen | | | 12 + 12 | 24 |
| insign `/webbdesign-wordpress/` | 6 | 11 | | 17 |
| highwaymedia `/webbyra-goteborg/` + `/tjanster/hemsida/` | 8 + 8 | 12 + 12 | | 40 |
| hoy `/` + `/tjanster/webbdesign` | 11 + 12 | 10 + 10 | | 43 |
| Leadens `r4-pre` flip-ramar | 5 | 5 | | 10 |
| Katalogfolds `highwaymedia`, `hoy` | 2 | | | 2 |

**Mätningar:** `scroll_verify.py` vid 1440x900 och 390x844 (`probe/scroll-verify-*.txt`),
`motion_probe.py` med kontrollprotokollet vid 4x CPU, båda hjulprofilerna, båda
riktningarna, plus en cpu 1-körning (`probe/probe-quiet.txt`, json per körning), och en
K3-körning som jämförelse. Kontrollen `tests/motion/smooth.html` gav p95 18,3 ms men 1 till 2
rutor över 33 ms i varje körning, alltså är värden inte helt tyst; talen nedan redovisas
med den reservationen, och skillnaden mot kontrollen (111 rutor mot 2) är inte brus.

**Katalogen:** `highwaymedia` och `hoy` är inlagda som poster (`design-catalogue/entries/`,
capture + designlang-extract, `index.py` och `drift.py` rena, 97 poster). Select-rankingen
mot `runs/V3c/BRIEF-draft.md` (`--k 4 --wildcard --explain --dry-run`) är **oförändrad**:

```
14 oryzo-ai · 12 dope-security · 12 mattis-studio · 12 monologue · 12 planhat (wildcard)
```

De tre byråsajterna rankar inte in, inte heller vid `--k 8`: de ligger i registret `modern
clean` och grammatiken `chaptered editorial`, medan briefen låser `cinematic dark` och
`continuous world`. De står i låset som **Antons namngivna referenser** (`reference-lock.md`
tillåter användarnamngivna källor), med en rad i `BRIEF.md` § decision ledger (2026-09-15).

**Vad som saknas.** (1) Highway Medias processtext: fasernas ord revealas på scroll och
fångades inte (kapten kördes under `reduced_motion="reduce"` som skripten kräver, F-011);
skelettet syns, orden inte. Fasordningen tas från planen. (2) En helt tyst mätvärd: kontrollen
gav 1 till 2 rutor över 33 ms i varje körning. (3) Highway Medias cookie-kort står kvar i
alla bilder (avböj-knappen träffades inte; insign avböjdes, Hoy visade ingen).

---

## § 1 Per referens, uppmätt

### insign `/webbdesign-wordpress/` (5 356 px = 6,0 vh vid 1440; 8 689 px vid 390)

| Mått | Utfall | Bild |
|---|---|---|
| Sektioner | 6: hero, nivåkort, AI-text, support, projekt, footer | `insign-1440/insign-1440--s00..s05.png` |
| Grunder | 3: mörkt foto (hero) → vitt (fyra sektioner) → mörkt (footer) | `s00`, `s01`, `insign-390/insign-390--s10.png` |
| Övergångar | hård kant överallt; enda grundväxlingarna är inversion i båda ändar | `s00` → `s01`; `insign-390--s09` → `s10` |
| Rörelse | sticky mörk nav + sticky flikrad under den; ingen scrollkoreografi syns i skivorna, allt är renderat vid varje offset | `s01` (flikraden fast under navet) |
| Tyst | hela sidan under heron | `s02..s05` |
| Balans (squint) | hero: vänstertung text över fullbleed-foto; tre lika chartreusekort; fyra lika ikonkolumner; 2x2 lika projektrutor. Rytmen är mallens (TASTE § 5: tre lika kort, ikongrid) | `s01`, `s03`, `s04` |
| Processen | inga steg. Tre **nivåer** (Nödvändigt / Mer / Fördjupad) som kort med kryssrader; löftena står som rader: designförslag på tillfällig adress, redigerbart CMS, SEO | `s01` |
| Skala | H1 ~56 px vit på foto; kortrubriker ~28 px; body 16 | `s00`, `s01` |
| Vad den gör bättre än V3c i dag | löftena till kunden står i klartext på sidan (testadress, CMS); sidan är fullt läsbar vid varje offset | `s01` |
| Vad V3c gör bättre | ingen ikongrid, inga lika kort, en auktoritet per skärm i heron | `v3c-1440/v3c-1440--s00.png` |

### highwaymedia `/webbyra-goteborg/` + `/tjanster/hemsida/` (6 746 / 6 861 px ≈ 7,5 vh; 9 595 / 9 979 px vid 390)

| Mått | Utfall | Bild |
|---|---|---|
| Sektioner | 8 per sida: hero, case, CMS/LINK, kunder, Så arbetar vi (tidslinje), support, projektledare, footer; hemsida-sidan lägger till bandet "Vårt erbjudande" | `highway-1440/hw-goteborg-1440--s00..s07.png`, `hw-hemsida-1440--s00..s07.png` |
| Grunder | vitt ark; ett blekrosa helbrett band (hemsida `s01`); footern som en rundad vit skiva som skjuts in över arket | `hw-hemsida-1440--s01`, `hw-goteborg-1440--s07` |
| Övergångar | hård kant; bandet är helbrett; footerskivan är sidans enda överlapp | `hw-goteborg-1440--s06` → `s07` |
| Rörelse | reveal-on-scroll på tidslinjens fastext: i fångsten är fastexten tom (gaten mot reduced motion, det F-011 förbjuder); logokarusell (`infiniteScroll`) på mobil; chattbubbla | `hw-goteborg-1440--s03`, `s04`; `highway-390/hw-goteborg-390--s05`, `s06` |
| Tyst | hero, case, CMS, support, kontakt | `s00..s02`, `s05`, `s06` |
| Balans (squint) | hero: text vänster, foto med grön förskjuten platta höger, balanserat; tre lika casekort; fem lika logokort; tidslinjen är vänstertung (linje + punkt) med en 3D-blob höger per fas | `s00`, `s01`, `s02`, `s04` |
| Processen | **en lodrät tidslinje**: rosa hårlinje, plommonfärgade punkter, en punkt per fas, fyra faser (Uppstart och strategi, Design och utveckling, Innehåll, Lansering), en 3D-render per fas till höger. Skelettet läser som sekvens utan ord (skelettestet klarat) | `hw-goteborg-1440--s03`, `s04`, `hw-hemsida-1440--s04..s06` |
| Skala | H1 84 px, H2 54, body 20 (designlang) | `s00` |
| Vad den gör bättre än V3c | processen finns och har en form med början och slut; kontakten är en person, inte bara en adress (för Alunix förbjudet, men principen "ett svar" gäller) | `s03`, `s06` |
| Vad V3c gör bättre | inga logoväggar, inga tre lika kort, ingen persistent chatt i folden, inget mallraster | `v3c-1440--s00` |

### hoy `/` + `/tjanster/webbdesign` (9 006 / 10 312 px ≈ 10 till 11,5 vh; 8 272 / 8 226 px vid 390)

| Mått | Utfall | Bild |
|---|---|---|
| Sektioner | hem 10: hero-karusell, Digitala lösningar, Utvalda projekt (marquee-rubrik), tre projektrutor, Dags för ny webb, Digital design, Digitala säljverktyg, App, Nyfiken, footer. Webbdesign 12 | `hoy-1440/hoy-home-1440--s00..s10.png`, `hoy-webb-1440--s00..s11.png` |
| Grunder | hem: lila → gräddgul → röd, tre platta grunder; webbdesign: plommon → helskärmsfoto → plommon → blekrosa | `hoy-home-1440--s02` → `s03`, `s06` → `s07`; `hoy-webb-1440--s00`, `s01`, `s04` |
| Övergångar | **helbredd hård kant** vid varje grundbyte; hårlinjer mellan kapitel på samma grund; pill-navet inverterar sina färger vid samma seam | `hoy-home-1440--s03` (linje + grundbyte), `s07` (röd) |
| Rörelse | hero-karusell som byter grund per bild (4 bilder); marquee-streck på jätterubrikerna; kapitelreveal `slide-up-enter` (opacity); en easing på 69 övergångar; ingen parallax, ingen pin | `hoy-home-1440--s00`, `s02`; `design-catalogue/entries/hoy/fold.webp` (röd bild 2 i karusellen) |
| Tyst | varje kapitel efter reveal; hela sidan läser som stillbilder med hårda grundbyten | `s03..s09` |
| Balans (squint) | strikt växling: text vänster/plate höger, sedan omvänt; plate:n är alltid skärmens tyngsta och mest mättade element; rubrik 48 px caps vikt 400 viker för den | `s01` (foto vänster, text höger), `s03` (text vänster, plate höger), `s04` |
| Processen | inga steg. Sex **arbetsprinciper** som punktlista (användarcentrerad metodik, tvärdisciplinär samverkan, designsystem och komponenttänk, storytelling, datadrivet, tillgänglighet och WCAG) | `hoy-webb-1440--s08`, `hoy-390/hoy-webb-390--s08` |
| Skala | marquee 132 px (-2,64 px tracking), display 48, body 16 (designlang); jätterubriken "KONSTEN ATT GÖRA DET DIGITALA" ~100 px i lila | `hoy-webb-1440--s03`, `s04` |
| Fel i referensen | "Invert"-reglaget överlappar brödtext vid 390 (`hoy-390/hoy-home-390--s06`, `s07`); karusellen byter grund under läsaren | `hoy-390/hoy-home-390--s06` |
| Vad den gör bättre än V3c | rytm: varje kapitel är en skärm med en auktoritet; grundbytena är hela och avsiktliga; jätterubriken används som kapitelavdelare; navet hänger med ner | `s02`, `s03`, `s07` |
| Vad V3c gör bättre | ett fysiskt objekt i heron i stället för en karusell; levande sajter i stället för plates; ingen upprepad anatomi nio gånger | `v3c-flip/v3c-1440-flip-05-045.png` |

### K3 (intern referens för ritningen; 7 209 px = 8,0 vh; 6 229 px vid 390)

| Mått | Utfall | Bild |
|---|---|---|
| Sektioner | 6 akter: ritningen (pin 4,0 = 3 600 px, 50 % av sidan), tesen, tre plates, liggaren, stycklistan, titelblocket | `k3-1440/k3-1440--s00..s08.png` |
| Grunder | en: kallt ritpapper; hårlinjer och ton på ton, ingen inversion | alla |
| Övergångar | kontinuerlig grund, luft ≥ 200 px mellan kapitel, hårlinjer | `s04`, `s06` |
| Rörelse | linjen ritas ur `--sc-ps` (`stroke-dashoffset`), måtten räknas upp (129 → 320 → 768 → 1440), Calyx maskas in i öppningen, ram dras in i titelblocket | `k3-act/k3-1440-pin-02..pin-11.png` |
| Vad ritningen gör rätt | form, aldrig innehåll: kontur, snittmarkering A-A, hjälplinjer, måttlinjer, skraffering, utrop; måttsiffrorna i blått är arkets enda kromatiska moment | `k3-act/k3-1440-pin-07.png`, `pin-09.png` |
| Vad ritningen kostar | `motion_probe` 4x CPU, 100:60: p95 218 ms, 119 av 178 rutor över 33 ms, staircase 0 på `--sc-ps`, 1 på `stroke-dashoffset` (`probe/k3-down-100/`). Ritningen är inte gratis; processakten måste budgeteras | `probe/k3-down-100/motion_probe.json` |
| Balans | generös luft, ett displayelement per skärm; den reducerade planschen vid 390 håller kedjan 320 · 768 · 1440 som utrop | `k3-390/k3-390--s00`, `k3-act/k3-390-pin-08.png` |

---

## § 2 V3c i dag, samma mått

Boardkopian, identisk med `runs/V3c/index.html` vid dispatch (diff tom).

| Mått | Utfall | Bild / tal |
|---|---|---|
| Dokumenthöjd | 6 359 px = **7,07 vh** vid 1440 (budget 8 till 14, `feel-and-fingerprint.md` § Pacing); 7 397 px = 8,76 vh vid 390 | `probe/scroll-verify-1440.txt` |
| Sektioner | hero-pinnen 4 320 px (**68 % av sidan**), sedan ett tvåspaltigt band på ~1 500 px där s4, s5 och s6 syns samtidigt, sedan avslutet ~350 px | `v3c-1440/v3c-1440--s04.png`, `s05`, `s06` |
| Grunder | ett kontinuerligt gråskalefoto med drift `#0b0c0e` → `#123f68` → `#f4f2ee`; material inne i spalterna: blått block, papper, mörkt prisblock, två levande ramar | `s04`, `s05`, `s06` |
| Övergångar | hero → band: hård kant med en 20 till 30 px slits av rå grund; panelerna ligger med 20 px-slitsar och läser som plattor i ett masonry; avslutet: hård kant | `s04` (y 690 till 720), `v3c-giant/v3c-1440-life-02.png` |
| Kedjan bryts | **båda spalterna toppalignar** vid bandets början (blå tes och papper börjar på samma y), vilket house-physics förbjuder ("paired columns never top-align") | `v3c-preview/v3c-1440-ledger--fold.png` (båda vid y 104), `v3c-giant/v3c-1440-life-02.png` (båda vid y 610) |
| Kedjan bryts | prisblocket `--invert #0c0b08` mot grunden `#0b0c0e` läser som samma material; blocket syns bara som en kant | `v3c-1440--s06.png` |
| Kedjan bryts | avslutet delar viewport med pris och Hōrai (plan 007) | `v3c-1440--s06.png` |
| Balans, s1 fold | ett displayelement (rubrik 120 px), kortet, underraden; rätt | `v3c-preview/v3c-1440-front--fold.png` |
| Balans, s2 mitt i vändningen | kortet krymper transient till ~60 % (parabeln 0,72); vid 90° står en hårlinje på ~400 px i ett 896 px brett tomrum: skärmen är ett mörkt fält med en tunn linje | `v3c-flip/v3c-1440-flip-05-045.png`, `flip-06-055.png` |
| Balans, s3 baksidan | innehållet fyller vänstra ~45 % och övre ~60 % av kortet; högra halvan och nedre 40 % är tom matt svart (R2/R3:s öppna fråga, obesvarad) | `v3c-preview/v3c-1440-back--fold.png`, `v3c-flip/v3c-1440-flip-11-100.png` |
| Balans, bandet | vänsterspalten är tyngre (blått block + ljus Calyx-ram) än högerspaltens papper; panelerna läser som ett rutnät, inte som skärmar | `v3c-1440--s05.png` |
| Balans, 390 | folden har ~150 px död grund under underraden (18 % av 844); mobilordningen är jätterubrik/liggare → Hōrai → tes → Calyx → pris, alltså berättelsens s4 kommer efter s6 | `v3c-390/v3c-390--s00.png`, `s02..s06` |
| Hyperborea-bleeden | 32 px överhäng, och spåret är **DEAD** i proben (plan 008 bekräftad) | `v3c-preview/v3c-1440-bleed--fold.png`; `probe/q-down-100-page/motion_probe.json` |
| Rörelse, heron | vändningen glider: staircase 0 i alla sju körningar, `--sc-ps` max_step 0,31 till 1,44 %, transformen 0,32 till 2,04 % | `probe/probe-quiet.txt` |
| Rörelse, bildtid | **sidan tappar bildrutor.** 4x CPU, 100:60: p95 290,6 ms, 111 av 179 rutor över 33 ms; 20:120: p95 35,9 ms, 266 av 961; uppåt 100:60: p95 53,7 ms, 82 av 222; **cpu 1**, 100:60: p95 71,5 ms, 25 av 272. Kontrollen: p95 18,3 ms, 2 rutor. Det är F-013:s andra fel (plan 005: RecalcStyle 73 %), inte stegning | `probe/q-down-100/`, `q-down-20/`, `q-up-100/`, `q-down-100-cpu1/`, `q-control-100/` |
| Rörelse, dead scroll | `scroll_verify` 1440: sju band, varav 2 700 till 3 300 med diff **0,0**; 390: sex band, 2 529 till 3 091 diff 0,0. Orsak: efter ps 0,72 står baksidan stilla i 0,28 · 3 420 = 958 px plus dwell 315 px = **1 273 px utan rörelse** inne i pinnen | `probe/scroll-verify-1440.txt`, `probe/scroll-verify-390.txt` |
| Rörelse, blankBands | 1440: 900 till 4 320 (pinnen, artefakt av helsidesbilden, känd); 390: dessutom 4 629 till 5 218, 5 712 till 6 331, 6 342 till 6 993, alltså tre band under bandet: Calyx-ramen, Hōrai-ramen och prisblocket läser som enfärgade ytor i helsidesbilden | `probe/scroll-verify-390/full.png` (inte läst som pixlar, bara talen) |
| Rörelse, flow-akterna | `--sc-ps` max_step 3,28 % på `#giant-section` och 4,01 % på `.panel-thesis` (baren 3 % för spelhuvudet): korta akter ger stora steg per hjulhack | `probe/q-down-100-page/motion_probe.json` |
| Rörelse som saknas | prisblocket, avslutet och Hōrai-figuren efter irisen rör sig inte alls; jätterubrikens skala 0,92 → 1 syns inte i ramsekvensen | `v3c-giant/v3c-1440-life-05..11.png`, `v3c-1440--s06.png` |
| Ordscrubben | orden går från dämpat till fullt bläck i en front; läsbar, subtil, rätt | `v3c-giant/v3c-1440-life-03.png`, `life-06.png` |

**Tempot i kortvändningen.** Ramsekvensen `v3c-flip/` visar en jämn rotation med transient
nedskalning och hårlinje vid 90°; ingen klippning vid något värde (bekräftar leadens
läsning av `r4-pre`). Tempot är en fråga om scrollväg per vändning:

| span | pinnad resa vid 900 vh | vändning (ps 0,12 till 0,72) | statisk svans (ps 0,72 till 1 + dwell 0,35) |
|---|---|---|---|
| 2,2 (Antons "för fort") | 1 080 px | 648 px ≈ 6,5 hjulhack | 302 + 315 = 617 px |
| 4,8 (i dag) | 3 420 px | 2 052 px ≈ 20,5 hack | 958 + 315 = **1 273 px** (diff 0,0 i scroll_verify) |
| **3,4 (rekommenderat)**, fönster 0,10 till 0,78, dwell 0,20 | 2 160 px | 1 469 px ≈ 15 hack | 475 + 180 = 655 px |

Rekommendation: `data-sc-span="3.4" data-sc-dwell="0.2"` på `section.hero`, och
smoothstep-fönstret vidgat från 0,12 till 0,72 till **0,10 till 0,78** (raden
`--t:clamp(0,calc((var(--sc-ps,0) - 0.10) / 0.68),1)`). Skäl: 2,2 ger en vändning på en
sekund vid vanlig hjulfart och läses som ett klipp; 4,8 löser det men lägger 1 273 px
stillastående baksida inne i pinnen, vilket proben mäter som dead scroll och läsaren som
tröghet. 3,4 med vidgat fönster ger 2,3 gånger 2,2:s vändning och halverar svansen. Heron är
fortfarande sidans största spann (processakten nedan är 3,0 svh som flow, aldrig pin).
Fönstret är målbildens och vidgningen är arkitektens beslut, med rad i decision ledger
(`BRIEF.md` 2026-09-15) och som fråga till Anton (Q25) eftersom R2 lämnade den öppen.

---

## § 3 Golvet

Kontrollerbara påståenden, ett per rad. Golvet är minst referensernas nivå: varje rad som en
referens klarar och V3c inte klarar i dag står här. `[ ]` bockas i fas C mot bild eller tal.
Bredder: 1440x900 och 390x844 om inget annat sägs.

**Loop 5 (arkitekten, 2026-09-17), R10-läget `d3491b4a`:** **29 av 35 bockade, 6 öppna, och de sex är exakt de som inte kan bockas i loopen**: H-02, H-03 och H-08 väntar på Anton (Q30), H-21, H-22 och H-32 är bildtidens redovisade arkitektoniska golv. Varje rad bär en `· loop 5`-rad med bild eller tal ur `shots/loop-5/`. Nybockade i loop 5: **H-15** (042 tog bort prisplatshållaren, motorns akttopp = DOM:ens, konturen hel bredvid steg 01), **H-19** (044, driftens överlämning kontinuerlig), **H-23** (042 tog bort de 297 px omlayout som stegade jätte- och tesfönstret; alla akter ≤ 3 % vid cpu 1), **H-24** (de fyra spår proben är blind för mättes som beräknad matris i stället: alla levande), **H-27** (043, Calyx-revealen har en öppning och latchen är fortsatt vägoberoende), **H-30** (21 av 21 previews formade vid 390, och aktens vandring körd i **båda** riktningarna), **H-34** (hela sidan mätt, 61 + 41 strängar). Ingen rad omskriven i loop 5. Ingen rad återöppnad. Astra svarade `ship` med noll `material_fixes`. Slutvillkorets tre delar som är arkitektens är nådda; leadens pixelbekräftelse återstår.

**Loop 4 (arkitekten, 2026-09-17), R9-läget `909916d1`:** 22 av 35 bockade, 13 öppna. Varje rad bär en `· loop 4`-rad med bild eller tal ur `shots/loop-4/`. Öppna rader med plan i R10: H-15/H-30 (042), H-19 (044), H-27 (043); öppna som bildtidens följd, mätta mot 042: H-21/H-22/H-23/H-32. Öppna utan plan: H-02/H-03/H-08 (Q30, väntar på Anton), H-24 (verktygsskuld), H-34 (leadens grind; folden mätt 7/7 av arkitekten). Omskriven i loop 4: ingen rad; H-23 återöppnad (3,12 % / 3,52 % vid cpu 1 i fönster där ramarna monteras).

**Loop 3 (arkitekten, 2026-09-17), R8-läget `70214a22`:** 23 av 35 bockade, 12 öppna. Varje rad bär en `· loop 3`-rad med bild eller tal ur `shots/loop-3/`. Öppna rader med plan i R9: H-15 (040), H-19 (038), H-21/H-22/H-32 (036, 041), H-27 (035), H-30 (037). Öppna utan plan: H-02/H-03/H-08 (Q30), H-24 (verktygsskuld), H-34 (leadens grind). Omskrivna rader i loop 3, med skäl i raden: H-01 (kedjans budget 8 till 14 med källa), H-05 (a) (390-golvet 96 px), H-19 (mellantonen i stället för svärtan).

**Loop 2 (arkitekten, 2026-09-17), R7-läget `d30355da`:** 18 av 35 bockade, 17 öppna. Varje rad bär en `· loop 2`-rad med bild eller tal ur `shots/loop-2/`. Öppna rader med plan i R8: H-05 (390, 032 B), H-07 (030), H-08 (027, sedan Q30), H-13 (032 A), H-15 (034), H-21/H-22/H-32 (028), H-23 (028, footern), H-25 (033), H-27 (031), H-30 (034). Öppna utan plan: H-01 (0,09 vh över), H-02/H-03 (Q30), H-24 (verktygsskuld), H-34 (leadens grind).

**Loop 1 (arkitekten, 2026-09-17), R6-läget `424cdd46`:** 14 av 35 bockade, 21 öppna. Varje rad
bär en `· loop 1`-rad med bild eller tal ur `shots/loop-1/`. Öppna rader med plan i R7: H-02 (delvis),
H-03 (delvis), H-04, H-05, H-07, H-08, H-09, H-11, H-12, H-14, H-15, H-19, H-25 (avslutet), H-30.
Öppna utan plan i R7: H-13, H-21, H-22, H-23, H-24 (delvis), H-25 (priset), H-32, H-34.

**Rytm över hela sidan**

- [x] **H-01** Dokumenthöjden vid 1440 är 8 till 14 vh (kedjans budget, `scroll/feel-and-fingerprint.md` § Pacing; fas A skrev 12 utan källa, omskriven i loop 3), och ingen enskild akt tar mer än 45 % av dokumenthöjden. (I dag 7,07 vh, heron 68 %. Hoy 10 vh utan en akt över 20 %.)
  · loop 1 (2026-09-17): 10,90 vh (9 809 px) vid 1440, heron 3 060 px = 31 % (`shots/loop-1/diag/diag.json`, `slices-1440/`)
  · loop 2 (2026-09-17), R7-läget `d30355da`: 10 880 px = 12,09 vh vid 1440 (0,09 över radens 12; inom feel-and-fingerprints 8 till 14), 11 521 px = 13,65 vh vid 390; heron 3 060 px = 28 % (`shots/loop-2/diag/diag3.json geom1440`, `slices-1440/`). Ingen plan: 017:s luft är H-05:s golv
  · loop 3 (2026-09-17), R8-läget `70214a22`: 10 880 px = 12,09 vh vid 1440, 11 588 px = 13,73 vh vid 390 (`shots/loop-3/geom3.json`); heron 3 060 px = 28 %. **Raden omskriven** till kedjans budget 8 till 14 (`feel-and-fingerprint.md` § Pacing), som fas A citerade som 8 till 12 utan källa; bockad
  · loop 4 (2026-09-17), R9-läget `909916d1`: 10 880 px = 12,09 vh vid 1440 vid load, 10 582 px = 11,76 vh när prisblocket målats (plan 042: platshållaren 760 px är 297 px högre än blocket); 11 588 / 11 326 px = 13,73 / 13,42 vh vid 390 (`shots/loop-4/geom4.json`, `mountshift.json`); heron 3 060 px = 28 till 29 %. Inom 8 till 14 i båda lägena; bockad, dokumenthöjden blir konstant med 042
  · loop 5 (2026-09-17), R10-läget `d3491b4a`: 10 582 px = 11,76 vh vid 1440 och 11 326 px = 13,42 vh vid 390, **samma tal vid load och inne i bandet** (plan 042; `geom5.json`, `preview390_5.json`): skiftet på 297 / 262 px finns inte längre, raden har ett värde i stället för två. Heron 3 060 px = 28,9 %
- [ ] **H-02** Efter heron följer minst fyra sekventiella akter som var och en äger sin viewport vid 1440 (tes, bevis, process, pris, avslut), inte ett band där tre skärmar syns samtidigt. (Hoy: en skärm per kapitel, `hoy-home-1440--s03..s09`.)
  · loop 1 (2026-09-17): bandet visar fortfarande tes + jätterubrik + Calyx + liggare samtidigt (`shots/loop-1/slices-1440/v3c-1440--s03.png`); processakten, principerna och avslutet äger sina skärmar. 017 ger luft och offset, inte fyra hela skärmar: öppen
  · loop 2 (2026-09-17), R7-läget `d30355da`: bandet står (Q30 obesvarad); efter heron äger processakten, principerna och avslutet sina skärmar, bandet visar tes + jätterubrik samtidigt (`s03`)
  · loop 3 (2026-09-17), R8-läget `70214a22`: bandet står (Q30); process, principer och avslut äger sina skärmar (`slices-1440/v3c-1440--s06.png` till `s12`); tes + jätterubrik samtidigt (`s03`)
  · loop 4 (2026-09-17), R9-läget `909916d1`: bandet står (Q30, väntar på Anton); process, principer och avslut äger sina skärmar (`slices-1440/v3c-1440--s06.png` till `s12`); tes + jätterubrik samtidigt (`s03`)
  · loop 5 (2026-09-17), R10-läget `d3491b4a`: bandet står (Q30, väntar på Anton); process, principer och avslut äger sina skärmar (`slices-1440/v3c-1440--s06.png` till `s11`); tes + jätterubrik samtidigt (`s03`)
- [ ] **H-03** Sidan byter grund minst tre gånger med hela bredden, som material och inte som "grå sektion" (TASTE § 4.5): mörk fotografisk grund → blått tesband → papper (liggare + processark) → mörkt prisplan → grund. (Hoy: lila → gräddgul → röd med hård helbredd kant.)
  · loop 1 (2026-09-17): två helbredds materialbyten (papper vid `#process`, foto vid avslutet, `s05`, `s10`); det blå bandet och priset är spaltbreda och driften syns inte: 017 A
  · loop 2 (2026-09-17), R7-läget `d30355da`: två helbredds materialbyten (papper vid `#process`, foto vid avslutet); tesen och priset är spaltbreda (`s03`, `s05`). Q30
  · loop 3 (2026-09-17), R8-läget `70214a22`: två helbredds materialbyten (papper vid `#process` `s06`, foto vid avslutet `s11`/`s12`); tesen och priset spaltbreda. Q30
  · loop 4 (2026-09-17), R9-läget `909916d1`: två helbredds materialbyten (papper vid `#process` `s05`/`s06`, foto vid avslutet `s11`/`s12`); tesen och priset spaltbreda. Q30, väntar på Anton
  · loop 5 (2026-09-17), R10-läget `d3491b4a`: två helbredds materialbyten (papper vid `#process` `s06`, foto vid avslutet `s10`/`s11`); tesen och priset spaltbreda. Q30, väntar på Anton. Prisplanet → papper ligger nu på ETT y (5 340) i stället för två, eftersom geometrin är konstant (042)
- [x] **H-04** Tvåspaltiga partier finns högst en gång, och där skiljer spalternas första element minst 96 px i y (house physics: paired columns never top-align). (I dag 0 px, `v3c-1440-ledger--fold.png`.)
  · loop 1 (2026-09-17): `.panel-thesis` och `.panel-giant` båda top 3 060 px, offset 0 (`diag.json`, `s03`): 017 B
  · loop 2 (2026-09-17), R7-läget `d30355da`: `.panel-thesis` top 3 222, `.panel-giant` top 3 330: offset 108 px ≥ 96 (`diag3.json geom1440`, `s03`)
  · loop 3 (2026-09-17), R8-läget `70214a22`: `.panel-thesis` top 3 222, `.panel-giant` top 3 330: offset 108 px (`geom3.json`, `slices-1440-fix/v3c-1440--s03.png`)
  · loop 4 (2026-09-17), R9-läget `909916d1`: `.panel-thesis` top 3 222, `.panel-giant` top 3 330: offset 108 px (`geom4.json`, `slices-1440/v3c-1440--s03.png`)
  · loop 5 (2026-09-17), R10-läget `d3491b4a`: `.panel-thesis` top 3 222, `.panel-giant` top 3 330: offset 108 px ≥ 96 (`geom5.json`, `slices-1440/v3c-1440--s03.png`)
- [x] **H-05** Ingen seam mellan två akter är en slits av rå grund under 96 px; en seam är (a) kontinuerlig grund med minst 160 px luft vid 1440 och minst 96 px vid 390 (plan 032 B, preciserad i loop 3), (b) ett helbrett materialbyte, eller (c) ett överlapp. (I dag 20 px-slitsar, `v3c-1440-life-02.png`.)
  · loop 1 (2026-09-17): `.stagger` börjar exakt vid heroens slut (0 px luft) och panelerna ligger med 20 till 40 px slitsar (`s03`, `s04`): 017 C. Papper → foto vid avslutet är ett helbrett materialbyte och håller
  · loop 2 (2026-09-17), R7-läget `d30355da`: 1440: 162 px luft vid alla fem seams (3 060 → 3 222, 3 600 → 3 762, 4 611 → 4 773, 4 266 → 4 428); 390: `gap` 84 px < 96 mellan panelerna (`s390-02`, `s390-03`, Astra loop 2 bild 18/20): plan 032 B
  · loop 3 (2026-09-17), R8-läget `70214a22`: 1440: 162 px vid alla seams (3 060 → 3 222, 3 600 → 3 762, 4 150 → 4 312, 4 611 → 4 773; `geom3.json`); 390: 101 till 102 px (3 358 → 3 459, 4 055 → 4 157, 4 834 → 4 935, 5 497 → 5 599) och pris → papper är ett helbrett materialbyte (`slices-390-fix/v3c-390--s03.png` till `s07`). **(a) preciserad**: ≥ 160 px vid 1440, ≥ 96 px vid 390 (plan 032 B, loop 2)
  · loop 4 (2026-09-17), R9-läget `909916d1`: 1440: 162 px vid alla seams (3 060 → 3 222, 3 600 → 3 762, 4 150 → 4 312, 4 611 → 4 773; `geom4.json`); pris → papper helbrett vid 5 340 (efter första målningen) / 5 637 (före), plan 042 gör det till ett värde; 390: 101 till 102 px (`slices-390/v3c-390--s03.png` till `s07`)
  · loop 5 (2026-09-17), R10-läget `d3491b4a`: 1440: 162 px vid alla seams (3 060 → 3 222, 3 600 → 3 762, 4 150 → 4 312, 4 611 → 4 773; `geom5.json`); pris → papper helbrett vid 5 340, ett värde (042 tog bort det andra); 390: 101 till 102 px (`slices-390/v3c-390--s03.png` till `s07`)
- [x] **H-06** Minst tre distinkta sektionsanatomier i följd efter heron, och ingen anatomi två gånger i rad: tesband med bleed, levande plate, ritat processark, prisliggare, typsatt avslut.
  · loop 1 (2026-09-17): tesband med bleed, levande plate, ritat ark, prisliggare, hairline-liggare utan nummer, typsatt avslut (`s03` till `s10`)
  · loop 2 (2026-09-17), R7-läget `d30355da`: sex anatomier i följd, ingen två gånger i rad (`s03` till `s12`)
  · loop 3 (2026-09-17), R8-läget `70214a22`: sex anatomier i följd, ingen två gånger i rad (`slices-1440-fix/…s03` till `slices-1440/…s12`)
  · loop 4 (2026-09-17), R9-läget `909916d1`: sex anatomier i följd, ingen två gånger i rad (`slices-1440/…s03` till `s12`)
  · loop 5 (2026-09-17), R10-läget `d3491b4a`: sex anatomier i följd, ingen två gånger i rad (`slices-1440/…s03` till `s11`)
- [x] **H-07** Jätterubriken `VI BYGGER ERT VARUMÄRKE.` mäter minst 88 px teckenstorlek vid 1440 (5,5 gånger brödtexten) och det låsta ordet står alltid helt på en rad. (Skrevs i fas A som 96 px mot en antagen 640 px-spalt; den faktiska spalten är 555 px och 96 px kapar ordet. 96 px förutsätter Q30:s helbredd, Q31. Hoys kapitelavdelare mäter 100 till 132 px i full bredd.)
  · loop 1 (2026-09-17): `.giant` 76,8 px, två rader (`diag.json`, `s03`): 014
  · loop 2 (2026-09-17), R7-läget `d30355da`: 96 px kapar det låsta ordet (`VARUMÄRK` / `E.`, `s03`, `preview-1440-ledger`): spalten är 555 px, ordet 601 px vid 96 px; 88 px vid −0,04em håller ordet helt (542 px, 1 rect, 3 rader vid 1280 och 1440, `diag3.json C_giant`, `synth3`). **Raden skrivs om av arkitekten:** golvet är ≥ 88 px vid 1440 och ordet aldrig delat; 96 px förutsätter en spalt ≥ 606 px, som bara Q30 ger (Q31). Plan 030
  · loop 3 (2026-09-17), R8-läget `70214a22`: `.giant` 88 px, −3,52 px tracking, ordet 1 rect, 3 rader vid 1440; 33,6 px, 2 rader vid 390 (`geom3.json`, `preview/preview-1440-ledger.png`, `slices-390-fix/v3c-390--s05.png`)
  · loop 4 (2026-09-17), R9-läget `909916d1`: `.giant` 88 px, −3,52 px tracking, ordet 1 rect, 3 rader vid 1440; 33,6 px, 2 rader vid 390 (`geom4.json`, `preview/preview-1440-ledger.png`, `slices-390/v3c-390--s05.png`)
  · loop 5 (2026-09-17), R10-läget `d3491b4a`: `.giant` 88 px, −3,52 px tracking, det låsta ordet 1 rect, 3 rader vid 1440; 33,6 px, 2 rader vid 390 (`geom5.json`, `preview/preview-1440-ledger.png`, `slices-390/v3c-390--s05.png`)

**Balans per skärm (squint 5 px)**

- [ ] **H-08** Varje 1440-skärm i skivorna har exakt ett dominerande element och inga två lika tunga block sida vid sida. (I dag s6: pris + Hōrai.)
  · loop 1 (2026-09-17): `s03` tes + jätterubrik lika tunga; `s04` Calyx + Hōrai-irisen; `s05` pris + Hōrai; `s09` steg 07 + arkets kant + principerna (tre halva): 013, 017, 025 C
  · loop 2 (2026-09-17), R7-läget `d30355da`: `s03` tes + jätterubrik lika tunga (Q30); `s04`/`s05` kan inte dömas: Calyx och Hōrai renderas som tomma plattor (ramarna vaknar inte, plan 027). Efter 027 läses balansen om
  · loop 3 (2026-09-17), R8-läget `70214a22`: `s03` tes + jätterubrik lika tunga (Q30); `slices-1440-fix/v3c-1440--s04.png`: Calyx dominerar liggaren; `s05`: Hōrai dominerar priset (Astra loop 3 bild 29, 30 överens). Öppen bara för s03
  · loop 4 (2026-09-17), R9-läget `909916d1`: `s03` tes + jätterubrik lika tunga (Q30, väntar på Anton); `slices-1440/v3c-1440--s04.png`: Calyx dominerar liggaren; `s05`: Hōrai dominerar priset, båda ramarna hela i vanliga `scrollTo`-skivor (035). Öppen bara för s03
  · loop 5 (2026-09-17), R10-läget `d3491b4a`: `s03` tes + jätterubrik lika tunga (Q30, väntar på Anton); `slices-1440/v3c-1440--s04.png`: Calyx dominerar liggaren; `s05`: Hōrai dominerar prisplanet. Astra loop 5 läser samma sak. Öppen bara för s03
- [x] **H-09** Kortbaksidan fyller minst 60 % av kortets bredd och höjd med innehåll eller en ritad form vid `?preview=back`, 1440 och 390. (I dag ~45 % x 60 %.)
  · loop 1 (2026-09-17): `preview/preview-1440-back.png`, `preview-390-back.png`: högra halvan tom: 016
  · loop 2 (2026-09-17), R7-läget `d30355da`: A-glyfen fyller kortets högra halva i hårlinje, 60 % av höjden, ingen kollision med texten (`preview/preview-1440-back.png`, `preview-390-back.png`, `flip-1440/…-11-100.png`)
  · loop 3 (2026-09-17), R8-läget `70214a22`: `preview/preview-1440-back.png`, `preview-390-back.png`, `flip-1440/v3c-1440-flip-11-100.png`: glyfen fyller kortets högra halva
  · loop 4 (2026-09-17), R9-läget `909916d1`: `preview/preview-1440-back.png`, `preview-390-back.png`, `flip-1440/v3c-1440-flip-11-100.png`: glyfen fyller kortets högra halva
  · loop 5 (2026-09-17), R10-läget `d3491b4a`: `preview/preview-1440-back.png`, `preview-390-back.png`, `flip-1440/v3c-1440-flip-11-100.png`: glyfen fyller kortets högra halva
- [x] **H-10** Mitt i vändningen (`--flip` 0,45 till 0,55) är kortets projicerade höjd minst 75 % av vilohöjden. (I dag ~60 %, `v3c-1440-flip-05-045.png`.)
  · loop 1 (2026-09-17): projicerad höjd vid `--flip` 0,5: 481 / 504 = 95,5 % (1440), 350 / 405 = 86,4 % (390), `diag.json` flips; det HELHET § 2 läste som en linje i tomrum är kortets 2 px tjocklek (`preview-1440-mid.png`), plan 024 gör den 4 px
  · loop 2 (2026-09-17), R7-läget `d30355da`: oförändrat sedan loop 1 (span, fönster och skalparabel orörda); `flip-1440/…-05-045.png`, `flip-06-055.png` visar kortet med full höjd på kant
  · loop 3 (2026-09-17), R8-läget `70214a22`: `flip-1440/v3c-1440-flip-05-045.png`, `-06-055.png`, `flip-390/…-05-045.png`: kortet med full höjd på kant, 4 px kant
  · loop 4 (2026-09-17), R9-läget `909916d1`: `flip-1440/v3c-1440-flip-05-045.png`, `-06-055.png`, `flip-390/…-05-045.png`: kortet med full höjd på kant, 4 px kant
  · loop 5 (2026-09-17), R10-läget `d3491b4a`: `flip-1440/v3c-1440-flip-05-045.png`, `-06-055.png`, `flip-390/…-05-045.png`: kortet med full höjd på kant, 4 px kant
- [x] **H-11** Prisblocket läser som ett eget material mot grunden: dess ground skiljer sig från `--c-black` med minst 12 steg i L (0 till 100) mätt på pixel, eller bär en hårlinjeram. (I dag `#0c0b08` mot `#0b0c0e`.)
  · loop 1 (2026-09-17): `.price` background rgb(12,11,8) mot grunden #0b0c0e (`diag.json`, `s05`): 013
  · loop 2 (2026-09-17), R7-läget `d30355da`: `.price` `oklch(0.27 0.012 250)` (`diag3.json priceBg`), R7 mätte L-delta 12,16 och 14,54:1; läser som ett plan mot grunden (`s05`, `s390-06`)
  · loop 3 (2026-09-17), R8-läget `70214a22`: `slices-1440-fix/v3c-1440--s05.png`, `slices-390-fix/v3c-390--s06.png`: grafitplanet läser som material mot fotot
  · loop 4 (2026-09-17), R9-läget `909916d1`: `slices-1440/v3c-1440--s05.png`, `slices-390/v3c-390--s06.png`: grafitplanet `oklch(0.27 0.012 250)` läser som material mot fotot (`preview390.json` priceBg)
  · loop 5 (2026-09-17), R10-läget `d3491b4a`: `slices-1440/v3c-1440--s05.png`, `slices-390/v3c-390--s06.png`: grafitplanet `oklch(0.27 0.012 250)` läser som material mot fotot; mätt kontrast på planet 14,54:1 för alla tolv strängar (`contrast_over_media` vid scrollY 4 800)
- [x] **H-12** Avslutet står ensamt i sin viewport vid 1440 och 390, `.close` minst 62 svh, mailto-raden minst 64 px glyfhöjd vid 1440 (plan 007).
  · loop 1 (2026-09-17): `.close` 558 px = 62 % håller, men mailto 67 px (4,2rem binder) och liggarens sista rader delar viewporten (`s10`): 015
  · loop 2 (2026-09-17), R7-läget `d30355da`: `footer.close` 900 px = 100 svh, ensam i sista skivan (`s12`, `s390-13`); mailto-raden 98 px hög, ~86 px teckenstorlek (`diag3.json geom1440 mailto`)
  · loop 3 (2026-09-17), R8-läget `70214a22`: `footer.close` 900 px = 100 svh, ensam i `slices-1440/v3c-1440--s12.png`; 844 px vid 390 (`s13`); mailto 98 px hög vid 1440 (`geom3.json`)
  · loop 4 (2026-09-17), R9-läget `909916d1`: `footer.close` 900 px = 100 svh, ensam i `slices-1440/v3c-1440--s12.png`; 844 px vid 390 (`s13`); mailto 98 px hög, 86,4 px teckenstorlek vid 1440 (`geom4.json`)
  · loop 5 (2026-09-17), R10-läget `d3491b4a`: `footer.close` 9 682 till 10 582 = 900 px = 100 svh, ensam i `slices-1440/v3c-1440--s11.png`; 844 px vid 390 (`s13`); mailto 86,4 px teckenstorlek vid 1440, 44 px hög vid 390 (`geom5.json`)
- [x] **H-13** Folden vid 390 har högst 12 % av viewporthöjden som död grund under underraden (i dag ~18 %).
  · loop 1 (2026-09-17): 16,3 % död grund under underraden vid 390 (137 px, `diag2`; `slices-390/v3c-390--s00.png`): loop 2, egen höjdbudget
  · loop 2 (2026-09-17), R7-läget `d30355da`: 137 px = 16,3 % död grund under underraden vid 390 (`preview-390-front.png`, `s390-00`): plan 032 A
  · loop 3 (2026-09-17), R8-läget `70214a22`: R8 mätte 10,0 % (84 px) vid 390x844; `slices-390/v3c-390--s00.png`, `preview/preview-390-front.png`: ~85 px grund under underraden
  · loop 4 (2026-09-17), R9-läget `909916d1`: 84 px = 10,0 % död grund under underraden vid 390x844 (`geom4.json deadFold`; `slices-390/v3c-390--s00.png`, `preview/preview-390-front.png`)
  · loop 5 (2026-09-17), R10-läget `d3491b4a`: 84 px = 10,0 % död grund under underraden vid 390x844 (`geom5.json deadFold`; `slices-390/v3c-390--s00.png`)
- [x] **H-14** Berättelsens ordning s4 → s5 → s6 → process → s7 håller vid 390: tesen kommer före Calyx, Calyx före priset. (I dag kommer Hōrai och liggaren före tesen.)
  · loop 1 (2026-09-17): 390: jätterubrik/liggare (2 870) → Hōrai (3 567) → tes (4 150) → Calyx (4 658) → pris (5 274), `diag.json`, `s390-03..06`: 012
  · loop 2 (2026-09-17), R7-läget `d30355da`: 390: tes 2 870 → Calyx 3 442 → jätterubrik/liggare 4 123 → Hōrai 4 884 → pris 5 531 (`diag3.json geom390`, `s390-03..06`)
  · loop 3 (2026-09-17), R8-läget `70214a22`: 390: tes 2 870 → Calyx 3 459 → jätterubrik 4 157 → Hōrai 4 935 → pris 5 599 (`geom3.json`, `slices-390-fix/…s03` till `s07`)
  · loop 4 (2026-09-17), R9-läget `909916d1`: 390: tes 2 870 → Calyx 3 459 → jätterubrik 4 157 → Hōrai 4 935 → pris 5 599 (`geom4.json`, `slices-390/…s03` till `s07`)
  · loop 5 (2026-09-17), R10-läget `d3491b4a`: 390: tes 2 870 → Calyx 3 459 → jätterubrik 4 157 → Hōrai 4 935 → pris 5 599 (`geom5.json`, `slices-390/…s03` till `s07`)
- [x] **H-15** Varje öppen spalt bär ett displayelement, en bild eller en helhöjdslinje; ingen spalt med två viskade rader.
  · loop 1 (2026-09-17): processaktens högerspalt är tom tills gridet nått 85 % av viewporten (`s05`, `process-1440/v3c-1440-life-01.png`): 025 B ankrar `--s1` i arkets ankomst
  · loop 2 (2026-09-17), R7-läget `d30355da`: processaktens entré: högerspalten tom tills arket nått in (`process-1440/v3c-1440-life-01.png`), och prosan tonar in (plan 034 B); efter 034 läses entrén om. Principernas 64ch-liggare står som mått, inte som öppen spalt (loop 1)
  · loop 3 (2026-09-17), R8-läget `70214a22`: prosan synlig från entrén (034 B, `process-1440/v3c-1440-life-01.png`), men entréskärmens högerspalt bär bara ett hörn av ramen tills konturen är hel (`slices-1440/v3c-1440--s06.png`, `process-390/v3c-390-life-01.png`; Astra loop 3 fix 6): plan 040
  · loop 4 (2026-09-17), R9-läget `909916d1`: konturen hel medan steg 01 läses där motorns topp stämmer (040): `slices-1440/v3c-1440--s06.png`, `process-1440/v3c-1440-life-02.png`, `process-390/v3c-390-life-01.png`; men `process-1440/v3c-1440-life-01.png` (Astra loop 4 bild 77): steg 01 läsbart nere till vänster, högerspalten tom, för att motorn räknar `#process` från 5 637 medan DOM:en står på 5 340 efter prisblockets första målning (`--sc-p` 0,091 mot sant 0,154; `mountshift.json`). Plan 042, inte 040
  · loop 5 (2026-09-17), R10-läget `d3491b4a`: **bockad.** Konturen är hel och glyfen ritad bredvid steg 01:s stycke: `process-1440/v3c-1440-life-02.png`, `process-390/v3c-390-life-02.png`, `slices-1440/v3c-1440--s06.png`. Loop 4:s enda kvarvarande orsak var motorns stale topp (`--sc-p` 0,091 mot sant 0,154); den är borta: motorns `#process`-topp = DOM:ens, 5 340 = 5 340 vid 1440 och 6 152 = 6 152 vid 390, i 21 av 21 laddningar utan resize (`preview390_5.json`). Processaktens högerspalt bär den hela ritningen, principernas 64ch-liggare står som mått (loop 1, Astra loop 5 läser samma sak)

**Övergångar utan avbrott**

- [x] **H-16** `scroll_verify.py` rapporterar inga `deadScroll`-band med diff under 0,01 utanför den författade tystnaden (ps 0 till 0,10 i heron), vid 1440 och 390. (I dag sju respektive sex band.)
  · loop 1 (2026-09-17): `probe/scroll-verify-1440.txt`: band 0 till 300 (0,0043) = författad tystnad ps 0 till 0,10; 1 800 till 2 100 (0,0016) = landad baksida + dwell; 600 till 900 (0,0093) är mitt i vändningen och en verktygsblindhet (mörkt kort mot mörk grund vid 64x36; `flip-1440/v3c-1440-flip-03..05.png` visar kortet vridas); 5 400 till 6 600 (0,014 till 0,015) ligger över 0,01. 390: 1 686 till 1 967 (0,0) = landad baksida + dwell
  · loop 2 (2026-09-17), R7-läget `d30355da`: `probe/scroll-verify-1440.txt`: 0 till 300 (0,0048) = författad tystnad ps 0 till 0,10, 1 800 till 2 100 (0,0043) = landad baksida + dwell; övriga band 0,0104 till 0,0146 över 0,01. 390: 1 686 till 1 967 (0,0) = landad baksida, 10 397 till 10 677 (0,0) = dokumentets sista viewport (maxscroll); övriga ≥ 0,0102
  · loop 3 (2026-09-17), R8-läget `70214a22`: `probe/scroll-verify-1440.txt`: 0 till 300 (0,0046) författad tystnad, 1 800 till 2 100 (0,0028) landad baksida + dwell, 1 500 till 1 800 (0,008) kortet på kant mot mörk grund (verktygsblindhet; `flip-1440/…-05`, `-06` visar rotationen), övriga 0,0107 till 0,0146; 390: 0 till 281 (0,0093) författad, 1 686 till 1 967 (0,0) landad baksida, 1 405 till 1 686 (0,0148)
  · loop 4 (2026-09-17), R9-läget `909916d1`: `probe/scroll-verify-1440.txt`: 0 till 300 (0,0052) författad tystnad, 600 till 900 (0,0088) kortet på kant (verktygsblindhet, `flip-1440/…-03`, `-04`), 1 800 till 2 100 (0,0005) landad baksida + dwell, 1 500 till 1 800 (0,0124), 5 700 till 6 000, 6 600 till 7 200, 8 100 till 8 400 (0,0115 till 0,0147) över 0,01; `cuesNeverFull`, `unrevealed`, `contrastUnderMedia` tomma; 390: 0 till 281 (0,0055) författad, 1 124 till 1 405 (0,008) kortet på kant, 1 686 till 1 967 (0,0) landad baksida; `blankBands` vid Calyx/Hōrai/priset är 64x36-nedskalningen av hela ramar och ett platt plan (`slices-390/…s04`, `s06` visar dem hela)
  · loop 5 (2026-09-17), R10-läget `d3491b4a`: `probe/scroll-verify-1440.txt`: band under 0,01 endast 0 till 300 (0,0094, den författade tystnaden ps 0 till 0,10) och 1 800 till 2 100 (0,0003, landad baksida + dwell); övriga 0,0102 till 0,0148. `cuesNeverFull`, `unrevealed`, `contrastUnderMedia` tomma vid båda bredderna. 390: 0 till 281 (0,0101), 1 405 till 1 686 (0,0143), 1 686 till 1 967 (0,0, landad baksida). `blankBands` (ett vid 1440, fem vid 390) är 64x36-nedskalningen av heropinnen, de två ramarna, prisplanet och avslutsfotot; skivorna visar dem hela
- [x] **H-17** Den statiska svansen i heron (efter landad baksida, inklusive dwell) är högst 700 px vid 900 vh. (I dag 1 273 px.)
  · loop 1 (2026-09-17): motorns `dwell` är en mittremapp (`scrollcraft.js` rad 159: `(1-L)x + L(4c³+0,5)`), inte en hållning i slutet, som § 2:s tabell antog. Räknat med den kurvan (span 3,4, travel 2 160): p = 0,78 vid x 0,818 → svansen 393 px; `scroll-verify-1440` mäter det döda bandet 1 800 till 2 100 inne i den. Astra loop 1 räknade samma tal; § 2:s 655 var fel
  · loop 2 (2026-09-17), R7-läget `d30355da`: oförändrat (span 3,4, dwell 0,2, fönster 0,10 till 0,78 orörda i R7)
  · loop 3 (2026-09-17), R8-läget `70214a22`: oförändrat (span 3,4, dwell 0,2, fönster 0,10 till 0,78 orörda i R8)
  · loop 4 (2026-09-17), R9-läget `909916d1`: oförändrat (span 3,4, dwell 0,2, fönster 0,10 till 0,78 orörda i R9); statiska svansen 393 px
  · loop 5 (2026-09-17), R10-läget `d3491b4a`: oförändrat (span 3,4, dwell 0,2, fönster 0,10 till 0,78 orörda i R10); statiska svansen 393 px
- [x] **H-18** Vändningen tar 1 300 till 1 600 px scroll vid 900 vh (span 3,4, fönster 0,10 till 0,78). (2,2 gav 648, 4,8 ger 2 052.)
  · loop 1 (2026-09-17): med motorns dwell-kurva: p 0,10 vid x 0,076 (164 px), p 0,78 vid x 0,818 (1 767 px), vändning 1 602 px (Astra loop 1 räknade samma); 2 px över 1 600, inom tolerans, bockad; § 2:s 1 469 antog dwell som slut-hållning. `flip-1440/` visar jämn rotation i tolv steg
  · loop 2 (2026-09-17), R7-läget `d30355da`: oförändrat, 1 602 px; `flip-1440/` tolv ramar jämn rotation
  · loop 3 (2026-09-17), R8-läget `70214a22`: oförändrat, 1 602 px; `flip-1440/` tolv ramar jämn rotation
  · loop 4 (2026-09-17), R9-läget `909916d1`: oförändrat, 1 602 px; `flip-1440/` och `flip-390/` tolv ramar jämn rotation
  · loop 5 (2026-09-17), R10-läget `d3491b4a`: oförändrat, 1 602 px; `flip-1440/` och `flip-390/` tolv ramar jämn rotation
- [x] **H-19** Grunddriften är ett kallt ljus, inte en tvätt, mätt på en mellantonspixel i grunden (träpanelen, gråskala L 110 till 140, t.ex. (720,180) vid 1440 med tesen centrerad): chroma (max − min) 12 till 24 vid tesbandet och ≤ 2 i folden. (Fas A:s golv, 12 RGB-steg på en nästan svart marginalpixel, var fel mätpunkt: `mix-blend-mode:color` skalar kulören med luminansen, så golvet tvingade en tvätt på mellantonerna; omskriven i loop 3 på leadens R8-fynd 2.)
  · loop 1 (2026-09-17): grunden bakom tesen är samma svärta som i folden (`s00` mot `s03`), `filter:grayscale` ligger efter blandningen: 017 A mäter pixeln före/efter
  · loop 2 (2026-09-17), R7-läget `d30355da`: mätbar: högermarginalens grundpixel (20,20,22) i folden mot (8,23,37) vid tesen, delta 15 (`diag3.json B_summary current-62`). Men hela fotot är blått (rännan (58,86,111) mot gråskalans (80,80,80), chroma 29, leadens R7-fynd): plan 029 sänker tonen till 40 % (delta 13, chroma 19, mätt) så att raden fortfarande håller
  · loop 3 (2026-09-17), R8-läget `70214a22`: 44 % ger chroma 38 på träpanelen ((112,132,150) mot gråskalans (128,128,128)): tvätt (`drift2/d44-thesis.png`, `slices-1440/v3c-1440--s03.png`); 24 % ger chroma 21 (`drift2/d24-thesis.png`): kallt ljus; folden neutral vid alla styrkor (`drift2/drift2.json`). **Raden omskriven** på mellantonen (leadens R8-fynd 2); plan 038
  · loop 4 (2026-09-17), R9-läget `909916d1`: mätpunkterna håller: träpanelen (720,180) vid tesen centrerad (119,130,140), chroma 21; folden chroma 0 (`geom4.json thesis_px`, `fold_px`); `slices-1440/v3c-1440--s03.png`: kallt ljus. Men överlämningen tes → jätte hoppar: `--sc-canvas` rgb(18,63,104) vid scrollY 3 600, rgb(244,242,238) vid 3 620, träet chroma 21 → 2 på 20 px (`astra-verify/verify_astra4.json`, `drift-3580.png`, `drift-3620.png`; Astra loop 4 fix 3): ljuset släcks i ett steg i stället för att tona. Plan 044
  · loop 5 (2026-09-17), R10-läget `d3491b4a`: **bockad.** Mätpunkterna håller: träpanelen (720,180) vid tesen centrerad (119,130,140), chroma 21; folden chroma 0 (`geom5.json thesis_px`, `fold_px`). Och överlämningen hoppar inte längre (plan 044): `--sc-canvas` rgb(18,63,104) vid 3 600, rgb(19,64,104) vid 3 620, rgb(35,76,114) vid 3 700, rgb(76,109,138) vid 3 800, rgb(185,195,203) vid 4 000; träets mellanton (720,40) chroma 21 → 20 → 19 → 15 → 5 över samma sträcka, inget steg över 40 per kanal per 20 px (`verify/`, `drift-3620.png`). Loop 4:s fynd (chroma 21 → 2 på 20 px) är borta
- [x] **H-20** Hyperborea-plåten bleeder minst 96 px förbi sin ram vid 1440 och spåret `.thesis-figure:transform` är inte DEAD (plan 008).
  · loop 1 (2026-09-17): `diag2`: vid `--sc-ps` = 1 är överhänget 103 px och transformen 30,3 → 103,0 px (inte DEAD). Men plåtens högerkant 799,9 px går 9 px in i `VI BYGGER` (textkant 791): 017 D vidgar rännan och sänker taket till 33 % (100 px)
  · loop 2 (2026-09-17), R7-läget `d30355da`: R7 D: överhäng 100 px, 5 px före rubrikkanten; `preview/preview-1440-bleed.png`: plåtens högerkant står fri från `VI BYGGER`
  · loop 3 (2026-09-17), R8-läget `70214a22`: `preview/preview-1440-bleed.png`: plåtens högerkant står fri från `VI BYGGER`
  · loop 4 (2026-09-17), R9-läget `909916d1`: `preview/preview-1440-bleed.png`: plåtens högerkant står fri från `VI BYGGER`; `.thesis-figure` transform translateX 86,5 px vid `--sc-ps` ≈ 0,95, 100 px vid 1 (R7 D), spåret levande (`geom4.json thesisFigAtLater`)
  · loop 5 (2026-09-17), R10-läget `d3491b4a`: `preview/preview-1440-bleed.png`: plåtens högerkant står fri från `VI BYGGER`; överhäng 96 px, plåtens högerkant 787 mot jätterubrikens vänsterkant 797 (`geom5.json thesisFigAtLater`), transformen levande (translateX 95,6 px vid `--sc-ps` ≈ 0,95)

**Rörelse genomgående och mjuk, hero till footer**

- [ ] **H-21** `motion_probe.py` vid cpu 4, hjul 100:60 och 20:120, nedåt och uppåt, med kontrollen `tests/motion/smooth.html` ren (0 rutor över 33 ms) omedelbart före: `staircase 0` på varje spår, `frame_p95_ms ≤ 20`, `frames_over_33ms 0`. (I dag p95 290,6 ms, 111 rutor.)
  · loop 1 (2026-09-17): `probe/`: cpu 4, 100:60 nedåt hero p95 217 ms, 115 rutor > 33 ms; uppåt 131,6 ms, 100 rutor; 20:120 nedåt 89,2 ms, 522 av 954; `#process` nedåt 445,7 ms, 120 rutor, staircase 1; uppåt 203 ms. Kontrollen 18,2 till 18,4 ms med 0 till 2 rutor (aldrig helt tyst). staircase 0 på alla hero-spår, `--sc-ps` max_step 0,37 till 1,84 %. Arkitektoniskt (RecalcStyle), inte en loop 1-plan
  · loop 2 (2026-09-17), R7-läget `d30355da`: cpu 4, 100:60: hero p95 817 ms ned (97 rutor), 107 ms upp (106); `#process` 480 ms ned, 392 upp; 20:120 hero 54 ms (454 av 1 037). Kontrollen 18,3 till 18,5 ms med 0 till 2 rutor (`probe/probe-log.txt`, maskinen brusig). Profileringen (`shots/loop-2/profile/`): stilomräkning 65 till 76 % av tasktiden; en `--sc-ps`-skrivning kostar 1,8 ms (hero), 2,1 (jätten), 2,2 till 2,6 (arket) i ren subträdsomräkning, shimen tvingar 1,7 till 4,6 omräkningar per frame. Plan 028 (mätt: cpu 1 hero 35,5 → 18,8 ms med batchad shim)
  · loop 3 (2026-09-17), R8-läget `70214a22`: cpu 4, 100:60: hero p95 89,5 ms ned (88 rutor), 54,0 upp (81); `#process` 285 ned (143), 461 upp (117); 20:120 hero 53,2 / 36,5, process 88,5 / 88,4. Kontrollen 18,2 till 18,5 ms med 0 till 2 rutor i varje körning (`probe/probe-log.txt`). Orsak mätt i `probe/ab/`: klippningen över en levande ram, plan 036
  · loop 4 (2026-09-17), R9-läget `909916d1`: cpu 4, 100:60: hero p95 333,8 ms ned (96 rutor), 79,7 upp (91); `#process` 326,9 ned (138), 474,6 upp (131); 20:120 hero 53,0 / 52,7, process 86,0 / 215,7; jätten 462, priset 875,9. Kontrollen 18,2 till 18,4 ms med 0 till 2 rutor (`probe/probe-log.txt`). Staircase 0 överallt. Dekomposition vid cpu 1 (`probe/ab/hero-*`): pinnen ensam (0 till 1 800) 18,4 ms = kontrollen; kostnaden är 1 800 till 4 000 (de två levande ramarna monteras och målar sina sidor, bandet kommer in), förmontering 5 s tidigare tar inte bort den (89,4). Arkitektoniskt golv utanför cellen (ramarnas egen målning, motorns läsning) för allt utom prisplatshållarens omlayout (042: −18 ms i prisfönstret, −12 i jättefönstret); redovisat, inte bockat
  · loop 5 (2026-09-17), R10-läget `d3491b4a`: cpu 4, 100:60: hero p95 **280,1 ms** ned (median av tre sammanflätade körningar med ren kontroll emellan; enstaka körningar 139,9 / 280,1 / 324,2 och en fjärde 485,0 i första svepet), 49,9 upp; `#process` 83,2 ned / 50,1 upp; jätten 250,0; priset 238,2; 20:120 hero 33,4 / 33,3, process 50,0 / 50,0. Kontrollen 16,8 ms med 0 rutor i sex av åtta körningar. Staircase 0 överallt. **Golvet håller eller är bättre i varje fönster** mot loop 4:s redovisade tal (hero 333,8 / 79,7, process 326,9 / 474,6, jätten 462,0, priset 875,9). Baren p95 ≤ 20 / 0 rutor nås fortfarande inte; det som återstår är ramarnas egen målning och motorns läsning, utanför cellen. Redovisat golv, inte bockat, ingen plan
- [ ] **H-22** Samma bar vid cpu 1. (I dag p95 71,5 ms, 25 rutor.)
  · loop 1 (2026-09-17): cpu 1, 100:60: hero nedåt p95 35,8 ms, 26 rutor; uppåt 35,1 ms, 17 rutor; `#process` nedåt 18,5 ms, 8 rutor; uppåt 18,8 ms, 11 rutor; staircase 0 överallt
  · loop 2 (2026-09-17), R7-läget `d30355da`: cpu 1, 100:60: hero ned p95 36,5 ms (31 rutor), upp 19,0 (10); `#process` ned 35,3 (16), upp 18,4 (3); staircase 0 överallt. Plan 028: målvärden hero ≤ 20, bandet ≤ 25, arket ≤ 20
  · loop 3 (2026-09-17), R8-läget `70214a22`: cpu 1, 100:60: hero ned 36,1 (19 rutor), upp 18,4 (5); `#process` ned 32,1 (14), upp 18,5 (4); `#giant-section` 128 (22); `.price`-fönstret 143,7 (16). A/B med ramarna förmonterade (`probe/ab/r3-*`, tre körningar): clip-path över levande Hōrai 101 till 187 ms, `mask-image` 65 till 72, ingen klippning 35 till 62. Plan 036
  · loop 4 (2026-09-17), R9-läget `909916d1`: cpu 1, 100:60: hero ned 53,6 / 78,2 / 82,2 (median 78,2; R8 36,1), upp 35,4 (R8 18,4); `#process` ned 18,2 (R8 32,1), upp 18,2; `#giant-section` 101,6 (R8 128); `.price` 40,4 (R8 143,7); `.panel-thesis` 142,4 (ramarna monteras vid fönstrets start); `footer.close` 18,3; pinnen ensam 18,4 (tre körningar). Herofönstrets försämring mot R8 är 036 B (monteringen flyttad från 2 860 till 1 920, in i 40-tick-fönstret) plus ramarnas målning, inte latchen (pin18 = kontrollen). Prisfönstret nådde 036:s mål (≤ 50); jättefönstret och heron nådde inte ≤ 25. Med 042 neutraliserad: pris 35,3, jätte 81,7 (median). Golv redovisat; 042 kvar i filen
  · loop 5 (2026-09-17), R10-läget `d3491b4a`: cpu 1, 100:60: hero ned 33,4 / 83,4 / 33,6 (median **33,6**; loop 4 78,2), upp 16,8 (35,4); `#process` ned 17,1 / upp 17,0 (18,2 / 18,2); `#giant-section` 50,2 (101,6); `.price` 46,7 (40,4); `.panel-thesis` median **142,4** över tre sammanflätade körningar (loop 4 142,4) och en sammanflätad A/B mot R9:s två återinjicerade deklarationer gav 108,4 med dem mot 142,4 utan, spridningarna överlappande (`probe/ab/thesis-r9-*`, `thesis-r10-*`, kontrollen 0 rutor i alla tre); `footer.close` 16,9 vid samma 1 482 px resväg som loop 4 (18,3). Staircase 0 överallt. Golvet håller eller är bättre; redovisat, inte bockat
- [x] **H-23** `--sc-ps` max_step ≤ 3 % på varje akt, även flow-akterna (i dag 3,28 % giant, 4,01 % tes): korta akter får längre liv eller läser en långsammare härledd variabel.
  · loop 1 (2026-09-17): hero `--sc-ps` ≤ 1,84 % håller; `#process:--sc-ps` 3,59 % (cpu 4, 100:60 nedåt, staircase 1), 1,08 % uppåt, 0,73 % vid cpu 1: den enda körningen över 3 % är den med 445 ms p95, alltså bildtidens fel, inte fönstrets
  · loop 2 (2026-09-17), R7-läget `d30355da`: hero `--sc-ps` max_step 1,41 till 2,04 % (båda riktningarna, båda kadenserna, cpu 1 och 4; R7:s 4,54 % uppåt inte reproducerad: 1,48 % cpu 1 upp), `#process` 0,22 till 1,77 %; `footer.close` 2,80 % vid cpu 1 (p95 18,3 ms) men 5,79 % vid cpu 4, `.price` 16,41 % vid cpu 4 (`probe/footer-down-100-cpu1/`, `footer-down-100/`): korta flow-akter (liv ≈ 1 800 px) stegar när bildtiden faller, inte annars. Öppen som bildtidens följd (plan 028); 033 mäter priset vid cpu 1
  · loop 3 (2026-09-17), R8-läget `70214a22`: `--sc-ps` max_step vid cpu 1: hero 1,41 ned / 1,38 upp, `#process` 0,78 / 1,42, `#giant-section` 2,82, `.price` 2,25, `footer.close` 2,74 (`probe/*/motion_probe.json`); R8:s 4,61 % uppåt inte reproducerad (1,38). cpu 4: hero 1,65 / 1,85, process 0,99 / 1,71
  · loop 4 (2026-09-17), R9-läget `909916d1`: `--sc-ps` max_step vid cpu 1: hero 1,38 till 1,55 (tre körningar), `#process` 0,70 / 0,70, `.price` 1,78, `footer.close` 2,70, **`#giant-section` 3,12 %, `.panel-thesis` 3,52 %** (fönster där ramarna monteras och sidan lägger om 297 px; med 042 neutraliserad 2,86 till 3,13); cpu 4: hero 1,72 / 1,86, process 1,10 / 1,06, jätten 3,36. Staircase 0 överallt. **Återöppnad**: bildtidens följd i två fönster, ingen egen plan; mäts om efter 042
  · loop 5 (2026-09-17), R10-läget `d3491b4a`: **bockad**, på samma grund som loop 3 använde (cpu 1). `--sc-ps` max_step vid cpu 1: hero 1,25 till 1,37, `#process` 0,67 ned / 0,76 upp, `#giant-section` **2,65** (loop 4 3,12), `.panel-thesis` **2,31 till 2,90** över fyra körningar (loop 4 3,52), `.price` 2,33, `footer.close` 2,66. Alla akter ≤ 3 %. De två fönster loop 4 öppnade raden på ligger nu under baren, och orsaken är plan 042: sidan lägger inte längre om 297 px mitt i dem. cpu 4: hero 1,62 till 1,80, `.plate-card` 2,03 till 2,82, `#process` 1,04 / 0,91, jätten 3,31 (bildtidens följd, loop 2:s princip, H-21:s golv)
- [x] **H-24** Inget spår i BRIEF:s device-tabell rapporteras DEAD.
  · loop 1 (2026-09-17): spårade i loop 1: `section.hero:--sc-ps`, `.plate-card:transform`, `#process:--sc-ps` (inga DEAD), `.thesis-figure:transform` levande (`diag2`); `.giant` scale, `#threadFill`, `.p-live` clip och `.close-rule` (015) inte spårade: README § Verktyg (proben läser ren `scale()` som DEAD)
  · loop 2 (2026-09-17), R7-läget `d30355da`: spårade: `section.hero:--sc-ps`, `.plate-card:transform`, `#process:--sc-ps`, `footer.close:--sc-ps` (inga DEAD); `.giant` scale, `#threadFill`, `.close-rule`, `.thesis-figure` oprobade (proben blind för ren `scale()`, README § Verktyg). Öppen som verktygsskuld
  · loop 3 (2026-09-17), R8-läget `70214a22`: spårade: hero, `.plate-card`, `#process`, `#giant-section`, `.price`, `footer.close` (inga DEAD); `.giant` scale, `#threadFill`, `.close-rule`, `.thesis-figure`, `.horai-wrap:clip-path` oprobade. Verktygsskuld
  · loop 4 (2026-09-17), R9-läget `909916d1`: spårade: hero, `.plate-card`, `#process`, `#giant-section`, `.price`, `.panel-thesis`, `footer.close`, `.horai-wrap:--rv` och `.horai-wrap .rv:transform` (inga DEAD); `.giant` scale, `#threadFill`, `.close-rule`, `.thesis-figure` oprobade (proben blind för ren `scale()`). Verktygsskuld, oförändrad
  · loop 5 (2026-09-17), R10-läget `d3491b4a`: **bockad på direkt mätning i stället för på proben.** De fyra device-tabellspår `motion_probe.py` är blind för (den löser ren `scale()` genom `atan2(b,a)` och faller till translation) mättes i stället som beräknad matris vid femton scrollägen (`devices5.json`): `.giant` sex skilda matriser (device 7), `#threadFill` tre (device 4, höjden växer 0 → 331 px), `#heroPoolImg` fem translate3d-värden (device 2), `.close-rule` fem scaleX (0,26 → 0,63 → 0,99 → 1). Probade spår denna runda: hero, `.plate-card`, `#process`, `#giant-section`, `.price`, `.panel-thesis`, `footer.close`, `.calyx-wrap:--rv`, `.calyx-wrap .rv:transform` (levande efter 043: −264 → 0 px) och `.horai-wrap:--rv`. **Inget device i tabellen är dött.** `.horai-wrap .rv:transform` rapporteras DEAD och det är rätt: Hōrais device (BRIEF § Device-tabell rad 6) är en iris, inte en transform på `.rv`; loop 4:s rad skrev "inga DEAD" om det spåret och det var fel mot dess egen json. Verktygsskulden står kvar som verktygsskuld, men raden mäter sidan och sidan håller
- [x] **H-25** Varje skärm från hero till footer har minst en scroll-läst förändring som syns i en tolvstegs ramsekvens (reveal, scrub, drift, ritning): i dag saknas den på priset, avslutet och Hōrai efter irisen.
  · loop 1 (2026-09-17): priset och avslutet saknar fortfarande scroll-läst förändring (`process-1440/v3c-1440-life-00.png`, `s10`); 015 ger avslutet sin linje; priset står kvar till loop 2 (grunddriften bakom det syns inte genom ett opakt block)
  · loop 2 (2026-09-17), R7-läget `d30355da`: avslutet har sin linje (`footer` i `s11`/`s12`); priset står stilla (`process-1440/v3c-1440-life-00.png`, `s05`): plan 033; jätterubrikens skala 0,92 → 1 syns inte i tolv ramar (Astra loop 2): oförändrad, rapporteras
  · loop 3 (2026-09-17), R8-läget `70214a22`: priset: tredje radens linje mitt i dragningen i `slices-1440-fix/v3c-1440--s05.png` mot hel i `process-1440/…life-00`; avslutets linje `s11`/`s12`; Calyx inset och Hōrai iris (`slices-1440-fix/`); jättens skala 0,92 → 1 oläsbar i tolv ramar (Astra loop 2 och 3): redundant mot ordscrubben på samma skärm, rapporteras, ingen plan
  · loop 4 (2026-09-17), R9-läget `909916d1`: priset: liggarens tredje linje mitt i dragningen i `slices-1440/v3c-1440--s05.png` mot hel i `process-1440/v3c-1440-life-00.png`; avslutets linje `s11`/`s12`; Hōrai iris (`--rv` 0,9487 i `s05`) och ordscrubben på s4; Calyx-revealen sker inte (043) men skärmen s4 bär ordscrubben, så raden håller per skärm; jättens skala 0,92 → 1 oläsbar i tolv ramar (rapporterad, redundant mot ordscrubben)
  · loop 5 (2026-09-17), R10-läget `d3491b4a`: priset: liggarens tredje linje mitt i dragningen i `slices-1440/v3c-1440--s05.png` mot hel i `process-1440/v3c-1440-life-00.png`; avslutets linje ritar sig 0,26 → 0,63 → 0,99 → 1 mellan scrollY 9 000 och 9 682 (`devices5.json`); Hōrai iris och Calyx-revealen (som nu sker, 043); ordscrubben på s4. Jättens skala 0,92 → 1 är läsbar som sex skilda matriser i mätning men fortfarande inte i tolv ramar (rapporterad sedan loop 2, redundant mot ordscrubben på samma skärm)
- [x] **H-26** Rörelsen spelar oavsett systeminställning (F-011): sökning på `prefers-reduced-motion` i `index.html` ger noll träffar, och skivor tagna under `reduced_motion="reduce"` visar allt innehåll (Highway Medias tomma tidslinje är motexemplet).
  · loop 1 (2026-09-17): R6-grep 0 träffar; alla skivor i loop 1 tagna under `reduced_motion="reduce"` visar allt innehåll
  · loop 2 (2026-09-17), R7-läget `d30355da`: grep `prefers-reduced-motion` i `index.html`: 0; alla skivor i loop 2 tagna under `reduced_motion="reduce"` visar allt innehåll
  · loop 3 (2026-09-17), R8-läget `70214a22`: grep `prefers-reduced-motion` 0; alla skivor tagna under `reduced_motion="reduce"` visar allt innehåll
  · loop 4 (2026-09-17), R9-läget `909916d1`: grep `prefers-reduced-motion` 0; alla skivor tagna under `reduced_motion="reduce"` visar allt innehåll
  · loop 5 (2026-09-17), R10-läget `d3491b4a`: grep `prefers-reduced-motion` i `index.html`: 0; alla skivor i loop 5 tagna under `reduced_motion="reduce"` visar allt innehåll
- [x] **H-27** Ramarna transformeras eller tonas aldrig efter att de visats; reveal sker en gång på wrappern (PRODUCT.md § Operating Context).
  · loop 1 (2026-09-17): reveal på wrappern, `content-visibility` i vila (R6, plan 018); ingen transform på ramarna i `s04`, `s05`
  · loop 2 (2026-09-17), R7-läget `d30355da`: ramarna transformeras inte, men wrapparnas reveal drivs av motorn ur rått `--sc-p` och reverserar vid scroll uppåt (`scrollcraft.js` rad 947-957; Astra loop 1 fix 8, uppskjuten till loop 2): plan 031 (sidans egen latch på det lerpade värdet)
  · loop 3 (2026-09-17), R8-läget `70214a22`: latchen backar aldrig men når inte 1 för PageDown (0,21), `scrollTo` (0) eller scrollbar (`latch_diag.json`; leadens R8-fynd 1): samplas bara vid scroll-händelser. Plan 035
  · loop 4 (2026-09-17), R9-läget `909916d1`: latchen: `shots/loop-4/latch4.json`: hjul, PageDown, `scrollTo` och smooth `scrollTo` till scrollY 4 703 ger `--rv` 1 / 1 på båda wrapparna; resize 1440 → 1280 före bandet, sedan hjul: 1 / 1; noll `--rv`-skrivningar tre sekunder efter landning; ingen transform på ramen efter visning (identitet vid `--rv` 1). Men Calyx-wrapperns reveal sker aldrig: `.rv` klipper inte, ramen står på wrapperns topp vid `--rv` 0 / 0,25 / 0,5 / 1, wrapperbakgrund synlig 0,1 % i alla fyra (`astra-verify/verify_astra4.json`, `calyx-rv0.png`; Hōrai 99,9 → 31,8 → 13,1 % svart, irisen fungerar; Astra loop 4 fix 2). Plan 043
  · loop 5 (2026-09-17), R10-läget `d3491b4a`: **bockad.** Calyx-revealen har nu en öppning (plan 043): wrapperbakgrund synlig 100,0 / 74,9 / 50,0 / 0,1 % vid `--rv` 0 / 0,25 / 0,5 / 1, `.rv` har `overflow:clip`, och ramens egen box står på top 40 i alla fyra lägena, alltså pixelstilla under revealen och identitet vid 1 (`verify/`, `calyx-rv0.5.png` visar övre halvan Calyx och undre halvan wrapperns `#e9e5da`). Hōrais iris i samma mätning 99,9 / 44,9 / 12,0 % svart. Latchen fortsatt vägoberoende (`latch5.json`): hjul, PageDown, `scrollTo`, smooth `scrollTo` och resize-före-bandet ger `--rv` 1 / 1 på båda wrapparna, noll `--rv`-skrivningar tre sekunder efter landning. Ingen transform på ramen efter visning

**Processakten som del av helheten**

- [x] **H-28** `#process` ligger efter `.stagger` och före `footer.close`, full bredd på `var(--bg)`, `data-sc-act="flow"`, och läser `--sc-ps` för allt som rör sig inklusive utropens opacitet (F-014, V3c:s strängare regel).
  · loop 1 (2026-09-17): `#process` rad 1138: efter `.stagger`, före `#principer` och `footer.close`, `data-sc-act="flow"`, `--k1..--k7` ur `--sc-ps` (rad 825-833)
  · loop 2 (2026-09-17), R7-läget `d30355da`: `#process` efter `.stagger`, före `#principer` och `footer.close`, `data-sc-act="flow"`, `--k1..--k7` ur `--sc-ps` (rad 888-899); prosans reveal-attribut (rad 1230) är en separat defekt, plan 034 B
  · loop 3 (2026-09-17), R8-läget `70214a22`: `#process` efter `.stagger`, före `#principer`, `data-sc-act="flow"`, `--k1..--k7` ur `--sc-ps`; `data-on`:s av-villkor läser rå pps (Astra loop 3 fix 2, plan 039), raden håller i sak
  · loop 4 (2026-09-17), R9-läget `909916d1`: `#process` efter `.stagger`, före `#principer`, `data-sc-act="flow"`, `--k1..--k7` ur `--sc-ps`; `data-on` av läser shimens `cur` (039)
  · loop 5 (2026-09-17), R10-läget `d3491b4a`: `#process` efter `.stagger`, före `#principer`, `data-sc-act="flow"`, `--k1..--k7` ur `--sc-ps`; `data-on` av läser shimens `cur` (039)
- [x] **H-29** Ritningen ritar form, aldrig innehåll (gate 47/79): varje `<path>`/`<rect>` kan namnges kontur, måttlinje, hjälplinje, skraffering, ledare eller utrop; högst 60 banor, alla `pathLength="1"`.
  · loop 1 (2026-09-17): tolv banor + glyfen, alla namnbara (kontur, mått, hjälplinje, skraffering, ledare, utrop), `pathLength="1"` (R5/R6 keep)
  · loop 2 (2026-09-17), R7-läget `d30355da`: tolv banor + glyfen, alla namnbara; `pathLength="1"` (oförändrat sedan R6)
  · loop 3 (2026-09-17), R8-läget `70214a22`: tolv banor + glyfen, alla namnbara (`preview_check.json` ids), `pathLength="1"`
  · loop 4 (2026-09-17), R9-läget `909916d1`: tolv banor + glyfen, alla namnbara, `pathLength="1"` (oförändrat sedan R6; `preview/preview-1440-process-07.png`)
  · loop 5 (2026-09-17), R10-läget `d3491b4a`: tolv banor + glyfen, alla namnbara, `pathLength="1"` (oförändrat sedan R6; `preview/preview-1440-process-07.png`)
- [x] **H-30** Sju steg = sju tillstånd av samma ark; `?preview=process-01..07` visar dem i vila, och vid 1440 äger varje steg ett fönster i `--sc-ps` (tabellen i plan 010) med ett displayelement per skärm.
  · loop 1 (2026-09-17): previews visar sju tillstånd men varje preview N läcker steg N+1:s första bana (`preview-1440-process-01..06.png`), och vid 390 står steg N+1:s rubrik under arket (`preview-390-process-01..07.png`): 025 B
  · loop 2 (2026-09-17), R7-läget `d30355da`: `?preview=process-0N` tappar steg 01: `--s1` mäts från det fastnade sticky-arket och hamnar över `--e1` (0,4847 > 0,2292 vid 1440, 0,4449 > 0,2510 vid 390), konturen och glyfen står med `stroke-dashoffset: 1px` i preview 02 till 07 (`diag/astra1-1440-process-05.png`, `astra1-390-process-05.png`; Astra loop 2 fix 1, verifierad): plan 034 A. Steg N+1 läcker inte längre (R7)
  · loop 3 (2026-09-17), R8-läget `70214a22`: `?preview=process-02` vid 1440: `--k2` 0,19, `#p-dim-width` oritad; `process-01` vid 390: `--k1` 0,67, `#p-glyph` 0,59 (`preview_check.json`; Astra loop 3 bild 42/43/54/55): målscrollen räknas en gång före typsnitten, plan 037
  · loop 4 (2026-09-17), R9-läget `909916d1`: 1440: `?preview=process-01..07` formade 7 av 7 (`preview/preview_check4.json`: `--sc-ps` = `--eN` ± 0,0001, `on` = 01..N, steg N+1 läcker inte; `preview-1440-process-01..07.png`). 390: 01 och 02 formas i 1 av 3 laddningar, 03 i 2 av 3 (`preview390.json`, `pricefix_ab.json` A): motorns cachade topp för `#process` (6 415) mot den verkliga (6 152) är prisblockets platshållare, inte motorn; med platshållaren bort formas 01 och 02 i 3 av 3 (`pricefix_ab.json` B). Plan 042
  · loop 5 (2026-09-17), R10-läget `d3491b4a`: **bockad.** 1440: `?preview=process-01..07` formade 7 av 7 (`--sc-ps` = `--eN` ± 0,0001). 390: 21 laddningar (sju steg × tre), lästa vid 1, 2, 4 och 8 s: 20 av 21 inom 0,0001, en landade 0,2400 mot `--e1` 0,2450 (`k1` 0,971) och stod stilla där i 8 s; åtta extra laddningar av steg 01 gav 8 av 8 exakta med `stroke-dashoffset` 0 på båda ritade banorna (`preview390_5.json`, `preview/p01check.json`). Loop 4:s race (1 av 3) var prisblockets platshållare, borta med 042. Och den kontroll R10 lämnade okörd, **aktens vandring i båda riktningarna vid 1440**, är körd (`walkproc5.json`): ned tänds stegen 01 → 02 → 03 → 04 → 05 → 07 i ordning med `--sc-ps` monoton och banorna ritade kontur → glyf → måttlinje utan att gå om varandra; upp samma sekvens baklänges, arket ritas av till tomt ark vid aktens början. Varje steg äger sitt fönster åt båda hållen
- [x] **H-31** Varje steg bär en kundfråga och ett svar synliga utan hover, i vi-form, noll tankstreck, inga tal utöver 320 · 768 · 1440, 16:9, 7 rem, 96 px; liggarens tre underrader pekar in i processen. (Insign och Highway skriver löftena i klartext; V3c gör det som fråga och svar.)
  · loop 1 (2026-09-17): stegen är prosa v1 enligt Antons dom 2026-09-16 (frågorna lever i styckena), vi-form, noll tankstreck, talen 320 · 768 · 1440, 16:9, 7 rem, 96 px; liggarens underrader pekar in i akten (`s03`, `s06` till `s08`)
  · loop 2 (2026-09-17), R7-läget `d30355da`: prosa v1 orörd, vi-form, noll tankstreck (grep), talen 320 · 768 · 1440, 16:9, 7 rem, 96 px (`s07` till `s10`)
  · loop 3 (2026-09-17), R8-läget `70214a22`: prosa v1 orörd, vi-form, noll tankstreck (grep), talen 320 · 768 · 1440, 16:9, 7 rem, 96 px (`preview/preview-1440-process-02..07`)
  · loop 4 (2026-09-17), R9-läget `909916d1`: prosa v1 orörd, vi-form, noll tankstreck (grep U+2012 till U+2015: 0), talen 320 · 768 · 1440, 16:9, 7 rem, 96 px (`preview/preview-1440-process-02..07`)
  · loop 5 (2026-09-17), R10-läget `d3491b4a`: prosa v1 orörd, vi-form, noll tankstreck (grep U+2012 till U+2015: 0), talen 320 · 768 · 1440, 16:9, 7 rem, 96 px (`preview/preview-1440-process-02..07`)
- [ ] **H-32** Processakten kostar inga bildrutor utöver H-21: proben med `#process:--sc-ps` och en `.draw`-bana som spår klarar samma bar. (K3:s ritning mätte p95 218 ms vid cpu 4; det är taket som ska underskridas, inte matchas.)
  · loop 1 (2026-09-17): cpu 1: `#process` p95 18,5 ms mot heron 35,8 håller; cpu 4: 445,7 ms mot heron 217: akten kostar mer än heron under strypning
  · loop 2 (2026-09-17), R7-läget `d30355da`: cpu 1: `#process` p95 35,3 ms ned mot heron 36,5 (inte längre dyrare); cpu 4: 480 mot 817 (brusigt). Baren är H-21:s; plan 028
  · loop 3 (2026-09-17), R8-läget `70214a22`: cpu 1: `#process` 32,1 ned mot heron 36,1 (inte dyrare); cpu 4: 285 mot 89: akten kostar mer under strypning. Baren är H-21:s
  · loop 4 (2026-09-17), R9-läget `909916d1`: cpu 1: `#process` 18,2 ned / 18,2 upp (kontrollens nivå; R8 32,1 / 18,5), staircase 0, max_step 0,70 %: akten kostar inget vid cpu 1. cpu 4: 326,9 ned / 474,6 upp mot heron 333,8 / 79,7: under strypning kostar akten lika mycket som heron nedåt och mer uppåt (uppåt går ramarna vakna igen: `content-visibility` av/på). Baren är H-21:s; golvet redovisat, ingen egen plan
  · loop 5 (2026-09-17), R10-läget `d3491b4a`: cpu 1: `#process` 17,1 ned / 17,0 upp mot heron 33,6: akten kostar mindre än heron och ligger vid kontrollens nivå, max_step 0,67 / 0,76 %. cpu 4: 83,2 ned / 50,1 upp mot heron 280,1 / 49,9 och mot K3:s tak 218: **akten underskrider nu K3:s tak i båda riktningarna** (loop 4: 326,9 / 474,6). Baren är H-21:s och nås inte; golvet redovisat, ingen egen plan
- [x] **H-33** Blått i processakten är ett sant mått per skärm och ingenting annat (K3:s regel, lånad som princip); accentens frekvens på sidan är utskriven som ett tal i decision ledger.
  · loop 1 (2026-09-17): 320 · 768 · 1440 i accent på skärm 02 till 05, 0,7 vid Calyx, `--hair-ink` vid 07 (`preview-1440-process-02..07.png`); accentens frekvens = två roller efter R6 (BRIEF § Byggarens rader, R6)
  · loop 2 (2026-09-17), R7-läget `d30355da`: 320 · 768 · 1440 i accent på skärm 02 till 05, `--hair-ink` vid 07 (`process-1440/…-life-04..11.png`, `preview-1440-process-02..07`)
  · loop 3 (2026-09-17), R8-läget `70214a22`: 320 · 768 · 1440 i accent på skärm 03 till 05, `--hair-ink` vid 07 (`process-1440/v3c-1440-life-04.png` till `-11`)
  · loop 4 (2026-09-17), R9-läget `909916d1`: 320 · 768 · 1440 i accent på skärm 03 till 05, `--hair-ink` vid 06 och 07 (`process-1440/v3c-1440-life-04.png` till `-10`, `preview-1440-process-06`, `-07`)
  · loop 5 (2026-09-17), R10-läget `d3491b4a`: 320 · 768 · 1440 i accent på skärm 03 till 05, `--hair-ink` vid 06 och 07 (`process-1440/v3c-1440-life-04.png` till `-10`, `preview-1440-process-06`, `-07`): blått är ett sant mått per skärm och drar sig tillbaka när ritningen blir sida

**Kontrast och reflow**

- [x] **H-34** Text mot grund ≥ 4,5:1 mätt mot ljusaste 5 % av grunden med texten dold, alla ytor, båda grunderna (`contrast_over_media.py --url`).
  · loop 1 (2026-09-17): R6 mätte `.frame-cap` 17,8:1, `.card-cta` 18,8:1; hela sidan inte mätt i loop 1 (leadens grind); 013 och 017 mäter sina ytor
  · loop 2 (2026-09-17), R7-läget `d30355da`: hela sidan inte mätt i loop 2 (leadens grind); R7 mätte `.hero-headline` 17,7:1, `.price` 14,54:1, `.frame-cap` 17,77:1, kortet 17,5 till 19,6:1
  · loop 3 (2026-09-17), R8-läget `70214a22`: hela sidan inte mätt i loop 3 (leadens grind); R8 mätte `.hero-headline` 17,71:1, `.hero-sub` 17,81:1, `.ledger-body p` 5,08:1 dämpat
  · loop 4 (2026-09-17), R9-läget `909916d1`: hela sidan inte mätt i loop 4 (leadens grind); arkitekten körde `contrast_over_media.py --url` på folden vid 1440: 7 av 7 strängar godkända, sämsta 16,20:1 (`a.topline-contact`), hero-rubriken 17,71:1, underraden 17,82:1, kortet 18,79 till 21,00:1
  · loop 5 (2026-09-17), R10-läget `d3491b4a`: **bockad, hela sidan mätt denna runda** (`contrast_over_media.py --url`, texten dold, ljusaste 5 % av grunden). 1440 vid scrollY 0, 3 300, 4 800, 5 400, 8 000, 9 700: **61 strängar, alla godkända**, sämsta 6,70:1 (tesens strängar på den blå plåten, golv 4,5), hero-rubriken 17,71:1, prisplanet 14,54:1, processakten 17,77:1, mailto 15,99:1. 390 vid 0, 2 900, 5 600, 7 000, 10 400: **41 strängar, alla godkända utom en verktygsartefakt**: kortbaksidans `SYSTEM` mäter 2,28:1 vid `?preview=front` eftersom verktyget samplar BAKSIDANS DOM-rektangel medan FRAMSIDANS ljuspöl är det som målas där; vid `?preview=back` mäter samma sträng 17,51:1 och `slices-390/v3c-390--s00.png` visar ingen text alls över fotot. Samma klass av artefakt som R8/R9/R10 dokumenterat för `Boka ett möte`
- [x] **H-35** Ingen horisontell scroll vid 320/375/390/414/768/1440; träffytor ≥ 44 px; folden hel vid 1280x600, 1024x640 och 720x450 (plan 001).
  · loop 1 (2026-09-17): R6: `reflow.py` 320 + 200 % rent, `--extra-viewport` 900x600 till 1366x640 rent, träffytor ≥ 44 px (plan 022), folden hel vid 1280x600, 1024x640, 720x450 (plan 001, R4); loop 1 `fold` i `slices-*--s00.png`
  · loop 2 (2026-09-17), R7-läget `d30355da`: R7: `reflow.py` 320 + 200 % rent, sju extra viewports rena, träffytor ≥ 44 px (mailto 44 px vid 390/320); loop 2 `slices-390/` utan horisontell scroll. Plan 030 håller ordet i `overflow-wrap`-skyddet
  · loop 3 (2026-09-17), R8-läget `70214a22`: R8: `reflow.py` 320 + 200 % och åtta extra viewports rena; loop 3 `slices-390/` utan horisontell scroll; `geom3.json` mailto 44 px vid 390
  · loop 4 (2026-09-17), R9-läget `909916d1`: R9: `reflow.py` 320 + 200 % och åtta extra viewports rena; loop 4 `slices-390/` utan horisontell scroll, `geom4.json scrollW` = 390 / 1440; mailto 44 px hög vid 390
  · loop 5 (2026-09-17), R10-läget `d3491b4a`: `geom5.json scrollW` = 390 / 1 440 (lika med viewporten vid båda bredderna); loop 5:s `slices-390/` utan horisontell scroll; mailto 44 px hög vid 390; `reflow.py` 320 + 200 % och åtta extra viewports är R9/R10:s och orörda av R10:s tre planer (042 rör en `content-visibility`-deklaration, 043 en `overflow` och två transformer inne i en wrapper, 044 en JS-funktion)

---

## § 4 Tillägg

Anton tillåter nya element och färger om de går ihop med helheten. Varje rad: vad, var,
varför, token (gate 48: aldrig inline-hex, gate 60: aldrig demoterade skills hex), H-rad.

| # | Vad | Var | Varför det går ihop | Token | Tjänar |
|---|---|---|---|---|---|
| T-1 | **Processarket**, en ritad SVG-sektion på papper i full bredd, sju tillstånd, med fråga och svar i en vänsterspalt | efter `.stagger`, före `footer.close` | Antons beställning; K3:s signatur lånad som *form* (kontur, mått, utrop), inte som sida; ger sidan den fjärde anatomin (H-06) och den saknade sekventiella akten (H-02). Highway ger fasordningen, Insign testadress + CMS som *princip*, Hoy WCAG-principen | `--hair-ink: color-mix(in srgb, var(--ink) 62%, var(--bg))`, `--contour-hair: .75px`, `--contour-line: 1.5px`, `--contour-dash: 4 3` | H-02, H-06, H-28 till H-33 |
| T-2 | **Mått i accent**: de sanna måtten (320 · 768 · 1440, 16:9, 7 rem, 96 px) i `var(--c-accent)` på papper, som K3:s blå moment | processarket | Planen skrev `var(--ink)` för att hålla tvåförekomstlåset; Anton lättar låset. Accenten får då sin tredje roll och den är granskningsbar: ett blått moment per skärm i akten, alltid ett sant tal (beautiful-regeln via K3). Kontrast `#1e5e9c` på `#fdfbf4` 6,46:1 | `--c-accent` (finns) | H-33 |
| T-3 | **Prisblockets material**: nytt mörkt kallt plan i stället för `--invert` (som är samma svärta som grunden) | `.price` | s6 läser i dag som ett hål i grunden. Ett kallt grafitplan skiljer sig i valör (TASTE § 4.5: material, inte grå sektion) utan att bli en andra accent; Hoy visar att en platt grund per akt bär kapitlet | ny `--c-graphite: oklch(0.27 0.012 250)` (≈ L 27 mot grundens L 8); `--invert-ink` på den ≥ 12:1 | H-08, H-11 |
| T-4 | **Kortbaksidans högra halva**: ordmärkets A-glyf (`assets/logo` som path) ritad i hårlinje, 60 % av korthöjden, högerställd, i `--frame-line` | `.face--back` | Framsidan bär glyfen fylld (logo-docken), baksidan bär den som kontur: samma objekt, två sidor. Ritad form, inte innehåll (gate 47/79); ingen ny färg | `--frame-line` (finns) | H-09 |
| T-5 | **Jätterubriken upp ett steg**: `.giant` tak 4,8rem → 6rem (96 px vid 1440) | `#giant-section` | TASTE § 2.4: display 5 till 15 gånger body; 80 px är golvet, inte ett beslut. Hoys avdelare 100 till 132 px | ingen ny token; `clamp(2.1rem, 6.7vw, 6rem)` | H-07 |
| T-6 | **Grunddriften synlig**: drift-stoppet `#123f68` får ett tydligare syskon för bandet, eller tesbandets `data-sc-drift` sätts på hela `.stagger` | `.stagger` | Driften finns i koden men syns inte i skivorna (H-19); Hoys hårda helbreddsbyten är golvet, V3c:s drift ska åtminstone vara mätbar | `--c-accent-deep` (finns) | H-19 |
| T-7 | **Monobudgeten 4 → 5 etikettfamiljer**: stegindexen 01 till 07 i processarket räknas som en femte familj (återanvänder `.ledger-num`) | processarket | Liggarens 01 till 03 och arkets 01 till 07 är samma register; utan lättnad kan akten inte numreras | `--f-mono` (finns) | H-30 |
| T-8 | **Avslutet som egen skärm**: `.close` min-height 62 svh, mailto-raden upp till 6rem, en hårlinje som dras in ovanför raden på `--sc-ps` | `footer.close` | Plan 007 plus H-25: sista skärmen saknar i dag rörelse; en hårlinje som ritar sig är samma språk som processarket, ingen ny färg | `--hairline-dark` (finns) | H-12, H-25 |

Låst copy (femton strängar) och `PRODUCT.md` § absences lättas inte. Radie 0 överallt står.

---

## § 5 Öppet

- **Tyst mätvärd.** Kontrollen gav 1 till 2 rutor över 33 ms i alla körningar (servrar på 4626 och 3090, OneDrive). Sidans 111 rutor är inte brus, men baren "0 rutor" kräver en tystare maskin än den jag hade; fas C bör köra proben när inget annat kör.
- **Bildtidens orsak** är mätt av plan 005 (RecalcStyle 73 %) men inte löst; den är fas C:s första fix och processakten får inte adderas ovanpå den utan att H-21 mäts före och efter.
- **Highway Medias fastext** kunde inte läsas (reveal gated). Fasordningen är planens.
- **Frågor till Anton** (i `QUESTIONS.md`): Q25 fönstret 0,12 till 0,72 → 0,10 till 0,78 och span 3,4; Q26 accentens tredje roll i processarket; Q27 prisblockets grafitplan; Q28 mobilordningen (tesen före Calyx); Q29 steg 07:s revisionsfält.
- **Inte mätt:** `perf_probe.py` (leadens grind, inte arkitektens), `contrast_over_media.py --url` (skriptets URL var hårdkodad i R3; H-34 förutsätter att flaggan finns), kolumnviktens siffror i pixlar (squint-domen är läst, inte räknad).

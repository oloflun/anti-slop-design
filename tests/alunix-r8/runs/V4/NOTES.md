# Alunix V4 · R1 · "Markören" — NOTES

Bygge: `tests/alunix-r8/runs/V4/index.html`, port 3308, servad från repo-roten.
Modell: Opus, inga subagenter. Webbläsare: headless, en i taget, via `browser_lock.py`.

## 1. Lästa underlag (referensgolvet)

- `design-catalogue/TASTE.md`, `design-catalogue/FEEDBACK.md` (F-001–F-027), `ANTON-VISION-OCH-FEEDBACK.md`
- `skills/design/references/reference-lock.md`, `chain-discipline.md`, `house-physics.md` (Structural)
- `references/scroll/` README, grammars, devices, feel-and-fingerprint, toolchain, `showcase-floor.md`,
  `journeys/era-residence.md` (som mall för hur en resa byggs, formen inte lånad)
- Fingerprint-registret i valvet (`wiki/projects/_index/design-fingerprints.md`), alla 36 rader
- Katalogval: `select.py --k 3 --wildcard` (uteslutna: aspensearch-com, cyphr-studio, exoape-com,
  area17-com, planhat, era-residence, collabcapitolium, forgeautomotive-co, filmbot, huehaus) →
  **vistal, bleibtgleich, example, pp-frama**; entry.md + fold.webp lästa för alla fyra, plus
  design-language-extrakten för vistal och example (de två som har ett)
- Rörelseark med `motion_floor: 2`, lästa som bild: **bleibtgleich, nodeck, sadumedia**
- Skills: design, lenis, gsap-core, gsap-scrolltrigger, gsap-timeline, gsap-plugins
  (+ `references/splittext.md`), gsap-performance; copywriting, copy-editing, humanizer-svenska
- V3g R9 (`runs/V3g/index.html`): `pkg-desc` och processtegen; skärmbild 1440 lästa som bild

## 2. Referenslås (F-024: en dominerande, minst två lån, vad som tas ur varje)

```text
Build target: approved reference lock (detta block), ingen målbild
What must not drift: papper + bläck + EN accent som yta; en grotesk; axeln; markören som tråd; ramarna orörda efter visning

Primary reference/direction: bleibtgleich (motion_floor 2, typographic poster, modern clean)
Preserve: korta påståenden förskjutna på en lodrät hårlinjeaxel i stället för centrerade; en enda grotesk familj i alla roller;
          introt där en linje dras och namnet sätts på den; gles komposition där typen ensam bär
Borrow only: (A) nodeck: verktyget ur varumärkets egen värld torkar skärmen, och samma gest markerar orden;
             (B) example (weareexample) + sadumedia: arbetet sitter i rubrikens mellanrum, och listans aktiva rad tänds medan resten står grå
Role rules: accenten (markeringsblå) är bara markering: en yta som växt ur ett svep, eller `::selection`; aldrig knapp, aldrig textfärg.
            Bläck är text och markör. Grafit är sekundär text på papper och kommande processteg.
Media strategy: product surface (de två levande sajterna i iframe, samma origin). Inga foton.
Reject: dither, cellnät, kort som vänds, Geist, mint (V3f/V3g); smeared-ink-reveal (bleibtgleich, gör ord oläsliga i rörelse);
        nodecks deck-navigering och rosa; sadus kondenserade versaler; exampels roterade foton; centrerad hero; jättesiffror
Token commitments: paper oklch(97.6% .004 250) · ink oklch(18% .012 262) · graphite oklch(46% .012 262) ·
                   select oklch(86% .07 248) (accent, bara som yta) · select-ink oklch(30% .05 258) (sekundär text på blått) ·
                   ash oklch(76% .008 262) (sekundär text på bläck) · rule oklch(18% .012 262 / .12) ·
                   type: Switzer Variable 100–900, en fil; display 300 / brödtext 400 / etikett 500;
                   radius 0 överallt; inga skuggor; pricing: ledger (hårlinjerader, namn vänster om axeln, beskrivning höger)
```

**Vad varje källa ger, per kategori:**

| Källa | Intro | Övergångar | Signaturobjekt | Typ | Media |
|---|---|---|---|---|---|
| **bleibtgleich** (dominant) | linjen dras, namnet sätts på den: **tas**, men linjen är en markör som först blinkar | (inget lånat) | hårlinjeaxeln: **tas** som markörens andra form | en grotesk, förskjutna rader på axeln: **tas** (Switzer i stället för Akzidenz) | (inget lånat, korten i ringen lämnas) |
| **nodeck** (lån A) | (lämnas) | verktyget torkar skärmen: **tas** som markeringen som sveper | överstrykningspennan → **markören och markeringen** (eget objekt ur byråns värld) | (lämnas, tjock kontur) | (lämnas) |
| **example / sadumedia** (lån B) | (lämnas) | (lämnas) | (lämnas) | (lämnas, kondenserat) | **arbetet i rubrikens mellanrum**: namnet glider isär och den levande sajten växer fram mellan orden; sadus grå→bläck-lista **tas** för processen |
| pp-frama (vald, inte lån) | — | — | — | — | blekblått "technical sheet"-kapitel bekräftar att en ljusblå yta bär en typaffisch; inget annat |
| vistal (vald, inte lån) | — | hård färgfältsklippning **lämnas** (vi kräver en materiell orsak) | — | — | — |

Tillgänglighetsbrister i referenserna som inte följer med: bleibtgleichs smetade ord (oläsliga mitt i
rörelsen), nodecks grå småtext, sadus cookie-bar och blixtrande ljusa sektioner.

## 3. Beslutslogg

| Beslut | Källa | Roll | Varför |
|---|---|---|---|
| Typographic poster, modern clean | grammars.md × register; bleibtgleich | grammatiken bär sidan | en byrå vars tillgång är meningen; nio chaptered editorial-rader redan tagna |
| En grotesk: Switzer Variable | bleibtgleich (en familj); lokal fil i repot | röst + register i samma familj, roller via vikt | 43 kB, en fil, å ä ö ō finns; Geist är V3:s |
| Hårlinjeaxel, förskjutna rader | bleibtgleich | layoutroll: varje akt står på samma axel | sidan läses som ett dokument; axeln är också markören |
| Markören som återkommande objekt | nodeck (verktyget ur världen) | signaturobjekt, golvregel 3 | byråns material är text som skrivs |
| Markeringsblå som enda accent, som yta | nodeck (gula svep) → eget material | accent: bara markering | den blå besökaren känner igen från egen markering |
| Scrollen skriver meningen | eget (signaturdraget) | golvregel 4: ett påstående styrt av scrollen | tell-someone-meningen |
| Processen som en lång rad förbi markören | sadumedia (aktiv rad tänd) + era (passage på annan axel) | passagen, golvregel 4 | sju steg är en sekvens; raden glider förbi skrivhuvudet |
| Namnet glider isär runt den levande ramen | example + sadumedia (arbete i ordmellanrummet) | golvregel 5: typ och media i samma ram | toppen; ramen går att använda |
| Ramarna avslöjas en gång, scrubbas aldrig | PRODUCT.md, F-021 | ramens roll: användbar | "en ram som visats transformeras eller tonas aldrig" |
| Paket som ledger på axeln, inga priser | V3g `pkg-desc` (godkänd), F-017 | pricing: ledger | Antons beslut R9: beskrivning i stället för pris |
| Mejl fast i nederkanten | stress-personan | nav | den enda handlingen ska alltid gå att nå |
| **Minnesvärd detalj** | eget, ur nodeck-principen | scrollen skriver och raderar | det besökaren berättar efteråt |

## 4. Övergångarna (golvregel 2), fem olika materiella orsaker ur byråns material

| # | Mellan | Orsak | Material |
|---|---|---|---|
| T1 | hero → tes | markören drar en markering från axeln till högerkanten, sedan fyller den höjden | text (markering) |
| T2 | tes → process | radbrott: den blå ytan delas på höjden, övre halvan upp, undre ned, processen i springan | text (radbrott) |
| T3 | process → exempel | markören byter till blockläge och växer till hela vyn i bläck | markören (överskrivning) |
| T4 | exempel → paket | bläcket smalnar till en mobilbred spalt och sedan till en hårlinje | skärmen (brytpunkt) |
| T5 | paket → kontakt | markeringen tar raderna en i taget nedåt och blir kontaktens yta | text (markering rad för rad) |

Aldrig samma orsak två gånger i rad. T1 och T5 delar material (markering) men inte riktning eller
form (sidled över hela vyn mot rad för rad nedåt) och står fyra övergångar isär.

## 5. Copy (tre pass, i ordning)

Pass körda som skills: `copywriting` → `copy-editing` (sju svep) → `humanizer-svenska`.
Låst copy orörd. Processtegen och `pkg-desc` är V3g R9:s godkända texter.

| Sträng | Efter alla tre pass | Ändring och skäl |
|---|---|---|
| 01 Design | Formen tar vi fram ur er verksamhet, aldrig ur en färdig mall. | passiv "tas fram" → aktiv (copy-editing); negativ parallellism "…, inte …" omskriven (humanizer) |
| 02 Utveckling | Vi skriver koden från grunden, så att sidan laddar snabbt. | |
| 03 System | Bokning, betalning och kunduppgifter, kopplade till sidan. | tre "Vi" i rad varierade (copy-editing) |
| Kontakt | Skriv några rader om vad ni gör. Vi svarar med förslag på ett första samtal. | nästa steg tydligt, stämmer med processteg 01 och paketraden (zero risk-svepet) |
| Calyx 1 | Fotot får första skärmen / Blommor väljs med ögonen innan någon läser ett pris. Därför får fotot hela första skärmen och knappen får vänta. Omslaget ger också ateljén ett skäl att byta bild varje säsong, och då känns sidan ny utan att byggas om. | "äger" (anglicism) → "får" (humanizer) |
| Calyx 2 | Veckans utbud på en rad var / (V3g R9, oförändrad) | |
| Hōrai 1 | Ett namn, en gång / Namnet står ensamt och stort. Loggan i menyraden väntar tills det har rullat förbi, för ett namn som syns två gånger samtidigt väger mindre. | "ingen skylt mot gatan" struken: står inte i horai.html (F-023); meningslängd varierad (humanizer) |
| Hōrai 2 | Priset står större än namnet / (V3g R9, oförändrad) | |

Faktakoll mot källkoden (F-023, F-027 § 4): Calyx `.hero-photo h-[88vh]` = fotot är första skärmen;
Calyx `<!-- INDEX: a typeset price list -->` = utbudet på en rad var med pris; Hōrai `h1 … 15rem`
+ `#logo.logo-hidden` medan namnet syns = "ett namn, en gång"; Hōrai pris `clamp(3.8rem,7vw,6rem)
text-lacquer` mot menynamn `clamp(2.6rem,4.6vw,4.4rem)` och "one menu a night" = "priset står
större än namnet".

## 6. Beslutslogg under bygget (R1, i ordning; varje rad bygger på en bild eller mätning)

| # | Fynd (källa) | Ändring |
|---|---|---|
| 1 | Processens läshuvud löpte som linje genom brödtexten (walk-1440/104) | läshuvudet är en markör i stegnumrens radhöjd; blocket växer ur den |
| 2 | Stegtexten för liten för vyn (walk-1440/104) | steg 29vw, h3 clamp(24–42), brödtext clamp(16–21) |
| 3 | Case-texter hängde på axeln, tom yta under namnet (walk-1440/164) | linjerade mot ramens kanter (22vw) |
| 4 | Sidan 16,9 vh (walk.json) | kortare pins; nu 14,9 vh på 1440 (13 365 px), 14,1 vh på 768, 14,2 vh på 390 |
| 5 | Hjulet fastnade i Calyx-ramen på 390/768 (walk-390: 127 steg, slutade vid Calyx) | ramen släpper igenom scrollen tills besökaren klickar ("Använd sidan här"); lämnar läget vid pekarutgång eller när ramen lämnar vyn |
| 6 | Heron tunn på 768 (walk-768) | axeln i vänsterkanten under 900 px, rubrik upp till 104 px |
| 7 | Tom pappersvy i ~1 vh efter radbrottet (alunix-v4-self, första fångsten) | processen ligger bakom tesen (negativ marginal, tesen överst); rubriken reser sig i springan |
| 8 | Bläcket stod tomt i drygt en vy efter blocket (samma ark) | kortare håll, exempel-padding 12→4 vh, avslöjandet vid 78 % |
| 9 | WCAG 1.4.12: "Er hemsida" utanför vänsterkanten, paketrubrik krockar med ingress, mobilheron krockar med tjänsterna (textspacing.json) | r1 får brytas, ingressen flödar under rubriken, mobilheron i flex-flöde |
| 10 | SplitText-maskerna ligger kvar och klipper | `revert()` när avslöjandet är klart (husreceptet) |
| 11 | axe `aria-prohibited-attr` på `span` (SplitText aria:auto) | aria:none; meningen scrollen skriver har en `.sr-only`-kopia, synliga tecken `aria-hidden` |
| 12 | Saknade landmärken (banner, navigation, contentinfo) | hopplänk "Hoppa till kontakt" (nav), mejlfliken som `<header>`, sidfoten utanför `<main>` |
| 13 | Tabb in i en ram: ingen ring, ingen scroll, ramen ännu inte avslöjad (focus-4.png) | `focused`-klass via `blur`, scroll till ramen via Lenis, avslöjandet körs; ringen var klippt av kvarlämnad inline `clip-path` (pixel y=101 efter fix) |
| 14 | Calyx öppnades som vit ruta: lat laddning startade vid avslöjandet (walk-1440) | ramarna laddas på idle när introt är klart; ommålad ram är bläck, inte vit |
| 15 | Exempel-sektionen p95 35–53 ms (probe 2–4) | avslöjandet med `clip-path` på ramen ersatt av två bläckluckor som skalas med `transform`; p95 18,7/18,8 ms (probe 5–6) |
| 16 | review-animations: linjär färgövergång, ogatad hover | `.24s var(--ease-out)`; hover under `(hover: hover) and (pointer: fine)` |

## 7. Golvet, regel för regel (showcase-floor.md § 2)

Underlag: sidans eget ark `design-catalogue/entries/alunix-v4-self/motion/sheet.webp` bredvid
`bleibtgleich`, `nodeck` och `sadumedia` (floor 2), plus hjulvandringarna i `shots/walk-*`.

| # | Regel | Uppfylld? | Belägg |
|---|---|---|---|
| 1 | Intro och hero är ett skott | **Ja** | introremsan: 0,4 s och 1,7 s en blinkande markör på tomt papper, 2,7 s står rubriken på samma linje, nu sträckt till axel. Markören består över överlämningen. |
| 2 | Varje sektionsbyte har en materiell orsak, ≥ 3 olika, aldrig samma två gånger i rad | **Ja, 5** | T1 markering (sidled) · T2 radbrott · T3 blockmarkör · T4 brytpunkt (bläck → mobilbred spalt → axel) · T5 markering rad för rad. Alla ur byråns material (text, markör, skärm). Ingen 14 px-tonning som övergång. |
| 3 | Ett signaturobjekt återkommer och förändras | **Ja** | markören i sju former: blink, axel, markeringskant, skrivhuvud, läshuvud, block, väntande markör efter adressen. Ramens första sliver när luckorna öppnas läses som samma vita streck. |
| 4 | Text i läsfart; ett påstående styrt av scrollen; rubrik hel och stilla ≥ 40 vh | **Ja** | SplitText `mask:'lines'` på hero, tes, process, kontakt. Scrollen skriver "Vi hjälper er att synas på rätt sätt." tecken för tecken. Stilla: hero 0,42 × 1,35 vh ≈ 57 vh, tesens rubrik hela pinnen (1,9 vh), processens rubrik hela panoreringen, paketrubriken 0,48 × 1,0 vh ≈ 48 vh, kontakten står sist. |
| 5 | Typ och media delar ram | **Ja** | "Calyx [levande sajt] florist", "Hōrai [levande sajt] krog": namnet glider isär och sajten växer fram i mellanrummet. |
| 6 | Husets utjämning | **Ja** | central `smooth-scroll.js` (lerp .075, wheelMultiplier .6, respectReducedMotion false, anchors true, autoRaf false), gsap.ticker enda RAF, lagSmoothing(500, 33), `scrub: true` på alla scrubbade tidslinjer; ingen numerisk scrub. Import bara via `/gsap.js` och `/smooth-scroll.js`, importmap mot `node_modules` (länkat 3.15.0 / 1.3.26), ingen CDN, ingen kopia. |
| 7 | Ingen grind | **Ja** | introt avslutas vid första scroll eller tangenttryck. |

Pinregler: fyra pins (hero, tes, process, paketrubrik), skapade en gång vid init, aldrig dödade.
Inga iframes ligger i en pinnad scen, så ingen `pinSpacer` behövs; ingen `refresh()` från en
ramens `load`. Varje animerad egenskap har en ägare (ägarkontrollen nedan).

Mot de två floor-2-arken, ärligt: V4 når golvet på alla sju regler. Det når inte nodecks
lekfullhet eller sadus filmtyngd, och ska inte; det är en typaffisch. Svagast är processakten,
som är korrekt men lugn: sju textkolumner som glider förbi en markör.

## 8. Mätvärden (slutversionen, headless, en webbläsare i taget via `browser_lock.py`)

Varje kontroll redovisar sitt trasiga fall (chain-discipline M3) där ett sådant går att bygga.

| Kontroll | Resultat | Trasigt fall / kontroll |
|---|---|---|
| `section_probe.py`, hela sidan, `shots/section-probe-5.json` och `-6.json` | p95 per sektion: top 18,2/18,8 · tes 18,2/18,3 · process 18,2/18,3 · exempel 18,7/18,8 · paket 18,3/18,3 · kontakt 18,3/18,2 ms. Alla ≤ 20 ms. `frame-calyx` 1 och `frame-horai` 1 laddning. 0 refresh. 0 fails. | Proben flaggade själv exempel-sektionen på 35–53 ms (pass 2–4, före GPU-luckorna). Tidigare under dagen gav maskinen 25 ms i varje sektion; V3g mätt samtidigt gav också 25 ms (`control-v3g-probe.json`), så den nivån var maskinens. Exempel har kvar 13–15 bildrutor > 33 ms per pass, när de två sajterna målas första gången. |
| Brief-kopia: `shots/section-probe.json` | den första körningen (25 ms-golvet), sparad för spårbarhet | se ovan |
| Hjulvandring 1440×900 / 768×1024 / 390×844 (`shots/walk-*`, `v4_shots.py`, 100 px per hjulsteg, musen mitt i vyn) | 0 egna konsolfel (enda varningarna är Tailwind-CDN inuti sajterna); en laddning per ram; sidan går hela vägen på alla tre (218 / 234 / 196 steg). Längd 14,85 / 14,1 / 14,2 vh. | Före ramfixen fastnade 390 och 768 i Calyx-ramen (127 resp. 148 steg, Hōrai laddades aldrig). |
| 320×640 kontakt (`v4_textspacing.py`) | ingen klippning, inget utanför skärmen, 0 px horisontell scroll; `shots/textspacing/320-contact.png` läst | |
| WCAG 1.4.12 textavstånd, 1440 och 390, sju lägen var (`shots/textspacing/textspacing.json`) | 0 klippt, 0 utanför skärmen, 0 överlapp (panoreringsspårets steg undantagna: de nås genom scroll) | en 40 px bred `overflow:hidden` runt "är nutidens" ger 1 träff. Första versionen av proben gav 0 här och kasserades. |
| axe (`a11y_scan.py`, 1440 + 390) | sista körningen: `color-contrast` på heron på 390, med nodernas egen stil `opacity: 0; translate3d(0, 6.26px, 0)`, alltså mitt i introts tonning. axe efter att introt är klart (`v4_axe_settled.py`, 6 s): **0 överträdelser** på 1440 och 390. Körningen innan gav också 0 (40 passes). | Försöket att återskapa tonningsträffen på 3,1 s lyckades inte (introt startar efter `fonts.ready`, axe tar själv tid), så orsaken vilar på nodernas stil, inte på ett återskapat fall. CARL: fixturen `tests/a11y/broken.html` ger kontrast, alt, landmärken och region. |
| `tab_walk.py` | 8 stopp, alla i vyn: hopplänk, mejlflik, logotyp, Calyx-ramen, "Öppna Calyx", Hōrai-ramen, "Öppna Hōrai", adressen. Kvar: `order_mismatch` (den fasta mejlfliken längst ned, och scrollen mellan stoppen: heuristik) och `no_focus_indicator` på iframe-elementet. Ringen ligger på ramen, mätt i pixlar: ljus rad på y=101, ramkant y=109 (`shots/a11y/focus-6.png`). | CARL: fixturen ger positiv tabindex, saknad ring och oåtkomlig klickyta |
| `reflow.py` | `unrevealed` 0. `overflow320`/`overflowZoom200` flaggar processpåret: den horisontella panoreringen, by design. Innehållet nås genom vertikal scroll, ingen tvådimensionell scroll för läsaren. | CARL: fixturen ger överflöd vid 320 och 1 oavslöjat element |
| `contrast.py` | **Inte kört.** Skriptet är hårdkodat mot `localhost:3055` och kraschar mot andra adresser. axe:s `color-contrast` täcker kontrasten. | |
| F-027 ägare: hjul till botten (12 465 px) och upp, mät vid scrollY 0 (`shots/roundtrip.json`) | 0 skillnader: axelns läge och klippning, markering, tesens halvor, spåret, bläcket, spalten, radmarkeringarna, rubrikraderna, skrivna tecken | axeln flyttad 120 px ger 1 skillnad |
| `microtext_scan.py --names` | 0 kandidater | självtest PASS |
| `self_reference_scan.py` (F-018) | 0 kandidater | självtest PASS: F-018-meningen flaggas |
| Tankstreck i synlig text och attribut | 0 em, 0 en | |
| Sidans rörelseark `alunix-v4-self` (40 bildrutor) | GSAP 3.15.0, Lenis, 4 pins, 0 WebGL, en font (Switzer); läst bredvid bleibtgleich, nodeck, sadumedia | 40 bildrutor räcker till Hōrai; resten av sidan läst i `shots/walk-*` |

Brief-täckning mot den renderade sidan: 1 vad byrån gör (hero, tre tjänster) · 2 tesen ·
3 sju processteg · 4 Calyx och Hōrai live i iframe, rörs aldrig efter avslöjandet (luckorna
ovanpå skalas, ramen själv har ingen transform, klippning eller opacitet) · 5 tre paket med
V3g:s `pkg-desc` och "Vi lämnar pris efter första samtalet." · 6 "Mejla oss" + `kontakt@alunix.se`
som mailto, både i den fasta fliken och i kontakten. Alla sex finns.

Kvar att säga rakt:
- Exempel-sektionen har 13–15 bildrutor över 33 ms per pass, när sajterna i ramarna målas
  första gången. p95 håller; enstaka hack kan synas där på en svagare dator.
- Grå (`--graphite`) kommande processteg har 6:1 mot papperet. De läses, men skillnaden mot
  bläck är tydlig främst genom att stegen tänds i tur och ordning.
- Rubriken "Från samtal till / lanserad sida." har ett stort hopp mellan raderna på desktop
  (axelns förskjutning); det är systemet, men det är den svagaste kompositionen på sidan.

## 9. Föreslagen registerrad (läggs i valvet först efter godkännande)

| Build | Grammar | Nav treatment | Hero device | Act-sequence shape | Close pattern | Signature move | Register | World / palette | Path |
|---|---|---|---|---|---|---|---|---|---|
| Alunix V4 R1 Markören | Typographic poster | No bar: logo mark in flow at the head of the axis (scrolls away); a fixed ink mail tab bottom-left ("Mejla oss" + address) that hides when the address itself is on screen; skip link to contact on focus | Blank paper; a caret blinks twice and stretches into a full-height hairline axis; the headline set staggered on both sides of it; no image | 7 acts + 5 material transitions, ~14–15 vh: timed caret door > pinned hero > selection sweep (sideways) > pinned scroll-typed thesis > line break opening onto the process > horizontal process pan past a caret on the number row > block caret floods to ink > two names parting around a live site (once-reveal, GPU covers) > ink narrows to a phone column, then to the axis > package ledger on the axis > selection row by row into the contact ground | Selection-blue ground, heading on the axis, "Mejla oss" + address at action size with the caret blinking after it; the page ends the way it began | The scroll types a sentence character by character and deletes it on the way back up; the caret recurs as axis, selection edge, typing head, reading head, block | Modern clean | Switzer Variable only; paper oklch(97.6% .004 250), ink oklch(18% .012 262), graphite oklch(46% .012 262), one accent: selection blue oklch(86% .07 248) used only as a surface | `anti-slop-design/tests/alunix-r8/runs/V4/index.html` |

Delar med tidigare rader: grammatiken med r1 K3, r2 R6, r6 A-K2, r6 B-K2, r7 B-K2. Det nästa
Alunix-bygget ska undvika: markören som tråd, markeringsblå som yta, hårlinjeaxeln med
förskjuten rubrik, scroll-skriven text.

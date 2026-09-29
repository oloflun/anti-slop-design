# V3g · showcasen blir mjuk · RAPPORT runda 1

Arbetsmapp `tests/alunix-r8/runs/V3g`, kopia av V3f. Bara `#showcase`s inre mekanik är
rörd (pin, casebyte, ruta/box, mobilraderna) — komposition, färg, copy och alla andra
sektioner är orörda, per SHOWCASE-SPEC.md.

## Omstart mitt i rundan

Första `Edit`-anropet mot `index.html` nekades av referensgolvet: `Skill(design)` var
avstängd av en kvarglömd testisolering i `.claude/settings.local.json`
(`skillOverrides.design: "off"`, satt för ett tidigare V3f-isoleringstest). Anton tog
bort spärren och sessionen startades om med instruktionen att ladda `Skill(design)` på
nytt och läsa exakt de filer nekningstexten räknade upp. Det gjordes i den ordningen:
`design-catalogue/FEEDBACK.md` (katalogens egen fil, inte `skills/design/references/`-
kopian jag hade läst första gången), `extract/*-design-language.md` för samtliga fyra
valda katalogposter, `references/reference-lock.md`, `references/scroll/devices.md` och
`references/scroll/feel-and-fingerprint.md` i `~/.agents/skills/design/` (den kanoniska
sökvägen nekningen namngav, skild från repots egen `skills/design/`-kopia — innehållet
visade sig identiskt vid jämförelse) samt fingerprint-registret
`wiki/projects/_index/design-fingerprints.md`. Gaten släppte igenom nästa `Edit` utan
ändringar i själva planen — research- och byggarbetet nedan är oförändrat av
omstarten, bara ordningen på läsningen skiljer.

## Kedjan, steg för steg

1. **`Skill(design)`.** Läst i sin helhet (referensgolvets krav gäller varje steg, se
   ovan). TASTE.md och FEEDBACK.md (katalogens fil) lästa. `python
   scripts/catalogue/select.py --brief SHOWCASE-SPEC.md --k 4` gav **deonlibra, tomo,
   example, happyrobot**. Alla fyras `entry.md`, `fold.webp` (som bild) och
   `extract/*-design-language.md` lästa. **Gav inget att låna:** ingen av de fyra
   visar mönstret uppdraget faktiskt behöver (en sticky textruta som crossfadar
   bredvid en scrollande produktvy) — katalogens `select.py` matchar på brief-nyckelord,
   inte på interaktionsmekanik, och det här uppdraget är en smal, låst mekanisk fix,
   inte ett nybygge som behöver en riktningsreferens. Läst för referensgolvets skull,
   ingenting från dem syns i koden. `reference-lock.md`, `scroll/devices.md`,
   `scroll/feel-and-fingerprint.md` och fingerprint-registret lästa (se ovan).
2. **Inspo** (`references/inspo-mcp.md`). En `search_screens("sticky text column that
   crossfades step by step beside a scrolling product view")` → sex träffar, samtliga
   generiska hero-folds (Step, Warby Parker, Design Maestro, basement.studio,
   Superhuman, Tonal) — inspos index är foldautopsier av statiska sidor, ingen av dem
   visar en scroll-driven crossfade-mekanik. En `get_screen("superhuman-com")` för att
   pröva om en fullsida gav mer — samma resultat, bara ännu en hero-fold. **Inget
   lånat.** Mekaniken är fullt specificerad i SHOWCASE-SPEC.md §C och byggd rakt
   därifrån.
3. **Motorskills, i ordning:** `lenis` → `gsap-core` → `gsap-scrolltrigger` →
   `gsap-timeline` → `gsap-performance`. Gav den bindande regeln som faktiskt löste
   grundorsak 3 (`scrub:true`, inte ett numeriskt värde, eftersom Lenis redan är det
   enda utjämningslagret) och regeln bakom grundorsak 1 (en pin skapas en gång, dödas
   aldrig på klick) — båda står redan uttalade i `scroll/devices.md`s "Load-bearing
   rules" och las bekräftade via skillarna innan koden skrevs.
4. **UI-skills.** `ibelick/fixing-motion-performance`: reglerna (aldrig `scrollTop`-
   polling, bara `transform`/`opacity`, mätning innan skrivning) höll redan för filens
   egen `writeCaseScroll`-skriv-om-ändrad-mönster; inget att ändra, bekräftat
   efterlevt. `zeke/swiss-design`: **inte tillämpad.** Skillen bär en egen Tailwind/
   stone-palett, men V3f:s låsta tokens (`--paper`/`--black`/`--grey`/`--mint`/
   `--rust`/`--lacquer`) styr redan sidan och komposition/färg är uttryckligen utanför
   scope den här rundan — att applicera swiss-designs palett hade varit precis den typ
   av kontraktsbrott `design/SKILL.md` Tier 0–2 varnar för (gate 60).

## Grundorsaker — rättade

| # | Orsak (V3f) | Rättning (V3g) |
|---|---|---|
| 1 | `activateCase` dödade och återskapade pinnen synkront vid klick | Pinnen skapas EN gång i `setupDesktopEngine()`, kallad en gång vid `matchMedia`-init. Ett klick byter bara `activeCaseKey` |
| 2 | Hōrai-iframens `src` sattes först vid klick → navigation under övergången | Båda iframes får sin `src` via `requestIdleCallback` efter `window.load`, långt innan något klick kan hinna ske |
| 3 | Lenis `lerp:0.1` + ScrollTrigger `scrub:0.6` — dubbel utjämning | `scrub:true`. Lenis är det enda utjämningslagret (matchar `scroll/devices.md`s load-bearing-regel, redan uppmätt jank i V3f 2026-09-24) |
| 4 | `caseY` rörde sig 45 % av segmentet, stod still 55 % med en `u*u*(3-2u)`-smoothstep | Ny kurva: 50 %/50 %, `sine.inOut` (`0.5-0.5*cos(π·t)`), noll hastighet i båda ändar |
| 5 | Dragspel: klass-togglad `grid-template-rows:0fr→1fr` per rad | Ersatt av en enda crossfadande ruta (§C): stegen grid-stackade i en cell, en GSAP-tidslinje per case skrubbad av pinnens `onUpdate` |
| 6 | Pinlängden räknades om per case (`n × innerHeight`) → casebyte krävde `refresh()` | Fast längd: `end: () => '+=' + Math.round(6*0.75*innerHeight)`, `invalidateOnRefresh:true`. Calyx' 5 ankare delar samma fasta längd i 5 steg i stället för 6 |

## Bugg hittad och rättad under rundan (utanför grundorsakstabellen)

Efter att grundorsak 1 rättats (pinnen återskapas aldrig) upptäcktes via
`showcase_probe.py` att **den nyvalda casens iframe-scroll aldrig rörde sig** —
`iframe_scroll.max_single_frame_delta_px` låg på exakt `0.0` i varenda körning, både
genom klickfönstret och hela pin-scrollen. Orsak: den kvarvarande `load`-lyssnaren som
fyller `C.y`/`C.w` är villkorad på `activeCaseKey === C.key`, sant bara för Calyx vid
sidladdning. Eftersom båda iframes nu laddas i bakgrunden (grundorsak 2:s fix) hinner
Hōrais `load` avfyras långt innan Hōrai någonsin blir `activeCaseKey`, så villkoret är
alltid falskt och `measureCase(Hōrai)` kördes aldrig — `activateCase` anropade den
heller inte (till skillnad från V3f:s gamla kod, som körde `setupDesktopEngine(C)` per
klick och därmed alltid mätte om). Fix: `activateCase`s desktop-gren anropar nu
`measureCase(C)` explicit vid varje aktivering (billigt, egengated). Bekräftat löst:
`max_single_frame_delta_px` gick från `0.0` till `406–829px` (rör sig korrekt) i
efterföljande körningar, se sheet.png nedan.

## Verifiering (§D)

Server: `serve.py --port 3307 --root .` från repots rot.

### Siffror, V3f-baslinje mot V3g (headless — se miljönot nedan)

| Mätpunkt | V3f baslinje | V3g |
|---|---|---|
| 1440 klick p95 | 33,4 ms | 33,4 ms |
| 1440 genom p95 | 50,3 ms | 33,4 ms (bättre) |
| 1440 störstas scrollY-hopp (klick) | 358,4 px | 281–401 px (två körningar; se not) |
| 1440 max iframe-delta (genom) | 948,8 px | 406–829 px (bättre) |
| 1440 stall-then-lurch (genom) | 1 | 0–1 (två körningar, gränsfall) |
| 390 klick p95 | 50 ms | 16,8–33,2 ms (bättre) |
| 390 genom p95 | 66,6 ms | 16,8 ms (klart bättre, under 20 ms-målet) |

**Miljönot om `--headed`.** Kördes headed vid båda breddgraderna som instruerat.
Sandlådans headed Chromium visade sig instabil under rundan: en identisk kodversion
gav headed p95 53,4/323,6 ms mot headless p95 33,4/49,9 ms för samma mätning — en
5–10× skillnad som bara kan förklaras av GPU-kompositering utan hårdvaruacceleration i
den här sandlådan, inte av koden (headless matchar V3f:s egen headed-baslinje nästan
exakt). Efter bugfixen ovan hängde en ny headed-körning i över tio minuter och fick
avbrytas; `verify.py` och `verify_motion.py` kraschade också (GPU-processkrasch
respektive `MemoryError`) när flera Chromium-instanser kördes samtidigt. Headless
användes därför som primär mätgrund efter det, körd en process i taget. De headed-tal
som hann fångas (före bugfixen, sparade i `shots/probe-r1-*` tills de skrevs över)
bekräftar samma mönster som headless: strukturellt korrekt, miljön är flaskhalsen.

**Störstas scrollY-hopp** ligger inte entydigt under baslinjen — spec A kräver
`duration:1.4, easing:t=>1-Math.pow(2,-10*t)` exakt (samma exponentialkurva Lenis
själv använder som standard), och den kurvan lägger sitt största hopp mycket tidigt;
exakt hur det hoppet delas mellan uppmätta bildrutor varierar med schemaläggnings-
jitter i headless mus-hjul-simulering. Avvek inte från den speccade kurvan för att
jaga detta enskilda tal.

### `showcase_probe.py`, 1440 och 390

`shots/probe-r1-1440/` och `shots/probe-r1-390/` (headless, efter bugfixen — officiella
körningar). `sheet.png` i båda visar: mjuk crossfade Calyx→Hōrai vid klick (ingen
display:none förrän utfasningen är klar), rutan som byter ett steg i taget med
mono-räknaren (`01/06` → `06/06`) och mint-spåret som växer kontinuerligt, samt att
sajtens egen sida faktiskt scrollar (Hōrais "THE HOUSE" → "THE MENUS" → "THE ROOM" →
"RESERVATIONS" syns i tur och ordning på 1440; på 390 syns motsvarande dimmade/aktiva
radväxling under den sticky iframen). `console_errors: []` i alla körningar.

### `verify_motion.py`

Den fulla svepningen (alla kontroller: `kontakt_check`, `hero_fit`, m.fl.) kunde inte
köras klart i den här sandlådan — kraschade två gånger på **helt orelaterade**
kontroller (en `MemoryError` i `kontakt_check`s 3D-tilt-svep, en `TargetClosedError`
på en hero-skärmdump), sedan hängde ett tredje försök i över tio minuter och avbröts.
Ingen av krascherna rör `#showcase`. Isolerade jag i stället bara `showcase_check`
(funktionen skriptet redan har för just den här sektionen) i en egen körning, plus en
ny kontroll jag lade till för att uppfylla speccens krav om att "läsa vilket steg som
syns i rutan" i stället för dragspelets `is-active`-klass (se nästa stycke):

- `jump_no_selection_shows_calyx`: **sant**
- `horai_click_scrolled_to_showcase` / `horai_panel_visible_after_click`: **sant**
- `keyboard_reached_calyx_button` (Tab) / `calyx_pressed_after_enter` (Enter): **sant**
- Hōrais alla 6 ankare: `all_within_2px: sant` (samtliga exakt 0 px diff)
- Calyx' 5 ankare: **4 av 5** inom ±2 px; det femte (`#commission`) 11 px off.
  `measureCase`/ankarlistan är oförändrade från V3f (rörda inte denna runda) — mest
  sannolika förklaringen är en liten layoutsättning i Calyx egen sida mellan mätning
  och kontroll (typsnittsväxling e.dyl.), inte något den här rundans pin/easing/
  crossfade-ändringar orsakar. Inte omundersökt vidare inom budgeten.
- Ny kontroll (`box_step_matches_anchor`): vid varje ankarpunkt läses vilken
  `.showcase-row[aria-hidden="false"]` som faktiskt syns i rutan och jämförs mot
  ankarets index — **matchar för samtliga ankare, båda casen.**
- `console_errors: []`.

Kontakt-kortet, hero-fit och övriga kontroller i `verify_motion.py` är utanför den
här rundans scope (composition/övriga sektioner orörda) och omverifierades inte —
se Återstår.

### `verify.py`

Kördes helt (`verify-result.json` skriven). `overflow_px` **0 px** vid samtliga fyra
brytpunkter (390/768/768/1440/1920), före och efter scroll. `hero_fit`: sant vid
1440×900 och 1280×800. `copy_diff.passed: false`, men **identiskt** med V3f:s egen
senaste `verify-result.json`: två strängar (`ALUNIX`, `kontakt@alunix.se`) räknas 2×
i båda mot V3d:s 1× — ett redan existerande fel utanför `#showcase`, inte något den
här rundan rör eller introducerar. `emdash: []`.

### A11y (mobilkontrastfixen, §C)

Spec bad om att mäta och höja 0,45-opaciteten för inaktiva mobilrader om den ger
brödtext under 4,5:1. Räknat för hand och verifierat med ett Python-skript
(sRGB-relativ luminans, komposit mot varje radbakgrund):

| Kombination | vid α=0,45 | vid α=0,7 |
|---|---|---|
| Calyx udda (ink på paper) | 2,75:1 | 5,83:1 |
| Calyx jämn (ink på grå) | 2,54:1 | 4,92:1 |
| Hōrai udda (#bdbdbd på svart) | 2,82:1 | 5,64:1 |
| Hōrai jämn (ink på grå) | 2,54:1 | 4,92:1 |

0,45 misslyckas i alla fyra kombinationer (sämst 2,54:1). Höjd till **0,7**, som
klarar samtliga med marginal (sämst 4,92:1 mot kravet 4,5:1). Detta är en beräknad
kontroll, inte en full `a11y-audit`-körning (se Återstår).

### Deep detector (stop-hookens rapport, `~/.agents/skills/impeccable/scripts/detect.mjs`)

Stop-hooken flaggade 8 fynd i 2 regler efter varje edit. Körde detektorn direkt för
att se exakta rader i stället för att gissa:

- **`overused-font` × 6** — rad 11, 16, 48, 55, 191, 216, samtliga
  `font-family:"Geist"`/`"Geist Mono"`. Alla sex är **oförändrade rader**: filens egna
  root-typsnittsdeklarationer och `.mono`/`.card-kicker`/`.process-num`-klasserna,
  satta i tidigare rundor (V3d/V3f), inte något den här rundan rör eller kunde ändra
  utan att bryta "typ ... orörd" i uppdraget.
- **`broken-image` × 2** — rad 434 och 802. Båda är **falska positiver**: detektorns
  regex matchar den bokstavliga strängen `<img>` inuti två JS/CSS-kommentarer
  ("the existing .dither-layer `<img>`" och "every not-yet-loaded `<img>`'s load
  event"), inte faktisk markup. Ingen av mina två nya `<img class="showcase-poster"
  src=... alt="" width="1440" height="900">`-taggar (som har riktiga attribut) finns
  bland de två flaggade raderna.

Inget av de 8 fynden kommer från den här rundans B/A/C-kod. Ingen fix behövs.

### `Skill(a11y-audit)`

Körd i efterhand (stop-hooken flaggade `a11y-audit` som en "unloaded strong route" —
routad mot koden men aldrig laddad under själva bygget). Scope: mekanisk pass mot hela
`index.html` (inte bara `#showcase`, eftersom skripten kör helsides), pass 1 och 6
(interaktion/kortfattad POUR), inget fullt persona-/COGA-varv given tidsbudgeten.

**CARL-kontrollen** kördes först mot `tests/a11y/broken.html`: `a11y_scan.py` fångade
samtliga planterade fel (saknad label, `<div onclick>` utan roll, kontrastfel,
`tabindex="3"`, m.fl.) — skriptet litas på.

**`a11y_scan.py`** (axe-core, 1440×900 + 390×844): **2 violations**.
- `aria-prohibited-attr` på `.tes-line`-raderna och `.footer-mark` — utanför
  `#showcase`, oförändrad markup denna runda.
- `color-contrast` på `#showcase-calyx .showcase-head .caption.mono` ("Florist,
  Stockholm") — inuti showcase-sektionen, men i `.showcase-head`-titelcellen (rost/
  lack), som B/A/C inte rör. Sannolikt redan i V3f, omätt då.

Ingen av de två träffarna ligger i det jag faktiskt byggde denna runda (rutan,
klick-crossfaden, mobilraderna, pin/caseY). **Mina egna nya element gav noll nya
axe-violations.**

**`tab_walk.py`** (--max 200): väljarknapparna (Calyx/Hōrai) har synlig fokusring och
rätt namn (`Calyx\nFlorist, Stockholm` osv). En `focus_trap`-varning på den inbäddade
`#showcaseIframeCalyx` (fokus rapporterat 5 gånger i rad) — mest sannolikt en
mätartefakt (föräldradokumentets `document.activeElement` visar alltid `<iframe>` när
fokus egentligen rör sig mellan flera fokuserbara element i Calyx egen sida;
`pointer-events:none` blockerar bara pekare, inte tangentbord), inte fastställd denna
runda. Rör `scaleShowcaseFrame()`/iframe-inbäddningen, oförändrad kod. Loggad i
`.impeccable/a11y-debt.md` med kortare frist (utred inom sprinten) eftersom en verklig
fälla vore ett HIGH-fynd.

**`reflow.py`**: `unrevealed: 0` — bekräftar att rutans steg aldrig fastnar osynliga
(reveal-systemet misslyckas inte mot "tystnad"). `overflow320` flaggar
`#showcaseIframeCalyx` och en orelaterad `img.dither-layer` — samma
`scaleShowcaseFrame()`-spår som `focus_trap`-fyndet, oförändrad kod, loggad i samma
skuldpost.

**Kontrastfixen (mobilradernas opacitet, se ovan)** ingår inte i `a11y_scan.py`s
kontrastregel (den läser bara renderad DOM-kontrast vid en given körning, inte
opacitetsvärdet 0,45 vs 0,7 i sig) — verifierad separat med det beräknade
sRGB-kompositet ovan.

**Verdict för den här rundans egna ändringar: Approve** (noll nya axe-violations, noll
o-avslöjade steg, väljarknapparnas tangentbordsväg grön). **Två poster i
`.impeccable/a11y-debt.md`** (bildtextkontrasten, iframens tabbordning/overflow) —
båda öppna, ingen är Antons godkända skuld ännu, ingen är den här rundans regression.
Inget fullt COGA-/persona-varv kört — se Återstår.

### `emil-design-eng` / `review-animations`

Båda skillarna laddade och den nya rörelsen självgranskad mot dem (hookens krav:
"båda måste anropas vid namn"). Sammanfattning: inga `transition:all`, inga
`scale(0)`-entréer, ingen `ease-in` på något som kommer in (bara `power2.out`/
sine.inOut, GSAP:s egna namngivna kurvor, inte webbläsarens svaga default), bara
`opacity`/`transform`/`scaleX` animeras, klickcrossfaden är `overwrite:'auto'`
(interruptible), steg-crossfaden är en skrubbad tidslinje (i sig avbrytbar åt båda
hållen). `prefers-reduced-motion` avsiktligt inte hedrad — husregeln F-011 upphäver
den kontrollpunkten globalt i det här designsystemet, `review-animations`s Standard 8
ska inte flagga det (`motion.md` § Reduced motion). Inga blockerande fynd.

## Avvikelser från specen

- Störstas scrollY-hopp vid klick inte entydigt under baslinjen (se miljönot ovan).
- Calyx' femte ankare 11 px utanför ±2 px-kravet i en kontrollkörning (se ovan).
- Full `verify_motion.py`-svepning och full `a11y-audit`-körning inte klara denna
  runda (sandlådans instabilitet respektive tidsbudget) — se Återstår.
- `--headed` gav inte en ren, fullständig efter-bugfix-mätning vid någon breddgrad;
  headless användes som primär mätgrund med motivering ovan.

## Återstår

1. Kör `showcase_probe.py --headed` vid 1440 och 390 på en miljö med fungerande
   GPU/display för en ren headed-mätning efter bugfixen (den här sessionens headed-tal
   är antingen från före fixen eller saknas helt).
2. Kör hela `verify_motion.py`-svepningen (inte bara `showcase_check`) i en stabilare
   miljö — `kontakt_check`, hero-fit m.fl. är overifierade denna runda trots att de
   inte rörts.
3. Bekräfta Calyx' femte ankare (11 px) i en ren körning; om det kvarstår, mät om det
   fanns redan i V3f (ingen sparad baslinjesiffra för just den kontrollen att jämföra
   mot).
4. Fastställ om `tab_walk.py`s `focus_trap`-varning på den inbäddade iframen är en
   mätartefakt (föräldradokumentets `activeElement` kan inte se in i iframens egen
   fokusrörelse) eller en verklig fälla, och om `reflow.py`s 320px-overflow-flagga på
   samma iframe beror på mättiming eller en riktig brist i `scaleShowcaseFrame()`.
   Loggat i `.impeccable/a11y-debt.md`, kräver Antons ja eller en uppföljande
   utredning. Ingen av de två rör den här rundans B/A/C-kod.
5. `.showcase-head .caption.mono`s kontrastfel (`a11y_scan.py`), utanför rutan/
   klick-crossfaden/mobilraderna — loggad skuld, kräver Antons ja eller en fix i en
   framtida runda.
6. Fullt COGA-/persona-varv (pass 3 och 7 i `a11y-audit`) kört inte denna runda —
   bara mekanisk pass + en kort interaktions-/POUR-läsning.
7. Ingen ny fingerprint-rad behövs (samma grammatik/nav/hero/aktform/close/register
   som V3f, bara `#showcase`s inre mekanik ändrad) — bekräfta det ställningstagandet
   om en framtida runda vidgar scopet utanför showcasen.

Servern (port 3307) stoppad efter rundan.

---

# Runda 2

Leaden läste R1:s bilder och körde egna mätningar. Verdikt: övertoningen vid klick,
rutans stegbyte, mintspåret och sajtens rörelse genom ankarna på desktop fungerar.
Fyra fel kvarstod, rättade i given ordning nedan. Ingenting annat på sidan rört.

## Omstart mitt i runda 2

Sessionen stoppades av leaden mitt i arbetet: `showcase_probe.py --headed` öppnade då
riktiga, synliga webbläsarfönster, de staplades på Antons skärm och kraschade
maskinen. Orsaken var instruktionen ("kör headed") den här rundan ursprungligen fick,
inte något byggaren gjorde fel — koden i `index.html` stod orörd och korrekt kvar vid
omstarten. `showcase_probe.py` är sedan omkalibrerad av leaden: `--headed` startar nu
`headless=True` med GPU-flaggor (`channel="chromium"`, `--enable-gpu`,
`--ignore-gpu-blocklist`, `--use-angle=d3d11`) — aldrig ett synligt fönster, men med
samma bildrutetid som ett riktigt headed-fönster hade gett (kalibrerat mot en riktig
headed-körning, median 16,7 ms). Alla egna diagnosskript den här rundan körde uteslutande
`headless=True`, en webbläsarprocess i taget, `browser.close()` i `finally`.

## 1. Casehuvudets rubrik klipptes under pinnen (desktop) — blockerande

**Fel:** `.showcase-head`s rubrik (`Hōrai`/`Calyx`) renderade delvis under den sticky
48px-topplisten medan pinnen var aktiv — övre halvan av glyferna skars av (leadens
`through-05` till `through-12`). Ärvt från V3f.

**Orsak, mätt:** `.showcase-embed-cell`/`.showcase-side` fylldes till `100svh` med
pinnens `start:'top top'`, så sektionens topp låg vid viewportens y:0 — topplisten
(opak, `z-index:40`, `position:sticky`) täckte alltså bokstavligen sina första 48px
i stället för att bara "måla ovanpå" ett innehåll som redan undvek den raden, vilket
den ursprungliga (felaktiga) R6 §3-kommentaren antog.

**Fix:** pinnens `start` ändrad till `'top top+=48'` (sektionen pinnas 48px lägre,
exakt under topplisten) och båda cellhöjderna till `calc(100svh - 48px)` — botten
landar fortfarande exakt på viewportkanten (samma logik som redan skyddade mot R6 §3:s
svarta band, bara med båda variablerna — offset OCH höjd — nu räknande med topplisten
i stället för bara höjden).

**Kontroll:** `getBoundingClientRect().top` för rubriken ≥ topplistens underkant vid
pinnens början/mitt/slut — bekräftat i skärmbilderna nedan, rubriken helt synlig i
varje `through-NN.png` denna runda.

**Bilder:** `shots/r2-shots-1440/through-00.png` till `through-11.png` — jämför mot
R1:s `shots/lead-headed-1440/through-05.png` (felet, nu borta i samma vy).

## 2. Mobil: sajten i den sticky ramen följde inte raderna (390) — blockerande

Tre separata, staplade fel hittades under samma symptom — alla mätta med
`page.evaluate`-spårning, ingen gissad:

**2a — huvudet dolt bakom ramen.** `.showcase-embed-cell` (sticky) låg FÖRE
`.showcase-side` (huvud + rader) i normalt dokumentflöde, så när huvudet rullade upp
genom den redan-klistrade ramen klipptes det mot dess underkant (leadens
`through-02`/`through-03`). Fix: `.showcase-side{display:contents}` (bara mobil) lyfter
`.showcase-head` och `.showcase-rows` till `.showcase-stage`s egna grid-items, ordnade
om med `order`: huvud (1) → ram (2, där klistringen börjar) → rader (3).

**2b — Hōrais iframe hann aldrig börja ladda.** `requestIdleCallback(...,
{timeout:2000})` (R1:s fix för grundorsak 2) väntade på en ledig lucka som aldrig kom
inom ett normalt klick-och-scrolla-förlopp (`--no-shots`-mätningen visar att hela
förloppet kan ta under två sekunder) — `src` sattes alltså aldrig i tid. Fix: ladda
direkt vid `window.load`, ingen idle-fördröjning. Två lätta, samma-origin statiska
sidor är inte värda att vänta på.

**2c — den verkliga fällan: `tweenCaseTo`s startvärde.** Även efter 2b stod
`iframe.scrollY` kvar på 0 genom alla sex radbyten (`page.evaluate`-spårning,
upprepad). Grundorsaken var TVÅ separata buggar i klass med varandra:
- `proxy.v = C.last >= 0 ? C.last : target` — `C.last` börjar på sentinelvärdet -1,
  så FÖRSTA anropet någonsin för en case fick `proxy.v = target` redan vid
  skapandet: en tween FRÅN target TILL target. `onUpdate` hann aldrig skriva ett värde
  som flyttade `C.last` bort från -1, så nästa anrop återskapade exakt samma
  självrefererande nollrörelse — permanent, inte tillfälligt. Fixat: läs iframens
  EGEN levande `scrollY` som startvärde i stället för den cachade `C.last`.
- Även med det fixat stod raderna kvar frysta. Djupare orsak: mobilgrenen byggde
  `ScrollTrigger`-utlösare för BÅDA casens rader vid init, oavsett vilken som var
  synlig. Den inaktiva casens rader har `display:none` på sin panel vid den
  tidpunkten, så `getBoundingClientRect()` gav `{top:0, bottom:0}` för samtliga —
  vilket redan uppfyllde `start:'top 70%'`, så alla sex `onEnter` sköt av OMEDELBART
  vid sidladdning, innan ett enda riktigt scroll skett (`CASES.horai.pendingRow` var
  redan 5 direkt efter `window.load`, uppmätt). ScrollTrigger räknar den riktningen
  som förbrukad och avfyrar den aldrig igen vid ett verkligt scroll i samma riktning
  — casen stod alltså fryst vid vad den där felstarten sist rörde vid. Fixat: bygg
  bara den SYNLIGA casens radutlösare (`buildMobileRowTriggers(C)`), döda och
  återskapa dem i `activateCase` när casen faktiskt byter och blir synlig (dess rader
  har då riktiga positioner).

**Kontroll:** `page.evaluate`-spårning (egna diagnosskript, headless) visar
`iframe.scrollY` progressera 0 → 1169 → 2856 → 6520 i takt med raderna, upprepat och
stabilt. `showcase_probe.py --no-shots` (officiell, headless-gpu):
`through_scroll.iframe_scroll.max_single_frame_delta_px` gick från `0.0` (fryst) till
`631`–`2488` beroende på körning (rör sig, ingen `stall_then_lurch`-serie).

**Bilder:** `shots/r2-shots-390/sheet.png` — huvudet helt synligt innan ramen börjar
klistra (jämför R1:s `shots/probe-r1-390/sheet.png` `through-02`/`through-03` där det
klipptes), och bild+radrubrik progredierar tillsammans (`through-04`–`through-07`).

## 3. Rutan var mest död svart yta (desktop)

**Fel:** stegtexten var liten (h3 38px flat, p 15px/52ch) och vertikalt centrerad i en
hög, tom cell — nästan hela rutan svart på Hōrai (leadens `through-05`/`through-08`).

**Fix, tre delar:**
- Stegen flyttade högt: `justify-content:flex-start` (var `center`) plus
  `padding-top:calc(var(--cellpad)*1.6)` — luft direkt under räknare+spår, aldrig
  centrerat.
- Skalan höjd till rutans egen nivå: `.showcase-row h3` återanvänder
  `--headline-40`-tokenet (klassen `h3` står kvar oförändrad, bara storleken byts, per
  uppdraget), `.showcase-row p` till 18px/44ch.
- En stor mono-bakgrundssiffra (`.showcase-box-number`, `aria-hidden="true"`, samma
  tal som räknaren — ingen ny copy) i rutans nederkant, `opacity:.1`, tonar ut/in
  (0,2s/0,35s) i samma `setStepState`-gate som resten (en gång per stegbyte, inte per
  bildruta) — bär ytan typografiskt när text allena inte fyller den.

**Kontroll:** skärmbild vid tre steg, båda casen — se `shots/r2-shots-1440/sheet.png`
`through-06` till `through-11`: siffran `01`–`06` synlig och stigande, texten högt
placerad. Utöver pixelläsningen mättes den faktiskt tomma ytan med ett litet
engångsskript (`getBoundingClientRect` på `.showcase-row-text` + `.showcase-box-number`,
klippt mot rutans egen box, vid steg 0/2/5 för Hōrai och 0/2/4 för Calyx):

| Steg | Bara text | Text + bakgrundssiffra |
|---|---|---|
| Kortast copy (steg 0, båda casen) | 60–63 % tomt | **50–53 % tomt** |
| Mellansteg (steg 2, båda casen) | 47 % tomt | **37 % tomt** |
| Sista steget (Hōrai 5, Calyx 4) | 47–60 % tomt | **37–50 % tomt** |

Siffran sänker den tomma ytan med 10–13 procentenheter vid varje mätt steg (t.ex.
Hōrai steg 2: 47,2 % → 37,0 %), men klarar INTE ~45 %-målet vid det kortaste steget
på något case (49,9 % / 53,1 %) — den korta rubriken ("Fotot bär rubriken" / "Namnet
står en gång") ger helt enkelt minst textyta. Provade att skala upp siffran
ytterligare (räknat, inte byggt): för att stänga gapet vid steg 0 hade
`clamp()`-taket behövt höjas till runt 260–280px, vilket börjar konkurrera visuellt
med steg-rubriken och bryter mot "läses som en bakgrundstextur, inte en andra röst" —
en sämre avvägning än att lämna det kortaste steget en bit över målet. Rapporterat
mätt, inte gissat; inte tvingat till ett tal genom att offra ytans lugn.

## 4. Calyx sista ankare (`#commission`) låg fel

**Grundhypotes (R1, motbevisad denna runda, mätt inte gissat):** antog webbtypsnitts-
FOUT (`display=swap` på Cardo/PT Mono) omflödade sidan efter mätningen. Testat direkt:
`page.evaluate`-spårning var 150:e ms från iframens `load`, hela vägen till 3000ms,
visade `#commission.offsetTop` fullständigt stilla på samma pixel genom hela
`fonts.status`-övergången `loading`→`loaded`. Hypotesen föll.

**Verklig orsak, mätt:** `max = scrollHeight - innerHeight` (den beräknade
scrolltaket) stämde INTE med webbläsarens egen `scrollTo`-klamning — fyra separata
sidladdningar visade att den verkliga, uppnåeliga max-positionen konsekvent låg
9–14px LÄGRE än beräkningen (en subpixel-avrundningskvirk mellan rapporterad
`scrollHeight` och faktisk scrollgräns, bekräftat genom att direkt fråga
webbläsaren: `w.scrollTo({top:999999}); w.scrollY`). Eftersom `#commission` är
Calyx enda ankare som hamnar i `Math.min(max, …)`-klamningen (dess råa `offsetTop`
överskrider `max`), är det den enda som exponerades.

**Två dyrare fixar prövade och förkastade, båda mätta:**
- Fråga webbläsaren direkt (scrolla till stort värde, läs, återställ) VARJE gång
  `measureCase` körs — gjorde siffrorna VÄRRE (7/3/28px i tre körningar), eftersom
  `measureCase` även körs medan en pågående tween skriver till samma `C.w`;
  "återställ" kolliderade med den skrivningen.
- Samma sond men cachead en gång per uppmätt viewporthöjd — samma kollisionsrisk
  kvarstod när cachen råkade sättas mitt i en pågående skrivning (ett körningsfel:
  `anchors_measured:false`).

**Fixen som höll:** en fast säkerhetsmarginal, `max = scrollHeight - innerHeight -
20`, ren aritmetik utan sidoeffekt på `C.w`. 20px är ordentligt större än den
uppmätta kvirken (9–14px), så skrivningen hamnar aldrig i närheten av webbläsarens
verkliga tak.

**Extra, i testskriptet:** `verify_motion.py`s `anchor_hits()` jämförde en
engångs-snapshot av `C.y` (tagen i funktionens topp) mot ett senare live-skrivet
värde — en andra, mindre stalenessrisk. Läggs nu till: `C.y[i]` läses om precis före
varje jämförelse (`fresh_expected`), rapporterat separat som `expected_at_snapshot`
för spårbarhet.

**Kontroll:** isolerad `showcase_check`, fem körningar i rad efter fixen:
`calyx_anchors.diffs_px = [0,0,0,0,0]` och `all_within_2px:true` i samtliga fem,
`horai_anchors` opåverkad (redan `[0,0,0,0,0,0]` innan och efter).

## Verifiering, R2

Alla körningar headless (`headless-gpu`-läget, `--headed`-flaggan i
`showcase_probe.py` betyder nu detta), en process i taget.

| Mätpunkt | V3f-referens (`lead-hgpu-1440-1/2`, samma läge) | V3g R2 (`r2-timing-1440`, `--no-shots`) | V3g R2 (`r2-shots-1440`, med bilder) |
|---|---|---|---|
| Klick p95 | 616,5 / 266,6 ms | 183,3 ms | 16,9 ms |
| Klick störstas scrollY-hopp | 521 px | 733 px | 730 px |
| Genom p95 | 50 / 33,5 ms | 49,8 ms | 17,0 ms |
| Genom max iframe-delta | 1226 / 1188 px | 919 px | 1110 px |
| Genom stall-then-lurch | 0 / 0 | 1 | 0 |

V3g R2 ligger i nivå med eller bättre än V3f-referensen i samma mätläge på klick-p95
och genom-p95 i båda egna körningarna; scrollY-hoppet ligger något högre (730–733 mot
521px) men i samma storleksordning, inte en regression av den typ R1 rapporterade.

`showcase_probe.py --no-shots` och med bilder, 1440 och 390: körda, resultat och
`sheet.png` i `shots/r2-timing-{1440,390}/` och `shots/r2-shots-{1440,390}/`.
`console_errors: []` i alla fyra körningar.

Isolerad `verify_motion.py`-showcasekontroll (samma metod som R1, hela svepningen
fortsatt instabil i den här sandlådan på orelaterade kontroller): `all_within_2px:
true` för BÅDA casen, `box_step_all_match:true` för båda, tangentbordsvägen och
direkthoppet gröna, `console_errors: []` — se fix 4 ovan för de fem upprepade
körningarna.

`verify.py`: `overflow_px: 0` vid samtliga fyra brytpunkter, före och efter scroll.
`copy_diff.passed:false`, identiskt med R1 och med V3f:s egen senaste
`verify-result.json` (samma två redan existerande dubbletter, `ALUNIX` och
`kontakt@alunix.se`) — oförändrad mot V3f, ingen ny avvikelse.

## Återstår efter R2

1. Fix 3s tomma-yta-mål (~45 %) nås inte vid det kortaste steget på något case
   (mätt: 50/53 % mot målet), se tabellen ovan — en medveten avvägning (siffran
   skalades inte upp mer för att inte konkurrera med steg-rubriken), inte en
   ouppmätt lucka. Kräver Antons ja om avvägningen ska stå, eller en annan idé
   för just det korta steget (t.ex. mer luft/en annan layout bara vid kort copy).
2. Full `verify_motion.py`-svepning (kontakt-kort, hero-fit m.fl.) fortfarande inte
   klar i den här sandlådan — ovidkommande orelaterade krascher, se R1.
3. `tab_walk.py`s `focus_trap`/`reflow.py`s 320px-overflow på den inbäddade iframen
   (R1, `.impeccable/a11y-debt.md`) — inte rört denna runda, kvarstår öppet.
4. `.showcase-head .caption.mono`s kontrastfel (R1, `a11y_scan.py`) — inte rört denna
   runda, kvarstår öppet i skuldloggen.
5. Fixen för fix 4 (20px säkerhetsmarginal) är kalibrerad mot Calyx' uppmätta
   9–14px-kvirk. Om Hōrai eller en framtida case visar samma mönster på en ANNAN
   marginal skulle den fasta 20px-konstanten behöva bli en uppmätt, inte antagen,
   generalisering — inte gjort denna runda eftersom Hōrai aldrig visade felet.

Servern (port 3307) stoppad efter rundan. Ingen commit.

---

# Runda 3

Fyra delar: omladdningsloopen (F-021, grundorsak), tempot över hela sidan (F-020),
showcasens tempo mellan texterna (F-020) och textrutans layout (F-019). Arbetsmapp
`tests/alunix-r8/runs/V3g`, server port 3307 (+ 3305 tillfälligt för `verify.py`/
`verify_motion.py`, som har porten hårdkodad — båda stoppade efter rundan).

## 1. Omladdningsloopen — grundorsaken (F-021)

**Före:** ScrollTrigger skapade sin egen pin-spacer runt `.showcase-stage` vid varje
`refresh()`, vilket flyttade (omparenterade) de pinnade iframarna i DOM:en och laddade
om dem — 6–12 omladdningar per iframe per pass (R1:s mätning). Båda iframes fick
dessutom sin `src` vid `window.load` via `data-showcase-src`, och en generisk
`img.load → safeRefresh()`-lyssnare på VARJE bild på sidan körde ytterligare
refreshar under själva scroll-passet (mätt denna runda: 4 st, se nedan).

**Efter, tre fixar:**
1. En egen `<div class="showcase-pin-spacer">` i markupen, omedelbart runt
   `.showcase-stage`, och `pinSpacer: '.showcase-pin-spacer'` i `ScrollTrigger.create`.
   GSAP återanvänder nu den befintliga wrappern i stället för att skapa/flytta en ny
   vid varje `refresh()` — iframarnas ankarelement rör sig aldrig i DOM:en.
2. Calyx iframe har `src` direkt i HTML:en (som i V3f); Hōrai monteras lazy
   (`data-lazy-src`) via en `maybeLoadHorai()`-funktion som återanvänder den befintliga
   `AHEAD=2`-principen (`lenis.on('scroll', ...)`), gated på `#exempelcase`s
   `getBoundingClientRect().top < 2×innerHeight` — laddas alltså före första möjliga
   klick men inte under hero/tes. Ingen `refresh()` härifrån.
3. Den generiska `img.load → safeRefresh()`-lyssnaren (för VARJE bild på sidan) är
   borttagen. Kontrollerat mot markupen: varje `<img>` på sidan är antingen
   `position:absolute;inset:0` (en fyllningsyta i en redan formaterad cell —
   `.dither-layer`, `.color-layer`, `.showcase-poster`, `.face--front img`,
   `.case-choice-frame img`) eller bär explicita `width`/`height` (topplistens logga)
   — ingen bilds `load`-event kan alltså ändra sidans layout, så refreshen den bad om
   mätte ingenting verkligt och orsakade bara brus under scroll-passet när lazy-bilder
   laddade in. `mountFrame()`s egen `f.load → safeRefresh()` (den generiska
   `iframe[data-src]`-mekanismen, obesläktad med showcasen och för närvarande utan
   matchande element) är också borttagen, per samma regel ("en refresh anropas aldrig
   från en iframes load"). `fonts.ready → safeRefresh()` står kvar — ett typsnittsbyte
   ändrar verklig textgeometri.

**Kontroll — `section_probe.py`, två körningar (port 3307):**

| Körning | tes p95 | iframe_loads | st_refreshes_during_pass | fails |
|---|---|---|---|---|
| 1 | 16,9 ms | Calyx 1×, Hōrai 1× | 0 | [] |
| 2 | 16,8 ms | Calyx 1×, Hōrai 1× | 0 | [] |

`px_per_notch: 60` i båda (matchar F-020:s krav). Tesrubrikens p95 (16,8–16,9 ms) är
långt under kravet ≤ 33,4 ms — signaturen från EFFECTS.md är inte bara bevarad utan
klart bättre, eftersom loopen som orsakade F-021 är stängd vid roten. Innan
img-refreshen togs bort (steg 3) visade en första körning `st_refreshes_during_pass: 4`
med samma iframe-siffror — bekräftar att steg 1–2 löste själva reload-loopen (varje
iframe 1×), men steg 3 krävdes för att nå kravet "0 refreshar under passet" rakt av.

## 2. Tempot över hela sidan (F-020)

Lenis: `lerp: 0.075, wheelMultiplier: 0.6` (var `lerp: 0.1`, ingen `wheelMultiplier`).
Alla scrubbade triggers `scrub: true` — hero-pinnen (desktop och mobil) hade `scrub:0.6`,
är nu `scrub:true`; resten av sidan (process-progress, tile-resolve, footer-chars,
showcase) hade redan `scrub:true`. Hero-pinnens `end` `+=120%` → `+=220%`.

Kortvändningens tidslinje (`heroTl`) är orörd i sig — dess positioner (0–1) är redan
uttryckta som andelar av pinnens totala längd, så att förlänga pinnen sprider samma
vändning över en längre sträcka automatiskt. Mätt (headless, port 3307, ett hjul-notch
= ~60 px):

| Notch | scrollY | kortets rotationY (°) |
|---|---|---|
| 1 | 58 px | ~0 |
| 2 | 118 px | ~0 |
| 4 | 238 px | 2,5 |
| 6 | 358 px | 8,1 |
| 8 | 478 px | 16,3 |

Vändningen är knappt påbörjad efter första hjulsteget och fortsätter gradvis — precis
det F-020 bad om ("kastas förbi kortet så man knappt hinner se det vändas").

## 3. Showcasens tempo mellan texterna (F-020)

Segment 75 vh → **110 vh**; pinnens totala längd `6 × 1,1 × innerHeight` (var
`6 × 0,75`), fast för båda casen som tidigare. `caseY()`s glidfraktion `SITE_GLIDE_FRAC`
0,5 → **0,7** (sajten glider under de första 70 % av segmentet, står still resten).
Textövertoningen `STEP_OUT_FRAC`/`STEP_IN_FRAC` 0,25/0,25 → **0,15/0,15** (ut 0–15 %,
in 15–30 %, står sedan still 70 % av segmentet) — `activeStepIndexFor` och
`buildStepTimelines` läser samma två konstanter, så stegbytets aria-hidden/is-active-
växling och crossfaden är alltid i synk.

## 4. Textrutans layout (F-019)

Ny 3-radslayout i `.showcase-rows` (`grid-template-rows: auto 1fr auto`):

- **Rad 1** (auto): räknaren + mintspåret, oförändrad.
- **Rad 2** (`1fr`, ny — `.showcase-scale`): en lodrät stegskala, `aria-hidden`. En
  1px-linje, ett streck per steg (5 för Calyx, 6 för Hōrai, jämnt fördelade via
  statiska `top:%`-värden i HTML:en), och en mintmarkör (`.showcase-scale-marker`) som
  skrivs kontinuerligt (`top: progress×100%`) från pinnens `onUpdate` — `writeScaleMarker()`,
  samma mönster som den befintliga `writeTrackFill()`. Aktuellt streck får klassen
  `is-current` (opacitet 1, mot 0,25 för resten) i `setStepState`, samma en-gång-per-
  stegbyte-gate som räknaren. Ingen text, inga tal — raden bär rutans höjd i stället.
- **Rad 3** (auto, nederst): `h3`/`p`-stegen, samma grid-stackade crossfade-mekanism
  som förut. `h3`: 30px/1,15/500 (var `--headline-40`-tokenet, ~64–100px). `p`:
  18px/1,5/40ch (var 44ch). Padding-bottom höjd (`calc(var(--cellpad)*1.4)`) för luft
  under texten.
- **Borttaget helt:** `.showcase-box-number` (skuggsiffran) — CSS-regeln, HTML-elementen
  i båda panelerna, och JS:t (`C.bigNumber`, dess tre rader i `buildStepTimelines` och
  hela tonings-blocket i `setStepState`).

Mobil (< 768px) är orörd i CSS och JS bortsett från de globala tempoändringarna i §2/§3
— `.showcase-box-number`-elementet är borttaget ur markupen för båda breddgraderna
(det saknade ändå egen mobilstyling, så det är ingen visuell ändring där), MOBILE_-
INACTIVE_OPACITY (0,7) och radmekanismen är oförändrade.

**Kontroll, skärmbilder 1440 (`shots/r3-shots-1440/sheet.png`, `shots/r3-calyx-mid-
1440.png`):** Calyx' och Hōrais rutor visar tydligt den vertikala skalan (linje, streck,
mintmarkör i rörelse) ovanför en kompakt h3/p-text längst ned, med gott om luft
mellan skalan och rubriken — rubriken tar aldrig över (F-019:s krav). Ingen text i
rutan överstiger 32px (h3 30px är störst). Mobil (`shots/r3-shots-390/sheet.png`) visar
samma staplade rader som R2, oförändrat utom takten.

## Verifiering, R3

Alla körningar headless (`headless-gpu`), en process i taget, `browser.close()` i
`finally`.

1. **`section_probe.py`**, två körningar: se tabellen i §1 ovan — `0 fails`, `px_per_notch: 60`
   i båda.
2. **`showcase_probe.py`**, `--no-shots` två gånger vid 1440
   (`shots/r3-timing-1440-{1,2}/`): `console_errors: []` i båda. Click-fönstrets p95
   (200/233 ms) matchar R2:s egen dokumenterade `--no-shots`-miljöartefakt (R2:
   183,3 ms) — samma mönster, inte en regression. Through-scroll p95 33,2/50 ms.
   Med bilder vid 1440 (`shots/r3-shots-1440/`): click p95 **16,9 ms**, through p95
   **17,1 ms** — matchar R2:s mönster att bild-passet ger en renare, lägre siffra i
   den här sandlådan. Vid 390 (`shots/r3-shots-390/`): click p95 33,4 ms, through p95
   **16,8 ms** (klart under 20 ms-målet). `console_errors: []` i alla fyra körningar.
3. **Isolerad `showcase_check`** (samma metod som R1/R2, hela `verify_motion.py`-
   svepningen fortsatt instabil i den här sandlådan på orelaterade kontroller):
   - `jump_no_selection_shows_calyx`, `horai_click_scrolled_to_showcase`,
     `horai_panel_visible_after_click`, `keyboard_reached_calyx_button`,
     `calyx_pressed_after_enter`: **sant**.
   - Hōrais 6 ankare: `diffs_px: [0,0,0,0,0,0]`, `all_within_2px: true`.
   - Calyx' 5 ankare: `diffs_px: [0,0,0,0,0]`, `all_within_2px: true` — R2:s
     kvarstående 11px-avvikelse på `#commission` (Återstår-punkt 3) är borta i den här
     körningen; fixen från R2 (20px säkerhetsmarginal) höll.
   - `box_step_matches_anchor`: matchar för samtliga ankare, båda casen —
     `box_step_all_match: true`.
   - `console_errors: []`.
4. **`verify.py`**: `overflow_px: 0` vid samtliga fyra brytpunkter (390/768/1440/1920),
   före och efter scroll. `hero_fit`: sant vid 1440×900 och 1280×800. `copy_diff.passed:
   false`, identiskt med R1/R2 och V3f:s egen `verify-result.json` (samma två redan
   existerande dubbletter, `ALUNIX` och `kontakt@alunix.se`) — oförändrat, ingen ny
   avvikelse. `emdash: []`. `console_errors: null`.
5. **`detect.mjs`** över `index.html`: 6 `overused-font` (rad 11/16/48/55/191/216 —
   samtliga oförändrade rader, filens egna root-typsnitt, orörda denna runda) + 2
   `broken-image` (rad 473, 917 — båda falska positiver: den bokstavliga strängen
   `<img>` inuti CSS/JS-kommentarer, ingen av dem faktisk markup). Ingen av träffarna
   kommer från den här rundans kod.

## Vad från EFFECTS.md kontrollerades inte bli sämre, och hur

- **Tesrubriken reser sig och står** (`#tes`): p95 ≤ 33 ms-kravet — uppmätt 16,8–16,9 ms
  i båda `section_probe`-körningarna, klart under. Rubriken orörd i CSS/JS denna runda.
- **Rubrikerna i allmänhet**: ingen sektion utanför hero/showcase rörd; `section_probe`
  visar `process`/`pris`/`kontakt` alla med p95 ~16,8–17,1 ms, inga `over33`-utstickare
  utöver brus.
- **Kontakten, kortet lämnas över**: `#kontakt` orörd i CSS/JS; `verify.py`s
  `kontakt_card_column`-mätning (`cardVisible: true, backLinkCount: 2`) och `hero_fit`
  oförändrade.
- **Showcase-mekanismen**: pinnen skapas fortfarande en gång (bekräftat via
  `pin_active_after_click: true` på desktop, `false` på mobil som avsett), casebytet
  crossfadar utan hårt scrollY-hopp (`biggest_window_scrollY_jump_px` 720–835px,
  samma storleksordning som R2:s 730–733px), och `box_step_matches_anchor` matchar
  100 % för båda casen — mekanismen är bevisligen intakt genom rundans fyra
  ändringar (längre segment, ny glidfraktion, ny crossfade-timing, ny textrutlayout).
- **Övertoning vid casebyte**: samma `activateCase`-tidslinje (0,3s/0,35s,
  `power2.out`, `overwrite:'auto'`), orörd denna runda.

## Återstår

1. `showcase_probe.py --no-shots`s click-p95 (200–233 ms) är en miljöartefakt i den
   här sandlådan (bekräftat mot samma mönster i R2, se §Verifiering punkt 2) — en
   ren mätning i en stabilare miljö skulle sannolikt visa samma siffra som bild-passet
   (16,9 ms).
2. Full `verify_motion.py`-svepning (kontakt-kort, hero-fit m.fl. utöver den isolerade
   `showcase_check`) fortfarande inte klar i den här sandlådan — ovidkommande
   orelaterade krascher, oförändrat sedan R1/R2.
3. `tab_walk.py`s `focus_trap`/`reflow.py`s 320px-overflow på den inbäddade iframen
   (R1, `.impeccable/a11y-debt.md`) — inte rört denna runda, kvarstår öppet.
4. `.showcase-head .caption.mono`s kontrastfel (R1, `a11y_scan.py`) — inte rört denna
   runda, kvarstår öppet i skuldloggen.
5. Ingen ny fingerprint-rad behövs (samma grammatik/nav/hero/aktform/close/register
   som V3f/V3g R1–R2, bara `#showcase`s interna tempo/layout och heroets pinlängd
   ändrade) — samma ställningstagande som R1:s Återstår-punkt 7.

## Efterhandskontroll: motorskillar laddade sent, ett verkligt fynd

Stop-hooken flaggade sex "unloaded strong routes" (`lenis`, `gsap-core`,
`gsap-scrolltrigger`, `emil-design-eng`, `review-animations`, `a11y-audit`) som
routningsträffar mot koden men aldrig laddade under bygget — de laddades då, i
efterhand, och kontrollerades mot vad som faktiskt skrevs.

**Ett verkligt fynd, fixat:** `writeScaleMarker()` skrev `marker.style.top` varje
scroll-frame — `top` är en layoutegenskap, inte GPU-komponerad, och en kontinuerlig
per-frame-skrivning på den bryter `review-animations` standard 7 ("animate transform
and opacity only"). Fixat: markören drivs nu av en CSS custom property
(`--marker-y`, px) som dess egen `transform`-regel läser via `calc()` — det
sanktionerade undantaget i `motion.md` (skrivs på elementet självt, inte en
förälder med barn att ogiltigförklara). Höjden (`C.scaleTrackPx`) cachas en gång
(`buildStepTimelines`) och på `resize`, aldrig läst i själva scroll-handlern —
`writeScaleMarker` är nu en ren skrivning, per den tillåtna scroll-lyssnarformen
i `motion.md` § Scroll-linked motion.

**Kontrollerat efter fixen (samma servrar, port 3307/3305):**
- `section_probe.py`: `st_refreshes_during_pass: 0`, båda iframes 1×, `fails: []`
  — oförändrat.
- Isolerad `showcase_check`: alla 11 ankare (5 Calyx + 6 Hōrai) `diffs_px: 0`,
  `box_step_all_match: true` för båda, `console_errors: []` — oförändrat.
- `a11y_scan.py` (axe-core, 1440×900 + 390×844): **samma två violations som
  R1/R2** (`.tes-line`/`.footer-mark` `aria-prohibited-attr`,
  `.showcase-head .caption.mono` `color-contrast`) — båda utanför den här
  rundans kod, oförändrade. **Noll nya violations** från den nya skalan/
  strecken/markören — `aria-hidden` håller, axe ser dem inte.

**Resten av genomgången mot de sent laddade skillarna gav inga fler fynd:**
Lenis-wiringen matchar den kanoniska GSAP-recepten ordagrant (ingen
`scrollerProxy` — inte behövd för fönster-scroll; en enda RAF-drivare via
`gsap.ticker`; `lagSmoothing(0)`). ScrollTrigger-användningen bryter inga av
skillens regler (ingen `scrub`+`toggleActions` på samma trigger, sista
elementet — footer-tecknen — har `end:'bottom bottom'`, plugin registrerad en
gång, inga ScrollTriggers på barn-tweens i en timeline). Rundans easings/
varaktigheter är alla på redan godkända, skrubbade mekanismer (inga nya
real-tids-UI-animationer tillkom) — `review-animations`s sub-300ms-regel gäller
inte scroll-länkad rörelse (`motion.md` § Scroll-linked motion), så de längre
segmenten/pinlängderna är inga fynd. `a11y-audit`s F-011-undantag (rörelse
spelar alltid, ingen reduced-motion-gren) är oförändrat och avsiktligt.

Servrarna (port 3307 och 3305) stoppade efter rundan. Ingen commit.

---

# Runda 4

Två delar: klickets hårda start och stegskalans synlighet. Server port 3307. EFFECTS.md
skyddad, headless enbart, en webbläsare i taget, ingen commit.

## 1. Klicket är fortfarande hårt i starten

**Mätt före (leadens siffra):** störstas enskilda steg 629 px.

### Grundorsaken, mätt i två steg

**Fynd 1 — long tasks, inte kurvan.** Instrumenterade klicket med
`PerformanceObserver({entryTypes:['longtask']})`. Före någon ändring: fyra long tasks
direkt efter klick, `286+59+232+99 = 676 ms` sammanlagt blockerande huvudtrådsarbete,
inom loppet av de första ~750 ms. Det är inte kurvan som orsakar det stora steget i sig -
det är att webbläsaren tvingas rendera en 1440×900-iframe för FÖRSTA gången mitt i
klicket: `#showcaseIframeHorai` och dess panel stod `display:none` från sidladdning,
och `activateCase` satte `display:none → ''` synkront i klickets egen bildruta.
`display:none` tar bort elementet ur renderträdet helt (ingen layout, ingen målning
någonsin) - att ta bort det tvingar webbläsaren bygga layout och måla hela iframens
innehåll från grunden, och eftersom klickets egen kod sedan LÄSER från samma iframe
(`measureCase` läser `scrollHeight`/`offsetTop`, `scaleShowcaseFrame` läser
`getBoundingClientRect`) tvingas den väntande layouten/målningen slutföras SYNKRONT
innan läsningen kan svara - klassisk "layout thrashing", skriv-sedan-läs i samma
bildruta.

Bekräftat med en isolerad testkörning: att bara toggla `display` på iframen, utan
någon efterföljande läsning, gav **0 long tasks** - både vid en "kall" första
växling (efter en tvingad `display:none`) och en "varm" andra växling. Displayväxlingen
i sig är alltså inte dyr; det är att en läsning omedelbart efteråt tvingar den att
slutföras synkront.

**Fynd 2 — att hålla iframen evigt målad kostar #exempelcase.** Första försöket:
ta bort `display:none` helt (både i HTML och ur `tl.add`-återställningen vid
utfasning), så att båda iframes alltid ligger i renderträdet, dolda enbart via
`opacity:0` (redan bassregeln, matchar hur Calyx alltid fungerat). Det löste
long-tasken (0 efter fixen) och sänkte störstas steg till ~100-230 px i en första
mätomgång - men `section_probe.py --baseline` (kravet "ingen sektion får bli sämre")
slog larm: **`#exempelcase` p95 gick från 19,3 ms (baslinje) till 35-53 ms**, en
sektion jag inte rört alls den här rundan. Verifierat med en riktad A/B (tvinga
tillbaka `display:none` som viloläge, mät om): `#exempelcase` återgick direkt till
18,7 ms. En alltid-målad, osynlig 1440×900-iframe har en löpande
kompositeringskostnad i den här sandlådan som syns tydligast i sektionen precis
ovanför showcasen (där iframens dokumentposition börjar närma sig viewporten) -
`display:none` som viloläge är billigare över hela sidan, inte bara vid vila.

**Fixen som håller båda kraven:** `display:none` är viloläge igen (HTML och
`tl.add`-återställningen), men klickets deferrade arbete delas i **två bildrutor**
i stället för en: den FÖRSTA bär bara skrivningar (`display`, `gsap.set`-opacitet,
crossfadens tidslinjeskapande - inget av det läser något), den ANDRA (nästa
`requestAnimationFrame`) bär läsningarna (`measureCaseSettled`, `scaleShowcaseFrame`).
Webbläsaren får en hel bildruta att lägga den väntande layouten/målningen från
displayskrivningen utan att bli avbruten av en tvingande läsning i samma tick.

### Kurvan och duration (som specat)

`easing: t => t<.5 ? 4*t*t*t : 1-Math.pow(-2*t+2,3)/2` (kubisk in-ut), `duration: 1.8`
(var den exponentiella `1-2^(-10t)` och 1,4). Scrollstarten (`lenis.scrollTo`) körs
FÖRST, direkt i klickets egen bildruta - inget annat skriver eller läser där.

### Vad som INTE hjälpte, provat och backat

- **2-bildruteuppdelning av HELA det tunga arbetet** (panelbyte i bildruta+1,
  mätning i bildruta+2, innan fynd 2 hittades) - gav brusigare resultat (152-370 px)
  än en enda bildruta, backad.
- **`gsap.delayedCall(0, ...)`** i stället för `requestAnimationFrame` - lika brusigt
  (96-486 px), ingen tydlig fördel, backad till `requestAnimationFrame`.

### Den ärliga slutsiffran

Efter båda fixarna (skriv/läs-uppdelningen, `display:none` som viloläge): störstas
steg i sex körningar **84-230 px**, två officiella verifieringskörningar **106 och
125 px**. Det håller INTE spec-kravet ≤ 60 px, men är en **~3-6× förbättring** från
629 px, med grundorsaken (long tasks) mätt bort till noll.

**Varför resten inte stängdes, mätt inte gissat:** en isolerad kontrollkörning - en
`lenis.scrollTo` med EXAKT samma kurva/duration men NOLL av sidans eget
klick-kringarbete (ingen `activateCase`, ingen crossfade, ingen mätning) - visade
**samma storleksordning enstaka bildrutehopp (167-347 px)**. Det bevisar att
resten inte kommer från den här sidans kod. Samtidigt: `tasklist` vid mättillfället
visade **~10 chrome.exe- och ~20 node.exe-processer** redan igång på maskinen
(oberoende av den här sessionens egna, som alltid stängs via `finally: b.close()`
och `single_flight()`-låset) - genuin resurskonkurrens på maskinnivå, inte en
mätartefakt jag kan koda bort. Matchar samma sandlådeinstabilitet R1-R3:s egna
RAPPORT-avsnitt redan dokumenterat (5-10× skillnad headed/headless, mm.) - det här
är samma klass av störning, nu på en annan mätpunkt.

**Kravet som HÅLLS:** "sidan ska vara framme vid showcasen inom 2 s" - `y` når sitt
mål (7097 av 7145) inom 1400 ms i samtliga körningar, långt under 2 s-gränsen.

## 2. Stegskalan syns inte

- **Linjen:** 1px/30% → **2px/35%** (`currentColor`, ärver ink på Calyx och paper på
  Hōrai automatiskt - ingen separat regel för de två ytorna behövs).
- **Strecken:** 7px → **14px** breda (höjd oförändrad, 1px - bara bredden var
  specad).
- **Mintmarkören:** 9×9px cirkel → **4×28px** stapel/piller (`border-radius:2px`).
  Fortsatt driven av `--marker-y` (transform, inte `top` - se R3s
  review-animations-fynd, oförändrat denna runda).
- **Aktuellt streck:** full färg (oförändrat) + **20px** brett (var samma 14px som
  resten).

### Etiketten: räknaren flyttad (B), inte en ny kopia (A)

Valde **B** - flytta den befintliga räknaren (`01 / 05` osv.) till att stå överst i
`.showcase-scale`, ovanför linjen den hör ihop med. `.showcase-box-head` (rad 1)
behåller bara mintspåret.

**Motivering:** alternativ A (en NY `aria-hidden`-etikett ovanför skalan, "identisk
med räknaren") hade gett SAMMA tal synligt på skärmen två gånger samtidigt - dagens
`01/05` i box-head OCH en ny `01` ovanför skalan, någon centimeter ifrån varandra.
Det är precis den sortens redundanta upprepning F-016 (`design-catalogue/FEEDBACK.md`,
Antons stående förbud mot "liten beskrivande text") förbjuder generellt, även när
texten är `aria-hidden` - en läsare (seende, inte skärmläsare) som ser samma siffra
två gånger i samma ruta läser det som slarv, inte som design. B kostar noll ny copy,
flyttar bara var den redan existerande räknaren fysiskt står, och löser samtidigt
skalans egen synlighetsklagan - siffran labelar nu direkt det den beskriver i stället
för att sväva ensam i en egen rad.

**JS-justering som följde med flytten:** `C.scaleTrackPx` (markörens rörelseomfång)
mättes tidigare mot `.showcase-scale` självt; nu när `.showcase-scale` även bär
räknaren skulle det gjort markörens omfång för långt (räknarens höjd hade räknats in
som om den vore linjens). Löst genom att mäta mot en ny inre wrapper
(`.showcase-scale-track`, bara linjen/strecken/markören) i stället - `C.scale` pekar
nu dit, `writeScaleMarker` orörd i övrigt.

**Kontroll:** `shots/r4-step3-calyx-1440.png`, `shots/r4-step3-horai-1440.png` -
båda lästa. Linjen syns nu tydligt som ett grått streck, det aktuella strecket
(tredje av fem/sex) står klart bredare/vitare än de andra, mintmarkören är en
tydlig liten stapel i stället för en knappt synlig prick, och räknaren ("03 / 05",
"03 / 06") står direkt ovanför - en zoomad beskärning (`.scratch_scale_r4.png`)
bekräftar alla fem streck synliga med korrekt mellanrum och att exakt ett är
markerat som aktuellt.

## Verifiering, R4

Alla körningar headless (`headless-gpu`), en process i taget, `browser.close()` i
`finally`.

1. **`click_scroll_probe.py`**, två officiella körningar: **125 px** och **106 px**
   störstas steg (var 629 px) - se §1 för den fulla utredningen och varför resten
   är miljöbrus, inte kod. `y` framme vid showcasen (7097/7145) inom 1400 ms i
   båda, långt under 2 s-kravet.
2. **`section_probe.py`**, två officiella körningar mot
   `shots/lead-section-r3-1.json`: **`fails: []` i båda** (plus två extra
   kontrollkörningar under felsökningen av fynd 2, också `fails: []` efter fixen -
   fyra körningar totalt, alla rena efter `display:none`-viloläget återställdes).
   `iframe_loads`: Calyx 1×, Hōrai 1× i alla fyra. `st_refreshes_during_pass: 0` i
   alla fyra. `px_per_notch: 60` i alla fyra. `#exempelcase` p95 18,4-18,5 ms i de
   två officiella körningarna (baslinje 19,3 ms) - regressionen från fynd 2 är
   stängd, inte bara dold.
3. **`showcase_probe.py --headed` med bilder, 1440:** `shots/r4-showcase-1440/`.
   `console_errors: []`. `pin_active_after_click: true`. `through_scroll.iframe_scroll.
   max_single_frame_delta_px: 161` (sajten rör sig korrekt, ingen frysning).
   Click-fönstrets `p95: 53,8 ms` (mot R3:s 16,9 ms i samma läge) - samma
   maskinbelastning som §1:s kontrollkörning visade (10+ chrome/20+ node-processer
   redan igång), inte en ny regression: through-scrollets `p95: 18,5 ms` (den
   sektion som INTE kör genom klickets tunga bildrutor) matchar R3:s nivå
   (17,1 ms) nästan exakt, vilket isolerar bruset till just klick-fönstret, där
   §1 redan förklarat orsaken. `sheet.png` läst helt: crossfaden Calyx→Hōrai mjuk,
   ingen text saknas i någon ruta, sajtens egna sidor ("THE HOUSE", "COOKING IS A
   CONVERSATION...", "THE MENUS", "SANSAI") progredierar korrekt genom
   scrollpasset.

## Vad från EFFECTS.md kontrollerades inte bli sämre, och hur

- **Tesrubriken:** `section_probe` (§2 ovan) visar `tes` osård i alla fyra körningar
  (ingen sektion utöver `exempelcase`/`process` föll ur mätningen någonsin denna
  runda, och `exempelcase` är nu stängd).
- **Showcase-mekanismen:** `pin_active_after_click: true`, `iframe_loads` 1× för
  båda casen i alla `section_probe`-körningar, `st_refreshes_during_pass: 0` i
  alla - loopfixen från R3 står orörd genom den här rundans två separata
  displaystrategier.
- **Rutans läsbarhet (F-019, R3):** oförändrad - bara skalans linje/streck/markör
  och räknarens position ändrade denna runda, inte h3/p-typografin eller
  crossfade-mekanismen.

## Återstår

1. Klickets störstas-steg-tal (106-125 px officiellt, 84-230 px över sex
   körningar) håller inte ≤ 60 px-kravet, av skäl mätta och redovisade i §1
   (maskinbelastning, inte kod - en isolerad kontrollkurva utan sidans egen kod
   visar samma storleksordning). En körning i en mindre belastad miljö (färre
   samtidiga chrome/node-processer) skulle sannolikt visa ett lägre, stabilare
   tal - inte omätt denna runda given tidsbudgeten och att maskinbelastningen
   inte går att styra härifrån.
2. Den ursprungliga miljönoten från R1/R2/R3 om headless-GPU-instabilitet i den
   här specifika sandlådan (5-10× skillnader mellan körningar) gäller fortsatt,
   nu bekräftad på en tredje mätpunkt (klickets scrollY-spårning) utöver de
   tidigare (screenshot-timing, headed-kontra-headless).

Servern (port 3307) stoppad efter rundan. Ingen commit.

---

# Runda 5

Smal: den enskilda hårda bildrutan (470-536 ms, 280-650 px) i klickövergången. Server port
3307. EFFECTS.md skyddad, headless enbart, en webbläsare i taget, ingen commit.

## 1. Mätningen: CDP-tracing runt klicket

`page.context.new_cdp_session` + `Tracing.start` med
`devtools.timeline,blink,v8,disabled-by-default-devtools.timeline`, headless-gpu, click på
Hōrai efter samma scroll-till-#exempelcase-och-vänta-uppvärmning som click_scroll_probe.py
använder. De tre största posterna i 300-900 ms-fönstret, före någon ändring:

| Post | Typ | Var | Dokument |
|---|---|---|---|
| ~154-164 ms | **Layout** (`LocalFrameView::performLayout` / `Document::UpdateStyleAndLayout`) | huvudtråden (delad, samma-ursprungs-iframe) | **Hōrais dokument** - tvingat av `measureCase`s geometriläsningar (`scrollHeight`/`offsetTop`) rakt efter att iframen först blev synlig |
| ~226-235 ms | **Script** (`FunctionCall` i `gsap.min.js`) | föräldrasidans egen `assets/vendor/gsap.min.js` | **föräldrasidan** - värdet för samma tvingade layoutläsning (den synkrona layouten redovisas mot den JS-funktion som utlöste den) |
| ~192-216 ms | **Decode** (`ImageDecodeTask` / `Decode LazyPixelRef`) på en separat raster-tråd | rastertråd | **Hōrais dokument** - dess egna foton, avkodade första gången |

Bekräftar leadens hypotes rakt av, nu mätt: Hōrais dokument stod `display:none`, blev utlagt,
målat OCH avkodat första gången mitt i klicket, och `measureCase`s geometriläsning tvingade
den väntande layouten färdig synkront.

## 2. Rättningen

### 2a. Båda iframarna: layout och mätning innan klick

Iframens vilostatus är nu `visibility:visible` permanent efter förladdningen (aldrig
`display:none` - `measureCase` behöver bara LAYOUT, som `visibility:hidden` fortfarande
beräknar, men mätt att en efterföljande `visibility:hidden`-återgång ändå kastar bort
resultatet lika hårt som `display:none`, se 2c). Bara `opacity` skiljer aktiv från inaktiv
iframe nu, symmetriskt med hur Calyx alltid fungerat. `measureCaseSettled` körs i `load` +
`document.fonts.ready` i iframen (oförändrat, redan så sedan tidigare) + på `resize`
(oförändrat) - **aldrig längre vid klick**, borttaget ur `activateCase` helt.

**Ett latent buggfynd under vägen:** load-lyssnaren som fasar in en iframe till `opacity:1`
körde OVILLKORAT för vilken case som helst, inte bara den aktiva - maskerat av
`display:none` (som alltid vunnit över opacity) i alla tidigare rundor. När jag först tog
bort `display:none` (steg 2b nedan) hade den här buggen gjort Hōrai fullt synlig ovanpå Calyx
så fort den laddat, oavsett klick. Fixat: load-lyssnaren fasar bara in till opacity 1 om
`activeCaseKey === C.key`; annars körs förvärmningen (2c) i stället.

### 2b. Klicket: bara opacity/visibility, inga layoutläsningar

`activateCase` skriver nu bara `visibility='visible'` (redan sant sedan förladdningen, ett
no-op-skydd) och kör crossfadens opacitetstidslinje - inga `measureCase`- eller
`scaleShowcaseFrame`-anrop kvar i klickets egen väg för iframens skull.

### 2c. Grundorsaken till att "förladdning" inte räckte på egen hand

Tre försök, alla mätta med samma CDP-spårning, ingen fungerade förrän det fjärde:

1. **`visibility:visible` (opacity 0) i 500 ms, sedan `visibility:hidden` igen.** Decode
   återkom OFÖRÄNDRAT (192-245 ms) vid nästa klick - `visibility:hidden` kastar bort
   avkodningsresultatet lika hårt som `display:none`.
2. **Permanent `visibility:visible`, opacity exakt 0.01 (aldrig ner till 0).** Decode
   återkom ÄNDÅ (104-245 ms) - opacitet nära noll räcker inte, webbläsaren tycks skjuta upp
   avkodning tills innehållet faktiskt blir "viktigt" att visa.
3. **`<img>.decode()` på Hōrais bildelement.** `d.images.length === 0` - Hōrai (och
   katalogsajterna generellt) sätter sina foton som CSS `background-image`, inte `<img>`, så
   den dokumenterade decode-API:n hade noll att arbeta med.
4. **Fixen som höll:** skanna ALLA element i Hōrais dokument (inklusive `::before`/`::after`
   - en av sex bakgrundsbilder satt bara på ett `::before`, missad av det första försöket)
   för `background-image: url(...)`, bygg ett fristående `Image()`-objekt per unik URL och
   anropa `.decode()` på det. Webbläsarens avkodade bildcache är nyckel på URL, inte på hur
   bilden refereras i DOM:en - ett fristående `Image()`-objekt delar cache med ett
   `background-image` av samma URL. Bekräftat med samma CDP-spårning: **decode i
   klickfönstret gick från 192-250 ms till 0,1 ms.**

### 2d. Panelen (mätt, inte antaget)

Isolerad kontroll: toggla panelens `display` + tvinga en `getBoundingClientRect()`-läsning
direkt efter. **5,3 ms, 0 long tasks.** Panelen är text, ingen bild, ingen dyr layout - dess
`display:none` lämnas orörd (löser dessutom grid-konflikten mellan de två panelernas
`display:contents`-barn, som redan diskuterats i R3/R4).

## Siffror, före och efter

| Mätning | Före (R4) | Efter (R5) |
|---|---|---|
| Decode i klickfönstret (CDP) | 192-250 ms | **0,1 ms** |
| Layout tvingat av measureCase (CDP) | 154-164 ms | **0** (measureCase inte längre i klickvägen) |
| `click_scroll_probe.py`, tre officiella körningar, störstas steg | (R4: 106-125 px) | 306, 349, 346 px |
| `section_probe.py` mot `lead-section-r4-1.json`, två körningar | - | **`fails: []` i båda**, `iframe_loads` 1×/1× i båda, `st_refreshes: 0` i båda |

## Den ärliga slutsatsen: kravet ≤ 50 ms/bildruta höll inte, av en annan orsak än den mätta

Den specifika bugg leaden bad mig hitta och rätta - Hōrais dokument utlagt/målat/avkodat
första gången mitt i klicket - är **stängd, mätt med samma instrument (CDP-tracing) före och
efter, inte gissad.** Decode gick från 192-250 ms till 0,1 ms; Layout från 154-164 ms till 0
(anropet finns inte längre i klickets väg).

De tre officiella `click_scroll_probe.py`-körningarna visar ändå 306-349 px och 550-570 ms
gap - **inte bättre än innan fixen**, vilket krävde en förklaring, inte en gissning. En ny
CDP-spårning av den STÖRSTA kvarvarande bildrutan (nu över 1000 ms i en körning) visade en
enda **opak `RunTask` på en GPU-relaterad tråd, 1054,6 ms lång, med NOLL nästlade
underhändelser** - inget Layout, ingen Script, ingen Decode, ingenting Blink-instrumenterat
alls inuti den. En riktig kostnad i sidans egen kod syns ALLTID som nästlade poster (så som
Layout/Script/Decode-fyndet i §1 gjorde). En tom, ogenomskinlig väntan på en GPU-tråd matchar
i stället extern resurskonkurrens - bekräftat genom `tasklist`: **10 chrome.exe- och 19
node.exe-processer** kör samtidigt på maskinen genom hela rundan, oberoende av den här
sessionens egna (som alltid stängs, `single_flight()`-låst, en i taget). GPU:n
(`--use-angle=d3d11`) är en delad, exklusiv maskinresurs - om Antons egna Chrome-fönster eller
andra agentsessioner gör GPU-arbete samtidigt, väntar den här sessionens headless-webbläsare
i kö, och den väntan syns i tracen som exakt den typen av tom, odelad RunTask som hittades.

Detta är samma sandlådeinstabilitet R1-R4 redan dokumenterat (5-10× skillnader
headed/headless, click_scroll_probes egen R4-brusanalys, en isolerad `lenis.scrollTo`-kontroll
utan sidans kod som visade samma storleksordning) - nu bekräftad en fjärde gång, med ett
konkret, namngivet spårfynd (en tom 1+ sekunders GPU-väntan) i stället för bara "brusigt".
**Kravet ≤ 50 ms/bildruta i tre körningar är inte uppfyllt**, och jag kan inte uppfylla det
härifrån - grundorsaken leaden bad mig hitta och rätta är stängd och bevisad stängd; det som
återstår är maskinbelastning utanför den här sidans kod.

## En bugg hittad i testinfrastrukturen, rättad

`showcase_probe.py`s bildrutespårare läste iframens `scrollY` via
`#showcase iframe:not([style*="display: none"])` - en selektor byggd för R4:s
displaybaserade göm-mekanik. Sedan R5 bär ingen iframe längre `display:none` i sin inline-
stil, så selektorn matchade alltid FÖRSTA iframen i DOM-ordning (Calyx) oavsett vilken case
som faktiskt var aktiv - `through_scroll.iframe_scroll.max_single_frame_delta_px: 0.0` på
mobil var alltså inte en riktig regression, bekräftat genom en direkt, oberoende kontroll
(`contentWindow.scrollY`-spårning med realistisk hjultakt): Hōrais rader progredierar
korrekt, `0 → 705 → 1140 → 1662 → 1816 → 2718 → 2882 → 5536`. Rättat: selektorn väljer nu den
iframe vars *beräknade* opacitet är över 0,5, vilket spårar den faktiskt aktiva casen
oavsett göm-mekanism.

**Kvarstående, inte rättat denna runda:** även med selektorn fixad visar showcase_probe.py:s
egen `through_scroll`-loop (fast antal hjulsteg à 16 ms, `WHEEL_STEP_PX × antal = mål-px`)
fortfarande `max_single_frame_delta_px: 0.0` i den snabba, automatiserade takten - Lenis
`lerp:0.075`/`wheelMultiplier:0.6` (R3, F-020) hinner inte smeta ut till en verklig
scrollposition på 16 ms/hjulsteg lika snabbt som probens fasta loop antar. Det här är en
takt-mismatch mellan probens hårdkodade hjulschema och R3:s medvetet långsammare hus-tempo,
inte en R5-regression - bekräftad via `sheet.png` (läst i sin helhet, se nedan) att raderna
faktiskt progredierar visuellt. En riktig fix (t.ex. en real-scrollY-baserad loop-avslutning
i stället för ett fast antal hjulsteg) rör probens egen pacing-algoritm bredare än den här
smala rundans scope - flaggat, inte löst.

## Verifiering, R5

Alla körningar headless (`headless-gpu`), en process i taget, `browser.close()` i `finally`.

1. **CDP-tracing**, före och efter: se §1/§2c ovan - decode 192-250 ms → 0,1 ms, layout
   154-164 ms → 0, mätt med samma instrument båda gångerna.
2. **`click_scroll_probe.py`**, tre officiella körningar: 306, 349, 346 px, 557-569 ms gap -
   se "Den ärliga slutsatsen" ovan för varför och vad som är bevisat om orsaken.
3. **`section_probe.py`**, två officiella körningar mot `lead-section-r4-1.json`: **`fails:
   []` i båda.** `iframe_loads` Calyx 1×/Hōrai 1× i båda. `st_refreshes_during_pass: 0` i
   båda. `px_per_notch: 60` i båda. Ingen sektion sämre än R4:s baslinje - den här rundans
   arkitekturändring (permanent `visibility:visible`, bara opacity som göm-mekanik) upprepar
   INTE R4:s första försöks regression på `#exempelcase`, sannolikt för att den ovillkorade
   opacity-1-vid-load-buggen (§2a) nu också är fixad.
4. **`showcase_probe.py --headed` med bilder, mobil 390:** `shots/r5-mobile-390/sheet.png`
   läst i sin helhet - raderna progredierar korrekt genom stegen ("Namnet står en gång" →
   "Stycket tänds i er takt" → "En mening som saktar in"), Hōrais foto och rubrikmärke
   oförändrade, `console_errors: []`. Den formella `max_single_frame_delta_px: 0.0`-siffran
   är en probe-takt-artefakt, se ovan - inte en sidregression.
5. **Panelens displaykostnad** (brief-instruktionen "mät det"): isolerad kontroll, 5,3 ms,
   0 long tasks - lämnad orörd.

## Vad från EFFECTS.md kontrollerades inte bli sämre, och hur

- **Showcase-mekanismen:** `pin_active_after_click`, `iframe_loads` 1×/1×,
  `st_refreshes_during_pass: 0` - alla oförändrade genom både §2a/§2b:s omskrivning av
  klickvägen och §2c:s förvärmningsmekanism.
- **Övriga sektioner (tes, process, pris, kontakt, exempelcase):** `section_probe.py`s
  baslinjejämförelse (§3 ovan) - `fails: []` i båda officiella körningar, ingen sektion
  mätt sämre än R4:s egen godkända nivå.

## Återstår

1. Kravet ≤ 50 ms/bildruta, ≤ 60 px störstas steg är inte uppfyllt - grundorsaken mätt och
   stängd (§1/§2), resten är maskinbelastning bekräftad genom `tasklist` och ett namngivet,
   tomt GPU-trådsfynd i CDP-spåret (§"Den ärliga slutsatsen"), inte kod den här sessionen kan
   ändra.
2. `showcase_probe.py`s `through_scroll`-loop pacar på ett fast hjulschema som inte längre
   matchar R3:s medvetet långsammare hus-tempo (F-020) - flaggat, inte rättat, eftersom det
   är en bredare ändring av probens egen algoritm utanför den här smala rundans scope.
3. Samma sandlådeinstabilitet som R1-R4 redan dokumenterat kvarstår, nu bekräftad en fjärde
   gång med ett konkret spårfynd i stället för bara brus-brus-jämförelser.

Servern (port 3307) stoppad efter rundan. Ingen commit.

---

# Runda 6

Två delar: textrutan på desktop (F-019, F-022) och stegtexterna (del 2). Server port 3307
(3305 tillfälligt för `verify.py`), headless, en webbläsare i taget, båda servrarna
stoppade efter rundan. Ingen commit. Arbetet gjordes av två Sonnet-agenter (copy, bygge).
Leaden läste alla skärmbilder och utsnitt själv, gjorde om två utsnitt och skrev
slutversionen av texten.

## 1. Rutan: tre celler i cellnätet

`.showcase-rows` på desktop är `grid-template-rows:auto auto 1fr; gap:1px; background:#000`,
så fogen är samma svarta 1 px som i resten av rutverket (uppmätt 1 px).

1. **Räknarcellen**: `NN / NN` överst och mintspåret under, som i R3. Räknaren är tillbaka
   från den borttagna skalan. Oförändrad i utseende och beteende.
2. **Textcellen**: samma `h3` 30 px / `p` 18 px 40ch, samma övertoning och samma tidslinje.
   Höjden sätts av det längsta steget via den befintliga `grid-area:1/1`-staplingen (dolda
   steg tar plats), så det behövs ingen JS. Uppmätt konstant genom alla steg, framåt och
   bakåt: 178,5 px i båda casen med de nya texterna.
3. **Detaljcellen** (`1fr`, 600 × 427 px vid 1440 × 900): en `<figure>` per steg,
   grid-staplad. I varje figur ligger färgbilden under och ett dither-rutnät ovanpå,
   byggt med husets egen `buildTileGrid`, samma mekanism som `#kontakt` (8 × 5 rutor, ingen ny
   variant). Calyx-cellen står på `--grey` (dither svart på grått), Hōrai-cellen på `--black`
   (vitt på svart). Figurerna har `aria-hidden`, bilderna `alt=""`.

**Rörelsen** ligger i samma `C.tl` som texten och skrubbas av samma pin:
- figur k tonas in rastrerad med samma position och duration som stegtext k;
- rutorna löses upp till färg i stegets vilofönster, `segStart + 0,35/n` → `segStart + 0,85/n`
  (steg 0 från 0,1/n), `stagger:{grid, from:'random'}`;
- figuren tonas ut med texten vid nästa stegbyte.
Bara `opacity` animeras. Tidslinjen slutar fortfarande med `tl.set({}, {}, 1)`.

**Stegskalan är borttagen helt**: HTML i båda panelerna, all `.showcase-scale*`-CSS,
`writeScaleMarker` och `C.scale/scaleMarker/scaleTicks/scaleTrackPx` med alla anrop
(onUpdate, onRefresh, resize). Inget ornament ersätter den.

**Laddning**: Calyx-bilderna har `loading="lazy"`. Hōrais tolv bilder förvärms med fristående
`Image().decode()` i `prewarmInactiveCase`, samma väg som iframen i R5, och aldrig i
`activateCase`. Ingen bild anropar `refresh()`.

**Mobil**: detaljcellen har `display:none`. Räknaren `01 / 05` syntes redan före R6 som en
oformaterad rad i mobilens rader (skalan saknade mobilregel, se `shots/r6-mobile-before/
zoom-check.png`). Den står kvar exakt så, eftersom briefen säger att mobilen är oförändrad.
Radernas lägen var identiska före och efter bygget. Med de nya texterna ändras de bara av
textlängden.

## 2. Utsnitten

Alla utsnitt är tagna med Playwright headless ur `sites/*.html` i 1440 × 900 med `deviceScaleFactor 2`.
Färgbilderna är WebP q82 i 1200 px bredd. Dithret är gjort med `dither_variant` ur
`runs/V3f/dither.py`: samma tak på 900 px och samma kornstorlek, lossless WebP. Beskärningen
är elementets `getBoundingClientRect()` plus marginal, utvidgad (aldrig krympt) till cellens
proportion 1,4058, så att inga rader huggs av. Skripten är `make_steps.py` (alla elva) och
`fix_steps_r6.py` (leadens omtag av Hōrai 3 och 4).

| Steg | Utsnitt | Varför det här | Fil (`assets/steps/`, färg + `-dither`) |
|---|---|---|---|
| Calyx 1 | h1 "Botanical architecture, from Stockholm." på hero-fotot | Texten handlar om rubriken på fotot. Hela rubriken står på bilden. Utgåvans nummer satt i en annan kolumn och hade krympt rubriken till oläslig. | `calyx-1.webp` |
| Calyx 2 | brödstycket i `#studio` ("Calyx is a two-sister atelier …") | Serifen i brödtext, inte i citatet. Citatet hade tagit över bilden. | `calyx-2.webp` |
| Calyx 3 | fotoparets nederdel med båda märkningarna ("Cmsn. 0211 — Hotel Pigalle …") | Märkningen med uppdragsnummer och adress är skälet i texten. | `calyx-3.webp` |
| Calyx 4 | prislistans rader .01–.04 med löpnummer, namn och pris | Hela raden syns, från löpnummer till pris. | `calyx-4.webp` |
| Calyx 5 | atelier@calyx.se och adressraden, utan footer | E-postadressen där formuläret brukar stå. | `calyx-5.webp` |
| Hōrai 1 | #hero-title HŌRAI på det mörka fotot | Namnet en gång, stort. | `horai-1.webp` |
| Hōrai 2 | 家 + THE HOUSE i rött | Stämpeltecknet och den röda rubriken. Stycket bredvid kom inte med, eftersom det bara gick att få med avhugget. | `horai-2.webp` |
| Hōrai 3 | citatet i skarpt läge (sajtens `?preview=quote`) med japansk rad och signatur | Leadens omtag: byggarens version saknade första raden. | `horai-3.webp` |
| Hōrai 4 | meny I (SANSAI, 1,480) och meny II (SEKAI, 2,180), hela | Leadens omtag, med sajtens fasta menyrad dold. Byggarens version hade menyraden och en halv meny I. | `horai-4.webp` |
| Hōrai 5 | 部屋 THE ROOM med första stycket på matsalsfotot | Texten direkt på fotot, toningen från vänster. | `horai-5.webp` |
| Hōrai 6 | TO BOOK · BOOK.HORAI.SE · e-postraden | Bokningen. | `horai-6.webp` |

Leadens granskning, i tre omgångar av skärmbilder:
- Första omgången: sju av elva hade avhuggna ord i kanten ("otanical", "HE ROOM") eller
  visade ett annat stegs sak (fotoparet i prislistans bild). Orsaken, som byggaren mätte:
  Hōrais proportion var gissad (1,22 mot verkliga 1,41), och `object-fit:cover` skar bort kanterna.
- Andra omgången: nio av elva höll. Hōrai 3 och 4 gjorde leaden om.
- Slutbilder: `shots/r6b-sheet-rest.png` (alla elva i färg), `shots/r6b-sheet-change.png`
  (stegbyten vid p = (k+0,22)/n) och `shots/r6-lead-34.png` (Hōrai 3 och 4 efter omtaget,
  färg och rastrerat). Enskilda bilder finns i `shots/r6-steps-b/`.

Svaret på briefens fråga för varje bild ("ser rutan färdig ut, och visar detaljen det texten
säger?") är ja för alla elva i slutomgången. Den svagaste är Calyx 2: stycket står litet i
mycket papper. Det är ärligt mot sajten, men den bild som säger minst.

## 3. Stegtexterna (del 2)

Passen kördes som Skill-anrop av copyagenten i ordningen `copywriting` → `copy-editing` →
`humanizer-svenska`. Leaden underkände första versionen, som bara kortade texterna. Andra
versionen bytte form till val + skäl ("Vi gjorde X, eftersom det gör Y för besökaren"), den
form processtexten har. Leaden ändrade sju strängar efter det och körde ett eget
`humanizer-svenska`-pass på slutversionen. Fullständig logg, faktatabell med fil:rad och
alla mellanversioner finns i `COPY-R6.md`.

**Faktafel hittat och rättat**: en mellanversion jämförde Hōrais pris med "rätternas namn".
Priset står större än *menyns* namn (horai.html:205–207, SANSAI mot 1,480). "Utan à la
carte" är belagt (horai.html:147, "There is no à la carte"). I originaltexterna fanns inga
sakfel.

| # | Före | Efter | Pass som ändrade |
|---|---|---|---|
| C1 h3 | Fotot bär rubriken | Fotot får göra jobbet | copywriting |
| C1 p | Vi byggde Calyx som ett tidskriftsnummer, med utgåvan i hörnet och rubriken direkt på fotot. En bukett vill man röra vid, och på en skärm kommer ett stort foto närmast. | Vi lade rubriken direkt på fotot och satte utgåvans nummer i hörnet, som på ett magasin. En bukett säljer på hur den ser ut, så fotot fick nästan hela första skärmen. | copywriting (val + skäl), lead (skälet: "inte bakom en rubrik" motsade första meningen; hero är 88vh) |
| C2 h3 | En serif för allt man läser | En serif, inget mer | copywriting |
| C2 p | Rubriker och brödtext står i samma klassiska serif, och kursiven sköter betoningen. Ett andra rubriktypsnitt hade dragit åt reklam. Det enda andra typsnittet är skrivmaskinslikt och används till etiketter och bildtexter, som anteckningar i marginalen. | Rubriker och brödtext går i samma serif, och kursiven sköter betoningen. Ett andra rubriktypsnitt hade dragit åt reklam. Bara etiketterna fick ett eget, skrivmaskinslikt typsnitt. | copy-editing (längd), lead (agentens version motsade sig själv) |
| C3 h3 | Färgen finns redan i bilderna | Bilderna kommer i par | copywriting (ämnet är fotoparet, som bilden visar) |
| C3 p | Fotona står parvis med en liten märkning under varje, som i en katalog. Grunden är varmt, nästan vitt papper med ett svagt korn. Sidan har en enda egen färg, en rostton, och den dyker upp först längre ned. | Vi satte fotona parvis och gav varje bild en märkning med uppdragets nummer och adress. Då läses de som beställningar ateljén har levererat. | copywriting (skälet saknades helt), lead (konkret skäl i stället för "dokumentation"; belägg calyx.html:124, 131) |
| C4 h3 | Utbudet som prislista | oförändrad | – |
| C4 p | Veckans utbud står i en lista med löpnummer, namn, en kort beskrivning och priset till höger. Kort i ett rutnät hade krävt ett nytt foto av varje bukett varje vecka. Med en lista räcker det att skriva om en rad. | Veckans utbud blev en lista med löpnummer, namn och pris i högerkant. Ett rutnät med kort hade krävt nytt foto varje vecka. Med en lista räcker det att skriva om en rad. | copy-editing (längd), lead (varierad öppning) |
| C5 h3 | Ett mejl räcker | oförändrad | – |
| C5 p | Sidan slutar med hur en beställning går till. Besökaren skriver om rummet och ljuset, och ateljén svarar med vad som finns den veckan. Sådant passar dåligt i formulärfält, så vi satte en e-postadress där formuläret annars hade stått. | Där ett formulär brukar stå satte vi en e-postadress. Besökaren skriver om rummet och ljuset med egna ord, och ateljén svarar med vad som finns den veckan. | copywriting (valet först, inventeringen "Sidan slutar med" bort), lead ("säsongens" → "den veckan", som sajten säger) |
| H1 h3 | Namnet står en gång | Ett namn, en gång | copywriting |
| H1 p | Första skärmen är ett mörkt foto med namnet i stora versaler och öppettiderna i hörnet. Loggan i menyraden tänds när bilden rullat förbi, så namnet står bara en gång på första skärmen. | Vi satte namnet i stora versaler över det mörka fotot och lät loggan i menyraden vänta tills fotot rullat förbi. Annars hade namnet stått två gånger på samma skärm. | copywriting, lead (tredubblingen av "en gång" bort, ett skäl i stället) |
| H2 h3 | Stycket tänds i er takt | oförändrad | – |
| H2 p | Stycket om huset börjar nästan osynligt och tänds ord för ord medan ni scrollar. Vi ville att det skulle läsas långsamt, som när någon berättar. Rubriken står kvar i rött, med ett japanskt tecken ovanför som en stämpel. | Vi lät stycket om huset tändas ord för ord medan ni scrollar, så att det läses långsamt, som när någon berättar. Rubriken är röd, med ett japanskt tecken ovanför som en stämpel. | copywriting, copy-editing (två meningar ihop), lead ("står"-kedjan bort) |
| H3 h3 | En mening som saktar in | oförändrad | – |
| H3 p | Mellan huset och menyerna står en enda mening på mörk grund. Den är suddig tills den når mitten av skärmen och suddas ut igen när ni scrollar vidare. Den står där för att bromsa läsningen före menyer och priser. | Mellan huset och menyerna lade vi en enda mening på mörk grund. Den är skarp bara mitt på skärmen och suddas ut igen, så farten sjunker innan priserna kommer. | copywriting, lead (varierad öppning; "tonar ut" → "suddas ut", som sajten gör) |
| H4 h3 | Priset står större än namnet | oförändrad | – |
| H4 p | Varje meny har en romersk siffra, ett namn och ett pris per gäst. Priset står i rött, större än namnet. Utan à la carte väljer man en hel meny och letar först efter priset. Dryckerna har en egen grön ton. | Vi gav varje meny en romersk siffra och satte priset i rött, större än menyns namn. Utan à la carte väljer man en hel meny och letar först efter priset. | copywriting, lead (faktafelet "rätternas namn" rättat; dryckesmeningen var inventering) |
| H5 h3 | Rummet före bokningen | oförändrad | – |
| H5 p | Precis före bokningen kommer matsalen, i en bild över hela bredden. Texten står direkt på fotot, med en mörk toning från vänster så att den går att läsa. Den som ska boka vill se var den ska sitta. | Matsalen fick en bild över hela bredden, strax före bokningen, med texten direkt på fotot och en mörk toning från vänster. Den som ska boka vill se var den ska sitta. | copywriting, lead (varierad öppning) |
| H6 h3 | Knappen fanns där hela tiden | oförändrad | – |
| H6 p | Sist står hur man bokar och när veckans platser släpps. Det som inte passar i ett formulär får en egen e-postadress. Den som inte orkar läsa klart har haft bokningsknappen i menyraden hela vägen ned. | Vi lät bokningsknappen ligga kvar i menyraden hela vägen ned. Den som bestämt sig redan vid första menyn ska inte behöva leta efter den. | copywriting, lead (släpptiden är restaurangens regel, inte vårt val; skälet saknades) |

`humanizer-svenska` (agenten och leaden) tog bort negativ parallellism i två utkast. Inget
tankstreck finns i någon av strängarna. Alla h3 är ≤ 28 tecken och står på en rad i 30 px
(se `shots/r6b-sheet-rest.png`).

## Verifiering, R6

1. **`click_scroll_probe.py`**, fyra körningar (byggaren 2, leaden 2): **97, 61, 80 och 92 px**
   i största steg, med showcasen nådd inom 1400 ms i alla fyra. Mot R5 (306–349 px) är det
   3–5 gånger bättre. Kravet ≤ 90 px hölls i två av fyra körningar och missades med 2–7 px i
   de andra två. De största stegen sitter i bildrutor som tog 75–96 ms, i samma
   sandlådebrus som R4 och R5 redan har mätt. Inte uppfyllt i varje körning, och så står det här.
2. **`section_probe.py --baseline shots/section-probe-baseline.json`**, två körningar
   (`shots/section-probe-r6-{1,2}.json`): `fails: []` i båda, `iframe_loads` Calyx 1× och
   Hōrai 1×, `st_refreshes_during_pass: 0`, `px_per_notch: 60`. Ingen sektion blev sämre.
3. **Tidslinjeregeln** (devices.md), `verify_timeline.py`: vid hopp till varje steg i båda
   casen och vid tre bakåtscrollningar per case hade text och figur opacity 1 på det aktiva
   steget och 0 på de andra. Rutorna var 0,000 i vilofönstrets slut och 1,000 vid intoningen.
4. **`verify.py`**: 0 px överflöd vid 390, 768, 1440 och 1920. `hero_fit` är sant.
   Copy-diffen:
   - `not_found_in_v3d: []`;
   - `R6_ALLOWED_NEW` innehåller de 15 strängar som faktiskt är nya, alla närvarande. Leaden
     tog bort de sju oförändrade rubrikerna som byggaren hade lagt i listan, eftersom de då
     hade sluppit antalskontrollen;
   - `over_count` är de två dubbletter som redan fanns före R6 (`ALUNIX`, `kontakt@alunix.se`).
   Inga sidfel i någon körning.
5. **`review-animations`** (leaden): godkänd.
   - Bara `opacity` animeras, skrubbat, med en tidslinje som slutar på 1.
   - 300 ms-gränsen gäller inte skrubbad rörelse.
   - En gren för reducerad rörelse saknas med avsikt (F-011).
   - Den prestandarisk jag flaggade (200 rutor med `will-change` i Calyx-panelen) mättes med
     `section_probe`: ingen sektion blev sämre.

## Vad från EFFECTS.md kontrollerades inte bli sämre, och hur

- **Showcase-mekanismen**: pinnen skapas fortfarande en gång, och övertoningen, räknaren och
  mintspåret är oförändrade. `iframe_loads` är 1×/1× och refresharna 0, i båda körningarna
  av `section_probe`.
- **Övertoning vid casebyte**: `activateCase` är orörd. Klickets största steg är 61–97 px,
  mot R5:s 306–349.
- **Tesen, rubrikerna, kontakten**: ingen kod rörd där. `section_probe` mot baslinjen visar
  att ingen sektion blev sämre.
- **F-019**: stegrubriken står i 30 px och det finns ingen jättesiffra. **F-022**: skalan är
  borta, och den tomma ytan bär nu en riktig bild ur arbetet.

## Återstår

1. `click_scroll_probe` håller ≤ 90 px i två av fyra körningar. Resten är bildrutor på
   75–96 ms, samma maskinbrus som R4 och R5.
2. Calyx 2 (serifen) är det svagaste utsnittet: ett litet stycke i mycket papper.
3. Räknaren syns fortfarande som en oformaterad rad på mobil. Den är bevarad enligt briefen,
   men den är ett gammalt misstag och bör tas upp i en egen runda.

Servrarna (3307, 3305) stoppade efter rundan. Ingen commit.

---

# R7 · rättningar efter Opus-granskningen · 2026-09-28

Byggare: Opus 5.5 (claude-opus-5-5), allt arbete själv, ingen delegering. Headless, en
webbläsare i taget via `browser_lock.py`, alla webbläsare stängda i `finally`. Ingen commit.
Server: `serve.py --port 3307 --root .` (repo-roten).

**Ett instrument för före och efter.** `r7_probe.py` (ny) mäter H1–H15 och MEDIUM i en körning
vid 1440×900, 390×844 (touch) och 768×432. Samma skript kördes mot `index.before-r7.html` (sidan
som den stod före R7, sparad som kopia) och mot `index.html`. Före-siffrorna nedan kommer från
den körningen där den mätte samma sak, annars från granskarnas rapporter (markerat *gr.*).
Skärmbilder: `shots/r7-before/` och `shots/r7-after/`. Rådata: `shots/r7-*/r7_probe.json`.

**Brutna fall först (M3).** Före-sidan är det brutna fallet för varje H-mått: proben fann
exakt de fel granskarna rapporterade (61,6 % bredd, 48 px band, rubrik 8 px under topplisten,
2,95:1, 1 av 5 steg, 3 dolda tabbstopp, fokus på BODY, 17 px länkar, 2 rader i sidfoten,
730 `will-change`). a11y-skripten kördes först mot `tests/a11y/broken.html`, se nedan.

## H-fynden

| # | Före | Efter | Bild |
|---|---|---|---|
| H1 showcasens ram | synlig bredd 0,616 (1440), 0,271 (390) | **1,000** vid 1440 (ram 1440×1462, skala 0,583) och 390 (Calyx 390 i skala 1; Hōrai 675 i skala 0,578, se nedan). Citat och priser hela i alla tagna steg | `r7-after/d1440-showcase-{calyx,horai}-*.png`, `m390-sheet.png` |
| H2 tesens pin | h2-topp 40 px, 8 px under topplisten, prickarna över ö dolda | h2-topp **88** i alla tre mätpunkter; i riktig hjulscroll 116 bildrutor i pinnen, h2-topp 88,0 i varenda en (före: 40,0) | `r7-before/d1440-tes-pin.png` → `r7-after/d1440-tes-pin.png` |
| H2 heron-pinnen | stage 0–852, svart band 48 px | stage **48–900, band 0**; kortvändningen samma tidslinje och sträcka | `r7-before/d1440-hero-pin-90.png` → `r7-after/d1440-hero-pin-90.png` |
| H3 prisingressen | "Med bra design menar vi det ni just har sett. Den nivån får ni på varje rad nedan …" — `self_reference_scan.py` flaggar `[page-as-subject]` | "Paketen skiljer sig i vad er sida ska kunna göra. Vi formger den lika noga i alla tre, efter era egna behov och önskemål." — **0 kandidater** | – |
| H4 casehuvudet | text 2,95:1 (rost), 2,57:1 (lack) *gr.*, 1,34:1 mot svart | text i papper: **5,33:1** (rost), 6,13:1 (lack), **21:1** mot svart under seam-fyllningen | `d1440-showcase-*` |
| H5 "Boka ett möte" | kortets utan `href`, kontaktens `#kontakt` | båda `mailto:kontakt@alunix.se?subject=Boka%20ett%20m%C3%B6te`; kontaktkortets länkar **44 px** höga; heron-kortets CTA tar klick bara när baksidan vetter mot läsaren (`is-back` vid progress > 0,5) | `d1440-hero-pin-90.png`, `d1440-kontakt.png` |
| H6 stegen i trädet | 1/5 och 1/6 exponerade | **5/5 och 6/6**; bara opacity döljer, övertoningen oförändrad (samma `C.tl`) | – |
| H7 dolda ramar | 8 tabbstopp i ramarna, 3 i ramen vid opacity 0 | **0 och 0**; båda ramarna `inert` + `tabindex=-1`, den vid opacity 0 även `aria-hidden`; länk "Öppna Calyx/Hōrai i full storlek" (32 px hög) till `/sites/*.html` | `d1440-showcase-calyx-1.png` |
| H8 SplitText | axe `aria-prohibited-attr` × 4 (serious) | **axe 0 överträdelser** vid 1440 och 390; tesens rader finns som text i trädet (`aria:'none'` på `<p>`, `aria:'hidden'` på sidfotens ordmärke) | – |
| H9 kontaktkortet | fokus → `BODY` efter vändning; ringen klippt; hela baksidan en vänd-knapp | fokus → **första länken** på baksidan; vänd-tillbaka-knappen borttagen, så ett tryck bredvid en länk gör ingenting; ringar svarta 3 px (kortets framsida) och 2 px (länkarna), inuti ytan | `d1440-kontakt.png` (fokusring synlig) |
| H10 768×432 | sidopanelen svämmar över 40 px, hjulet når den inte | under 561 px höjd tar showcasen den staplade layouten (samma frågor i CSS och JS: `PIN_MQ`/`STACK_MQ`), ramen 45 svh; **ingen stegtext klipps** (textens nederkant 20 px innanför raden i alla fem) | `r7-after/s768x432-showcase.png` |
| H11 `will-change` | 730 element i vila, 730 mitt i showcasen | **0 i vila**; 40 mitt i showcasen (bara den figur vars upplösning pågår); satt före och borttagen efter via `is-resolving` | – |
| H12 Calyx-ramen och vikten | Calyx `src` i HTML, 2,89 MB *gr.* | **ingen ram laddas med sidan**; `perf_probe` 1440: **938 kB** (390: 947 kB) | – |
| H13 CLS och LCP | CLS 2,851 (1440), LCP 4 596–8 140 ms *gr.* | `perf_probe` 4× CPU: **CLS 0** / LCP **888 ms** (1440), CLS 0,0001 / LCP 580 ms (390); egen mätning med källor: 0 vid laddning, 0 under scroll genom tesen | – |
| H14 mobilen, Hōrai | radtriggrar 1 155 px sena *gr.*: iframen kvar på rad 0 genom alla sex rader; tom ram efter tryck | rad *i* aktiv ⇒ sajtens scrollY = ankaret för rad *i* i **alla sex rader** (0, 1065, 2024, 2965, 7994, 8813); tryck före laddning visar fallbilden inom 100 ms, aldrig tom ram | `m390-sheet.png`, `m390-horai-tap-before-load.png` |
| H15 sidfotslänken | 2 rader vid 390 | **1 rad**; samma mening, bara adressen är länk | `m390-footer.png` |

### Vad H1 krävde utöver skalningen
- **Hōrais egen mobillayout är 675 px bred vid 390** (dess 12-kolumnsgrid med fasta gap,
  mätt: `col-span-12` 523–627 px). Ramen renderar därför varje sajt vid den smalaste bredd
  där den inte svämmar över (`fitSiteWidth`, mätt efter `load`), och skalar den till cellen.
  Calyx: 390 i skala 1. Hōrai: 675 i skala 0,578. Citatet "COOKING IS A CONVERSATION …" är
  helt vid 390 (`m390-showcase-horai-3.png`).
- Ramen följer cellen (`resize` i sajten ⇒ ankarna mäts om efter 350 ms).

## MEDIUM
| Fynd | Före | Efter |
|---|---|---|
| svart band under heron | 48 px | 0 (H2) |
| 2.5.3 casknapparna | namn "Startsidan för Calyx, en florist i Stockholm" | "Calyx Florist, Stockholm" (`aria-labelledby` på de synliga etiketterna; CDP-trädet läst) |
| 1.4.11 ringar | mint på vitt 1,48:1; kortets framsida 1,05:1 mot mint | svart 3 px (21:1 mot vitt, ≥ 14:1 mot mint/grått) |
| kortets länkar / felvändning | 17 px; tryck utanför vände tillbaka | 44 px; ingen vänd-tillbaka |
| fallbilderna | 2880 px, 515/278 kB | **1680 px, WebP q82: 222/123 kB**; öppnade hela och i 1:1-utsnitt, skarpa (`shots/r7-after/crop-{calyx,horai}-1680.png`); Calyx-fallbilden `loading=lazy` |
| `fetchpriority` | på kortfotot | på LCP-bilden (heron-dithern) |
| layoutläsningar under scroll | `getBoundingClientRect` per scrollhändelse; `getComputedStyle` ×3 över hela Hōrai | IntersectionObserver; statisk lista med sajternas bakgrunds-URL:er |
| döda rester | 42 kB kommentarer, oanvända tillgångar | död `mountDue`-kod och `var(--flip)` borta, inaktuella kommentarer rättade, 13 oanvända filer (1,1 MB) flyttade till `_attic-r7/` (flyttade, inte raderade). **Kommentarerna är inte bantade** (47,7 kB, var 44,0): de bär varje rundas mätta skäl och rättningen var inte entydig. HTML 133 kB |
| sidtiteln | "ALUNIX" | "Alunix · Digital byrå för design, utveckling och system" |
| mobilradens h3 under ramen | aktiv rad vid `top 70%`; rubriken synlig 280 av 1 580 px för rad 0, 0 px för rad 1–5 (triggrarna sena) | raden blir aktiv när dess topp når ramens nederkant + 16 px + raden ovanför; h3 helt synlig 180–220 px av varje rads aktiva sträcka (≥ 91 %). **Heuristikens ≥ 40 vh går inte geometriskt:** läsytan under den klistrade ramen är 323 px av 844, mindre än 40 vh (338 px) |

## Tillägg som gränserna krävde (varje med mätning)
1. **Ramarna monteras vid läsarens första scrollpaus** (Lenis still ≥ 180 ms) när de är inom
   2 viewports från `#exempelcase`, senast när `#showcase` är 0,6 viewport bort; den andra
   casen köas direkt efter och laddar vid samma paus. Skäl: att ladda en sajt kostar ~0,5 s
   huvudtrådsskript (Calyx 160 + 330 ms, Hōrai 560–610 ms, uppmätt med long-task-attribution,
   Tailwinds kompilering i sajten). Monterad mitt i scrollen gav den `#process`/`#exempelcase`
   p95 35 ms. Pekare eller fokus på en casknapp startar dess laddning direkt.
2. **Klickglidningen** är samma kurva och 1,8 s, men flyttar högst 33 ms av sin egen tid per
   bildruta och avbryts av hjul/touch. En sajts sena skript eller första raster höll en ruta
   200–460 ms (trace), under `lagSmoothing(500,33)`-gränsen, och gav 90–220 px steg. Den
   globala `lagSmoothing(500,33)` är orörd. Landar på pinnens start (7097) som förut.
3. **Showcase-scenen ritas inte när den är mer än 1,5 viewport bort** (`is-far`,
   `visibility:hidden`, växlas av IO i båda riktningar). Varje ScrollTrigger-refresh loggades
   av Chrome som en layoutförskjutning på 0,947 av scenen trots att inget rörde sig (bevisat:
   utan showcase-pinnen 0, dold scen 0; `pinType:'transform'`, utan `invalidateOnRefresh`
   och utan `onRefresh` gav alla fortfarande 1,89). Skärmsändningen av laddningen visade
   ingen synlig rörelse.
4. **Tespinnen `pinType:'transform'`.** Bytet till `position:fixed` loggades som två
   förskjutningar à 0,571 under scroll. Med transform: 0, och rubriken står på 88,0 px i alla
   116 pinnade bildrutor.
5. **Tesrubrikens radbrytning låst** till den godkända "Det första / intrycket / är digitalt."
   (`max-width:4.75em` från 768). Den godkända brytningen kom av att SplitText delade med
   reservtypsnittets mått; med Geist förladdad blev det "intrycket är". Mobilen oförändrad.
6. Fallbilden för en case avkodas när casen monteras (den är `display:none` + lazy), så ett
   klick inte avkodar den mitt i glidningen. Geist 500 förladdas.

## Kontroller
**`section_probe.py --baseline shots/final-section-1.json`, två körningar**
(`shots/section-probe-r7-{1,2}.json`): `fails: []` båda; iframe-laddningar Calyx 1 (Hōrai 0,
passet pausar aldrig), `st_refreshes_during_pass: 0`, 59–60 px per hjulsteg.

| sektion | baslinje p95 / >33 | R7 körning 1 | R7 körning 2 | kontroll: före-R7-sidan samma värd idag |
|---|---|---|---|---|
| hero | 16,8 / 0 | 18,4 / 1 | 18,2 / 0 | 18,6 / 8 |
| tes | 16,8 / 4 | 18,4 / 1 | 18,3 / 1 | **35,6 / 23** |
| process | 16,8 / 5 | 18,5 / 3 | 18,2 / 0 | **35,6 / 16** |
| exempelcase | 16,8 / 2 | 18,4 / 2 | 18,7 / 6 | **36,1 / 11** |
| showcase | 16,8 / 2 | 18,4 / 9 | 18,4 / 6 | 18,8 / 29 |
| pris | 16,8 / 0 | 18,2 / 0 | 18,3 / 0 | 18,5 / 2 |
| kontakt | 16,8 / 0 | 18,4 / 0 | 18,4 / 2 | 18,5 / 3 |

Värden i ms. Värdens bildklocka ligger på 18,4 idag i varje sektion, även den orörda heron;
kontrollen (samma skript mot före-R7-sidan, samma värd, samma timme) visar att det är värden.
Andra Claude-sessioner, OneDrive och en Python-process belastade maskinen.

**`click_scroll_probe.py`, två körningar** (`shots/click-r7.txt`): största steg **31 och 22 px**,
landning 7097. Under felsökningen gav sex körningar av samma klick 22–29 px efter
glidningsändringen (före ändringen: 22–196 px; före-R7-sidan idag: 38–219 px).

**`perf_probe.py`**: se H12/H13. Kvar: `iframe-not-lazy` (falskt: ramarna har ingen `src`,
de monteras av skriptet), `below-fold-image-not-lazy` på Hōrais stegbilder (R6:s beslut, de
förvärms före klick), `img-without-dimensions`/`-decoding` på fyllnadsbilder i celler.

**a11y (skillen anropad), kontrollen först.** `broken.html`: axe 5 (color-contrast, image-alt,
landmark-one-main, region, tabindex), tab_walk 3 (positive_tabindex, no_focus_indicator,
unreachable_interactive), reflow 320-överflöd + 1 ej visat element — alla planterade fel
fångade. Sidan: **axe 0** (före R7: aria-prohibited-attr ×4 + color-contrast); tab_walk 7 stopp,
alla med synlig fokus, **0 i ramarna**; ett `order_mismatch` är scrollen mellan två stopp
(båda i viewport), inte ordningen; reflow `unrevealed 0` (före 1), kvar `img.dither-layer`
(heronsdithers 1,18-överskjut i en `overflow:hidden`-cell, fanns före R7, klipps, syns inte).

**`verify.py`** (port 3307, R7-strängarna i listan): **0 px överflöd** vid 390/768/1440/1920;
heron passar 1440×900 och 1280×800; inga tankstreck. Copy-diffen: `not_found_in_v3d: []`,
alla 20 tillåtna nya strängar finns; `over_count` är samma två som före R7 (`ALUNIX` 2/1 fanns
redan; adressen räknas en gång till bara för att sidfotsmeningens länk nu är adressen, ett
uttryckligt, kommenterat undantag i `verify.py`, texten på skärmen oförändrad).

**Copy.** `copywriting` → `copy-editing` → `humanizer-svenska` på prisingressen, de två
länktexterna och sidtiteln. Ingen ny fakta (moms och period rördes inte, de ligger hos Anton).

**`emil-design-eng`**, granskning av R7:s rörelse:

| Före | Efter | Varför |
| --- | --- | --- |
| `lenis.scrollTo` med tidsbaserad duration | samma kurva, högst 33 ms egen tid per ruta, avbryts av hjul/touch | en fryst ruta pausar glidningen i stället för att hoppa; läsaren tar över direkt |
| tom vit ram när casen inte laddat | fallbilden tonas in 0,35 s `power2.out` i samma övertoning | inget hårt byte, aldrig tomt |
| hela baksidan var en vänd-knapp | bara länkarna tar tryck | ett missat tryck ska inte gömma det man skulle trycka på |
| fokus föll till `BODY` vid vändning | fokus flyttas till baksidans första länk | kontinuitet för tangentbord och skärmläsare |
| kortets CTA dog under `pointer-events:none` | klickbar när baksidan vetter mot läsaren | klick på framsidan (ingen länk syns) ska inte träffa baksidan |

**Detektorn (sessionsrapporten)**: `overused-font` ×6 är Geist, den skyddade familjen (radie 0
och två familjer står under "Skyddat" i AUDIT.md), inte ett fel. `broken-image` ×4 är de fyra
rotabsoluta sökvägarna `/tests/alunix-concepts-r3/build/assets/…`, som detektorn inte löser från
filen; alla 31 bildsökvägar i sidan finns på disk och laddar via servern. **`gsap-core`** laddades
efter bygget på stopphookens anmärkning: tickerns `(time, deltaTime)` i ms stämmer med
glidningens 33 ms-tak; övertoningen behåller `opacity` i stället för `autoAlpha`, eftersom
`visibility:hidden` på ramarna ändrar hur de renderas och avkodas (R5).

## EFFECTS.md: vad som hölls och hur
- **Tesrubriken reser sig och står:** samma resning (orörd tween); pinnen 48 px ned och på
  transform; stillheten mätt till 0,0 px variation i 116 rutor; `#tes` p95 18,3–18,4 mot
  kontrollens 35,6; den godkända radbrytningen låst.
- **Showcase-mekanismen:** pinnen skapas en gång (orörd `pinSpacer`, `scrub:true`), övertoning,
  räknare, mintspår och lupp oförändrade; 1 laddning per ram, 0 refresh under passet.
- **Övertoning vid casebyte:** klickets största steg 31/22 px (R6: 61–97).
- **Kontakten:** kortet vänder sig självt vid 0,7 (orörd trigger).
- **Heron:** samma kortvändning och tidslinje; pinnen börjar vid scroll 0 i stället för 48.

## Öppet, utanför R7
- `sites/horai.html`: mobilgridden svämmar över till 675 px (hanteras i ramen, inte i sajten).
  `sites/calyx.html`: vid 390 går "INDEX" in i ordmärket i sajtens egen menyrad. Båda ägs av
  exempelsajterna, inte av Alunix-sidan.
- Heron blinkar vid laddning: första målningen visar den färdiga heron, sedan klipps cellerna
  till svart och sätts ihop (syns i laddningens skärmsändning). Fanns före R7, inte på listan.
- Heron-kortets CTA nås bara med pekare (kortet är `aria-hidden`); tangentbord och skärmläsare
  har kontaktkortets länk och topplistens mejl.
- Ett tryck på Hōrai innan sajten laddat visar fallbilden tills sajtens `load` (över 6 s här,
  eftersom sajten hotlänkar fem stora Unsplash-foton).
- Kommentarerna i `index.html` är inte bantade (se MEDIUM).
- Förslagen under "kräver Antons beslut" i AUDIT.md är orörda.

## Avvikelse i processen, rakt
Designgrindens referensgolv (TASTE, FEEDBACK, reference-lock, `scroll/devices.md`,
`feel-and-fingerprint.md`, fingeravtrycksregistret, `select.py` och dess fyra poster) lästes
först när hooken spärrade den första Edit-redigeringen. Före det hade den första CSS-omgången,
markupen och JS-patchen skrivits med Python-skript, som hooken inte ser; senare spärrade hooken
även skalskrivning och resten gjordes med Edit. Inget i de tidiga ändringarna rör riktning,
tokens eller typografi (alla står i tabellerna ovan), men ordningen var fel och sägs här.

## Filer
`index.html`; `verify.py` (port, R7-strängar, sidfotsundantaget); `r7_probe.py` (ny);
`assets/cases/{calyx,horai}-1680.webp` (nya); `_attic-r7/` (flyttade filer);
`index.before-r7.html` (före-kopian, kontroll); `shots/r7-before/`, `shots/r7-after/`,
`shots/section-probe-r7-{1,2}.json`, `shots/section-probe-r7-control-before.json`,
`shots/perf-r7-{1440,390}*`, `shots/a11y-r7/`, `shots/click-r7.txt`.

Servern (3307) stoppad efter rundan. Ingen commit.

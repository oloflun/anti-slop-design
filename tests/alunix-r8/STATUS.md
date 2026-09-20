# Alunix r8, status

_Senast uppdaterad: 2026-09-20 (V3d R23)._

En rad per cell. Lead uppdaterar efter varje runda, före nästa startas.
Rundordningen står i `PROTOCOL.md`, exit-villkoren i planens § 7.6.

Dispositionsord: `not-started` · `in-round` · `blocked` · `pending-anton` ·
`SHIP`. `SHIP` sätts bara när allt i § 7.6 är sant, inte på känsla.

| Cell | Runda | Disposition | Gröna grindar | Öppna punkter |
|---|---|---|---|---|
| V3c | **klar, exit-granskad** (R4-R13) | **ship med oppna fragor till Anton** | Astra ship utan fynd - design-critic: slar V3b, oryzo-ai, dope-security, mattis-studio, monologue, planhat, insign, highwaymedia; star sig bredvid hoy - a11y: WCAG 2.2 AA konform, alla atta R5-fynd stangda - HELHET 29 av 35 - last copy 15/15 - 768-felet fixat, noll text utanfor arket vid sex bredder | Oppet: Q30 bandet (tre H-rader), Q31 rubrikens grad, Q32 papper eller invert, P1-P10 i processunderlaget, liggarens rad 03, plugin-cachen. Sma: 16:9-ledaren, tal i ledger R1, a11y-skuld i sju rader |
| V3d | **R23 byggd, overifierad** (V3d R1-R23, 2026-09-20) | **in-round, vantar pa veckokvot** | R22: konturen sluter sig om arkets fyra sidor, slutrektangeln landar inom 1 px (Astra r22 `ship`). R23: alla nio punkter i Antons beställning byggda och renderande — `.hero-sub` borta, processtexten i vänsterspalt med arket flush höger (1311 px / 68,8 % vw), stämpelruta med rubriken inne i arket, Exempelcase 49 px mot Calyx 122 px, case-etiketterna `Florist, Stockholm` / `Restaurang, Asian Fusion`, Young Serif borttagen (tre typsnittsfiler, noll tredjepartsanrop), prisliggare i Public Sans med tabulära siffror, egen kontaktsektion med formulär. Copy-kedjan körd, låst copy 11/11. **Plan 067 § Verification A/B/C kördes aldrig — full disk.** | **Antons dom 2026-09-20: punkterna gjorda, nivån inte nådd.** Underkänt: övergången blå → ritning (46 av 121 bildrutor under 18 % textyta; planets blå ljusare än tesbandets), processektionerna trånga med för lång text och klippt rubrik, case-övergångens mörka ruta, case-ingressen fortfarande slop (F-018 bruten av min egen leverans), kontaktsektionen ska inverteras till svart. Allt i `runs/V3d/HANDOFF-2026-09-20.md`. `PROMPT-V3d-R24.md` klar men måste utökas. Hos Anton: P4 (skriver/fotograferar vi åt kunden?), Hōrai 390, 260-532 ms i Hōrai-ramen |
| K3 | R3 klar, fixrunda | **blocked** | gate 75 · noll gate-deny · catalogue-select · staircase 0 · max_step 1,41 % | Plan 002, 004, 005 verified; 003 accepterad avvikelse med skäl; **001 kvarstående**: öppningen visar inget fotografi och Calyx nav överlappar sig själv vid 390. Ny plan 006 ersätter 001 |
| K4 | R3 klar, **parkerad som referensmönster** för före/efter-showcase (Antons dom 2026-09-15, F-015) | **parkerad** | gate 75 · noll gate-deny · catalogue-select · staircase 0 · max_step 2,49 % | Plan 001 och 002 verified; 003 accepterad avvikelse på 3,7 px-raden; **ny avvikelse**: `.tag--after` klipper den låsta bildtexten vid varje bredd under 640, ett följdfel av plan 003. Ny plan 004 |

**Gröna grindar** noteras med skriptnamn, inte prosa: `detect` · `preflight_taste`
· `scroll_verify` · `perf_probe` · `motion_probe` · `contrast_over_media` ·
`a11y-audit` · `copy-gate` · `F-007` · `kvartetten 4/4`. Bara grindar som körts
efter den runda raden gäller räknas som gröna.

**Öppna punkter** är det som hindrar nästa disposition, med källa (F-post,
TASTE-§, katalogpost eller agentrapport).

## Fas 0

| Leverabel | Status | Bevis |
|---|---|---|
| Registret | **klar, utan append** | De 31 raderna fanns redan: 29 Alunix-rader plus r7:s K1 v2 och K2 v2, införda vid conclude 2026-09-08. Att appenda igen hade duplicerat, och rader är append-only. I stället verifierades alla 29 rader ha sex ifyllda grinddimensioner, och tio tomma Register-celler fylldes ur cellernas egna filer. `grep -c -i alunix` ger 35; noll dubblerade Build-värden bland de 36 dataraderna |
| `PRODUCT.md` | **klar** | 180 rader. 84 påståenden spårade till `tests/alunix-ab-r7/PROMPT.md` rad för rad, två underkända och rättade före leverans. Noll tankstreck, kontrollerat också för U+2010 till U+2015 och U+2212 |
| `concepts.md` med målbildsgrind per cell | **klar** | 183 766 tecken. Sammanslagen ur `concepts-V3c.md`, `concepts-K3.md` och `concepts-K4.md`, med leadens godkännandetabell, K3-lås-villkoret och K3-mot-K4-tabellen i huvudet. Fingerprint: K3 ingen rad under 4/6, K4 lägst 5/6 mot tre rader som bara delar grammatik, K3 mot K4 8/8 |
| Briefskelett per cell | **klar** | `runs/V3c/BRIEF.md`, `runs/K3/BRIEF.md` (35 496 B), `runs/K4/BRIEF.md` (33 854 B) |
| Assetpaket per cell | **klar** | `runs/<cell>/assets/ASSETS.md` och `credits.json` för alla tre. Noll genererat material i r8 |
| Beslutsledger per cell | **klar** | `runs/<cell>/NOTES.md` för alla tre |
| Rundprompter R1 till R3 | **klar** | Nio filer, `PROMPT-R{1,2,3}-{V3c,K3,K4}.md`. Alla nio torrkörningar exit 0, verifierade av lead |
| Leadens pixelgrind | **klar** | Lead läste `oryzo-ai`, `mattis-studio`, `squarespace`, `paper`, `aevi-wellness`, `beautiful`, `insign` och `mode` som bilder. Utfallet blev villkoret i `concepts.md` och Q19 |

## Infrastruktur

Klar, torrkörd 2026-09-09. `run.py` (ärver r6), `PROTOCOL.md`, den här filen,
`runs/<cell>/{assets,shots,plans}`, `logs/`, `board/`, launch-posten
`alunix-board-r8` på port 4626 med `--single`.

## Runda 1, mätt

| Cell | Turer | Kostnad, USD | Exit | Subtype | Anmärkning |
|---|---|---|---|---|---|
| V3c | 116 | 12,84 | 0 | success | Avslutade rent med en egen slutrapport |
| K3 | 98 | 17,97 | 1 | success, `is_error: true` | Avbruten av kontots användningsgräns efter att briefen skrivits |
| K4 | 127 | 23,02 | 1 | success, `is_error: true` | Samma. Avslutade med ett `cat >>`-heredoc mot briefen, läst extra noga av lead: rent och fullständigt |

Summa runda 1: **53,83 USD**. Leveransen landade i alla tre cellerna trots de två avbrotten;
briefarna slutar sammanhängande och ingen bär en `[PAUSED]`-markör.

**Route-vs-invocation-gap (GOALS mätpunkt 2): inte mätbar i R1.** Ingen av de tre sessionerna
skrev en Stop-rapport under `.impeccable/`, och R1 skriver noll UI-filer, alltså utlöses noll
route-rader. Ett gap på noll skulle vara sant men tomt. Första meningsfulla mätningen är R2.
Kontrollera då först att `design-stop.py` faktiskt lämnar en rapport.

**Teckenåterställning.** `runs/K3/BRIEF.md`, `runs/K3/NOTES.md` och `runs/K4/BRIEF.md` skrevs av
fas 0-arkitekterna via skalet och tappade å, ä och ö på 127 rader. Lead återställde dem
deterministiskt och verifierade att ingen låst copy-sträng och inget kodspann rördes. Se Q21.

## Runda 2, mätt

| Cell | Turer | Kostnad, USD | Exit | Subtype | F-007 |
|---|---|---|---|---|---|
| V3c | 106 | 37,89 | 0 | success | godkänd |
| K3 | 107 | 38,68 | 0 | success | avvikelse |
| K4 | 94 | 36,18 | 0 | success | avvikelse |

Summa runda 2: **112,75 USD**. Alla tre avslutade rent, till skillnad från runda 1.

### Mekaniska grindar

| Grind | V3c | K3 | K4 |
|---|---|---|---|
| `scroll_verify` deadScroll | 0 | 12 | 15 |
| `scroll_verify` cuesNeverFull / unrevealed / contrastUnderMedia | 0 / 0 / 0 | 0 / 0 / 0 | 0 / 0 / 0 |
| `motion_probe` staircase | **0** | **0** | **0** |
| `motion_probe` p95, cpu 1 | 16,7 ms | 16,8 ms | 33,3 ms |
| `motion_probe` frames > 33 ms, cpu 1 | 1 | 5 | 19 |
| `motion_probe` max_step | **4,12 %** | 1,45 % | 2,33 % |
| Tankstreck i synlig text | 0 | 0 | 0 |
| `gate-deny`, inklusive `shell-write` | 0 | 0 | 0 |
| Motorn och `sc-smooth.js` inkopierade | ja | ja | ja |
| `catalogue-select`-låset oförändrat | ja | ja | ja |

Baren är p95 ≤ 20 ms, noll frames > 33 ms, max_step ≤ 3 %, staircase 0. **Ingen cell klarar
den ännu**, men staircase är 0 i alla tre: F-014:s utjämning fungerar, och det som återstår är
bildtid, alltså F-013:s andra fel. Alla tal ska tas om i fixrundan, eftersom hela runda 2
mättes mot fallback-typsnitt (se nedan).

### Route-vs-invocation-gap, GOALS mätpunkt 2

Rått: V3c 3, K3 5, K4 4. Rättat blir det **1 per cell**, och rättelsen är i sig ett fynd:
`review-animations` bär `disable-model-invocation: true` och kan bara startas av Anton, så att
räkna den lägger ett permanent golv på 1 i varje session och måttet kan aldrig nå 0.
**Mätpunkten behöver den definitionsändringen för att vara meningsfull.** `a11y-audit` och
`emil-design-eng` ligger i R3-prompten och är schemalagda, inte hoppade. Kvar är `copy-gate`
och `impeccable`, som inte kördes trots att R2 skrev synlig text i alla tre cellerna. Att gate
97 stod öppen på V3c är beviset: pilen är precis vad copy-gaten fångar.

### Typsnitten var ovendorade under hela rundan

`assets/chivo-var.woff2`, `martian-mono-var.woff2`, `switzer-variable.woff2` och
`reddit-mono-variable.woff2` refererades av cellerna men fanns inte på disk, så varje skärmbild
och varje mätning i rundan, byggarnas egna inräknade, togs mot fallback-stacken. Lead har
vendorat alla fyra och bekräftat i webbläsaren att de laddar. K3 ligger på 2 filer och 57 kB,
K4 på 2 filer och 74 kB, båda under budgetens 3 filer och 300 kB.

## Runda 3, mätt

| Cell | Runda | Turer | Kostnad, USD | Exit | Rundans art |
|---|---|---|---|---|---|
| V3c | 3 | 104 | 38,95 | 0 | hela sidan |
| K3 | 3 | 77 | 28,75 | 0 | fixrunda, planer 001 till 005 |
| K4 | 3 | 82 | 31,72 | 0 | fixrunda, planer 001 till 003 |

Summa runda 3: **99,42 USD**. Ackumulerat för r8: **266,00 USD**. Alla tre avslutade rent.

### Mekaniska grindar, runda 3

| Grind | V3c | K3 | K4 |
|---|---|---|---|
| Låst copy ordagrant | **15 av 15** | ej byggd än | ej byggd än |
| Tankstreck i synlig text | 0 | 0 | 0 |
| `gate-deny`, inkl. `shell-write` | 0 | 0 | 0 |
| `catalogue-select`-låset | oförändrat | oförändrat | oförändrat |
| Typsnitt lokala, 200 per fil | ja, 3 filer | ja, 2 filer | ja, 2 filer |
| `motion_probe` staircase | 0 | 0 | 0 |
| `motion_probe` p95 / rutor > 33 ms, cpu 1 | 33,4 ms / 36 | 16,8 ms / 5 | 33,3 ms / 17 |
| `motion_probe` max_step på spelhuvudet | **3,38 %** | 1,41 % | 2,49 % |
| `preflight_taste` | PASS | FAIL (7), alla dömda | PASS |
| `detect.mjs` | 4, namngivet undantag | 0 | 0 |
| CLS 1440 / 390 | 0,003 / **1,038** | ej mätt | ej mätt |
| Stop-rapport under `.impeccable/` | ja | ja | ja |

**Mätprotokollet.** Kontrollen `tests/motion/smooth.html` kördes före varje sidmätning.
Vid cpu 1 gav kontrollen noll rutor över 33 ms, så talen ovan gäller. Vid cpu 4 gav kontrollen
2 rutor över 33 ms i två körningar i rad, alltså har den här maskinen ett golv vid cpu 4 och
cpu 4 används inte som dom. Rått `--sc-p` spårades aldrig.

### Route-vs-invocation-gap, GOALS mätpunkt 2

Rått: V3c 3, K3 5, K4 4. Rättat, alltså exklusive `review-animations` som bar
`disable-model-invocation: true` upstream: V3c 2, K3 4, K4 3. Men **copy-gaten är substantiellt
täckt i V3c den här rundan**: transkriptet namnger `copywriting` 15 gånger, `copy-editing` 7,
`humanizer` 15, `humanizer-svenska` 6 och `deslop` 11, alltså gatens fem pass, och R2:s strängar
ingick. Kvar i V3c:s gap är bara `impeccable`. K3 och K4 var fixrundor och deras R3-skills
ligger kvar i R3.

**Undantaget som inte var byggarens fel:** `Skill(review-animations)` nekades för V3c:s byggare
eftersom skillen bar `disable-model-invocation: true`. Bevakaren har tagit bort flaggan (Q24).
Steget är öppet, inte rött, och körs om i nästa V3c-körning.

### Öppna punkter i mätningen

- V3c:s byggare hoppade över `scroll_verify` helt i R3 och skrev bara spelhuvudets `max_step`
  i NOTES, inte rutorna mot kontrollen. Leadens egna mätningar täcker rundan.
- `contrast_over_media.py` ignorerar `--url` och går mot port 3055. Verktygsbugg utanför r8.
- `perf_probe` mäter de inbäddade exempelsajternas skuld som cellens: hero-bilden på 1,12 MB
  och de 19 typsnittsfilerna kommer ur `sites/*.html`. Prestandagranskaren mätte cellens egen
  vikt till **334 kB vid både 1440 och 390**, med tre typsnittsfiler på 37 792 B och noll
  externa referenser i cellens egen markup.

## Nästa körning per cell

| Cell | Promptfil |
|---|---|
| V3c | `tests/alunix-r8/PROMPT-FIX-V3c.md`, planerna 001 till 008 i nummerordning, och steg 3 först: `review-animations`, `scroll_verify` och `motion_probe` med kontrollprotokollet |
| K3 | `tests/alunix-r8/PROMPT-FIX-K3.md` med plan 006 inlagd, som ersätter plan 001 |
| K4 | `tests/alunix-r8/PROMPT-FIX-K4.md` med plan 004 inlagd |

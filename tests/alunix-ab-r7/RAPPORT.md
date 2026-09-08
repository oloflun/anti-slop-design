# r7-rapport — K1 Skymning och K2 Affischen om igen, kedjan bevisat tänd

Skriven av Claude (orkestrerare) 2026-09-06. Alla siffror kommer ur loggarna
(`logs/round-N/*.jsonl`, `probes/*.jsonl`), ledgern (`.impeccable/design-session.jsonl`) och
monitorn (`monitor/*.md`); alla domar ur bilder jag läst (`review/`). Ingenting i rapporten är
antaget. Läs `README.md` för uppställningen och `design-catalogue/FEEDBACK.md` för domen på r6.

## 0. Det r6 aldrig visade dig

Din Chrome kör `prefers-reduced-motion: reduce` (Windows: Animationseffekter av). r6:s celler
lydde det. Med rörelse påtvingad ser kedjans K1 ut så här: `../alunix-ab-r6/review/B-K1/grid-motion.png`
(set-piece 15–40 %: inzoomning mot fönstret som blir Hōrai i helskärm). Under reduced motion:
`../alunix-ab-r6/review/B-K1/grid-reduced.png` (tumnageln i vila, resten plant). Det senare är
vad du dömde. Boarden varnar nu när läget är på (kontrollerat i panelen 2026-09-06).

## 1. Kedjeförändringarna (verifierade)

| Ändring | Fil | Bevis |
|---|---|---|
| `ref-read` per fil och kategori | `hooks/design-vision-track.py` | ledgerrader i provet, § 2 |
| Referensgolv: gate nekar första UI-skrivning | `hooks/design-gate.py` | provet steg 1 (neka) och 3 (släpp), § 2 |
| Scroll-signal i intent + SCROLL-block | `hooks/design_hook_lib.py`, `hooks/design-intent.py` | korpus 45/45; provets `<design-gate>` |
| Scroll-route på kodsignaler | `references/component-routing.md` | verify-check; route-rad i runda 2 |
| Stop: § 8 Referensgolv, scroll-gap, rm-bild i exit-bar | `hooks/design-stop.py` | stop-rapporterna per runda |
| Dött `scroll-craft` bort | `hooks/design-telemetry.py` | diff |
| TASTE + FEEDBACK alltid, `extract/*-DESIGN.md`, 2b 1–4 obligatoriska, reservläget, `serve.py` | `SKILL.md` | diff |
| Målet tyst i vila; TASTE § 4.8-precisering | `house-physics.md`, `TASTE.md` | diff |
| § 12 Delegated builds (golv i brief, rundor, målbildsgrind, fotopaket) | `skill-orchestration.md` | diff |
| `FEEDBACK.md` F-001–F-009 | `design-catalogue/FEEDBACK.md` | filen |
| `serve.py`, boardens reduced-motion-rad | `scripts/serve.py`, `scripts/board.py` | Playwright-test (reduce → rad, no-preference → ingen) |

**Parallellsäkring (hittad i runda 1, 2026-09-07).** `design-session-start.py` raderade vid varje
ny session `.armed`, `.design-verb`, `.stop-blocks`, `.linked-roots` och roterade ledgern
över `prev`; två parallella byggare + orkestreraren delade samma filer, så K2:s intent-rad
försvann när K1 startade och provets rader hamnade i prev. Nu: per-session-filer
(`.armed-<sid8>` osv. via `design_hook_lib.session_file`), ledgern *appenderas* till prev
(tak 4000 rader) och `all_rows()` läser båda; stale filer (>24 h) rensas i stället för allt.
Verify: ny sektion "behaviour: concurrent sessions". Byggt av en Sonnet-agent i en
worktree mot commit-toppen och portat av mig för hand ovanpå golvändringarna.

`python verify-design-system.py`: efter porten alla check gröna utom 2 fel som fanns före sessionen (två portade
referenser skiljer sig från uppströms `hallmark`, orörda av oss). `tests/intent_corpus.jsonl`
45/45. `scripts/sync-from-live.py --check`: in sync.

## 2. Provet (Sonnet, headless, kedjan på)

`run.py probe B --prompt-file probe-prompt.md`: `claude-sonnet-5`, effort high, 23 varv, 107 s,
$0,91, session `b03dc010…`. Logg `probes/B.jsonl`, monitor `monitor/probe-B.md`.

| Steg i provet | Vad loggen visar |
|---|---|
| Prompten nämner scroll, pin, scrub | `UserPromptSubmit` → `<design-gate>` injicerad **med SCROLL-blocket** efter `</design-gate>`; ledgerraden `intent … scroll: 1` |
| Första `Write` av `probe.html` innan läsning | `PreToolUse:Write` → **deny**, `[design-gate · referensgolv]` med fyra rader (TASTE.md, FEEDBACK.md, entries, reference-lock.md) och två scrollrader (devices.md, feel-and-fingerprint.md) |
| Sju `Read` | sju `ref-read`-rader: taste 1, feedback 1, catalogue 2 (rogo: `entry.md`, `fold.webp`), references 1 (`reference-lock.md`), references/scroll 2; `fold.webp` gav dessutom `vision` |
| Andra `Write` | tillåten; `PostToolUse:Write` → route-rader (`copy-gate`, `impeccable layout`) |
| Första `Stop` | **block**: "1 UI edits this session and the page has scroll choreography but no reduced-motion capture …" |
| Agenten skjuter `rm-probe.png` och läser den | andra `Stop` → rapport `.impeccable/design-report-20260906-2133.md`, § 8 Referensgolv: taste 1 · feedback 1 · catalogue 2 (rogo) · references 1 · scroll 2 · scripts 0 |

Ett hål som provet avslöjade och som stängdes direkt: agenten läste alla referenser men
laddade aldrig `Skill(design)` (0 Skill-anrop). Golvet kräver nu också att skillen är laddad
(Skill-anrop eller läsning av `design/SKILL.md`); ny verify-check "floor names Skill(design)".
Provet kördes före den ändringen; runda 2:s loggar bevisar den skarpt.

Monitorns "hook source: other" beror på att 2.1.260 rapporterar hooknamn som
`PreToolUse:Write` utan sökväg; de enda designhookarna i processen är repots (plugin-skalet,
`super-intelligence` avstängd i `--settings`), vilket init-raden visar.

## 3. K1 Skymning v2, runda för runda

| Runda | Varv · kostnad | Kedjebevis (monitor) | Min dom på pixlarna |
|---|---|---|---|
| 1 (referensdigest) | 56 · $1,81 | `Skill(design)` varv 3; ref-read: taste 1, feedback 1, references 6 (scroll 4), scripts 2, catalogue 21 (rogo + groupemontoni: entry, DESIGN.md, fold, slices) | BRIEF.md 495 rader: lock (Rogo primär, Montoni lånad detalj), grammatik med sju förlorare, feeling curve, device-tabell (scrub → pin → kinetic → reveal → flow → reveal+drift), fingerprint 4/6 mot r6 B-K1, reduced-motion-plan, `?preview=`-plan. Skrevs mot målbilden före F-010; F-010 gick in i runda 2:s prompt |
| 2 (fold + signaturakt), avbruten av användningsgränsen efter 72 varv och återupptagen (10 varv) | 82 · $8,04 | `Skill(design)` varv 3, `Skill(emil-design-eng)` varv 117; ref-read 35 (feedback läst två gånger: F-010), 53 vision-rader (egna maskkontroller `mask_check_f064/076/088/100.png` + 21 skärmbilder), 13 route-rader varav 4 `scroll`, 0 nekanden | **Godkänt:** resan scrubbas, rubriken tonar och blurrar, Hōrai bara i öppningen från ruta 64 bakom glasets spröjs, fortsatt inzoomning tills öppningen fyller skärmen (`review/B-K1/grid-dense.png` 28–40 %), reduced motion med fyra egna sektioner. **Underkänt → runda 3:** ramen läcker in som en remsa längst ned vid 40 % innan bytet; `?preview=window` mot svart i stället för sista videorutan; två Hōrai-ramar laddas i rörelseläge; utgångens plate krymper till en gissad position i tomrum eftersom akt 4 inte fanns |
| 3 (hela sidan) | 86 · $9,37 | `Skill(copywriting)` varv 8, `humanizer-svenska` varv 10, `design` varv 3, `emil-design-eng` varv 192; 36 route-rader varav 9 `scroll`, 81 vision-rader, 0 nekanden | **Godkänt:** `?preview=window` visar sista rutan, en Hōrai-ram, bevisrader (Design/Calyx, Utveckling/Hōrai, System/Hyperborea), liggare i ljus serif, nattlandning med kontaktraden och krediter, reduced motion i ordning. **Underkänt → runda 4:** signaturen byggd som tre motorakter i rad, varje scen synlig en viewport innan sin egen akt (motorns ground-or-greet) → fönstret dubblerat vid 20–25 % och Hōrai dubblerat vid 34–46 % (`review/B-K1/grid-dense2.png`) |
| 4 (en pinnad akt) | 53 · $8,66 | `design-verify` varv 47, `emil-design-eng` varv 76 och 192, `copywriting` 235, `humanizer-svenska` 237; DOM: `pin` span 5,0 → reveal → flow → drift; inga `[scrollcraft]`-varningar | **Godkänt:** obruten sekvens 0–56 % och baklänges (`grid-dense3.png`), ingen dubblering, exit landar i akt 4. **Underkänt → runda 5:** första rutan svart i vila (canvasen ritas först vid scroll); tomt vitt i över en skärmhöjd mellan utgången och första bevisraden |
| 5 (två rättelser) | 27 · $6,57 | `emil-design-eng` ×3, `copywriting`, `humanizer-svenska`, `design-verify`; 104 vision-rader | **Godkänt (slutläge inför kritikerna):** fotot ritat 300 ms efter load utan scroll (`review/B-K1/fold-300ms.png`), utgången landar i första bevisraden inom en halv skärmhöjd (`grid-dense4.png` 44–56 %). scroll_verify: 0 cues never full, 0 unrevealed. |
| 6 (kritikertrion) | 86 · $21,35 (ackumulerat) | `design`, `emil-design-eng` ×3, `copywriting`, `humanizer-svenska`, `design-verify`; 120 vision-rader | **Verifierat av mig efteråt:** `elementFromPoint` vid p=0,3 träffar ramen på tre punkter (klickbar); Tab går toppbar → Öppna Calyx → Öppna Hōrai → Öppna Hyperborea → kontakt; amberbrickan borta (`background: transparent`, siffran i amber-ink); glaslagret dämpat (`r6-preview-window.png`); inga ramar i DOM:en under reduced motion och toppbaren byter zon där; nattlandningen helt öppen på 390 (`r6-m390-end.png`); focus-ring mörk i ljus zon (`r6-proof.png`). Kvar: artefaktrutorna 40–60 i materialet (mildrade i tempo och vinjett, inte borta). **Slutläge.** |

## 4. K2 Affischen v2, runda för runda

| Runda | Varv · kostnad | Kedjebevis (monitor) | Min dom på pixlarna |
|---|---|---|---|
| 1 (referensdigest) | 45 · $1,67 | `Skill(design)` varv 3; ref-read: taste 1, feedback 1, references 6 (varav scroll 4), scripts 2, catalogue 24 (springsummer + indoek: entry, DESIGN.md, fold, 18 slices) | BRIEF.md 479 rader: lock, grammatik, feeling curve, device-tabell (pin+kinetic → reveal → flow → reveal → flow+drift), fingerprint 4/6 mot r6 B-K2, tre frågor (typsnitt, platen, Stockholm), alla besvarade i K2-r2.md |
| 2 (fold + signaturakt) | 65 · $6,41 | 12 UI-edits, 15 route-rader varav 7 `scroll` (kodsignaler `data-sc-`), 0 nekanden (golvet uppfyllt), 45 vision-rader (30 egna bilder lästa) | **Godkänt:** bokstavsfönstren mätta ur bläcket i A/U/X, platen bredvid dämpad, papperet glider Calyx → Hōrai → Hyperborea, kicker byts i takt, reduced motion bär sekvensen, 768-krasch hittad och fixad av agenten. **Underkänt:** andningen är en opacitetskorstoning med ALUNIX som grått spöke bakom nya rubriken (`review/B-K2/d-75.png`), och slutläget lämnar ett tomt band på nästan en skärmhöjd mellan `VI BYGGER` och `ERT VARUMÄRKE.` → runda 3 |
| 3 (hela sidan), avbruten av användningsgränsen efter 44 varv och återupptagen (40 varv) | 84 · $10,07 | 25 UI-edits, 31 route-rader varav 9 `scroll`, 82 vision-rader, 0 nekanden; **bara `Skill(design)`**: humanizer-svenska och emil-design-eng kördes som "checklistor" i huvudet, inte som anrop (route gap) | **Godkänt:** öppningen är nu ALU upp / NIX ned med rubriken i gapet, inget spöke; bevisrader som plates i spalt, svartvitt → färg; liggare för tjänster och pris; drift till bläck; reduced motion i ordning; 0 dött scroll (scroll_verify båda lägena); inget överflöde. **Underkänt → runda 4:** rubriken i gapet i lässtorlek och dubblerad i displaygrad under affischen; tjänsteraderna osynliga i helsidesfångsten (reveal utan säkring); avslutet ett tomt mörkt band; skills som anrop |
| 4 (rättelser + skills) | 145 · $23,85 (sessionens ackumulerade) | `Skill(humanizer-svenska)` varv 147, `Skill(emil-design-eng)` varv 150, `Skill(design-verify)` varv 193; 104 vision-rader; 0 nekanden | **Godkänt:** dubbletten borta, akt B börjar med kickern BEVIS, avslutet med kontaktlänken i övre tredjedelen, tjänsteraderna synliga i rörelseläge (helsidesfångsten visar dem inte: motorns flow-cue tänder i vy, noterat). **Underkänt → runda 5:** rubriken i gapet fortfarande i lässtorlek och kolliderar med NIX under öppningen (`review/B-K2/d-25.png`) |
| 5 (rubriken i gapet) | 127 · $24,50 (ackumulerat) | `emil-design-eng` ×2, `humanizer-svenska`, `design-verify`; 126 vision-rader | **Godkänt (slutläge inför kritikerna):** rubriken i gapet i displaygrad, syns först när gapet är öppet (`review/B-K2/grid-dense.png` 22 → 26 %), ingen kollision, `?preview=open` = reduced-motion-sektionen. |
| 6 (kritikertrion), avbruten av användningsgränsen efter 119 varv och återupptagen (7 varv) | 126 · $13,56 | `humanizer-svenska` ×2, `design-verify` ×2, `emil-design-eng` ×2, `design`; 149 vision-rader | **Verifierat av mig efteråt:** `?preview=open` under reduced motion visar rubriken (`.hline` opacity 1); mobil: blocket först, ingen kollision, egen scroll-länkad övergång (isärglidning + byte utan pin, `review/B-K2/r6-m390-grid.png`); klockan centrerad (x = 720); `<title>` utan tankstreck; ramarna `tabindex="-1"`; `Bevis`/`Tjänster` som `<h2>`; ordmärkes-svg `aria-hidden`; kicker `ORDMÄRKET ÖPPET` mellan hero och `.opened` i reduced motion; focus-ring `currentColor` i avslutet. **Kvarstående, flaggat till Anton:** kontrasten under avslutets drift har ett smalt sämsta läge på 3,35:1 (≈90 px scroll) som inte går att lösa inom fem färger utan att antingen sluta driften vid ~40 % mörker eller lägga en sjätte kulör; byggaren bevisade det matematiskt (`runs/B/K2/NOTES.md` § Öppna frågor). **Slutläge.** |

## 5. Higgsfield

Fullständig logg med varje anrop, kostnad och min läsning av rutorna: `higgsfield/LOG.md`.

| Steg | Modell | Credits | Utfall |
|---|---|---|---|
| Slutbild 1 (portens bågfönster) | Nano Banana 2, image-to-image | 2 | godkänd som bild, men fel mål |
| Std-test | Kling 3.0 std, 10 s, start+end | 15 | resan håller, slutar i porten (Antons rättelse: "det där är porten, ta fönstret bredvid", "det nedre") |
| Slutbild 2 (bottenvåningsfönstret till vänster om porten) | Nano Banana 2 | 2 | godkänd, `end-window-2.png` |
| Slutmaterial | Kling 3.0 **pro**, 10 s, start + ny slutbild | 17,5 | `pro.mp4` 1764×1176; resan kajen → porten passeras → det bågkrönta fönstret till vänster om banderollen fyller rutan t=7–9. Antons ja till pro 2026-09-07 (36,5 totalt, taket 35 höjt av honom) |

Material till K1: `runs/B/K1/assets/push/` = 100 rutor WebP 1440 px (10/s), `push-last.webp`,
`push.mp4` (all-intra), `window-track.json` (fönsteröppningen nycklad för hand av mig i åtta
rutor ur `higgsfield/pro-grid.png`, kontrollerad mot rutorna i `higgsfield/track-check.png`).
Den automatiska spårningen (`track_window.py`, färgtröskel) gav fel öppning i var tredje
ruta och lades åt sidan; nycklarna har ±2 % tolerans och byggaren kontrollerar masken
mot rutorna som bilder. Kvar: banderollen med hallucinerade tecken i sekund 4–6 (i utkanten
i pro-klippet; noteras som känd brist, ej maskad).

Saldo: 110 → 73,5 credits.

## 6. Kritikertrion

Sex Sonnet-agenter (`design-critic`, `design-a11y-reviewer`, `design-heuristics` per cell) med egna
Playwright-fångster i båda lägena; rapporterna i `review/B-K1/` och `review/B-K2/`
(`critic.md`, `a11y.md`, `heuristics.md`; a11y-agenterna skrev inte själva, deras fynd sparades av
mig). Alla fynd nedan verifierade av mig mot bilder eller mätvärden innan de gick in i runda 6.

**K1 Skymning** (kritiker: "F-010 är genuint löst"; alla tre: revise/block)
- Blockerande: ramen kan inte klickas i rörelseläge (`.exit-frame-wrap` opacity 0 ligger över
  den, `elementFromPoint` träffar aldrig ramen); sista aktens `--sc-p` når 0,50 vid max scroll på
  tre viewportar (nattfotot öppnas aldrig helt); ramen fångar mushjulet under reduced motion;
  Tab hoppar från toppbaren till sidfoten (inga länkar i bevisraderna).
- Höga: focus-ring guld mot ljus toppbar 1,65:1; toppbaren byter aldrig zon under reduced
  motion (2,2–2,4:1); fylld amberbricka bakom 01/02/03 mot byggets eget lock; glaslagret som
  moiré vid `?preview=window`; artefaktrutorna 40–60 i den genererade sekvensen.
- Mindre: kollisionsruta vid 44 %; `aria-hidden` på informativ toppbarsrad; alt-text som
  beskriver animationen; ingen laddningsindikator; inget `forced-colors`-pass.
→ runda 6 (`rounds/K1-r6.md`, 13 punkter).

**K2 Affischen** (kritiker: "klart bättre än r6, ännu inte bättre än SpringSummer/Indoek"; alla tre: revise/block)
- Blockerande: `?preview=open` visar tomt gap under reduced motion (`:not(.rm)`-gating);
  `?preview=open` trycker ALU in i platen på mobil; focus-ring 1,04:1 i avslutet; kontrasten
  faller till 1,29:1 under driften när grunden mörknar före texten.
- Höga: X:ets mask sväljer glyfen (rader + kolumner öppnas); signaturen saknas helt under
  900 px i båda lägena (två statiska ordmärken i rad).
- Medel/mindre: tab-ordning genom tre inbäddade sajter (17 stopp); ordmärket två gånger under
  reduced motion utan koppling; kickers som `<p>` i stället för `<h2>`; masker utan aria;
  klockan inte centrerad; mobilens ordning foto före ordmärke; tankstreck i `<title>`; ALU:s
  topp klipps 18 px vid `?preview=open`; träffyta 21,75 px.
- Orkestrerarens avgöranden: rubriken i gapet vid 3,5× läsgrad accepteras som andra
  displaynivå; `Stockholm` står kvar som antagande.
→ runda 6 (`rounds/K2-r6.md`, 18 punkter).

## 7. Slutläge och vad som inte gjordes

**Boarden:** `http://127.0.0.1:4625/board.html` (`alunix-board-r7` i launch.json). Riktning 1 =
K1 Skymning, riktning 2 = K2 Affischen; motor 1 = r6:s kedjecell (före), motor 2 = r7 (efter);
`p` för par, `x` för helskärm. Cellerna serveras från repo-roten så att `/sites/…`-ramarna
laddar. **Slå på Animationseffekter i Windows innan du dömer**, annars visar boarden
reservlägena och varnar om det i en rad högst upp. Servrarna 3201 (K1), 3202 (K2) och 4625
(board) står kvar.

**Kedjan, bevisad rad för rad.** Varje runda i varje cell började med `Skill(design)` (varv 3),
läste golvets filer (ref-read: taste 1, feedback 1–2, catalogue 21–24, references 6 varav
scroll 4, scripts 2–5), fick route-rader med `scroll`-signal från första UI-skrivningen,
anropade `emil-design-eng`, `humanizer-svenska`, `copywriting` och `design-verify` som skills
när prompten krävde det, och avslutades med en stop-rapport med § 8 Referensgolv. Noll
nekanden i byggrundorna (golvet var redan uppfyllt); provet visade nekandet. Monitorn per
runda: `monitor/B-K1-r1…r6.md`, `monitor/B-K2-r1…r6.md`, `monitor/summary.md`.

**Vad r7 kostade (CLI:ns resultatrader, USD):** K1 rundor 1–6: 1,81 · 8,04 · 9,37 · 8,66 ·
6,57 · 21,35; K2: 1,67 · 6,41 · 10,07 · 23,85 · 24,50 · 13,56 (vissa rader är sessionens
ackumulerade belopp, CLI:n är inte konsekvent). Higgsfield 36,5 credits. Tre användnings-
gränser (K1 r2, K2 r3, K2 r6, alla återupptagna med `--resume`).

**Inte gjort, medvetet:**
- Ingen omtagning av Kling-klippet trots artefakterna i rutorna 40–60 (banderoll, skylt,
  lyktstolpe): budgettaket. K1 mildrar dem i tempo och vinjett. En omtagning kostar 17,5
  credits; din sak.
- K2:s kontrastdipp under driften (3,35:1 i 90 px) lämnad som dokumenterat restproblem med
  två lösningsvägar; din sak att välja.
- `Stockholm` vid K2:s klocka och rubriken i gapet vid 3,5× läsgrad: mina avgöranden, kan
  ändras.
- Fingerprint-raderna för K1 v2/K2 v2 är inte förda in i valvets register
  (`wiki/projects/_index/design-fingerprints.md`); görs vid `/conclude` om du vill ha dem.
- Ingen commit, ingen push.

**Fynd om kedjan under r7 som inte fanns i planen:**
- Orkestreringssessionen saknar `CLAUDE_CODE_SESSION_ID` i hookmiljön, så dess stop-hook
  räknade byggarnas rader (125–209 "UI edits") och blockerade mina stopp tills en bild
  lästs. Per-session-filerna hamnar i `nosession`-hinken för den sessionen. Bör fixas i
  `scope_to_session` (tom sid → bara rader utan sessionsfält) eller genom att sätta id:t.
- Motorns `drift`-device med en enda zon faller tillbaka på samma färg (`mixColor(X,X,t)`),
  så grunden hoppar i stället för att drifta; K2 kringgick det med egen JS. Bör upp i
  `devices.md` som fälla.
- `contrast.py`/`contrast_over_media.py` är hårdkodade till `localhost:3055`; både byggare
  och granskare skrev egna prober. Bör få en URL-parameter.
- a11y-granskaragenten vägrar skriva sin rapportfil (läs-bar roll); orkestreraren sparar.
- Runda-prompter med ordet `skill`/`skills` går inte längre under negativlistan (verifierat:
  `classify` = high för båda runda 2-prompterna), men gaten återinjiceras bara när verbet
  byts, så en resumerad runda får ingen ny `<design-gate>`; det är avsett.

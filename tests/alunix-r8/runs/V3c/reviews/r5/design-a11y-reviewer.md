fix

## persistence

Läst denna körning, i ordning: `~/.claude/skills/a11y-audit/SKILL.md` i sin helhet (inklusive F-011-överstyrningen), `references/principles.md`, `references/report-template.md`. Mål och brief: `tests/alunix-r8/runs/V3c/index.html` (rader 180-905 CSS, 906-1240 markup, 1241-1460 JS), `BRIEF.md` rad 1-433, `NOTES.md` § R5 + § R5 leadens pixelläsning. Målbild: `tests/alunix-r8/malbilder/V3c.md` och `plans/010-process.md` § Target + § Målbild skärm för skärm (1440 och 390) + § Device-tabell. Pixlar lästa: `shots/r5-lead/proc-1440-01.png`, `proc-1440-05.png`, `proc-390-03.png`, `p390-back.png`, plus två egna fångster vid scrollY 4000 och 4700 (1440x900). Referenspixlar: `design-catalogue/entries/{oryzo-ai,mattis-studio,insign,highwaymedia,hoy}/fold.webp`.

Kontrollen körd först mot `tests/a11y/broken.html`: `a11y_scan.py` 5 violations, `tab_walk.py` 3 issues, `reflow.py` overflow320 på 6 noder plus `unrevealed: 1`. Alla tre hittar fel. `contrast.py` **kunde inte köras**: URL hårdkodad till `localhost:3055`, ingen `--url` (rad 77); posten är `Not verified` och ersätts av `contrast_over_media.py --url` plus egna pixelmätningar.

| Pass | Bevis som inspekterats | Resultat |
|---|---|---|
| 0 Scope | Live URL på `localhost:3090`, källfil, 5 skärmbilder, brief, målbild | Verifierat, inte inferrerat |
| 1 Mekanisk | `a11y_scan.py` (0 violations, 40 passes, 1 incomplete), `tab_walk.py` (2 stopp, 0 issues), `reflow.py` (overflow320 tom, overflowZoom200 tom, `unrevealed: ["li"]`), `contrast_over_media.py` vid 1440 och 390 samt scroll 3900/4400/5900 (allt pass), `contrast.py` ej körbar | 0 mekaniska fynd, 1 verktygsblind fläck bekräftad (F-01) |
| 2 POUR | Landmärken (banner/main/contentinfo), rubrikträd (1 h1, h2, h3), `lang="sv"`, båda iframes har `title`, SVG:n `role="img"` + `title` + `desc`, alla `<img>` har alt | 2 fynd (F-01, F-02) |
| 3 Kognitiv (COGA) | Sju skärmar vid 1440x900 och 390x844, processaktens 2700 px med 41 mätpunkter | 3 fynd (F-03, F-05, F-08) |
| 4 Innehåll | All synlig copy, 18 låsta strängar, alt-texter, länktexter | 2 fynd (F-09, F-11), båda LOW |
| 5 Adaptiv | 320, 390, 1000x600, 1200x700, 1366x640, 1440x900, 200 % zoom, textavstånd 1.4.12, gråskaletest. `prefers-reduced-motion` ej granskad, F-011 | 1 fynd (F-08) |
| 6 Interaktion | Tab-vandring, PageDown-vandring (8 tryck), fokusring mot båda grunder, träffytor vid 320/390/1440, elementFromPoint och caretRangeFromPoint över processtegen, iframe-inertitet | 4 fynd (F-03, F-04, F-05, F-06) |
| 7 Personor | 6 personor, 4 uppgifter ur briefen | 3 celler `fails`, 9 `friction` |

Inte granskat, redovisat: forced-colors och Firefox/Safari (`inert` på `<iframe>` propagerar enligt spec men är inte empiriskt verifierat här; bara Chromium är mätt). Testning med verkliga funktionshindrade användare är inte gjord.

## fidelity

s1 till s3 heron: topologin stämmer. Kortvändningen efter plan 011 läses i tre PageDown-tryck (ps 0, 0,39, 0,69, 1), signaturakten håller för Edge-personan. **Drift, defekt:** understrykningen i `Boka ett möte` mäter 2,92:1 mot kortets grund. s4 tes: rent, `cap-line` 5,95:1. s5 och s6: ramarna `inert` plus `pointer-events:none`, samma upplevelse för pekare och tangentbord, rätt lösning av plan 002. **Drift, defekt:** båda bildtexterna under ramarna faller till 3,06:1 när grunden driftar mot papper. s7 avslut: rent, 539x76 px mailto, 17,5:1.

`#process` mot plan 010: arket 880x495 sticky `top:202px`, vänsterspalt 384 px, sju fönster, allt läser `--sc-ps`. Stämmer. Måttsiffrorna kvar i accent i s-process-06: i denna domän **positiv** avvikelse (6,47:1 i stället för 5,09:1). Mobilavvikelsen (stegen staplade och alltid synliga) är materiell mot målbilden och samtidigt den enda anledningen till att mobilen inte ärver desktopens värsta barriär (F-03): återställs planens form måste den byggas med ett hållfönster som tål ett sidhopp, aldrig genom att kopiera desktopbeteendet nedåt.

| Severity | Location | Before | After | Why | WCAG | Who |
|---|---|---|---|---|---|---|
| HIGH | `index.html:580-581` (`.frame-cap`), `:994` Calyx och `:1069` Hōrai | `color:rgba(244,242,239,.86)`, 12 px, på den driftande fotografiska grunden. Mätt vid scrollY 4000: sämsta lapp 3,06:1, 50,1 % av bildtextens yta under 4,5:1; Hōrai vid 4700: 3,06:1, 10,4 % | Bildtexten på en yta med känd valör (ramens egen ljusa grund `#e9e5da` eller papperet) eller en valör per grund. Mål: >= 4,5:1 mot de ljusaste 5 % av underlaget vid varje scrolldjup | Axe missade den (foto som grund, `incomplete`); byggarens fyra kontrastkörningar låg alla inne i `#process` | 1.4.3 | Elin, Marcus, alla med kontrastkänslighet |
| HIGH | `index.html:445` (`.card-cta`, `text-decoration-color:var(--c-accent)`) | `#1e5e9c` mot `#0b0c0e` = 2,92:1; understrykningen är det enda som identifierar raden som länk | `text-decoration-color: currentColor` (17,5:1), eller ljusheten lyft till cirka `#3f84c9` = 5,0:1. Mål: >= 3:1 | Briefen mätte paret (§ rättelse 2, 2,93:1) och tog bort det ur fokusringen men lämnade det på sidans enda konverteringskontroll | 1.4.11 | Elin, Marcus |
| MEDIUM | `index.html:712-718` + `:683` | Varje steg håller full opacitet i 243 px scroll; PageDown flyttar 787 px. Mätt PageDown-vandring vid 1440x900: steg 01, 03, 05, 07 syns, 02, 04, 06 renderas aldrig | Mål: varje `<li>` >= 0,99 opacitet i >= 800 px scroll, PageDown ger 7 av 7 | Tre sjundedelar av akten existerar inte för den som scrollar med sidhopp; friktion, inte blockering (DOM) | 2.1.1, 1.4.13 | Tomas, Jonas |
| MEDIUM | `index.html:697` (`.process-steps li{position:absolute;inset:0}`) | Alla sju li i samma rektangel med `pointer-events:auto`. Mätt: med steg 02 synligt returnerar `elementFromPoint` steg 07:s fråga och `caretRangeFromPoint` ger "Vi finns kvar…" | Mål: `elementFromPoint`/`caretRangeFromPoint` över det synliga steget returnerar samma steg; rAF-läsaren sätter `data-active`, CSS `li{pointer-events:none} li[data-active]{pointer-events:auto}` | Den som markerar synlig text får en osynlig text | 1.3.2 | Sofia |
| MEDIUM | `index.html:1271-1277` (`setFace`), från `:1335` | Fokus på `.card-cta`, scroll uppåt, `faceBack.inert = true`: `document.activeElement` blir `BODY` | Mål: `activeElement` aldrig `body` av en scroll; `heroPlate.focus()` med `tabindex="-1"` före inertering | Nästa Tab börjar om från toppen, en hel scancykel per omstart | 2.4.3 | Tomas, Jonas, Elin |
| MEDIUM | `index.html:443-446` (`.card-cta`), `:257` (`.topline-contact`) | Träffyta 104x23 px vid 390 och 320, 116x26 vid 1440; toppradens kontakt 109x19 | Mål: >= 24x24 px golv, 44 px höjd via `inline-flex`/`::after`, utan överlapp | Under 2.5.8:s golv; sidans enda CTA | 2.5.8, 2.5.5 | Marcus, äldre användare |
| MEDIUM | `index.html:940-948` (`.face--back`), från `:1276` | Vid vila `aria-hidden="true"` + `inert`; kortbaksidans fyra strängar annonseras aldrig för en linjär skärmläsare | Mål: baksidans text i tillgänglighetsträdet från p = 0; ta bort `aria-hidden`, behåll `inert` för pekar-/fokusvägen, eller `.sr-only`-kopia | Innehåll villkorat av en scrollposition AT-användaren aldrig intar | 1.3.1 | Karin |
| LOW | `index.html:691-693` (`.process-stage{top:202px;height:495px}`) | 697 px; vid 1000x600 och 1366x640 ligger arkets nedersta band under vikningen under hela ritakten | Mål: hela arket innanför vikningen vid 1366x640, `height: min(495px, 100svh - 220px)` | Aktens sanna tal saknas när de skulle läsas på en vanlig bärbar | 1.4.10 | Elin |
| LOW | `index.html:1037`, `:1045` mot `:1102`, `:1109` | `h3 Design` och `h3 Utveckling` två gånger med olika betydelse | Mål: unika rubriktexter eller stegtiteln kvalificerad av index i tillgängligt namn | Rubriknavigering hör samma etikett två gånger | 2.4.6 | Karin, SEO |
| LOW | `index.html:937` (`alt` på `#heroPoolImg`) | Alt beskriver utseendet; bilden är dekor i sitt sammanhang | Mål: `alt=""` | Alt ska svara på vad som går förlorat | 1.1.1 | Karin, SEO |

**Barriärmatris.** T1 förstå vad Alunix gör och se kortet vändas, T2 läsa de sju processtegen, T3 hitta priset, T4 nå kontaktvägen.

| Persona | Villkor | Teknik | T1 | T2 | T3 | T4 |
|---|---|---|---|---|---|---|
| Karin, blind | permanent | NVDA, Firefox, bläddringsläge | friction (F-07) | works | works | works |
| Tomas, gipsad handled | temporär | tangentbord, PageDown | works | **fails** (F-03) | works | friction (F-04) |
| Elin, svag syn | permanent | ZoomText 400 %, 1366x640 | works | friction (F-08, F-01) | works | friction (F-02, F-04) |
| Marcus, situationell | situationell | iPhone 390, sol, en hand | works | works | works | friction (F-06, F-01) |
| Sofia, dyslexi | permanent | text-till-tal på markering | works | **fails** (F-05) | works | works |
| Jonas, switch | permanent | två-switch scanning | friction | **fails** (F-03) | works | workaround |

**Legal map.** WCAG 2.2 AA ej konform: 1.4.3 (F-01) och 1.4.11 (F-02), därtill 2.1.1/1.4.13, 1.3.2, 2.4.3, 2.5.8, 1.3.1, 1.4.10, 2.4.6, 1.1.1. EAA / EN 301 549 i kraft sedan juni 2025; de två HIGH-fynden är den sortens brist ett tillsynsärende börjar i. ADA och Section 508 ej i scope.

**SEO-relevanta fynd.** Dubblerade h3-etiketter; hero-bildens alt. Reflow rent vid 320 och 200 % zoom, `lang="sv"`, självständiga länktexter.

**Vad som håller:** 0 axe-violations mot V3b:s fyra `no_focus_indicator` plus `order_mismatch`; iframes `title` + `inert` + `pointer-events:none`; SVG `role="img"` med `title`/`desc`; ordscrubben additiv med golv 6,3:1; fokusringen en valör per grund; banner/main/contentinfo; rubrikdjup h3; 1.4.12 spräcker ingenting.

## ceiling

- **V3b-chain** (körd med samma skript): **slår**. V3b ger fyra `no_focus_indicator` och ett `order_mismatch`, V3c 0 issues. V3b:s iframes är fokuserbara, V3c tar bort möjligheten för alla; rätt val här, men ett bortval.
- **oryzo-ai** (`fold.webp`): **slår**. Vit-på-mellanton över foto i hela folden. Oryzo gör bättre: sektionsnav som svarar på "vart kan jag gå".
- **mattis-studio**: **slår**. Grått-på-grått som betydelsebärare. Mattis gör bättre: synlig primär knapp med riktig träffyta.
- **insign**: **står sig bredvid**. 21:1 på rubriken, nav, till-toppen. Tillgänglighetswidgeten är inget att låna.
- **highwaymedia**: **förlorar**. Brödsmulor, 44 px knappar, telefonnumret som kontroll. V3c har ingen väg tillbaka i en 8 126 px lång sida och en 23 px CTA.
- **hoy**: **står sig bredvid**. Invert-kontroll i toppen, men gräddvit på rött runt 3,3:1.

## material_fixes

1. `index.html:580-581` `.frame-cap`: bildtexten på en yta med känd valör eller en valör per grund. Mål: **>= 4,5:1 mot de ljusaste 5 % av underlaget vid varje scrolldjup mellan p 0,2 och 0,9**; i dag 3,06:1 med 50,1 % av ytan underkänd vid scrollY 4000.
2. `index.html:445` `.card-cta`: `text-decoration-color` till `currentColor` (17,5:1) eller ljusheten lyft till cirka `#3f84c9`. Mål: **>= 3:1 mot `#0b0c0e`**, i dag 2,92:1.
3. `index.html:712-718` + `:683`: stegtexterna slutar vara scrollgrindade på desktop (som mobilregeln `:841`), arket behåller sin ritning. Mål: **varje `<li>` >= 0,99 opacitet i >= 800 px scroll vid 1440x900**, PageDown ger 7 av 7 (i dag 4 av 7).
4. `index.html:1271-1277` `setFace`: flytta fokus innan ytan inerteras, `figure.hero-plate` med `tabindex="-1"`. Mål: **`document.activeElement` blir aldrig `body` av en scroll**.
5. `index.html:697` `.process-steps li`: `pointer-events:none` som grundläge, `li[data-active]{pointer-events:auto}` satt av den befintliga `scrollY`-loopen. Mål: **`elementFromPoint` och `caretRangeFromPoint` returnerar det synliga steget vid varje `--sc-ps`**.
6. `index.html:443-446` `.card-cta`: träffytan förlängs utan att flytta baslinjen. Mål: **>= 24x24 px golv och 44 px höjd**, i dag 104x23 px vid 390 och 320.
7. `index.html:940-948` + `:1276`: `aria-hidden` bort från `.face--back`, `inert` behålls. Mål: **kortbaksidans fyra strängar i tillgänglighetsträdet vid `--sc-ps` = 0**.
8. `index.html:691-693` `.process-stage`: `height: min(495px, 100svh - 220px)` med proportionell viewBox. Mål: **hela arket innanför vikningen vid 1366x640**.

Kvar som namngiven skuld till `.impeccable/a11y-debt.md` med Antons medgivande: dubblerade h3-etiketter (2.4.6, LOW, 90 dagar); hero-bildens alt (1.1.1, LOW, 90 dagar); DOM-ordningen i tvåspaltsläget plus den obyggda mobilordningen Q28 / plan 012 (1.3.2, LOW, 30 dagar); forced-colors och Firefox/Safari-verifiering av `inert` på iframe (30 dagar); testning med verkliga användare.

## keep

Båda iframes `inert` **plus** `pointer-events:none`; ordscrubbens additiva ton med golv 6,3:1; `<ol>` med `<li>` och h3 per steg med all text i DOM oavsett opacitet (räddar skärmläsarparitet när fix 3 ändrar visningen); `role="img"` med `title` och `desc` på arket; fokusringens två valörer; rubrikdjupet vid h3.

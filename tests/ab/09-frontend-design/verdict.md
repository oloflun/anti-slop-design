# AB09 — frontend-design (Anthropic-skillen) injicerad eller inte

Brief 07 (Florhuset Majorna, Tier 3). A = Skill(design) + house-physics + gates + ett registerexempel; B = samma + frontend-design/SKILL.md först (designplan, generic-default-review).

| Mått | A | B | Not |
|---|---|---|---|
| Register / lane | editorial print, "salt-bleached harbour atelier", cream + koppar | editorial print, "saltblekt verkstadsflorist", kall dimma + petrol + tegel | B bryter cream-defaulten (look #1) — precis den effekt frontend-designs kalibreringslista förutspådde |
| Sektionsanatomier | 8 (hero, ledger, set-piece, diptyk, centrerad, rail, inversion, kolofon) | 5 | |
| Helsida utan scroll | allt synligt | tom efter heron | B: reveal med threshold 0.1, ingen failsafe, ingen mount-reveal → bryter exit-baren "fails toward visible" |
| Skivor med scroll | komplett | komplett (fasad-tuschlinje som grid-break, bröllop på petrol) | innehållet finns, men beror på JS-scroll |
| hairlineRules / distinctBackgrounds / images | 14 / 4 / 3 | 13 / 2 / 4 | |
| Typsnitt | Fraunces + IBM Plex Mono | Piazzolla + Fragment Mono (bytte efter detektorträff) | B reagerade på overused-font-detektorn |

Visuellt (compare/fold.png, full.png, B s02 lästa): A är den rikare och mer färdiga sidan, men den ser ut som Calyx-familjen (cream, rost, serif-italic) — bra utförd default. B har den mer distinkta världen (petrol/fog, tegel bara i display) och ett riktigt grid-break-moment, men skeppar en reveal som gömmer sidan utan scroll och har färre anatomier.

**Beslut: INTE som skill, MEN två regler portas.** Som laddad skill blev den ett tredje direction-huvud och bygget tappade en exit-bar-regel. Det den tillför är verkligt och syns på pixlar: registervalet sammanföll med en AI-default-look och B skilde sig då på palett-temperatur + typparning (2 av 3 axlar). Porta in i craft floor: (1) "sammanfaller registret med en AI-default-look (cream+serif+terracotta / near-black+acid / broadsheet hairlines) måste bygget skilja sig på ≥2 av {palett-temperatur, typparning, grammatik}"; (2) generic-default-självtestet i pre-emit-kritiken. Pluginet frontend-design stängs av lokalt (konkurrerar om auto-invocation). Skärpning från fyndet: reveal-guarden (threshold 0, mount-reveal, failsafe, noscript) flyttas från exit-baren till Step 4 "binding while building".

# Design rework v3 — genomförandeplan (projektkopia)

Fullständig plan: `~/.claude/plans/uppgift-design-rework-v3-validated-hammock.md`. Bevis: `tests/ab/*/verdict.md`, loggboken "Design Rework v3" (artifact).

## Scope
- Hookar tysta utanför designjobb, a11y-audit, reference lock, designkatalog, Step 2b (grammatik + bake-off), visuell kritik, emil-uppdatering, frontend-design-analys, SlopMonster-hybrid; A/B-test per tillägg och kumulativt.

## Completed
- [x] 01 kanonisk kopia + spegel (beslut 2A)
- [x] 02 hook-klassificerare, arm/disarm, unloaded strong routes (137/139)
- [x] 03 emil-skills (AB08: in)
- [x] 04 reference lock (AB05: in, modifierad)
- [x] 05 a11y-audit + tre granskaragenter (AB02, AB04: in)
- [x] 06 visual critique + review-orkestrator (AB03: in)
- [x] 07 scroll-craft (AB06: in, motorn opt-in)
- [x] 08 bake-off-board (AB07: in)
- [x] 09 designkatalog på localhost (AB10: in)
- [x] 10 frontend-design (ute som skill, två regler portade)
- [x] K kumulativt test (kedjan intakt och bättre)
- [x] 11 SlopMonster (hybrid)
- [x] 12 runda 2: sju spakar testade (fem ute, worlds in, loop nödvändig men inte svaret)
- [x] 13 breddkontrakt (fyra byggen, in som default i Step 2b)
- [x] 14–15 två fristående copy-exempel, gamla kedjan vs. hybridkedjan (Kajplats + Reglabok) — B vinner tydligt på båda (reviderat efter Antons läsning); ny strukturregel i copy-gate.md (diskreta fakta som egna fetstilsrader, en process återberättad som en mening)

- [x] 16 katalogen in i repot (95 poster, extract, /catalogue på Vercel) — 2026-09-04
- [x] 17 TASTE.md ur 89 källor — 2026-09-04
- [x] 18 sex Alunix-koncept (runda 1, underkänd: enmansröst, svag balans)
- [x] 19 sex byråkoncept (runda 2, board 127.0.0.1:4621) — väntar på Antons val
- [x] 20 plugin-avknoppning (anti-slop-design eget plugin, super-intelligence 0.10.0) — opushat

- [x] 21 r3: Antons val, R5 + R6 kombinerade till en sida (`tests/alunix-concepts-r3/`), sex agentrundor efter pixelläsning, kedjan bevisad via ledger-räknare — 2026-09-04

- [x] 22 r4: tre remixer av r3 (M1 kontinuerlig grund, M2 kapitel med pinnad scen, M3 galleri med rail), board 127.0.0.1:4622 — 2026-09-04

- [x] 23 r5: M1 vald; tre varianter (V1 dokumentärt band, V2 cinematisk tvätt, V3 plåt i grunden) med hero-bild, fylld lucka, Exempelsida-etiketter, nya paket 26 900/38 900; board 127.0.0.1:4623; board.py serverar repo-rot som fallback — 2026-09-04/05

- [x] 24 V3 vald; V3b polerad (Hōrai-källan, etiketter bort, hero i folden, bleed synlig, kritikerfynd), board 4623 riktning 1 = V3, 2 = V3b — 2026-09-05

- [x] 25 r6: isolerat A/B-test, Claude-native (Anthropics frontend-design som systemprompt, inga skills, inga hookar) mot kedjan (repots hookar via plugin-skal + live-skillen), tre nya koncept (K1 Skymning / K2 Affischen / K3 Konsolen) ur katalogen, en fryst prompt, sju headless Fable-high-processer, bevakning per cell, blind board 127.0.0.1:4624. Unsplash-API-vägen i `unsplash_sheet.py` + `scripts/keys.py` (nyckel i `~/.secrets/.env`, demo-läge 50/h). Kedjefynd: `NEGATIVE_GUARD` tystade gaten på ordet `commit` (fixad, korpus 42/42); skillen laddades men inga referenser lästes och inga procedurskills kördes. `tests/alunix-ab-r6/verdict.md` — 2026-09-05/06

- [ ] 26 r7 (pågår): Antons r6-dom → `design-catalogue/FEEDBACK.md` (F-001–F-009, feedbacksystemet), referensgolv i hookarna (`ref-read`, gate nekar UI-skrivning innan TASTE/FEEDBACK/lock/katalog/scroll-refs), scroll-route + scroll-gap + rm-bild i stop, SKILL.md Step 1b/2b/Motion/Step 5, TASTE § 4.8, house-physics, skill-orchestration § 12, `scripts/serve.py`, boardens reduced-motion-varning; K1 + K2 om igen med Sonnet i rundor (`tests/alunix-ab-r7/`), Higgsfield/Kling-push-in för K1 (tak 35 cr), board 4625 — 2026-09-06

## In Progress
- [ ] r7: båda cellerna i slutläge (sex rundor + kritikertrion, verifierade av Claude), RAPPORT.md komplett, board 4625 uppdaterad. Kvar: hans beslut om Kling-omtagning (17,5 cr) och K2:s driftkontrast (lättare slutton eller sjätte kulör).
- [x] 2026-09-07: motion-always-regeln (F-011) — `prefers-reduced-motion` borttagen ur scrollcraft.js/.css och K1/K2, `a11y-audit` uppdaterad globalt, `board.py` HTTP/1.1+webp-mime-fix (samma bugg som `serve.py` löste, aldrig portad till boarden). Verifierat i en riktig reduced-motion-webbläsare.
- [x] 2026-09-07: kedjerevision av r7-byggena — `tests/alunix-ab-r7/CHAIN-AUDIT-2026-09-07.md`. Fynd: Stop-hookens sessionsscoping trasig (blandar sessioner när miljövariabeln saknas i hook-processen — förslag: läs `session_id` ur event-payloaden, ej gjort än); `imagegen-frontend-web` triggar för brett (vilken `<img>` som helst); `"impeccable layout"` är fel skillnamn (riktiga namnet är `impeccable`) plus oklart om `impeccable` ens är laddningsbart för byggarna; `Skill(design-catalog)` kallades aldrig i något av K1/K2 — orkestrerarens egen runda-1-prompt gav filvägar direkt i stället för att köra skillets `query.py`-urval.
- [ ] **Öppet för nästa session (Antons uttryckliga överlämning 2026-09-07):** rörelsen spelar nu upp korrekt (F-011) men "ser hackigt och billigt gjort ut" — orsak inte fastställd, se FEEDBACK.md F-012. Nästa agent: fastställ vilken cell/akt, mät (frame-times i push-sekvensen, `--sc-p`-kontinuitet, om något smoothing-villkor rört sig av `reduce=false`-patchningen), skriv den härledda regeln som ny FEEDBACK-post.
- [x] Antons omdöme på r6-boarden (port 4624): underkänt, se FEEDBACK.md. Mappning: körning 1 = kedjan, körning 2 = Claude-native.
- [ ] Antons jämförelse V3 mot V3b (board port 4623).

## Remaining
- [x] Unsplash API-nyckel på plats 2026-09-05 (`~/.secrets/.env`, `scripts/keys.py`), `unsplash_sheet.py --api/--download/--verify`, photo-sources.md uppdaterad. Kvar: produktionsansökan hos Unsplash (50 → 5 000 anrop/h), Antons sak.
- [ ] r6-fynd att ta vidare: kedjan laddar `design` men läser inga referenser och kör inga procedurskills på Fable high headless; `python -m http.server` tappar WebP-svar mot Chromium (alla sex agenter skrev egna servrar); `references/upstream/anthropic/frontend-design/SKILL.md` skiljer sig från den installerade pluginens version.
- [ ] Liten kvarstående nyans från Reglabok-testet: B:s hero klämde in en kundsiffra i samma mening som mekaniken i stället för att leda med en bild — inte tillräckligt för en ny regel, men värt att hålla ögonen på i nästa Tier 2/3-bygge med statistik i heron.
- [ ] Pusha `super-intelligence` (gren design-system-v2) och uppdatera plugin-cachen — Antons go-ahead.
- [ ] Merge/push `anti-slop-design` gren `design-rework-v3` — Antons beslut.
- [ ] Logga v3-besluten i CARL DESIGN-domänen.

## Deferred
- Katalogen till Vercel + GitHub OAuth (planens 8b); Refero MCP; kie.ai-video; obligatorisk rival-cleanse.

## Blockers
- Inga tekniska; push kräver Antons instruktion.

## Next Steps
- En skarp designsession som kör bake-off + Step 5-looparna på ett riktigt kundprojekt och mäter route gap = 0 med de nya hookarna.

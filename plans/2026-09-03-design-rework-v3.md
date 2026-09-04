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

## In Progress
- [ ] Antons val bland V1–V3 (board port 4623); M1-boarden kvar på 4622.

## Remaining
- [ ] Unsplash API-nyckel (Antons handpåläggning) → photo-sources.md får riktig sökning; fotopoolen är 19 bilder i dag.
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

# Alunix V3f och integrationen i designsystemet
### 2026-10-01 (uppdaterad 2026-10-05)
Planen följer arbetet med V3f/V3g, integrationen av Inspo-MCP, UI-skills och GSAP+Lenis i designsystemet, och nu publiceringen av Alunix.

## Scope
- Bygget av V3f och showcasen i V3g (R8 till R10).
- Integrationen enligt `tests/alunix-r8/HANDOFF-V3f.md` § 6.
- Publicering av godkänd flik på alunix.se.

## Completed
- [x] V3f byggt över sex rundor med leadens pixelgranskning mellan varje.
- [x] Lenis-skill skriven ur primärkällor (`~/.agents/skills/lenis/`).
- [x] Handoff med process, fel och integrationsplan.
- [x] V3g R8/R8b: copy i två stycken, rutor bort, lupp som band.
- [x] F-023 till F-028 införda i FEEDBACK.md.
- [x] Integrationsstegen 1 till 7 (se `HANDOFF-2026-10-03.md`), plus golvet: designkedjan kräver showcase-golvet, motion sheets och GSAP/Lenis-skills före första UI-skrivning (plugin 1.2.2).
- [x] R9 och R10. R10 delad: flik 7 bara beställt, flik 9 egna idéer.
- [x] Flik 8 "Markören", nytt koncept genom kedjan.
- [x] Flik 7 live på alunix.se och www.alunix.se (2026-10-04/05), showcase-bilderna borttagna.
- [x] Skill `loopia-vercel-domain` för domänflödet.
- [x] Boarden öppnar sig själv i preview-panelen.

## In Progress
- [ ] Anton bedömer flik 8 och flik 9.

## Remaining
- [ ] Vercel-projektet `alunix` är Git-länkat till `alunix-site`; Anton avgör om länken ska bort.
- [ ] Integrationssteg 8: A/B-körning med kedjan på.
- [ ] R7b-klickregressionen i V3g (kontrollera om den finns kvar i R10).

## Deferred
- Push av `design-rework-v3` och super-intelligence (kräver Antons klartecken).
- Fingeravtrycksrad för V4 i valvet (efter Antons godkännande).

## Blockers
- Inga tekniska. Besluten ovan ligger hos Anton.

## Next Steps
- Antons beslut om Git-länken och flik 8/9; därefter push på klartecken. Se `HANDOFF-2026-10-05-ALUNIX-LIVE.md`.

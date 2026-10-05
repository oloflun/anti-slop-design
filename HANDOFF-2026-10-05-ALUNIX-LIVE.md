# Handoff 2026-10-05: Alunix tab 7 live on alunix.se, board fixed, Loopia domain skill

Written for an agent that has never seen this project. Read this first, then
`HANDOFF-2026-10-03.md` (R9/R10 detail) and `tests/alunix-r8/HANDOFF-V3f.md`.

## 1. Current state, verified 2026-10-05

| What | State | Checked how |
|---|---|---|
| Main repo `anti-slop-design` | branch `design-rework-v3`, last commit `8ebf1bf`; **not pushed** (commits `0199866`..`8ebf1bf`, 7 of them, plus older ones) | `git log` |
| Deploy repo `deploy/alunix-v3g/` | own git repo, private GitHub `oloflun/alunix-v3g`, branch `main`, `3419c3c` **pushed**; untracked in the main repo | `git -C deploy/alunix-v3g log` |
| Production | Vercel project `alunix` (team `team_xLbo3OZ554hw3HEJBC7F5Dui`), deployment `dpl_AqhSUxHimLiCNDJPCP2FCMAwjaE4` from `alunix-v3g@3419c3c` | live HTML md5 == `deploy/alunix-v3g/index.html` |
| Domains | `https://www.alunix.se` 200 (production), `https://alunix.se` 308 -> www, both valid TLS; `alunix-three.vercel.app` also serves it | `curl -sL` |
| DNS at Loopia | `@ A 216.198.79.1`, `www CNAME 645a93e3832fd0c2.vercel-dns-017.com`, NS ns1/ns2.loopia.se, TTL 600; parking records gone; no MX/TXT existed | `loopia_dns.py alunix.se --check` (all four resolvers agree) |
| Board | `python board.py tests/alunix-r8/board --port 4626 --fallback-root . --single` (launch.json `alunix-board-r8`); `/` now redirects to `/board.html`; tabs 2, 6, 7, 8, 9 | preview pane, title "Alunix r10 · 2, 6, 7, 8, 9" |
| super-intelligence | `design-system-v2`, `94edb25` (0.11.2, new skill) **not pushed** | `git log` |
| Plugin dist | `dist/plugin/skills/design/scripts/board.py` synced (dist/ is gitignored, rebuilt by the plugin build) | grep |

Board tabs: 2 V3d (inverted), 6 V3f (Rutverket), **7 V3g R10 ordered = live**, 8 V4 "Markören" (new
concept), 9 V3h R10 creative. Tab 7's cell is a junction to `tests/alunix-r8/runs/V3g/`.

## 2. What was built (since the 2026-10-03 handoff)

1. **R10, split in two tabs** (Anton: R10 changed more than ordered). Tab 7 = only the ordered
   items on top of R9: topline anchors (Process/Exempel/Paket/Kontakt, hidden < 768), "Vår process:"
   kicker removed, the cost line, a11y L2/M1, and a new tes hand-over played by time, not scrubbed
   (A's words leave, B uses A's own char entrance; past progress .45 plays, back reverses at 1.4x).
   Tab 9 = builder's creative extras, with approved copy restored ("Boka ett möte", "Så berättar vi
   vad vi kan göra för er."), thumbnails and the "Från samtal" image removed, smoother mint
   transitions (dome clip, rounded contraction). Commit `bdcbd94`.
2. **Design chain** now requires the showcase floor, `journeys/era-residence.md`, two motion sheets
   at `motion_floor: 2`, and Skill(lenis)/(gsap-core)/(gsap-scrolltrigger) before the first UI write
   on scroll work. `verify-design-system.py` 212/212. Plugin 1.2.2. Commit `bdcbd94`.
3. **Tab 8, V4 "Markören"**, new concept built by a headless Opus 5.5 builder ($28.02, modelUsage
   Opus only), section probe 0 fails. Approved by the lead at 1440/768/390. Commit `d4b41df`.
4. **Tab 7 deployed** to Vercel (static override, `vercel.json` framework null) and **put on
   alunix.se**: domains added in the Vercel dashboard (Anton logged in in the pane; MCP token gets
   403 on project domains), DNS set via LoopiaAPI with the Snajp keys (`snipe-leads/.env.deploy`,
   value never seen). Waited out Loopia ns1 lag (~1 h) and Vercel's certificate retry.
   Verified: byte-identical HTML, headless 1440 + 390, 0 console errors, 35/35 images.
5. **Board fix**: preview pane opened `/` = directory listing. `board.py` now 302s `/` ->
   `/board.html` (live skill + repo copy + dist). Commit `6c75596`.
6. **Showcase step images removed** under the descriptions (both Calyx and Hōrai `.showcase-detail`
   blocks + their CSS; JS was already null-safe). Anton thought they were gone because the band hides
   itself under 160 px height, which it was on the board. Tab 7 source + deploy, pushed and deployed.
   Commits `8ebf1bf` (main), `3419c3c` (deploy).
7. **New skill `loopia-vercel-domain`** (`~/.agents/skills/loopia-vercel-domain/`, synced to
   super-intelligence `94edb25`): SKILL.md with the whole flow and pitfalls, `scripts/loopia_dns.py`
   (dry run default, `--apply`, `--check`). Tested against alunix.se: idempotent no-op.

## 3. What remains, in priority order

1. **The Vercel project `alunix` is still Git-linked to the Next.js repo `alunix-site`.** A push
   there redeploys production over the static tab 7. Owner: Anton decides (unlink in Project
   Settings -> Git, or keep and never push alunix-site main). Agent can do it in the dashboard if asked.
2. **Push** the main repo (`design-rework-v3`) and super-intelligence (`design-system-v2`). Waits
   on Anton's explicit go-ahead, every time.
3. **Anton's verdict on tabs 8 and 9.** Tab 8 is approved by the lead, not by Anton. Tab 9 holds
   the creative R10 extras; nothing from it goes into tab 7 unless he orders it (F-028).
4. Optional, only after Anton approves: fingerprint registry row for V4 in the vault.
5. The design report flagged 8 "broken-image" and 1 em-dash finding without file paths; none are in
   tab 7 (checked). If someone wants them traced, the detector needs to print paths.
6. `memory/BLOCKS.md` in the vault is ~28 700 chars against a 3 000 cap; resolved blocks need to
   move to `BLOCKS-RESOLVED.md` (not done this session).

## 4. Traps

- **Opening `deploy/alunix-v3g` as cwd** made the design hook link gsap/lenis into it (package.json,
  `node_modules` junctions, gsap.js, smooth-scroll.js). Removed with `rmdir` on the junctions;
  `rm -rf` through a junction deletes the global npm install. Check `git status` there before committing.
- **Loopia ns1 lags ns2 by up to an hour.** Vercel verified the apex against ns1, so the apex sat
  in "Invalid Configuration" with `SEC_E_WRONG_PRINCIPAL`; it fixed itself. Don't change records while waiting.
- **Vercel MCP 403** on `add_project_domain`/`assign_alias`/create project: use the dashboard.
- `create_deployment` from `oloflun/alunix-v3g@main` needs `projectSettings` framework null,
  empty build/install, output `.`, plus `skipAutoDetectionConfirmation: 1`.
- `find .` from the repo root hangs past 2 minutes (huge tree); use Glob.
- Copy rule F-028: never rewrite approved copy; ordered work and own initiative go in separate tabs.

## 5. Anton's instructions, verbatim

- "Kör nästa runda enligt § 4, jag godkänner planen. Updatera först boarden, ta bort nuvarande 1, 3, 4 & 5. Behåll nuvarande 6 som den är och lägg till en ny 7 med ändringarna i nästa runda, sedan vill jag att du skapar 8, ett helt nytt koncept för sidan som tar inspiration från helt nya källor och implementerar de nya designmekanismerna från Gsap och Lenis, eller rättare sagt, se till att designkedjan är updaterad med detta och kallar dem, annars se till att det görs först och bevaka sedan alla skill-calls."
- "Den R10 som visas är fortfarande oförändrad mot tidigare, trots att jag sett ändringarna för bland annat \"Vi hjälper er att synas\" i skärmdumparna från förra rundan."
- "R10 gjorde mer ändringar än jag beställde- Dela upp dem i 2 olika flikar- en med enbart vad jag beställde och en med dina kreativa ändringar, men just nu ser det inte bra ut, den klippta rubriken högst upp och de små bilderna för att byta mellan Horai och Calyx samt den lilla bilden vid \"Från samtal\"? och övergångarna till grönt som blir väldigt kantiga. Övergången till \"Vi hjälper er att synas\" har varit väldigt ryckig i alla versioner jag sett, se till att den blir mjukare och matchar hur den första texten dyker upp. Bekräfta att du förstått vad jag syftar på"
- "\"Berätta om er verksamhet. Så berättar vi vad vi kan göra för er och föreslår en tid för ett första samtal.\" blir för långt, det var bättre innan. Samma sak med \"Mejla oss för att boka ett möte\" i stället för \"Boka ett möte\" Ändra inget om jag inte bett om det, copy-gaten ska inte omarbeta redan godkänd copy, endast skapa ny där det inte finns eller förbättra om det beställs av användaren"
- "Fortsätt bygga på de andra men pusha flik 7 till Vercel och använd mina Loopia- nycklar för att lägga den på Alunix.se. Jag behöver att du löser detta, har ett kundmöte om 45 min"
- "Konfigurera domäninställningarna i Vercel åt mig, du har tillåtelse"
- "Please restart the devserver and fix the board, it's not loading despite restarting the server from the app, I've also logged in so that you can complete the domain configuration"
- "Du har nycklarna för att göra allt på Loopia, Sebbe har kunnat göra det för Snajp med nyckel utan min inloggning, så det är möjligt, gör vad som krävs."
- "Perfekt, skapa en skill för detta. En sak till: Ta även bort alla bilderna under beskrivningarna för showcasen på live-sidan, de syntes inte längre i boarden  så jag trodde de var borta, vilket var vad jag ville. Gör det och kör sedan /conclude"
- Standing goal: "Fortsätt tills ALLT är klart, verifierat och godkänt mot pixlar enligt det nya golvet som vi satt nu."

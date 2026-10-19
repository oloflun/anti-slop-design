# Alunix r9, runda 6. Cell {{KONCEPT}}. Fixrunda efter R5-granskningen: processakten får sin riktiga text och form.

Samma session, samma cell. R5 byggde processakten (plan 010) och kortvändningens tempo
(plan 011). Fem granskare (craft, heuristik, a11y, perf, codex/Astra med bilder) och leadens
F-007 gav `fix`. Anton såg R5 och dömde att stegen inte får vara fråga och svar utan riktiga
beskrivningar, som referenserna. Den här rundan utför arkitektens fixplaner i
`{{UT_MAPP}}/plans/README.md` § R6, i README:s ordning. Ut-mapp `{{UT_MAPP}}`, port {{PORT}}.

## 0. Läs först

1. `{{UT_MAPP}}/plans/README.md` § R6: vilka planer, i vilken ordning, och beroenden.
2. Varje R6-plan i sin helhet (Problem / Target / Conventions / Steps / Boundaries /
   Verification). Planerna bär radhänvisningar mot R5-filen; hitta varje ankare med `Grep`
   innan du redigerar och STOPPA (skriv i NOTES § R6) om koden inte matchar i sak.
3. `{{UT_MAPP}}/PROCESS-UNDERLAG.md` § 3 (copy v1, ordagrant) och § 4 (antagandena gäller;
   rader märkta [A] skrivs enligt antagandet i tabellen).
4. `{{UT_MAPP}}/HELHET.md` § 3 H-21 till H-35, `{{UT_MAPP}}/reviews/r5/` (fem rapporter; läs
   `material_fixes` och `keep` i var och en: `keep` är det du inte får riva).
5. `Skill(design)` (verbet build, komponentskop), `Skill(animate)` och `Skill(emil-design-eng)`
   före ändringar i rörelse, `Skill(a11y-audit)` före a11y-planerna. Via `Skill`-verktyget,
   namngivna i transkriptet.

## 1. Utför

Planerna i README-ordning, Verification per plan innan nästa öppnas, utfall i transkriptet
och i NOTES § R6: `verified`, `best-effort` (med vad som återstår) eller `reverted` (orsak).
Aldrig `verified` på känsla. Kirurgiska `Edit`-anrop, aldrig `Write` av hela filen, aldrig
shell-skrivningar mot UI-filer. Motorn `scroll/*.js` och `sites/*` rörs aldrig. Rör aldrig
det som står i rapporternas `keep`: `--sc-ps`-kontraktet (staircase 0), `will-change` bara
via klass, sticky som enda höjdmekanism, `pathLength="1"` med `*1px`, `@property`-raderna,
iframes `inert` + `pointer-events:none`, `<ol>` med text i DOM oavsett opacitet.

Copy v1 skrivs in ordagrant ur underlaget § 3 (stegtitlar, stycken, marginalrader,
principer, liggarrader), märkt `<!-- copy v1, copy-gate i R7 -->`. Låst copy (femton
strängar) rörs aldrig. Noll tankstreck. Inga tal utöver ritningens mått och de låsta priserna.
`7 rem`-måttet rättas som planen anger (linjen ska visa det utropet säger).

## 2. Grinden efter sista planen, i din session

Servern `python ~/.claude/skills/design/scripts/serve.py --port {{PORT}} --root .`.
Kontrollprotokollet gäller (`tests/motion/smooth.html` först, ren kontroll omedelbart före
varje sidmätning).

1. `motion_probe.py --cpu 4`, spår `section.hero:--sc-ps,.plate-card:transform` och
   `#process:--sc-ps,#p-outline:stroke-dashoffset,#p-opening:stroke-dashoffset`, `--wheel 100:60`
   och `--wheel 20:120`; också `--cpu 1`. Skriv kontroll och sida sida vid sida. Bar: staircase 0,
   p95 ≤ 20 ms, 0 rutor > 33 ms, `--sc-ps` max_step ≤ 3 %; faller bildtiden ändå, skriv talen
   före och efter perf-planerna, inte bara efter.
2. `scroll_verify.py` vid 1440x900 och 390x844 (`--out {{UT_MAPP}}/shots/r6`): H-16, H-17, H-18.
3. `perf_probe.py --cpu 4` vid 1440 och 390: `long-task-under-scroll` 0, CLS ≤ 0,05, sidans egen vikt.
4. `preflight_taste.py`, `detect.mjs --json`, `contrast_over_media.py --url` (bildtexterna under
   ramarna, papperet under arket, kortbaksidan), `a11y_scan.py`, `tab_walk.py`, `reflow.py`,
   plus 900x600, 1024x640, 1180x740, 1280x800, 1366x640 (arkets klippning och vikning).
5. Grep: `prefers-reduced-motion` 0, U+2013/U+2014 0 i synlig text, inga nya inline-hex.
6. Skärmbilder: `?preview=process-01…07` vid 1440 och 390, tolv ramar genom akten vid 1440
   och vid 390, heron `--flip` 0/0,25/0,5/0,75/1, hela sidan i skivor vid 1440 och 390,
   fold vid 320/375/414/768/1024/1280. Allt i `{{UT_MAPP}}/shots/r6/`. Läs varje bild,
   `läst: <fil>` i NOTES, F-007 bild för bild mot planens målbildstabell.
7. PageDown-vandringen ur a11y fix 3: sju av sju steg ska renderas; skriv utfallet.

## 3. Invarianter

F-011, F-014, gate 47/79/75/88, `PRODUCT.md` § absences, `@property` för varje `--p-*`,
en höjdmekanism, ingen tredje iframe, ingen generering. Fullständig output; `[PAUSED — plan X]`
som sista rad om du måste pausa.

## 4. Leverans

`{{UT_MAPP}}/index.html`, `{{UT_MAPP}}/shots/r6/`, `{{UT_MAPP}}/NOTES.md` § R6 (en rad per plan
med dom, grinden med kontroll- och sidtal, F-007-tabellen, PageDown-utfallet, låst copy 15/15,
avvikelser med skäl), `{{UT_MAPP}}/BRIEF.md` § decision ledger (raderna planerna anger).
Sista raden i sista meddelandet: `R6 klar` eller `[PAUSED — plan X]`.

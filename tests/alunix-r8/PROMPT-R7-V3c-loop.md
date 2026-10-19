# Alunix r9, runda 7. Cell {{KONCEPT}}. Helhetsloopen, runda 1: åtta fixplaner mot golvet i HELHET.md.

Samma session, samma cell. R6 godkändes som fixrunda; helhetsloopen (fas C) startade med
arkitektens runda 1 (`{{UT_MAPP}}/NOTES.md` § Loop 1, `reviews/loop-1-astra.md`). Den här
rundan utför arkitektens åtta fixplaner i `{{UT_MAPP}}/plans/README.md` § R7, i README:s
ordning. Ut-mapp `{{UT_MAPP}}`, port {{PORT}}.

## 0. Läs först

1. `{{UT_MAPP}}/plans/README.md` § R7: vilka planer, i vilken ordning, och beroenden
   (025 först: den rättar ett layoutfel och stegens fönster; 017 före 012: samma
   mediablock; 015 delar `.close` med plan 007, som redan byggt `min-height:62svh`).
2. Varje R7-plan i sin helhet (Problem / Target / Conventions / Steps / Boundaries /
   Verification): 025, 017, 012, 013, 014, 015, 016, 026. Planerna bär radhänvisningar mot
   R6-filen (md5 `424cdd46`); hitta varje ankare med `Grep` innan du redigerar och STOPPA
   (skriv i NOTES § R7) om koden inte matchar i sak.
3. `{{UT_MAPP}}/HELHET.md` § 3 (golvet H-01 till H-35, med arkitektens bockar från loop 1)
   och § 4 (tilläggen T-1 till T-8: varje ny färg eller element har token och H-rad där).
4. `{{UT_MAPP}}/reviews/loop-1-astra.md` och `{{UT_MAPP}}/reviews/r5/` (sex rapporter; läs
   `keep` i var och en: `keep` är det du inte får riva).
5. `{{UT_MAPP}}/PROCESS-UNDERLAG.md` § 3: stegens copy v1 är låst för dig; copy-gaten körs
   av en copy-agent efter loopen. Rör inga strängar.
6. `Skill(design)` (verbet build, komponentskop), `Skill(animate)` och `Skill(emil-design-eng)`
   före ändringar i rörelse (015, 017 A och D, 025 B), `Skill(a11y-audit)` före 012, 015 och 016.
   Via `Skill`-verktyget, namngivna i transkriptet.

## 1. Utför

Planerna i README-ordning, Verification per plan innan nästa öppnas, utfall i transkriptet
och i NOTES § R7: `verified`, `best-effort` (med vad som återstår) eller `reverted` (orsak).
Aldrig `verified` på känsla. Kirurgiska `Edit`-anrop, aldrig `Write` av hela filen, aldrig
shell-skrivningar mot UI-filer. Motorn `scroll/*.js` och `sites/*` rörs aldrig. Rör aldrig
det som står i rapporternas `keep`: `--sc-ps`-kontraktet (staircase 0), `will-change` bara
via klass, sticky som enda höjdmekanism i processakten, `pathLength="1"` med `*1px`,
`@property`-raderna, iframes `inert` + `pointer-events:none`, `<ol>` med text i DOM oavsett
opacitet, ramarnas viloläge (`content-visibility:hidden` via `.is-asleep`), `.ground`s
`contain:strict`.

Varje plan har mätbara mål (tal eller bild). Mät före och efter där planen säger det, och
skriv båda talen. Faller ett STOPPA-villkor: stanna i den planen, skriv talen, gå vidare
till nästa plan bara om planen uttryckligen tillåter det.

Tillägg och färger: bara de som står i HELHET.md § 4 med token och ledgerrad
(`--c-graphite` i 013, `--panel-pad-y` på `.principles` i 025). Ingen inline-hex (gate 48),
inga värden ur demoterade skills (gate 60). Låst copy (femton strängar) rörs aldrig. Noll
tankstreck. Inga tal utöver ritningens mått och de låsta priserna.

## 2. Grinden efter sista planen, i din session

Servern `python ~/.claude/skills/design/scripts/serve.py --port {{PORT}} --root .` från
repo-roten. Kontrollprotokollet gäller (`tests/motion/smooth.html` först, ren kontroll
omedelbart före varje sidmätning; ger kontrollen en ruta > 33 ms: vänta en minut och kör om;
ger den fortfarande brus efter två försök mäts sidan ändå och kontrollens tal skrivs bredvid).

1. `motion_probe.py --cpu 4`, spår `section.hero:--sc-ps,.plate-card:transform` (40 ticks
   från toppen) och `#process:--sc-ps` (`--ticks 45`, start vid `#process`s överkant minus
   en viewport), `--wheel 100:60` och `--wheel 20:120`, båda riktningarna (uppåt: negativt
   px-tal och start vid aktens slut; saknar din kopia `--start`, skriv scrollY-starten via
   `page.evaluate` i en kopia i scratch, aldrig i skill-filen); också `--cpu 1`. Skriv
   kontroll och sida sida vid sida. Bar: staircase 0, p95 ≤ 20 ms, 0 rutor > 33 ms,
   `--sc-ps` max_step ≤ 3 %. Loop 1:s tal (NOTES § Loop 1) är utgångsläget: skriv före och
   efter, inte bara efter. Faller bildtiden ändå (den föll i R4, R5, R6 och loop 1 vid cpu 4):
   rapportera, bygg inte om något utanför planerna.
2. `scroll_verify.py` vid 1440x900 och 390x844 (`--out {{UT_MAPP}}/shots/r7`): H-16, H-17,
   H-18; nya `blankBands` av 017:s luft redovisas mot `gates.md` § Both directions.
3. `perf_probe.py --cpu 4` vid 1440 och 390: `long-task-under-scroll`, CLS ≤ 0,05 (015 och
   017 ändrar höjder), sidans egen vikt.
4. `preflight_taste.py`, `detect.mjs --json` (finns inte skriptet: skriv det som saknat, inte
   som kört), `contrast_over_media.py --url` (hero-rubriken och underraden mot den nya
   grunden efter 017; `.price`-texterna mot `--c-graphite` efter 013; bildtexterna;
   kortbaksidan efter 016), `contrast.py` där planen säger det, `a11y_scan.py`, `tab_walk.py`
   (012: tabbordningen redovisas som avsiktlig skillnad mot visuell ordning), `reflow.py`
   vid 320 och 200 % plus 900x600, 1024x640, 1180x740, 1280x800, 1366x640 och plan 001:s
   1280x600, 720x450.
5. Grep: `prefers-reduced-motion` 0, U+2013/U+2014 0 i synlig text, inga nya inline-hex
   utanför `:root`.
6. Skärmbilder, allt i `{{UT_MAPP}}/shots/r7/`: hela sidan i skivor vid 1440 och 390 (som
   `shots/loop-1/slices-*`), fold vid 320/375/414/768/1024/1280, `?preview=front|mid|back|
   ledger|bleed|process-01…07` vid 1440 och 390, tolv ramar genom heron (`--flip` 0 till 1)
   och tolv genom `#process` (från överkant minus en viewport till underkant) vid 1440 och
   390, tolv ramar genom `footer.close` vid 1440 (015). Läs varje bild, `läst: <fil>` i NOTES,
   F-007 bild för bild mot varje plans Verification-bild.
7. PageDown-vandringen (a11y fix 3) om igen efter 025: sju av sju steg.
8. `?preview=process-01…07` vid 1440: i varje preview N får ingen bana ur
   `g[data-step="0(N+1)"]` vara synlig (025 steg 4); vid 390: stegrubriken under arket är
   steg N:s.

## 3. Invarianter

F-011 rörelsen spelar alltid. F-014 allt som förflyttar sig läser `--sc-ps`. Gate 47/79
(ritningen ritar form, aldrig innehåll), 75 (noll tankstreck), 88 (ingen scroll-cue-text).
Ingen generering, ingen tredje iframe, en höjdmekanism, `@property` för varje `--p-*`.
Ordagrann copy ur `PRODUCT.md` § Låst copy rörs aldrig, femton strängar, alla ska finnas kvar
byte för byte efter rundan; stegens copy v1 orörd. `PRODUCT.md` § absences. Motorn och
`sites/*` orörda. Fullständig output; måste du pausa: `[PAUSED — plan X av 8]` som sista rad.

## 4. Leverans

- `{{UT_MAPP}}/index.html`, `{{UT_MAPP}}/shots/r7/`.
- `{{UT_MAPP}}/NOTES.md` § R7: en rad per plan med dom och orsak (talen före/efter där
  planen kräver det), grinden med kontroll- och sidtal, F-007-tabellen, PageDown-utfallet,
  preview-läckagekontrollen (punkt 8), låst copy 15/15, avvikelser med skäl.
- `{{UT_MAPP}}/BRIEF.md` § decision ledger, "Byggarens rader, R7": raderna planerna anger
  (017 seams/offset/bleed, 026 ramarnas montering, 025 stegens ankare, 013 `--c-graphite`, 015 avslutet 100 svh).
- HELHET.md § 3 rörs INTE av byggaren: arkitekten bockar i loop 2.

Sista raden i sista meddelandet: `R7 klar` eller `[PAUSED — plan X av 8]`.

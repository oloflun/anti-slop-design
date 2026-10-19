# Alunix r8, runda 4. Cell {{KONCEPT}}. Fixrunda efter kvartetten.

Samma session, samma cell. R3 byggde hela sidan; fem granskare (craft, heuristik, a11y, perf,
codex) och arkitektens F-007 gav `fix` och åtta sammanslagna planer. Den här rundan utför dem,
och stänger dessutom två steg som R3 lämnade öppna.

## 1. Planerna, i nummerordning

Utför `{{UT_MAPP}}/plans/001` till `008` i nummerordning. Varje plan har **Problem**, **Steps**
och **Verification**. Kör planens Verification innan du öppnar nästa, och skriv utfallet i
transkriptet: `verified`, `best-effort` (med vad som återstår) eller `reverted` (med orsak).
Aldrig `verified` på känsla. Ordningen är redan planernas: funktionsfel (001 folden under
700 px höjd, 002 ramarna tar scroll och tabb, 003 CLS vid 390) före states, flöde, visuellt.

Läs `~/.claude/skills/impeccable/` harden-passet innan 001–003, `Skill(animate)` +
`emil-design-eng` innan 005 (bildtiden i signaturakten: RecalcStyle 73 % av tasktiden,
mätt; planen anger var kostnaden sitter). Kirurgiska `Edit`-anrop på
`{{UT_MAPP}}/index.html`, en plan i taget, aldrig `Write` av hela filen. UI-filer författas
bara med `Write`/`Edit`; `design-gate.py` nekar `cat >`, heredoc, `tee`, `sed -i`,
`Set-Content` och inline-skript (ledgersignal `shell-write`). Motorn i `{{UT_MAPP}}/scroll/`
redigeras aldrig, `.sc-*` restylas aldrig. Exempelsajterna under `sites/` redigeras aldrig.

## 2. De två öppna stegen från R3

1. **`Skill(review-animations)`**, i din egen session, rapporten i sin helhet i transkriptet.
   R3-anropet nekades för att skillen bar `disable-model-invocation`; flaggan är borttagen
   (Q24). Standard 8 (reduced motion) gäller inte, F-011. Kör den **efter** plan 005, så att
   den granskar den rörelse som faktiskt lämnar rundan.
2. **`scroll_verify.py`** kördes aldrig i R3. Den ingår i grinden nedan.

## 3. Hela mekaniska grinden efter sista planen

Servern är `python ~/.claude/skills/design/scripts/serve.py --port {{PORT}} --root .` från
repo-roten. I ordning, med utfallen i transkriptet och i NOTES.md:

1. `scroll_verify.py --url http://127.0.0.1:{{PORT}}/{{UT_MAPP}}/index.html --out {{UT_MAPP}}/shots/r4`
2. `motion_probe.py` med kontrollprotokollet: först
   `--url http://127.0.0.1:{{PORT}}/tests/motion/smooth.html --cpu 4 --track "#act:--sc-ps,#card:transform"`;
   ger kontrollen någon ruta > 33 ms är värden brusig, vänta en minut och kör om. Mät sidan
   bara när kontrollen är noll: `--track "section.hero:--sc-ps,.plate-card:transform"`,
   `--cpu 4`, `--wheel 100:60` och `--wheel 20:120`, båda riktningarna. Baren: `staircase 0`,
   `max_step <= 3 %` på `--sc-ps` (rapporteras, grindar inte, på `transform`), p95 <= 20 ms,
   noll rutor > 33 ms. Spåra aldrig rått `--sc-p`. Skriv kontrollens och sidans tal sida vid
   sida.
3. `perf_probe.py --url ... --cpu 4` vid 1440 och 390. Skriv sidans **egen** vikt (utan
   ramarnas resurser) och ramarnas separat, som i R3; budgeten döms på sidans egen tills
   proben attribuerar själv.
4. `preflight_taste.py {{UT_MAPP}}/index.html --url ...`
5. `node ~/.agents/skills/impeccable/scripts/detect.mjs --json {{UT_MAPP}}/index.html`
6. `contrast_over_media.py --url ...` på varje yta med text över bild.
7. `a11y_scan.py`, `tab_walk.py`, `reflow.py` mot din URL, plus vid 1280x600, 1024x640 och
   720x450 (plan 001:s mått), och tabbordningen genom båda ramarna (plan 002).
8. Skärmbilder: 320 / 375 / 414 / 768 / 1440, båda grunderna, `?preview=`-lägena,
   1280x600 och 720x450 för folden. Läs varje som bild, `läst: <fil>` i NOTES.md.

## 4. Invarianter

F-011 rörelsen spelar alltid. F-014 allt som förflyttar sig läser `--sc-ps`. Ingen
generering. Noll tankstreck i synlig text. Ordagrann copy ur `PRODUCT.md` § Låst copy rörs
aldrig, femton strängar, alla ska finnas kvar byte för byte efter rundan. Fullständig
output; måste du pausa: `[PAUSED — plan X av 8]` som sista rad.

## 5. Leverans

- `{{UT_MAPP}}/index.html`, `{{UT_MAPP}}/shots/r4/`.
- `{{UT_MAPP}}/NOTES.md` § R4: en rad per plan med dom och orsak, `review-animations`-
  rapporten, sedan grinden med kontroll- och sidtal, låst copy 15/15 bekräftad.

## Tillägg från lead (2026-09-15)

1. **Plan 004 är redan delvis utförd.** Heron i `{{UT_MAPP}}/index.html` gjordes om 14/9:
   `data-sc-span="4.8"`, `perspective:2600px`, transient nedskalning
   `scale(calc(1 - 0.72*flip*(1-flip)))` på `.plate-card`. Lead pixelverifierade 15/9 vid
   `--flip` 0 / 0.25 / 0.5 / 0.75 / 1 på 1440 och 390: kortets hörn står innanför plåten,
   inget klipps (`{{UT_MAPP}}/shots/r4-pre/`). Kör bara planens **Verification**; ändra
   vändningens geometri bara om den faller, och skriv i så fall vad som föll. Spannet 4.8
   rörs inte i den här rundan: arkitekten dömer tempot parallellt.
2. **Modellen är Sonnet i den här rundan** (Antons regel: bara byggare får vara Sonnet).
   Det ändrar inget i uppdraget; det ändrar att du läser varje plan i sin helhet innan du
   rör filen, och kör varje Verification innan du kallar något `verified`.
3. **Ingen processakt i den här rundan.** En ny sektion `#process` (ritningen ur K3) byggs i
   R5 efter arkitektens plan 010. Bygg inget under `.stagger` utöver vad planerna säger.
4. `{{UT_MAPP}}/assets/demo-calyx-1440.webp` ligger nu i cellen (vendorat av lead för R5).
   Rör den inte.

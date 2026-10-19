# Alunix r8, runda 3. Cell {{KONCEPT}}. Fixrunda.

Samma session, samma cell. R2 stoppades på F-007: fem avvikelser mot målbilden, dömda av
arkitekten bild för bild och skrivna som planer. Den här rundan utför planerna. Hela sidan
(R3:s innehåll) byggs **inte** nu; platshållarna `<!-- R3 -->` ligger kvar.

## 1. Planerna, i nummerordning

Utför `{{UT_MAPP}}/plans/001` till `005` i nummerordning. Varje plan har **Problem**,
**Steps** och **Verification**. Kör planens Verification innan du öppnar nästa plan, och
skriv utfallet i transkriptet: `verified`, `best-effort` (med vad som återstår) eller
`reverted` (med orsak). En plan som inte kan verifieras lämnas `best-effort`, aldrig som
`verified` på känsla.

Läs `~/.claude/skills/impeccable/` layout-passet (planerna 001, 004 och 005 är
layoutvyport, mediafråga och koordinater) innan första `Edit`. Plan 003 är två koordinater
i SVG:n; plan 002 är ett element.

Kirurgiska `Edit`-anrop på `{{UT_MAPP}}/index.html`, en plan i taget. Aldrig `Write` av hela
filen. UI-filer författas bara med `Write` eller `Edit`; `design-gate.py` nekar `cat >`,
heredoc, `tee`, `sed -i`, `Set-Content` och inline-skript (ledgersignal `shell-write`).
Motorn i `{{UT_MAPP}}/scroll/` redigeras aldrig, `.sc-*` restylas aldrig.

## 2. Typsnitten

Typsnitten var **ovendorade under hela R2**; lead har vendorat dem efteråt. Bekräfta först i
transkriptet att varje `@font-face`-fil svarar 200 på din port. Varje mätning och skärmbild
från R2 är ogiltig och tas om nedan.

## 3. Hela mekaniska grinden efter sista planen

Servern är `python ~/.claude/skills/design/scripts/serve.py --port {{PORT}} --root .` från
repo-roten, aldrig `http.server`. Sedan, i ordning, med utfallen i transkriptet:

1. `scroll_verify.py --url http://127.0.0.1:{{PORT}}/{{UT_MAPP}}/index.html --out {{UT_MAPP}}/shots/r3`
2. `motion_probe.py` på signaturakten, samma spår som i din R2-prompt **men utan rått
   `--sc-p`** (det trappar per hjultick av konstruktion och ska aldrig spåras). Kör först
   kontrollen `--url http://127.0.0.1:{{PORT}}/tests/motion/smooth.html --cpu 4 --track "#act:--sc-ps,#card:transform"`;
   ger den någon ruta > 33 ms är värden brusig, vänta en minut och kör om. Mät sidan bara
   när kontrollen är noll, med `--wheel 100:60` och `--wheel 20:120`, `--cpu 4`. Baren:
   `staircase = 0`, `max_step <= 3 %` på `--sc-ps` (på härledda spår rapporteras talet men
   grindar inte, Q22), p95 <= 20 ms, noll rutor > 33 ms, båda riktningarna. Läs sparklinen
   som bild.
3. `perf_probe.py --url ... --cpu 4` vid 1440 och 390.
4. `preflight_taste.py {{UT_MAPP}}/index.html --url ...`
5. `node ~/.agents/skills/impeccable/scripts/detect.mjs --json {{UT_MAPP}}/index.html`
6. `contrast_over_media.py --url ...` på varje yta med text över bild.
7. Skärmbilder: 320 / 375 / 414 / 768 / 1440, båda grunderna, `?preview=drawn`. Läs varje
   som bild och skriv `läst: <fil>` i NOTES.md. Särskilt: s1, s3 och s4 vid 390, som
   planerna 001, 002, 004 och 005 adresserar, och s3/s4 vid 1440 för plan 003.

Alla gröna, eller namngivna undantag i NOTES.md med orsak.

## 4. Invarianter

F-011: rörelsen spelar alltid, aldrig `prefers-reduced-motion`. F-014: allt som förflyttar
sig läser `--sc-ps`. Ingen generering (Higgsfield spärrat, 0 krediter). Noll tankstreck i
synlig text. Ordagrann copy ur `PRODUCT.md` § Låst copy rörs aldrig. Exempelsajterna
(`sites/calyx.html` m.fl.) redigeras aldrig (Q23). Fullständig output; måste du pausa:
`[PAUSED — plan X av 5]` som sista rad.

## 5. Leverans

- `{{UT_MAPP}}/index.html` med planerna utförda.
- `{{UT_MAPP}}/shots/r3/`.
- `{{UT_MAPP}}/NOTES.md` § R3 (fixrunda): en rad per plan med `verified` / `best-effort` /
  `reverted` och orsak, typsnittsbekräftelsen, sedan probe-utfallen med kontrollens och
  sidans tal från `motion_probe` sida vid sida.

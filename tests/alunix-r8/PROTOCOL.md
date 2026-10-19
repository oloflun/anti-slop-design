# Alunix r8, rundordning

Den här filen är körordningen, inte innehållet. Vad cellerna ska bli står i
planen `C:\Users\Anton L\.claude\plans\trots-den-senaste-design-system-federated-raven.md`
§ 7.5 (målbilderna), § 7.6 (exit per cell), § 6.1 (lyftet) och § 8 (prompterna).
Faller planen och den här filen isär: planen gäller, den här filen rättas.

Läses av lead. Lead skriver aldrig UI-kod. Byggarna är headless `claude -p`,
en session per cell, startade av `run.py`.

## Fasta fakta

| | |
|---|---|
| Celler | `V3c` (port 3301), `K3` (3302), `K4` (3303) |
| Arm | `B` för allt: kedjan på, r6:s plugin-shim `tests/alunix-ab-r6/plugin-b` |
| Modell | `claude-opus-5` för alla agenter, byggare inräknade (`--model` är default) |
| Cellens mapp | `tests/alunix-r8/runs/<cell>/` med `assets/`, `shots/`, `plans/` |
| Rundlogg | `tests/alunix-r8/logs/round-<N>/` |
| Board | `tests/alunix-r8/board/`, port 4626, en cell i taget i full bredd |
| Cwd | repo-roten. Alla kommandon nedan körs därifrån |

Byggarens env sätts av harnesset: `DESIGN_HOOKS_FORCE_ARM=1` (utan den armar en
headless session aldrig hookarna, och då finns ingen ledger att mäta),
`SCROLLCRAFT_CHROME`, `UNSPLASH_*`. Byggarens argv har `--disallowed-tools` mot
Higgsfields genereringsverktyg: **bara lead genererar material** (§ 10.7).

## Kommandon

```
# runda 1, ny session per cell
python tests/alunix-r8/run.py build B <cell> --round 1 --prompt-file <rundprompt>

# runda 2 och framåt, samma session fortsätter
python tests/alunix-r8/run.py build B <cell> --round <N> --resume --prompt-file <rundprompt>

# torrkörning: visar argv, env-nycklar och flaggor, spawnar ingenting
python tests/alunix-r8/run.py build B <cell> --round <N> --dry-run

# boarden: bygg board.json och kopiera cellerna, starta sedan launch-posten
python tests/alunix-r8/run.py board
```

Rundprompten är en fil och måste innehålla `{{KONCEPT}}`, `{{UT_MAPP}}` och
`{{PORT}}`; harnesset byter ut dem per cell och stannar på okända platshållare.
Samma fil kan därför köras för alla tre cellerna. Utan `--prompt-file` faller
`build` tillbaka på `tests/alunix-r8/PROMPT.md` (finns inte ännu, och behöver
inte finnas: rundprompterna är arkitektens leverabler).

Boarden startas som launch-posten `alunix-board-r8`; den kräver att
`run.py board` har skrivit `board/board.json` först.

## Fas 0, arkitekten, innan någon byggare startar

Ingen byggare startas förrän alla fem är klara. Ordningen är bindande
(planens § 7.4, fas 0; arkitektens fulla prompt är § 8.2).

1. **Registret.** 31 rader appendas till `wiki/projects/_index/design-fingerprints.md`
   i radformatet. Grind: `grep -c -i alunix` ≥ 29, sex fyllda kolumner per rad.
2. **`PRODUCT.md`.** Impeccables `init.md`-schema, bara fakta ur
   `tests/alunix-ab-r7/PROMPT.md` § Alunix. "Evidence on hand" listar exakt vad
   som får synas; "absences" listar vad som aldrig får hittas på.
3. **`concepts.md`.** Katalog-först per cell: `sweep_raw.py` (ska vara tom),
   `select.py --brief … --k 4 --wildcard --explain`, de valda posterna lästa som
   pixlar, sedan målbildsgrinden ifylld per cell: auktoritet + vad som viker,
   troplistan avprickad, ett displayelement per skärm, fingerprint mot **varje**
   registerrad utskriven. Faller K3 eller K4 under 4/6: byt plan, aldrig raden.
   V3c är en iteration av V3b och undantas fingerprint-gaten.
4. **Briefskelett per cell.** Reference lock, decision ledger, direction
   contract, motion-tes, feeling curve, tell-someone-mening, device-tabell,
   Rejected-lista.
5. **Rundprompter R1 till R3** lämnas till lead som filer.

Grind ut ur fas 0: lead har läst `concepts.md` och de valda katalogposterna som
pixlar själv och godkänt målbilden per cell. Först då startar R1.

## Fas 1, rundor per cell

Celler kör parallellt, rundor sekventiellt inom en cell. En runda i taget per
cell. Innan lead läser något i en runda: vänta på
`logs/round-<N>/B-<cell>.done`. Filen skrivs när sessionen har avslutats och
`*.meta.json` är komplett.

### R1, referenspaket, ingen HTML

```
python tests/alunix-r8/run.py build B <cell> --round 1 --prompt-file tests/alunix-r8/PROMPT-R1.md
```

Byggaren kör `Skill(design)` först, läser golvet och de valda katalogposterna,
och skriver `runs/<cell>/BRIEF.md`: r7-formatet, Design Read-enraden,
dial-deklaration, motion-tes, Rejected-lista, `?preview=`-plan.

Lead läser BRIEF.md mot filerna den påstår sig ha läst. Arkitekten godkänner
eller skickar tillbaka, **max ett varv**. Ingen HTML får finnas efter R1.

### R2, fold och signaturakt

```
python tests/alunix-r8/run.py build B <cell> --round 2 --resume --prompt-file tests/alunix-r8/PROMPT-R2.md
```

`index.html` med hero-akten komplett (V3c: flippen, K3: ritningen som ritar sig,
K4: delaren som tippar), motorn och `sc-smooth.js` kopierade, `?preview=`-lägen.

Lead: skärmbilder vid 1440 och 390, `motion_probe`, `scroll_verify`. Arkitekten
gör **F-007-kontrollen bild för bild mot målbilden innan något annat bedöms**.
Avvikelse stoppar rundan; nästa runda blir en fixrunda, inte R3.

### R3, hela sidan

```
python tests/alunix-r8/run.py build B <cell> --round 3 --resume --prompt-file tests/alunix-r8/PROMPT-R3.md
```

Hela sidan, copy-gate i fem pass **namngivna i transkriptet**, och i byggarens
egen session: `Skill(emil-design-eng)` med Before/After/Why per övergång,
`Skill(review-animations)` explicit, `Skill(a11y-audit)` explicit. Att de körs i
byggarens session och inte bara hos lead är r7-luckan som r8 stänger.

### R4 och framåt, fixrundor

```
python tests/alunix-r8/run.py build B <cell> --round <N> --resume --prompt-file runs/<cell>/plans/PROMPT-R<N>.md
```

Kvartettens `material_fixes` blir planer i PLAN-TEMPLATE-format, skrivna av
arkitekten till `runs/<cell>/plans/NNN-slug.md`. Byggaren utför, **max 8 fixar
per runda**. Ordning: funktionsfel, states, flöde och hierarki, visuellt, kod.

### Mellan varje runda, samma sekvens varje gång

1. Vänta på `.done` **eller `.failed`**. `.failed` skrivs när sessionens sista
   result-post har `is_error: true` (R1 2026-09-10: kontots användningsgräns
   klippte två byggare mitt i rundan, med subtype `success` och `is_error: true`)
   eller exitkoden inte är 0. En `.failed` cell återupptas med `--resume` och en
   fortsättningsprompt innan något granskas; läs aldrig en `.failed` cell som
   klar. Läs `*.meta.json` (exit, kostnad, `result.is_error`).
2. Lead läser **varje** skärmbild som pixlar och skriver "läst: `<fil>`" i
   `runs/<cell>/NOTES.md`. En skärmbild som inte lästs räknas inte.
3. Mekaniska grindar: `detect.mjs --json`, `preflight_taste.py`,
   `scroll_verify.py`, `perf_probe.py`, `motion_probe.py`,
   `contrast_over_media.py --url`.
4. Kvartetten väcks med URL, cellens BRIEF.md och skärmbildskatalogen.
   Lead sparar varje rapport som en fil under `runs/<cell>/reviews/` och kör
   `python scripts/check_reviewer_report.py <rapport>` på var och en innan den
   läses. Kontrollen avvisar en rapport utan dispositionsord på första raden,
   med saknad, dubblerad, felordnad eller sjätte sektion, med fler än åtta
   `material_fixes`, eller som tar upp reduced motion som ett fynd (F-011).
   En rapport som faller kontrollen skickas tillbaka, den sammanfogas inte.
   Lead verifierar sedan varje fynd mot pixlarna innan det sammanfogas.
   Prioritet vid konflikt: accessibility > performance > usability > brief >
   personas > escalate.
   Femte granskaren, `codex-review`, körs på samma sätt och i samma kontrakt,
   men läser koden i stället för designen och verifierar varje codex-fynd mot
   filen innan det rapporteras.
5. Varje beslut blir en rad i `runs/<cell>/NOTES.md` (datum, beslut, källa:
   F-post, TASTE-§, katalogpost eller agentrapport).
6. `STATUS.md` uppdateras: cell, runda, disposition, gröna grindar, öppna punkter.

## Fas 2, lyftet

Per cell, enligt planens § 6.1: läs-bara revision → kvartetten parallellt →
var rörelsen ska sitta → fixlista → fix-passen i ordning (layout, typeset,
colorize bara vid platt eller grå, animate, delight bara vid delight-tes,
copy-gate, harden, optimize, polish sist) → mekanisk grind efter varje pass.

Stopp: en hel pass (revision + kvartett) hittar noll materiella fynd och
kritikern skriver "slår" per låst referens. **Tak 6 varv per cell**, sedan
tabell över öppna punkter till Anton i stället för ett sjunde varv.

Sedan, i denna ordning:

1. `python tests/alunix-r8/run.py board`
2. Starta `alunix-board-r8` (port 4626, en cell i taget, full bredd).
3. Antons dom.
4. F-post per cell i `design-catalogue/FEEDBACK.md` i fältformatet. Innan domen
   är cellens rad `pending-anton`.
5. Fingerprint-rad appendas, `NOTES.md` har beslutsledgern,
   `design-stop.py`-rapporten sparas i `logs/final/<cell>/`.

Cellens rad blir `SHIP` när allt i planens § 7.6 är sant, inte tidigare.

## Vad som stoppar en runda

- F-007-avvikelse mot målbilden.
- En mekanisk grind röd.
- Byggaren skrev UI innan golvet lästs (syns i ledgern som nekat verktygsanrop).
- Byggaren försökte generera material (nekat verktygsanrop, se `--disallowed-tools`).
- Kritikern skriver "står sig bredvid" i stället för "slår".
- Påhittade fakta: kunder, omdömen, team, kontor. Stoppar rundan direkt.
- Tankstreck i synlig text, eller ändrad ordagrann Alunix-copy.

Rörelsen spelar alltid (F-011). Ingen `prefers-reduced-motion`, inga statiska
fallback-träd, och ingen reviewer får flagga frånvaron som fynd.

## Valt läge 2026-09-09: headless lead, bevakaren är loopen

Anton valde att leaden körs headless (`claude -p --model claude-opus-5`) och
återupptas per fas/runda av den bevakande Fable-sessionen, i stället för en
terminal med `/loop` och teammates. Skäl, mätt: en terminalsession syns inte i
sessionsregistret och kan inte nås med `send_message`, så den hade bara gått att
bevaka via filer, inte korrigera. Prompten ligger i `LEAD-PROMPT.md`; leaden
skriver `LEAD-REPORT.md` efter varje körning och startar aldrig nästa fas själv.
Teammates ersätts av `Agent`-subagenter (samma agenter, samma kontrakt).
Avsnittet nedan beskriver terminalvägen och gäller om läget byts tillbaka.

## Så startas lead-sessionen i terminal (mätt 2026-09-09, planens § 8.1 och § 8.6 rättade)

Planen säger `/goal <villkor>` och därefter `/loop <text>`. **`/goal` finns inte.**
Kontrollerat i båda binärerna på maskinen (npm 2.1.241 och den som desktop-appen
paketerar, 2.1.260): ingen `goal`-rad i `--help`, ingen `goal*.md` under
`~/.claude/commands/` eller i något plugin. `/loop` finns och är inbyggd.

Måltillståndet försvinner inte, det flyttar: skriv villkoret i planens § 8.6a som
**exit-villkoret inuti `/loop`-texten**. Loopen läser ändå `STATUS.md` varje varv,
så den kan avgöra samma sak — den säger "green and quiet" och stoppar när varje
cell står `SHIP`, eller `STOPPED` efter 8 byggrundor plus 6 lyftvarv.

Terminalstarten fungerar, men den tar två tangenttryck av Anton första gången:

```
powershell -NoProfile -Command "Start-Process -FilePath 'wt.exe' -ArgumentList 'cmd','/k','cd /d \"C:\Users\Anton L\anti-slop-design\" && set CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1 && claude'"
```

1. **Förtroendedialogen.** `~/.claude.json` har `hasTrustDialogAccepted: false` för
   den här mappen, så första interaktiva sessionen i repot stannar där. Engångs.
2. **Enter.** En prompt som skickas med som argument hamnar förifylld i
   inmatningsrutan; den skickas inte av sig själv. Utan TTY (t.ex. via en
   `.cmd` med omdirigerad utdata) körs den direkt — det är skillnaden som gjorde
   att fönstret i förra sessionen "levde" utan att någonsin behandla en tur.

Sessionen registrerar sig i `ListAgents` först efter sin första behandlade tur.
Därefter går den att styra med `SendMessage`.

## Att veta om harnesset

- **UI-filer författas bara med Write eller Edit.** Proben 2026-09-09 skrev sin
  HTML med `cat > … <<'EOF'` och passerade referensgolvet obemärkt, eftersom
  varje grind i kedjan lyssnade på Write/Edit. `design-gate.py` nekar nu
  skalförfattande (omdirigering, heredoc, `tee`, `sed -i`, `Set-Content`,
  inline-skript) av `.html/.css/.js`-filer i en armad session. Att **kopiera**
  motorn (`cp`, `Copy-Item`) är fortfarande tillåtet. Nekandet syns i ledgern
  som `gate-deny` med signalen `shell-write`.
- `run.py` ärver `tests/alunix-ab-r6/run.py`. r6 ändras aldrig; det r8 behöver
  annorlunda patchas som modulnamn i `tests/alunix-r8/run.py`.
- `--resume` hämtar sessions-id från närmast föregående rundas `*.meta.json` och
  kopierar in det i den nya rundans loggmapp. Hoppa aldrig över `--round`:
  utan den hamnar loggarna i `logs/` direkt och resume-kedjan tappar spåret.
- `--dry-run` spawnar ingen process. Den visar argv med prompten förkortad till
  sha256, vilka env-nycklar som läggs till, och för `board` vilken serve-rad
  launch-posten motsvarar.
- Byggarens env ärver `UNSPLASH_*` från `~/.secrets/.env`. Att byggaren inte gör
  egna Unsplash-anrop är en promptregel, inte en spärr; kontrollera det i
  ledgern om en cell plötsligt har foton ingen bett om.
- Higgsfield-spärren listar verktygsnamn per MCP-server-id. Byter connectorn id:
  sätt `ALUNIX_HIGGSFIELD_MCP` (kommaseparerat) och kör om torrkörningen.

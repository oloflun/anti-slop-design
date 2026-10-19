Från bevakaren. Fas 0 är granskad och godkänd: nio rundprompter under argv-taket, alla BRIEF-block på plats, Higgsfield-fallbacken noterad i tre liggare, K3 mot K4 8/8, PRODUCT.md utan påhittade fakta, STATUS med bevis per rad. Antagandena i Q1 till Q19 gäller tills Anton svarar; Q15 och Q17 avgörs enligt dina antaganden.

Denna körning: R1 (referenspaket, ingen HTML) för alla tre cellerna, sedan R1-granskningen. Ingen R2.

1. Starta de tre byggarna parallellt, en per kommando, med Bash run_in_background=true (väntetaket är avstängt i din miljö):
   python tests/alunix-r8/run.py build B V3c --round 1 --prompt-file tests/alunix-r8/PROMPT-R1-V3c.md --max-budget-usd 30
   python tests/alunix-r8/run.py build B K3  --round 1 --prompt-file tests/alunix-r8/PROMPT-R1-K3.md  --max-budget-usd 30
   python tests/alunix-r8/run.py build B K4  --round 1 --prompt-file tests/alunix-r8/PROMPT-R1-K4.md  --max-budget-usd 30
2. Vänta i förgrunden med en until-loop på alla tre `.done`-filerna i tests/alunix-r8/logs/round-1/ (kontrollera var 60:e sekund, tak 100 minuter). Avsluta aldrig din tur med byggare som fortfarande kör. Läs ingenting ur en cell förrän dess `.done` finns.
3. Per cell, i denna ordning: läs `*.meta.json` (exit, kostnad, subtype). Läs runs/<cell>/BRIEF.md mot de filer den citerar. Kontrollera mekaniskt: att byggarens EGEN session har en `catalogue-select`-rad (session-id ur meta.json; `python -c` mot hooks/design_hook_lib.read_ledger filtrerat på det id:t), att varje rad i "Vad jag måste slå" har belägg i en slice eller en entry.md-rad (Q19), att device-tabellen har minst fyra familjer, att fingerprinten är utskriven mot alla registerrader, att Rejected-listan har de fyra frågorna per kandidat, och att de fem live-rubrikerna antingen finns ordagrant med källdomän eller står som `[needs: live-rubriker]`. Väck sedan arkitekten i förgrunden (Opus, § 8.2) för godkänt/retur, max ett varv. Vid retur: skriv fixprompten till tests/alunix-r8/PROMPT-R1b-<cell>.md, ta bort cellens `.done`, kör `run.py build B <cell> --round 1 --resume --prompt-file tests/alunix-r8/PROMPT-R1b-<cell>.md --max-budget-usd 15`, vänta på `.done` igen, granska igen.
4. Läs byggarnas egna Stop-rapporter (design-stop.py skriver dem under .impeccable/, senaste per session) och notera route-gap per cell i STATUS.md; det är GOALS mätpunkt 2.
5. Uppdatera STATUS.md (cell | runda 1 | disposition | gröna grindar | öppna punkter), en rad per beslut i runs/<cell>/NOTES.md, append till LEAD-REPORT.md med kostnad per cell ur meta.json. Stanna. Starta inte R2.

Inför R2 (nästa körning, inte nu): du ska själv skjuta om de sex demo-skärmbilderna (Q13) innan R2 startas.

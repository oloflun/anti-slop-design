# AB11 — SlopMonster mot copywriting → copy-editing → humanizer (EN + SV)

Samma AI-präglade utkast (Kvist på engelska, Florhuset på svenska; deslop 1/5). A = vår kedja (tre pass, humanizer per språk). B = SlopMonster-loopen (score → tre pass → cleanse via codex/GPT → rescore).

| Mått | A (vår kedja) | B (SlopMonster) | Not |
|---|---|---|---|
| deslop-score (B:s egen skala) | 4/5 | 5/5 | A:s två träffar är produktens riktiga tre funktioner ("records, replays, and diffs") — regel 4 falsklarmar |
| em-dashes synliga (gate 75) | 0 (en-dash bara i tidsintervall) | 9 (listavskiljare, "[Start recording — free]") | B bryter vår hårdaste copy-gate |
| påhittade tal/kunder/citat | 0 | 0 | båda strök "10,000+ happy developers" |
| påståenden utanför briefen | 0 | 3 ("no account required", "raw bytes", "no trial clock, no credit card") | B uppfann produktfakta; texture är ok, produktlöften inte |
| svenska | humanizer-svenska: rent men generiskt ("Vår enklaste bukett") | scorern blind (falsk 5/5 på svensk halva); handpassen gav den bästa svenskan i testet ("vad som blev över från veckans snitt", "Blommor är en av de saker man glömmer bort att boka") | |
| engelska | korrekt, platt ("Know what your API actually changed") | specifik, röst ("No mock that quietly stopped matching reality"; Diff: "field, old value, new value") | B vinner på röst |
| rival-cleanse (codex) | — | ändrade bara dash → punkt och meningslängd; lade till en sammanfattning trots "return only the copy" | liten effekt, ett protokollbrott |
| tid/beroenden | tre skills, ingen extern modell | scorer (stdlib) + codex-anrop + manuell svensk hantering | |

Läst av mig: B:s copy är den jag hellre skulle skeppa på båda språken, efter att dashen tagits bort och de tre uppfunna produktlöftena strukits. A:s copy är den som passerar alla våra gates utan efterarbete. Skillnaden ligger inte i scorern (som är engelsk, smal och falsklarmar) utan i SlopMonsters omskrivningsprinciper: "var kommer raden ifrån" (hantverket, kundens rädsla, det konkurrenten inte säger, raderna som redan var bra).

**Beslut: HYBRID, inte ersättning.** Kedjan behålls som skrivare (den enda som klarar svenska och gate 75). In: (1) `deslop.py` som mekanisk grind efter Step 6 på engelska strängar (som detect.mjs för copy), med tricolon-träffar bedömda för hand; (2) SlopMonsters fyra radkällor och "never invent proof"-regeln in i copy-gate.md som skrivpass 1b; (3) en svensk twin-lista (inte bara X — det är Y · tricolon med "och" · i hjärtat av · kurerar · älskad mötesplats · passion/precision/kärlek) i copy-gate för humanizer-svenska. Ute: rival-cleansen som obligatoriskt steg (liten effekt, extern modell, protokollbrott) — valfri på engelska marknadssidor.

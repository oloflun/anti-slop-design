# LEAD-REPORT

En `## `-rubrik per körning. Append, aldrig omskrivning.

## 2026-09-10 · Fas 0

Gjort:
- `tests/alunix-r8/PRODUCT.md`: beviskassan, 180 rader, bara fakta ur `tests/alunix-ab-r7/PROMPT.md`.
- `wiki/projects/_index/design-fingerprints.md`: tio tomma Register-celler ifyllda; inga rader appendade, se Verifierat.
- `tests/alunix-r8/concepts.md`: sammanslagen målbildsfil, 183 766 tecken, med leadens godkännandetabell och K3-mot-K4-tabellen.
- `tests/alunix-r8/concepts-V3c.md`, `concepts-K3.md`, `concepts-K4.md`: källfilerna, målbildsgrinden 1 till 8 per cell.
- `tests/alunix-r8/malbilder/{V3c,K3,K4}.md`: planens § 7.5-text per cell, ordagrant, som arkitekterna och rundprompterna citerar.
- `tests/alunix-r8/ARCHITECT-PROMPT.md`: planens § 8.2 ordagrant, så att varje arkitektsubagent får samma rollprompt.
- `tests/alunix-r8/runs/{V3c,K3,K4}/BRIEF.md`: briefskelett med `[fylls i R1]`-fält.
- `tests/alunix-r8/runs/{V3c,K3,K4}/assets/ASSETS.md` och `credits.json`: assetpaket och proveniens.
- `tests/alunix-r8/runs/{V3c,K3,K4}/NOTES.md`: beslutsledger per cell.
- `tests/alunix-r8/PROMPT-R{1,2,3}-{V3c,K3,K4}.md`: nio rundprompter.
- `tests/alunix-r8/QUESTIONS.md`: Q1 till Q19, var och en med ett antagande som gäller tills svar kommer.
- `tests/alunix-r8/STATUS.md`: fas 0-tabellen uppdaterad rad för rad med bevis per leverabel.

Verifierat:
- **Registret behövde ingen append.** Planens § 8.2 A säger "append 31 rader". Jag räknade raderna innan något skrevs: de 29 Alunix-raderna fanns redan, och r7:s K1 v2 och K2 v2 är rad 105 och 106, införda vid conclude 2026-09-08, alltså efter att planen skrevs. En andra append hade duplicerat dem, och rader är append-only, så en dubblett går inte att ta bort. Uppgiften blev därför verifiering: alla 29 rader har sex ifyllda grinddimensioner, `grep -c -i alunix` ger 35, och de 36 dataraderna innehåller noll dubblerade Build-värden. Tio tomma Register-celler fylldes ur cellernas egna filer.
- **Higgsfield är ute.** Jag mätte saldot i stället för att anta det: `balance` ger noll krediter på free plan, och kontot har en enda privat workspace. r7:s 73,5 krediter finns inte kvar. Enligt planens § 10.6 tog jag beslutet att r8 kör med noll genererat material, och korrigerade två arkitekter mitt i arbetet. För K3 är fallbackens tredje steg strikt bättre än det första, inte bara billigare: en procedurell textur är sömlös genom konstruktion, medan en genererad kakling måste sömkontrolleras och ändå kan visa repetition.
- **Nio torrkörningar, alla exit 0.** Jag körde dem själv efter arkitekten, inte på rapporten: varje rundprompt innehåller exakt `{{KONCEPT}}`, `{{UT_MAPP}}` och `{{PORT}}` och inga andra platshållare, och kommandoraden ligger minst 12 kB under Windows-gränsen.
- **Pixelgrinden är min och den är körd.** Jag läste `oryzo-ai`, `mattis-studio`, `squarespace`, `paper`, `aevi-wellness`, `beautiful`, `insign` och `mode` som bilder. Det gav ett verkligt fynd, se Öppet.
- **PRODUCT.md är spårad.** 84 påståenden pekades ut i `PROMPT.md` rad för rad; två underkändes och rättades före leverans. Noll tankstreck, kontrollerat även mot U+2010 till U+2015 och U+2212.
- `a11y-audit`-skripten finns på båda sökvägarna arkitekten var osäker på, så R3-prompternas prefix behövde ingen rättelse.
- Mätservern på port 3399 som en arkitekt lämnade igång är stängd.

Öppet:
- K3:s primärpost `squarespace` äger inte cellens stämning, täthet eller struktur, vilket `reference-lock.md` kräver av en primärkälla, och det ser jag i folden: Squarespace är fotografisk, centrerad och knappledd, medan K3 är ett kallt ritpapper utan ett enda fotografi. Jag löste det utan att välja om ur minnet, vilket vore precis det `catalogue-first.md` finns för att stoppa: Alunix ligger på Tier 1, där låset enligt `reference-lock.md` är kvalitetsribban det härledda systemet ska klara och inte riktningen, så avsnitt (7) i varje cell är det operativa innehållet. Nästa konkreta steg är att byggaren i R1 belägger varje rad i avsnitt (7) med den slice eller den `entry.md`-rad den vilar på, eftersom tre av K3:s fem rader påstår saker folden inte visar, och att en rad utan belägg stryks ur låset (Q19).
- K4:s aktform skiljer sig från K3:s på struktur men båda öppnar med `pin` span 2,4, vilket gör den till den tunnaste raden i cellens jämförelse, och nästa konkreta steg är att F-007-kontrollen i R2 avgör om de två akterna skiljer sig i pixlar och inte bara i markup, varefter K4 byter dwell eller aktordning om de inte gör det.
- Nitton frågor till Anton står obesvarade i `QUESTIONS.md`, var och en med ett antagande som gäller tills svar kommer, och nästa konkreta steg är att Anton läser dem i ett svep före boarden, eftersom bara Q15 och Q17 måste avgöras före R2 medan resten kan besvaras när som helst.
- Demo-skärmbilderna är daterade 2026-09-04 medan exempelsajterna ändrades 2026-09-09 av F-011-saneringen, och nästa konkreta steg är att skjuta om en av dem vid 1440, lägga den bredvid den ärvda och läsa båda som pixlar innan hela uppsättningen skjuts om (Q13).
- `shoot.py` har bredden hårdkodad till 1440 och kan inte skjuta 390, och nästa konkreta steg är att köra det inline-Playwright-block som ligger i K4:s `ASSETS.md` när mobilbilderna behövs i R2.
- Fem live-rubriker i kategorin saknas i alla tre briefskeletten eftersom arkitektsessionerna saknar webbsökning, och nästa konkreta steg är att byggaren hämtar dem i R1 enligt uppgiften som står i R1-prompten, eller att lead klistrar in dem innan R1 startas (Q10).

Kostnad: byggarna har inte startat, så ingen `meta.json` finns. Higgsfield: noll krediter spenderade, noll tillgängliga. Fas 0 kördes på arkitektsubagenter i denna session.

Nästa steg som bevakaren ska beställa: starta R1 för alla tre cellerna parallellt med `python tests/alunix-r8/run.py build B <cell> --round 1 --prompt-file tests/alunix-r8/PROMPT-R1-<cell>.md`, och vänta på `.done` per cell innan något läses.

## 2026-09-10 · Runda 1, referenspaket och granskning

Gjort:
- `tests/alunix-r8/runs/{V3c,K3,K4}/BRIEF.md`, ifyllda av byggarna, granskade och godkända.
- `tests/alunix-r8/runs/{V3c,K3,K4}/NOTES.md`, leadens R1-rader appendade.
- Teckenåterställning av 127 rader i `runs/K3/BRIEF.md`, `runs/K3/NOTES.md` och `runs/K4/BRIEF.md`.
- `tests/alunix-r8/PROMPT-R2-{V3c,K3,K4}.md`, fyra tillägg efter granskningen, alla tre torrkörda om.
- `tests/alunix-r8/runs/K4/assets/demo-{calyx,horai,hyperborea}-{1440,390}.webp`, sex nya skärmbilder.
- `tests/alunix-r8/runs/K4/shots/{1440,390}/`, källbilderna som webp-filerna gjordes av.
- `tests/alunix-r8/QUESTIONS.md`, Q20 och Q21.
- `tests/alunix-r8/STATUS.md`, cellraderna och ett nytt avsnitt med rundans mätvärden.

Verifierat:
- **Två av tre byggare avslutade med fel, vilket rapporten jag fick inte nämnde.** K3 och K4 har `exit_code: 1` och `is_error: true`, och resultatsträngen är `You've hit your session limit`. Bara V3c avslutade rent. Jag kontrollerade därför om leveransen var stympad: alla tre briefarna slutar sammanhängande, ingen bär en `[PAUSED]`-markör, och alla obligatoriska avsnitt finns. Arbetet landade, men rundan avslutades inte av byggaren i två fall.
- **Referensgolvet, mätt i varje byggares egen sessionsledger**, inte i rapporten: TASTE 1, FEEDBACK 1, registret 1, references 7, och varje låst slug läst som `entry.md` plus `fold` eller `slice`. `Skill(design)` anropad i alla tre. Noll `gate-deny`. Noll UI-filer. Vision-rader 54, 33 och 58.
- **Katalogvalet.** Sista `catalogue-select`-raden stämmer exakt med fas 0 i alla tre cellerna. Alla tre körde dessutom en första nollrad mot det ofyllda skelettet, inte bara V3c som jag hade fått uppgift om. Golvet läser sista raden, så låset håller.
- **Teckenkorruptionen är arkitektens, inte byggarnas.** Jag prövade påståendet innan jag accepterade det: `runs/K3/NOTES.md` bär samma fel med en tidsstämpel timmar före byggarna startade, byggarens egna avsnitt i briefen har noll träffar, och `concepts-K3.md` och rundprompterna är rena. Att returnera en byggare för det hade varit att straffa den för att den följde sin instruktion.
- **Återställningen är kontrollerad åt båda hållen.** Jag skilde entydiga former från tvetydiga: `bara`, `andra` och `satt` är korrekt svenska och rördes aldrig, medan `ar` och `matt` avgjordes per förekomst eftersom de betyder olika saker i olika meningar. Efter körningen är residualen noll, alla låsta copy-strängar finns kvar oförändrade, och inget kodspann är ändrat.
- **Q13 är besvarad med pixlar och svaret är nej.** Jag lade den nya Hyperborea-folden bredvid den ärvda och läste båda: innehåll och komposition är identiska, så borttagningen av reduced-motion-grenen ändrade inte vad folden visar. Omskjutningen behövdes ändå, eftersom cellen kräver äkta 1440 och 390 och katalogen bara hade 1200.
- Nio rundprompter dry-körs fortfarande rent efter mina tillägg.

Öppet:
- Route-vs-invocation-gapet saknar artefakt för R1, eftersom ingen session skrev en Stop-rapport och R1 skriver noll UI-filer och därmed noll route-rader, så nästa konkreta steg är att kontrollera att `design-stop.py` lämnar en rapport efter R2 innan måttet citeras som grönt.
- Q19 uppfylls inte i K3 och K4 i briefen utan i R2, där varje takrad ska bära den slice eller `entry.md`-rad den vilar på, och nästa konkreta steg är att jag kontrollerar det i R2-granskningen mot briefens egen paragraf Lästa referenser där belägget redan står.
- V3c:s takavsnitt namnger två referenser cellen aldrig låste, och nästa konkreta steg är att kritikern i fas 2 bara skriver "slår" för de fem låsta sluggarna, vilket nu står i cellens R2-prompt.
- Tjugoen frågor står obesvarade hos Anton, och nästa konkreta steg är att han läser dem i ett svep, eftersom bara Q15 och Q17 måste avgöras före R2 och båda kör på mina antaganden tills dess.
- Kostnaden för R1 blev 53,83 USD för tre celler, alltså högre än r7:s referensrundor, och nästa konkreta steg är att jag jämför R2:s utfall mot den siffran innan fixrundorna planeras.

Kostnad: V3c 12,84 USD, K3 17,97 USD, K4 23,02 USD, summa 53,83 USD ur `logs/round-1/*.meta.json`. Higgsfield: noll krediter, noll spenderade.

Nästa steg som bevakaren ska beställa: R2 för alla tre cellerna med `python tests/alunix-r8/run.py build B <cell> --round 2 --resume --prompt-file tests/alunix-r8/PROMPT-R2-<cell>.md`, och kontrollera att en Stop-rapport landar under `.impeccable/` när rundan är klar.

## 2026-09-10 · Runda 2, fold och signaturakt, med granskning

Gjort:
- `tests/alunix-r8/runs/{V3c,K3,K4}/index.html`, folden och signaturakten byggda, motorn och `sc-smooth.js` inkopierade i alla tre.
- `tests/alunix-r8/review/r2/`, leadens egna skärmbilder vid 1440 och 390 plus previewlägen, sexton bilder, var och en läst som pixlar.
- `tests/alunix-r8/review/r2/sv-*` och `mp*-*`, leadens egna `scroll_verify`- och `motion_probe`-körningar.
- `tests/alunix-r8/runs/K3/assets/` och `runs/K4/assets/`, fyra vendorade typsnittsfiler.
- `tests/alunix-r8/runs/K3/plans/` fem fixplaner, `runs/K4/plans/` tre, alla i PLAN-TEMPLATE-format.
- `tests/alunix-r8/PROMPT-R3-V3c.md`, pilbeslutet infört och torrkört.
- `tests/alunix-r8/runs/*/NOTES.md`, leadens R2-rader. `STATUS.md`, cellrader plus ett mätvärdesavsnitt. `QUESTIONS.md`, Q22 och Q23.

Verifierat:
- **Alla tre byggarna avslutade rent den här gången**, till skillnad från runda 1: exit 0, `is_error` false, `.done`. Ingen återupptagning behövdes.
- **Jag läste varje skärmbild själv som pixlar**, och det var pixlarna som avgjorde, inte rapporterna. Två av tre celler har en avvikelse som bara syns i bild.
- **Typsnitten var ovendorade under hela rundan.** Cellerna refererade fyra filer som inte fanns på disk, så varje bild och varje mätning i runda 2, byggarnas egna inräknade, togs mot fallback. Jag upptäckte det när jag kontrollerade arkitektens påstående i stället för att ta det på ord. Jag har vendorat alla fyra, bekräftat i webbläsaren att de laddar, och tagit om bilderna. Det var mitt att göra och det låg kvar sedan runda 1.
- **Jag kontrollerade tre av arkitektens bärande påståenden mot källan** innan jag accepterade domen. Gate 97:s undantagsklausul finns ordagrant i `production-tells.md` och säger det arkitekten citerade. `review-animations` bär `disable-model-invocation: true`, så den kan inte anropas av en modell och ska inte räknas i gapet. Typsnitten var faktiskt ovendorade.
- **Gate 75 är ren i alla tre cellerna**, kontrollerat per kodpunkt över U+2010 till U+2015 och U+2212 efter att kommentarer, `<style>` och `<script>` strippats. Mitt första grep gav falska träffar på rutritningstecken i CSS-kommentarer och dög inte.
- **Noll `gate-deny` i alla tre sessionerna**, alltså noll skalförfattade UI-filer. Regeln jag lade in i R2-prompterna efter runda 1 höll.
- `staircase = 0` i alla tre cellerna. F-014:s utjämning fungerar. Det som fallerar är bildtid.

Öppet:
- V3c klarar F-007 på varje skärm och i signaturakten men går ändå till fixrunda, eftersom `motion_probe` ger max_step 4,12 % mot barens 3 % vid både full och strypt CPU, och PROTOCOL räknar en röd mekanisk grind som ett rundstopp; nästa konkreta steg är att Anton avgör Q22, eftersom arkitekten visar att talet är smoothstepens egen derivata och att baren sattes mot en linjär fixtur.
- K3 stoppas av tre avvikelser i den pinnade akten, alla vid 390 utom utropet `16:9` som kolliderar med snittpilen vid båda bredderna, och nästa konkreta steg är fixrundan med de fem planerna i nummerordning.
- K4 stoppas av att sömmen halverar två ordmärken vid ps = 0 och av att delaren inte är aktens tyngsta objekt mellan ps 0,10 och 0,68, och nästa konkreta steg är fixrundan med de tre planerna, där plan 002 och 003 måste mätas tillsammans eftersom de delar samma funktion.
- Ingen cell klarar rörelsebaren ännu, och alla tal ska tas om i fixrundan eftersom rundan mättes mot fel typsnitt, så nästa konkreta steg är att köra `motion_probe` och `perf_probe` igen först efter att fixrundan lämnat sina filer.
- Route-gapet är nu mätbart och landar på 1 per cell efter rättelse, men mätpunkten behöver en definitionsändring för att vara meningsfull, och nästa konkreta steg är att exkludera routes som bara en människa får starta, annars kan måttet aldrig nå noll.
- Den kvarvarande ettan i gapet är materiell: `copy-gate` kördes inte trots att alla tre cellerna skrev synlig text, och nästa konkreta steg är att fixrundans prompt kräver copy-gaten på de strängar R2 införde, inte bara på R3:s.

Kostnad: V3c 37,89 USD, K3 38,68 USD, K4 36,18 USD, summa 112,75 USD ur `logs/round-2/*.meta.json`. Ackumulerat för r8: 166,58 USD. Higgsfield: noll krediter, noll spenderade.

Nästa steg som bevakaren ska beställa: fixrunda för alla tre cellerna med `run.py build B <cell> --round 3 --resume --prompt-file <fixprompt>`, där K3 och K4 kör sina planer i nummerordning och V3c kör den enda punkten om max_step, och där prompten kräver att typsnitten nu finns och att alla mätvärden tas om.

## 2026-09-10 · Runda 3, hela sidan för V3c och fixrunda för K3 och K4

Gjort:
- `tests/alunix-r8/runs/V3c/index.html`, hela sidan byggd, sju skärmar, låst copy 15 av 15 ordagrant.
- `tests/alunix-r8/runs/{K3,K4}/index.html`, fixrundornas planer utförda, fem respektive tre.
- `tests/alunix-r8/review/r3/`, leadens egna skärmbilder vid 1440, 390 och för V3c även 320, 375, 414 och 768, plus en helsidesfångst och ett femdelat kontaktark.
- `tests/alunix-r8/runs/V3c/reviews/r3/{critic,heuristics,a11y,perf,codex}.md`, fem granskarrapporter, alla genom kontraktskontrollen.
- `tests/alunix-r8/runs/V3c/plans/`, åtta sammanslagna planer. `runs/K3/plans/006`, `runs/K4/plans/004`, arkitektens ersättare.
- `tests/alunix-r8/runs/*/NOTES.md`, leadens R3-rader. `STATUS.md`, cellrader, mätvärden och nästa promptfil per cell.

Verifierat:
- **Alla tre avslutade rent**, exit 0 och `is_error` false, ingen återupptagning.
- **Jag rättade ett fel i min egen R2-rapport innan jag började.** Jag hade skrivit att V3c:s typsnitt var ovendorade och att jag hade vendorat dem. Bägge halvorna var fel för den cellen: V3c hade inga trasiga font-deklarationer, den laddade Geist och Public Sans från Google Fonts, och det jag vendorade var K3:s och K4:s fyra filer. Felet var att jag skrev samma rad till alla tre cellerna utan att kontrollera den per cell. Det verkliga V3c-fyndet var ett annat och står nu i cellens ledger.
- **Mätprotokollet med kontrollfixtur användes genomgående.** Vid full hastighet gav kontrollen noll tappade rutor, så cellernas tal gäller. Vid fyrfaldig strypning gav kontrollen två tappade rutor i två körningar i rad, så maskinen har ett golv där och den nivån används inte som dom. Rått spelhuvudvärde spårades aldrig.
- **Låst copy är 15 av 15 ordagrant i V3c**, kontrollerat per sträng mot renderad text. K3 och K4 saknar tolv respektive tretton, vilket är väntat: båda är fixrundor och bär kvar sina platshållare.
- **Alla fem granskarrapporter klarade kontraktskontrollen** och alla fem säger `fix`. Jag verifierade två bärande fynd själv mot filens rader innan jag slog ihop dem.
- **Noll nekade verktygsanrop i alla tre sessionerna**, alltså noll skalförfattade gränssnittsfiler.

Öppet:
- V3c går till fixrunda med åtta planer, och den tyngsta är att foldens höjdbudget spränger den pinnade scenens klippning under 700 pixlars viewporthöjd så att låst copy försvinner ur dokumentet, vilket också inträffar vid 200 procents zoom; nästa konkreta steg är plan 001 med hela mätmatrisen utskriven före ändring.
- De två levande ramarna tar över hjulet och tabbordningen på två av sju skärmar, vilket gör sidans enda navigationsmedel till en främmande sajts, och nästa konkreta steg är plan 002, som ska bevisa i anteckningarna att ramarna fortfarande lever efter fixen, eftersom de är hela beviset.
- Sidan tappar bildrutor av stilomräkning, mätt till 73 procent av tasktiden, och sex ablationer tog var för sig inte bort den, så nästa konkreta steg är plan 005 som jagar vilken selektor som räknas om per bildruta i stället för att gissa.
- K3 står kvar som blockerad därför att den ritade öppningen fortfarande inte visar något fotografi och Calyx egen navrad överlappar sig själv, och nästa konkreta steg är plan 006, som byter 320 mot samma fasta layoutvyport och statiska skala som K4 redan bevisat i samma runda.
- K4 står kvar som blockerad på ett följdfel arkitekten hittade i sitt eget tidigare steg: etiketten på efter-sidan klipper den låsta bildtexten vid varje bredd under 640, och nästa konkreta steg är plan 004, som binder etikettbredden till delarens läge i stället för till en andel av scenen.
- Prestandabudgeten går inte att klara så länge den mäter de inbäddade exempelsajternas skuld som cellens, och nästa konkreta steg är att lyfta exempelsajternas egen skuld som ett eget spår, eftersom cellernas egen vikt är 334 kilobyte och de inte får redigera sajterna.
- Ett verktyg för kontrastmätning över media ignorerar sitt URL-argument och går mot en fast port, så det är inte kört i den här rundan och nästa konkreta steg är att laga det utanför r8:s rundräkning.

Kostnad: V3c 38,95 USD, K3 28,75 USD, K4 31,72 USD, summa 99,42 USD. Ackumulerat för r8: 266,00 USD. Higgsfield: noll krediter, noll spenderade.

Nästa steg som bevakaren ska beställa: fixrunda för alla tre cellerna. V3c kör `PROMPT-FIX-V3c.md` med planerna 001 till 008 och börjar med steg 3, alltså `review-animations`, `scroll_verify` och `motion_probe` med kontrollprotokollet. K3 kör `PROMPT-FIX-K3.md` med plan 006 inlagd. K4 kör `PROMPT-FIX-K4.md` med plan 004 inlagd.

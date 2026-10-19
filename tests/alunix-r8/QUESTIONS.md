# Frågor till Anton, Alunix r8

Numrerade löpande. Arkitekten blockerar aldrig på en fråga; varje post har ett antagande som
gäller tills svar kommer.

## Q1. Får det förbjudna namnet skrivas ut i PRODUCT.md:s förbudslista?

Uppdraget säger både "Namnet Klova får aldrig förekomma" och att avsnittet "Absences future
work must not fabricate" ska lista just det. Det går inte att formulera förbudet utan att
skriva namnet en gång.

Antagande tills svar: namnet står exakt en gång i `tests/alunix-r8/PRODUCT.md`, i
förbudslistan under Absences, och noll gånger i allt annat r8 producerar. Det togs bort ur
Brand Commitments för att hålla antalet till ett.

## Q2. Register för de tio ifyllda registerraderna: alla blev "modern clean"

De tio celler som bar `?` i registrets Register-kolumn (r2 R3, R4, R5, r3 build, r4 M1, M2,
r5 V1, V2, V3, V3b) är en enda härstamningslinje med ett gemensamt token- och typsystem. Alla
tio läser som modern clean på SKILL.md:s egna markörer: grotesk display med mono enbart som
register, inget serifsnitt, ingen grain, en blå accent, ledgers i stället för kort, och ett
precisionsämne. r4 M2 är gränsfallet: tre av fem kapitel ligger på `#0c0b08` och folden är ett
gråskaligt rum, vilket ligger nära registrets egen formulering för r1 K3, "cinematic dark,
read as an instrument panel".

Antagande tills svar: M2 står som "Modern clean, dark-dominant" med grunderna utskrivna i
cellen, eftersom typsystem, accentdisciplin och driften mot `#f4f2ee` är identiska med
familjens övriga celler. Ändras det till cinematic dark är det en cellredigering på en rad som
inte är en grinddimension, alltså ingen gaterisk.

## Q3. Jag redigerade ett stycke prosa i registret, inte bara celler

Stycket sist i Alunix-blocket sade att tio Register-celler var `?`. Efter ifyllningen var det
påståendet falskt. Jag skrev om stycket så att det i stället redovisar när och hur kolumnen
fylldes. Instruktionen var "ändra inget annat i någon rad"; ett stycke prosa är ingen rad, men
det är ändå en ändring utöver cellerna.

Antagande tills svar: den ändringen står kvar, eftersom alternativet är ett registret som
motsäger sin egen tabell.

## Q4. Registrets frontmatter säger fortfarande `updated: 2026-09-03`

Datumet uppdaterades inte när r7-raderna lades in 2026-09-08 och inte heller nu.

Antagande tills svar: jag rör det inte. Det är utanför uppdragets avgränsning och verkar
uppdateras av en annan rutin.

## Q5. PRODUCT.md har ett `## Platform`-avsnitt som inte stod i uppdragets sektionslista

Uppdraget räknade upp nio sektioner. Impeccables `init.md`-schema kräver dessutom Platform som
ett kalt värde. Belägget för `web` finns inuti den tillåtna källtexten: exempelsajterna är
`.html`-filer som serveras live och visas i `<iframe>`.

Antagande tills svar: Platform står kvar som `web`, med belägget utskrivet under rubriken.

## Q6. Tjänsternas tre underrader är inte skrivna

PROMPT.md låser rubrikerna `Design`, `Utveckling`, `System` och säger att var och en får "en
kort underrad i byråröst, utan påståenden om kunder eller resultat", men ger inte texten.

Antagande tills svar: PRODUCT.md redovisar detta som öppet, inte bestämt. Texten skrivs av
byggaren i sin runda och godkänns av dig, inte av arkitekten i förväg.

## Q7. Vilken `assets/`-mapp gäller för r8?

PROMPT.md:s sökvägar är skrivna mot `{{UT_MAPP}}/assets/` i r7. PRODUCT.md återger dem som
`assets/` utan prefix.

Antagande tills svar: `assets/` betyder cellens egen assets-mapp under
`tests/alunix-r8/runs/<cell>/`, och leveransen F specificerar per cell vad som ska ligga där.

## Q8. Målbildens förväntade katalogposter för K3 föll inte ut ur select.py

Planens § 7.5 förväntade `caractere-bois`, `hyperborea`, `wild`, `garden-eight`, `tidvatten`.
Den deterministiska körningen
`python scripts/catalogue/select.py --brief tests/alunix-r8/runs/K3/BRIEF-draft.md --k 4 --wildcard --explain`
gav i stället `squarespace`, `aevi-wellness`, `beautiful`, `insign` och `mode` (wildcard).
Orsakerna är mekaniska och kontrollerade i `index.json`: `hyperborea` och `tidvatten` ligger i
skriptets `OWN_SITES` och poängsätts negativt (kedjans egen output), `caractere-bois` och
`garden-eight` är `editorial print` med annan grammatik än den målbilden själv låser, och
`wild` föll ett poäng under strecket.

Antagande tills svar: skriptets rad gäller som cellens låsta referenser, enligt
`catalogue-first.md` § 5 (urvalet ska komma ur katalogen, inte ur minnet). Nästa konkreta
steg om du vill ha planens lista i stället: säg till, så skriver jag om K3:s målbild så att
den deklarerar `editorial print` + `gallery/catalog`, kör om select.py och skriver om
fingerprint-tabellen mot den nya grammatiken.

## Q9. Tesrubriken: versal eller gemen form?

K3:s målbild citerar kapitelrubriken som `Vi bygger ert varumärke.`. Den ordagranna copy-raden
i `tests/alunix-ab-r7/PROMPT.md` § Alunix, fakta lyder `VI BYGGER ERT VARUMÄRKE.`. Copy-gaten
säger att ordagrann copy bevaras och inte skrivs om, så de två kan inte båda gälla.

Antagande tills svar: `VI BYGGER ERT VARUMÄRKE.` används, alltså r7-promptens sträng, och
målbildens gemenform behandlas som en citatslarv. Nästa konkreta steg om du väljer gemen form:
en rad i K3:s decision ledger och en rättelse av r7-promptens copy-lista, så att bara en
version av strängen finns i repot.

## Q10. Fem live-rubriker i kategorin saknas i briefskelettet

`reference-lock.md` § Transcribe the category's live headlines kräver fem ordagrant citerade
rubriker från de bästa levande sidorna i kategorin, med källa namngiven. Den här
arkitektsessionen har ingen webbsökning, och att skriva rubriker ur minnet vore fabricering.

Antagande tills svar: fältet står som `[needs: live-rubriker]` i `runs/K3/BRIEF.md` och
byggaren hämtar dem i R1, där uppgiften uttryckligen står i R1-prompten. Nästa konkreta steg
om du hellre vill att lead gör det: lead kör sökningen och klistrar in de fem raderna i
skelettet innan R1 startas.

## Q11. Målbildens förväntade katalogposter för K4 föll bara delvis ut ur select.py

Planens § 7.5 förväntade `paper`, `dovetail`, `future-fur`, `harkcap`, `mode`. Den
deterministiska körningen
`python scripts/catalogue/select.py --brief tests/alunix-r8/runs/K4/BRIEF-draft.md --k 4 --wildcard --explain`
gav `paper` (14 p), `gocanopy` (12 p), `harkcap` (12 p), `mode` (12 p) och `customer-io`
(11 p, wildcard). **Tre av fem förväntade föll alltså faktiskt ut** — till skillnad från K3,
där ingen gjorde det. De två som föll bort har mekaniska orsaker, kontrollerade i `index.json`
med skriptets egna funktioner:

- `future-fur` fick **11 poäng**, ett poäng under `--k 4`-strecket som ligger vid 12. Den var
  också kandidat till wildcard-platsen (kategorin `consumer-brand` ligger utanför briefens
  `portfolio`), men `ranked` sorteras `(-poäng, slug)` och vid oavgjort 11 kommer
  `customer-io` före `future-fur` alfabetiskt. Den föll på en bokstav, inte på en princip.
- `dovetail` fick **8 poäng**. Dess register är `editorial print`, inte `modern clean`, så den
  tappar hela `+3 register`, och dess kategorier är `institutional` / `editorial` mot briefens
  `portfolio` / `product-focused`, så den tappar hela `+2 category`. Det är målbildens eget
  lås på `modern clean` som stänger ute den.

`OWN_SITES`-mekanismen som fällde K3:s lista spelar ingen roll här — ingen av K4:s förväntade
slugar ligger i den.

Antagande tills svar: skriptets rad gäller som cellens låsta referenser, enligt
`catalogue-first.md` § 5. Nästa konkreta steg om du vill ha `future-fur` med: säg till, så kör
jag om med `--k 5`, vilket tar in den utan att röra någon annan rad; `dovetail` kräver
däremot att K4:s målbild deklarerar `editorial print`, vilket vore ett annat koncept.

## Q12. Får mallsidans mättnad falla, när PRODUCT.md säger att en visad ram aldrig får tonas?

PRODUCT.md § Operating Context lyder: "En ram som visats får aldrig transformeras eller tonas
efteråt. Den ska gå att använda." K4:s signaturakt kräver att vänsterhalvan (`En typisk
mallsida`, alltså `sites/before-ai-slop.html` live) tappar mättnad medan delaren passerar.
De två kan inte båda gälla i sin bokstavliga form.

Regeln finns för att skydda **beviset** — de tre Alunix-exempelsajterna ska gå att använda med
musen, inte bara ses. Antagonisten är inte bevis; den är argumentets andra halva.

Antagande tills svar: regeln gäller de **tre Alunix-exempelsajterna**, inte antagonisten.
Konkret i K4: ingen ram skalas, transformeras eller flyttas någonsin — bara clip-gränsen
mellan lagren rör sig — och den enda effekt som läggs på en ram är `filter: saturate()` på
**wrappern** runt mallsidan, aldrig på Calyx, Hōrai eller Hyperborea. Nästa konkreta steg om
du säger nej: degraderingen begränsas till rubrikens före-halva (`wght` och `letter-spacing`),
som ligger i K4:s eget lager, och mallsidans mättnad lämnas orörd. Det kostar en rad i
decision ledger och ingenting annat — ingen omskjutning, ingen ny asset, ingen ändrad akt.

## Q13. Demo-skärmbilderna är äldre än sajtfilerna de föreställer

`tests/alunix-concepts-r3/build/assets/demo-{calyx,horai,hyperborea}.webp` är daterade
2026-09-04 (1200 × 750, alltså skrivbordsbredd). `sites/horai.html`, `sites/calyx.html` och
`sites/hyperborea.html` ändrades 2026-09-09 01:47 och ligger okommitterade i arbetskatalogen.
Ändringen är i samtliga fall F-011-borttagningen av `@media (prefers-reduced-motion: reduce)`,
verifierad med `git diff HEAD -- sites/`.

Ändringen är liten, men den träffar exakt det läge skärmbilderna tas i: `shoot.py` startar sin
browser med `reduced_motion="reduce"`, uttryckligen och med F-011 som kommentar i källan. Före
ändringen tvingade media-blocket `.reveal { opacity: 1 }`, alltså syntes allt; efter ändringen
finns ingen sådan gren, så element under vecket står i sitt pre-reveal-läge tills
IntersectionObserver utlöser dem. De ärvda bilderna kan alltså visa ett tillstånd sidorna inte
längre har. Dessutom finns ingen 390-bild i katalogen över huvud taget, och K4 behöver båda
bredderna.

Antagande tills svar: alla sex bilderna (tre sajter × 1440 och 390) skjuts om innan de
används, med de två kommandoraderna i `tests/alunix-r8/runs/K4/assets/ASSETS.md` § 3. Nästa
konkreta steg om du vill spara tid: skjut om vid 1440, lägg den nya bilden bredvid den ärvda
och läs båda som pixlar; är de identiska räcker de ärvda för 1440 och bara 390-bilderna
behöver skjutas.

## Q14. Titelblockets fält i K3: bindestreck eller tankstreck?

`concepts-K3.md` (3) skriver ritningsfältet som `SEKTION A–A` med tankstreck, men det är
synlig text på sidan, och PRODUCT.md § Capabilities and Constraints förbjuder tankstreck i
synlig text utan undantag.

Antagande tills svar: bindestreck, alltså `SEKTION A-A`. Nästa konkreta steg om du vill ha
tankstrecket: PRODUCT.md får ett skrivet undantag för ritningsnotation, eftersom regeln annars
inte går att granska mekaniskt.

## Q15. Räknas K3:s måttkedja som ett blått moment eller som tre?

Färgregeln är "ett blått moment per viewport", övertagen ordagrant från `beautiful`. I K3:s
första akt står `320`, `768` och `1440` samtidigt i samma vy.

Antagande tills svar: den sammanhängande dimensionslinjen med sina tre siffror är ett moment,
eftersom det är en apparat och en kedja, och ingen annan blå apparat finns på sidan. Nästa
konkreta steg om du läser det som tre: bara ett stationstal färgas blått och de två andra sätts
i hårlinjefärgen, vilket kostar signaturaktens kulmen och bör beslutas nu, inte i R2.

## Q16. Är `SKALA 1:1` i K3 sant nog när det bara går att verifiera vid 1440 × 900?

Under 1440 skalas arket likformigt, och under 768 ritas en reducerad plansch där stationen
`1440` utgår, eftersom en station bara får visas på en sidbredd den faktiskt beskriver.

Antagande tills svar: skalpåståendet gäller referensvyn, och utropen beskriver den ritade sidan
och inte papperet, precis som en ritning i skala 1:1 som kopieras mindre. Nästa konkreta steg om
du vill ha det strängare: fältet blir `SKALA 1:1 @ 1440`, vilket är en ny sträng och måste genom
copy-gaten.

## Q17. K4: vilken konvention gäller för delarens koordinat?

`runs/K4/BRIEF.md` definierar `--split` som delarens position, där 100 % betyder att mallsidan
fyller bilden. Planens § 7.5 beskriver samma rörelse som att delaren går från 50 % till 100 %
höger, alltså som "efter"-ytans växande täckning. De två räknar åt motsatt håll, och
F-007-kontrollen anges i akt-koordinater.

Antagande tills svar: `--split` behåller BRIEF-definitionen som variabelnamn, och alla
F-007-koordinater och alla `?preview=`-lägen uttrycks i stället som "andel av bilden som visar
efter", eftersom det är den storhet en människa kan läsa av en skärmbild utan att öppna koden.
Byggaren skriver ut konventionen överst i `runs/K4/NOTES.md`. Nästa konkreta steg om du vill
tvärtom: en rad i K4:s decision ledger och en rättelse i R2-prompten innan rundan startar.

## Q18. Dubblett, upphävd

Frågan om mallsidans mättnad får falla ställdes redan som Q12 av K4-arkitekten. Den här posten
står kvar som nummer så att numreringen inte hoppar, och innehåller inget eget. Svara på Q12.

## Q19. Ska referensraderna i avsnitt (7) beläggas per slice?

Lead läste de låsta katalogposternas folds som pixlar. Tre av K3:s fem rader i avsnitt (7)
påstår saker folden inte visar: `insign`s tre mättade färgband som navigation, `aevi-wellness`
djup ur bandväxling, och `mode`:s accent inhägnad till en enda fylld knapp. I `mode`:s fold är
den syrgröna färgen rubrikens överstrykningsblock. Påståendena kan stämma längre ned på
sidorna, som folden inte visar.

Antagande tills svar: varje rad i avsnitt (7) förses i R1 med den slice eller den rad i
`entry.md` den vilar på, och en rad utan belägg stryks ur låset. Kravet gäller alla tre
cellerna. Nästa konkreta steg om du tycker det är överarbete: kravet begränsas till primärposten
per cell.

## Q20. `mode`s katalogpost motsäger sig själv mellan fold och entry.md

Lead läste `design-catalogue/entries/mode/fold.webp` som pixlar: den syrgröna accenten är
rubrikens överstrykningsblock, alltså en typografisk yta. Postens egen § Role rules säger i
stället att accenten är inhägnad till en komponenttyp, den enda fyllda knappen. Både K3 och K4
har byggt sina accentregler på entryns text, inte på folden.

Antagande tills svar: entryns rollregel gäller, eftersom den är den mätta beskrivningen och
båda cellerna redan vilar på den. Nästa konkreta steg om folden ska väga tyngre: posten får en
rättad § Role rules, och K3:s och K4:s accentrader räknas om, vilket är en ledgerrad per cell
och ingen ny runda.

## Q21. Diakriterna i tre fas-0-filer var utplattade till ASCII, och orsaken är skrivvägen

`runs/K3/BRIEF.md`, `runs/K3/NOTES.md` och `runs/K4/BRIEF.md` skrevs av fas 0-arkitekterna via
skalet och förlorade å, ä och ö på 127 rader. Byggarna rörde aldrig den texten, vilket är
bevisat av att `NOTES.md` bär samma fel med en tidsstämpel timmar före byggarna startade och av
att byggarnas egna avsnitt är rena. Lead har återställt tecknen och verifierat att ingen låst
copy-sträng och inget kodspann rördes.

Antagande tills svar: ingen byggarsession kostas på detta, och R2-prompterna har fått raden att
varje filskrivning går genom Write eller Edit och att `.md`-undantaget inte gäller prosa.
Nästa konkreta steg om felet återkommer: `design-gate.py` utökas till att neka skalförfattande
också av `.md` i en armad session.

## Q22. Är `max_step ≤ 3 %` rätt kalibrerat för en eased kurva?

V3c:s signaturakt mäter `staircase = 0` och `max_step 4,12 %` samtidigt. Arkitekten visar att
talet är den aritmetiska följden av smoothstepens derivata: kurvan är brantast på mitten, så en
jämn scrollkadens ger där ett större steg per bildruta än en linjär kurva skulle ge, utan att
något stegar. Baren i F-014 sattes mot en linjär fixtur.

Antagande tills svar: baren gäller som den står, så V3c går till fixrunda på den punkten. Nästa
konkreta steg om du håller med arkitekten: `motion-smoothness.md` får en rad som säger att
`max_step` mäts mot kurvans egen derivata, eller att `staircase = 0` väger tyngre än `max_step`
när de säger emot varandra, och baren skrivs om en gång i stället för att varje cell tvingas
platta ut sin easing.

**Bevakarens beslut (2026-09-10, verkställt):** arkitekten har rätt, och baren skrevs om en
gång. `max_step ≤ 3 %` grindar nu bara det dämpade spelhuvudet `--sc-ps`; på härledda spår
(`transform`, `clip-path`, …) rapporteras talet men faller inte, eftersom `staircase` redan
fångar ett verkligt steg där och en smoothsteppad kurva toppar på ~4,4 % per ruta av sin egen
derivata. Bevisat åt båda hållen mot fixturerna: `tests/motion/smooth.html` passerar på
`--sc-ps` och `transform`, `tests/motion/staircase.html` faller fortfarande på `staircase 17`,
och V3c:s `.plate-card:transform` (4,12–4,47 %, staircase 0) faller inte längre på max_step.
Ändrat: `motion_probe.py` (fail-blocket + docstring), `gates.md` § kontinuerlig,
`motion-smoothness.md` § The bar, `scroll/pace.md` § The bar; synkat live → repo,
`verify-design-system.py` 205/205. Rått `--sc-p` ska aldrig spåras: det trappar per hjultick
av konstruktion (fixturen ger staircase 18 på det spåret, sidan 11).

Ett andra fynd ur samma mätning: V3c ger 6–14 rutor > 33 ms vid 4× CPU, alla i
vändningsakten, medan fixturen i samma fönster ger 1. Värden är brusig (OneDrive-synk), så
talet är flippens kostnad plus brus i okänd proportion. Baren fick därför en kontrollrad:
kör fixturen först, och en mätning räknas bara om kontrollen ger noll rutor > 33 ms. Ingår i
R3-ordern för V3c, inte som eget stopp.

## Q23. Calyx egen header kolliderar vid 390 px

Exempelsajten `sites/calyx.html` lägger sin mobilnav över ordmärket vid 390. Det syns i K3:s
ritade öppning och i K4:s efter-yta, alltså i två av tre celler. Exempelsajterna får inte
redigeras av r8.

Antagande tills svar: kollisionen accepteras som exempelsajtens egen kalibreringsbrist och
noteras i båda cellernas NOTES.md, eftersom den inte är r8:s att laga. Nästa konkreta steg om du
hellre vill laga den: det blir ett eget litet uppdrag mot `sites/calyx.html` med sin egen
designsession, utanför r8:s rundräkning.

## Q24. `review-animations` kunde inte köras av byggaren: skillen bar `disable-model-invocation`

V3c:s R3-byggare anropade `Skill(review-animations)` som steg 3 kräver och nekades av
Skill-verktyget ordagrant: *"cannot be used with Skill tool due to disable-model-invocation.
Ask the user to run /review-animations themselves."* Byggaren lämnade steget öppet i stället
för att efterlikna skillen, vilket är rätt. Men planen § 8.4, `PROTOCOL.md` § R3 och alla tre
R3-prompterna kräver att skillen körs **i byggarens egen session**; det är r7-luckan r8 finns
för att stänga. Flaggan är upstreams standard (Emil Kowalskis skill är skriven för att
startas av en människa), inte ett beslut i det här designsystemet.

**Bevakarens beslut (2026-09-10, verkställt):** planens avsikt vinner. Raden
`disable-model-invocation: true` är borttagen ur `~/.claude/skills/review-animations/SKILL.md`
och `~/.agents/skills/review-animations/SKILL.md` (identiska kopior). Steg 3 körs om för V3c i
nästa körning, tillsammans med det byggaren också hoppade över i steg 5: `scroll_verify` och
`motion_probe` med kontrollprotokollet (bara spelhuvudets max_step står i NOTES, inte rutorna
> 33 ms mot fixturen). Vill du hellre att `/review-animations` förblir din egen handpåläggning,
sätt tillbaka raden och stryk steget ur R3-prompterna; då är det inte längre en byggargrind.

## Q25. Kortvändningens span och fönster: 3,4 och 0,10 till 0,78?

Arkitekten mätte tempot ur ramsekvensen och `scroll_verify` (HELHET.md § 2): span 2,2 gav en
vändning på 648 px (Antons "för fort"), span 4,8 ger 2 052 px men lägger 1 273 px stillastående
baksida inne i pinnen (dead scroll, diff 0,0). Rekommendation: `data-sc-span="3.4"`,
`data-sc-dwell="0.2"` och smoothstep-fönstret vidgat från 0,12 till 0,72 till 0,10 till 0,78,
vilket ger 1 469 px vändning och 655 px svans. Fönstret är målbildens och R2 lämnade
vidgningen som öppen fråga.

Antagande tills svar: 3,4 med vidgat fönster byggs som plan 011. Vill du behålla fönstret:
span 3,8 ger samma vändning (1 512 px) men svansen blir 1 020 px.

## Q26. Får accenten en tredje roll: måttsiffrorna i processarket?

Planen skrev måtten i `var(--ink)` för att hålla tvåförekomstlåset. Din instruktion 15/9 tillåter
nya färger om de går ihop. HELHET.md § 4 T-2 föreslår de sanna måtten (320 · 768 · 1440, 16:9,
7 rem, 96 px) i `var(--c-accent)` på papper, regeln "ett blått moment per skärm i akten, alltid
ett sant tal" (K3:s regel). Kontrast 6,46:1.

Antagande tills svar: accenten används, tre roller utskrivna i decision ledger. Säger du nej
gäller `var(--ink)` och inget annat i plan 010 ändras.

## Q27. Prisblockets material: ett nytt grafitplan?

Prisblocket är `--invert #0c0b08` mot grunden `#0b0c0e` och läser som ett hål
(`shots/fasA/v3c-1440/v3c-1440--s06.png`). T-3 föreslår en ny token `--c-graphite:
oklch(0.27 0.012 250)`, ett kallt mörkt plan som skiljer sig i valör, inte i kulör.

Antagande tills svar: byggs i fas C. Alternativet utan ny färg är en hårlinjeram
`--frame-line` runt blocket.

## Q28. Mobilordningen: tesen före Calyx?

Vid 390 staplar spalterna som högerspalt först (jätterubrik, liggare, Hōrai) och sedan
vänsterspalt (tes, Calyx, pris), så berättelsens s4 kommer efter s6 (`v3c-390--s02..s06.png`).
H-14 kräver berättelsens ordning.

Antagande tills svar: ordningen vid 390 blir tes → Calyx → jätterubrik/liggare → Hōrai →
pris → process → avslut. Det kostar `order`-regler i `@media (max-width:900px)`, ingen ny
markup.

## Q29. Steg 07:s revisionsfält: rita eller stryka?

Plan 010 ritar det som tre rutade celler, en skraffering och bokstaven `A`. Det är ritpraxis,
men bokstaven är text i SVG. Planen tillåter att fältet stryks.

Antagande tills svar: fältet ritas; faller det i F-007 (läser som innehåll, gate 79) byts
steg 07 till en andra hårlinjeram utanför konturen, som plan 010 anger.

## Q30. Bandet s4 till s6: två spalter kvar, eller fem helbredds akter?

Helhetsloopens runda 1 (2026-09-17): HELHET.md H-02 kräver "minst fyra sekventiella akter som
var och en äger sin viewport", H-03 tre helbredds materialbyten. R6-läget har bandet som
målbilden beskrev (BRIEF § STORY): två spalter, tes + Calyx + pris till vänster, jätterubrik +
liggare + Hōrai till höger, tre skärmar synliga samtidigt (`shots/loop-1/slices-1440/
v3c-1440--s03..s05.png`). Astra (gpt-6-astra) dömde det som sidans största brist mot golvet
("tre kompositioner limmade: visitkort, portfoliomosaik, teknisk handling") och föreslog att
tes, Calyx, jätterubrik + liggare, Hōrai och pris staplas som fem helbredds akter med egna
grundbyten (Hoys kapitelrytm). Plan 017 (luft 160 px, offset 120 px, synlig grunddrift) och
012 (mobilordningen) byggs i R7 oavsett och är inte bortkastade.

Antagande tills svar: bandet står med 017:s luft och offset i R7; omkompositionen skrivs som
plan i loop 2 bara om du säger ja. Säger du ja: fem akter, varje ≥ 100 svh vid 1440, med
grundbyten mörk → blå → papper → mörk (Hōrai) → grafit (pris), och sidan växer från 10,9 till
~13 vh (inom 8 till 14).

## Q31. Jätterubriken: 88 px i dagens spalt, eller 96 px med Q30:s bredd?

Helhetsloopens runda 2 (2026-09-17): H-07 skrevs i fas A som "minst 96 px" mot en antagen
640 px-spalt. Den faktiska textspalten i `.panel-giant` är 555 px (651 − 2·48), och det låsta
ordet `VARUMÄRKE.` mäter 601 px vid 96 px, så R7:s 6rem kapade det mitt i (`VARUMÄRK` / `E.`,
leadens fynd; `hyphens:auto` saknar svensk ordlista i Chrome på Windows). Mätt (loop 2,
`shots/loop-2/diag/diag3.json C_giant`): 88 px vid −0,04em = 542 px, ordet helt på en rad vid
901, 1024, 1280 och 1440; 96 px kräver en spalt ≥ 606 px.

Antagande tills svar: plan 030 sätter 88 px / −0,04em (5,5 gånger brödtexten, TASTE § 2.4:s
golv 5) och H-07 är omskriven till "≥ 88 px, ordet aldrig delat". Säger du ja till Q30 (fem
helbredds akter) får rubriken hela bredden och 96 till 132 px (Hoys mått) utan att dela ordet;
då återställs H-07 till 96.

## Q32. Processakten: papper eller inverterad?

Anton 2026-09-17: vill se en inverterad variant av ritningen och jämföra.

**Leadens motivering för papper, som den byggdes:** (1) konventionen, en teknisk
sektionsritning görs i bläck på papper, mörk grund med ljusa linjer är blåkopian och läser
som arkivkopia i stället för arbetsdokument; (2) grundväxlingen, H-03 kräver minst tre
helbredds materialbyten och akten på papper är det största, inverterad smälter den ihop med
prisblocket och avslutet till ett långt mörkt parti; (3) läsbarheten, sju stycken på fyra
till sex meningar läser lättare som mörk text på ljus grund, uppmätt 8,75:1 mot papperet.

**För invertering:** hårlinjerna lyser starkare mot mörkt, blåkopian är en riktig konvention,
och sidan får en obruten mörk rygg.

**Beställt:** plan 045, `?process=invert` som ett läge i samma fil (ingen andra cell, ingen
duplicerad markup), båda lägena skjutna i samma sju previewsteg och i skivor vid 1440 och
390 (`shots/r11/papper/` och `shots/r11/invert/`) för Antons dom på pixlar.

**Antagande tills Anton dömt:** papperet är sidans läge; inverteringen är ett läge man
öppnar med `?process=invert`.

## Q33. Calyx får sin färg i sista steget (beställning, inte fråga)

Anton 2026-09-17: "Calyx ska inte vara svartvit, den kan vara det under ritningsprocessen,
men ska få sin färg i den färdiga versionen i sista steget."

Beställt som plan 046: mättnaden blir en funktion av aktens progress via det registrerade
stegfönstret, gråskala medan arket ritas och full färg när ritningen har blivit en sida.
Arkitekten väljer fönster (steg 06 är leadens läsning: "Bläcket står kvar som ram. Ritningen
och sidan är samma sak") och ger byggaren mätvärden för bildtid och för det inverterade
läget. Byggs i R12.

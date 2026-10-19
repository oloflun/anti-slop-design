# NOTES — Alunix r8, cell K4 · Före/Efter

En rad per beslut: datum, beslut, källa. Skriven av arkitekten. Byggaren lägger till rader
under sin egen rubrik i R1 och skriver aldrig om en rad ovanför.

---

## Arkitektens beslut, 2026-09-09/10

| Datum | Beslut | Källa |
|---|---|---|
| 2026-09-09 | **`sweep_raw.py` kördes om innan urvalet och var rent (0 ignorerade, EXIT=0).** | Planens § 4.1, katalog-först |
| 2026-09-09 | **Cellens låsta referenser är `select.py`s faktiska rad: `paper`, `gocanopy`, `harkcap`, `mode`, `customer-io` (wildcard).** Inte målbildens förväntade lista. | `catalogue-first.md` § 5 — urvalet ska komma ur katalogen, inte ur minnet |
| 2026-09-09 | **Tre av målbildens fem förväntade slugar föll faktiskt ut:** `paper` (14 p, högst i katalogen), `harkcap` (12 p), `mode` (12 p). Två föll bort och skälen är mekaniskt kontrollerade i `index.json`: **`future-fur`** fick 11 p, ett poäng under `--k 4`-strecket vid 12, och förlorade wildcard-platsen till `customer-io` på en alfabetisk tiebreak vid samma poäng (`ranked.sort(key=lambda r: (-r[0], r[1].get("slug","")))`); **`dovetail`** fick 8 p därför att dess register är `editorial print` (tappar `+3 register`) och dess kategorier `institutional`/`editorial` (tappar `+2 category`) mot briefens `modern clean` + `portfolio`/`product-focused` — alltså stängde målbildens eget lås ute den. | `scripts/catalogue/select.py`, funktionerna `score()` och `main()`; poängen körda med skriptets egna funktioner, inte uppskattade. **Q11** |
| 2026-09-09 | **K4:s papper är varmt:** `--paper` `oklch(0.957 0.013 85)`, med `--paper-2` `oklch(0.928 0.018 78)`, `--ink` `oklch(0.26 0.021 62)`, `--ink-2` `oklch(0.62 0.014 70)` och `--hair` `oklch(0.80 0.010 78)`. Hue 85 mot K3:s hue 230 är 145° isär vid samma låga chroma, och ingen av dem är kräm. Bläcket är också varmt, så att ett kallt nästan-svart aldrig läggs på ett varmt ark. | Lead-lås 2026-09-09 (K3 har låst kallt `oklch(0.95 0.012 230)`; de två nya cellerna får inte dela temperatur) + `paper`-postens kanvasprincip + AB09-lärdomen om kräm |
| 2026-09-09 | **Accenten är `#1E5E9C` = `oklch(0.47 0.13 252)`, och den finns på ett enda objekt: delaren.** Aldrig text, aldrig länk, aldrig ram, aldrig ett tal, aldrig en yta. Regeln är formulerad som *ett objekt som existerar exakt en gång*, inte som *en komponenttyp*, eftersom en komponenttyp kan förökas. | `mode` § What to borrow (inhägnad till en komponenttyp), skärpt ett steg; `paper` § Role rules (blått aldrig på knapp, länk eller stor text); TASTE § 4.4 |
| 2026-09-09 | **Typsnittsvalet: Switzer (röst) + Reddit Mono (register).** Rollerna korsar aldrig. Reserv om Fontshare-vendoringen faller: **Onest** (Google Fonts, samma `wght`-axel 100–900). Motiveringen enligt `brand.md`s fyra steg står i `concepts-K4.md` § (6): tvåtonsdevicen kräver ett snitt utan egen händelse på raden, och degraderingen `wght` 500 → 200 kräver en lång viktaxel. | `brand.md` fyra steg; TASTE § 4.2 (två snitt, mono bara register) |
| 2026-09-09 | **Kontrollerat mekaniskt att Switzer och Reddit Mono är obrukade:** `grep -rohiE "family=[A-Za-z+0-9]+" tests/alunix-*/ --include=*.html | sort -u` ger exakt de 21 snitt r1–r7 laddat, och ingen cell länkar till Fontshare över huvud taget. Varken Switzer, Onest, Host Grotesk, Satoshi, Anek Latin, Reddit Mono, Red Hat Mono, Azeret Mono, Sometype Mono eller Sono finns i listan. | Egen körning; lead-instruktionens förbudslista |
| 2026-09-09 | **K3:s reservkedja rörs inte.** K4 väljer varken Chivo eller Martian Mono, och inte heller något av K3:s fyra reservval per roll (General Sans, Sora, Anybody, Darker Grotesque / Chivo Mono, Spline Sans Mono, Azeret Mono, Sometype Mono). K3:s egen krockregel utlöses därmed inte. Skulle lead flytta K4 till dess tredje eller fjärde monoval (Azeret Mono, Sometype Mono) trampar K4 in i K3:s reserver och båda cellernas ledger måste få en rad. | `concepts-K3.md` § (6) § Krock-hantering |
| 2026-09-09 | **Ingen generering. Noll genererat material, ingen asset-lock för en genererad bild, ingen bildprompt.** Två sammanfallande skäl, i den här ordningen. **(1) Principiellt, och det är det bärande:** cellens hela argument är att allt som visas är verkligt och mätbart, så en genererad bild vore ett påhittat objekt i en sida vars tes är att den inte hittar på något; material som letar efter en användning är inte tillåtet. **(2) Praktiskt:** Higgsfield är ute — lead mätte `balance` = `{"credits":0,"subscription_plan_type":"free"}` och en enda privat workspace på free plan 2026-09-09, så steg 1 och 2 i planens § 10.6 faller. **Skäl (2) ändrade ingenting i K4**, eftersom skäl (1) redan uteslöt generering innan krediterna räknades. | Planens § 10.6 fallback steg 3; F-009; `assets/credits.json` `generated_material.present: false` |
| 2026-09-09 | **Hōrai och Hyperborea visas som skärmbilder, inte som ytterligare live-ramar.** Calyx förblir live. | Målbilden kallar dem "full-bleed **objekt**", inte ramar; `performance.md` § 1 (fyra samtidiga iframes ryms inte i 2,5 MB); PRODUCT.md princip 1 är uppfylld så länge minst ett bevis är levande och användbart |
| 2026-09-09 | **De ärvda demo-skärmbilderna räcker inte och skjuts om, alla sex (tre sajter × 1440 och 390).** Två oberoende skäl: de är daterade 2026-09-04 medan sajtfilerna ändrades 2026-09-09 01:47 (F-011-borttagningen av `prefers-reduced-motion`-blocken, verifierad med `git diff HEAD`), och `shoot.py` skjuter med `reduced_motion="reduce"`, alltså exakt det läge ändringen träffar; och det finns ingen 390-bild i katalogen över huvud taget. | Egen `ls`, `PIL`-läsning och `git diff`; `shoot.py` källkod. **Q13** |
| 2026-09-09 | **`shoot.py` och `shoot_slices.py` har `WIDTH = 1440` hårdkodat och tar ingen breddflagga** (kontrollerat i källan). 390-bilderna kan därför inte skjutas med dem; `ASSETS.md` § 3 innehåller en inline-Playwright-körning med samma `reduced_motion="reduce"` i stället. | Egen läsning av `~/.claude/skills/design/scripts/shoot.py` |

## Plan-avvikelser fingerprint-gaten eller en regel tvingade fram

Gaten **föll aldrig under 4/6**. Lägsta summa mot registrets 36 byggrader är **5/6**, mot
r1 K2 Tjänsteledger, r2 R5 Konsolram och r3 build, och den delade dimensionen är i alla tre
fallen *grammatik*, som målbilden själv låser. Mot K3 klarar K4 alla sex dimensioner plus de
två extra (temperatur, typsnitt), alltså 8/8.

Ingen av ändringarna nedan tvingades alltså fram av gaten. Varje rad har en annan källa.

| Datum | Ändring mot målbildens text | Källa och skäl |
|---|---|---|
| 2026-09-09 | **`pan` ströks.** Min första aktplan lade Hōrai och Hyperborea i en vågrät `pan`-akt som en fortsättning på delarens axel. Ersatt av `flow` + `in` med stagger 90 ms. | `scroll/grammars.md`, raden **Split stage**, kolumnen *Bans*: `pan`, `spotlight`, `magnet`, > 1 `scrub`, `drift`. Målbilden namnger ingen familj för den akten, så ingen låst rad bryts |
| 2026-09-09 | **Målbildens andra `flow` (paketen) blev `count`.** Målbilden skriver `flow` (liggaren) följt av `flow` (paketen), alltså samma familj två gånger i rad. Aktordningen är nu `pin → reveal → flow+in → kinetic → count → reveal`. | `devices.md` § device kit, "never the same one twice running"; `devices.md` § 7, en count kräver verifierade tal — `26 900` och `38 900` är sanna, och `Pris vid förfrågan` räknar inte utan skrivs. `count` är dessutom en av split stages tre egna lutningar ("real `count`") |
| 2026-09-09 | **`VI BYGGER ERT VARUMÄRKE.` fick en plats som a2:s löphuvud.** Målbildens aktlista för K4 nämner den aldrig, men strängen står i PRODUCT.md:s låsta copy-lista. Den får ingen egen akt. | Copy-gate (ordagrann copy bevaras) + PRODUCT.md § Brand Commitments + `feel-and-fingerprint.md` § The peak, "a page with three peaks has none". Versalformen enligt lead och **Q9** |
| 2026-09-09 | **`dwell` sattes till 0,22, inte K3:s 0,35.** | `feel-and-fingerprint.md` § Pacing och F-002. K3:s pin öppnar med ett medvetet tomt ark; K4:s fold är full av innehåll vid ps = 0 och behöver bara en kort stillhet, inte en tystnad |
| 2026-09-09 | **Skärmlistan växte från målbildens 6 till 9.** Den pinnade akten delades i tre granskningsbara vyer och tjänsteliggaren fick en egen skärm. | F-007: målbildskontrollen körs skärm för skärm, så varje vy som ska skärmbildas måste finnas i listan |
| 2026-09-09 | **Skillnadsraden `hårlinjer` ströks ur liggaren.** Målbilden räknar upp den, men `measure.py` ger `hairlineRules` **12 för mallsidan och 10 för Calyx**, alltså tvärtemot vad målbilden antar. Ersatt av `Sidmarginal vid 1440` (0 px mot 32 px, ur `contentWidthUsed` 1440 mot 1376) som reservrad. Raden får inte återinföras och får inte vändas till en fördel med en annan tolkning. | TASTE § 4.9, siffror får vara textur bara om de är sanna; lead-instruktionens "sanna, mätta skillnader bara" |
| 2026-09-09 | **Två live-iframes är budgetens svåraste post och fick en egen beslutsregel.** `before-ai-slop.html` är 9 016 B med noll bilder; `calyx.html` är 16 238 B men hämtar själv fyra externa Unsplash-fotografier vid `w=1600/1600/2000/2400` som K4 inte kan påverka. Regeln: **om `perf_probe` visar över 2,5 MB degraderas vänsterramen till en skärmbild och högerramen förblir live, aldrig tvärtom.** LCP-elementet är K4:s egen rubrik, aldrig en ram. | `performance.md` § 1; PRODUCT.md princip 1, beviset ska gå att använda; antagonisten är inte bevis |
| 2026-09-09 | **Mallsidans degradering görs som `filter: saturate()` på wrappern, aldrig som transform, scale eller opacity på ramen**, och regeln "en visad ram får aldrig transformeras eller tonas" tolkas som gällande de tre Alunix-exempelsajterna, inte antagonisten. | PRODUCT.md § Operating Context, snävad. **Q12** — antagandet gäller tills Anton svarar, och nästa steg om han säger nej står i `assets/credits.json` § open |
| 2026-09-09 | **Fältet "Reduced motion-planen" finns inte i K4:s skelett.** Ingen `prefers-reduced-motion`-gren, inget statiskt reservläge. | F-011, rörelsen spelas alltid. Fältet är pensionerat ur r7-briefen |
| 2026-09-10 | **De fem live-rubrikerna hämtades och står ordagrant i `BRIEF.md`**, alltså inte som `[needs: live-rubriker]` som i K3. H1 hämtad per sida 2026-09-10 från frojd.se, ead.se, sitea.se, norrlandswebbyra.se och digitalwebbyra.se/webbdesign. | `reference-lock.md` § Transcribe the category's live headlines |

## Kontroller jag körde själv, med utfall

| Kontroll | Kommando | Utfall |
|---|---|---|
| Katalogsvepet rent | `python scripts/catalogue/sweep_raw.py` | `sweep: rent - varje kalla under raw/ och processed/ har en post (0 ignorerade).` EXIT=0 |
| Urvalet deterministiskt | `python scripts/catalogue/select.py --brief tests/alunix-r8/runs/K4/BRIEF-draft.md --k 4 --wildcard --explain` | `paper, gocanopy, harkcap, mode, customer-io`; hela utdatan ordagrant i `concepts-K4.md` |
| De två filerna serveras | `serve.py --port 3399 --root .` + `curl -w "%{http_code}"` | `200` för både `/sites/calyx.html` och `/sites/before-ai-slop.html` |
| Mallsidan mätt | `measure.py http://localhost:3399/sites/before-ai-slop.html` | `distinctTextColors` 9 · `distinctWeights` 4 · `fontSizeRange` [12, 60] · `distinctBackgrounds` 8 · `hairlineRules` 12 · `contentWidthUsed` 1440 · `families` `{"Inter": 61}` |
| Calyx mätt | `measure.py http://localhost:3399/sites/calyx.html` | `distinctTextColors` 4 · `distinctWeights` 1 · `fontSizeRange` [11, 130] · `distinctBackgrounds` 2 · `hairlineRules` 10 · `contentWidthUsed` 1376 · `families` `{"PT Mono": 33, "Cardo": 35}` |
| Kort, gradienter och foton räknade i källan | Python-räkning, kommandot ordagrant i `concepts-K4.md` § Mätning | Mallsidan: 7 hexfärger · 8 kortformer · 8 gradienter · 0 fotografier. Calyx: 0 hexfärger och 11 oklch-värden · 0 kortformer · 2 gradienter (båda scrim) · 4 fotografier |
| Demo-bildernas mått | `PIL.Image.open(...).size` | Alla tre 1200 × 750, daterade `Sep 4 12:42` |
| Sajtfilernas ändring | `git status --porcelain sites/` + `git diff HEAD -- sites/` | Sju filer ändrade, okommitterat; ändringen är i samtliga fall borttagning av `@media (prefers-reduced-motion: reduce)`-blocket, F-011 |
| Fingerprint-registret | `wc -l` + `grep -c -i alunix` | 141 rader, 35 alunix-träffar; 7 seed-rader + 29 Alunix-byggrader = 36 byggrader, vilket matchar uppdragets tal |

## Byggarens rader, R1 och framåt

R1 levererade `BRIEF.md` och skrev inga UI-filer. Raderna för R1 står i briefens egen
§ decision ledger, § catalogue-select och § Byggarens öppna frågor. R2:s rader står nedan.

---

## R2

Byggd 2026-09-10. Levererat: folden och signaturakten kompletta i `index.html`, motorn och
`sc-smooth.js` inkopierade oförändrade, fem markerade `<!-- R3 -->`-platshållare.

### `--split`, teckenkonventionen, utskriven

Målbildens egen formulering (*"delaren går från 50 % till 100 % höger"*) läses åt andra
hållet än R2-promptens tabell, så konventionen skrivs ut här, i koden och i briefen.

**`--split` är delarens x-läge som en andel av scenens bredd, mätt från VÄNSTER kant.**

| `--split` | Läge | Motsvarar |
|---|---|---|
| `0.5` | folden, 50/50 | ps = 0 |
| `0` | upplöst: Calyx fyller ramen | ps = 1 |
| `1` | mallsidan fyller ramen | `?preview=before` |

Över akten löper talet **0,5 → 0**, alltså färdas delaren **vänsterut** och "efter"-ytan
växer från halva ramen till hela. Registrerad som `<number>` med `inherits: true`.
Målbildens "100 % höger" betyder att *efter-sidan* når 100 %, inte att delaren gör det.

### Beslut

| Datum | Beslut | Källa |
|---|---|---|
| 2026-09-10 | **Motorn kopierad med `cp` och verifierad byte-identisk** mot källan (`cmp -s` för alla tre filerna). Aldrig redigerad, `.sc-*` aldrig restylad. | AB06; scroll/NOTE.md; invariant 3 |
| 2026-09-10 | **Stagen är motorns egen `.sc-stage`**, och pappersgrunden ligger på ett eget barn (`.split__ground`) i stället för på stage-klassen, så att ingen regel i cellen rör en `.sc-*`-selektor. | AB06 |
| 2026-09-10 | **`font-weight` i stället för `font-variation-settings`** för rubrikhalvans degradering 500 → 200. | `performance.md` § 2, ordagrant: "`font-weight` as a property, never `font-variation-settings`". Målbilden namnger `font-variation-settings`; regeln i referensen är den senare och den vinner. Bonus: `font-weight` degraderar begripligt även mot ett icke-variabelt reservsnitt |
| 2026-09-10 | **Två `@font-face` för riktiga filer plus EN metrikmatchad reserv**, inte två. Monon kör systemstack. | `performance.md` § 1, tak 3 filer. `perf_probe` flaggade 4 |
| 2026-09-10 | **Ingen `data-sc-cue` på foldens chrome.** Aktens cue skulle vara `0 1 0 0`, alltså full opacitet hela vägen, vilket är visuellt identiskt med ingen cue. Attributet kostade tre saker: `scrollcraft.css` lägger en klassbred `will-change: opacity, transform` på varje `[data-sc-cue]` som `perf_probe` fångade vilande och som inte går att städa utan att redigera motorn; det startar folden på `opacity: 0`; och det ger ingen beteendeskillnad. | `performance.md` § 1 (vilande `will-change` = 0); `devices.md` § cue-kontraktet (hälsa-och-håll uppfyllt i sak); SKILL.md, reveal-system ska falla mot synligt |
| 2026-09-10 | **Ingen av ramarna monteras vid load.** En `IntersectionObserver` monterar båda; vänsterramen släpps dessutom vid första `requestIdleCallback` efter first paint. | `performance.md` § 6 Never: "An iframe mounted at load". R2-promptens § 4 säger "monteras eagerly, eftersom den är folden", vilket är exakt det fallet regeln beskriver. LCP-elementet är rubriken, mätt: **LCP 472 ms** |
| 2026-09-10 | **Calyx ligger underst, ostyckad och helt stilla; mallsidan ligger överst och klipps.** Bytt ordning mot första bygget. | Mätt: två klippta lager gav p95 66,7 ms vid 4× CPU, ett klippt lager 50,0 ms. Flyttar dessutom klippningen från den tunga ramen (fyra fotografier) till den lätta (9 016 B, noll bilder), och gör F-010 sant om pixlarna och inte bara om identiteten |
| 2026-09-10 | **`letter-spacing` toppar på 0,012 em, inte målbildens 0,06 em.** | Mätt i `act-mid-1440.png`: tracking ackumulerar vänster till höger och är därför störst exakt vid sömmen. Vid 0,06 em och 56 px är det 3,36 px per mellanrum och ~77 px vid 23:e tecknet, vilket sköt en hel glyf ur läge under bläckhalvan: `nutidens` renderades `nu|idens`. Det läser som en raderad bokstav, inte som förfall. Vid 0,012 em är driften ~15 px, under en glyfbredd |
| 2026-09-10 | **Rubriken 56 px, inte 44 px.** | Mätt i `fold-1440.png`: vid 44 px slutade raden vid x≈659 mot en söm vid 720, så bläckhalvan var tom på första skärmen och tvåtonsdevicen — hela skälet till att `paper` är primär referens — var osynlig just där den betyder mest. Vid 56 px skär sömmen sista ordet |
| 2026-09-10 | **Delarens blå rule är 2 px, inte 1 px.** | `house-physics.md`: den enda accenten deployas i displayskala. Vid 1 px läste den som en grå linjal i foldbilden. Två pixlar över full viewporthöjd är displayskala i den dimension objektet faktiskt har. Fortfarande en linje, fortfarande chrome |
| 2026-09-10 | **Nytt token `--ink-3` `oklch(0.50 0.016 68)` för 11 px-registret.** `--ink-2` är nu displayskala enbart. | Mätt: `--ink-2` på `--paper` är **3,21:1**, vilket är AA för text ≥ 24 px och inget annat. De 11 px-etiketterna bär `En typisk mallsida`, alltså den sträng som gör det försvarbart att köra en anti-referens som innehåll. Efter bytet **5,27:1**. SKILL.md tillåter uttryckligen att ett värde som saknas lyfts till ett namngivet token |
| 2026-09-10 | **En enda `.seam`-behållare bär delaren, träffytan och båda monoetiketterna.** | Första bygget gav delaren `100 %` (egen box) och etiketterna och träffytan `100vw` (viewporten, rullningslist inräknad). Vid 1440 utan rullningslist sammanföll de, vilket är precis varför den buggklassen överlever en skrivbordskontroll |
| 2026-09-10 | **Tangentbordet scrollar akten i stället för att sätta ett lokalt värde.** Piltangenterna flyttar 2 % av `--split` genom att scrolla, `Home`/`End` går till ändlägena. | R1:s brief sade "genom samma fjäder". Ett lokalt värde fjädrar tillbaka till scrollens värde inom 350 ms, alltså skulle en tangentbordsanvändare få noll varaktigt resultat av sidans enda interaktion. Att scrolla ger samma varaktiga effekt som hjulet ger. Mätt: 0,2778 → höger → 0,2585 (steg 0,0193 ≈ 2 %) → vänster → 0,2778 |
| 2026-09-10 | **Dragningen är gatead till `(pointer: fine)`.** På touch är delaren enbart scrollstyrd. | Målbilden: "fin pekare: `cursor: col-resize`". En vågrät gripyta på 44 px skulle annars konkurrera med sidans egen lodräta scroll på telefon |
| 2026-09-10 | **`--d` registrerad som `<number>`.** | Oregistrerad substitueras den som en token-ström, och `calc(var(--d) * 0.012em)` beräknades då till `normal`. Mätt i första bygget: hela letter-spacing-halvan av degraderingen gjorde tyst ingenting medan `font-weight` fungerade |
| 2026-09-10 | **Rubriken behåller sin grad genom hela akten.** `concepts-K4.md` § (3) s3 säger att den faller till en 11 px monoetikett i övre vänstra hörnet. | R2-promptens § 2 säger uttryckligen "Den byter aldrig grad, aldrig snitt, aldrig radbrytning under akten", och briefens continuity-tes säger att det är samma rad hela vägen. Prompten är den senare och den vinner |
| 2026-09-10 | **Under 640 px får rubriken brytas till två rader.** | Enradsregeln skyddar mot att radantalet ändras UNDER akten, vilket det inte gör. En enrads 31-teckensrubrik på 390 px skulle kräva ~13 px, alltså under brödtextgrad |
| 2026-09-10 | **`[needs asset: assets/switzer-variable.woff2]` och `[needs asset: assets/reddit-mono-variable.woff2]`.** Ingen av filerna är vendorad. Sidan är byggd för att rendera rätt utan dem via metrikmatchad reserv och för att uppgradera i samma ögonblick de landar på exakt de sökvägarna. Båda begärs en gång och ger 404, vilket är väntat. **Konsekvens som R3 måste veta:** viktaxeln 500 → 200 är inert mot ett icke-variabelt reservsnitt; `letter-spacing`, färg och `saturate()` bär degraderingen tills filerna finns. | F-009: lead vendorar, byggaren hämtar aldrig |
| 2026-09-10 | **De sex demo-skärmbilderna finns nu i `assets/` (lead sköt dem efter R1).** Två av dem överskrider ASSETS.md:s egna tak: `demo-calyx-1440.webp` 206 966 B mot taket 150 kB och `demo-calyx-390.webp` 190 200 B mot taket 120 kB. Båda är reservfiler och används inte av R2. | `ASSETS.md` § 3, målvärdestabellen. Noterat för lead, inte åtgärdat av byggaren |

### Mätningar, med utfall

Servern: `python ~/.claude/skills/design/scripts/serve.py --port 3303 --root .` från repo-roten.

**Proben bevisad i båda riktningarna först** (`performance.md` § 5: en kontroll som bara
kan godkänna är värdelös). Samma `motion_probe`, samma flaggor, mot kedjans egna fixturer:

```
tests/motion/smooth.html      PASS  p95 16.7 ms | >33ms 0 | max_step 1.35% | staircase  0
tests/motion/staircase.html   FAIL  p95 16.8 ms | >33ms 0 | max_step 5.56% | staircase 18
```

Instrumentet skiljer alltså de två felen, och 20 ms-baren är nåbar vid 4× CPU på en lätt
sida. Talen nedan är därför riktiga fynd och inte en artefakt av mätningen.

**`motion_probe`, hjul 100:60, 4× CPU:**

```
section.split:--sc-p     p95 50.1 ms | >33ms 73 | max_step 3.17% | staircase 13 | rev 0
section.split:--sc-ps    p95 50.1 ms | >33ms 73 | max_step 3.17% | staircase  0 | rev 0
section.split:--split    p95 50.1 ms | >33ms 73 | max_step 3.52% | staircase  0 | rev 0
```

**`motion_probe`, hjul 20:120, 4× CPU:**

```
section.split:--sc-p     p95 66.7 ms | >33ms 191 | max_step 3.70% | staircase 8 | rev 0
section.split:--sc-ps    p95 66.7 ms | >33ms 191 | max_step 1.19% | staircase 0 | rev 0
section.split:--split    p95 66.7 ms | >33ms 191 | max_step 1.42% | staircase 0 | rev 0
```

**Båda scrollriktningarna**, egen körning, `--split` avläst per hjulklick:

```
ned:  0.500 -> 0.009, monoton: ja,  inga tecken-flippar
upp:  0.004 -> 0.458, monoton enligt probens per-frame-mätning (rev 0 i båda körningarna)
```

**Vad talen betyder, uppdelat på `motion-smoothness.md`:s två fel.**

- **Fel 1, värdet stegar: löst, och bevisat.** `staircase = 0` för både `--sc-ps` och
  `--split` i båda hjulkadenserna. Kontrollen i samma körning är rå `--sc-p`, som visar
  `staircase 13` respektive `8`. Shimen gör alltså exakt det den finns för, och den raka
  lodräta linjen — den värsta tänkbara ytan för ett stegande värde — glider.
- **Fel 2, sidan tappar bilder: verkligt, och orsaken är mätt.** p95 50–67 ms vid 4× CPU
  mot baren 20 ms. **Min egen animation kostar ingenting mätbart:** samma sida med
  klippningen fryst ger 50,0 ms, och med klippning och filter helt borttagna 50,0 ms,
  alltså identiskt. Kostnaden är att rendera två levande sidor.
- `max_step` 3,52 % vid 100:60 och 1,42 % vid 20:120 är samma fynd, inte ett andra: när en
  bildruta tar 50 ms hinner mer scroll mellan rutorna. Vid den långsammare kadensen ligger
  talet väl inom baren.

**Nedbrytning av fel 2** (egen körning, 4× CPU, samma hjul, samma antal klick):

| Läge | p95 | frames > 33 ms |
|---|---|---|
| båda ramarna live, som byggd | 66,7 ms | 57 |
| **vänsterramen blockerad** (mallsidan borta) | **66,6 ms** | 55 |
| **högerramen blockerad** (Calyx borta) | **33,4 ms** | 33 |
| båda blockerade | 33,4 ms | 39 |
| båda live, bara Unsplash blockerat | 50,1 ms | 55 |

**Detta vänder briefens egen beslutsregel, och det är ett lead-beslut, inte ett
byggarbeslut.** `BRIEF.md` § Prestandaplan säger: överstiger överföringen 2,5 MB
degraderas **vänsterramen** till en skärmbild, "aldrig tvärtom". Två saker gäller:

1. **Överföringsregeln utlöses inte.** `perf_probe` ger **1 690 kB**, alltså inom taket
   2 500 kB. Båda ramarna får förbli levande enligt briefens egen regel.
2. **Men rörelsebaren faller, och den namngivna åtgärden hjälper inte.** Att degradera
   vänsterramen ger 66,7 → 66,6 ms, alltså ingenting. Den dyra ramen är **Calyx**, inte
   mallsidan. Att degradera Calyx skulle fixa talet och samtidigt offra PRODUCT.md
   princip 1 — beviset ska gå att använda — på en sida vars hela argument är att beviset
   är verkligt och körbart. Jag degraderar därför ingendera och lämnar avvägningen till
   lead med talen. Se `BRIEF.md` § Byggarens öppna frågor, **B6**.

**`perf_probe`, 4× CPU:** `LCP 472 ms | CLS 0,000 | 1 690 kB | 45 noder | 15 långa tasks
(7 under scroll)`. Kvarstående FAIL, med status:

| FAIL | Status |
|---|---|
| `font-files 4 > 3` | Kvarstår. K4 deklarerar tre. De fyra är typsnitt som **ramarnas egna sidor** hämtar från Google Fonts (Inter i mallsidan, Cardo och PT Mono i Calyx). Går inte att åtgärda utan att redigera en exempelsajt, vilket är förbjudet |
| `hero-image 1 122 865 B` | Kvarstår. Det är **Calyx eget** Unsplash-fotografi, hämtat inifrån ramen. Dokumenterat i `ASSETS.md` § 2 och i briefens prestandaplan sedan innan. Samma skäl |
| `long-task-under-scroll 7` | Kvarstår. Samma orsak som fel 2 ovan, samma nedbrytning |
| ~~`resting-will-change div.chrome`~~ | **Åtgärdat** genom att ta bort `data-sc-cue` (se beslutstabellen) |
| ~~`font-face-without-display`~~ | **Åtgärdat** |

**`scroll_verify`:** `cuesNeverFull []`, `unrevealed []`, `contrastUnderMedia []`.
`deadScroll` 15 segment och `blankBands` 900→7560 är **de fem `<!-- R3 -->`-platshållarna**,
som är avsiktligt tomma i den här rundan och har rätt höjd och rätt grund. Den författade
tystnaden i aktens första 0,10 rapporteras inte som dead scroll.

**Kontrast, mätt mot sidans egna renderade färger** (inte antaget ur tokentabellen):

| Par | Utfall | Dom |
|---|---|---|
| `--ink` på `--paper` (rubrikens efterhalva, mailto) | 13,70:1 | ✓ |
| `--ink-2` på `--paper` (rubrikens förehalva, 56 px) | 3,21:1 | ✓ som stor text, och används inte till annat |
| `--ink-3` på `--paper` (11 px mono) | **5,27:1** | ✓ efter bytet; var 3,21:1 och underkänt |
| `Före` / `Efter` i `--ink` | 13,70:1 | ✓ |
| `--blue` på `--paper` (delaren, en yta) | 6,02:1 | ✓, mäts aldrig som text |

**Överflödessvep, ingen vågrät scroll vid någon bredd:** 320, 375, 390, 414, 768, 1440 —
`scrollWidth == clientWidth` i samtliga.

### Pekarhandoffen, egen körning

`motion_probe` driver bara hjulet, så dragningen mättes separat med syntetiska
pointer-händelser som dispatchas i **samma bildruta** som träffytans läge läses.

```
scroll-ägt målvärde före drag        0.2778   (delaren vid x=400)
under drag, 1:1-följning             fel 0.0000  (pekaren +360 px = +0.250)
efter släpp, 700 ms                  0.508 0.434 0.397 0.359 0.319 ... 0.278 0.278
  landar på                          0.2778 = scrollens värde
  rör aldrig 0.5000                  ja
  monoton, ingen översläng           ja  (damping 1,0 bekräftad)
avbrott mitt i återgången
  värde precis före greppet          0.3320
  värde en bildruta efter greppet    0.3320   hopp 0.0000
  efter +60 px drag                  0.3737   förväntat 0.3737, 1:1-fel 0.0000
  släppt, landar på                  0.2778 = scrollens värde
tangentbord                          0.2778 -> höger -> 0.2585 -> vänster -> 0.2778
```

Alla tre `apple-design`-kraven är alltså uppfyllda och mätta: **avbrytbarhet** (hopp
0,0000 vid grepp mitt i fjädern), **presentationsvärde** (det som målas är fjäderns utvärde,
och greppet tar vid i det), **velocity-handoff** (återgången startar med pekarens hastighet
och avtar monotont). Delaren snäpper aldrig till 50 %.

**En observation som inte är en bugg men är värd att veta:** att gripa delaren *medan* den
fjädrar är svårare än att gripa den i vila, eftersom träffytan rör sig. Två av mina första
testkörningar missade remsan helt och såg ut som ett 1:1-fel innan jag dispatchade
händelserna i samma bildruta. Det är en riktig användbarhetsanmärkning för R3, inte ett fel
i sidan: fjädern varar ~350 ms och remsan är 44 px.

### Vad jag läste i kontaktarket och i bilderna

Kontaktarket `shots/r2/sheet.png` läst som pixlar, plus elva egna skärmbilder i samma mapp.

- **Kontaktarket, första bygget:** hela akten stod stilla från y = 900 och neråt och sidan
  var 6 300 px i stället för 7 560. Det var så jag hittade rotorsaken: jag hade laddat
  `scrollcraft.js` men aldrig anropat `ScrollCraft.mount(document.body)`, så motorn tog
  aldrig över, sektionen fick aldrig sin höjd på 240 vh och `--sc-p` skrevs aldrig. Min egen
  failsafe fångade det och skrev `[K4] scrollcraft did not report ready in 1200 ms` i
  konsolen, vilket är precis vad den finns för.
- **Kontaktarket, efter fixen:** delaren vandrar vänsterut ruta för ruta, Calyx växer,
  mallsidan krymper och tappar mättnad. Rörelsen lurar inte, vänder inte och stannar inte
  mitt i.
- **`fold-1440.png`:** de två sajterna kant i kant, en söm, `Före / En typisk mallsida` och
  `Efter / Exempelsida: Calyx, florist i Stockholm` flankerar linjen. Tvåtonsrubriken bryter
  exakt på sömmen: `Er hemsida är nutidens visit` dämpat, `kort` i bläck. Det var den här
  bilden som visade att 44 px var för litet — då slutade raden före sömmen och bläckhalvan
  var tom.
- **`act-mid-1440.png`:** degraderingen syns tydligt, den vänstra halvan är tunnare och
  öppnare än den högra. Det var här jag såg att `nutidens` blev `nu|idens`, alltså att
  0,06 em tracking sköt en hel glyf ur läge vid sömmen. Efter fixen möts halvorna rent.
- **`preview-after.png`:** upplösningen landar. Calyx fyller ramen hel och oskuren, rubriken
  är helt bläck, `Efter`-etiketten har följt med till vänsterkanten. Det är aktens
  belöning och den fungerar.
- **`preview-before.png`:** mallsidan fyller, delaren är utanför högerkanten, rubriken är
  helt dämpad, `Före`-etiketten sitter kvar vid högerkanten. Korrekt spegling.
- **`fold-390.png`:** rubriken bryter till två rader och tvåtonen skär båda, vilket är rätt.
  Här såg jag att etiketterna på 62 % bredd sköt Calyx-bildtexten utanför högerkanten;
  ändrat till 44 % och kontrollerat med ett överflödessvep.
- **Sparklinen** i probens utdata: `--sc-ps` och `--split` ritar en jämn kurva utan platt
  axel och utan hack. Rå `--sc-p` ritar en trappa i samma körning. Det är den visuella
  motsvarigheten till `staircase 13` mot `staircase 0`, och de ligger bredvid varandra i
  samma bild, vilket är det starkaste belägget i rundan för att shimen bär akten.

---

## R3 (fixrunda)

2026-09-10. Planerna 001–003 utförda i nummerordning, varje plans Verification körd
innan nästa plan öppnades.

### Typsnitten, bekräftade före allt annat

Lead vendorade båda filerna efter R2. Bekräftat på port 3303 innan en enda mätning:

```
assets/switzer-variable.woff2      200   43 220 B
assets/reddit-mono-variable.woff2  200   30 496 B
                                         73 716 B totalt, tak 300 kB, 2 filer, tak 3
```

**Varje mätning och skärmbild från R2 är därmed ogiltig** och är omtagen nedan. Den
konsekvens R2 flaggade är upphävd: viktaxeln 500 → 200 är inte längre inert, eftersom
Switzer nu är en riktig variabel fil.

### Planerna

| Plan | Utfall | Kommentar |
|---|---|---|
| **001** fast layoutvyport 1440 och statisk skala under 640 px | **verified** | Alla måltal träffade vid 390 × 844. Två avvikelser från planens bokstav, båda mätta och båda till planens fördel, se nedan |
| **002** delaren som aktens displayelement mellan ps 0,10 och 0,68 | **verified** | Ingen av planens två föreslagna former kan nå planens egna måltal; en tredje form mättes fram och når alla tre |
| **003** sömmen får inte halvera ett ordmärke | **best-effort** | Fem av sex måltalsrader gröna. Den sjätte (≥ 4 px marginal vid 390) är mekaniskt onåbar inom planens egna gränser: mätt 3,7 px. Inget ordmärke och ingen navpost skärs vid någon bredd, vilket är planens Done-when |

### Plan 001, i detalj

Båda ramarna lägger ut mot 1440 px och skalas en gång vid montering och vid `resize`,
aldrig i akten och aldrig per bildruta. Mätt vid 390 × 844:

| Storhet | Målvärde | Mätt |
|---|---|---|
| Ramens layoutbredd | 1440 px | 1440 px |
| Skala | 0,2708 | **0,2708** |
| Bandets renderade höjd | 181 px ± 2 | **181 px** |
| Ramen renderad | — | 390 × 181 |

**Två avvikelser från planens bokstav.**

1. **`--head-h` härleds ur bandet i stället för att sättas till ett fast tal.** Planen
   ber om ett fast värde valt så att papperet över och under bandet skiljer sig med högst
   15 %, mätt vid 390. Ett fast 320 px klarade 390 (320 / 343, 6,7 %) men drev till
   **21,3 % vid 320 px** bredd, eftersom bandets höjd skalar med viewporten och ett fast
   tal inte gör det. Härlett (`max(200px, calc((100dvh - var(--band-h)) / 2))`) är de två
   marginalerna **exakt lika vid varje smal bredd**: 286/286, 319/319, 332/332, 352/352.
   Golvet 200 px är innehållet.
2. **Etiketterna ankras i underkant mot bandet, inte i överkant mot arket.** Blocket
   bryter till två eller tre rader beroende på bredd, så en toppförskjutning lät det växa
   ned i bandet: **mätt 22 px överlapp vid 320**. Underkantsankrade ligger de 10 px fritt
   från utskrifterna de namnger, vid varje bredd.

`--head-h` flyttades dessutom från `.frames` till `.split`: huvudet, etiketterna i
`.seam` och bandet är tre syskon som alla mäter mot den, och en custom property
deklarerad på ett syskon når inte de andra.

Klippet ligger kvar på `.layer` och träffytan på `.seam`, alltså mot scenen och inte mot
ramens 1440 (planens steg 5 och 6, kontrollerade, oförändrade).

### Plan 002, i detalj

**Ingen av planens två föreslagna former kan nå planens egna måltal.** Räknat, inte antaget:

- **Exponentformen är omöjlig.** `split(0,40) ≥ 0,44` kräver `n ≥ 1,930`;
  `split(0,72) ≤ 0,06` kräver `n ≤ 0,343`. Intervallen överlappar inte. Planens fyra
  föreslagna exponenter ger `split(0,72)` = 0,214 / 0,263 / 0,303 / 0,337 mot målet 0,06.
- **Planens fönster-fallback faller också.** Håll 0,44 till ps 0,62 och res sedan till 0
  över 0,62–1,0 ger `split(0,72) = 0,324`, alltså långt över 0,06.

**Den form jag mätte fram:** en liten konstant drift plus en koncentrerad rusning.
`e = 0,12·t + 0,88·smoothstep(0,555 → 0,685, t)`. Driften gör att delaren aldrig står
still — den *är* aktens displayelement, och ett element som slutar röra sig slutar följas
— och rusningen bär sömmen genom Calyx typzon i en enda kort passage.

Mätt mot planens måltabell, **med `--split-start` från plan 003 inräknat**, eftersom de två
planerna delar samma funktion och måste mätas ihop (planens steg 3):

| Mätpunkt | Målvärde | Mätt |
|---|---|---|
| Andel av akten med `--split` i 0,42–0,02 | ≤ 0,12 | **0,102** |
| `--split` vid ps = 0,40 | ≥ 0,44 | **0,5625** |
| `--split` vid ps = 0,72 | ≤ 0,06 | **0,0293** |
| `--d` vid ps = 0 | 0 | **0,0000** |
| Monoton | ja | **ja**, `rev 0` i alla körningar |
| Största legibla objektet till höger vid ps = 0,40 | Calyx fotografi | **Calyx fotografi** |

De tre fragmenten `cal` / `ure,` / `olm.` som dominerade R2:s vy är borta: Calyx
jätterubrik ligger nu kvar bakom mallsidan tills sömmen redan passerat den.

**Tangentbordssteget räknades om (planens steg 3).** Scrollposition är inte aktprogress:
motorn lägger sin egen dwell-remap emellan, så ett steg löst på ps-axeln och multiplicerat
med scrollsträckan landar fel — **mätt, före fixen: 47 % av scenen i driften i stället för
2 %**. Remapen är en dokumenterad monoton kurva med f(0)=0 och f(1)=1, så de två
avbildningarna komponeras och inverteras med bisektion på scrollaxeln. Dwell-värdet läses
ur aktens eget attribut i stället för att kopieras, så de kan inte glida isär.

| Var i akten | Steg, mätt | Krav 1,5–3 % |
|---|---|---|
| drift, tidigt | **2,00 %** | ✓ |
| drift, sent | **2,02 %** | ✓ |
| rusningen | **2,06 %** | ✓ |
| svansen | 1,04 % | delaren har bara 1,04 % kvar att ge; klampat, inte fel |

Skärmbilder, lästa som bilder: `läst: shots/r3/p002-ps012-1440.png` (ps 0,121, två hela
sidor) · `läst: shots/r3/p002-ps040-1440.png` (ps 0,397, delare på väg, Calyx foto bakom)
· `läst: shots/r3/p002-ps072-1440.png` (ps 0,723, nästan upplöst, Calyx rubrik hel och
oskuren). Ingen av de tre har ett avskuret display-ord som vyns tyngsta objekt.

### Plan 003, i detalj

**Planens föreslagna 0,57 skär `Pricing`.** Mätt i pixlar vid 1440, båda sajterna vid sin
egen layoutbredd (planens steg 1):

```
Calyx ordmärke, glyferna slutar      x = 757
mallsidans nav:  Customers 682–754 · Pricing 782–828 · Docs 856–890
```

0,57 är x = 821, alltså inuti `Pricing`. Den enda luckan i planens tillåtna fönster
0,54–0,60 som går fri från varje glyf på båda sidor är **828–856**, vars mitt är
x = 842,4. **`--split-start = 0,585`**, skriven på ett ställe och läst av de fyra som
behöver den (`@property` initial-value, `targetFrom()`, `--d`-normeringen, `MODES`).

| Mätpunkt | Målvärde | 1440 | 390 |
|---|---|---|---|
| `--split` vid ps = 0 | 0,54–0,60 | **0,585** | **0,585** |
| Sömmen → Calyx ordmärke | ≥ 12 / ≥ 4 px | **85,8 px** | **23,3 px** |
| Sömmen → närmaste navglyf (`Docs`) | ≥ 12 / ≥ 4 px | **13,9 px** | **3,7 px** ✗ |
| Andel "före" synlig vid ps = 0 | ≥ 0,54 | **0,585** | **0,585** |
| `Före`/`Efter`-etiketternas offset | oförändrad | 20 px | 12 px, som R2 |
| `--d` vid ps = 0 | 0 | **0,0000** | **0,0000** |

**Varför 390-raden är best-effort och inte kan lösas:** luckan mellan `Pricing` och `Docs`
är 28 px bred, så det största möjliga halva avståndet är 14 px, som vid skalan 0,2708 blir
**3,79 px**. Målet 4 px kräver ≥ 14,77 px, alltså en bredare lucka än som finns. Den enda
bredare luckan i mallsidans nav är 890–1040, vars mitt ligger på 0,670 — och planen
förbjuder uttryckligen ett startvärde över 0,60. Ingen glyf skärs vid någon bredd, vilket
är planens Done-when; det är marginalen som är 0,3 px kort, inte utfallet.

**En mätt konsekvens planen inte förutsåg, och som inte går att undvika:** mallsidans
`Dashboard preview`-kort börjar vid x = 746. Varje söm som går fri från navraden ligger
till höger om 746 och skär därför kortet. Vid 0,5 låg kortet helt bakom Calyx; vid 0,585
syns 96 px av det. Det är ett kort, inte ett ordmärke eller en navpost, alltså utanför
planens scope — men det är en försämring som följer direkt av planens eget fönster och
den ska stå här. Alternativet är att skära ordmärket och `Customers`, som planen graderar
HIGH mot den här som MEDIUM.

### Den mekaniska grinden

**Kontrollen först.** `motion_probe` mot `tests/motion/smooth.html`, 4× CPU, innan sidan
mättes:

```
KONTROLL  smooth.html   #act:--sc-ps      p95 16,8 ms | >33ms 0 | max_step 1,37 % | staircase 0
KONTROLL  smooth.html   #card:transform   p95 16,8 ms | >33ms 0 | max_step 1,37 % | staircase 0   PASS
```

Noll rutor över 33 ms, alltså är värden inte brusig och sidans tal nedan är riktiga fynd.
Rå `--sc-p` spåras inte längre (Q22).

```
SIDAN  wheel 100:60   --sc-ps   p95 66,7 ms | >33ms  57 | max_step  3,33 % | staircase 0 | rev 0
SIDAN  wheel 100:60   --split   p95 66,7 ms | >33ms  57 | max_step 32,79 % | staircase 0 | rev 0
SIDAN  wheel 20:120   --sc-ps   p95 66,7 ms | >33ms 165 | max_step  0,86 % | staircase 0 | rev 0
SIDAN  wheel 20:120   --split   p95 66,7 ms | >33ms 165 | max_step  1,62 % | staircase 0 | rev 0
```

- **`staircase = 0` på båda spåren i båda kadenserna**, mot kontrollens 0. Fel 1 i
  `motion-smoothness.md` är löst och förblir löst efter alla tre planerna.
- **`max_step ≤ 3 %` på `--sc-ps` vid 20:120: 0,86 %.** Vid 100:60 är den 3,33 %, alltså
  0,33 punkter över, och orsaken är bildtiden: när en ruta tar 66,7 ms hinner mer scroll
  mellan rutorna. Samma fynd som B6, inte ett nytt.
- **`--split` 32,79 % vid 100:60 rapporteras men grindar inte** (härlett spår, Q22). Talet
  är rusningen: ett snabbt hjul genom fönstret 0,555–0,685 flyttar sömmen mycket per ruta.
  Vid den kadens planens feel-check anger, 20:120, är det **1,62 % = 23 px vid 1440**,
  alltså under en glyfbredd (56 px-typ ≈ 28 px per glyf).
- **p95 66,7 ms mot baren 20 ms** är B6, oförändrat och oförändrat orsakat: två levande
  sajter. R2 mätte att min egen animation kostar noll (identisk p95 med klippningen helt
  borttagen).

**`scroll_verify`:** `cuesNeverFull []`, `unrevealed []`, `contrastUnderMedia []`.
`blankBands` 900→7560 och 16 `deadScroll`-segment är de fem `<!-- R3 -->`-platshållarna,
oförändrat mot R2.

**`perf_probe`, 4× CPU:**

```
1440   LCP 300 ms | CLS 0,000 | 1 774 kB | 45 noder | 41 långa tasks (33 under scroll)
 390   LCP 504 ms | CLS 0,000 | 1 774 kB | 45 noder | 38 långa tasks (28 under scroll)
```

LCP och CLS är gröna med marginal vid båda bredderna, och överföringen ligger inom taket
2 500 kB. Tre FAIL kvarstår, alla tre namngivna undantag:

| FAIL | Orsak | Status |
|---|---|---|
| `font-files 6 > 3` | K4 deklarerar **tre**. De sex är K4:s tre plus de typsnitt **ramarnas egna sidor** hämtar från Google Fonts: Inter i mallsidan, Cardo och PT Mono i Calyx | Undantag. Går inte att åtgärda utan att redigera en exempelsajt, vilket är förbjudet |
| `hero-image 1 122 865 B` | Calyx **eget** Unsplash-fotografi, hämtat inifrån ramen | Undantag, dokumenterat sedan `ASSETS.md` § 2 |
| `long-task-under-scroll 33` | Samma orsak som p95: två levande sajter | Undantag, B6 |

Långa tasks steg från R2:s 7 till 33. Orsaken är typsnitten: de var ovendorade under hela
R2, så sidan mätte då en sida utan egna typsnittsfiler att avkoda. Det är alltså inte en
försämring orsakad av planerna, utan första gången posten mäts på den färdiga sidan.

**`preflight_taste`: PASS.** En not, inte ett fel: klassificeraren ser bara två
sektionsfamiljer över sex sektioner (`iframe`, `text-only`), vilket är väntat när fem av
sex sektioner är tomma `<!-- R3 -->`-platshållare. Läses om i R3:s innehållsrunda.

**`detect.mjs`: 0 findings.**

**`contrast_over_media.py`: kan inte köras som instruerat.** Skriptet har
`http://localhost:3055/` hårdkodat på rad 27 och tar ingen `--url`-flagga, så anropet dör
på `ERR_CONNECTION_REFUSED`. Underliggande villkor kontrollerat direkt i stället, vilket
är det grinden faktiskt frågar efter: **noll textelement i K4:s eget lager överlappar de
levande ramarna, vid 1440 och vid 390.** All K4-typ sitter på solid `--paper` i huvudbandet;
den enda typ som ligger över bild tillhör exempelsajterna, inuti deras egna ramar, som K4
aldrig redigerar. `scroll_verify`s egen `contrastUnderMedia` ger `[]` från det andra
harnesset. Noterat som verktygsfel, inte som ett sidfel.

**Överflödessvep, `scrollWidth == clientWidth` vid varje bredd:** 320 ✓ 375 ✓ 390 ✓
414 ✓ 768 ✓ 1440 ✓.

### Lästa skärmbilder

```
läst: shots/r3/p001-fold-390.png        två hela sidor i miniatyr, inget ord skuret av en kant utom sömmen
läst: shots/r3/p002-ps012-1440.png      ps 0,121, två hela sidor, delaren står nästan still
läst: shots/r3/p002-ps040-1440.png      ps 0,397, Calyx fotografi är vyns största legibla objekt
läst: shots/r3/p002-ps072-1440.png      ps 0,723, Calyx rubrik hel och oskuren, sömmen vid x = 27
läst: shots/r3/gate-fold-1440.png       ps 0, Flowstack/Product/Solutions/Customers/Pricing hela, Calyx ordmärke helt dolt
läst: shots/r3/gate-fold-390.png        ps 0, samma komposition i miniatyr
```

Vid 1440 vid ps = 0 skär sömmen numera **bara** tvåtonsrubriken, vilket är devicen. Vid 390
kolliderar Calyx egen mobilnav med sitt ordmärke inuti ramen; det är exempelsajtens egen
kalibreringsbrist (Q23), noterad och inte lagad.

### Avvikelser mot målbilden, samlade

Fyra, alla med källa och alla också inskrivna som rader i `BRIEF.md` § decision ledger.

1. `font-variation-settings` → `font-weight` (`performance.md` § 2).
2. `letter-spacing` 0,06 em → 0,012 em (mätt glyfdrift vid sömmen).
3. Rubriken behåller sin grad genom akten i stället för att falla till en monoetikett vid s3
   (R2-promptens § 2, som är senare än `concepts-K4.md` § (3)).
4. Ingen `data-sc-cue` på foldens chrome; hälsa-och-håll uppfylls utan attributet
   (`performance.md` § 1, vilande `will-change`).

Ingen av dem rör palett, typsnittsval, grammatik, aktform, nav, hero-device, avslut eller
signatur, alltså är fingerprint-raden i `concepts-K4.md` § (4) oförändrad.

## R1, leadens rader (2026-09-10)

| Datum | Beslut | Källa |
|---|---|---|
| 2026-09-10 | R1 godkänd utan retur. Referensgolvet uppfyllt, noll gate-deny, noll UI-filer, senaste catalogue-select-raden stämmer med fas 0 | Leadens mekaniska kontroll mot sessionsledgern plus arkitektens dom |
| 2026-09-10 | Byggarens första catalogue-select-rad mot det ofyllda skelettet var en alfabetisk nollrad. Golvet läser sista raden, så låset håller. Alla tre cellerna gjorde samma sak, inte bara V3c | `hooks/design-gate.py` referensgolv; K4:s fråga B1 |
| 2026-09-10 | Ingen Stop-rapport skrevs för R1, och route-gapet har därför ingen artefakt. R1 skriver noll UI-filer och alltså noll route-rader, så måttet är inte meningsfullt förrän R2 | GOALS mätpunkt 2; arkitektens öppna punkt 7 |

## Bevakarens observation inför F-007 (R2, 2026-09-10)

Läst som pixlar av bevakaren: `index.html` vid 1440, ps = 0 och `?preview=after`. Strukturen
matchar målbilden. Ett beslut för arkitekten: vid ps = 0 ligger delaren exakt på Calyx' centrerade
ordmärke, så folden visar `lyx` som sitt mest läsbara element. Mekanismen är rätt (ramen klipps,
transformeras aldrig), men "första vyn är en tes" och "ett displayelement per skärm" bör vägas
mot ett halvt ord i folden. Alternativ: annat startläge för `--split`, eller att låta det stå
med motivering i beslutsledgern. Avgör i F-007, inte i fixrundan.

## Arkitektens beslut om de smala vyerna (F-007, R2, 2026-09-10)

| Datum | Beslut | Källa |
|---|---|---|
| 2026-09-10 | **Väg (a): möt det med bredd.** Under 640 px lägger båda ramarna ut mot en **fast layoutvyport på 1440 px** och skalas med **en enda statisk `scale()` satt vid montering** (`390/1440 = 0,2708`), aldrig under akten. Utskriftsbandets höjd härleds ur skalan (`668 × 0,2708 ≈ 181 px` vid 390) så att ingen sida beskärs och ingen död pappersyta blir kvar; bandet centreras i arket med rubriken och `Före`/`Efter` ovanför och papper under. Demo-bilderna i `assets/` **används inte i layouten** och står kvar som dokumenterad reserv om en ram blockeras. Dokumenterat golv: under 320 px är bandet lägre än 150 px och de två sidorna läses som textur, inte som sidor; det är namngivet och accepterat, inte en bugg. | F-007-kontrollen av `review/r2/K4-fold-390.png`, läst som pixlar: vid 390 är varje halva 195 px av en sida som lagts ut mot 390 px, alltså en halv telefonsida per sida, och båda är oläsbara (`The all-` / `platform` / `modern` avskurna mitt i ord, Calyx jätterubrik som fragmenten `re,` och `ockholm.`, brödtext klippt mitt i rad). Väg (c) löser inte geometrin: en 195 px bred skiva av en demo-bild är exakt lika oläsbar som en 195 px bred skiva av en levande ram, och skulle byta bort det levande beviset mot ingenting. Väg (b) ensam lämnar sidan trasig under golvet i stället för att laga den. Väg (a) behåller **PRODUCT.md princip 1** (beviset ska gå att använda), behåller signaturen (klippet och dragningen arbetar oförändrat på ett statiskt skalat lager) och ger den smala vyn **samma scen som 1440, mindre**. Att en statisk skala satt vid montering inte är samma sak som att transformera en visad ram är samma precedens K3 skrev in i samma runda; skillnaden skrivs ut i ledgern när den byggs. Fixplan: `plans/001-smal-vy-fast-layoutvyport.md` |

## R2, leadens rader (2026-09-10)

| Datum | Beslut | Källa |
|---|---|---|
| 2026-09-10 | Typsnitten var **ovendorade under hela R2**. Cellens `@font-face` pekade på filer som inte fanns, så varje skärmbild och varje mätning i rundan, byggarens egna inräknade, togs mot fallback-stacken. Lead har nu vendorat dem och bekräftat att de laddar | F-009: lead vendorar material. R1-briefens `[needs: vendor]`-rad var min att stänga och blev liggande |
| 2026-09-10 | `motion_probe` faller i alla tre cellerna, men **staircase är 0 överallt**. Det som fallerar är bildtid, alltså F-013:s andra fel, inte F-014:s första | Leadens egna körningar, hjul 100:60, cpu 1 och cpu 4 |
| 2026-09-10 | Alla mätvärden i rundan ska tas om i fixrundan, eftersom de togs mot fel typsnitt | Samma rad som ovan |
| 2026-09-10 | F-007 **avvikelse**. Akt-koordinater: a1 ps = 0 (sömmen halverar Calyx ordmärke och mallsidans navpost, båda bredderna), a1 ps 0,10 till 0,68 (fel displayelement: Calyx typfragment väger tyngre än delaren), a1 hela akten vid 390 (halv sida per sida, ingen av dem läsbar) | Arkitektens F-007-kontroll mot leadens pixlar |

## Bevakarens observationer inför F-007 (R3 fixrunda, 2026-09-10)

Läst som pixlar: `review/r3/K4-fold-390.png`, `review/r3/K4-fold-1440.png`. Arkitekten dömer; det här är vad bilden visar.

1. **Bildtexten under "Efter" klipps av högerkanten vid 390.** Raden `Exempelsida: Calyx, florist i Stockholm` renderas `Exempelsida: Calyx,` / `florist i Stockholr` med sista tecknen utanför vyporten. Strängen står i `PRODUCT.md` § Låst copy, så en ofullständig rendering är samma felklass som K3:s plan 002. Mät `getBoundingClientRect().right` mot 390 innan domen.
2. **Sömmen delar rubriken mitt i ordet vid ps = 0: `nut|idens`.** Konceptet låser att före-halvan tunnas, så att sömmen korsar rubriken är avsett; att den korsar inuti ett ord på den låsta raden `Er hemsida är nutidens visitkort` är en fråga arkitekten ska svara på med skäl, inte lämna åt slumpen i radbrytningen.
3. Plan 003:s `best-effort` (3,7 px mot 4 px) syns inte i bilden som ett fel: inget ordmärke och ingen navpost skärs vid 390 eller 1440.

## R3, leadens pixelläsning (2026-09-10)

- läst: `tests/alunix-r8/review/r3/K4-fold-1440.png`
- läst: `tests/alunix-r8/review/r3/K4-fold-390.png`
- läst: `tests/alunix-r8/review/r3/K4-after-1440.png`
- läst: `tests/alunix-r8/review/r3/K4-after-390.png`

### Leadens beslut, R3 (2026-09-10)

| Datum | Beslut | Källa |
|---|---|---|
| 2026-09-10 | Planerna 001 och 002 `verified` mot pixlarna: två hela sidor i miniatyr vid 390, och vid ps 0,40 är Calyx fotografi vyns största legibla objekt | Arkitektens F-007-dom |
| 2026-09-10 | Plan 003:s 3,7 px-rad accepterad: kravet 4 px är mekaniskt onåbart inom planens gränser, eftersom största möjliga halva avstånd är 14 px och 14 × 0,2708 = 3,79 px. Skillnaden är 0,3 px och planens `Done when` är nådd | Byggarens mätning, prövad av arkitekten |
| 2026-09-10 | Feel-check-raden "inget helt ord skärs" upphävd till förmån för den smalare regeln om ordmärke och navpost. Räknat finns ingen sömposition som klarar båda: det enda fönstret är 1 px brett och kollapsar om ett typsnitt laddar annorlunda. En wipe måste skära något; regeln är att den aldrig får skära ett namn | Arkitektens beräkning ur byggarens mätvärden |
| 2026-09-10 | **Ny avvikelse, cellen står kvar som blocked:** `.tag--after` klipper den låsta bildtexten `Exempelsida: Calyx, florist i Stockholm` vid varje bredd under 640. Spillet är `0,025 × W + 12` px, alltså positivt vid varje bredd. Följdfel av plan 003 och av arkitektens eget steg 4, som bara kontrollerade `Före`-etiketten | Arkitektens räkning ur `index.html:497`, bekräftad i `K4-fold-390.png` |

## Leadens rad, 2026-09-15

| Datum | Beslut | Källa |
|---|---|---|
| 2026-09-15 | Cellen parkeras som referensmönster för före/efter-showcase, inte som helsideskoncept. Plan 004 lämnas öppen; ingen fixrunda startas. Ritningen (K3) går i stället in i V3c som processakt | Antons dom 2026-09-15, `design-catalogue/FEEDBACK.md` F-015 |

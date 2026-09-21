# R24-BRIEF — de nio felen, med kontroller

Detaljerna för runda 24. Prompten `PROMPT-V3d-R24.md` är dispensern; den här filen är
innehållet. Läs hela innan du rör en fil.

## Läget i `index.html`. Läs det här först — det sparar dig en halv runda

Rundan har körts tre gånger utan att bli färdig. **Du kör i en färsk session; filen bär allt
du behöver.** Läs i små stycken och undvik stora utskrifter — stora verktygssvar har fällt
körningen två gånger.

- **Lagt, återupprepa inte:** fel 1 (`@property --tx`, `--cx`, `--slit-p` registrerade på
  rad 258–260), fel 5 (alla sju stegen bär den nya copyn), fel 9 (steg 05:s P4-sträng står i
  filen).
- **Kvar att bygga:** fel 7 (case-ingressen står kvar ordagrant: `Vi har ingen husstil. …`)
  och fel 8 (ingen av kontaktsektionens sex ändringar).
- **Byggt men overifierat:** fel 2, 3, 4, 6. Fel 2 kan redan vara löst av fel 1 —
  registreringen av `--cx` kan ha fått `color-mix` att resolva där det föll tillbaka förut.
  **Mät, anta inte.**

Sidan är strukturellt hel: 8 `<section>` med 8 stängningar, 2 iframes, inga trasiga
redigeringar efter avbrotten.

---

# Fel 1–4. Uppmätta av lead 2026-09-20. Bevis: `shots/lead-r23/`

## 1 · `--tx` är en oregistrerad custom property

`getPropertyValue('--tx')` ger tokenströmmen `clamp(0,calc((0.3214 - 0.2258) / 0.1613),1)`,
inte ett tal. `parseFloat` ger `NaN`, som i filter och jämförelser tyst blir 0. Samma fälla
gjorde `--slit-p`-filtret verkningslöst i r18 **och** i Astras r21 och r22.

**Lagt:** `@property --tx`, `--cx` och `--slit-p` är registrerade. Ändra inga värden.

**Kontroll:** `parseFloat(getComputedStyle(el).getPropertyValue('--tx'))` ger ett tal mellan
0 och 1 i varje scrolläge, aldrig `NaN`. Samma för `--slit-p` och `--cx`. **Kör mot nuvarande
läge först, där den ska ge `NaN`** — annars mäter den ingenting.

## 2 · planets fyllning är ljusare än accenten från start

Vid scrollY 6880, 1920x930, tx ≈ 0,59: `.tes-plane` beräknas till
`oklab(0.609854 -0.0475896 -0.140082)` medan `.thesis-stage` är `rgb(30, 94, 156)`. C8 säger
att planet ska **hålla accenten till tx 0,75** och vända först över sista fjärdedelen. Den
hårda skarven mellan två blå ytor syns i `worst-6880-1920.png`.

**Gör:** se till att `.tes-plane`s bakgrund är **exakt** `var(--c-accent)` för varje
`tx ≤ 0,75`. Diagnosticera först varför `color-mix` inte ger det — den uppenbara misstanken är
att fel 1:s tokenström gjorde `calc()`-uttrycket ogiltigt så hela `color-mix` föll tillbaka.
Rätta orsaken, inte symtomet.

**Kontroll:** vid tx 0,10 / 0,40 / 0,70, vid 1920, 1440 och 390: ΔE mellan `.tes-plane`s
**renderade** fyllning och `.thesis-stage`s ska vara **≤ 1**. Mät på pixlar, inte på computed
style. Vid tx 1,0 gäller fortfarande C8:s krav ΔE ≥ 12 mot tx 0,70.

## 3 · 46 av 121 bildrutor under textytegolvet

Plan 067 Target 7:2 kräver **≥ 18 % synlig textyta i varje bildruta**. Uppmätt med riktig
hjulscroll (20 px, y5800 → y8200, 121 bildrutor): **46 under**, lägst **1,5 %**. Ingen bildruta
är helt utan text, så den delen av kravet håller.

Stämpelrutan löser slutet av draget. Det som saknas är **början**: mellan tesens sista mening
och stämpelrutans inbläckning finns en sträcka där skärmen bär nästan inget bläck.

**Gör:** lös det inom den befintliga mekaniken. Två vägar, välj med mätning och motivera i
NOTES: låt tesens sista mening ligga kvar längre så att den lämnar först när stämpelrutan
börjar bläckas (överlappa i stället för att köa), eller tidigarelägg stämpelrutans
inbläckningsfönster så att rubriken är läsbar innan planet har krympt färdigt.
**Uppfinn ingen ny form.** Stämpelrutan, klockan, landningslinjen och de fyra mätlinjerna är
rätt och ska stå kvar.

**Kontroll:** `shots/lead-r23/wheelink.py` **oförändrad**, 20 px, båda riktningarna, vid 1920,
1440 och 390: **0 bildrutor under 18 %** vid 1920/1440, och aldrig noll textlöpor vid 390.

## 4 · förhandsvisningarna siktar på det gamla tx-fönstret

`aimFlow` använder `.07 + .29 * k / 4`, plan 061:s hårdkodade tal. Plan 067 C3 ersatte dem med
uträknade `--tx-a` / `--tx-b` (0,2258 och 0,1613) och antog att målpunkterna följde med. De gör
de inte: vid `tes-till-ritning-3` ligger arket **1329 px under** viewporten. Varje granskning
som använt förhandsvisningarna har mätt fel scrolläge.

**Gör:** låt `aimFlow` för de fem lägena räkna målet ur `--tx-a` och `--tx-b` i stället för ur
de hårdkodade talen, så att `-0` landar på tx 0 och `-4` på tx 1.

**Kontroll:** vid varje av de fem lägena, vid 1920 och 390, ligger `--tx` inom **±0,03** av
0 / 0,25 / 0,5 / 0,75 / 1,0, och `.process-sheet`s rektangel skär viewporten vid `-2`, `-3`
och `-4`.

---

# Fel 5–9. Antons granskning av R23. Ordagrant: `HANDOFF-2026-09-20.md` § 3

## 5 · processektionerna

*"för trånga och texterna för långa, med siffrorna som går ihop med texterna och undersidan av
'Från samtal till lanserad sida' som klipps i underkant."*

**Gör:** (a) byt in copyn ur `COPY-V3d-r24-steg.md` § Stegen — sju steg, 28–34 ord, steg 01 är
Antons egen mening och står ordagrant. **Copyn är redan lagd i filen; kontrollera att den
stämmer.** (b) ge `.ledger-num` och `.process-p` var sin plats. (c) släpp rubriken fri i
underkant. (d) vidga spalten så copyn ryms utan att radlängden går över husets mått.

**Kontroll** vid 1920 / 1440 / 390:
- varje stegs ordantal ligger i 28–34, räknat ur den **renderade** texten,
- minsta avstånd mellan `.ledger-num`s och `.process-p`s rektanglar **≥ 16 px**, på pixlar,
- varje stegrubriks bounding box ligger **helt innanför** sin container: ingen klippt
  descender, ingen horisontell overflow.

## 6 · övergången till Exempelcase: den mörka rutan

*"väldigt dåligt gjord med en mörk ruta."* En grå/mörk rektangel ligger över papperet vid
kapitelingången. Det är `.chapter-plate` (plan 067 steg 5) som inte landar rätt — mest
sannolikt `--cp-up`-geometrin, som planen införde men aldrig verifierade. Samma klass av fel
som fel 4: ett mått flyttades utan att målpunkten följde med.

**Gör:** diagnostisera varför plattan hamnar över papperet i stället för att bläddras in.
Rätta orsaken, inte symtomet. **Rör inte stämpelrutan** — den fungerar.

**Kontroll:** rendera kapitelingången vid 1920, 1440 och 390 och **läs bilden**. Ingen mörk
eller grå rektangel får ligga över papperet i något läge. Kör kontrollen mot nuvarande läge
först, där den ska hitta rutan.

## 7 · case-ingressen är fortfarande slop

*"fortfarande fruktansvärd AI-slop, bekräfta att du förstått vad jag menar, det är väldigt
tydligt."*

Nuvarande sträng:

> Vi har ingen husstil. Formen kommer ur verksamheten, och därför valde vi de två projekt som
> ligger längst ifrån varandra.

**Varför den är slop.** Den förklarar fortfarande **sidans eget urval**. Ingen frågar varför
just de två exemplen finns på sidan. Varje mening vars ämne är *därför valde vi dessa* är
sidan som pratar om sig själv — F-018, bara i finare kläder än förra gången. Därtill öppnar
den med en negation ("Vi har ingen husstil") och besvarar sig själv i samma andetag med "och
därför", vilket är språkmodellens tvåtaktare.

**Skriv inte en tredje variant på samma stans.** Antingen handlar raden om **kundens
situation** — vad den som läser ska känna igen sig i — eller så finns den inte. Anton har
uttryckligen godkänt att rubriken `Exempelcase` får stå ensam om det ser bra ut; sätt den då
så att den bär sig, och lägg ingen lede för att fylla utrymmet.

**Kontroll:** `python ~/.agents/skills/design/scripts/self_reference_scan.py --file
runs/V3d/index.html` ger **0 träffar** i case-kapitlet. Kör mot nuvarande sträng först, där den
ska ge en `selection-justification`-träff.

## 8 · kontaktsektionen: sex ändringar

Anton: *"själva rutorna är bra gjorda … jag gillar det rena formatet."* **Behåll fältformen.**
Fältens utseende, layout och etiketter rörs inte. Det här är ytan runt dem.

1. **Animationen är för hastig.** Fokusövergången ligger på 200 ms `scaleX`. Gå till
   **320–400 ms** och en mjukare kurva.
2. **Invertera sektionen till svart**, med en snygg övergång från prissektionens bild. Detta
   **river plan 067 B11/B12**, som valde papper. Antons order går före planen; skriv
   avvikelsen i `NOTES.md`.
3. Byt `Så säger vi vad en sida kan göra för den.` → **`Så berättar vi vad vi kan göra för er.`**
4. **Lägg en bild under texten**, bredvid formuläret — till exempel visitkortets baksida.
5. **Flytta upp** `Eller mejla kontakt@alunix.se` och byt till
   **`Eller mejla oss direkt på kontakt@alunix.se`**.
6. **`Boka ett möte` på visitkortet längst upp ska länka till kontaktsektionen** (`#kontakt`).

**Kontroll:** brödtext och etiketter mot den svarta ytan klarar WCAG 2.2 AA (≥ 4,5:1 för text,
≥ 3:1 för stora rubriker) — mät, gissa inte. Övergångens varaktighet mätt ur den renderade
stilen, och läst i bildrutor så att ingen hård kant syns. Klicka `Boka ett möte` i en riktig
webbläsare och verifiera att `#kontakt` hamnar i viewporten — inte bara att `href` är satt.

## 9 · steg 05 är P4-frågan, nu besvarad

P4 har stått obesvarad genom tre sessioner. **Anton svarade 2026-09-21:** den försiktiga formen
**behålls** — texten säger aldrig att vi inte fotograferar — men textlöftet är nu utskrivet, och
bearbeta-bygga-vidare-komplettera står där han gav det. Strängen står i
`COPY-V3d-r24-steg.md` § P4 och **är redan lagd i filen**. Ändra inget annat i steg 05.

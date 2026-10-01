# V3g · R8 · showcasen utan rutor, texten i två stycken

**Modell:** Opus. Starta inga subagenter; gör hela uppdraget själv (Antons regel om samma
modellklass, `~/CLAUDE.md` § Delegering).
**Webbläsare:** bara headless, en i taget, via `tests/alunix-r8/browser_lock.py`. Server:
`python skills/design/scripts/serve.py --port 3305 --root .` från repo-roten (kör redan om
port 3305 svarar).

## Beställningen (Anton, 2026-09-29, ordagrant)

"Testa att ta bort rutorna och låta texten ta lite mer plats, gör den mer visuellt intressant
och låt den bli lite längre i 2 stycken, försök även att göra copyn mindre 'AI'-ig och mer
beskrivande kring själva processen och vägvalen, ta inspiration från webbyråerna jag nämnde."

Copyn är redan skriven och har gått igenom tre pass (copywriting, copy-editing,
humanizer-svenska): `tests/alunix-r8/runs/V3g/COPY-R8.md`. **Sätt in den ordagrant**: rubrik
till `h3`, och två `<p>` per steg. Ändra inte ett tecken. Om en mening inte ryms är det
layouten som ska ändras, inte texten.

## Läs först

1. `runs/V3g/EFFECTS.md`: de skyddade effekterna. Följande får inte bli sämre:
   - pinnen, som skapas en gång;
   - övertoningen mellan stegen;
   - räknaren och mintspåret;
   - casebytet utan hopp.
2. `design-catalogue/FEEDBACK.md` F-019 till F-022, som är bindande:
   - stegrubriken i h3-skala (28–32 px);
   - inga jättesiffror och inga ornament eller streck för att fylla yta;
   - tom yta löses med innehåll eller komposition.
3. `runs/V3g/SHOWCASE-SPEC.md` § C, som beskriver dagens ruta, och den nuvarande markupen i
   `runs/V3g/index.html` (sök `showcase-rows`, `showcase-box-head`, `showcase-detail`).

## Vad som ändras (bara desktop ≥ 768; mobilens staplade rader behålls)

1. **Rutorna bort.** Under casehuvudet (rost/lack, orört) blir högerkolumnen en enda
   sammanhängande yta: Calyx `--paper`, Hōrai `--black`. Inga cellkanter, ingen
   bakgrundsväxling och inga skarvar mellan räknaren, texten och luppen.
2. **Räknaren och mintspåret** står kvar överst, som en rad direkt på ytan, utan box
   (skyddad effekt).
3. **Texten tar mer plats.**
   - `h3` ligger kvar i 28–32 px.
   - Första stycket är ingress, 20–22 px, radavstånd ca 1,4, full textfärg.
   - Andra stycket är 16–17 px, radavstånd ca 1,55, i sekundärfärg. Calyx `#4a4a4a`; Hōrai
     `#bdbdbd`. Mät ≥ 4,5:1.
   - Mått högst ca 46ch. Luft mellan rubrik, ingress och stycke enligt husets 8-skala.
4. **Visuellt intresse med innehåll, inte ornament.** Luppen (`.showcase-figure`, en detalj ur
   sajten själv) förlorar sin ram och sin cell. Den blir ett fritt utsnitt som ligger lågt i
   kolumnen och bryter ut över skarven mot iframen med ca 48 px. Det är sidans enda
   grid-break i showcasen.
   - Textblocket och luppen får aldrig överlappa varandra. Mät med `getBoundingClientRect` i
     varje steg.
   - Rastrets upplösning i luppen behålls.
   - Vid viewporthöjd under ca 860 px får luppen krympa, men den får aldrig kapa text.
5. **Övertoningen** gäller hela steget: rubrik och två stycken. Det andra stycket följer det
   första med ca 60 ms förskjutning inom samma fönster. Fortfarande bara `opacity` och
   `transform`, skrubbat av samma pin.
6. **Mobil:** raderna får båda styckena, samma typsnittsstorlekar som i dag (ingress ett steg
   större), och inga rutor runt raderna om det går utan att bryta layouten.

## Invarianter

- Ingen text klipps, i något steg, i båda casen, vid 1440×900, 1280×800, 1920×1080 och 390×844.
  Kontroll: `scrollHeight > clientHeight` på textblocket, plus att dess botten ≤ kolumnens
  botten.
- `section_probe.py` på hela sidan mot baslinjen (`runs/V3g/shots/section-probe-baseline.json`):
  ingen sektion sämre. Showcasens p95 får inte gå över dagens.
- 0 px horisontellt överflöd på 390/768/1440/1920 och 0 konsolfel.
- Copy: ingen annan synlig text ändras. Kör `verify.py`. De nya stegtexterna ska matcha
  `COPY-R8.md` exakt; lägg till en kontroll som jämför.

## Leverans

- `runs/V3g/index.html`.
- Ett R8-avsnitt sist i `runs/V3g/RAPPORT.md` med uppmätta värden, skärmbilder i
  `runs/V3g/shots/r8/` och en rad per ändring. Skärmbilderna:
  - båda casen, steg 1 och ett mittsteg, vid 1440 och 1280×800;
  - ett mellanläge av övertoningen;
  - mobil 390.
- En rad per Skill- eller MCP-anrop du gjorde, med vad det ändrade.

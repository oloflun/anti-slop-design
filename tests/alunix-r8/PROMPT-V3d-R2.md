# Alunix, V3d runda 2: fixrundan. Cell {{KONCEPT}}, ut-mapp `{{UT_MAPP}}`, port {{PORT}}.

Du byggde runda 1. Astra har granskat nivån mot referenserna i paritetsläget och svarat `fix`
med åtta verifierade material_fixes: `{{UT_MAPP}}/reviews/r1-astra.md` § material_fixes. Lead
har läst dem mot pixlarna och **tar alla åtta**. Det här är den enda fixrundan som är planerad.
Allt ska vara klart när den är slut.

## 0. Först
1. `Skill(design)`, `Skill(animate)`, `Skill(emil-design-eng)` via Skill-verktyget.
2. Läs `{{UT_MAPP}}/reviews/r1-astra.md` i sin helhet, både § fidelity (paritetsraderna)
   och § material_fixes.
3. Skriv `{{UT_MAPP}}/plans/049-fixrundan.md` (samma format som 048). Problem ska vara Astras
   fynd med hans mätvärden. Target ska vara hans "Expected". Ordningen: 1 och 2 först, de är
   funktionsfel. Därefter 3, 4 och 5, sedan 7, och till sist 6 och 8.

## 1. Bygg, fixarna 1–8
Varje fix är en synlig förbättring. Ingen av dem får lösas genom att backa ett djärvt drag
från runda 1, alltså genom att göra arket, siffrorna eller rubrikerna mindre, eller genom att
ta bort scenen. Tre av fixarna kräver beslut som du fattar och motiverar i planen:

- **Fix 6, P04:** jättesektionen ska få ett eget intervall där den svarta plåten äger skärmen.
  Välj den minsta ändring av `.stagger`-geometrin som ger det, och pröva den mot par-bilden
  P04.
- **Fix 6, P03:** Hyperborea ska vara minst 40 % vw i tesintervallet. Bandets balans från
  runda 1 får inte gå förlorad: Calyx och Hōrai ska fortfarande stå sida vid sida.
- **Fix 7:** kodan efter steg 07 ska antingen bort eller bli en egen scen. Varje steg ska
  ändra arket synligt, också vid 390.

Kirurgiska `Edit`, aldrig `Write` av hela filen. Låst copy 15/15 ordagrant, och noll
tankstreck i synlig text. F-011 och F-014 gäller. Motorn `scroll/*.js`, `scrollcraft.css` och
`sites/*` rörs aldrig. Ingen tredje iframe. Antalet inline-hex får inte öka.

## 2. Verifiera, innan du kallar något klart
1. Mät varje fix mot sitt Expected i Astras rapport. Ta talen med skript. För kamerans
   transform: läs den beräknade `transform` och applicera matrisen själv, lita inte på
   `getBoundingClientRect` under navigering.
2. Ta nya par-bilder för alla PARITET-rader vid 1440 och 390 till `{{UT_MAPP}}/shots/r2/par/`,
   **en skärmbild per sida**. Inga ihopsydda helsidesbilder: runda 1:s P15 fick en syskarv
   som dubblerade rubriken. Läs varje bild själv. Håller en rad inte nivån, laga den i samma
   runda.
3. Ta hjulscrollsekvenser, alltså Playwright `mouse.wheel`, inte `scrollTo`, genom hela
   processakten vid 1440 och 390, var 150:e px, till `{{UT_MAPP}}/shots/r2/wheel-1440/` och
   `wheel-390/`. Läs dem och bekräfta att fix 5 håller: ingen glyfspringa, inga halva band.
   Bekräfta också att varje steg ändrar arket.
4. Hela grinden ur `PROMPT-V3d-R1.md`: `scroll_verify`, `motion_probe` med kontrollen först
   (båda riktningarna, `#process` också vid 390), `contrast_over_media --url`, `a11y_scan` och
   `reflow` vid 390 och 768, noll horisontell scroll 320–1440, samt grep för tankstreck,
   `prefers-reduced-motion` och inline-hex.

## 3. Leverans
`{{UT_MAPP}}/index.html`, `plans/049-*.md`, `shots/r2/` och `NOTES.md` § V3d R2 med en tabell:
fix, Expected, uppmätt före, uppmätt efter, par-bild. Sista raden ska vara `V3d R2 klar` eller
`[PAUSED — steg X]`.

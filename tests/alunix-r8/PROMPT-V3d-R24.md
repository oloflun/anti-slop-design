# Alunix, V3d runda 24: övergången tes → ritning, tre fel. Cell {{KONCEPT}}, ut-mapp `{{UT_MAPP}}`, port {{PORT}}.

R23 byggde plan 067 i sin helhet. **Stämpelrutan fungerar och rörs inte** — rubriken sitter
inne i rektangeln med landningslinjen som överlinje, steg 01 kliver in i vänsterspalten i
samma bildruta, och arket är 1311 px vid 1920. Tvåspaltsakten, case-kapitlet, priset och
kontaktsektionen är byggda och ska inte backas.

Den här rundan har **tre fel**, alla i övergångens tidiga fas, alla uppmätta av lead
2026-09-20. Bevisen ligger i `{{UT_MAPP}}/shots/lead-r23/`
(`worst-6880-1920.png`, `wheelink-1920.json`, `probe-1920.json`).

## Fel 1 — `--tx` är en oregistrerad custom property, så varje mätning av akten ljuger

`getPropertyValue('--tx')` ger tokenströmmen `clamp(0,calc((0.3214 - 0.2258) / 0.1613),1)`,
inte ett tal. `parseFloat` på den ger `NaN`, som i filter och jämförelser tyst blir 0.

Det är inte ett nytt fel, det är ett **upprepat** fel: samma fälla gjorde `--slit-p`-filtret
verkningslöst i både r18:s och Astras r21-körning, och den lurade lead i R23:s första
mätning till att tro att draget inte hade börjat.

**Gör:** registrera de custom properties som mäts, med `@property`:

```css
@property --tx   { syntax:'<number>'; inherits:true; initial-value:0; }
@property --slit-p { syntax:'<number>'; inherits:true; initial-value:0; }
@property --cx   { syntax:'<number>'; inherits:true; initial-value:0; }
```

Registrera varje ytterligare numerisk property som något skript läser. Ändra inga värden och
ingen logik — det här är en deklaration, inte en omskrivning.

**Kontroll:** `parseFloat(getComputedStyle(el).getPropertyValue('--tx'))` ger ett tal mellan
0 och 1 i varje scrollage, aldrig `NaN`. Samma för `--slit-p` och `--cx`. Kör kontrollen mot
nuvarande läge först, där den ska ge `NaN` — annars mäter den ingenting.

## Fel 2 — planets fyllning är ljusare än accenten från start

Uppmätt vid scrollY 6880, 1920x930, tx ≈ 0,59: `.tes-plane` beräknas till
`oklab(0.609854 -0.0475896 -0.140082)` medan `.thesis-stage` är `rgb(30, 94, 156)`.

C8 säger att planet ska **hålla accenten till tx 0,75** och vända först över sista
fjärdedelen. Vid tx 0,59 ska fyllningen alltså vara oskiljbar från tesbandet. Den är det
inte, och resultatet syns i `worst-6880-1920.png` som två blå ytor med en hård vågrät skarv
mellan sig.

**Gör:** se till att `.tes-plane`s bakgrund är **exakt** `var(--c-accent)` för varje
`tx ≤ 0,75`. Diagnosticera först varför `color-mix` inte ger det (den uppenbara misstanken är
att procentandelen inte resolverar till `0%` som avsett, eller att fel 1:s tokenström gör
`calc()`-uttrycket ogiltigt så hela `color-mix` faller tillbaka). Rätta orsaken, inte
symtomet.

**Kontroll:** vid tx 0,10 / 0,40 / 0,70, vid 1920, 1440 och 390: ΔE mellan `.tes-plane`s
renderade fyllning och `.thesis-stage`s ska vara **≤ 1**. Mät på renderade pixlar, inte på
computed style. Vid tx 1,0 gäller fortfarande C8:s krav ΔE ≥ 12 mot tx 0,70.

## Fel 3 — 46 av 121 bildrutor under textytegolvet

Plan 067 Target 7:2 kräver **≥ 18 % synlig textyta i varje bildruta** vid 1920/1440. Uppmätt
med riktig hjulscroll (20 px, y5800 → y8200, 121 bildrutor): **46 bildrutor under**, lägst
**1,5 %**. Ingen bildruta är helt utan text, så den delen av kravet håller.

Stämpelrutan löser slutet av draget. Det som saknas är **början**: mellan tesens sista mening
och stämpelrutans inbläckning finns en sträcka där skärmen bär nästan inget bläck.

**Gör:** lös det inom den befintliga mekaniken. Två vägar, välj med mätning och motivera i
NOTES:
- låt tesens sista mening ligga kvar längre, så att den lämnar först när stämpelrutan börjar
  bläckas (överlappa i stället för att köa), eller
- tidigarelägg stämpelrutans inbläckningsfönster ytterligare, så att rubriken är läsbar
  innan planet har krympt färdigt.

**Uppfinn ingen ny form.** Stämpelrutan, klockan, landningslinjen och de fyra mätlinjerna är
rätt och ska stå kvar.

**Kontroll:** samma svep, 20 px, båda riktningarna, vid 1920, 1440 och 390: **0 bildrutor
under 18 %** vid 1920/1440, och aldrig noll textlöpor vid 390. Skriptet ligger i
`{{UT_MAPP}}/shots/lead-r23/wheelink.py` och återanvänds oförändrat.

## Fel 4 — förhandsvisningarna siktar på det gamla tx-fönstret

`?preview=tes-till-ritning-0` … `-4` siktar via `aimFlow` på `.07 + .29 * k / 4`, alltså
plan 061:s hårdkodade fönster. Plan 067 C3 ersatte det med uträknade `--tx-a` / `--tx-b`
(uppmätt: 0,2258 och 0,1613), och planens 7.4 antog felaktigt att målpunkterna skulle följa
med automatiskt. De gör de inte: vid `tes-till-ritning-3` ligger arket 1329 px **under**
viewporten.

Det är ett verifieringsfel, inte ett synligt fel — men det gör att varje granskning som
använder förhandsvisningarna mäter fel scrollägen.

**Gör:** låt `aimFlow` för de fem lägena räkna målet ur `--tx-a` och `--tx-b` i stället för
ur de hårdkodade talen, så att `-0` landar på tx 0 och `-4` på tx 1.

**Kontroll:** vid varje av de fem lägena, vid 1920 och 390, ligger `--tx` inom **±0,03** av
0 / 0,25 / 0,5 / 0,75 / 1,0, och `.process-sheet`s rektangel skär viewporten vid `-2`, `-3`
och `-4`.

## Invarianter
- Motorn `scroll/*.js` och `scrollcraft.css` rörs aldrig. `sites/*` rörs aldrig.
- Exakt två levande iframes. Ramarna transformeras aldrig. F-011 och F-014 gäller.
- Astras § keep ur r21/r22: R21:s borttagning (`position:absolute`, aldrig `fixed`), R22:s
  två fixar, r18:s fyra fixar. Får inte regressera.
- R23:s egna resultat får inte backas: stämpelrutan, tvåspaltsakten, arkets 1311 px,
  case-kapitlets storlek och luft, prissektionen utan serif, kontaktsektionen.
- Gate 48, gate 99 / F-016, F-018. Inga tankstreck. Låst copy 11 rader.

## Verifiera
- Alla fyra kontroller ovan, **var och en körd mot nuvarande (trasigt) läge först** så att du
  ser att den hittar felet. En kontroll som ger grönt mot både trasigt och lagat mäter
  ingenting, och det har hänt tre gånger i det här projektet.
- Enskilda skärmbilder, aldrig kontaktark som bevis. Chromium med
  `ignore_default_args=['--hide-scrollbars']`, `mouse.wheel`, en skärmbild per sida.
- Kort grind: 0 horisontell scroll 320–1920, 0 JS-fel, rubrikskriptet, låst copy.
- **Kör därefter hela plan 067 § Verification A/B/C**, som R23 aldrig hann med på grund av
  full disk. Det är den körningen som avgör om R23 plus R24 kan kallas klara.

Leverans: `NOTES.md` § V3d R24 med en tabell per fel: mål, före, efter, bild. Sista raden ska
vara `V3d R24 klar` eller `[PAUSED — fel X]`.

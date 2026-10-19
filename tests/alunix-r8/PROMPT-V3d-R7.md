# Alunix, V3d runda 7: tesbandet, övergången och Exempelcase. Cell {{KONCEPT}}, ut-mapp `{{UT_MAPP}}`, port {{PORT}}.

Antons nya beställning 2026-09-19 är planerad av arkitekten i
`{{UT_MAPP}}/plans/054-tesband-och-case.md`. Copy-kedjan är redan körd, med
humanizer-svenska sist, och texten ligger i `{{UT_MAPP}}/COPY-V3d-final.md`. **All synlig text
skrivs in ordagrant från kolumnen `final`.** Du ändrar ingen sträng. Om en sträng inte får
plats eller inte fungerar i layouten, stoppa och skriv en rad i NOTES i stället för att
skriva om den.

## 0. Först
1. `Skill(design)`, `Skill(animate)` och `Skill(emil-design-eng)` via Skill-verktyget.
2. Läs plan 054 i sin helhet. Läs sedan `COPY-V3d-final.md`, `PARITET.md` (P03, P04, P14 och
   P17–P20 är nya eller omskrivna) och `{{UT_MAPP}}/reviews/r6-astra.md`.

## 1. Bygg, i planens ordning
Plan 054:s Steps 1–5:
- tesbandet som en egen pinnad sektion där meningarna byts ut, med "Vi hjälper er att synas
  på rätt sätt." inskriven,
- jättesektionen borttagen och ridån till processen,
- den förenklade copyn,
- "Hur vi tänker" ersatt av kapitelskärmen och Exempelcase: Calyx med texten till vänster
  och sajten till höger, bryggan, sedan Hōrai spegelvänt,
- balansen över hela sidan.

Ta också Astras två kvarvarande fynd från r6:
- `.process-p` vid 768–1023 behöver `grid-row:3` i media-frågan, så att brödtexten inte
  ligger över siffran och noten.
- Revisionsfältet vid 390 får inte gå in över fotot. Det ligger 2 px in i dag.

Planens stoppregel gäller: blir de levande ramarna för tunga i mätningen, stoppa och
rapportera. Byt inte själv till skärmbildsvägen.

Kirurgiska `Edit`, aldrig `Write` av hela filen. Låst copy ordagrant. F-011 och F-014 gäller.
Motorn `scroll/*.js`, `scrollcraft.css` och `sites/*` rörs aldrig. Exakt två iframes. Antalet
inline-hex får inte öka. Inget djärvt drag får backas för att laga ett fel.

## 2. Verifiera, innan du kallar något klart
1. Varje Target i plan 054 mäts med skript och med bild, positionerna nådda med
   `mouse.wheel`. Mät särskilt:
   - att varje tesmening äger rubrikplatsen i sitt eget intervall,
   - att Calyx- och Hōrai-sajterna rullar i takt med sidan i båda riktningarna, med högst
     2 px avvikelse,
   - att ingen ram någonsin visas tom.
2. Hjulsekvenser, var 150:e px, genom hela sidan vid 1440, 1024, **768** och 390. Lägg dem i
   `{{UT_MAPP}}/shots/r7/wheel-<bredd>/` och läs dem. Bredden 768 är obligatorisk: förra
   rundan missade ett överlapp där.
3. Par-bilder för alla PARITET-rader, en skärmbild per sida, till `{{UT_MAPP}}/shots/r7/par/`.
   Läs dem. Laga det som inte håller nivån i samma runda.
4. Hela grinden:
   - `scroll_verify`,
   - `motion_probe` med kontrollen först, båda riktningarna, `#process` och den nya
     tessektionen, samt case-sektionerna med ramarna levande,
   - `perf_probe` (sidvikt och tid per bildruta med två scrollade iframes),
   - `contrast_over_media --url`,
   - `a11y_scan` och `reflow` vid 390 och 768, samt `tab_walk`,
   - noll horisontell scroll 320–1920,
   - rubrikskriptet från R3 (noll delade ord i någon rubrik eller tesmening, 768–1920),
   - grep för tankstreck, `prefers-reduced-motion` och inline-hex.

## 3. Leverans
- `{{UT_MAPP}}/index.html` och `shots/r7/`.
- `NOTES.md` § V3d R7 med en tabell: Target, mål, uppmätt, bild.
- Sista raden ska vara `V3d R7 klar` eller `[PAUSED — steg X]`.

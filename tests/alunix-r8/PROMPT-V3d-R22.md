# Alunix, V3d runda 22: konturen sluter sig om arket. Cell {{KONCEPT}}, ut-mapp `{{UT_MAPP}}`, port {{PORT}}.

Läs `{{UT_MAPP}}/reviews/r21-astra.md` § material_fixes. Svaret är `fix`, med **två**
fynd, båda i blåkopian. Astra dömer i övrigt övergången som färdig och listar i § keep allt
som inte får regressera. Rundan har exakt dessa två fixar. Ingenting annat rörs.

## Fix 1 — konturen ritar bara två vågräta streck, inte en rektangel
`index.html:1189–1190`. `box-shadow:inset` målar ringen vid elementets **egen** border-box,
och `.tes-plane` är `left:50%;width:100vw;translateX(-50%)`, alltså x −5 … vw+5. `clip-path`
flyttar inte ringen, den klipper bort den. Uppmätt: skuggans sidor ligger på x −5 respektive
1915 i **varje** tx-läge, medan den klippta rektangeln ligger på 254…1647 (t3). Läsaren ser
en fylld rektangel vars sidor ligger 84–178 px (1920) utanför de vita linjer som ska vara
arkets kanter, genom hela tx 0,6→1,0.

**Mål:** konturens fyra sidor följer den klippta rektangeln, vid varje tx och vid varje
bredd. Kommentaren på rad 1186–1188 påstår motsatsen om `box-shadow:inset` och ska rättas
samtidigt, inte lämnas kvar som fel dokumentation.

Den lata vägen är ett `::after` på `.tes-plane` med samma `inset`-tal som `clip-path`
(`calc(var(--tx) * var(--pl-t,0px))` osv., botten 0) och `border:2px solid` i samma
`--p-edge`-toning. Elementet har inget `::after` i dag. Väljer du en annan lösning ska den
nå samma mätvärde. Ingen ny scroll-lyssnare, ingen ny JS-tillståndsmaskin — R21 tog bort en
sådan och § keep förbjuder att den kommer tillbaka.

## Fix 2 — slutrektangeln landar +5 / −6 px fel
`index.html:2538–2539`. `--pl-r` räknas som `window.innerWidth − x4` och `--pl-l` som `x1`,
men planet är `100vw` och börjar på −5 (rullningslisten ligger utanför `clientWidth`).
Uppmätt vid t4: klippt vänsterkant 341 / 126 / 11 mot `--x1` 346 / 131 / 16, högerkant
1558 / 1293 / 358 mot `--x4`+2 1564 / 1299 / 364.

**Mål:** `--pl-l` och `--pl-r` räknas mot planets **egna** kanter
(`getBoundingClientRect()` på `.tes-plane`), så den klippta rektangeln vid tx = 1
sammanfaller med `--x1`/`--x4` inom ±1 px vid 1920, 1440 och 390. Felet är osynligt i dag
bara för att fyllningen är identisk med grunden vid tx = 1 — det blir en dubbel kant i
samma ögonblick fix 1 landar, så fix 2 måste med i samma runda.

## Gör
- `Skill(design)` först.
- Skriv planen `{{UT_MAPP}}/plans/066-konturen.md`, kort: två Targets, mätvärde per Target.
- Kirurgiska `Edit`. Motorn, `scrollcraft.css` och `sites/*` rörs aldrig. Exakt två iframes.
  Ramarna transformeras aldrig. F-011 och F-014 gäller. Inga inline-hex tillkommer. Ingen
  copy ändras. Inget i Astras § keep får regressera.

## Verifiera
1. **Fix 1, på renderade pixlar:** vid `?preview=tes-till-ritning-2` och `-3`, vid 1920,
   1440 och 390, ska en 2 px ljus kolumn finnas inom ±1 px av planets klippta vänster- och
   högerkant. Mät i PNG, inte i CSS. Kör samma prov mot nuvarande läge först, så att du ser
   att det hittar felet.
2. **Fix 2:** `contour2.py`-motsvarande mätning vid `tes-till-ritning-4`: `sideGapLeft` och
   `sideGapRight` ≤ 1 px vid 1920, 1440 och 390.
3. **Regressionsvakt:** kör `plane21.py`-motsvarigheten (20 px-hjul i båda riktningarna
   genom tes → ritning vid 1920, 1440, 390 och 768) och kräv 0 träffar av text i eller
   bakom konturen och `position:absolute` i varje bildruta, `fixed` aldrig. Astras skript
   ligger i `{{UT_MAPP}}/shots/astra-r21/`; återanvänd det i stället för att skriva ett nytt.
4. Enskilda skärmbilder (aldrig kontaktark) av t1–t4 vid 1920, 1440 och 390 till
   `{{UT_MAPP}}/shots/r22/`. Läs dem.
5. Kort grind: noll horisontell scroll 320–1920, rubrikskriptet (noll delade ord), låst copy
   14/14, noll tankstreck.

Leverans: `NOTES.md` § V3d R22 med en tabell över fix, mål, före, efter och bild. Sista
raden ska vara `V3d R22 klar` eller `[PAUSED — steg X]`.

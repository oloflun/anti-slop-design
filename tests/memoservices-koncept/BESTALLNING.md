# Beställning: konceptskiss av memoservices.se (Antons beställning 2026-10-12)

Det här dokumentet är en **beställning**. Det beskriver vilka sidor, vilket innehåll och vilka funktioner som ska finnas, men inte hur sidan ska se ut. Designriktningen tar designkedjan fram själv (`Skill(design)`, Tier 1: härled från varumärket nedan). Ingenting här är ett förslag om layout, komposition eller rörelse.

## 0. Syfte och ramar

- **Vad:** en konceptskiss av MemoServices AB:s webbplats (memoservices.se). Anton Lundin visar den för vd:n Linda Swartling i en intervju om rollen som AI Engineer. Intervjun är **tisdag 2026-10-13 kl. 11:00 i Teams**, och sidan ska kunna visas via skärmdelning.
- **Poängen:** visa (1) att varje tjänsteområde kan få en egen sida och (2) en fungerande AI-funktion, **Kvittotolken**, som bygger på flödet i deras egen artikel. Dagens sajt är byggd i Webflow och har ett genomarbetat tokensystem. Det här är en vidareutveckling, ingen ersättning av en mall, och inget i skissen ska antyda något annat.
- **Inte publik.** Den publiceras bara på en privat förhandsadress och aldrig på en domän som liknar deras (se § 8).

## 1. Leveransens omfattning

**Ska byggas (9 sidor + 1 funktion):**

| # | Sökväg | Sida |
|---|---|---|
| 1 | `/` | Startsida |
| 2 | `/tjanster` | Översikt över tjänsterna |
| 3 | `/tjanster/redovisning` | Tjänstesida + **Kvittotolken** (§ 5) |
| 4 | `/tjanster/hr-och-rekrytering` | Tjänstesida |
| 5 | `/tjanster/skatt` | Tjänstesida |
| 6 | `/tjanster/juridik` | Tjänstesida |
| 7 | `/tjanster/finans-och-ma` | Tjänstesida |
| 8 | `/tjanster/governance-risk-och-compliance` | Tjänstesida |
| 9 | `/tjanster/operativ-effektivisering` | Tjänstesida (länkar till Kvittotolken, § 3.3) |

**Ska inte byggas.** Länka i stället till originalet på memoservices.se: Insikter och alla artiklar, Karriär, Kontakt, Integritetspolicy, Cookies och AI Act. Kartläggningen ligger på assess.memoservices.no och ska bara länkas, inte byggas om.

**Prioritet om tiden inte räcker:** (1) Redovisning med Kvittotolken, (2) de sex andra tjänstesidorna, (3) översikten, (4) startsidan.

## 2. Innehållsregel (bindande)

1. **All text kommer ordagrant från dagens sajt.** Källorna, strukturerade och kontrollerade:
   - `content/tjanster.json`: översiktens ingress och alla sju tjänster (rubrik, ingress, brödtext, 4 × "Passar för", leveransrubrik, 6 × leverans, CTA, kortet på startsidan, mosaikfärger)
   - `content/start.json`: alla avsnitt på startsidan i ordning
   - `content/delat.json`: navigation, sidfot och kontaktperson
   - Råtext för varje sida finns i `evidens/*.txt` och skärmbilder i `evidens/*.png`. JSON-filerna genereras av `content/parse_*.py` och kan köras om.
2. **Ingenting skrivs om, kortas, förlängs eller "förtydligas"**, inte heller av copy-grinden (F-028). Versaler och gemener följer originalet. Kända fel i originalet lämnas som de är och listas i handoffen som förslag:
   - "längre fram.." (Skatt, Passar för 3)
   - "egen jurist" utan punkt (Juridik, Passar för 1)
   - datum i engelskt format ("September 7, 2026") på insiktskorten.
3. **Text får bara skapas på följande ställen**, och den går då genom copy-grinden (copywriting → copy-editing → humanizer-svenska):
   - konceptbannern (§ 7)
   - alla texter i Kvittotolken (§ 5.7)
   - etiketter för navigering mellan tjänsterna (föregående/nästa och undermeny), som bara får använda tjänstenamnen
   - `<title>` och meta description för de nya undersidorna, byggda av tjänstens namn och ingress.
4. **Ingenting påhittat:** inga kunder, citat, siffror, medarbetare, logotyper eller resultat.
5. **Kontrollen körs maskinellt:** byggaren skriver eller använder ett skript som läser den renderade texten på varje sida och kontrollerar att varje textnod antingen finns ordagrant i `content/*.json` eller i listan med ny text i § 5.7 och § 7. Skriptet ska ge 0 avvikelser.

## 3. Sidorna, en och en

### 3.1 Startsida `/` (källa: `start.json`)
Avsnitten och deras innehåll, i originalets ordning. Ordningen får ändras om designen kräver det, men inget avsnitt får falla bort:
1. **Hero:** kicker, rubrikens två rader, lead, ingress och två knappar. "Se tjänsterna" leder till `/tjanster` och "Gör kartläggningen ↗" till assess (extern).
2. **Tjänsteområden:** kicker, rubrik och länken "Läs mer om tjänsterna →" till `/tjanster`. Sju poster med tjänstens mosaik, namn och startsidetext (`kort_pa_startsidan`) och "Läs mer →". **Varje post länkar till sin egen tjänstesida.** Dessutom posten "Behöver du hjälp inom flera områden?" med text och "Kontakta oss →", som leder till kontaktsidan i original.
3. **Kartläggning:** kicker, rubrik, text och knappen "Starta kartläggningen ↗" till assess.
4. **Om:** måste ha ankaret `id="om"`, eftersom navigationens "Om oss" pekar dit. Innehåll: kicker, två rubrikrader, text, koncernraden med länk och fyra punkter med originalets fetstil (`punkter_fetstil`).
5. **Insikter:** rubrik, länken "Alla artiklar och nyheter →" och tre artikelkort (kategori · datum, rubrik, utdrag). Korten länkar till artiklarna på originalsajten.

### 3.2 Översikt `/tjanster` (källa: `tjanster.json → oversikt` + `tjanster[]`)
- Kicker "TJÄNSTER", rubriken "SJU TJÄNSTEOMRÅDEN. ETT AVTAL." och ingressen.
- De sju tjänsterna, var och en med mosaik, namn, ingress (`ingress`) och länk till sin sida.
- Inga ankare längre. Det här är nu en sida för att komma vidare, inte en lång sida där man scrollar till rätt ställe.

### 3.3 Tjänstesida `/tjanster/<slug>` (samma mall, sju gånger; källa: `tjanster[slug]`)
Varje sida innehåller alla dessa delar, ordagrant:
1. Tjänstens **mosaik** (§ 4) och **rubrik**
2. **Ingress**
3. **Brödtext**
4. **"PASSAR FÖR"** med fyra poster. Varje post har frågan och svaret som separata fält.
5. **Leveransrubriken** och **sex leveranser**, var och en med namn och text
6. **"Prata med oss →"**, som leder till kontaktsidan i original
7. **Vidare till kartläggningen** ("Gör kartläggningen ↗", samma etikett som i originalets navigering)
8. **Navigering till föregående och nästa tjänst**, med deras mosaik och namn, så att man kan gå runt mellan alla sju. Ordningen följer `tjanster.json`, och den sista leder till den första.

Särskilt:
- **Redovisning** har Kvittotolken (§ 5) som en egen del av sidan.
- **Operativ effektivisering** har en länk till Kvittotolken på Redovisningssidan, kopplad till leveransen "Automatisering". Länktexten är ny och går genom copy-grinden.
- Webbadressen `/tjanster#<slug>` (dagens ankare) ska skicka vidare till `/tjanster/<slug>`, så att gamla länkar fungerar.

### 3.4 Delat på alla sidor (källa: `delat.json`)
- **Huvudmeny:** samma poster som i originalet. "Tjänster" leder till `/tjanster` och måste **dessutom ge direkt åtkomst till alla sju tjänstesidorna**, till exempel via en undermeny eller en panel. Hur det ser ut är designerns val. Det måste fungera med mus, tangentbord och på mobil.
- **Knappen "Kontakta oss"** leder till kontaktsidan i original.
- **Mobilmeny** med samma innehåll.
- **Sidfot** med adress, e-post (`mailto:`), kolumnerna TJÄNSTER (de sju sidorna), FÖRETAGET och JURIDISKT, copyright, koncernraden och länk till memoservices.no. "Cookie-inställningar" tas bort, eftersom skissen inte använder cookies.
- **Konceptbanner** (§ 7).
- **Logotypen** leder till `/`.

## 4. Mosaiken (varumärkets identitetsform, ska finnas med)

**Detta är fakta om originalet, mätt 2026-10-11:**
- Varje tjänsteområde har en **2×2-mosaik** med **tre rutor i tjänstens huvudfärg och en accentruta nere till höger**. Mosaiken visas i originalet på tjänstekorten på startsidan.

| Tjänst | Huvudfärg | Accent |
|---|---|---|
| Redovisning | `#2c546d` | `#c5eb43` |
| HR och rekrytering | `#6dabbf` | `#c5eb43` |
| Skatt | `#8b5e3c` | `#f3aaaf` |
| Juridik | `#4b4b4b` | `#e72835` |
| Finans och M&A | `#9db377` | `#2c546d` |
| Governance, risk & compliance | `#294b3f` | `#c5eb43` |
| Operativ effektivisering | `#b1b0aa` | `#ee646e` |

- **Hero-mosaiken** på startsidan består av 25 rundade rutor (51 px vid 1440 px bredd, hörnradie 10 px, 8 px mellanrum) i tjänstefärgerna plus brandröd. De animeras in med en fjädrande rörelse (`msIn`, `cubic-bezier(0.34, 1.56, …)`) och flyttar sig sedan. Skärmbild: `evidens/start-fold.png`.

**Krav (funktion, inte form):**
1. Varje tjänst ska kännas igen på sin mosaik **överallt där den förekommer**: på startsidan, i översikten, på den egna sidan, i föregående/nästa och i undermenyn.
2. Färgerna ovan är låsta. Varje tjänstesida ska bära sin tjänstes färg som identitet. Hur färgen används bestämmer designen.
3. Startsidan ska ha en mosaik i hero som rymmer alla sju tjänsternas färger, så att idén "sju områden, ett avtal" finns kvar. Om och hur den rör sig bestämmer designen.

## 5. Kvittotolken (AI-funktion på Redovisningssidan)

### 5.1 Underlag (läs före bygget)
- `evidens/insikter-fran-kvitto-till-bokfort-helt-automatiskt.txt`: deras artikel "Från kvitto till bokfört – helt automatiskt" (29 maj 2026). Stegen i Kvittotolken är artikelns steg.
- `evidens/ai-forordningen.txt`: deras AI-policy. Tre krav gäller direkt:
  - "alla leveranser granskas av en kvalificerad medarbetare"
  - "Om du interagerar direkt med ett AI-system … informerar vi tydligt om det"
  - "Kunddata används inte för att träna externa AI-modeller"

### 5.2 Vad användaren kan göra
1. **Välja ett av tre exempelkvitton** med ett klick. Det här är huvudvägen i intervjun: demon fungerar utan uppladdning och ger samma resultat varje gång.
2. **Ladda upp ett eget kvitto** (JPG, PNG, HEIC eller PDF, max 10 MB). På mobil kan man i stället **fotografera** med kameran (`accept="image/*" capture`).
3. **Börja om** med ett nytt kvitto.
4. **Se resultatet steg för steg** (§ 5.3) och **visa råtexten** som modellen läste.

### 5.3 Stegen (artikelns ordning; varje steg har ett eget tillstånd)

| # | Artikelns steg | Vad som visas | Status |
|---|---|---|---|
| 1 | "systemet läser texten automatiskt" | Kvittobilden och den tolkade texten | Riktigt |
| 2 | "leverantör och belopp identifieras" | Leverantör, datum, kvittonummer om det finns, totalbelopp inkl. moms, betalsätt om det framgår | Riktigt |
| 3 | "momsen beräknas" | Per momssats: underlag, sats och momsbelopp. Netto och totalbelopp. Kontrollen "går ihop" eller "går inte ihop" | Riktigt. Kontrollen görs i kod, inte av modellen |
| 4 | "rätt konto föreslås" | Kontoförslag ur den låsta BAS-listan (§ 5.5) med en kort motivering. Konteringsförslag: kostnadskonto debet, 2641 debet, motkonto kredit | Riktigt |
| 5 | "transaktionen matchas mot bank- eller kortköpet" | Visas som ett steg som **inte ingår i demon** och kräver koppling till bank | Inte byggt. Det ska sägas tydligt |
| 6 | "verifikationen bokförs" | Status **"Förslag, granskas av redovisningskonsult"**. **Aldrig "bokfört"** | Följer AI-policyn |

### 5.4 Osäkerhet och fel (tillstånd som måste finnas)
- **Säkerhet per fält:** modellen anger hög, medel eller låg. Är den låg markeras fältet tydligt och kvittot får statusen "Osäker, kräver granskning" ("varna vid osäkerhet" ur artikeln).
- **Summan går inte ihop:** om netto + moms ≠ total (avrundning ±1 kr tillåts) flaggas det i steg 3. Siffrorna rättas aldrig tyst.
- **Inte ett kvitto, eller oläsligt:** ett tydligt besked och möjlighet att försöka igen.
- **Fel filtyp eller för stor fil:** beskedet ges innan något laddas upp.
- **API:et svarar inte eller gränsen för antal anrop är nådd:** de tre exempelkvittona fungerar ändå eftersom deras svar är sparade i förväg. Eget kvitto ger ett besked om att försöka igen.
- **Tillstånd som ska finnas:** tomt, laddar (per steg), klart, osäkert, fel och gränsen nådd.

### 5.5 Kontolistan (låst)
Modellen får bara föreslå konton ur en lista med cirka 15 vanliga kostnadskonton i BAS, till exempel:
- 5410 Förbrukningsinventarier, 5460 Förbrukningsmaterial
- 5611 Drivmedel för personbilar
- 5800 Resekostnader, 5831 Kost och logi i Sverige
- 6071 Representation, avdragsgill
- 6110 Kontorsmateriel, 6212 Mobiltelefon, 6250 Postbefordran
- 6540 IT-tjänster, 6570 Bankkostnader
- 6991 Övriga externa kostnader, avdragsgilla
- 2641 Debiterad ingående moms
- motkonto 1930 Företagskonto (betalt med företagskort) eller 2890 Övriga kortfristiga skulder (utlägg).

**Byggaren kontrollerar nummer och namn mot aktuell BAS-kontoplan** (bas.se) innan listan låses. Om modellen svarar med ett konto utanför listan ersätts det med "Kräver granskning". Representation flaggas alltid för granskning, eftersom avdragsreglerna inte hanteras i demon.

### 5.6 Teknik och dataskydd
- **Arkitektur:** statiska sidor och **en** serverlös funktion (Vercel) som tar emot bilden, anropar en vision-modell och returnerar strikt JSON.
- **Schemat** som funktionen returnerar och som valideras innan något visas:
  - `leverantor`, `datum` (ISO), `kvittonummer?`, `valuta`
  - `rader[]` (text, belopp)
  - `moms[]` (sats, underlag, belopp)
  - `total`, `betalsatt?`
  - `kontoforslag` (konto, namn, motivering)
  - `motkonto`
  - `sakerhet` per fält
  - `rattext`
- **Momssatser:** systemet hanterar 25, 12 och 6 %. Vilken sats som gäller läses från kvittot och hårdkodas aldrig efter varutyp. Byggaren kontrollerar vilka svenska satser som gäller i oktober 2026 innan testfallen skrivs.
- **Modell:** Gemini Vision är förvalt, samma som i Antons lagersystem. Claude med vision är alternativet (öppet beslut, § 10). Valet ska kunna bytas med en miljövariabel.
- **API-nyckel:** finns bara på servern och läggs in via `api-key-setup` av Anton. Agenten ser aldrig värdet.
- **Dataskydd:**
  - Bilden sparas inte, loggas inte och används inte för träning.
  - Om modellens leverantör erbjuder att stänga av lagring eller träning för API-anrop ska det vara avstängt.
  - Svaren för exempelkvittona sparas i förväg i repot.
- **Gräns:** 20 anrop per timme och IP mot den serverlösa funktionen.
- **Exempelkvittona:** tre påhittade kvitton som uppenbart är exempel:
  - en tankstation (drivmedel, 25 %)
  - en lunchrestaurang (12 %)
  - kontorsmaterial (25 %, flera rader)
  
  Leverantörerna har påhittade namn som tydligt är märkta som exempel och inget org.nr som skulle kunna vara ett riktigt. Kvittona ritas av byggaren, till exempel som HTML renderad till PNG, och vendras i repot. Om Anton i stället levererar egna kvitton med maskade uppgifter ersätter de dessa.

### 5.7 Text som måste finnas (betydelse; formuleringen går genom copy-grinden)
- **AI-märkning:** "Detta är ett AI-system". Resultatet är ett förslag som granskas av en redovisningskonsult. Uppladdade bilder sparas inte och används inte för träning.
- Konceptmärkningen gäller också här (§ 7).
- **Etiketter:**
  - val av exempel, ladda upp, fotografera, börja om, visa råtext
  - stegens namn (artikelns ordalydelse får användas)
  - status: förslag/granskas, osäker, går ihop, går inte ihop
  - felbeskeden i § 5.4.
- **Källhänvisning** till deras artikel, med länk till originalet.

## 6. Varumärkesunderlag (bindande, Tier 1)

- **Tokens ordagrant från deras CSS:**
  - `--bakgrund #faf8f5`
  - `--ink #161616`
  - `--brand-röd #e72835`
  - `--grafit #4b4b4b`
  - `--sand #dfded3`
  - `--lime #c5eb43`
  - `--sten #b1b0aa`
  
  Därtill tjänstefärgerna i § 4. Inga nya kulörer.
- **Typsnitt:** Archivo Black (400) och Arimo (400/500/600/700), båda från Google Fonts. Inga andra familjer.
- **Logotyp:** `assets/original/memo-logo-color.svg` (röd bokmärkesform och ordmärket). Favicons och app-ikoner (32/48/180/192/512) finns i `assets/original/`. App-ikonen är själv en 2×2-mosaik.
- **Alla bilder och vad som får användas:** se `assets/KATALOG.md`.
  - `assets/assess/hero-bricks-*.png` är hero-mosaiken som färdig bild (1316×944).
  - `assets/koncernsajt-no/` har koncernens illustrerade tjänstemotiv: spargris för redovisning, fyr för skatt, kompass och berg för operativ effektivisering, skylt för HR och böcker för juridik. De får användas för de fem tjänster som har ett motiv. Finans och M&A samt GRC har inget motiv, och inget får hittas på i samma stil.
  - Teambilderna i `assets/karriarsida-no/` är norska och visar identifierbara personer. De **får inte användas**.
- **Foto:** `assets/original/hero-lindholmen.jpg`, Lindholmspiren. Det är deras eget foto, men bara **1024×768**. EXIF och GPS är borttagna. Fler foton finns inte i underlaget. Om fler bilder behövs sker det enligt designkedjans bildregler, och det får aldrig vara bilder som utger sig för att visa deras kontor eller medarbetare.
- **Originalets knappar:** brandröd fyllning, vit text, hörnradie 12 px. Sekundärknappen har kontur. Det här är fakta om originalet och ingen instruktion.
- **Delningsbild:** `assets/original/og.jpg` (1200×630).

## 7. Konceptmärkning och spridning

- På **varje sida** finns en synlig, permanent rad som säger att detta är en konceptskiss av Anton Lundin och inte MemoServices officiella webbplats. Formuleringen går genom copy-grinden.
- `<meta name="robots" content="noindex, nofollow">` på alla sidor och `X-Robots-Tag: noindex` från servern.
- Ingen analys, inga cookies och inga spårare.
- Alla externa länkar (originalsajten, assess, memoservices.no) öppnas i en ny flik.

## 8. Publicering

- Vercel, **privat förhandsadress**. Projektnamnet får inte innehålla "memoservices" så att det inte kan förväxlas med en officiell adress. Förslag: `koncept-al-ms`.
- Ingen egen domän. Länken delas bara av Anton.
- Inget pushas eller publiceras utan Antons uttryckliga ja (CLAUDE.md, push-regeln).

## 9. Acceptans (byggaren kör, orkestratorn läser pixlarna)

1. Alla 9 sidor svarar 200. Alla interna länkar fungerar. `/tjanster#<slug>` skickas vidare rätt.
2. Kontrollen av ordagrann text (§ 2.5) ger 0 avvikelser på alla 9 sidor.
3. Alla 7 × 4 "Passar för" och 7 × 6 leveranser finns, och det räknas maskinellt.
4. Mosaikfärgerna på varje plats matchar tabellen i § 4, mätt i renderingen.
5. Kvittotolken:
   - De tre exemplen ger förväntat resultat (leverantör, total, moms per sats och konto) med API:et avstängt.
   - Ett eget kvitto går hela vägen med API:et på.
   - En bild som inte är ett kvitto ger beskedet "inte ett kvitto".
   - En fil på 11 MB stoppas.
   - Ett manipulerat svar där summan inte går ihop flaggas.
   - Ett konto utanför listan ersätts med "Kräver granskning".
6. Navigeringen: alla sju tjänster nås direkt från menyn med mus, tangentbord och mobilmeny.
7. Designkedjans exit bar gäller i övrigt i sin helhet: 320/375/414/768, a11y-audit, copy-grinden på all ny text, inget horisontellt överflöde, skärmbilder som har lästs.
8. Testat i en Teams-delning i 1920×1080 och 1440×900: texten ska gå att läsa vid delning.

## 10. Öppna beslut (Anton)

1. **Vision-modell:** Gemini (förval) eller Claude.
2. **Exempelkvitton:** påhittade (förval) eller Antons egna med maskade uppgifter.
3. **Tidpunkt:** klart till tisdag 11:00 (förval), eller till en eventuell andra intervju.

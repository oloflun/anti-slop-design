# Handoff 2026-10-12: konceptskiss memoservices.se (beställning klar, inget byggt)

Skriven för en agent som aldrig har sett projektet. Läs den här filen först och sedan
`tests/memoservices-koncept/BESTALLNING.md`. Beställningen är bindande för **vad** som ska byggas.
**Hur** det ska se ut tar designkedjan fram (`Skill(design)`, Tier 1).

## 1. Bakgrund

Anton har en första intervju som AI Engineer med Linda Swartling, vd för MemoServices AB, på
**tisdag 2026-10-13 kl. 11:00 i Teams**. MemoServices AB öppnade i Göteborg i juni 2026 och är en del
av en norsk koncern som säljer redovisning, skatt, HR, juridik, finans, GRC och operativ
effektivisering. Anton vill visa en konceptskiss av deras webbplats:
- de sju tjänsteområdena får **egna sidor** (i dag ligger de som ankare på en enda lång sida)
- en fungerande AI-funktion, **Kvittotolken**, som bygger på flödet i deras egen artikel
  "Från kvitto till bokfört".

Skissen visas bara för henne och publiceras aldrig öppet.

Viktiga fakta som går emot det man lätt antar:
- Dagens sajt är **byggd i Webflow med ett eget tokensystem** (`--brand-röd` m.fl.), inte i Lovable
  eller ChatGPT. Behandla den som ett genomtänkt varumärke att härleda ifrån, inte som en mall att
  ersätta.
- **Mosaiken** är varumärkets identitetsform: en 2×2-mosaik per tjänst och en animerad
  hero-mosaik med 25 rutor. Den ska bära skissen (BESTALLNING § 4).
- De har redan en **AI-driven kartläggning** på assess.memoservices.no. Den ska länkas, inte byggas om.

## 2. Läget, verifierat 2026-10-12

| Vad | Läge |
|---|---|
| Mapp | `tests/memoservices-koncept/` (ny, ej committad) |
| Beställning | `BESTALLNING.md`: 9 sidor + Kvittotolken, innehållsregel, mosaik, acceptans |
| Innehåll | `content/tjanster.json`, `start.json`, `delat.json`, genererade av `content/parse_content.py` och `parse_start.py` ur `evidens/*.txt`. Parsern kontrollerar att varje tjänst har 4 "Passar för" och 6 leveranser och att ingress och brödtext finns ordagrant i källan. Körd utan fel. |
| Underlag | `evidens/`: text och skärmbilder (fold och hel sida) för alla 25 sidor på memoservices.se, assess.memoservices.no, mobilbild av startsidan och `pages.json` (typsnitt, färger, tokens, nav, footer per sida) |
| Bilder | `assets/`, med katalog i `assets/KATALOG.md`. `original/`: logotyp, hero-foto 1024×768 (EXIF/GPS borttagen), og-bild och 5 ikoner. `assess/`: hero-mosaiken som bild. `koncernsajt-no/`: koncernens illustrerade tjänstemotiv, får användas. `karriarsida-no/`: norska teambilder, **får inte användas**. Det finns ingen högre upplösning av hero-fotot: `-p-1080` och större ger 403 |
| Byggt | Ingenting. Ingen kod, inget Vercel-projekt, ingen API-nyckel |
| Branch | `design-rework-v3`. Repot har sedan tidigare ändringar i `.agent-chorus/` som inte hör hit. Committa bara `tests/memoservices-koncept/` och den här filen, och bara om Anton ber om det |

Antons egen förstudie, med designförslag som **inte** är bindande här, finns i
`~/ai-job-search/documents/applications/konsilito_ai-engineer/memoservices-koncept/SPEC.md`.
Beställningen ersätter den när det gäller vad som ska byggas.

## 3. Nästa steg

1. Läs `BESTALLNING.md` i sin helhet. Läs sedan `evidens/start-full.png`, `evidens/tjanster-full.png`
   och `evidens/start-fold.png` **som bilder**, och artikeln och AI-policyn i `evidens/`.
2. Kör designkedjan från Steg 0. Det här är verbet **build**, sidtyp Persuade, **Tier 1** som härleds
   ur § 6 i beställningen. Referensfångst (Steg 1b) och bake-off (Steg 2b.5) ingår. Bake-offen får
   bara hoppas över om Anton säger det, och det ska då sägas uttryckligen.
3. Bygg i prioritetsordning (BESTALLNING § 1): Redovisning + Kvittotolken → de sex andra
   tjänstesidorna → översikten → startsidan.
4. Kvittotolken: be Anton köra `api-key-setup` för den valda modellen. Bygg och verifiera
   exempelkvittona med sparade svar **först**, så att demon fungerar även utan nyckel.
5. Acceptans enligt BESTALLNING § 9. Orkestratorn läser alla skärmbilder själv.
6. Publicera till en privat Vercel-förhandsadress först efter Antons ja. Lämna länken till Anton
   senast måndag kväll.

## 4. Fällor

- **Skriv aldrig om originaltexten.** Det gäller även uppenbara fel ("längre fram..", "egen jurist"
  utan punkt). De listas som förslag till Anton. Copy-grinden körs bara på ny text (F-028).
- **Påstå inte att något är "bokfört" och visa inte bankmatchning som om den fungerade.** Steg 5 i
  Kvittotolken är uttryckligen inte byggt och steg 6 är alltid "Förslag, granskas av
  redovisningskonsult". Det är deras egen AI-policy.
- **Ingen förväxling med deras riktiga sajt.** Konceptbanner på varje sida, `noindex`, ett
  Vercel-projekt utan "memoservices" i namnet och ingen egen domän.
- **Hero-fotot är bara 1024×768.** Det räcker inte för en skarp yta i full bredd vid 1440 px.
  Designen måste ta hänsyn till det. Hämta inget högupplöst från deras CDN, det finns inget.
- **Momssatser och BAS-konton ska kontrolleras mot aktuella källor** innan testfallen låses
  (BESTALLNING § 5.5–5.6). Gör inga antaganden ur minnet.
- **Modellregeln** (CLAUDE.md § Delegering): byggare och granskare kör på samma modellklass som
  sessionen. Kontrollera `modelUsage` efteråt.
- Maskinen har 16 GB RAM. Starta inte dev-server, tsc och qmd-embed parallellt.

## 5. Öppna beslut (Anton)

1. Vision-modell för Kvittotolken: Gemini (förval, samma som i hans lagersystem) eller Claude.
2. Exempelkvitton: påhittade (förval) eller hans egna med maskade uppgifter.
3. Tidpunkt: till tisdag 11:00 (förval) eller till en eventuell andra intervju.

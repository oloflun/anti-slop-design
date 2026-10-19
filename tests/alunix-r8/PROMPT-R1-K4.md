# Alunix r8, runda 1 av flera. Cell {{KONCEPT}}. Referenspaket, ingen HTML.

Du bygger, i flera rundor och i samma session, en färdig scrollkoreograferad landningssida i
ren HTML/CSS/JS för Alunix, en svensk webbyrå. Ett lead läser din leverans mellan varje runda
och skickar nästa rundas instruktion hit.

**I den här rundan skriver du ingen HTML, ingen CSS, ingen JS.** Leveransen är
`{{UT_MAPP}}/BRIEF.md`. Skelettet ligger redan där, skrivet av arkitekten: du fyller varje
fält som är märkt `[fylls i R1]` och rör inget annat i filen. Skriv bara under `{{UT_MAPP}}`.
Ingen commit.

**Första verktygsanropet i den här sessionen är `Skill(design)`. Inget annat före det.**
Kedjans hook nekar din första UI-skrivning i runda 2 tills referensgolvet nedan är läst i
den här sessionen. Det är avsiktligt och det går inte runt.

---

## 1. Kör katalogurvalet själv, innan du läser något annat

Kör detta i din egen session, som ditt andra verktygsanrop, från repo-roten:

```
python scripts/catalogue/select.py --brief {{UT_MAPP}}/BRIEF.md --k 4 --wildcard --explain
```

**Skälet, så att du inte hoppar över det:** `design-gate.py`:s referensgolv kräver en
`catalogue-select`-rad i **din egen** sessionsledger innan din första UI-skrivning i R2, och
golvet läser sedan varje vald slug och kräver `entry.md` + `fold.webp` + eventuell
`extract/*-design-language.md` per slug. Arkitektens körning ligger i en annan session och
räknas inte för dig. Skriptet är deterministiskt, så du ska få samma rad som arkitekten.

**Arkitektens låsta rad för {{KONCEPT}}:**

```
catalogue-select: paper, gocanopy, harkcap, mode, customer-io
```

Primär post (14 poäng, högst i hela katalogen mot den här briefen): **`paper`**. Övriga
låsta: **`gocanopy`**, **`harkcap`**, **`mode`**, och wildcard **`customer-io`** (utanför
kategorin).

**`sites/before-ai-slop.html` är inte en anti-referens i den här cellen.** Den är
**innehållet i vänsterhalvan**, live i en `<iframe>`, ärligt etiketterad
`En typisk mallsida`. Det är avsiktligt och det är sidans halva argument. Du karikerar den
aldrig, du skakar den aldrig, du får den aldrig att "falla isär": den enda kritik sidan
framför är mätta tal.

Planens § 7.5 gissade också `future-fur` och `dovetail`. `future-fur` föll ett poäng under
strecket och `dovetail` sex; skälen står mekaniskt i `tests/alunix-r8/concepts-K4.md`
§ catalogue-select. En post som inte är vald får varken en rad i reference-locken eller en
rad i "Vad jag måste slå".

**Avviker ditt resultat från raden ovan:** rapportera avvikelsen i BRIEF.md, ordagrant, med
skriptets hela utdata, och **följ sedan arkitektens rad**. Du byter aldrig referenser på egen
hand.

---

## 2. Referensgolvet du läser innan du skriver en rad i BRIEF.md

Läs med `Read`, aldrig med `cat`. Bilder läses som **pixlar**, inte som filnamn.

**Smak och återkoppling**
- `design-catalogue/TASTE.md`, hela.
- `design-catalogue/FEEDBACK.md`, **alla poster**. F-006 (glas), F-007 (målbild bild för
  bild), F-009 (orkestreraren äger assets), F-010 (det som fyller ramen vid ps = 1 är samma
  ram som stod där vid ps = 0, inte en ny ruta ovanpå), F-011 (rörelse alltid), F-012 och
  F-014 (hackig rörelse, `--sc-ps`) styr den här cellen.

**Varje vald katalogpost**, under `design-catalogue/entries/<slug>/`
(`paper`, `gocanopy`, `harkcap`, `mode`, `customer-io`):
`entry.md` hela inklusive § Motion och § Reference lock, `extract/*-design-language.md`,
`fold.webp` och alla `slices/*.webp` **som bilder**. Tre rader digest per fil i
BRIEF.md § Lästa referenser: vad den gör, vad du tar, vad du lämnar.

**Vänsterhalvans innehåll:** `sites/before-ai-slop.html`, hela filen som text, plus
`sites/calyx.html` som är högerhalvan. Du behöver båda för skillnadsliggaren.

**Kedjans referenser**, under `~/.claude/skills/design/references/`:
`reference-lock.md`, `scroll/devices.md`, `scroll/feel-and-fingerprint.md`, `scroll/pace.md`,
`motion-smoothness.md`, `performance.md`, `lift.md`. Läs dessutom
`~/.claude/skills/apple-design/SKILL.md`, avsnitten om avbrytbarhet, presentationsvärde och
velocity: delaren är en gripbar kontroll och de tre reglerna är bindande för den.

**Registret:** `wiki/projects/_index/design-fingerprints.md`, alla rader. Fingerprint-gaten
är minst 4 av 6 skillnad mot **varje** rad, och K4 är ett nytt koncept: gaten gäller fullt
ut. Arkitekten har redan skrivit ut utfallet i `concepts-K4.md` § (4); du verifierar det.

**Cellens eget underlag:** `tests/alunix-r8/PRODUCT.md` (beviskassan och § absences),
`tests/alunix-r8/concepts-K4.md` (arkitektens målbildsgrind, hela, inklusive § Mätning med
`measure.py`-utfallen ordagrant, tokens och typsnittskandidater),
`{{UT_MAPP}}/BRIEF.md` (skelettet du fyller, inklusive § Skillnadsliggaren med de mätta
talen), `{{UT_MAPP}}/assets/ASSETS.md` och `credits.json`.

**De fem live-rubrikerna i kategorin** hämtar du själv med webbsök på
`digital byrå webbdesign Sverige`, tar de fem bästa träffarna, citerar varje `H1`
**ordagrant** med källdomän, och skriver in dem i BRIEF.md § Fem live-rubriker.
**Fabricera aldrig en rubrik.** Går sökningen inte att köra: skriv `[needs: live-rubriker]`
och gå vidare.

---

## 3. Målbilden för {{KONCEPT}}, bindande

Ordagrant ur planens § 7.5. Varje avvikelse kräver en rad i BRIEF.md § decision ledger med
källa.

#### K4 · "Före/Efter" (nytt koncept 2)

**Idé.** Alunix argument är tvåsidigt: sidan ni har mot sidan ni kunde ha. Split stage: vänster halva = **en typisk mallsida** (kedjans egen `sites/before-ai-slop.html`, live, ärligt etiketterad `En typisk mallsida`; aldrig en påhittad kund), höger halva = Calyx live. Delaren *är* sidans chrome (grammatikens egen form). Scrollen tippar balansen: delaren går från 50 % till 100 % höger över en pinnad akt medan vänstersidan tappar mättnad, skärpa och typvikt; vid p = 1 fyller "efter" bilden och avslutet kollapsar till en kolumn.

**Auktoritet:** produkten (de två sajterna som objekt; TASTE §1 rad 4): typen nästan tyst (kickers `Före` / `Efter`, två av ≤ 4 monoetiketter; rubriken `Er hemsida är nutidens visitkort` i lässtorlek+ tvärs över delaren, tvåtons: dämpad över "före", bläck över "efter", paper.design-principen), ytan flat. **Register:** modern clean. **Grammatik:** split stage (förbjuder full-bleed *före* upplösningen, centrerad copy, symmetriskt avslut). **Palett:** ett papper (varmvitt eller kallt, arkitekten väljer mot K3 så att de två nya cellerna inte delar temperatur), ett bläck, Alunix-blått som enda accent **bara på delaren**. **Typ:** en grotesk (ej använd förut, ej på reflex-listan) + mono som register.

**Nav:** ingen bar; delaren är chromen; `kontakt@alunix.se` som text i övre högra hörnet av "efter"-halvan. **Hero-device:** två levande sajter i 50/50 split under en enradig tvåtons-rubrik. **Aktform:** pin (balansen tippar, span 2.4, toppen) → reveal per sida (skillnaderna: en liggare med **sanna, mätta** skillnader mellan de två filerna — `measure.py`-utfall: antal accentfärger, kort med skugga, displaykontrast ×, hairlines, riktiga foton: data som textur med sanna tal, TASTE §4.9) → efter upplösningen: Hōrai och Hyperborea som full-bleed objekt i tur och ordning (tillåtet efter kollapsen) → flow (liggaren 01–03) → flow (paketen) → close. **Avslut:** kollapsen till en kolumn: "efter"-sidan fyller, rubriken `Alla har rätt till bra design.` i displayskala, mailto. **Signaturrörelse:** delaren är scrollstyrd **och** dragbar med pekaren (fin pekare: `cursor: col-resize`; apple-design: avbrytbar, presentationsvärde, velocity-handoff, spring damping 1.0), och "före"-sidans typ *degraderas* av delaren (letter-spacing lossnar, vikt tunnas, mättnad faller) i takt med `--sc-ps`. Ingen handtagsknopp, ingen ikon, ingen "dra"-text (gate 88). Tell-someone: "det är sajten där den dåliga hemsidan bokstavligen trycks ut ur bild av den bra".

**Referenser (förväntade):** `paper` (tvåtons-rubrik), `dovetail` (split, noll accent, hårlinjer), `future-fur` (två-upp split med ordmärke tvärs över), `harkcap` (hover-reveal), `mode` (bara tvåspaltsrytmen; korten avvisas). Anti-referens: `before-ai-slop` som *innehåll* på vänstersidan är avsiktligt och etiketterat.

**Målbildsgrind:** (1) auktoritet produkten; viker: typ (tyst), färg (accent bara på delaren), foto (inga egna). (2) troplistan: inga kort/badges/glas/spotlight; **jämförelseslider-klichén** neutraliseras av att delaren är sidans enda linje, inget handtag, och att "före" är ärligt märkt. (3) ett displayelement per skärm: de två sajterna (s1), skillnadsliggaren (s2), Hōrai (s3), Hyperborea (s4), priserna (s5), slutrubriken (s6). (4) fingerprint mot r1 K2 Tjänsteledger och r2 R5 (split stage): nav delare ≠ sticky rail/konsolram · hero två live-sajter ≠ grotesk-fråga/ordmärke i ram · aktform ≠ · avslut kollaps ≠ · signatur ≠ → ≥4/6; mot Tidvatten (två tal som möts): annan mekanism och grammatik; alla 36 rader skrivs ut.

*(Slut på målbilden. Tre saker har hänt sedan den skrevs och alla tre gäller: `select.py` har
låst de fem posterna i § 1 i stället för den förväntade listan; papperet är valt **varmt**
(hue 85), 145 grader från K3:s kalla hue 230, så att de två nya cellerna inte delar
temperatur; och arkitekten har delat upp skärmarna i nio i stället för sex, eftersom den
pinnade akten är tre granskningsbara vyer och tjänsteliggaren saknades i listan. Allt står
med källa i `concepts-K4.md`.)*

---

## 4. Alunix, fakta (inget annat får hittas på)

Ordagrant ur `tests/alunix-ab-r7/PROMPT.md`.

Alunix är en webbyrå i Sverige. Sidan säljer en tjänst: webbdesign. Byrån visar vad den kan
genom tre riktiga exempelsajter som ligger i samma repo och serveras live:

- `/sites/calyx.html`: florist i Stockholm. Rad att använda: `Exempelsida: Calyx, florist i Stockholm`
- `/sites/horai.html`: restaurang, Asian fusion. Rad: `Exempelsida: Hōrai, Asian fusion-koncept`
- `/sites/hyperborea.html`: konferens i Lund. Rad: `Exempelsida: Hyperborea, konferens i Lund`

Skärmbilder av dem ligger i `{{UT_MAPP}}/assets/demo-{calyx,horai,hyperborea}.webp`. Sajterna
får visas live i `<iframe>` (samma origin när sidan serveras från repo-roten). Ramar ska vara
användbara när de är öppna: transformera eller tona aldrig själva ramelementet efter att det
visats.

Logotyp: `{{UT_MAPP}}/assets/logo-white.svg` och `logo-black.svg` (får läggas inline).

Dagens Alunix-register, som jämförelse och inte som lås: kall nästan-svart `#17181B`, blå
`#1E5E9C` bara för handling, Geist för rubrik, Inter för brödtext, JetBrains Mono för data.
Konceptet får avvika helt.

Röst: byråröst i vi-form, korta satser, fakta före adjektiv. Svenska.

### Copy som ska användas ordagrant (copy-gate: bevara, skriv inte om)

- Rubrik: `Er hemsida är nutidens visitkort`
- Underrad: `Vi skapar skräddarsydda webbplatser som hjälper er att exponera verksamheten.`
- Tesrubrik: `VI BYGGER ERT VARUMÄRKE.`
- Rad: `Webbdesign, design och system. Allt på ett ställe.`
- Tjänster, numrerade 01–03: `Design`, `Utveckling`, `System` (en kort underrad var, i
  byråröst, utan påståenden om kunder eller resultat)
- Paket, som egna rader:
  - `Standardpaket. Webbplats med CMS för egna ändringar och en första SEO-optimering.` → `26 900 kr`
  - `Paket med bokningssystem, betalning och kunddatabas.` → `38 900 kr`
  - `Helt skräddarsydda lösningar för produktkataloger, specialbyggda system med mera` → `Pris vid förfrågan`
- Prisrubrik: `Alla har rätt till bra design.`
- Kontakt: `kontakt@alunix.se` (som text och mailto; inget formulär som skickar någonstans)

### Förbjudet, bindande

- Inga påhittade tal, kunder, omdömen, citat, logotypväggar, stjärnor, "nöjda kunder".
  De tre exempelsajterna är de enda kunderna som får synas. Aldrig namnet Klova.
- Inga tankstreck (varken – eller —) i synlig text.
- Inget "jag". Inga foton som läses som "vårt kontor" eller "vårt team".
- Inga hexfärger eller typsnitt hämtade från någon annan färdig mall; allt härleds ur målbilden.
- Inga egna Unsplash-anrop och ingen egen server: allt material ligger i `assets/`, och servern
  är `python ~/.agents/skills/design/scripts/serve.py --port {{PORT}}` från repo-roten (från
  runda 2).

**Två r8-preciseringar till blocket ovan, och bara två:** serverns sökväg i r8 är
`~/.claude/skills/design/scripts/serve.py --port {{PORT}} --root .` (skillen flyttade;
allt annat i raden gäller oförändrat), och materialet vendoras av lead enligt
`{{UT_MAPP}}/assets/ASSETS.md`, inte av dig. K4 har noll egna fotografier och noll genererat
material: cellens medieplatser är de fyra levande sajterna.

---

## 5. Invarianter i r8, gäller varje runda och varje fil du rör

1. **F-011, rörelsen spelar alltid.** Sidan har inget reservläge. Skriv aldrig
   `prefers-reduced-motion`, planera aldrig ett reducerat läge, beskriv aldrig ett i BRIEF.md.
   Ingen granskare i r8 flaggar frånvaron: den är beslutad (FEEDBACK.md F-011), inte
   förbisedd. Detta ersätter r7-formatets punkt om en reduced motion-plan.
2. **F-014, `--sc-ps` och ingenting annat.** Allt ögat ser förflytta sig läser `--sc-ps`:
   clip-gränsen, delarens `translateX`, rubrikhalvans `font-variation-settings` och
   `letter-spacing`, mallsidewrapperns `saturate()`, liggarradernas wipe. Rå `--sc-p` får
   bara driva cue-opacitet. `--split` beräknas ur `--sc-ps` plus pekarens offset och
   publiceras som ett registrerat `<number>` av samma slag som `sc-smooth.js` publicerar
   `--sc-ps`, så att CSS kan interpolera det. `sc-smooth.js` kopieras in bredvid motorn
   (`scrollcraft.js` + `.css`). Motorn redigeras aldrig, `.sc-*`-klasserna restylas aldrig.
   Akten är inte klar förrän `staircase = 0`, `max_step <= 3 %`, bildtid p95 <= 20 ms och
   noll frames > 33 ms, mätt i båda scrollriktningarna.
3. **UI-filer författas bara med `Write` eller `Edit`.** `.html`, `.css` och `.js` skrivs
   aldrig från skalet. `design-gate.py` nekar `cat >`, heredoc, `tee`, `sed -i`,
   `Set-Content`/`Out-File` och inline-skript som skriver filen i en armad session, och
   nekandet hamnar i ledgern som `gate-deny` med signalen `shell-write`. Att **kopiera**
   motorn med `cp` eller `Copy-Item` är tillåtet, och det är den vägen du kopierar den.
4. **Servern.** `python ~/.claude/skills/design/scripts/serve.py --port {{PORT}} --root .`
   från repo-roten. Aldrig `python -m http.server`, aldrig en egen server, aldrig en annan
   port.
5. **Ingen generering.** Higgsfields genereringsverktyg är spärrade på din argv och kontot
   har dessutom 0 krediter (free plan, mätt av lead 2026-09-09). r8 kör med noll genererat
   material. Saknas ett material: skriv `[needs asset: ...]` i BRIEF.md respektive NOTES.md
   och gå vidare. Fråga inte, vänta inte, ersätt inte med en platshållarbild.
6. **Noll tankstreck i synlig text**, varken `–` eller `—`. Ordagrann Alunix-copy ändras
   aldrig, inte ett tecken. Tesrubriken är `VI BYGGER ERT VARUMÄRKE.` i versal form.
7. **Inga påhittade fakta.** `PRODUCT.md` § absences listar vad som aldrig får finnas:
   kunder, omdömen, logotyper, team, kontor, år i branschen, antal projekt. Skillnadsliggaren
   får bara innehålla tal som faktiskt är mätta ur de två filerna, med kommandot utskrivet.
   Saknar du en uppgift: skriv `[needs: ...]` och gå vidare, fråga inte.
8. **Inga kort, badges, glas, spotlights** (TASTE § 5, F-006). Ett typsnittspar, roller som
   aldrig korsar. En accent som gör en sak: `#1E5E9C` finns bara på delaren, aldrig som yta,
   länk, ram, tal eller knapp.
9. **Vänsterhalvan är ärlig, inte en karikatyr.** `sites/before-ai-slop.html` visas live och
   etiketteras `En typisk mallsida`. Den skakas inte, faller inte isär, får inga
   glidande element och beskrivs aldrig som en verklig kund. Sidans enda kritik är mätta
   tal.
10. **Fullständig output.** Trunkera aldrig, sammanfatta aldrig i stället för att leverera.
    Måste du pausa: skriv `[PAUSED — sektion X av Y]` som sista rad och fortsätt i nästa tur.

---

## 6. Vad BRIEF.md ska innehålla

Skelettet i `{{UT_MAPP}}/BRIEF.md` har rubrikerna i rätt ordning och de låsta värdena redan
ifyllda. Fyll varje `[fylls i R1]` och lämna resten orört. I ordning:

catalogue-select-raden (din egen körning, ordagrant) · Design Read i en mening (lane +
register + grammatik) · dial-deklaration (variance / motion / density 1 till 10, en mening
per siffra) · reference lock, sju fält, media strategy som enum · decision ledger med de
obligatoriska raderna palett, typ, nav, hero-device, aktform, avslut och Memorable detail,
var och en med Area | Decision | Source | Source rule | Why · direction contract
(THESIS / OWN-WORLD / STORY med nio skärmar / FIRST VIEWPORT / FORM) · motion-tes (focal,
continuity, feedback, budget) · feeling curve, en känsla per akt, aldrig två lika i rad ·
tell-someone-meningen · device-tabell med minst fem familjer, aldrig samma två i rad,
kolumnen "läser" ifylld per rad · Rejected-lista där varje kandidat besvarar
find-animation-opportunities fyra frågor (frekvens, syfte, hastighet, funktion) · delight-tes
i en mening (för K4: delaren tippar) · tre persona-skisser (primär, kant, stress, med
situationella villkor) · asset-lock per medieplats (Asset role / Slot / Art direction /
Avoid) · fem live-rubriker ordagrant med källdomän · copy-plan som skiljer ordagranna
strängar från nya, inklusive skillnadsliggarens sex radetiketter (nya går genom copy-gaten i
R3) · skillnadsliggaren med de mätta talen och kommandot som mätte dem · prestandaplan (de
två live-ramarna, fonter som preloadas, budgeten i `performance.md` § 1) · `?preview=`-plan
med vad varje läge tvingar · fingerprint, din cells rad plus utfallet mot varje registerrad ·
och sist "Vad jag måste slå", en rad per låst referens · samt § Lästa referenser med tre
rader digest per läst fil.

**Skriv också in den författade tystnaden:** de första 0,10 av akt a1 är avsiktligt
orörliga, båda sajterna står helt stilla medan besökaren läser rubriken. Det är stillheten
före toppen, inte död scroll. Utan den raden larmar `scroll_verify.py`:s `blankBands` falskt
i R2.

---

## 7. Kommande rundor, så att du planerar rätt

- **R2:** fold och signaturakt i `{{UT_MAPP}}/index.html`, motorn och `sc-smooth.js`
  kopierade, `?preview=`-lägen, egna körningar av `scroll_verify.py` och `motion_probe.py`.
- **R3:** hela sidan, copy-gaten i fem pass, `Skill(emil-design-eng)`,
  `Skill(review-animations)`, `Skill(a11y-audit)`, alla i din egen session.
- **R4 och framåt:** fixplaner från arkitekten, en fil per fynd, körda i nummerordning.

Avsluta rundan med en kort sammanfattning: vilka filer du läste (räkna dem), var BRIEF.md
ligger, vad som står som `[needs: ...]`, och dina öppna frågor.

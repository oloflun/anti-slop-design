# Gemensam brief · MemoServices konceptskiss · startsidan · runda 1

Du bygger EN cell i en bake-off: startsidan `/` i en av tre riktningar. Varje cell är en komplett
startsida (alla avsnitt i BESTALLNING § 3.1 + det delade i § 3.4), inte bara folden. Anton väljer
riktning på boarden; den valda byggs sedan ut till nio sidor. Läs den här filen helt, sedan din
riktnings `BRIEF-<ID>.md`. Läs inget annat av cellerna.

## 0. Läs först (i den här ordningen, allt är obligatoriskt)

1. `tests/memoservices-koncept/BESTALLNING.md` (beställningen, bindande)
2. `tests/memoservices-koncept/assets/KATALOG.md` (vad som får användas)
3. `~/.claude/skills/design/references/scroll/toolchain.md` § 4 (importmap) och
   `~/.claude/skills/design/references/scroll/devices.md` § The engine + § Load-bearing rules
4. `~/.claude/skills/design/references/scroll/showcase-floor.md` § 2 (de sju reglerna)
5. `~/.claude/skills/design/references/house-physics.md` § Structural (bara den delen)
6. Skills: `Skill(lenis)`, `Skill(gsap-core)`, `Skill(gsap-scrolltrigger)`, `Skill(gsap-timeline)`,
   `Skill(gsap-plugins)` (SplitText + det din brief namnger)
7. Bilderna, som bilder: `evidens/start-fold.png` (originalet), `assets/assess/hero-bricks-BCEGB_Vf.png`
   (hero-mosaiken som facit), `assets/video/piren-contact.webp` (videons tolv bildrutor)

## 1. Filer och sökvägar

- Din cell: `tests/memoservices-koncept/board/cells/<ID>-r1/`. Där skriver du
  `template.html` (med platshållare) och kör `python tests/memoservices-koncept/content/render.py
  template.html index.html`. **Du skriver aldrig sidans text själv**, se § 3.
- Boarden serverar `board/` som rot med repo-roten som reserv. Alla sökvägar i HTML är därför
  absoluta från serverroten och fungerar både på boarden och via `serve.py` från repo-roten:
  - `/gsap.js`, `/smooth-scroll.js` (projektets centrala filer, importera bara därifrån)
  - `/node_modules/lenis/dist/lenis.css`
  - `/tests/memoservices-koncept/assets/...` (video, logotyp, ikoner)
- Importmap, ordagrant (toolchain.md § 4):

```html
<link rel="stylesheet" href="/node_modules/lenis/dist/lenis.css">
<script type="importmap">
{ "imports": {
  "gsap": "/node_modules/gsap/index.js",
  "gsap/all": "/node_modules/gsap/all.js",
  "gsap/": "/node_modules/gsap/",
  "lenis": "/node_modules/lenis/dist/lenis.mjs"
} }
</script>
<script type="module" src="./main.js"></script>
```

- `main.js` ligger i cellmappen och börjar med
  `import { gsap, ScrollTrigger, SplitText, CustomEase } from "/gsap.js"; import lenis from "/smooth-scroll.js";`
  Lenis-instansen med husets tempo finns redan i `/smooth-scroll.js`. Skapa ALDRIG en egen Lenis,
  registrera ALDRIG plugins själv, ingen CDN, ingen `npm install`.
- Fonter: Google Fonts, bara dessa två familjer: Archivo Black (400) och Arimo (400, 500, 700).
  `<link rel="preconnect">` + en `<link>` med `display=swap`. Inga andra typsnitt, ingen serif.

## 2. Låsta tokens (Tier 1, ur deras CSS; inga andra kulörer får förekomma i filen)

```css
:root{
  --bakgrund:#faf8f5; --ink:#161616; --brand-rod:#e72835; --grafit:#4b4b4b;
  --sand:#dfded3; --lime:#c5eb43; --sten:#b1b0aa;
  /* tjänstefärger: huvud (3 rutor) + accent (1 ruta nere till höger) */
  --t-redovisning:#2c546d;   --a-redovisning:#c5eb43;
  --t-hr:#6dabbf;            --a-hr:#c5eb43;
  --t-skatt:#8b5e3c;         --a-skatt:#f3aaaf;
  --t-juridik:#4b4b4b;       --a-juridik:#e72835;
  --t-finans:#9db377;        --a-finans:#2c546d;
  --t-grc:#294b3f;           --a-grc:#c5eb43;
  --t-opex:#b1b0aa;          --a-opex:#ee646e;
  --font-display:"Archivo Black", Impact, sans-serif;
  --font-body:Arimo, Arial, sans-serif;
  --radie:10px; /* brickans hörnradie; samma radie på knappar; ingen annan radie på sidan */
}
```

Varje färg och `font-family` i CSS refererar en token (gate 48). Brandröd är den enda accenten på
små kontroller (knappar, länkpil). Lime får vara grund för kartläggningsavsnittet, som i originalet.
Tjänstefärgerna används bara som tjänstens identitet (mosaik, band, markör), aldrig som dekor.
Ljus grund `--bakgrund`, mörk grund `--ink`; grafit för sekundär text på ljus grund, sand/sten
för sekundär text på mörk grund. Mät kontrasten per grund (TASTE: varje dämpad ton har ett värde
per grund).

## 3. Innehåll: ordagrant, maskinellt

All text kommer ur `content/start.json`, `content/delat.json`, `content/tjanster.json` och den
nya texten i `content/ny-text.json` via `render.py`. Läs `render.py`:s docstring för mallspråket.
Tillgängliga nycklar (exempel): `{{meta.title}}`, `{{meta.description}}`, `{{hero.kicker}}`,
`{{hero.rubrik_rader.0}}`, `{{hero.lead}}`, `{{hero.ingress}}`, `{{hero.knappar.0.text}}`,
`{{hero.knappar.1.till}}`, `{{tjansteomraden.kicker}}`, `{{tjansteomraden.rubrik}}`,
`{{tjansteomraden.lank.text}}`, `{{tjansteomraden.kortlank_text}}`,
`{{tjansteomraden.flera_omraden.rubrik|text|lank.text|lank.till}}`, `{{kartlaggning.*}}`,
`{{om.kicker}}`, `{{om.rubrik_rader.0}}`, `{{om.text}}`, `{{om.koncern}}`, `{{om.koncern_lank}}`,
`{{insikter.rubrik}}`, `{{insikter.lank.text}}`, `{{delat.nav.0.0}}` (text) `{{delat.nav.0.1}}` (href),
`{{delat.nav_knapp.0}}`, `{{delat.footer.adress}}`, `{{delat.footer.epost}}`,
`{{delat.footer.copyright}}`, `{{delat.footer.koncernrad}}`, `{{delat.footer.koncernlank.0}}`,
`{{ny.banner}}`, `{{ny.hopp_till_innehall}}`, `{{ny.meny}}`, `{{ny.stang_menyn}}`.
Loopar: `{{#tjanster}}…{{.namn}} {{.slug}} {{.kort_pa_startsidan}} {{.mosaik.huvudfarg}}
{{.mosaik.accent}} {{@n}}…{{/tjanster}}`, `{{#om.punkter}}…{{.}}…{{/om.punkter}}` (fetstilen:
originalet har `<strong>` på `om.punkter_fetstil[i]`, resten av meningen normal; lös det med
`{{^om.punkter_fetstil}}` + resten, se `render.py` och exemplet i docstringen), `{{#insikter.artiklar}}
{{.kategori_datum}} {{.rubrik}} {{.utdrag}} {{^insikter.artikel_lankar}}{{/insikter.artiklar}}`,
`{{#delat.footer.kolumner.FÖRETAGET}}{{.0}} {{.1}}{{/delat.footer.kolumner.FÖRETAGET}}`, samma för
`JURIDISKT`. TJÄNSTER-kolumnen i sidfoten är `{{#tjanster}}`-loopen med `/tjanster/{{.slug}}`.
Koncernraden "MemoServices AB är en del av MemoServices-koncernen, med verksamhet i Norge och
Sverige. www.memoservices.no ↗" i om-avsnittet: länken täcker "www.memoservices.no ↗".

Regler:
- Ingen annan text i filen. Inga egna kickers, bildtexter, etiketter, "Scrolla", siffror, räknare.
  Ett löpnummer (01–07) får finnas men i ett **eget element** (annars faller textkontrollen).
- `<title>` = `{{meta.title}}`, meta description = `{{meta.description}}`, båda ordagrant.
- `aria-label` räknas inte som synlig text men ska också vara ett av tjänstenamnen eller en
  sträng i ny-text.json. Videon är `aria-hidden="true"`.
- Länkar: tjänsterna till `/tjanster/{{.slug}}` (404 på boarden, förväntat), "Se tjänsterna" och
  "Läs mer om tjänsterna →" till `/tjanster`, "Om oss" till `/#om` (avsnittet har `id="om"`),
  externa länkar (`https://…`) med `target="_blank" rel="noopener"`. Logotypen till `/`.
- Kontroll: `python tests/memoservices-koncept/content/verify_text.py <url>` ska ge 0 avvikelser.

## 4. Mosaiken (varumärkets form, genomgående tema i alla tre riktningar)

- **Brickan**: fyrkant, radie `--radie` (10 px vid 51 px bricka, skala proportionellt), mellanrum
  8/51 av sidan. Tjänstens 2×2: tre brickor i huvudfärgen, accentbrickan nere till höger.
- **Hero-mosaiken** (facit `hero-bricks-BCEGB_Vf.png`, 7 kolumner × 5 rader, 25 brickor; kolumn
  1–7, rad 1–5): r1: röd röd röd ljusblå · · marin marin; r2: röd · ljusblå lime ljusblå marin marin;
  r3: grön grön grön ljusblå · rosa korall; r4: · oliv oliv oliv rosa rosa; r5: · · · oliv marin.
  (röd `--brand-rod`, ljusblå `--t-hr`, marin `--t-redovisning`, lime `--lime`, grön `--t-grc`,
  rosa `--a-skatt`, korall `--a-opex`, oliv `--t-finans`.) Facit saknar skattens brun `--t-skatt`
  och opex sten `--t-opex`. **Kravet (§ 4.3) är att alla sju huvudfärgerna ryms i hero-mosaiken**:
  lägg till brickor eller byt två så att brun och sten finns med. 25–32 brickor.
- Varje tjänst känns igen på sin 2×2 **överallt** den förekommer: tjänstelistan, undermenyn,
  sidfotens TJÄNSTER-kolumn. Mosaiken ritas i DOM/SVG med tokens, aldrig som bild (förutom att
  facit-PNG:n får användas som referens). App-ikonen `assets/original/icon-512.png` är själv en 2×2
  (röd botten, lime nere till höger) och får användas som bild där briefen säger.
- Brickan är sidans **signaturobjekt** (floor-regel 3): den återkommer och byter jobb minst tre
  gånger per sida (din brief säger vilka).

## 5. Videon (hero i alla tre)

`assets/video/piren-hero.mp4` (1280×720, 22 s, 4,2 MB, h264, ljudlös),
`piren-hero-540.mp4` (960×540, 2,1 MB) för `max-width: 768px`-fallet via JS-byte av `src`,
`piren-scrub.mp4` (täta keyframes, bara för scrubbning), `piren-poster.webp` (första rutan),
`piren-last.webp` (sista rutan: kameran står inne i glasfasaden, fönsterrastret fyller bilden).
Innehåll: kameran åker längs piren, förbi vattnet, upp mot de kopparramade glaskuberna och in i
fasadens fönsterraster. **Fasadens raster är i sig en mosaik**: använd det.
`<video autoplay muted loop playsinline preload="metadata" poster=…>` om inte din brief scrubbar.
Typ över video: aldrig direkt på den ljusa himlen. Text står på en mätt platta (`--ink` eller
`--bakgrund`, opak eller minst 0,88) eller bredvid videon. Mät med
`python ~/.agents/skills/design/scripts/contrast_over_media.py <url>`.

## 6. Rörelsen: GSAP 3.15 + Lenis, golvet gäller

- Importera bara från `/gsap.js` och `/smooth-scroll.js`. `lenis` är redan kopplad till
  `ScrollTrigger.update` och `gsap.ticker`.
- **Alla scrubbade triggers `scrub: true`** (aldrig ett tal, Lenis är den enda utjämningen).
- Pin skapas en gång vid init, aldrig vid klick. `end` som funktion i px, `invalidateOnRefresh: true`,
  aldrig `'+=Nvh'`. Sista triggern på sidan `end: 'bottom bottom'`. Triggers i sidordning.
- En pin vars innehåll ska ses spänner ≥ 200 vh. Rubriker står helt synliga, oklippta och stilla
  i minst 40 vh (F-025). Text i en helskärmsvy har tyngdpunkten vid 42–46 % av höjden, inte 50 %.
- Rubriker: `SplitText.create(el, {type:'lines', mask:'lines', autoSplit:true, onSplit})` efter
  `document.fonts.ready`; per-tecken bara på ett kort ord, aldrig på brödtext. Masken behöver
  luft för nedstaplar (padding-bottom + negativ margin).
- **Fail toward visible:** ingenting döljs i CSS. All starttillstånd (`opacity:0`, förskjutning)
  sätts i JS (`gsap.set`/`gsap.from`), så att sidan är komplett utan JavaScript. Ingen
  `prefers-reduced-motion`-läsning någonstans (F-011). Reveals körs en gång och göms aldrig igen
  vid scroll uppåt.
- Floor-regel 1: introt och heron är ett tag, något består över överlämningen. Regel 2: varje
  avsnittsbyte har en materiell orsak, **minst tre olika orsaker per sida, aldrig samma två gånger
  i rad**. Regel 3: brickan är signaturobjektet. Regel 4: en text på sidan drivs av scrollen i
  lästempo (ord som tänds grå→ink, eller aktiv rad lyser medan resten är grå). Regel 5: typ och
  media delar en ram minst en gång. Regel 6: tempot är husets, höj det inte.
- Minst fyra enhetsfamiljer per sida (scrub/pin/pan/reveal/kinetic/parallax/flow+in/pekare), aldrig
  samma två gånger i rad. Pekarenheter (magnet på primär-CTA, tilt på brickor) bara under
  `(hover:hover) and (pointer:fine)`, via `gsap.quickTo`.
- Varje animerad egenskap på ett element har exakt en ägare (en tidslinje). En scrubbad tween på
  något som laddningen redan flyttat ger fel läge efter scroll ned+upp; lägg scrollrörelsen på ett
  annat lager.
- `?preview=<namn>`-krokar: för varje akt i din brief ska `?preview=<akt>` scrolla dit (via
  `window.__lenis.scrollTo(el,{immediate:true})` efter `ScrollTrigger.refresh()`), så att läget går
  att skärmdumpa. Lista krokarna i `NOTES.md`.
- `will-change` bara medan något rör sig. Inga `filter`/`backdrop-filter` över mer än halva vyn.

## 7. Det som inte får finnas

Serif eller kursiv display · kort med skugga eller kantlinje som rutnät (ledger/hårlinjer och
flata ytor i stället) · ikonrad/ikongrid · glas, gradienter, pill-knappar med gradient · falska
webbläsar-/telefonramar · små beskrivande etiketter och bildtexter (F-016; marknadssida = noll
mikrotext utöver originalets egna kickers, som är innehåll) · text som beskriver sidan själv ·
påhittade siffror, kunder, citat · tankstreck i ny text · hotlänkade resurser · `scroll-behavior:
smooth` · en andra Lenis · `ScrollSmoother` · numerisk scrub · en akt som bara tonar upp 14 px som
"övergång" · samma enhet två gånger i rad · en spinner-intro.

## 8. Delat på sidan (BESTALLNING § 3.4, § 7)

- Huvudmeny med originalets poster (`delat.nav`), "Kontakta oss"-knapp, logotyp till `/`.
  "Tjänster" leder till `/tjanster` **och** öppnar direkt åtkomst till de sju tjänstesidorna med
  mosaik + namn. Fungerar med mus, tangentbord (`aria-expanded`, Esc stänger, fokus synligt) och i
  mobilmenyn. Hur den ser ut säger din brief.
- Mobilmeny (knappen `{{ny.meny}}` / `{{ny.stang_menyn}}`) med samma innehåll.
- Hopplänk `{{ny.hopp_till_innehall}}` till `#innehall`, synlig vid fokus.
- Sidfot: adress, e-post (`mailto:`), kolumnerna TJÄNSTER / FÖRETAGET / JURIDISKT (rubrikerna är
  nycklarna i `delat.footer.kolumner`, ordagrant), copyright, koncernraden + länk till
  memoservices.no. Ingen "Cookie-inställningar".
- Konceptbanner `{{ny.banner}}`: synlig, permanent rad på varje sida (t.ex. en tunn rad överst
  eller nederst, `--sand` på ljus / `--grafit` på mörk). Inte ett popup.
- `<meta name="robots" content="noindex, nofollow">`. Inga spårare, inga cookies.
- `<html lang="sv">`, `overflow-x: clip` på html och body, `color-scheme`, `theme-color`.

## 9. Responsivt (hårt golv)

320 / 375 / 414 / 768 / 1440: inget horisontellt överflöde (elementgränser, inte scrollWidth),
inga tvåradiga knappar eller navlänkar, `minmax(0,1fr)` i bildbärande grid, `overflow-wrap:
anywhere; min-width:0` på display-rubriker, sektionshuvuden en kolumn på mobil. Pinnade akter
finns kvar på mobil som staplade scener (kortare spann går bra), aldrig borttagna.

## 10. Verifiering som DU kör innan du rapporterar

```bash
python tests/memoservices-koncept/content/render.py tests/memoservices-koncept/board/cells/<ID>-r1/template.html tests/memoservices-koncept/board/cells/<ID>-r1/index.html
python ~/.agents/skills/design/scripts/serve.py --port <din port 3101/3102/3103> --root .     # i bakgrunden, från repo-roten
python ~/.agents/skills/design/scripts/shoot.py tests/memoservices-koncept/board/cells/<ID>-r1/.shots http://localhost:<port>/tests/memoservices-koncept/board/cells/<ID>-r1/index.html
python tests/memoservices-koncept/content/verify_text.py http://localhost:<port>/tests/memoservices-koncept/board/cells/<ID>-r1/index.html
python ~/.agents/skills/design/scripts/scroll_verify.py http://localhost:<port>/tests/memoservices-koncept/board/cells/<ID>-r1/index.html
python ~/.agents/skills/design/scripts/contrast_over_media.py http://localhost:<port>/tests/memoservices-koncept/board/cells/<ID>-r1/index.html
```

Läs varje skärmbild som bild (fold, hela sidan, 390 px), läs konsolen (0 fel, 0 404 utom
`/tjanster/*`-länkar som inte klickas), rätta, kör om. Rapportera inte förrän: 0 textavvikelser,
0 konsolfel, inget dött scroll, inget horisontellt överflöde vid 320/375/414/768, varje
`?preview=` landar rätt. Headless Chromium bara, aldrig ett synligt fönster.

## 11. Leverans

I cellmappen: `template.html`, `index.html` (renderad), `main.js`, `NOTES.md` med: lane i en
mening, auktoriteten (TASTE § 1), akterna med enhet/spann/orsak, signaturobjektets tre jobb,
`?preview=`-krokarna, mätvärden (textkontroll, scroll_verify, konsol), och det du inte hann.
Rapportera: `DONE <sökväg> <radantal>` eller `FAILED <orsak>`. Inga andra filer i repot ändras.
Modellen som bygger är Opus (CLAUDE.md § Delegering); delegera inte vidare.

# V3e-r2 · Mätbordet — rapport

Sidan serveras på `http://127.0.0.1:3305/tests/alunix-r8/runs/V3e-r2/index.html`
(`python skills/design/scripts/serve.py --port 3305 --root .`). Alla siffror
nedan är uppmätta i Chromium (Playwright, headless) mot den servern.

Detta är ett **nytt bygge**, inte en fjärde runda på V3e. Specen är
`BYGGSPEC.md`. Det som byttes från V3d: registret (grafit + blå → instrumentvitt
+ monokrom ram + verkens egna färger), layouten (helskärms-pinnade inbäddningar →
helbredds mörka plattor), och rörelsen (kortet vänds → plattan öppnar sig).

---

## 1. Vad som byggdes

**Mätbordet.** Ramen är ett kallt, monokromt instrument; de två levande verken och
priset är monterade som helbredds mörka plattor (ljuslådor); verkens egna färger är
sidans enda kromatik.

- **Heron** öppnar på sidans egen namn som ett gigantiskt **konturordmärke**
  (stroke-only, `-webkit-text-stroke`, mjukt bläck, blöder ur viewportkanten), med
  h1 `Er hemsida är nutidens visitkort` satt **monumentalt** (Geist 700, 158 px,
  tre rader) över den, och provetiketten nere till vänster. Rubrik, etikett och
  ordmärke ryms alla i första vyn.
- **Tesen** är en numrerad utsaga (monokrom), Hyperborea-plåten i tunn ram.
- **Processen** är ett linjerat register (nummer i bläck, inte i färg).
- **Provarket** är två helbredds mörka plattor. Varje platta bär en topplist med
  verkets egen färg på numret och på regeln, den levande sajten i ett **fönster**
  (sticky, `16/10`) med registreringsmärken, och liggaren i ljus text bredvid.
  Hōrai är spegelvänt.
- **Priset** är samma mörka platta, satt innanför arket.
- **Kontakten** och **footern** är tillbaka på instrumentvitt.

Referenserna (lästa med Inspo-MCP, inte ur minne): primär `exoape-com` (monumental
typ som skärs av viewportkanten), lån `dversostudio-io` (konturordmärke som stomme +
Geist Mono-apparat) och `nbstudio-co-uk` (verket som monterat föremål).
`christophrauscher-de` och dess varma serif avvisades mot gate 89 och de tre
vendorade snitten. `compare` gav `sameRegister:false` på kandidaterna — därför en
dominerande riktning, inget medelvärde (gate 90).

## 2. Copyn

Källan är `runs/V3e/index.html` (redan parity-verifierad mot `runs/V3d/index.html`).
Varje synlig sträng återanvänds ordagrant. Verifierat mekaniskt mot V3d med en
BeautifulSoup-diff som filtrerar script/style/kommentarer **och aria-hidden**:

- **I r2 men inte V3d: 0 strängar.** Ingenting påhittat.
- **I V3d men inte r2: 8 strängar**, alla i den självritande SVG-ritningen
  (`Sektionsritning av processen`, `En måttsatt ritning…`, `320`, `768`, `1440`,
  `7 rem`, `16:9`, `96 px`, `A`) — borttagna med avsikt (K3 äger ritningen).
- h1 är **en sträng**, inte delad i två (V3e:s delning var en avvikelse).
- `SEO&#8209;optimering` bär U+2011 (`&#8209;`, en förekomst, samma form som V3d).
- `Eller mejla oss direkt på kontakt@alunix.se` är R24:s form.
- Numren i tesen (`01`–`04`), processtegen (`01`–`07`) och liggarna (`01`–`05`/`06`)
  är `aria-hidden` och räknas inte som synlig text — samma som V3d:s processnummer.

## 3. Verifiering, uppmätt

| Kontroll | Utfall |
|---|---|
| Horisontell overflow 390/414/768/1440/1920 | **0 px** på alla fem |
| Konsolfel (exkl. Tailwind-CDN-varningen från de inbäddade sajterna) | **0** |
| h1 | Geist 700, 158,4 px, top 72 px (inget tomrum), 3 rader |
| Konturordmärket | stroke 1,5 px, fyll transparent, mjukt bläck |
| Första vyn | h1 72–423, etikett 652–900 — allt innanför 0–900 |
| Calyx-färg (numret) | `oklch(0.72 0.12 45)` — enbart på Calyx platta |
| Hōrai-färg (numret) | `oklch(0.68 0.16 30)` — enbart på Hōrais platta |
| Plattans grund | `oklch(0.16 0.012 255)` (mörk) |
| Inbäddning Calyx | monterad, 134 noder, sticky, `title`/`loading` ordagrant |
| Inbäddning Hōrai | monterad, 197 noder, sticky, ordagrant |
| Em-dash U+2014 i synlig text | **0** |
| En-dash / raka citat / `...` | **0** / **0** / **0** |
| `border-radius` | en deklaration, värdet `0` |
| `prefers-reduced-motion` | **0** (F-011) |
| `outline:none` / `will-change` / `position:fixed` | **0** / **0** / **0** |
| Rå `--sc-p` i en `transform` | **0** (all bespoke-rörelse läser dämpad `--sc-ps`) |
| Gradient / `backdrop-filter` / `var(--accent)` | **0** / **0** / **0** |
| Sidhöjd 1440 | 7 609 px (V3e: 7 516; V3d: 30 926) |

## 4. Vad som uteslöts ur V3d

1. Det vändbara visitkortet (rotationen) → provetiketten.
2. Den självritande SVG-ritningen → registret.
3. Grafitgrunden `#0b0c0e` och blå accent `#1e5e9c` → instrumentvitt + monokrom
   ram + verkens egna färger.
4. Helskärmsifyllda, scroll-pinnade inbäddningar → helbredds mörka plattor med
   sticky fönster.
5. Interna spår (`PLAN`, `R-`, `F-`, `Astra`, `Target`, `gate`, `TASTE`, `C-8`,
   `COPY-V3d`, `cell V3c`, mätvärden) och `data-preview`/`?preview=`-mekaniken.

## 5. Osäkert

- **Konturordmärkets överlapp med h1.** Ordmärket ligger bakom h1:s första rader
  (överlapp mätt: 964 × 226 px). Det är avsett — "bokstäverna som stomme bakom
  rubriken" är dverso-greppet — men jag har **inte kunnat granska det visuellt**:
  den här sessionen renderar inga bilder till mig (screenshottarna ligger i
  `_shot-*.png` för Anton att titta på). Om överlappet läser som kollision i stället
  för stomme är fixen att förankra ordmärket i botten i stället för toppen.
- **`theme-color` och faviconens fyll** är satta till `#eef0f3`, samplat ur en
  skärmbild (pixel 238,240,243) — inte läst ur koden. Grunden är
  `oklch(0.955 0.004 250)`.
- **Den vertikala rytmen.** Specen säger 8 px-enhet; skarvarna ligger på
  `--ry:96px`/`--ry-lg:128px`, men plattans `padding-block` (40/28/96) är valda för
  att ge topplisten och fönstret luft snarare än för att ligga på 8-multiplar.
  Vill man ha rytmen strikt är det en rad att räta.
- **`overflow-x: clip` på `.work`** är min lösning på sidoöversvämningen (settle-
  svepets 38,4 px mot en 20 px telefonmarginal), samma mekanism som V3e:s `.prov`.
  Den klipper vid plattans egen kant och rör ingenting i stillastående läge.

## 6. Filer

- `index.html` — hela sidan, en fil (fonts och motor ligger kvar i `assets/` och `scroll/`).
- `BYGGSPEC.md`, `RAPPORT.md`, `verify.py` — spek, rapport, verifieringsskript.
- `_shot-hero.png`, `_shot-full.png`, `_shot-mobile-case.png` — skärmbilder för granskning.
- `board.json` är **inte** rörd; om V3e-r2 ska upp på boarden som ersättare till V3e
  är det Antons beslut (handoff § 10.3).

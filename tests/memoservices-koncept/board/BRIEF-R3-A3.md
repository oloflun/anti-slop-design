# A3 · "Linsen II" · filmic one-shot, mörk först, brickorna är fönster och sedan raster

Cell `cells/A3-r1/` · port 3104 · `?preview=`: `hero`, `fasad`, `tjanster`, `kartlaggning`, `om`, `insikter`, `slut`.

**Lane:** mörk film i gemener, mosaiken som lins över piren.
**Typsnitt:** display **Bricolage Grotesque** (opsz 96, vikt 300 i rubriker, 500 på ett bärande ord
per rubrik: "KOMPETENS." i heron, "VÄXA" i tjänster, "KONTAKTPERSON." i om) + text **Instrument
Sans** 400/600. Display `clamp(3rem, 7.5vw, 6.5rem)`, leading .95, spärr +.012em.
**Auktoritet:** videon i första halvan, sedan ytan.
**Grund:** `--ink` från toppen till och med tjänsterna, `--bakgrund` från kartläggningen.

## Formationer (bricklagret, 28 brickor)
| # | Sektion | Formation | Övergångsfönster |
|---|---|---|---|
| F1 | Intro/hero | **fönster**: 28 brickor som ett 7×4-raster över högra 55 % av vyn (slots i hero), ink-täckning med SVG-mask där brickorna är hålen mot videon (runda 1-mekaniken, men brickorna i lagret är ramarna: 2 px ink-kant, transparent mitt) | intro 1,4 s |
| F2 | Hero scrub (pin 260 vh, `piren-scrub.mp4`) | fönstren växer ihop till full video (mask), lagrets brickor krymper till 10 px prickar som lägger sig i ett 7×4-raster nere till höger (**kompassen**: ett litet rutnät som visar var i sidan man är, en bricka tänds per sektion) | 0–30 % av pinnen |
| F3 | Fasad/tjänster (flöde, ingen pin) | brickorna lämnar kompassen rad för rad och bildar **sju 2×2 i en rad** tvärs över vyn vid 46 % höjd (slots i en 7-kolumnsrad i sektionen); under raden rullar tjänstetexterna som en vertikal lista (namn 2 rem Bricolage 500, `kort_pa_startsidan`, "Läs mer →") och **den 2×2 vars text passerar 60 % av vyn lyser** (opacity 1, skala 1,12), övriga .55 | 100 % → 25 % |
| F4 | Kartläggning (lime, panel ur axeln) | brickorna samlas till **en** lime-bricka (28 → 1: alla flyttar till samma slot, färgen tweenas till lime) som växer till bandet; på bandet står texten i 7 kolumner vid 44 % | 100 % → 20 % |
| F5 | Om | lime-brickan delar sig i fyra markörer (2×2 röd/lime) i ledgern till höger; resterande 24 blir en **lodrät kolumn av små brickor** till vänster om rubriken (slotkolumn, 12 px, som en hårlinje av färg) | 100 % → 25 % |
| F6 | Insikter | tre brickor blir kategorimarkörer (marin/brun/röd) framför raderna; de andra 25 bildar en tunn rad under rubriken "INSIKTER" (slots i en rad) | 100 % → 25 % |
| F7 | Sidfot | alla 28 bildar **app-ikonen** 2×2 (7 brickor per ruta, röd ×3 rutor, lime ×1) bredvid logotypen; `end: 'bottom bottom'` | 100 % → 0 % |

Övergångsorsaker: fönster som växer ihop · kompassen lämnas rad för rad · samling till en bricka · delning till markörer · samling till ikonen. Fem olika.

## Layout
- **Nav:** en ink-bricka top-vänster med logotypen; länkarna i en **centrerad** ink-bricka
  (ny), "Kontakta oss" i en röd bricka top-höger. "Tjänster" fäller ut den centrerade brickan nedåt
  med sju rader (2×2 + namn). Inverteras till bakgrund på ljus grund. Mobil: logotyp + Meny.
- **Hero:** rubriken **centrerad** i vyn (Persona-principen: stor, lätt, centrerad) på en smal ink-
  platta (`--ink` .92, bara så bred som texten + 48 px, radie `--radie`), lead + ingress centrerade
  under i 48 ch, knapparna under. Plattans tyngdpunkt 44 %. Videon full-bleed bakom, scrubbad.
  Kickern (originalets, röd versal) står som en liten rad ovanför rubriken i plattan.
- **Tjänster:** rubriken "DET DU BEHÖVER FÖR ATT VÄXA" + kicker + länken i en **vänster sticky
  kolumn** (4/12); listan i 8/12 till höger, under 2×2-raden. "Behöver du hjälp inom flera
  områden?" som sista post i listan, på en hårlinje.
- **Kartläggning:** som ovan. **Om:** rubrik 8/12 vänster, text 40 ch; ledger 4/12 höger, 10 vh
  förskjuten. **Insikter:** ledger-rader (bricka, kategori·datum, rubrik Instrument Sans 600, utdrag).
- **Sidfot:** ink; logotyp + ikonen; TJÄNSTER med riktiga små 2×2 (HTML, inte lagret); bannern sist.

## Enheter
intro-tidslinje → scrub (hero, pin) → flöde + lagerformation (tjänster, ljus-aktiv rad) → reveal/clip (lime) → flow+in (om, insikter) → lagerformation (slut). Pekare: lagret följer pekaren 0,6 %.

## Skiljer A3 från B3/C3
Grammatik filmic · nav tre brickor (vänster/mitt/höger) · hero centrerad platta över scrubbad video + fönstermask · 1 pin · slut = app-ikonen · signatur = kompassen (brickorna som sidans läge).

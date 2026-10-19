# Riktning C · "Passagen" · tjänsterna som objekt i en sidledes passage

Cell: `tests/memoservices-koncept/board/cells/C-r1/` · port 3103 · `?preview=` krokar: `hero`,
`passage`, `passage-4`, `kartlaggning`, `om`, `insikter`, `slut`.

**Lane (en fras):** ljus katalog, piren i djup, brickorna som objekt.
**Register:** modern clean. **Grammatik:** gallery/catalog: sidan är ett rum man går igenom,
objekten (de sju mosaikerna) i sin egen takt. **Auktoritet (TASTE § 1):** objektet (brickan).
Typen är stram: Archivo Black i rubriker, Arimo i allt annat; videon är scen, inte budskap.
**Tell-someone:** "sajten där brickorna svävade i luften över piren och sedan ställde upp sig i en
rad man gick förbi."
**Grund:** `--bakgrund` genomgående; tonal inversion i passagen (`--ink`) och i sidfoten.

## Känslokurvan

| # | Akt | Känsla | Vad på skärmen |
|---|---|---|---|
| 0 | Intro → hero | Ankomst | kickern sätts rad för rad på papper, sedan lyfter papperet och piren tonar upp bakom; brickorna hänger i tre djupplan |
| 1 | Hero | Djup | videon spelar; tre brickplan driver i olika takt när man scrollar; rubriken på pappersplatta |
| 2 | Passagen | Breddsyn | sidan vänder sig: en horisontell pinnad rail med rubriken och sju stora brickobjekt, vart och ett landar helt |
| 3 | Kartläggning | Lättnad | en lime-bricka växer ur passagens slut till ett band |
| 4 | Om | Förtroende | papper, två rader rubrik, ledger med markörer |
| 5 | Insikter | Kontinuitet | tre objekt i rad, varje med sin bricka |
| 6 | Slut | Index | brickorna från heron lägger sig som sju små 2×2 i sidfotens TJÄNSTER-kolumn |

Peaken är akt 2 (största spannet, enda axelbytet).

## Akterna i detalj

**Intro → hero (regel 1, "copy first" + scene fade-up).** På `--bakgrund`: kickern
"MEMOSERVICES AB · SKALA SMART. VÄX LÖNSAMT." sätts som SplitText `words` i röd, Arimo 500,
0,9 s; sedan lyfter papperet (en `--bakgrund`-yta glider upp som en gardin 1,2 s `power3.inOut`)
och avslöjar videon som redan spelar, medan brickorna **faller in i tre djupplan** (fjärr: 9
små brickor 24 px; mellan: 9 brickor 44 px; nära: 7 brickor 72 px, alla i tjänstefärgerna så att
alla sju huvudfärgerna finns) med `back.out(1.3)`. Kickern stannar: den glider upp och blir
navbarens vänstra etikett (det som består).

**Hero (akt 1, scrub: true över 220 vh, ingen pin).** `piren-hero.mp4` autoplay loop full-bleed.
Tre brickplan parallaxar (devices.md § 6, "Layered scenes"): fjärr −31 % av scrollen, mellan −17 %,
nära +0 % men **framför** rubrikplattan så att det nära planet passerar över plattans kant; copy
rider i 1×. Rubriken "RÄTT KOMPETENS. / NÄR NI BEHÖVER DEN." i ink på en pappersplatta
(`--bakgrund` opak, radie `--radie`, 7 kolumner, tyngdpunkt 44 % av höjden) med lead, ingress,
knappar (röd fylld + konturknapp). Rubriken still ≥ 40 vh. Planen har `max-width:none`, fast
pixelbredd, ingen `transition: transform`.

**Passagen (akt 2, pin + pan, spann = railens överflöde + 100 vh, scrub: true).** Orsak in: *dot
field forms the next object*: de 25 brickorna i heron **flyger ihop** till den första 2×2:an i
railen (Flip från hero-läget till railens första objekt) medan grunden byter till `--ink`.
Scenen: en horisontell rail (`x: -(scrollWidth - innerWidth)`, `ease:'none'`, `end` i px som
funktion, `invalidateOnRefresh`), objekt i ordning:
1. rubrikkortet: kicker "TJÄNSTEOMRÅDEN", "DET DU BEHÖVER FÖR ATT VÄXA" (vit, Archivo Black,
   clamp till 7 rem), "Läs mer om tjänsterna →";
2–8. sju objekt, vart och ett 60 vw brett på desktop / 86 vw på mobil: 2×2:an stor (brickor
   16 vh, radie skalad), löpnummer i eget element, namnet (Archivo Black, vit), `kort_pa_startsidan`
   (`--sand`), "Läs mer →" (vit med röd pil);
9. slutnoten: "Behöver du hjälp inom flera områden?" + text + "Kontakta oss →".
Railens objekt får **rail settle** (devices.md § Rail settle): varje objekt kommer in med opacity
.55 → 1 och y 24 → 0 via `containerAnimation` när det passerar 70 % från höger; första objektet
undantaget. Mät överflödet (`rail.scrollWidth - innerWidth`) i konsolen och skriv in det i
NOTES.md. Mobil: samma rail, smalare objekt (passagen finns kvar, aldrig staplad bort).
Brickorna i varje objekt får tilt 6° mot pekaren (hover:hover).

**Kartläggning (akt 3, flow + reveal).** Orsak ut ur passagen: *panel ur axeln*: en lime-bricka
som står sist i railen växer (scale från 1 till den täcker vyn, scrub 120 vh) och blir
kartläggningsbandet på `--lime`: kicker, "HUR REDO ÄR DITT BOLAG FÖR NÄSTA TILLVÄXTFAS?" (ink),
text, knappen "Starta kartläggningen ↗" (ink fylld).

**Om (akt 4, flow+in, `id="om"`).** Orsak: *ark läggs över*: papperet glider upp över limen med
hårlinje. Vänster 7 kolumner: kicker, "ETT AVTAL. / EN KONTAKTPERSON." (ink), text, koncernrad
med länk. Höger 5 kolumner, 12 vh förskjutna nedåt: de fyra punkterna som ledger med
hårlinjer och en liten 2×2-markör per rad (röd/lime som originalet), `<strong>` på fetstilsdelen;
regel 4: punkternas ord tänds grå→ink i scrollens takt (`--grafit` → `--ink` per ord, scrub).

**Insikter (akt 5, reveal per objekt).** Tre objekt i en rad (desktop) / stapel (mobil), varje
som en *plate* utan kant: en stor bricka i kategorins färg (Redovisning marin, Skatt brun, Nyhet
brandröd) 96 px, kategori·datum, rubrik (Arimo 700), utdrag, hårlinje under; clip-path-reveal
nedifrån per objekt med 80 ms stagger. Länken "Alla artiklar och nyheter →" bredvid rubriken.

**Slut (akt 6).** Sidfot på `--ink`. Orsak: *indexet bildas*: de små brickorna som följt med sedan
heron (fjärrplanet, 9 st + 5 till) lägger sig som sju små 2×2 framför tjänstenamnen i
TJÄNSTER-kolumnen när sidfoten rullar in (Flip eller `.to` per bricka, sista triggern
`end:'bottom bottom'`). Adress, e-post, FÖRETAGET, JURIDISKT, copyright, koncernrad; bannern
som sista rad i `--sand`.

## Nav

Katalogens nav är ett **index som hoppar**: en tunn övre rad (48 px, `--bakgrund`, hårlinje
under) med logotypen, de fem länkarna, "Gör en kartläggning ↗" och "Kontakta oss"; under den en
**indexrad** med de sju tjänsterna (liten 2×2 + namn, Arimo 500, 13 px) som är synlig på desktop
och som i passagen markerar den aktiva tjänsten (brickan skalar 1,2, namnet ink; övriga
`--grafit`). Klick på ett indexnamn: `lenis.scrollTo` till objektets läge i passagen (räkna
pinnens scrollposition + objektets x). Indexraden är "Tjänster"-undermenyn: på mobil fälls den
ut under `{{ny.meny}}`. Tangentbord: tab genom indexet, fokus synligt. "Tjänster" i huvudraden
går till `/tjanster`.

## Enheter

intro-tidslinje → parallax i tre plan (hero, scrub) → pin+pan med containerAnimation-reveals (passagen) → reveal/scale (lime ur axeln) → flow+in + ordtändning (om) → reveal per objekt (insikter) → Flip/scrub (slut). Pekare: tilt på brickor, magnet på "Se tjänsterna".

## Övergångsorsaker

gardin upp + brickor faller in (intro→hero) · brickfältet bildar nästa objekt (hero→passage) · panel ur axeln (passage→lime) · ark läggs över (lime→om) · indexet bildas (→slut). Fem olika, aldrig samma två i rad.

## Vad som skiljer C från A och B (fingerprint)

Grammatik gallery/catalog · nav = tunn rad + indexrad som hoppar · hero = full-bleed video med tre parallaxplan av brickor · aktform: 1 pinnad horisontell passage (~8 objekt) + flöde, ~12 vh · slut = brickorna blir sidfotens index · signatur = passagen där heroens brickmoln blir de sju objekten.

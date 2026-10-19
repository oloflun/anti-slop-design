# Riktning B · "Banden" · sju färgband med mosaikkant

Cell: `tests/memoservices-koncept/board/cells/B-r1/` · port 3102 · `?preview=` krokar: `hero`,
`fullbleed`, `band-1` … `band-7`, `flera`, `kartlaggning`, `om`, `insikter`, `slut`.

**Lane (en fras):** platt och ljus, färgbandet är tjänsten.
**Register:** modern clean. **Grammatik:** chaptered editorial, men kapitlen är flata färgband
(Huehaus-principen: logotypens enhet, brickan, är kanten på varje övergång). **Auktoritet
(TASTE § 1):** ytan/färgen. Typen: Archivo Black i stor grad men en vikt, ink eller vit beroende
på band; videon är inramad, aldrig under typen.
**Tell-someone:** "sajten där hela skärmen blir tjänstens mosaik, ett band i taget."
**Grund:** `--bakgrund` som papper mellan banden. Tonal inversion: de mörka banden (marin, grön,
grafit) räknas, plus sidfoten på `--ink`.

## Känslokurvan

| # | Akt | Känsla | Vad på skärmen |
|---|---|---|---|
| 0 | Intro → hero | Fokus | en enda bricka (app-ikonens 2×2) står på papper, växer och blir ramen som håller videon |
| 1 | Hero | Lugn | rubriken på papper till vänster, videon spelar i brickramen till höger |
| 2 | Full bleed | Rymd | ramen växer till hela vyn, rubriken rider med i 1×, kameran går in i fasaden |
| 3 | Sju band | Rytm | vänster kolumn står kvar; grunden byter färg sju gånger med stegad kant; varje tjänsts 2×2 förstoras och *blir* bandet |
| 4 | Flera + Kartläggning | Lättnad | limebandet som åttonde; ljusare, knappen |
| 5 | Om | Förtroende | ett pappersark läggs över limen, två rader rubrik, punkter som ledger |
| 6 | Insikter | Kontinuitet | tre rader med färgbricka |
| 7 | Slut | Svar på öppningen | den sista bilden (videons sista ruta) krymper tillbaka till en bricka i sidfoten |

Peaken är akt 3 (störst spann). Akt 2:s tomma vy när ramen täcker allt och bara kameran rör sig är
avsiktlig tystnad före peaken: skriv det i NOTES.md.

## Akterna i detalj

**Intro → hero (regel 1).** På `--bakgrund` står en 2×2 i mitten (tre `--brand-rod`, `--lime`
nere till höger, varje bricka 64 px, radie `--radie`), inflygning med `back.out(1.4)` och stagger.
Den nedre högra lime-brickan växer till en **ram** (rundad rektangel 16:9, radie `--radie`, ~52 vw
bred) som glider till högra kolumnen medan de tre röda krymper och parkerar som logotypens
mosaikmärke i navet. Videon (`piren-hero.mp4`, autoplay loop) tonas in inne i ramen (ramen är
`overflow:hidden`; `object-fit: cover`). Samtidigt reser sig rubriken ur radmasker till vänster.
Det som består: ramen (= brickan).

**Hero (akt 1, flow, ingen pin).** Vänster: kicker (röd), "RÄTT KOMPETENS. / NÄR NI BEHÖVER DEN."
(ink, clamp upp till 9 rem, leading .92), lead, ingress, två knappar (röd fylld + konturknapp i
ink, radie `--radie`). Höger: videon i brickramen, med 24 px luft mot kanten. Rubriken står still
≥ 40 vh.

**Full bleed (akt 2, pin, spann 220 vh, scrub: true).** Orsak: *card-to-full-bleed grow* (Era,
Forge): ramen växer (Flip eller `width/height/x/y` från mätt rect till `inset:0`, radie → 0)
tills videon täcker vyn; textkolumnen stannar kvar i 1× (ingen parallax på brödtext) ovanpå
på en papperplatta (`--bakgrund`, opak) som i slutet glider upp och ut. Under de sista 20 % av
pinnen ligger videon ensam i vyn (tystnaden). Rubriken får inte klippas när plattan glider.

**Sju band (akt 3, pin, spann 700 vh, scrub: true).** Orsak in: *stegad mosaikkant*: det första
bandet (marin, Redovisning) stiger underifrån över videon med en **stegad överkant** i brickans
enhet (clip-path polygon med 10–14 steg, slumpad höjd 0–2 enheter, animerad `inset`-liknande
polygon som glider upp). Scenen: vänster kolumn (sticky inom pinnen): kicker "TJÄNSTEOMRÅDEN",
rubriken "DET DU BEHÖVER FÖR ATT VÄXA" (står kvar hela akten, vit eller ink efter bandets
ljushet, mät), länken "Läs mer om tjänsterna →". Höger: det aktiva bandets innehåll: tjänstens
2×2 i stor skala (brickorna 18 vh), namnet (Archivo Black), `kort_pa_startsidan`, "Läs mer →".
Bandbyte: nästa tjänsts 2×2 kommer in i liten storlek nere till höger och **växer tills den täcker
hela vyn** (tre brickor i huvudfärg + accent-brickan nere till höger = bandets grund med ett
accentfält i hörnet), medan föregående innehåll glider upp och ut. Sju gånger, ~90 vh var.
Löpnummer "01"–"07" i eget element, Arimo 500. Textfärg per band: ljusa band (ljusblå, oliv, sten)
→ ink; mörka (marin, brun, grafit, grön) → `--bakgrund`. Mät kontrasten per band.

**Flera områden + Kartläggning (akt 4, flow).** Orsak: samma mekanik men bandet är `--lime`
(ett åttonde band utan tjänst): "Behöver du hjälp inom flera områden?" + text + "Kontakta oss →"
överst på limen i ink, sedan kickern, "HUR REDO ÄR DITT BOLAG FÖR NÄSTA TILLVÄXTFAS?", texten och
knappen "Starta kartläggningen ↗" (ink fylld). Det här bandet är **inte** pinnat.

**Om (akt 5, reveal + flow, `id="om"`).** Orsak: *ark läggs över* (ddark): ett papper
(`--bakgrund`) glider upp över limen med rak kant och 2 px hårlinje, scrub över 100 vh.
Vänster: kicker, "ETT AVTAL. / EN KONTAKTPERSON.", text, koncernrad. Höger (med 10 vh
förskjutning, kolumner toppas aldrig lika): de fyra punkterna som ledger-rader med hårlinje och
en liten 2×2-markör (röd/lime enligt originalets punktfärger), `<strong>` på fetstilsdelen.

**Insikter (akt 6, flow+in).** Som en ledger: tre rader, bricka i kategorins färg, kategori·datum,
rubrik (Arimo 700, 1,5 rem), utdrag 52 ch, hårlinje. Länken "Alla artiklar och nyheter →" uppe
till höger om rubriken "INSIKTER".

**Slut (akt 7).** Orsak: *omvänd växt* (Era): videons sista ruta (`piren-last.webp`, eller
videon pausad) ligger full-bleed under sidfoten och **krymper till en bricka** (clip-path inset
från 0 till ~88 % med radie) när sidfoten rullar in, sista triggern `end:'bottom bottom'`;
brickan hamnar bredvid logotypen. Sidfot på `--ink`: adress, e-post, TJÄNSTER med 2×2 per rad,
FÖRETAGET, JURIDISKT, copyright, koncernrad; bannern som sista rad i `--sand`.

## Nav

Sticky full bar, 64 px, som **tar bandets färg**: bakgrunden tweenas till aktiv sektions grund
(`[data-ground]` per sektion, Era-mönstret) och texten inverteras efter grundens ljushet.
Logotypen + fem länkar + "Gör en kartläggning ↗" + knappen "Kontakta oss" (brandröd på ljus,
`--bakgrund` på mörk). "Tjänster" öppnar en **nedfällning i bandform**: en panel som glider ned
under baren med stegad underkant, sju rader med 2×2 + namn i en 7-kolumnsrad på desktop (en
kolumn per tjänst, bandfärg som hover-grund), en lista på mobil. Tangentbord: `aria-expanded`,
pil/tab, Esc. Mobil: `{{ny.meny}}` öppnar helskärm på `--bakgrund`.

## Enheter

intro-tidslinje → flow (hero) → pin+scrub (full bleed) → pin+scrub med stegad reveal (band) → flow (lime) → reveal/scrub (ark) → flow+in (om, insikter) → scrub (omvänd växt). Pekare: magnet på "Se tjänsterna"; i bandakten följer den stora 2×2:an pekaren 6 px (`quickTo`), hover:hover.

## Övergångsorsaker

bricka växer till ram (intro→hero) · ram växer till full bleed (hero→video) · stegad mosaikkant (video→band) · bandbyte genom en 2×2 som växer till grund (inom akten, sju gånger; räknas som aktens inre mekanik) · ark läggs över (lime→om) · omvänd växt (→slut). Fem olika, aldrig samma två i rad.

## Vad som skiljer B från A och C (fingerprint)

Grammatik chaptered (färgband) · nav = full bar som tar bandets färg · hero = video i brickram som växer · aktform: 2 pinnar (220 + 700 vh), ~13 vh · slut = bilden krymper till bricka · signatur = varje tjänsts mosaik förstoras till hela viewporten.

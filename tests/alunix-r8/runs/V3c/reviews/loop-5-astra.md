ship

## persistence

Codex `gpt-6-astra` (`model_reasoning_effort=medium`) kördes av arkitekten 2026-09-17
21:13:55 till 21:21:01 (7 min 6 s, inom tio minuter, ett försök, exit 0). Prompt:
`shots/loop-5/astra/astra5-prompt.txt` (HELHET.md i sin helhet med loop 4:s rader,
femsektionskontraktet, 98 bilder i ordning ur `shots/loop-5/`: 12 + 14 helsidesskivor med
plain `scrollTo` och 3 s väntan, 12 + 12 previews, 12 + 12 flip-ramar, 12 + 12 processramar;
loop 5:s probtabell med jämförelsen mot loop 4:s redovisade golv; de åtta redan verifierade
lägena K13 till K20, var och en **ommätt av arkitekten denna runda, inte tagen på byggarens
ord**; invarianterna F-011, motorn, `--sc-ps`, gate 75, låst copy, `sites/*`, ramarna orörda
efter visning; slutvillkoret utskrivet; de sex frågorna). Rå utdata:
`shots/loop-5/astra/astra5-out.txt`.

Astra svarade **`ship`** med **noll** `material_fixes` och en H-radstabell för alla 35 rader.
Inga nya element eller färger föreslogs.

Arkitekten verifierade Astras fyra kodpåståenden mot filen (`index.html` md5 `d3491b4a`),
eftersom ett `ship` är lika mycket ett påstående som ett fynd och ska granskas lika hårt:

1. *"`.price` har ingen intrinsisk platshållare, rad 735"* — **stämmer**: rad 735-736 är
   `.price{background:var(--c-graphite);color:var(--invert-ink);padding:…}` och ovanför den
   står bara plan 042:s kommentar om den borttagna mekaniken.
2. *"de kvarvarande sovande wrapparna, rad 651 och 857, har allokerad geometri"* —
   **stämmer**: `.calyx-wrap{min-height:90dvh}` (651) och `.horai-wrap{min-height:80dvh}`
   (857). Ingen av dem har en reserverad höjd som beror av innehållet, så prisblockets
   defekt kan inte upprepas av någon annan sovande wrapper.
3. *"Calyx' lika stora translationer tar ut varandra för varje `--rv`, rad 681"* —
   **stämmer**: `.calyx-wrap .rv{overflow:clip;transform:translateY(calc((var(--rv) - 1) *
   100%))}` och `.calyx-wrap .rv iframe{transform:translateY(calc((1 - var(--rv)) * 100%))}`.
   Summan är noll för varje `--rv`, och vid 1 är båda identitet. Hōrais iris (rad 689-696)
   är orörd av 043.
4. *"`driftHand` (rad 1781) räknas ur geometri, inte genom att invänta en korsning"* —
   **stämmer**: den räknas i `measureAct()` som
   `(thesisTop + thesisH + innerHeight - giantTop) / (giantH + innerHeight)`, klamrad till
   [0, 1], och `measureAct` körs vid mount, `resize` och `load` (rad 1828-1830). En läsare
   som djuplänkar mitt i bandet får samma värde; inget ögonblick kan missas.

Noll fynd att förkasta (det fanns inga). Två rader där Astra är mer försiktig än
arkitekten, båda i Astras favör och båda åtgärdade av arkitekten efter passet i stället för
att avfärdas: H-30:s "1440 bidirectional preview walk still unrun" (kördes efter passet,
`shots/loop-5/walkproc5.json`, se § fidelity) och H-24:s "complete device-track proof
remains incomplete" (redovisad som kvarvarande verktygsskuld, inte som uppfylld).

Dispositionen `ship` står och slutvillkorets Astra-del är nådd i runda 5.

## fidelity

Koden gör vad `BRIEF.md` säger (aktsekvensen, `?preview=`-lägena, device-tabellen), och
denna runda utan någon avvikelse. Arkitektens egna mätningar på R10-läget, var och en körd
denna runda och inte övertagen från byggarens grind:

| Vad | Mätning | Tal |
|---|---|---|
| Dokumentgeometri konstant (042) | `geom5.json`, `preview390_5.json` | `scrollHeight` 10 582 px vid load och i bandet (1440), 11 326 (390); motorns `#process`-topp = DOM:ens, 5 340 = 5 340 och 6 152 = 6 152, i 21 av 21 laddningar, utan resize |
| `?preview=process-0N` vid 390 (042) | `preview390_5.json` + `preview/p01check.json` | 20 av 21 laddningar `--sc-ps` inom 0,0001 från `--eN`; en landade 0,2400 mot 0,2450 (`k1` 0,971) och stod stilla där i 8 s. Åtta extra laddningar av steg 01: 8 av 8 exakta, `stroke-dashoffset` 0 på båda ritade banorna. Vid 1440: 7 av 7 |
| Calyx-revealen har en öppning (043) | `verify/` | wrapperbakgrund synlig 100,0 / 74,9 / 50,0 / 0,1 % vid `--rv` 0 / 0,25 / 0,5 / 1; `.rv` har `overflow:clip`; ramens egen box står på top 40 i alla fyra (pixelstilla); identitet vid 1. Hōrais iris i samma körning 99,9 / 44,9 / 12,0 % svart |
| Driftens överlämning (044) | `verify/`, `drift-3620.png` | `--sc-canvas` 3 600 rgb(18,63,104), 3 620 rgb(19,64,104), 3 700 rgb(35,76,114), 3 800 rgb(76,109,138), 4 000 rgb(185,195,203); träets mellanton (720,40) chroma 21 → 20 → 19 → 15 → 5. Inget steg över 40 per kanal per 20 px |
| Revealens latch efter 043 | `latch5.json` | hjul, PageDown, `scrollTo`, smooth `scrollTo` och resize-före-bandet ger `--rv` 1 / 1 på båda wrapparna; noll `--rv`-skrivningar tre sekunder efter landning |
| Kontrast, hela sidan | `contrast_over_media.py --url` | 1440 vid scrollY 0 / 3 300 / 4 800 / 5 400 / 8 000 / 9 700: 61 strängar, alla godkända, sämsta 6,70:1. 390 vid 0 / 2 900 / 5 600 / 7 000 / 10 400: 41 strängar, alla godkända utom en verktygsartefakt (se H-34) |
| Processakten i **båda riktningarna** vid 1440 | `walkproc5.json` | ned: `--sc-ps` monoton, max steg 2,50 %, stegen tänds 01 → 02 → 03 → 04 → 05 → 07 i ordning, banorna ritas kontur → glyf → måttlinje utan att gå om varandra. Upp: monoton, samma sekvens baklänges, arket ritas av till tomt ark vid aktens början. Symmetriskt |

Pixlarna, skärm för skärm (1440, `slices-1440/`, tolv skivor mot loop 4:s tretton eftersom
dokumentet är 298 px kortare): s00 till s02 matchar (rubriken dominerar, kortet vänds, hela
baksidan med glyfen). **s03 avviker** (tes + jätterubrik lika tunga, Q30, väntar på Anton;
grunden är kallt ljus, inte tvätt). s04 matchar (Calyx hel och dominerande mot liggaren).
s05 matchar (Hōrai dominerar prisplanet; prisliggarens tredje linje mitt i dragningen).
s06 matchar (processentrén med hel kontur och ritad glyf bredvid steg 01: det som var
Astras loop-4-bild 77 är borta). s07 till s09 matchar (arket kumulativt, måtten i accent,
Calyx maskad i öppningen, tonbytet vid steg 07). s10 matchar (principerna i rail, papper →
foto helbrett). s11 matchar (avslutet ensamt på fotot med sin dragna linje). 390
(`slices-390/`, fjorton skivor): s00 matchar (10,0 % död grund), s01 till s03 matchar,
s04 matchar (Calyx hel; Calyx egen nav över sitt ordmärke är referenssajtens, rapporterad
sedan R9), s05 till s13 matchar.

Astras H-radstabell mot arkitektens bockar (loop 5, HELHET § 3):

| H | Astra | Arkitekten | Dom |
|---|---|---|---|
| H-01, H-04 till H-07, H-09 till H-14, H-16 till H-20, H-25 till H-29, H-31, H-33, H-35 | met | [x] | överens |
| H-02, H-03, H-08 (s03) | waiting for owner | [ ] Q30 | överens; räknas inte som öppna fynd |
| H-15 | met (bild 7 och 77) | [x] | överens; 042 stängde loop 4:s enda kvarvarande orsak |
| H-21, H-22, H-32 | "numerical bar unmet; architectural floor, accounted for" | [ ] golv | överens; talen håller loop 4:s redovisade golv eller är bättre (§ keep) |
| H-23 | met vid cpu 1; cpu 4 jätten 3,31 % | [x] | överens; raden bockas på samma grund som loop 3 använde (cpu 1), och alla akter ligger nu ≤ 3 % (jätten 2,65, tesen 2,31 till 2,90, mot loop 4:s 3,12 och 3,52) |
| H-24 | "no verified dead device found; complete proof incomplete" | [ ] | överens; verktygsskuld, oförändrad. `.horai-wrap .rv:transform` rapporteras DEAD och det är **rätt**: Hōrais device (BRIEF § Device-tabell rad 6) är en iris, inte en transform på `.rv`. Loop 4:s rad skrev "inga DEAD" om det spåret och det var fel mot dess egen json; rättat i loop 5 |
| H-30 | "formed states supported; 1440 bidirectional walk still unrun" | [x] | **avvikelse, Astras favör, sedan åtgärdad**: arkitekten körde vandringen efter passet (`walkproc5.json`) och den håller i båda riktningarna; raden bockas på den mätningen, inte på Astras |
| H-34 | met on supplied measurements | [x] | överens; hela sidan mätt denna runda, inte bara folden |

Svar på frågorna 1 till 4, sammanfattat: sidan läser som en sida (fotografisk grund,
A-glyfen som återkommande objekt, ritningen, grafitplanet, det återhållna blå måttet); det
enda som fortfarande läser som två kapitel på samma skärm är bandets entré, som är Q30.
Rytmen: inga nya skarvar, inga slitsar, ingen oförfattad tom skärm. Balansen: en auktoritet
per skärm utom s03 (Q30). Rörelsen: kortet kontinuerligt genom tolv ramar, arket kumulativt
och symmetriskt i båda riktningarna, previews 7 av 7 vid 1440 och 21 av 21 vid 390, Calyx
öppnar, driften tonar över utan hopp.

## ceiling

- insign: ingen kvarvarande fördel i utskrivna kundlöften; V3c:s sju stycken säger samma
  sak i prosa.
- highwaymedia: ingen kvarvarande brist i fassekvensen; ritningen har början, utveckling
  och avslut, och ligger inte längre ur fas med prosan (042).
- hoy: en auktoritet per kapitel i full bredd är fortfarande skillnaden vid bandets entré
  (s03). Det är Q30 och Antons beslut, inte ett fynd.
- K3: ingen kvarvarande materiell fördel i ritningen; V3c:s 390-previews är inte längre ett
  race.

## material_fixes

none

## keep

Astras egen keep-lista, verifierad av arkitekten och utökad med talen:

- Konstant dokumentgeometri från första laddning (042): 10 582 / 11 326 px.
- Calyx öppning uppifrån med utraderande transformer (043); ramen pixelstilla under
  revealen, identitet vid 1.
- Geometrihärledd, reversibel driftöverlämning (044): `driftHand` i `measureAct`, klamrad,
  ommätt vid resize och load.
- `--sc-ps`-kontraktet: LERP 0,16, DEAD 0,0005, `inherits:true`, **staircase 0 på varje
  kontraktsspår i varje körning**, båda riktningarna, båda kadenserna, cpu 1 och 4. De två
  extra spår som först rapporterade staircase 1 (`.calyx-wrap:--rv`, `.horai-wrap:--rv`)
  gav staircase 0 när de probades från **före** revealens utlösning i stället för efter:
  flaggan var probens egen settle-platå, bevisat i två körningar, inte sidans.
- Engångsreveal på wrappern, wrapperobservern och ramarnas sömn.
- Hel kontur vid processentrén, den kumulativa ritningen, måtten i accent som byter till
  `--hair-ink` vid steg 07.
- Seamsen (162 px vid 1440, 101 till 102 px vid 390), spaltoffseten 108 px, grafitplanet,
  avslutet ensamt i sin viewport, den vägoberoende latchen (035), Hōrais kvadratiska iris
  med kontraskalad ram (036 A), monteringen i heroens svans (036 B), `aimPreview` med
  generations-id (037), lägena ur shimens `cur` (039), 24 % drift (038), driften skriven
  på `.ground` av sidan (041).
- Bildtidens golv som det nu står, för nästa rundas skull: cpu 4 hero ned 280,1 ms (loop 4
  333,8), hero upp 49,9 (79,7), `#process` ned 83,2 (326,9) och upp 50,1 (474,6), jätten
  250,0 (462,0), priset 238,2 (875,9); cpu 1 hero ned median 33,6 (78,2), hero upp 16,8
  (35,4), `#process` 17,1 / 17,0 (18,2 / 18,2), jätten 50,2 (101,6), priset 46,7 (40,4),
  tesen median 142,4 (142,4), avslutet 16,9 (18,3). Varje fönster lika med eller bättre än
  loop 4:s redovisade golv.

Inga nya element eller färger föreslogs av Astra; arkitekten föreslår inga heller inom
golvet. Den enda tillkommande posten i nästa runda är Antons egen beställning av ett
inverterat läge för processakten (plan 045), som är ett jämförelseunderlag åt honom och
inte ett fynd ur den här granskningen.

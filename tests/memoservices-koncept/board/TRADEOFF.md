# Avvägningstabell · tre riktningar för memoservices.se

Boarden: `python ~/.agents/skills/design/scripts/board.py tests/memoservices-koncept/board --port 4630 --fallback-root . --single`
(launch-posten `memo-board`). Tangent 1–3 byter riktning, `f` öppnar betyg, `submit` skriver `feedback.json`.
Ingen favorit anges här; boarden väljer.

| Riktning | Var den står på axeln (grammatik) | Rätt när | Kostar |
|---|---|---|---|
| **A · Linsen** | Filmic one-shot: videon är auktoriteten, mosaiken är fönster och lins; kamerafärden drivs av hjulet | Linda ska känna *platsen* först och tjänsterna som något som växer ur byggnaden; demon i Teams får sin effekt av att scrollen styr kameran | Två långa pinnar (hero 300 vh + fasad 500 vh); mörk första halva; mest tid i heron innan innehållet; mest känslig för en svag dator i delningen (scrubbad video) |
| **B · Banden** | Chaptered editorial i flata färgband: ytan är auktoriteten; varje tjänsts 2×2 blir hela viewporten | Tjänsterna ska vara det man minns, var och en som ett rum i sin färg; starkast koppling till deras app-ikon och mosaik; mest "sajt" av de tre (minst effekt för effektens skull) | Videon får en mindre roll (ram → full bleed → bort); sju bandbyten i rad är en lång pinnad akt (700 vh) som måste scrollas igenom; ljusa band kräver mätt textfärg per band |
| **C · Passagen** | Gallery/catalog: objektet (brickan) är auktoriteten; brickmolnet i djupplan blir en sidledes passage | De sju områdena ska upplevas som jämbördiga objekt man går förbi, med indexraden som permanent karta; luftigast och ljusast; bäst nav för "direkt till en tjänst" | Horisontell passage är en känd risk på laptop-trackpad (sidledes scroll = ovant); mörk passage mitt i en ljus sida; längsta sidan (≈ 12–14 vh) |

## Runda 3 (flik 4–6): "nivån upp"

Samma tre grammatiker, men ett enda bricklager som formar om sig genom hela sidan (inga pinnar
utom heron), nya sans-par i gemener och nya layouter.

| Riktning | Typsnitt | Vad som är nytt | Rätt när | Kostar |
|---|---|---|---|---|
| **A3 · Linsen II** | Bricolage Grotesque 300/500 + Host Grotesk | centrerad lätt rubrik över scrubbad video bakom ett fönsterraster; kompassen (brickorna som sidans läge); sticky rubrikkolumn + lysande lista | den mörka filmkänslan ska vara kvar men lättare och mer skriven | fortfarande en lång hero-pin; mörk första halva |
| **B3 · Banden II** | Schibsted Grotesk 800 + Onest | rubrik 12/12 + videoband; sidans grund är fyra fält som byter färg per tjänst med stegad kant; sticky tjänsterail som karta | tjänsterna ska vara rummen och listan alltid synlig | sju bandbyten i följd; mobilen får en smal accentremsa |
| **C3 · Väggen** | Funnel Display 500 + Figtree | video med ink-remsa nederst; väggen av sju 2×2; varje tjänst växer till rummet inne i det föregående; golv, kolumn, index | brickan ska bära hela resan som ett objekt (d2c-principen) och sidan ska kännas ljus och katalogisk | högra fältet i dyken är tyst; sju dyk à 100 vh |

## Anti-konvergenstest
Byt rubrik mellan två celler: A:s hero är en ink-platta över scrubbad video, B:s en pappersyta med
video i bricka, C:s en pappersplatta med brickmoln i djup. Bytet syns. Navigationen skiljer sig i alla
tre (hörnbrickor / full bar som tar bandets färg / tunn rad + indexrad). Slutet skiljer sig (brickorna
samlas till app-ikonen / videon krymper till bricka / indexet bildas i sidfoten).

## Gemensamt i alla tre
Samma låsta tokens, samma ordagranna text (0 avvikelser i textkontrollen), samma video, mosaiken
som signaturobjekt, GSAP 3.15 + Lenis från den globala installationen, husets tempo.

## Vad som händer efter valet
Den valda riktningen blir Step 4-utgångspunkt för de nio sidorna (översikt + sju tjänstesidor med
Kvittotolken på Redovisning) enligt BESTALLNING § 3. De två andra cellerna behålls på boarden som
referens.

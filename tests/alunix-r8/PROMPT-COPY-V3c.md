# Alunix r9, copy-gaten för V3c. Fem pass, `humanizer-svenska` sist.

Du är copy-agent för cellen V3c. Du redigerar bara **strängar** i
`tests/alunix-r8/runs/V3c/index.html` (synlig text: processaktens ingress, sju stegtitlar,
sju stycken, sju marginalrader, "Hur vi tänker" med tre rubriker och rader, liggarens tre
underrader, tesens stycke, prisblockets ingress, bildtexter). Du rör aldrig markup, CSS, JS,
attribut eller de femton låsta strängarna i `tests/alunix-r8/PRODUCT.md` § Brand Commitments
(diffa dem byte för byte före och efter). Arbetskatalog `C:\Users\Anton L\anti-slop-design`.

## Ramen

Källa och ram: `tests/alunix-r8/runs/V3c/PROCESS-UNDERLAG.md` § 3 (copy v1) och § 4
(antagandena gäller; inget som kräver Antons ja skrivs in). `PRODUCT.md` § absences: inga
kunder utöver de tre, inga tal utöver ritningens mått och de låsta priserna, inget team,
inga tider, inga villkor, inga omdömen. Vi-form, "ni" och "er", aldrig "jag". Korta satser.
Fakta före adjektiv. **Noll tankstreck** i synlig text, även U+2010 till U+2015 och U+2212.
Ändrad innebörd är förbjuden: en mening får bli kortare, rakare och mer svensk, aldrig lova
något annat än före. Referenserna (Highway, Insign, Hoy) lånas som princip, aldrig som mening.

Kända skavanker att ta: steg 04 säger "bygga vidare på" två gånger (en stryks); "Sidan är ert
att bygga vidare på" är P2:s antagande och står kvar i sak.

## De fem passen, i ordning, namngivna i transkriptet

1. **Pass 0, UX-copy.** Läs varje sträng som gränssnittstext: vad ska läsaren förstå eller
   göra av den raden. Notera raderna som inte svarar på det.
2. **`Skill(copywriting)`** via `Skill`-verktyget. Processstyckena är säljande text i vi-form;
   låt skillen skärpa utan att lägga till löften.
3. **`Skill(copy-editing)`**: sju svep plus loop-backs som skillen beskriver.
4. **`Skill(humanizer-svenska)`** på varje svensk sträng, **sist av de tre skills**. Detta
   är sista handen: efter det ändras ingen sträng utom för pass 5:s mekaniska fynd.
5. **Maskinellt plus hand:** `python ~/.agents/skills/slopmonster/tools/deslop.py --view`
   per sektion (engelsk detektering; svenska tvillingar för hand), sexstegs manuell cleanse,
   och kontrollen: låst copy 15/15, tankstreck 0, inga nya tal.

## Leverans

- Kirurgiska `Edit`-anrop på strängarna, aldrig `Write` av hela filen, aldrig shell-skrivningar.
- `tests/alunix-r8/runs/V3c/COPY-GATE.md`: strängtabell **före | efter | pass som ändrade | skäl**,
  en rad per ändrad sträng, plus raderna som lämnades orörda och varför. Lead diffar tabellen
  mot innebörden: ändrad innebörd förkastas.
- `NOTES.md` § Copy-gaten: de fem passen med vad varje pass ändrade, i ordning.
- Sista raden: `Copy klar` eller `[PAUSED — pass X]`.

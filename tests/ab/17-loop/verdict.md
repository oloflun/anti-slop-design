# T17 — kedjans riktiga läge: K1 + två Step 5-rundor (critique → fix, a11y + skript → fix)

| Mått | K1 (före) | efter runda 2 |
|---|---|---|
| axe-violations | 1 (flimrande kontrastträff pga reveal-race) | 0 (stabilt över 3 körningar) |
| korall på fog (10.5 px-etiketter) | 3.71:1 | 5.67:1 (ny --korall-onlight) |
| alt-texter som beskrev fel bild | 3 | 0 (verifierade mot hämtade bilder) |
| px-satt text | 10 selektorer | 0 (rem) |
| tabellcaption / rubrik i avslutet | saknades | tillagda |
| oavslöjade element i helsida / [scrollcraft]-varningar | 0 / 0 | 0 / 0 |

Läst (compare-loop.png): hero-högerpanelen är omcroppad mot blommorna, i övrigt är sidan identisk i stillbild; det pinnade bröllopspartiets tomma spacer syns fortfarande som en blank remsa i helsidan (samma klass som AB06: en pinnad akt med gles innehåll). Loopen gör sidan **korrektare**, inte **modigare**.

**Beslut: loopen är nödvändig men inte svaret på "underwhelming".** Ambitionen bestäms i Step 2b (register × grammatik × värld, förbjudna syskondrag), inte i Step 5. Tillägg: helsides-captures utan scroll ska flaggas för "tom remsa > 60 % av en viewport" så att pinnade set-pieces med gles innehåll fångas som defekt (läggs i scroll_verify som `blankBands`).

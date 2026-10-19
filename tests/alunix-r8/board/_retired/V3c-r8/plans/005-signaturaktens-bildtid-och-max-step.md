# 005 · Signaturaktens bildtid, och max_step över baren

## Problem
Två tal, en rot. `section.hero:--sc-ps` ger `max_step` 3,38 % mot barens 3 % (leadens mätning
med ren kontroll vid cpu 1) och 3,67 % i prestandagranskarens omkörning. Bildtiden är värre:
p95 37,5 ms och 49 rutor över 33 ms vid cpu 1, och p95 133 till 144 ms med 74 till 109 rutor
vid cpu 4. Orsaken är mätt, inte gissad: med `/sites/**` blockerat kvarstår p95 83,3 ms, och
`Performance.getMetrics` över samma scroll ger RecalcStyle 3 768 ms av 5 134 ms tasktid,
alltså 73 %, mot Layout 5 ms och Script 332 ms. Sex ablationer (ordscrub, jätte, flip, tråd,
grund, filter) tar var för sig inte bort den. `staircase` är 0 i varje körning, båda
kadenserna, båda riktningarna: detta är F-013:s andra fel, inte det första.

## Target
`max_step` högst 2,7 % på `section.hero:--sc-ps`, p95 högst 20 ms och noll rutor över 33 ms
vid cpu 1 med kontrollen körd ren omedelbart före, `staircase` kvar på 0, och heron kvar som
sidans största spann.

## Conventions
Platta aldrig ut easingen (Q22). `max_step` gatear bara spelhuvudet.

## Steps
1. Kör kontrollen `tests/motion/smooth.html` före varje mätning. Mät sidan bara när
   kontrollen ger noll rutor över 33 ms.
2. Svep `data-sc-span` på `section.hero` 2,2 till 2,6 till 3,0 till 3,4 och skriv `max_step`
   per steg.
3. Jaga RecalcStyle: hitta vilken selektor som räknas om per bildruta. Misstänk regler som
   matchar brett och som beror på en custom property som skrivs varje frame.
4. Mät om, både 100:60 och 20:120, båda riktningarna.

## Boundaries
Motorn redigeras aldrig. `--sc-ps` byts aldrig mot `--sc-p`.

## Verification
Kontrollens tal och sidans tal bredvid varandra i NOTES.md, per svepsteg.
Feel-check: vändningen ska kännas som ett kort som vänds med handen, i båda riktningarna.

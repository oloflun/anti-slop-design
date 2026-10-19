# 008 · Hyperborea-plåten bleeder inte, och dess akt är död

## Problem
Arkitekten mätte 32 px överhäng förbi den blå platens högerkant (696 till 728), alltså 11 %
av insatsens egen bredd, medan målbilden säger att platen ska bleeda. Prestandagranskaren
mätte dessutom att `.thesis-figure` håller ett konstant `matrix(1,0,0,1,33.3111,0)` vid varje
scrolloffset mellan 0 och 3000 px, medan BRIEF.md device-tabell rad 3 lovar en
`--sc-ps`-driven bleed. Överhänget är alltså inte bara litet, det rör sig inte alls.

## Target
Insatsen lämnar den blå platen på minst en kant med minst 96 px vid 1440, eller går ut till
spaltens ytterkant. Rörelsen läser `--sc-ps` och `motion_probe` rapporterar `dead: false`.

## Conventions
Allt som ögat ser förflytta sig läser `--sc-ps`, aldrig rått `--sc-p` (F-014). En insats som
ligger 32 px utanför läser som en förskjutning, inte som en bleed.

## Steps
1. Bekräfta att spåret är dött med `motion_probe` och skriv talet i NOTES.md.
2. Koppla transformen till aktens `--sc-ps`.
3. Öka överhänget till minst en rail och mät det i pixlar.

## Boundaries
Hyperborea-bilden byts inte. Den blå platens färg och bredd rörs inte.

## Verification
`motion_probe` på `.thesis-figure:transform` med `dead: false`, plus en pixelmätning av
överhänget.
Feel-check: platen ska läsa som att den skjuter ut ur bandet.

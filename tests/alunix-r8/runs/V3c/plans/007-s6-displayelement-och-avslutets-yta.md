# 007 · s6:s displayelement är sidans minsta, och avslutet delar skärm

## Problem
Två fynd i samma spalt. Arkitekten mätte att prisrubriken sätts på ungefär 38 px mot
jätterubrikens 80 px och mailto-radens 54 px, alltså sidans minsta displaymoment, på en skärm
vars högra halva är ett fullblödande matfotografi. Heuristik- och kraftgranskaren fann
dessutom att `.close` bara har 108 px toppadding, så mailto-raden delar sista viewporten med
prisblocket och Hōrai, och målbildens krav att avslutet står ensamt uppfylls aldrig.

## Target
Prisrubriken minst 48 px vid 1440, alltså minst 0,6 gånger jätterubriken, så att
vänsterspalten äger skärmens största glyfhöjd vid s6. `.close` `min-height` så att avslutet
fyller minst 62 svh och mailto-raden står ensam i sin viewport vid 1440 och 390.

## Conventions
Priserna och brödgraden rörs inte. Ingen ny CTA, inget formulär.

## Steps
1. Mät nuvarande glyfhöjder och skriv dem i NOTES.md.
2. Höj prisrubriken och sätt `.close` `min-height`.
3. Skjut s6 och s7 vid 1440 och 390 och läs båda som bilder.

## Boundaries
Låst copy ändras aldrig. Prisliggarens tre rader och deras tal rörs inte.

## Verification
Glyfhöjderna utskrivna, plus en helsidesfångst som visar att s7 är en egen skärm.
Feel-check: sista skärmen ska vara tyst och sluta stilla.

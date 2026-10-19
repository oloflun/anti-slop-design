# 006 · Kickern på kortets baksida tillbaka till målbildens sträng

## Problem
Kickern står `WEBBYRÅ I SVERIGE` i stället för målbildens `Digital byrå`, utan rad i decision
ledger. Arkitekten och kritikern dömer båda retur, med tre skäl: målbilden är kontraktet och
bytet saknar ledgerrad; kortets tes är att sajten är nutidens visitkort, och på ett visitkort
står yrkesbeteckningen, inte sökfrasen; och versal mono i formen substantiv plus ort är
kategorins default i sin sökmotorvariant, vilket rut-testet i concepts-V3c.md punkt 8
uttryckligen håller utanför.

## Target
`Digital byrå`, Geist Mono 10,5 px, tracking .22em, i övrigt oförändrad.

## Conventions
Ett framtida byte kräver en rad i BRIEF.md decision ledger med källa och källregel, skriven
före bytet.

## Steps
1. Byt strängen.
2. Skriv en ledgerrad som dokumenterar att bytet prövades och återställdes, med skälet.

## Boundaries
Ingen annan sträng på kortet rörs. Strängen är inte låst copy, men målbilden är bindande.

## Verification
Pixelläsning av `?preview=back` vid 1440 och 390.
Feel-check: raden ska läsa som en yrkesbeteckning på ett visitkort.

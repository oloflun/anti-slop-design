# 002 · De levande ramarna tar över scrollen och tabbordningen

## Problem
Två fynd med samma rot. Heuristikgranskaren mätte att hjul och tumme över Calyx (90dvh) och
Hōrai (80dvh) scrollar den inbäddade sajten i stället för sidan: sidans enda navigationsmedel
lämnas över till främmande dokument på två av sju skärmar (Nielsen 3, fail). A11y-granskaren
mätte att samma ramar är tabbstopp utan synlig fokusmarkering före montering
(`:focus-visible` false, `outline: none`, `rect.top` 2380, och sidan scrollar inte dit), och
att tabben efter montering går in i två hela främmande sajter, åtta stopp.

## Target
100 % av ramarnas yta scrollar sidan. Högst tre Tab-stopp från toppen till kontaktlänken.
Ramarna syns aldrig som fokusstopp, varken monterade eller omonterade.

## Conventions
Ramarna får aldrig transformeras eller tonas efter att de visats (PRODUCT.md). De ska
fortfarande vara synligt levande sidor, inte skärmbilder: det är hela beviset.

## Steps
1. `pointer-events: none` på båda `.frame-wrap` och `inert` på båda, prövat i webbläsaren.
2. Kontrollera att ramarna fortfarande renderar och animerar internt, alltså att beviset
   lever, och skriv utfallet i NOTES.md.
3. Tab-vandra sidan och skriv ut varje stopp i ordning.

## Boundaries
Ingen overlay-bild över en ram. Ingen skärmbild som ersättning.

## Verification
`tab_walk.py` mot URL:en med stoppen utskrivna, plus en manuell hjulmätning över mitten av
varje ram som visar att sidans `scrollY` ändras.
Feel-check: att dra tummen över Calyx ska flytta sidan, inte Calyx.

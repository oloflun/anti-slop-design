# 004 · Kortets kantställda linje klipps till 405 av 502 px

## Problem
Arkitekten mätte kolumnvis i `preview-mid.png`: linjen står på x 532 och löper y 296 till
701, sedan noll kontrast, medan kortet är y 296 till 798. Bortfallet ligger helt i
underkanten, alltså en klippning och inte en perspektivförkortning. Codex isolerade orsaken
till `index.html:271`, `.hero-plate{overflow:clip}`, genom att slå av den ensam: som byggd
projiceras kanten till 749 px och 420 målas; med `overflow:visible` på platen målas 749.
Stagens egen `overflow:clip` och platens `container-type` är oskyldiga, båda avstängda var
för sig. Förlusten är asymmetrisk, 110 px upptill och 219 px nedtill, därför att klippet
läggs i den otransformerade lokala boxen och sedan projiceras.

## Target
Linjens målade höjd lika med kortets projicerade höjd, 502 px plus minus 4 vid 1440x900, med
över- och underkant sammanfallande med `figure.hero-plate`s.

## Conventions
Byggaren skrev på rad 264 att klippet står kvar med avsikt, eftersom kortets närmaste kant
annars sticker 84 px utanför vid 63 grader. Den avvägningen är riktig och ska inte kastas:
lös klippningen utan att låta kortet spilla ut över rubriken.

## Steps
1. Logga `.plate-card`s och båda `.face`s `getBoundingClientRect()` vid `--flip: 0.5` och
   skriv talen i NOTES.md.
2. Pröva ett klipp som följer den projicerade geometrin i stället för den lokala boxen, eller
   flytta klippet till en förälder vars box inte roterar.
3. Mät om linjens målade höjd, kolumnvis, i samma bild.

## Boundaries
Kortet får aldrig spilla över rubriken eller utanför platens rail. `--flip`-kurvan rörs inte.

## Verification
Kolumnmätning av `preview-mid.png` med linjens span utskriven.
Feel-check: vid 90 grader ska kanten läsa som ett kort som står på högkant, hela vägen.

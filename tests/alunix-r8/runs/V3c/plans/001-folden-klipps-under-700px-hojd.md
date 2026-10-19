# 001 · Folden klipps under 700 px viewporthöjd

## Problem
Den pinnade stagens `overflow: clip` skär foldens innehåll när viewporten är låg. Mätt av
a11y-granskaren mot den levande URL:en: vid 1280x600 kolliderar ordmärket med rubriken med
48 px OCH den låsta underraden klipps bort med 37 px, med rubrikens överkant på -7 px. Vid
720x450, vilket är 1440x900 vid 200 % zoom, blir det -27 och -21. Vid 1024x640 utan zoom -16
och -6. Samma rot ger 129 px klippning vid textavstånd 1.4.12. Att låst copy försvinner ur
dokumentet är det allvarligaste: underraden är ordagrann copy ur PRODUCT.md.

## Target
Vid varje kombination av bredderna 320, 375, 390, 414, 768, 1024, 1280 och 1440 med höjderna
450, 600, 640 och 900: noll kollision mellan ordmärke och rubrik, hela underraden inom
viewporten, rubrikens överkant minst 0. Samma sak vid 200 % zoom och vid WCAG 1.4.12.

## Conventions
Foldens höjdbudget löses med typskalan och stagens egen höjd, aldrig genom att ta bort
`overflow: clip` från stagen, som bär pinnen. Motorn redigeras aldrig.

## Steps
1. Logga `getBoundingClientRect()` för toppraden, `h1.hero-headline`, `figure.hero-plate` och
   underraden vid alla åtta bredder gånger fyra höjder. Skriv talen i NOTES.md före ändring.
2. Bind foldens vertikala rytm till `svh` i stället för fasta px, och ge rubrikens `clamp()`
   ett golv som faller med viewporthöjden, inte bara med bredden.
3. Mät om samma matris.

## Boundaries
Låst copy ändras aldrig. Kortets storlek och 16:9-förhållande vid 1440 rörs inte.
Signaturaktens `--flip`-fönster rörs inte i den här planen.

## Verification
Matrisen ovan med alla värden utskrivna i NOTES.md, plus `reflow.py` mot URL:en.
Feel-check: vid 200 % zoom ska folden fortfarande läsa som ett kort på en grund, inte som en
avskuren rubrik.

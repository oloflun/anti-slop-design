# Alunix, V3d runda 10: Hyperborea-bilden beskärs vid 390. Cell {{KONCEPT}}, ut-mapp `{{UT_MAPP}}`, port {{PORT}}.

I R9 blev fotot i tesbandet större vid 390, men nu beskärs vänsterkanten. Rubriken inne i
skärmbilden läses som "ystems / ith warmth" i stället för "Systems with warmth". Se
`{{UT_MAPP}}/shots/lead-r9/thesis-01.png` och `thesis-03.png`.

**Mål:** vid 320, 375, 390, 414 och 768 syns sajtens vänsterkant och rubriken "Systems"
hel. Fotot ändrar inte fyllnaden eller höjden från R9. Lös det med `object-position` eller
`background-position` förankrad i vänsterkanten (eller vänster och överkant), eller med en
proportion som visar sajtens vänstra del. Vid 1440 ändras ingenting, och det kontrolleras
pixel för pixel mot före-bilden.

`Skill(design)` först. Använd kirurgiska `Edit`. Verifiera med enskilda skärmbilder av
`?preview=thesis-01` och `thesis-03` vid de fem bredderna och läs dem. Kontrollera också att
ingen sida scrollar horisontellt. Leverans: `NOTES.md` § V3d R10. Sista raden ska vara
`V3d R10 klar`.

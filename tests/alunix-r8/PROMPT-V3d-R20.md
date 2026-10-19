# Alunix, V3d runda 20: det frysta konturarket korsar stegbandets text. Cell {{KONCEPT}}, ut-mapp `{{UT_MAPP}}`, port {{PORT}}.

Lead har läst övergången vid 1920x930 i 200 px-steg, i enskilda bilder:
`{{UT_MAPP}}/shots/lead-r19b/04.png`–`07.png`. När `.tes-plane` fryser (`data-frozen`, fixed)
och landar om på steg 01:s ark, ligger dess kontur **ovanpå** band 01. Arkets överkant drar
då en linje rakt genom "01 UPPSTART / Vi börjar med ett samtal…". Se `05.png`, där linjen
passerar genom brödtexten, och `04.png`, där konturen står bakom siffran.

**Mål:** det frysta arket ligger under stegbanden i stacken, så att banden täcker det precis
som de täcker steg 01:s sticky ark. Inget av dess streck får synas över eller genom någon text
i något scrolläge. Mät med en hjulsekvens i 20 px-steg åt båda hållen genom 1000 px före och
efter `data-gone`, vid 1920x930, 1440, 768 och 390. Kontrollera varje bildruta med
`elementsFromPoint` längs arkets fyra kanter: inget av dess streck får ligga ovanför en
textnod. Läs bilderna.

Kan det inte lösas rent med stacken, tar du bort `data-frozen`-omlandningen och låter det
landade arket rulla ut med kapitlet, som i R19a. Motivera valet i NOTES.

`Skill(design)` först. Använd kirurgiska `Edit`. Rör ingenting annat, och pixeldiffa resten
av sidan mot R19. Leverans: `NOTES.md` § V3d R20. Sista raden ska vara `V3d R20 klar`.

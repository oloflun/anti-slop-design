# Alunix, V3d runda 15: case-rubrikens mening på mobil. Cell {{KONCEPT}}, ut-mapp `{{UT_MAPP}}`, port {{PORT}}.

I R14 döljs `.case-line` helt under 768 px (`index.html` rad ~1012), med lead-valet
öppet i kommentaren. Lead väljer **alternativ 1: meningen visas bara i steg 1**. På mobil ska
rubriken "Calyx fick bli ett vårnummer." respektive "Hōrai dukar upp kvällen och ber om
bokningen sist." synas hel medan steg 1 läses. När steg 2 tar över tonas `.case-line` ut och
fäller ihop sin höjd, så att R8–R11:s bildkrav för de senare stegen (bildtexten inne i ramen)
håller exakt som i dag. Ut- och intoningen är scrubbad på casets egen progress i båda
riktningarna, utan transition-tid. `h2` behåller hela meningen som tillgängligt namn i alla
lägen. 1440 och 1920 rörs inte, och det kontrolleras pixel för pixel mot
`{{UT_MAPP}}/shots/lead-r14/w-*.png`.

`Skill(design)` först. Använd kirurgiska `Edit`. Verifiera vid 390 och 375 med enskilda
skärmbilder av `?preview=case-calyx-01`, `-02`, `-03`, `case-horai-01`, `-02` och `-03`, och
med en hjulsekvens i 20 px-steg genom övergången från steg 1 till steg 2. Läs bilderna.
Rubriken ska vara hel i steg 1, texten får inte överlappa, och steg 3:s bildtext ska ligga
kvar inne i ramen. Kör rubrikskriptet och `a11y_scan` vid 390. Leverans: `NOTES.md`
§ V3d R15. Sista raden ska vara `V3d R15 klar`.

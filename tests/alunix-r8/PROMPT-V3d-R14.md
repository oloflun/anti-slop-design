# Alunix, V3d runda 14: tre fynd ur leadens läsning av R13 vid 1920. Cell {{KONCEPT}}, ut-mapp `{{UT_MAPP}}`, port {{PORT}}.

Lead har läst R13 i enskilda skärmbilder vid 1920x930 och 390, i
`{{UT_MAPP}}/shots/lead-r13/w-*.png` och `m-*.png`. Tre fel ska lagas, och ingenting annat
rörs.

1. **Namnen dubbleras i case-rubrikerna.** I dag står "Calyx" stort och direkt under det
   "Calyx fick bli ett vårnummer.". Samma sak gäller "HŌRAI" och "Hōrai dukar upp kvällen…",
   så namnet läses två gånger i rad.
   **Mål:** namnet syns en gång. Meningen är rubriken, och namnet i meningen bär displayrösten.
   För Calyx står "Calyx" i den kursiva displaystilen i stor skala, och resten av meningen
   står i samma `h2` i mindre och lättare vikt. Hōrai får samma grepp med versaler och spärr.
   Copyn ändras inte, ordagrant: "Calyx fick bli ett vårnummer." och "Hōrai dukar upp kvällen
   och ber om bokningen sist." Hela `h2` ska ha ett tillgängligt namn som är hela meningen.
   Rubriken ska rymmas vid 1920, 1440, 1024, 390 och 375.
2. **Pristexten är för liten.** Texten under "Alla har rätt till bra design." ser finstilt ut
   vid 1920, fast det är den text som ska sälja in paketen.
   **Mål:** texten är minst 20 px vid 1440 och 1920, högst cirka 48 tecken per rad, och
   tydligt större än prisradernas beskrivningar. Den korta raden "Första steget är ett samtal
   om vad ni gör." är i samma storlek eller en nivå mindre. Vid 390 är texten minst 17 px.
3. **Kapitelskärmen vid 1920.** Band 01 ("UPPSTART") kikar fram i nederkanten när kapitlet
   står i sitt ensamma läge, se `w-chapter.png`.
   **Mål:** kapitlet står ensamt vid 1920x930 och 1920x1080, precis som vid 1440.

`Skill(design)` först. Använd kirurgiska `Edit`. Verifiera med enskilda skärmbilder, via
`mouse.wheel`, vid 1920x930, 1440 och 390, och läs dem. Kör rubrikskriptet (noll delade ord),
kontrollera noll horisontell scroll och kör `a11y_scan` vid 390 och 1440. Leverans:
`NOTES.md` § V3d R14. Sista raden ska vara `V3d R14 klar`.

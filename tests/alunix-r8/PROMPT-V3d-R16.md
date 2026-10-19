# Alunix, V3d runda 16: tre fynd från Astras slutgranskning. Cell {{KONCEPT}}, ut-mapp `{{UT_MAPP}}`, port {{PORT}}.

Läs `{{UT_MAPP}}/reviews/r15-astra.md`, material_fixes 1–3. Bevisen ligger i
`{{UT_MAPP}}/shots/astra-r15/`. Fix 4 (arkets bredd vid 1920) tas inte i den här rundan, den
ligger hos Anton. Rör ingenting annat.

1. **Hōrais stegrubriker klipps i förhandsvisningen** (`index.html` rad ~2672). Siktet
   `(N-1+.8)/n` hamnar inne i stegets utfönster.
   **Mål:** siktet ligger inom `[a+f, b-f]`, till exempel `Math.min((N-1+.8)/n, N/n-.045)`.
   Stegrubriken ska synas hel i `?preview=case-horai-01..06` och `case-calyx-01..05` vid 1920,
   1440 och 390. Kontrollera också med riktig hjulscroll att rubriken syns i vila.
2. **Case-linjen fäller aldrig ihop på mobil** (rad ~1025). `calc((1 - var(--out)) * 1fr)` är
   ogiltig CSS, så en osynlig rad på 22 px vid 390 och 44 px vid 375 ligger kvar och trycker
   ned texten. Vid 375 hamnar Hōrais text 5–10 px nedanför sektionens underkant.
   **Mål:** raden fäller ihop till 0 px från steg 2 och framåt, till exempel med `max-height`
   styrd av `--out`. Steg 1 vid 375 ska få plats utan att texten går under kanten. All text i
   varje steg ligger inom sektionen vid 390 och 375.
3. **Priset bryts som "26 / 900 kr" vid 390** (rad ~1995). Använd hårt mellanslag i talet och
   före "kr" i pristexten. Om `&nbsp;` behövs i de låsta prisraderna är det en typografisk
   ändring, inte en ändring av copyn.

`Skill(design)` först. Använd kirurgiska `Edit`. Verifiera med enskilda skärmbilder, med
rullningslisterna synliga (`ignore_default_args=['--hide-scrollbars']`), vid 1920x930, 1440,
390 och 375, och läs dem. Kontrollera noll horisontell scroll, kör rubrikskriptet och
`a11y_scan` vid 390. Leverans: `NOTES.md` § V3d R16. Sista raden ska vara `V3d R16 klar`.

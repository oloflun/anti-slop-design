Alunix {{KONCEPT}}, runda 7b (smal regression). Arbetsmapp `{{UT_MAPP}}`, port {{PORT}}. Du gör allt
själv och delegerar ingenting (Antons order, CLAUDE.md § Delegering). Kör bara headless, och varje
webbläsare via `python tests/alunix-r8/browser_lock.py -- …`. Ingen commit. **Aldrig headed**:
vakten stoppade en synlig webbläsare från din runda 7 klockan 04:20. Gör om det skriptet headless.

## Regressionen
R7 rättade granskningens fynd, och `section_probe` är grön. Men klicket på Hōrai har blivit sämre.
`python tests/alunix-r8/click_scroll_probe.py http://127.0.0.1:{{PORT}}/{{UT_MAPP}}/index.html`,
körd fem gånger av leaden: i tre av fem startar scrollen först efter 1,5–2,5 s och är inte framme
efter 2,5 s. I R6b var den framme efter cirka 1,4 s i varje körning.

Leadens diagnos, som du ska bekräfta med CDP-tracing:
- `activateCase` → `mountCase(C)` börjar ladda Hōrai först vid klicket om den inte monterats. Det
  händer när läsaren kommer till väljaren snabbt, till exempel med ett hopp. Hōrais parse, layout
  och avkodning blockerar huvudtråden.
- `glideTo` begränsar varje bildruta till 33 ms av tiden, så scrollen står still under blockeringen.
- R7 tog bort den förvärmning som i R5 flyttade arbetet ut ur klicket.

## Krav
- Hōrai monteras, läggs ut och avkodas **innan** väljaren syns: montering när `#exempelcase` är
  inom 2 viewports, plus avkodning av dess bilder. Ingen layoutläsning i scroll-callbacks; gör
  mätningen i iframens `load` eller i `requestIdleCallback`.
- Om ett klick ändå kommer innan Hōrai är klar: scrollen startar direkt, affischbilden visas, och
  sajten tonas in när den är klar. Ingenting i klicket får vänta på laddningen.
- **Mål:**
  - `click_scroll_probe` fem gånger: framme inom 2,0 s i alla fem, största steg ≤ 60 px, och ingen
    bildruta över 100 ms under de första 2 s.
  - Lägg också till ett scenario i proben: klick inom 300 ms efter att väljaren nåtts. Det ska
    klara samma mål.
- `section_probe.py --baseline {{UT_MAPP}}/shots/final-section-1.json`: fortsatt grön.
- Inga av R7:s rättningar får backas.
- En R7b-sektion i `RAPPORT.md` med tracen och siffrorna före och efter.

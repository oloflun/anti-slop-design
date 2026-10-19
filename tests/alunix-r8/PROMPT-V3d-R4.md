# Alunix, V3d runda 4: Astras andra granskning. Cell {{KONCEPT}}, ut-mapp `{{UT_MAPP}}`, port {{PORT}}.

Astra har granskat R3 i paritetsläget och svarat `fix`: `{{UT_MAPP}}/reviews/r3-astra.md`,
§ fidelity och § material_fixes. Läs rapporten i sin helhet. Par-bilderna och mätskripten
ligger i `{{UT_MAPP}}/shots/astra-r3/`. Lead tar fynden så här:

| Astras fix | Lead | Anmärkning |
|---|---|---|
| 1. Steg 07 står aldrig still, arket släpper vid ungefär 0,90 medan 07 spelar till 0,944. Revisionsfältet ligger över Calyx | **tas** | Steg 07 ska stå färdigt i arket medan dess text läses. Revisionsfältet får inte ligga över bilden |
| 2. Jättens bredd kommer för sent, scrub-värdena mättes före `margin-top:820px`, och `?preview=ledger` visar ett läge som vanlig scroll aldrig når | **tas** | Mät om fönstret mot den faktiska geometrin |
| 3. Kapitelskärmen står inte ensam, band 01 syns redan (P06), och vid 390 är nedre halvan tom | **tas, delvis** | Kapitelskärmen ska stå ensam vid 1440 och fylla sin skärm vid 390. Punkten "åtta mörka skärmar i följd" **stryks**. Anton beställde processakten inverterad, och ingen ljus yta ska stoppas in i akten |
| 4. Mobilarket vid 390: etiketten "96 px" hamnar utanför arket, rutmönstret är 16×16 px, och Calyx täcker bara cirka 56 % av arket i steg 06 | **tas** | Calyx ska fylla minst 80 % av arket i steg 06–07 även vid 390. Det är Antons krav "utan lika mycket luft" |
| 5. Tesrubriken är 38 px mot referensens cirka 80 px | **tas, med villkor** | Rubriken görs större, men **inget ord får brytas** vid någon bredd, 768–1920. Det var R3:s regression. Behöver panelen eller spalten ändras för att ge plats, gör det. Mät med samma skript som i R3 |
| 6. Kortbaksidans ALUNIX är 80,6 px, målet är minst 100 px | **tas** | Kontrollera att ordmärket inte klipps vid någon bredd |
| 7. Hōrai-demon svämmar över vid 390 | **tas inte** | Felet ligger i `sites/horai.html`, som aldrig rörs. Notera det i NOTES |
| 8. Band 07 lämnar glyffragment vid utgången, och de streckade linjerna i steg 05 saknar `--cam-fade` | **tas** | |

## Gör
- Kör `Skill(design)`, `Skill(animate)` och `Skill(emil-design-eng)` först.
- Skriv planen `{{UT_MAPP}}/plans/051-astra-r3.md`.
- Använd kirurgiska `Edit`, aldrig `Write` av hela filen.
- Ingen fix får lösas genom att backa ett djärvt drag, det vill säga genom att göra arket,
  siffrorna, rubrikerna eller Calyx mindre.
- Verifiera varje fix mot Astras "Expected" med skript och med bild.
- Ta nya par-bilder, en skärmbild per sida via `mouse.wheel`, för P02, P03, P04, P06, P10,
  P12, P13 och P16 vid 1440 och 390. Lägg dem i `{{UT_MAPP}}/shots/r4/`.
- Ta hjulscrollssekvenser genom hela processakten vid 1440 och 390, var 150:e px, och läs
  dem. Varje bildruta mellan två band ska vara ren, och varje steg ska ändra arket.
- Kör hela grinden: `scroll_verify`, `motion_probe` med kontrollen först (båda riktningarna),
  `contrast_over_media --url`, `a11y_scan` och `reflow` vid 390 och 768, noll horisontell
  scroll 320–1920, rubrikskriptet (noll delade ord), låst copy 15/15 samt grep för
  tankstreck, `prefers-reduced-motion` och inline-hex.

Samma invarianter som tidigare: F-011, F-014, motorn och `sites/*` rörs inte, ingen tredje
iframe. Leverans: `NOTES.md` § V3d R4 med en tabell över fix, Expected, före och efter, och
par-bild. Sista raden ska vara `V3d R4 klar` eller `[PAUSED — steg X]`.

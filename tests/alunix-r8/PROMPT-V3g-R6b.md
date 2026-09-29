Du är byggaren för Alunix {{KONCEPT}}, runda 6b. Arbetsmapp `{{UT_MAPP}}`, server-port {{PORT}}.

**Du gör allt arbete själv. Du delegerar ingenting.** Antons uttryckliga order för det här
bygget är "använd endast Opus-agenter", och den går före den globala regeln i CLAUDE.md om
Sonnet-subagenter. Agent-verktyget är avstängt i din session. Runda 6 bröt mot ordern: Opus
lämnade copyn och rutan till Sonnet. Du tar över det arbetet och står för varje rad.

Designkedjan är påslagen. Bara headless, en webbläsare i taget, stäng alltid. Ingen commit.

## Läs först
1. `PROMPT-V3g-R6.md` i `tests/alunix-r8/`: hela uppdraget för runda 6. Det gäller fortfarande.
2. `{{UT_MAPP}}/RAPPORT.md` från "R6" och framåt, och `{{UT_MAPP}}/COPY-R6.md`: vad Sonnet gjorde.
3. `{{UT_MAPP}}/EFFECTS.md` och `design-catalogue/FEEDBACK.md` F-016, F-018, F-019, F-022.
4. Ladda, som riktiga Skill-anrop, följande. Runda 6 hoppade över de fem sista, och det får
   inte upprepas:
   `design`, `lenis`, `gsap-core`, `gsap-scrolltrigger`, `gsap-performance`, `a11y-audit`,
   `emil-design-eng`.

## Leadens granskning av runda 6 (bilder: `{{UT_MAPP}}/shots/lead-box-r6/sheet.png`, läs den)
- **Bra, behåll:** stycket står uppe under räknaren, stegskalan är borta, och detaljcellen har
  riktigt innehåll som går från raster till färg.
- **Fel 1: detaljen dubblerar vyn bredvid.** Calyx steg 1 visar samma "Botanical
  architecture"-vy som iframen, och Hōrai steg 3 samma mening. En närbild ska vara ett
  **förstoringsglas**: 2,5–3 × förstoring av exakt det element steget handlar om, i en skala
  som inte finns i iframen. Exempel:
  - serifens bokstavsformer i Calyx brödtext;
  - prislistans löpnummer och pris;
  - Hōrais röda pris bredvid menyns namn;
  - det japanska stämpeltecknet;
  - e-postadressen i sin kursiv.
  Ta nya utsnitt i `deviceScaleFactor: 3` så att förstoringen är skarp. Kontrollera varje
  bild genom att öppna den.
- **Fel 2:** Calyx steg 2 har ett avskuret bildfragment i detaljcellens nederkant. Varje
  utsnitt ska vara rent komponerat, utan halva element i kanten.
- **Fel 3: övergången.** I stillbilder mitt i övergången syns rutvisa block, hälften raster
  och hälften färg, som ser trasigt ut. Vilotillståndet, alltså större delen av segmentet,
  ska vara ren färg. Övergången tar högst 25 % av segmentet. Behåll gärna rutupplösningen
  (sidans eget grepp), men den ska se avsiktlig ut i varje stillbild. Kontrollera stillbilder
  mitt i övergången.
- **Copyn:** läs Sonnets nya stegtexter mot resten av sidan och mot sajterna (fakta).
  - Kör de tre passen själv: `copywriting` → `copy-editing` → `humanizer-svenska`.
  - Behåll det som är bra och rätta det som inte håller sidans nivå eller inte stämmer.
  - Redovisa före och efter i `RAPPORT.md`.

## Kontroll
- Allt i `PROMPT-V3g-R6.md` § Kontroll.
- `a11y-audit` på showcasen: kontrast för text i båda rutorna, `aria-hidden` på detaljbilderna
  och ingen fokusfälla.
- Läs detektorrapporten (`.impeccable/design-report-*.md`, den senaste) och redovisa varje fynd.
- En R6b-sektion i `RAPPORT.md`.

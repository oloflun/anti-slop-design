Du är byggaren för Alunix {{KONCEPT}}, runda 7 (rättningar efter Opus-granskningen). Arbetsmapp
`{{UT_MAPP}}`, server-port {{PORT}}.

**Du gör allt arbete själv och delegerar ingenting.** Det är Antons order för det här bygget, och
reglerna i CLAUDE.md § Delegering gäller: ingen lägre modellklass. Agent-verktyget är avstängt.
Designkedjan är påslagen. Bara headless, en webbläsare i taget: varje kommando som startar en
webbläsare körs genom `python tests/alunix-r8/browser_lock.py -- …`, och webbläsaren stängs alltid.
Ingen commit.

## Läs först
1. `{{UT_MAPP}}/AUDIT.md`: den sammanställda granskningen. Din lista är **HIGH H1–H15** och
   **MEDIUM**. Förslagen under "kräver Antons beslut" rörs inte.
2. `{{UT_MAPP}}/reviews/opus-*.md`: granskarnas detaljer, med rader, mätvärden och föreslagna mål.
3. `{{UT_MAPP}}/EFFECTS.md` och `design-catalogue/FEEDBACK.md`: skyddade effekter och Antons domar.
   Inget skyddat får bli sämre. Varje rättning bevarar effekten och ändrar bara det felaktiga.
4. Skills, som riktiga anrop: `design`, `lenis`, `gsap-scrolltrigger`, `gsap-performance`,
   `a11y-audit`, `emil-design-eng`. För copy (H3) kör du `copywriting` → `copy-editing` →
   `humanizer-svenska`.

## Riktlinjer för de knepiga fynden
- **H1 iframen:** skala sajten efter **cellens bredd**, inte höjden, så att hela 1440-bredden syns.
  Iframens höjd blir då cellens höjd delad med skalan.
  - Klientsajterna använder `vh`, så en högre virtuell viewport gör deras sektioner högre. Det är
    acceptabelt.
  - Mät om ankarna efteråt. `measureCase` måste köras efter storleksändringen.
  - Mobil: rendera sajten i 390 bredd i ramen, alltså sajtens egen mobillayout, skalad 1:1 eller
    till ramen.
  - Kontrollera i pixlar att citat och priser syns hela.
- **H2 och hero-bandet:** tes- och hero-pinnen startar på `'top top+=48'` med scen-höjd
  `calc(100svh - 48px)`, som showcasen redan gör. Kortvändningen och tesens resning ska se
  likadana ut som nu, bara oklippta. Jämför före- och efterbilder.
- **H6:** stegen döljs bara med opacity, inte med `aria-hidden` eller `visibility`. Övertoningen
  ska se exakt likadan ut.
- **H7:** den iframe som ligger vid opacity 0 får `inert` och `aria-hidden`. Båda ramarna blir
  `inert` förhandsvisningar, eftersom sajten ska ses och inte användas i ramen. Lägg en länk
  "Öppna Calyx i full storlek" / "Öppna Hōrai i full storlek" (≥ 24 px) till `/sites/*.html`.
  - Länktexten är ny copy och kör samma tre pass.
  - Lägg den i `verify.py`:s lista över tillåtna nya strängar.
- **H5:** båda "Boka ett möte" blir
  `mailto:kontakt@alunix.se?subject=Boka%20ett%20m%C3%B6te`. Kortets länkar ska vara ≥ 44 px
  höga. Ett tryck utanför en länk på baksidan får inte vända tillbaka kortet.
- **H11:** `will-change` bara under själva upplösningen (sätt före, ta bort efter), aldrig
  permanent.
- **H12 och H13:**
  - Calyx-iframen monteras lat, som Hōrai: `mountDue` inom 2 viewports från `#exempelcase`.
  - Ingen `refresh` under laddning som flyttar layout. Om de tre refresharna vid laddning behövs,
    reservera höjderna i CSS så att de inte orsakar CLS.
  - Mål: CLS ≤ 0,05 och sidvikt ≤ 2,5 MB utan att någon ram har laddats.
- **Fallbilder:** koda om till 1680 px bredd, WebP kvalitet 82. Kontrollera skärpan genom att öppna
  dem.

## Kontroll, var och en med mått, före och efter, i `RAPPORT.md` (R7-sektion)
- Varje H-fynd: granskarens mått före, ditt mått efter, bildväg när det gäller något visuellt.
- `section_probe.py --baseline {{UT_MAPP}}/shots/final-section-1.json` två gånger: grönt, och ingen
  sektion sämre.
- `click_scroll_probe.py` två gånger: största steg ≤ 60 px.
- Skillens `perf_probe.py`: CLS, LCP och sidvikt.
- `a11y-audit`-skripten, med kontrollsidan först: axe utan `aria-prohibited-attr`, och 0 tabbstopp
  i dolda ramar.
- `verify.py`: 0 px överflöd på alla bredder, och copy-diffen oförändrad utom de tillåtna
  strängarna.
- Skärmbilder av showcasen (båda casen, tre steg), tesens pin, heron-pinnen och kontaktkortet,
  vid 1440 och 390. Läs varje bild.

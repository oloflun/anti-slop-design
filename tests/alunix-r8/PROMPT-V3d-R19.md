# Alunix, V3d runda 19: övergången blått → ritning på riktigt, och tre fynd från Astra. Cell {{KONCEPT}}, ut-mapp `{{UT_MAPP}}`, port {{PORT}}.

Läs `{{UT_MAPP}}/reviews/r18-astra.md`. Svaret är `fix`, med fyra material_fixes. Bevisen
ligger i `{{UT_MAPP}}/shots/astra-r18/`. Astras dom är att övergången blått → ritning är
**för återhållsam**. Den har fyra tunna linjer med kontrasten 2,86:1 på det blå, skarven är
fortfarande en rak kant, och landningslinjen ritas som en 1×1 px-punkt. Anton sa redan att den
var "extremt platt" och vill ha en fin övergång med en scrolleffekt.

## 1. Övergången, ny form: det blå arket blir ritningens ark
Skriv den som `{{UT_MAPP}}/plans/062-blakopian-arket.md` innan du bygger.
- **Idén:** när tesbandet lämnar krymper det blå planet, scrubbat på `--sc-ps` i båda
  riktningarna, från helbredd till **exakt ritningsarkets rektangel** i processens steg 01.
  Använd `clip-path: inset(...)` eller en transform på en inre yta, inte layout.
- Under krympningen tonas den blå fyllnaden till ritbordets ton, och en vit kontur på 1,5 till
  2 px tonas in längs kanten. Det som landar är arkets kontur, samma ark som sedan ritas i
  steg 01–07. Tesen blir alltså ritningen i ett drag.
- Blåkopians konstruktionslinjer får stå kvar som andra lager, men i minst 2 px på arkets
  kanter och landningslinjen, med minst 3:1 mot det blå. Landningslinjen ska verkligen synas:
  rätta specificiteten `.seam i` mot `.seam-h`, som Astras fynd 1 beskriver.
- Tesmeningen och Hyperborea-bilden får inte sträckas eller klippas mitt i en rad. De tonas ut
  före krympningen, eller följer med planet och försvinner in i det, beroende på vad som läses
  renast.
- Kapitelrubriken "Från samtal till lanserad sida." kommer först när arket har landat. Ingen
  rubrik halvklipps i något scrolläge. Kontrollera med `elementFromPoint` och den geometriska
  kontrollen från R18, och kör båda först mot en medvetet trasig version.
- Gäller vid 1024 och uppåt. Vid 768 och 390 krymper planet till mobilarkets rektangel på
  samma sätt, eller så används en förenklad variant som du motiverar.
- F-011 och F-014 gäller, och minst två koordinerade lager. `motion_probe` med kontrollen
  först, båda riktningarna: staircase 0 och max_step ≤ 3 %.

## 2. Astras övriga fynd
- **Fynd 3:** ladda Hōrai-ramen medan Calyx står i steg 1–3, så att övergången Calyx → Hōrai
  aldrig stannar. **Mål:** inga uppgifter över 50 ms i det fönstret. Mät vid 1440, 1920 och
  390.
- **Fynd 4:** skriv "SEO‑optimering" med ett icke-brytande bindestreck (`&#8209;`) i
  prislistan. Ordvalet ändras inte.

## Gör och verifiera
- Kör `Skill(design)`, `Skill(animate)` och `Skill(emil-design-eng)` först.
- Använd kirurgiska `Edit`. Motorn och `sites/*` rörs aldrig. Antalet inline-hex får inte öka.
- Starta Chromium med `ignore_default_args=['--hide-scrollbars']`. Döm bara i enskilda
  skärmbilder.
- Ta en hjulsekvens i 20 px-steg genom övergången vid 1920x930, 1440, 768 och 390, åt båda
  hållen. Lägg den i `{{UT_MAPP}}/shots/r19/` och läs den. Lägg också fem förhandsvisningslägen
  som `?preview=tes-till-ritning-0..4`.
- Pixeldiffa resten av sidan mot R18. Ingen oavsiktlig ändring får finnas.
- Kör `perf_probe`, `microtext_scan.py`, rubrikskriptet och `a11y_scan` vid 390 och 1440, och
  kontrollera noll horisontell scroll.

Leverans: `NOTES.md` § V3d R19. Sista raden ska vara `V3d R19 klar` eller `[PAUSED — steg X]`.

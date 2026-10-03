# V3g · R10 · materiella övergångar och nästa runda enligt auditen

Koncept {{KONCEPT}}, arbetsmapp `{{UT_MAPP}}`, port {{PORT}}.

**Modell:** Opus. Starta inga subagenter, gör hela uppdraget själv (`~/CLAUDE.md` § Delegering).
**Webbläsare:** bara headless, en i taget, via `tests/alunix-r8/browser_lock.py` (vänta på låset,
ta det aldrig från någon annan). Server: `python skills/design/scripts/serve.py --port {{PORT}}
--root .` från repo-roten (kör redan om porten svarar).
**Push:** aldrig. Commit: nej, leaden committar.

## Beställningen

Anton, 2026-10-03, ordagrant: "Kör nästa runda enligt § 4, jag godkänner planen."

Planen är `AUDIT-ALUNIX-R9.md` § 4 (repo-roten). Läs hela filen först. § 2 visar var sidan står
mot golvet. Backup före första ändringen: `cp {{UT_MAPP}}/index.html {{UT_MAPP}}/index.before-r10.html`.

## Kedjan, utan genvägar

Ladda Skill(design) och gå igenom Step 0–2b som vanligt. Referensgolvet i `design-gate`
spärrar första UI-skrivningen tills allt är läst. Sedan 2026-10-03 hör följande till golvet
(SKILL.md 2b.4):
- `references/scroll/showcase-floor.md`
- `references/scroll/journeys/era-residence.md` (läs § 2b)
- två rörelseark med `motion_floor: 2` (`design-catalogue/entries/<slug>/motion/sheet.webp`,
  som bild)
- Skill(lenis), Skill(gsap-core), Skill(gsap-scrolltrigger), plus gsap-timeline och
  gsap-plugins (sidan använder SplitText).

Välj arken efter övergångarna du ska bygga. Kandidater med just de orsakerna:
`collabcapitolium`, `era-residence`, `forgeautomotive-co`, `filmbot`, `huehaus`. Kontrollera
`motion_floor` i deras `entry.md`. I beslutsloggen (`{{UT_MAPP}}/R10-BESLUT.md`) ska du namnge
vad du tar från vart och ett.

Copy: varje ny eller ändrad sträng går genom Skill(copywriting) och sedan
Skill(humanizer-svenska). Fakta finns bara i `tests/alunix-r8/PRODUCT.md`. Inga påståenden
om kunder, resultat eller svarstider.

## Skyddat (får inte bli sämre)

`{{UT_MAPP}}/EFFECTS.md`, hela tabellen:
- tesens överlämning A → B i en pinnad svart cell (R9);
- heron och kortet (en ägare per egenskap, R9 § 1);
- showcase-mekanismen (en pin, skapad en gång; övertoning; räknare och mintspår);
- kontaktkortet som vänder sig självt vid 0,7.

Allt rörelse körs med `scrub: true`, Lenis är det enda utjämningslagret, och `lerp .075` och
`wheelMultiplier .6` ligger kvar.

## Vad som byggs (AUDIT § 4, punkt för punkt)

1. **Regel 2, tre materiella sektionsbyten.** Var och en drivs av sidans eget material och
   är scrubbad i båda riktningar. Ingen övergång får vara samma som den föregående.
   - **process → showcase:** processfotot (cellen med skrivbordet) växer ur sin ram till den
     fulla Calyx-ramen (kort → helbild, som Forge och Filmbot). Showcasens iframe får aldrig
     transformeras: väx en bildyta eller en clip-path fram till ramens mått, och låt sedan
     den levande ramen ta över utan synlig skarv. Läs PRODUCT.md § Operating Context: en ram
     som visats får aldrig transformeras eller tonas efteråt.
   - **showcase → pris:** mintspåret i showcasen fyller sin yta och blir prisbentons mintruta
     (samma färgfält, ett grepp, som Eras skål som blir nästa sektions mark).
   - **pris → kontakt:** mintrutan krymper till kontaktkortets skugga, så att kortet lämnas ut
     ur pris.
   - Rytmbanden mellan grupperna tas bort där en övergång ersätter dem.
2. **Regel 5, typ och media i samma ram.** En bild i luckan i processrubriken "Från samtal
   till lanserad sida.", som rör sig i läsfart och står still medan rubriken läses (≥ 40 vh).
3. **Sektionsnavigering.** Tre eller fyra textankare i topplinjen (process, exempel, paket,
   kontakt). De ska fungera med Lenis (`anchors: true`, `lenis.scrollTo`) och med tangentbord.
   Mobil: inget hamburgermeny-ornament, bara ankarna om de ryms, annars utelämnas de.
4. **Byt case inne i showcasen.** Calyx/Hōrai-valet ska nås medan showcasen är pinnad, utan
   att man scrollar ~115 steg. Pinnen skapas fortfarande en gång och dödas aldrig, och casebytet
   tonar över (skyddat).
5. **Kostnadsfrågan.** Raden "Vi lämnar pris efter första samtalet." placeras i pris, i
   ingressens skala, under prisrubriken eller i bentons foot. Den är godkänd i planen.
6. **Erbjudandet i första skärmen.** En kort rad som säger vad Alunix gör, hämtad ur
   PRODUCT.md (`Webbdesign, design och system. Allt på ett ställe.` finns där ordagrant). Den
   får inte krocka med kortet eller sömmarna och får inte tvinga fram en mono-kicker.
7. **"Boka ett möte" är en mailto-länk.** Etiketten ska säga vad som händer: "Mejla oss" eller
   "Mejla oss om ett möte". Gäller herokortet och kontaktkortet.
8. **Kontakten: vad som händer sedan.** En rad i ingressens skala, utan tidslöfte, t.ex. "Vi
   svarar med ett förslag på tid för ett första samtal."
9. **"Vår process:"-kickern bort** (F-016).
10. **a11y (granskarens kvarvarande punkter):**
    - M1 showcase: `.showcase-stage.is-far{visibility:hidden}` döljer Calyx-rubrikerna i
      tillgänglighetsträdet. Ersätt med `content-visibility:auto` eller opacity, men bara om
      section_probe fortfarande visar en iframe-laddning och 0 refresh. Annars behålls
      dagens lösning och skälet skrivs i beslutsloggen.
    - L2: case-knapparnas fokusring ska vara svart med vit halo, ≥ 3:1 mot Hōrais foto.

## Mät innan du säger klart

Kör allt headless genom låset och läs varje bild själv:
- `python skills/design/scripts/section_probe.py http://127.0.0.1:{{PORT}}/tests/alunix-r8/runs/V3g/index.html --baseline {{UT_MAPP}}/shots/section-probe-r9.json --out {{UT_MAPP}}/shots/section-probe-r10.json`
  (baslinjen är R9-siffrorna: kopiera `C:\Users\ANTONL~1\AppData\Local\Temp\claude\C--Users-Anton-L-anti-slop-design\b0a224e3-0c02-4e0d-8ab0-29e97b39941e\scratchpad\sp5.json` dit först om filen saknas). Kravet är 0 fel, en iframe-laddning och 0 refresh.
- Hjulvandring 1440×900, 768×1024 och 390×844. Varje övergång ska synas i minst två bildrutor
  i båda riktningar.
- Sidans eget rörelseark: `MOTION_FRAMES=40 python scripts/catalogue/motion_capture.py --url
  http://127.0.0.1:{{PORT}}/tests/alunix-r8/runs/V3g/index.html --slug alunix-v3g-r10-self
  --redo`. Lägg det bredvid dina två floor-2-ark och gå regel för regel genom golvets § 2 i
  `R10-BESLUT.md`.
- `python skills/design/scripts/microtext_scan.py --names sites/calyx.html sites/horai.html`:
  0 träffar.
- Hero efter tur och retur: scrolla ned förbi heron och upp igen. clipPath ska vara `inset(0%)`
  och h1-raderna hela.

Avslutningsvis skriver du `{{UT_MAPP}}/R10-RAPPORT.md`. För varje punkt 1–10: vad som byggdes,
mätvärdet, och den bild som visar det. Rapporten tar också upp vad som inte gick och varför.

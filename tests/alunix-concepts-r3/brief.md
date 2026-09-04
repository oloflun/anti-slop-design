# Brief r3 — R5 + R6 kombinerade till EN sida (2026-09-04, Antons beställning)

Anton har valt en kombination: R5 (Mattis/Geist, `../alunix-concepts-r2/cells/R5-chain/index.html`)
som VÄNSTER spalt och R6 (Creative Giants/Public Sans, `../alunix-concepts-r2/cells/R6-chain/index.html`)
som HÖGER spalt, sida vid sida, **exakt som i `reference-mosaic.png`** (vänster = R5, höger = R6),
inklusive höjdskillnaderna mellan spalternas sektioner. Varje spalt är sin källsidas 1440-px-layout
i halv skala (spalten är 50 % av viewporten): behåll proportionerna mellan typ, luft och bild.

## Bindande ändringar mot källorna

1. **Rubriker oförändrade, samma typsnitt** (Geist 700 vänster, Public Sans 300 höger). Ordagrant:
   - V: `ALUNIX` + `Digital byrå`, `DET FÖRSTA INTRYCKET ÄR DIGITALT.`, `DESIGN` / `UTVECKLING` / `SYSTEM` (01–03)
   - V: `VI BYGGER WEBBPLATSER.` → **`VI BYGGER ERT VARUMÄRKE.`** (enda rubrikbytet)
   - H: `ALUNIX` (affischordmärket), `Er webbplats är nutidens visitkort.`, `Webbdesign, design och
     system. Allt på ett ställe.`, `Webbdesign` / `Design` / `System`, `Tre sajter, i drift.`,
     `Alla har rätt till bra design.`
2. **Undertexterna skrivs om** så att inget upprepas mellan spalterna (i dag återkommer "skräddarsydda",
   "exponerar ert företag", "nutidens visitkort", "allt på ett ställe" på båda sidor). Samma byråröst
   som r2 (`../alunix-concepts-r2/brief.md`: vi-form, Insigns nivå, inga enmans-formuleringar).
   Kör copy-kedjan på undertexterna: `Skill(copywriting)` → `copy-gate.md` Pass 1b → `Skill(humanizer-svenska)`.
3. **Hōrai interaktiv i den svarta rutan** (höger spalt, sektionen `Tre sajter, i drift.` under
   tjänsterna): rubriken kvar, de tre projektraderna ersätts av en **kantlös** `<iframe
   src="/sites/horai.html">` (ingen border, ingen radie, ingen skugga, kant till kant i spalten), en
   kort rad ovanför som säger vad det är (Hōrai, restaurang i Stockholm) och att sajten går att
   använda direkt.
4. **Calyx interaktiv i vänster spalt** där projektminiatyrerna börjar (efter ledger-raden 03 System):
   kickern `Utvalda projekt` kvar, tre-kortsgriden ersätts av en kantlös `<iframe src="/sites/calyx.html">`,
   kant till kant. Filosofi- och kontaktblocket i vänster spalt utgår (filosofin och kontakten bor nu i
   prisrutan till höger). Hyperborea-fotot i det blå blocket stannar (tredje sajten).
5. **Prisrutan** = höger spalts sista sektion (`Alla har rätt till bra design.`), **inverterad**: mörk
   grund (#0c0b08) och off-white text i R6:s typografi. Innehåll, som egna fetstilsrader (copy-gate:
   diskreta fakta får egna rader):
   - Standardhemsida, sex sidor: **10 990 kr**
   - Med bokningssystem: **15 990 kr**
   - Helt skräddarsydda lösningar för produktkataloger, specialbyggda system med mera: **pris vid förfrågan**
   - Kontakt: **kontakt@alunix.se** (mailto)
   Ingen "exkl. moms"/"inkl. moms" (vet vi inte). Filosofimeningen får stå som ingress under rubriken.
   Kolofonen (hej@alunix.se) utgår; **all kontakt på sidan är kontakt@alunix.se** (även hero-CTA:n).
6. **Sidan slutar där Calyx slutar.** Båda spalterna har samma bottenkant: vänster spalt slutar med
   Calyx-ramen, höger spalt slutar med prisrutan, kapad/sträckt så att den slutar på samma y.
   (Lösning: två spalter som flex-kolumner med lika höjd; Calyx-ramen respektive prisrutan är `flex:1`;
   Calyx min-höjd ≈ 100vh, Hōrai ≈ 90vh.)
7. **Loggan** (`build/assets/logo-white.svg`, inline-SVG, fyll vit) placeras i mitten där de fyra
   översta rutorna möts: horisontellt centrerad på skarven mellan spalterna, vertikalt mitt emellan
   vänster heros nederkant och höger ordmärkes nederkant (mät i JS vid load/resize, eller lös det i
   CSS). Höjd ≈ clamp(88px, 9vw, 150px). Vit mot mörk hero (vänster) och foto (höger); en mjuk
   radiell scrim bakom får läggas till om kontrasten mäts under 4.5:1 (`contrast_over_media.py`).
8. **Ingen fast nav** över sidan (R6:s fixed nav utgår; R5:s fasta hörnmarkeringar får vara kvar som
   sidsignatur). Under 900 px staplas spalterna (vänster, sedan höger); ramarna 70vh.

## Scroll-koreografi (Antons ord: "imponerande scroll-effekter över hela sidan, som passar in i layouten
## och ger en premiumkänsla", inspiration från liknande sidor i katalogen)

- Grammatik: **split stage** (två sidor av samma argument, skarven är chromet). Läs
  `~/.agents/skills/design/references/scroll/{grammars,devices,feel-and-fingerprint}.md` och
  `references/motion.md`. Motorn `~/.agents/skills/design/scripts/scroll/{scrollcraft.js,scrollcraft.css}`
  kopieras in oförändrad (tema via de sex tokens), bespoke rörelse läser `--sc-p`/egna attribut.
- Katalogposter att läsa för signature moves i scroll: `design-catalogue/entries/{vintergatan,vinterspelen,
  rre-ventures,veloura,mattis-studio,creative-giants,shelby-kay}/entry.md` (avsnitten Signature move + Motion)
  och `design-catalogue/TASTE.md` §4 (rörelse bär aldrig auktoriteten ensam).
- Krav: känslokurva per akt skriven FÖRE byggandet (NOTES.md), en topp, ett tell-someone-test, ≥4
  device-familjer, aldrig samma två i rad, en **signature move** som bara finns här. Mitt förslag (får
  förbättras, inte bytas mot en kit-parameter): skarven mellan spalterna är en hårlinje som **ritar sig
  själv nedåt från loggan i takt med scrollen** (stroke-dashoffset/height från scrollposition), loggan
  sätter sig (docks) när linjen börjat; högerspaltens ordmärke driver långsammare än scrollen
  (parallax i hundratals px), fotot får en parallax i motsatt riktning, det blå blocket kommer in som
  en `reveal` (wipe från vänster), `VI BYGGER ERT VARUMÄRKE.` är kinetic (lines), ledgerraderna `in`
  med stagger, Hōrai-ramen öppnar sig med `iris` (en gång per sida), prisrutan landar stilla (avslutet
  ska vila, inte tona ut).
- Förbjudet: transform/opacity på själva iframe-elementen efter att de öppnats (de ska vara
  interaktiva), pin på hela sidan (Anton vill se layouten som den är), dead scroll, marquee,
  räknare (inga tal utöver priserna, som är statisk text), pointer-effekter på ramarna.
- Reduced motion: allt synligt, inga resor; loggan och skarven statiska.

## Förbjudet (oförändrat från r2)

Inga påhittade tal utöver Antons priser, inga kunder utöver de tre demona, aldrig Klova, inga
tankstreck i synlig text, inga "jag", inga foton som läses som "vårt kontor/team".

## Verifiering (agenten kör, jag läser pixlarna)

`shoot.py` (desktop 1440 helsida + fold, mobil 390), `scroll_verify.py`, `a11y_scan.py`, konsolen utan
`[scrollcraft]`-varningar, båda ramarna laddade (dokumentet i ramen har `<title>`), inget horisontellt
överflöde, `contrast_over_media.py` för loggan. Servern: `python -m http.server 3091` från repo-roten
(ramarna använder absoluta `/sites/...`-sökvägar som också gäller på Vercel).

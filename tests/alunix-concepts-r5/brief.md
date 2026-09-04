# Brief r5 — M1 vidare i tre varianter (2026-09-04, Antons beställning)

Anton valde **M1** (`../alunix-concepts-r4/cells/M1-chain/index.html`, kontinuerlig grund, förskjutna
spalter) som klar vinnare. Nu tre varianter av M1 som skiljer sig på tre axlar: **hero-bilden**,
**Hyperborea-figuren i det blå blocket** och **scrollanimationerna för resten av sidan**. Allt annat
gemensamt. Jag (orkestratorn) läser allt med egna ögon.

## Gemensamt för alla tre (bindande)

1. **Heron är en bild, inte Tidvatten-ramen.** Fullbredd som i M1, med rubriken `Er hemsida är
   nutidens visitkort` och underraden `Vi skapar skräddarsydda webbplatser som hjälper er att
   exponera verksamheten.` (ordagrant) lagda på bilden. Foto ur poolen `/tests/alunix-concepts/_assets/`
   (k4-cabin-desk.webp, k1-stage-beams.webp, k1-stage-pool.webp; k4-desk-overhead är avvisad som
   stockig). Presentationen skiljer per variant (contract.md). Loggan ligger kvar i heron.
2. **Ingen tom lucka under heron.** Högerspaltens 50vh-förskjutning ersätts av blocket
   `VI BYGGER ERT VARUMÄRKE.` med sin underrad och ledgern 01–03 (Design/Utveckling/System), som
   börjar direkt under hero-bilden och fyller ytan ned till tjänsterna. Högerspalt uppifrån:
   **jätterubrik + ledger → `Webbdesign, design och system. Allt på ett ställe.` + tjänster 01–03 →
   Hōrai-ramen → prisrutan.** Vänsterspalt: **konsolkortet → blått tesblock → Calyx-ramen** (V2 även
   Hyperborea-ramen). Grunden (gråskalefotot) syns fortfarande i spaltmellanrum och luckor, men inga
   luckor högre än 8vh mellan två paneler i samma spalt.
3. **Exempelsidorna benämns** med kicker + rad: `Exempelsida: Calyx, florist i Stockholm`,
   `Exempelsida: Hōrai, Asian fusion-koncept`, `Exempelsida: Hyperborea, konferens i Lund`. Inget
   "byggd av Alunix", inget "En sajt vi byggt, öppen att utforska här" (underförstått).
4. **Prislistan** (Antons nya paket; raderna som egna fetstilsrader, copy-gate-regeln):
   - `Standardpaket. Webbplats med CMS för egna ändringar och en första SEO-optimering.` → **26 900 kr**
   - `Paket med bokningssystem, betalning och kunddatabas.` → **38 900 kr**
   - `Helt skräddarsydda lösningar för produktkataloger, specialbyggda system med mera` → **Pris vid förfrågan**
   Rubriken `Alla har rätt till bra design.`, ingressen och `kontakt@alunix.se` oförändrade.
5. **Copyn i övrigt ordagrann** ur M1 (rubriker, undertexter). Ingen ny copy utöver raderna ovan.
6. **Tre ramar interaktiva** (Calyx, Hōrai, i V2 Hyperborea), aldrig transformerade när de är öppna.
   Ramar: `/sites/calyx.html`, `/sites/horai.html`, `/sites/hyperborea.html`. Bilder:
   `/tests/alunix-concepts-r3/build/assets/` (demo-hyperborea.webp m.fl.) och `/tests/alunix-concepts/_assets/`.
7. **Scrollanimationer över hela sidan**, inte bara ramarna och den statiska grunden: ≥ 4
   device-familjer, en signature move per variant, text och bild i olika riktningar minst i en akt,
   inga tomband, reduced motion statisk. Motorn oförändrad.
8. Förbjudet: påhittade tal utöver priserna, kunder utöver de tre demona, Klova, tankstreck i synlig
   text, "jag", foton som "vårt kontor/team", pointer-effekter på ramarna.

## Verifiering (agenten kör; jag läser pixlarna)

`shoot.py` (1440 fold + full efter skriptad genomscroll, mobil 390), `scroll_verify.py`, `a11y_scan.py`,
inget horisontellt överflöde, ramar laddade med titel, konsol ren, `shots/motion-0..4.png` genom den
akt där text och bild går åt olika håll, plus en JS-mätning av alla luckor mellan paneler per spalt
(max 8vh). Server: `python -m http.server 3091` från repo-roten.

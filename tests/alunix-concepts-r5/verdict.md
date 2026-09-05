# Verdict r5 — M1 vidare i tre varianter (2026-09-04)

Anton valde M1 (r4) och gav sex ändringar: hero-bild i stället för Tidvatten (alternativ ur katalogen),
luckan under heron fylld av "Vi bygger ert varumärke" med Calyx flyttad upp under det blå blocket,
olika lösningar på Hyperborea-figuren, scrollanimationer över hela sidan, "Exempelsida:"-etiketter
utan "byggd av Alunix", och den nya prislistan (26 900 / 38 900 / pris vid förfrågan).
Board: http://127.0.0.1:4623/board.html (tangent 1–3). Cellerna: `cells/V1..V3-chain/index.html`.
Boarden serverar nu repo-roten som fallback, så ramar och bilder laddar (rättat i `board.py`).

## Tre varianter

| V | hero | Hyperborea i blått | scroll för resten | signature move | källor |
|---|---|---|---|---|---|
| V1 Dokumentär band | cream-panel 38 % + skrivbordsfoto i färg 62 % | fullbreddsremsa 16:6 under texten | wipes växelvis per panel, kinetiska rader, stagger, grund-drift | panelen glider till 55 % över fotot i takt med scrollen | insign, creative-giants, rre-ventures |
| V2 Cinematisk tvätt | ljusstrålar under svart tvätt, rubrik centrerad | ingen figur; Hyperborea som tredje ram under Calyx | hero sjunker/rubrik stiger, pinnat tesblock (span 1,3), parallax, drift | tvätten lättar 0,72 → 0,2 när man lämnar heron | planhat, mattis-studio, veloura |
| V3 Plåt i grunden | inramad ljuspöl med rubrik utanför bilden i affischskala | plåt som bleeder 11 % ut över blockets kant | ordscrubb i ledgern med tråd, iris på Hōrai, rubrikskala 0,92 → 1, drift | ljuspölen vandrar (object-position från scrollen) | vintergatan, mattis-studio, garden-eight |

Unsplash blockerades i webbläsarpanelen den här gången, så heron fick varianter ur den redan hämtade
poolen (skrivbordet i färg, ljusstrålarna, ljuspölen; skrivbordet uppifrån avvisat som stockigt).

## Min pixelläsning, per variant

**V1.** Första bygget: loggan ett svart klotter (vit + difference-blend mot cream, klippt), panelens
växt gav en hel tom cream-viewport, vänsterspalten slutade en skärm före högerspalten. Efter fixen:
loggan i bläck i panelen, växten stannar vid 55 % med minst 45 % foto synligt i varje steg, spalterna
slutar på samma pixel. Ren.

**V2.** Första bygget: det pinnade blå blocket centrerade texten och gav tomma blå skärmar; högerspalten
slutade en viewport före vänsterspalten. Efter fixen: texten hälsar överst, span 1,3, som mest 43 %
tom blå yta i något steg; spalterna slutar jämnt. Ren.

**V3.** Första bygget: hero-plåten laddade inte alls (den råa poolfilen resettas av dev-servern;
omkodad kopia i den serverade mappen), vänsterspalten slutade för tidigt, loggan renderades som ett
klotter på plåtens kant. Efter två fixar: bilden laddar, ljuspölen vandrar, spalterna slutar jämnt,
loggan ≥ 72 px med mätt kontrast.

## Gemensamt verifierat (alla tre)

scroll_verify rent, a11y 0 fel, inget dokumentöverflöde vid 1440/390, alla ramar med titel och utan
transform, konsol utan motorvarningar, panel-till-panel-luckor ≤ 3,3vh (kravet 8vh), spalterna slutar
inom 0 px av varandra, rörelsebevis `shots/motion-0..4.png` per cell. Copyn är M1:s ordagrant utom
etiketterna och prisraderna (Antons ord; ingen copy-kedja kördes på dem, de är produktfakta).

## Rangordning på pixlar

V1, V2, V3. V1 är den som ser mest ut som en byråsida och minst som en effekt; V2 har den starkaste
öppningen men det pinnade blocket kostar scroll; V3:s plåt och ordscrubb är de mest egna dragen men
heron är tystast. Alla tre är utan tomband nu, vilket var den här rundans egentliga krav.

## V3 vald → V3b (2026-09-05)

Anton valde V3 och bad om två rättningar plus min egen granskning. Gjort:

- **Hōrai-källan** (`sites/horai.html`): navloggan döljs medan heron syns (IntersectionObserver) och
  återkommer med den mörka bannern; öppettidsstycket i full cream med textskugga; bannern hade
  ingen bakgrund alls eftersom Tailwinds play-CDN inte genererade `bg-walnut/92` vid körning, en
  statisk regel löser det.
- **Etikettrutorna** över Calyx och Hōrai borttagna; Hyperboreas bildtext kvar i det blå blocket.
- **Min granskning** (pixlar vid 1280/1440/1920) + kritikeragenten (design-critic), bekräftade fynd:
  hero-plåten tog 95 % av viewporten (nu 56vh, rubrik + plåt + underrad i en fold), toppraden och
  plåten delade inte kant (gemensam `--rail-x`), det blå blockets text kläms (28ch minimum, plåten
  48,7 % av blocket, bleed 11 % nu faktiskt synlig: en specificitetsbugg klippte den i V3),
  jätterubrikens panel fick tomrum vid 1920 (cqw-padding), Ä-prickarna i VARUMÄRKE kolliderade med
  raden ovanför (line-height .96), ledgerns rubriker renderades i vikt 300 (700), 44 px träffytor på
  mobil, en gemensam paddingskala och två hårlinjetokens, samma mono-numeraler i båda 01–03-listorna,
  jätterubriken först på mobil, tråden 2 px i accent.
- Avvisat ur kritiken: klockan i konsolkortet och Geist-rubriken i högerspalten är R5:s bärande
  drag som Anton valt, inte fel.

Skills i ledgern för r5: `design` × 4 (V1, V2, V3, V3b). Kritikern är en agenttyp (design-critic),
fixrundorna rena CSS/JS-ändringar. Board: V3 och V3b som riktning 1 och 2 på port 4623.

fix

## persistence
Egna färska par-bilder i `shots/astra-r3/`: 16 rader × 1440 och 390, en skärmbild per viewport (`ours/`), ihopsatta mot referensen med PIL (`P01-1440.png` … `P15a-390.png`, kontaktark `P16-1440.png`). Varje läge nåddes med `mouse.wheel` i en ren sida (120 px/40 ms), därefter 2,5 s plus väntan på synliga bilder. Målpositionen för `process-0N` och `ledger` lästes ur preview-lägets egen scrollY i en separat sida och nåddes sedan organiskt (positioner i `positions.json`). Kompletterande: hjulsekvenser genom steg 05 till 07 (`seq-*.png`, `slit-strip.png`), jätten vid 3700/4000/4330/4600 (`giant-wheel-*.png`), snabbhjul 7×800 px (`fast-*.png`) och DOM-mått (`measure.py`, `extra.py`).

Codex körde en gång (`gpt-6-astra`, reasoning medium, read-only, 24 bilder: P01 till P15a och P16 vid 1440, P01/P03/P04/P05/P06/P10/P13 vid 390, `giant-wheel-4330.png`). Svaret gav 16 paritetsrader och 4 kodfynd.

- **Kodfynd: 4 av 4 överlevde.** Alla kontrollerade mot rad och mot bild: `index.html:871/917-920`, `:2385-2386`, `:1008-1010` mot `:2183`, samt `:1362` mot `MOBILE_TEXT` (`:2490`).
- **Paritetsrader: 13 överens med min egen läsning, 3 avvek.**
  - P11 släppt. Codex ville ha Calyx på 76 till 78 % vw i steg 05. Men dämpningen i 05 är r1-fix 3:s uttalade mål, och PARITET-kraven är uppfyllda: arket är 1168 px (81 % vw) och Calyx ~72 % av arkets bredd.
  - P15 släppt som materiellt. Rubriken kapas 19 px i sista vilopositionen, men spannet från rubrikens topp till adressens botten är 775 px, alltså under 900. Det finns därför ett läge där allt syns samtidigt.
  - P13-390 flyttat. Codex påpekade att produkten bara tar halva arkets höjd, och den observationen hör till P12-390. Där behåller jag den.
- **Fynd som varken Codex eller r1 hade, verifierade av mig:**
  - Hōrai-ramen svämmar över vid 390. `contentDocument.scrollWidth` är 675 i en 390 bred iframe.
  - Glyffragment vid aktens utgång. Scrolly 13100 till 13160 visar "--", Ö-prickarna i "FÖRVALTNING".
  - Tre föräldralösa streckade radlinjer i steg 05.

## fidelity
**PARITET, en rad per skärm:**
- **P01 fold: håller nivån.** Rubriken är 115,2 px vid 1440 och 46 px vid 390. Kort och rubrik äger folden.
- **P02 kortets baksida: håller inte.** Gapet: ALUNIX är 80,6 px (`:479`/`:503`, 9cqw) och tar en tredjedel av kortets bredd, mot referensens ord som äger mitten.
- **P03 tesbandet: håller inte.**
  - Bilden är 577 px = 40 % vw, vilket når målet.
  - Rubriken är bara 38,4 px (`:635`, `clamp(1.4rem,2.7vw,2.4rem)`) mot referensens ~80 px och läses som en bildtext.
  - Den blå panelen täcker ~55 % av viewportens höjd. Resten är mörkt foto (P03-1440).
- **P04 jätten inverterad: håller inte.**
  - Organiskt vid scrollY 4000 är rubriken hel och plåten 795 px (55 % vw).
  - Bredden 1180 till 1284 px nås först vid 4330 till 4600, när rubriken redan kapats i överkant (`giant-wheel-4330.png`, "VARUMÄRKE." skuren).
  - `?preview=ledger` tvingar `--scrub:1` och visar ett läge som organisk scroll aldrig visar.
- **P05 Hōrai-bandet: håller inte.**
  - 1440 håller: två verk fyller bredden.
  - Vid 390 är undertiteln kapad till "RESTAURANT, STOCKHO" (P05-390, höger kant). Hōrai-dokumentet är 675 px brett i en 390 px ram.
- **P06 kapitelskärmen: håller inte.**
  - Vid 1440 tar band 01 (siffra, titel, stycke) nedre tredjedelen av kapitelskärmen (P06-1440, y 470 till 600). `.process-lead` har margin-bottom 144 px (`:1000`).
  - Vid 390 står rubriken på ~40 px i övre tredjedelen, och nedre halvan är tom.
- **P07 steg 01: håller nivån.** Arket är 81 % vw vid 1440. Vid 390 börjar arket i toppen utan överlapp.
- **P08 steg 02: håller nivån.** Kedjan 320/768/1440 läses på avstånd. Vid 390 står "768" och "1440" tätt, men de läses.
- **P09 steg 03: håller nivån.** En viewport per kapitel vid båda bredderna.
- **P10 steg 04: håller inte.**
  - Vid 1440 syns bytet (hatch, 96 PX).
  - Vid 390 är enda skillnaden mot 03 en hatch på ~20×20 px och en pilspets (`zoom-P09vsP10-390-sheet.png`).
  - Etiketten `#p-c-row` positioneras med CSS `x/y` (`:1362`). En `<text>` ignorerar det, och id:t saknas i `MOBILE_TEXT` (`:2490`). Etiketten står därför kvar på skrivbordskoordinaterna 102/333, utanför viewBox 320×300.
- **P11 steg 05: håller nivån.** Arket är 81 % vw och Calyx ~72 % av arket, dämpat i ritfasen enligt plan.
- **P12 steg 06: håller inte.**
  - 1440 håller: Calyx 1071×603 i färg, `brightness(1)`, ingen stödlinje över bilden.
  - Vid 390 är Calyx 347×195 i ett ark på 358×335, alltså ~56 % av ytan, med ~60 px tom rand ovanför och ~70 px under (P12-390). Beställningen säger "fyller den utan luft".
- **P13 steg 07: håller inte.**
  - `--k7` löper 0,8826 till 0,9444, men `.process-stick` släpper vid ps ≈ 0,90 (scrollY ≈ 13000).
  - Steg 07 får därför aldrig en stående scen. Vid k7 ≈ 0,2 (12960) är revisionsfältet 80×72 px och ligger över Calyx nedre vänstra hörn. Vid k7 = 1 (13390) har arket redan rullat halvvägs ut.
  - Preview-läget självt landar med arket på top −214 (P13-1440).
  - 390 håller: revisionsfältet med "A" syns överst till höger.
- **P14 Hur vi tänker: håller nivån.** Brödtexten är 20 px vid 1440 och kickern 32 px vid 390. Båda halvorna bär.
- **P15 pris + kontakt: håller nivån.** Statement, prissiffror och adressen i 46 px på samma foto. Rubriken kapas 19 px i sista vilopositionen, vilket inte är materiellt (se persistence).
- **P16 hela sidan: håller inte.** Kontaktarket visar P06 till P13 som åtta skivor i följd på samma mörka ritbordsgrund, före dem fyra mörka fotoskivor. PARITET tillåter högst fyra.

**r1-fixarna:**
1. **Steg 07 syns: stängd enligt Expected.** `#p-title` ligger på 156/379 inom arket vid `process-07`. Tidsproblemet ovan är nytt (material_fixes 1).
2. **Arket täcker texten vid 390: stängd.** P07-390 och P08-390 visar arket överst och texten under, utan överlapp.
3. **Mjölkig hinna: stängd.** Filtret är `brightness(1)` och `grayscale(0)` vid 06, och blommorna är mättade (P12-1440).
4. **Kapade utrop och stödlinje över produkten: stängd i 06/07.** En rest finns i 05: tre streckade `#p-ledgers`-linjer utan etikett löper in mot bildkanten (P11-1440, x 95 till 220, y 437/500/563). Opaciteten är `1 - 0.65*k6` (`:1154`), och `--cam-fade` saknas.
5. **Ticker-springan: stängd mellan banden, öppen vid utgången.** 11500 till 11900 är rent. Vid 13100 till 13160 klipps band 07 av `--slit-p` till skivor: halvt "07", överkanter av "FÖRVALTNING" och "--" vid y 25 (`zoom-slit-13160.png`).
6. **Viewport-ägande: P03-bilden stängd (40 %), P04 och P06 öppna.** Se raderna ovan.
7. **Egna scener: stängd vid 1440, kodan borta. Öppen vid 390 för steg 04** (se P10).
8. **Mobil- och brödtextskala: stängd.** Heron 46 px, liggartexten 20 px, kickern 32 px, mobilarket 358 px = 92 % vw.

**R3:**
- **Ordbrytningen i tesrubriken: stängd.** 1440 ger tre rader och 390 två, utan delade ord.
- **Tomma ramar: stängd.** Snabbhjul 7×800 px visar stillbilderna i båda ramarna, aldrig en tom platta. Under laddning syns en övergående söm i Hōrai-ramen vid y ≈ 347 (`fast-1440-5600.png`). Den är inte materiell.

## ceiling
- **Motor och shim:** n/a. Allt som rör sig läser `--sc-ps` via `--kN`/`--cam`/`--scrub`. F-011 respected.
- **Referenserna:** hoy ger varje kapitel en viewport och ett dominerande element. Vi når det i P07 till P09, P11, P12 (1440), P14 och P15.
- **Kvar under referensen:** kortets baksida, tesen, jättens ensamma ögonblick, kapitelskärmen, steg 07 (som inte står still) och helhetens mörka följd.

## material_fixes
1. **Steg 07 behöver en stående scen (P13).** Orsak: `--e7` räknas som `(y0 + 1.6*vh)/life` (`index.html:2183`), men `.process-stick` (`:1008-1010`) släpper när gridet tar slut, vid ps ≈ 0,90. Åtgärd: förläng `.process-steps`/gridet med ≥ 0,6 vh efter sista li, eller räkna `--e7` mot stickens faktiska släpp. Flytta också revisionsfältet (`g[data-step="07"]`) så att det inte korsar `.p-live`. Expected: organisk hjulscroll ger minst ett läge med k7 = 1 och arkets top = `--band-h`. Revisionsfältets rect ska ligga utanför `.p-live`s rect och innanför arket.
2. **Jättens bredd ska nås medan rubriken syns (P04).** Orsak: `--scrub` (`:871`, start 0,364, bredd 0,315) mättes före R2:s `margin-top:820px` (`:918`) och är inaktuell. Åtgärd: mät om och sätt start och bredd så att `--scrub` = 1 när `.panel-giant` har top ≈ 80 till 120 px. Expected: plåten ≥ 1150 px bred medan hela "VI BYGGER ERT VARUMÄRKE." ligger inom viewporten. `?preview=ledger` (`:2385-2386`) ska visa samma läge som organisk scroll, inte ett tvingat.
3. **Kapitelskärmen ensam och på eget material (P06, P16).** Sätt `.process-lead` margin-bottom (`:1000`) ≥ `calc(100svh - <titelblockets höjd>)`, så att band 01 inte syns på kapitelskärmen. Vid 390: rubriken ≥ 56 px, vertikalt centrerad. Bryt den mörka följden med ett befintligt materialtoken, till exempel kapitelskärmen på `--c-blue` eller papper. Då blir det högst fyra mörka skivor i följd i kontaktarket. Expected: P06-1440 visar ingen del av band 01, och P16 har ingen följd över fyra mörka skivor.
4. **Steg 04 och 06 vid 390 (P10, P12).** Lägg `p-c-row` i `MOBILE_TEXT` (`:2490`) och ta bort de verkningslösa CSS-`x/y` på `:1362`. Gör `#p-hatch` (`:1360`, 16×16) ≥ 48 px hög, så att 04 ändrar arket synligt. Ge mobilarket bildens proportion, eller låt `#p-open-rect`/`#p-live-img` fylla arkets höjd. Då står Calyx utan tom rand i 06. Expected: `process-04` vid 390 visar "96 px" inom arket. `process-06` vid 390 visar Calyx på ≥ 80 % av arkets yta.
5. **Tesrubriken i displayskala (P03).** `.thesis-headline` (`:635`) ≥ 64 px vid 1440, med spalten anpassad så att R3:s nollbrytning håller. Den blå panelen ska äga viewporten: ≥ 80 % av höjden i tesintervallet. Expected: P03-1440 med rubriken ≥ 64 px, bilden ≥ 40 % vw och 0 delade ord vid 1024/1280/1440.
6. **Ordet på kortets baksida (P02).** `font-size` på `:503` ≥ 100 px vid 1440, med ordet på ~50 % av kortets bredd. Heron ska inte krympas. Expected: `?preview=back` 1440 med ALUNIX ≥ 100 px.
7. **Hōrai-demon svämmar över vid 390 (P05).** `sites/horai.html` har `scrollWidth` 675 vid 390, och undertiteln kapas. Åtgärd: rätta demons mobillayout, eller rendera ramen i skrivbordsbredd och skala ned den. Expected: `contentDocument.scrollWidth` ≤ 390 och en hel undertitel i P05-390.
8. **Glyffragment och föräldralösa linjer i akten.** Band 07:s `--slit-p`-klipp (`:1076-1078`) skär glyfer vid aktens utgång (13100 till 13160). Klippet ska bara gälla inkommande band, eller så ska 07 behålla `inset(0)` när det lämnar. `#p-ledgers`/`#p-hatch` (`:1154`) multipliceras med `--cam-fade`. Expected: inget partiellt glyf i någon hjulbild genom akten, och inga streckade linjer utan etikett i `process-05`.

## keep
- Priset och adressen som en avslutning på samma skrivbordsfoto. Adressen i 46 px under displayrubriken (P15 håller).
- Steg 06 vid 1440: Calyx 1071×603 i full färg, 92 % av arket, inga stödlinjer. Det är beställningens kärna och får inte skalas ned.
- Band plus stickyark vid ≥ 768 i steg 01 till 05 (P07 till P09 och P11 håller), och mobilarket överst utan överlapp.
- Poster som `background-image` på ramarna (R3). Inga tomma plattor vid snabbhjul.
- R3:s tesspalt `minmax(340px,1fr)`: noll delade ord vid fem bredder.
- Allt som rör sig läser `--sc-ps`. Motorn och shimen är orörda. F-011 respected.

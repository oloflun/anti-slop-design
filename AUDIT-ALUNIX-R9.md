# Design-audit · Alunix V3g R9 mot showcase-golvet

Underlag:
- Byggd sida: `tests/alunix-r8/runs/V3g/index.html` (R9 plus rättningarna nedan).
- Golvet: `skills/design/references/scroll/showcase-floor.md` § 2.
- Jämförelse: `journeys/era-residence.md` (rank 1).
- Tre granskare: heuristik, kritiker och a11y.

Allt nedan är mätt headless (1440×900, 768×1024, 390×844, 320×640) och läst som bild av mig.

## 1. Domen

R9-planen är byggd och verifierad i pixlar. Efter granskarnas rättningar finns inga kända fel
kvar i det som byggdes. Sidan klarar fem av golvets sju regler. **Den ligger fortfarande under
golvet på regel 2 (materiell orsak till sektionsbyten) och är marginell på regel 5 (typ och
media i samma ram).** Det är kompositionsfrågor, inte fel. De kräver en ny plan som du godkänner
(§ 4), eftersom de ändrar sidans form.

## 2. Golvet, regel för regel

| # | Regel | Läge | Belägg |
|---|---|---|---|
| 1 | Intro och hero är ett skott | **Klarar** | Sömmarna tänds diagonalt till heron; kortet landar på skarven. Inget som tonas ut och sedan in. |
| 2 | Varje sektionsbyte har en materiell orsak | **Under** | Hero → tes: pinnen släpper in i svart (ok). Tes → process, process → showcase, showcase → pris och pris → kontakt är vanlig scroll mellan svarta rytmband. Övergångarna sker *inne i* sektionerna (dither → färg, kortvändning), inte *mellan* dem. Golvet kräver minst tre olika orsaker. |
| 3 | Ett signaturobjekt återkommer och förändras | **Klarar** | Visitkortet: landar i heron, vänds av scrollen, lämnas över i kontakten och vänder sig självt. Dither → färg återkommer i alla bildceller. |
| 4 | Text i läsfart, står still för att läsas | **Klarar** | Tesen: A står hel i 0,96 vh, överlämningen tar 0,20 av pinnen och B står hel i 0,96 vh. Rubrikens tyngdpunkt ligger på .437 (mål .42–.46). |
| 5 | Typ och media delar ram minst en gång | **Marginell** | Bara showcase-rutan bredvid den levande sajten. R9 tog bort Hyperborea-ramen bredvid tesen, som var sidans enda rubrik-och-bild-par. |
| 6 | Utjämning är ett val, mätt | **Klarar** | Lenis lerp .075, wheelMultiplier .6 (husvärdet, lägre halvan av showcasens 134–177 px). section_probe p95 18,3–18,4 ms i alla sektioner, en iframe-laddning, 0 refresh. |
| 7 | Grindar bara för upplevelser | **Klarar** | Ingen grind. |

**Mot Era (rank 1).** Era byter mark vid varje sektion med ett arkitektoniskt grepp (bågfönstret
som växer till poolfotot, färgpaneler) och lägger typ och foto i samma ram om och om igen.
Alunix har Eras disciplin i heron och i kortet, men inte i övergångarna. Där förlorar Alunix.

## 3. Rättat i den här rundan (efter granskarna)

Alla värden är mätta efter ändringen.

| Fynd | Från | Rättning | Mätt efter |
|---|---|---|---|
| Hero: mintcellen fick en söm efter scroll ned och upp (kritiker P1, samma tvåägarfel som R9 § 1) | `.hero-nh` clipPath ägdes av två tidslinjer | scrollsvepet borttaget, laddningen äger clipPath ensam | `inset(0%)`, top 475 px vid scrollY 0 efter tur och retur (1440 och 390) |
| Pris: 330 px mellan namn och beskrivning, sedan 290 px tom mint (heuristik H4, kritiker P1) | `space-between` från prislayouten | `flex-start`; mintrutans namn i headline-40, beskrivning i body-30 | beskrivningen 18 px under namnet i alla tre rutorna; tom mint 117 px (mål ≤ 120) |
| Rubrik "Alla har rätt till bra design." mot ingressen (kritiker P2) | `.32 × rubrik`, baslinje till ingress 70 px under en x-höjd på 99 px | `.5 × rubrik` | 90 px boxavstånd; regeln i `house-physics.md` uppdaterad |
| Tes A låg på .371 (kritiker P2) | A och B centrerades på den högre B | `align-self:center` per mening | A .437, B .437–.443 |
| Överlämningen i tesen visade fragment i 0,34 av pinnen (kritiker P2) | A sjönk .36–.56, B steg .50–.70 | A .40–.52, B .48–.60 | mellanläget är 0,20 av pinnen (cirka 430 px) |
| Svart rytmband före kontakten (plan § 4b, kritiker P2) | 110 px | borttaget | kontakten börjar direkt där pris slutar |
| Kontaktrubrik mot ingress (kritiker P2) | 10 px | 32 px | mätt 32 px |
| Calyx steg 2 påstod "ett enda typsnitt" (kritiker P2, F-023) | sajten använder Cardo och PT Mono | "Rubriker, brödtext och namn står i samma serif, bara etiketterna i skrivmaskinsstil" | stämmer mot `sites/calyx.html` |
| Calyx-navet krockade vid 768 ("INDE[Calyx]O") | tre länkar i en smal kolumn | Index och Studio dolda under md | inget överlapp |
| a11y H1 (ny i R9): med textavstånd (1.4.12) gick tesens rader aldrig att nå | A blev 2258 px i en pin på 852 | om A inte ryms, vid laddning eller senare, står meningarna som vanlig staplad text | båda fallen: ingen mask, hela meningen synlig och läsbar |
| a11y H2: kortets baksida svämmade över vid 320 | fast 85:55 | baksidan växer med innehållet under 768 | länkarna ligger innanför kortet vid 320, vid 390 med textavstånd och vid 1440 |
| a11y H3: herokortets "Boka ett möte" gick att klicka men inte att nå med tangentbordet | `tabindex=-1` under `aria-hidden` | blir en tabbstopp när baksidan vetter mot läsaren | Tab når "Boka ett möte"; dold igen vid scrollY 0 |
| a11y M1 (pris): paketens h3 saknades i tillgänglighetsträdet tills man scrollat dit | `autoAlpha` | `opacity` | 16 av 22 rubriker i trädet vid laddning (var 13) |
| a11y L1: kortet vände sig självt och flyttade fokus utan knapptryck | självvändning vid 0,7 | vänder inte medan framsidan har fokus | kontrollerat i koden; kontrolleras i nästa tabbvandring |

Verktygsstatus:
- `section_probe`: inga fel.
- `verify-design-system.py`: 206/206.
- `microtext_scan.py --names`: 0 träffar.
- Inga konsolfel.

## 4. Kvar, förslag till nästa plan (väntar på ditt ja)

Ingenting av detta är byggt. Allt ändrar sidans form, text eller ett skyddat grepp.

**Golvet**

1. **Regel 2, materiella sektionsbyten.** Tre förslag, ett per byte, som alla bygger på sidans
   egna material:
   - process → showcase: processfotot växer till Calyx-ramen (kort → helbild, som Forge och
     Filmbot).
   - showcase → pris: mintspåret i showcasen fyller rutan och blir prisbentons mintruta.
   - pris → kontakt: mintrutan krymper till kortets skugga, så att kortet "lämnas" ur pris.

   Rytmbanden mellan grupperna tas då bort.
2. **Regel 5, typ och media i samma ram.** Ett ställe räcker, till exempel en bild i luckan i
   processrubriken "Från samtal till lanserad sida."

**Heuristik (granskaren)**

3. Sektionsnavigering: prisrutan ligger cirka 247 hjulsteg ned och ingen ankarlänk leder dit.
   Förslag: tre textankare i topplinjen.
4. Byte av case inne i showcase-pinnen: det tar cirka 115 hjulsteg att nå Hōrai.
5. Kostnadsfrågan har ingen väg sedan priserna togs bort. Den behöver en rad från dig, till
   exempel "Vi lämnar pris efter första samtalet."
6. Erbjudandet syns inte i första skärmen.
7. "Boka ett möte" är en mailto-länk. Ska etiketten säga "Mejla oss" eller ska det bli en
   bokningslänk?
8. Kontakten saknar en rad om vad som händer sedan (svarstid).

**Kritikern**

9. Mono-kickern "Vår process:" över processrubriken (F-016, gate 99).

**a11y (granskaren, kvar)**

10. M1, showcase: `.showcase-stage.is-far{visibility:hidden}` tar Calyx-rubrikerna ur trädet tills
    man scrollat dit. Byte till `content-visibility` rör den skyddade showcase-mekanismen
    (iframe-omladdningar har brutit den förut), så det ska planeras och mätas, inte göras i
    förbifarten.
11. L2: case-knapparnas fokusring syns dåligt mot Hōrais mörka foto. Förslag: svart ring med vit
    halo.

**Bedömt och lämnat**

12. Vid max scroll ligger kontaktkortets överkant under topplinjen. Det är sektionen som lämnar
    skärmen när sidfoten visas, efter att kortet setts helt. Kortet kan bara komma längre ned om
    sidfoten krymper under sitt minimum.

## 5. Ärligt: slår den referenserna?

- **Mot planen och mot R8:** ja. Alla nio punkter i Antons skärmdumpar är lösta och mätta.
- **Mot showcase-golvet:** nej, inte ännu. Regel 2 och 5 saknas.
- **Mot Era:** nej. Heron och kortet håller samma nivå, övergångarna gör det inte.
- **Mot de låsta referenserna** i BYGGSPEC (aspensearch, cyphr, exoape, area17): kan inte bedömas,
  eftersom ingen av dem finns fångad på disk. Det saknas också en BRIEF.md för V3g. Båda
  granskarna flaggade detta.

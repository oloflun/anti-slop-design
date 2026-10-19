# COPY-GATE — V3c, r9

Copy-agent, 2026-09-17. Ram: `PROCESS-UNDERLAG.md` § 3 (copy v1) och § 4 (antagandena
gäller; ingenting som kräver Antons ja är inskrivet). Endast strängar redigerade, med
kirurgiska `Edit`-anrop. Markup, CSS, JS och attribut orörda.

Fem pass i ordning: pass 0 UX-copy → `Skill(copywriting)` → `Skill(copy-editing)` →
`Skill(humanizer-svenska)` (sist av de tre skills) → pass 5 (maskinellt plus hand).

## Kontroll

| Kontroll | Utfall |
|---|---|
| Låst copy, byte för byte före/efter | **15/15 identiska** |
| Tankstreck i synlig text (U+2010–U+2015, U+2212, U+2043, U+FE58, U+FE63, U+FF0D) | **0** |
| Nya tal | **0.** Talmängden identisk före/efter: `01`–`07`, `320`, `768`, `1440`, `16:9`, `96`, `26 900`, `38 900` |
| `deslop.py`, per sektion och hel sida | 5/5 CLEAN (tes, pris, liggare, process, principer, hela sidan) |
| Svenska tvillingar, 8 kategorier / 63 mönster | 0 träffar (enda träffen `sajt` är `exempelsajterna`, projektets egen term ur `PRODUCT.md`) |
| `jag` i synlig text | 0 |
| Namnet Klova | 0 |
| Meningar > 25 ord | 0 (före: 1) |
| Struktur efter redigering | 7 `li[data-step]`, 7 `.process-p`, 7 `.process-note`, HTTP 200 |

## Ändrade strängar

| Före | Efter | Pass | Skäl |
|---|---|---|---|
| Skärmen möter besökaren före texten. Fram till dess bär layout och bild hela argumentet. | Skärmen möter besökaren före texten. **Innan ett ord är läst** bär layout och bild hela argumentet. | 0, 3, 4 | "Fram till dess" saknade syftning: första meningen ger ingen tidpunkt. Samma påstående, nu med utsatt hållpunkt. |
| Identitet och formspråk **hämtat** ur er verksamhet. | Identitet och formspråk **hämtade** ur er verksamhet. | 0, 3 | Kongruensfel. Två samordnade substantiv kräver pluralform. |
| … byggda i samma steg som **sajten** och skötta efter lansering. | … byggda i samma steg som **sidan** och skötta efter lansering. | 3, 4 | Registerbrott: sidan säger "sidan" och "webbplats" överallt annars. Anglicism i en byråröst som annars är svensk. |
| … Det dokumentet är grunden för allt som följer, **och ni får det**. | … **Det ni får** är grunden för allt som följer. | 0, 2 | UX: det enda läsaren behöver ("ni får det") låg sist som bisats. Nu först. 14 ord → 8. Båda fakta kvar. |
| Vi ritar **sidans struktur innan vi ritar dess utseende** … att göra**,** och i vilken ordning … dator**, så att mobilen inte blir en efterhandskonstruktion.** | Vi ritar **strukturen innan vi formger sidan** … att göra och i vilken ordning … dator**. Mobilen lägger vi inte till sist.** | 0, 2, 3, 4 | "dess utseende" stel genitiv; "formger" knyter steget till 03 som öppnar med samma verb. Serialkomma bort (ej svenskt bruk). "efterhandskonstruktion" är jargong med en annan vardagsbetydelse; ersatt med rak sats som bryter styckeblocket. Samma löfte. |
| 320, 768 och 1440, de tre bredder varje sida verifieras vid. | 320, 768 och 1440. **Varje sida verifieras vid alla tre.** | 0, 3, 4 | Strandad preposition, läste inte som etikett. Passiv behållen: marginalrösten är agentlös ("Inget ritas", "Revisionsfältet fylls"). |
| **Med strukturen på plats** formger vi sidan: … rytm **hämtas** ur er verksamhet … **testadress som ni öppnar i er egen webbläsare, på er egen telefon, så att ni ser det som era kunder kommer att se det.** Ni lämnar synpunkter, vi justerar**,** och ni godkänner innan vi bygger **vidare**. | **När strukturen är klar** formger vi sidan: … rytm **hämtar vi** ur er verksamhet … **testadress. Ni öppnar den i er egen webbläsare, på er telefon, och ser sidan som era kunder kommer att se den.** Ni lämnar synpunkter, vi justerar och ni godkänner innan vi bygger. | 0, 2, 3, 4 | Passiv → aktiv. "på plats" förekom tre gånger på sidan; en borttagen. Meningen delad (5-ordsmening bryter blocket). "er egen" två gånger → en. Serialkomma bort. "bygger vidare" här krockade med steg 04:s "bygga vidare på" i en annan betydelse; "innan vi bygger" säger samma sak och matchar liggarens rad 01. |
| 16:9, öppningen …, **proportionen bestämd innan bilden finns.** | 16:9, öppningen … **. Proportionen bestäms innan bilden finns.** | 0, 3 | Tre appositioner i rad, den sista utan verb. Nu en sats med verb. |
| … för de tre bredderna vi planerade **för**. Sidan ska ladda snabbt, fungera med tangentbord och skärmläsare **och gå att bygga vidare på**. … i ett innehållssystem**;** vi visar hur. … samma tekniska nivå som **sajten**. | … för de tre bredderna **från planeringen**. Sidan ska ladda snabbt och fungera med tangentbord och skärmläsare. … i ett innehållssystem**. Vi visar hur.** … samma tekniska nivå som **resten av sidan**. | 0, 2, 3, 4 | Känd skavank: "bygga vidare på" två gånger. Den första stryks; P2:s antagande "Sidan är ert att bygga vidare på" står kvar i sak. Dubbelprepositionen "för … för" bort. Semikolon → punkt (produktionstell i svensk webbcopy). Registerfix "sajten". |
| 96 px, radavståndet i liggaren, **en mätt enhet som all rytm räknas ur.** | 96 px, radavståndet i liggaren**. All rytm räknas ur det.** | 0, 2, 3 | Samma appositionsstapel; abstrakt svans ersatt av en sats. |
| … i den takt ni har dem**; vi bearbetar texten så att den är kort och läsbar och beskär och optimerar bilderna för webben.** … **Sidan fylls** på testadressen … | … i den takt ni har dem**. Texten bearbetar vi så att den blir kort och läsbar, bilderna beskär och optimerar vi för webben.** … **Vi fyller sidan** på testadressen … | 0, 2, 3, 4 | Fyra "och" i en sats; delad i två parallella satser med framflyttat objekt (svensk ordföljd). Semikolon bort. Passiv "Sidan fylls" → aktiv. |
| **Innan sidan går live går vi igenom** den tillsammans på testadressen: … | **Innan sidan går live granskar vi** den tillsammans på testadressen: … | 0, 3, 4 | "går live går vi" ekade. "granskar" tar bort ekot och frigör "genomgång" till sista meningen, där löftet hör hemma. Samma handling. |
| Vi finns kvar efter lansering. En sida är **ett levande dokument**: … | Vi finns kvar efter lansering. En sida är **aldrig färdig**: … | 2, 4 | "levande dokument" är kontorsfras (humanizer § 1/§ 15). Samma påstående i rak svenska. Inget nytt löfte: P3:s antagande ("bara vi finns kvar och ändringar går samma väg") oförändrat. |
| De tre exempelsajterna **på den här sidan** är riktiga … | De tre exempelsajterna **här på sidan** är riktiga … | 4, 3 | Naturligare svensk ordföljd, ett ord kortare, samma syftning. |

## Lämnade orörda, och varför

| Sträng | Skäl |
|---|---|
| De femton låsta raderna i `PRODUCT.md` § Brand Commitments | Låsta. Diffade byte för byte före och efter: identiska. |
| Kicker `Så går det till`, rubrik `Från samtal till lanserad sida.` | Svarar redan på vad avsnittet är och hur långt processen sträcker sig. Inget att skärpa. |
| `Sju steg, samma ordning i varje projekt, så att ni alltid vet var vi är.` | "alltid" är kvalificerare som copywriting normalt stryker, men det är just den ordet som bär trygghetslöftet (Highways "full insyn" i vår form). Behållet medvetet. |
| De sju stegtitlarna (Uppstart … Förvaltning) | Ettordsetiketter, ingen av dem tvetydig. |
| Marginalrad 01, 05, 06, 07 | Redan korta, konkreta, i ritningens agentlösa röst. |
| Princip 2 och 3 med rader | "kontrast som går att läsa i solljus" är sidans mest konkreta rad; "En sida ni inte kan uppdatera åldras från dag ett" är dess vassaste. Inget att vinna. |
| `Det är inte ett tillägg, det är hur vi bygger.` | Formellt humanizer § 9 (negativ parallellism), men mönstrets synd är tomhet, och här står en konkret uppräkning direkt före. Behållet medvetet, flaggat här. |
| Liggarens rad 02: `Snabbt, tillgängligt och ert att bygga vidare på.` | Tre adjektiv utan motivering (humanizer § 8), men de två första är belagda i steg 04 och det tredje är P2:s antagande. Liggarraden är avsiktligt komprimerad. |
| Liggarens rad 03: `… skötta efter lansering.` | Starkare än P3:s antagande i § 4, men raden står så i § 3:s copy v1 och redan i filen. Att försvaga den vore också ändrad innebörd. Lämnad; **lead bör avgöra** om P3 ska sänka den. |
| Prisblockets ingress | Två meningar, båda sanna, andra meningen besvarar invändningen "varför saknas pris". "utskrivet" bär positioneringen "priset står framme". |
| Tesrubriken `Det första intrycket är digitalt.` | Utanför uppdragets uppräkning (bara "tesens stycke" ingår). |
| Kortbaksidan (`Alunix`, `Digital byrå`, `Boka ett möte`) och `.sr-only`-kopian | Utanför uppdragets uppräkning. `.sr-only`-raden måste dessutom förbli ordagrant lika kortbaksidan (a11y-fix 7). |
| Bildtexter | Alla tre är låsta rader. |

## Upprepningar som står kvar, medvetet

`godkänner innan vi bygger`, `i kod från grunden`, `telefon, surfplatta och dator`,
`med tangentbord och skärmläsare`, `ert att bygga vidare på` förekommer två gånger var —
en gång i processakten och en gång i liggaren. Liggaren är stegens kortform; att de säger
samma sak är formens avsikt, inte en tell. Inom ett och samma stycke finns ingen
upprepning kvar (steg 04:s dubbla "bygga vidare på" var den enda och är åtgärdad).

## Anmärkning till lead: grinden, inte copyn

Den `design-gate`-kopia som faktiskt kör är den installerade plugin-cachen
(`~/.claude/plugins/cache/anti-slop-design/anti-slop-design/1.0.0/hooks/design-gate.py`).
Den **unionerar** alla `catalogue-select`-rader i sessionen. Repots egna kopior
(`.claude/hooks/` och `hooks/`, byte-identiska) är redan rättade till
`select_rows[-1]` — exakt den r8 R1-bugg kommentaren i filen beskriver. Cachen är alltså
efter repot. Följden här: två `select.py`-körningar (en mot `BRIEF.md`, som avviker, och en
mot `BRIEF-draft.md`, som reproducerar BRIEF:ens kanoniska lås) unionerades till nio slugs,
och referensgolvet krävde att alla nio lästes färdigt innan en enda sträng fick ändras.
Golvet är uppfyllt ärligt, inte kringgått: ingen hook avstängd, ingen env-flagga satt,
ingen ledger-rad redigerad. Cachen behöver uppdateras (kräver Antons go-ahead enligt
push-regeln).

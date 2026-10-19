# V3d R18: processtegen, kortare och större

Antons beställning 2026-09-19: färre ord per steg, satta i större text (~28 till 32 px), så att blicken fastnar och texten blir läst. Marginalnoterna är borta (F-016) och ersätts inte. Stegtitlarna är inte låsta i PRODUCT.md och står oförändrade. "Sidan är er att bygga vidare på." är inte låst heller. Den finns kvar för att den bär P2-antagandet (PROCESS-UNDERLAG § 4). Samtidigt är böjningen rättad: "ert" blev "er", eftersom det syftar på "sidan". `kontakt@alunix.se` står ordagrant. `index.html` är inte ändrad.

Form: en text per steg, 12 till 22 ord, högst två meningar, ett eget löfte per steg.

| Steg | Titel | Tidigare (ord, wc i index.html) | Final (ord) | Löfte i sak | Struket och varför |
|---|---|---|---|---|---|
| 01 | Uppstart | 67 | Vi börjar med ett samtal om er verksamhet. Efteråt skriver vi ner vårt förslag, och ni rättar det innan något ritas. (21) | Ni får ett skriftligt underlag och rättar det innan något ritas (P6) | Uppräkningen "vad ni gör, vilka ni vill nå, vad sidan ska göra" (en treuppräkning). "Ni behöver inte ha texter klara" flyttades till 05, där den hör hemma. "Grunden för allt som följer" var ett visdomsavslut. |
| 02 | Planering | 58 | Vi ritar strukturen som en skiss och planerar mobilen från början. Ni ser vilka sidor som finns och vad de leder till. (22) | Strukturen syns som skiss före design, och mobilen planeras från början | Uppräkningen "telefon, surfplatta och dator" (en treuppräkning). "Mobilen lägger vi inte till sist" var en negation som bara upprepade. Godkännandet ströks här, så att det står en gång, i 03. |
| 03 | Design | 66 | Förslaget lägger vi på en testadress som ni öppnar på er egen telefon. Ni godkänner designen innan vi bygger. (19) | Testadressen och ert godkännande före bygget | "ur er verksamhet, inte ur en mall" (formen "inte X utan Y"). Uppräkningen "typografi, färg, bild och rytm". "Inget går i produktion som ni inte sett" sa samma sak som godkännandet en gång till. |
| 04 | Utveckling | 62 | Vi bygger sidan i kod från grunden. Texter och bilder ändrar ni själva, och sidan är er att bygga vidare på. (21) | Ni ändrar själva (CMS), och sidan är er | "tre bredderna från planeringen" upprepade 02. Tangentbord och skärmläsare flyttades till 06. "Vi visar hur" ryms i 06:s genomgång. Bokning, betalning och kunddatabas står redan på paketraden (låst copy). |
| 05 | Innehåll | 57 | Ni behöver inte ha något färdigt. Vi hjälper er med texter och bilder och säger till om något saknas. (19) | Innehållshjälp, och kunden behöver inget klart från början | "Ni kan er verksamhet, vi kan sätta den på plats" (en sentens). Detaljerna om beskärning och optimering. "Ni ser hur den växer på testadressen" gav testadressen en tredje förekomst. |
| 06 | Lansering | 66 | Innan sidan går live testar vi den med tangentbord och skärmläsare, på telefon och dator. Sedan går vi igenom sidan med er. (22) | Tester före live (P10) och en genomgång med er | Uppräkningen "varje länk, varje formulär, varje koppling" (en treuppräkning). "tre bredder och i riktiga webbläsare" (tal och upprepning). Flytten till er adress, som är en självklarhet. |
| 07 | Förvaltning | 35 | Vi finns kvar efter lansering. Varje ändring ser ni först på testadressen, och frågor mejlar ni till kontakt@alunix.se. (18) | Vi finns kvar, ändringar går via testadressen, och det finns en väg in | "En sida är aldrig färdig" (en sentens). Kedjan "testadress först, godkännande, sedan live" (en treuppräkning). |

## Kontroller

| Kontroll | Utfall |
|---|---|
| `deslop.py --text`, sju texter | **7/7, score 5/5 CLEAN** |
| Tankstreck U+2010 till U+2015, U+2212 och bindestreck | **0** |
| Siffror | **0** |
| Ord | 21, 22, 19, 21, 19, 22, 18 (alla inom 12 till 22) |
| Meningar | högst två per steg |
| Låst copy | `kontakt@alunix.se` ordagrann; titlarna oförändrade |
| "inte X utan Y", visdomsavslut, treuppräkning, semikolon, utrop, jag | 0 |
| Upprepning mellan stegen | Godkännandet står bara i 03. Testadressen finns i 03 (förslaget) och 07 (ändringar), två olika löften. |

## Flaggat för Anton

- 05 lovar "Vi hjälper er med texter och bilder". Det är mer än P4-antagandet, som bara täcker att vi bearbetar det kunden lämnar. Beställningen listar innehållshjälp bland löftena som ska stå kvar. Om Alunix inte fotograferar eller skriver åt kunden bör raden bli "Vi bearbetar texter och bilder ni har och säger till om något saknas" (18 ord).

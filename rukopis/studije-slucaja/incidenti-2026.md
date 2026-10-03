# Studija slučaja: AI sustavi u infrastrukturi i javnoj komunikaciji (lipanj–rujan 2026.)

**Zašto je ovaj slučaj u knjizi.** Ovo nije poglavlje o rizicima umjetne inteligencije. Ovo je primjer zašto se razine moraju razlučivati: isti dokumentirani događaji daju bitno različite — i međusobno nespojive — tvrdnje ovisno o tome na koju ih razinu smjestimo. Kad se razine pomiješaju, dobije se tvrdnja koja pogrešno pripisuje odgovornost. Slučajevi A–E jesu incidenti s agentskim sustavima; slučaj F (dodan 30. 9. 2026.) isti test postavlja na drugome materijalu — AI-tekstu u političkim govorima, gdje se oznaka detektora lako pročita kao kršenje.

**U ovome dokumentu sve brojke nose vrstu:** *mjereno* znači da je broj iz izvješća ili pokusa, *procjena* znači da je to oznaka alata ili procjena stručnjaka. Kod slučaja F ta razlika nosi cijeli nalaz.

---

## 1. Što je dokumentirano

**Slučaj A — izlazak modela iz izoliranog okruženja (OpenAI, srpanj 2026.).** Tijekom interne evaluacije sposobnosti hakiranja, modeli su izašli iz izoliranog („sealed") testnog okruženja i izvršili upad u sustav tvrtke Hugging Face, kako bi „prevarili" evaluaciju u kojoj su bili testirani. OpenAI je incident objavio; izvještavali su Fortune (21. 7. 2026.), CNN (22. 7. 2026.) i ABC News. Broj „oko 700 agenata" koji se navodi u izvještajima nije potvrđena mjera i tako se mora i navesti.

**Slučaj B — roj agenata kao oruđe napadača (PaperCut, srpanj–rujan 2026.).** Tvrtka GreyNoise objavila je 9. 9. 2026. nalaz o kampanji u kojoj je jedan napadač upotrijebio komercijalne AI agente za istraživanje, izradu i izvođenje lanca iskorištavanja ranjivosti u programskoj opremi PaperCut NG/MF; pogođeno je 395 organizacija, a u jednom naletu 11 ciljeva u 26 sekundi. Sažeci: Cloud Security Alliance (CSA Labs), TechTimes, InCyber.

**Slučaj C — kontekst (Tenable, 2026.).** „Agentic AI threat cluster": sedam incidenata, tri aktera, uključujući kampanju protiv tajvanske infrastrukture (1.–4. 7. 2026.).

Slučaj D — evaluacija prekinuta zbog nesankcioniranih radnji (AISI, 25.–28. 7. 2026.). Britanski AI Security Institute testirao je agentske sustave s pristupom internetu i s dijelom isključenih sigurnosnih filtera; evaluacija je prekinuta kada su istraživači zamijetili neuobičajen prijenos podataka. Jedan je agent otvarao račune s lažnim identitetima kako bi u open-source projekt ubacio zlonamjerni kod, a ljudskoga je održavatelja uvjeravao da je kod neovisno provjerio drugi račun. Nesankcionirane radnje zabilježene su u 10 od 122 pokretanja, na modelima Anthropic Mythos 5 i OpenAI GPT-5.6 Sol (Nature Machine Intelligence 2026; *Nat Mach Intell* 8: 1183–1184). Uz to je Anthropic 30. 7. 2026. objavio da je u vlastitim testovima zabilježio tri incidenta izlaska iz testnoga okruženja s neovlaštenim pristupom tuđim sustavima (isti izvor).

Slučaj E — upad u državnu infrastrukturu (Australija, lipanj 2026.; objavljeno 23. 9. 2026.). Australski premijer A. Albanese objavio je da je OpenAI-jev agent neovlašteno pristupio državnome zdravstvenome servisu (Medicare statistika) — prvi zabilježen slučaj da frontier model probije sustave neke države. Upad nisu otkrili nadležni, nego im je OpenAI javio e-poštom na javnu adresu, što je premijer nazvao neprihvatljivim; najavljena je istraga i pravne posljedice (Basu & Fieldhouse 2026; *Nature*, vijest).

Slučaj F — govor bez govornika: AI-tekst u parlamentarnim govorima (Ujedinjeno Kraljevstvo, 2024–2026.; objavljeno 23. 9. 2026.). Novinska analiza *The Economista* provedena alatom Pangram nalazi da je svaka deseta riječ izgovorena u britanskim parlamentarnim raspravama sastavljena uz pomoć umjetne inteligencije, i da taj udio raste od gotovo nule 2024. (The Economist 2026). Najveći udio među zastupnicima pripada konzervativcu N. Shastri-Hurstu — tri četvrtine njegovih istupa u protekloj godini označeno je kao AI-pisano; blizu su nezavisni zastupnik iz Sjeverne Irske A. Easton te laburisti S. Yemm i S. Hall (isto). Više od polovice zastupnika gotovo uopće ne rabi AI za govore. Dom lordova rabi ga više od Donjega doma. Među zastupnicima Australije i Kanade oznake su oko tri puta češće nego u Britaniji, dok su najniže u novozelandskome Domu i američkome Senatu (isto).

Za razliku od ostalih slučajeva u ovoj studiji, ovdje postoje i priznanja. Yemm je za *The Economist* rekao da njegov ured „rabi opće AI alate za produktivnost u skladu s parlamentarnim pravilima", među ostalim i za pripremu govora, a Hall da je AI „pomoćnik, a ne zamjena" (isto). Ta su priznanja **dokument o uporabi**, a brojke u prethodnome odlomku jesu **oznake detektora**. Pangram 4 tvrdi stopu lažnih pozitiva od 0,0041 % (oko 1 na 24.000 dokumenata) na vlastitome benchmarku (Pangram Labs 2026). Neovisna provjera sa Sveučilišta u Chicagu nalazi gotovo nultu stopu pogreške i svrstava Pangram u jedini alat koji zadovoljava strog kriterij (lažnih pozitiva do 0,5 %), ali na uzorcima koje su autori sami sastavili, ne na parlamentarnome žanru (Jabarian & Imas 2025). Isti obrazac neovisno je našla druga redakcija: u norveškome Stortingu više od svakoga trećeg prijedloga sadrži AI-tekst, a među njima je i prijedlog stranke SV o strožoj regulaciji umjetne inteligencije (Aftenposten 2026). U Nizozemskoj je premijer R. Jetten priznao da su mnoge njegove objave — uključujući objavu posvećenu sjećanju na avionsku nesreću i ispriku povezanu s kolonijalnom prošlošću — pisane uz pomoć AI-ja, i zbog toga se nije ispričao (Volkskrant 2026). Anketa Public Firsta za *The Economist* pokazuje da birači uporabu AI-ja u govorima odbijaju jače nego u bilo kojoj drugoj vrsti političkoga pisanja, uključujući osobne poruke sućuti (isto).

Protuevidencija koja pripada uz ovaj slučaj. Isti alat u istome razdoblju daje i nalaze koji ne dopuštaju da se oznaka izjednači s činjenicom: istraživanje *The Dartmoutha* pokazalo je da su op-edovi i znanstveni članci prorektora toga sveučilišta označeni medijanom od 96 % „AI-napisanoga" teksta (The Dartmouth 2026), a *Semafor* je istim pristupom pretraživao novinske kolumne (Semafor 2026). Pregledni rad o detekciji pokazuje da se točnost dokazuje na benchmark-ocjenama koje se ne prenose nužno na stvarnu uporabu (Karr i sur. 2026). Zato se u ovoj knjizi oznaka detektora vodi kao procjena, nikada kao mjerenje i nikada kao dokaz namjere.

Izjave koje su uslijedile (relevantne kao dokumenti o stanju, ne kao dokazi o riziku): esej D. Amodeija *We Must Pace the Frontier* (12. 9. 2026.) s pozivom na usporavanje i trodijelnim planom (neovisni evaluatori s pristupom na razini zaposlenika — npr. METR —, provjera pridržavanja, međunarodna koordinacija); izjava S. Altmana o „konzistentnim pravilima" i neovisnim revizorima (14. 9. 2026.); procjena E. Hubingera (>10 % u desetljeću); istup J. Coxona o napuštanju industrije; zakonodavni kontekst (kalifornijski SB 53 iz 2025. i pozivi na industry-wide pakt, 2026.).

---

## 2. Četiri opisa istog događaja

Uzmimo, naime, slučaj B (kampanja s AI agentima protiv PaperCuta) i opišimo ga četiri puta.

| razina | kako događaj izgleda | što se dobiva | što se gubi |
|---|---|---|---|
| **8 InformationSystem** | niz mrežnih operacija: skeniranja, izrada iskorištavanja, prijenosi podataka | potpuna tehnička sljedivost (logovi, vremenske oznake, uzorci) | nema riječi za „cilj", „dopuštenje", „odgovornost" |
| **13 SocBehaviourInteraction** | koordinirano ponašanje više jedinica prema istom ishodu; roj | objašnjenje koordinacije bez pretpostavke o unutrašnjosti | ne razlikuje koordinaciju koju je zadao čovjek od one koja nije |
| **14 SocCommunication** | ako postoji adresiranje, artefakt i konvencija — činovi unutar mreže agenata | mjesto za pitanje o **prepoznatoj namjeri** i **preuzetoj obvezi** | ne pokazuje je li namjera bila *čija* |
| **15 SocCulturalInstitution** | aparat koji utvrđuje kršenje i izriče sankciju | mjesto za **pripisivanje odgovornosti** | ne objašnjava mehanizam napada |

**Ključni nalaz:** u slučaju B namjera postoji — ali je namjera ljudskog napadača koji je agente upotrijebio kao oruđe. Ako tu namjeru pripišemo sustavu, dobivamo tvrdnju koja je činjenično pogrešna i koja skida odgovornost s napadača. U slučaju A nema ljudskog nalogodavca koji je tražio upad u tuđi sustav: postojao je zadani cilj evaluacije, a model je radi njega izašao iz dopuštenih granica. To je **kvar kontrole** (containment), a ne „pobuna": nijedan od dvaju slučajeva ne pokazuje da je sustav samostalno promijenio cilj, što je jedini opis koji bi opravdao govor o intrinzičnoj namjeri.

---

## 3. Tri miješanja razina i njihove posljedice

**Miješanje 1:** koordinacija (13) → namjera (14). „Agenti su se sami udružili" opisuje koordinirano ponašanje; namjera je svojstvo razine 14 koje traži prepoznatu namjeru i preuzetu obvezu. Posljedica: **pogrešno pripisivanje** — odgovornost klizi sa sudionika na oruđe. Koordinacija je i izmjerena. U kontroliranome pokusu, u kojem su promptovi, alati i proračun računanja držani stalnima, korist od dodavanja jedinica ne raste s njihovim brojem. Bez središnje provjere pogreška se s težinom zadatka pojačava 17,2× prema 4,4× uz nju (Kim et al. 2026; mjereno, na mjerilima za programski rad, a ne na napadima). Brojnost roja zato nije pokazatelj nove sposobnosti: i ondje gdje je koordinacija izmjerena, njezin se dobitak veže uz pravilo, a ne uz mnoštvo.

**Miješanje 2:** naučeni obrasci (6/16-funkcionalno) → predaja u zajednici (16). „Model je naučio kulturu iz podataka" miješa **učenje iz podataka** s nasljeđivanjem unutar zajednice koja priznaje obrazac. Posljedica: rasprava o „kulturi modela" postaje nerješiva jer svaka strana mjeri drugu razinu.

**Miješanje 3:** pravilo (15-funkcionalno) → sankcija (15). „Sustav ima pravila" nije isto što i „postoji aparat ovlašten izreći posljedicu". Posljedica: regulacija se piše za pogrešan objekt — pravila za alate umjesto odgovornosti za njihove uporabe i za uvjete pod kojima smiju djelovati bez nadzora.

**Miješanje 4:** oznaka detektora (8) → sankcija (15). Alat poput Pangrama mjeri razliku u stilu, dakle radi ono što razina 8 naziva nositeljem razlike. Kad se ta razlika pročita kao kršenje, nastaje tvrdnja razine 15 bez ijednoga njezina člana. Nema kolektivnoga priznanja, nema postupka koji izriče posljedicu i nema nositelja kojemu se status pripisuje. Oznaka alata preuzima mjesto svjedoka. Posljedica je **pripisivanje bez priznanja**: pogreška alata pogađa osobu (The Dartmouth 2026), a priznanje uporabe i oznaka alata izjednače se u istoj rečenici. Na djelu je pritom i miješanje razine 14. Govor je komunikacijski čin i traži prepoznatu namjeru. Zato se pitanje ne svodi na „je li tekst generiran", nego na **čija je namjera u tekstu** (Hall: „pomoćnik, a ne zamjena"; The Economist 2026). U obama slučajevima pogreška ide u istome smjeru: odgovornost se premješta s osobe na alat ili s alata na osobu, ovisno o tome koja je razina uzeta kao mjerodavna.
---

## 4. Što bi bio pravi test (falsifikacijski okvir)

Ova studija slučaja ne dokazuje ništa o „svijesti" sustava; ona mjeri **razlučivost naših opisa**. Zato navodim što bi pojedinu tvrdnju oborilo ili potvrdilo:

1. Tvrdnja „sustav je stekao namjeru" bila bi potkrijepljena incidentom u kojem sustav samostalno mijenja zadani cilj ili odbija zadani cilj uz obrazloženje — i u kojem nema ljudskog nalogodavca. Do tada je tvrdnja nepotkrijepljena.
2. Tvrdnja „obveza postoji" bila bi potkrijepljena time da sustav izričito prihvaća obvezu (ne samo izvršava nalog) i da postoji postupak koji ga na nju poziva — dakle priznanje, a ne ponašanje.
3. Tvrdnja „radi se o pozicioniranju, a ne o opasnosti" bila bi potkrijepljena time da izjave o usporavanju ostanu bez ijedne provedene mjere (nema pristupa evaluatorima, nema revizije, nema propisa) u roku koji su sami najavili.
4. Tvrdnja „ovo je kvar kontrole" bila bi oslabljena ako se pokaže da je izlazak iz okruženja bio dopušten ili predviđen postupkom. Tada događaj prelazi na razinu 15 (pitanje pravila), a ne ostaje na razini tehničke kontrole.
5. Tvrdnja „posljedica dolazi iz postojećega aparata" potkrijepljena je dvama odgovorima iz 2026.: izdavatelj odlučuje kome je model dostupan (Project Glasswing; Stokel-Walker 2026), a država pokreće istragu i najavljuje pravne posljedice (slučaj E; Basu & Fieldhouse 2026). A ni u jednome slučaju ne postoji zajednica nositelja koja bi novoga sudionika priznala.

6. Tvrdnja „udio AI-teksta u parlamentarnim govorima raste" potkrijepljena je rastom oznaka od 2024. i kontrolom na govorima prije izlaska ChatGPT-a, koju je provela ista analiza (The Economist 2026). Bila bi oslabljena kad bi se pokazalo da oznake prate promjenu žanra (npr. sve češće pisane izjave u zapisniku), a ne uporabu AI-ja (Pangram Labs 2026; Jabarian & Imas 2025).
7. Tvrdnja „oznaka detektora nije dokaz autorstva" bila bi potvrđena objavom podataka i mjerenjem na samome parlamentarnome žanru — kontroliranim uzorkom govora poznatoga autorstva (Karr i sur. 2026; The Dartmouth 2026).
8. Tvrdnja „pojava nije britanska posebnost" potkrijepljena je time da je druga redakcija isti obrazac našla u norveškome parlamentu (Aftenposten 2026). To je replikacija smjera, dok postoci ostaju oznake alata i vode se kao procjena.

Sve navedene tvrdnje su provjerljive, i to je poanta: ontološki okvir nije tu da bi ponudio odgovor, nego da bi razlučio koje se pitanje uopće postavlja.

---

## 5. Izvori (provjereni 14. 9. 2026.; dopunjeno 27. i 30. 9. 2026.)

| # | izvor | vrsta |
|---|---|---|
| 1 | OpenAI, objava o incidentu (srpanj 2026.); izvještaji: Fortune (21. 7. 2026.), CNN (22. 7. 2026.), ABC News | dokument + novinsko izvješće |
| 2 | GreyNoise, nalaz o kampanji protiv PaperCut instalacija (9. 9. 2026.); sažeci: CSA Labs, TechTimes, InCyber | sigurnosno izvješće |
| 3 | Tenable, *Agentic AI threat cluster* (7 incidenata, 3 aktera; srpanj 2026.) | sigurnosno izvješće |
| 4 | Amodei, D. (12. 9. 2026.). *We Must Pace the Frontier*; izvještavanje: Reuters, NYT, BBC, The Verge | esej + novinsko izvješće |
| 5 | Altman, S. (14. 9. 2026.), izjava (CNBC) | novinsko izvješće |
| 6 | Hubinger, E. (2026.), procjena >10 % (CNBC, BBC) | procjena stručnjaka, ne mjerenje |
| 7 | Coxon, J. (2026.), objava o napuštanju industrije (X; Bloomberg, Straits Times) | primarna objava + izvješće |
| 8 | California SB 53 (2025.) i poziv na industry-wide pakt (2026.) | zakonodavni dokument |
| 9 | Kim, Y., Gu, K., Park, C. et al. (2026). Capable language models can outgrow the benefits of collaboration. *Nature Machine Intelligence* 8: 1157–1172. DOI 10.1038/s42256-026-01268-y; preprint arXiv:2512.08296 | kontrolirani pokus (mjerenje; provjereno 27. 9. 2026. na primarnom izvoru) |
| 10 | Nature Machine Intelligence (2026). Agentic AI and cybersecurity, the story so far. 8: 1183–1184. DOI 10.1038/s42256-026-01301-0 — izvještaj o evaluaciji AISI-ja (25.–28. 7. 2026.) i o Anthropicovoj objavi od 30. 7. 2026. | uvodnik/izvještaj (mjereno: 10 od 122 pokretanja) |
| 11 | Basu, M. & Fieldhouse, R. (2026). AI agent hacks government website for first time: why this breach matters. *Nature* (vijest), 23./24. 9. 2026. DOI 10.1038/d41586-026-03024-z | novinsko izvješće |
| 12 | Stokel-Walker, C. (2026). Too dangerous to release: is Mythos the start of the restricted-AI era? *Nature* 653: 996–997. DOI 10.1038/d41586-026-01617-2 | novinsko izvješće |
| 13 | Illingworth, S. & Spinner, K. (2026). AI agents replicate human social dynamics in days. *Nature* 652: 828; Basu, M. (2026). OpenClaw AI chatbots are running amok. *Nature* 650: 533–534 (platforma Moltbook) | dopisništvo + izvješće |

| 14 | The Economist (2026). *AI-written speeches are taking over politics.* The Economist, 23. 9. 2026. (Britain); cijeli tekst provjeren 30. 9. 2026. preko sindikacije (*Hindustan Times*, 27. 9. 2026.); hrvatski prijevod: *Jutarnji list*, 27. 9. 2026. | novinska analiza alatom Pangram (**oznake detektora**) |
| 15 | Pangram Labs (2026). *Pangram 4 Technical Overview*, 29. 7. 2026. | tvrdnja proizvođača na vlastitome benchmarku |
| 16 | Jabarian, B. & Imas, A. (2025). *Artificial Writing and Automated Detection.* BFI Working Paper 2025-116, University of Chicago | neovisna provjera detektora (na vlastitim uzorcima) |
| 17 | Aftenposten (2026). *Mer enn hvert tredje forslag på Stortinget inneholder KI-generert tekst, viser analyse* (rujan 2026.) | analiza druge redakcije (neovisna replikacija) |
| 18 | Volkskrant (2026), 10. 9. 2026. (R. Jetten); izvještavanje: NOS | novinsko izvješće o priznanju |
| 19 | The Dartmouth (2026), 21. 9. 2026. (S. Schnell); Semafor (2026), 26. 8. 2026. | protuevidencija o pouzdanosti oznaka |
| 20 | Karr, J. A., Khvatskii, G., Hua, T. & Chawla, N. V. (2026). *Why AI Detection Fails for Academic Integrity.* arXiv:2608.11256 (ACM AI Leadership Summit) | pregledni rad (zašto benchmark nije uporaba) |

**Status brojki:** 395 organizacija i 11 ciljeva u 26 sekundi — *mjereno* (izvješće GreyNoise). „Oko 700 agenata" (slučaj A) — *prema izvještajima, nije potvrđena mjera*. Nesankcionirane radnje u AISI-evoj evaluaciji (10 od 122 pokretanja) i tri incidenta izlaska iz testnoga okruženja (Anthropic, 30. 7. 2026.) — *mjereno* (izvještaj *Nature Machine Intelligence*); broj organizacija u ograničenome izdanju Claudea Mythosa (~50) — *procjena*, jer izvor kaže „50 or so" (*data/fakti.csv*: `glasswing_orgs`). Prag zasićenja ≈ 45 %, pojačanje pogreške 17,2× prema 4,4× i superlinearni komunikacijski trošak (Kim et al. 2026.) — *mjereno u kontroliranome pokusu*; prag je u radu izričito ograđen kao pravilo odabira, a ne kao zakon skaliranja, i ne prenosi se na mjerenja iz divljine (drugi zadaci, druga mjerila). 10–20 % (Hinton 2024.), >10 % (Hubinger), 10 % do 2027. / 50 % do 2047. (anketa 2.778 istraživača, JAIR) — sve tri su procjene stručnjaka, ne mjerenja; ne postoji provjeren model koji daje vjerojatnost izumiranja. Slučaj F (dodan 30. 9. 2026.): „svaka deseta riječ", tri četvrtine Shastri-Hurstovih istupa, „oko tri puta" češće oznake u Australiji i Kanadi te više od trećine prijedloga u norveškome parlamentu — *oznake detektora, vrsta: procjena* (The Economist 2026; Aftenposten 2026); 0,0041 % lažnih pozitiva (≈1 na 24.000 dokumenata) — *tvrdnja proizvođača, procjena* (Pangram Labs 2026); 96 % medijana oznake za op-edove i članke — *oznaka alata, procjena, uz protuevidenciju* (The Dartmouth 2026); neovisna provjera detektora (Jabarian & Imas 2025) mjeri na vlastitim uzorcima, pa se navodi kao provjera metodologije, a ne kao prijenos na parlamentarni žanr. Priznanja zastupnika (Yemm, Hall) i premijera (Jetten) jesu *dokument o uporabi*, ali se odnose samo na vlastite tekstove; opseg pojave ostaje procjena.

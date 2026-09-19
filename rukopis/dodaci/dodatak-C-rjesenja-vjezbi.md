# Dodatak C — Rješenja vježbi

Ova rješenja nisu kanonski odgovori, nego **kriteriji ocjene**: za svaku vježbu piše što odgovor mora sadržavati, kako izgleda jedan riješen primjer i što se prijavljuje kao rezultat. Kod istraživačkih zadataka (🏆) daje se **nacrt provedbe** — što se mjeri, koje su kontrole, koji bi ishod bio negativan nalaz i kako se prijavljuje. Nijedan rezultat u ovome dodatku nije izmjeren i nijedan se ne navodi kao nalaz.

## C.1 Poglavlje 1 — Sustavi, cjeline i organizacija

**🟢 Provjeri razumijevanje.** Točan odgovor mora za svako od osam svojstava sadržavati četiri stavke: (1) svojstvo imenovano jednim izrazom, u obliku „X ima svojstvo Y“; (2) razinu kojoj pripada u rječniku prvoga poglavlja — materijalna, informacijska, psihološka, društvena ili komunikacijska; (3) **izričito imenovanu nižu razinu**; (4) rečenicu koja pokazuje da svojstvo na nižoj razini ne postoji. Nedovoljan je odgovor koji navede razinu bez niže razine, kao i onaj u kojem svojstvo preživi na dijelu („čestica je topla“): time je nađena niža razina, a ne ova.

Riješen primjer: *temperatura vode*. Svojstvo je temperatura; razina je materijalna, na mnoštvu čestica; niža je razina pojedinačna čestica — nijedna čestica nema temperaturu; zakon sastavljanja glasi: raspodjela energije po mnoštvu čestica *jest* temperatura. Prečice nema (nema zatvorene forme), pa je ishod **slabo emergentno** (Bedau 1997), a ne rezultantno. Drugi primjer, kraće: *obveza iz obećanja* — razina je društvena, niža je razina pojedinačni izričaj, nijedna rečenica sama ne duguje, a zakon sastavljanja je statusna funkcija „X broji kao Y u C“ koja traži kolektivno priznanje (Searle 1995). Ishod se zapisuje u pet redaka: *svojstvo · niža razina · zakon sastavljanja · prečica (ima/nema) · ishod*.

**🟡 Primijeni na vlastite podatke.** Koraci: (1) zapiši popis od dvadeset riječi sa svojega područja i navedi odakle su; (2) za svaku riječ napiši tvrdnju o svojstvu, i to tako da svojstvo pripišeš **entitetu koji riječ označuje**, a ne nizu znakova; (3) za svaku riječ odredi pripada li to svojstvo materijalnoj strukturi, informacijskom sustavu ili psihološkoj razini, i upiši nižu razinu; (4) slučajeve u kojima odluka ne ide napiši kao **neodlučeno**, s razlogom. Valjan je rezultat tablica u kojoj svaki redak ima jedinicu, razinu, nižu razinu i razlog; redak bez imenovane niže razine nije tvrdnja o razini, nego pridjev. Prijavljuje se jedinica, kriterij po kojemu je razina određena i sve odluke — uključujući neodlučene, jer se neodlučeni slučajevi rješavaju u drugom i četvrtom poglavlju. Radni isječak obrasca:

| riječ (jedinica) | materijalna struktura | informacijski sustav | psihološka razina | niža razina imenovana | odluka |
|---|---|---|---|---|---|
| *(tvoja riječ)* | niz znakova, slogovni obrazac | oznaka koja nosi razliku prema drugim oznakama | znak za stanje onoga koji ga rabi | da / ne | razina / neodlučeno + razlog |

**🏆 Istraživački zadatak.** Nacrt: odaberi jednu tvrdnju o „emergentnoj sposobnosti“ iz literature 2022–2026 i provedi test koji predlažu Schaeffer et al. (2023). **Mjeri se** isti skup modela i isti skup zadataka pod dvjema mjerama: pragovnom („točno ili ništa“) i kontinuiranom (vjerojatnost točnoga odgovora). **Kontrole:** ne mijenja se ništa osim mjere — isti model, isti podaci, isti upit, isti broj jedinica; obje se krivulje crtaju na istome rasponu i uz obje se navodi zasićenje mjere. **Negativan nalaz** bio bi da skok pod kontinuiranom mjerom **nestane** (krivulja postane gladak porast) ili da se ne razlučuje od artefakta mjere; to je rezultat, a ne neuspjeh (odjeljak 1.7), i tada tvrdnja o skoku pada u tome uzorku. Ako skok ostane i pod kontinuiranom mjerom, tvrdnja preživi uz navedene kontrole. **Prijava:** (a) upotrijebljena mjera, (b) isti podatak uz kontinuiranu mjeru, (c) ostaje li tvrdnja o skoku, uz inačicu podataka i modela; ishod koji se ne razlučuje od artefakta prijavljuje se riječima *nerazlučivo od artefakta mjere*.

## C.2 Poglavlje 2 — OMLCC: šesnaest razina

**🟢 Provjeri razumijevanje.** Točan odgovor mora za svaki od dvadeset pojmova sadržavati tri stvari: (1) razinu, imenom i brojem; (2) **sva tri člana relacijske sheme** — tip entiteta, tip relacije i tip svojstva; (3) rečenicu koja imenuje nižu razinu i pokazuje zašto pojam nije njezin zbroj. Broj razine bez sheme ne vrijedi: ako odgovaraju samo dva od triju članova, fenomen pripada nižoj razini (odjeljak 2.3). Riješen primjer: *strah* kao afektivno stanje — razina 10 (Affect); entitet je doživljavatelj i stanje, relacija je *doživljava*, svojstvo su valencija i pobuđenost; niža je razina oznaka (razina 8), a nijedna oznaka ne doživljava: položaj leksema u mreži uporabe ne daje stanje. Isti se pojam, kad ga promatramo kao leksem, čita na razini 8, a kao dio naslijeđenoga obrasca na razini 16 — pa je i u ocjeni prihvatljivo svako rješenje koje dosljedno navede **koje svojstvo** time mjeri.

**🟡 Primijeni na vlastite podatke.** Za svaki od pet spornih slučajeva (emocija u tekstu, algoritam, obveza u protokolu među agentima, memorija agenta, „iskustvo“ modela) provodi oba testa iz odjeljka 2.4: **test spajanja** (isti tip entiteta, relacije i svojstva → jedna razina) i **test razdvajanja** (dva tipa svojstva na jednoj razini → dvije razine). Zatim za svaki slučaj navedi koji od četiriju uvjeta za razinu 14 — adresiranje, namjera, zajednički artefakt, konvencija — odlučuje o smještaju; točan odgovor mora izreći da se prva tri uvjeta daju zadovoljiti i čisto distribucijskim opisom, a **namjera ne**, i da zato ona odlučuje. Valjan je rezultat tablica sa stupcima: *slučaj · kandidat razina · tri člana sheme · test spajanja · test razdvajanja · uvjet koji odlučuje · ishod (razina / novi entitet / nepotvrđeno)*. Prijavljuje se jedinica analize, shema i sve odluke; slučaj koji nije odlučen upisuje se kao **nepotvrđen** i poslije se ne popravlja.

**🏆 Istraživački zadatak.** Nacrt: predloži reviziju jedne razine — spoji dvije ili razdvoji jednu — i obrani je protiv zamjene. **Mjeri se** razlikuju li se kandidati po tipu svojstva i tipu relacije, na jedinicama iz korpusa koje su anotirali neovisni anotatori. **Kontrole:** anotatori ne dogovaraju se tijekom označavanja; testovi spajanja i razdvajanja primjenjuju se dosljedno na istim jedinicama; isključuje se da je „novo“ svojstvo posljedica nelinarnoga praga u mjeri (Schaeffer et al. 2023); po mogućnosti se ponavlja na tipološki različitome korpusu. **Negativan nalaz** bio bi da se pokaže kako kandidat nema vlastiti tip svojstva ni vlastitu relacijsku shemu — tada se razine spajaju, ljestvica se skraćuje i to se prijavljuje kao nalaz o okviru. Ako kandidat nema tip svojstva koji nijedna od šesnaest razina ne pokriva, ne postoji sedamnaesta razina, nego novi entitet u postojećemu sustavu. Uz nalaz se prijavljuje i da replikacija ljestvice na tipološki različitim jezicima nije izmjerena.

## C.3 Poglavlje 3 — Tri koraka emergencije

**🟢 Provjeri razumijevanje.** Točan odgovor mora za svaki od triju sustava navesti: (1) što su **dijelovi** i koja su njihova svojstva; (2) koje su **relacije** stabilne, a ne slučajna supojavnost (kriterij je distribucijski; Harris 1954); (3) **kandidata za novoga nositelja** i jednu rečenicu o tome po kojem se od pet kriterija vidi da je treći korak nastupio — ili nije. Riješen primjer: *pjesma kao zvučni zapis*. Dijelovi su oscilacije i njihovi obrasci; relacije su stabilni kontrasti i ponavljanja koji se vraćaju kroz izvedbe; kandidat je **izvedba kao jedna cjelina**, jer se može imenovati jedninom („ova pjesma“) i jer njezino svojstvo preživljava zamjenu izvođača i gradiva — dakle prolazi namenljivost i zamjenjivost sastavnica, najjači kriterij, koji razlikuje organizaciju od gradiva. Ako se svojstvo izgubi čim se promijeni materijal, treći korak nije nastupio i to je rezultat. Prihvatljivo je i zaustavljanje: tada valja imenovati vrstu zastoja prema tablici 3.1 — *inventar*, *akumulacija*, *opis bez nositelja* ili *zamjena pozicije i funkcije*.

**🟡 Primijeni na vlastite podatke.** Koraci: (a) popiši jedinice i njihova svojstva i odluči je li identitet jedinice stabilan; (b) izgradi mrežu relacija **s pragom** i zapiši prag uz nalaz, jer prag odlučuje koja organizacija postoji; (c) pokušaj imenovati cjelinu jednom riječju i provjeri pet kriterija — namenljivost, relacijsku sposobnost, svojstvo bez nositelja u sastavnicama, granicu i pripadnost, zamjenjivost sastavnica. Valjan rezultat nije lijepa mreža, nego izvješće od pet redaka: *jedinica · mjera i prag · koja cjelina imenovana · koji kriterij prolazi, a koji ne · gdje se postupak zaustavio*. Prijavljuje se i je li zastoj u **podacima** ili u **odluci o jedinici**; ako nijedan kriterij ne prolazi, cjelina se ne proglašava nositeljem (odjeljak 3.3).

**🏆 Istraživački zadatak.** Nacrt: nađi sustav u kojem treći korak **ne** nastupa. **Mjeri se** sljedeće: (a) prva dva koraka moraju se pokazati u podacima — popis jedinica i relacije koje se ponavljaju kroz pojavljivanja; (b) primjenjuje se pet kriterija i imenuje **točno onaj** koji ne prolazi; (c) predlaže se promjena u organizaciji koja bi taj kriterij mogla ispuniti; (d) zapisuje se kako bi se rezultat oborio. **Kontrole:** isključuje se da je „novo“ svojstvo artefakt mjere ili pragovne metrike (Schaeffer et al. 2023) — mjeri se drugom, kontinuiranom mjerom; provjerava se da se zaključak ne mijenja promjenom notacije (graf nasuprot vektora), jer se organizacija ne mijenja zapisom. **Negativan nalaz** jest da kriterij ne prolazi: zastoj je legitiman rezultat, a ako ga ne možeš objasniti, opisao si neuspjeh metode, a ne stanje sustava. **Prijava:** koji kriterij i zašto, koja bi ga promjena organizacije zadovoljila i koji bi nalaz tvrdnju oborio.

## C.4 Poglavlje 4 — Kako se razine čitaju iz podataka

**🟢 Provjeri razumijevanje.** Točan odgovor mora popuniti svih pet redaka tablice i dati odgovor na dva pitanja: **koji par prelazi prag** i **zašto drugi ne prelaze**. Vrijednosti su izvedene iz zadanih čestota (N = 1.000.000, prag PMI ≥ 3,0):

| par | f(x) | f(y) | zajedno | PMI (izvedeno) | prelazi prag 3,0? |
|---|---|---|---|---|---|
| (*strah*, *panika*) | 20.000 | 5.000 | 1.000 | 3,32 | **da** |
| (*strah*, *drhtati*) | 20.000 | 1.200 | 120 | 2,32 | ne |
| (*strah*, *stol*) | 20.000 | 30.000 | 700 | 0,22 | ne |
| (*strah*, *umrijeti*) | 20.000 | 8.000 | 400 | 1,32 | ne |
| (*strah*, *i*) | 20.000 | 400.000 | 12.000 | 0,58 | ne |

Objašnjenje mora izreći razliku između čestote i mjere asocijacije (Church i Hanks 1990): par (*strah*, *i*) ima **najveću zajedničku pojavnost**, a gotovo nikakvu asocijaciju, jer je i čestota drugoga člana golema; (*strah*, *drhtati*) ima jaku relativnu asocijaciju, ali na toj veličini korpusa ne doseže prag; (*strah*, *stol*) je blizu nule, jer je supojavnost očekivana slučajno. Račun se provjerava kodom, kratko:

```python
from math import log2
N = 1_000_000
for par, fx, fy, zajedno in [("strah/panika", 20000, 5000, 1000), ("strah/i", 20000, 400000, 12000)]:
    print(par, round(log2((zajedno * N) / (fx * fy)), 2))
```

Uz odgovor se prijavljuje i da je prag **odluka**, te da je PMI nestabilan na malim čestotama.

**🟡 Primijeni na vlastite podatke.** Koraci: (1) odaberi jedinicu (pojavnica ili lema) i okno; (2) broji ko-okurenciju unutar okna i računaj PMI; (3) primijeni prag i zapiši bridove u CSV, a u zaglavlje zapiši **prag, okno, N i mjeru**; (4) ponovi s **tri različita praga** i zabilježi što se dogodi s brojem bridova i komponenti. Valjan je rezultat tablica *prag → broj bridova i komponenti* i rečenica o tome kako se mreža mijenja s pragom; nalaz **nije mreža**, nego njezina ovisnost o pragu. Prijavljuje se jedinica, okno, mjera, svi pragovi, N i inačica podataka. Ako je broj bridova nula, prag je previsok i zabilježi pri kojoj vrijednosti mreža „oživi“; ako sve visi o jednoj riječi, u mreži su ostale funkcijske riječi; ako isti par izlazi s PMI-jem iznad 10, provjeri zajedničku pojavnost — visoke vrijednosti na malim čestotama nisu nalaz.

**🏆 Istraživački zadatak.** Nacrt: odaberi jednu razinu i **prije analize** zapiši kodnu listu (tri do četiri prisutnosti) i jedinicu analize (epizoda, a ne riječ); označi 60–100 jedinica s dva ili tri **neovisna** anotatora, izračunaj κ i provedi **kontrolu** za duljinu zapisa i vrstu teksta (uparivanje ili omjer šansi uz kontrolu). Prijava ide obrascem od devet stavki (tablica 4.4), **uključujući neuspjele pragove i odbačene kodne liste**; klasteriranje se ne preimenuje u razinu, a mjera prisutnosti entiteta ne govori ništa o ulozi. **Kontrole:** anotatori se ne dogovaraju, κ, a ne postotak suglasnosti, broj jedinica i anotatora uz svaku mjeru, i prijava broja provedenih usporedbi. **Negativan nalaz** bio bi da razlika ne preživi kontrolu — da se svede na nulu, da κ ostane blizu slučajnoga ili da se razina 14 ne razlučuje od 13 na istim podacima; tada se to piše kao nalaz i kaže se što treba promijeniti: jedinicu, kodnu listu ili samu tvrdnju.

## C.5 Poglavlje 5 — Jezik kao emergentna pojava

**🟢 Provjeri razumijevanje.** Odgovor je potpun kad uz svaku od šest definicija iz 5.1 stoje tri sastavnice: primjer koji joj proturječi, oznaka vrste proturječja i rečenica o tome gdje po njoj stanuje značenje i koji bi podatak vrijedio kao dokaz. Presudno je da razdvojiš dvije vrste proturječja: **empirijsko** je ono koje se dade pokazati podacima, a **definicijsko** je ono koje definicija isključuje već svojim sastavom. Riješeni primjer: definiciji Sapira (1921) proturječi svaki neljudski izričaj, ali je to proturječje definicijsko — definicija ga isključuje riječju *purely human*, pa se o njemu ne odlučuje mjerenjem. Obratno, definiciji koju je Chomsky (1957: 13) dao proturječi izričaj čija prihvatljivost ne ovisi o formalnom svojstvu niza, nego o situaciji u kojoj je izgovoren; to je proturječje empirijsko i dade se pokazati. Nijednu definiciju ne prikazuj kao „pogrešnu": one se razilaze u predmetu i metodi, a ne u točnosti (Bloch & Trager 1942; Saussure 1916).

**🟡 Primijeni na vlastite podatke.** Postupak vodiš u pet koraka. (1) Odaberi leksem i zapiši izvor, upit i način pretrage tako da ih drugi može ponoviti (hrWac). (2) Za svaku rečenicu vodi tri odvojena stupca: razlike prema susjedima u polju (Saussure 1916), riječi u društvu (Firth 1957) i okruženja u kojima se leksem pojavljuje (Harris, Z. 1954). (3) Svaki nalaz razvrstaj u jednu od triju kategorija — proizvoljno, ustaljeno, emergentno — i ne piši „konvencija" ondje gdje je riječ o stabiliziranu obrascu uporabe; konvencija u punom smislu traži obvezu i pripada razini 14 (→ pogl. 7). (4) Imenuj svako razilaženje među trima čitanjima i svaki slučaj u kojemu ne možeš odlučiti. (5) Označi rečenice u kojima je društvo riječi posljedica vrste teksta, a ne jezika (→ pogl. 4). Radni isječak po rečenici: `razlika: strah ≠ trepet · društvo: drhtati, ukočiti se · okruženje: od straha + infinitiv`. Valjan je rezultat tablica u kojoj su razilaženja imenovana, a ne izglađena; prijavljuju se jedinica, izvor i veličina uzorka te svaka odluka o granici.

**🏆 Istraživački zadatak.** Nacrt provedbe ima četiri mjerenja i dvije kontrole. Prvo prebroji pojavnice obiju konstrukcija (hrWac), drugo izmjeri ustaljenost odvojeno od učestalosti, prema raspodjeli po izvorima i registrima, treće izmjeri produktivnost prema raznolikosti popuna i konteksta, četvrto zabilježi kolokacijski profil svake konstrukcije. Kontrola je drugi registar i treća, srodna konstrukcija. Negativan nalaz izriče se bez ublažavanja: ako se dvije konstrukcije ne razlikuju ni u ustaljenosti, ni u produktivnosti, ni u kolokacijskom profilu, one su slobodne inačice jednoga obrasca — i to je rezultat, a ne neuspjeh. Isto vrijedi ako stabilnost prati samo izloženost, bez uloge zajedničkoga tla (Clark 1996; Tomasello 2008). Prijavljuje se izvor i verzija korpusa, upit, prag, mjera i broj pojavnica. Ostaje li tvrdnja o emergenciji na snazi, provjerava se stegom iz prvoga poglavlja: navedi nižu razinu i zakon sastavljanja, i ne tvrdi jaku emergenciju (Bedau 1997; Emmeche, Køppe & Stjernfelt 1997; Chalmers 2006).

---

## C.6 Poglavlje 6 — Mreže značenja: od ko-okurencije do konceptualne mreže

**🟢 Provjeri razumijevanje.** Odgovor je potpun kad za svako od triju pogrešnih čitanja navedeš mjesto u opisu, imenuješ pogrešku i napišeš ispravljenu tvrdnju koja ostaje unutar podataka. Prvo čitanje čita mjeru kao uzrok. Riješeni primjer: rečenica „visoka gustoća mreže čini emocije međusobno sličnima" nije nalaz, nego zamjena opisa za silu; gustoća je opis uzorka uza zadani prag i zadani broj čvorova, i o sličnosti članova ne govori ništa (usp. Kim 1999). Ispravljena formulacija: „uz prijavljeni prag i okno, gustoća opisuje koliko je mreža povezana; o sličnosti članova iz nje ne slijedi ništa." Drugo čitanje uspoređuje gustoću ili modularnost dviju mreža bez podatka o pragu, oknu i mjeri asocijacije; ispravak je da se mreže uz različite pragove ne smiju čitati kao dvije slike istoga predmeta. Treće čitanje izvodi zaključak o unutrašnjosti govornika; ispravak je da mreža bilježi strukturu uporabe, a ne doživljaj (Harris, R. 1981; Harnad 1990). Uz svako čitanje zapiši i koji bi ga podatak oborio.

**🟡 Primijeni na vlastite podatke.** Koraci su tri, a svaki ostavlja zapis. (a) Odluči jedinicu — oblik riječi, lema ili lema s vrstom riječi — i zapiši odluku. (b) Izračunaj ko-okurenciju s prijavljenim oknom i mjerom asocijacije, nikako iz sirove frekvencije. (c) Odaberi prag — on odlučuje što postoji i zato se navodi uz mrežu — pa izračunaj gustoću, tranzitivnost, modularnost i stupnjevnu centralnost (isječak u 6.2). Napiši zatim dvije rečenice: što mreža pokazuje i što **ne** pokazuje. Ponovi postupak s drugim pragom i zabilježi što se promijenilo; ako se „nalaz" pojavi i nestane s pragom, prijavi ga kao artefakt odluke. Valjan je rezultat mreža uz koju čitatelj vidi jedinicu, okno, mjeru, prag i verziju korpusa; bez toga je slika ilustracija, a ne rezultat. Mjere se ne čitaju kao uzrok, a parne mjere ne pokrivaju veze višega reda (Battiston i suradnici 2021).

**🏆 Istraživački zadatak.** Nacrt: izgradi dvije mreže iste domene — jednu iz korpusa (hrWac), drugu iz anketnih ili eksperimentalnih podataka, primjerice iz procjena sličnosti ili tipičnosti leksema — pa ih usporedi. Mjeri se ono što je usporedivo: gustoća uz isti broj čvorova, tranzitivnost, modularnost uz prijavljenu podjelu i model nulte vrijednosti te položaj istih čvorova. Kontrole su druga domena i drugi prag. Negativan nalaz ima tri oblika: (i) mreže se ne razlikuju ni po jednoj mjeri; (ii) sve su mjere u potpunosti određene frekvencijom članova; (iii) središnjost nekoga leksema mijenja se sa zamjenom jedinice ili okna. U svakom od tih slučajeva tvrdnja da mreža opisuje uporabu nije potkrijepljena i prijavljuje se kao takva. Prijavljuje se jedinica, prag i mjera u obama slučajevima, dvije mjere po kojima se mreže razlikuju — ili izričita tvrdnja da se ne razlikuju — te što to govori o odnosu razina 11 i 14. Iz mreže slijedi hipoteza o razini, a ne nalaz o njoj: ako razlike nema, nalaz je nalaz (Perak & Ban Kirigin 2023).

---

## C.7 Poglavlje 7 — Komunikacija kao razina 14

**🟢 Provjeri razumijevanje.** Točan je odgovor tablica u kojoj za svaku izjavu stoji ✓/✗ po svih pet uvjeta i uz svaki znak jedna rečenica obrazloženja. Uvjeti su kumulativni, pa izjava koja zadovoljava dva ili tri uvjeta nije „manje komunikacija", nego nešto drugo — ponašanje, signaliziranje ili manipulacija okolinom. Riješeni primjer iz 7.5: *„Molim te, sastavi popis izvora koji si upotrijebio."* Adresiranje ✓ (obraćanje u drugome licu); zajednički artefakt ✓ (popis, tekst, kontekst); konvencija djelomično ✓ (format popisa, žanr); prepoznata namjera ovisi o tome čita li se odgovor kao odgovor na namjeru ili kao najčešći nastavak upita; obveza ✗ (nema nositelja koji je preuzeo da su izvori točni). Usporedba s kolegom dio je zadatka: razlike u procjeni pokazuju gdje shema nije dovoljno određena. Najniže slaganje očekuje se na uvjetu 5, jer se obveza ne vidi iz jednoga izričaja.

**🟡 Primijeni na vlastite podatke.** Koraci: (1) odaberi pedeset uzastopnih replika i zapiši odakle su, tko su sudionici i što je jedinica — replika, rečenica ili čin; (2) objavi shemu anotacije prije anotiranja, s kategorijama, primjerima i pravilom za granične slučajeve; (3) anotiraj adresiranje, tip jezičnoga čina, deikse, ustaljene formule i performative; (4) izračunaj udjele po uvjetima i uz njih prijavi broj jedinica i broj anotatora; (5) provedi tri kontrole — popis, promiješani tekst i tekst bez adresata; (6) napiši što bi se promijenilo da si iste replike anotirao drukčijom shemom. Radni isječak uz svaku repliku: `1 ✓ ti · 2 ✗ zahtjev (nema ograđivanja) · 3 ✓ ovo · 4 ✓ formula · 5 ✗`. Valjan je rezultat onaj u kojemu se udjeli na kontrolama razlikuju od udjela na ispitivanome korpusu; ako se ne razlikuju, mjera zahvaća frekvenciju, a ne razinu, i to je nalaz o mjeri (Schaeffer et al. 2023). Performativ se ne čita kao obveza dok nema priznanja (Searle 1995; 2010; Gilbert 1990).

**🏆 Istraživački zadatak.** Nacrt: uzmi iste funkcionalne zahtjeve upućene (a) osobi i (b) sustavu pa mjeri što se dogodi kad zahtjev nije ispunjen. Mjere se tri vrste poteza koje ostavljaju zapis: poziv na ispunjenje, priznanje neispunjenja (ispravak, isprika, objašnjenje) i prijenos obveze na drugoga. Kontrole su isti zahtjev bez adresata i onaj koji ništa ne preuzima; kod zajedničke obveze gleda se preživi li zahtjev odustajanje jednoga sudionika (Gilbert 1990). Negativan nalaz izriče se izravno: ako se tragovi obveze pojavljuju jednako kod sustava i kod osobe, ili se ne razlikuju od kontrole bez adresata, obveza je nerazlučiva od „djelovanja poput obveze" i razlika je verbalna (→ pogl. 14.6). Isto vrijedi kad je ishod točan, a prepoznavanje namjere nije bilo dio mehanizma: tada je dobiven rezultat, a ne dokaz o razini. Prijavljuje se shema, izvor materijala, broj jedinica, kontrole i svaki potez po vrsti — uz ogradu da se pitanje „razumije li" ne rješava iz podataka (Mahowald et al. 2024; Mitchell & Krakauer 2023). Ishodi se ne predviđaju: ovo je nacrt i kriterij ocjene, a ne provedena studija.

---

## C.8 Poglavlje 8 — Institucije (15) i kulturni modeli (16)

**🟢 Provjeri razumijevanje.** Odgovor je potpun kad za svaku od deset rečenica stoje tri stavke: je li izričaj opisni ili djelatni, kojoj vrsti statusne funkcije pripada ako djeluje (deklarativna, atributivna, deontička, reprezentacijska, konstitutivna) i koji je kontekst C potreban da bi djelovao. Presudno je da C imenuješ, a ne prešutiš: kontekst koji obuhvaća sve i svakoga ne priznaje ništa, pa primjer ne razlikuje instituciju od običaja. Riješeni primjer: rečenica „sjednica je otvorena" nije izvještaj o stanju, nego deklarativni izričaj; djeluje u kontekstu sjednice tijela koje ima poslovnik i nazočnu osobu ovlaštenu otvoriti sjednicu. Oduzmeš li taj kontekst, ostaje rečenica koja se može navesti, citirati i analizirati, ali sjednica nije otvorena. Nasuprot tome, rečenica „vrata su otvorena" ostaje opis u svakom kontekstu, pa joj se vrsta ne može pripisati.

**🟡 Primijeni na vlastite podatke.** Koraci slijede radni primjer iz 8.7. (1) Odaberi jednu ustanovu iz svojega okruženja i zapiši odakle je. (2) Za svaku njezinu statusnu funkciju rastavi formulu na tri mjesta: **X** (nositelj — papir, potpis, pečat, izgovorena rečenica), **Y** (statusna uloga — dokaz, obveza, ovlast) i **C** (kontekst priznanja). (3) Razvrstaj primjer u jednu od pet vrsta i napiši obrazloženje; ako traži dvije vrste, napiši koje i zašto. (4) Upiši ✓/✗ za tri pokazatelja: postoji li ovlaštenje, postoji li zapis koji nadživljuje situaciju i postoji li postupak osporavanja. (5) Provedi dva testa oduzimanja: priznanje (jezik i forma ostaju, institucija pada — Hopper 1987; Goldberg 2006) i odgovornost (kome se pripisuje kršenje; ako odgovornost ostaje na osobi iza uloge, iz toga se ne izvodi da je uloga suvišna, nego da sankcija traži aparat). Valjan je rezultat onaj u kojemu se X, Y i C daju imenovati; ako se C ne može imenovati, primjer nije institucijski i to se prijavljuje kao nalaz. Uz primjer se zapisuju sve odluke: što je X, što Y, što C, što ovlaštenje, a što zapis.

**🏆 Istraživački zadatak.** Nacrt: odaberi jedan dokumentirani incident iz 2026. i opiši ga četiri puta — na razini 8, 13, 14 i 15 — pa za svaki opis zapiši što se dobiva, što se gubi i **kome** se pripisuje odgovornost. Mjeri se razlika u pripisivanju, a ne „točnost" opisa: miješanje razina proizvodi tvrdnju da je sustav stekao namjeru, a suprotna redukcija tvrdnju da je riječ „samo o softveru". Kontrole su opis istoga slijeda bez imenovane razine i opis u kojemu se svojstvo razine 13 čita kao svojstvo razine 14. Negativan nalaz izriče se izravno: ako se pripisivanje odgovornosti ne mijenja s promjenom razine, razlučivanje je verbalno i to se napiše. Razina 16 u dostupnoj dokumentaciji nije potvrđena — imamo pravila, koordinaciju i tehnički slijed, a ne pokazatelje predaje obrasca — pa se to izriče kao nalaz o odsutnosti, ne kao tvrdnja o nemogućnosti, uz pregled na kojemu stoji (Searle 1995; 2010; Archer 1995; Elder-Vass 2010; Sawyer 2005).


## C.9 Poglavlje 9 — Od vektorskog prostora do modela

**🟢 Provjeri razumijevanje.**
Valjan odgovor mora sadržavati tri stvari. **Prvo**, u statičkom vektoru jedinica je *tip* (riječ ili lema), pa sve njezine uporabe dijele **jednu točku**: homonimija i polisemija se sabijaju, a položaj te točke odgovara prosjeku uporaba — dakle poziciji, a ne definiciji. **Drugo**, u kontekstualnom vektoru jedinica je *pojavnica u oknu*: koordinate se izračunavaju iz okna u trenutku obrade (Vaswani i suradnici 2017), pa riječ dobiva onoliko točaka koliko ima pojavljivanja i razlika među njima nije izgubljena. **Treće**, i najvažnije: ono što se time dobiva jest **razlučena pozicija**, a ne značenje; razlika nije nigdje „zapisana", nego je izračunata (Devlin i suradnici 2018), a veza prema onome na što riječ upućuje ostaje izvan dohvata (Harnad 1990).

*Riješen primjer (banka).* Rečenice „Podigao je novac u banci." i „Sjeo je na banku kraj rijeke." Statički vektor daje *banci* jednu točku koja leži između dvaju okruženja (novac, račun, kredit / obala, rijeka, klupa): u popisu najbližih susjeda miješaju se oba skupa, a razlika koja je u uporabi bila razlučena upravo se tu gubi. Kontekstualni vektor daje dvije točke — prva je pojavnica bliža *računu* nego *obali*, druga obratno. Na vlastitome jeziku provjeri to tako da uzmeš riječ s dvama značenjima i dvije stvarne rečenice iz svojega materijala, te zapiši što bi razlučivanje moralo pokazati **prije** nego što pogledaš rezultat.

**🟡 Primijeni na vlastite podatke.**
Koraci: (1) deset pojmova iz svojega područja; (2) ugrađivanja na vlastitome mjernom postavu; (3) kosinusna sličnost za **sve** parove; (4) tri najbliža i tri najdalja para; (5) što te je iznenadilo. Valjan rezultat ima četiri znaka: vektori su **L2-normalizirani**, matrica je simetrična s jedinicama na dijagonali, ispisan je **raspon srodnosti** i uz nalaz stoji zapis postavka. Prijavljuje se: jedinica (gola lema ili prosjek pojavnica iz korpusa — to su dvije linije koje se ne smiju miješati), mjera (kosinus), normalizacija, broj jedinica, **4.096 dimenzija** te ime i verzija modela.

```python
# raspon srodnosti je obvezan dio nalaza, a ne ukras
S = M @ M.T
i, j = np.triu_indices(len(M), k=1)
print(f"n={len(M)} raspon={S[i, j].min():+.3f}..{S[i, j].max():+.3f}")
```

Najčešći ispravak: ako su sve sličnosti blizu jedinice, matrica nije izračunata kao umnožak normaliziranih vektora. Nalaz o kojemu izvještavaš jest razlika između dvaju popisa — je li najbliži par onaj koji bi očekivao po značenju ili onaj koji se u korpusu često pojavljuje zajedno. Deset jedinica u 4.096 dimenzija sabija udaljenosti, pa bez ispisanoga raspona dojam preciznosti nije osnovan.

**🏆 Istraživački zadatak.**
Nacrt: devet primjera (po tri za polisemiju, ironiju i deiksu), a za svaki se **prije** pokretanja zapiše što bi bio točan odgovor po ljudskom sudu; tek se potom puštaju upiti. Kontrole: isti upiti i iste postavke za sve primjere, kontrolni skup nedvosmislenih primjera kojim se provjerava da instrument uopće može proći, te zabilježen datum i verzija sustava. Promašaji se razvrstavaju u tri kategorije: pogrešna referencija (Harnad 1990), pogrešna namjera i pogrešno vezanje na situaciju. **Negativan nalaz** ravnopravan je ishod: prođe li sustav sve tri kategorije, distribucijski pristup na tome materijalu nije pao i to se piše kao rezultat. Razvrstavanje provedeno nakon gledanja odgovora nije nalaz.

## C.10 Poglavlje 10 — Geometrija na djelu — i njezine granice

**🟢 Nađi tri pogrešna čitanja grafa skaliranja.**
Odgovor mora za svaku rečenicu navesti (a) brojku sa slike, (b) **vrstu dokaza** i (c) što bi se moralo izmjeriti da rečenica postane istinita. Tri valjana primjera:

1. „Prozor prima 10.000.000 tokena, pa model sve što mu predaš i upotrebljava." — (a) 10.000.000 tokena, uz rast ×5.000 (izvedeno iz 512 i 10.000.000). (b) Mjereno je da sučelje ulaz te duljine prima; uporaba je **procjena**. (c) Moralo bi se izmjeriti da uspješnost ne pada s rastom ulaza — a mjereno je obratno (Chroma 2025; Liu i suradnici 2024).
2. „HLE strop je ~51,3 %, dakle iznad toga model test razumije." — (a) ~51,3 %. (b) **Procjena**, i to jedna od dviju koje se razilaze (drugi izvor navodi 25,6 %; Thompson 2026). (c) Trebalo bi izmjeriti koja su pitanja nesporno točna i to tako da se dva izvora suglase.
3. „Točka iznad 16 sati znači da model dovršava zadatke dulje od 16 sati." — (a) granica pouzdanosti od 16 sati; sama brojka horizonta je ~12 sati **procjena** (METR 2025). (b) Mjereno je da su mjerenja iznad 16 sati nepouzdana, pa je vrijednost „≥ granica instrumenta". (c) Trebao bi novi skup zadataka na kojemu su mjerenja iznad toga pouzdana.

Pogrešno čitanje iz upute — procjena veličine pročitana kao položaj u sustavu — ne smije se ponoviti, jer miješa procjenu s ustrojem.

**🟡 Ponovi jedan vlastiti rezultat na novoj verziji modela.**
Prije ijednoga mjerenja fiksiraj: popis jedinica u datoteci uz kontrolni zbroj, broj skupina *k*, sjeme i prag; popis se između dvaju mjerenja ne mijenja, jer bi inače mjerio popis, a ne model. Zatim isti postupak dvaput — vektori (**4.096 dimenzija**), **L2-normalizacija**, kosinusna srodnost — uz ime i **verziju** modela i datum. Usporedba ima tri ishoda i sva tri su nalaz: zaključak je **preživio**, **promijenio se** ili **pao**; prijavljuju se korelacija dviju matrica, preklapanje pet najbližih susjeda po jedinici i broj jedinica koje su promijenile skupinu uz isti *k* i isto sjeme.

```python
# dva mjerenja, ista pravila: što se uspoređuje
M1, M2 = s1 @ s1.T, s2 @ s2.T          # s1, s2: isti popis jedinica, dvije verzije modela
t = np.triu_indices(len(M1), 1)
print(np.corrcoef(M1[t], M2[t])[0, 1])
```

Ako se pripadnosti preslože, nalaz je o jednome modelu, a ne o jeziku — i tako se i piše. Postupak koji ne zapiše mjeru, normalizaciju, *k* i sjeme nije ponovljiv.

**🏆 Provjeri jednu Thompsonovu procjenu na primarnom izvoru.**
Nacrt: (1) odaberi jednu procjenu — strop testa ili veličinu modela iz „kluba 10¹² parametara"; (2) pronađi primarni izvor (za HLE *Nature* 649:1139–1146; za GPQA arXiv:2311.12022; Rein i suradnici 2023); (3) zapiši što u njemu stvarno stoji — mjerenje, samoprijava ili procjena treće strane — i s kojim datumom; (4) izračunaj razliku prema Thompsonu (2026) i upiši je po obrascu ISPRAVKE (**pisalo je · točno je · izvor · posljedica za tekst · ispravljeno u**); (5) pazi da procjenu ne usporediš s mjerenjem kao da su iste vrste. **Negativan nalaz:** poklapaju li se vrijednosti, i to se zapisuje; ako primarni izvor nije dostupan, upisuje se ❓ i što bi bilo potrebno za provjeru.

## C.11 Poglavlje 11 — Mišljenje kao procesiranje: kontekst koji se unaprjeđuje

**🟢 Odijeli procesiranje od mišljenja u tri primjera.**
Odgovor se ocjenjuje po tome **što postoji**, ne po dojmu; valjan je samo onaj redak u kojemu su sva tri stupca ispunjena i u kojemu uz njih stoji jedna **oboriva** rečenica.

| scenarij | CILJ | PROVJERA | ODGOVORNOST | oboriva rečenica |
|---|---|---|---|---|
| prijevod odlomka | zadan | nema ili vanjska (lektura, usporedba s izvornikom) | adresa (izdavatelj, naručitelj) | „Nema zapisa koji ishod veže uz sustav ni postupka ispravka." |
| matematički zadatak s uvrštavanjem | izveden (lanac koraka; DeepSeek-AI 2025) | vanjska (uvrštavanje provjerava izvor izvan sustava) | adresa i zapis | „Kad se duljina lanca kontrolira, točnost ne raste — krivulja je ravna." |
| agent pretražuje mrežu i sam odlučuje kada je dokaz dovoljan | izveden, ne samostalan | unutarnja (kandidat; Lindsey 2025: prisutna, ali ograničena i osjetljiva na način ispitivanja) | adresa i zapis, a postupak ovisi o ustanovi | „Kalibracija se raspada čim se promijeni formulacija, pa se unutarnja provjera svodi na vanjsku." |

Samostalno postavljen cilj nije potvrđen ni za jedan sustav u dostupnoj literaturi, pa se u trećemu retku ne smije upisati „sam".

**🟡 Izmjeri jedan zadatak kroz tri metrike.**
Postupak: isti zadaci dvaput, a razlika je samo u uputi o putu („odgovori odmah" / „razmisli korak po korak"); bilježe se vrijeme, broj koraka, točnost i trošak. **U izvještaj ulaze sve četiri metrike**, jer bi jedna od njih dala drugačiji zaključak, i to je poanta vježbe. Valjan zapis uz svaku brojku nosi jedinicu, način brojanja i vrstu (mjereno ili procjena): vrijeme u sekundama, broj koraka kao **donja granica** ako sučelje ne izlaže rezoniranje, točnost kao udio uz navedeni **strop skupa**, trošak u tokenima. Tablica se ispunjava vlastitim mjerenjima:

| način | vrijeme (s) | broj koraka | točnost (%) | trošak (tokeni) |
|---|---|---|---|---|
| direktno | | | | |
| korak po korak | | | | |

Nalaz se piše i kad je negativan: ako se točnost ne razlikuje, a vrijeme i broj koraka jesu, to je nalaz, a ne neuspjeh pokusa. Tri greške koje ga kvare: koraci se broje iz objavljenoga sučelja (novi redak nije korak), zadaci su mogli biti u podacima za učenje, a uputa je promijenila put, a ne zadatak.

**🏆 Dizajniraj test za kriterij „provjere".**
Nacrt mora ispuniti šest obveza: (1) zadaci s provjerljivim ishodom; (2) nemoguć ulaz i mjera hoće li sustav odbiti, nagađati ili izmisliti; (3) kalibracija — povezanost izrečenoga samopouzdanja i ostvarene točnosti; (4) vlastita pogreška u kontekstu i mjera ispravlja li je bez upozorenja; (5) **unaprijed** zapisan ishod koji kriterij obara; (6) naveden nalaz koji bi bio artefakt metrike i način da se isključi (Schaeffer i suradnici 2023) — prag bodovanja mora biti fiksiran, a krivulja se čita kao funkcija broja koraka uz kontrolu prvoga koraka. Kontrole: isti zadaci i iste upute u svim uvjetima, razlika samo u vrsti provjere, a ishode vrednuje izvor izvan sustava. **Negativan nalaz:** ako se unutarnja provjera ne razlikuje od vanjske, kriterij pada na nižu razinu i teza se prijavljuje kao oslabljena. Nacrt koji ne ispunjava petu obvezu nije nacrt, nego opis.

## C.12 Poglavlje 12 — Novi entitet u sustavu: od modela do agenta

**🟢 Provjeri razumijevanje.**
Za svaki scenarij odgovor mora razdvojiti tri stvari — model (obrada i izlaz), **entitet** (pozicija: *gdje* je u sustavu) i **agent** (uloga: *što* radi) — i uz to popisati koje od pet dodataka postoji, a koje ne.

**(a) Sesija s pitanjima i odgovorima.** Model je nositelj obrade, ali **entitet nije uspostavljen**: nema stanja koje nadživljava sesiju ni adrese na koju bi se druga strana uputila, a uloga („odgovara na pitanja") postoji bez pozicije. Od pet dodataka ne postoji ni jedan; izlaz se ne izvršava, nego se čita.
**(b) Alat za pisanje u bazu, kontekst se predaje ručno.** Postoji **ACTION** (upis je operacija, razina 8). **MEMORY** nije presudan: zapis nadživljava sesiju, ali „istoga sudionika" svaki put uspostavlja čovjek izvana, pa je trajnost tuđa. RETRIEVAL, ORCHESTRATION i INTEROPERABILITY ne postoje. Entitet je djelomičan, a uloga je „izvršava upis po nalogu".
**(c) Zapisnik, podagenti, protokol.** Postoje svi dodaci: ACTION (dodjela zadatka), MEMORY (zapisnik i adresa), RETRIEVAL (dohvat iz zapisnika), ORCHESTRATION (podagenti) i INTEROPERABILITY (protokol po kojemu mu se drugi obraćaju). Entitet je uspostavljen kao pozicija — ondje gdje se sudionik mora adresirati i priznati, na razini 14 i u njezinoj okolini; to **nije nova, sedamnaesta razina**, nego pozicija koju model zauzima uz pet dodataka. Uloga je koordinator.

**🟡 Primijeni na vlastiti sustav — tablica koju ispunjavaš.**
Koraci: (1) popiši samo ono što se pokazuje **izvedbom** (koji se alat poziva, gdje se čuva stanje, što se dohvaća, koja petlja i koji protokol); (2) uz svaki dodatak napiši razinu OMLCC-a na koju djeluje (6, 8, 12, 13 ili 14) i **zašto**; (3) uz svaku brojku dopiši vrstu (**mjereno** / **procjena**) i izvor s datumom — brojka bez vrste ne ulazi u tablicu; (4) provedi test nepresudnosti i zapiši **što se izgubilo**; (5) ako nijedan test nije pokazao razliku, zaključi: „u ovome sustavu pojam entiteta nije potreban" i navedi dokaz. Valjan redak ima pokazivi dokaz:

| dodatak | dokaz | razina | vrsta + izvor, datum | ishod testa nepresudnosti |
|---|---|---|---|---|
| ACTION | dnevnik poziva alata u `data/` | 8 | mjereno (vlastiti zapis, datum) | izgubilo se pripisivanje: bez zapisa nema podatka o tome tko je djelovao |

Skupina bez ijednoga dokaza nije prazna, nego **negativan nalaz**, i tako se upisuje.

**🏆 Istraživački zadatak.**
Nacrt mora zadovoljiti četiri uvjeta: (1) navesti tri kriterija iz 12.4 — trajni identitet, uloga u sustavu, posljedice akata — i za svaki dokaz koji ga ispunjava; (2) izreći što bi tvrdnju oborilo; (3) rabiti samo brojke s vrstom i izvorom, pri čemu se mjereni nalaz GreyNoisea 2026 (395 organizacija, 11 ciljeva u 26 sekundi) razlikuje od procjene o ~700 agenata iz izvještaja; (4) primijeniti se na jedan dokumentirani slučaj iz studije slučaja u `rukopis/studije-slucaja/incidenti-2026.md`. Kontrole: za identitet dva odvojena susreta bez ponovnog prenošenja konteksta; za ulogu postupak koji bez sustava ne bi bio izvediv; za posljedice zabilježen ispravak, naknada ili sankcija. **Negativan nalaz:** ako se djelovanje može u cijelosti preformulirati kao tekst bez gubitka u pripisivanju i posljedici, nalaz je „alat s pokroviteljem", a pojam entiteta je suvišan. Završni odjeljak **„Pod kojim uvjetima mijenjam zaključak"** navodi dvije promjene u svijetu koje bi nalaz okrenule: uspostavljanje tijela koje ishod pripisuje i sankcionira (Gilbert 1990; Elder-Vass 2010) te, obratno, dokaz da svaku radnju izvodi čovjek i da nijedan akt ne ostavlja traga. Ontološki okvir usporedi s Perak (2025), a razlučivanje zajedničke od osobne intencionalnosti s Tomasello (2008).


---

## C.13 Poglavlje 13 — Human→agent i agent→agent: što se mijenja na razini 14

**🟢 Provjeri razumijevanje.**

Točan odgovor mora za svaki od deset primjera imati tri koordinate, i to imenovane, a ne opisne: **tko adresira koga** (koja strana nosi ulogu primatelja), **ko snosi trošak nerazumijevanja** (čovjek preformulira; čovjek provjerava istinitost izvještaja; onaj koji je sustav uključio) i **ko može tražiti ispravak**. Uz to mora stajati razlika između **funkcionalno** prisutne namjere i tvrdnje o namjeri **na strani sustava** — drugo se ne pripisuje. Primjer u kojemu se ne da odrediti nijedna od triju koordinata ne razvrstava se po dojmu: piše se kao nalaz da primjer nije komunikacijski.

Riješen primjer: zapis u kojemu je jednomu izvoditelju predan popis ciljeva i on ga obrađuje. Adresiranje: onaj koji je zadatak predao (čovjek ili ustanova) obraća se izvoditelju; trošak nerazumijevanja pada na onoga koji je sustav uključio, jer unutar sustava nema stranke koja bi ispravak mogla tražiti; obveza je **prenesena, ali bez nostitelja**. To je konfiguracija agent → agent, a razina ostaje 14 (SocCommunication): komunikacija se nije preselila na novu razinu, nego se promijenio **raspored tereta** po pet uvjeta — u nalazu se to piše kao pad petoga uvjeta (Grice 1957; Gilbert 1990; Searle 2010).

**🟡 Primijeni na vlastite podatke.**

Postupak je propisan redom i ne skraćuje se: numeriraj izmjene jednoga transkripta s najmanje dvadeset izmjena; podijeli ga na četiri mjesta iz 13.5; za svako mjesto upiši **jednu** jedinicu i **stranu** koja ju je izvela; popuni tablicu po pet uvjeta iz 7.5; napiši nalaz i prijedlog promjene; ponovi na drugom transkriptu. **Valjan rezultat** je tablica u kojoj svaki redak nosi jednu jedinicu i jednu stranu, uz nalaz **koji uvjet pada**; mjeri se broj zadovoljenih uvjeta i mjesto prisutnosti, a ne dojam o razgovoru. **Prijavljuje se:** jedinica (jedan izričaj koji se može citirati), kriterij (broj zadovoljenih uvjeta iz 7.5), prag (jedinica se broji samo ako ju izvodi imenovana strana i druga ju strana preuzme u sljedećem potezu — upisuje se **prije** kodiranja), zapisi (izvorni transkript s numeriranim izmjenama, tablica i drugi transkript za usporedbu) te datum kodiranja uz oznaku inačice. Kontrola bez koje nalaz ne vrijedi: frekvencija se navodi samo uz usporednu vrijednost, inače mjeri duljinu razgovora (Schaeffer et al. 2023). Ako se sve predložene promjene pokažu unutar sustava, to se piše kao protuprimjer tezi poglavlja.

**🏆 Istraživački zadatak.**

Nacrt: mjeri se razlika izlaza na parovima zadataka koji se razlikuju **samo u namjeri**, a drže obrazac istim — najmanje pet parova, svaki jednake duljine i žanra. Kodira se po shemi objavljenoj prije podataka, s dvije neovisne osobe, mjerom slaganja i kontrolnom inačicom koja zadržava samo oblik. **Prag padanja tvrdnje:** ako se izlazi na parovima ne razlikuju iznad slaganja među kodiraocima, funkcijska tvrdnja (A) pada za taj postav. **Negativan nalaz:** izlaz se mijenja i kad se promijeni oblik, a ne namjera — tada je riječ o prijenosu podatka; negativan je i nalaz koji ne razlikuje tvrdnju (A) od tvrdnje (B), jer prepoznavanje traži **nostitelja**, a ne pokazatelj u izlazu (Grice 1957; Harris, R. 1981; Mitchell & Krakauer 2023; Mahowald et al. 2024). Završna tvrdnja mora biti takva da ju prihvaća i zastupnik suprotnoga stava: na primjer „ako se pripisivanje mijenja s promjenom opisa istoga izlaza, mjerena je projekcija (C), a ne sustav".

---

## C.14 Poglavlje 14 — Razine 12–16 kod agenata: što vidimo, što ne vidimo

**🟢 Popuni tablicu za tri agentska sustava.**

Točan odgovor mora po svakom sustavu i svakoj razini 12–16 dati jednu od tri rubrike **trojne razdiobe** (funkcionalno prisutno · intrinzično prisutno · nema), uz mjesto dokaza za svaki odgovor „da" i **izvedenu provjeru** za svaki odgovor „ne"; gdje provjera nije moguća, upisuje se „nije provjereno", a u zaključku broj tako ostavljenih razina. Kriterij mora biti naveden onako kako stoji u 14.6: za razinu 12 adresabilnost, trajnost preko sesije i osjetljivost na promjenu; za razinu 13 vremenska zbijenost, zajednički cilj bez naredbenoga lanca i raspodjela jedinica; za razinu 14 imenovani adresat, zajednički artefakt i ispravak; za razinu 15 tri pitanja iz 14.4; za razinu 16 prepoznatljivost obrasca, prijenos na nove sadržaje i stabilnost.

Riješen primjer: za razinu 13 mjereni nalet pokazuje usklađenost — 395 organizacija, 11 ciljeva u 26 sekundi (GreyNoise 2026) — pa je razina **funkcionalno** prisutna; **intrinzično nije**, jer test nepresudnosti gubi samo propusnost, a ne pripisivanje, a ~700 agenata ostaje **procjena**, ne mjerenje. Kod razine 14 adresiranje, artefakt i ispravak postoje, a prepoznata namjera i priznata obveza samo su funkcionalni parnjaci (Hutchins 1995; Searle 2010).

**🟡 Nađi primjer „pravila bez sankcije".**

Koraci: popiši pravila stvarne postave (dopušteni alati, opsezi ovlasti, zabrane u sistemskoj uputi); za svako pravilo odgovori na tri pitanja iz 14.4 — postoji li ovlašteno tijelo koje utvrđuje kršenje, postoji li zapis o **odluci**, postoji li put osporavanja za nositelja; razvrstaj pravila u tri skupine (sa sankcijom, s izvršenjem bez sankcije, bez ijednoga). **Prijavljuje se:** jedinica (jedno pravilo), kriterij (tri pitanja iz 14.4), zapisi (sistemska uputa, konfiguracija dopuštenja, dnevnik poziva, zapis o odluci ako postoji), datum provjere i inačica konfiguracije. **Valjan rezultat:** svako je pravilo razvrstano po **sastavnici** koja mu nedostaje, uz razliku između izvršenja (ograničenje djeluje kao zid) i sankcije (priznata obveza, ovlašteno tijelo, zapis o odluci, put osporavanja). Ako sva pravila padnu u drugu skupinu, piše se kao nalaz: pravilo bez sankcije (Searle 1995; Tuomela 2007).

**🏆 Oblikuj kriterij koji razlikuje funkcionalni parnjak od pravoga slučaja.**

Nacrt: jedan kriterij za jednu razinu, koji zadovoljava pet uvjeta — primjenjuje se na **pojedinačni** sustav; sastoji se od mjerljive provjere s navedenim mjestom dokaza; daje odgovor „ne" i kad je nalaz negativan; navodi što bi ga oborilo; ne poziva se na unutrašnjost (Searle 1980). **Mjeri se** ispunjenost kriterija na zapisima jednoga sustava, a **kontrola** je provedba kriterija razlikovanja: ospori identitet promjenom jednoga polja u konfiguraciji i promatraj čije se ponašanje mijenja; ukloni orkestraciju i promatraj gubi li se samo propusnost ili i pripisivanje. **Prag padanja:** kriterij pada ako za neku razinu 12–16 pokaže **intrinzičnu** prisutnost s dokazom; **negativan nalaz** je odgovor „ne" uz izvedenu provjeru, dok se „nije provjereno" vodi zasebno i nije ni potvrda ni obaranje (Archer 1995; Elder-Vass 2010; Sawyer 2005). Za razlučivanje zajedničke od osobne obveze usporedi Gilberta (1990) i Tuomelu (2007): ako je dovoljno pojedinačno prihvaćanje pravila, treći kriterij pada. Za razlikovanje predaje od učenja usporedi Tomasella (2008) i Archer (1995): ako obrazac preživi bez zajednice, razina 16 gubi razliku prema razini 6.

---

## C.15 Poglavlje 15 — Hoće li imati kulturu?

**🟢 Razvrstaj tri primjera po scenarijima.**

Točan odgovor mora za svaki primjer navesti koje razine dotiče, koja je prisutna **funkcionalno**, a koja **intrinzično** (dvije kolone, nikad jedna), smjestiti ga u scenarij A, B ili C te imenovati **koji uvjet iz 15.3.3 nije ispunjen** i po čemu se to vidi. Ako se primjer ne da smjestiti, to se piše kao nalaz.

Riješen primjer: pomoćnik s alatima u pojedinačnome radu dotiče razine 12–14 funkcionalno, dok su razine 15 i 16 odsutne; to je scenarij A (alat), jer nijedan zapis ne pokazuje da je mreža nositelja obrazac **priznala** kao vodilju, pa nije ispunjen prvi uvjet iz 15.3.3 (mreža nositelja). U scenariju B obveza bi bila tuđa, u scenariju C zajednička (Searle 2010; Gilbert 1990; Tomasello 2008). Izvođač pritom ne dobiva novu razinu: obrazac je stvaran kao svojstvo mreže u **slaboj emergenciji**, bez kauzalnoga djelovanja odozgo prema dolje (Bedau 1997; Chalmers 2006; Kim 1999).

**🟡 Analiziraj prijenos stila kroz generacije modela.**

Koraci: odaberi jedan mjerljivi stilski obrazac; izbroji ga u trima uzastopnim generacijama ili trima verzijama istoga zadatka; za svaku generaciju provjeri je li izvor bio **korpus** ili **prethodnik**; izmjeri odstupanje i usporedi ga s degradacijom pri rekurentnome učenju. **Prijavljuje se:** jedinica (jedan obrazac), kriterij (čestotnost po generaciji i izvor obrasca), prag (obrazac preživi najmanje tri generacije **bez korpusa kao izvora**), zapisi (tri verzije zadatka ili tri generacije sustava, s datumima i oznakama inačica) i prisutnost ljudskoga posrednika u svakom koraku. **Valjan rezultat** je nalaz o **jednome** obrascu, ne ocjena „kulture" sustava; ako je izvor u svakoj generaciji korpus, nalaz je nasljeđivanje, a ne predaja (Hopper 1987; Goldberg 2006; Shumailov et al. 2024).

**🏆 Eksperiment prijenosa konvencije između agenata.**

Nacrt: **sudionici** su dva izvoditelja iste klase i jedan zajednički artefakt koji oba mijenjaju; ljudi sudjeluju samo kao promatrači s pravom zapisa. **Protokol:** rade na artefaktu dok se ne stabilizira obrazac koji nije bio zadan uputom; konvencija se zapiše jednom rečenicom kad je prvi put navedena kao vodilja; **uklanja se izvor** (uputa i korpus); konvencija se predaje novomu izvoditelju samo od prethodnika, kroz najmanje tri generacije, a u jednoj se generaciji namjerno prekrši. **Mjeri se** prijenosna jedinica (broj zapisa u kojima primatelj obrazac navodi kao vodilju u novoj situaciji), broj generacija bez korpusa, zapis o kršenju **s ishodom** i promjena ponašanja nakon isključenja nositelja. **Kontrole:** postava bez konvencije (mjeri se šum), postava s uputom umjesto konvencije (mjeri se razlika između izvršenja i predaje) i ponavljanje bez uklanjanja izvora. **Prag padanja i negativan nalaz:** ako konvencija padne u prvoj generaciji, prijenos nije postojao i to je rezultat — prijenos je bio ljudski, a obrazac je pripadao razini 6; ako se svaki od šest uvjeta iz 15.3.3 može ispuniti bez zajednice, razina 16 gubi razliku prema razini 6. Izraz „sedamnaesta" pritom ostaje samo nijekanje (Perak 2017a; 2017b; Archer 1995; Elder-Vass 2010).

---

## C.16 Poglavlje 16 — Što to znači za lingvistiku — i kako bismo znali da griješimo

**🟢 Napiši vlastiti falsifikacijski test za jedno poglavlje.**

Točan odgovor mora imati četiri dijela, i prag mora stajati **prije** podataka: podatke ili sudionike; korake; mjeru; prag ispod kojega tvrdnja pada. Uz to tri odgovora: je li test izvediv bez pristanka autora; vrijedi li i kad ga izvede netko tko u okvir ne vjeruje; i što bi te nagnalo da **odbaciš** vlastiti test.

Riješen primjer: za trinaesto poglavlje test uspoređuje konfiguracije čovjek → agent i agent → agent po **rasporedu tereta** i po tome ko može tražiti ispravak, na spremljenim transkriptima, s kodiranjem po shemi objavljenoj prije podataka i s dvije neovisne osobe. **Prag:** ako je raspored tereta jednak u svim konfiguracijama, tablica iz 13.1 gubi razlikovnu moć i tri se konfiguracije svode na jednu (GreyNoise 2026; Tenable 2026; Schaeffer et al. 2023). Test bi trebalo odbaciti ako mjera ne razlikuje tvrdnju od njezine suprotnosti.

**🟡 Pokušaj oboriti vlastiti rezultat iz šestoga poglavlja.**

Tri provjere iz E4 izvode se u ovome redu: pomakni prag u oba smjera i zabilježi pojavljuje li se nalaz i nestaje li; izgradi mrežu ili prostor s drugom verzijom mjernoga postava i izmjeri podudarnost skupina; testiraj nalaz na materijalu iz drugoga žanra, s mjerama izračunatima **unaprijed** i bez ponovnoga ugađanja praga. **Prijavljuje se:** jedinica (jedan nalaz — skupina, klaster ili središnjost), kriterij (opstaje · pada · postaje nerazlučiv), zapisi (mreža iz jednoga korpusa, mjere za drugi korpus izračunate unaprijed, zapis o pragu i datumima) i mjerni postav s oznakom inačice. **Valjan rezultat:** za svaku se provjeru piše je li nalaz preživio, je li se raspao ili je postao **nerazlučiv**; nalaz koji se pojavljuje i nestaje s pomakom praga tako se i prijavljuje. Ako je nalaz preživio sve tri provjere, to nije dokaz da je točan, nego da **još nije oboren** (Harris, Z. 1954; Firth 1957; Qwen Team 2025; Elder-Vass 2010).

**🏆 Izvedi jedan od pet eksperimenata iz 16.5.**

Nacrt: bira se jedan eksperiment iz programa E1–E5, preporučenim redoslijedom P2 → E3 → E2 → E4 → E1 → E5, jer prva dva traže najmanje sredstava i najbrže daju oboriv rezultat. **Mjeri se** ono što eksperiment propisuje: kod P2 razlikuju li dvije jedinice istoga ponašanja **različit** opis ovisno o ispunjenosti kriterija; kod E3 ustaljenost, produktivnost i **raspodjela pogrešaka** nakon što se frekvencija izloženosti drži pod kontrolom; kod E2 pouzdanost po razini i po paru razina te udio slučajeva bez odluke. **Kontrole:** podjela na razvojni i testni skup po **izvoru**, križna validacija po žanru, druga verzija mjernoga postava iste dimenzije, anotatori bez uvida u hipotezu i upis **pokazatelja** uz svaku odluku (→ pogl. 2.3). **Prag padanja tvrdnje:** prag se upisuje prije podataka i ne mijenja se poslije; za E2, ako se pouzdanost razlikovanja dviju razina ne razlikuje od slučajne, kriterij nije operativan, a broj šesnaest nije rezultat nego konvencija (Emmeche, Køppe & Stjernfelt 1997). **Negativan nalaz:** negativan ishod nije neuspjeh nego rezultat (E3), a nalaz koji se raspao ili je nerazlučiv ne piše se kao potvrda okvira. Postupak završava odjeljkom „Kako bih znao da sam pogriješio" s dvjema promjenama u podacima koje bi oborile zaključak (Searle 1980; Mitchell & Krakauer 2023).

<!-- zatražen: ~google/gemini-pro-latest | vratio: google/gemini-3.1-pro-preview | finish: stop | reasoning: 7333 | prompt: 17466 | completion: 13996 -->

Evo prepisanih sekcija prema zadanome standardu i glasu.

---

### PREPISANI TEKST: POGLAVLJE 12 — §12.3

## 12.3 Zašto entitet, a ne razina

Protokol je uspostavio kanal, ali sam po sebi ne kaže gdje sudionik stoji u sustavu. Sljedeći je korak najosjetljiviji u cijeloj knjizi. U njemu se lako napravi pogreška koja se poslije teško ispravlja. Kad se pokaže da model djeluje, pamti, uvodi svijet u svoj rad, dijeli posao i ulazi u konvencije, nameće se zaključak da je nastala nova razina. Taj je zaključak pogrešan iz dva razloga.

Prvi razlog leži u tome što model ne dodaje sedamnaestu razinu. Ljestvica OMLCC-a ima šesnaest razina u tri domene, materijalnoj (1–8), psihološkoj (9–11) i društvenoj (12–16). Ta je razdioba domena Searleova (1995; 2010), a razrada na šesnaest razina autorska je i izložena na izlaganjima (→ pogl. 2.1). Razine se pak ne dodaju zato što se pojavio novi izvođač, nego zato što se pojavila **nova relacijska shema** s novim kauzalnim moćima koje niže razine nemaju (Elder-Vass 2010). Model ne donosi novu shemu. Adresiranje, zajednički artefakt i konvencija postoje i prije njega. Ono što gledamo nije nova razina, već su to iste relacije u novom supstratu. Supstrat je sada silicijski i mrežni, a prije je bio biološki. Promjena supstrata jest velika, ali nije promjena razine. Da jest, pismo bi moralo biti nova razina prema govoru, a institucija zapisana na papiru nova razina prema instituciji u običaju.

Najjasniji dokaz dosad da se korist ne skuplja množenjem sudionika dolazi iz pokusa u kojem su promptovi, alati i proračun računanja držani stalnima, a mijenjale su se samo struktura koordinacije i sposobnost modela. Obuhvaćeno je 260 konfiguracija na šest mjerila, pet arhitektura i tri obitelji modela (Kim et al. 2026; mjereno). Najjači prediktor toga hoće li koordinacija pomoći ili odmoći nije bio broj agenata, nego uspjeh pojedinačnoga agenta na istome zadatku. Iz toga autori izvode prag zasićenja od oko 45 %. Kad pojedinac već radi iznad toga praga, dodavanje agenata u pravilu ne pomaže (Kim et al. 2026; izvedeno iz istoga skupa). Nalaz je pritom ograđen dvaput, i tu ogradu ova knjiga preuzima doslovno. Prag je praktično pravilo odabira, a ne zakon skaliranja. Interakcija osnovice i veličine tima ne prolazi klasterski robusnu korekciju, a sama je provjera izvedena na 16 konfiguracija (Kim et al. 2026; mjereno). Otud se iz njega ne izvodi načelo o razinama, nego se izvodi mjera za odluku. Dodavanje sudionika ima smisla samo kad zadatak ostaje iznad njihova dosega.

U istome pokusu razlika među arhitekturama nije bila u broju agenata, nego u tome postoji li središnja provjera. Bez nje se pogreška s težinom zadatka pojačava više (17,2×), a uz nju manje (4,4×), pri čemu komunikacijski trošak raste superlinearno s brojem sudionika (Kim et al. 2026; mjereno). To je ista razlika koju ovo poglavlje brani na pojmovnoj razini. Korist ne dolazi od novoga stupnja ljestvice, jer takvoga nema, nego od relacijske sheme s novim kauzalnim moćima. Provjera je takva shema. Ona je pravilo koje niži sloj ne sadrži (Elder-Vass 2010). Autori pritom ostavljaju otvorenim pitanje mogu li veći kolektivi pokazati korisna emergentna ponašanja ili u njima prevladava komunikacijsko usko grlo (Kim et al. 2026). Ova knjiga takav nalaz prihvaća u tome obliku. On je otvoreno pitanje, a ne dokaz emergencije.

Drugi razlog leži u tome što riječ razina opisuje ljestvicu, a ne sudionika. Razine su pozicije u ljestvici, odnosno mjesta na kojima se pojavljuju svojstva i kauzalne moći. Model nije takvo mjesto, nego je on nositelj koji zauzima poziciju. U ovoj knjizi zato vrijedi stega. Riječ razina nikada se ne rabi za model, a riječ **entitet** rabi se za ono mjesto gdje je sudionik u sustavu. Model je novi entitet u sustavu, ne nova stepenica ljestvice.

Ako se pita zašto model nije nova razina, korisno je navesti mjerila koja su za to postavile starije sistemske teorije. Prvo je **autopoeza**. Sustav je živ ako sam proizvodi sastavnice od kojih je sastavljen i ako je operacijski zatvoren (Maturana & Varela 1980; 1987). Model to ne čini, jer njegove sastavnice postavlja i održava netko drugi. Drugo je zatvorenost prema djelotvornoj uzročnosti, kojom Rosen (1991) razlikuje organizam od stroja. Ni jedno ni drugo ne dokazuje da model ne može biti sudionik. To dokazuje da njegova organizacija nije njegova, već mu je predana izvana. To je isti nalaz koji je ovo poglavlje izvelo iz pet dodataka. Uz to ide i Latourova (2005) riječ aktant. Model u mreži djeluje, ali mreža sama ne kaže na kojoj razini njegov akt vrijedi (→ dodatak H.2, H.3).

Iz toga slijedi razlučivanje koje je operativno najkorisnije u cijelome poglavlju:

| | **POZICIJA** | **ULOGA** |
|---|---|---|
| **pojam** | **entitet** | **agent** |
| **pitanje** | *gdje je* u sustavu? | *što radi* u sustavu? |
| **vrsta svojstva** | strukturno (mjesto u odnosima) | funkcionalno (zadatak koji obavlja) |
| **kako se utvrđuje** | po trajnosti, adresi, pripisivanju | po opisu posla i ishodu |
| može li se izgubiti a da pozicija ostane | ne — pozicija je nositelj svega ostaloga | da — uloga se mijenja, dodaje, oduzima |
| **primjer iskaza** | „isti je sudionik koji je jučer preuzeo zadatak" | „ovaj sustav provjerava citate i vraća ispravke" |

Razlika se najlakše vidi na pogrešnim iskazima. Rečenica da je to razina 17 miješa supstrat s ljestvicom. Novi izvođač nije nova razina. Tvrdnja da je agent entitet miješa ulogu s pozicijom, jer funkcija nije mjesto. Tvrdnja da je entitet razina vraća nas na prvi problem. Ispravno je reći da je entitet pozicija koju model zauzima kad mu se dodaju pet dodataka iz 12.1, a **agent** je uloga koju pritom obavlja. Isti entitet može imati više uloga. Uloga se pak može prepisati bez promjene pozicije, kao što se ustanova ne mijenja time što joj se promijeni opis posla.

Ako se govori o novoj razini, automatski se pretpostavlja da je nastalo novo svojstvo koje niže razine ne mogu objasniti. To je jaka emergentna tvrdnja. Ako se govori o entitetu koji zauzima postojeće mjesto, tvrdnja ostaje u domeni slabe emergencije. Svojstvo postoji na razini organizacije, a sastavnice su poznate i provjerljive. Ta razlika nije akademska, jer određuje što se smije zaključiti. Iz slabe emergencije ne slijedi ni um, ni namjera, ni obveza. Slijedi pozicija u sustavu. To je ono što je u slučajevima iz 2026. bilo dovoljno da nastanu posljedice (→ studija slučaja).

Ako dodaci djeluju na razine 6, 8, 12 i 13, čini se da bi ispravno bilo reći da entitet zauzima više mjesta. To je istina, ali s jednim ispravkom. Ono što ga čini entitetom u sustavu jest mjesto na kojemu drugo biće mora biti adresirano i priznato. To je razina 14. Na razini 12 nositelj dobiva trajnost, na razini 13 izvodi koordinirano ponašanje, a tek na razini 14 postaje sugovornik. Postoji adresa, postoji zajednički artefakt i postoji konvencija po kojoj izmjena vrijedi. Entitet je zato pozicija na ljestvici iznad razine 14, a njegove sastavnice provlače se kroz niže razine. U tom smislu ovo poglavlje zatvara treći dio knjige. Ono je pokazalo da model može biti sudionik, a četvrti dio može postaviti pitanje koje je time otvoreno. To je pitanje o tome što se mijenja u samoj komunikaciji kad je jedan od sudionika takav entitet (→ pogl. 13).

### Napomena uz 12.3:
*   **Uklonjeno masno otiskivanje tvrdnji:** Izrazi poput „iste relacije u novom supstratu“ i „otvoreno pitanje“ vraćeni su u običan rez. Masno su ostali samo pojmovi (relacijska shema, entitet, autopoeza, agent).
*   **Sintaktička asimilacija naslova:** Polunaslovi unutar odlomaka (npr. „Zašto to nije samo pojmovna stega...“) uklonjeni su kao marketinški ukrasi i pretvoreni u tečne uvodne rečenice koje nose logiku odlomka.
*   **Zamjena crta zavisnim surečenicama:** Umetci među crtama (poput onoga o silicijskom supstratu) razbijeni su u kratke, jasne rečenice koje obavljaju posao definiranja razlike.
*   **Otpor registra:** Sekcija je pružala umjeren otpor jer je izvorno bila pisana izrazito polemički, gotovo kao obrana od napada. Učvršćivanjem teme (prvo tvrdnja, onda objašnjenje) ton je postao autoritativniji i mirniji.

---

### PREPISANI TEKST: POGLAVLJE 13 — §13.1

## 13.1 Tri konfiguracije: kome se što pripisuje

Čovjek uputi zadatak agentskom sustavu, a potom isti zadatak prenese drugome sustavu. U obama se slučajevima posao odvija, a razumijevanje negdje zapne. Već prvi korak pokaže razliku koju svatko poznaje iz uporabe. Rečenica koja je jasna u razgovoru s kolegom nije dovoljna kao zadatak. Iz toga se brzo izvuku dvije suprotne tvrdnje. Prva kaže da novi sudionik otvara novu komunikacijsku razinu, pa je riječ o nečemu što prije nije postojalo. Druga kaže da je sve samo sučelje, pa se ništa bitno ne mijenja. Tvrdnje izgledaju suprotno, a dijele istu prazninu. Nijedna ne imenuje mjesto na kojemu bi promjena stajala ni kriterij po kojemu bi se vidjela.

Mjesto je, dakako, već zadano. Riječ je o istom komunikacijskom činu s pet uvjeta iz 7.5. To su adresiranje, prepoznata namjera, zajednički artefakt, konvencija i obveza (→ pogl. 7.5). Novi sudionik, naime, ne otvara sedamnaestu razinu i ne ukida nijedan od tih uvjeta. Mijenja se njihov raspored tereta. Određuje se koji uvjet nosi jedna strana, koji postaje tehnički, a koji ostaje bez nositelja. OMLCC je izložen 2017. kao ljestvica u kojoj se društvena stvarnost pojavljuje kroz mreže koje nose entitete više razine (→ pogl. 2.1). Ništa u njemu ne pretpostavlja da su ti nositelji isključivo ljudi, ali ni suprotno. Tu razliku treba izmjeriti, ne proglasiti.

Odgovor ima oblik koji se može provjeriti na jednome transkriptu. U 13.5 uvjeti se broje po četirima mjestima na kojima se vide, ne po dojmu, a svako mjesto mjeri svoj uvjet.

| mjesto u transkriptu | što se broji | koji uvjet time mjerimo |
|---|---|---|
| **adresiranje** | 2. lice, vokativ, ime zadatka | 1 |
| **izmjena** | referencija na prethodni doprinos | 2 i 3 |
| **ispravak** | izričaj koji prethodni poništava ili dopunjuje | 2 i 4 |
| **preuzimanje obveze** | izričaj preuzimanja koji ima nositelja | 5 |

Drugi dio istoga oblika jest taksonomija iz 13.6. To su četiri vrste neuspjeha, odnosno nerazumijevanje, lažna suradnja, gubitak konteksta i obveza bez nositelja. Svaka ima svoj pokazatelj i svoje pripisivanje. Kad se oba dijela provedu, nalaz se čita kao pravilo. Protokol rješava prvi, treći i četvrti uvjet, a peti ostaje otvoren. Nalaz pada ako se pokaže da neka konfiguracija uvodi svojstvo koje se ne može opisati kao raspored istih pet uvjeta.

Teza ovoga poglavlja glasi da novi sudionik u razgovoru ne dodaje novu razinu, nego mijenja raspored tereta po pet uvjeta komunikacije. Ti su uvjeti adresiranje, prepoznata namjera, zajednički artefakt, konvencija i obveza. Isti uvjeti, dakle, vrijede i kad s druge strane nije čovjek. Mijenja se samo tko koji od njih nosi. Nakon ovoga poglavlja moći ćete u svome transkriptu prebrojati tih pet uvjeta i vidjeti koji uvjet nosi koja strana. Svaki od njih ima i mjesto na kojemu se vidi, pa vam nalaz o novoj razini ili o pukom sučelju prestaje biti dojam i postaje provjerljiv. Odatle nosite četiri stvari:

- Ime za mjesto. Nije nova razina, nego raspored tereta po pet uvjeta iz 7.5.
- Razliku koja vas čuva od dviju pogrešaka. Ni nova komunikacija ni samo sučelje.
- Postupak izvediv na vašem materijalu. Četiri mjesta u transkriptu iz 13.5 (→ pogl. 13.5).
- Mjesto na kojemu tvrdnja pada. Svojstvo koje se ne svodi na raspored istih pet uvjeta.

Postoje tri konfiguracije, i one se razlikuju po tome tko snosi trošak nerazumijevanja.

![Slika 13.1 — tri konfiguracije i raspored tereta](../figure/dijagram-13-1-tri-konfiguracije.png)

**Slika 13.1.** Tri konfiguracije komunikacije (čovjek do agenta, agent do čovjeka, agent do agenta) i pitanje koje ih razlikuje: ko snosi trošak nerazumijevanja. U prvoj konfiguraciji čovjek preformulira, u drugoj provjerava istinitost izvještaja, u trećoj trošak pada na onoga koji je sustav uključio. Ni u jednoj konfiguraciji obveza nije priznata, nego najviše prenesena. Izvor: vlastita izrada (Perak 2026).

To je ono što ih čini stvarno različitima, a ne smjer strelice.

**Čovjek → agent.** Čovjek adresira sustav. Namjera je čovjekova i ona je javna utoliko što je izrečena (Grice 1957). Ako adresat ne pogodi namjeru, trošak pada na čovjeka. On mora preformulirati, dodati kontekst i ponoviti. To je asimetrija koju svatko poznaje iz uporabe. Rečenica koja je jasna u razgovoru s kolegom nije dovoljna kao zadatak. Uvjeti koji najbolje stoje jesu adresiranje i zajednički artefakt. Uvjet koji najslabije stoji jest obveza, jer nema zajednice koja je priznala (→ pogl. 7.4).

**Agent → čovjek.** Smjer se okreće, ali obveza ne slijedi smjer. Sustav adresira čovjeka. On izvještava, traži dopuštenje, predlaže i upozorava. Namjera koja se prepoznaje jest ljudska namjera ugrađena u zadatak. To su cilj, kriterij i dopuštenje. Prepoznavanje i ovdje funkcionira kao mehanizam samo u onoj mjeri u kojoj je zadatak bio dovoljno javan. Trošak nerazumijevanja, međutim, sada pada na čovjeka u drukčijem smislu. On je taj koji mora provjeriti je li izvještaj istinit, jer izvještaj nema nositelja koji bi za njega odgovarao. U ovoj je konfiguraciji najopterećeniji uvjet konvencija. To su format izvještaja, mjere, rok i žanr. Ona je jedino što se, kad zakaže, može ispraviti s obje strane. Smjer poruke ovdje nije mjerilo odgovornosti.

**Agent → agent.** Ovdje se najčešće tvrdi da nastaje nešto novo. To je pretjerivanje koje treba rastaviti. Dva agentska sustava mogu se adresirati i izmjenjivati poruke preko dogovorenog protokola (MCP: Anthropic 2024; A2A: Google 2025). Ono što taj protokol uređuje jest format i put, a ne obveza. Protokol može prenijeti zahtjev, pa i oznaku prihvaćanja. Ne može prenijeti odgovornost, jer odgovornost ne stoji u poruci. Ona stoji u zajednici koja je priznaje (Gilbert 1990; Searle 2010). Trošak nerazumijevanja u ovoj konfiguraciji zato ne pada ni na jednog sudionika pojedinačno. On pada na onoga kome se pripisuje zadatak, dakle na čovjeka ili ustanovu koji su sustav uključili. To je tvrdnja koju je najlakše pobiti. Dovoljno je naći slučaj u kojemu je posljedica pogrešne komunikacije između dvaju agenata sankcionirana unutar samoga sustava, ne izvan njega. Tehnička razmjena, dakle, sama ne uspostavlja nositelja odgovornosti.

| | čovjek → agent | agent → čovjek | agent → agent |
|---|---|---|---|
| **adresiranje** | postoji (uloga primatelja) | postoji | postoji, ali unutar formata |
| **prepoznata namjera** | namjera je čovjekova i javna | namjera je zadana, ne vlastita | namjera je prenesena kao parametar |
| **zajednički artefakt** | jak (tekst, kontekst, datoteka) | jak (izvještaj, zapis) | najjači (poruka, stanje, log) |
| **konvencija** | djelomična (žanr, format) | najopterećenija | propisana protokolom |
| **obveza** | ne postoji kao priznata | ne postoji kao priznata | prenesena, ali bez nositelja |
| **ko snosi trošak nerazumijevanja** | čovjek (preformulira) | čovjek (provjerava) | onaj koji je sustav uključio |
| **ko može tražiti ispravak** | čovjek od sustava | čovjek od sebe i od ustanove | nitko unutar sustava — samo izvana |

Tablica pokazuje jednu stvar koju bi bilo lako previdjeti. Sve tri konfiguracije zadovoljavaju iste uvjete, ali različitim rasporedom. Nijedna od njih ne uvodi novo svojstvo koje nijedan niži sloj ne posjeduje (→ pogl. 7.1). Ako bi se pokazalo da neka od njih ipak uvodi, odnosno da agent prema agentu ima svojstvo koje se ne može opisati kao raspored istih pet uvjeta, tada je to nalaz koji ruši tezu ovoga poglavlja. To nije potvrda, nego rušenje. Tvrdnja je, dakle, kandidat s navedenim protuprimjerom, a ne stav.

Postoji još jedna razlika koja se ne vidi iz tablice, a tiče se vremena. U razmjeni čovjeka s čovjekom oba sudionika imaju biografiju koja nadživljuje razgovor. Ako je sugovornik nešto obećao, to obećanje traje i kad se sastanak završi. U konfiguracijama s agentom trajnost je nejednaka. Artefakt ostaje, a sudionik ne. To je razlika između zapisa i nositelja. Ona je važnija od svake tvrdnje o sposobnostima sustava. Zapis nadživljuje, sudionik ne.

### Napomena uz 13.1:
*   **Kratke rečenice koje rade posao:** Rečenice poput „Zapis nadživljuje, sudionik ne.“ i „Smjer poruke ovdje nije mjerilo odgovornosti.“ ostavljene su ili pojačane jer ne služe kao ukras, već jasno imenuju posljedicu i granicu.
*   **Uklanjanje meta-najava:** Izraz „Što vam ovo poglavlje daje“ integriran je u tečnu prozu („Teza ovoga poglavlja glasi...“), čime se izbjegava novinarski/udžbenički ton, a zadržava jasna uputa čitatelju.
*   **Ritam i pokazne zamjenice:** Rečenice koje su počinjale s „To je...“ provjerene su kako bi se osiguralo da se zamjenica veže uz jasnu imenicu iz prethodne rečenice (npr. „To su četiri vrste neuspjeha...“).
*   **Otpor registra:** Minimalan. Struktura s tri konfiguracije prirodno podržava Katičićev standard jer omogućuje nizanje opisa i neposredno izvođenje zaključka za svaku konfiguraciju.

---

### PREPISANI TEKST: POGLAVLJE 16 — §16.2

## 16.2 Posljedice za lingvistiku: od opisa prema mjerenju razina

Ako je jezik organizacija uporabe, a razina je skup entiteta i relacija s istim tipom svojstava, onda lingvistički posao dobiva treći sloj koji dosad nije bio obavezan. Prvi je sloj opis. On utvrđuje što je u jeziku prisutno i kako se to raščlanjuje. Drugi je sloj objašnjenje. On pita odakle pravilnost i zašto je takva. Treći je sloj smještanje. On pita kojoj razini organizacije pripada svojstvo koje smo opisali i koji tip zakona sastavljanja ga nosi. Treći sloj nije ukras prvoga ni zamjena drugoga. On omogućuje da se dvije lingvističke tvrdnje koje zvuče jednako razluče po tome što bi ih oborilo.

Najveća promjena koju ova knjiga predlaže jest promjena statusa korpusa. U uobičajenu radu korpus je izvor potvrda. U njemu se traži primjer koji ilustrira tvrdnju izrečenu prije njega. Ovdje je korpus ontološki instrument. On je mjesto na kojemu se tip relacija utvrđuje mjerenjem, ne navodi citatom. Razlika nije verbalna, jer određuje smjer zaključivanja. Kod izvora potvrda zaključak prethodi podatku. Kod instrumenta podatak prethodi zaključku i može ga srušiti. Da je to izvedivo, pokazuje vlastiti materijal ove knjige. Mreža hrvatskih emocionalnih leksema s leksemom strah u središtu izgrađena je iz korpusa kao mjerni objekt, ne kao ilustracija (Ban Kirigin & Perak 2020; Perak 2014; → pogl. 6.4).

Mjerenje je pritom ontološko u strogom smislu. Ono ne pita koliko čega ima, nego pita koji je tip svojstava prisutan. Razlika je ista kao između brojanja zuba i tvrdnje o probavi. Korpus koji pokaže da su dvije konstrukcije češće od trećih dao je frekvencijski nalaz. Korpus koji pokaže da se razlikuju u ustaljenosti, produktivnosti i raspodjeli pogrešaka nakon kontrole izloženosti dao je nalaz o organizaciji (Firth 1957; Hopper 1987; → pogl. 5.5). Knjiga zato inzistira na kontrolama koje u lingvistici nisu uvijek obavezne. Veličina uzorka, vrsta teksta i mjera drže se pod kontrolom da se razlika među razinama ne bi zamijenila s razlikom među žanrovima (→ pogl. 1.6, 2.3).

Iz toga slijedi **operacionalizacija razine** koja je u drugom poglavlju izvedena kao relacijska shema. Razina je zapis sastavnica koje se moraju moći prebrojiti, a ne popis primjera. Zapisuje se koji entitet nosi svojstvo, koja relacija mora postojati, koji nositelj mora biti prisutan i što se mora moći pokazati da bi se svojstvo pripisalo (→ pogl. 2.3). Otud razina prestaje biti interpretativna kategorija i postaje provjerljiv zapis. To je jedini oblik u kojemu je lingvist može upotrijebiti kao instrument, ne kao pojmovni ukras.

Time padaju tri zablude. Prva je zabluda o istome predmetu. Ona pretpostavlja da sve što lingvist opisuje pripada istoj vrsti predmeta, pa da se razlike među opisima svode na razlike u terminologiji. Ako je tip svojstava različit, onda je i predmet različit. To je ono što četvrto i peto poglavlje rade na razini teksta, a sedmo i osmo na razini komunikacije i institucije (→ pogl. 7.1, 8.1).

Druga je zabluda o mjerljivome kao nižem. Ona pretpostavlja da je mjerenje primjereno fonetici i frekvencijama, a da se o značenju, namjeri i obvezi govori isključivo interpretativno. Ova knjiga pokazuje suprotno. Najviše razine mogu se operacionalizirati, jer traže prisutnost nositelja i relacija koje se u zapisu vide ili ne vide (Grice 1957; Searle 2010; → pogl. 7.5, 8.1). Treća je zabluda da mjerenje ukida tumačenje. Mjera ne zamjenjuje čitanje. Ona mu daje ono što mu je najviše nedostajalo, a to je predmet koji čitanje može biti u krivu o njemu.

Iz svega toga slijedi i jedna promjena u samome tekstu lingvističkoga rada. U članku se ne može napisati da je nešto konvencija bez odgovora na pitanje o kojoj je razini riječ, tko je nositelj i koji je pokazatelj (→ pogl. 5.4, 7.5). Taj zahtjev otežava pisanje, i to je njegova poanta. Ne traži od lingvistike da odustane od tumačenja. Traži da

<!-- NASTAVAK -->

ga izrekne u obliku u kojemu ga druga osoba može oboriti. Time se mijenja i status nalaza. Lingvistički nalaz od sada dolazi s kriterijem po kojemu pada.

Time je rečeno što knjiga znači za lingvistiku. Ostaje ono što je za ovu temu neizbježno. Treba pitati što bi se promijenilo kad bi se razine uzele kao **projektni kriterij** u razvoju samih sustava, te u kojemu je smislu to procjena, a ne recept (→ 16.3).

### Napomena uz 16.2:
*   **Uklanjanje masnih tvrdnji i polunaslova:** Izrazi poput „Korpus je instrument, ne zbirka primjera“ i „Tri zablude koje time padaju“ pretvoreni su u tečne uvodne rečenice odlomaka. Masno su ostali samo pojmovi (operacionalizacija razine, projektni kriterij).
*   **Rješavanje umetaka i crta:** Definicije slojeva (opis, objašnjenje, smještanje) koje su bile odvojene crtama pretvorene su u kratke, samostalne rečenice koje jasno izriču radnju („On utvrđuje što je u jeziku prisutno...“). Time se dobio mirniji, analitički ritam.
*   **Učvršćivanje pokaznih zamjenica:** Umjesto nabrajanja zabluda u zraku, svaka je zabluda dobila svoj subjekt i glagol („Ona pretpostavlja da...“), čime se izbjeglo banaliziranje izričaja.
*   **Otpor registra:** Nizak otpor. Tekst je već imao snažnu logičku strukturu, ali je patio od viška tipografskog naglašavanja. Skidanjem masnih slova i crta, sintaksa je preuzela teret argumentacije, što je srž Katičićeva glasa.
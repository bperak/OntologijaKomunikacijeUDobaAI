<!-- zatražen: openai/gpt-6.1-sol-pro | vratio: openai/gpt-6.1-sol-pro | finish: stop | reasoning: 156 | prompt: 26872 | completion: 5370 -->

# Predgovor

## Zašto još jedna knjiga

Rečenica „model razumije“ danas se izgovara bez osobita zastoja. Isto vrijedi za rečenice „model komunicira“ i „model stvara značenje“. Mogu se prihvatiti ili odbaciti, a da se pritom ne postavi pitanje **gdje** bi to svojstvo stajalo — na kojoj razini stvarnosti i kod kojega nositelja. Spor tada izgleda kao neslaganje o odgovoru. Često je posrijedi neslaganje o pitanju koje nitko nije do kraja izrekao.

Posljedice toga propusta nisu samo teorijske. O granici između pomoći i prepisivanja, pripisivanju autorstva i onome što se traži od studenta odlučuje se i prije nego što pojmovi dobiju kriterije. Odluke ne mogu čekati dovršenu ontologiju. Mogu, međutim, biti jasnije o tome na što se oslanjaju.

Zbog toga je nastala ova knjiga. Ne zato što raspravi o umjetnoj inteligenciji nedostaje još jedan stav, nego zato što tvrdnjama o njoj nedostaje određeno mjesto. *Razine i entiteti* nude **operativan okvir**: šesnaest ontoloških razina OMLCC-a, njihove relacijske sheme i uvjete pod kojima se pojedina tvrdnja može prihvatiti ili oboriti. Komunikacija u tome okviru zauzima razinu 14. Jezični model nije dodatna razina; razmatra se kao kandidat za novi **entitet** unutar postojećega sustava.

Čitatelju se time ne obećava konačan sud o modelima. Nudi mu se postupak kojim će vlastiti sud učiniti određenijim — i dostupnim provjeri.

## Kome je knjiga namijenjena

Knjiga je namijenjena lingvistima, filozofima i informatičarima, ali i studentima kulturalnih studija i digitalne humanistike, istraživačima kompleksnosti te praktičarima u jezičnim tehnologijama i kulturnoj baštini. Njihova pitanja nisu ista. Lingvist pita što se zbiva s jezikom, filozof što se nekomu nositelju smije pripisati, a informatičar kojim se postupkom tvrdnja može ispitati. Ovdje ta pitanja trebaju zajednički pojmovni okvir, ne isti odgovor.

Knjiga pretpostavlja znatiželju, a ne predznanje programiranja. Kod je objašnjen i može se preskočiti bez gubitka osnovne tvrdnje. Postupak provjere ipak se ne može preskočiti: čitatelj koji ne izvodi izračun i dalje treba znati što se mjeri, kojim izborima i uz koja ograničenja. Pojmovna pristupačnost ne znači oslobađanje od metodološke odgovornosti.

## Organizacija i put čitanja

Knjiga ima četiri dijela i šesnaest poglavlja. Prvi dio postavlja okvir: sustave, organizaciju, razine, emergenciju i metodologiju. Drugi obrazlaže zašto je komunikacija razina, a ne samo alat. Treći razmatra jezične modele, od vektorskoga prostora do njihova mjesta u sustavu. Četvrti ispituje što njihov ulazak mijenja u komunikaciji, kulturi i lingvistici te gdje su granice iznesenih tvrdnji.

Poglavlja počinju tezom i njezinim prijevodom na običan jezik. Slijede teorijski okvir, metode i podaci, a zatim praktikum ili radni primjer. Uz kod stoji pomoć za slučaj da postupak ne radi. Vježbe vode od provjere preko primjene do istraživanja; sažetak i ključni pojmovi omogućuju povratak na nosive razlike.

Odjeljak *Kako bismo znali da griješimo* zatvara taj slijed. Njegova je zadaća jednostavna: pokazati koji bi rezultat prisilio na promjenu tvrdnje. Nije potrebno unaprijed prihvatiti okvir da bi se knjiga čitala. Potrebno je pratiti što bi ga moglo oboriti.

## Tri knjige, tri posla

Ova knjiga pripada mreži triju knjiga, ali se može čitati samostalno. *Komunikacija u doba umjetne inteligencije* (2025) obrađuje povijest, arhitekturu i praksu: što se dogodilo. *Data Science u kulturi*, knjiga u izradi, obrađuje podatke, statistiku i ugrađivanja: kako se mjeri. Ova knjiga pita gdje nalaz ontološki stoji.

Podjela posla štedi ponavljanje. Priprema korpusa i izračun ugrađivanja ne objašnjavaju se iznova ondje gdje je pitanje što ti postupci dopuštaju tvrditi o razinama. Znak ↗ upućuje na drugu knjigu, a znak → na drugo poglavlje ove. Popis uputa nalazi se u `docs/UPUTE-PO-POGLAVLJIMA.md`, a zajednički rječnik u `pojmovnik/RJECNIK.md`.

Ta mreža olakšava čitanje. Ona nije dokaz teorije.

## Četiri pravila čitanja

Prvo je pravilo **slaba emergencija**. Knjiga se služi isključivo njome: ono što nastaje na višoj razini izvedivo je iz niže, ali simulacijom, ne izračunom u jednome koraku (Bedau 1997). Jaka emergencija nije objašnjenje koje se uvodi kada drugo zakaže.

Drugo je pravilo razlika između **entiteta** i **agenta**. Entitet odgovara na pitanje *gdje*: imenuje mjesto u sustavu. Agent odgovara na pitanje *što radi*: imenuje sistemsku ulogu. Riječ „razina“ nikada ne označava jezični model. Tu razliku treba zadržati i kada svakodnevni jezik nudi kraći izraz.

Treće je pravilo da je **mjera** dio tvrdnje. Ako se pojava ne može razlučiti od artefakta mjerenja, prijavljuje se kao nerazlučiva. Izbor postupka nije neutralna pozadina nalaza; može proizvesti razliku koju smo namjeravali pronaći.

Četvrto je pravilo evidencija brojki. Svaka brojka ima izvor, datum i vrstu: *mjereno*, *procjena* ili *izvedeno*. Procjena se ne prikazuje kao mjerenje. Evidencija se vodi u `data/fakti.csv`, kako bi čitatelj mogao provjeriti ne samo broj nego i njegov status.

## Granice i nastanak rukopisa

Knjiga ne tvrdi da su razine upisane u prirodu kao gotove podjele. Predlaže okvir čija se razlučivost ispituje. Ne tvrdi da model ima svijest, iskustvo ili namjeru. Ne zamjenjuje slabu emergenciju jakom i ne uzima korisnost kao dokaz istinitosti. To što okvir uređuje raspravu još ne znači da je točan.

Rukopis se razvija iz izlaganja *Elements of Cognition in Complex Language*, održanoga u Inter-University Centru u Dubrovniku 11. rujna 2026. Reference prolaze kroz zajedničku bazu `referencije/REFERENCE_BASE.md`; citat ne ulazi u tekst ako nije evidentiran, a izvor stoji uz tvrdnju koju podupire.

Automatske provjere obuhvaćaju izgradnju pojmovnika, unutarnje i mrežne upute te usklađenost brojki s evidencijom. Za njih služe skripte `kod/pojmovnik_build.py`, `kod/check_links.py` i `kod/check_fakti.py`. One mogu pronaći nedosljednost rukopisa. Ne mogu odlučiti je li njegova teorija istinita. Taj posao ostaje istraživanju.

## Zahvale

Zahvaljujem Inter-University Centru u Dubrovniku na stipendiji koja mi je omogućila izlaganje iz kojega je knjiga nastala. Zahvaljujem projektima STUDIA, DEMOKRACIJA i FORMALS te projektu Erasmus+ AI4LANG (AI Language Tutor), uz koje se razvijao istraživački i metodološki aparat knjige.

Zahvaljujem Laboratoriju za istraživanje kulturne složenosti, Odsjeku za kulturalne studije Filozofskoga fakulteta u Rijeci, na prostoru za spore provjere i brze pogreške.

*Benedikt Perak*  
*Rijeka, rujna 2026.*

---

## Što ostaje nepromijenjeno

- Polazno pitanje *gdje svojstvo stoji*. To je najjača poveznica predgovora s naslovom i uvodom.
- Podjela posla među trima knjigama: što se dogodilo, kako se mjeri, gdje ontološki stoji.
- Četiri pravila čitanja, granice tvrdnje i zahtjev da se navede rezultat koji bi tvrdnju oborio.
- Podaci o nastanku rukopisa, infrastruktura provjere i zahvale. Rečenicu „na prostoru za spore provjere i brze pogreške“ zadržao sam: osobna je, a ne izlazi iz registra knjige.

## Što sam promijenio i zašto

1. Predgovoru sam dao posao koji prethodi uvodu. Umjesto ponovnog izlaganja teze i obećanih rezultata, uspostavlja razlog nastanka, odnos prema čitatelju i uvjete čitanja.

2. Publiku sam povezao preko različitih pitanja. Nabrajanje disciplina ostaje, ali sada pokazuje zašto im treba zajednički okvir, bez pretpostavke da traže isti odgovor.

3. Organizaciju sam preveo iz sheme u prozu. Struktura poglavlja ostaje vidljiva, ali predgovor manje nalikuje tehničkim uputama. Putanje datoteka i nazivi skripti zadržani su kao mjesta provjere, bez izvršnoga bloka.

4. Ublažio sam tvrdnje koje unaprijed presuđuju. „Obrazlaže zašto“ zamjenjuje „dokazuje“, a završni falsifikacijski odjeljak opisuje se svojom funkcijom. Istraživački program tako ne zvuči dovršenije nego što jest.

5. Uskladio sam terminologiju s uvodom. Model ostaje kandidat za novi entitet, „razina“ ga ne označava, a među vrstama brojki dodano je *izvedeno*. Podebljanje je ograničeno na pojmove.

## Treba li predgovoru drukčiji registar?

Ne treba mu drukčiji registar, nego drukčija zadaća. Uvod razvija argument; predgovor uspostavlja odnos čitatelja prema knjizi. Zato sam zadržao kratke zaključne rečenice, pojmovnu stegu i prijelaz od problema prema provjeri, ali smanjio gustoću dokazivanja. Osobni glas pojavljuje se u zahvalama. Nema potrebe uvoditi autobiografski ton koji zadana građa ne podupire.
# Dodatak B — Rječnik pojmova

Rječnik nije sastavljen za ovu knjigu: on je **zajednički** trima knjigama mreže (*Razine i entiteti*, *Komunikacija u doba umjetne inteligencije*, *Data Science u kulturi*), jer se pojmovi među njima prenose i moraju značiti isto. Zato se ne piše u tekstu, nego se **generira** iz jednoga registra:

```
pojmovnik/koncepti.csv      ← registar: pojam · knjiga · poglavlje · uloga u tekstu
pojmovnik/RJECNIK.md        ← generirani rječnik (čitljiv oblik)
kod/pojmovnik_build.py      ← skripta koja iz registra gradi rječnik
```

## B.1 Zašto generirani, a ne ručno pisani rječnik

Ručno pisan rječnik razvezuje se od teksta pri prvoj izmjeni: pojam se u poglavlju preimenuje, a u rječniku ostane stara inačica. Ovdje je veza obrnuta — **poglavlje je izvor, a rječnik je pogled** na njega. Svaka izmjena u tekstu dovodi se u vezu s registrom jednom naredbom, pa se ne može dogoditi da rječnik tvrdi nešto što tekst ne tvrdi.

## B.2 Kako se rječnik čita

- **pojam** — naziv kako se rabi u tekstu, u nominativu;
- **knjiga** — kojoj knjizi mreže pojam pripada (pojmovi se dijele, definicije se ne prepisuju);
- **poglavlje** — gdje se pojam uvodi ili razrađuje;
- **uloga u tekstu** — je li pojam nositelj tvrdnje, mjera, alat ili samo spomenut.

Uz rječnik u tiskanome izdanju stoji i **kazalo pojmova i imena** (dodatak G), koje je također generirano — iz registra pojmova i iz baze referenci — pa se ne može razilaziti s tekstom.

## B.3 Terminološka stega koju rječnik čuva

Rječnik je i mjesto na kojemu se čuvaju tri razlikovanja bez kojih se tvrdnje knjige raspadaju:

1. **entitet** imenuje **gdje** je nešto (pozicija u sustavu), a **agent** imenuje **što radi** (sistemska uloga);
2. **funkcionalno prisutno** (razina se može prebrojati u zapisima) nije isto što i **intrinzično prisutno** (razinu ima sam nositelj, s kriterijem razlikovanja);
3. **ustaljeno** (obrazac se reproducira), **proizvoljno** (znak nije motiviran svijetom) i **emergentno** (obrazac je proizvod procesa) nisu isto značenje, iako se u govoru miješaju.

Pojam koji u tekstu prekrši ta razlikovanja ne ulazi u rječnik — a kad se pojavi potreba za novim pojmom, dodaje se **najprije u registar**, pa u poglavlje, i to s naznakom uloge.

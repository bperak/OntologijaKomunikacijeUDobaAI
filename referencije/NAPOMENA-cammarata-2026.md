# Cammarata 2026 — „Neural Networks Are Already Clean": što tvrdi, na čemu stoji i gdje pogađa kritika

**Namjena:** izvor za rukopis. **Nije dio rukopisa** i **nije u `REFERENCE_BASE.md`** — uvrštavanje u bazu
je zaseban korak koji autor odobrava.

## Citat

> Cammarata, N. (2026). *Neural Networks Are Already Clean*. Goodfire, 15. listopada 2026.
> https://already-clean.goodfire.com/ — radna hipoteza, esej od 65 minuta čitanja (~26.000 riječi).
> Popratni tehnički rad (o neuronima jezičnih modela) **još nije objavljen**.

BibTeX (autorov):
`@article{cammarata2026clean, author = {Cammarata, Nick}, title = {Neural Networks Are Already Clean}, publisher = {Goodfire}, year = {2026}, note = {https://already-clean.goodfire.com/}}`

**Tko je autor:** Nick Cammarata, istraživač u Goodfireu; bivši član OpenAI-ova interpretability tima;
koautor rada *Zoom In: An Introduction to Circuits* (Olah, Cammarata, Schubert, Goh, Petrov, Carter, Distill
2020.) i jedan od tvoraca hipoteze superpozicije — dakle **pobija dio vlastitoga ranijeg okvira**.

*Citati su na izvornom jeziku; gdje je tekst preveden, prijevod je naš.*

## Što tvrdi (pet tvrdnji)

1. **Superpozicija nije bila ispravno objašnjenje za InceptionV1.** Ono što je izgledalo kao „proizvoljno
   pakiranje" koncepata bili su arhitekturni problemi (prelijevanje kasnih slojeva) i slabi alati. Uz
   obična arhitekturna poboljšanja, **bez promjene veličine modela i podataka**, **99–100 % neurona
   zadnjega sloja je lako interpretirati**, a model je čitljiv cijelim putem; vrijedi na **300× rasponu
   veličina**. „S manje mjesta neuron ne skriva nepovezane stvari; pokriva grublje pojmove."
2. **Kanonizirani primjer superpozicije bio je pogreška.** „Automobil" koji se „skriva" u neuronskoj grupi
   pasa iz *Zoom In* (2019./2020.) nije skriven: „ništa ne čita tu kombinaciju" — to je obična
   generalizacija i kompozicija. Prema autorovu znanju, **nijedan drugi sklop istoga oblika nije objavljen**.
3. **Novi motiv umjesto superpozicije: rekurzivna generalizacija** — neuron pokriva srodne stvari i njihove
   „izdanke", što je mnogo manje zabrinjavajuće od proizvoljnoga pakiranja.
4. **Suvremeni jezični modeli čitljiviji su nego što se misli.** U **preliminarnim auditima Qwen3-32B**
   autor procjenjuje da **~90 % neuronskih polova ima jedan glavni posao**, ~7 % dva srodna, a **~2–4 %**
   još nije razumljivo (uz ogradu da udio ovisi o pragu za slabe aktivacije, dubini i tome što se broji
   kao „jedna stvar").
5. **Kontrast s 2023.:** Anthropicov *Towards Monosemanticity* dao je medijalnom neuronu **0 od 14** na
   rubrici (ispitivač nije mogao oblikovati nikakvu hipotezu); OpenAI-ov projekt automatske
   interpretabilnosti našao je **~1,7 %** neurona interpretabilnima po najblagom mjerilu.

## Na čemu stoji

Neuroni i sklopovi u **slikovnim modelima** (InceptionV1 i inačice kroz 300× raspon veličina) · **kausalne
intervencije u jezičnim modelima** · eksperimenti u kojima automatizirani ispitivači svojim opisima neurona
**predviđaju odgovore na nove ulaze** · audit Qwen3-32B. Sve je to **esejistički izloženo**, s pomoćnim
materijalom („mikroskop" za pregled modela) — ali **bez recenzije i bez popratnoga tehničkog rada**.

## Vlastite ograde (autorove riječi)

- „**A working hypothesis**" · „**We're maybe 85% sure**" · „**We don't have a proof**, but I don't think
  anything here is provable in that sense anyway."
- „**We haven't fully audited every neural network**, and we don't know whether that's even possible in
  theory."
- O najvećim modelima: „We found similar results in models up to trillions of parameters, like Kimi K3,
  which the companion paper will cover in more detail." — dakle tvrdi da nalaz vrijedi i na razini bilijuna
  parametara, ali **taj će dio nositi popratni rad**, koji još nije objavljen.
- O jezičnim modelima: „work on much larger language models remained **promising exploration with extensive
  mapping ahead**" (autorovo pojašnjenje).
- O otvorenome: „I **don't fully understand** these exceptions yet."

## Gdje kritika pogađa

**Neel Nanda (Google DeepMind, jedan od utemeljitelja mehaničke interpretabilnosti)** — njegova objava
(`x.com/NeelNanda5/status/2110875974296654062`), kako je prenosi The Decoder:

1. **Nije pomak u velikoj slici:** rad je zanimljiv, ali „ne mijenja bitno cjelinu"; neuronska analiza može
   pomoći u praktičnim pitanjima (zašto je model učinio nešto sumnjivo) i lakše se primjenjuje na granične
   modele, **ali interpretabilnost nije blizu tome da je „razbijena"**; očekuje ozbiljne mane i propuste.
2. **Superpozicija još stoji:** jezični modeli **pamte više činjenica nego što imaju neurona**, a **slabe
   aktivacije** vjerojatno nose velik dio toga.
3. **Prijenos s malih slikovnih modela na jezične nije dokazan** — Nanda u to sumnja.
4. **„Monosemantičnost" je definirana preširoko** (uz priznanje da je autor provjerio vlastiti stari rad
   suvremenim alatima).

**I važna nijansa:** spor je dijelom **pojmovan**. Cammarata **ne spori** da model može predstavljati više
pojmova nego što ima dimenzija — Nanda ga u tome vidi kao suglasna. Sporno je uže: tvrdnja da mreža
**proizvoljno pakira posve nepovezane stvari**. Tko to pročita kao „superpozicije nema", pročitao je više
nego što obje strane tvrde.

## Što to znači za ovu knjigu

Esej govori o **unutarnjoj kompoziciji jednoga sustava**, ne o razinama stvarnosti. Za rukopis je koristan
na dva mjesta: (a) kao **mehanicistička potpora tvrdnji da model ima čitljivu unutarnju strukturu** — dakle
da je entitet na poziciji (razina 8, informacijski sustav; s kognitivnim svojstvima na 11), a ne „razina";
(b) kao **protuteza brzom zaključku da je distribuirana reprezentacija dokaz da razina nema**. Ali: esej
**ne pokazuje novu razinu, ni novo svojstvo koje niži sloj ne posjeduje** — pokazuje da su mehanizmi istoga
sustava čitljivi. Za tvrdnju o razini 14 to ne mijenja ništa; za tvrdnju o modelu kao entitetu daje joj
empirijsku podlogu koja se može citirati — uz Nandinu ogradu.

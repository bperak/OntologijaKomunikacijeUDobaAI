#!/usr/bin/env python3
"""check_lit.py — provjera dvaju smjerova citiranja.

Zašto postoji
-------------
Pravilo knjige je „nema rupa u citiranju": tvrdnja, citat i izvor stoje u istoj
rečenici, a nijedna se referencija ne pojavljuje bez izvora u `REFERENCE_BASE.md`.
Ta dva pravila idu u DVA smjera, a dosad se provjeravao samo jedan:

  (A) svaka jedinica u „### Literatura poglavlja" mora biti citirana u tekstu toga
      poglavlja  →  inače je popis nabujao referencijama koje poglavlje ne koristi;
  (B) svaki citat (Prezime Godina) u tekstu mora postojati u `REFERENCE_BASE.md`
      →  inače je citat bez pokrića.

Zamke koje su već prouzročile lažne nalaze (i zato su ugrađene u kod):
  - kratka prezimena (Kim, Liu, Wei, Huh) — ne traži se korijen od 6 znakova;
  - imena s velikim slovima u sredini (METR, EmoCNet, hrWaC) — ne traži se uzorak
    „veliko pa mala slova";
  - tipografski apostrof (O’Connor) — normalizira se prije usporedbe;
  - hrvatski padeži (Searleova, Gilberta, Tuomelu) — odbacuju se nastavci.

Pokretanje: python3 kod/check_lit.py   (izlaz 0 = čisto, 1 = ima nalaza)
"""
import glob
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REF = os.path.join(ROOT, "referencije", "REFERENCE_BASE.md")
RUK = os.path.join(ROOT, "rukopis")
NASLOV_LIT = "### Literatura poglavlja"

# riječi koje nisu prezime
STOP = {"et", "al", "i", "suradnici", "ur", "in", "the", "of", "and", "SEP", "OMLCC"}


def norm(s: str) -> str:
    """Ujednači apostrofe (O’Connor -> O'Connor)."""
    return s.replace("\u2019", "'").replace("\u2018", "'").replace("\u00b4", "'")


def prvi_token(entry: str):
    """Prva smislena riječ jedinice popisa (prezime ili naslov izvora)."""
    for t in re.findall(r"[A-Za-zŠĐČĆŽšđčćž][A-Za-zŠĐČĆŽšđčćž'’\-]*", entry):
        if t.lower() in {w.lower() for w in STOP}:
            continue
        return norm(t)
    return None


def prisutan(token, tekst: str) -> bool:
    """Je li prezime u tekstu — s kratkim korijenom za kratka prezimena."""
    if not token:
        return True
    return re.search(re.escape(token[:4] if len(token) >= 4 else token), tekst, re.I) is not None


def u_bazi(ime: str, baza: str) -> bool:
    """Je li prezime (ili njegov padežni oblik) u referentnoj bazi."""
    kandidati = {ime, ime[:-1], ime[:-1] + "a", ime.rstrip("a")}
    for suf in ("ova", "ov", "om", "a", "e", "u", "inu"):
        if ime.endswith(suf) and len(ime) - len(suf) > 2:
            kandidati.add(ime[: -len(suf)])
    return any(len(k) > 2 and k.lower() in baza for k in kandidati)


def main() -> int:
    baza = norm(open(REF, encoding="utf-8").read()).lower()
    popis_nalaza, citat_nalaza = [], []
    ukupno_jedinica = ukupno_citata = 0

    # Svi dijelovi rukopisa, ne samo poglavlja: od 17.9.2026. knjiga ima i uvod.md,
    # zakljucak.md, predgovor.md i studije slucaja. Oni nemaju popis „Literatura
    # poglavlja", pa se za njih provjerava samo smjer (B) — citat mora imati pokrice
    # u bazi. Bez toga bi uvod i zakljucak mogli citirati bez ikakve provjere.
    putanje = sorted(glob.glob(os.path.join(RUK, "**", "*.md"), recursive=True))
    bez_popisa = []
    for put in putanje:
        tekst = norm(open(put, encoding="utf-8").read())
        ime = os.path.relpath(put, RUK)
        if NASLOV_LIT not in tekst:
            bez_popisa.append(ime)
            tijelo = tekst
        else:
            tijelo, _, rep = tekst.partition(NASLOV_LIT)
            jedinice = [s.strip() for s in re.split(r"\s*·\s*", rep.split("\n\n", 1)[1].split("\n")[0]) if s.strip()]

            # (A) popis -> tekst
            for j in jedinice:
                ukupno_jedinica += 1
                if not prisutan(prvi_token(j), tijelo):
                    popis_nalaza.append(f"{ime}: „{j[:50]}\" je u popisu, a ne u tekstu poglavlja")

        # (B) tekst -> baza
        uzorak = re.compile(
            r"([A-ZŠĐČĆŽ][a-zšđčćž\-]{2,})(?:\s*(?:et al\.|i suradnici|&|i)\s*[A-ZŠĐČĆŽ][a-zšđčćž\-]+)?"
            r"\s*\(?((?:19|20)\d{2})"
        )
        for m in uzorak.finditer(tijelo):
            ukupno_citata += 1
            if not u_bazi(m.group(1), baza):
                citat_nalaza.append(f"{ime}: citat „{m.group(1)} {m.group(2)}" + "„ nema u REFERENCE_BASE.md")

    print("=== Provjera citiranja (oba smjera) ===")
    print(f"jedinica u popisima: {ukupno_jedinica} | citata u tekstu: {ukupno_citata}")
    if bez_popisa:
        print(f"\nℹ provjereno samo u smjeru (B) — bez popisa „{NASLOV_LIT}\": "
              + ", ".join(bez_popisa))
    if popis_nalaza:
        print("\n⚠ jedinice u popisu koje poglavlje ne citira:")
        for n in popis_nalaza:
            print("   -", n)
    if citat_nalaza:
        print("\n⚠ citati bez pokrića u REFERENCE_BASE.md:")
        for n in citat_nalaza:
            print("   -", n)
    if popis_nalaza or citat_nalaza:
        return 1
    print("\n✔ svi citati imaju izvor u bazi, a svi popisi odgovaraju tekstu")
    return 0


if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
"""mermaid_render.py — Mermaid → vektorski SVG (siguran za tisak) + PNG za pregled.

Dvije stvari koje ovaj alat rješava — obje su se stvarno dogodile:

1. **`foreignObject`.** Mermaid CLI (mmdc) upisuje natpise u SVG kao HTML unutar
   `<foreignObject>`. Vektorski rendereri (resvg, InDesign, LaTeX) takve natpise
   odbacuju i okviri ostaju prazni. Zato se svaki `foreignObject` prevodi u prave
   `<text>` elemente — i to **red po red**: razlomljeni natpis drži se kao više `<p>`
   redova, pa spajanje u jedan `<text>` čini natpis širim od okvira.

2. **Nesuglasje mjera fonta.** Širine okvira računa Chromium (mmdc), a ako PNG crta
   drugi renderer (resvg) s drugim fontom, tekst je širi od okvira i „izlazi" iz kućice.
   Zato se **PNG traži od poslužitelja** (crta ga isti Chromium koji je mjerio okvire),
   a u SVG-u se tekst dodatno umanjuje za `SIGURNOSNA_MARGINA` da u prijelomu ostane
   unutar okvira i kad se crta drugim fontom.

Zahtjevi: `paramiko` + `~/.ssh/id_hermes`; H2 poslužitelj na portu 3333 (skill
`mermaid-diagrams`); `resvg-py` samo kao rezerva ako poslužitelj ne vrati PNG.

Uporaba:
    python3 kod/mermaid_render.py                    # sve figure/izvori/*.mmd
    python3 kod/mermaid_render.py dijagram-4         # samo jedna
"""
import json
import os
import re
import sys
import unicodedata
from html import unescape

import paramiko

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
IZVORI = os.path.join(ROOT, "figure", "izvori")
FIG = os.path.join(ROOT, "figure")
HOST, USER, PORT = "72.62.48.157", "benedikt", 22
FONT, SIZE = "DejaVu Sans", 18.0
SIGURNOSNA_MARGINA = 0.92      # SVG: tekst 8 % manji od širine koju je izmjerio Chromium
FONT_PNG = 40                  # PNG: početna veličina fonta za izvoz iz Chromiuma
CILJ_PNG = 2200                # ciljna širina PNG-a u pikselima (za tisak ~150 mm / 300 dpi)
LOM_SIRINA = 300              # širina lomljenja natpisa (zadano mermaid: 200 → previše kratkih redaka)
# Uklanjaju se SAMO pravi emoji (kategorija So: 😀, ✅, 🟢 …), varijacijski selektori i
# nevidljivi spojnici. Ranija inačica bila je popis dopuštenih raspona i brisala je sve
# ostalo — pa su nestajale STRELICE (→, kategorija Sm), srednja točka (·, Po) i × :
# u dijagramu 13.1 natpis „Čovjek → agent" ispao je kao „Čovjek agent" (uočeno 2026-09-16).
EMOJI = re.compile(
    "[" + "".join(chr(c) for c in range(0x110000)
                  if unicodedata.category(chr(c)) in ("So", "Cs", "Co", "Cn")
                  or c in (0xFE0F, 0xFE0E, 0x200D)) + "]")


def fo_to_text(svg: str, font: str = FONT, size: float = SIZE, lh: float = 1.3) -> str:
    """<foreignObject> (HTML natpisi) → pravi SVG <text>, **red po red**.

    Svaki `<p>` unutar bloka je jedan red natpisa; prenosi se kao zaseban `<text>` uz
    okomito centriranje bloka u izvornome pravokutniku. `<br/>` u Mermaid izvoru zato
    služi kao pouzdana kontrola lomova.
    """
    def repl(m):
        blok = m.group(0)

        def attr(ime, zadano=0.0):
            g = re.search(rf'\b{ime}="([-\d.]+)"', blok)
            return float(g.group(1)) if g else zadano

        x, y, w, h = attr("x"), attr("y"), attr("width"), attr("height")
        izvori = re.findall(r"<p\b[^>]*>(.*?)</p>", blok, flags=re.S)
        if not izvori:
            izvori = [s for s in re.findall(r"<span\b[^>]*>(.*?)</span>", blok, flags=re.S)
                      if "nodeLabel" not in s]
        redovi = []
        for komad in izvori:
            # <br/> unutar istoga <p> je PRIJELOM REDA, ne razmak — inače se redovi spoje
            # i natpis postane širi od okvira (uočeno 2026-09-16 na četiri dijagrama)
            for dio in re.split(r"<br\s*/?>", komad, flags=re.I):
                cist = re.sub(r"\s+", " ", unescape(re.sub(r"<[^>]+>", " ", dio))).strip()
                if cist:
                    redovi.append(cist)
        if not redovi:
            cist = re.sub(r"\s+", " ", unescape(re.sub(r"<[^>]+>", " ", blok))).strip()
            if cist and "nodeLabel" not in cist:
                redovi = [cist]
        if not redovi:
            return ""

        # procjena širine najduljega reda (konzervativno: 0,60 × veličina po znaku);
        # ako prelazi okvir, veličina se smanjuje tako da u prijelomu ostane unutra
        najdulji = max(redovi, key=len)
        procjena = 0.60 * size * len(najdulji)
        velicina = size * min(SIGURNOSNA_MARGINA, (w * SIGURNOSNA_MARGINA) / procjena) if procjena > 0 else size
        visina_reda = velicina * lh
        y_prvi = y + h / 2 - (len(redovi) - 1) * visina_reda / 2 + velicina * 0.35
        return "".join(
            f'<text x="{x + w / 2:.1f}" y="{y_prvi + i * visina_reda:.1f}" text-anchor="middle" '
            f'font-family="{font}" font-size="{velicina:.1f}" fill="#333">'
            f'{r.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")}</text>'
            for i, r in enumerate(redovi))

    return re.sub(r"<foreignObject\b.*?</foreignObject>", repl, svg, flags=re.S)


def _lom_iz_izvora(kod: str) -> int:
    """Dopusti da izvor zada širinu lomljenja: prva linija `%% wrap: 200`."""
    m = re.search(r"^%%\s*wrap:\s*(\d+)", kod, flags=re.M)
    return int(m.group(1)) if m else LOM_SIRINA


def _kod_za_png(kod: str, font_px: int = FONT_PNG) -> str:
    """Isti dijagram, ali s većim fontom → Chromium izvozi PNG u većoj rezoluciji."""
    kod = EMOJI.sub("", kod)
    kod = re.sub(r"^%%\{init.*?\}%%\s*", "", kod, flags=re.S)
    # wrappingWidth je u PIKselima, pa se mora skalirati s fontom — inače se pri većem
    # fontu natpisi lome drugdje i izvoz ne pogodi ciljnu širinu (uočeno 2026-09-16)
    lom = round(_lom_iz_izvora(kod) * font_px / SIZE)
    return ('%%{init: {"flowchart": {"useMaxWidth": false, "wrappingWidth": ' + str(lom)
            + '}, "themeVariables": {"fontFamily": "' + FONT + '", "fontSize": "' + str(font_px) + 'px"}} }%%\n' + kod)


def _kod_za_svg(kod: str) -> str:
    kod = EMOJI.sub("", kod)
    if not kod.lstrip().startswith("%%"):
        kod = ('%%{init: {"flowchart": {"wrappingWidth": ' + str(_lom_iz_izvora(kod))
               + '}, "themeVariables": {"fontFamily": "' + FONT + '", "fontSize": "18px"}} }%%\n' + kod)
    return kod


def render(kod: str, format_: str = "svg"):
    """Pošalji Mermaid kod na H2; vrati SVG (s prevedenim natpisima) ili PNG (bytes)."""
    klijent = paramiko.SSHClient()
    klijent.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    klijent.connect(HOST, port=PORT, username=USER,
                    pkey=paramiko.RSAKey.from_private_key_file(os.path.expanduser("~/.ssh/id_hermes")),
                    timeout=20)
    try:
        sftp = klijent.open_sftp()
        with sftp.open("/tmp/mmd_payload.json", "w") as f:
            f.write(json.dumps({"code": kod, "format": format_, "theme": "default"}))
        izlaz = "/tmp/mmd_out." + format_
        _, out, err = klijent.exec_command(
            f"curl -s -X POST http://localhost:3333/render -H 'Content-Type: application/json' "
            f"-d @/tmp/mmd_payload.json -o {izlaz} && stat --format=%s {izlaz}", timeout=180)
        velicina = out.read().decode().strip()
        greska = err.read().decode().strip()
        if not velicina.isdigit() or int(velicina) < 200:
            raise RuntimeError(f"render nije vratio {format_} (stderr: {greska[:200]})")
        sftp.get(izlaz, "/tmp/mmd_local." + format_)
        sftp.close()
    finally:
        klijent.close()
    if format_ == "png":
        return open("/tmp/mmd_local.png", "rb").read()
    return fo_to_text(open("/tmp/mmd_local.svg", encoding="utf-8").read())


def main() -> int:
    cilj = sys.argv[1] if len(sys.argv) > 1 else None
    datoteke = sorted(f for f in os.listdir(IZVORI) if f.endswith(".mmd")) if os.path.isdir(IZVORI) else []
    if cilj:
        datoteke = [f for f in datoteke if cilj in f]
    if not datoteke:
        print("nema .mmd datoteka za zadani cilj")
        return 1
    for f in datoteke:
        ime = f[:-4]
        kod = open(os.path.join(IZVORI, f), encoding="utf-8").read()
        svg = render(_kod_za_svg(kod), "svg")
        open(os.path.join(FIG, ime + ".svg"), "w", encoding="utf-8").write(svg)
        natpisi = re.findall(r"<text[^>]*>([^<]+)</text>", svg)
        red = f"{ime}: SVG {len(svg)} znakova | foreignObject {svg.count('foreignObject')} | redova natpisa {len(natpisi)}"
        try:
            import io

            from PIL import Image
            # 1. prolaz: izmjeri prirodnu širinu pa povećaj font tako da PNG dođe na CILJ_PNG
            png = render(_kod_za_png(kod), "png")
            sirina = Image.open(io.BytesIO(png)).size[0]
            faktor = min(3.0, max(1.0, CILJ_PNG / max(sirina, 1)))
            if faktor > 1.05:
                png = render(_kod_za_png(kod, int(FONT_PNG * faktor)), "png")
            open(os.path.join(FIG, ime + ".png"), "wb").write(png)
            red += f" | PNG {Image.open(os.path.join(FIG, ime + '.png')).size} (Chromium, faktor {faktor:.2f})"
        except Exception as e:
            red += f" | PNG s poslužitelja nije prošao ({str(e)[:60]})"
            try:
                import resvg_py
                open(os.path.join(FIG, ime + ".png"), "wb").write(
                    bytes(resvg_py.svg_to_bytes(svg_string=svg, width=2000)))
                red += " → rezerva resvg (⚠ mjere fonta mogu se razlikovati)"
            except ImportError:
                red += " → rezerve nema"
        print(red)
    print("\n✔ gotovo")
    return 0


if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
"""Fabrique l'image de partage (og:image) d'une publication.

Les réseaux sociaux et les moteurs de réponse affichent cette vignette ;
c'est elle qui décide du clic. Plutôt qu'une photographie d'ambiance
identique sur tout le site, on y met le graphique central de l'étude,
dans la typographie du mémoire PDF (Latin Modern Roman et Inter).

    python3 outils/partage.py

Sortie : public/images/partage/<nom>.png, au format 1200 × 630.
Le rendu passe par Playwright, comme rendre.py, pour que le SVG soit
dessiné par un vrai moteur de rendu et non réinterprété.
"""

import sys
from pathlib import Path

from playwright.sync_api import sync_playwright

ICI = Path(__file__).resolve().parent
RACINE = ICI.parent
SORTIE = RACINE / "public" / "images" / "partage"

MARINE = "#162b4b"
OR = "#b4913c"
CREME = "#faf7f2"
ENCRE = "#13263b"

GABARIT = """<!doctype html>
<meta charset="utf-8">
<style>
  * {{ margin: 0; padding: 0; box-sizing: border-box; }}
  html, body {{ width: 1200px; height: 630px; }}
  body {{
    background: {creme};
    font-family: 'Inter', sans-serif;
    display: flex;
    flex-direction: column;
    padding: 44px 56px 0;
  }}
  .sur {{
    font-size: 17px;
    letter-spacing: .2em;
    text-transform: uppercase;
    color: {or_};
    font-weight: 500;
  }}
  h1 {{
    font-family: 'Latin Modern Roman', serif;
    font-weight: 400;
    font-size: 50px;
    line-height: 1.12;
    color: {encre};
    margin-top: 16px;
    max-width: 30ch;
  }}
  .graphique {{
    flex: 1;
    display: flex;
    align-items: center;
    justify-content: center;
    margin-top: 4px;
    min-height: 0;
  }}
  .graphique svg {{ width: 100%; height: auto; max-height: 100%; }}
  footer {{
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-top: 1px solid rgba(19, 38, 59, .22);
    padding: 16px 0 22px;
    font-size: 17px;
    color: {marine};
  }}
  footer .nom {{ font-family: 'Latin Modern Roman', serif; font-size: 22px; }}
  footer .pied {{ color: rgba(19, 38, 59, .62); }}
</style>
<p class="sur">{sur}</p>
<h1>{titre}</h1>
<div class="graphique">{svg}</div>
<footer>
  <span class="nom">sous-jacent</span>
  <span class="pied">{pied}</span>
</footer>
"""


def carte(svg: Path, sur: str, titre: str, pied: str, nom: str) -> Path:
    """Rend une carte 1200 × 630 et renvoie le chemin du PNG écrit."""
    corps = svg.read_text(encoding="utf-8")
    # On retire la déclaration XML : le fragment est inséré dans du HTML.
    corps = corps.split("?>", 1)[-1].strip()
    page = GABARIT.format(
        svg=corps, sur=sur, titre=titre, pied=pied,
        creme=CREME, or_=OR, encre=ENCRE, marine=MARINE,
    )
    SORTIE.mkdir(parents=True, exist_ok=True)
    cible = SORTIE / f"{nom}.png"
    with sync_playwright() as p:
        nav = p.chromium.launch()
        vue = nav.new_page(viewport={"width": 1200, "height": 630},
                           device_scale_factor=1)
        vue.set_content(page, wait_until="load")
        vue.screenshot(path=str(cible))
        nav.close()
    return cible


PUBLICATIONS = [
    dict(
        svg=RACINE / "public/graphiques/vicor-2005-2025/marge-brute.svg",
        sur="Étude n° 01 · Vicor Corporation",
        titre="45 M$ logés dans le chiffre d’affaires",
        pied="Vingt et un exercices retraités · 2005 – 2025",
        nom="vicor-2005-2025",
    ),
]

if __name__ == "__main__":
    for pub in PUBLICATIONS:
        chemin = carte(**pub)
        taille = chemin.stat().st_size / 1024
        print(f"{chemin.relative_to(RACINE)} — {taille:.0f} ko", file=sys.stderr)

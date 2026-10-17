#!/usr/bin/env python3
"""Prévient Bing (et donc une partie de ChatGPT et de Copilot) qu'une ou
plusieurs pages du site ont changé.

Usage :
    python3 outils/indexnow.py                      # toutes les URL du sitemap
    python3 outils/indexnow.py /etudes/vicor-2005-2025/   # une ou plusieurs pages

Prérequis : public/4a2ce6f19919a48da9e158308a584510.txt doit être déployé et
accessible à https://www.sousjacent.com/4a2ce6f19919a48da9e158308a584510.txt
"""

import json
import sys
import urllib.request
import xml.etree.ElementTree as ET

HOTE = "www.sousjacent.com"
SITE = f"https://{HOTE}"
CLE = "4a2ce6f19919a48da9e158308a584510"
SITEMAP = f"{SITE}/sitemap-0.xml"
NS = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}


def urls_du_sitemap():
    with urllib.request.urlopen(SITEMAP, timeout=30) as r:
        arbre = ET.fromstring(r.read())
    return [e.text for e in arbre.findall(".//sm:loc", NS)]


def main():
    chemins = sys.argv[1:]
    urls = [SITE + c if c.startswith("/") else c for c in chemins] or urls_du_sitemap()

    charge = {
        "host": HOTE,
        "key": CLE,
        "keyLocation": f"{SITE}/{CLE}.txt",
        "urlList": urls,
    }
    requete = urllib.request.Request(
        "https://api.indexnow.org/indexnow",
        data=json.dumps(charge).encode(),
        headers={"Content-Type": "application/json; charset=utf-8"},
        method="POST",
    )
    with urllib.request.urlopen(requete, timeout=30) as r:
        code = r.status

    print(f"{len(urls)} URL soumises — réponse {code}")
    print("200 ou 202 = accepté. 403 = la clé n'est pas accessible à keyLocation.")


if __name__ == "__main__":
    main()

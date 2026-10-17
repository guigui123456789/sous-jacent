# Outils de fabrication des PDF

Ces scripts régénèrent l'étude complète et le résumé de deux pages à
l'identique. Ils ne font pas partie du site : Astro ne les lit pas.

## Chaîne de fabrication

```bash
python3 build.py      # écrit etude-vicor.html   (30 pages)
python3 resume.py     # écrit resume-vicor.html  (2 pages)
python3 rendre.py etude-vicor.html  Etude-Vicor-2005-2025.pdf
python3 rendre.py resume-vicor.html Resume-Vicor-2005-2025.pdf
python3 normaliser.py Etude-Vicor-2005-2025.pdf Resume-Vicor-2005-2025.pdf
```

Puis copier les deux PDF dans `public/documents/`.

## Les fichiers

| Fichier | Rôle |
|---|---|
| `data.py` | les séries 2005-2025, les éléments non récurrents, le moteur de DCF |
| `charts.py` | les neuf graphiques en SVG, et l'emblème du site |
| `style.py` | la feuille de style d'impression : palette, grille, filigrane |
| `build.py` | assemble les trente pages de l'étude |
| `resume.py` | assemble les deux pages du résumé |
| `rendre.py` | rendu PDF par Playwright |
| `normaliser.py` | passe de robustesse (voir ci-dessous) |
| `assets/images.json` | les sept photographies, en bichromie, encodées en base64 |

## Deux pièges déjà rencontrés — ne pas les réintroduire

**1. Le rendu par `chromium --print-to-pdf` rétrécit la page.** Un seul
élément plus large que la feuille suffit à faire appliquer un facteur de
réduction à tout le document : les pages ne couvraient que 86 % de la
feuille et un liseré blanc apparaissait à droite et en bas. `rendre.py`
passe par Playwright avec `prefer_css_page_size`, et la mise en page des
pages vedettes utilise une boîte flexible plutôt qu'un positionnement
absolu, qui débordait de 62 mm.

**2. Les photographies viraient au rose dans les visualiseurs intégrés
aux navigateurs.** Deux causes cumulées : les JPEG étaient enregistrés en
mode progressif, et Chromium enrobait chaque image dans un espace
colorimétrique ICCBased que les visualiseurs n'appliquent pas tous de la
même façon. Les images doivent donc être enregistrées **en JPEG de base**
(`progressive=False`, sans profil ICC, sans marqueur Adobe APP14), et
`normaliser.py` doit être exécuté après chaque rendu pour ramener les
espaces colorimétriques à `DeviceRGB`. Contrôle :

```bash
pdfimages -list Etude-Vicor-2005-2025.pdf   # la colonne « color » doit dire rgb, jamais icc
```

`normaliser.py` pose aussi les métadonnées du document : titre, auteur,
éditeur, mention de droits et mots-clés.

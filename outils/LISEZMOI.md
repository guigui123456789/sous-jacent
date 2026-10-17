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

**2. Les pages de partie viraient au rose dans les visualiseurs intégrés
aux navigateurs.** La cause n'était pas l'image : c'était le **voile marine
semi-transparent** posé par-dessus en CSS. PDF.js, le moteur des
visualiseurs intégrés, rendait mal ce dégradé à transparence, et toute la
page basculait dans le magenta. Le voile est désormais **fusionné dans le
JPEG** par la fonction `voile()` du script de préparation des images : le
PDF ne contient plus aucune transparence sur ces pages, donc plus rien à
mal interpréter.

Par précaution, deux autres durcissements ont été conservés : les images
sont enregistrées **en JPEG de base** (`progressive=False`, sans profil
ICC, sans marqueur Adobe APP14), et `normaliser.py` ramène les espaces
colorimétriques à `DeviceRGB`.

```bash
pdfimages -list Etude-Vicor-2005-2025.pdf   # la colonne « color » doit dire rgb, jamais icc
```

**Comment vérifier pour de bon.** Les rendus par `pdftoppm` (poppler) et
par les visualiseurs de bureau ne reproduisent pas le défaut : ils sont
plus tolérants. Le seul test fiable est de rendre le PDF avec **PDF.js**,
le moteur des navigateurs :

```bash
npm install pdfjs-dist
# charger le PDF dans une page qui appelle pdfjsLib.getDocument(),
# rendre la page dans un <canvas>, et contrôler la couleur moyenne :
# une page de partie doit ressortir autour de (16, 28, 43), jamais R > B.
```

`normaliser.py` pose aussi les métadonnées du document : titre, auteur,
éditeur, mention de droits et mots-clés.

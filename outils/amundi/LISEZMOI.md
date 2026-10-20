# Étude n° 2 — Amundi : chaîne de fabrication du PDF

1. `build.py` lit le classeur (`amundi-comptes-2010-2025.xlsx`), `macro.json`, `etf.json` et `funds.json`, et écrit `amundi.html` (50 pages, A4).
2. `rendre.py` rend le PDF avec Playwright (Chromium).
3. `normaliser.py` ramène les images en DeviceRGB et pose les métadonnées. Contrôle : `pdfimages -list` → colonne color = rgb.
Polices : Bodoni Moda (fontsource) et Inter. Photos : Unsplash, JPEG de base sans profil ICC (voir crédits en annexe du PDF).
Les chemins absolus (/root/amundi/...) sont ceux du poste de travail du 20/10/2026 : à adapter.

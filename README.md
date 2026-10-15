# sous-jacent.com

Site statique Astro. Les articles sont des fichiers Markdown dans `src/content/`, que tu n'as pas besoin d'ouvrir à la main : tout passe par l'éditeur en ligne.

## Écrire un article (usage courant)

1. Va sur `https://sous-jacent.com/admin`
2. Connecte-toi avec GitHub
3. Choisis la rubrique (Le mécanisme / Les études / Les fondamentaux), clique « New »
4. Remplis le titre, le chapô, la date, écris le corps
5. Décoche « Garder en brouillon », puis « Publish »

Le site se reconstruit tout seul, en ligne en une à deux minutes. Ça marche aussi depuis le téléphone.

Un article coché « brouillon » reste invisible sur le site mais reste enregistré : utile pour écrire en plusieurs fois.

## Lancer le site en local (optionnel)

```
npm install
npm run dev        # http://localhost:4321
```

## Mise en ligne — ce qu'il reste à faire une seule fois

1. Créer un dépôt GitHub `sous-jacent` et y pousser ce dossier.
2. Dans `public/admin/config.yml`, remplacer `guigui123456789/sous-jacent` par le vrai `utilisateur/dépôt`.
3. Importer le dépôt dans Vercel (framework détecté automatiquement : Astro).
4. Brancher le domaine sous-jacent.com dans Vercel, puis mettre à jour les DNS chez le registrar.
5. Brancher l'authentification de l'éditeur : l'éditeur a besoin d'un petit service OAuth GitHub pour te connecter. Deux voies possibles, à choisir au moment du déploiement — une route serverless sur Vercel, ou l'authentification intégrée si le site est hébergé sur Netlify.

## Structure

```
src/content/mecanisme/     articles hebdo
src/content/etudes/        études mensuelles
src/content/fondamentaux/  fiches de méthode
src/pages/                 pages et routes
src/styles/global.css      toute l'identité visuelle (couleurs, typo)
public/admin/config.yml    les champs de l'éditeur en ligne
```

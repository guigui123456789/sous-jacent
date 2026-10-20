---
titre: "La duration : de combien un prix bouge quand les taux bougent"
rubrique: "Risque et taux"
chapo: "Un terme de vocabulaire qui sert à mesurer la sensibilité d'une obligation, et qui explique aussi pourquoi les actions de croissance souffrent quand les taux montent."
date: 2026-10-21
brouillon: false
---

La duration est un mot que l'on rencontre partout dans la finance de marché, et qui prête à confusion parce qu'il recouvre deux notions voisines. Dans les deux cas, il s'agit de répondre à la même question : **si les taux montent d'un point, de combien le prix baisse-t-il ?**

## Les deux définitions

- **La duration de Macaulay** est la durée de vie moyenne d'un instrument, pondérée par les flux. Chaque flux (coupon ou remboursement) est actualisé, puis on calcule le délai moyen auquel on récupère son argent, en donnant plus de poids aux flux les plus gros et les plus proches. Elle s'exprime en années.
- **La duration modifiée** est la duration de Macaulay divisée par (1 + le rendement). Elle donne directement la sensibilité : le prix varie d'environ « duration modifiée × variation du taux », avec le signe inverse.

```
Variation du prix ≈ − duration modifiée × variation du taux
```

## Un exemple chiffré

Une obligation de 10 ans, avec un coupon de 4 % et un rendement de 4 % (elle cote donc à 100) a une duration de Macaulay de 8,44 ans et une duration modifiée de 8,11.

- Si le taux passe de 4 % à 5 %, la formule donne une baisse d'environ 8,1 %. Le calcul exact, en réactualisant tous les flux à 5 %, donne un prix de 92,28, soit **-7,7 %**.
- Si le taux passe de 4 % à 3 %, la formule donne +8,1 % et le calcul exact **+8,5 %**.

L'écart entre la formule et le résultat exact vient de la **convexité** : la relation entre le prix et le taux est une courbe, pas une droite. La duration est la pente de la tangente. Pour de petites variations, elle suffit. Pour de grandes, la courbure joue, et elle joue en faveur du détenteur (la hausse est plus forte que la baisse pour un même écart de taux).

## Ce qu'il faut retenir de la duration d'une obligation

Elle augmente avec l'échéance et diminue avec le coupon. Un titre à 30 ans sans coupon a une duration égale à son échéance, soit 30 : c'est le plus sensible. Un titre à 2 ans qui verse un coupon élevé a une duration d'un peu moins de 2 : il est peu sensible. Un gérant qui anticipe une hausse des taux raccourcit la duration de son portefeuille ; celui qui anticipe une baisse l'allonge.

## Pourquoi cela concerne aussi les actions

Une action est, elle aussi, une suite de flux actualisés, mais sans échéance. Dans le modèle le plus simple (flux qui croissent à un taux constant *g*, actualisés au taux *r*), la duration de l'action vaut environ :

```
(1 + r) / (r − g)
```

Avec r = 8 % et g = 3 %, cela donne 1,08 / 0,05 = **21,6 ans**. Plus la croissance attendue est proche du taux d'actualisation, plus le dénominateur est petit, et plus la duration de l'action est longue.

C'est pourquoi les valeurs dont l'essentiel des profits est attendu dans longtemps (croissance forte, peu de bénéfices aujourd'hui) se comportent comme des obligations très longues : elles perdent plus quand les taux montent. Une société qui distribue l'essentiel de ses bénéfices maintenant a une duration plus courte, et souffre moins.

## Comment le lire

La duration ne prédit rien. Elle mesure une **exposition** : elle dit où l'on perd si les taux montent, pas s'ils vont monter. Elle est utile surtout en comparaison, pour savoir quelle ligne d'un portefeuille réagit le plus à un choc sur les taux, et pour comprendre qu'un portefeuille « d'actions » peut porter, sans que cela se voie, un risque de taux comparable à celui d'obligations longues.

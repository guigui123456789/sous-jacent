---
titre: "Markowitz et le ratio de Sharpe : pourquoi la diversification est le seul repas gratuit"
rubrique: "Portefeuille et risque"
chapo: "Le risque d'un portefeuille n'est pas la moyenne du risque de ses lignes. Un exemple à deux actifs montre pourquoi, comment se construit la frontière efficiente, et ce que mesure vraiment le ratio de Sharpe."
date: 2026-10-21
brouillon: false
---

En 1952, Harry Markowitz propose une idée qui paraît simple aujourd'hui : on ne juge pas un actif seul, mais par ce qu'il apporte à un portefeuille. Deux chiffres suffisent pour décrire un portefeuille : son **rendement espéré** et son **risque**, mesuré par l'écart-type des rendements (la volatilité).

## Le rendement est une moyenne, le risque n'en est pas une

Pour deux actifs A et B détenus avec les poids w et (1 − w) :

```
rendement du portefeuille = w × E(A) + (1 − w) × E(B)

variance du portefeuille = w² σA² + (1 − w)² σB² + 2 w (1 − w) ρ σA σB
```

Le rendement est la moyenne pondérée des rendements. Mais la variance contient un troisième terme, qui dépend de la **corrélation** ρ entre les deux actifs. Plus elle est faible, plus les fluctuations de l'un compensent celles de l'autre, et plus le risque du portefeuille tombe sous la moyenne des risques.

## Un exemple chiffré

Actif A : rendement espéré 8 %, volatilité 15 %. Actif B : rendement espéré 4 %, volatilité 6 %. Corrélation de 0,2. Un portefeuille 60 % A, 40 % B :

```
rendement = 0,6 × 8 % + 0,4 × 4 % = 6,4 %
volatilité = √[ (0,6×15 %)² + (0,4×6 %)² + 2×0,6×0,4×0,2×15 %×6 % ] = 9,77 %
```

La moyenne pondérée des volatilités serait de 0,6 × 15 % + 0,4 × 6 % = 11,4 %. Le portefeuille est donc à **9,77 %**, soit 1,6 point de moins, sans rien sacrifier sur le rendement. L'effet dépend directement de la corrélation :

| Corrélation | Volatilité du portefeuille 60/40 |
|---|---|
| +1,0 | 11,40 % (aucun gain) |
| +0,2 | 9,77 % |
| −0,5 | 8,07 % |

À corrélation de 1, on retrouve la moyenne : aucune diversification. À mesure que la corrélation baisse, le risque diminue pour le même rendement. C'est ce que l'on appelle **le seul repas gratuit de la finance** : le rendement attendu est inchangé, le risque baisse.

## La frontière efficiente

En faisant varier le poids w de 0 à 100 %, on trace l'ensemble des combinaisons possibles dans le plan (volatilité, rendement). Les portefeuilles situés sur la partie haute de la courbe, à partir du portefeuille de variance minimale, sont dits **efficients** : pour un niveau de risque donné, aucun autre ne rapporte davantage.

Dans l'exemple, le portefeuille de variance minimale est composé de 8 % d'A et 92 % de B. Il affiche une volatilité de 5,88 %, **plus basse que celle de l'actif le moins risqué pris seul** (6 %) : on réduit le risque en ajoutant un actif plus risqué. Son rendement est de 4,32 %.

## Le ratio de Sharpe

Pour comparer des portefeuilles de risques différents, William Sharpe propose de ramener le rendement **au-dessus du sans-risque** au risque pris :

```
Sharpe = (rendement du portefeuille − taux sans risque) ÷ volatilité
```

Avec un taux sans risque de 3 % :

| Portefeuille | Sharpe |
|---|---|
| A seul | (8 − 3) ÷ 15 = 0,333 |
| B seul | (4 − 3) ÷ 6 = 0,167 |
| 60 % A, 40 % B | (6,4 − 3) ÷ 9,77 = **0,348** |
| Optimum (54,5 % A) | **0,349** |

Le mélange a un meilleur ratio que **chacun de ses composants**. C'est le résultat de la diversification : pour un même risque, on obtient un meilleur excès de rendement. Le point qui maximise le ratio (ici environ 54,5 % d'A, rendement de 6,18 %, volatilité de 9,12 %) est le **portefeuille tangent**. Combiné avec du sans-risque, il offre la meilleure droite de choix pour tout investisseur, quelle que soit son aversion au risque : c'est le point de départ du MEDAF.

## Les limites

- **Les entrées sont des estimations.** Rendements espérés, volatilités et corrélations sont tirés de l'histoire. L'optimiseur amplifie les erreurs : un petit changement d'hypothèse déplace fortement les poids (on dit qu'il « maximise les erreurs »).
- **Les corrélations ne sont pas stables.** Elles montent en période de crise, précisément quand la diversification serait la plus utile.
- **La volatilité n'est pas tout le risque.** Elle traite pareillement un mouvement à la hausse et à la baisse, et ignore les queues épaisses : c'est l'objet de la fiche sur la VaR et l'*expected shortfall*.
- **Le Sharpe se manipule.** Un fonds qui vend des options hors de la monnaie a un excellent Sharpe jusqu'au jour où il perd tout : la volatilité passée ne voit pas le risque rare.

## Ce qu'il faut en retenir

Un actif se juge par sa contribution au portefeuille, pas isolément. Et un ratio de Sharpe se lit toujours avec la question : **sur quelle période, avec quelle hypothèse sur les queues ?** Un chiffre élevé obtenu sur une période calme n'est pas une preuve de robustesse.

---
titre: "Black-Scholes-Merton : valoriser une option sans prédire le cours"
rubrique: "Dérivés"
chapo: "La formule qui donne le prix d'un call ou d'un put européen, ce que représentent N(d1) et N(d2), un calcul complet à la main, et les cinq hypothèses qui la rendent fausse en pratique."
date: 2026-10-21
brouillon: false
---

Une option européenne donne le droit, sans l'obligation, d'acheter (*call*) ou de vendre (*put*) un actif à un prix fixé d'avance (le *strike*, noté K) à une date donnée. Le modèle de Black-Scholes-Merton (1973) donne son prix, et son apport décisif est de montrer qu'**il ne dépend pas de l'espérance de rendement de l'actif**.

## L'idée centrale : la réplication

On peut construire, à chaque instant, un portefeuille composé de l'actif sous-jacent et d'un emprunt sans risque qui reproduit exactement les gains de l'option. Si deux choses produisent les mêmes flux, elles valent le même prix, sinon on pourrait gagner sans risque en achetant l'une et en vendant l'autre (absence d'opportunité d'arbitrage). Le prix de l'option est donc le **coût de ce portefeuille de réplication**, et ce coût ne fait pas intervenir l'opinion de chacun sur l'avenir du cours : seule compte la volatilité.

## La formule

Pour un call, avec S le cours actuel, K le strike, T la durée en années, r le taux sans risque continu et σ la volatilité annuelle :

```
Call = S × N(d1) − K × e^(−rT) × N(d2)
Put  = K × e^(−rT) × N(−d2) − S × N(−d1)

d1 = [ ln(S/K) + (r + σ²/2) × T ] ÷ (σ × √T)
d2 = d1 − σ × √T
```

N(·) est la fonction de répartition de la loi normale centrée réduite.

## Un calcul complet

S = 100, K = 100, T = 1 an, r = 4 %, σ = 20 % :

```
d1 = [ ln(1) + (0,04 + 0,02) × 1 ] ÷ 0,20 = 0,30
d2 = 0,30 − 0,20 = 0,10
N(d1) = 0,6179     N(d2) = 0,5398

Call = 100 × 0,6179 − 100 × e^(−0,04) × 0,5398 = 9,93
Put  = 100 × e^(−0,04) × 0,4602 − 100 × 0,3821 = 6,00
```

Vérification par la parité call-put : Call − Put = S − K × e^(−rT), soit 9,93 − 6,00 = 3,92 et 100 − 96,08 = 3,92. Les deux membres sont égaux, ce qui valide le calcul.

## Ce que représentent N(d1) et N(d2)

- **N(d2)** est, dans un monde où l'on valorise comme si l'actif rapportait le taux sans risque, la probabilité que l'option soit dans la monnaie à l'échéance (ici 54 %). Ce n'est pas une probabilité réelle, mais une probabilité dite *risque-neutre*.
- **N(d1)** est le **delta** du call : le nombre d'actions à détenir pour répliquer l'option (ici 0,62 action). Le premier terme de la formule, S × N(d1), est la valeur de ce portefeuille d'actions, le second, l'emprunt à rembourser.

## Les trois leviers du prix

| Paramètre | Effet sur le call | Raison |
|---|---|---|
| Cours S plus haut | Hausse | Le droit d'acheter à K vaut davantage |
| Volatilité σ plus haute | Hausse (et pour le put aussi) | Le gain est illimité d'un côté, la perte bornée à la prime de l'autre : plus le cours bouge, plus l'asymétrie vaut cher |
| Durée T plus longue | Hausse en général | Plus de temps pour que l'option rapporte |

Le deuxième point est le plus contre-intuitif : **une option vaut plus cher quand le risque augmente**, parce que son détenteur ne subit que le côté favorable de ce risque.

## Les cinq hypothèses et leurs limites

1. **Volatilité constante.** Les marchés montrent le contraire : la volatilité implicite varie selon le strike (le *smile*) et la durée. On extrait d'ailleurs la volatilité implicite en inversant la formule à partir du prix observé.
2. **Rendements log-normaux, sans saut.** Les krachs sont plus fréquents que la loi normale ne le prévoit (queues épaisses).
3. **Réplication continue et sans coûts.** En pratique, on réajuste par intervalles, avec des frais d'exécution.
4. **Taux sans risque constant et emprunt illimité.**
5. **Option européenne, sans dividendes.** Les options américaines (exerçables avant l'échéance) et les dividendes demandent des extensions du modèle.

## Ce qu'il faut en retenir

Black-Scholes-Merton ne dit pas ce que vaut l'option, mais **ce qu'elle coûte à couvrir**, sous des hypothèses que l'on sait imparfaites. Sa valeur est de fournir un langage commun : on n'échange pas des prix, on échange des volatilités implicites. Avec un prix d'option observé, la formule renseigne sur ce que le marché croit de l'incertitude à venir, ce qui est exactement la logique du DCF inversé appliquée aux dérivés.

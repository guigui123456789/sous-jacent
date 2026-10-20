---
titre: "La valeur terminale : pourquoi l'essentiel d'une valorisation se joue après la dernière année"
rubrique: "Valorisation"
chapo: "On ne projette pas une entreprise à l'infini : on projette dix ans, puis on résume le reste en un nombre. La formule de Gordon-Shapiro, ses trois paramètres, et le poids qu'elle prend dans le résultat."
date: 2026-10-21
brouillon: false
---

Un modèle de flux actualisés projette les flux de trésorerie sur un horizon explicite, en général cinq à dix ans. Mais l'entreprise est supposée continuer après. Pour ne pas projeter indéfiniment, on résume tout ce qui vient après la dernière année en un seul nombre : la **valeur terminale**.

## La formule de Gordon-Shapiro

Si le flux de trésorerie libre (le free cash flow) croît ensuite à un taux constant *g*, et qu'on l'actualise au taux *r*, la valeur à la fin de l'horizon est :

```
Valeur terminale = flux de l'année suivante ÷ (r − g)
                 = flux de la dernière année × (1 + g) ÷ (r − g)
```

Elle n'est valide que si *g* est strictement inférieur à *r*. Dans le cas contraire, la valeur serait infinie, ce qui n'a pas de sens.

## Un exemple chiffré

Le flux de la dixième année est de 100. On retient r = 8 % et g = 2 % :

```
Valeur terminale = 100 × 1,02 ÷ (0,08 − 0,02) = 1 700
```

Cette valeur se situe à la fin de la dixième année. Pour la ramener à aujourd'hui, on l'actualise : 1 700 ÷ 1,08¹⁰ = **787**.

## Pourquoi c'est le point le plus sensible du modèle

Faisons varier un seul paramètre à la fois :

| Hypothèses | Valeur terminale | Valeur actuelle |
|---|---|---|
| r = 8 %, g = 2 % | 1 700 | 787 |
| r = 8 %, g = 3 % | 2 060 | 954 (+21 %) |
| r = 9 %, g = 2 % | 1 457 | 616 (−22 %) |

Un point de croissance perpétuelle de plus, ou un point de taux de plus, déplace la valeur de plus de 20 %. Et c'est cette valeur-là qui pèse le plus lourd : dans l'étude Vicor, la valeur terminale représente 65,5 % de la valeur centrale. Autrement dit, près des deux tiers du prix reposent sur ce qui se passera au-delà de l'horizon que l'on a pris la peine de projeter.

## Comment choisir *g*

Le taux de croissance à l'infini doit rester **cohérent avec l'économie** : une société ne peut pas croître indéfiniment plus vite que l'économie dans laquelle elle opère. En pratique, on le borne par la croissance nominale de long terme (inflation plus croissance réelle), soit en général 2 à 3 % pour les économies développées. Un *g* de 5 % à perpétuité signifie que l'entreprise finira par devenir l'économie entière.

Le flux terminal doit aussi être **normalisé** : une marge exceptionnelle ou un niveau d'investissement inférieur à la normale ne peuvent pas être prolongés à l'infini. Un flux terminal qui suppose des investissements inférieurs à l'amortissement détruit son propre actif au fil du temps.

## L'autre méthode : le multiple de sortie

Au lieu de Gordon-Shapiro, on peut valoriser la fin d'horizon par un multiple (par exemple un multiple de l'EBITDA observé sur des sociétés comparables). C'est plus simple, mais cela revient à importer le niveau de valorisation d'aujourd'hui dans l'avenir, y compris s'il est excessif. Les deux méthodes se vérifient mutuellement : un multiple de sortie qui implique un *g* irréaliste est un signal d'alerte.

## Ce qu'il faut en retenir

La valeur terminale n'est pas un détail technique mais l'endroit où se loge la plus grande part de l'incertitude. Une valorisation sérieuse doit donc dire quelle part du prix elle représente, quel *g* elle suppose, et ce qui se passe si l'on se trompe d'un point.

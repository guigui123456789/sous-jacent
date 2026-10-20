---
titre: "Courbe zéro-coupon et taux forward : ce que le marché dit des taux de demain"
rubrique: "Risque et taux"
chapo: "Comment passer des rendements des obligations à une courbe de taux zéro-coupon par la méthode du bootstrap, puis en extraire les taux à terme implicites. Un exemple chiffré sur trois maturités."
date: 2026-10-21
brouillon: false
---

Quand on parle de « la courbe des taux », on désigne en fait plusieurs objets. La courbe affichée dans la presse est celle des **rendements à maturité** d'obligations d'État de durées différentes. Mais ces obligations versent des coupons, qui tombent à des dates différentes : on ne peut donc pas actualiser un flux à cinq ans avec le rendement d'une obligation qui verse aussi des flux à un, deux, trois ans. La bonne courbe pour actualiser est la courbe des **taux zéro-coupon**.

## Le taux zéro-coupon

Le taux zéro-coupon à *n* ans, noté z(n), est le rendement d'un placement qui ne verse aucun flux intermédiaire : on place 1 aujourd'hui, on reçoit (1 + z(n))^n dans *n* ans. Chaque flux d'une obligation, à sa date, doit être actualisé avec **le taux zéro-coupon de cette date**, et non avec un taux unique.

## Le bootstrap : reconstruire les taux zéro-coupon

On part d'obligations cotant au pair (le rendement est égal au coupon) et on en déduit les taux zéro-coupon de proche en proche. Données de l'exemple, en coupons annuels :

| Maturité | Rendement au pair |
|---|---|
| 1 an | 3,00 % |
| 2 ans | 3,50 % |
| 3 ans | 4,00 % |

**Un an.** L'obligation ne verse qu'un flux : z(1) = 3,00 %.

**Deux ans.** Une obligation au pair vaut 1 et verse un coupon de 0,035 à un an, puis 1,035 à deux ans :

```
1 = 0,035 ÷ (1 + z1) + 1,035 ÷ (1 + z2)²
1 = 0,035 ÷ 1,03 + 1,035 ÷ (1 + z2)²   →   z2 = 3,509 %
```

**Trois ans.** Même principe, avec les deux taux déjà trouvés :

```
1 = 0,04 ÷ 1,03 + 0,04 ÷ (1,03509)² + 1,04 ÷ (1 + z3)³   →   z3 = 4,027 %
```

La courbe zéro-coupon (3,00 %, 3,51 %, 4,03 %) est un peu plus pentue que celle des rendements (3,00 %, 3,50 %, 4,00 %), parce qu'un rendement à maturité est une sorte de moyenne des taux zéro-coupon de ses flux. Plus la courbe est pentue, plus l'écart grandit.

## Les taux forward : ce que la courbe implique

Un taux *forward* (ou à terme) est le taux d'une période future, implicite dans la courbe d'aujourd'hui. Il vient d'un raisonnement d'arbitrage : placer 1 pendant deux ans doit donner le même résultat que le placer un an puis le replacer un an au taux forward.

```
(1 + z2)² = (1 + z1) × (1 + f(1,2))
f(1,2) = (1,03509)² ÷ 1,03 − 1 = 4,020 %
```

Le taux d'un an, **dans un an**, est de 4,02 %. De même :

```
f(2,3) = (1,04027)³ ÷ (1,03509)² − 1 = 5,072 %
```

| Période | Taux zéro-coupon | Taux forward annuel |
|---|---|---|
| 0 à 1 an | 3,00 % | 3,00 % |
| 1 à 2 ans | (moyenne : 3,51 %) | 4,02 % |
| 2 à 3 ans | (moyenne : 4,03 %) | 5,07 % |

Le taux zéro-coupon est une moyenne ; **le taux forward est le taux marginal**, celui de chaque année supplémentaire. Quand la courbe monte, les forwards sont au-dessus des taux zéro-coupon, et ils montent plus vite.

## Comment on s'en sert

- **Valoriser** : chaque flux se valorise avec son propre taux zéro-coupon, ce qui est exact pour n'importe quelle obligation, au pair ou non.
- **Lire les anticipations** : un taux forward est le taux de réinvestissement qui laisse indifférent entre deux placements. Si le marché anticipait un taux d'un an dans un an de 4,02 %, c'est le niveau à partir duquel on ne gagne ni ne perd à choisir l'un ou l'autre. On l'appelle souvent « l'anticipation du marché », mais c'est un raccourci.
- **Détecter la prime de terme** : un taux forward n'est pas la prévision du taux futur. Il contient aussi une compensation pour le risque de se tromper. Le taux qui sera effectivement observé dans un an diffère presque toujours du forward, dans un sens ou dans l'autre.

## Le lien avec la pentification de la courbe

Dans le mécanisme de la semaine consacré à la pentification avant une décision de banque centrale, l'écart entre le deux ans et le dix ans s'ouvre quand le marché change d'avis sur la trajectoire des taux directeurs. En langage de forwards : **les taux forward des premières années se déplacent d'abord, ceux de long terme ensuite**, et c'est ce qui modifie la forme de la courbe avant même la décision.

## Les limites

Le bootstrap suppose des obligations liquides cotant exactement au pair et des maturités régulièrement espacées. En pratique, les opérateurs ajustent une courbe lisse à des dizaines de titres par des méthodes d'interpolation (splines, modèle de Nelson-Siegel), et le choix de la méthode change les forwards de quelques points de base. Les forwards lointains sont très sensibles à ces choix : une petite erreur sur un taux zéro-coupon se multiplie dans le calcul.

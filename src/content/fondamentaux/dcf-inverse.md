---
titre: "Le DCF inversé : que faut-il croire pour justifier le cours ?"
rubrique: "Valorisation"
chapo: "Au lieu de calculer un prix à partir d'hypothèses, on part du prix pour retrouver les hypothèses. C'est la question centrale de ce site, et la méthode la plus honnête pour lire un cours."
date: 2026-10-21
brouillon: false
---

Une valorisation classique par les flux actualisés (le *DCF*, *discounted cash flow*) va dans un sens : on pose des hypothèses sur la croissance, la marge et le taux, et l'on en déduit une valeur. Le DCF inversé fait l'inverse : **on prend le cours comme donné, et l'on cherche quelles hypothèses le rendent juste.**

## Pourquoi renverser la question

Un DCF direct produit un chiffre précis à partir d'hypothèses incertaines, ce qui donne une impression de rigueur qu'il n'a pas. Le DCF inversé évite ce piège : il ne dit pas « l'action vaut X », il dit « pour que l'action vaille son prix, **il faut croire que...** ». Le lecteur peut alors juger lui-même si cette croyance est plausible, en la comparant à l'histoire de l'entreprise.

C'est aussi la raison pour laquelle cette approche est compatible avec la pédagogie : elle outille au lieu de prophétiser.

## La version la plus simple

Pour une société dont on attend un flux de trésorerie libre *F* l'an prochain, valorisée à la valeur d'entreprise VE, la formule de Gordon-Shapiro donne VE = F ÷ (r − g). On l'inverse :

```
g = r − F ÷ VE
```

**Exemple.** VE de 2 000, flux de l'an prochain de 80, taux d'actualisation de 8 % :

```
g = 8 % − 80 ÷ 2 000 = 8 % − 4 % = 4 %
```

Le marché paie donc comme si cette société devait croître de **4 % par an à perpétuité**. Si la croissance nominale de long terme de l'économie est de 2 à 3 %, ce chiffre est trop élevé : pour que le cours tienne, il faut supposer une phase de croissance plus rapide d'abord, ou une marge qui monte.

Le rendement du flux (80 ÷ 2 000 = 4 %) est ici la clé : plus il est bas, plus le cours suppose de croissance future.

## La version complète : retrouver la marge ou la croissance

Dans un vrai modèle, on fixe tous les paramètres sauf un, que l'on résout :

- **La croissance** : quel taux de croissance du chiffre d'affaires sur dix ans justifie le cours, à marge et taux donnés ?
- **La marge** : quelle marge opérationnelle à maturité est nécessaire, à croissance et taux donnés ?
- **Le taux** : quel rendement implicite offre le cours, si les flux se réalisent comme prévu ?

La deuxième question est celle que pose l'étude Vicor : une société qui a dégagé 3,5 % de marge opérationnelle en moyenne sur vingt et un ans est valorisée comme si elle devait atteindre 33 %. On ne dit pas que c'est impossible. On dit ce qu'il faut croire, et on le compare à l'histoire : ici, une marge multipliée par plus de neuf par rapport à la moyenne passée.

## Le test de plausibilité

Le résultat se lit en le comparant à trois références :

| Hypothèse implicite | Référence de comparaison |
|---|---|
| Croissance à l'infini | Croissance nominale de l'économie |
| Croissance sur dix ans | Meilleure décennie historique de la société, et du secteur |
| Marge à maturité | Marge moyenne et marge maximale observées sur le cycle |

Si l'hypothèse implicite dépasse nettement la meilleure performance déjà observée, le cours repose sur une rupture. Une rupture est possible, mais elle se justifie par un fait précis (un produit, un brevet, une position de marché), pas par le seul niveau du cours.

## Les limites

- Le résultat dépend du taux d'actualisation retenu, qu'il faut donc publier et faire varier.
- Un cours reflète des attentes très diverses, pas une seule croyance : le DCF inversé en donne une lecture moyenne.
- Il ne dit pas si le cours est « trop haut » : il dit ce qu'il faudrait croire, et laisse le jugement au lecteur.

Ce dernier point est essentiel. Le DCF inversé ne fournit pas de verdict, et c'est ce qui en fait un outil d'analyse plutôt qu'une recommandation.

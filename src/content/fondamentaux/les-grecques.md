---
titre: "Les grecques : lire le risque d'une option en cinq chiffres"
rubrique: "Dérivés"
chapo: "Delta, gamma, vega, theta, rho : chaque lettre mesure la réaction du prix d'une option à un paramètre. Un exemple chiffré complet, et la manière dont une table de trading s'en sert pour se couvrir."
date: 2026-10-21
brouillon: false
---

Le prix d'une option dépend de cinq paramètres : le cours du sous-jacent, la volatilité, le temps, le taux sans risque (et le strike, fixe). Les **grecques** sont les dérivées partielles du prix par rapport à chacun. Elles répondent à une question de gestionnaire : *si tel paramètre bouge d'un cran, de combien mon option change-t-elle de valeur ?*

On reprend le call de la fiche sur Black-Scholes-Merton : S = 100, K = 100, T = 1 an, r = 4 %, σ = 20 %, prix de 9,93.

## Les cinq grecques

| Grecque | Mesure | Valeur ici | Lecture |
|---|---|---|---|
| **Delta** (Δ) | Variation du prix pour +1 sur le sous-jacent | 0,618 | Si le cours monte de 1, l'option gagne environ 0,62 |
| **Gamma** (Γ) | Variation du delta pour +1 sur le sous-jacent | 0,0191 | Le delta passe de 0,618 à environ 0,637 si le cours monte de 1 |
| **Vega** (ν) | Variation du prix pour +1 point de volatilité | 0,381 | À 21 % de volatilité, l'option vaut 10,31 au lieu de 9,93 |
| **Theta** (Θ) | Variation du prix par jour qui passe | −0,0161 | L'option perd environ 1,6 centime par jour, toutes choses égales |
| **Rho** (ρ) | Variation du prix pour +1 point de taux | 0,519 | Un taux plus haut augmente un peu la valeur d'un call |

Le delta d'un put vaut le delta du call moins 1, soit −0,382 : il perd de la valeur quand le cours monte.

## L'approximation de Taylor, ou comment les grecques se combinent

Les grecques permettent d'estimer le nouveau prix sans refaire tout le calcul. Pour un cours qui passe de 100 à 102 :

```
nouveau prix ≈ prix + delta × ΔS + ½ × gamma × ΔS²
            ≈ 9,93 + 0,618 × 2 + ½ × 0,0191 × 4 = 11,20
```

Le prix exact par la formule complète est de 11,198. L'écart est de l'ordre du millième : l'approximation est excellente pour de petites variations. Avec le delta seul, on aurait obtenu 11,16, ce qui montre que **le gamma corrige la courbure** du prix (le prix d'un call n'est pas une droite en fonction du cours).

## Ce que chaque grecque dit du risque

- **Delta : l'exposition directionnelle.** Un portefeuille d'options à delta total de 5 000 se comporte, pour de petits mouvements, comme 5 000 actions. Une couverture *delta-neutre* consiste à neutraliser cette exposition en vendant le nombre d'actions correspondant.
- **Gamma : la stabilité de la couverture.** Un gamma élevé signifie que le delta change vite : la couverture doit être réajustée souvent. Un détenteur d'option (position longue) a un gamma positif : il profite des grands mouvements dans les deux sens. Un vendeur a un gamma négatif : il subit les grands mouvements, et doit racheter quand le marché monte et vendre quand il baisse.
- **Vega : l'exposition à la volatilité.** Elle est maximale pour une option à la monnaie et à longue échéance. Un trader qui achète une option achète en réalité de la volatilité.
- **Theta : le prix du temps.** C'est le coût quotidien de détenir un droit qui s'érode. Il est la contrepartie du gamma : **être long gamma coûte du theta**. C'est la même exposition vue sous deux angles : on paie chaque jour pour profiter, si le marché bouge, de mouvements plus larges que ceux anticipés.
- **Rho : l'exposition aux taux.** Souvent la plus faible pour les options courtes, elle devient importante pour les échéances longues.

## Un exemple de couverture

Une banque vend 1 000 calls identiques à celui ci-dessus. Son delta est de −618 (elle a vendu des calls) : elle achète 618 actions pour être neutre. Si le cours monte de 1, ses calls vendus perdent environ 618 et ses actions gagnent 618 : le résultat est nul **au premier ordre**.

Mais son gamma est négatif (−19,1) : après la hausse, le delta des calls est devenu −637, elle doit acheter 19 actions de plus, plus cher. Si le cours baisse, elle doit en vendre, moins cher. Elle perd à chaque aller-retour : c'est le coût de couverture que la prime encaissée doit payer. Si la volatilité réalisée dépasse la volatilité vendue, la prime ne suffit pas.

## Les limites

Les grecques sont des **pentes locales** : elles valent pour de petits mouvements et changent quand le marché change. Elles supposent le modèle juste (volatilité constante), alors que la volatilité elle-même bouge, ce qui rend le vega instable. Dans une journée de forte tension, la couverture delta peut échouer parce que le marché saute d'un niveau à un autre sans permettre de réajuster.

C'est pourquoi les desks surveillent aussi des grecques d'ordre supérieur (vanna, volga) et pratiquent des tests de scénarios, et ne se contentent pas des cinq lettres.

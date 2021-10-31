# PROJET DE WEB SCRAPING ET DEEP LEARNING
## DETECTION DE PLAQUE D'IMMATRICULATION
![Cchéma global du projet](./img/img1.jpg)
### SOMMAIRE
  - [Objectif du projet](#Objectif-du-projet)
  - [Méthodologie appliquée](#Méthodologie-appliquée)
  #### Full Deep Learning
  - [Modèle CNN](#Modèle-CNN)
  - [Modèle AutoEncodeur Apprentissage semi supervisé](#Modèle-AutoEncodeur-Apprentissage-semi-supervisé)
  - [Modèle GAN et DCGAN](#Modèle-GAN-et-DCGAN)
  - [Optimisation Modèle Full Deep Learning Renforcement Learning](#Optimisation-Modèle-Full-Deep-Learning-Renforcement-Learning)
  - [Supervising Tensorboard cas Modèle CNN](#Supervising-Tensorboard-cas-Modèle-CNN)
  - [Conclusion](#Conclusion)

#### Objectif du projet

L'objectif de ce projet est d'executer quelques modèles de deep learning après avoir scraper des données.

Les données scraper contiennent des informations sur des images des voitures de plusieurs pays montrant leur plaque d'immatriculation et les images elles mêmes.


#### Méthodologie appliquée

# Modèle CNN:

Detection de la plaque d'immatriculation : l'objectif du modèle est de permettre à detecter correctement les plaques d'immatriculations des différentes pays à travers un modèle CNN.Imaginez qu’un camera de surveillance n’arrive pas à détecter l’image d’une plaque d’immatriculation pour cause de la pluie,neige, partie d’image, …)

![image](https://user-images.githubusercontent.com/77580993/139585361-d9c0720f-9e7f-4ae3-b0a5-431ad2e67f10.png)


# Modèle AutoEncodeur (Apprentissage semi-supervisé)

Réduction de la dimensionnalité : le but de ce projet est de réduire la taille des entrées de nos images afin de le récréer à la sortie pour chaque phase.

C'est un cas simulaire au modèle ACP pour l'apprentissage non - spervisé La capacité de traiter un grand nombre de fonctionnalités rend l'apprentissage en profondeur très puissant lorsqu'il s'agit de données non structurées . ... Si les données sont trop simples ou incomplètes, il est très facile pour un modèle d'apprentissage en profondeur de devenir surajusté et de ne pas bien se généraliser à de nouvelles données.  

# Modèle DCGAN


# Optimisation Modèle Full Deep Learning Renforcement Learning

Dans cette partie nous allons nous inspiré de notre modèle de Q-learning pour l'automatisation d'un robot pour une entreprise logistique e-commerce un projet que nous devons présenter le mois  prochain pour le cours de Renforcement Learning.De ce fait, c'est plutôt un modèle simulaire à quelques différences près notre modèle Modeling-learnng c'est un modèle qui n'existe pas dans la réalité les techniques et les méthodes sont propres à nous.

Qu’est-ce qui se passe ? Si N = nombres d’images augmentent. Avec   N0 = 5000 images avec  N0 = Nombre d'images initials.NB: Le but est de trouver le model qui arrive à prédire correctement plus d’images que les autres. 

Nous allons aussi faire une différence absolue et rélative entre les modèles afin d'identifier le modèle  qui prédire plus d'images que les autres en comparant la distribution aléatoire et l'algorithme de THOMPSON SAMPLY .![image](https://user-images.githubusercontent.com/77580993/139585758-a871ba06-74c8-4fb6-8e25-91cb59d6c908.png)


![image](https://user-images.githubusercontent.com/77580993/139585705-95feecda-8f53-480c-b2d5-32a2d3ba4e96.png)



#### Supervising Tensorboard cas Modèle CNN

Dans cette partie nous allons utiliser la fonction callbalck pour répresenter les graphiques de model loss et d'accuracy.
La partie visualisation graphique ne sera pas introduit pour faute de temps mais on mettre le lien Tensorboard si possible.
DEMONSTRATION pendant le cours. 

## Conclusion



## DIFFULCUTES 

# Pour la PARTIE SCRAPY:

Scraper plusieurs pages : on avait un problème lorsque on utilisait la fonction urlibjoin pour passer de page à page lorsqu'on exécutait on avait bien les résultats mais vu que dans le site s'etendait jusqu'à plus de 100 PAGES.De ce fait, lorsqu'on mettait une limite de 100 pages , le script continuait et cela que nous avions corriger cela avec la fonction callbalck. 

 Pour la partie Deep Learning :

Problème rencontrer : lorsuq'on a voulu transformer notre variable prédict y en catégorie :

il fallait d'abord labeliser la variable y en convertisant la matrice name belgique en 1 et ...en
suite il fallait fit(FITER) les variables qui étaient en l'interieur de sorte eque nous puissions  les transformer en matrice résolution stack overflow.
 ValueError: invalid literal for int() with base 10: <s>.

# Limite :
Optimisation Modèle Full Deep Learning Renforcement Learning : Nous rappellons tout de même que la selection du meilleur modèle n'est possible que si les paramètres permettant d'obtenir le taux de conversion pour l'accuracy reste le même ceteris paribus(epoch,verbose, optimiser,...)
  



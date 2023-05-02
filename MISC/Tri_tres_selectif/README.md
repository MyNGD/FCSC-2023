
###Introduction

Ce challenge est un challenge d’algorithmie de la catégorie MISC. L’objectif de ce challenge est de trier un tableau dans l’ordre croissant avec un nombre limité de permutation.

###Résolution

Pour résoudre ce challenge, il faut trouver une méthode permettant de trier un tableau en effectuant le moins de mouvement possible.
Après quelque recherches sur internet, on tombe sur l’algorithme de tri rapide (QuickSort) qui le permet.
Vous pouvez retrouver cet algorithme [ici](https://www.geeksforgeeks.org/quick-sort/).

Après lecture de différents articles et après avoir compris le fonctionnement de l’algorithme. On crée un programme python qui implémente cet algorithme pour trier notre tableau.
Les étapes de résolutions sont donc:
<ul>
<li>Récupération du tableau non trié</li>
<li>Utilisation de l’algorithme QuickSort pour trier le tableau</li>
<li>Envoi du tableau trié au serveur.</li>
</ul>

Le script de résolution du challenge est le fichier ***solve.py***.

On exécute ensuite le script et on récupère le flag.


**FCSC{6d275607ccfba86daddaa2df6115af5f5623f1f8f2dbb62606e543fc3244e33a}**

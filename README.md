# Le gif: une image animée
# CreationGif

Projet de Bac spécialité ISN, en langage Python

Présentation du Projet
Le but de notre projet était de réaliser un gif, c'est-à-dire une image animée en utilisant
le langage informatique Python sur la plateforme Pyzo. L'image animée sera constituée de
plusieurs autres images compressées qui n’en formeront qu’une à la fin. Dans laquelle, une
bande défile horizontalement en affichant le négatif de l’image sur son passage.


# Explication du sujet

On cherche à obtenir une bande qui défile du haut vers le bas de l'image et qui affiche le négatif des
couleurs d'origine sur son passage. Pour cela, on aura besoin du module PIL de python.
A la fin du programme, on s'attend à obtenir une image animée sur laquelle défilera une bande qui
affichera le négatif de l'image localement.

# Interactions prévisibles utilisateur/programme

L’utilisateur choisit une image, l’enregistre sous le nom ‘Bac.jpg’. Ensuite, l’utilisateur clique
sur la touche F5 et le programme se déroulera pour créer le gif animé.

Après que l’utilisateur enregistre l’image et ait cliqué sur la touche F5, l’ordinateur va créer les
‘k’ nombres d’images nécessaires à la formation du gif animé. Puisque la bande qui affiche le négatif
de l’image doit défiler sur toute la hauteur de l’image choisie.

# Calculs mathématiques

On a calculé l'aire de la surface restante, c'est-à-dire l'aire au dessus et en dessous de la bande. Et
cela nous donne: Aire(surface_autour_bande)= (h-25)*l. On a aussi fait le calcul du nombre d'images necéssaires, qui varie en fonction de la hauteur de la
bande négative.

# Dossier Projet : Un site web explicatif

Lors de notre projet, il nous a été demandé de créer un site web avec du code html et du css, un site qui aborde tous les problèmes rencontrés, comment nous avons avancé dans ce projet etc.

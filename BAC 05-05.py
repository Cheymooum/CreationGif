# L'utilisateur doit choisir une image et la nommer 'Bac'
# Pour installer 'imageio', entrer : " conda install imageio " dans la console

##----- Importation des modules -----##
from PIL import Image
import imageio                                                      # ? Pour GIF ?
import numpy                                                        # ? Pour GIF ?

##----- Ouverture des Fichiers -----##
im = Image.open('Bac.jpg')

##----- Dimensions de l'image choisie par l'utilisateur -----##
couleur = im.mode
l, h = im.size
print('largeur : {} et hauteur : {}'.format(l, h)) # Donne largeur & longueur de l'image

##----- Creation d'une nouvelle image -----##
im_test = Image.new('RGB', (l, h)) #Creation d'une nouvelle image

##----- Bande Négative -----##
images = []                                                         # ? Pour GIF ?
k=0                                                                 # Compteur pour numéroter les nouvelles images

for i in range(-22,h):                                              # Boucle sur la verticale de l'image avec un rectangle qui se deplace sur                                                                       .                                                                     toute  la largeur l (la largeur du rectangle fait 25 pixels)

    a=i+22;                                                         # Encadrement complet de l'image avec "+22" en haut et "-22" en bas
    im_nega = Image.new(couleur, (l, h))                            # Symetrie horizontale
    for y in range(h):                                              # Pour y allant de 1 à h
       for x in range(l):                                           # On parcourt chaque pixel de l'image analysée plus haut
          r, v, b = im.getpixel((x,y))                              # Récupération tu triplet de couleur (saisi des pixels)
          im_nega.putpixel((x,y), (r,v,b))                          # Injection des pixels
            
    if a>h:                                                         # Si le bord > de l'image négative dépasse la largeur de l'image original .                                                                     .                                                                     alors, la largeur de la b-n devient de plus en plus petite jusqu'à 0.
        a=h
    
    if i<0:
        i=0                                                         # Même chose pour le bord supérieur (>) de l'image négative
            
    for y in range(i,a):                                            # Image négative de largeur 25
        for x in range(l):                                          # On parcourt chaque pixel de l'image analysée plus haut
            r, v, b = im.getpixel((x,y))                            # On récupère le triplet de couleur
            im_nega.putpixel((x, y ), (255-r, 255-v, 255-b))        # Injection des pixels négatif
                        
##----- Enregistrement et affichage des nouvelles images -----##

    k=k+1                                                           # Numérotation des nouvelles images
    im_nega.save('Im' + str(k) +'.png')                             # Enregistrement des nouvelles images en .png commencant par 'Im'
#    im_nega.show()                                                 # Visionage des nouvelles images dès le lancement du programme
##----- Création du GIF -----##

    images.append(numpy.asarray(im_nega))                           # ? Pour GIF ?
imageio.mimsave('BacAnimé.gif',images,duration = 0.0001)            # ? Pour GIF ?


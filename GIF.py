# L'utilisateur doit choisir une image et la nommer 'Bac'
##----- Importation des modules -----##
from PIL import Image
import os

##----- Ouverture des Fichiers -----##
im = Image.open('Bac.jpg')

##----- Dimensions de l'image choisie par l'utilisateur -----##
couleur = im.mode
l, h = im.size
print('largeur : {} et hauteur : {}'.format(l, h)) # Donne largeur & longueur de l'image

##----- Creation d'une nouvelle image -----##
im_test = Image.new('RGB', (l, h))
        
##----- Bande Négative -----##

k=0  
for i in range(-25,h):                     
    
    a=i+25;
    im_nega = Image.new(couleur, (l, h))              # Symetrie horizontale
    for y in range(h):
       for x in range(l):                            # On parcourt chaque pixel de l'image analysée plus haut   
          r, v, b = im.getpixel((x,y))          #Récupération tu triplet de couleur (saisi des pixels)
          im_nega.putpixel((x,y), (r,v,b))      #Injection des pixels
            
    if a>h:
        a=h
    
    if i<0:
        i=0
            
    for y in range(i,a):        #(depuis ligne 0)
        for x in range(l):                            # On parcourt chaque pixel de l'image analysée plus haut
            r, v, b = im.getpixel((x,y))            #Récupération tu triplet de couleur (saisi des pixels)
            im_nega.putpixel((x, y ), (255-r, 255-v, 255-b))      #Injection des pixels négatifs
            
##----- Enregistrement et affichage des nouvelles images -----##

    k=k+1       #Pour la numérotation des nouvelles images
    im_nega.save('Im' + str(k+1) +'.gif') #Nom des nouvelles images .jpg commencant par 'Im'+ Chiffre 'k+1'
   # im_nega.show()
   
##----- Création du gif -----##
os.system('convert -delay 30 -loop 0 *.gif animation.gif') 
# convert : convertir
# -delay : temps en ms entre chaque image pour simuler animation
# loop 0 : en boucle
# *.gif : tous les fichiers qui finissent par .gif dans le dossier
# animation.gif : nom du fichier image à obtenir

os.system('del Im*.gif')
# destruction des fichiers temporaires
# del : detruire (utiliser rem sous Linux)
# tous les fichiers nommés sous la forme image_*.gif
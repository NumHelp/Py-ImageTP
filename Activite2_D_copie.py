# -*- coding: utf-8 -*-
"""
Created on Wed Feb 20 15:07:13 2019

@author: frederic
"""
# PIL est une bibliothèque pour traiter les images
from PIL import Image

# ouverture de l'image pomme.jpg placée dans le repertoire de ce programme
#COMMENT1 J'ai réduit ton image pomme de 3000x4000pixels à 300x400pixels pour que le programme puisse s'exécuter beaucoup plus vite (VOIR FICHIER POMMEMINI.JPG)
img1=Image.open("pommemini.jpg")

# Récupération de la largeur et de la hauteur de l'image  en pixels :
largeur,hauteur=img1.size

# ouverture d’une nouvelle image  nommée img2
img2=Image.new('RGB',(largeur,hauteur))

# On parcourt pour chaque ligne de l'image

#COOMENT2 TU AVAIS MIS CECI "for i in range(hauteur):"
for i in range(largeur):
    #et chaque colonne :

    #COMMENT3 TU AVAIS MIS CECI "for j in range(largeur):"
    for j in range(hauteur):
        # On récupère les 3 composantes (r,v,b) du pixel de coordonnées (i,j) 
        r,v,b = img1.getpixel((i, j))
        
        pixel2 = (r,v,b)
        img2.putpixel((i, j), pixel2)

# On sauvegarde l'image modifiée dans pommecopie
img2.save("pommecopie.jpg" )
# on montre l’image :
img2.show()

# Pour exécuter ce programme, tu dois aller dans le SHELL (regarde à droite juste à coté de la Console). Ensuite dans le Shell, tu peux utiliser cette commande:
# python Activite2_D_copie.py
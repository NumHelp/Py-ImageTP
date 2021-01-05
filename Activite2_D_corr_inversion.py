# -*- coding: utf-8 -*-
"""
Created on Wed Feb 20 15:07:13 2019

@author: frederic
"""

from PIL import Image

# ouverture de l'image
# remarque : img1 est un nom de variable, vous pouvez mettre un autre nom à la place .
#COMMENT1 J'ai réduit ton image pomme de 3000x4000pixels à 300x400pixels pour que le programme puisse s'exécuter beaucoup plus vite (VOIR FICHIER POMMEMINI.JPG)
img1=Image.open("pommemini.jpg")

# Récupération de la largeur et de la hauteur de l'image  en pixels :
largeur,hauteur=img1.size
# ouverture d’une nouvelle image
# remarque : img2 est un nom de variable , vous pouvez mettre un autre nom à la place .
img2=Image.new('RGB',(largeur,hauteur))

# pour chaque ligne :
#COMMENT2 TU AVAIS MIS CECI "for i in range(hauteur):"
for x in range(largeur):
    #et chaque colonne :

    #COMMENT3 TU AVAIS MIS CECI "for j in range(largeur):"
    for y in range(hauteur):
        # Récupération des composantes RGB du pixel courant (triplet r,g,b).
        r,g,b = img1.getpixel((x, y))
        
        pixel2 = (g,r,b)
        img2.putpixel((x, y), pixel2)

# sauvegarde de img2 :
img2.save("pommeinv.jpg" )
# on montre l’image :
img2.show()
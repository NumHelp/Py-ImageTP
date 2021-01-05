# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 16:10:13 2019

@author: frederic
"""
#PIL est une bibliothèque qui permet de traiter les images.
import PIL.Image
img = PIL.Image.open('pomme.jpg')
exif_data = img._getexif()
print(exif_data)

# Pour exécuter ce programme, tu dois aller dans le SHELL (regarde à droite juste à coté de la Console). Ensuite dans le Shell, tu peux utiliser cette commande:
# python Activite1_D_ex3_programme.py
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 20 14:50:48 2019

@author: frederic
"""

from PIL import Image
img = Image.open("pomme.jpg")
r,v,b=img.getpixel((2000,2500))
print("canal rouge : ",r,"canal vert : ",v,"canal bleu : ",b)

# Pour exécuter ce programme, tu dois aller dans le SHELL (regarde à droite juste à coté de la Console). Ensuite dans le Shell, tu peux utiliser cette commande:
# python Activite2_B.py
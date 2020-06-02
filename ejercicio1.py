# -*- coding: utf-8 -*-
"""
Created on Sun May 31 2020
@author: williamhyuk
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt


img = cv2.imread('add_1.jpg', cv2.IMREAD_GRAYSCALE)

#Adecuamos los tamaños de Ambos archivos para que sean iguales
imgnew= cv2.resize(img,(324,324))
img2 = cv2.imread('add_2.jpg', cv2.IMREAD_GRAYSCALE)
imgnew2= cv2.resize(img2,(324,324))
res = cv2.imread('add_1.jpg', cv2.IMREAD_GRAYSCALE)

x,y = imgnew.shape #tomamos la altura y el ancho de la imagen 

#print(x,y)

for i in range(x):
    for j in range(y):
        #escalamos la imagen para evitar overflow 
        s=((imgnew[i][j]/2)+(imgnew2[i][j]/2))#Sumamos ambos valores de cada pixel
        #escalamos la imagen para evitar overflow    
        
        s=int(s) #Transmitimos la imagen a int, antes de la operación de agregar.

        if(s<0):
            res[i][j]=0
        elif(s>255):
            res[i][j]=255
        else:
            res[i][j]=s #el resultado lo guaradmos en el picxel de la imagen de salida

cv2.imshow('Resultado',res)
cv2.imwrite('res.png',res)

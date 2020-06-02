# -*- coding: utf-8 -*-
"""
Created on Sun May 2020
@author: williamhyuk
"""



import cv2
import numpy as np
from matplotlib import pyplot as plt

# Cargamos la imagen 
imagen = cv2.imread('add_10.jpg')

#Adecuamos los tamaños de Ambos archivos para que sean iguales
imgnew= cv2.resize(imagen,(832,543))
img2 = cv2.imread('add_11.jpg')
img2new= cv2.resize(img2,(832,543))

res = cv2.imread('add_10.jpg')

height, width, chanels=imagen.shape#tomamos la altura y el ancho de la imagen 

#recorremos los pixeles de la imagen
for i in range(height):
    for j in range(width):
        suma=(imgnew[i][j]/2)+(img2new[i][j]/2) #Sumamos ambos valores de cada pixel
        #escalamos la imagen para evitar overflow        
        res[i][j]=suma #el resultado lo guaradmos en el picxel de la imagen de salida

        
cv2.imshow('imagen final',res)
cv2.imwrite('res2.png',res)



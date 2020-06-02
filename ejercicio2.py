
import cv2
import numpy as np
from matplotlib import pyplot as plt

# Cargamos la imagen 
imagen = cv2.imread('add_10.jpg')

imgnew= cv2.resize(imagen,(832,543))
img2 = cv2.imread('add_11.jpg')
img2new= cv2.resize(img2,(832,543))

res = cv2.imread('add_10.jpg')

for i in range(height):
    for j in range(width):
        suma=(imgnew[i][j]/2)+(img2new[i][j]/2)        
        res[i][j]=suma

        
cv2.imshow('imagen final',res)
cv2.waitKey()
cv2.imwrite('res2.png',res)



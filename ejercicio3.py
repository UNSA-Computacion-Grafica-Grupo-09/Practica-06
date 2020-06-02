# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 21:08:17 2020

@author: MILAGROS PC
"""

import cv2
import os
import numpy as np
from matplotlib import pyplot as plt

def pixel_sustraction(folder, filename1, filename2):
    full_filename1 = os.path.join(folder, filename1)
    full_filename2 = os.path.join(folder, filename2)    
    img1 = cv2.imread(full_filename1,0)
    img2 = cv2.imread(full_filename2,0)
    img1 = img1.astype(int)
    img2 = img2.astype(int)
    
    alto1, ancho1 = img1.shape
    alto2, ancho2 = img2.shape
    
    for i in range(alto1):
        for j in range(ancho1):
            img1[i][j] = abs(img1[i][j] - img2[i][j])
            img1[i][j] = abs(img1[i][j] - 95)
            
    salidaImg1 = "img/prueba_salida.png" # en ez de img pones static
    cv2.imwrite(salidaImg1,img1)
    img = cv2.imread('img/prueba_salida.png',0) # en ez de img pones static
    
    alto,ancho = img.shape
    
    result = img
    
    
    for i in range(alto):
        for j in range(ancho):
            if (70 < img[i][j] and img[i][j] < 130):
                result[i,j]=255
            else:
                result[i,j]=0
	    
                
    img_result = result  # importante
    full_filename_new = os.path.join(folder, 'sustraImg' + filename1)  # importante
    cv2.imwrite(full_filename_new, img_result)  # importante

    return full_filename_new  # importante



pixel_sustraction('./img/','sub_1.jpg', 'sub_2.jpg')
    

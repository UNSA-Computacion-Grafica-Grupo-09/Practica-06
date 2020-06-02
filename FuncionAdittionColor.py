# -*- coding: utf-8 -*-
"""
Created on Mon Apr 01 2020
@author: williamhyuk
"""

import cv2
import numpy as np


def AdittionBN(folder, filename1,filename2):

	full_filename1 = os.path.join(folder, filename)#importante
	full_filename2 = os.path.join(folder, filename2)#importante

    	res= cv2.imread(full_filename)#importante
    	imagen= cv2.imread(full_filename , cv2.IMREAD_GRAYSCALE)
    	img2 = cv2.imread(full_filename2)#importante

	imgnew= cv2.resize(imagen,(832,543))
	
	img2new= cv2.resize(img2,(832,543))



	#x,y = imgnew.shape #tomamos la altura y el ancho de la imagen 


	height, width, chanels=imagen.shape#tomamos la altura y el ancho de la imagen 

	#recorremos los pixeles de la imagen
	for i in range(height):
	    for j in range(width):
	        suma=(imgnew[i][j]/2)+(img2new[i][j]/2) #Sumamos ambos valores de cada pixel
	        #escalamos la imagen para evitar overflow        
	        res[i][j]=suma #el resultado lo guaradmos en el picxel de la imagen de salida

	        

	img_result = res #importante
	full_filename_new = os.path.join(folder, 'AdittionColor' + filename) #importante
	cv2.imwrite(full_filename_new, img_result) #importante

	return full_filename_new #importante

AdittionColor('./img/' , 'AdittionColor.jpg')


 

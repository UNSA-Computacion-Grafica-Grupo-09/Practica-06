import cv2
import numpy as np


def AdittionBN(folder, filename1,filename2):

	full_filename1 = os.path.join(folder, filename)#importante
	full_filename2 = os.path.join(folder, filename2)#importante

    res= cv2.imread(full_filename)#importante
    img= cv2.imread(full_filename , cv2.IMREAD_GRAYSCALE)
    img2 = cv2.imread(full_filename2)#importante

	imgnew= cv2.resize(imagen,(324,324))
	
	imgnew2= cv2.resize(img2,(324,324))



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



	img_result = res #importante
	full_filename_new = os.path.join(folder, 'AdittionBN' + filename) #importante
	cv2.imwrite(full_filename_new, img_result) #importante

	return full_filename_new #importante

AdittionBN('./img/' , 'AdittionBN.jpg')

 
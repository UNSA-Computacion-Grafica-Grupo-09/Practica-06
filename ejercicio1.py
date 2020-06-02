import cv2
import numpy as np
from matplotlib import pyplot as plt


img = cv2.imread('add_1.jpg', cv2.IMREAD_GRAYSCALE)
imgnew= cv2.resize(img,(324,324))
img2 = cv2.imread('add_2.jpg', cv2.IMREAD_GRAYSCALE)

res = cv2.imread('add_1.jpg', cv2.IMREAD_GRAYSCALE)

x,y = imgnew.shape
print(x,y)

for i in range(x):
    for j in range(y):
        s=((imgnew[i][j]/2)+(img2[i][j]/2))
        s=int(s)

        if(s<0):
            res[i][j]=0
        elif(s>255):
            res[i][j]=255
        else:
            res[i][j]=s

#hisR = cv2.calcHist([res], [0], None, [256], [0, 256])
cv2.imshow('Resultado',res)
cv2.imwrite('res.png',res)


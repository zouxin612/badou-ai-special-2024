
import numpy as np
import cv2

def function(img):
    height,width,channels = img.shape
    emptyImage=np.zeros((800,800,channels),np.uint8)
    sh=800/height
    sw=800/width
    for i in range(800):
        for j in range(800):
            x=int(i/sh + 0.5)
            y=int(j/sw + 0.5)
            emptyImage[i,j]=img[x,y]
    return emptyImage

img=cv2.imread("lenna.png")
zoom=function(img)
print(zoom)
cv2.imshow("nearest interp",zoom)
cv2.imshow("1",img)
cv2.waitKey()
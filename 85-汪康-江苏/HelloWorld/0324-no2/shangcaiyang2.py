# -*- coding: utf-8 -*-
'''@Time: 2024/1/31 21:37
上采样2
'''

import cv2
import numpy as np


def function(img):
    height,width,channels = img.shape
    emptyImage = np.zeros((800,800,3),np.uint8)
    sh = 800/height
    sw = 800/width
    for i in range(800):
        for j in range(800):
            x = int(height*i/800+0.5)
            y = int(width*j/800+0.5)
            emptyImage[i,j] = img[x,y]
    return emptyImage

img = cv2.imread("../lenna.png")
print(img.shape)
zoom = function(img)
print(zoom)
print(zoom.shape)

cv2.imshow("nearest intert",zoom)
cv2.imshow("image",img)
cv2.waitKey(0)
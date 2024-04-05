'''
双线性插值
'''

import cv2
import numpy as np

def function(img):
    height, width, channels = img.shape
    print('height=%d, width=%d' % (height, width))
    emptyImage = np.zeros([800, 800, channels], np.uint8)
    sh = height/800
    sw = width/800
    for i in range(800):
        for j in range(800):
            x = int((i + 0.5) * sh - 0.5)
            y = int((j + 0.5) * sw - 0.5)
            emptyImage[i, j] = img[x, y]
    return emptyImage

img = cv2.imread('lenna.png')
zoom = function(img)
print(zoom)
print(zoom.shape)
cv2.imshow('nearest interp', zoom)
cv2.imshow('image', img)
cv2.waitKey(0)

# -*- coding: utf-8 -*-
"""
@author: Michael

彩色图像的灰度化、二值化
"""
from skimage.color import rgb2gray
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import cv2

config_value = "gray_two"

# 图像灰度化
img = cv2.imread("sj.jpg")
if config_value == "gray_one":
    h,w = img.shape[:2]                               #获取图片的high和wide
    img_gray = np.zeros([h,w],img.dtype)                   #创建一张和当前图片大小一样的单通道图片
    for i in range(h):
        for j in range(w):
            m = img[i,j]                             #取出当前high和wide中的BGR坐标
            img_gray[i,j] = int(m[0]*0.11 + m[1]*0.59 + m[2]*0.3)   #将BGR坐标转化为gray坐标并赋值给新图像
elif config_value == "gray_two":
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 图像黑白化（二值法）
img_gray_two = rgb2gray(img)
rows, cols = img_gray_two.shape
for i in range(rows):
    for j in range(cols):
        if (img_gray_two[i, j] <= 0.5):
            img_gray_two[i, j] = 0
        else:
            img_gray_two[i, j] = 1
img_binary = np.where(img_gray_two >= 0.5, 1, 0)


plt.subplot(221)
img = plt.imread("sj.jpg")
plt.imshow(img)
plt.subplot(222)
plt.imshow(img_gray, cmap='gray')
plt.subplot(223)
plt.imshow(img_binary, cmap='gray')
plt.show()

#图像放大(临近插值）
def function(img):
    height, width, channels = img.shape
    emptyImage = np.zeros((800, 800, channels), np.uint8)
    sh = 800 / height
    sw = 800 / width
    for i in range(800):
        for j in range(800):
            x = int(i / sh + 0.5)  # int(),转为整型，使用向下取整。
            y = int(j / sw + 0.5)
            emptyImage[i, j] = img[x, y]
    return emptyImage


# cv2.resize(img, (800,800,c),near/bin)

img = cv2.imread("sj.jpg")
zoom = function(img)
print(zoom)
print(zoom.shape)
cv2.imshow("nearest interp", zoom)
cv2.imshow("image", img)
cv2.waitKey(0)
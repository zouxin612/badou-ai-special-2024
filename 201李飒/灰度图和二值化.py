from skimage.color import rgb2gray
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import cv2

img = cv2.imread("lenna.png")
h,w = img.shape[:2]
img_gray = np.zeros([h,w],img.dtype)
for i in range(8):
    for j in range(8):
        m = img[i,j]
        img_gray[i,j] =int(m[0]*0.11+m[1]*0.59+m[2]*0.3)

print(img)
print(img_gray)
cv2.imshow("image show gray",img_gray)
cv2.waitKey()

img = plt.imread("lenna.png")
print(img)
img_gray = rgb2gray(img)
print(img_gray)



# 二值化
rows,cols = img_gray.shape
img_binary =np.zeros([rows,cols],img_gray.dtype)
for i in range(rows):
    for j in range(cols):
        if(img_gray[i,j]<= 0.5):
            img_binary[i,j] = 0
        else:
            img_binary[i,j]= 1

print(img_binary)
plt.subplot(221)
plt.imshow(img)
plt.subplot(222)
plt.imshow(img_gray,cmap="gray")
plt.subplot(223)
plt.imshow(img_binary,cmap="gray")
plt.show()





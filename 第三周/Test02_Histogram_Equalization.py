"""
@Date    : 2024/4/6 17:05
@Author  : zwx
@Version : 1.0
@Desc    : 直方图均衡化（图像增强）
"""

'''
单通道图像均衡化
函数： equalizeHist(src, dst=None)
src：图像矩阵(单通道图像)
dst：默认即可
'''
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('../data/input/lenna.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # 获取灰度图
dst = cv2.equalizeHist(gray)  # 直方图均衡化
# hist = cv2.calcHist([dst], [0], None, [256], [0, 256])  # 获取直方图

plt.figure()
plt.hist(dst.ravel(), 256)  # 展示均衡后的直方图
plt.show()

cv2.imshow("compare", np.hstack([gray, dst]))  # 原灰度图和增强后的图像同图对比
cv2.waitKey(0)

'''
彩色图像均衡化：本质上是拆分成单通道来均衡化，最后合并
函数： 函数相同
'''
img = cv2.imread("../data/input/lenna.png", 1)

(b, g, r) = cv2.split(img)  # 获取每一个通道的图像

# 对每一个通道图像均衡化
bH = cv2.equalizeHist(b)
gH = cv2.equalizeHist(g)
rH = cv2.equalizeHist(r)

# 合并每一个通道
result = cv2.merge((bH, gH, rH))

cv2.imshow("compare", np.hstack([img, result]))
cv2.waitKey(0)

cv2.waitKey(0)

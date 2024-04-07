"""
@Date    : 2024/4/6 17:30
@Author  : zwx
@Version : 1.0
@Desc    : 常用卷积核/滤波器 - Sobel边缘检测
"""
import cv2
import numpy as np

img = cv2.imread("../data/input/lenna.png", 0)

'''
Sobel函数求完导数后会有负值，还有会大于255的值。
而原图像是uint8，即8位正整数(范围在[0,255])，所以Sobel建立的图像位数不够，会有截断。
因此要使用16位有符号的数据类型，即cv2.CV_16S。
'''
x = cv2.Sobel(img, cv2.CV_16S, 1, 0)  # 基于纵向
y = cv2.Sobel(img, cv2.CV_16S, 0, 1)  # 基于横向

absX = cv2.convertScaleAbs(x)  # 转回原来的 uint8 类型的图像，否则将无法显示图像，而只是一副灰色的窗口。
absY = cv2.convertScaleAbs(y)

'''
dst = cv2.addWeighted(src1, alpha, src2, beta, gamma[, dst[, dtype]])  
其中alpha是第一幅图片中元素的权重，beta是第二个的权重
'''

dst = cv2.addWeighted(absX, 0.5, absY, 0.5, 0)  # 将纵横两个方向的计算结果合并，权重各占一半
# cv2.imshow("absX", absX)
# cv2.imshow("absY", absY)
# cv2.imshow("Result", dst)

cv2.imshow("x+y+all", np.hstack([absX, absY, dst]))
cv2.waitKey(0)

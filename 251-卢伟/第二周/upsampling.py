import cv2
import numpy as np


def upsampling(new_height, new_weight):
    # 拿原图
    # 定义新图
    # 从原图中获取像素值
    img = cv2.imread("C:\\Users\\1\\Desktop\\test1.png")
    h, w, c = img.shape

    #  缩放倍数
    hw = new_height / h
    ww = new_weight / w

    new_pic = np.zeros((new_height, new_weight, c), np.uint8)
    for i in range(new_height):
        for j in range(new_weight):
            oldh = int(i / hw + 0.5)  # 0.5 和int强转，起到四舍五入的作用
            oldw = int(j / ww + 0.5)
            new_pic[i, j] = img[oldh, oldw]
    cv2.imwrite("C:\\Users\\1\\Desktop\\upsampling1024.png", new_pic)


upsampling(2048, 2048)

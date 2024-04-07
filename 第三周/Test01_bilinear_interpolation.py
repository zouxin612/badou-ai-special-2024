"""
@Date    : 2024/4/6 16:16
@Author  : zwx
@Version : 1.0
@Desc    : 双线性插值算法demo
"""

import numpy as np
import cv2


def bilinear_interpolation(img, out_dim):
    src_h, src_w, channels = img.shape
    dst_h, dst_w = out_dim[1], out_dim[0]
    if src_h == dst_h and src_w == dst_w:  # 图像大小相同直接复制
        return img.copy()

    dst_img = np.zeros((dst_h, dst_w, channels), np.uint8)
    scale_y, scale_x = float(src_h) / dst_h, float(src_w) / dst_w  # 原图与新图的行列大小比值
    for i in range(channels):  # 对每个通道进行循环
        for dst_y in range(dst_h):  # 按行循环
            for dst_x in range(dst_w):  # 按列循环

                # 0.5 为固定平移值
                src_x = (dst_x + 0.5) * scale_x - 0.5  # 几何中心靠近： x 方向进行平移
                src_y = (dst_y + 0.5) * scale_y - 0.5  # 几何中心靠近： y 方向进行平移

                # 取最近四个点的值
                src_x0 = int(np.floor(src_x))  # 向下取整
                src_x1 = min(src_x0 + 1, src_w - 1)  # src_w-1 为列边界，不能越界
                src_y0 = int(np.floor(src_y))  # 列
                src_y1 = min(src_y0 + 1, src_h - 1)  # src_h-1 为行边界

                # 公式计算
                tmp0 = (src_x1 - src_x) * img[src_y0, src_x0, i] + (src_x - src_x0) * img[src_y0, src_x1, i]
                tmp1 = (src_x1 - src_x) * img[src_y1, src_x0, i] + (src_x - src_x0) * img[src_y1, src_x1, i]
                dst_img[dst_y, dst_x, i] = int((src_y1 - src_y) * tmp0 + (src_y - src_y0) * tmp1)

    return dst_img


if __name__ == '__main__':
    img = cv2.imread('../data/input/lenna.png')
    dst = bilinear_interpolation(img, (700, 700))
    cv2.imshow('bilinear interp', dst)
    cv2.waitKey()

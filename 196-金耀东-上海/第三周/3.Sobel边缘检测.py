import os
import cv2

def display_imgs(titles, imgs):
    for title, img in zip(titles, imgs):
        cv2.imshow(title, img)
        cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__" :
    # 设置图像路径
    img_dir = "img"
    img_filename = "lenna.jpg"
    img_path = os.path.join(img_dir, img_filename)

    # 读取RGB图像并计算灰度图
    src_img = cv2.imread(img_path)
    gray_img = cv2.cvtColor(src_img, cv2.COLOR_RGB2GRAY)

    # 水平方向进行边缘检测
    sobel_x = cv2.Sobel(gray_img, cv2.CV_64F, 1, 0, ksize=3)
    sobel_x = cv2.convertScaleAbs(sobel_x)

    # 垂直方向进行边缘检测
    sobel_y = cv2.Sobel(gray_img, cv2.CV_64F, 0, 1, ksize=3)
    sobel_y = cv2.convertScaleAbs(sobel_y)

    # 结合水平与垂直方向的计算结果
    sobel_img = cv2.addWeighted( sobel_x, 0.5, sobel_y, 0.5, 0)

    # 展示图像
    display_imgs(
        titles=["source image","gray image", "sobel x", "sobel y", "sobel image"],
        imgs=[src_img, gray_img, sobel_img, sobel_x, sobel_y, sobel_img]
    )

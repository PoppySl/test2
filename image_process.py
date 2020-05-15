from PIL import Image, ImageDraw, ImageEnhance
import matplotlib.pyplot as plt
import cv2 as cv
import numpy as np
import time

import glob


class ImageProcess:
    # def __init__(self, image):
    #     self.image = image
        # self.get_pixel = self.get_pixel()

    def grayscale(self, image, threshold=160):
        '''
        获取灰度转二值的映射table,0表示黑色,1表示白色
        :param threshold:  二值化阈值
        :return:
        '''
        imageName = image.split("/")
        print(imageName)
        image = Image.open(image)
        image = image.crop((0, 0, 110, 20))
        image = image.convert("L")  # 图片灰度化
        table = []
        for i in range(256):
            if i < threshold:
                table.append(0)
            else:
                table.append(1)
        image = image.point(table, '1')
        print(image)
        imageName = './GrayscaleImage/%s' % imageName[1]
        image.save(imageName, 'png')
        print('————————图片%s二值化成功————————' % imageName[1])
        return imageName

    def get_pixel(self, image, x, y, G, N):
        '''
        八邻域降噪，根据中心点上，下，左，右，左上，左下，右上，右下连通点个数进行噪点判断
        :param x: 中心点坐标
        :param y: 中心点坐标
        :param G: 阈值
        :param N:  0<N<8  连同点个数
        :return:
        '''
        L = image.getpixel((x, y))
        # 与阈值比较
        if L > G:
            L = True
        else:
            L = False
        nearDots = 0
        if L == (image.getpixel((x - 1, y - 1)) > G):
            nearDots += 1
        if L == (image.getpixel((x - 1, y)) > G):
            nearDots += 1
        if L == (image.getpixel((x - 1, y + 1)) > G):
            nearDots += 1
        if L == (image.getpixel((x, y - 1)) > G):
            nearDots += 1
        if L == (image.getpixel((x, y + 1)) > G):
            nearDots += 1
        if L == (image.getpixel((x + 1, y - 1)) > G):
            nearDots += 1
        if L == (image.getpixel((x + 1, y)) > G):
            nearDots += 1
        if L == (image.getpixel((x + 1, y + 1)) > G):
            nearDots += 1

        if nearDots < N:
            return image.getpixel((x, y - 1))
        else:
            return None

    def clear_noise(slef, image, G, N, Z):
        '''

        :param G:  阈值
        :param N: 0<N<8
        :param Z: 降噪次数
        :return:
        '''
        draw = ImageDraw.Draw(image)
        for i in range(0, Z):
            for x in range(1, image.size[0] - 1):
                for y in range(1, image.size[1] - 1):
                    color = slef.get_pixel(image, x, y, G, N)
                    if color is not None:
                        draw.point((x, y), color)
        return image



def fill_image(image):
    copyImage = image.copy()  # 复制原图像
    h, w = image.shape[:2]  # 读取图像的宽和高
    mask = np.zeros([h + 2, w + 2], np.uint8)  # 新建图像矩阵  +2是官方函数要求
    cv.floodFill(copyImage, mask, (110, 20), (255, 255, 255), (90, 90, 90), (30, 30, 30),
                 flags=8 | (255 << 8) | cv.FLOODFILL_FIXED_RANGE)
    mask_copy = mask[1:h + 1, 1:w + 1]  # 把掩码中的数值取出来大小和原图一样,这样才能和原图进行运算,注意掩码的取值范围从1到h/w+1
    mask_copy = cv.merge([mask_copy, mask_copy, mask_copy])  # 要进行图像操作通道数目要一致,用merge函数合并出一个三通道图像
    src = cv.bitwise_and(image, mask_copy)  # 两个图像相与,mask中非标记区域为0与出来的结果也是0,起到屏蔽作用
    cv.namedWindow("fill", cv.WINDOW_NORMAL)
    cv.imshow("fill", copyImage)  # 显示填充过后的图像
    cv.waitKey(0)
    cv.namedWindow("and", cv.WINDOW_NORMAL)  # 显示屏蔽过后图像
    cv.imshow("and", src)
    return src


# 检查边界
def check_edge():
    # img = cv.imread("ImageData/0.jpg", 0)
    filename = "ImageData/0.jpg"
    img = cv.imread(filename, 0)
    blur = cv.GaussianBlur(img, (3, 3), 0)  # 用高斯滤波处理原图像降噪
    canny = cv.Canny(blur, 50, 150)  # 50是最小阈值,150是最大阈值
    cv.imshow('canny', canny)
    cv.waitKey(0)
    cv.destroyAllWindows()
# check_edge()

## 图片旋转
def rotate_bound(image, angle):
    # 获取宽高
    (h, w) = image.shape[:2]
    (cX, cY) = (w // 2, h // 2)

    # 提取旋转矩阵 sin cos
    M = cv.getRotationMatrix2D((cX, cY), -angle, 1.0)
    cos = np.abs(M[0, 0])
    sin = np.abs(M[0, 1])

    # 计算图像的新边界尺寸
    nW = int((h * sin) + (w * cos))
    #     nH = int((h * cos) + (w * sin))
    nH = h

    # 调整旋转矩阵
    M[0, 2] += (nW / 2) - cX
    M[1, 2] += (nH / 2) - cY

    return cv.warpAffine(image, M, (nW, nH), flags=cv.INTER_CUBIC, borderMode=cv.BORDER_REPLICATE)


## 获取图片旋转角度
def get_minAreaRect(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    gray = cv.bitwise_not(gray)
    thresh = cv.threshold(gray, 0, 255,
                           cv.THRESH_BINARY | cv.THRESH_OTSU)[1]
    coords = np.column_stack(np.where(thresh > 0))
    return cv.minAreaRect(coords)


    image_path = "./Modif/0_97.png."
    image = cv.imread(image_path)
    angle = get_minAreaRect(image)[-1]
    rotated = rotate_bound(image, angle)
    cv.putText(rotated, "angle: {:.2f} ".format(angle),
                (10, 30), cv.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

    # show the output image
    print("[INFO] angle: {:.3f}".format(angle))
    cv.imshow("imput", image)
    cv.imshow("output", rotated)
    cv.waitKey(0)

# 图片增强
def imageSharpness(image):
    im = Image.open(image)
    en = ImageEnhance.Contrast(im)
    en_end = en.enhance(5)
    en_end.show()


if __name__ == '__main__':
    imagePro = ImageProcess()
    # 图片二值化
    # image_file = 'image/*'
    # for image in glob.glob(image_file):
    #     print(image)
    #     imagePro.grayscale(image)
    # 图片降噪
    image_file = 'GrayscaleImage/*'
    for image in glob.glob(image_file):
        print('正在处理图片%s'% image)
        imageName = image.split('/')
        img = Image.open(image)
        images = imagePro.clear_noise(img,150,2,1)
        images.save("BinarizationImage/%s" % imageName[1], 'png')
    # image_file = 'image/*'
    # for image in glob.glob(image_file):
    #     images = Image.open(image)
    #     print(image)
    #     # images = images.crop((0,0,110,20))
    #     images.save(image[:-4]+'.png','PNG')
    # fill_image 调试

    # src = cv.imread("ImageData/1.jpg")
    # img = cv.imread("ImageData/1.jpg", 0)
    # blur = cv.GaussianBlur(img, (3, 3), 0)  # 用高斯滤波处理原图像降噪
    # src = cv.Canny(blur, 50, 150)
    # cv.namedWindow("raw", cv.WINDOW_NORMAL)  # 设置框体大小和名字
    # cv.imshow("raw", src)
    # fill_image(src)

    # 图片增强调试
    # image = "./ImageData/0.jpg"
    # imageSharpness(image)
    pass
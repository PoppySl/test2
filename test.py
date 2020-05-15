from captcha.image import ImageCaptcha
from PIL import ImageFont, ImageDraw, Image, ImageFilter
import numpy as np
import cv2
import uuid
import math


def made_code():
    letters = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    width = 25
    hight = 30
    code_len = 4
    fonts = 'font/msjhbd.ttc'
    font_size = 18
    font_color = tuple(int(np.random.choice(range(0, 156)))
                           for _ in range(3))
    text = ''.join(np.random.choice(letters, code_len))  # 获得验证码
    fontText = ImageFont.truetype(fonts, font_size)  # 设置字体
    sum_width = 0
    mother_img = Image.new('RGB', (120, 30), color='white')
    for index, letter in enumerate(text):
        img = Image.new(
            'RGBA', (width, hight), color=(
                255, 255, 255))  # 创建一个图片
        draw = ImageDraw.Draw(img)  # 创建一个画笔
        delta_high = np.random.randint(-2, 0)   # 随机一个高度
        delta_width = np.random.randint(0, 5)   # 随机一个宽度
        draw.text(
            (delta_width, delta_high),
            letter,
            font_color,
            font=fontText)
        jiaodu = np.random.randint(-50, 40)
        _img = img.rotate(jiaodu, expand=0)   # 随机一个旋转角度
        sum_width = sum_width + delta_width   # 字符宽度+随机间隔宽度
        *drop, alpha = _img.split()
        bottom_left_coordinate = (
            index * width + sum_width, delta_high)
        mother_img.paste(
            _img,
            box=bottom_left_coordinate,
            mask=alpha)  # 将旋转后的图片粘贴到最终图片
    # mother_img.show()
    # 画随机噪点
    draw = ImageDraw.Draw(mother_img)


    img = cv2.cvtColor(np.asarray(mother_img), cv2.COLOR_RGB2BGR)
    x = np.random.choice(range(70, 80))
    y = np.random.choice(range(10, 20))
    axes = (x, y)  # 椭圆长主轴与短主轴值
    center = (119, 29)  # 原中心点
    angle = 180  # 旋转角度
    start_angle = 0  # 开始角
    end_angle = 360  # 终点角度
    line_color = tuple(int(np.random.choice(range(0, 156)))
                       for _ in range(3))
    line_thickness = 2
    cv2.ellipse(
        img,
        center,
        axes,
        angle,
        start_angle,
        end_angle,
        line_color,
        line_thickness,
        lineType=4)  # 画弧线

    # dst = cv2.medianBlur(img, 3)
    # cv2.imshow("11111", dst)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    fn = text + ('_' + str(uuid.uuid1())[4: 8])
    cropped = img[0:20, 0:110]
    cv2.imwrite('{}/{}.png'.format('sample/train/', fn), cropped)


for i in range(5000):
    print('第%s张验证码生成成功' % i)
    made_code()

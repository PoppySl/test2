import time
import os
import requests

Get_path = "./img_data/"  # 下载图片保存路径
Get_url = "https://www.mvdis.gov.tw/m3-emv-mobo/verifyCodeServlet?m="
Get_number = 1  # 下载图片数量


def GetImgCode():
    get_img_start = time.time()
    if os.path.isdir(Get_path):
        pass
    else:
        mkdir = os.makedirs(Get_path)
        print('下载目录不存在，创建目录中----------')
        print('下载目录创建成功，目录名->' + Get_path)
    if Get_url != '':
        print("获取下载链接成功---------")
        print("开始下载验证码")
        for i in range(0, Get_number):
            print("下载第" + str(i) + "张验证码")
            filePath = Get_path + str(i) + '.png'
            Get_img = requests.get(Get_url)
            with open(filePath, 'bw') as f:
                f.write(Get_img.content)
        get_img_end = time.time()
        print("已完成，共下载" + str(Get_number) + "张验证码---------")
        print("执行时间 %f m" % (get_img_end - get_img_start))

    else:
        print('验证码下载地址为空')
        exit()

GetImgCode()
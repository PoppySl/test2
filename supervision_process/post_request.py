import requests
import recognize_online
import json
from pyquery import PyQuery as pq


class SupervisionProcess:
    '''
    post请求监理站并回对应内容
    '''

    def __init__(self, isplay, queryType, searchID, page=1):
        self.isplay = isplay
        self.queryType = queryType
        self.searchID = searchID
        self.page = page
        self.url = 'https://www.mvdis.gov.tw/m3-emv-mobo/public/moboTrafficFineResult'
        self.code = self.get_validate_code()

    def get_supervision_data(self):
        headers = {
            'Origin': 'https://www.mvdis.gov.tw',
            'Upgrade-Insecure-Requests': '1',
            'Content-Type': 'application/x-www-form-urlencoded',
            'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1',
            'Sec-Fetch-Dest': 'document',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        }

        data = {
            'isplay': self.isplay,    # 0非線上繳費項目，1可線上繳費項目
            'queryType': self.queryType,  # 0個人，1法人
            'searchID': self.searchID,
            'thisPage': '1',
            'validateCode': self.code
        }
        requests.request("POST", self.url, headers=headers, data=data)
        response = requests.request("POST", self.url, headers=headers, data=data)
        # print(type(response.content))
        return response.content
        # html = pq(response.content)
        # print(html)
        # text = html('.moboTrafficFinePay')
        # print(text)

    def paese_html(self):
        response = self.get_supervision_data()
        response = response.decode('utf-8')
        errorList = ['驗證碼不存在', '身分證號(或統一編號)格式不正確', '請重新查詢']
        if any(error in response for error in errorList) == True:
            return False
        else:
            response = pq(response)
            results = response('.irregularities_table01').text()
            return results.splitlines()

    def get_validate_code(self):
        with open("../conf/sample_config.json", "r") as f:
            sample_conf = json.load(f)
        # 配置相关参数
        save_path = sample_conf["online_image_dir"]  # 下载图片保存的地址
        remote_url = sample_conf["remote_url"]  # 网络验证码地址
        image_suffix = sample_conf["image_suffix"]  # 文件后缀
        rec_times = 1
        code = recognize_online.recognize_captcha(
            remote_url, rec_times, save_path, image_suffix)
        return code


if __name__ == '__main__':
    # get_supervision_data()
    pass

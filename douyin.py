import requests

import re


class douyin(object):
    print('#####抖音视频下载脚本#######################################################')
    print('#####作者:纷扰#############################################################')
    print('#####github:https://github.com/fenrao/douyin_Video_download###############')

    def __init__(self):
        self.header = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Accept-Language': 'zh,zh-CN;q=0.9',
            'Connection': 'keep-alive',
            'Content-Type': 'application/x-www-form-urlencoded',
            'DNT': '1',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.81 Safari/537.36',
        }

    def run(self):
        self.url = input('请输入视频链接：')
        self.title = re.findall('记录美好生活#(\S*)', self.url)[0]
        print(self.title)
        try:

            self.url = re.findall('https|http://\S*', self.url)[0]
        except Exception as e:
            print('url地址错误，请重新输入')
            return self.run()
        html = requests.get(url=self.url, headers=self.header)
        self.url = re.findall(' playAddr: "(https://\S*)"', html.text)[0]  # 视频地址
        self.header['User-Agent']='Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) CriOS/56.0.2924.75 Mobile/14E5239e Safari/602.1'
        self.url = self.url.replace('playwm', 'play') + '&line=0&device_platform=iphone'

        video = requests.get(self.url, headers=self.header, stream=True)
        with open(self.title+'.mp4', 'wb')as file:
            file.write(video.content)
        print('##########下载完成感谢使用################')


if __name__ == "__main__":
    d = douyin()
    d.run()
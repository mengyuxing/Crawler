# -*- coding：utf-8 -*-
#
# name：Meng
# mail：614886708@qq.com

import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from fake_useragent import UserAgent


class OuterChain:
    def __init__(self, url):
        self.LinkInfo = []   # 返回结果
        # 修改传入url格式
        if url[:4] != 'http':
            self.url = 'http://' + url
        else:
            self.url = url

    def session(self):
        """
        会话保持
        """
        s = requests.Session()
        # 随机生成浏览器代理
        s.headers.update({'User-Agent': str(UserAgent().random)})
        return s

    def get_Links(self, base):
        """
        访问地址并查找源码中的链接
        """
        linkLst = []    # 临时外链列表

        conn = self.session()
        text = conn.get(base).text
        isi = BeautifulSoup(text, "html.parser")

        # 获取页面中所有<a>标签
        for obj in isi.find_all("a", href=True):

            # 获取href属性的值
            url = obj["href"]

            # 过滤掉无用外链
            if url.startswith("mailto:") or url.startswith("javascript:"):
                continue
            # 路径拼接去重
            elif urljoin(base, url) in linkLst:
                continue
            # 符合的外链
            else:
                linkLst.append(urljoin(base, url))

        for link in linkLst:
            self.LinkInfo.append({'url': link, 'status': requests.get(link).status_code})

    def run(self):
        self.get_Links(self.url)
        return self.LinkInfo


if __name__ == '__main__':
    a = OuterChain('www.xxx.com')
    print(a.run())

# 返回结果
# [{'url': 'http://www.xxxx.com', 'status': 200},
#  {'url': 'http://www.xxxxxx.com', 'status': 404},]

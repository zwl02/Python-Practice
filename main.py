import re
import requests


class XiaoYuan(object):
    def __init__(self):
        self.url = "http://i.whut.edu.cn/xxtg/"

    def get_html(self):
        response = requests.get(self.url)
        response.encoding = "utf-8"
        '''print(response.text)'''
        return response.text

    def get_ifo(self, html):
        pattern = re.compile('</i><a href="./(.*?)title="(.*?)">.*?</a>',re.S)
        r = re.findall(pattern, html)
        for item in r:
            yield {
                "题目": item[1],
                "链接": self.url+item[0]
            }

xiaoyuan = XiaoYuan()
html = xiaoyuan.get_html()
for i in xiaoyuan.get_ifo(html):
    print(i)
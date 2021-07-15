import re
import requests
from bs4 import BeautifulSoup

class story(object):
    def __init__(self):#初始化数据
        self.url = "https://www.bqkan8.com/74_74343/"
        self.line = int(input("请输入想显示的行数："))
        self.headers = "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"
    def get_html(self):#获取html代码
        response = requests.get(self.url, self.headers)
        response.encoding = "GB2312"
        self.status_code=requests.get(self.url).status_code
        self.apparent_encoding=response.apparent_encoding
        #print(response.text)
        return response.text

    def get_story_url(self, html):#获取题目和链接
        pattern = re.compile('<dd><a href ="/74_74343/(.*?)">(.*?)</a></dd>',re.S)
        r = re.findall(pattern, html)
        i=0
        for item in r:
            if(i < self.line):
                i+=1
                yield {
                    "序号": i,
                    "题目": item[1],
                    "链接": self.url+item[0]
                }

    def text_create(self,name):#保存到文件中
        desktop_path = "D:\\desk\\"
        full_path = desktop_path + name + '.txt'
        self.file = open(full_path, 'w+',encoding='utf-8')#,encoding='utf-8'
    def text_write(self,msg):
        self.file.write(msg)


print("《美剧大世界里的骑士》")
story = story()#创建对象
html = story.get_html()#获取html代码
print("当前网页状态码：",story.status_code)
print("当前网页编码格式：",story.apparent_encoding)
for i in story.get_story_url(html):#打印获取到的迭代对象
    print(i)
soup = BeautifulSoup(story.get_html(),"html.parser")#创建bs对象
print(soup.title)
names = soup.find_all('a')#获取a标签
story.text_create('save')#在桌面创建文件
for name in names:#将获取到的文字内容写入到txt文件中
    #print(name.string)
    story.text_write(str(name.string)+'\r\n')

from urllib import request
import gzip
from io import BytesIO

import spider_object.factory as factory


# 定义一个爬虫类
class Spider:
    def __init__(self, url, web_tag):
        self.url = url
        self.web_tag = web_tag

    # 获取html，并转化编码
    def fetch_content(self):
        with request.urlopen(self.url) as r:
            htmls = str(r.read(), encoding='utf-8')
            return htmls

    # html分析，调用工厂类创建对应的实例并调用实例的入口方法
    def __analysis(self, htmls):
        analyser = factory.CategoryFactory.get_category(self.web_tag)
        analyser.analysis(htmls)

    # Spider类的入口方法
    def spider_run(self):
        htmls = self.fetch_content()
        self.__analysis(htmls)


# 爬虫子类，用于适配斗鱼网站爬取
class Spider_Douyu(Spider):
    def __init__(self, url, web_tag):
        super().__init__(url, web_tag)

    # 根据斗鱼网站反爬逻辑，重写父类fetch_content方法
    def fetch_content(self):
        with request.urlopen(self.url) as r:
            htmls = r.read()
            buffer = BytesIO(htmls)
            f = gzip.GzipFile(fileobj=buffer)
            htmls = f.read().decode('utf-8')
            return htmls

    # def __analysis(self, htmls):
    #     analyser = factory.CategoryFactory.get_category(self.web_tag)
    #     analyser.analysis(htmls)

    # def spider_run(self):
    #     htmls = self.fetch_content()
    #     self.__analysis(htmls)

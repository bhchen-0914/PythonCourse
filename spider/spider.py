"""
HTML的结构分析与基本原则3条：
尽量选取具有唯一标识的标签作为定位标签
尽量选取位置最接近于我们需要提取的数据的标签
尽量选取可以闭合的标签
"""

from urllib import request
import re

# 一般来说一个网站的模块是按照通用的模板写的，可以通过改变url访问其他模块的数据

class Spider:  # 构建一个爬虫类
    url = 'https://www.huya.com/g/wzry'
    root_pattern = '<span class="avatar fl">(.*?)</li>'
    name_pattern = '<i class="nick" title="(.*?)"'
    number_pattern = '<i class="js-num">(.*?)</i>'
    float_pattern = '\d*'

    def __fetch_content(self):
        r = request.urlopen(self.__class__.url)  # r的结果是byte类型的字节，需要转换成str类型
        htmls = str(r.read(), encoding='utf-8')  # 关键字参数设置编码格式
        return htmls

    def __analysis(self, htmls):  # 对抓取到的html进行处理
        root_htmls = re.findall(self.__class__.root_pattern, htmls, re.S)

        anchors = []
        for html in root_htmls:
            name = re.findall(self.__class__.name_pattern, html)
            number = re.findall(self.__class__.number_pattern, html)
            anchor = {'name': name, 'number': number}
            anchors.append(anchor)

        return anchors

    @staticmethod
    def __refines(data):  # 用于数据精炼，此处主要是对list格式的数据字符串化
        last_deal = lambda anchor: {'name': anchor['name'][0], 'number': anchor['number'][0]}
        return map(last_deal, data)

    def __sort(self, anchors):  #  用于排序
        last_anchors = sorted(anchors, key=self.__sort_seed, reverse=True)  # key参数是排序的依据，这里是一个函数，reverse参数为True表示降序
        return last_anchors

    def __sort_seed(self, anchor):  # 作为sort方法排序key参数的参考
        r = re.findall(self.__class__.float_pattern, anchor['number'])

        number = float(r[0])   # 按照人气的数值排列，需要对单位 万 进行处理
        if '万' in anchor['number']:
            number *= 10000

        return number

    @staticmethod
    def __show(anchors):
        for num in range(0, len(anchors)):
            print('人气排名',num+1,'主播：', anchors[num]['name'], '-------', '人气：', anchors[num]['number'])

    def go(self):  # 入口方法与总控方法，所有方法的调用都会汇集到go方法内
        htmls = self.__fetch_content()
        anchors = self.__analysis(htmls)
        new_anchors = list(self.__refines(anchors))
        last_anchors = self.__sort(new_anchors)
        self.__show(last_anchors)


spider = Spider()
spider.go()

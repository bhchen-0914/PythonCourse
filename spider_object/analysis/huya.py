import time

from spider_object.analysis.analysis import Analysis

class Huya(Analysis):

    def __init__(self):
        super().__init__()
        self.root_pattern = '<span class="avatar fl">(.*?)</li>'
        self.name_pattern = '<i class="nick" title="(.*?)"'
        self.number_pattern = '<i class="js-num">(.*?)</i>'
        self.float_pattern = '\d*'

    @staticmethod
    def show(anchors):
        print('当前时间:', time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()), '虎牙人气榜:')
        for num in range(0, len(anchors)):
            print('人气排名', num + 1, '主播：', anchors[num]['name'], '-------', '人气：', anchors[num]['number'])


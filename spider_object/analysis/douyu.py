import time

from spider_object.analysis.analysis import Analysis


class Douyu(Analysis):
    def __init__(self):
        super().__init__()
        self.root_pattern = '<div class="DyListCover-content">(.*?)<div class="LazyLoad is-visible">'
        self.name_pattern = '<use xlink:href="#icon-user_c95acf8"></use></svg>(.*?)</h2></div>'
        self.number_pattern = '<use xlink:href="#icon-hot_8a57f0b"></use></svg>(.*?)</span>'
        self.float_pattern = '\d*'

    @staticmethod
    def show(anchors):
        print('当前时间:', time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()), '斗鱼人气榜:')
        for num in range(0, len(anchors)):
            print('人气排名', num + 1, '主播：', anchors[num]['name'], '-------', '人气：', anchors[num]['number'])

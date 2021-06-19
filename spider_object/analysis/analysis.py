import re


class Analysis:
    def __init__(self):
        self.root_pattern = ''
        self.name_pattern = ''
        self.number_pattern = ''
        self.float_pattern = ''

    def analysis(self, htmls):
        root_htmls = re.findall(self.root_pattern, htmls, re.S)

        anchors = []
        for html in root_htmls:
            name = re.findall(self.name_pattern, html)
            number = re.findall(self.number_pattern, html)
            anchors.append({'name': name, 'number': number})

        new_anchors = self.__refine(anchors)
        last_anchors = self.__sort(list(new_anchors))
        self.show(last_anchors)

    @staticmethod
    def __refine(anchors):
        last_deal = lambda anchor: {'name': anchor['name'][0], 'number': anchor['number'][0]}
        return map(last_deal, anchors)

    # 按人气排序
    def __sort(self, anchors):
        last_anchors = sorted(anchors, key=self.__sort_seed, reverse=True)
        return last_anchors

    def __sort_seed(self, anchor):
        r = re.findall(self.float_pattern, anchor['number'])
        number = float(r[0])
        if '万' in anchor['number']:
            number *= 10000

        return number

    @staticmethod
    def show(anchors):
        for num in range(0, len(anchors)):
            print('人气排名', num + 1, '主播：', anchors[num]['name'], '-------', '人气：', anchors[num]['number'])

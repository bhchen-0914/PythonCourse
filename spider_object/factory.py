"""
工厂类，供Spider类调用，返回指定的类
"""
from spider_object.analysis import huya, douyu


class CategoryFactory:

    @staticmethod
    def get_category(web_tag):
        if web_tag == 'Huya':
            return huya.Huya()
        elif web_tag == 'Douyu':
            return douyu.Douyu()

from spider_object.spider import Spider, Spider_Douyu
from spider_object.config.huya_config.huya_config import *
from spider_object.config.douyu_config.douyu_config import *


def main():
    douyu_lol = Spider_Douyu(Douyu_Page_URL_wzry, Web_Tag_Douyu)
    douyu_lol.spider_run()
    huya_lol = Spider(Huya_Page_URL_wzry, Web_Tag_Huya)
    huya_lol.spider_run()


if __name__ == '__main__':
    main()

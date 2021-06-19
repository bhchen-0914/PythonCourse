# -*- coding: UTF-8 -*-
import requests
from bs4 import BeautifulSoup
import lxml


def connect_link(url, *kwargs):  # 构造请求响应的方法
    response = requests.get(url, *kwargs)
    soup = BeautifulSoup(response.content, 'lxml')
    # print(soup.contents)
    return soup


def catch_data(soup, feature1, feature2, open_mode):  # 获取资料
    content = soup.find_all(feature1, feature2)
    # print(content)
    for i in content:
        i = i.encode('utf-8')
        f = open('file11.txt', open_mode)
        f.write(i)
        f.close()


def data_deal():  # 处理数据的编码
    f2 = open('file11.txt', 'rb')
    f3 = open('file22.txt', 'w')
    for m in f2.readlines():
        f3.write(str(m, encoding="utf-8"))
    f2.close()
    f3.close()


def to_chinese(str1):  # 从字符串中提取中文、空格、换行符，返回一个仅含中文、空格、换行符的字符串
    str2 = ""
    for i in str1:
        if i == "\n" or i == " ":
            str2 = str2 + i
        else:
            x = len(i.encode('utf-8'))
            if x == 3:
                str2 = str2 + i
    return str2


def txt_to_chinese(path, encoding="UTF-8"):  # 对象为txt文件，默认编码格式为"UTF-8"
    f4 = open(path, 'r', encoding=encoding)
    text = str(f4.read())
    text = to_chinese(text)
    f4.close()
    f4 = open(path, 'w', encoding=encoding)
    f4.write(text)
    f4.close()


def clearBlankLine():
    f5 = open('file22.txt', 'r', encoding='ANSI')  # 要去掉空行的文件
    f6 = open('final_new.txt', 'w', encoding='utf-8')  # 生成没有空行的文件
    try:
        for line in f5.readlines():
            if line == '\n':
                line = line.strip("\n")
            f6.write(line)
    finally:
        f5.close()
        f6.close()


def final_data(path):  # 构造整合资料的方法
    data_deal()
    txt_to_chinese(path, encoding="ANSI")
    clearBlankLine()


url1 = "https://poi.mapbar.com/chongqing/FF1/"
url2 = "https://poi.mapbar.com/chongqing/901/"
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/83.0.4103.97 Safari/537.36', 'referer': 'https://poi.mapbar.com/chongqing/FF1/',
           'Sec-Fetch-Mode': 'navigate'}
path = "E:/untitled/file22.txt"
soup1 = connect_link(url1, headers)
soup2 = connect_link(url2)
catch_data(soup1, 'div', 'sortC', 'wb')
catch_data(soup2, 'div', 'sortC', 'ab')
final_data(path)




# -*- coding: UTF-8 -*-
import requests
from bs4 import BeautifulSoup

# import xml
# from lxml import html
url1 = "https://poi.mapbar.com/chongqing/FF1/"
url2 = "https://poi.mapbar.com/chongqing/901/"
headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/83.0.4103.97 Safari/537.36',
        'referer': 'https://poi.mapbar.com/chongqing/FF1/',
        'Sec-Fetch-Mode': 'navigate'
}
r1 = requests.get(url1, headers)
r2 = requests.get(url2)
soup = BeautifulSoup(r1.content, "lxml")
soup2 = BeautifulSoup(r2.content, "lxml")


content = soup.find_all('div', class_='sortC')
content2 = soup2.find_all('div', class_='sortC')

for i in content:
    i = i.encode('utf-8')
    f = open('file1.txt', "wb")
    f.write(i)
    f.close()

for i in content2:
    i = i.encode('utf-8')
    f = open('file1.txt', "ab")
    f.write(i)
    f.close()


f2 = open('file1.txt', 'rb')
f3 = open('file2.txt', 'w')
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
    f5 = open('file2.txt', 'r', encoding='ANSI')  # 要去掉空行的文件
    f6 = open('final.txt', 'w', encoding='utf-8')  # 生成没有空行的文件
    try:
        for line in f5.readlines():
            if line == '\n':
                line = line.strip("\n")
            f6.write(line)
    finally:
        f5.close()
        f6.close()


txt_to_chinese("E:/untitled/file2.txt", encoding="ANSI")
clearBlankLine()
print('File generated successfully')
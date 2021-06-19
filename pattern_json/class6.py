"""
re.sub正则替换
re.sub返回的是一个字符串
把函数作为参数传递
"""
import re

language = 'Python__C#__99sdC#89_!!JAVAphpC#'

r1 = re.sub('C#', 'GO', language, 0)  # 参数0表示替换将无限次数的进行
print(r1)
r2 = re.sub('C#', 'GO', language, 2)  # 最后一个参数非0时表示替换的最大次数
print(r2)
r3 = language.replace('C#', 'GO', 2)  # 也可用.replace内置函数代替上述写法
print(r3)

str1 = 'hello123hello 23ssdhello!!sd'


def convert(value):  # value 是一个re.Match object类，内置group()方法，用于返回字符串
    print(value)  # 打印<re.Match object; span=(0, 5), match='hello'>，这里value是一个类（0，5）表示匹配的值的所在位置，左闭右开
    matched = value.group()
    return matched + 'world'


result = re.sub('hello', convert, str1)  # re.sub可以将函数当做参数传递，这里替换值为convert函数的返回值，通过传入函数的
print(result)  # 方法，re.sub可以非常灵活的实现各种替换操作

"""
有一个字符串str2，提取其中的数字，当数字小于5时，替换为0，数字大于5时替换为1
"""
str2 = 'ADS2350838asd%%!!3'


def convert_num(value):
    matched = value.group()
    if int(matched) < 5:
        return '0'
    elif int(matched) > 5:
        return '1'
    else:
        return matched


result2 = re.sub('\d', convert_num, str2)
print(result2)

"""
查找str3中的二位数，>=50的用**替换，<50的用##替换，单个数字不用替换
"""

str3 = '78hello49pyt1hon9'


def convert_num2(value):
    matched = value.group()
    if int(matched) >= 50:
        return '**'
    else:
        return '##'


result3 = re.sub('\d{2}', convert_num2, str3)
print(result3)

"""
剔除str3中的单个数字，查找二位数，>=50的用**替换，<50的用##替换
"""


def convert_num3(value):
    matched = value.group()
    if int(matched) >= 50:
        return '**'
    elif int(matched) < 10:
        pass
    else:
        return '##'


result4 = re.sub('\d{1,2}', convert_num3, str3)
print(result4)
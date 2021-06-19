"""
边界匹配
"""
import re

# 判断一串数字在4到8位之间
str1 = '10000001'
r = re.findall('\d{4,8}', str1)  # 这样写不行，因为超过数量词范围时会截取，而不是判断返回失败
print(r)
r1 = re.findall('^\d{4,8}$', str1)  # ^表示从字符串开头匹配，$表示从字符串末尾匹配，组合起来可用作边界值匹配
print(r1)
print(re.findall('^000', str1))  # 理解^用法
print(re.findall('^100', str1))
print(re.findall('000$', str1))  # 理解$用法
print(re.findall('001$', str1))

# 判断QQ号是否合法：全数字，6~11位
qq = input('输入qq号：')


def input_qq(qq):
    r = re.findall('^\d{8,11}$', qq)
    print(r)
    if r:
        print('输入合法')
    else:
        print('输入不合法')


input_qq(qq)
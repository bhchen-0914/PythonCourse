"""
group分组
"""

import re

s = "<t>this is a webpage 's title<t> "

r1 = re.search('<t>.*<t>', s)
print(r1.group())
r2 = re.search('<t>(.*)<t>', s)  # （）内表示一个分组
print(r2.group(0))  # 0是默认取值，会默认匹配完整的正则表达式结果
print(r2.group(1))

s2 = s = "<t>this is a webpage 's title<t>this is other webpage 's title<t>"
r3 = re.search('<t>(.*)<t>(.*)<t>', s2)
print(r3.group(0))
print(r3.group(1))  # 使用group（）方法内参数表示组号
print(r3.group(2))

print(r3.group(0, 1, 2))  # 快捷访问多组数据，返回值是一个元组

print(r3.groups())  # group只会返回普通字符中间的内容 
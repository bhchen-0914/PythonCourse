"""
search 与 match函数
"""
import re

s = 'SBD14!!8p02'
s2 = '2SBD14!!8p02'
r1 = re.match('\d', s)
r2 = re.search('\d', s)
r3 = re.match('\d', s2)
print(r1)  # None
print(r2)  # <re.Match object; span=(3, 4), match='1'>
print(r3)
print(type(r2.span()), r2.span())   # 返回匹配值所在的位置,是一个元组
"""
re.match 作用是从字符串开头进行匹配，若开头不是正则表达描述的字符，则返回None，若满足，返回一个object对象  
re.search 作用是搜索整个字符串，直到找到第一个满足的结果，并返回,返回结果是一个object对象。span是匹配值的所在位置，左闭右开
与re.findall 不同，match和search只会匹配一次并返回结果，且返回结果的类型也不同
"""

print(r3.group())  # group()方法可以将匹配结果以字符串的形式返回

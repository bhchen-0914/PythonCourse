"""
元字符与普通字符
字符集
"""
import re

language = 'C0C++1C#89Python278java00javascript56HTML'
list1 = []  # for循环提取数字
for i in language:
    if i.isdigit():
        list1.append(i)
print('list1:', list1)
r = re.findall('\d', language)  # 提取数字  这里‘Python’作为普通字符，‘\d’作为元字符，正则表达式有普通字符和元字符组成
print(r)

list2 = []
for s in language:
    if not s.isdigit():
        list2.append(s)
print('list2:', list2)
r2 = re.findall('\D', language)  # \D表示提取非数字
print(r2)

s = 'abc, acc, adc, aec, afc, ahc'
r3 = re.findall('a[cef]c', s)  # 字符集，匹配中间为 c,e,f的字符串，这里ac是普通字符，[cef]是元字符，普通字符的作用通常为精确查抄
r4 = re.findall('a[^cef]c', s)  # 匹配ac中间非cef的字符串
r5 = re.findall('a[c-f]c', s)  # 匹配ac中间为c到f的字符串
print(r3)
print(r4)
print(r5)

s2 = 'Python\' 111\n11~~1_java22!!ph\tp++78\r9'
result1 = re.findall('\d', s2)  # 提取数字
result2 = re.findall('[0-9]', s2)  # 与上述结果一样
print(result1)
print(result2)
result3 = re.findall('\D', s2)  # 提取非数字
result4 = re.findall('[^0-9]', s2)  # 等价于上述写法
print(result3)
print(result4)
result5 = re.findall('\w', s2)  # 提取字母、数字、下划线,/w是单词字符
result6 = re.findall('[0-9a-zA-Z_]', s2)  # 等价上述写法
print(result5)
print(result6)
result7 = re.findall('\W', s2)  # 匹配非单词字符
result8 = re.findall('[^0-9a-zA-Z_]', s2)  # 等价上述写法
print(result7)
print(result8)
result9 = re.findall('\s', s2)  # 匹配空白字符
result10 = re.findall('\S', s2)  # 匹配非空白字符
print(result9)
print(result10)
result11 = re.findall('.', s2)  # 匹配除换行符\n外所有字符
print(result11)
"""
数量词
贪婪与非贪婪
* 匹配0次或无限多次
+ 匹配1次或无线多次
? 匹配0次或者1次，？常用来去重
"""
import re

str1 = 'python  11112222java-php'

r = re.findall('[a-z][a-z][a-z][a-z][a-z][a-z]', str1)  # 匹配6个字母的单词，这样的写法太繁琐。可以用数量词表示
print(r)
r1 = re.findall('[a-z]{3}', str1)  # {}内为数量词
print(r1)
r2 = re.findall('[a-z]{3,6}', str1)  # 设置数量词匹配的长度范围
print(r2)
"""
这里打印出python 而不是pyt和hon的原因，是因为python的正则表达式默认为贪婪模式，
贪婪模式意思是，当数量词有限定在一个区间内，python倾向于在区间内取最大的一个值进行匹配，直到某一个值不满足他的匹配规则
"""
str2 = 'aaabbbcccdddeeefff'
r3 = re.findall('[a-z]{3,6}?', str2)  # ?表示非贪婪
print(r3)
r4 = re.findall('[a-z]{3,6}', str2)
print(r4)

str3 = 'pytho**python+pythonn23s   pythonnnnnn'
result1 = re.findall('python*', str3)  # *表示：*前面的字符可以出现0次或者无限多次，pytho 没有n，n出现了0次，所以也匹配上了
print(result1)
result2 = re.findall('python+', str3)  # +示：+前面的字符可以出现1次或者无限多次，pytho 没有n，n出现了0次，所以不会匹配
print(result2)
result3 = re.findall('python?', str3)  # ?示：?前面的字符可以出现0或者1次，pythonn n出现了2次，但是n最多匹配一次，因此只能匹配出python
print(result3)
result4 = re.findall('python{1,3}', str3)  # 普通字符加数量词，表示最后一个字符出现次数，默认为贪婪
print(result4)
result5 = re.findall('python{1,3}?', str3)  # 非贪婪
print(result5)

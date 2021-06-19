"""
组的概念
匹配模式参数
"""
import re

# 判断st1里是否包含3个Python
st1 = 'PythonPythonPython,,**sdPythonPythonJSJS'
print(re.findall('(Python){3}', st1))  # 打印['Python']，表示的是连续匹配三个python，如果匹配成功，则返回一个python
print(re.findall('(Python){2}(JS){2}', st1))  # 打印[('Python', 'JS')]，表示连续匹配2个Python和2个JS组合，成功则返回包含Python和JS的元组

language = 'Python\rC#\nJAVa'
r1 = re.findall('java', language)
print(r1)
r2 = re.findall('java', language, re.I)  # re.I参数表示忽略大小写模式
print(r2)
print(re.findall('.', language))  # 匹配除换行符\n外所有字符
print(re.findall('.', language, re.S))  # re.S模式表示'.'会匹配所有字符，包括换行符
r3 = re.findall('C#.{2}', language, re.S)  # 表示在C#后再匹配2个字符
print(r3)
r4 = re.findall('c#.{2}', language, re.I | re.S)  # 多个匹配模式参数共存使用|连接
print(r4)

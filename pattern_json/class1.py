"""
正则表达式是一个特殊的字符序列，判断一个字符串是否与我们所设定的字符序列相匹配
可以实现快速检索文本，或替换文本的操作，比如：
1.检查一组数字是否是电话号码
2.检查一组字符串是否符合email格式
3.把一个文本里指定的单词替换为另一个单词
。。。。。
"""
import re

language = 'C|C++|C#|Python|java|javascript|HTML'
print('Python' in language)
print(language.index('Python') >= 0)
r = re.findall('Python', language)   # findall方法里第一个参数pattern，代表正则表达式。这里python是一个常量表达式，几乎没有使用意义
# print(r)  返回值是一个列表
if len(r) > 0:
    print('包含Python')
else:
    print('不包含Python')

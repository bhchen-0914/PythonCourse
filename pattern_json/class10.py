"""
整理json数据类型转换为python数据类型
json          python

object        dict
array         list
string        str
number        int/float
true          True
false         False
null          None

反序列化
"""
import json

student = [
            {'name:': '吴彦祖', 'age': 19, 'flag': True},
            {'name:': '陈柏宏', 'age': 18}
          ]

json_str1 = json.dumps(student, ensure_ascii=False)  # dumps函数实现序列化，其接收的参数是一个object对象,ensure_ascii参数是指明是否将汉字转为ASCII码
print(type(json_str1), json_str1)

"""
总结json对象，json，json字符串
对于以上3项的理解，需要跳出JavaScript的范围，json不是JavaScript的附属，某种程度上说，是平级的语言概念
json对象在js里，是包含用于解析json，与将对象/值转换为json两种方法的对象，在python里没有特别的意义

"""
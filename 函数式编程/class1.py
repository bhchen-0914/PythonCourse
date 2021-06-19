"""
lambda表达式,匿名函数
lambda语法：lambda(关键字) + parameter_list（参数列表）: + expression（表达式）\
三元表达式
filter:用于过滤不需要的元素
filter(function or None, iterable),function的返回值只能是布尔类型的
"""
import re


def add(x, y):
    return x + y


f = lambda x, y: x + y  # 等价于add函数

print(add(1, 9))
print(f(1, 9))

#  三元表达式  x ,y ，条件为真时返回的结果 + if 条件判断 else + 条件为假时返回的结果
x, y = 2, 1
result = x if x > y else y
print(result)
"""
以上等价于
x, y = 2, 1
if x > y：
    return x
else：
    return y
"""

list_x = [1, 2, 'hello', 3, 'world']
str1 = 'sasdSSDdfdSDFvf23d6!!!_sdRA'
result2 = filter(lambda param: True if isinstance(param, int) else False, list_x)  # 过滤非int类型的数据
print(list(result2))
result3 = filter(lambda i: True if i.isupper() else False, str1)  # 过滤非大写的字符
print(list(result3))
result4 = filter(lambda i: re.match('[A-Z]', i), str1)  # 使用正则表达式的写法
print(list(result4))


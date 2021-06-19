# -*- coding: UTF-8 -*-

"""
总结
对象的三个特征：身份（id），值(Value)，类型(type)
"""

# 判断身份用身份运算符
a = 1
b = 1.0
print(a is b)

# 判断值用比较运算符
print(a == b)

# 使用isinstance方法可判断数据类型
list1 = [1, 2, 3]
list2 = [2, 1, 3]
print(isinstance(list2[0], str))
print(isinstance(list1, (list, tuple, set, dict)))

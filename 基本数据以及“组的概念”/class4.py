# -*- coding: UTF-8 -*-
"""
序列总结
字符串、列表、元组都是序列
"""

str1 = 'hello world'
list1 = [1, 2, 'hello world']
tuple1 = (1, 2, 3, True)
print(str1[1], list1[0], tuple1[3])  # 序列可以通过[x]的方式索引元素，序列内的元素都会被分配序号
print(str1 * 2, list1 + [3, 4], tuple1 * 2)  # 系列可以使用+ ，* 操作方式

print(str1[0::2])  # 切片操作，0:9表示选取范围，2表示步长

# 使用 in 方法判断某个元素是否在序列内,返回布尔值
print(str1 in list1)
print(True not in tuple1)

# 使用len方法返回序列的长度
print(len(str1))

# max方法返回最大值，min方法返回最小值,比较字符串大小时，是将元素转换为ASCII码，再比较大小
print(max([1, 2, 3, 4]))
print(min('a', 'b', 'c', 'd'))

# 使用ord方法将元素转化为ASCII码
print(ord('a'))
print(ord(' '))
print(ord(','))

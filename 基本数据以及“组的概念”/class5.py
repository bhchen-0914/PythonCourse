# -*- coding: UTF-8 -*-
"""
set集合：{}， dict字典：{key，value}
"""
# set集合是一个无序数据类型

set1 = {1, 2, 3, 4, 'hello'}
print(type(set1))

# 集合内的元素不会重复
print({1, 1, 2, 2})

# 集合也可以用 in 判断元素是否存在，用 len 返回集合长度
print(10 not in set1)
print(len(set1))

set_1 = {1, 2, 3, 4, 5, 6}
set_2 = {4, 5, 6, 7, 8}

# 求两个集合的差集: -
print(set_1 - set_2)

# 求两个集合的交集: &
print(set_1 & set_2)

# 求两个集合的并集：|
print(set_1 | set_2)

# 用set()表示空集
print(type(set()))
a = set()
print(set1 & a)
print(set_2 | a)

# 字典：{Key1:Value1:Key2:Value2,Key3:Value3.....}
dict1 = {1: 124, 'first name': 'hello', 'last name': 'world', 'age': 18}
print(type(dict1))
print(dict1['age'])  # 字典和集合一样，不可用[x]访问元素,可通过['Key']访问Value
dict1 = {1: 124, 'first name': 'hello', 'last name': 'world', 'age': 18, 'age': 20}
print(dict1)
print(dict1['age'])  # 字典中Key值相同时，会保留后一个key的Value值

'''
字典的value值可以是任意值，包括int,float,str,list,set,dict等
字典的Key值必须是不可变类型，比如int,str,tuple
'''

"""
请根据列表list1 = [1，2，3，4，5，6]，使用一行代码生成一个新的列表list2
list2中每个元素是list1中的平方
"""
list1 = [1, 2, 3, 4, 5, 6]
# 方法1，使用lambda表达式配合map函数(函数式编程)
list2 = list(map(lambda x: x * x, list1))
print(list2)

# 方法2，使用列表推导式
list3 = [x * x for x in list1]
print(list3)

'''
延申：其他推导式
'''

# 带条件的列表推导
list4 = [x * x for x in list1 if x > 2]
print(list4)

# 字典推导式
my_dict = {
    "key1": 1,
    "key2": 2,
    "key3": 3
}
dict1 = {value: key for key, value in my_dict.items()}  # 键值转换
print(dict1)

key = [key for key, value in my_dict.items()]  # 提取key值
print(key)

value = tuple(value ** 2 for key, value in my_dict.items())  # 操作value
print(value)
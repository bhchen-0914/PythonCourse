"""
map类
map(function, param_list) 将参数列表中的每一项都传入函数中，执行一次函数，并接受函数的返回结果
map与lambda（map真正的使用方式）
"""
list_x = [1, 2, 3, 4, 5, 6, 7, 8]


def curve(x):
    a, b, c = 2, 3, 4
    return a * x ** 2 + b * x + c


r = map(curve, list_x)
print(list(r))  # 要将结果转换为列表
"""
以上写法等价于
list1 = []
for x in list_x:
    list1.append(curve(x))
print(list1) 
"""

# map与lambda混合使用
result = map(lambda x: 2 * x ** 2 + 3 * x + 4, list_x)
print(list(result))

list1 = [1, 2, 3, 4]
list2 = [1, 2, 3, 4]
list3 = [1, 2, 3, 4]
result2 = map(lambda x, y, z: x ** 3 + y ** 3 + z ** 3, list1, list2, list3)  # 有多个参数时的用法
print(list(result2))

list4 = [1, 2]
result3 = map(lambda x, y, z: x ** 3 + y ** 3 + z ** 3, list1, list2, list4)
print(list(result3))  # 只有2个值，map返回的结果数取决于最少的参数列表的数量

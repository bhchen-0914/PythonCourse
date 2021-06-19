# -*- coding: UTF-8 -*-
"""
运算符学习
"""

# 以下为算数运算符

print([1, 2, 3] + [1, 2, 4])  # 加号

print([1, 2] * 2)  # 乘法

print(3 / 2)  # 除

print(3 // 2)  # 整除

print(5 % 3)  # 取余数

print(3 ** 4)  # 取次方

# 赋值运算符，目的是给变量赋值
a = 1  # 赋值
a += 1  # 等价于a=a+1
print(a)

b = 10
b -= a  # 等价于b = b -a
print(b)

b *= a  # 等价于b = b*a
print(b)

b **= a
print(b)  # 等价于b = b^a

# 还有b /=a , b %= a , b // a 等操作


# 比较运算符，返回一个bool值

m = [1, 2, 3]
n = [1, 2, 3, 4]
l = [1, 2, 3]
print(m == l)
print(n > m)
print(m[0] >= n[1])
print(n <= l)
print(m != n)

num = 1
num += num < 1
print(num)  # num < 1 返回False，num += num < 1 等价于 num = num + False ,False的int值为0

# 不止是数字才能用比较运算符
print('a' <= 'b')  # 字符的比较是将其转换为ASCII码，再进行比较
print('aba' > 'aaz')  # 字符串的比较是逐个比较，若第一个字符相同则比较下一个，第一次不同的结果即为字符串比较的结果
print([1] > [1, 2, 3, 4])  # 列表、元组的比较规则与字符串相同

# 逻辑运算符
# and、or、not 逻辑运算符主要用来操作bool类型，返回结果也是bool类型

# and代表且运算，当都为True时才会返回True
print(True and True)
print(True and False)
print('a and b:')
print('a' and 'b')

# or代表或运算，当有一个为True即返回True
print(False or False or True or False)
print(False or False)
print('a' or 'b')

# not代表非运算，非真即假
print(not False)
print(not True)
print(not '')

# 对于int,float类型，非0时表示True，为0时表示False
# 对于str类型，非空时表示True，空时为False，使用or和and运算时，如果结果为True，则返回非空字符串
# list,tuple,set,dict类型与str类型相似
print([1, 2, 3] and [])
print(() or (1))

# and运算会比较所有数，当都为真时，则会返回最后一个
print(2 and 1)
print(1 and 2)
# or运算只要有一个为True则为True，当结果为真时，返回第一个True的值
print(0 or '' or [1] or False)
print(0 and '' or [1] or False)

# 成员运算符，用来判断一组元素是否在另一组元素中，返回值是bool
print((1, 2) in [1, 2, (1, 2)])
print('hello' not in 'hello world')
print('hh' in {'name': 'hh'})
print('name' in {'name': 'hh'})  # 字典中成员运算只能算Key值

# 身份运算符，(is ,is not)返回一个bool值
k1 = 1
k2 = 1.0
# 比较运算符== 比较的是2个变量值的大小，而身份运算符 is 比较的是两个变量的身份是否相同，这里可理解为内存地址是否相同
print(k1 == k2)
print(k1 is k2)
print(id(k1))
print(id(k2))
set1 = {1, 2, 3}
set2 = {2, 1, 3}
tuple1 = (1, 2, 3)
tuple2 = (2, 1, 3)
list1 = [1, 2, 3]
list2 = [2, 1, 3]
print(set1 == set2)
print(set1 is set2)
print(tuple1 == tuple2)
print(tuple1 is tuple2)
print(list1 == list2)
print(list1 is list2)
print(type(tuple1[2]) == int)
print(isinstance(list2[0], int))
# 集合set是无序数据类型，值tu的大小与顺序无关，因此 == 结果为True，但内存地址不同，is 结果为False
# tuple,list是有序数据类型，比较大小时是逐一比较，因此 == 为False

print(isinstance(list2[0], str))
print(isinstance(list1, (list, tuple, set, dict)))

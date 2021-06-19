# -*- coding: UTF-8 -*-

"""
for循环与for...else...
for循环主要用来遍历/循环序列或集合、字典
"""

list1 = [1, 2, 'hello', 3.14, True, False, [1, 2], {'name': 'john'}, (1, 2), 0]
for item in list1:
    print(item)

# for循环嵌套
print('以下为嵌套循环：')
Array = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[11, 12, 13], [14, 15, 16], [17, 18, 19]],
         [[21, 22, 23], [24, 25, 26], [27, 28, 29]]]

for i in Array:
    for j in i:
        for k in j:
            print(k, end=' ')

list2 = [1, 2, 3, 4, 5]
print('\n')
for i in list2:
    if i == 3:
        continue
    print(i)
else:
    print('over')

# contiune表示跳出本次循环，后续循环还会继续进行；break表示跳出所有循环，后面的循环不会再进行

for i in list2:
    if i == 3:
        break
    print(i)
else:
    print('over')

# 在嵌套循环中，break只会跳出这一层的循环,for i in Array这一层的循环仍会进行
print('break:')
for i in Array:
    print('i:', i)
    for j in i:
        if j == [11, 12, 13]:
            break
        print('j:', j)
        for k in j:
            print('k:', k)

# break终止的是最外层循环，嵌套的循环都将终止
print('break2')
for i in Array:
    if [4, 5, 6] in i:
        break
    print('i:', i)
    for j in i:
        print('j', j)
        for k in j:
            print('k:', k)

# range左闭右开
print('for... range:')
for x in range(0, 10):
    print(x)

for x in range(0, 10, 2):
    print(x, end=' ')  # 2是步长

# 反向取等差数列,步长的正负表示取的方向，负号表示反向取值
print('\n')
for x in range(10, 0, -2):
    print(x, end=' ')
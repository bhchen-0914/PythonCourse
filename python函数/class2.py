# -*- coding: UTF-8 -*-
"""
让函数返回多个结果
python函数返回的结果无需定义类型
介绍序列解包
"""


def show():
    print('this is a')
    return  # print('this is b')   不会执行，因为return会直接结束函数进程


# show()
"""
def count(a, b, out/ref result2):     C语言返回多个结果
    result1 = a + b
    result2 = a * b
    # return result1   /  return (result1, result2) java使用数组集合或封装对象
"""


def count(a, b):
    result1 = a + b
    result2 = a * b
    return result1, result2  # 返回多个参数


result = count(2, 3)
print(type(result))  # 函数返回的多个结果以元组的形式储存
print(result[0], result[1])  # 可以使用返回的结果，但是不推荐使用序号的方法访问

# 序列解包
add_result, mul_result = count(2, 3)  # 推荐使用这种方法，使用有意义的变量名称来接收返回结果
print(add_result, mul_result)

# a = 1
# b = 2
# c = 3  以上代码可以表达为：a, b, c = 1, 2, 3

a, b, c = 1, 2, 3
print(a, b, c)
d = 1, 2, 3
print(type(d), d)  # 反向过程

m, n = 'ab'
print(m)  # 解包的对象不一定是元组，只要是序列都可以使用序列解包

# j, k = (1, 2, 3)  会报错，接收变量的个数要与元素个数相等

x = y = z = 1  # 链式赋值
print('x: %d' % x, 'y: %d' % y, 'z: %d' % z)

# -*- coding: UTF-8 -*-

"""
变量作用域
"""

c = 50  # 函数外部定义的变量，全局变量，全局变量的作用域不仅仅局限于模块内，整个应用程序内都可以调用


def add(a, b):
    c = a + b  # 函数内部定义的变量c，作用域只存在与函数内，局部变量
    print(c)


add(1, 3)
print(c)


def demo():
    d = 20


# print(d)  会报错，d的引用已经超出了d的作用域

def demo2():
    e = 20  # 此处的e相对于循环体来说不是全局变量，因此局部变量的概念是相对的
    for i in range(0, 6):
        e += i
    print('e:', e)


demo2()
num = 0
for j in range(0, 10):
    num += j
    k = 'hello'
print(num)
print(k)  # python可以在循环体外部直接调用循环内部的变量，因为python没有块级作用域的概念。循环无法形成单独的作用域
# java、C不行，需要在循环外初始化k的值，


x = 1


def func1():
    x = 2  # 注释此处，打印？
    print('this is func1:', x)

    def func2():
        x = 3  # 注释此处，打印？
        print('this is func2:', x)

    func2()
    print('this is func1:', x)


# 作用域链，逐级寻找

func1()
print(x)
list1 = [1, 2]   # list作为引用类型，函数的调用可以改变它的值


def func3():
    list1[0] = 2  # 注释此处，打印？
    print('this is func3:', list1)

    def func4():
        list1[0] = 3  # 注释此处，打印？
        print('this is func4:', list1)

    func4()
    print('this is func3:', list1)


func3()
print(list1)

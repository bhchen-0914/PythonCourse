# -*- coding: UTF-8 -*-

"""
参数类型：
1. ...
2. ...
3. ...
4. 可变参数
"""


def demo(*param):  # 用*来定义可变参数
    print(param)
    print(type(param))
    print('~~~~~~~~~~~~~~~~~~~~~')


# def demo2(param):
#     print(param)
# demo2(('a', 1, 2, 3, [1, 2]))   将元素组装成元组作为参数传入函数，效果与可变参数相同，但不推荐

demo('a', 1, 2, 3, [1, 2])  # python会把可变参数列表对应的实参组装成元组
t = ('a', 'b', 'c')
demo(t)  # 在使用可变参数的同时，再将元组传入，参数会成为一个二维元组
demo(*t)  # 若必须将元素组装成元组传入，可以在实参前加*，*可以理解为解包，解包的对象可以是元组，也可以是列表


def demo3(param1, param2=2, *param):
    print(param1)
    print(param2)
    print(param)
    print('~~~~~~~~~~~~~~~~~~~~~')


demo3('a', 1, 2, 3, 4)  # 这里将1作为默认参数的修改值传给了param2。将默认参数放在可变参数前，


# 无法保持默认参数不变，传入可变参数


# 想将'param2'作为默认参数param2的修改值
def demo4(param1, *param, param2='a'):
    print(param1)
    print(param)
    print(param2)
    print('~~~~~~~~~~~~~~~~~~~~~')


demo4('param1', 1, 2, 3, 4, 'param2')  # 当可变参数在这里会将’param2‘这个值作为可变参数的一部分,而不是默认参数的修改值
demo4('param1', 1, 2, 3, 4, param2='param2')  # 可以使用关键字参数的方法实现既传入可变参数，又改变默认参数
# demo4('param1', param2='param2', 1, 2, 3, 4 )  报错
"""
终告：不要将参数列表设计得太过复杂，在实现功能的前提下，参数列表越简单越好
"""

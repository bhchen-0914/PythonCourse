"""
__all__ 方法可指定import* 导入的变量、方法
"""

# __all__是模块的内置变量
__all__ = ['a', 'b', 'demo1', 'demo2']

a = 1
b = 2
c = 3


def demo1():
    print('this is demo1')


def demo2():
    print('this is demo2')


def demo3():
    print('this is demo3')



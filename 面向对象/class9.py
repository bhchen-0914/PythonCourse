"""
多继承
py2 经典类是按深度优先来继承的，新式类是按广度优先来继承的。
py3 经典类和新式类都是统一按广度优先来继承的。
"""


class A:
    def __init__(self):
        print("A")


class B(A):
    def __init__(self):
        print("B")


class C(A):

    def __init__(self):
        print("C")


class D(B, C):
    pass


d1 = D()

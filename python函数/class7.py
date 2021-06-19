"""
global关键字，将局部变量变为全局变量，其他模块也可以调用
"""

a = 0


def demo():
    global a
    a = 10


demo()  # 需要执行函数，golbal关键字才会生效
print(a)

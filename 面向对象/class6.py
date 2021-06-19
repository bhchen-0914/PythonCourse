"""
面向对象3大特性：继承性，封装性，多态性
封装性用的最广泛，最容易理解也是最难理解的
类的组成：特性（类变量、实例变量） 方法（静态方法、类方法、实例方法）
建议一个模块只写一个类
"""


class Humam:
    number = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_message(self):
        print('我叫%s,今年%d岁' % (self.name, self.age))

    def test(self):
        print(__class__, 'this is parent method')
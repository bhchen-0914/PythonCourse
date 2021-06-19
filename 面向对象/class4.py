# -*- coding: UTF-8 -*-

"""
在实例方法中访问实例变量与类变量
类方法
静态方法
"""


class Student:
    sum = 0  # 班级人数
    seat = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        # print(name)          # 也可以通过构造函数来访问实例变量，但这里的name和self.name 有本质的区别，这里的name是参数列表的形参
        # print(sum)           # 不可以通过构造函数来访问类变量，这里不会报错的原因是打印了内部函数sum

    def show(self):
        print(self.name)  # 实例方法访问实例变量很简单，通过self. 的方法就可访问，这也是self的定义
        print(self.age)
        print('这里是show方法', self.__class__.sum)  # 通过__class__. 的方法可以访问类变量，self.__class__ 代表的含义就是当前实例所在的类

    def number_now(self):
        self.__class__.sum += 1  # 实例方法操控类变量
        print('当前人数：', self.__class__.sum)

    @classmethod  # 构造类方法
    def seat_add(cls):
        cls.seat += 1
        print('当前座位：', cls.seat)  # 类方法可以访问类变量
        # print(self.name)   会报错，类方法不能访问实例变量

    @staticmethod  # 构造静态方法
    def test_static():
        print('this is staticmethod')
        print(Student.sum, Student.seat)  # 静态方法能访问类变量
        # print(self.name)  会报错，静态方法不能访问实例变量


st1 = Student('吴彦祖', 18)
st1.show()
print(st1.sum)  # 实例方法访问类变量的一种方式
st1.number_now()
Student.seat_add()  # 调用类方法
st2 = Student('谢霆锋', 19)
st2.number_now()
Student.seat_add()
print(Student.seat)
st3 = Student('tom', 21)
st3.seat_add()  # 对象可以调用类方法，但是最好不用，逻辑没有意义
st4 = Student('尼古拉斯', 22)
st4.seat_add()
st4.number_now()
st4.test_static()  # 静态方法可以被对象调用
Student.test_static()  # 静态方法可以被类调用
Student.show(st4)  # 类调用实例方法要将对象作为参数传递
"""
静态方法与面向对象关联性不大，当方法与类和对象关系不大时，可以用静态方法，尽量少用静态方法
"""


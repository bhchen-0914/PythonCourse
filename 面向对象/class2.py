# -*- coding: UTF-8 -*-

"""
类与对象
类：是现实世界或思维世界中的实体在计算机中的反映，它将数据以及数据上的操作封装在一起，可理解为一个模板
    理解类的 行为与特征 是设计类的重要方式，行为要找对主体
对象：类实例化的产物。
构造函数
"""


class Student:
    name = 'student'
    age = 0

    def do_homework(self):
        print("%s's homework has been finished" % self.name)


student1 = Student()
student2 = Student()
print(id(student1))  # student1 和 student2 特征上是同一个对象，但在本质上是两个不同的实例

print(id(student2))


class StudentMessage:
    name = ''
    age = 0

    def __init__(self):   # 构造函数 构造函数可以被显示调用，但不推荐
        print('this is __init__')


student_1 = StudentMessage()
student_1.__init__()  # 会打印2次‘student’,这是因为在类实例化的时候，构造函数会自动调用一次
print(student_1.__init__())  # 构造函数的返回结果默认是None，且只能是None。相当于在__init__()函数里 return None


class StudentInfo:
    name = ''
    age = 0

    def __init__(self, name, age):  # 当构造函数定义了参数时，创建对象的时候也必须传入对应的参数
        # name = name       # 不能访问实例变量的原因在于这样的写法不能定义实例变量，访问的是类变量
        self.name = name    # 初始化对象的熟悉
        # age = age
        self.age = age      # 区别模块变量与类中的变量


tom = StudentInfo('Tom', 18)
print(tom.name)
print()
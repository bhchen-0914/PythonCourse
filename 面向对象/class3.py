# -*- coding: UTF-8 -*-

"""
类变量与实例变量
类与对象的变量的查找顺序
"""


class StudentInfo:
    name = '吴彦祖'  # 这是类变量   # 对于这个类来说，定义名字和年龄的变量并没有意义，因为它是一个抽象的概念。
                                 # 有意义的应该是这个类实例化的对象
    age = 20
    sum = 30   # sum表示一个班级学生人数，这样的类变量是有意义的

    def __init__(self, name, age):
        self.name = name  # 这里使用self定义的特征值表示只与实例相关，与类无关。self不是一个关键字，可以看做一个指针
        self.age = age
        # print(name)
        # print(age)

    def show(self):   # 类中参数包含self的函数称为实例方法
        print('i am %s ' % self.name)
        print('i am %d years old' % self.age)


stu1 = StudentInfo('chen', 18)
print(stu1.name)  # 实例变量
print(StudentInfo.name)  # 类变量
print(stu1.__dict__)  # 打印实例变量
print(StudentInfo.__dict__)  # 打印类变量
stu1.show()
print(stu1.sum)

"""
当python访问实例变量时，首先会在构造函数中查找变量，如果没有，再去访问类变量，如果类里也没有，会到父类中寻找
实例方法中，self必须作为参数显式写入括号中，调用时却不用作为参数传入
"""
# -*- coding: UTF-8 -*-

"""
面向对象
类  对象
类最基本的作用是封装一系列变量和函数
类只能去描述对象，不能执行方法
类和实例最好分不同的模块写
浅谈方法和函数的区别
"""


class StudentMessage:  # 类的命名首字母大写，
    name = 'name'  # 类的变量
    age = 0

    def set_name(self, name):
        self.name = name

    def set_age(self, age):
        self.age = age

    def print_message(self):   # self是固定关键字，是为了初始化实例
        # print('i am %s' % self.name)
        # print('i am %d years old' % self.age)
        print(self.name)
        print(self.age)


student = StudentMessage()  # 实例化对象不用加 new
student.set_name('jack')
student.set_age(18)
student.print_message()
print(StudentMessage.name)
"""
方法：设计层面的意义比如面向对象
函数：主要是程序运行，过程式的一种称谓
比如变量在模块内一般被称为变量，而在类的内部，一般被称为数据成员
"""

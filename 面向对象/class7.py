"""
面向对象3大特性：继承性，封装性，多态性
封装性用的最广泛，最容易理解也是最难理解的
类的组成：特性（类变量、实例变量） 方法（静态方法、类方法、实例方法）
建议一个模块只写一个类
"""

from 面向对象.class6 import Humam


class Student(Humam):
    def __init__(self, name, age, school):  # school为子类特有的变量
        self.school = school
        # Humam.__init__(self, name, age)  # 调用父类构造函数的时候需要传入self,因为这里是类来调用实例方法，需要传入self参数
        super(Student, self).__init__(name, age)  # 推荐这种调用父类方法的方式，更有意义，且不用大量修改代码

    def do_homework(self):
        print("%s's homework has been finished" % self.name)

    def test(self):
        print(__class__, 'this is son method')
        super(Student, self).test()


print(Student.number)  # 子类可以直接继承父类的类变量
student1 = Student('JACK', 18, 'QH')  # 实例化子类时，也要传入父类构造函数的参数
student1.get_message()  # 子类可以直接继承父类的方法
print(student1.age, student1.name)  # 子类可以直接继承父类的实例变量
print(student1.school)
student1.do_homework()
student1.test()  # 当子类的方法和父类重名时，对象会优先调用子类方法(方法的重写)

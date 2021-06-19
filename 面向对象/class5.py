"""
成员的可见性：公开和私有(变量、方法)
内中所有的变量与方法都可以被外部更改，因此不安全，需要私有化
不推荐直接对内中的成员变量直接赋值，改变变量的值，推荐使用方法更改
public：公开的  可在外部直接访问  private： 私有的
"""


class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.score = 0  # 这里的score为实例的特殊变量，不想被外部直接访问
        self.__sum = 0  # __定义私有变量
        self.__level = ''

    def do_homework(self):
        print('%s is doing homework:' % self.name)
        self.do_math_work()  # 类的内部调用实例方法
        self.do_english_work()  # 类的内部调用静态方法

    def do_math_work(self):
        print("%s's Math homework" % self.name)

    @staticmethod
    def do_english_work():
        print('English homework')

    def marking(self, score):  # 通过实例方法修改实例变量score，使用实例方法修改变量，可以保证数据有效性与安全性
        if score < 0 or score > 100:
            print('无效打分')
            return
        self.score = score
        print('%s的分数为：' % self.name, self.score)

    def __private(self):  # 私有方法
        print('这是一个关于%s的私有方法' % self.name)

    def __private__(self):  # 私有方法
        print('这是一个关于%s的私有方法吗？' % self.name)

    def private_test(self):
        print('内部访问私有变量sum：', self.__sum)
        self.__private()  # 内部访问私有方法

    def set_level(self, level):
        if level not in 'ABCD':
            print('非法等级')
        self.__level = level
        print('%s的等级是：' % self.name, self.__level)


st1 = Student('TOM', 18)
st1.do_homework()  # 类的外部调用方法
# st1.score = 90  # 不推荐使用这种办法打分
st1.marking(-1)
st1.marking(100)
# print(st1.__sum) 访问失败，__sum是私有变量
# st1.__private() 会报错，私有方法无法在外部访问
st1.__private__()  # 以__结尾不会被当成私有
st1.private_test()
st1.set_level('A')  # 通过实例方法修改私有变量
st1.__sum = 1  # 因为动态语言的特性，相当于重新给st1增加了一个新的名为__sum的实例变量，与定义的私有变量完全不同
print(st1.__sum)  # 这里打印的是新的__sum变量的值
st1.private_test()  # 对比一下私有变量__sum的值
print(st1.__dict__)
"""
打印出来的'_Student__sum'代表私有变量__sum，python会自动在其前面加上_‘类名’,外部不能访问私有变量,
以及外部可以添加与私有变量同名的新变量的原因正是因为私有变量的储存的程序内部的名字已经发生了改变，这也表示
python无法通过动态的方式添加私有变量，这是python对于私有变量的保护机制（很low）
"""
st2 = Student('吴彦祖', 22)
print(st1.__dir__())
print(st2._Student__sum)  # 能通过特殊的方式访问私有变量，所以说python对于私有变量的保护机制很low
st2._Student__private()  # 私有方法也是类似的情况，所以说python的面向对象里没有什么是绝对不可访问的

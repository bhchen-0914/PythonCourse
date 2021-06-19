class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __new__(cls, name, age):
        if 0 < age < 120:
            return object.__new__(cls)
        print('年龄不合适')


def make_human(name, age):
    obj = Human(name, age)
    try:
        print(obj.name, obj.age)
    except AttributeError:
        print('对象创建失败，无法访问实例变量')


make_human('吴彦祖', 20)
make_human('蔡徐坤', -1)
make_human('TOM', 18)
make_human('monster', 121)
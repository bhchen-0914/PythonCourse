"""
多态指的是一类事物有多种形态，（一个抽象类有多个子类，因而多态的概念依赖于继承）
多态性是指具有不同功能的函数可以使用相同的函数名，这样就可以用一个函数名调用不同内容的函数。
在面向对象方法中一般是这样表述多态性：向不同的对象发送同一条消息，不同的对象在接收时会产生不同的行为（即方法）。
也就是说，每个对象可以用自己的方式去响应共同的消息。所谓消息，就是调用函数，不同的行为就是指不同的实现，即执行不同的函数。
"""


class Animal:
    def talk(self):
        print('i can talk')


class Cat(Animal):
    def talk(self):
        print('喵喵喵')


class Dog(Animal):
    def talk(self):
        print('汪汪汪')


class Human(Animal):
    pass


people = Human()
cat = Cat()
dog = Dog()


def test(obj):
    obj.talk()


test(people)
test(cat)
test(dog)  # 综上可以说，多态性是一个接口,多钟实现

"""
多态性的好处：
（1）增加了程序的灵活性
　　以不变应万变，不论对象千变万化，使用者都是同一种形式去调用，如test(people)
（2）增加了程序额可扩展性
　　通过继承animal类创建了一个新的类，使用者无需更改自己的代码，还是用test(animal)去调用
"""

"""
初识装饰器
"""
import time


def test1():  # 实现打印执行函数的时间
    print('执行%s的时间是:' % test1.__name__, time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))
    print('this is function test1')


def test2():
    print('this is function test2')


def print_current_time(func):  # 通过一个打印时间的函数，传入function类型的参数，达到test1实现的效果，这样的方法比test1便捷，但仍不够好
    print('执行%s的时间是:' % func.__name__, time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))
    func()


def decorator_time(func):  # 装饰器的结构，类似闭包
    def wrapper():
        print('执行%s的时间是:' % func.__name__, time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))
        func()

    return wrapper


@decorator_time  # 语法糖
def test3():
    print('this is function test3')


test1()
time.sleep(2)
print_current_time(test2)
time.sleep(2)
test3()
"""
以上代码等同于没加语法糖时：
f1 = decorator_time(test3)
f1()
使用语法糖能更加直观的提现装饰器对原函数拓展的关系，也更加
直观的提现了装饰器的作用，它没有改变原函数的结构、写法，也没有改变原函数的调用
"""

print(test3.__name__)  # 加了语法糖后，test3的函数名已经变成了装饰器内被封装的函数wrapper

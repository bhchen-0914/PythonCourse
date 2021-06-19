"""
装饰器优化：装饰带参数的函数
"""

import time


def decorator(func):
    def wrapper(*args, **kwargs):  # 不定长参数
        print('执行%s函数的时间是:' % func.__name__, time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))
        func(*args, **kwargs)  # 将参数传入原函数

    return wrapper


@decorator
def print_message(name, age):
    print("my name is %s, I'm %d years old" % (name, age))


print_message('Tom', 19)


@decorator
def hero_message(name, hero_type, **kwargs):  # 带键值对类型的参数
    print('hero_name:', name)
    print('hero_type', hero_type)
    if kwargs:
        for skill, skill_name in kwargs.items():
            print(skill, ':', skill_name)


hero_message('梦魇', '刺客', **{'skill1': '老衲冲击', 'skill2': '港派指压', 'skill3': '精油护体', 'skill4': '合肥推拿'})
hero_message('石头人', '坦克', skill1='印度飞饼', skill2='化骨绵掌', skill3='铁牛冲撞')









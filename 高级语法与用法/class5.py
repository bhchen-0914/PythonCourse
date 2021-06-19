"""
题目：
一个人初始位置为0，每次运动x个单位，要求返回若干次运动后的坐标
要求用非闭包和闭包两种方式解决
"""

#  用闭包方式解决：

origin = 0


def func(poi):  # 解决此问题的关键在于poi称为环境变量
    def run(step):
        nonlocal poi  # nonlocal作用是将内层函数变量上升到外层作用域，这是实现poi保存上次位置的关键步骤
        now_poi = step + poi
        poi = now_poi  # 保存位置
        return now_poi

    return run


person = func(origin)
print('环境变量：', person.__closure__[0].cell_contents)
print(person(1))
print('环境变量：', person.__closure__[0].cell_contents)
print(person(3))
print('环境变量：', person.__closure__[0].cell_contents)
print(person(5))

"""
闭包的方式可以不用改变origin的值，此方法优于global方法
"""

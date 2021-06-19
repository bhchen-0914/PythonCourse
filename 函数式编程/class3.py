"""
reduce
reduce(function<函数>, sequence<序列>, initial=None)
reduce的function参数只能有2个参数
"""
from functools import reduce

# reduce是做连续的运算，会连续调用函数,如下：第一次调用时x=1，y=2，第一次调用后结果为3，第二次调用时会将3作为第二次调用x的值，y=3，往后类推
list1 = [1, 2, 3, 4]
r1 = reduce(lambda x, y: x + y, list1)
print(r1)
r2 = reduce(lambda x, y: x + y, list1, 10)  # 第三个参数是初始值，这里的初始值为10，第一次调用是10+1
print(r2)

"""
旅行者问题，现在旅行者运动的轨迹为2维，以（x,y）表示，求若干次运动后的坐标
"""
start = (0, 0)
run = [(1, 2), (5, 5), (0, -1), (1, 9)]
local = reduce(lambda now_poi, next_poi: (now_poi[0] + next_poi[0], now_poi[1] + next_poi[1]), run, start)
print(local)

# 闭包方式
local_poi = [(0, 0)]


def func(poi):
    def move(step):
        nonlocal poi
        local_poi.append(step)
        new_poi = reduce(lambda now_poi, next_poi: (now_poi[0] + next_poi[0], now_poi[1] + next_poi[1]), local_poi)
        poi = new_poi
        return poi
    return move


tourist = func(local_poi[0])
print('环境变量：', tourist.__closure__[0].cell_contents, '运动坐标：', (0, 1))
print(tourist((0, 1)))
print('环境变量：', tourist.__closure__[0].cell_contents, '运动坐标：', (2, 9))
print(tourist((2, 9)))
print('环境变量：', tourist.__closure__[0].cell_contents, '运动坐标：', (3, 7))
print(tourist((3, 7)))
print('环境变量：', tourist.__closure__[0].cell_contents, '运动坐标：', (-1, -9))
print(tourist((-1, -9)))
print('环境变量：', tourist.__closure__[0].cell_contents, '运动坐标：', (-2, 7))
print(tourist((-2, 7)))


"""
题目：
一个人初始位置为0，每次运动x个单位，要求返回若干次运动后的坐标
要求用非闭包和闭包两种方式解决
"""

#  非闭包方式

origin = 0  # 初始为位置


def run(step):
    global origin
    now_poi = origin + step
    origin = now_poi
    return origin


print(run(2))
print(run(5))
print(run(8))
print(run(10))
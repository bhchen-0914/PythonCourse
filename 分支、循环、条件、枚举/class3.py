# -*- coding: UTF-8 -*-

"""
snippet、嵌套分支、代码块概念
"""

# 可以在File>Setting>Live Templates>python里设置补全代码块的功能，类似snippet
from methodclass import timetable

"""
if True:
    pass
elif True:
    pass
else:
    pass

for target_list in expression_list:
    pass

class classname:
    pass
"""

# 代码块，嵌套
"""
if condition1:
    if condition11:
        code1
        code2 
    elif condition22:
        code3
        code4
elif condition2:
    if condition21:
        code5
        code6
    elif condition22:
        code7
        code8
else:
    code9
    code10
"""
# 一个代码块的同级代码都会被执行
timetable.cat_time()
num = int(input('输入一个数:'))

'''
if num == 0:
    print('零')
else:
    if num < 0:
        print('负数')
    else:
        if num > 0:
            print('正数') 
'''
# 以上代码等价于：
if num == '0':
    print('零')
elif num < 0:
    print('负数')
else:
    print('正数')

# 可以看出使用elif可以减少嵌套的层数，增加代码可读性



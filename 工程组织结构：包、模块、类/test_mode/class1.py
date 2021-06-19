# -*- coding: UTF-8 -*-
"""
python工程的组织结构：包，模块，类
包的物理表现形式为目录
模块的物理表现形式为.py文件
类（class）包含函数和变量
"""

# 要让一个文件夹成为一个python包，必须包含一个_init_.py文件,而_init_py模块的名字为包名，这里为test_mode

# import methodclass.c2 as c2
# import methodclass.timetool as timetool

from methodclass import c2
from methodclass import timetable
from methodclass.c2 import lis1
from methodclass.c1 import *  # __all__ 方法可指定import* 导入的变量、方法

# from...import可导入模块的变量、方法等

a = c2.add(1, 3)
print(a)
timetable.cat_time()
print(lis1)
print(b)
demo1()
demo2()

"""
注意：
包和模块不会被重复的导入
导入包和模块时应避免循环导入

"""
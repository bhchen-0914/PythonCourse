# -*- coding: UTF-8 -*-
"""
__init__.py模块的作用
"""
from methodclass import *
import methodclass as mc
c1.demo3()
c1.demo1()
c2.add(1, 2)
print(c2.lis1)
timetable.cat_time()
# c3.init_test()会报错，因为初始化时__init__.py文件中没有指定c3模块

# 可通过__init__.py文件批量导入包
mc.time.sleep(1)
print(mc.sys.path)

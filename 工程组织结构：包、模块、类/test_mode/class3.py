# -*- coding: UTF-8 -*-
"""
模块内置变量
一般来说双下划线的变量是系统内置变量，如：__name__ , __package__ 等
"""
import methodclass.c4
import time
infos = dir()  # 使用dir（）函数可得到模块内所有变量
print(infos)
infos2 = dir(time)  # 带参数的时候，可以得到参数的所有属性和方法列表
print("info2:", infos2)

print('name:', __name__)  # 当.py文件作为入口文件时，name为__main__
print('package:', __package__)  # 当.py文件作为入口文件时，不属于任何包
print('doc:', __doc__)
print('file:', __file__)


"""
用于测试绝对和相对导入
"""
from .demo2 import test  # 相对导入

test()
from ..demo3 import test_demo3  # ..import 用来相对导入上层目录的模块

test_demo3()
print('~~~~~~~~~~~~~~~~~~~~~demo~~~~~~~~~~~~~~~~~~~~~~')
print('this is demo')
print('demo', __package__)
print('demo：', __package__)

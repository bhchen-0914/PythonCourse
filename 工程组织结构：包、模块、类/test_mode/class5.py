# -*- coding: UTF-8 -*-

"""
相对导入与绝对导入
绝对导入是从顶级包，一层一层向下寻找，untitled工程内的顶级包为
methodclass、package1等一级目录
"""
import package1.pcakage2.directory1.demo

"""
运行结果：
~~~~~~~~~~~~~~~~~demo2~~~~~~~~~~~~~~~~~        ps：demo1相对导入demo2模块的内容
demo2: package1.pcakage2.directory1.demo2  
demo2： package1.pcakage2.directory1
This is deemo2
~~~~~~~~~~~~~~~~~demo3~~~~~~~~~~~~~~~~~         ps：demo1相对导入demo3模块的内容
demo3: package1.pcakage2.demo3
demo3： package1.pcakage2
This is demo3
~~~~~~~~~~~~~~~~~~~~~demo~~~~~~~~~~~~~~~~~~~~~~  demo模块本身的内容
this is demo
demo package1.pcakage2.directory1
demo： package1.pcakage2.directory1
"""

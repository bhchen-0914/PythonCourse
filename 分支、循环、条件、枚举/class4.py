# -*- coding: UTF-8 -*-
"""
while循环

while condition:
    code...

while condition:
    code...
else:
    code...
"""
# while循环通常使用在有目标，但循环次数未知的情况下，也常用于递归函数

i = 0
while i <= 10:
    print(i)
    i += 1
else:
    print('over')

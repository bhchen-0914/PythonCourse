# -*- coding: UTF-8 -*-
"""
字符串学习
"""
a = 'hello world'
b = "hello world"
print(type(a))
print(type(b));
# 单双引号都表示字符串，但可以用单双引号来表示一段字符串
print("let's go")
print('let"s go')
# print('let's go') 这种表示会出错，单双引号就是为了解决类似情况
print('let\'s go')
# 这里的\是转义字符。

'''
多行字符串
'''
print('''
    hello world
    hello world
    hello world
    ''')  # 使用'''打印多行字符串

print('hello world\nhello world\nhello world')
# 使用\n可以换行
print('hello \
world')  # \可以让字符串换行

'''
转义字符
\n      换行
\'      单引号
\t      横向制表符
\r      回车   
'''
print('hello \\n world')  # 若要打印转义字符，在转义字符前加上\即可，这里将n变为普通字符，\\变为转义字符
print(r'hello \n world \n my \n world')  # 在打印的字符串前加上r，可打印原始字符串

'''
字符串运算
'''
m = 'hello'
n = 'world'
print(m + n)
print(m * 3)
print(m[0] + n[1])
print(m[-1])
a = 'hello world'
print(a[0:5])  # 截取‘hello’字符串，截取时要左闭右开
print(a[0:-1])  # 左闭右开
print(a[6:100])  # 当右区间大于字符长长度时，会截取到字符串最后一位
print(a[2:])  # 表示截取下标为2的字符开始到后面的所有字符
print(a[-5:])

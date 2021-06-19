# -*- coding: UTF-8 -*-

"""
条件控制语句，与 pylint规范
if ...else...
"""
Y = False
if Y:
    print(Y)
else:
    print('N')

admin = {'account': 'bhchen3', 'password': '123456'}
user_account = input('请输入用户名:')
user_password = input('请输入密码:')
if user_account == admin['account'] and user_password == admin['password']:
    print('success')
else:
    print('fail to access')

# python中没有真正意义上的常量，他们的值都可以通过赋值来改变。
# python中形式上的常量，一般用大写字母表示,如ACCOUNT = 'name123'
# 标准的模块里应该有由""" """多行注释的模块说明
# 不是在函数或类中，会被pylint认为是常量



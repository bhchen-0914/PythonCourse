# -*- coding: UTF-8 -*-

"""
表达式
"""

# 表达式是运算符和操作数所构成的序列
ex1 = 1 + 2 * 3  # 也是一个表达式，= 是赋值运算符
ex2 = 1 + int('1')  # 表达式中可包含函数调用

a = 1
b = 2
c = 5
print(a + b * c)  # 7
print(a or b and c)  # 1
print((a or b) and c)  # 3
# 运算符的优先级不同，得出的结果也不同，*优先于 + -， and优先于or ，（）优先级最高
# 若优先级同级，解释器会从左向右解释，这种情况为左结合
# 运算优先级具体情况参照网页：http://c.biancheng.net/view/2190.html
d = a + b + c  # 当又赋值符号 = 时，表达式为右结合，即先运算 = 右边的式子
print(d)

print(not a or b + 2 == c)  # False 根据表达式的优先级，not a or b + 2 == c 的运算顺序等价为：（not a） or （（b + 2） == c）
print(not (a or b) + 2 == c)  # True ,括号改变了运算顺序

# -*- coding: UTF-8 -*-

"""
形式参数（形参）,定义函数时的参数；实际参数（实参）：调用函数时的参数
参数类型：
1.必须参数：定义函数时参数列表定义的必须赋值的参数，缺少必须参数函数无法执行
2.关键字参数：在调用函数时可以明确指出实参是赋值给哪个形参，而不用考虑形参的顺序
3.默认参数：赋予的默认值的参数,可以省略重复参数的赋值，简化调用函数的过程
"""


def sub(x, y):  # 此处x,y为必须参数，也是形参
    result = x - y
    return result


sub1 = sub(2, 1)  # 此处为实参
print(sub1)
sub2 = sub(y=2, x=3)  # 关键字参数可以不用考虑形参的顺序


# 关键字参数主要是为了代码的可读性和方便性。关键字参数的意思在于函数的调用上，而不是函数的定义


def print_student_message(name, stu_id, age=18, sexual='M'):  # 默认参数
    print('name: ', name)
    print('stu_id: ', stu_id)
    print('age: ', age)
    print('sexual: ', sexual)
    print('~~~~~~~~~~~~~~~~~~~~~~~')


"""
默认参数规则：
没有默认值的参数在调用时一定要传入值
定义函数时，非默认参数不能放在默认参数后（默认参数必须放在参数列表的最后）
使用关键字参数方法调用时，非默认参数也不能放在默认参数后
"""

print_student_message('jack', 1235, )
print_student_message('john', 1213, 20, 'FM')
# print_student_message('Tom', 12333, 'FM') 调用不正确，因为形参和实参顺序没有对应
print_student_message('Tom', 12333, sexual='FM')  # 当需要改变的默认参数与形参顺序有冲突时，可以使用关键字参数
# print('jerry', age=10, stu_id=1234, sexual='FM')  会报错，因为age默认参数放在了非默认参数前
print_student_message('jerry', 1234, sexual='FM', age=12)

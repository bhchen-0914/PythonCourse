"""
认识函数
终端python3内输入，help（函数名）可返回该函数介绍
函数特征：
1.功能性，一个函数必定会有目的
2.隐藏细节，调用者不必关注函数内部逻辑，只需关注结果
3.避免编写重复的代码
4.可以组织代码
函数的执行流程和调用顺序
"""

result = round(3.1415, 3)  # round(unm1, num2)函数,表示将num1保留到小数点后num2位，并四舍五入
print(result)

# 自定义函数
# def func_name(parameter_list):   def是构造函数关键字，后面跟函数名和参数列表
#    pass

'''
def print(code):     
    print(code)
print('a')        会报错：Previous line repeated 995 more times，递归超过995次
                        maximum recursion depth exceeded 超过递归最大深度
'''


def add(a, b):
    add_result = a + b
    print(add_result)
    return add_result   # 若没有返回值则无意义


def print_code(code):
    print(code)
    return code


a = add(1, 4)
b = print_code('hello')
print(a, b)

# -*- coding: UTF-8 -*-
A = [1, 2, 3, 4]  # 将列表的值赋值给A

'''
变量命名规则：
1、首字母不能是数字
2、只能用数字、字母、下划线命名变量
3、系统保留关键字不能用来命名，（type不是保留关键字，但不建议用来命名）
4、变量的命名区分大小写
5、可以把任意数据类型复制给python变量，这是因为python作为一种动态语言的最大特性，即变量类型不固定性
'''

a = 1
b = a
a = 12
print(id(a))
print(id(b))
print(b)  # int、str作为不可变类型，系统会为a,b分配2个不同的内存地址，因此b不会随a的改变而改变

m = [1, 2]
n = m
m[0] = 2
print(id(m))
print(id(n))
print(n)  # list作为可变类型，在m = n 时，系统会为m，n分配2相同的内存地址，因此m的值改变，n也会随之改变

'''
值类型与引用类型
引用类型是可变的，当指向发生改变时，会本身进行变化；值类型是不可变的，当指向发生改变时，会生成一个新的值类型
简单来说，引用类型是可变类型，如list、set、dict等，值类型是不可变类型，如int、str、tuple等
'''
list1 = [1, 'str']  # list为引用类型，int、str为值类型
# 如上文，b = a 时，a，b指向了同一个值类型：1，当a = 12时，a指向了新的值类型：12，而b没有改变执向，b依然为1
# 当n = m 时，n与m指向了同一个引用类型[1,2]，当m[0] = 2时，引用类型[1,2]变为[2,2]，此时没有新的引用类型出现，
# m，n依然指向同一个引用类型，因此m的值改变后，n也同样改变

str1 = 'hello'
print(str1)
print(id(str1))
str2 = str1 + ' world'
print(str2)
print(id(str2))  # 此处的str的id地址已经发生了改变，相当于另一个变量
print(str2[0])  # str[0] = 'i' 此处会报错：TypeError: 'str' object does not support item assignment，因为str是一个值类型，不可变

import copy

list_1 = [1, 2, 3]
list1 = ["a", "b", 1, 2, list_1]

a = copy.copy(list1)  # 浅拷贝
b = copy.deepcopy(list1)  # 深拷贝

print("a==b?", a == b)
print("a==list1?", a == list1)
print("a[4] == tuple1?", a[4] == list_1)
print("b[4] == tuple1?", b[4] == list_1)

"""
深拷贝相当于重新开辟一块内存空间，把原有数据拷贝进去，此时深拷贝的对象与原有数据已经没有关联
浅拷贝相当于重新复制一份数据，对于引用数据类型的元素，只是引用地址指针改变
"""

print("list1", id(list1))
print("a", id(a))
print("b", id(b))
print("list1[4]", id(list1[4]))
print("a[4]", id(a[4]))
print("b[4]", id(b[4]))

# 改变list_1 的值，深拷贝数据不受影响，浅拷贝值改变
list_1.append(4)
print("a", a)
print("b", b)

"""
对于不可变类型，浅拷贝与赋值操作一样，只是用一个新变量接收原来的内存地址的引用
只有深拷贝是相当于重新有开辟内存空间
"""
t1 = (1, 2, 3, list_1)
a1 = t1
b1 = copy.copy(t1)
c1 = copy.deepcopy(t1)
print("a1", id(a1))
print("b1", id(b1))
print("c1", id(c1))
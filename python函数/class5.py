# -*- coding: UTF-8 -*-

"""
参数类型：
1. ...
2. ...
3. ...
4. ...
5. 关键字可变参数
"""


def stu_age(**param):
    for key, value in param.items():  # 遍历字典所有元素
        print(key, ':', value)


stu_age(john=18, jack=20)  # 传入键值对
message = {'john': 18, 'jack': 20}
stu_age(**message)  # 传入字典


for keys in message.keys():  # 遍历字典key值
    print(keys)

for values in message.values():  # 遍历字典value值
    print(values)



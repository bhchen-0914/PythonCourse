"""
枚举是一个类
枚举类型、枚举名称和枚举值
枚举转换
"""

from enum import Enum


class VIP(Enum):  # 继承枚举的类
    RED_DIAMOND = 1   # 枚举的标识建议用大写
    YELLOW_DIAMOND = 2
    GREEN_DIAMOND = 3
    BLUE_DIAMOND = 4
    BLACK_DIAMOND = 5
    # BLACK_DIAMOND = 10 会报错，key值重复


print(VIP.BLACK_DIAMOND)  # 和普通的类不同，打印的结果就是 VIP.BLACK_DIAMOND，也就是枚举的标识,和也是枚举的意义所在
print(type(VIP.RED_DIAMOND))  # 类型为<enum 'VIP'>,也就是VIP类

"""
表示类型还有以下几种方式：
    全局变量；(最不可取)
yellow = 1
red = 2
black = 3
    
    字典：
{'yello': 1, 'red': 2, 'blcak': 3}

    普通类封装：
class TYPE:
    yello = 1
    red = 2
    black = 3
    
以上几种表示类型的方法有2个缺陷：
1.类型或变量可变
2.不能规避重复    
"""

# VIP.RED_DIAMOND = 3  会报错，枚举中的值不可被更改
print(type(VIP.RED_DIAMOND.value), VIP.RED_DIAMOND.value)  # .value获取类型的数值
print(type(VIP.RED_DIAMOND.name), VIP.RED_DIAMOND.name)  # .name获取标签的名字,是str类型，与之前的VIP.RED_DIAMOND的VIP类型做区分
print(type(VIP['RED_DIAMOND']), VIP['RED_DIAMOND'])   # 通过枚举的名称可以得到枚举的类型
"""
要注意区分枚举类型、枚举名称、枚举值
"""

for vip in VIP:  # 可以通过for循环遍历枚举
    print(vip)


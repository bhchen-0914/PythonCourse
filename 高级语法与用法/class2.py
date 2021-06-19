"""
枚举的比较运算
枚举的注意事项
IntEnum，unique 使用方法
"""

from enum import Enum
from enum import IntEnum, unique


class VIP(Enum):
    RED_DIAMOND = 1
    YELLOW_DIAMOND = 2
    GREEN_DIAMOND = 3
    BLUE_DIAMOND = 4
    BLACK_DIAMOND = 1


class VIP2(Enum):
    RED_DIAMOND = 1
    YELLOW_DIAMOND = 2
    GREEN_DIAMOND = 3
    BLUE_DIAMOND = 4
    BLACK_DIAMOND = 1


print(VIP.RED_DIAMOND != VIP.YELLOW_DIAMOND)  # 枚举类型之间可以做等值比较
#  print(VIP.BLUE_DIAMOND > VIP.BLACK_DIAMOND) 会报错，枚举类型之间不能做大小比较
print(VIP.RED_DIAMOND is VIP.BLACK_DIAMOND)  # 枚举类型之间可以做身份比较
print(VIP.GREEN_DIAMOND == VIP2.GREEN_DIAMOND)  # 虽然枚举的值相等，但VIP,VIP2属于2个不同的枚举，因此枚举类型也不同
print(VIP.BLACK_DIAMOND)  # 这里打印的是VIP.RED_DIAMOND枚举类型，因为黑钻的枚举值和红钻相等，因此黑钻相当于是红钻的一个别名，此时将
# BLACK_DIAMOND写作RED_DIAMOND_ALIAS更为合适
print('~~~~~~~~')
for vip in VIP:  # 这里不会把BLACK_DIAMOND打印出来，这种遍历不会遍历别名
    print(vip)

print('~~~~~~~~')
for vip in VIP.__members__:  # 如果需要遍历别名，可以用__members__实现
    print(vip)

print('~~~~~~~~')
for vip in VIP.__members__.items():  # 可以遍历较为完整的信息，以元组的形式存在
    print(vip)

"""
若从数据库中取到一个值是2（通常存储在数据库中的数据类型不会是字符串，因为读取效率较低），需将它转换为
对应的枚举类型
"""
print('~~~~~~~~~')
type_num = 2
vip_type = VIP(type_num)
print(vip_type)

print('~~~~~~~IntEnum~~~~~~~')


@unique  # unique 装饰器用于限制枚举值不能相等的情况
class VIP3(IntEnum):
    # vip1 = 'str1'  会报错，IntEnum规定了枚举值只能是数字
    vip1 = 1.1
    vip2 = 2
    # vip3 = 2 会报错，因为使用了unique装饰器，枚举值不能相等


vip3_type = VIP3.vip1.value
print(vip3_type)  # 枚举值只会打印1，而不是1.1


"""
枚举在python里是单例模式存在的，没有实例化的意义
"""

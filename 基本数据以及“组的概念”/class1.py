# -*- coding: UTF-8 -*-
"""
各进制的表示与转换
"""


# 用0b表示二进制，0b10表示二进制的10在十进制中是什么
print(0b10)
print(0b11001)

# 用0o表示八进制，0o11表示八进制的11转换为十进制是什么
print(0o11)
print(0o7)

# 用0x表示十六进制,0x12表示十六进制的12转换为十进制是什么
# 十六进制：0,1,2,..........,9,A,B,C,D,E,F

print(0x14)
print(0xF)

# 用bin()将任意进制转换为二进制
print(bin(0o12))  # 将八进制的12转化为二进制
print(bin(192))   # 将十进制的192....

# 用oct将任意进制转换为八进制
print(oct(0b1101))
print(oct(0x22E))


# 用int将任意进制转换为十进制
print(int(0x1E))

# 用hex将任意进制转换为16进制
print(hex(66))
print(hex(0o777))
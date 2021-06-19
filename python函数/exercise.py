"""
练习
宝石合成：
宝石有1~6级，有两种途径获得，①从1级自己合成 ②直接购买
合成规则：消耗金币、钻石、体力
购买一级宝石：消耗金币和钻石
1级合成3级宝石：消耗金币、体力、1级宝石
3级合成4级宝石：消耗金币、体力和1级宝石（一定概率）
4级合成6级宝石：消耗金币、体力和4级宝石
"""

"""
    购买1级宝石
"""
l1_value = 0.75  # 买一级宝石消耗0.75金币
l1_value_diamond = 8  # 同时要消耗8钻石

"""
    1级合成3级
"""
l1_to_l3 = 12  # 1级宝石合成3级宝石要消耗12个1级石头
l1_to_l3_gold = 0.39  # 同时要消耗0.39金币
l1_to_l3_vid = 10  # 同时消耗10点体力

"""
    3级合成4级
"""
l3_to_l4 = 16  # 1颗3级宝石变成1颗4级宝石要消耗16颗1级宝石
l3_to_l4_gold = 0.897  # 3级变4级要消耗0.897金币
l3_to_l4_vid = 10  # 消耗10体力
l3_to_l4_rate = 0.4878  # 3级宝石变4级宝石成功率为0.4878
# 失败的话会扣除1级宝石和金币，不消耗体力

"""
    4级合成6级
"""
l4_to_16 = 12  # 4级宝石合成6级宝石需要消耗12颗4级宝石，概率100%
l4_to_16_gold = 19.75  # 消耗19.75金币
l4_to_16_vid = 10  # 消耗10体力

"""
6级宝石直接购买消耗750金币，问是自己合成划算还是直接买划算
其他数据：
    1钻石可以卖 0.05金币
    1体力可以卖 1金币
"""
diamond_to_gold = 0.05
vit_to_gold = 1


def buy_l1_value():  # 计算购买1级宝石的消耗
    l1_cost = l1_value + l1_value_diamond * diamond_to_gold
    return l1_cost


def l1_to_l3_cost():
    l1_cost = buy_l1_value()
    l3_cost = l1_cost * l1_to_l3 + l1_to_l3_gold + l1_to_l3_vid * vit_to_gold
    return l1_cost, l3_cost


def l3_to_l4_cost():
    l1_cost, l3_cost = l1_to_l3_cost()
    # 成功所消耗的金币
    success_cost = (l3_cost + l1_cost * l3_to_l4 + l3_to_l4_gold + l3_to_l4_vid * vit_to_gold) * l3_to_l4_rate
    fail_cost = (l1_cost * l3_to_l4 + l3_to_l4_gold) * (1 - l3_to_l4_rate)
    l4_cost = (success_cost + fail_cost) / l3_to_l4_rate  # 概率论理论
    return l4_cost


def become_l6_cost():
    l4_cost = l3_to_l4_cost()
    l6_cost = l4_cost * l4_to_16 + l4_to_16_gold + l4_to_16_vid * vit_to_gold
    return l6_cost


def compare(l6_cost):
    print('合成会消耗%d' % l6_cost + '金币', end='')
    if l6_cost < 750:
        print(',合成划算')
    elif l6_cost > 750:
        print(',直接买划算')
    else:
        print(',差不多')


if __name__ == '__main__':
    compare(become_l6_cost())

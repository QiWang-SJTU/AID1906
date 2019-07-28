"""
    类成员
    15:25
"""


class ICBC:
    # 类变量:总行的钱
    total_money = 1000000

    # 类方法
    @classmethod
    def print_total_money(cls):
        print(id(cls), id(ICBC))
        # cls : 存储当前类的地址
        # print("当前总行金额:",ICBC.total_money)
        print("当前总行金额:", cls.total_money)

    def __init__(self, name, money):
        self.name = name
        self.money = money
        # 从总行扣除当前支行的钱
        ICBC.total_money -= money


i01 = ICBC("天坛支行", 100000)
i02 = ICBC("陶然亭支行", 100000)
# 主流:通过类访问类成员
ICBC.print_total_money()
print(ICBC.total_money)
# 非主流:通过对象访问类成员
# print(i02.total_money)
# i02.print_total_money()

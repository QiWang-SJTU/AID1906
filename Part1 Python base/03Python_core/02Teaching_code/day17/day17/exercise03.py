"""
    闭包应用
"""


def give_gife_money(money):
    """
        获取压岁钱
    """

    def child_buy(target, price):
        """
            购买商品
        """
        nonlocal money
        if money > price:
            money -= price
            print("购买%s,花了%d钱" % (target, price))
        else:
            print("钱不够了")

    return child_buy


# 价值:逻辑连续(多次购买商品,不脱离获得的压岁钱)
aciton = give_gife_money(10000)
aciton("无人机", 8000)
aciton("外星人", 20000)

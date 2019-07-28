class People:
    def __init__(self, name="", money=None):
        self.name = name
        self.money = money


class Bank:
    def __init__(self, total_money=None):
        self.total_money = total_money

    def draw_money(self, amount, target):
        self.total_money -= amount
        target.money += amount
        print(target.name, "在取", amount, "钱")


p01 = People("小明", 0)
zs = Bank(10000)
zs.draw_money(1000, p01)

# 练习: 小明在银行取钱.
class Person:
    def __init__(self, name="", money=None):
        self.name = name
        self.money = money

class Bank:
    def __init__(self, money=None):
        self.total_money = money

    def draw_money(self,price,target):
        self.total_money -= price #self是银行,所以银行钱少了.
        target.money += price# target传递的是小明,所以小明钱多了
        print(target.name,"在取",price,"钱")

xm = Person("小明",0)
zs = Bank(100000)
zs.draw_money(1000,xm)
print("小明的钱",xm.money)
print("银行的钱",zs.total_money)
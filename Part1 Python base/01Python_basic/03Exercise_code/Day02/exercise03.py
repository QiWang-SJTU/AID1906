price = float(input("请输入商品单价："))
number = int(input("请输入购买数量："))
money_give = int(input("请输入给的金额："))

money_back = money_give - price * number
print("应找回的金额是：" + str(money_back))

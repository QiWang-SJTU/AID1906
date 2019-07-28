"""
练习2:
    在控制台中录入一个商品单价.  25
    再录入一个购买的数量   2
    最后录入一个金额 60
    计算应找回多少钱. 60 - 2 * 25
    15:35 上课
"""

price = input("请输入一个单价:")
price = float(price)
count = int(input("请输入数量："))
money = float(input("请输入金额："))

result = money - count * price

print("应找回" + str(result) + "钱。")

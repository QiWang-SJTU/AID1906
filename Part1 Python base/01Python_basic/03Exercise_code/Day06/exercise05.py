dict_goods = {}
while True:
    name_goods = input("请输入商品名称： ")
    if not name_goods:
        break
    price_goods = float(input("请输入商品价格： "))
    dict_goods[name_goods] = price_goods

for good, price in dict_goods.items():
    print("%s的价格是%.0f元" % (good, price))

if "游戏机" in dict_goods:
    price_game = dict_goods["游戏机"]
    print("游戏机的价格是%.1f" % price_game)

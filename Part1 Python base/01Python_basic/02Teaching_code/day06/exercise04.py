"""
    练习：在控制台中录入商品信息(名称,价格)
         如果名称为空字符串,停止录入.
         -- 将所有商品的名称与价格打印出来(一个商品一行)
         -- 如果录入了"游戏机",则单独打印其价格.
"""

dict_commodity_info = {}
while True:
    name = input("请输入名称:")
    if name =="":
        break
    price = float(input("请输入价格:"))
    dict_commodity_info[name] = price
for k,v in dict_commodity_info.items():
    print("%s的价格是%f"%(k,v))
if "游戏机" in dict_commodity_info:
    value = dict_commodity_info["游戏机"]
    print("游戏机的价格是：%f"%value)





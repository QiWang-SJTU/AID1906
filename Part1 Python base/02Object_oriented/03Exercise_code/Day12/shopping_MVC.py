class CommodityModel:
    def __init__(self):
        self.dict_commodity = {
            101: {"name": "屠龙刀", "price": 10000},
            102: {"name": "倚天剑", "price": 10000},
            103: {"name": "九阴白骨爪", "price": 8000},
            104: {"name": "九阳神功", "price": 9000},
            105: {"name": "降龙十八掌", "price": 8000},
            106: {"name": "乾坤大挪移", "price": 10000}
        }


class OrderModel:
    def __init__(self):
        self.__order_list = []

    @property
    def order_list(self):
        return self.__order_list


class ShoppingManagerController:
    def __init__(self):
        self.__order = OrderModel()
        self.__commodity = CommodityModel()

    @property
    def order(self):
        return self.__order

    def create_order(self, cid, count):
        # 创建一条订单
        dict_order_single = {"cid": cid, "count": count}
        # 加入到订单列表中
        self.order.order_list.append(dict_order_single)

    def cal_total_price(self):
        total_price = 0
        for item in self.order.order_list:
            commodity = self.__commodity.dict_commodity[item["cid"]]
            total_price += commodity["price"] * item["count"]
        return total_price

    def paying(self, money):
        total_price = self.cal_total_price()
        if money >= total_price:
            self.order.order_list.clear()
            return True, money - total_price
        else:
            return False, None


class ShoppingManagerView:

    def __init__(self):
        self.__commodity = CommodityModel()
        self.__controller = ShoppingManagerController()

    @staticmethod
    def __display_menu():
        print("1)显示商品")
        print("2)购买商品")
        print("3)查看购物车")
        print("4)结算")

    def __select_menu_item(self):
        item = input("请您输入选项:")
        if item == "1":
            self.__show_commodity()
        elif item == "2":
            self.__buying_commodity()
        elif item == "3":
            self.__show_order()
        elif item == "4":
            self.__settlement_commodity()

    def main(self):
        """
            主函数，先显示再选择
        :return:
        """
        while True:
            self.__display_menu()
            self.__select_menu_item()

    def __show_commodity(self):
        for key, value in self.__commodity.dict_commodity.items():
            print("编号：%d，名称：%s，单价：%d。" % (key, value["name"], value["price"]))

    def __buying_commodity(self):
        while True:
            cid = int(input("请输入商品编号："))
            if cid in self.__commodity.dict_commodity:
                break
            else:
                print("该商品不存在")
        count = int(input("请输入购买数量："))
        self.__controller.create_order(cid, count)
        print("添加到购物车")

    def __show_order(self):
        for item in self.__controller.order.order_list:
            commodity = self.__commodity.dict_commodity[item["cid"]]
            print("商品：%s, 单价：%d, 数量:%d." % (commodity["name"], commodity["price"], item["count"]))

    def __settlement_commodity(self):
        while True:
            money = float(input("总价%d元，请输入金额：" % self.__controller.cal_total_price()))
            bool_value, money_left = self.__controller.paying(money)
            if bool_value:
                print("购买成功，找回：%d元。" % money_left)
                break
            else:
                print("金额不足.")


shopping = ShoppingManagerView()
shopping.main()

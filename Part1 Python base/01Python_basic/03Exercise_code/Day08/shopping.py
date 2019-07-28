goods_info = {
    101: {"name": "屠龙刀", "price": 10000},
    102: {"name": "倚天剑", "price": 10000},
    103: {"name": "九阴白骨爪", "price": 8000},
    104: {"name": "九阳神功", "price": 9000},
    105: {"name": "降龙十八掌", "price": 8000},
    106: {"name": "乾坤大挪移", "price": 10000}
}

order = []


def show_goods_info(goods_dict):
    """
        显示所有商品信息的函数

    :param goods_dict: dict, 存储所有商品的字典
    :return:
    """
    for key, value in goods_dict.items():
        print("编号：%d，名称：%s，单价：%d。" % (key, value["name"], value["price"]))


def show_order_goods(goods_dict, order_id):
    print("商品：%s，单价：%d,数量:%d." % (goods_dict["name"], goods_dict["price"], order_id["count"]))


def input_wanted_goods(goods_dict):
    """
        输入想购买的商品的函数

    :param goods_dict: dict, 存储所有商品的字典
    :return: str, 所选择的商品的id
    """
    while True:
        good_id = int(input("请输入商品编号："))
        if good_id in goods_dict:
            break
        else:
            print("该商品不存在")
    return good_id


def cal_total_price(order_dict, goods_dict):
    """
        计算商品总价的函数

    :param order_dict: dict, 存储想购买商品的字典
    :param goods_dict: dict, 存储所有商品的字典
    :return: float, 商品总价格
    """
    total_price = 0
    for item in order_dict:
        good = goods_dict[item["good_id"]]
        show_order_goods(goods_dict, item)
        total_price += good["price"] * item["count"]
    return total_price


def purchase_goods(goods_dict):
    """
        购买商品的函数

    :param goods_dict: 存储所有商品的字典
    :return:
    """
    show_goods_info(goods_dict)
    good_id = input_wanted_goods(goods_dict)
    count = int(input("请输入购买数量："))
    order.append({"good_id": good_id, "count": count})
    print("添加到购物车。")


def settle_account(order_dict, goods_dict):
    """
        结算的函数

    :param order_dict:
    :param goods_dict:
    :return:
    """
    total_price = cal_total_price(order_dict, goods_dict)
    while True:
        money = float(input("总价%d元，请输入金额：" % total_price))
        if money >= total_price:
            print("购买成功，找回：%d元。" % (money - total_price))
            order.clear()
            break
        else:
            print("金额不足.")


def shopping():
    """
        购物
    :return:
    """
    while True:
        item = input("1键购买，2键结算。")
        if item == "1":
            purchase_goods(goods_info)
        if item == "2":
            settle_account(order, goods_info)


shopping()


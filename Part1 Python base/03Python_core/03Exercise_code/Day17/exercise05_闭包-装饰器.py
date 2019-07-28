"""
    闭包的应用 ---> 装饰器
"""
import time


# 练习一
def verify_permissions(func):              # 1. 首先把verify_permissions的代码放到方法区
    def wrapper(*args, **kwargs):          # 2. 执行到装饰器时执行外部函数，此时开外部函数的栈帧，将内部函数wrapper的代码放到方法区
        # 定义新功能                             并创建与原函数名相同的变量关联内部函数，外部函数栈帧不销毁
        print("验证权限")                   # 3. 调用原函数时实际上调用了内部函数，在栈帧区继续开内部函数栈帧，并在内部
        # 调用旧功能                             函数中返回外部函数的执行结果
        return func(*args, **kwargs)

    return wrapper


@verify_permissions
def delete_order():
    print("删除订单")


@verify_permissions  # 将内部函数放到方法区，创建与原函数名相同的变量关联内部函数
def enter_background():
    print("进入后台")


enter_background()  # 调用原函数时执行内部函数
delete_order()

# 练习二
# def verify_account(func):
#     def wrapper(*args, **kwargs):  # 应对调用旧功能时实参不一致
#         print("验证账户")
#         return func(*args, **kwargs)  # 应对旧功能的形参不一致
#
#     return wrapper
#
#
# @verify_account
# def save_money(name, money):
#     print(name, "存了", money)
#
#
# @verify_account
# def draw_money(name="", money=None):
#     print(name, "取了", money)
#
#
# # 调用旧功能，但执行的是内部函数
# save_money("小明", 10000)
# draw_money(name="老王", money=5000)
#
#
# # 练习三
# def cal_running_time(func):
#     def wrapper(*args, **kwargs):
#         start_time = time.time()
#         result = func(*args, **kwargs)
#         end_time = time.time()
#         print("执行时间为", end_time - start_time)
#         return result
#
#     return wrapper
#
#
# @cal_running_time
# def save_money():
#     for i in range(1000000):
#         print(i)
#     # print(money)
#
#
# class DrawMoney:
#     def __init__(self, money=None):
#         self.money = money
#
#     @cal_running_time
#     def draw_money(self):
#         for i in range(self.money):
#             print("取了", i)
#
#
# save_money()
# dr01 = DrawMoney(5000)
# dr01.draw_money()

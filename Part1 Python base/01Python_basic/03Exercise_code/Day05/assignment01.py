# import random
#
# lottery_num = []
# for i in range(6):
#     red_num = random.randint(1, 33)
#     while red_num in lottery_num:
#         red_num = random.randint(1, 33)
#     lottery_num.append(red_num)
#
# blue_num = random.randint(1, 16)
# lottery_num.append(blue_num)
#
# answer_num = []
# while answer_num != lottery_num:
#     answer_num = []
#     for i in range(6):
#         red_number = int(input("请输入第" + str(i + 1) + "个红球号码: "))
#         while red_number < 1 or red_number > 33:
#             print("号码不在范围内, 请重新输入： ")
#             red_number = int(input("请输入红球号码： "))
#         while red_number in answer_num:
#             print("号码已经存在, 请重新输入： ")
#             red_number = int(input("请输入红球号码： "))
#         answer_num.append(red_number)
#
#     blue_number = int(input("请输入蓝球号码： "))
#     while blue_number < 1 or blue_number > 16:
#         print("号码不在范围内, 请重新输入： ")
#         blue_number = int(input("请输入蓝球号码： "))
#
#     answer_num.append(blue_number)
# print("恭喜你, 猜对了！")


import random

list_ticket = []
while len(list_ticket) < 6:
    red_num = random.randint(1, 33)
    if red_num not in list_ticket:
        list_ticket.append(red_num)
blue_num = random.randint(1, 16)
list_ticket.append(blue_num)

list_answer = []
while len(list_answer) < 6:
    red_number = int(input("请输入第%d个红球号码: " % (len(list_answer) + 1)))
    if red_number < 1 or red_number > 33:
        print("号码不在范围内, 请重新输入： ")
    elif red_number in list_answer:
        print("号码已经存在, 请重新输入： ")
    else:
        list_answer.append(red_number)

while len(list_answer) < 7:
    blue_number = int(input("请输入蓝球号码："))
    if blue_number < 1 or blue_number > 16:
        print("号码不在范围内, 请重新输入： ")
    else:
        list_answer.append(blue_number)







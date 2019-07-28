"""
    (2)在控制台中购买一注彩票
        请输入第1个红球号码:"
        "号码不在范围内"
        "号码已经存在"
        注意：号码必须满足彩票条件.
"""
list_ticket = []
while len(list_ticket) < 6:
    number = int(input("请输入第%d个红球号码："%(len(list_ticket)+1)))
    if number < 1 or number > 33:
        print("号码不在范围内")
    elif number in  list_ticket:
        print("号码已经存在")
    else:
        list_ticket.append(number)


while len(list_ticket) < 7:
    number = int(input("请输入第7个蓝球号码："))
    if number < 1 or number > 16:
        print("号码不在范围内")
    else:
        list_ticket.append(number)

print(list_ticket)
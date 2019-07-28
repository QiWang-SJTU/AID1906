"""
3. 彩票：双色球
    红球：1--33之间的整数，6个，还不能重复.
    蓝球：1--16之间的整数，1个.
    (1)随机产生一注彩票
重点：如何产生多个不重复的随机数.
"""
import random

list_ticket = []
# 六个红球号码
while len(list_ticket) < 6:
    number = random.randint(1, 33)
    if number not in list_ticket:
        list_ticket.append(number)
# 一个蓝球号码
list_ticket.append(random.randint(1, 16))

print(list_ticket)

# 练习2:定义函数,根据生日(年月日)计算活了多少天.
# 当前时间 - 出生时间  --> 差
# 10:50
import time


def life_days(year,month,day):
    # time.time()
    time_tuple = time.strptime("%d/%d/%d"%(year,month,day), "%Y/%m/%d")
    life_second = time.time() - time.mktime(time_tuple)
    return life_second /60 /60 // 24

print("%d"%life_days(1984,6,11))
year = int(input("请输入年： "))
month = int(input("请输入月： "))
day = int(input("请输入日： "))

day_of_month = 29 if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0) else 28
days_of_month = (31, day_of_month, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)


# 方法1
# day_num = 0
# for i in range(month - 1):
#     day_num += days_of_month[i]
# day_num += day

# 方法2
day_num = sum(days_of_month[:month - 1], day)
print(day_num)

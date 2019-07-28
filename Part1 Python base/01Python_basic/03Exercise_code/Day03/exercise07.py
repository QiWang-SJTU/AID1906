state = "偶数" if int(input("请输入整数： ")) % 2 == 0 else "奇数"
print(state)


year = int(input("请输入年份： "))
day = 29 if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0) else 28
# day = 29 if not year % 4 and year % 100 or not year % 400 else 28
print(day)



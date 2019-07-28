# tuple01 = ("a",)
# print(tuple01)
#
# name1, name2 = (100, 200)
# print(name1, name2)
#
# # 正向
# tuple02 = (1, 2, 3, 4, 5)
# for i in tuple02:
#     print(i)
#
# # 倒序
# for i in range(len(tuple02) - 1, -1, -1):
#     print(tuple02[i])


# 用元组代替列表
# year = int(input("请输入年份： "))
# month = int(input("请输入月份： "))
#
# if month in (1, 3, 5, 7, 8, 10, 12):
#     print(31)
# elif month in (4, 6, 9, 11):
#     print(30)
# elif month == 2:
#     if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#         print(29)
#     else:
#         print(28)
# else:
#     print("月份输入错误.")

# 更简洁
year = int(input("请输入年份： "))
month = int(input("请输入月份： "))

if month < 1 or month > 12:
    print("月份输入有误")
else:
    day_of_month = 29 if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0) else 28
    days_of_month = (31, day_of_month, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
    print(days_of_month[month - 1])

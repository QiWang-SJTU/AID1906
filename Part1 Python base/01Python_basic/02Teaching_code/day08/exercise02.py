# 练习：定义根据月份计算天的函数

# def calculate_day_by_month(month, year):
#     if month < 1 or month > 12:
#         return "月份输入有误"
#     elif month == 2:
#         if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
#             return "29天"
#         else:
#             return "28天"
#     elif month == 4 or month == 6 or month == 9 or month == 11:
#         return "30天"
#     else:
#         return "31天"

# def calculate_day_by_month(month, year):
#     if month < 1 or month > 12:
#         # return "月份输入有误"# 函数的返回值类型应该是一种
#         return 0
#     elif month == 2:
#         if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
#             return 29
#         else:
#             return 28
#     elif month == 4 or month == 6 or month == 9 or month == 11:
#         return 30
#     else:
#         return 31

# def calculate_day_by_month(month, year):
#     if month < 1 or month > 12:
#         # return "月份输入有误"# 函数的返回值类型应该是一种
#         return 0
#     if month == 2:
#         # if is_leap_year(year):
#         #     return 29
#         # else:
#         #     return 28
#         return 29 if is_leap_year(year) else 28
#     if month in (4,6,9,11):
#         return 30
#     return 31

def is_leap_year(year):
    # if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    #     return True
    # else:
    #     return False
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0


def calculate_day_by_month(month, year):
    if month < 1 or month > 12:
        return 0
    if month == 2:
        return 29 if is_leap_year(year) else 28
    if month in (4, 6, 9, 11):
        return 30
    return 31


print(calculate_day_by_month(13, 2019))

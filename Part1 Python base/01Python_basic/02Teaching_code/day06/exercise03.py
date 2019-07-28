"""
    练习:
    在控制台中录入日期(年，月,日),计算这是这一年的第几天？
    2019,3月10日.--> 1月天数 + 2月天数 +  10
"""
year = int(input("请输入年份："))
month = int(input("请输入月份："))
day = int(input("请输入日："))
if month < 1 or month > 12:
    print("月份输入有误")
else:
    day_of_month02 = 29 if year % 4 == 0 and year % 100 != 0 or year % 400 == 0 else 28
    days_of_month = (31,day_of_month02,31,30,31,30,31,31,30,31,30,31)
    """ 方式一
    # 先累加前几个月的天数
    total_day = 0
    for i in range(month - 1):
        total_day += days_of_month[i]
    """
    total_day = sum(days_of_month[:month - 1])
    # 再累加当月天数
    total_day += day
    print(total_day)


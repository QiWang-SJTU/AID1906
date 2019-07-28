def is_leap_year(year):
    """
        判断是否是闰年的函数

    :param year: int, 输入的年份
    :return: True, False
    """
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)


def cal_days_by_month(year, month):
    """
        根据年月计算天数的函数

    :param year: int, 输入的年份
    :param month: int, 输入的月份
    :return: int, 当月的天数
    """
    if month < 1 or month > 12:
        return 0
    if month == 2:
        return 29 if is_leap_year(year) else 28
    if month in (4, 6, 9, 11):
        return 30
    # 函数的返回值类型必须是一种，不能同时返回数字和字符串
    # return "月份输入错误"
    return 31


print(cal_days_by_month(2019, 12))

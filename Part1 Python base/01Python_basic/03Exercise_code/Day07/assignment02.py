def cal_total_seconds(minute, hour, day):
    """
        根据分钟、小时、天计算总秒数的函数

    :param minute: 整型--分钟
    :param hour: 整型--小时
    :param day: 整型--天
    :return: 整型--总秒数
    """
    return minute * 60 + hour * 60 * 60 + day * 24 * 60 * 60


print(cal_total_seconds(24, 6, 10))
def add_fourth_int_number(fourth_int_number):
    """
        计算四位整数各位数之和的函数

    :param fourth_int_number: 四位整型数字
    :return:
    """
    result = fourth_int_number % 10
    result += fourth_int_number // 10 % 10
    result += fourth_int_number // 100 % 10
    result += fourth_int_number // 1000
    return result


print("%d的各位数之和为%d" % (1234, add_fourth_int_number(1234)))

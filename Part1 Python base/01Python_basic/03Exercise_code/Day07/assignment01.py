def print_list_2d(list_2d):
    """
        打印二维列表的函数

    :param list_2d: 需要打印的二维列表
    :return:None
    """
    for item in list_2d:
        for num in item:
            print(num, end=" ")
        print()


list_01 = [
    [1, 5, 8, 9, 6],
    [2, 6, 45, 63, 40],
    [47, 36, 54, 20, 12],
]

print_list_2d(list_01)

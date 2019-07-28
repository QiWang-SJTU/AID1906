def print_list_1d(list_1d):
    """
        将一维列表的元素打印到终端的函数

    :param list_1d: 要打印的一维列表
    :return:
    """
    for i in range(len(list_1d)):
        print(list_1d[i], end=" ")
    print()


list_01 = [2, 4, 6, 8, 10]
list_02 = ["a", "bbb", 200]
print_list_1d(list_01)
print_list_1d(list_02)

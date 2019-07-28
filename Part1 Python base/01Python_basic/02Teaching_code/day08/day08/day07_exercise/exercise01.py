"""
3. 定义在终端中打印二维列表的函数

"""


def print_double_list(list_target):
    """
        打印二维列表
    :param list_target: 需要打印的二维列表
    """
    for r in range(len(list_target)):
        for item in list_target[r]:
            print(item, end=" ")
        print()

list01 = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
]

print_double_list(list01)
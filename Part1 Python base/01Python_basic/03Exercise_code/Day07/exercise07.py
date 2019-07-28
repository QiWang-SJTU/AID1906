def print_rect(row, col, char):
    """
        在终端中打印符号矩形的函数

    :param row: 整型的行数
    :param col: 整型的列数
    :param char: 打印的字符
    :return:
    """
    for i in range(row):
        for j in range(col):
            print(char, end=" ")
        print()


print_rect(3, 5, "#")

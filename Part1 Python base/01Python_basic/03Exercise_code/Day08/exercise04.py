def matrix_transpose(list_2d):
    """
        二维矩阵转置

    :param list_2d:待转置的二维矩阵
    :return:该矩阵的转置
    """
    list_2d_transpose = []
    for j in range(len(list_2d[0])):
        list_2d_transpose.append([])
        for i in range(len(list_2d)):
            list_2d_transpose[j].append(list_2d[i][j])
    return list_2d_transpose


def square_matrix_2d_transpose(list_2d):
    """
        求方阵转置的函数

    :param list_2d: 二维方阵
    :return: 二维方阵的转置
    """
    for i in range(1, len(list_2d)):
        for j in range(i):
            list_2d[i][j], list_2d[j][i] = list_2d[j][i], list_2d[i][j]


list01 = [
    [1, 2, 3, 20],
    [5, 6, 7, 12],
    [9, 14, 11, 12],
    [13, 14, 15, 16]
]

print(matrix_transpose(list01))
print(list01)
square_matrix_2d_transpose(list01)
print(list01)

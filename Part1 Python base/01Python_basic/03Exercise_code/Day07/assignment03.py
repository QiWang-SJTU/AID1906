# 方阵转置---自己第一次写
# list01_transpose = list01[:]
# for i in range(len(list01)):
#     for j in range(i, len(list01)):
#         if i == j:
#             continue
#         list01_transpose[i][j], list01_transpose[j][i] = list01[j][i], list01[i][j]
# print(list01_transpose)


# 自己改进
# def square_matrix_2d_transpose(list_2d):
#     """
#         求方阵转置的函数
#
#     :param list_2d: 二维方阵
#     :return: 二维方阵的转置
#     """
#     for i in range(len(list_2d)):
#         for j in range(i + 1, len(list_2d)):
#             list_2d[i][j], list_2d[j][i] = list_2d[j][i], list_2d[i][j]
#     return list_2d


# 老师讲解
def square_matrix_2d_transpose_example(list_2d):
    """
        求方阵转置的函数

    :param list_2d: 二维方阵
    :return: 二维方阵的转置
    """
    for i in range(1, len(list_2d)):
        for j in range(i):
            list_2d[i][j], list_2d[j][i] = list_2d[j][i], list_2d[i][j]
    return list_2d


list01 = [
    [1, 2, 3, 20],
    [5, 6, 7, 12],
    [9, 14, 11, 12],
    [13, 14, 15, 16]
]

print(square_matrix_2d_transpose_example(list01))

# 练习2:定义方阵转置函数
def square_matrix_transpose(list_matrix):
    for c in range(1, len(list_matrix)):  # 1 2 3
        for r in range(c, len(list_matrix)):
            list_matrix[r][c - 1], list_matrix[c - 1][r] = list_matrix[c - 1][r], list_matrix[r][c - 1]

list01 = [
    [1, 2, 3],
    [5, 6, 7],
    [9, 10, 11],
]

square_matrix_transpose(list01)  # 转置1
print(list01)
square_matrix_transpose(list01)  # 转置2
print(list01)

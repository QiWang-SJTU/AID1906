list_2d = [
    [1, 5, 8, 9, 6],
    [2, 6, 45, 63, 40],
    [47, 36, 54, 20, 12],
]

# # 打印第二行元素
# # for num in list_2d[1]:
# #     print(num)
# #
# # # 打印第一列的元素
# # for i in range(len(list_2d)):
# #     print(list_2d[i][0])
# #
# # # 打印全部的元素
# # for i in range(len(list_2d)):
# #     for j in range(len(list_2d[i])):
# #         print(list_2d[i][j], end=" ")
# #     print()
# #
# # for list_1d in list_2d:
# #     for num in list_1d:
# #         print(num, end=" ")
# #     print()

# 矩阵转置1
list_2d_transpose = []
for j in range(len(list_2d[0])):
    list01 = []
    for i in range(len(list_2d)):
        list01.append(list_2d[i][j])
    list_2d_transpose.append(list01)
print(list_2d_transpose)

# 矩阵转置2
list_2d_transpose = []
for j in range(len(list_2d[0])):
    list_2d_transpose.append([])
    for i in range(len(list_2d)):
        list_2d_transpose[j].append(list_2d[i][j])
# print(list_2d_transpose)

for item1 in list_2d_transpose:
    for item2 in item1:
        print(item2, end=" ")
    print()

# 矩阵转置3
# 创建一个二维空列表
list_transpose = [[None for col in range(len(list_2d))] for row in range(len(list_2d[0]))]
for j in range(len(list_2d[0])):
    for i in range(len(list_2d)):
        list_transpose[j][i] = list_2d[i][j]
print(list_transpose)

# 通过乘法创建二维列表时所有行的引用地址都一样，一旦给某一行赋值，其他行也指向同样的值
# list01 = [[] * 3] * 5
# print(list01)
# list01[0].append(1)
# print(list01)

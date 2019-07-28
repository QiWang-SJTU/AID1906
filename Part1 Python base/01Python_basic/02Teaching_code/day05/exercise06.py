# 要求：画出内存图
# 练习3:删除列表[4,54,5,6,67,17,8]中所有奇数

# 不能完全删除。
# list01 = [4,54,5,6,67,17,8]
# for item in list01:
#     if item % 2:
#         # print(item)
#         list01.remove(item)
#
# print(list01)

# 结论：倒序删除
list01 = [4, 54, 5, 6, 67, 17, 8]
for i in range(len(list01) - 1, -1, -1):
    if list01[i] % 2:
        # print(item)
        # list01.remove(list01[i])
        del list01[i]

print(list01)

# 17:10

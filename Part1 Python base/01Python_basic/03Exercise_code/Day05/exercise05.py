# 练习1
# list01 = [4, 54, 5, 6, 67, 17, 8]
# list02 = []
# for i in list01:
#     if i > 10:
#         list02.append(i)
# print(list02)
#
# 练习2
# list01 = [4, 54, 5, 6, 67, 17, 8]
# max_list = list01[0]
# for i in range(1, len(list01)):
#     if list01[i] > max_list:
#         max_list = list01[i]
# print(max_list)

# a = 1000
# b = 1000
# print(id(a))
# print(id(b))

# 练习3
list01 = [4, 54, 5, 6, 67, 17, 8]
# list02 = list01[:]
# for item in list02:
#     if item % 2:
#         list01.remove(item)
# print(list01)

# test
# 会跳过17这个元素， 因为从列表中删除元素后会重新判断列表长度。但索引号总是依次递增的。
# list01 = [4, 54, 5, 6, 67, 17, 8]
# for item in list01:
#     if item % 2:
#         list01.remove(item)
# print(list01)

# 删除要逆向
for i in range(len(list01) - 1, -1, -1):
    if list01[i] % 2:
        del list01[i]
print(list01)

# list1 = list(range(10))

# list1.append('WangQi')
# print(list1)
#
# list1.insert(3, 'WangQi')
# print(list1)

# list1.remove(4)
# print(list1)
#
# del list1[2]
# print(list1)

# list1[0] = 'wang'
# print(list1)

# 通过切片获取元素都会创建一个新列表
# list2 = list1[:3]
# print(list2)

# list2[-2:]
# print(list2[-2:])

# list2 = 3
# print(list2)
# print(list1)

# list1[2:5] = []
# print(list1)

# list1[2:4] = ['a', 'b', 'c']
# print(list1)

# 正序获取元素
# for i in range(len(list1)):
#     print(list1[i])

# 逆序获取元素
# range(9, -1, -1)
# 表示从9开始，到-1为止，一次递减1 取到[9, 8, 7...2, 1, 0]
# for i in range(len(list1) - 1, -1, -1):
#     print(list1[i])

# 练习1
# 太阳系  各行星组成
list_planes = ['水星', '金星', '地球', '火星', '木星', '土星', '天王星', '海王星']
print("距离太阳最近的行星是： " + list_planes[0])
print("距离太阳最远的行星是： " + list_planes[-1])

print("\n打印太阳和地球之间的行星：")
for i in list_planes[:2]:
    print(i)

print("\n打印八大行星：")
for i in range(len(list_planes)):
    print(list_planes[i])

print("\n倒序打印八大行星：")
for i in range(len(list_planes) - 1, -1, -1):
    print(list_planes[i])

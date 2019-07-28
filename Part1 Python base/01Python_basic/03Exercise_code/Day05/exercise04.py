list01 = ['800', '900', '1000']
list02 = list01
print(id(list01[1]))
print(id(list01[2]))
# list03 = list01
# print(list01[1:2])
# print(list01[1])

list01[1:2] = ["a", "b"]
print(id(list01[1]))
print(id(list01[2]))
#
# list01[1] = "a", "b"
# print(list01)

# list01[0] = "八百"
# print(list02[0])

# list03 = "九百"
# print(type(list03))
# print(list03)
# print(list03[0])
# print(list03[1])
# print(id(list03[0]))
# print(id(list03[1]))
#
# print("\n")
# list04 = list01[:]
# print(id(list01))
# print(id(list04))


# list01 = [100, 200]
# list02 = [100, 200]
# print(list01 == list02)
# print(list01 is list02)


# import copy
#
# list01 = [100, [200, 300]]
# # 深拷贝
# list02 = copy.deepcopy(list01)
# list01[1][0] = 500
# print(list02[1][0])
#
# # 浅拷贝
# list03 = list01[:]
# list01[1][0] = 500
# print(list03[1][0])





# name1 = ["a", "b", "c", "d"]
# name2 = name1.copy()
#
# print(name1, name2, sep="\n")
#
# name1[2] = "e"
# print(name1, name2, sep="\n")

# 浅拷贝，只能拷贝一级
# 中间加一个列表,修改第一级元素，不会反应到name4上
# name3 = ["a", "b", ["e", "f", "g"], "c", "d"]
# name4 = name3.copy()
# name3[2] = "w"
# print(name3, name4, sep="\n")
#
# # 中间加一个列表，修改第二级元素，会反应到name4上
# name3 = ["a", "b", ["e", "f", "g"], "c", "d"]
# name4 = name3.copy()
# name3[2][1] = "w"
# print(name3, name4, sep="\n")
#
# # 中间加一个元组，元组不可修改，不会反应到name4上
# name3 = ["a", "b", ("e", "f", "g"), "c", "d"]
# name4 = name3.copy()
# name3[2] = "w"
# print(name3, name4, sep="\n")


# 深拷贝, 拷贝所有级 但不可迭代对象实际上存放的地址不变，相当于浅拷贝
import copy

name3 = ["a", "b", ["e", "f", "g"], "c", "d"]
name4 = copy.deepcopy(name3)
name3[2][1] = "w"
print(name3, name4, sep="\n")
print(id(name3[0]))
print(id(name4[0]))

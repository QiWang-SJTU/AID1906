list01 = ["a", "b", "c"]
list01[0] = ["A", "B"]
list01[1:2] = ["悟空"]
print(list01)

list02 = list01[::-1]
list01[0] = "老大"
print(list02[0])
print(list01)
print(list02)

print(id(list01[0]))
print(id(list02[2]))

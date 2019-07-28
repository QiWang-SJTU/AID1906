name = "lzmly"
print(id(name))

t01 = ("qtx", name)
print(id(t01))
print(id(t01[1]))

name = "mm"
print(id(name))

print(t01)


list_names = ["lzmly", "mm"]
t01 = ("qtx", list_names)
list_names.append("zx")
print(t01)

# 一个变量，2个列表
list01 = [100, 200]
print(id(list01))
list01 = [100, 200]
print(id(list01))
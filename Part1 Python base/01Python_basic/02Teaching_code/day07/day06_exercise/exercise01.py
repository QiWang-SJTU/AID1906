name = "lzmly"
t01 = ("qtx",name)
name = "mm"
print(t01)#?('qtx', 'lzmly')

list_names = ["lzmly","mm"]
print(id(list_names))

t01 = ("qtx",list_names)

list_names.append("zx")
print(t01)# ('qtx', ['lzmly', 'mm', 'zx'])
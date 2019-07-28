list_name = ["无忌", "翠山", "张三丰"]
dict_name = {}
for i in list_name:
    dict_name[i] = len(i)
print(dict_name)

list_room = [101, 102, 103]
dict_room = {}
for i in range(len(list_name)):
    dict_room[list_name[i]] = list_room[i]
print(dict_room)

# 练习2:姓名列表:  ["无忌","周芷若","赵敏"]
#      房间号列表：[101,102,103]
#      将两个列表合并为一个字典,名字作为key,房间号作为value

list_names = ["无忌", "周芷若", "赵敏"]
list_room_number = [101, 102, 103]

# dict_name_room = {}
# for i in range(len(list_names)):
#     dict_name_room[list_names[i]] = list_room_number[i]

dict_name_room = {list_names[i]: list_room_number[i] for i in range(len(list_names))}
print(dict_name_room)

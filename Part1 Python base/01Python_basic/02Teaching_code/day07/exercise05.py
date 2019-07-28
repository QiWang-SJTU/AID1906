# 练习1：打印所有城市（一行一个）
# 练习2：打印所有城市的景区（一行一个）
dict_info = {
    "北京":
        {
            "景区": ["故宫", "天安门", "长城"],

            "美食": ["烤鸭", "豆汁", "焦圈", "炒肝"],
        },
    "四川":
        {
            "景区": ["九寨沟", "峨眉山", "春熙路"],
            "美食": ["火锅", "兔头"],
        }
}
# 1.
for key in dict_info:
    print(key)

# 2.
# for item in dict_info["北京"]["景区"]:
#     print(item)
#
# for item in dict_info["四川"]["景区"]:
#     print(item)
for key in dict_info:
    for item in dict_info[key]["景区"]:
        print(item)







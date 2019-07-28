dict_cities = {
    "北京": {
        "景区": ["故宫", "天安门", "长城"],
        "美食": ["烤鸭", "豆汁", "焦圈", "炒肝"]
    },
    "四川": {
        "景区": ["九寨沟", "峨眉山", "春熙路"],
        "美食": ["火锅", "兔头"]},
}

# 打印所有城市：
for city in dict_cities:
    print(city)

# 打印所有城市的景区：
for city in dict_cities:
    for site in dict_cities[city]["景区"]:
        print(site, end=" ")
    print()

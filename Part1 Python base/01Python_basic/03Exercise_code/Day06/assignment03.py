dict_interests = {"qtx": ["学习", "看书", "跑步", "钢琴"],
                  "lzmly": ["追剧", "刷抖音", "自拍"], }
for interest in dict_interests["qtx"]:
    print(interest)

dict_cities = {
       "北京": {
              "景区": ["故宫", "天安门", "长城"],
              "美食": ["烤鸭", "豆汁", "焦圈", "炒肝"]
              },
       "四川": {
              "景区": ["九寨沟", "峨眉山", "春熙路"],
              "美食": ["火锅", "兔头"]}, 
              }
for foods in dict_cities["四川"]["美食"]:
    print(foods)

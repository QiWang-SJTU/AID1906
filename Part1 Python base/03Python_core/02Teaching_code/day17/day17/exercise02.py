"""
    1. ([1,1],[2,2,2,2],[3,3])
        获取元组中,长度最大的列表.
    2. 在老婆列表中,获取所有名称与体重.
    3. 在老婆列表中,获取所有身高大于1.5的老婆.
    4. 根据体重对老婆列表进行降序排列
    要求:以上所有功能,使用内置高阶函数实现.
"""


class Wife:
    def __init__(self, name, age, weight, height):
        self.name = name
        self.age = age
        self.weight = weight
        self.height = height


list01 = [
    Wife("翠花", 36, 60, 1.5),
    Wife("如花", 39, 75, 1.3),
    Wife("赵敏", 25, 46, 1.7),
    Wife("灭绝", 42, 50, 1.8)
]
tuple01 = ([1, 1], [2, 2, 2, 2], [3, 3])

re = max(tuple01, key=lambda item: len(item))
print(re)

for item in map(lambda item: (item.name, item.weight), list01):
    print(item)

for item in filter(lambda item: item.height > 1.5, list01):
    print(item.name)

for item in sorted(list01,key = lambda item:item.weight,reverse=True):
    print(item.weight)

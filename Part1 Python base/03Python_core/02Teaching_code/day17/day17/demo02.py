"""
    内置高阶函数
    17:05
"""
from common.list_helper import ListHelper


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

# for item in ListHelper.find_all(list01,lambda item:item.age < 40):
#     print(item.name)

# 1. 过滤:根据条件筛选可迭代对象中的元素，返回值为新可迭代对象。
for item in filter(lambda item:item.age < 40,list01):
    print(item.name)

# for item in ListHelper.select(list01,lambda item:(item.name,item.age)):
#     print(item)

# 2. 映射:使用可迭代对象中的每个元素调用函数，将返回值作为新可迭代对象元素；
for item in map(lambda item:(item.name,item.age),list01):
    print(item)

# 3. 排序(返回排序结果,支持升序与降序)
# ListHelper.order_by(list01,lambda item:item.height)
# for item in list01:
#     print(item.height)

# 升序排列
for item in sorted(list01,key = lambda item:item.height):
    print(item.height)

# 降序排列
for item in sorted(list01,key = lambda item:item.height,reverse=True):
    print(item.height)

# 4. 获取最大值
re = max(list01, key=lambda item: item.weight)
print(re.name)

# 5. 获取最小值
re = min(list01, key=lambda item: item.weight)
print(re.name)


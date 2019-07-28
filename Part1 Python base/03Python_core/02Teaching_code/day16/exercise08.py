from common.list_helper import ListHelper

class Skill:
    def __init__(self, id=0,name="", atk=0, duration=0.1):
        self.id = id
        self.name = name
        self.atk = atk
        self.duration = duration

list01 = [
    Skill(101,"葵花宝典",850,10),
    Skill(102,"辟邪剑法",800,5),
    Skill(103,"狮吼功",500,8),
    Skill(104,"降龙十八掌",700,3),
    Skill(105,"电炮飞脚",8,2),
]

# 练习:以函数式编程思想,重构下列代码.
"""
def find01():
    for item in list01:
        if item.atk > 10:
            yield item
def find02():
    for item in list01:
        if 2 <= item.duration <= 10:
            yield item
def find03():
    for item in list01:
        if len(item.name) > 3:
            yield item
"""
# "封装":提取变化
def condition01(item):
    return item.atk > 10

def condition02(item):
    return  2 <= item.duration <= 10

def condition03(item):
    return len(item.name) > 3

# 根据任何条件,在任何可迭代对象中,查找多个元素.
def find(func):
    for item in list01:
        # if len(item.name) > 3:
        # if condition03(item):
        if func(item):
            yield item

for item in find(condition02):
    print(item.name)

for item in ListHelper.find_all(list01, condition02):
    print(item.name)


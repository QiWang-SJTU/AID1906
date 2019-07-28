"""
    待重构代码:
    "封装"
    "继承"
    "多态"
    list_helper.py
    练习1:
        需求:
            定义函数,在列能列表中,查找编号是101的技能
            定义函数,在列能列表中,查找名称是狮吼功的技能
            定义函数,在列能列表中,查找持续时间大于5的单个技能
        目标:在ListHelper中定义根据条件查找在可迭代对象中查找
            单个对象的方法
"""
from common.list_helper import ListHelper


class Skill:
    def __init__(self, id=0, name="", atk=0, duration=0.1):
        self.id = id
        self.name = name
        self.atk = atk
        self.duration = duration


list01 = [
    Skill(101, "葵花宝典", 850, 10),
    Skill(102, "辟邪剑法", 800, 5),
    Skill(103, "狮吼功", 500, 20),
    Skill(104, "降龙十八掌", 700, 3),
    Skill(105, "电炮飞脚", 8, 2),
]
"""
# 待重构代码:
def find01():
    for item in list01:
        if item.id == 101:
            return item

def find02():
    for item in list01:
        if item.name == "狮吼功":
            return item

def find03():
    for item in list01:
        if item.duration > 5:
            return item
# "封装"
def condition01(item):
    return item.id == 101

def condition02(item):
    return item.name == "狮吼功"

def condition03(item):
    return item.duration > 5

# "继承"
def find(func):
    for item in list01:
        # if item.duration > 5:
        # if condition03(item):
        if func(item):
            return item

# "多态"
re = find(condition03)
print(re.name)
"""


# 10:40
def condition01(item):
    return item.id == 101


# list_helper.py
re = ListHelper.find_single(list01, condition01)
print(re.name)

"""
    练习2:
    需求:
    定义函数, 在技能列表中, 计算技能名称大于3个字的技能数量
    定义函数, 在技能列表中, 计算攻击力大于500的技能数量
    定义函数, 在技能列表中, 查找持续时间在5--10之间的技能数量
    目标: 在ListHelper中定义计算满足指定条件的元素数量
    要求:使用lambda调用ListHelper
"""

"""
def get_count01():
    count = 0
    for item in list01:
        if len(item.name) > 3:
            count += 1
    return count


def get_count02():
    count = 0
    for item in list01:
        if item.atk > 500:
            count += 1
    return count


def get_count03():
    count = 0
    for item in list01:
        if 5 <= item.duration <= 10:
            count += 1
    return count


def condition01(item):
    return len(item.name) > 3


def condition02(item):
    return item.atk > 500


def condition03(item):
    return 5 <= item.duration <= 10


def get_count(func):
    count = 0
    for item in list01:
        # if 5 <= item.duration <= 10:
        # if condition03(item):
        if func(item):
            count += 1
    return count
    
print(get_count(condition03))
"""

print(ListHelper.get_count(list01,lambda item:len(item.name) > 3))
print(ListHelper.get_count(list01,lambda item:item.atk > 500))
print(ListHelper.get_count(list01,lambda item:5 <= item.duration<=10))

"""
    练习3:
    需求:
    定义函数, 在技能列表中, 判断是否存在编号是105的技能
    定义函数, 在技能列表中, 判断是否存在"九阳神功"技能
    定义函数, 在技能列表中, 判断是否攻击力大于10的技能
    目标: 在ListHelper中定义判断是否具有满足条件的元素
    要求:使用lambda调用ListHelper
"""
"""
def is_exists01():
    for item in list01:
        if item.id == 105:
            return True
    return False

def is_exists02():
    for item in list01:
        if item.name == "九阳神功":
            return True
    return False

def is_exists03():
    for item in list01:
        if item.atk > 10:
            return True
    return False
"""
print(ListHelper.is_exists(list01,lambda element:element.id == 105))
print(ListHelper.is_exists(list01,lambda element:element.name == "九阳神功"))
print(ListHelper.is_exists(list01,lambda element:element.atk> 10))

"""
    练习4:
    需求:
    定义函数, 在技能列表中, 计算所有攻击力的和
    定义函数, 在技能列表中, 计算所有持续时间的和 
    目标: 在ListHelper中定义根据条件求和的方法
"""

"""
def sum01():
    sum_value = 0
    for item in list01:
        sum_value += item.atk
    return sum_value

def sum02():
    sum_value = 0
    for item in list01:
        sum_value += item.duration
    return sum_value

def condition01(item):
    return item.atk

def condition02(item):
    return item.duration

def sum(func):
    sum_value = 0
    for item in list01:
        # sum_value += item.duration
        # sum_value += condition02(item)
        sum_value += func(item)
    return sum_value

print(sum(condition01))
"""
print(ListHelper.sum(list01,lambda e:e.atk))
print(ListHelper.sum(list01,lambda e:e.duration))


"""
    练习5:
    需求:
    定义函数, 在技能列表中, 获取所有技能的名称与攻击力.
    定义函数, 在技能列表中, 获取所有技能的编号与名称与持续时间.
    目标: 在ListHelper中定义根据条件筛选信息的函数
"""

"""
def select01():
    for item in list01:
        yield (item.name,item.atk)

def select02():
    for item in list01:
        yield (item.id,item.name,item.duration)

def condition01(item):
    return (item.name, item.atk)

def condition02(item):
    return (item.id,item.name,item.duration)

def select(func):
    for item in list01:
        # yield (item.id,item.name,item.duration)
        # yield condition02(item)
        yield func(item)
"""
for item in ListHelper.select(list01,lambda info:(info.id,info.atk)):
    print(item)

for item in ListHelper.select(list01,lambda info:(info.id,info.name,info.duration)):
    print(item)

"""
    练习6:
    需求:
    定义函数, 在技能列表中, 获取攻击力最大的技能.
    定义函数, 在技能列表中, 获取持续时间最大的技能.
    目标: 在ListHelper中定义根据指定条件获取最大元素的功能
"""
max = ListHelper.get_max(list01,lambda item:item.atk)
print(max.name)


max = ListHelper.get_max(list01,lambda item:item.duration)
print(max.name)


"""
    练习7:
    需求:
    定义函数, 在技能列表中, 根据攻击力升序排列.
    定义函数, 在技能列表中, 根据持续时间升序排列.
    目标: 在ListHelper中定义根据指定条件升序排列的功能
"""
ListHelper.order_by(list01,lambda item:item.atk)
for item in list01:
    print(item.atk)









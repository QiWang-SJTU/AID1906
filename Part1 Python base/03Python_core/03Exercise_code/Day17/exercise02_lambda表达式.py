from common.list_helper import ListHelper


class Skill:
    def __init__(self, skill_id, name, atk, duration):
        self.id = skill_id
        self.name = name
        self.atk = atk
        self.duration = duration


skill_list = [Skill(101, "降龙十八掌", 12, 4),
              Skill(102, "狮吼功", 12, 10),
              Skill(103, "乾坤大挪移", 510, 5),
              Skill(104, "九阳神功", 8, 6)]


# 封装
def condition01(item):
    return item.atk > 500


def condition02(item):
    return len(item.name) > 3


def condition03(item):
    return 5 < item.duration < 10


# 多态
# 练习一  根据指定条件求和
print(ListHelper.get_num(skill_list, lambda item: item.atk > 500))
print(ListHelper.get_num(skill_list, lambda item: len(item.name) > 3))
print(ListHelper.get_num(skill_list, lambda item: 5 < item.duration < 10))


def condition04(item):
    return item.id == 103


def condition05(item):
    return item.name == "乾坤大挪移"


def condition06(item):
    return item.atk > 10


def condition07(item):
    return item.atk


def condition08(item):
    return item.duration


def condition09(item):
    return item.name, item.atk


def condition10(item):
    return item.id, item.name, item.duration


def condition11(item):
    return item.atk


def condition12(item):
    return item.duration


def get_max():
    max_item = skill_list[0]
    for i in range(1, len(skill_list)):
        if max_item < skill_list[i]:
            max_item = skill_list[i]
    return max_item


# 练习二  判断信息是否存在
print(ListHelper.is_exist(skill_list, lambda item: item.id == 103))
print(ListHelper.is_exist(skill_list, lambda item: item.name == "乾坤大挪移"))
print(ListHelper.is_exist(skill_list, lambda item: item.atk > 10))

# 练习三  根据指定条件求和
print(ListHelper.sum_item(skill_list, lambda element: element.atk))
print(ListHelper.sum_item(skill_list, lambda element: element.duration))

# 练习四  获取指定信息
print(tuple(ListHelper.select_info(skill_list, lambda info: (info.name, info.atk))))
print(tuple(ListHelper.select_info(skill_list, lambda info: (info.id, info.name, info.duration))))

# 练习五  获取最大元素
re51 = ListHelper.get_max(skill_list, lambda item: item.atk)
re52 = ListHelper.get_max(skill_list, lambda item: item.duration)
print(re51.name)
print(re52.name)

# 练习六  升序排列
ListHelper.order_by(skill_list, lambda item: item.atk)

for item in skill_list:
    print(item.atk)

ListHelper.order_by(skill_list, lambda item: item.duration)

for item in skill_list:
    print(item.duration)


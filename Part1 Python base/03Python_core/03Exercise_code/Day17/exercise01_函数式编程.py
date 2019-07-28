from common.list_helper import ListHelper


class Skill:
    def __init__(self, skill_id, name, atk, duration):
        self.id = skill_id
        self.name = name
        self.atk = atk
        self.duration = duration


skill_list = [Skill(101, "降龙十八掌", 12, 4),
              Skill(102, "狮吼功", 12, 10),
              Skill(103, "乾坤大挪移", 10, 5),
              Skill(104, "九阳神功", 8, 6)]


# 返回一个结果用return，返回多个对象用yield
def find_id():
    for item in skill_list:
        if item.id == 101:
            return item


def find_name():
    for item in skill_list:
        if item.name == "乾坤大挪移":
            return item


def find_duration():
    for item in skill_list:
        if item.duration > 5:
            return item


# 封装


def condition01(item):
    return item.id == 101


def condition02(item):
    return item.name == "乾坤大挪移"


def condition03(item):
    return item.duration > 5


# 继承
def find(func):
    for item in skill_list:
        if func(item):
            return item


# 多态
re = ListHelper.find_single(skill_list, condition03)
print(re.name)

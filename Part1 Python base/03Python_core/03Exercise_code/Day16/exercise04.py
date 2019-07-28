from common.list_helper import ListHelper


class Skill:
    def __init__(self, skill_id, name, atk, duration):
        self.id = skill_id
        self.name = name
        self.atk = atk
        self.duration = duration


skill_list = [Skill(101, "降龙十八掌", 12, 10),
              Skill(102, "乾坤大挪移", 10, 5),
              Skill(103, "九阳神功", 8, 6)]


def find_skill():
    for item in skill_list:
        if item.atk > 10:
            yield item


def find_duration():
    for item in skill_list:
        if 6 <= item.duration <= 10:
            yield item


def find_name():
    for item in skill_list:
        if len(item.name) > 4:
            yield item


def condition01(item):
    return item.atk > 10


def condition02(item):
    return 6 <= item.duration <= 10


def condition03(item):
    return len(item.name) > 4


def find(func):
    for item in skill_list:
        if func(item):
            yield item


for item in ListHelper.find_all(skill_list, condition01):
    print(item.name)

class Skill:
    def __init__(self, skill_id, name, atk, duration):
        self.id = skill_id
        self.name = name
        self.atk = atk
        self.duration = duration


skill_list = [Skill(101, "降龙十八掌", 12, 10),
              Skill(102, "乾坤大挪移", 10, 5),
              Skill(103, "九阳神功", 8, 6)]


def find_skill(list_target):
    for item in list_target:
        if item.atk > 10:
            yield item


for item in (item for item in skill_list if item.atk > 10):
    print(item.name)


# 返回单个对象使用return语句，返回后可以直接输出不需要for循环
def find_id(list_target):
    for item in list_target:
        if item.id == 103:
            return item


item = find_id(skill_list)
print(item.name)


def find_name(list_target):
    for item in list_target:
        if len(item.name) > 3:
            yield item


re = tuple(find_name(skill_list))


def find01():
    for item in skill_list:
        yield item.id, item.name


re01 = list(find01())
for item in re01:
    print(item)

for item in re01[::-1]:
    print(item)
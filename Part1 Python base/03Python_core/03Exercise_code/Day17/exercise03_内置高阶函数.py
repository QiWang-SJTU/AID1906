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

# filter ---> find_all 函数
for i in (filter(lambda item: item.atk > 10, skill_list)):
    print(i.atk)

# map ---> select 函数
for i in (map(lambda item: item.name, skill_list)):
    print(i)

# sorted 返回值为一个新列表
# 升序
for i in sorted(skill_list, key=lambda item: item.atk):
    print(i.atk)

# 降序
for i in sorted(skill_list, key=lambda item: item.atk, reverse=True):
    print(i.atk)

# max 获取最大值

print(max(skill_list, key=lambda item: item.atk).atk)

# max 获取最小值
print(min(skill_list, key=lambda item: item.atk).atk)

tuple01 = ([1, 1], [2, 2, 2, 2], [3, 3])
# 练习1
print(max(tuple01, key=lambda item: len(item)))

# 练习2
for i in (map(lambda item: (item.name, item.atk), skill_list)):
    print(i)

# 练习3
for i in (filter(lambda item: item.atk > 10, skill_list)):
    print(i.atk)

# 练习4
for i in sorted(skill_list, key=lambda item: item.duration, reverse=True):
    print(i.duration)

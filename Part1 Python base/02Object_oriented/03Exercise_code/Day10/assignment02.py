# 练习:创建技能类(名称,攻击比例(0.1 -- 5),持续时间(0.1 -- 10),消耗法力0 -- 100)


class Skill:
    def __init__(self, name="", atk_ratio=0.1, duration=0.1, cost_sp=0):
        self.name = name
        self.atk_ratio = atk_ratio
        self.duration = duration
        self.cost_sp = cost_sp

    @property
    def atk_ratio(self):
        return self.__atk_ratio

    @atk_ratio.setter
    def atk_ratio(self, value):
        if 0.1 <= value <= 5:
            self.__atk_ratio = value
        else:
            raise ValueError("攻击比例不在范围")

    @property
    def duration(self):
        return self.__duration

    @duration.setter
    def duration(self, value):
        if 0.1 <= value <= 10:
            self.__duration = value
        else:
            raise ValueError("攻击比例不在范围")

    @property
    def cost_sp(self):
        return self.__cost_sp

    @cost_sp.setter
    def cost_sp(self, value):
        if 0 <= value <= 100:
            self.__cost_sp = value
        else:
            raise ValueError("攻击比例不在范围")


list_skill = [
    Skill("降龙十八掌", 5, 9, 80),
    Skill("六脉神剑", 5, 10, 70),
    Skill("蛤蟆功", 4, 8.5, 90),
    Skill("一阳指", 3.5, 7.5, 75),
    Skill("凌波微步", 1, 10, 0),
]


# 1.查找“降龙十八掌”技能对象的函数
def find_01():
    for skill in list_skill:
        if skill.name == "降龙十八掌":
            return skill
    return None


# skill_1 = find_01()
# print(skill_1.name)

# 2.查找所有不需要消耗法力的技能对象的函数
def find_02():
    list_zero_cost = []
    for skill in list_skill:
        if not skill.cost_sp:
            list_zero_cost.append(skill)
    return list_zero_cost


# skill_2 = find_02()
# for item in skill_2:
#     print(item.name)


# 3.删除不需要消耗法力的技能的函数
# def del_01():
#     count = 0
#     for i in range(len(list_skill) - 1, -1, -1):
#         if not list_skill[i].cost_sp:
#             del list_skill[i]
#             count += 1
#     return count


# del_01()
# for item in list_skill:
#     print(item.name)

# 4.查找所有技能的名称与持续时间的函数
def find_03():
    dict_01 = {}
    for i in range(len(list_skill)):
        dict_01[list_skill[i].name] = list_skill[i].duration
    return dict_01


# dict_1 = find_03()
# print(dict_1)


# 5.找出攻击比例最大的技能对象
def find_04():
    for i in range(len(list_skill) - 1):
        if list_skill[i].atk_ratio > list_skill[i + 1].atk_ratio:
            list_skill[i], list_skill[i + 1] = list_skill[i + 1], list_skill[i]

    list_same = []
    for skill in list_skill:
        if skill.atk_ratio == list_skill[-1].atk_ratio:
            list_same.append(skill)
    return list_same


# list_02 = find_04()
# for item in list_02:
#     print(item.name)


# 6.根据时间升序排列的函数
def sort_01():
    for i in range(len(list_skill) - 1):
        for j in range(i + 1, len(list_skill)):
            if list_skill[i].duration > list_skill[j].duration:
                list_skill[i], list_skill[j] = list_skill[j], list_skill[i]


sort_01()
for item in list_skill:
    print(item.name)

"""
3. 创建技能类(名称,攻击比例(0.1 -- 5),持续时间(0.1 -- 10),
             消耗法力0 -- 100)
   -- 定义至少具有4个元素的技能列表
   -- 定义函数,查找"降龙十八掌"技能对象.
   -- 定义函数,查找所有不需要消耗法力的技能对象.
   -- 定义函数,查找技能列表中所有技能的名称与持续时间.
   -- 定义函数,删除技能列表中不需要消耗法力的技能
   -- 定义函数,找出技能列表中攻击比例最大的技能对象
   -- 定义函数,对技能列表根据持续时间做升序排列.
"""


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

    @property  # duration = property(读取方法,None)
    def duration(self):
        return self.__duration

    @duration.setter  # duration.setter(写入方法)
    def duration(self, value):
        self.__duration = value


list01 = [
    Skill("降龙十八掌", 3, 2, 5),
    Skill("黯然销魂掌", 2, 4, 3),
    Skill("六脉神剑", 1.5, 0.2, 0),
    Skill("乾坤大挪移", 5, 3, 2)
]


def find01():
    for item in list01:
        if item.name == "降龙十九掌":
            return item
    # return None


# s01 = find01()
# if s01:
#     print(s01.name)

def find02():
    result = []
    for item in list01:
        if item.cost_sp == 0:
            result.append(item)
    return result


# re = find02()
# for item in re:
#     print(item.name)

def find03():
    result = []
    for item in list01:
        result.append((item.name, item.duration))
    return result


#
# for item in find03():
#     print(item)

def delete01():
    # 统计成功删除的元素数量
    count = 0
    for i in range(len(list01) - 1, -1, -1):
        if list01[i].cost_sp == 0:
            del list01[i]
            count += 1
    return count


# re = delete01()
# print(re)

# -- 定义函数, 找出技能列表中攻击比例最大的技能对象[重要]
def get_max():
    max_value = list01[0]
    for i in range(1, len(list01)):
        if max_value.atk_ratio < list01[i].atk_ratio:
            max_value = list01[i]
    return max_value


# re = get_max()
# print(re.name)

# -- 定义函数, 对技能列表根据持续时间做升序排列.
def sort():
    for r in range(len(list01) - 1):
        for c in range(r + 1, len(list01)):
            if list01[r].duration > list01[c].duration:
                list01[r], list01[c] = list01[c], list01[r]
    # return list01 # 因为sort操作的是列表对象,方法调用后,也可以拿到.
    # day08/demo01.py

sort()
for item in list01:
    print(item.duration)











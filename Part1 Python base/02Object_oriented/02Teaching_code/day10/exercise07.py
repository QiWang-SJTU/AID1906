# 练习:创建技能类(名称,攻击比例(0.1 -- 5),持续时间(0.1 -- 10),
#               消耗法力0 -- 100)


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
    def atk_ratio(self,value):
        if 0.1 <= value <= 5:
            self.__atk_ratio = value
        else:
            raise  ValueError("攻击比例不在范围")

s01 = Skill("降龙十八掌",5,2,50)
print(s01.name)
print(s01.atk_ratio)
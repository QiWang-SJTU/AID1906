# 练习:
# 定义技能类(技能名称,攻击比例,持续时间)
# 创建技能对象,直接print.
# 克隆技能对象,体会改变其中一个,不影响另外一个.
# 15:10

class Skill:
    def __init__(self, name="", atk_ratio=0.1, duration=0.1):
        self.name = name
        self.atk_ratio = atk_ratio
        self.duration = duration

    def __str__(self):
        return "%s---%d---%d" % (self.name, self.atk_ratio, self.duration)
 
    def __repr__(self):
        return "Skill('%s',%d,%d)" % (self.name, self.atk_ratio, self.duration)


s01 = Skill("降龙十八掌", 3, 5)
print(s01)  # s01.__str__()

# s02 = eval("Skill('降龙十八掌',3,5)")
s02 = eval(s01.__repr__())
s01.name = "降龙18掌"
print(s02)

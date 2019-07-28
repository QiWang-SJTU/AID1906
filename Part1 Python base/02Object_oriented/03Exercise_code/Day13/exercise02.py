"""
    内置可重写函数
        自定义对象--->str
"""


class Skill:
    def __init__(self, name="", atk_ratio=10, duration=10):
        self.name = name
        self.atk_ratio = atk_ratio
        self.duration = duration

    # 对人友的--->随心所欲的规定字符串内容
    # 将对象按照自己的风格显示出来
    def __str__(self):
        return "技能是%s, 攻击比例是%d, 持续时间是%d" % (self.name, self.atk_ratio, self.duration)

    # 对解释器友好--->根据python语法规定字符串内容
    # 应用 eval() 将括号里的字符串作为代码执行了
    def __repr__(self):
        # 返回字符串，注意格式
        return "Skill('%s',%d,%d)" % (self.name, self.atk_ratio, self.duration)


s01 = Skill("降龙十八掌", 5, 10)
print(s01)

# print(s01.__repr__())
s02 = eval(repr(s01))
print(id(s01), id(s02))
s01.name = "蛤蟆功"
print(s01, s02)

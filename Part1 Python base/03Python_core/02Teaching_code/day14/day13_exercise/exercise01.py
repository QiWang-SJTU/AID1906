"""
    技能系统
    11:05
"""


class SkillImpactEffect:
    """
        技能影响效果
    """

    def impact(self):
        pass


class DamageEffect(SkillImpactEffect):
    """
        伤害效果

    """

    def __init__(self, value=0):
        self.value = value

    def impact(self):
        print("扣你%d血" % self.value)


class LowerDeffenseEffect(SkillImpactEffect):
    """
        降低防御力效果
    """

    def __init__(self, ratio=0, time=0):
        self.ratio = ratio
        self.time = time

    def impact(self):
        print("降低%.1f防御力%d秒" % (self.ratio, self.time))


class CostSPEffect(SkillImpactEffect):
    """
        消耗法力效果
    """

    def __init__(self, value=0):
        self.value = value

    def impact(self):
        print("消耗%d法力" % self.value)


class SkillDeployer:
    """
        技能释放器
    """

    def __init__(self, name=""):
        self.name = name
        # 读取配置文件
        self.__dict_skill_config = self.__locad_config_file()
        # 创建对象
        self.__list_effect_object = self.__create_effect_object()

    def __locad_config_file(self):
        # 读取代码....(略)
        return {
            "降龙十八掌": ["DamageEffect(500)", "CostSPEffect(50)"],
            "乾坤大挪移": ["DamageEffect(500)", "LowerDeffenseEffect(0.3,10)"],
        }

    def __create_effect_object(self):
        # 在字典中,根据当前技能名称,找出需要的影响效果名称.
        # 降龙十八掌 --> ["DamageEffect(500)", "CostSPEffect(50)"]
        list_effect_name = self.__dict_skill_config[self.name]
        # list_effect_object = []
        # for item in list_effect_name:
        #     # 字符串"DamageEffect(500)" --> 对象 DamageEffect(500)
        #     effect_object = eval(item)
        #     list_effect_object.append(effect_object)
        # return list_effect_object
        return [eval(item) for item in list_effect_name]

    def generate_skill(self):
        """
            生成技能 -- 执行当前技能的影响效果
        """
        # 调用方法
        print(self.name, "技能释放啦")
        for item in self.__list_effect_object:
            item.impact()


# 测试
skill01 = SkillDeployer("降龙十八掌")
skill01.generate_skill()

skill02 = SkillDeployer("乾坤大挪移")
skill02.generate_skill()

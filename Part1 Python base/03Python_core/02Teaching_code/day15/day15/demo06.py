"""
    做迭代器/可迭代对象
    17:13
"""
# 需求:让技能管理器对象可以参与for循环.
class SkillManager:
    """
        技能管理器
        具有__iter__方法,可迭代对象.
    """
    def __init__(self):
        self.__all_skill = []

    def add_skill(self, skill):
        self.__all_skill.append(skill)

    def __iter__(self):
        # 创建技能迭代器对象(传递需要迭代的数据)
        return SkillIterator(self.__all_skill)

class SkillIterator:
    """
        技能迭代器
    """
    def __init__(self, data):
        self.__target = data
        self.__index = -1# 返回数据时,会先自增1

    def __next__(self):
        self.__index += 1
        # 当前需要获取的索引 比最大索引还大
        if self.__index  >  len(self.__target) - 1:
            raise StopIteration
        return self.__target[self.__index]

manager = SkillManager()
manager.add_skill("九阳神功")
manager.add_skill("乾坤大挪移")
manager.add_skill("九阴白骨爪")

# for item in manager:
#     print(item)

iterator = manager.__iter__()
while True:
    try:
        # 2. 获取下一个元素
        item = iterator.__next__()  # Stop Iteration
        print(item)
        # 3. 遇到"停止迭代"异常,则停止循环.
    except StopIteration:
        break

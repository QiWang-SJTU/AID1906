class Skill:
    def __init__(self, id=0,name="", atk=0, duration=0.1):
        self.id = id
        self.name = name
        self.atk = atk
        self.duration = duration

list01 = [
    Skill(101,"葵花宝典",850,10),
    Skill(102,"辟邪剑法",800,5),
    Skill(103,"狮吼功",500,8),
    Skill(104,"降龙十八掌",700,3),
    Skill(105,"电炮飞脚",8,2),
]
# 练习:定义技能类(编号,技能名称,攻击力,持续时间)
#      定义技能列表
#     1)定义生成器函数,查找所有攻击力大于10的技能
#     2)定义函数,查找所编号是103的技能

#15:45
# 返回多个对象使用yield语句
def find01():
    for item in list01:
        if item.atk > 10:
            yield item

# for item in find01():
#     print(item.name)

# 返回单个对象使用return语句
def find02():
    for item in list01:
        if item.id == 101:
            return item

# re = find02()
# print(re.name)

# 练习:定义函数,在技能列表中,查找技能名称大于3字的所有技能.
def find03():
    for item in list01:
        if len(item.name) > 3:
            yield item
# 延迟/惰性操作缺点:获取结果不灵活(只能从头到尾依次获取所有元素)
# for item in find03():
#     print(item.name)
# 解决: 延迟/惰性操作  --> 立即操作
re = tuple(find03())
# 需求:找出满足条件的前两个技能
for item in re[:2]:
    print(item.name)
# 需求:找出满足条件的后两个技能
for item in re[-2:]:
    print(item.name)

# 练习:定义函数,在技能列表中查找所有技能的编号与名称
# 要求:体会惰性查找 -->  立即查找的过程
#  实现从头到位,从尾到头打印结果.
def find04():
    for item in list01:
        yield item.id,item.name

tuple_result = tuple(find04())
for item in tuple_result:
    print(item)

for i in range(len(tuple_result)-1,-1,-1):
    print(tuple_result[i])






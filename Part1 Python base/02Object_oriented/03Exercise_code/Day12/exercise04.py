# 三大特征是主题思想，设计原则是细化的原则
# 封装：定义了手雷、玩家、敌人等类
# 继承：受害者隔离了手雷爆炸的逻辑与玩家或敌人受伤的逻辑
# 多态：手雷爆炸依赖受害者，实际执行玩家与敌人
# 开闭：增加了多个受害者（玩家、敌人），不改变手雷的代码
# 单一：每个类做一件事。手雷（爆炸）、受害者（隔离变化）。体现封装的思想
# 依赖倒置：手雷依赖受害者，而不依赖玩家、敌人
# 组合复用：手雷的爆炸方法通过参数“受害者”访问玩家、敌人的“受伤”方法


class Antitank:
    def boom(self, target):
        print("手雷炸了")
        target.damage()


class Object:
    def damage(self):
        pass


class Player(Object):

    def damage(self):
        print("伤害了玩家")


class Enemy(Object):

    def damage(self):
        print("伤害了敌人")


class House(Object):

    def damage(self):
        print("炸毁了房子")


class Duck(Object):

    def damage(self):
        print("伤害了鸭子")


a01 = Antitank()
p01 = Player()
e01 = Enemy()
d01 = Duck()
a01.boom(p01)
a01.boom(e01)
a01.boom(d01)


class Flat(House):

    def damage(self):
        print("炸毁了公寓")


f01 = Flat()
a01.boom(f01)

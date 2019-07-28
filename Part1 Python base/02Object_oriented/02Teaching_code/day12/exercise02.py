"""
    练习:手雷爆炸了,可能伤害敌人/玩家的生命.
        需求变化:房子/鸭子...
"""

#----------------架构师---------------

class Granade:
    """
        手雷
    """
    def __init__(self,atk):
        self.atk = atk

    def explode(self,sufferer):
        print("爆炸啦")
        # 调用的是父类受伤方法
        # 执行的是子类受伤方法
        sufferer.damage(self.atk)

class Sufferer:
    """
        受害者
    """
    def damage(self,value):
        pass

# ---------------初/中级程序员-----------------
class Player(Sufferer):

    def damage(self, value):
        print("玩家受伤啦")

class Enemy(Sufferer):

    def damage(self, value):
        print("敌人受伤啦")
# ------------------测试-----------------------

g01 = Granade(50)
p01 = Player()
e01 = Enemy()
g01.explode(p01)






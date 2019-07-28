# 练习:玩家(攻击力)攻击敌人(血量),敌人受伤(减血)后可能死亡(播放动画).
# 敌人(攻击力)攻击玩家(血量),玩家受伤(减血,碎屏)后可能死亡(游戏结束).
class Enemy:
    def __init__(self, hp=100, atk=10):
        self.hp = hp
        self.atk = atk

    def damage(self, value):
        print("受伤啦")
        self.hp -= value
        if self.hp == 0:
            self.death()

    def death(self):
        print("播放死亡动画")

    def attack(self, player):
        print("敌人攻击玩家喽")
        player.damage(self.atk)


class Player:
    def __init__(self, atk=10, hp=100):
        self.atk = atk
        self.hp = hp

    def attack(self, enemy):
        print("玩家攻击了敌人")
        enemy.damage(self.atk)

    def damage(self, value):
        print("玩家受伤啦")
        if self.hp == 0:
            self.death()

    def death(self):
        print("游戏结束")


p01 = Player(50)
e01 = Enemy()
p01.attack(e01)
e01.attack(p01)
p01.attack(e01)

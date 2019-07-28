# 练习:创建敌人类(名字,血量0--100,攻击力10--50)
class Enemy:
    def __init__(self, name, hp, attack):
        self.name = name
        self.hp = hp
        self.attack = attack

    def get_hp(self):
        return self.__hp

    def set_hp(self, value):
        # 创建实例变量
        if 0 <= value <= 100:
            self.__hp = value
        else:
            raise ValueError("血量不在范围内")

    hp = property(get_hp,set_hp)

    def get_attack(self):
        return self.__attack

    def set_attack(self, value):
        if 10 <= value <= 50:
            self.__attack = value
        else:
            raise ValueError("攻击力不在范围内")

    attack = property(get_attack, set_attack)

e01 = Enemy("灭霸", 100, 50)
print(e01.hp)
print(e01.attack)

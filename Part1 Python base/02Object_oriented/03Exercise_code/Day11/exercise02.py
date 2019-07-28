# class Player:
#     def __init__(self, attack=25, blood=100, name=""):
#         self.player_name = name
#         self.player_attack = attack
#         self.player_blood = blood
#
#     def attack_enemy(self, target_enemy):
#         target_enemy.enemy_blood -= self.player_blood
#         if target_enemy.enemy_blood <= 0:
#             print(target_enemy.enemy_name, "死亡", "播放动画")
#
#
# class Enemy:
#     def __init__(self, attack=20, blood=100, name=""):
#         self.enemy_name = name
#         self.enemy_attack = attack
#         self.enemy_blood = blood
#
#     def attack_player(self, target_player):
#         target_player.player_blood -= self.enemy_attack
#         if target_player.player_blood <= 0:
#             print("碎屏")
#
#
# player1 = Player(25, 100, "Nick")
# enemy1 = Enemy(20, 100, "Bob")
# player1.attack_enemy(enemy1)
# enemy1.attack_player(player1)




















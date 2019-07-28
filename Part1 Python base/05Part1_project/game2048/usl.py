"""
    用户界面
"""
import os

from game2048.bll import GameController
from game2048.model import MoveDirection


class GameConsoleView:
    """
        负责处理界面逻辑
    """

    def __init__(self):
        self.__controller = GameController()

    def start(self):
        self.__controller.generate_new_number()
        self.__controller.generate_new_number()
        self.__print_map()

    def __print_map(self):
        # 在终端中可以清空界面
        # os.system("clear")

        for line in self.__controller.double:
            for item in line:
                print(item, end="     ")
            print()
            print()

    def update(self):
        while True:
            str_input = input("请输入(wsad): ")
            # 移动地图
            self.__move_map(str_input)
            # 如果地图没有变化则跳过
            if not self.__controller.is_change:
                continue
            # 生成新数字并绘制界面
            self.__controller.generate_new_number()
            self.__print_map()
            # 判断游戏是否结束
            if self.__controller.is_game_over():
                # 如果结束则退出循环
                print("游戏结束!")
                break

    def __move_map(self, str_input):
        if str_input == "w":
            self.__controller.move(MoveDirection.UP)
        elif str_input == "s":
            self.__controller.move(MoveDirection.DOWN)
        elif str_input == "a":
            self.__controller.move(MoveDirection.LEFT)
        elif str_input == "d":
            self.__controller.move(MoveDirection.RIGHT)

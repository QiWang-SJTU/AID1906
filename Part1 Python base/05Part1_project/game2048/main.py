"""
    游戏入口
"""
from game2048.usl import GameConsoleView

if __name__ == "__main__":
    view = GameConsoleView()
    view.start()
    view.update()

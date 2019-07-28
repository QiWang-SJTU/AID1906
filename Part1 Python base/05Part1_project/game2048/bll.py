"""
    负责处理游核心逻辑模块
"""
import copy
import random

from game2048.model import Location, MoveDirection


class GameController:
    def __init__(self):
        self.__list_merge = [2, 16, 0, 4]
        self.__double = [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ]
        self.__list_empty_location = []
        self.__is_change = False

    # 只读属性
    @property
    def double(self):
        return self.__double  # 缺点: 类外仍然可以修改列表内的对象
        # return self.__double[:]  浅拷贝只针对第一层有效
        # return copy.deepcopy(self.__double) 缺点: 占内存

    @property
    def is_change(self):
        return self.__is_change

    # 1. 0元素后移,不需要别人知道
    def __zero_to_end(self):
        """
            将列表里的零元素后移到末尾。思想：从后往前删，是零元素则在末尾添加
            修改全局变量列表里的元素，不改变列表地址，不创建新的变量
        :return:
        """
        for i in range(len(self.__list_merge) - 1, -1, -1):
            if not self.__list_merge[i]:
                del self.__list_merge[i]
                self.__list_merge.append(0)

    # 2. 合并相邻相同元素
    def __merge_same_element(self):
        """
            合并相邻相同的元素。思想：先将0元素后移，然后相邻元素比较，
            相同元素相加赋值给第一个元素，第二个元素赋0，再将0元素后移
        """
        self.__zero_to_end()
        for i in range(len(self.__list_merge) - 1):
            if self.__list_merge[i] == self.__list_merge[i + 1]:
                self.__list_merge[i], self.__list_merge[i + 1] = 2 * self.__list_merge[i], 0
                self.__zero_to_end()

    # 3. 向左移动
    def __move_left(self):
        """
            向左移动。思想：取二维列表每一行，执行向左移动操作
        """
        for item in self.__double:
            self.__list_merge = item
            self.__merge_same_element()

    # 4. 向右移动
    def __move_right(self):
        """
            向右移动。思想：反向赋值列表，合并相同元素，再反向赋值回去
        """
        for item in self.__double:
            self.__list_merge = item[::-1]
            self.__merge_same_element()
            item[::-1] = self.__list_merge

    # 5. 向上移动
    def __move_up(self):
        """
            向上移动。思想：转置，调用向左移动
        """
        self.__square_matrix_transpose()
        self.__move_left()
        self.__square_matrix_transpose()

    # 6. 向下移动
    def __move_down(self):
        """
            向下移动。思想：转置，调用向右移动
        """
        self.__square_matrix_transpose()
        self.__move_right()
        self.__square_matrix_transpose()

    # 移动函数
    def move(self, direction=MoveDirection.UP):
        # 移动前记录
        original_double = copy.deepcopy(self.__double)
        if direction == MoveDirection.UP:
            self.__move_up()
        if direction == MoveDirection.DOWN:
            self.__move_down()
        if direction == MoveDirection.LEFT:
            self.__move_left()
        if direction == MoveDirection.RIGHT:
            self.__move_right()

        # 移动后比较
        self.__is_change = self.__double != original_double

    # 7. 方阵转置
    def __square_matrix_transpose(self):
        """
            求方阵转置的函数
        """
        for i in range(1, len(self.__double)):
            for j in range(i):
                self.__double[i][j], self.__double[j][i] = self.__double[j][i], self.__double[i][j]

    # 8. 随机产生新数组
    def generate_new_number(self):
        self.__cal_empty_location()
        if len(self.__list_empty_location) == 0:
            return
        loc = random.choice(self.__list_empty_location)
        self.__double[loc.r][loc.c] = self.__create_random_number()
        self.__list_empty_location.remove(loc)

    # 9. 依概率产生随机数2和4
    @staticmethod
    def __create_random_number():
        return 4 if random.randint(1, 10) == 1 else 2

    # 10. 计算空位置
    def __cal_empty_location(self, num=0):
        self.__list_empty_location.clear()
        for r in range(len(self.__double)):
            for c in range(len(self.__double)):
                if self.__double[r][c] == num:
                    self.__list_empty_location.append(Location(r, c))

    # 11. 游戏结束判定方法
    def is_game_over(self):
        if self.is_empty() and self.is_same():
            return True
        return False

    # 12. 判断是否存在空位置
    def is_empty(self):
        self.__cal_empty_location()
        if len(self.__list_empty_location):
            return False
        return True

    # 13. 同时判断水平/竖直方向是否存在相邻相同元素
    def is_same(self):
        for r in range(len(self.__double)):
            for c in range(len(self.__double) - 1):
                if self.__double[r][c] == self.__double[r][c + 1] or self.__double[c][r] == self.__double[c + 1][r]:
                    return False
        return True


if __name__ == "__main__":
    """测试代码"""

    controller = GameController()
    print(controller.double)
    controller.generate_new_number()
    print(controller.double)
    # todo controller.double[0][0] = 100会修改原数据 ---> 深拷贝

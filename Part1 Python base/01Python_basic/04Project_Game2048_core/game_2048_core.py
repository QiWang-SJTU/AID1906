"""
    2048游戏核心算法
"""

# 1. 0元素后移
list_merge = [2, 4, 0, 4]


def zero_to_end():
    """
        将列表里的零元素后移到末尾。思想：从后往前删，是零元素则在末尾添加
        修改全局变量列表里的元素，不改变列表地址，不创建新的变量
    :return:
    """
    for i in range(len(list_merge) - 1, -1, -1):
        if not list_merge[i]:
            del list_merge[i]
            list_merge.append(0)


# 2. 合并相邻相同元素
def merge_same_element():
    """
        合并相邻相同的元素。思想：先将0元素后移，然后相邻元素比较，
        相同元素相加赋值给第一个元素，第二个元素赋0，再将0元素后移
    """
    zero_to_end()
    for i in range(len(list_merge) - 1):
        if list_merge[i] == list_merge[i + 1]:
            list_merge[i], list_merge[i + 1] = 2 * list_merge[i], 0
            zero_to_end()


# 3. 向左移动
def move_left():
    """
        向左移动。思想：取二位列表每一行，执行向左移动操作
    """
    global list_merge
    for item in list_double:
        list_merge = item
        merge_same_element()


# 4. 向右移动
def move_right():
    """
        向右移动。思想：反向赋值列表，合并相同元素，再反向赋值回去
    """
    global list_merge
    for item in list_double:
        list_merge = item[::-1]
        merge_same_element()
        item[::-1] = list_merge


# 5. 向上移动
def move_up():
    """
        向上移动。思想：转置，调用向左移动
    """
    square_matrix_transpose()
    move_right()
    square_matrix_transpose()


# 6. 向下移动
def move_down():
    """
        向下移动。思想：转置，调用向右移动
    """
    square_matrix_transpose()
    move_left()
    square_matrix_transpose()


# 方阵转置
def square_matrix_transpose():
    """
        求方阵转置的函数
    """
    for i in range(1, len(list_double)):
        for j in range(i):
            list_double[i][j], list_double[j][i] = list_double[j][i], list_double[i][j]


list_double = [
    [2, 0, 0, 2],
    [2, 2, 0, 4],
    [0, 4, 0, 4],
    [2, 2, 2, 0]
]

move_up()
print(list_double)



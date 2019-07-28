import numpy as np
import time


def sort_list(list_target):
    """
        对列表升序排列的函数

    :param list_target:待排序的列表
    :return:
    """
    for i in range(len(list_target)):
        for j in range(i + 1, len(list_target)):
            if list_target[j] < list_target[i]:
                list_target[i], list_target[j] = list_target[j], list_target[i]


list01 = np.random.randint(100, size=100)
time_start = time.time()
sort_list(list01)
print(list01)
time_end = time.time()
print('time cost', time_end - time_start, 's')

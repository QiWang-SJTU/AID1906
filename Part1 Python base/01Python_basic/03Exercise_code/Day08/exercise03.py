import time


def is_same_element_in_list(list_target):
    """
        判断列表中有无重复元素的函数

    :param list_target: 要判断的列表
    :return: True, False
    """
    for i in range(len(list_target)):
        for j in range(i + 1, len(list_target)):
            if list_target[i] == list_target[j]:
                return True
    return False
 

list01 = list(range(20000))
time_start = time.time()
print(is_same_element_in_list(list01))
time_end = time.time()
print('time cost', time_end - time_start, 's')

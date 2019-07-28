"""
    要求是排好序的顺序表
"""


def binary_search_recursion(list_target, item):
    """
            二分查找的递归函数

            最优时间复杂度 ---> O(1)

            最坏时间复杂度 ---> O(log(n))

    :param list_target: 待查找的有序列表
    :param item: 待查找的元素
    :return: True: 存在  False: 不存在
    """
    if not len(list_target):
        return False
    else:
        mid_index = len(list_target) // 2
        if list_target[mid_index] == item:
            return True
        else:
            if list_target[mid_index] > item:
                return binary_search_recursion(list_target[:mid_index], item)
            else:
                return binary_search_recursion(list_target[mid_index + 1:], item)


def binary_search(list_target, item):
    """
            二分查找的非递归函数

            最优时间复杂度 ---> O(1)

            最坏时间复杂度 ---> O(log(n))

    :param list_target: 待查找的有序列表
    :param item: 待查找的元素
    :return: True: 存在  False: 不存在
    """
    first = 0
    last = len(list_target) - 1
    while first <= last:
        mid_index = (first + last) // 2
        if list_target[mid_index] == item:
            return True
        elif list_target[mid_index] > item:
            last = mid_index - 1
        else:
            first = mid_index + 1
    return False


if __name__ == "__main__":
    list01 = [2, 7, 4, 5, 45, 30, 9, 29, 36]
    print(binary_search_recursion(list01, 45))
    print(binary_search_recursion(list01, 100))
    print(binary_search(list01, 45))
    print(binary_search(list01, 100))

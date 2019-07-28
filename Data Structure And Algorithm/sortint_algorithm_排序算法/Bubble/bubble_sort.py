def bubble_sort(list_target):
    """
        冒泡排序算法（默认升序）

        最坏时间复杂度 ---> O(n^2)

        最优时间复杂度 ---> O(n)

        稳定

    :param list_target: 待排序的列表
    :return: None
    """
    # 外层循环控制要做多少次循环
    for i in range(len(list_target) - 1, 0, -1):
        # 内层循环控制每轮循环做多少次比较
        # 冒泡排序的优化，在已是顺序排列的情况下跳出循环，最优时间复杂度为O(n)
        count = 0
        for j in range(i):
            if list_target[j] > list_target[j + 1]:
                list_target[j], list_target[j + 1] = list_target[j + 1], list_target[j]
                count += 1
        if not count:
            break


if __name__ == "__main__":
    list01 = [2, 3, 4, 5, 6, 18, 9, 29]
    print(list01)
    bubble_sort(list01)
    print(list01)

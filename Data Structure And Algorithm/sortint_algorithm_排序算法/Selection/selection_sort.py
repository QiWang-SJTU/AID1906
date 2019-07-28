def selection_sort(list_target):
    """
        选择排序算法（默认升序）

        最坏时间复杂度 ---> O(n^2)

        最优时间复杂度 ---> O(n^2)

        不稳定

    :param list_target: 待排序的列表
    :return: None
    """
    for j in range(len(list_target) - 1):  # j ---> 0 ~ n-2 每次比较最小值的起始下标
        # 记录最小值的下标
        min_index = j
        for i in range(j + 1, len(list_target)):  # i ---> (1~n-1), (2~n-1), ... , n-1 每次比较无序序列的下标
            if list_target[min_index] > list_target[i]:
                min_index = i
        list_target[j], list_target[min_index] = list_target[min_index], list_target[j]

    """
        不稳定的例子：升序排列，每次记录并交换最大值
        元组中的序号表示相同元素出现的顺序
        list = [(26, 1), 23, 5, 8, (26, 2), 17, 10]
        1. [10, 23, 5, 8, (26, 2), 17, (26, 1)]
        2. [10, 23, 5, 8, 17, (26, 2), (26, 1)]
        26的顺序发生了变化，不稳定
    """


if __name__ == "__main__":
    list01 = [2, 7, 4, 5, 45, 30, 9, 29]
    print(list01)
    selection_sort(list01)
    print(list01)

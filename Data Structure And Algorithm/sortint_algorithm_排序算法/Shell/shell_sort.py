def shell_sort(list_target):
    """
        希尔排序算法（默认升序）

        最坏时间复杂度 ---> O(n^2)

        最优时间复杂度 ---> 因步长序列而异

        不稳定

    :param list_target: 待排序的序列
    :return: None
    """
    # 初始增量
    gap = len(list_target) // 2
    # 最后一轮步长为1，1//2 = 0
    while gap > 0:
        # j = gap, gap + 1, gap + 2, ... , n -1
        # 这一轮循环将所有子序列的插入排序都操作完
        for i in range(gap, len(list_target)):
            # 每次从i的位置开始插入
            j = i
            # 插入排序
            while j >= gap:
                if list_target[j] < list_target[j - gap]:
                    list_target[j], list_target[j - gap] = list_target[j - gap], list_target[j]
                j -= gap
        # 得到新步长
        gap //= 2


if __name__ == "__main__":
    list01 = [2, 7, 4, 5, 45, 30, 9, 29]
    print(list01)
    shell_sort(list01)
    print(list01)

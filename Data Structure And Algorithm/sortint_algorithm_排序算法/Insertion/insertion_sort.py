def insertion_sort(list_target):
    """
        插入排序算法（默认升序）

        最坏时间复杂度 ---> O(n^2)

        最优时间复杂度 ---> O(n)

        稳定

    :param list_target: 待排序的序列
    :return: None
    """
    # 外层循环表示每次从无序序列中拿出元素的下标 ---> j = 1~n-1
    for j in range(1, len(list_target)):
        # 内层循环表示每次最多要与已排好序列比较的次数 ---> i = 1, (2~1), (3~1), ... ,(n-1 ~ 1)
        for i in range(j, 0, -1):
            if list_target[i] < list_target[i - 1]:
                list_target[i], list_target[i - 1] = list_target[i - 1], list_target[i]
            # 优化的方法，如果取出的元素大于等于已排序好的左边的元素，则直接退出循环
            # 序列已处于升序状态时，时间复杂度为O(n)
            else:
                break


if __name__ == "__main__":
    list01 = [2, 7, 4, 5, 45, 30, 9, 29]
    print(list01)
    insertion_sort(list01)
    print(list01)

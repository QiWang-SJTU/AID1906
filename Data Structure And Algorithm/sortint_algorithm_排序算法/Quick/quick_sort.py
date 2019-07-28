def quick_sort(list_target, start, end):
    """
        快速排序算法（默认升序）

        最坏时间复杂度 ---> O(n ^ 2)

        最优时间复杂度 ---> O(n * log(n))

        不稳定
    :param list_target: 待排序列表
    :param start: int 起始下标
    :param end: int 终止下标
    :return: None
    """
    # 递归的退出条件
    if start >= end:
        return

    # 设定起始元素为要寻找位置的基准元素
    mid = list_target[start]

    # low为序列左边的由左向右移动的游标
    low = start

    # high为序列右边的由右向左移动的游标
    high = end

    while low < high:
        # 如果low与high未重合，high指向的元素不比基准元素小，则high向左移动
        while low < high and list_target[high] >= mid:
            high -= 1
        # 将high指向的元素放到low的位置上
        list_target[low] = list_target[high]

        # 如果low与high未重合，low指向的元素比基准元素小，则low向右移动
        while low < high and list_target[low] < mid:
            low += 1
        # 将low指向的元素放到high的位置上
        list_target[high] = list_target[low]

    # 退出循环后，low与high重合，此时所指位置为基准元素的正确位置
    # 将基准元素放到该位置
    list_target[low] = mid

    # 对基准元素左边的子序列进行快速排序
    quick_sort(list_target, start, low - 1)

    # 对基准元素右边的子序列进行快速排序
    quick_sort(list_target, low + 1, end)

    # todo 必须掌握快排


if __name__ == "__main__":
    list01 = [2, 7, 4, 5, 45, 30, 9, 29]
    print(list01)
    quick_sort(list01, 0, len(list01) - 1)
    print(list01)

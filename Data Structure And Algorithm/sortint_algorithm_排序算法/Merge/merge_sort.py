def merge_sort(list_target):
    """
        归并排序算法（默认升序）

        最坏时间复杂度 ---> O(n * log(n))

        最优时间复杂度 ---> O(n * log(n))

        稳定
    :param list_target: 待排序列表
    :return: 已排序列表
    """
    # 递归的退出条件
    if len(list_target) <= 1:
        return list_target

    # 二分分解
    num = len(list_target) // 2

    # 递归分解
    left_list = merge_sort(list_target[:num])
    right_list = merge_sort(list_target[num:])

    # 递归合并
    return merge(left_list, right_list)


def merge(left, right):
    """
        合并函数，将两个有序数组left[]和right[]合并成一个大的有序数组

    :param left: 有序数组
    :param right: 有序数组
    :return: result: 合并后的有序数组
    """
    # left 和 right 的下标指针，从第一个元素开始比较
    l_pointer, r_pointer = 0, 0
    result = []
    while l_pointer < len(left) and r_pointer < len(right):
        if left[l_pointer] < right[r_pointer]:
            result.append(left[l_pointer])
            l_pointer += 1
        else:
            result.append(right[r_pointer])
            r_pointer += 1
    result += left[l_pointer:]
    result += right[r_pointer:]
    return result


if __name__ == "__main__":
    list01 = [2, 7, 4, 5, 45, 30, 9, 29, 36]
    print(list01)
    print(merge_sort(list01))

"""
    归并排序递归执行过程
    
    merge_sort([7, 2, 5, 4, 45, 30, 9, 29, 36])
    
        num = 4
        
        ---------------------------------------------------
        # 第一层：执行第21行(拆分左子序列)
        
        left_list = merge_sort([7, 2, 5, 4])
            num = 2
            
            -----------------------------------------------
            -----------------------------------------------
            # 第二层：执行第21行(拆分左子序列)
            
            left_list = merge_sort([7, 2])
                num = 1
                # 第三层：执行第21行(拆分左子序列)
                
                left_list = merge_sort([7])
                    return [7]
                left_list = [7]
                
                # 第三层：执行第22行(拆分右子序列)
                right_list = merge_sort([2])
                    return [2]
                left_list = [2]
                
                # 第三层：执行第25行(合并操作)
                result = [2, 7]
            left_list = [2, 7]
            
            ------------------------------------------------    
            ------------------------------------------------    
            # 第二层：执行第22行(拆分右子序列)
            
            right_list = merge_sort([5, 4])
                num = 1
                # 第三层：执行第21行(拆分左子序列)
                
                left_list = merge_sort([5])
                    return [5]
                left_list = [5]
                
                # 第三层：执行第22行(拆分右子序列)
                right_list = merge_sort([4])
                    return [4]
                left_list = [4]
                
                # 第三层：执行第25行(合并操作)
                result = [4, 5]
            right_list = [4, 5]
            
            ------------------------------------------------
            ------------------------------------------------
            # 第二层：执行第25行(合并操作)
            result = [2, 4, 5, 7]
        left_list = [2, 4, 5, 7]
    
        ----------------------------------------------------    
        # 第一层：执行第22行(拆分右子序列)
        
            right_list = merge_sort([45, 30, 9, 29, 36])
            num = 2
            
            ------------------------------------------------
            ------------------------------------------------
            # 第二层：执行第21行(拆分左子序列)
            
            left_list = merge_sort([45, 30])
                num = 1
                # 第三层：执行第21行(拆分左子序列)
                
                left_list = merge_sort([45])
                    return [45]
                left_list = [45]
                
                # 第三层：执行第22行(拆分右子序列)
                right_list = merge_sort([30])
                    return [30]
                left_list = [30]
                
                # 第三层：执行第25行(合并操作)
                result = [30, 45]
            left_list = [30, 45]
                       
            ------------------------------------------------
            ------------------------------------------------
            # 第二层：执行第22行(拆分右子序列)
            
            right_list = merge_sort([9, 29, 36])
                num = 1
                # 第三层：执行第21行(拆分左子序列)
                
                left_list = merge_sort([9])
                    return [9]
                left_list = [9]
                
                # 第三层：执行第22行(拆分右子序列)
                right_list = merge_sort([29, 36])
                    num =1
                    # 第四层：执行第21行(拆分左子序列)
                    
                    left_list = merge_sort([29])
                        return [29]
                    left_list = [29]
                    
                    # 第四层：执行第22行(拆分右子序列)
                    
                    right_list = merge_sort([36])
                        return [36]
                    right_list = [36]
                    
                    # 第四层：执行第25行(合并操作)
                    result = [29, 36]
                right_list = [29, 36]
                
                # 第三层：执行第25行(合并操作)
                result = [9, 29, 36]
            right_list = [9, 29, 36]
            
            ------------------------------------------------
            ------------------------------------------------
            # 第二层：执行第25行(合并操作)
            result = [9, 29, 30, 36, 45]
        right_list = [9, 29, 30, 36, 45]
        
        ----------------------------------------------------
        # 第一层：执行第25行(合并操作)
        result = [2, 4, 5, 7, 9, 29, 30, 36, 45]
    return [2, 4, 5, 7, 9, 29, 30, 36, 45]
       
"""

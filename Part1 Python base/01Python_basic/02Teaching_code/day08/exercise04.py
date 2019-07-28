def fun01(p1, p2):
    # 修改栈帧中的变量
    p1 = "悟空"
    # 修改列表的元素
    p2[0] = "八戒"


a = 100
b = [200]
fun01(a, b)
print(a)  # ?100
print(b)  # ['八戒']

#总结：
# 1. 向函数传递可变类型对象(列表)
# 2. 函数内部修改可变对象
# 3. 函数执行过后，不用通过返回值，也能拿到修改后的结果。

# 练习1:定义矩阵转置函数
# day07/exercise07.py
def matrix_transpose(list_matrix):
    result = []
    for c in range(len(list_matrix[0])):
        result.append([])
        for r in range(len(list_matrix)):
            result[c].append(list_matrix[r][c])
    return result


list01 = [
    [1, 2, 3],
    [5, 6, 7],
    [9, 10, 11],
]

re = matrix_transpose(list01)
print(re)



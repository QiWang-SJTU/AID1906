"""编译器用栈实现的递归"""

def factorial(n):
    '''
    @Description: 递归求阶乘
    @param {type} int
    @return: 该数的阶乘
    '''
    if n <= 1:
        return 1
    return factorial(n - 1) * n

print(factorial(3)) 
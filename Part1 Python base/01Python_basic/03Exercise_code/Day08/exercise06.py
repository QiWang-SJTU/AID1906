# 全局变量 global语句

# count = 0
#
#
# def my_print():
#     global count
#     count += 1
#
#
# my_print()
# print(count)


# 局部变量 nonlocal语句
def outer():
    num = 10

    def inner():
        nonlocal num  # nonlocal关键字声明，在内层函数中修改外层函数中定义的变量
        num = 100
        print(num)

    inner()
    print(num)


outer()

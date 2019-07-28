# 练习:定义my_print函数，统计该函数调用的次数。
#      提示：在my_print函数中统计

count = 0
def my_print():
    global count
    count = count + 1

my_print()
my_print()
my_print()
print(count)

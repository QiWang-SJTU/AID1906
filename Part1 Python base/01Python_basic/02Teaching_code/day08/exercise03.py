# 练习：定义判断列表中是否存在相同元素的函数
list01 = [4,5,6,7,6]
# 目标：让列表中所有元素俩俩比较.
# 思想：
# 让第一个元素,与后面所有元素进行比较(如果相同,则有了结论,应该退出方法)
# 让第二个元素,与后面所有元素进行比较(如果相同,则有了结论,应该退出方法)
# 让第三个元素,与后面所有元素进行比较(如果相同,则有了结论,应该退出方法)
# .....
# 让倒数第二个元素，与后面所有元素进行比较

"""
    # list_target[0]   list_target[1]   
    # list_target[0]   list_target[2] 
    #  ...
    # list_target[0]   list_target[4]  
    for index in range(1,len(list_target)):
        if list_target[0] == list_target[index]:
            return True# 具有相同元素

    # list_target[1]   list_target[2]   
    # list_target[1]   list_target[3] 
    #  ...
    # list_target[1]   list_target[4] 
    for index in range(2,len(list_target)):
        if list_target[1] == list_target[index]:
            return True# 具有相同元素

    # list_target[2]   list_target[3]   
    # list_target[2]   list_target[4]  
    for index in range(3,len(list_target)):
        if list_target[2] == list_target[index]:
            return True# 具有相同元素
"""

def is_repeating(list_target):
    # 取数据
    for r in range(len(list_target)-1):#0 1 2 ...
        # 作比较
        # 1  2 3 ... len(list_target) -1
        for c in range(r+1,len(list_target)):
            # 0  1 2 ...
            if list_target[r] == list_target[c]:
                return True# 具有相同元素
    return False

print(is_repeating(list01))

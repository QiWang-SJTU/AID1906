"""
    函数式编程 -- 思想
    17:10
"""

list01 = [4,5,5,6,767,8,10]

"""
# 1. 找出所有偶数
def find01():
    for item in list01:
        if item % 2 == 0:
            yield item
            
# 2. 找出所有奇数
def find02():
    for item in list01:
        if item % 2:
            yield item

# 3. 找出所有大于10
def find03():
    for item in list01:
        if item  > 10:
            yield item
"""
# "封装":提取变化
def condition01(item):
    return item % 2 == 0

def condition02(item):
    return item % 2

def condition03(item):
    return item  > 10

# "继承":隔离变化
# 根据任何条件,在任何可迭代对象中查找多个元素.
def find(target,func):
    for item in target:
        # if item > 10:
        # if condition03(item):
        if func(item):
            yield item

# "多态":执行变化
for item in find(list01,condition03):
    print(item)





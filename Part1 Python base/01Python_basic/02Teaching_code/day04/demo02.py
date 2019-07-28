"""
    for
        for 变量 in 可迭代对象:
            循环体
    练习：exercise05.py
         exercise06.py
"""

# for item in "我爱Python":
#     print(item)


# range(开始值,结束值,步长)  -->  整数生成器
# 不包含结束值
# for item in range(0,5,1):# 0 1 2 3 4
#     print(item)

# range(结束值)
# for item in range(5):# 0 1 2 3 4
#     print(item)

# range(开始值,结束值)
# for item in range(2,6):# 2 3 4 5
#     print(item)

# 倒序
# for item in range(6,3,-1):#6  5  4
#     print(item)

# 跳着
# for item in range(2,11,2):#2 4 6 8 10
#     print(item)


# for + range 特别适合做预定次数的循环.
for item in range(50):
    print(item)












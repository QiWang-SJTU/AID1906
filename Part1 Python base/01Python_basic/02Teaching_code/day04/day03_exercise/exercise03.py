"""
3. 在控制台中获取一个开始值5，一个结束值10。
                       8           2
   将中间的数字打印出来。
   6  7  8  9

   7  6  5  4  3
"""

# begin = 5
# end = 10
# # 6 7 8 9 10
# while begin < end - 1:
#     begin += 1
#     print(begin)


# begin = 10
# end = 5
# # 9 8 7 6
# while begin > end + 1:
#     begin -= 1
#     print(begin)


begin = 10
end = 5

if end > begin:
    # 正向
    while begin < end - 1:
        begin += 1
        print(begin)
else:
    # 反向
    while begin > end + 1:
        begin -= 1
        print(begin)

"""
# (扩展版本)
begin = int(input("请输入开始值："))
end = int(input("请输入结束值："))

# dir = None
# if end > begin:
#     dir = 1
# else:
#     dir = -1

dir = 1 if end > begin else -1
# 5 [6  7  8  9]  10
while begin != end - dir:
    begin += dir
    print(begin)
"""
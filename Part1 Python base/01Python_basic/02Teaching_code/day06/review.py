"""
    day06 复习
    容器
        字符串:存储字符编码值，不可变，序列。
        列表 ：存储变量，可变，序列。
            基础操作
"""
# 基础操作
# 创建
list01 = [1,2,3]
list01 = list("abc")
print(list01)
# 添加
list01.append("悟空")
list01.insert(2,"唐僧")

# 删除
list01.remove("悟空")
del list01[0]
print(list01)

# 修改
# 定位单个 --> 索引
# 定位多个 --> 切片
# 获取元素 --> 创建新的列表
# ? = 定位[切片]
# 修改元素
# 定位[切片] = ？

list01[2:2] = [1,2,3]
print(list01)

# 获取全部元素
for item in list01:
    print(item)

#2  1  0
for i in range(len(list01) - 1,-1,-1):
    print(list01[i])



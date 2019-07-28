"""
    str 通用操作
"""

#1. 数学运算符

# 拼接 +  +=
str01 = "悟空" +"八戒"
print(id(str01))# 139637893711808
# 产生了新的字符串"悟空八戒唐僧"
str01 += "唐僧"# 139637893711984
print(id(str01))

# 乘法：重复产生
str02 = "白雪公主"
str02 *= 10
print(str02)

# 比较运算：依次比较两个容器中元素,一但不同则返回比较结果
# 字符串比较的是编码值
str03 = "ac悟空"
str04 = "b唐僧"
print(str03 > str04)

# 2. 成员运算
re = "八戒" in str01
print(re)

# 3. 索引:定位单个元素
message = "我叫齐天大圣。"
# 获取第一个字符
print(message[0])
print(message[-len(message)])

# 获取最后一个字符
print(message[-1])
print(message[len(message)-1])

# IndexError: string index out of range
# 索引越界
# print(message[500])

# 4. 切片:定位多个元素
print(message[2:6])# 齐天大圣
print(message[2:6:2])# 齐大
# 开始索引，默认从头开始。
print(message[:6])# 我叫齐天大圣
# 结束索引，默认到末尾。
print(message[2:])# 齐天大圣。
# 正向获取
print(message[:])# 我叫齐天大圣。
# 反向获取
print(message[::-1])# 。圣大天齐叫我

print(message[-3:-6:-1])# 大天齐
# 可以同时使用反向与正向索引
print(message[-3:1:-1])# 大天齐

print(message[3:1])# 空
print(message[3:1:-1])# 天齐
print(message[1:1])# 空
print(message[-2:1])# 空
print(message[1:500])# 叫齐天大圣。









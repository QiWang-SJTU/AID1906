str_1 = input("请输入字符串： ")

# 打印第一个字符
print(str_1[0])

# 打印倒数第三个字符
print(str_1[len(str_1) - 3])
# print(str_1[-3])

# 打印前两个字符
print(str_1[:2])

# 倒序打印所有字符
print(str_1[::-1])

# 打印所有正向索引是奇数的字符
for i in range(1, len(str_1)):
    if i % 2:
        print(str_1[i])

# 如果字符串长度是奇数，则打印中间的字符
if len(str_1) % 2:
    print(str_1[int((len(str_1) - 1) / 2)])
else:
    print("字符串长度为偶数")

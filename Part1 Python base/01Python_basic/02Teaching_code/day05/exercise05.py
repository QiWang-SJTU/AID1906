# 练习2:获取列表[4,54,5,6,67,17,8]中最大数字.不使用max
list01 = [4, 54, 5, 6, 67, 17, 8]
# 思想：
# 假设第一个元素就是最大的
max_value = list01[0]
# 依次与后面的元素进行比较
for i in range(1, len(list01)):
    # 发现更大的元素则替换假设的元素
    if max_value < list01[i]:
        max_value = list01[i]
print(max_value)

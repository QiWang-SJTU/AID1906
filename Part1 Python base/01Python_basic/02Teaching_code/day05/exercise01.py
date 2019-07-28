"""
练习：
1. 定义列表，存储八大行星.
2. 打印距离太阳最近的行星(第一个元素)
3. 打印距离太阳最远的行星(最后一个元素)
4. 打印太阳到地球之间的行星。
5. 打印八大行星(一行一个)
6. 倒序打印八大行星(一行一个)
"""
list_planets = ["水星", "金星", "地球", "火星", "木星", "土星", "天王星", "海王星"]
print(list_planets[0])
print(list_planets[-1])
# print(list_planets[:2])
# list_planets[:2] --》 ["水星", "金星"]
for item in list_planets[:2]:
    print(item)

# 获取所有
for item in list_planets:
    print(item)

# 根据索引 倒序获取
for i in range(len(list_planets)-1,-1,-1):
    print(list_planets[i])


"""
    练习：一张纸的厚度是0.01毫米
        请计算对折多少次，超过珠穆朗玛峰8844.43米.
    10:40
"""

count = 0
# 毫米 --> 米
thickness = 0.01 / 1000

while thickness < 8844.43:
    thickness *= 2 # 对折一次
    count +=1# 记录对折的次数
    # print("对折"+str(count)+"次的厚度是："+str(thickness))

# 结论
print(count)

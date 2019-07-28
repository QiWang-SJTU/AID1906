"""
6. (扩展)
    一个小球从100米的高度落下
    每次弹回原高度的一半
    计算:
     总共弹起来多少次?(最小弹起高度0.01m)
     总共走了多少米(从100米算起)
     提示：使用循环模拟弹起来的过程.
"""
height = 100# 高度
count = 0 # 统计弹起次数的变量
distance = height# 统计弹起距离的变量

# 循环条件：弹起来的高度大于0.01
while height / 2 > 0.01:
    count += 1
    # 弹起来 高度的变化
    height /= 2
    print("第%d次弹起来的高度是：%f." % (count, height))
    distance += height * 2  # 累加起落距离

print("总共弹起来%d次." % (count))
print("总共走了%.2f米." % distance)

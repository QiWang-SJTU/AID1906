"""
    在控制台中获取一个四位整数：1234
    计算每位相加和.1+2+3+4 --> 10
    提示:17 -->  7
    16:55 上课
"""
# 方法一：
# number = int(input("请输入四位整数："))  # "1234" --> 1234
# # 个位  1234 % 10 --> 4
# unit01 = number % 10
# # 十位  1234 // 10 --> 123 % 10 --> 3
# unit02 = number // 10 % 10
# # 百位
# unit03 = number // 100 % 10
# # 千位
# unit04 = number // 1000
# result = unit01 + unit02 + unit03 + unit04
# print("结果是：" + str(result))

# 方法二（建议）：
number = int(input("请输入四位整数："))  # "1234" --> 1234
# 个位
result = number % 10
# 个位 累加　十位
# result = result + number // 10 % 10
result += number // 10 % 10
# 继续累加百位
result += number // 100 % 10
# 继续累加千位
result += number // 1000

print("结果是：" + str(result))

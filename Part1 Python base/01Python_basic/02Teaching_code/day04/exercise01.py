"""
    练习:
        累加1 -- 50之间的整数
        1 +2 + 3 + 4 + 5 ... 50
"""
# 1. 准备需要累加的数字
# 2. 在循环外定义存储累加和的变量
# 3. 在循环内累加需要累加的数字


begin = 1
sum_value = 0  #用于存储累加和的变量
while begin <= 50:
    # 累加 begin
    sum_value += begin
    begin += 1

print(sum_value)






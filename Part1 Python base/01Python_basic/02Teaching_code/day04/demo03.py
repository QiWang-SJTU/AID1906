"""
    continue
    练习:exercise07.py
"""

# 累加1 -- 50 之间，能被6整除的数字.
# sum_value = 0
# for item in range(1,51):
#     # 如果能被6整除则累加
#     if item % 6 == 0:
#         sum_value += item
#
# print(sum_value)

sum_value = 0
for item in range(5,51):
    # 如果不能被6整除则跳过
    if item % 6 != 0:
        continue
    sum_value += item

print(sum_value)







# 练习:累加10--80之间，个位不是2,5,6的整数

sum_value = 0
for item in range(10,81):
    unit = item % 10
    if unit == 2 or unit ==  5 or unit ==  6:
        continue
    sum_value += item

print(sum_value)

#15:35 上课
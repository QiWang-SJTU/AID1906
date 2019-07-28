number1 = float(input("请输入数字1： "))
number2 = float(input("请输入数字2： "))
number3 = float(input("请输入数字3： "))
number4 = float(input("请输入数字4： "))

result_max = number1
if result_max < number2:
    result_max = number2

if result_max < number3:
    result_max = number3

if result_max < number4:
    result_max = number4

print(result_max)

# result = []
# for i in range(4):
#     number = input("请输入数字: ")
#     result.append(number)
#
# result_max = max(result)
# print(result_max)

number = int(input("请输入一个四位整数："))

# 方法一：
first = number//1000
second = number//100 % 10
third = number//10 % 10
fourth = number % 10

total = first + second + third + fourth
print("四位相加和为： " + str(total))

# 方法二：

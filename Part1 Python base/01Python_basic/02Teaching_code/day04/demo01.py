"""
   猜数字2.0版本
   如果猜错3次，退出循环，提示 次数到达3次.
   练习：exercise04.py

"""
# 生成随机数的工具
import random

# 产生一个随机数
random_number = random.randint(1, 100)
print(random_number)

count = 0
while count < 3:
    count += 1
    input_number = int(input("请输入："))
    if input_number > random_number:
        print("大了")
    elif input_number < random_number:
        print("小了")
    else:
        print("恭喜猜对了，总共猜了" + str(count) + "次。")
        break
else:# 可以判断循环是从条件离开的，还是从循环体中离开(break)的.
    print("次数到达3次")

print("后续逻辑")

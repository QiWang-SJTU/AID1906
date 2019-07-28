"""
    练习:
        程序运行后，产生一个1--100之间的随机数.
        让玩家重复猜测，直到猜对了为止.
        提示：大了
             小了
             恭喜，猜对了，总共猜了多少次.
"""
# 生成随机数的工具
import random

# 产生一个随机数
random_number = random.randint(1, 100)
print(random_number)

count = 0
while True:
    count += 1
    input_number = int(input("请输入："))
    if input_number > random_number:
        print("大了")
    elif input_number < random_number:
        print("小了")
    else:
        print("恭喜猜对了，总共猜了" + str(count) + "次。")
        break


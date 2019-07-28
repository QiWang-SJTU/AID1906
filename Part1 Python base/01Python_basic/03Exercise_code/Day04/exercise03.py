# import random
#
# num = random.randint(1, 100)
# guess_n = 0
#
# while True:
#
#     guess_num = int(input("请输入猜测值： "))
#     guess_n += 1
#     if guess_num < num:
#         print("猜小了")
#     elif guess_num > num:
#         print("猜大了")
#     else:
#         print("恭喜你，猜对了，总共猜了 " + str(guess_n) + "次")
#         print("猜的数为： " + str(guess_num))
#         break

# 猜三次
import random

num = random.randint(1, 100)
guess_n = 0

while guess_n < 3:

    guess_num = int(input("请输入猜测值： "))
    guess_n += 1
    if guess_num < num:
        print("猜小了")
    elif guess_num > num:
        print("猜大了")
    else:
        print("恭喜你，猜对了，总共猜了 " + str(guess_n) + "次")
        print("猜的数为： " + str(guess_num))
        break
# 判断是从条件退出还是从循环中退出
else:
    print("次数到达3次.")

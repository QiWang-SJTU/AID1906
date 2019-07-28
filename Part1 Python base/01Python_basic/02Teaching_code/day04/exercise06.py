# 练习：随机加法考试题  2   +   10  =  ？
# 随机产生两个数字，在控制台中获取两个数相加的结果
# 如果输入正确，得10分，如果输入错误，扣5分。
# 总共3道题，最后输出总分.

# 生成随机数的工具
import random

score = 0
for i in range(3):  # 0 1 2
    # 产生一个随机数
    random_number01 = random.randint(1, 100)
    random_number02 = random.randint(1, 100)
    result = int(input(str(random_number01) + "+" + str(random_number02) + "=?:"))
    # 如果答对了
    if random_number01 + random_number02 == result:
        score += 10
    else:
        score -= 5

print("总分是：" + str(score))

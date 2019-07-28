
# 练习:定义函数,在控制台中获取成绩.
#     要求:如果异常,则继续获取成绩,直到正确为止.

def get_score():
    while True:
        try:
            score = int(input("请输入成绩:"))
            return score
        except:
            print("输入有误")


score = get_score()
print(score)

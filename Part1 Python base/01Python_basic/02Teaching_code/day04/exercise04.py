# 循环根据成绩判断等级，如果录入空字符串则退出程序.
# 如果成绩范围超过0--100之间到达3次，则退出程序，提示"成绩录入过多"

count = 0
while count < 3:
    str_score = input("请输入成绩：")
    # if str_score == "":
    #     break 
    if not str_score:
        break
    score = int(str_score)
    if score < 0 or score > 100:
        print("成绩有误")
        count += 1
    elif 90 <= score:
        print("优秀")
    elif 80 <= score:
        print("良好")
    elif 60 <= score:
        print("及格")
    else:
        print("不及格")
else:
    print("成绩录入过多")
# 练习:在控制台中获取所有学生的成绩(循环，一个一个录入)
#     如果录入空字符串，则停止.
#     获取最高分，最低分，平均分.(借助内置函数实现)

list_scores = []
while True:
    str_score = input("请输入成绩：")
    if str_score == "":
        break
    score = int(str_score)
    list_scores.append(score)

print(max(list_scores))
print(min(list_scores))
print(sum(list_scores) / len(list_scores))


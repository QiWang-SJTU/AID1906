student_score_final = []
while True:
    student_score = input("请输入所有学生成绩： ")
    if not student_score:
        print("录入结束.")
        break
    student_score = int(student_score)
    student_score_final.append(student_score)

max_score = max(student_score_final)
min_score = min(student_score_final)
sum_score = sum(student_score_final)
mean_score = sum_score / len(student_score_final)

print(max_score, min_score, mean_score)

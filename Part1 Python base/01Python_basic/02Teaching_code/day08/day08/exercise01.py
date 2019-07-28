"""
    定义根据成绩，计算等级的函数
"""
# def calculate_score_level(score):
#     if score < 0 or score > 100:
#         return "成绩有误"
#     elif 90 <= score:
#         return "优秀"
#     elif 80 <= score:
#         return "良好"
#     elif 60 <= score:
#         return "及格"
#     else:
#         return "不及格"

def calculate_score_level(score):
    if score < 0 or score > 100:
        return "成绩有误"# 满足条件，退出函数。
    if 90 <= score:
        return "优秀"
    if 80 <= score:
        return "良好"
    if 60 <= score:
        return "及格"
    return "不及格"
print(calculate_score_level(80))

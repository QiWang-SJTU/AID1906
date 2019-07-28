"""
    字符串格式化

    "..%s..%s.."%(变量,变量)

    练习:exercise10
"""

name = "孙悟空"
age = 800
score = 85.62

# 我叫：xx，今年:xx岁.
str01 = "我叫：" + name + "，今年:" + str(age) + "岁."

str02 = "我叫：%s，今年:%d岁,成绩是:%.1f。"%(name, age, score)
print(str02)



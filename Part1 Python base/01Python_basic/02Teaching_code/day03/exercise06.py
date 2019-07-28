# 根据身高体重，打印身体状况.
# BMI：用体重(公斤)除以身高(米)的平方而得出的数字.
# BMI <18.5  --> 体重过轻
# 18.5 <= BMI < 24   --> 体重正常
# 24 <= BMI < 28   --> 超重
# 28 <= BMI < 30   --> I度肥胖
# 30 <= BMI < 40   --> II度肥胖
# BMI >= 40   --> III度肥胖


height = float(input("请输入身高："))
weight = float(input("请输入体重："))
BMI = weight / height ** 2
if BMI < 18.5:
    print("体重过轻")
elif BMI < 24:
    print("体重正常")
elif BMI < 28:
    print("超重")
elif BMI < 30:
    print("I度肥胖")
elif BMI < 40:
    print("II度肥胖")
else:
    print("III度肥胖")











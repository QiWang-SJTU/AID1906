# 练习2: 定义函数,在控制台中获取年龄.
#     要求:如果异常或者超过范围(23 -- 30)则继续获取年龄,直到正确为止.

def get_age():
    while True:
        try:
            age = int(input("请输入年龄:"))
            if 23 <= age <= 30:
                return age
            else:
                print("年龄输入超过范围")
        except:
            print("输入有误")


score = get_age()
print(score)
# 练习:让信息管理系统,没有异常.
# 要求:异常处理必须保证程序按照既定流程执行.

"""
    异常处理
"""
def div_apple(apple_count):
    """
        分苹果
    """
    person_count = int(input("请输入人数:"))# ValueError
    result = apple_count / person_count# ZeroDivisionError
    print("每个人分到了%d个苹果"%result)

"""
try:
    div_apple(10)
except:
    # 错误的处理逻辑
    print("出错喽")
"""

"""
try:
    div_apple(10)
except ValueError:
    print("输入的人数必须是整数")
except ZeroDivisionError:
    print("输入的人数不能是零")
except Exception:
    # 错误的处理逻辑
    print("出错喽")
else:
    print("没有错误执行的代码")
"""

try:
    # 如果有错误
    div_apple(10)
finally:
    # 不处理错误,但有一件非常重要的事情,必须执行.
    print("一定执行的代码")


print("后续逻辑.........")

# 练习:定义函数,在控制台中获取成绩.
#     要求:如果异常,则继续获取成绩,直到正确为止.















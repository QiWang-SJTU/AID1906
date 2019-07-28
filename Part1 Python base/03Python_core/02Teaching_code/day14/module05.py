__all__ = ["fun01"]
# 定义可以被其他模块导入的成员


def fun01():
    print("fun01")


# 隐藏成员:使用单下划线命名,
#          在其他模块中不使用
#         仅限于from ? import *
def _fun02():
    print("fun02")


def fun03():
    print("fun03")

print(__name__)# module05.py


if __name__ == "__main__":
    print("是主模块(程序从当前模块开始执行)")
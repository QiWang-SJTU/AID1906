# 练习2:
# 不影响旧功能(函数, 实例方法)基础,增加新功能(统计方法/函数的执行时间).
import time


def calculate_execute_time(func):
    def wrapper(*args, **kwargs):
        # 新功能
        start_time = time.time()
        re = func(*args, **kwargs)
        stop_time = time.time()
        print(stop_time - start_time)
        return re

    return wrapper


@calculate_execute_time
def fun01():
    print("fun01执行喽")

class MyClass:
    @calculate_execute_time
    def fun02(self):
        for i in range(1000000):
            print(i)

fun01()

MyClass().fun02()

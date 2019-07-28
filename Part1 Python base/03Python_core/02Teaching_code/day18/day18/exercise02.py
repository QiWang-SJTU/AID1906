# 练习2:
# 在不影响旧功能(存款, 取款)基础上, 增加新功能(验证账户).

def verify_accont(func):
    def wrapper(*args, **kwargs):  # 应对调用旧功能的实参不一致
        print("验证账户")
        return func(*args, **kwargs)  # 应对旧功能的形参不一致

    return wrapper


# deposit = verify_accont(deposit)
# 旧功能 = 内部函数 -> 新+旧
@verify_accont
def deposit(money):
    print("存入:", money)


@verify_accont
def withdraw():
    print("取款")
    return 10000


# deposit(1000000)# 调用旧功能,但执行内部函数.
deposit(money=1000000)  # 调用旧功能,但执行内部函数.
print(withdraw())

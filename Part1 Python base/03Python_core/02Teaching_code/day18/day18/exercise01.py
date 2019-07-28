"""
    练习1:
        在不影响旧功能(进入后台,删除订单)基础上,增加新功能(验证权限).
        体会:装饰器的拦截调用
"""

def verif_permissions(func):
    def wrapper(*args, **kwargs):
        print("验证权限")
        # if 通过:
        return func(*args, **kwargs)
    return wrapper

# 旧功能
@verif_permissions
def enter_background():
    print("进入后台")
@verif_permissions
def delete_order():
    print("删除订单")

enter_background()
delete_order()

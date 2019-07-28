"""
    装饰器
"""

# 需求变化:在以下两个函数中,增加新功能(在控制台中打印函数名称).
"""
def say_hello(): 
    print("hello")

def say_goodbye(): 
    print("goodbye")

say_hello()
say_goodbye()
"""

# 缺点:新增加的功能,定义了多次.
"""
def say_hello():
    print("say_hello")
    print("hello")

def say_goodbye():
    print("say_goodbye")
    print("goodbye")

say_hello()
say_goodbye()
"""

# 行为相同,数据不同.
# 提取相同的行为

# 缺点: 增加新功能,修改原有函数内部(代码可读性不高).
"""
def print_func_name(func):
    print(func.__name__)# 函数 --> 名称

def say_hello():
    print_func_name(say_hello)
    print("hello")

def say_goodbye():
    print_func_name(say_goodbye)
    print("goodbye")
"""
"""
# 新功能
def print_func_name(func):
    print(func.__name__)

# 旧功能
def say_hello(): 
    print("hello")

def say_goodbye(): 
    print("goodbye")

# 旧功能 = 新功能  + 旧功能
say_hello = print_func_name + say_hello

    
say_hello()
say_goodbye()
"""


# 缺点:定义完旧功能,需要在旧功能下面用内部函数覆盖.
"""
def print_func_name(func): # func --> say_hello
    def wrapper():
        # 定义新功能
        print(func.__name__)
        # 调用旧功能
        func()

    return wrapper

# 旧功能
def say_hello():
    print("hello")

def say_goodbye():
    print("goodbye")

# 旧功能 = 新功能  + 旧功能
# 旧功能 = 新功能 ( 旧功能 ) # 返回值是内部函数(新功能  + 旧功能)
say_hello = print_func_name(say_hello)
say_goodbye = print_func_name(say_goodbye)

say_hello()# 调用内部函数
say_goodbye()
"""

# 缺点:如果参数不同，会异常．
"""
def print_func_name(func): # func --> say_hello
    def wrapper():
        # 定义新功能
        print(func.__name__)
        # 调用旧功能
        func()

    return wrapper

# 旧功能
@print_func_name # say_hello = print_func_name(say_hello)
def say_hello():
    print("hello")

@print_func_name # say_goodbye = print_func_name(say_goodbye)
def say_goodbye():
    print("goodbye")

say_hello()# 调用内部函数
say_goodbye()
"""

# 缺点：旧功能的返回值丢失了
"""
def print_func_name(func): # func --> say_hello
    def wrapper(*args):# 星号元组形参
        # 定义新功能
        print(func.__name__)
        # 调用旧功能
        func(*args)# 序列实参
    return wrapper

# 旧功能
@print_func_name# say_hello = print_func_name(say_hello)
def say_hello():
    print("hello")
    return 1

@print_func_name# say_goodbye = print_func_name(say_goodbye)
def say_goodbye(name):
    print(name,"goodbye")
    return 2

print(say_hello())# 调用内部函数
print(say_goodbye("qtx"))
"""


def print_func_name(func): # func --> say_hello
    def wrapper(*args,**kwargs):
        # 定义新功能
        print(func.__name__)
        # 调用旧功能
        return func(*args,**kwargs)
    return wrapper

# 旧功能
@print_func_name# say_hello = print_func_name(say_hello)
def say_hello():
    print("hello")
    return 1

@print_func_name# say_goodbye = print_func_name(say_goodbye)
def say_goodbye(name):
    print(name,"goodbye")
    return 2

print(say_hello())# 调用内部函数
print(say_goodbye("qtx"))







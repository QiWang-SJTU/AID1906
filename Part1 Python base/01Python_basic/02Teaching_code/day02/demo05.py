"""
    运算符
        算数运算符
            + - * /   // %  **
        增强运算符
            += -=  *=  /=   //=  %=  **=
    练习:exercise05.py
        exercise06.py
        exercise07.py
        exercise08.py
        exercise09.py
"""
number01 = 5
number02 = 2
# result = number01 / number02 # 2.5
# result = number01 // number02 # 2
result = number01 % number02 # 2
print(result)  # ?

number03 = 4 ** 2
print(number03)# 4 * 4


#  增强运算符
number04 = 100
# print(number04 + 10)# 110
# print(number04)# ?100

temp = number04 + 10 # 110
print(number04)# 100

# # 变量 = 变量　+ 数据
number04 = number04 + 10
print(number04)# 110

# 变量 += 数据(改变自身变量)
number04 += 10
print(number04)# 110
















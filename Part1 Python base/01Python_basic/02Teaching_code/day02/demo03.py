"""
    核心数据类型
        变量没有类型，关联的对象才有类型.
"""

# 1. None 空 NoneType

# 占位:只希望有个变量，指向的对象还不确定。
name = None

skill01 = "乾坤大挪移"
# 解除"乾坤大挪移" 与　变量 skill01 的关系
skill01 = None

# 2. 整形(整数)int
# 十进制：每逢十进一位　0 1 2 3 ...10
number01 = 250
# 二进制：每逢二进一位　0 1  10  11  100  101
number02 = 0b100
# 八进制：每逢八进一位　0 1  2 ..  7 10  11
number03 = 0o10
# 十六进制：每逢十六进一位0 1 3 ...9   a(10) f(15)
number04 = 0xf
print(number04)

# 3. 浮点型(小数)float
number05 = 10.5
# 科学计数法
number06 = 1.23456e5
print(number06)  # 123456.0
number07 = 0.00000000000000000000000005
number08 = 5e-26
print(0.00001)

# 4. 字符串str
message01 = "我爱编程"
number09 = "100.5"
print(type(name))

# 5. *复数 complex
num01 = 10 + 1.5j
print(type(num01))

# 6. 类型转换
# input 函数的结果是字符串类型
str_age = input("请输入年龄：")  # "18"  + 1
# str --> int
int_age = int(str_age)  # 19
# int --> str
print("明年是：" + str(int_age))  # "明年是："  19

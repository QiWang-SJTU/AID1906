# 练习1：在控制台中获取一个整数，
#       如果是偶数为变量state赋值"偶数",否则赋值"奇数"

number = int(input("请输入整数："))
# if number % 2 == 1:
#     state = "奇数"
# else:
#     state = "偶数"

# state = "奇数" if number % 2 == 1 else "偶数"

# 17:05 上课
state = "奇数" if number % 2 else "偶数"
print(state)

# 练习2：在控制台中获取一个年份，
#       如果是闰年为变量day赋值29,否则赋值28
year = int(input("请输入年份："))
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    day = 29
else:
    day = 28

# 代码可读性要尽可能的高
# 由于逻辑比较复杂，还是建议传统写法。
# day = 29 if year % 4 == 0 and year % 100 != 0 or year % 400 == 0 else 28

# day = 29 if not year % 4 and year % 100 or not year % 400 else 28

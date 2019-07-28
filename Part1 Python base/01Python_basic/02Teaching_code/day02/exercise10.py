# 练习:在控制台中获取一个年份，判断是否为闰年.(True,Flase)
# 是闰年的条件：
#   （１）年份能被4整除，但是不能被100整除
# 　（２）年份能被400整除
year = int(input("请输入年份："))
result = (year % 4 == 0 and year % 100 != 0) or year % 400 == 0
print(result)

"""
    练习：
    在控制台中获取一个分钟数，
    再获取一个小时数，
    最后获取一个天数，
    计算总秒数
    按照指定格式输出：总秒数数是:xx。
"""
minute = int(input("请输入分钟："))
hour = int(input("请输入小时数："))
day = int(input("请输入天数："))
result = minute * 60 + hour * 60 * 60 + day * 24 * 60 * 60
print("总秒数数是:" + str(result) +"。")



minute = int(input("请输入分钟数："))
hour = int(input("请输入小时数："))
day = int(input("请输入天数："))

total_seconds = (day*24 + hour)*3600 + 60*minute
print("总秒数是：" + str(total_seconds))

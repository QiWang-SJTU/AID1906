import time

# 时间戳
print(time.time())
# 时间元组
print(time.localtime())

# 时间戳--->时间元组
print(time.localtime(1563326915.261526))

# 时间元组--->时间戳
time_tuple = time.localtime()
print(time.mktime(time_tuple))

# 时间元组--->字符串
print(time.strftime("%Y/%m/%d", time_tuple))

# 字符串--->时间元组
a = time.strptime("2019/07/17", "%Y/%m/%d")
print(a[6])


# def cal_week(year, month, day):
#     time_str = "%d/%d/%d" % (year, month, day)
#     time_tuple = time.strptime(time_str, "%Y/%m/%d")
#     tuple_week = ("星期一", "星期二", "星期三", "星期四", "星期五", "星期六", "星期日")
#     return tuple_week[time_tuple.tm_wday]
#
#
# print(cal_week(2019, 7, 17))
#
#
def cal_day_nums(year, month, day):
    time_str = "%d/%d/%d" % (year, month, day)
    birth_stamp = time.mktime(time.strptime(time_str, "%Y/%m/%d"))
    now_stamp = time.mktime(time.localtime())
    return "%d" % ((now_stamp - birth_stamp) / 3600 // 24)


print(cal_day_nums(1995, 8, 24))

print('This float, % -10.5f, has width 10 and precision 5.' % (3.1415926))

alist = ['hello', 'world']
for x, y in enumerate(alist):
    print('index %s:%s' % (x, y))

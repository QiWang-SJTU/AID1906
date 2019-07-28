"""
    标准库模块
    时间 time
    练习:exercise01.py
    练习:exercise02.py
"""
import time

# 1. 获取当前时间戳(从1970年1月1日到现在经过的秒数)
# 1563326340.661173
print(time.time())
# 2. 获取当前时间元组(年,月,日,小时,分钟,秒,一周的第几天,一年的第几天,夏令时)
time_tuple = time.localtime()
print(time_tuple)
# 3. 时间戳 -->时间元组
print(time.localtime(15633263))
# 4. 时间元组 -- 时间戳
print(time.mktime(time_tuple))
# 5. 时间元组 -->  字符串
print(time.strftime("%y/%m/%d %H:%M:%S",time_tuple))
print(time.strftime("%Y/%m/%d %H:%M:%S",time_tuple))
# 6. 字符串 --> 时间元组
# "19/07/17 09:36:48"
print(time.strptime("19/07/17 09:36:48","%y/%m/%d %H:%M:%S"))

















"""
4. 定义根据分钟,小时,天计算总秒数的函数
"""

def get_total_second(minute,hour,day):
    return minute * 60 + hour * 60 * 60 + day * 24 * 60 * 60

result = get_total_second(1,2,3)
print(result)

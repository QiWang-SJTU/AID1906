"""
5. 判断一个字符串是否位回文。
    判断算法：正向与反向相同.
    上海自来水来自海上
"""
message = "上海自来水来自海上"
if message == message[::-1]:
    print("是回文")
else:
    print("不是回文")

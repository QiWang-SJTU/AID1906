"""
3. 在控制台中录入一个字符串
   打印第一个字符
   打印倒数第三个字符
   打印前2个字符
   倒序打印所有字符串
   打印所有正向索引是奇数的字符
   如果字符串长度是奇数，则打印中间的字符。
"""
message = "我叫齐天大圣。"
print(message[0])
print(message[-3])
print(message[:2])
print(message[::-1])
print(message[1::2])

# if len(message) % 2 !=0:
#     pass
length = len(message)
if length % 2:
    print(message[length // 2])

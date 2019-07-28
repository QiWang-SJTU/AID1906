# 练习:将英文语句每个单词反转:
#  How are you  --> you are How
# 将字符串按照空格拆分为列表
# 将列表反转
# 将列表中元素拼接为字符串

message = "How are you"
list_temp = message.split(" ")
message = " ".join(list_temp[::-1])
print(message)

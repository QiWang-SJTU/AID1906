"""
    str 字面值
"""


name = "悟空"
name = '悟空'

# 可见即所得
name = """悟空"""
name = '''
        悟
        空
        '''

message = """我叫"齐'天'大圣"."""
print(message)

# 转义符:改变原有字符含义的特殊字符
# \"   \'  \n换行  \t tab键   \\
message ="我\n叫\"齐天\t大圣\"."
print(message)

url = "C:\\appData\\boaming\\ciniconfig"
# 原始字符串:没有转义符的字符串
url = r"C:\appData\boaming\ciniconfig"
print(url)


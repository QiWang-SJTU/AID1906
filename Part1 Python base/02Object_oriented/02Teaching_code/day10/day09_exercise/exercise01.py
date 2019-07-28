"""
3. 自学字符串/列表/字典常用函数
    (1)看看字符串都提供了哪些功能(中文含义)
    (2)参照文档自学常用函数
      to_student_for_month01\documentation\str_method.docx
    (3)解决具体问题：
    str01 = "  校训：  自 强不息,厚德 载 物.      "
        -- 查找空格的数量
        -- 删除字符串前后空格(中间的空格留着)
        -- 删除所有空格
        -- 查找"厚德"的位置
        -- 判断字符串是否一"校训"开头
"""

str01 = "校训：  自 强不息,厚德 载 物.      "
print(str01.count(" "))
# 删除左右空格,会产生新字符串.
print(str01.lstrip().rstrip())
# 将空格替换为空字符串
print(str01.replace(" ", ""))
# 查找第一个字符的索引
print(str01.index("厚德"))
print(str01.startswith("校训"))

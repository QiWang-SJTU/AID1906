import os  # 操作系统接口
import glob  # 文件通配符
from datetime import date  # 日期和时间

# 返回当前的工作目录
print(os.getcwd())
print(dir(os))

# 从目录通配符搜索中生成文件列表
print(glob.glob("*.py"))

# 返回年月日
now = date.today()
print(now)
birthday = date(1995, 8, 24)
age = now - birthday
print(age.days)


"""
5. 温度转换器
   公式：摄氏度　＝　(华氏度　- 32) / 1.8
   练习:已知摄氏度（在控制台中获取），计算华氏度.
"""
# 摄氏度 × 1.8　+ 32 ＝ 华氏度
centigrade = float(input("请输入摄氏度："))
fahrenheit = centigrade * 1.8 + 32
print("华氏度神是：" + str(fahrenheit))

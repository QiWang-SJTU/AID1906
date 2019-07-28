"""
4. 古代的秤一斤十六两  33
   在控制台中获取两，计算是几斤零几两.
"""
weight = int(input("请输入两："))
jin = weight // 16
liang = weight % 16
print("结果是："+str(jin)+"斤"+str(liang)+"两")
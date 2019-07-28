list01 = [1]
print(id(list01))
print(id(list01[0]))

# 删不掉，因为每次都从list01里面取值赋值给变量item
# del相当于解除了item与list01[0]之间的引用关系，并不改变list01
for item in list01:
    print(id(item))
    del item

print(list01)
print("----------------------------------------")


# 能删掉，因为remove方法是将item指向的对象给删除掉了，即是删除list01[0]
for item in list01:
    list01.remove(item)

print(list01)
print("----------------------------------------")
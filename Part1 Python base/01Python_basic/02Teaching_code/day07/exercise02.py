"""
    经理:曹操,刘备,孙权
    技术:曹操,刘备,张飞,关羽
    1)是经理也是技术的有谁？
    2)是经理不是技术的有谁？
    3)不是经理，是技术的有谁？
    4)张飞是经理吗？
    5)身兼一职的都有谁？
    6)总共有多少人？
"""
# 字典内嵌集合
dict_persons = {
    "经理": {"曹操", "刘备", "孙权"},
    "技术": {"曹操", "刘备", "张飞", "关羽"},
}
print(dict_persons["经理"] & dict_persons["技术"])
print(dict_persons["经理"] - dict_persons["技术"])
print(dict_persons["技术"] - dict_persons["经理"])
print("张飞" in dict_persons["经理"])
print(dict_persons["技术"] ^ dict_persons["经理"])
print(len(dict_persons["技术"] | dict_persons["经理"]))

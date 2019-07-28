dict_person = {
    "经理": {"曹操", "刘备", "孙权"},
    "技术": {"曹操", "刘备", "张飞", "关羽"}
}

set_01 = dict_person["经理"] & dict_person["技术"]
print(set_01)

set_02 = dict_person["经理"] - dict_person["技术"]
print(set_02)

set_03 = dict_person["技术"] - dict_person["经理"]
print(set_03)

answer_04 = "张飞" in dict_person["经理"]
print(answer_04)

answer_05 = dict_person["经理"] ^ dict_person["技术"]
print(answer_05)

answer_06 = dict_person["经理"] | dict_person["技术"]
print(len(answer_06))

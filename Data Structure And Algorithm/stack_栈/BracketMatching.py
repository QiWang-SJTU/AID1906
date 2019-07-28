'''
@Description: 数据结构第二天作业---括号匹配函数
@Author: Nick_QiWang
@Date: 2019-07-25 18:44:07
@LastEditors: Nick_QiWang
@LastEditTime: 2019-07-26 10:13:04
'''

from sstack import SStack

ss = SStack()
brackets = ("(", ")", "[", "]", "{", "}")
dict_bracket = {"}": "{", "]": "[", ")": "("}
bracket_left, bracket_right = dict_bracket.values(), dict_bracket.keys()

def bracket_match(str_input):
    """
    @Description: 括号匹配函数
    @param {type} str
    @return: None
    """

    if not str_input:
        print("输入为空")
        return
    for item in str_input:
        if item in bracket_left:
            ss.push(item)
        elif item in bracket_right:
            if ss.is_empty():
                print("少前括号")
                return
            elif dict_bracket[item] == ss.peek():
                ss.pop()
            else:
                print("括号不匹配")
                return
        else:
            continue
    if not ss.is_empty():
        print("少后括号")
        return
    print("匹配正确")

def generate_bracket(str_input):
    """括号生成器"""

    i, str_len = 0, len(str_input)
    while True:
        while i < str_len and str_input[i] not in brackets:
            i += 1
        if i >= str_len:
            return
        else:
            yield i, str_input[i]
            i += 1

def match(str_input):
    
    for i, item in generate_bracket(str_input):
        if item in bracket_left:
            ss.push((i, item))
        elif ss.is_empty() or ss.pop()[1] != dict_bracket[item]:
            print("Unmatch is found at %d for %s." % (i, item))
            return
    if not ss.is_empty():
        print("Unmatch is found at %d for %s." % (i, item))
    else:
        print("All brackets are matched.")

        
if __name__ == "__main__":
    str_input = "When an Open (Data] (standard) is created and promoted, it’s [important] to think why - what change is th=is {trying (to) drive}? What will people do with this data that they couldn’t do before?"
    # bracket_match(str_input)
    match(str_input)

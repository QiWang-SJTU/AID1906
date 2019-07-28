from sstack import SStack


def reverse_polish(str_input):
    """
        计算逆波兰表达式

    :param str_input: 待输入的逆波兰表达式
    :return: 计算结果 ---> float
    """
    res_ss = SStack()
    temp = str_input.split(" ")
    for item in temp:
        if item not in ("+", "-", "*", "/", "p"):
            res_ss.push(float(item))
        elif item == "+":
            y = res_ss.pop()
            x = res_ss.pop()
            res_ss.push(x + y)
        elif item == "-":
            y = res_ss.pop()
            x = res_ss.pop()
            res_ss.push(x - y)
        elif item == "*":
            y = res_ss.pop()
            x = res_ss.pop()
            res_ss.push(x * y)
        elif item == "/":
            y = res_ss.pop()
            x = res_ss.pop()
            res_ss.push(x / y)
        elif item == "p":
            return res_ss.peek()

def infix_to_postinfix(str_input):
    # TODO 中缀表达式转后缀表达式
    pass

if __name__ == "__main__":
    print(reverse_polish("1 2 + 4 * p"))

class SStack:
    """
        用顺序表实现栈的基本操作
    """

    def __init__(self):
        self.__list = []

    def is_empty(self):
        """判断是否为空"""
        return not self.__list

    def push(self, item):
        """加入元素"""
        self.__list.append(item)

    def pop(self):
        """弹出元素"""
        if self.is_empty():
            raise SStackError("pop from empty SStack")
        else:
            return self.__list.pop()

    def peek(self):
        """返回栈顶元素"""
        if self.is_empty():
            raise SStackError("peek from empty SStack")
        else:
            return self.__list[-1]

    def size(self):
        """返回栈的长度"""
        return len(self.__list)


class SStackError(Exception):
    """自定义异常类"""
    pass


if __name__ == "__main__":
    SStack = SStack()
    print(SStack.is_empty())
    SStack.push(1)
    print(SStack.is_empty())
    SStack.push(2)
    SStack.push(3)
    SStack.push(4)
    SStack.push(5)
    SStack.push(6)
    print(SStack.size())
    print(SStack.peek())
    print(SStack.pop())
    print(SStack.pop())
    print(SStack.pop())
    print(SStack.pop())
    print(SStack.pop())
    print(SStack.pop())

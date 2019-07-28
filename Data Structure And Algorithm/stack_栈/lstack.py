'''
@Description: coding- utf-8
@Author: Nick_QiWang
@Date: 2019-07-25 14:16:29
@LastEditors: Nick_QiWang
@LastEditTime: 2019-07-25 20:21:01
'''

"""用链表实现栈的基本操作 ---> 链式栈模型"""

class Node:
    """节点"""

    def __init__(self, elem, next=None):
        # elem存放数据元素
        self.elem = elem
        # next存放下一个结点的标识
        self.next = next

class LStack(object):
    def __init__(self):
        """top作为栈顶标记"""
        self.__top = None
    
    @property
    def top(self):
        return self.__top
    
    def is_empty(self):
        """判空"""
        return self.__top is None

    def push(self, item):
        """压栈"""
        self.__top = Node(item, self.__top)
        # node = Node(item)
        # node.next = self.__top
        # self.__top = node

    def pop(self):
        """出栈"""
        if self.is_empty():
            raise LStackError("pop from empty LStack")
        item = self.__top.elem
        self.__top = self.__top.next
        return item

    def peek(self):
        """查看栈顶元素"""
        if self.is_empty():
            raise LStackError("peek from empty LStack")
        return self.__top.elem
        
    
class LStackError(Exception):
    """自定义异常类"""
    pass


if __name__ == "__main__":
    ls = LStack()
    print(ls.is_empty())
    ls.push(1)
    print(ls.is_empty())
    ls.push(2)
    ls.push(3)
    ls.push(4)
    print(ls.pop())
    print(ls.pop())
    print(ls.pop())
    print(ls.pop())

    
    

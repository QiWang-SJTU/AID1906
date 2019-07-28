'''
@Description: 
@Author: Nick_QiWang
@Date: 2019-07-25 15:17:27
@LastEditors: Nick_QiWang
@LastEditTime: 2019-07-26 12:53:06
'''

"""用链表实现队列的基本操作 ---> 链式队列模型"""


class Node:
    """节点"""

    def __init__(self, elem, next=None):
        # elem存放数据元素
        self.elem = elem
        # next存放下一个结点的标识
        self.next = next

class LQueue:
    def __init__(self):
        """定义队头、队尾"""
        self.__front = self.__rear = Node(None)
    
    def is_empty(self):
        """判空"""
        return self.__front == self.__rear
    
    def enqueue(self, item):
        """入队,rear动"""
        node = Node(item)
        self.__rear.next = node
        self.__rear = node

    def dequeue(self):
        """出队,front动"""
        if self.is_empty():
            raise LQueueError("dequeue from empty Lqueue")
        if self.__front.next == self.__rear:
            item = self.__rear.elem
            self.__rear = self.__front
            self.__front.next = None
            return item
        else:
            temp = self.__front.next
            self.__front.next = temp.next
            return temp.elem

class LQueueError(Exception):
    pass


if __name__ == "__main__":
    lq = LQueue()
    lq.enqueue(1)
    lq.enqueue(2)
    lq.enqueue(3)
    lq.enqueue(4)
    lq.enqueue(5)
    print(lq.dequeue())
    print(lq.dequeue())
    print(lq.dequeue())
    print(lq.dequeue())
    print(lq.dequeue())
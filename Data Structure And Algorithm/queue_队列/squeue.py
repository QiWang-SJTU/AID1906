class Queue:
    """顺序表实现队列基本操作"""

    # todo 用链表来实现
    def __init__(self):
        self.__list = []

    def is_empty(self):
        """判断队列是否为空"""
        return not self.__list

    def size(self):
        """返回队列大小"""
        return len(self.__list)

    # 这两种出入队操作将取决于使用时是常用出队还是入队操作
    def enqueue(self, item):
        """入队"""
        self.__list.insert(0, item)
        # self.__list.append(item)

    def dequeue(self):
        """出队"""
        if self.is_empty():
            raise SQueueError("dequeue from empty Squeue")
        return self.__list.pop()
        # return self.__list.pop(0)


class SQueueError(Exception):
    pass


if __name__ == "__main__":
    queue = Queue()
    print(queue.is_empty())
    queue.enqueue(1)
    print(queue.is_empty())
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(4)
    queue.enqueue(5)
    queue.enqueue(6)
    print(queue.size())
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.dequeue())



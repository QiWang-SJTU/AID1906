'''
@Description: 反转队列
@Author: Nick_QiWang
@Date: 2019-07-25 16:03:31
@LastEditors: Nick_QiWang
@LastEditTime: 2019-07-25 17:07:18
'''

import sys, os

sys.path.append("./")
from stack_栈.lstack import LStack
from squeue import Queue

sq = Queue()
for item in range(8):
    sq.enqueue(item)

# 出队入栈
ls = LStack()
while not sq.is_empty():
    ls.push(sq.dequeue())

# 出栈入队
while not ls.is_empty():
    sq.enqueue(ls.pop())

print(sq.dequeue())
print(sq.dequeue())
print(sq.dequeue())
print(sq.dequeue())
print(sq.dequeue())
print(sq.dequeue())

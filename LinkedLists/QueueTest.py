from collections import deque
import datetime
# from matplotlib import pyplot as plt
from LinkedLists import SingleLinkedList as SLL
import gc

def test_simple_queue(iters):
    queue = []
    start = datetime.datetime.now()

    for i in range(iters):
        #queue.append(i)
        queue.insert(0,i)

    end = datetime.datetime.now()
    delta = end-start
    print(delta.seconds*1000+int(delta.microseconds/1000))


def test_dequeue(iters):
    queue = deque()
    start = datetime.datetime.now()

    for i in range(iters):
        #queue.append(i)
        queue.appendleft(i)

    end = datetime.datetime.now()
    delta = end-start
    print(delta.seconds*1000+int(delta.microseconds/1000))

def test_mylist(iters):
    queue = SLL.SingleLinkedList()
    start = datetime.datetime.now()

    queue.add(-1)
    for i in range(iters):
        #queue.add_to_tail_direct(i)
        queue.add(i, i-1)

    end = datetime.datetime.now()
    delta = end-start
    print(delta.seconds*1000+int(delta.microseconds/1000))

def test_list_addition(iters, period):
    gc.disable()
    #alist= []
    alist = SLL.SingleLinkedList()
    mlist = []
    alist.add(-1)
    for i in range(1, iters+1):
        if i % period == 1:
            start = datetime.datetime.now()

        #alist.append(i)
        alist.add_to_tail_direct(i)
        if i % period == 0:
            end = datetime.datetime.now()
            delta = end-start
            mlist.append(delta.seconds*1000000+delta.microseconds)
    gc.enable()
    plt.plot(mlist)
    plt.show()
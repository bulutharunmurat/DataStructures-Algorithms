from collections import deque

def queue_example():
    my_queue = []
    my_queue.append(5)
    my_queue.append(10)
    my_queue.append(4)
    print(my_queue)
    my_queue.pop(0)
    my_queue.pop(0)
    print(my_queue)

def dequeue_example():
    q = deque()
    q.append(5)
    q.append(10)
    q.append(4)
    print(q)
    print(q.popleft())
    print(q.popleft())
    print(q)
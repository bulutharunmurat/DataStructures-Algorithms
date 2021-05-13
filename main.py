''' LIFO => STACKS,    UNDO, BACK PAGE in WEB PAGES, NESTED FUNCTION CALLS
    FIFO => QUEUES,    AIRLINE MANAGEMENT
'''
from StacksQueues import StackByList
from StacksQueues import MyStack
from StacksQueues import QueuesByList
from StacksQueues import MyQueue
if __name__ == '__main__':
    '''
    if StackByList.checkParantheses("(((2+5)-(3*7))"):
        print("Correct parantheses")
    else:
        print("Incorrect parantheses")
    '''

    # a_stack = MyStack.MyStack(5)
    # a_stack.push("A")
    # print(a_stack)
    # a_stack.push("C")
    # print(a_stack)
    # a_stack.push("E")
    # print(a_stack.peek())
    # print(a_stack)
    # print(a_stack.pop())
    # print(a_stack.pop())
    # a_stack.push("X")
    # a_stack.push("Y")
    # print(a_stack)
    # a_stack.clear()

    q = MyQueue.MyQueue(5)
    q.enqueue("A")
    q.enqueue("B")
    q.enqueue("C")
    print(q)
    print(q.dequeue())
    q.dequeue()
    print(q)



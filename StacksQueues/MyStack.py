class MyStack():
    def __init__(self, capacity):
        self.top = -1
        self.capacity = capacity
        self.array = [i for i in range(capacity)]

    def push(self, var):
        if not self.is_full():
            self.top += 1
            self.array[self.top] = var
            #self.array.append(var)

    def pop(self):
        if not self.is_empty():
            val = self.array[self.top]
            self.top -= 1
            return val
        raise Exception("Stack is empty")

    def is_empty(self):
        return self.top == -1

    def is_full(self):
         return self.top == self.capacity - 1

    def clear(self):
        self.top = -1

    def peek(self):
        return self.array[self.top]

    def __str__(self):
        ret = ""
        for i in range(self.top + 1):
            ret += self.array[i]
        return ret




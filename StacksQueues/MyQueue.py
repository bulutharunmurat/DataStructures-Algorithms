class MyQueue:
    def __init__(self, capacity):
        self.front = 0
        self.rear = -1
        self.capacity = capacity
        self.array = capacity*[0]
        self.count = 0

    def is_empty(self):
        return self.count == 0

    def is_full(self):
        return self.count == self.capacity

    def enqueue(self, var):
        if not self.is_full():
            self.count += 1
            self.rear = (self.rear + 1) % self.capacity
            self.array[self.rear] = var

    def dequeue(self):
        if not self.is_empty():
            self.count -= 1
            var = self.array[self.front]
            self.front = (self.front+1) % self.capacity
            return var
        raise Exception("Queue is empty")

    def clear(self):
        self.rear = -1
        self.front = 0

    def __str__(self):
        var = ""
        for i in range(self.count):
            var += self.array[(self.front+i) % self.capacity]
        return var
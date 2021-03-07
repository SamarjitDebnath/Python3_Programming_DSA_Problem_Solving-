"""
Stack using Queue

@samarjit_debnath
"""


class Queue:
    def __init__(self, maxsize):
        self.front = -1
        self.rear = -1
        self.box = [None] * maxsize
        self.maxsize = maxsize

    def enqueue(self, x):
        if self.rear == self.maxsize - 1:
            print('Queue over flow')
        elif self.front == -1 and self.rear == -1:
            self.front = self.rear = 0
            self.box[self.rear] = x
        else:
            self.rear += 1
            self.box[self.rear] = x

    def deque(self):
        if self.is_empty():
            return 'Empty'
        elif self.front == self.rear:
            r = self.box[self.front]
            self.front = self.rear = -1
            return r
        else:
            r = self.box[self.front]
            self.front += 1
            return r

    def is_empty(self):
        return self.front == -1 and self.rear == -1

    def get_queue(self):
        if self.is_empty():
            return 'Empty'
        else:
            return self.box


class Stack:
    def __init__(self, size):
        self.size = size
        self.q1 = Queue(self.size)
        self.q2 = Queue(self.size)
        self.count = 0

    def push(self, a):
        self.count += 1
        while not self.q1.is_empty():
            self.q2.enqueue(self.q1.deque())
        self.q1.enqueue(a)
        while not self.q2.is_empty():
            self.q1.enqueue(self.q2.deque())

    def pop(self):
        return self.q1.deque()

    def display(self):
        return self.q1.get_queue()

# Driver code


if __name__ == '__main__':
    s = Stack(5)
    s.push(2)
    s.push(4)
    s.push(5)
    print(s.display())
    print()
    print(s.pop())

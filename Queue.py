"""Q. WAP to implement food ordering system in a restaurant, where one customer can place at a time and the shop
serves in FIFO process. Also calculate the waiting time for a customer.

@samarjit_debnath
"""

from collections import deque
import time
import threading


# Queue Class

class Queue:
    def __init__(self):
        self.box = deque()

    def enqueue(self, data):
        return self.box.appendleft(data)

    def dequeue(self):
        return self.box.pop()

    def is_empty(self):
        return len(self.box) == 0

    def size(self):
        return len(self.box)

    def get_queue(self):
        return self.box


global order


def place_order(*data):       # Order Function
    global order
    order = Queue()
    time.sleep(0.5)
    order.enqueue(data)
    print('Your Order is: ' + str(data))


def serve_order():           # Server Function
    global order
    order = Queue()
    time.sleep(1)
    if order.is_empty():
        print('No Order has been placed')
        return
    else:
        print('Thank and Enjoy: ', end=" ")
        print(order.dequeue())


if __name__ == '__main__':
    t = time.time()

    food = list(map(str, input('Please Order Something: ').split()))

    task1 = threading.Thread(target=place_order, args=food)
    task2 = threading.Thread(target=serve_order)

    task1.start()
    task2.start()

    task1.join()
    task1.join()

    print('Your waiting time: ' + str(time.time() - t) + ' Seconds')

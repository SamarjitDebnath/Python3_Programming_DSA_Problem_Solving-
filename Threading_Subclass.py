"""
Threading Subclass Example

@samarjit_debnath
"""

import threading
import time
import random


class CustThread(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name

    def run(self):
        getTime(self.name)
        print("Thread", self.name, "Execution ends")


def getTime(name):
    print('\nThread {} sleeps at {}'.format(name, time.strftime("%H:%M:%S", time.gmtime())))
    randSleepTime = random.randint(1, 5)
    time.sleep(randSleepTime)

# Driver Code


if __name__ == '__main__':
    thread1 = CustThread("1")
    thread2 = CustThread("2")

    thread1.start()
    thread2.start()

    print("\nThread 1 is Alive: ", thread1.is_alive())
    print("\nThread 2 is Alive: ", thread2.is_alive())

    print("\nThread 1 Name: ", thread1.getName())
    print("\nThread 2 Name: ", thread2.getName())

    print()

    thread1.join()
    thread2.join()

    print('\nExecution Ends')
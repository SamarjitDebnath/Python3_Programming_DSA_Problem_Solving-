import threading
import time
import random


def execute_thread(i):
    print('\nThread {} sleeps at {}'.format(i, time.strftime("%H:%M:%S", time.gmtime())))
    rand_sleep_time = random.randint(1, 5)
    time.sleep(rand_sleep_time)
    print("\nThread {} stops sleeping at {}".format(i, (time.strftime("%H:%M:%S", time.gmtime()))))


for j in range(10):
    thread = threading.Thread(target=execute_thread, args=(j, ))
    thread.start()
    print("\nActive Threads : ", threading.activeCount())
    print('\nThread Objects: ', threading.enumerate())

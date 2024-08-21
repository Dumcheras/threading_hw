import time
from random import randint
import threading
from statistics import mean
from threading import Lock

random_len = []
lock = Lock()


def rand(random_len):
    for i in range(20):
        i = randint(0, 10)
        random_len.append(i)
    print(random_len)


def summ_list(random_len, lock: Lock):
    lock.acquire()
    time.sleep(1)
    lock.release()
    print(sum(random_len))


def arifm_list(random_len):
    print(mean(random_len))


thread_1 = threading.Thread(target=rand(random_len), args=(random_len,))
thread_2 = threading.Thread(target=summ_list(random_len, lock), args=(random_len, lock,))
thread_3 = threading.Thread(target=arifm_list, args=(random_len,))

thread_1.start()
thread_2.start()
thread_3.start()

thread_1.join()
thread_2.join()
thread_3.join()

import threading
import time
from threading import Lock

# user_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#
#
# def func_max(user_list):
#     print(max(user_list), end=" ")
#
#
# def func_min(user_list):
#     print(min(user_list), end=" ")
#
#
# for i in range(5):
#     thread_1 = threading.Thread(target=func_max, args=(user_list,))
#     thread_1.start()
#
#     thread_2 = threading.Thread(target=func_min, args=(user_list,))
#     thread_2.start()


user_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
lock = Lock()


def func_max(user_list, lock: Lock):
    for i in range(5):
        lock.acquire()
        time.sleep(0.3)
        lock.release()
        print(max(user_list), end=" ")


def func_min(user_list, lock: Lock):
    for i in range(5):
        lock.acquire()
        time.sleep(0.3)
        lock.release()
        print(min(user_list), end=" ")


thread_1 = threading.Thread(target=func_max, args=(user_list, lock))
thread_1.start()


thread_2 = threading.Thread(target=func_min, args=(user_list, lock))
thread_2.start()

from random import randint
import threading
from statistics import mean

random_len = []


def rand(random_len):
    random_len = [randint(-10, 10) for _ in range(10)]
    print(random_len)


thread_1 = threading.Thread(target=rand(random_len), args=(random_len,))
thread_1.start()


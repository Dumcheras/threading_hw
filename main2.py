import threading
from statistics import mean

user_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def summ_list(user_list):
    print(sum(user_list), end=" ")


def arifm_list(user_list):
    print(mean(user_list), end=" ")


for i in range(5):
    thread_1 = threading.Thread(target=summ_list, args=(user_list,))
    thread_1.start()
print(" ")
for i in range(5):
    thread_2 = threading.Thread(target=arifm_list, args=(user_list,))
    thread_2.start()

import threading

user_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def func_max(user_list):
    print(max(user_list), end=" ")


def func_min(user_list):
    print(min(user_list), end=" ")


for i in range(5):
    thread_1 = threading.Thread(target=func_max, args=(user_list,))
    thread_1.start()
for i in range(5):
    thread_2 = threading.Thread(target=func_min, args=(user_list,))
    thread_2.start()

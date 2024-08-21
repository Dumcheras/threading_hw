import threading

user_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def func_max(user_list):
    print(max(user_list))


for i in range(5):
    thread_1 = threading.Thread(target=func_max, args=(user_list,))
    thread_1.start()

import threading
import time
import json


f = open("inventory.dat","r")
cart_list = json.load(f)
f.close()


shared_cart = []
lock = threading.Lock()


def bot_clerk(items, /):
    """" """
    robot_fetcher_lists = [[] for _ in range(3)] #create 3 empty list of list

    for i, item in enumerate(items, start=1):
        robot_fetcher_lists[(i-1)%3].append(item)
    
    threads_start = []
    threads_join = []

    for robot_fetcher_list in robot_fetcher_lists:
        thread = threading.Thread(target=bot_fetcher, args=(robot_fetcher_list, shared_cart, lock))
        threads_start.append(thread)
        threads_join.append(thread)

    for thread in threads_start:
        thread.start()

    for thread in threads_join:
        thread.join()

    # shared_cart.sort(key=lambda x: cart_list[x[0]][1])
    return shared_cart


def bot_fetcher(items, cart, thread_lock, /):
    for item in items:
        # with thread_lock:
        time.sleep(cart_list[item][1])
        cart.append([item,cart_list[item][0]])




# input_4 = ['103', '108', '102', '110', '106']
# # input_1 = ['106','109','102']
# print(bot_clerk(input_4))

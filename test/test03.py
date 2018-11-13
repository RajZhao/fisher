"""
    Created by RajZhao on 2018/11/08
"""


import threading
import time


def worker():
    print("I am thread")
    t = threading.current_thread()
    time.sleep(100)
    print(t.getName())
# print("I am Raj")


new_t = threading.Thread(target=worker)
new_t.start()

t = threading.current_thread()
print(t.getName())

"""
# @Author         : SYACHUN
# @Date           : 2020-06-16 16:24:12
# @LastEditTime: 2020-06-16 16:30:09
# @LastEditors: SYACHUN
# @Description    : 
# @FilePath       : \weikeban\基于queue模块中队列的同步.py
"""
import time
import queue
import threading
q = queue.Queue(10)


def productor(i):
    while True:
        time.sleep(1)
        q.put("厨师{}做的包子！".format(i))


def consumer(j):
    while True:
        print("顾客{}吃了一个{}".format(j, q.get()))
        time.sleep(1)


for i in range(3):
    t = threading.Thread(target=productor, args=(i,))
    t.start()
for k in range(10):
    v = threading.Thread(target=consumer, args=(k,))
    v.start()

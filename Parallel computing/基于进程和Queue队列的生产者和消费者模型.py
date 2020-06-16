"""
# @Author         : SYACHUN
# @Date           : 2020-06-16 16:52:43
# @LastEditTime: 2020-06-16 16:58:57
# @LastEditors: SYACHUN
# @Description    : 
# @FilePath       : \weikeban\基于进程和Queue队列的生产者和消费者模型.py
"""
import time
import multiprocessing as mp


def productor(i, q):
    while True:
        time.sleep(1)
        q.put('厨师{}做的包子！'.format(i))


def consumer(j, q):
    while True:
        print('顾客{}吃了一个{}'.format(j, q.get()))
        time.sleep(1)


if __name__ == "__main__":
    q = mp.Queue(10)
    for i in range(3):
        p = mp.Process(target=productor, args=(i, q))
        p.start()
    for k in range(10):
        p = mp.Process(target=consumer, args=(k, q))
        p.start()

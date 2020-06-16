"""
# @Author         : SYACHUN
# @Date           : 2020-06-16 17:01:13
# @LastEditTime: 2020-06-16 17:08:01
# @LastEditors: SYACHUN
# @Description    : 
# @FilePath       : \weikeban\基于multiprocessing中的Pipe管道通信.py
"""
import multiprocessing as mp
import time
import random
import itertools


def consumer(conn):
    while True:
        try:
            item = conn.recv()
            time.sleep(random.randrange(2))
            print("consumer:{}".format(item))
        except EOFError:
            break


def producer(conn):
    for i in itertools.count(1):
        time.sleep(random.randrange(2))
        conn.send(i)
        print("producer:{}".format(i))


if __name__ == "__main__":
    conn_out, conn_in = mp.Pipe()
    p_producer = mp.Process(target=producer, args=(conn_out,))
    p_producer.start()
    p_consumer = mp.Process(target=consumer, args=(conn_in,))
    p_consumer.start()

    p_producer.join()
    p_consumer.join()

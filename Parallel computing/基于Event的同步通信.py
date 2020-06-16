"""
# @Author         : SYACHUN
# @Date           : 2020-06-16 16:32:22
# @LastEditTime: 2020-06-16 16:49:25
# @LastEditors: SYACHUN
# @Description    : 
# @FilePath       : \weikeban\基于Event的同步通信.py
"""
import threading
import random


def f(i, e):
    e.wait()
    print("线程{}的随机结果为{}\n".format(i, random.randrange(1, 100)))


if __name__ == "__main__":
    event = threading.Event()
    for i in range(3):
        t = threading.Thread(target=f, args=(i, event))
        t.start()
    ready = input('请输入1开始继续执行阻塞的线程：')
    if ready == "1":
        event.set()

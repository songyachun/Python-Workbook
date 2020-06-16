"""
# @Author         : SYACHUN
# @Date           : 2020-06-16 15:10:59
# @LastEditTime: 2020-06-16 15:56:32
# @LastEditors: SYACHUN
# @Description    : 
# @FilePath       : \weikeban\td_producer_consumer.py
"""
import threading
import time
import random


class Container1():   # 基于同步和通信
    def __init__(self):
        self.contents = 0
        self.available = False
        self.cv = threading.Condition()

    def put(self, value):
        with self.cv:
            if self.available:
                self.cv.wait()
            self.contents = value
            t = threading.current_thread()
            print('{0}生产{1}'.format(t.name, self.contents))
            self.available = True
            self.cv.notify()

    def get(self):
        with self.cv:
            if not self.available:
                self.cv.wait()
            t = threading.current_thread()
            print('{0}消费{1}'.format(t.name, self.contents))
            self.available = False
            self.cv.notify()


class Container2():  # 无同步和通信
    def __init__(self):
        self.contents = 0
        self.available = False

    def put(self, value):
        if self.available:
            pass
        else:
            self.contents = value
            t = threading.current_thread()
            print('{0}生产{1}'.format(t.name, self.contents))
            self.available = True

    def get(self):
        if not self.available:
            pass
        else:
            t = threading.current_thread()
            print('{0}消费{1}'.format(t.name, self.contents))
            self.available = False


class Producer(threading.Thread):   # 生产者类
    def __init__(self, container):
        threading.Thread.__init__(self)
        self.container = container

    def run(self):
        for i in range(1, 6):
            time.sleep(random.choice(range(5)))
            self.container.put(i)


class Consumer(threading.Thread):  # 消费者类
    def __init__(self, container):
        threading.Thread.__init__(self)
        self.container = container

    def run(self):
        for i in range(1, 6):
            time.sleep(random.choice(range(5)))
            self.container.get()


def test1():
    print('基于同步和通信的生产者与消费者模型：')
    container = Container1()
    Producer(container).start()
    Consumer(container).start()


def test2():
    print('无同步和通信的生产者消费者模型：')
    container = Container2()
    Producer(container).start()
    Consumer(container).start()


if __name__ == "__main__":
    # test1()
    test2()

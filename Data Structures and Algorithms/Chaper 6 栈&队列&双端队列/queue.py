"""
队列 
1. 先进先出
"""


class ArrayQueue:
    """ FIFO queue implementation using a Python list as underlying storage. """
    DEFAULT_CAPACITY = 10

    def __init__(self):
        """ Create an empty queue. """
        self._data = [None] * ArrayQueue.DEFAULT_CAPACITY
        self._size = 0
        self._front = 0

    def __len__(self):
        """ Return the number of elements in the queue. """
        return self._size

    def is_empty(self):
        """ Return True if the queue is empty。 """
        return self._size == 0

    def first(self):
        """ Return (but do not remove) the element at the front of the queue. """
        if self.is_empty():
            raise Exception('Queue is empty.')
        return self._data[self._front]

    def dequeue(self):
        """ Remove and return the first element if the queue(i.e.,FIFO).
        Raise Empty exception if the queue is empty.
        """
        if self.is_empty():
            raise Exception('Queue is empty')
        answer = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front+1) % len(self._data)
        self._size -= 1
        return answer

    def enqueue(self, e):
        """ Add an element to the back of queue. """
        if self._size == len(self._data):
            self._resize(2*len(self._data))
        avail = (self._front+self._size) % len(self._data)
        self._data[avail] = e
        self._size += 1

    def _resize(self, cap):
        """ Resize to a new list of capacity>=len(self) """
        old = self._data
        self._data = self._front
        walk = self._front
        for k in range(self._size):
            self._data[k] = old[walk]
            walk = (1+walk) % len(old)
        self._front = 0

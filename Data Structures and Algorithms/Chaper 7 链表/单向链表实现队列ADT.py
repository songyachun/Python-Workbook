""" 使用单向链表操作队列，时间复杂度为O(1) """


class LinkedQueue():
    """ FIFO queue implementation using a singly linked list for storage. """
    # ----------------------------------nested _Node class-------------------
    class _Node:
        """ Lightweight,nonpublic class for storing a singly linked node. """
        __slots__ = '_element', '_next'

        def __init__(self, element, next):
            self._element = element
            self._next = next
    # ----------------------------------queue methods-------------------------

    def __init__(self):
        """ Create an empty queue. """
        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):
        """ Return the number of element in the queue. """
        return self._size

    def is_empty(self):
        """ Return True if the queue is empty. """
        return self._size == 0

    def first(self):
        """ Return (but do not remove) the element at the front of the queue. """
        if self.is_empty():
            raise Exception('Queue is empty')
        return self._head._element

    def dequeue(self):
        """ Remove and return the first element of the queue(i.e.,FIFO).
        Raise Empty exception if the queue is empty. """
        if self.is_empty():
            raise Exception('Queue is empty')
        answer = self._head._element
        self._head = self._head._next
        self._size -= 1
        if self.is_empty():
            self._tail = None
        return answer

    def enqueue(self, e):
        """ Add  element to the back of queue. """
        newest = self._Node(e, None)
        if self.is_empty():
            self._head = newest
        else:
            self._tail._next = newest
        self._tail = newest
        self._size += 1

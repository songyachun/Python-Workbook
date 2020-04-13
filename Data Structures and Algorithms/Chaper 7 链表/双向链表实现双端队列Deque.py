""" 使用哨兵时，实现方法的关键是要记住双端队列的第一个元素并不存储在头节点，而是存储在头节点后的第一个节点。同样，尾节点之前的一个节点中存储的是双端队列的最后一个元素 """

from 双向链表基本类 import _DoublyLinkedBase


class LinkedDeque(_DoublyLinkedBase):
    """ Double-ended queue implementation based on a doubly linked list """

    def first(self):
        """ Return (but do not remove) the element at the front of the deque. """
        if self.is_empty():
            raise Exception('Deque is empty')
        return self._header._next._element

    def last(self):
        """ Return (but do not remove) the element at the back of the deque. """
        if self.is_empty():
            raise Exception('Deque is empty')
        return self._trailer._prev._element

    def insert_first(self, e):
        """ Add an element to the back of the deque """
        self._insert_between(e, self._trailer._prev, self._trailer)

    def delete_first(self):
        """ Remove and return the element from the front of the deque. """
        if self.is_empty():
            raise Exception('Deque is empty')
        return self._delete_node(self._header._next)

    def delete_last(self):
        """ Remove and return the element from the back of the deque. """
        if self.is_empty():
            raise Exception('Deque is empty')
        return self._delete_node(self._trailer._prev)

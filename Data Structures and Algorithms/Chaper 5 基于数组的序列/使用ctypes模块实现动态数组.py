""" 使用从types模块提供的原始数组实现DynamicArray类 """

import ctypes


class DynamicArray:
    """ A dynamic array class akin to a simplified Python list. """

    def __init__(self):
        """ Create an empty array. """
        self._n = 0     # 元素个数
        self._capacity = 1  # 默认数据容量
        self._A = self._make_array(self._capacity)  # 低级数据

    def __len__(self):
        """ Retuen number of elements stored in the array. """
        return self._n

    def __getitem__(self, k):
        """ Return element at index k. """
        if not 0 <= k < self._n:
            raise IndexError('invalid index')
        return self._A[k]

    def append(self, obj):
        """ Add object to end of the array.
        返回下标为k的元素
         """
        if self._n == self._capacity:
            self._resize(2*self._capacity)
        self._A[self._n] = obj
        self._n += 1

    def _resize(self, c):
        """ Resize internal array to capacity c. 
        将内部数组的大小调整到容量c
        """
        B = self._make_array(c)
        for k in range(self._n):
            B[k] = self._A[k]
        self._A = B
        self._capacity = c

    def _make_array(self, c):
        """ Return new array with capacity c. 
            c: 数组容量
            返回一个容量为c的新数据
        """
        return (c * ctypes.py_object)()

"""
    栈
    1. 后进先出，
    2. 例：浏览器的历史记录存放方式，当用户访问一个新的网站后，这个新网站就会压入栈顶
    3. 例：文本编辑器的撤销操作
"""


class ArrayStack:
    """ LIFO Stack implemention using a Python list as underlying storage. """

    def __init__(self):
        """ Create an empty stack """
        self._data = []   # nonpublic list instance

    def __len__(self):
        """ Return the number of elements in the stack. """
        return len(self._data)

    def is_empty(self):
        """ Return True if the stack is empty. """
        return len(self._data) == 0

    def push(self, e):
        """ Add element e to the top of the stack. """
        self._data.append(e)

    def top(self):
        """ Return (but do not remove) the element at the top of the stack.
            Raise Empty exception if the stack is empty.
        """
        if self.is_empty():
            raise Exception('Stack is empty')
        return self._data[-1]

    def pop(self):
        """ Remove and return the element from the top of the stack(i.e.,LIFO). 
        Raise Empty exception if the stack is empty.
        """
        if self.is_empty():
            raise Exception('Stack is empty')
        return self._data.pop()

if __name__ == "__main__":
    s=ArrayStack()
    s.push(2)
    s.push(3)
    s.pop()
    s.pop()
    s.top()

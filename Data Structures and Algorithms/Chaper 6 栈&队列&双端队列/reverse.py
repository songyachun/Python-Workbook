""" 实现文件中各行的逆置 """
from stack import ArrayStack
import os

def reverse_file(filename):
    """ Overwrite given file with its contents line-by-line reversed. """
    S = ArrayStack()
    original = open(filename)
    for line in original:
        S.push(line.rstrip('\n'))  # we will re-insert newlines when writing
    original.close()

    # now we overwrite with contents in LIFO order
    output = open(filename, 'w')
    while not S.is_empty():
        output.write(S.pop()+'\n')
    output.close()

if __name__ == "__main__":
    filename='reversetest.txt'
    r1=reverse_file(filename)
    
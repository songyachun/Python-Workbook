""" 在算数表达式中分隔符匹配算法 """
from stack import ArrayStack


def is_matched(expr):
    """ Return True if all delimiters are properly match;False otherwise. """
    lefty = '({['
    righty = ')}]'
    S = ArrayStack()
    for c in expr:
        if c in lefty:
            S.push(c)
        elif c in righty:
            if S.is_empty():
                return False
            if righty.index(c) != lefty.index(S.pop()):
                return False
    return S.is_empty()


if __name__ == "__main__":
    a = is_matched('()(()){([()])}')
    print(a)

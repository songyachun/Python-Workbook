

""" 
5!=5*(4*3*2*1)=5*4!
我们可以定义n!=n*(n-1)!
"""
from pysnooper import snoop
@snoop()
def factorial(n):
    if n == 1:
        return n

    else:
        return n * factorial(n-1)


if __name__ == "__main__":
    factorial(6)

__author__ = 'nikhil'

from functools import partial

def mul(x,y):
    return x*y

def fun(num):
    double = partial(mul,2)
    return double(num)

print fun(7)
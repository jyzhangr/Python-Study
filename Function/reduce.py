#Python提供的sum()函数可以接受一个list并求和，请编写一个prod()函数，可以接受一个list并利用reduce()求积：
# -*- coding: utf-8 -*-
from functools import reduce
def fn(x,y):
    return x*y

def prod(L):
    return reduce(fn,L)

L1=[3,5,7,9]
L2=prod(L1)
print(L2)

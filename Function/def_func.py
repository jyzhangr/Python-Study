#   请定义一个函数quadratic(a, b, c)，接收3个参数，返回一元二次方程：
#   ax2 + bx + c = 0
#   的两个解。
# -*- coding: utf-8 -*-
import math
a=float(input('Enter the value of a: '))
b=float(input('Enter the value of b: '))
c=float(input('Enter the value of c: '))
def quadratic(a,b,c):
    delta=b*b-4*a*c
    if(delta<0):
    	  print('Real Solutions Do Not Exist!')
    else:
    	x1=(-b+math.sqrt(delta))/(2*a)
    	x2=(-b-math.sqrt(delta))/(2*a)
    return x1, x2
x1,x2=quadratic(a,b,c)
print(str(x1),str(x2))

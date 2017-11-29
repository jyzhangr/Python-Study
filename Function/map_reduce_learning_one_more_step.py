# -*- coding: utf-8 -*-
from functools import reduce
def char2num(s):
    return{'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}[s]

def char2num2(ss):
    return {'0':0,'1':11,'2':22,'3':33,'4':44,'5':55,'6':66,'7':77,'8':88,'9':99}[ss]

strr='123.456'
dot_pos = strr.find('.')          #得到字符串中‘.’的位置
re_int = strr[0:dot_pos]      #截取字符串小数点左面的整数部分
re_dot = strr[dot_pos+1:]     #截取字符串小数点右面的整数部分
re = re_int + re_dot
#去掉小数点的整数字符串转为int类型
result = list(map(char2num,re))
results=list(map(char2num2,re_int + re_dot))

print('hello')
print(re)
print(result)
print(results)
#{'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
#这个东西是dict，[s]是key。
#map()将char2num(s)依次作用于字符串'123456'里的每个元素，能理解吧，反过来说就是依次让'1''2''3'...当作key去索引dict得到value，即依次得到123456

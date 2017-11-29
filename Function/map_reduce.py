#利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456：
# -*- coding: utf-8 -*-
from functools import reduce

def str2num(x,y):
    return x*10+y

def char2num(s):
    return{'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}[s]

def str2float(num):
    dot_pos = num.find('.')          #得到字符串中‘.’的位置
    re_int = num[0:dot_pos]      #截取字符串小数点左面的整数部分
    re_dot = num[dot_pos+1:]     #截取字符串小数点右面的整数部分
    #去掉小数点的整数字符串转为int类型
    result = reduce(str2num,list(map(char2num,re_int + re_dot)))
    #根据小数点位置还原数值
    result = result / (10**dot_pos)
    return result
#print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')

# 题目：小明的成绩从去年的72分提升到了今年的85分，请计算小明成绩提升的百分点，并用字符串格式化显示出'xx.xx%'，只保留小数点后2位：

# -*- coding: utf-8 -*-
s1=72
s2=85
r=(s2-s1)/s1*100
print('growth rate: %.2f %%' %r)

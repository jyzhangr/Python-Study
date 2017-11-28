#首字母大写

# -*- coding: utf-8 -*-
def normalize(name):
    return name.upper()[0:1] + name.lower()[1:]
L1=['adam','LISA','barT']
L2=list(map(normalize,L1))
print(L2)

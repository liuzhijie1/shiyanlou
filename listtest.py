#!/usr/bin/env python3
#!-*-coding:utf-8 -*-

import sys
a=[]
b=[]
for arg in sys.argv[1:]:
    if(len(arg)<=3):
        a.append(arg)
    else:
        b.append(arg)
qq=bb=''
for i in range(len(a)):
    if(i != len(a)-1):
        qq+=(a[i]+' ')
    else:
        qq+=a[i]

for j in range(len(b)):
    if(j!=len(b)-1):
        bb+=(b[j]+' ')
    else:
        bb+=b[j]
print(qq)
print(bb)
